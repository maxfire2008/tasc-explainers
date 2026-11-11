"""Slide kinds shared by the four CHM415115 videos (Chemistry criteria 5 to 8).

Most Chemistry slides are cards, tables, bullets, formulas and lines of working, so they are data-driven:
every scene's draw function is `Slide(kind, **config)`.  A Slide has a deterministic repr, so the engine's clip
cache key follows its content (a plain closure would hide the content from the cache key).  Diagrams (cells,
energy profiles, molecules, graphs) are ordinary draw functions in each criterion's visuals file.

Text helper `ch()`: write chemistry in plain ASCII and it is converted for display.
    ^2+  ^-  ^-1  ->  <=>  become superscripts and arrows anywhere in a string;
    `...` (backticks) additionally turns digits after a letter or ')' into subscripts: `Cr_2O_7^2-` or `H2O`.
    Charges must always be written with ^ (Fe^3+), coefficients with a space or at the start (2H2O).

Common config
    title   slide title (header)         chip   small label top right, e.g. 'Element 2 · half-equations'
    counts  how many items are visible at each step (list; the last value carries on).  Default: step s shows s+1.
Kinds
    title / assess / elements / standards / roadmap   the four intro slides and the title card
    bullets, cards, table, eqs, worked, tips, summary, note
"""
import re
import textwrap

from matplotlib.patches import Rectangle

from explainer import layout as L
from explainer.layout import (header, T, chip, frac, box, card, bullets, FG, SOFT, MUT, GRID, PANEL, PANEL2, BG, PINK,
                              GREEN, YELLOW, wax)

_SUP = dict(zip('0123456789+-', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻'))
_SUB = dict(zip('0123456789', '₀₁₂₃₄₅₆₇₈₉'))


def C():
    return L.A1(), L.A2()


def ch(s):
    """Convert compact chemistry notation to display text (see module docstring)."""
    def sup(m):
        return ''.join(_SUP[c] for c in m.group(1))

    def one(seg, formula):
        seg = seg.replace('<=>', '⇌').replace('->', '→').replace('<-', '←')
        seg = re.sub(r'_(\d+)', lambda m: ''.join(_SUB[c] for c in m.group(1)), seg)
        if formula:
            seg = re.sub(r'(?<=[A-Za-z\)\]])(\d+)', lambda m: ''.join(_SUB[c] for c in m.group(1)), seg)
            seg = re.sub(r'_(\d+)', lambda m: ''.join(_SUB[c] for c in m.group(1)), seg)
        seg = re.sub(r'\^([0-9+\-]+)', sup, seg)
        return seg
    parts = s.split('`')
    return ''.join(one(p, i % 2 == 1) for i, p in enumerate(parts))


def fit(s, w, size, k=0.50, reflow=True):
    """Wrap s to a column w (figure fraction) wide at `size` pt.  Single line breaks are treated as spaces when
    reflow=True (blank lines are kept)."""
    chars = max(8, int(w * 1920 / (size * 100 / 72 * k)))
    if reflow:
        s = '\n\n'.join(' '.join(p.split('\n')) for p in s.split('\n\n'))
    return '\n'.join(textwrap.fill(p, chars) if p else '' for p in s.split('\n'))


def nl(s):
    return s.count('\n') + 1


def _n(cfg, s, total):
    """Number of items visible at step s."""
    c = cfg.get('counts')
    if c is None:
        per = cfg.get('per', 1)
        return min(total, (s + 1) * per)
    return min(total, c[min(s, len(c) - 1)])


def sf(fig, x, y, s):
    """The rounded answer under an unrounded one.  On screen only: never narrated."""
    T(fig, x, y, s, size=21, color=GREEN)


def extend(base, n, *extras):
    """Add steps after a finished scene: steps 0..n-1 use base, later steps use extras in turn."""
    def draw(fig, s, ph):
        if s < n:
            return base(fig, s, ph)
        return extras[s - n](fig, 0, ph)
    return draw


def sheet(section, fig, x, y, s, **kw):
    """sheet_eq with the real information-sheet section heading (this course's sheet has several)."""
    L.ctx['sheet_section'] = section
    return L.sheet_eq(fig, x, y, s, **kw)


def lines(fig, x, y, rows, size=26, gap=0.07):
    """Lines of working: (text, colour) from y downwards.  Returns the y below the last line."""
    for st, c in rows:
        T(fig, x, y, ch(st), size=size, color=c)
        y -= gap
    return y


class Slide:
    def __init__(self, kind, **cfg):
        self.kind, self.cfg = kind, cfg

    def __repr__(self):
        return f'Slide({self.kind!r}, {self.cfg!r})'

    def __call__(self, fig, s, ph):
        c = self.cfg
        if c.get('title'):
            header(fig, ch(c['title']))
        if c.get('chip'):
            chip(fig, c['chip'], color=c.get('chip_color'))
        getattr(self, '_' + self.kind)(fig, s, ph, c)

    # ------------------------------------------------------------------ title card + intro
    def _title(self, fig, s, ph, c):
        C1, C2 = C()
        fig.text(0.04, 0.76, c['kicker'], ha='left', va='center', color=C1, fontsize=40, weight='bold')
        fig.text(0.04, 0.53, c['name'], ha='left', va='center', color=FG, fontsize=c.get('size', 58), weight='bold',
                 linespacing=1.15)
        fig.text(0.04, 0.27, f"TASC Chemistry  CHM415115\nRevision for class tests and the exam", ha='left', va='center',
                 color=SOFT, fontsize=26, linespacing=1.4)
        c['art'](fig, [0.57, 0.14, 0.42, 0.7467], ph)

    def _assess(self, fig, s, ph, c):
        C1, C2 = C()
        card(fig, 0.05, 0.50, 0.40, 0.25, 'Internal', c['internal'], tcol=GREEN)
        card(fig, 0.05, 0.20, 0.40, 0.25, 'External', c['external'], tcol=C2)
        tiles = [('≈45 min', 'suggested time'), ('45', 'marks'), ('5–7', 'compulsory questions'),
                 ('Info sheet', '+ approved calculator')]
        for i, (big, small) in enumerate(tiles):
            x = 0.52 + (i % 2) * 0.225; y = 0.50 - (i // 2) * 0.30
            box(fig, x, y, 0.205, 0.25, fc=PANEL2)
            T(fig, x + 0.1025, y + 0.16, big, size=46 if len(big) < 8 else 36, color=YELLOW, weight='bold', ha='center',
              va='center')
            T(fig, x + 0.1025, y + 0.06, small, size=21, color=SOFT, ha='center', va='center')
        T(fig, 0.52, 0.16, f"{c['section']} of the exam (external assessment specifications)", size=18, color=MUT)

    def _elements(self, fig, s, ph, c):
        C1, C2 = C()
        items = c['items']                       # (title, body)
        n = len(items)
        cols = [C1, C2, PINK, GREEN, YELLOW, C1]
        per_row = 3 if n > 4 else n
        rows = (n + per_row - 1) // per_row
        w = (0.90 - 0.02 * (per_row - 1)) / per_row
        h = 0.52 if rows == 1 else 0.315
        for i, (t, b) in enumerate(items):
            r, k = divmod(i, per_row)
            x = 0.05 + k * (w + 0.02)
            y = 0.79 - h - r * (h + 0.03)
            box(fig, x, y, w, h)
            T(fig, x + 0.02, y + h - 0.02, f'Element {i + 1}', size=30, color=cols[i % 6], weight='bold')
            T(fig, x + 0.02, y + h - 0.02 - frac(30) - 0.008, t, size=26, color=FG, weight='bold')
            T(fig, x + 0.02, y + h - 0.02 - frac(30) - frac(26) * nl(t) - 0.02, fit(b, w - 0.04, 20), size=20, color=SOFT)
        T(fig, 0.05, 0.105, 'Numbered in the order they appear in the course document’s standards table', size=19, color=MUT)

    def _standards(self, fig, s, ph, c):
        C1, C2 = C()
        cols = [(0.33, 'C', GREEN), (0.54, 'B', C1), (0.75, 'A', C2)]
        for x, l, col in cols:
            T(fig, x, 0.80, l, size=40, color=col, weight='bold')
        rows = c['rows']
        n = len(rows)
        step = 0.64 / n
        for j, r in enumerate(rows):
            y = 0.725 - j * step
            box(fig, 0.05, y - step + 0.012, 0.90, step - 0.012, fc=PANEL if j % 2 == 0 else PANEL2)
            T(fig, 0.065, y - (step - 0.012) / 2, r[0], size=22, color=FG, weight='bold', va='center')
            for (x, _, col), txt in zip(cols, r[1:]):
                T(fig, x, y - (step - 0.012) / 2, fit(txt, 0.2, 18), size=18, color=SOFT if col != C2 else FG, va='center')

    def _roadmap(self, fig, s, ph, c):
        C1, C2 = C()
        parts = c['parts']
        n = len(parts)
        pitch = min(0.112, 0.64 / n)
        cols = [C1, C2, PINK, GREEN, YELLOW, FG, C1, C2]
        for i, (a, b) in enumerate(parts):
            y = 0.73 - i * pitch
            box(fig, 0.05, y - pitch / 2 + 0.008, 0.90, pitch - 0.016)
            T(fig, 0.07, y, a, size=28, color=cols[i % 8], weight='bold', va='center')
            T(fig, 0.19, y, ch(b), size=27, color=FG, va='center')

    # ------------------------------------------------------------------ general kinds
    def _bullets(self, fig, s, ph, c):
        items = [ch(i) for i in c['items']]
        n = _n(c, s, len(items))
        w = c.get('w', 0.88)
        size = c.get('size', 27)
        items = [fit(i, w - 0.03, size) for i in items]
        y = bullets(fig, items, n, c.get('x', 0.05), c.get('y', 0.78), size=size, gap=c.get('gap', 0.022), dim=c.get('dim', True))
        if c.get('note'):
            T(fig, 0.05, 0.14, ch(c['note']), size=21, color=c.get('note_color', YELLOW))
        if c.get('art'):
            c['art'](fig, s, ph)

    def _note(self, fig, s, ph, c):
        T(fig, 0.05, 0.78, fit(ch(c['text']), 0.88, c.get('size', 30)), size=c.get('size', 30), color=FG)

    def _cards(self, fig, s, ph, c):
        cards = c['cards']                      # (title, body, colour)
        n = _n(c, s, len(cards))
        cols = c.get('cols', 2)
        size = c.get('size', 22) + 4
        gx = 0.02
        w = (0.90 - gx * (cols - 1)) / cols
        rows = (len(cards) + cols - 1) // cols
        h = c.get('h', min(0.34, (0.66 - 0.02 * (rows - 1)) / rows))
        for i in range(n):
            t, b, col = cards[i][:3]
            r, k = divmod(i, cols)
            x = 0.05 + k * (w + gx)
            y = 0.78 - h - r * (h + 0.02)
            card(fig, x, y, w, h, ch(t), fit(ch(b), w - 0.035, size), tcol=col, size=size)
        if c.get('note'):
            T(fig, 0.05, 0.12, ch(c['note']), size=20, color=MUT)

    def _table(self, fig, s, ph, c):
        C1, C2 = C()
        head, rows = c['head'], c['rows']
        widths = c['widths']
        n = _n(c, s, len(rows))
        size = c.get('size', 22) + 2
        x0 = 0.05
        xs = [x0]
        for w in widths:
            xs.append(xs[-1] + w)
        y = 0.80
        for j, hd in enumerate(head):
            T(fig, xs[j] + 0.012, y, ch(hd), size=size, color=C1, weight='bold')
        y -= frac(size) + 0.012
        fig.add_artist(Rectangle((xs[0], y + 0.004), xs[-1] - xs[0], 0.0016, transform=fig.transFigure, fc=GRID, ec='none'))
        y -= 0.01
        for i in range(n):
            cells = [fit(ch(t), widths[j] - 0.02, size) for j, t in enumerate(rows[i])]
            h = max(nl(t) for t in cells) * frac(size) + 0.024
            box(fig, x0, y - h + 0.006, xs[-1] - x0, h - 0.004, fc=PANEL if i % 2 == 0 else PANEL2)
            for j, t in enumerate(cells):
                T(fig, xs[j] + 0.012, y - 0.004, t, size=size, color=FG if (j == 0 or i == n - 1) else SOFT,
                  weight='bold' if j == 0 else 'normal')
            y -= h + 0.006
        if c.get('note'):
            T(fig, 0.05, 0.12, ch(c['note']), size=20, color=MUT)

    def _eqs(self, fig, s, ph, c):
        """items: (kind, text, note); kind 'sheet:<section>' | 'learn' | 'eq' | 'text'.  Optional side bullets."""
        items = c['items']
        n = _n(c, s, len(items))
        x = c.get('x', 0.06)
        y = c.get('y', 0.74)
        size = c.get('size', 34)
        gap = c.get('gap', 0.16)
        for i in range(n):
            kind, tex, note = (list(items[i]) + [''])[:3]
            dim = i < n - 1 and c.get('dim', False)
            if kind.startswith('sheet'):
                sheet(kind.split(':', 1)[1] if ':' in kind else c.get('section', ''), fig, x, y, tex, size=size)
            elif kind == 'learn':
                L.learn_eq(fig, x, y, tex, size=size)
            elif kind == 'eq':
                L.eq(fig, x, y, ch(tex), size=size)
            else:
                T(fig, x, y, ch(tex), size=size, color=FG)
            if note:
                T(fig, c.get('nx', 0.50), y + 0.02, fit(ch(note), 0.45, 22), size=22, color=SOFT)
            y -= gap
        if c.get('side'):
            side = [fit(ch(t), 0.40, 24) for t in c['side']]
            bullets(fig, side, _n(dict(counts=c.get('side_counts', c.get('counts')), per=c.get('per', 1)), s, len(side)),
                    0.55, 0.74, size=24)

    def _worked(self, fig, s, ph, c):
        """q: question text; rows: dict(s=step, t=text, sf=rounded line, col=colour, h=extra gap)."""
        C1, C2 = C()
        q = fit(ch(c['q']), 0.86, 22)
        qh = 0.06 + frac(26) + nl(q) * frac(22) * 1.05
        card(fig, 0.05, 0.80 - qh, 0.90, qh, 'Question', q, tcol=C2, size=22)
        y = 0.80 - qh - 0.03
        for r in c['rows']:
            if r['s'] > s:
                continue
            col = r.get('col', FG)
            t = ch(r['t'])
            size = r.get('size', c.get('size', 25))
            if t:
                T(fig, r.get('x', 0.06), y, t, size=size, color=col)
                y -= frac(size) * nl(t) + 0.012
            if r.get('sf'):
                sf(fig, r.get('x', 0.06), y, ch(r['sf']))
                y -= frac(21) + 0.012
            y -= r.get('gap', 0.012)
        if c.get('art'):
            c['art'](fig, s, ph)

    def _tips(self, fig, s, ph, c):
        C1, C2 = C()
        tips = c['tips']
        n = _n(c, s, len(tips))
        cols = [C1, C2, PINK, GREEN, YELLOW]
        base = c.get('start', 1)
        per_col = (len(tips) + 1) // 2 if len(tips) > 8 else 4
        h = 0.145
        for i in range(n):
            x = 0.05 + (i % 2) * 0.46; y = 0.66 - (i // 2) * 0.165
            box(fig, x, y, 0.44, h, fc=PANEL)
            T(fig, x + 0.015, y + h / 2, str(base + i), size=34, color=cols[(base + i) % 5], weight='bold', va='center')
            T(fig, x + 0.07, y + h / 2, fit(ch(tips[i]), 0.35, 20), size=20, va='center')
        T(fig, 0.05, 0.13, c.get('foot', 'From examiners’ comments in TASC assessment reports'), size=18, color=MUT)

    def _summary(self, fig, s, ph, c):
        C1, C2 = C()
        x, y = 0.06, 0.75
        for t, col in c['chips']:
            t = ch(t)
            w = len(t) * 0.0105 + 0.012
            if x + w > 0.95:
                x = 0.06; y -= 0.10
            chip(fig, t, color={'1': C1, '2': C2, 'p': PINK, 'g': GREEN, 'y': YELLOW}[col], size=24, x=x, y=y, ha='left')
            x += w + 0.015
        T(fig, 0.06, 0.18, ch(c['close']), size=30, color=YELLOW, weight='bold')



class Seq:
    """One scene whose steps are different Slides (step s draws slides[s]; the last one carries on)."""
    def __init__(self, *slides):
        self.slides = slides

    def __repr__(self):
        return f'Seq({self.slides!r})'

    def __call__(self, fig, s, ph):
        self.slides[min(s, len(self.slides) - 1)](fig, 0, ph)


def sheet_tag(fig, x, y, section, color=None):
    """Tag for information-sheet material that is not a formula (a table, a constant).  Counts as sheet use."""
    from explainer import style as S
    L.ctx['sheet_used'] = True
    fig.text(x, y, '▣ ' + S.INFO_SHEET_TAG.format(section=section), fontsize=15, color=color or L.A1(), ha='left',
             va='top', weight='bold')


def path_dots(ax, pts, ph, n=6, color=YELLOW, size=90, label=None):
    """Dots marching along a polyline (a loop when ph runs 0 -> 1)."""
    import numpy as np
    pts = np.array(pts, float)
    seg = np.hypot(*np.diff(pts, axis=0).T)
    cum = np.concatenate([[0], np.cumsum(seg)])
    for k in range(n):
        d = ((k / n + ph) % 1.0) * cum[-1]
        i = min(np.searchsorted(cum, d, side='right') - 1, len(seg) - 1)
        f = (d - cum[i]) / seg[i]
        p = pts[i] + f * (pts[i + 1] - pts[i])
        ax.scatter([p[0]], [p[1]], s=size, color=color, edgecolor=BG, linewidth=1.5, zorder=8)
