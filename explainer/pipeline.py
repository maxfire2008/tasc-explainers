"""check -> preview -> tts -> render.  See CLAUDE.md for the workflow."""
import hashlib
import inspect
import json
import math
import os
import re
import shutil
import subprocess
import sys
import warnings
from functools import lru_cache

import numpy as np

from . import builtin, layout as L, sources as SRC, style as S, subtitles, tts
from .spec import load

warnings.filterwarnings('ignore')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FPS = S.VIDEO['fps']

# ffmpeg program and video encoder for `render`. Set them here, or per machine with the environment variables.
# Use FFMPEG='ffmpeg.exe' in WSL to run the Windows ffmpeg, which can reach the GPU; paths are converted with wslpath.
FFMPEG = os.environ.get('EXPLAINER_FFMPEG', 'ffmpeg')
ENCODER = os.environ.get('EXPLAINER_ENCODER', 'libx264')
_CRF = str(S.VIDEO['crf'])
ENCODERS = {  # name -> ffmpeg options for about the same quality; the hardware ones give larger files
    'libx264': ['-preset', S.VIDEO['preset'], '-crf', _CRF],
    'libx265': ['-preset', S.VIDEO['preset'], '-crf', _CRF, '-tag:v', 'hvc1'],
    'h264_nvenc': ['-preset', 'p5', '-rc', 'vbr', '-cq', _CRF, '-b:v', '0'],
    'hevc_nvenc': ['-preset', 'p5', '-rc', 'vbr', '-cq', _CRF, '-b:v', '0', '-tag:v', 'hvc1'],
    'h264_qsv': ['-preset', 'veryfast', '-global_quality', _CRF],
    'hevc_qsv': ['-preset', 'veryfast', '-global_quality', _CRF, '-tag:v', 'hvc1'],
    'h264_amf': ['-quality', 'quality', '-rc', 'cqp', '-qp_i', _CRF, '-qp_p', _CRF],
    'hevc_amf': ['-quality', 'quality', '-rc', 'cqp', '-qp_i', _CRF, '-qp_p', _CRF, '-tag:v', 'hvc1'],
}
NUMWORDS = {w: i for i, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve'.split())}


def out_dir(v, *p):
    d = os.path.join(ROOT, 'out', v.id, *p)
    os.makedirs(d if not os.path.splitext(d)[1] else os.path.dirname(d), exist_ok=True)
    return d


# ----------------------------------------------------------------------------- ffmpeg
def _codec_args():
    if ENCODER not in ENCODERS:
        raise SystemExit(f'unknown encoder {ENCODER!r}: use one of {", ".join(ENCODERS)}')
    return ['-c:v', ENCODER] + ENCODERS[ENCODER]


@lru_cache(maxsize=None)
def _wsl_dir(d):
    return subprocess.run(['wslpath', '-m', d], check=True, capture_output=True, text=True).stdout.strip()


def _ff_path(p):
    """A path as FFMPEG needs it: ffmpeg.exe under WSL takes Windows paths. p's folder must exist, its file need not."""
    if not FFMPEG.lower().endswith('.exe') or not shutil.which('wslpath'):
        return p
    d, name = os.path.split(p)
    return _wsl_dir(d) + '/' + name


def _filter_path(p):
    """A path as a filter option, where the colon in C:/... would otherwise end the value."""
    return "'" + _ff_path(p).replace(':', r'\:') + "'"


# ----------------------------------------------------------------------------- drawing
def setup(v):
    L.use(S.theme(v.course, v.module))
    L.ctx['course_label'] = v.course_label
    L.ctx['sheet_section'] = v.info_sheet.section if v.info_sheet else ''


def draw(v, sc, i, ph, ref_numbers=None):
    """Draw one frame -> (rgb, texts, sheet_used)."""
    L.ctx['part'] = sc.part
    L.ctx['sheet_used'] = False
    fig = L.new_fig()
    sc.draw(fig, i, ph)
    used = L.ctx['sheet_used']
    if ref_numbers is not None:
        L.footer(fig, ref_numbers)
    else:
        L.footer(fig)
    rgb = L.to_rgb(fig)
    txt = L.texts(fig)
    import matplotlib.pyplot as plt
    plt.close(fig)
    return rgb, txt, used


def analyse(v):
    """Draw every step once; record on-screen text and info-sheet use; number references."""
    if getattr(v, '_an', None):
        return v._an
    setup(v)
    an = {}
    for sc, i, st in v.all_steps():
        _, txt, used = draw(v, sc, i, 0.0)
        refs = list(st.refs)
        if used and v.info_sheet and v.info_sheet.ref not in refs:
            refs.append(v.info_sheet.ref)
        an[(sc.id, i)] = dict(texts=txt, sheet=used, refs=refs)
    order = []
    for sc, i, st in v.all_steps():
        for r in an[(sc.id, i)]['refs']:
            if r not in order:
                order.append(r)
    for coll in (v.syllabus, v.elements, v.exam_topics):
        for val in coll.values():
            if val[1] not in order:
                order.append(val[1])
    for r in v.refs:
        if r not in order:
            order.append(r)
    v._refnum = {r: n + 1 for n, r in enumerate(order)}
    v._an = an
    return an


def ref_numbers(v, sc, i):
    return sorted({v._refnum[r] for r in v._an[(sc.id, i)]['refs'] if r in v._refnum})


# ----------------------------------------------------------------------------- check
def check(v, allow_missing_sources=False, copyright_scan=True):
    errs, warns = [], []
    E, W = errs.append, warns.append
    corpus = SRC.Corpus(ROOT, v.course)
    if not corpus.csv_path:
        (W if allow_missing_sources else E)(f'no content.csv in sources/{v.course}/ or sources/')
    an = analyse(v)

    ids = [sc.id for sc in v.scenes]
    for d in {x for x in ids if ids.count(x) > 1}:
        E(f'duplicate scene id {d}')
    missing = set()
    for k, r in v.refs.items():
        name = corpus.key(r.file)
        if corpus.table and not name:
            E(f'ref {k}: "{r.file}" is not in content.csv (use the source NAME from `python -m explainer sources` or its URL)')
        elif corpus.table and corpus.table[name][0] not in SRC.LICENCES:
            E(f'ref {k}: unknown licence "{corpus.table[name][0]}" for {name}')
        if name and not corpus.paths.get(name) and name not in missing:
            missing.add(name)
            (W if allow_missing_sources else E)(
                f'source "{name}" (ref {k} and others) could not be downloaded from {corpus.urls[name]}: '
                f'{corpus.errors.get(name, "")}. Put the file at {os.path.join(SRC.cache_dir(ROOT, v.course), name)}')
        if r.file.lower().endswith('.pdf') and r.page in (None, ''):
            W(f'ref {k}: no page number for PDF "{r.file}" ({r.loc})')
    for name in corpus.table:
        if not any(corpus.key(r.file) == name for r in v.refs.values()):
            W(f'source "{name}" is in content.csv but never referenced: did you read and use it?')
        if 'exam' in name.lower() and 'report' not in name.lower() and not any(
                corpus.key(v.refs[t[1]].file) == name for t in v.exam_topics.values() if t[1] in v.refs):
            W(f'exam "{name}" has no exam_topics entry: list what it examined for this module')

    for coll, nm in ((v.syllabus, 'syllabus'), (v.elements, 'elements'), (v.exam_topics, 'exam_topics')):
        for k, val in coll.items():
            if val[1] not in v.refs:
                E(f'{nm}[{k}] cites unknown ref "{val[1]}"')
    cov = {'syllabus': set(), 'elements': set(), 'exam': set()}
    if v.info_sheet and v.info_sheet.ref not in v.refs:
        E(f'info_sheet.ref "{v.info_sheet.ref}" not in refs')
    for sc, i, st in v.all_steps():
        where = f'{sc.id}[{i}]'
        for r in st.refs:
            if r not in v.refs: E(f'{where}: unknown ref "{r}"')
        for c in st.covers:
            (cov['syllabus'].add(c) if c in v.syllabus else E(f'{where}: unknown syllabus key "{c}"'))
        for e in st.elements:
            (cov['elements'].add(e) if e in v.elements else E(f'{where}: unknown element {e}'))
        for x in st.exam:
            (cov['exam'].add(x) if x in v.exam_topics else E(f'{where}: unknown exam topic "{x}"'))
        low = st.text.lower()
        for m in re.finditer(r'\belements? (\w+)', low):
            n = NUMWORDS.get(m.group(1), int(m.group(1)) if m.group(1).isdigit() else None)
            if n is not None and n not in v.elements:
                E(f'{where}: narration mentions element {n}, which does not exist')
        info = an[(sc.id, i)]
        first_show = info['sheet'] and not (i > 0 and an[(sc.id, i - 1)]['sheet'])
        if first_show and 'information sheet' not in low:
            E(f'{where}: an information-sheet formula appears here but the narration never says "information sheet"')
        if info['sheet'] and not v.info_sheet:
            E(f'{where}: sheet_eq used but Video.info_sheet is not set')
        bad = sorted(set(re.findall(r'[λθμωπ=×÷/^√≈°≪≫→∝±∴<>%]', st.text)))
        if bad:
            W(f'{where}: narration contains symbols {"".join(bad)}; write them as spoken words')
        if st.anim and abs(st.anim * FPS - round(st.anim * FPS)) > 1e-6:
            W(f'{where}: anim period {st.anim}s is not a whole number of frames')
        if '\n' in st.problem:
            E(f'{where}: Step.problem must be a single line')
        if copyright_scan and corpus.table:
            cited = {corpus.key(v.refs[r].file) for r in info['refs'] if r in v.refs}
            for lvl, msg in corpus.check_text(where + ' narration', st.text, cited, v.allowed_overlaps):
                (E if lvl == 'ERROR' else W)(msg)
            for lvl, msg in corpus.check_text(where + ' problem', st.problem, cited, v.allowed_overlaps):
                (E if lvl == 'ERROR' else W)(msg)
            for lvl, msg in corpus.check_text(where + ' on-screen', '\n'.join(info['texts']), cited,
                                              v.allowed_overlaps):
                (E if lvl == 'ERROR' else W)(msg)
    if not any(st.problem for _, _, st in v.all_steps()):
        W('no Step.problem set: tag the step where each problem explanation starts')
    if not v.thumbnail:
        W('Video.thumbnail is not set: add a thumbnail based on the title card')
    for k in v.syllabus:
        if k not in cov['syllabus']: E(f'syllabus point {k} is not covered: "{v.syllabus[k][0]}"')
    for k in v.elements:
        if k not in cov['elements']: E(f'element {k} is never exercised: "{v.elements[k][0]}"')
    for k in v.exam_topics:
        if k not in cov['exam']: E(f'exam topic {k} is not covered: "{v.exam_topics[k][0]}"')
    for label_, fn, expect, tol in v.checks:
        try:
            got = fn()
            if abs(got - expect) > tol * max(abs(expect), 1e-12):
                E(f'numeric check "{label_}": got {got:.6g}, spoken/shown {expect}')
        except Exception as ex:  # noqa
            E(f'numeric check "{label_}" raised {ex!r}')

    words = {}
    for sc, i, st in v.all_steps():
        words[sc.part or sc.topic] = words.get(sc.part or sc.topic, 0) + len(st.text.split())
    print('Estimated narration time by part (at ~155 words/min):')
    for p, w in words.items():
        print(f'  {w / 155:5.1f} min  {p}')
    print(f'  {sum(words.values()) / 155:5.1f} min  TOTAL')
    for w in warns: print('WARN ', w)
    for e in errs: print('ERROR', e)
    print(f'{len(errs)} error(s), {len(warns)} warning(s)')
    return errs, warns


# ----------------------------------------------------------------------------- preview
def preview(v, only=None):
    """One frame per step (animated steps at phase 0.3) + 3x3 contact sheets."""
    from PIL import Image, ImageDraw
    analyse(v); setup(v)
    v.credit_lines = credit_lines(v)
    d = out_dir(v, 'preview')
    names = []
    for n, (sc, i, st) in enumerate(v.all_steps()):
        if only and sc.id not in only:
            continue
        rgb, _, _ = draw(v, sc, i, 0.3 if st.anim else 0.0, ref_numbers(v, sc, i))
        nm = f'{n:03d}_{sc.id}_{i}.jpg'
        Image.fromarray(rgb).save(os.path.join(d, nm), quality=88)
        names.append(nm)
    for k in range(0, len(names), 9):
        sheet = Image.new('RGB', (1920, 1080), 'white'); dr = ImageDraw.Draw(sheet)
        for j, nm in enumerate(names[k:k + 9]):
            im = Image.open(os.path.join(d, nm)).resize((636, 358))
            x, y = (j % 3) * 642, (j // 3) * 361
            sheet.paste(im, (x, y)); dr.text((x + 5, y + 340), nm, fill='yellow')
        sheet.save(os.path.join(d, f'_sheet{k // 9:02d}.jpg'), quality=88)
    print(f'{len(names)} frames + contact sheets in {d}')


# ----------------------------------------------------------------------------- thumbnail
def make_thumbnail(v):
    """Draw Video.thumbnail on the slide canvas and save <id>_thumbnail.png at YouTube's size."""
    if not v.thumbnail:
        print('no thumbnail: Video.thumbnail is not set')
        return None
    from PIL import Image
    import matplotlib.pyplot as plt
    setup(v)
    fig = L.new_fig()
    v.thumbnail(fig)
    L.ai_badge(fig)
    rgb = L.to_rgb(fig)
    plt.close(fig)
    size = (S.THUMBNAIL['width'], S.THUMBNAIL['height'])
    path = os.path.join(out_dir(v), f'{v.id}_thumbnail.png')
    Image.fromarray(rgb).resize(size, Image.LANCZOS).save(path, optimize=True)
    n = os.path.getsize(path)
    if n > S.THUMBNAIL['max_bytes']:
        print(f'WARNING: thumbnail is {n // 1024} KB, over the limit of {S.THUMBNAIL["max_bytes"] // 1024} KB')
    print(f'thumbnail: {path} ({n // 1024} KB)')
    return path


# ----------------------------------------------------------------------------- tts + timeline
def make_tts(v):
    d = out_dir(v, 'audio')
    for sc, i, st in v.all_steps():
        p = tts.synth(st.text, d, ROOT)
        print('tts', sc.id, i, os.path.basename(p), flush=True)


def timeline(v):
    import soundfile as sf
    d = out_dir(v, 'audio')
    tl, t = [], 0.0
    steps = list(v.all_steps())
    for n, (sc, i, st) in enumerate(steps):
        p = os.path.join(d, tts.key(st.text) + '.wav')
        if not os.path.exists(p):
            raise SystemExit(f'missing narration audio for {sc.id}[{i}]: run the tts command first')
        ad = sf.info(p).duration
        lead = S.LEAD_FIRST if i == 0 else S.LEAD
        tail = S.TAIL_LAST if n == len(steps) - 1 else S.TAIL
        nfr = math.ceil(max(lead + ad + tail, st.min_dur) * FPS)
        tl.append(dict(scene=sc, i=i, step=st, wav=p, lead=lead, nfr=nfr, start=t, dur=nfr / FPS,
                       audio_start=t + lead, audio_dur=ad, text=st.text))
        t += nfr / FPS
    return tl


def fmt_time(t):
    t = int(t); h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f'{h}:{m:02d}:{s:02d}' if h else f'{m}:{s:02d}'


# ----------------------------------------------------------------------------- documents
def chapters(v, tl):
    ch = []
    for it in tl:
        sc = it['scene']
        if ch and ch[-1]['topic'] == sc.topic:
            ch[-1]['end'] = it['start'] + it['dur']; continue
        ch.append(dict(topic=sc.topic, part=sc.part, start=it['start'], end=it['start'] + it['dur']))
    merged = []
    for c in ch:
        if merged and c['end'] - c['start'] < S.MIN_CHAPTER:
            merged[-1]['end'] = c['end']; merged[-1]['topic'] += ' & ' + c['topic']
        else:
            merged.append(c)
    return merged


def write_docs(v, tl):
    od = out_dir(v)
    corpus = SRC.Corpus(ROOT, v.course, download=False)
    # timestamps
    lines = []
    for c in chapters(v, tl):
        ps = c['part'].split('·')[0].strip() if c['part'] else ''
        if ps:
            line = S.TIMESTAMP_FORMAT.format(time=fmt_time(c['start']), part=c['part'], part_short=ps, topic=c['topic'])
        else:
            line = f"{fmt_time(c['start'])} {c['topic']}"
        lines.append(line)
    open(os.path.join(od, 'timestamps.txt'), 'w').write('\n'.join(lines) + '\n')
    # references
    used_at = {}
    for it in tl:
        for r in v._an[(it['scene'].id, it['i'])]['refs']:
            used_at.setdefault(r, []).append(fmt_time(it['start']))
    inv = sorted(v._refnum.items(), key=lambda kv: kv[1])
    ref_md = [f'# References: {v.title}', '', f'{v.course} {v.course_name} · {v.module_name}', '',
              'Numbers match the "Refs [n]" badges in the slide footers.', '']
    ref_txt = []
    for key_, n in inv:
        r = v.refs[key_]
        name = corpus.key(r.file) or r.file
        lic, att = corpus.table.get(name, ('?', ''))
        url = corpus.urls.get(name, r.file if r.file.startswith('http') else '')
        if not att:
            att = f'{S.COPYRIGHT_HOLDER}. {name}' + (' (all rights reserved; referenced, not reproduced)'
                                                    if lic == 'copyrighted' else '')
        page = f', p. {r.page}' if r.page not in (None, '') else ''
        at = ', '.join(sorted(set(used_at.get(key_, [])), key=lambda s: [int(x) for x in s.split(':')]))
        ref_md.append(f'[{n}] {att} {r.loc}{page}.' + (f' <{url}>' if url else '') + f' Licence: {lic}.'
                      + (f' Shown at {at}.' if at else '') + (f' {r.note}' if r.note else ''))
        ref_md.append('')
        ref_txt.append(f'[{n}] {r.loc}{page}: {url or name}')
    open(os.path.join(od, 'references.md'), 'w').write('\n'.join(ref_md))
    # coverage
    cov = ['# Coverage map', '']
    for title, coll, attr in (('Syllabus content', v.syllabus, 'covers'), ('Criterion elements', v.elements, 'elements'),
                              ('Past exam topics', v.exam_topics, 'exam')):
        cov += [f'## {title}', '', '| key | item | covered at |', '|---|---|---|']
        for k, (txt, _) in coll.items():
            at = sorted({fmt_time(it['start']) for it in tl if k in getattr(it['step'], attr)},
                        key=lambda s: [int(x) for x in s.split(':')])
            cov.append(f'| {k} | {txt} | {", ".join(at) or "**NOT COVERED**"} |')
        cov.append('')
    open(os.path.join(od, 'coverage.md'), 'w').write('\n'.join(cov))
    # transcript
    tr = [f'# Transcript: {v.title}', '']
    for it in tl:
        tr.append(f'**{fmt_time(it["start"])}** ({it["scene"].id}[{it["i"]}]) {it["text"]}\n')
    open(os.path.join(od, 'transcript.md'), 'w').write('\n'.join(tr))
    # problems: one "time question" per line, to help learners find each explanation
    problems = [f"{fmt_time(it['start'])} {it['step'].problem.strip()}" for it in tl if it['step'].problem.strip()]
    open(os.path.join(od, 'problems.txt'), 'w').write('\n'.join(problems) + '\n')
    # description
    desc = [v.description.strip(), '', 'AI generated content: may contain errors.', '', S.UPDATES_NOTE, '', 'Chapters', *lines, '',
            *(['Problems solved in this video', *problems, ''] if problems else []),
            'References (numbers match the slide footers)', *ref_txt]
    open(os.path.join(od, 'description.txt'), 'w').write('\n'.join(desc).strip() + '\n')
    # subtitles
    subtitles.write_all([dict(audio_start=it['audio_start'], audio_dur=it['audio_dur'], text=it['text']) for it in tl],
                        os.path.join(od, v.id), S.theme(v.course, v.module), v.keywords)
    print('wrote timestamps.txt, problems.txt, references.md, coverage.md, transcript.md, description.txt, subtitles in', od)


def credit_lines(v):
    corpus = SRC.Corpus(ROOT, v.course, download=False)
    files = []
    for key_ in sorted(v._refnum, key=v._refnum.get):
        f = corpus.key(v.refs[key_].file) or v.refs[key_].file
        if f not in files:
            files.append(f)
    att = [corpus.table[f][1] for f in files if f in corpus.table and corpus.table[f][0] == 'attribution'
           and corpus.table[f][1]]
    other = [f for f in files if corpus.table.get(f, ('',))[0] in ('quotes', 'copyrighted')]
    import textwrap
    lines = [('Course content adapted from (used under a ' + S.ATTRIBUTION_LICENCE + '):', L.SOFT, 22)]
    lines += [(textwrap.fill(a, 95), L.FG, 22) for a in dict.fromkeys(att)] or [('(see references.md)', L.FG, 22)]
    if other:
        lines += [('Referenced, not reproduced:', L.SOFT, 22), (textwrap.fill(' · '.join(other), 120), L.FG, 19)]
    lines += [('', L.FG, 8), ('Example questions are original. Full numbered references and updated versions: see the description.',
                              L.SOFT, 20),
              (f'Narration: synthetic voice (Kokoro, {S.VOICE["voice"]}) · Visuals: Python / Matplotlib · '
               + S.FOOTER_AI, L.SOFT, 18)]
    return lines


# ----------------------------------------------------------------------------- render
def _clip_key(v, sc, it, offset, N):
    try:
        src = inspect.getsource(sc.draw)
    except (OSError, TypeError):
        src = repr(sc.draw)
    blob = json.dumps([src, it['i'], it['nfr'], it['step'].anim, offset % N if N else 0,
                       str(S.theme(v.course, v.module)), ref_numbers(v, sc, it['i']), v.course_label,
                       repr(getattr(v, 'credit_lines', '')) if sc.id == builtin.CREDITS_ID else '',
                       open(S.__file__).read(), open(L.__file__).read()]
                      # clips are joined with -c copy, so they must not mix encoders; libx264 keeps existing caches valid
                      + ([] if ENCODER == 'libx264' else [_codec_args()]))
    return hashlib.sha1(blob.encode()).hexdigest()[:16]


def render(v, force=False, burn_subs=False):
    """Narration (cached), video, then every timed document, including problems.txt, and the thumbnail."""
    import soundfile as sf
    from PIL import Image
    make_tts(v)
    make_thumbnail(v)
    L.ctx['scale'] = S.VIDEO['render_scale']
    analyse(v); setup(v)
    v.credit_lines = credit_lines(v)
    tl = timeline(v)
    cd = out_dir(v, 'clips')
    codec = _codec_args()
    enc = codec + ['-pix_fmt', 'yuv420p', '-r', str(FPS), '-g', str(S.VIDEO['gop']), '-video_track_timescale', '15360']
    W, H = S.VIDEO['width'] * L.ctx['scale'], S.VIDEO['height'] * L.ctx['scale']
    counter, prev_scene, clips = 0, None, []
    for n, it in enumerate(tl):
        sc, i, st = it['scene'], it['i'], it['step']
        if sc.id != prev_scene:
            counter, prev_scene = 0, sc.id
        N = int(round(st.anim * FPS)) if st.anim else 0
        name = os.path.join(cd, _clip_key(v, sc, it, counter, N) + '.mp4')
        clips.append(name)
        if os.path.exists(name) and not force:
            counter += it['nfr']; continue
        tmp = name[:-4] + '.tmp.mp4'
        refs = ref_numbers(v, sc, i)
        if not N:
            png = os.path.join(cd, '_still.png')
            Image.fromarray(draw(v, sc, i, 0.0, refs)[0]).save(png)
            r = subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', _ff_path(png), '-vf',
                                f'format=yuv420p,loop=-1:1,trim=end_frame={it["nfr"]}'] + enc + [_ff_path(tmp)])
            rc = r.returncode
        else:
            frames = [draw(v, sc, i, j / N, refs)[0] for j in range(N)]
            p = subprocess.Popen([FFMPEG, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s',
                                  f'{W}x{H}', '-r', str(FPS), '-i', '-'] + enc + [_ff_path(tmp)], stdin=subprocess.PIPE)
            for f in range(it['nfr']):
                p.stdin.write(frames[(counter + f) % N].tobytes())
            p.stdin.close(); rc = p.wait()
        if rc != 0:
            raise SystemExit(f'ffmpeg failed on {sc.id}[{i}]')
        os.replace(tmp, name)
        counter += it['nfr']
        print(f'{n + 1}/{len(tl)} {sc.id}[{i}] {it["dur"]:.1f}s {"anim" if N else "still"}', flush=True)
    # narration track
    sr = sf.info(tl[0]['wav']).samplerate
    parts = []
    for it in tl:
        a, r_ = sf.read(it['wav'], dtype='float32')
        assert r_ == sr, 'all narration must share one sample rate'
        if a.ndim > 1: a = a.mean(1)
        seg = np.zeros(round(it['nfr'] / FPS * sr), dtype=np.float32)
        st0 = round(it['lead'] * sr); k = min(len(a), len(seg) - st0)
        seg[st0:st0 + k] = a[:k]; parts.append(seg)
    audio = np.concatenate(parts); audio = audio / max(1e-6, float(np.abs(audio).max())) * 0.89
    od = out_dir(v)
    wav = os.path.join(od, 'narration.wav'); sf.write(wav, audio, sr)
    lst = os.path.join(od, 'concat.txt')
    open(lst, 'w').write(''.join(f"file '{_ff_path(c)}'\n" for c in clips))
    vid = os.path.join(od, 'video_only.mp4')
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', _ff_path(lst), '-c', 'copy',
                    _ff_path(vid)], check=True)
    final = os.path.join(od, v.id + '.mp4'); tmp = final[:-4] + '.tmp.mp4'
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', _ff_path(vid), '-i', _ff_path(wav), '-map', '0:v', '-map', '1:a', '-c:v',
                    'copy', '-c:a', 'aac', '-b:a', S.VIDEO['audio_bitrate'], '-movflags', '+faststart', '-shortest',
                    _ff_path(tmp)], check=True)
    os.replace(tmp, final)
    write_docs(v, tl)
    if burn_subs:
        ass = os.path.join(od, v.id + '.ass'); bs = os.path.join(od, v.id + '_subtitled.mp4')
        r = subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', _ff_path(final), '-vf', f'ass={_filter_path(ass)}',
                            '-c:a', 'copy'] + codec + [_ff_path(bs + '.tmp.mp4')])
        if r.returncode == 0:
            os.replace(bs + '.tmp.mp4', bs); print('burnt-in subtitles:', bs)
        else:
            print('burn-in failed (ffmpeg needs libass); the .srv3/.srt files are still usable')
    print('DONE', final, f'{tl[-1]["start"] + tl[-1]["dur"]:.0f}s')


def docs_only(v):
    """Timestamps/refs/coverage/subtitles from cached narration audio, without rendering video."""
    analyse(v)
    write_docs(v, timeline(v))
    make_thumbnail(v)


def list_sources(course, refresh=False):
    """Download (or refresh) every source in content.csv and print NAME -> licence, size, URL."""
    c = SRC.Corpus(ROOT, course, download=True, refresh=refresh)
    if not c.csv_path:
        raise SystemExit(f'no content.csv in sources/{course}/ or sources/')
    print(f'{c.csv_path}\n{"NAME (use in Ref)":55s} {"licence":12s} {"cached":>10s}  URL')
    for n in c.table:
        p = c.paths.get(n)
        size = f'{os.path.getsize(p) // 1024} KB' if p else 'MISSING'
        print(f'{n:55s} {c.table[n][0]:12s} {size:>10s}  {c.urls[n]}')
    print(f'cache: {SRC.cache_dir(ROOT, course)}')
