"""Source documents: content.csv, download + local cache, text extraction and the
verbatim-overlap checker.

content.csv (no header needed):   url, licence, attribution
    licence = attribution  -> may be adapted/quoted freely; must be credited (attribution text shown)
    licence = quotes       -> short verbatim quotes only (<= style.QUOTE_MAX_WORDS), always cited
    licence = copyrighted  -> reference only: NO verbatim text, no copied figures, no copied questions
Searched in sources/<COURSE>/content.csv, then sources/content.csv.

Each URL gets a short NAME = the last part of the URL path (URL-decoded); paths with no
extension get '.html' (e.g. .../phy415115-9/ -> 'phy415115-9.html').  Specs cite sources by
NAME (or by the full URL).  `python -m explainer sources <spec>` downloads everything and
lists names, licences and cache paths.

Downloads are cached in sources/<COURSE>/cache/<NAME> with metadata in cache/index.json and
are never re-downloaded unless you pass --refresh.  If a download is blocked, put the file
at that cache path by hand; it is then used as if downloaded.
"""
import csv
import datetime
import hashlib
import html
import json
import os
import re
import subprocess
import urllib.parse
import urllib.request
from html.parser import HTMLParser

from . import style as S

LICENCES = ('attribution', 'quotes', 'copyrighted')
USER_AGENT = 'Mozilla/5.0 (compatible; tasc-explainers/1.0)'


def sources_dir(root, course):
    return os.path.join(root, 'sources', course)


def cache_dir(root, course):
    return os.path.join(sources_dir(root, course), 'cache')


def find_csv(root, course):
    for p in (os.path.join(root, 'sources', course, 'content.csv'), os.path.join(root, 'sources', 'content.csv')):
        if os.path.exists(p):
            return p
    return None


def name_for(url):
    """Short, stable file name for a URL."""
    path = urllib.parse.urlparse(url).path.rstrip('/')
    base = urllib.parse.unquote(os.path.basename(path)) or urllib.parse.urlparse(url).netloc
    base = re.sub(r'[^\w.\- ]+', '_', base)
    if not os.path.splitext(base)[1]:
        base += '.html'
    return base


def load_content(path):
    """-> {name: dict(url, licence, attribution)}  (name collisions get a short hash suffix)"""
    out = {}
    with open(path, newline='', encoding='utf-8-sig') as f:
        for row in csv.reader(f):
            if not row or not row[0].strip() or row[0].strip().startswith('#'):
                continue
            url = row[0].strip()
            lic = row[1].strip().lower() if len(row) > 1 else ''
            if url.lower() in ('url', 'link') and lic in ('licence', 'license'):
                continue
            name = name_for(url)
            if name in out and out[name]['url'] != url:
                stem, ext = os.path.splitext(name)
                name = f'{stem}-{hashlib.sha1(url.encode()).hexdigest()[:6]}{ext}'
            out[name] = dict(url=url, licence=lic, attribution=row[2].strip() if len(row) > 2 else '')
    return out


def fetch(url, dest, refresh=False, timeout=60):
    """Download url -> dest (atomic).  Returns (path or None, error message or None)."""
    if os.path.exists(dest) and os.path.getsize(dest) > 0 and not refresh:
        return dest, None
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read(); ctype = r.headers.get('Content-Type', '')
    except Exception as ex:  # noqa: network errors of every kind
        return (dest if os.path.exists(dest) else None), f'{type(ex).__name__}: {ex}'
    tmp = dest + '.part'
    with open(tmp, 'wb') as f:
        f.write(data)
    os.replace(tmp, dest)
    idx_path = os.path.join(os.path.dirname(dest), 'index.json')
    idx = json.load(open(idx_path)) if os.path.exists(idx_path) else {}
    idx[os.path.basename(dest)] = dict(url=url, content_type=ctype, bytes=len(data),
                                       sha256=hashlib.sha256(data).hexdigest(),
                                       fetched=datetime.datetime.now().isoformat(timespec='seconds'))
    json.dump(idx, open(idx_path, 'w'), indent=1)
    return dest, None


class _HTMLText(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0

    def handle_starttag(self, tag, a):
        if tag in ('script', 'style', 'noscript'): self.skip += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript') and self.skip: self.skip -= 1

    def handle_data(self, d):
        if not self.skip: self.parts.append(d)


def extract_text(path):
    """Plain text of a source (html, pdf, txt, md).  PDFs: pypdf, falling back to pdftotext."""
    ext = os.path.splitext(path)[1].lower()
    with open(path, 'rb') as f:
        if f.read(5) == b'%PDF-':
            ext = '.pdf'
    if ext in ('.html', '.htm'):
        p = _HTMLText(); p.feed(open(path, encoding='utf-8', errors='ignore').read())
        return html.unescape(' '.join(p.parts))
    if ext == '.pdf':
        try:
            from pypdf import PdfReader
            return '\n'.join((pg.extract_text() or '') for pg in PdfReader(path).pages)
        except Exception:
            try:
                return subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True).stdout
            except FileNotFoundError:
                return ''
    return open(path, encoding='utf-8', errors='ignore').read()


def extract_pages(path):
    """List of page texts for a PDF (1-based page n = list[n-1]).  Handy for finding page refs."""
    from pypdf import PdfReader
    return [(pg.extract_text() or '') for pg in PdfReader(path).pages]


_MATH = re.compile(r'\\[a-zA-Z]+|[{}$^_]')


def tokens(s):
    s = _MATH.sub(' ', s)
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", s.lower())


def ngram_set(toks, n):
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def runs(target, src_ngrams, n):
    """Maximal verbatim runs (start, length_in_words) of target tokens found in the source."""
    hits = [tuple(target[i:i + n]) in src_ngrams for i in range(len(target) - n + 1)]
    out, i = [], 0
    while i < len(hits):
        if hits[i]:
            j = i
            while j + 1 < len(hits) and hits[j + 1]:
                j += 1
            out.append((i, j - i + n)); i = j + 1
        else:
            i += 1
    return out


class Corpus:
    """All sources for one course: content.csv rows, downloaded into the local cache."""

    def __init__(self, root, course, download=True, refresh=False, quiet=False):
        self.root, self.course = root, course
        self.csv_path = find_csv(root, course)
        rows = load_content(self.csv_path) if self.csv_path else {}
        self.table = {n: (r['licence'], r['attribution']) for n, r in rows.items()}
        self.urls = {n: r['url'] for n, r in rows.items()}
        self.paths, self.errors = {}, {}
        cd = cache_dir(root, course)
        for n, url in self.urls.items():
            dest = os.path.join(cd, n)
            if download:
                p, err = fetch(url, dest, refresh)
            else:
                p, err = (dest if os.path.exists(dest) else None), None
            self.paths[n] = p
            if err:
                self.errors[n] = err
                if not quiet:
                    print(f'download failed for {url}\n  {err}\n  -> put the file at {dest} manually' +
                          (' (using the existing cached copy)' if p else ''))
        self._ng = {}

    def key(self, file_or_url):
        """Source NAME for a Ref.file given as a NAME or a URL (None if unknown)."""
        if file_or_url in self.table:
            return file_or_url
        for n, u in self.urls.items():
            if u == file_or_url:
                return n
        return None

    def ngrams(self, name):
        if name not in self._ng:
            p = self.paths.get(name)
            self._ng[name] = ngram_set(tokens(extract_text(p)), S.NGRAM) if p else set()
        return self._ng[name]

    def check_text(self, where, text, cited_files, allowed):
        """Yield (level, message) for verbatim runs of `text` found in any source."""
        toks = tokens(text)
        allowed_toks = [tokens(a) for a in allowed]
        for name, (lic, _) in self.table.items():
            ng = self.ngrams(name)
            if not ng:
                continue
            for st, ln in runs(toks, ng, S.NGRAM):
                frag = toks[st:st + ln]
                if any(' '.join(a) in ' '.join(frag) or ' '.join(frag) in ' '.join(a) for a in allowed_toks if a):
                    continue
                snippet = ' '.join(frag)
                if lic == 'copyrighted':
                    yield 'ERROR', f'{where}: {ln}-word verbatim run from COPYRIGHTED "{name}": "{snippet}"'
                elif lic == 'quotes':
                    if ln > S.QUOTE_MAX_WORDS:
                        yield 'ERROR', f'{where}: {ln}-word quote from "{name}" exceeds {S.QUOTE_MAX_WORDS} words: "{snippet}"'
                    elif name not in cited_files:
                        yield 'ERROR', f'{where}: quote from "{name}" but the step does not cite it: "{snippet}"'
                else:
                    if name not in cited_files:
                        yield 'WARN', f'{where}: verbatim text from "{name}" without citing it: "{snippet}"'
