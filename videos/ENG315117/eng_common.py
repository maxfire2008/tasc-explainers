"""Slide kinds shared by the three ENG315117 videos (English: no formulas, so the slides are built from quotations,
freeze frames, cards and tables rather than diagrams).

Every scene's draw function is a `Slide(kind, **config)`.  Each Slide has a deterministic repr, so the engine's clip cache
key changes whenever the slide's content changes (a plain closure would hide the content from the cache key).

Common config
    title   slide title (header)           chip   small label top right, e.g. 'Element 3 · codes and conventions'
Kinds
    media   freeze frame / clip on the left, quotation under it, bullets on the right (all build up with the step number)
    quotes  full-width quotation cards, each with a technique tag and a short comment
    grid    cards in columns (tag, heading, body); `per` cards appear per step
    table   comparison table: header row + one row per step
    bullets plain build-up list (optionally beside a freeze frame)
    model   an annotated paragraph, one labelled part per step
    tips    numbered tips, cumulative
"""
import os
import textwrap

from explainer import layout as L
from explainer.layout import header, T, chip, tag, frac, box, quote, still, GRID

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FRAMES = os.path.join(ROOT, 'sources', 'ENG315117', 'cache', 'frames')
CLIP_FPS = 10
CLIP_LEN = {'nx_plane_clip': 24, 'sh_beach_clip': 24}     # frames available for each clip (2.4 s at 10 fps)


def FR(name):
    return os.path.join(FRAMES, name + '.jpg')


def clip_path(name, ph):
    n = CLIP_LEN[name]
    return os.path.join(FRAMES, f'{name}_{min(n, 1 + int(ph * n)):03d}.jpg')


def fit(s, w, size, k=0.56):
    """Wrap s to a column w (figure fraction) wide at `size` pt.  Existing line breaks are kept."""
    chars = max(8, int(w * 1920 / (size * 100 / 72 * k)))
    return '\n'.join(textwrap.fill(p, chars) if p else '' for p in s.split('\n'))


def lines(s):
    return s.count('\n') + 1


def _pick(seq, s, default=None):
    """Value for step s from a per-step list (the last given value carries on)."""
    if seq is None:
        return default
    if not isinstance(seq, (list, tuple)):
        return seq
    if not seq:
        return default
    return seq[min(s, len(seq) - 1)]


class Slide:
    def __init__(self, kind, **cfg):
        self.kind, self.cfg = kind, cfg

    def __repr__(self):
        return f'Slide({self.kind!r}, {self.cfg!r})'

    def __call__(self, fig, s, ph):
        c = self.cfg
        if c.get('title'):
            header(fig, c['title'])
        if c.get('chip'):
            chip(fig, c['chip'])
        getattr(self, '_' + self.kind)(fig, s, ph, c)

    # ------------------------------------------------------------------ media
    def _media(self, fig, s, ph, c):
        img = _pick(c.get('img'), s)
        w_img = c.get('img_w', 0.44)
        x0, y_top = 0.05, 0.80
        y_img = y_top - w_img * 1.0
        if img:
            path = clip_path(img, ph) if img.endswith('_clip') else FR(img)
            still(fig, path, [x0, y_img, w_img, w_img], credit=_pick(c.get('credit'), s, ''))
            cap = _pick(c.get('cap'), s, '')
            ycur = y_img - 0.012
            if cap:
                t = fig.text(x0 + w_img / 2, ycur, fit(cap, w_img, 19), color=L.MUT, fontsize=19, ha='center', va='top')
                ycur -= frac(19) * lines(fit(cap, w_img, 19)) + 0.012
        else:
            ycur = y_top
        q = _pick(c.get('quote'), s)
        if q:
            text, who = q
            size = c.get('qsize', 30)
            ycur = quote(fig, x0, ycur - 0.01, w_img, fit(text, w_img - 0.03, size), who, size=size)
        xr = x0 + w_img + 0.04
        items = c.get('bullets', [])
        n = _pick(c.get('bshow'), s, s + 1)
        y = 0.80
        size = c.get('bsize', 29)
        wr = 0.96 - xr - 0.022
        for i, it in enumerate(items[:n]):
            txt = fit(it, wr, size)
            col = L.FG if (i == n - 1 or not c.get('dim', True)) else L.SOFT
            fig.text(xr, y, '•', color=L.A1(), fontsize=size, va='top')
            fig.text(xr + 0.022, y, txt, color=col, fontsize=size, va='top', linespacing=1.3)
            y -= frac(size) * lines(txt) + 0.03
        t = _pick(c.get('tagline'), s)
        if t:
            tag(fig, xr, 0.12, t, color=c.get('tagcol'))

    # ------------------------------------------------------------------ bullets (optionally with a frame on the right)
    def _bullets(self, fig, s, ph, c):
        items = c['items']
        size = c.get('size', 34)
        img = _pick(c.get('img'), s)
        width = (0.46 if img else 0.88)
        y = 0.77
        n = _pick(c.get('show'), s, s + 1)
        for i, it in enumerate(items[:n]):
            txt = fit(it, width - 0.03, size)
            col = L.FG if (i == n - 1 or not c.get('dim', True)) else L.SOFT
            fig.text(0.05, y, '•', color=L.A1(), fontsize=size, va='top')
            fig.text(0.073, y, txt, color=col, fontsize=size, va='top', linespacing=1.3)
            y -= frac(size) * lines(txt) + c.get('gap', 0.045)
        if img:
            still(fig, FR(img), [0.56, 0.38, 0.38, 0.38], caption=fit(_pick(c.get('cap'), s, ''), 0.38, 17))
        foot = _pick(c.get('foot'), s)
        if foot:
            T(fig, 0.05, 0.115, fit(foot, 0.9, 22), size=22, color=L.YELLOW)

    # ------------------------------------------------------------------ quotes
    def _quotes(self, fig, s, ph, c):
        items = c['items']                       # (quote, source, tag, comment)
        n = _pick(c.get('show'), s, s + 1)
        size = c.get('size', 34)
        slot = min(0.26, 0.74 / max(c.get('rows', 3), 1))
        for i, (qt, who, tg, com) in enumerate(items[:n]):
            bright = (i == n - 1)
            ytop = 0.80 - i * slot
            wq = 0.58
            quote(fig, 0.05, ytop, wq, fit(qt, wq - 0.03, size), who, size=size, color=L.FG if bright else L.SOFT)
            tag(fig, 0.68, ytop - 0.02, tg, color=L.A2() if bright else L.MUT, size=19)
            fig.text(0.68, ytop - 0.065, fit(com, 0.29, 22), color=L.SOFT if bright else L.MUT, fontsize=22, va='top',
                     linespacing=1.3)

    # ------------------------------------------------------------------ grid
    def _grid(self, fig, s, ph, c):
        items = c['items']                       # (tag, heading, body)
        cols = c.get('cols', 3)
        per = c.get('per', 1)
        n = _pick(c.get('show'), s, min(len(items), (s + 1) * per))
        gx, gy = 0.018, 0.02
        top, bottom = 0.80, 0.09
        rows = (len(items) + cols - 1) // cols
        cw = (0.90 - gx * (cols - 1)) / cols
        ch = (top - bottom - gy * (rows - 1)) / rows
        size = c.get('size', 24)
        ch = min(ch, c.get('ch_max', 0.40))
        for i, (tg, hd, body) in enumerate(items[:n]):
            r, k = divmod(i, cols)
            x = 0.05 + k * (cw + gx)
            y = top - (r + 1) * ch - r * gy
            new = (i >= n - per)
            box(fig, x, y, cw, ch, fc=L.PANEL2 if new else L.PANEL, ec=L.A2() if new else L.GRID, lw=2)
            tag(fig, x + 0.014, y + ch - 0.03, tg, color=c.get('tagcol') or L.A1(), size=15)
            T(fig, x + 0.014, y + ch - 0.058, fit(hd, cw - 0.028, size + 2), size=size + 2, color=L.FG, weight='bold')
            hl = lines(fit(hd, cw - 0.028, size + 2))
            T(fig, x + 0.014, y + ch - 0.066 - frac(size + 2) * hl, fit(body, cw - 0.028, size), size=size,
              color=L.SOFT if not new else L.FG)

    # ------------------------------------------------------------------ table
    def _table(self, fig, s, ph, c):
        head = c['head']                         # ['', 'North by Northwest', ...]
        rows = c['rows']
        n = _pick(c.get('show'), s, s + 1)
        k = len(head)
        size = c.get('size', 26)
        x0, w_label = 0.05, c.get('label_w', 0.14)
        cw = (0.91 - w_label) / (k - 1)
        y = 0.80
        hl = 1
        for j in range(1, k):
            ht = fit(head[j], cw - 0.02, size + 2)
            hl = max(hl, lines(ht))
            fig.text(x0 + w_label + (j - 1) * cw + 0.008, y, ht, color=L.A1(), fontsize=size + 2, weight='bold', va='top')
        y -= frac(size + 2) * hl + 0.03
        for i, row in enumerate(rows[:n]):
            bright = (i == n - 1)
            cells = [fit(t, cw - 0.02, size) for t in row[1:]]
            h = max(lines(t) for t in cells) * frac(size) + 0.034
            box(fig, x0, y - h + 0.008, 0.91, h, fc=L.PANEL2 if bright else L.PANEL, ec=L.A2() if bright else L.PANEL, lw=2, r=0.008)
            fig.text(x0 + 0.01, y - 0.004, fit(row[0], w_label - 0.012, size), color=L.A2(), fontsize=size, weight='bold', va='top')
            for j, t in enumerate(cells):
                fig.text(x0 + w_label + j * cw + 0.008, y - 0.004, t, color=L.FG if bright else L.SOFT, fontsize=size,
                         va='top', linespacing=1.25)
            y -= h + 0.01

    # ------------------------------------------------------------------ model paragraph
    def _model(self, fig, s, ph, c):
        parts = c['parts']                       # (label, text)
        size = c.get('size', 28)
        n = _pick(c.get('show'), s, s + 1)
        if c.get('question'):
            box(fig, 0.05, 0.66, 0.90, 0.145, fc=L.PANEL, ec=L.GRID)
            T(fig, 0.065, 0.795, fit('Practice question: ' + c['question'], 0.86, 26), size=26, color=L.A2(), weight='bold')
        y = 0.625 if c.get('question') else 0.79
        for i, (lab, txt) in enumerate(parts[:n]):
            bright = (i == n - 1)
            t = fit(txt, 0.74, size)
            tag(fig, 0.05, y - 0.02, lab, color=L.A2() if bright else L.GRID, size=18)
            fig.text(0.19, y, t, color=L.FG if bright else L.SOFT, fontsize=size, va='top', linespacing=1.3)
            y -= frac(size) * lines(t) + 0.03

    # ------------------------------------------------------------------ tips
    def _tips(self, fig, s, ph, c):
        items = c['items']
        n = _pick(c.get('show'), s, s + 1)
        size = c.get('size', 26)
        cols = c.get('cols', 2)
        rows = (len(items) + cols - 1) // cols
        cw = 0.43
        y0 = 0.80
        per_row = (0.80 - 0.09) / rows
        for i, (hd, body) in enumerate(items[:n]):
            r, k = divmod(i, cols)
            x = 0.05 + k * (cw + 0.04)
            y = y0 - r * per_row
            new = (i == n - 1)
            fig.text(x, y, str(i + 1), color=L.BG, fontsize=22, weight='bold', ha='center', va='center',
                     bbox=dict(boxstyle='circle,pad=0.3', fc=L.YELLOW if new else L.GRID, ec='none'))
            T(fig, x + 0.03, y + 0.018, fit(hd, cw - 0.04, size + 1), size=size + 1, color=L.FG if new else L.SOFT, weight='bold')
            hl = lines(fit(hd, cw - 0.04, size + 1))
            T(fig, x + 0.03, y + 0.018 - frac(size + 1) * hl - 0.004, fit(body, cw - 0.04, size - 3), size=size - 3,
              color=L.SOFT if new else L.MUT)


def title_text(fig, kicker, title, sub, course):
    """Shared text block for the three title cards (left aligned, over a signature graphic drawn by the module)."""
    fig.text(0.06, 0.80, kicker, color=L.A2(), fontsize=30, weight='bold', va='center')
    fig.text(0.06, 0.72, title, color=L.FG, fontsize=62, weight='bold', va='top', linespacing=1.15)
    fig.text(0.06, 0.34, sub, color=L.SOFT, fontsize=27, va='top', linespacing=1.4)
    fig.text(0.06, 0.17, course, color=L.A1(), fontsize=28, weight='bold', va='center')
