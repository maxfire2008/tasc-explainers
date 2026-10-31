"""Subtitle generation from the narration timeline.

Outputs (all in out/<video>/):
  <id>.srv3   YouTube timed text with styling (colours, background, highlighted terms).
              Upload in YouTube Studio > Subtitles > Upload file > "With timing".
  <id>.srt    plain SubRip (any player / platform)
  <id>.vtt    WebVTT (web players)
  <id>.ass    styled Advanced SubStation, used by `render --burn-subs` for a burnt-in copy
Timing: each step's narration is split into cues of at most two lines; cue time is shared
out over that step's audio in proportion to characters.
"""
import html
import re

from . import style as S

MAX_LINE = 42
MAX_CUE = 2 * MAX_LINE

# highlight classes -> (regexes); keywords from Video.keywords are added to 'term'
BASE_PATTERNS = {
    'term': [r'information sheet'],
    'module': [r'\bElement \d+\b', r'\bSection [A-Z]\b', r'\bexam\b', r'\bclass tests?\b', r'\btests?\b'],
    'warn': [r'\b[Cc]areful\b', r'\bcommon mistake\b', r'\b[Nn]ever\b', r'\bnot L\b', r'\b[Ee]xam tip\b'],
}


def _sentences(text):
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    out = []
    for p in parts:
        while len(p) > MAX_CUE:
            cut = p.rfind(', ', 0, MAX_CUE)
            if cut < MAX_CUE // 3:
                cut = p.rfind(' ', 0, MAX_CUE)
            out.append(p[:cut + 1].strip()); p = p[cut + 1:].strip()
        if p:
            out.append(p)
    return out


def _wrap(s):
    if len(s) <= MAX_LINE:
        return [s]
    mid = len(s) // 2
    cands = [m.start() for m in re.finditer(' ', s)]
    cut = min(cands, key=lambda i: abs(i - mid))
    return [s[:cut].strip(), s[cut:].strip()]


def cues(timeline):
    """timeline: list of dict(start, audio_start, audio_dur, text) -> list of (t0, t1, lines)."""
    out = []
    for it in timeline:
        sents = _sentences(it['text'])
        total = sum(len(s) for s in sents) or 1
        t = it['audio_start']
        for s in sents:
            d = it['audio_dur'] * len(s) / total
            out.append((t, t + d, _wrap(s)))
            t += d
    return out


def _ts(t, sep=','):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}'


def write_srt(cs, path):
    with open(path, 'w', encoding='utf-8') as f:
        for i, (a, b, lines) in enumerate(cs, 1):
            f.write(f'{i}\n{_ts(a)} --> {_ts(b)}\n' + '\n'.join(lines) + '\n\n')


def write_vtt(cs, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('WEBVTT\n\n')
        for a, b, lines in cs:
            f.write(f'{_ts(a, ".")} --> {_ts(b, ".")}\n' + '\n'.join(lines) + '\n\n')


def _spans(text, patterns):
    """Split text into [(segment, class_or_None)] using the highlight patterns."""
    marks = []
    for cls, pats in patterns.items():
        for p in pats:
            for m in re.finditer(p, text, flags=re.I if cls == 'term' else 0):
                marks.append((m.start(), m.end(), cls))
    marks.sort()
    out, pos = [], 0
    for a, b, cls in marks:
        if a < pos:
            continue
        if a > pos:
            out.append((text[pos:a], None))
        out.append((text[a:b], cls)); pos = b
    if pos < len(text):
        out.append((text[pos:], None))
    return out


def _patterns(keywords):
    pats = {k: list(v) for k, v in BASE_PATTERNS.items()}
    pats['term'] += [r'\b' + re.escape(k) + r'\b' for k in sorted(keywords, key=len, reverse=True)]
    return pats


def write_srv3(cs, path, theme, keywords=()):
    """YouTube 'format 3' timed text.  Pens: 0 normal, 1 key term (course accent),
    2 module/assessment words (module accent), 3 warnings (pink)."""
    pats = _patterns(keywords)
    pen_of = {None: 0, 'term': 1, 'module': 2, 'warn': 3}
    bg = S.BG.upper()
    head = ['<?xml version="1.0" encoding="utf-8"?>', '<timedtext format="3">', '<head>']
    for pid, (fc, bold) in enumerate([('#FFFFFF', 0), (theme.accent, 1), (theme.accent2, 1), (S.PINK, 1)]):
        head.append(f'<pen id="{pid}" b="{bold}" fc="{fc.upper()}" fo="254" bc="{bg}" bo="200" '
                    f'et="3" ec="#000000" fs="4" sz="100"/>')
    head += ['<ws id="0" ju="2" pd="0" sd="0"/>', '<wp id="0" ap="7" ah="50" av="94"/>', '</head>', '<body>']
    body = []
    for a, b, lines in cs:
        segs = []
        for li, line in enumerate(lines):
            for seg, cls in _spans(line, pats):
                segs.append(f'<s p="{pen_of[cls]}">{html.escape(seg, quote=False)}</s>')
            if li < len(lines) - 1:
                segs.append('<s p="0">\n</s>')
        body.append(f'<p t="{int(a * 1000)}" d="{int((b - a) * 1000)}" wp="0" ws="0">' + ''.join(segs) + '</p>')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(head + body + ['</body>', '</timedtext>']) + '\n')


def _ass_col(hexcol, alpha=0):
    h = hexcol.lstrip('#'); r, g, b = h[0:2], h[2:4], h[4:6]
    return f'&H{alpha:02X}{b}{g}{r}'.upper()


def write_ass(cs, path, theme, keywords=()):
    pats = _patterns(keywords)
    col = {'term': theme.accent, 'module': theme.accent2, 'warn': S.PINK}
    W, H = S.VIDEO['width'], S.VIDEO['height']
    lines = ['[Script Info]', 'ScriptType: v4.00+', f'PlayResX: {W}', f'PlayResY: {H}', 'WrapStyle: 2', '',
             '[V4+ Styles]',
             'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, '
             'Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, '
             'Alignment, MarginL, MarginR, MarginV, Encoding',
             f'Style: Default,{S.FONT_FAMILY[0]},46,{_ass_col("#FFFFFF")},{_ass_col("#FFFFFF")},'
             f'{_ass_col(S.BG, 0x30)},{_ass_col(S.BG, 0x30)},0,0,0,0,100,100,0,0,3,14,0,2,160,160,70,1',
             '', '[Events]', 'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']

    def ts(t):
        cs_ = int(round(t * 100)); h, cs_ = divmod(cs_, 360000); m, cs_ = divmod(cs_, 6000); s, cs_ = divmod(cs_, 100)
        return f'{h}:{m:02d}:{s:02d}.{cs_:02d}'

    for a, b, ls in cs:
        txt = []
        for line in ls:
            seg_txt = ''
            for seg, cls in _spans(line, pats):
                seg = seg.replace('{', '(').replace('}', ')')
                seg_txt += ('{\\b1\\c' + _ass_col(col[cls]) + '&}' + seg + '{\\b0\\c&HFFFFFF&}') if cls else seg
            txt.append(seg_txt)
        lines.append(f'Dialogue: 0,{ts(a)},{ts(b)},Default,,0,0,0,,' + '\\N'.join(txt))
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def write_all(timeline, base, theme, keywords=()):
    cs = cues(timeline)
    write_srt(cs, base + '.srt'); write_vtt(cs, base + '.vtt')
    write_srv3(cs, base + '.srv3', theme, keywords); write_ass(cs, base + '.ass', theme, keywords)
    return cs
