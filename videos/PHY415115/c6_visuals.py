"""Draw functions for PHY415115 Criterion 6 (electricity and magnetism).

Every function has the signature draw(fig, s, ph):
  s  = step index within the scene (the slide builds up as s increases)
  ph = animation phase in [0, 1) for animated steps (Step.anim), 0 for stills.
Animations must loop seamlessly: anything periodic must complete a whole number of
cycles as ph goes 0 -> 1.
Colours: C1 = course accent, C2 = module accent (from the theme), PINK/GREEN/YELLOW are semantic.
Conventions used throughout: positive charge = PINK, negative charge = C1 (course accent),
B out of the page = dot, B into the page = cross.
"""
import numpy as np
from matplotlib.patches import Circle, Rectangle, Polygon, FancyArrowPatch, Arc, Ellipse, Wedge

from explainer import layout as L
from explainer.layout import (header, T, bullets, box, card, eq, sheet_eq, learn_eq, chip, wax, gax, darrow, arrow,
                              label, frac, FG, SOFT, MUT, GRID, PANEL, PANEL2, BG, PINK, GREEN, YELLOW, TAU)


def C():
    return L.A1(), L.A2()


def _sheet(section, fig, x, y, s, **kw):
    """sheet_eq with the real section heading: this criterion uses several sections of the sheet."""
    L.ctx['sheet_section'] = section
    return sheet_eq(fig, x, y, s, **kw)


def eeq(fig, x, y, s, **kw):
    return _sheet('Electrostatics', fig, x, y, s, **kw)


def beq(fig, x, y, s, **kw):
    return _sheet('Magnetism', fig, x, y, s, **kw)


def ieq(fig, x, y, s, **kw):
    return _sheet('Induction', fig, x, y, s, **kw)


def _lines(fig, x, y, rows, size=26, gap=0.085):
    """Lines of working: (text, colour) from y downwards.  Returns the y below the last line."""
    for st, c in rows:
        T(fig, x, y, st, size=size, color=c)
        y -= gap
    return y


def _sf(fig, x, y, s):
    """The rounded answer, shown under the unrounded one.  On screen only: never narrated."""
    T(fig, x, y, s, size=21, color=GREEN)


def _note(fig, x, y, s, size=18):
    T(fig, x, y, s, size=size, color=MUT)


def _q(ax, x, y, q, r=0.05, size=22, label_=None):
    """A point charge: positive = PINK, negative = course accent."""
    C1, _ = C()
    ax.add_patch(Circle((x, y), r, fc=PINK if q > 0 else C1, ec=BG, lw=2, zorder=6))
    ax.text(x, y, '+' if q > 0 else '−', color=BG, fontsize=size, ha='center', va='center', weight='bold', zorder=7)
    if label_:
        ax.text(x, y - r - 0.035 * (ax.get_ylim()[1] - ax.get_ylim()[0]), label_, color=SOFT, fontsize=19, ha='center', va='top', zorder=7)


def _sym(ax, x, y, out, size=300, color=None):
    """B out of the page (dot in circle) or into the page (cross)."""
    color = color or SOFT
    if out:
        ax.scatter([x], [y], s=size, marker='o', facecolors='none', edgecolors=color, linewidths=2, zorder=4)
        ax.scatter([x], [y], s=size / 9, marker='o', color=color, zorder=4)
    else:
        ax.scatter([x], [y], s=size, marker='x', color=color, linewidths=2, zorder=4)


def _symgrid(ax, xs, ys, out, **kw):
    for x in xs:
        for y in ys:
            _sym(ax, x, y, out, **kw)


def _ring(x0, y0, r, n, off=0.0):
    a = off + TAU * np.arange(n) / n
    return np.c_[x0 + r * np.cos(a), y0 + r * np.sin(a)]


def _vecfield(xlim, ylim, fn, n=260):
    xs = np.linspace(*xlim, n); ys = np.linspace(*ylim, n)
    X, Y = np.meshgrid(xs, ys)
    U, W = fn(X, Y)
    return X, Y, U, W


def _stream(ax, xlim, ylim, fn, seeds, mask, color=None, lw=2.2, direction='forward', arrows=1.5, maxlen=30):
    """Field lines through `seeds`.  fn(X,Y)->(U,W); mask(X,Y)->bool where the field is not drawn."""
    X, Y, U, W = _vecfield(xlim, ylim, fn)
    m = mask(X, Y)
    U = np.ma.array(U, mask=m); W = np.ma.array(W, mask=m)
    ax.streamplot(X, Y, U, W, start_points=np.asarray(seeds), color=color or C()[0], linewidth=lw, arrowsize=arrows,
                  density=10, integration_direction=direction, maxlength=maxlen, broken_streamlines=False)


def _efield(ax, xlim, ylim, charges, nper=12, r0=0.09, mask_r=0.07, **kw):
    """Electric field lines of point charges [(x, y, q), ...]: lines start on the positive charges."""
    def fn(X, Y):
        U = np.zeros_like(X); W = np.zeros_like(X)
        for x0, y0, q in charges:
            dx, dy = X - x0, Y - y0
            r2 = dx * dx + dy * dy + 1e-9
            U += q * dx / r2 ** 1.5; W += q * dy / r2 ** 1.5
        return U, W

    def mask(X, Y):
        m = np.zeros(X.shape, bool)
        for x0, y0, q in charges:
            m |= (X - x0) ** 2 + (Y - y0) ** 2 < mask_r ** 2
        return m
    pos = [c for c in charges if c[2] > 0]
    neg = [c for c in charges if c[2] < 0]
    if pos:
        seeds = np.vstack([_ring(x0, y0, r0, max(4, int(round(nper * abs(q) / max(abs(c[2]) for c in pos)))), 0.1) for x0, y0, q in pos])
        _stream(ax, xlim, ylim, fn, seeds, mask, direction='forward', **kw)
    else:
        seeds = np.vstack([_ring(x0, y0, r0, nper, 0.1) for x0, y0, q in neg])
        _stream(ax, xlim, ylim, fn, seeds, mask, direction='backward', **kw)


def _bwires(ax, xlim, ylim, wires, nper=10, r0=0.1, mask_r=0.07, extra_seeds=None, **kw):
    """Magnetic field lines of long straight wires [(x, y, I), ...]; I > 0 is out of the page."""
    def fn(X, Y):
        U = np.zeros_like(X); W = np.zeros_like(X)
        for x0, y0, I in wires:
            dx, dy = X - x0, Y - y0
            r2 = dx * dx + dy * dy + 1e-9
            U += -I * dy / r2; W += I * dx / r2
        return U, W

    def mask(X, Y):
        m = np.zeros(X.shape, bool)
        for x0, y0, I in wires:
            m |= (X - x0) ** 2 + (Y - y0) ** 2 < mask_r ** 2
        return m
    seeds = np.vstack([np.array([[x0 + r0 * 1.45 ** k, y0] for k in range(nper)]) for x0, y0, I in wires]
                      + ([np.asarray(extra_seeds)] if extra_seeds is not None else []))
    _stream(ax, xlim, ylim, fn, seeds, mask, direction='both', **kw)


def _wire_pt(ax, x, y, out, size=1100):
    """A wire cross-section drawn as a marker (round whatever the axes aspect)."""
    ax.scatter([x], [y], s=size, marker='o', facecolors=PANEL2, edgecolors=YELLOW, linewidths=3, zorder=6)
    _sym(ax, x, y, out, size=size * 0.5, color=YELLOW)


def _wire(ax, x, y, out, r=0.05, label_=None):
    """Cross-section of a wire: current out of the page (dot) or into it (cross)."""
    ax.add_patch(Circle((x, y), r, fc=PANEL2, ec=YELLOW, lw=2.5, zorder=6))
    _sym(ax, x, y, out, size=200, color=YELLOW)
    if label_:
        ax.text(x, y - r - 0.03, label_, color=SOFT, fontsize=19, ha='center', va='top')


def _plates(ax, x0, x1, ytop, ybot, ptop='+', pbot='−', lw=7):
    C1, _ = C()
    for y, p in [(ytop, ptop), (ybot, pbot)]:
        ax.plot([x0, x1], [y, y], color=PINK if p == '+' else C1, lw=lw, solid_capstyle='butt', zorder=5)
        ax.text(x0 - 0.02 * (x1 - x0), y, p, color=PINK if p == '+' else C1, fontsize=26, ha='right', va='center', weight='bold')


def _unif(ax, x0, x1, ytop, ybot, n=6, down=True, color=None):
    """Uniform field lines between horizontal plates (down = from the top plate to the bottom plate)."""
    color = color or C()[0]
    for x in np.linspace(x0 + 0.1 * (x1 - x0), x1 - 0.1 * (x1 - x0), n):
        a, b = ((ytop, ybot) if down else (ybot, ytop))
        arrow(ax, (x, a - np.sign(a - b) * 0.01), (x, b + np.sign(a - b) * 0.01), color=color, lw=2, ms=18)


def _graph_pts(ax, x, y, c=YELLOW, s=90):
    ax.scatter(x, y, s=s, color=c, zorder=6, edgecolor=BG)


def _tablegrid(fig, x, y, colw, rowh, rows, size=22, head=True, colors=None):
    """A simple table: rows of strings; the first row is a header."""
    C1, C2 = C()
    for i, row in enumerate(rows):
        yy = y - i * rowh
        box(fig, x, yy - rowh * 0.92, sum(colw), rowh * 0.9, fc=PANEL2 if (head and i == 0) else PANEL)
        xx = x
        for j, cell in enumerate(row):
            col = (colors or {}).get((i, j), YELLOW if (head and i == 0) else FG)
            T(fig, xx + 0.012, yy - rowh * 0.45, cell, size=size, color=col, va='center', weight='bold' if (head and i == 0) else 'normal')
            xx += colw[j]


# ============================================================================ title and overview
def _title_fields(fig, rect, ph=0):
    """The title card and thumbnail graphic: dipole field lines and current loops, so Criterion 6 stands apart from 7 and 8."""
    C1, C2 = C()
    ax = wax(fig, rect, (-1.6, 1.6), (-1.1, 1.1))
    ax.set_aspect('equal')
    _efield(ax, (-1.6, 1.6), (-1.1, 1.1), [(-0.75, 0, 1), (0.75, 0, -1)], nper=14, r0=0.16, mask_r=0.14, lw=4.5, arrows=2.2, maxlen=60)
    for sx, q in [(-0.75, 1), (0.75, -1)]:
        ax.add_patch(Circle((sx, 0), 0.22, fc=PINK if q > 0 else C1, ec=BG, lw=5, zorder=6))
        ax.text(sx, 0, '+' if q > 0 else '−', color=BG, fontsize=46, ha='center', va='center', weight='bold', zorder=7)
    th = TAU * (ph + 0.0)
    for k, r in enumerate([0.22, 0.34]):
        ax.add_patch(Circle((0, -0.7), r, fill=False, ec=C2, lw=5, zorder=5, alpha=0.9 - 0.3 * k))
    ax.scatter([0], [-0.7], s=1100, color=YELLOW, edgecolor=BG, linewidth=4, zorder=8)


def thumbnail(fig):
    """The title card's colours, with fewer and larger words so it reads at small sizes."""
    C1, C2 = C()
    fig.text(0.04, 0.87, 'CRITERION 6', ha='left', va='center', color=C1, fontsize=64, weight='bold')
    fig.text(0.04, 0.65, 'Fields', ha='left', va='center', color=FG, fontsize=150, weight='bold')
    fig.text(0.04, 0.42, '& forces', ha='left', va='center', color=FG, fontsize=150, weight='bold')
    fig.text(0.04, 0.22, 'TASC Physics revision', ha='left', va='center', color=SOFT, fontsize=58)
    _title_fields(fig, [0.50, 0.19, 0.49, 0.7467])


def title_card(fig, s, ph):
    intro(fig, 0, ph)


def overview(fig, s, ph):
    intro(fig, s + 1, ph)


def intro(fig, s, ph):
    C1, C2 = C()
    if s == 0:
        fig.text(0.04, 0.76, 'CRITERION 6', ha='left', va='center', color=C1, fontsize=40, weight='bold')
        fig.text(0.04, 0.53, 'Electricity and\nmagnetism', ha='left', va='center',
                 color=FG, fontsize=62, weight='bold', linespacing=1.15)
        fig.text(0.04, 0.27, 'TASC Physics  PHY415115\nRevision for class tests and the exam', ha='left', va='center',
                 color=SOFT, fontsize=26, linespacing=1.4)
        _title_fields(fig, [0.52, 0.14, 0.47, 0.7467], ph)
        return
    if s == 1:
        header(fig, 'How Criterion 6 is assessed')
        card(fig, 0.05, 0.50, 0.40, 0.25, 'Internal', 'Your teacher: class tests, practicals\nand tasks during the year', tcol=GREEN)
        card(fig, 0.05, 0.20, 0.40, 0.25, 'External', 'End-of-year TASC exam:\nSection B is all Criterion 6', tcol=C2)
        tiles = [('≈45 min', 'suggested time'), ('45', 'marks'), ('5–7', 'compulsory questions'), ('Info sheet', '+ approved calculator')]
        for i, (big, small) in enumerate(tiles):
            x = 0.52 + (i % 2) * 0.225; y = 0.50 - (i // 2) * 0.30
            box(fig, x, y, 0.205, 0.25, fc=PANEL2)
            T(fig, x + 0.1025, y + 0.16, big, size=46 if len(big) < 8 else 36, color=YELLOW, weight='bold', ha='center', va='center')
            T(fig, x + 0.1025, y + 0.06, small, size=21, color=SOFT, ha='center', va='center')
        _note(fig, 0.52, 0.16, 'Section B of the exam (external assessment specifications)')
        return
    if s == 2:
        header(fig, 'The four elements of Criterion 6')
        items = [('Element 1', 'Principles', 'identify, describe and\nexplain principles\nand theories'),
                 ('Element 2', 'Problems', 'select and apply\nformulas to solve\nnumerical problems'),
                 ('Element 3', 'Data', 'interpret and analyse\ngraphs and tables'),
                 ('Element 4', 'Predictions', 'apply principles and\npredict in real-world\ncontexts')]
        for i, (n, t, b) in enumerate(items):
            x = 0.05 + i * 0.228
            box(fig, x, 0.22, 0.21, 0.50)
            T(fig, x + 0.02, 0.69, n, size=34, color=[C1, C2, PINK, GREEN][i], weight='bold')
            T(fig, x + 0.02, 0.54, t, size=32, color=FG, weight='bold')
            T(fig, x + 0.02, 0.46, b, size=21, color=SOFT)
        _note(fig, 0.05, 0.16, 'Numbered in the order they appear in the course document’s standards table', 19)
        return
    if s == 3:
        header(fig, 'What the standards ask for')
        cols = [(0.30, 'C', GREEN), (0.51, 'B', C1), (0.72, 'A', C2)]
        for x, l, c in cols:
            T(fig, x, 0.80, l, size=40, color=c, weight='bold')
        rows = [('E1 Principles', 'identifies', 'describes', 'explains'),
                ('E2 Problems', 'straightforward', 'several steps', 'complex, and\nanalyses validity'),
                ('E3 Data', 'interprets', 'analyses to generate\nnew information', 'analyses, evaluates,\ngeneralises'),
                ('E4 Predictions', 'familiar contexts', 'plausible, in\nunfamiliar contexts', 'reasoned and plausible,\nin unfamiliar contexts')]
        for j, r in enumerate(rows):
            y = 0.70 - j * 0.145
            box(fig, 0.05, y - 0.105, 0.90, 0.125, fc=PANEL if j % 2 == 0 else PANEL2)
            T(fig, 0.065, y - 0.042, r[0], size=26, color=FG, weight='bold', va='center')
            for (x, _, c), txt in zip(cols, r[1:]):
                T(fig, x, y - 0.042, txt, size=22, color=SOFT if c != C2 else FG, va='center')
        return
    header(fig, 'Roadmap')
    parts = [('Part 1', 'Charge, Coulomb’s law, electric fields, potential difference, charges in fields', C1),
             ('Part 2', 'Magnetic fields, forces on currents and moving charges, mass spectrometer', C2),
             ('Part 3', 'Induction: emf, Lenz’s law, eddy currents, generators', PINK),
             ('Part 4', 'Contexts: MRI, superconductors, light as a wave, real-world cases', GREEN),
             ('Finish', 'Tests & exam technique, and a one-screen summary', FG)]
    for i, (a, b, c) in enumerate(parts):
        y = 0.73 - i * 0.125
        box(fig, 0.05, y - 0.052, 0.90, 0.104)
        T(fig, 0.07, y, a, size=28, color=c, weight='bold', va='center')
        T(fig, 0.17, y, b, size=26, color=FG, va='center')


# ============================================================================ part 1: charge and fields
def principles(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Charge: the big picture')
    if s == 0:
        cols = [('Stationary charges', 'electrostatic effects', C1), ('Moving charges', 'magnetic effects', C2),
                ('Accelerating charges', 'electromagnetic radiation', PINK)]
        for i, (a, b, c) in enumerate(cols):
            x = 0.05 + i * 0.31
            box(fig, x, 0.16, 0.29, 0.62)
            T(fig, x + 0.145, 0.75, a, size=25, color=c, weight='bold', ha='center')
            T(fig, x + 0.145, 0.69, '→ ' + b, size=21, color=FG, ha='center')
            ax = wax(fig, [x + 0.02, 0.19, 0.25, 0.42], (-1, 1), (-1, 1))
            ax.set_aspect('equal')
            if i == 0:
                _efield(ax, (-1, 1), (-1, 1), [(0, 0, 1)], nper=10, r0=0.2, mask_r=0.15, lw=2.5)
                _q(ax, 0, 0, 1, r=0.16)
            elif i == 1:
                _wire(ax, 0, 0, True, r=0.14)
                for r in (0.4, 0.65, 0.9):
                    ax.add_patch(Circle((0, 0), r, fill=False, ec=C2, lw=2.5))
                    arrow(ax, (r * np.cos(2.2), r * np.sin(2.2)), (r * np.cos(2.35), r * np.sin(2.35)), color=C2, lw=2.5, ms=16)
            else:
                xs = np.linspace(-1, 1, 200)
                for k in range(3):
                    ax.add_patch(Circle((0, 0), 0.25 + 0.3 * ((k + ph * 1) % 3), fill=False, ec=PINK, lw=2.5, alpha=1 - 0.3 * ((k + ph * 1) % 3)))
                _q(ax, 0, 0.0 + 0.1 * np.sin(TAU * ph), 1, r=0.14)
        _note(fig, 0.05, 0.12, 'An oscillating charge emits waves at the oscillation frequency', 21)
        return
    items = ['Two kinds of charge: positive (protons)\nand negative (electrons)', 'Friction moves electrons between surfaces',
             'The surface that gains electrons is negative;\nthe one that loses them is positive', 'Charge is conserved: not created or destroyed',
             'Like charges repel, unlike charges attract']
    bullets(fig, items, 5, 0.05, 0.76, size=25, gap=0.026)
    ax = wax(fig, [0.55, 0.20, 0.40, 0.55], (0, 4), (0, 3.6))
    ax.set_aspect('equal')
    ax.add_patch(Rectangle((0.2, 1.6), 1.5, 1.2, fc=PANEL2, ec=C1, lw=3)); ax.text(0.95, 3.05, 'cloth (+)', color=PINK, fontsize=22, ha='center')
    ax.add_patch(Rectangle((2.3, 1.6), 1.5, 1.2, fc=PANEL2, ec=PINK, lw=3)); ax.text(3.05, 3.05, 'balloon (−)', color=C1, fontsize=22, ha='center')
    for k in range(4):
        ax.text(2.3 - 0.2, 1.8 + 0.28 * k, '−', color=C1, fontsize=26, ha='center', weight='bold')
        arrow(ax, (1.55, 1.9 + 0.28 * k), (2.5, 1.9 + 0.28 * k), color=C1, lw=2, ms=14)
    ax.text(2.0, 1.15, 'electrons move,\nprotons stay put', color=SOFT, fontsize=21, ha='center', va='top')


def _electroscope(ax, cx, cy, spread, cap, leaf, color=None):
    """Gold-leaf electroscope: cap on top, rod, two leaves.  spread = half angle in degrees."""
    C1, _ = C()
    ax.add_patch(Rectangle((cx - 0.6, cy - 1.0), 1.2, 1.45, fc='none', ec=MUT, lw=2.5, zorder=2))
    ax.plot([cx, cx], [cy - 0.1, cy + 0.9], color=SOFT, lw=5, zorder=3)
    ax.add_patch(Circle((cx, cy + 1.0), 0.18, fc=PANEL2, ec=SOFT, lw=2.5, zorder=3))
    a = np.radians(spread)
    for sg in (-1, 1):
        ax.plot([cx, cx + sg * 0.55 * np.sin(a) / max(np.sin(np.radians(30)), 0.01) * 0.5],
                [cy - 0.1, cy - 0.1 - 0.7 * np.cos(a)], color=YELLOW, lw=6, zorder=3)
    for txt, (x, y) in [(cap, (cx, cy + 1.0)), (leaf, (cx - 0.25, cy - 0.6)), (leaf, (cx + 0.25, cy - 0.6))]:
        if txt:
            ax.text(x, y, txt, color=PINK if txt == '+' else C1, fontsize=22, ha='center', va='center', weight='bold', zorder=6)


def polarise(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Charged objects attract neutral ones')
    chip(fig, 'Element 1 · explain')
    if s == 0:
        ax = wax(fig, [0.05, 0.14, 0.58, 0.62], (0, 6), (0, 3.6))
        ax.set_aspect('equal')
        ax.add_patch(Rectangle((0.3, 1.6), 1.7, 0.7, fc=PANEL2, ec=C1, lw=3)); ax.text(1.15, 1.95, 'charged rod', color=C1, fontsize=21, ha='center', va='center')
        for x in (0.55, 1.0, 1.45, 1.9):
            ax.text(x, 2.5, '−', color=C1, fontsize=24, ha='center')
        ax.add_patch(Rectangle((3.7, 1.7), 1.0, 0.5, fc=PANEL2, ec=SOFT, lw=2.5)); ax.text(4.2, 2.45, 'paper', color=SOFT, fontsize=21, ha='center')
        for x, y, t in [(3.82, 1.95, '+'), (3.82, 2.08, ''), (4.58, 1.95, '−')]:
            if t:
                ax.text(x, y, t, color=PINK if t == '+' else C1, fontsize=26, ha='center', va='center', weight='bold')
        arrow(ax, (3.62, 1.95), (2.5, 1.95), color=GREEN, lw=5, ms=28)
        arrow(ax, (4.8, 1.95), (5.5, 1.95), color=PINK, lw=2.5, ms=18)
        ax.text(3.0, 1.45, 'bigger pull', color=GREEN, fontsize=20, ha='center'); ax.text(5.3, 1.6, 'smaller push', color=PINK, fontsize=20, ha='center')
        bullets(fig, ['Charges in the neutral paper shift\n(it is polarised)', 'Near side is opposite to the rod:\nit is closer, so the force is bigger',
                      'Inverse square law: net force\ntowards the rod'], 3, 0.62, 0.74, size=22, gap=0.02)
        return
    if s == 1:
        ax = wax(fig, [0.05, 0.12, 0.45, 0.65], (-2, 2), (-1.6, 2.6)); ax.set_aspect('equal')
        _electroscope(ax, 0, 0.2, 38, '+', '−')
        ax.add_patch(Circle((0, 2.2), 0.45, fc=PANEL2, ec=C1, lw=3, zorder=5)); ax.text(0, 2.2, 'charged\nballoon −', color=C1, fontsize=17, ha='center', va='center', zorder=6)
        arrow(ax, (-0.3, 1.0), (-0.3, 0.1), color=C1, lw=2, ms=14)
        ax.text(0, -1.45, 'near, not touching', color=SOFT, fontsize=19, ha='center')
        bullets(fig, ['Neutral overall', 'Electrons are pushed away from\nthe balloon, down to the leaves', 'Both leaves are negative:\nthey repel and spread',
                      'Balloon removed: leaves fall back'], 4, 0.55, 0.74, size=23, gap=0.02)
        return
    ax = wax(fig, [0.05, 0.12, 0.45, 0.65], (-2, 2), (-1.6, 2.6)); ax.set_aspect('equal')
    _electroscope(ax, 0, 0.2, 38, '−', '−')
    ax.add_patch(Circle((0, 1.75), 0.45, fc=PANEL2, ec=C1, lw=3, zorder=5)); ax.text(0, 1.75, 'balloon\ntouches', color=C1, fontsize=17, ha='center', va='center', zorder=6)
    ax.text(0, -1.45, 'then removed: electroscope keeps a net charge', color=SOFT, fontsize=19, ha='center')
    bullets(fig, ['Touching transfers charge', 'Electroscope is left with a net charge', 'Leaves stay apart after the balloon is moved away',
                  'Near = induction (temporary)\nTouch = charging (lasting)'], 4, 0.55, 0.74, size=23, gap=0.02)


def coulomb(fig, s, ph):
    C1, C2 = C()
    header(fig, "Coulomb’s law")
    chip(fig, 'Element 2 · problems')
    eeq(fig, 0.05, 0.70, r'$F_E = \dfrac{k_E\,q_1 q_2}{r^2}$', size=44)
    T(fig, 0.05, 0.545, 'k_E = 9.00 × 10⁹ N m² C⁻²   (on the sheet)', size=22, color=SOFT)
    ax = gax(fig, [0.55, 0.20, 0.38, 0.52], (0, 4.2), (0, 4.2), 'distance r', 'force F', ticks=False)
    r = np.linspace(0.45, 4.2, 200); ax.plot(r, 1.0 / r ** 2 * 1.1, color=YELLOW, lw=3.5)
    for rr, c in [(1, PINK), (2, GREEN)]:
        ax.scatter([rr], [1.1 / rr ** 2], s=110, color=c, zorder=6, edgecolor=BG)
    ax.annotate('', xy=(2, 0.27), xytext=(1, 1.1), arrowprops=dict(arrowstyle='->', color=SOFT, lw=2))
    ax.text(2.1, 1.0, '2× distance:\n¼ force', color=SOFT, fontsize=20)
    _note(fig, 0.55, 0.15, 'illustrative inverse-square shape')
    if s == 0:
        bullets(fig, ['Use the sizes of the charges, then\nfind direction yourself', 'Like repel, unlike attract'], 2, 0.05, 0.47, size=24, gap=0.02)
        return
    items = ['Convert to C and m first', 'Square the distance', 'r is centre to centre: for a charged sphere\nuse the centre',
             'Always say: attraction or repulsion']
    bullets(fig, items, 4, 0.05, 0.47, size=24, gap=0.018)
    ax2 = wax(fig, [0.05, 0.05, 0.42, 0.13], (0, 8), (0, 1.6)); ax2.set_aspect('equal')
    ax2.add_patch(Circle((0.7, 0.7), 0.55, fc=PANEL2, ec=PINK, lw=3)); ax2.add_patch(Circle((7.2, 0.7), 0.14, fc=C1, ec=BG))
    ax2.annotate('', xy=(7.2, 1.3), xytext=(0.7, 1.3), arrowprops=dict(arrowstyle='<->', color=YELLOW, lw=2))
    ax2.text(4.0, 1.4, 'r = 2.20 m, from the centre', color=YELLOW, fontsize=17, ha='center')
    ax2.text(0.7, 0.7, 'R', color=FG, fontsize=16, ha='center', va='center')


def we_ball(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a hanging charged ball')
    chip(fig, 'Element 2 · problems')
    th = np.radians(25.0)
    ax = wax(fig, [0.03, 0.12, 0.48, 0.66], (-1.7, 1.7), (-0.6, 2.4)); ax.set_aspect('equal')
    ax.plot([-1.5, -1.5], [-0.3, 2.2], color=C1, lw=8); ax.plot([1.5, 1.5], [-0.3, 2.2], color=PINK, lw=8)
    ax.text(-1.5, 2.35, '−', color=C1, fontsize=28, ha='center', weight='bold'); ax.text(1.5, 2.35, '+', color=PINK, fontsize=28, ha='center', weight='bold')
    L_ = 1.9; bx, by = L_ * np.sin(th), 2.2 - L_ * np.cos(th)
    ax.scatter([0], [2.2], s=80, color=SOFT, zorder=5); ax.plot([0, bx], [2.2, by], color=SOFT, lw=2.5, zorder=3)
    ax.add_patch(Circle((bx, by), 0.12, fc=C1, ec=BG, lw=2, zorder=6))
    ax.plot([0, 0], [2.2, 0.2], color=MUT, lw=1.5, ls='--'); ax.add_patch(Arc((0, 2.2), 1.2, 1.2, theta1=270, theta2=270 + 25, color=YELLOW, lw=2.5)); ax.text(0.12, 1.2, '25°', color=YELLOW, fontsize=19)
    _note(fig, 0.05, 0.10, 'plates 5.00 cm apart, 400 V', 18)
    ax.text(0, -0.5, 'forces: not to scale', color=MUT, fontsize=16, ha='center')
    arrow(ax, (bx, by), (bx, by - 0.65), color=PINK, lw=4, ms=22); ax.text(bx + 0.08, by - 0.8, 'weight mg', color=PINK, fontsize=19)
    arrow(ax, (bx, by), (bx - 0.40 * np.sin(th) * 1.6, by + 0.40 * np.cos(th) * 1.6), color=YELLOW, lw=4, ms=22); ax.text(bx - 1.0, by + 0.95, 'tension', color=YELLOW, fontsize=19)
    arrow(ax, (bx, by), (bx + 0.30, by), color=GREEN, lw=4, ms=22); ax.text(bx + 0.02, by + 0.2, 'F_E', color=GREEN, fontsize=19, va='bottom')
    if s == 0:
        card(fig, 0.53, 0.52, 0.43, 0.27, 'Question', 'A 2.50 mg ball hangs between plates 5.00 cm\napart with 400 V across them, 25.0° from the\nvertical. Find the electric force, the charge and\nits sign.', tcol=C2, size=21)
        bullets(fig, ['Draw: weight, tension, ONE electric force', 'Equilibrium: forces form a closed triangle'], 2, 0.54, 0.46, size=22, gap=0.015, dim=False)
        return
    if s == 1:
        ax3 = wax(fig, [0.55, 0.40, 0.18, 0.35], (0, 1.2), (0, 1.8))
        ax3.add_patch(Polygon([[0.1, 0.1], [0.1, 1.5], [0.85, 0.1]], fc='none', ec=SOFT, lw=2))
        ax3.text(-0.1, 0.8, 'mg', color=PINK, fontsize=19, ha='center'); ax3.text(0.5, -0.05, 'F_E', color=GREEN, fontsize=19, ha='center'); ax3.text(0.62, 0.85, 'T', color=YELLOW, fontsize=19)
        ax3.add_patch(Arc((0.1, 1.5), 0.5, 0.5, theta1=-80, theta2=-65, color=YELLOW, lw=2))
        T(fig, 0.76, 0.74, r'$\tan\theta = \dfrac{F_E}{mg}$', size=26, color=YELLOW)
        T(fig, 0.55, 0.30, r'$mg = 2.50\times10^{-6}\times 9.81 = 2.4525\times10^{-5}\ \mathrm{N}$', size=22)
        T(fig, 0.55, 0.22, r'$F_E = mg\tan 25.0^\circ = 1.1437\times10^{-5}\ \mathrm{N}$  to the right', size=22)
        _sf(fig, 0.55, 0.15, '= 1.14 × 10⁻⁵ N (3 s.f.)')
        return
    _lines(fig, 0.54, 0.72, [(r'$E = \dfrac{V}{d} = \dfrac{400}{0.0500} = 8000\ \mathrm{N\,C^{-1}}$', FG)], size=24)
    T(fig, 0.54, 0.60, r'$q = \dfrac{F_E}{E} = \dfrac{1.1437\times10^{-5}}{8000} = 1.4296\times10^{-9}\ \mathrm{C}$', size=24)
    _sf(fig, 0.54, 0.50, '= 1.43 × 10⁻⁹ C (3 s.f.)')
    card(fig, 0.54, 0.22, 0.42, 0.22, 'Sign', 'Pulled towards the positive plate, so the ball\nis NEGATIVE: force opposite to the field.', tcol=GREEN, size=21)
    T(fig, 0.54, 0.16, 'tension: T = mg / cos 25.0° = 2.71 × 10⁻⁵ N', size=20, color=SOFT)


def we_coulomb(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: forces from two charges')
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.03, 0.12, 0.50, 0.66], (-0.2, 0.6), (-0.12, 0.62)); ax.set_aspect('equal')
    _q(ax, 0, 0, 1, r=0.035); _q(ax, 0.30, 0, -1, r=0.035); _q(ax, 0, 0.40, 1, r=0.035)
    ax.text(-0.06, 0, 'Q₁\n+5.0 μC', color=SOFT, fontsize=17, ha='right', va='center'); ax.text(0.30, -0.065, 'Q₂ −2.0 μC', color=SOFT, fontsize=17, ha='center')
    ax.text(0.04, 0.43, 'Q₃ +1.0 μC', color=SOFT, fontsize=17, va='bottom')
    ax.plot([0, 0.30], [0, 0], color=MUT, lw=1.5, ls=':'); ax.plot([0, 0], [0, 0.40], color=MUT, lw=1.5, ls=':'); ax.plot([0.30, 0], [0, 0.40], color=MUT, lw=1.5, ls=':')
    ax.text(0.15, 0.015, '0.30 m', color=MUT, fontsize=16, ha='center'); ax.text(-0.02, 0.2, '0.40 m', color=MUT, fontsize=16, ha='right', va='center')
    if s == 0:
        card(fig, 0.56, 0.50, 0.40, 0.27, 'Question', 'Q₁ = +5.0 μC at the origin, Q₂ = −2.0 μC\n0.30 m to its right. Find the force on Q₃ =\n+1.0 μC, 0.40 m directly above Q₁.', tcol=C2, size=21)
        bullets(fig, ['Force from each charge, separately', 'Add as VECTORS, not as plain numbers'], 2, 0.57, 0.43, size=23, gap=0.015, dim=False)
        return
    sc = 0.7
    F31, F32 = 0.28125, 0.072
    arrow(ax, (0, 0.4), (0, 0.4 + F31 * sc), color=GREEN, lw=4, ms=22)
    arrow(ax, (0, 0.4), (0.6 * F32 * sc, 0.4 - 0.8 * F32 * sc), color=YELLOW, lw=4, ms=22)
    ax.text(0.02, 0.4 + F31 * sc * 0.6, 'F₃₁ = 0.28125 N\n(repulsion)', color=GREEN, fontsize=18, va='center')
    ax.text(0.07, 0.34, 'F₃₂ = 0.0720 N\n(attraction)', color=YELLOW, fontsize=17, va='top')
    if s == 1:
        T(fig, 0.56, 0.76, r'$r_{32} = \sqrt{0.30^2 + 0.40^2} = 0.50\ \mathrm{m}$', size=24)
        T(fig, 0.56, 0.66, r'$F_{31} = \dfrac{9.00\times10^{9}(5.0\times10^{-6})(1.0\times10^{-6})}{0.40^2} = 0.28125\ \mathrm{N}$', size=22)
        T(fig, 0.56, 0.54, r'$F_{32} = \dfrac{9.00\times10^{9}(2.0\times10^{-6})(1.0\times10^{-6})}{0.50^2} = 0.0720\ \mathrm{N}$', size=22)
        T(fig, 0.56, 0.42, 'Draw both arrows from Q₃; the longer arrow\nfor the bigger force', size=21, color=SOFT)
        return
    arrow(ax, (0, 0.4), (0.6 * F32 * sc, 0.4), color=PINK, lw=2, ms=14, ls='--')
    T(fig, 0.56, 0.78, 'Split F₃₂ using the 3-4-5 triangle:', size=22, color=SOFT)
    T(fig, 0.56, 0.70, r'$F_x = 0.0720\times 0.6 = 0.0432\ \mathrm{N}$', size=24)
    T(fig, 0.56, 0.61, r'$F_y = 0.28125 - 0.0720\times 0.8 = 0.22365\ \mathrm{N}$', size=24)
    if s == 2:
        T(fig, 0.56, 0.50, 'Add the components for each direction,\nnot the magnitudes', size=22, color=SOFT)
        return
    T(fig, 0.56, 0.50, r'$F = \sqrt{0.0432^2 + 0.22365^2} = 0.22778\ \mathrm{N}$', size=24, color=FG)
    _sf(fig, 0.56, 0.43, '= 0.23 N (2 s.f.)')
    T(fig, 0.56, 0.35, r'$\theta = \tan^{-1}\!\dfrac{0.22365}{0.0432} = 79.07^\circ$ above the horizontal', size=23)
    _sf(fig, 0.56, 0.27, '= 79° (2 s.f.), about 11° from the vertical')
    T(fig, 0.56, 0.19, 'Check: close to the big upward force, tilted\ntowards Q₂. Sensible.', size=21, color=SOFT)


def field(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Electric field strength')
    ax = wax(fig, [0.04, 0.14, 0.44, 0.62], (-1.2, 1.2), (-1.0, 1.0)); ax.set_aspect('equal')
    _efield(ax, (-1.2, 1.2), (-1.0, 1.0), [(0, 0, 1)], nper=12, r0=0.17, mask_r=0.13, lw=2.2)
    _q(ax, 0, 0, 1, r=0.12, size=26)
    if s == 0:
        ax.scatter([0.75], [0.0], s=140, color=YELLOW, zorder=7, edgecolor=BG); ax.text(0.75, 0.13, '+q test', color=YELLOW, fontsize=18, ha='center')
        arrow(ax, (0.75, 0), (1.12, 0), color=GREEN, lw=4, ms=22); ax.text(1.12, -0.12, 'F', color=GREEN, fontsize=22, ha='center')
        eeq(fig, 0.54, 0.70, r'$E = \dfrac{F_E}{q}$', size=42)
        T(fig, 0.66, 0.69, '(the definition)', size=20, color=SOFT)
        bullets(fig, ['Field theory: charges make a field;\nthe field exerts the force', 'Units: N C⁻¹ (= V m⁻¹)', 'Direction: the way a positive charge\nwould be pushed'], 3, 0.54, 0.44, size=23, gap=0.02)
        return
    if s == 1:
        eeq(fig, 0.54, 0.70, r'$E = \dfrac{k_E\,q}{r^2}$', size=42)
        bullets(fig, ['Away from +, towards −', 'A sphere acts like a point charge\nat its centre', 'Force on any charge: F = qE\n(reversed for a negative charge)'], 3, 0.54, 0.48, size=22, gap=0.015)
        T(fig, 0.54, 0.27, r'balloon: $E = \dfrac{9.00\times10^{9}\times 25\times10^{-6}}{1.5^2}$', size=22)
        T(fig, 0.54, 0.17, r'$= 100\,000\ \mathrm{N\,C^{-1}}$ outward', size=22, color=YELLOW)
        _sf(fig, 0.54, 0.11, '= 1.0 × 10⁵ N C⁻¹ (2 s.f.)')
        return
    box(fig, 0.52, 0.52, 0.43, 0.27); box(fig, 0.52, 0.18, 0.43, 0.27)
    T(fig, 0.54, 0.77, 'Point charge', size=26, color=PINK, weight='bold'); T(fig, 0.54, 0.70, r'$E = \dfrac{k_E\,q}{r^2}$,  radial, falls as $1/r^2$', size=26)
    T(fig, 0.54, 0.43, 'Parallel plates', size=26, color=C1, weight='bold'); T(fig, 0.54, 0.36, r'$E = \dfrac{V}{d}$,  uniform between the plates', size=26)
    T(fig, 0.54, 0.26, 'A common error (2022): using the point-charge\nfield in a plates question', size=20, color=SOFT)


def field_sketch(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Sketching electric fields')
    chip(fig, 'Element 1 · sketches')
    if s == 0:
        for i, (q, nm) in enumerate([(1, 'positive: out'), (-1, 'negative: in')]):
            ax = wax(fig, [0.04 + i * 0.25, 0.20, 0.23, 0.50], (-1.1, 1.1), (-1.1, 1.1)); ax.set_aspect('equal')
            _efield(ax, (-1.1, 1.1), (-1.1, 1.1), [(0, 0, q)], nper=10, r0=0.2, mask_r=0.15, lw=2.4)
            _q(ax, 0, 0, q, r=0.14); T(fig, 0.04 + i * 0.25 + 0.115, 0.17, nm, size=20, color=SOFT, ha='center')
        bullets(fig, ['Start on +, end on − (or go off to ∞)', 'Never cross', 'Arrows: direction a + charge would move',
                      'Closer lines = stronger field'], 4, 0.54, 0.72, size=23, gap=0.025)
        return
    if s == 1:
        ax = wax(fig, [0.04, 0.12, 0.55, 0.62], (-1.8, 1.8), (-1.0, 1.0)); ax.set_aspect('equal')
        _efield(ax, (-1.8, 1.8), (-1.0, 1.0), [(-0.8, 0, 2), (0.8, 0, -1)], nper=18, r0=0.17, mask_r=0.13, lw=2.2, maxlen=60)
        _q(ax, -0.8, 0, 1, r=0.13); _q(ax, 0.8, 0, -1, r=0.13)
        ax.text(-0.8, 0.3, '+2q', color=PINK, fontsize=19, ha='center', bbox=dict(fc=BG, ec='none', pad=1.5)); ax.text(0.8, 0.3, '−q', color=C1, fontsize=19, ha='center', bbox=dict(fc=BG, ec='none', pad=1.5))
        bullets(fig, ['Unlike charges: lines leave + and\ncurve into −', 'Unequal charges: MORE lines from the\nbigger charge, and an asymmetric picture',
                      'Add arrows and avoid crossings'], 3, 0.62, 0.72, size=22, gap=0.02)
        return
    ax = wax(fig, [0.04, 0.12, 0.55, 0.62], (-1.8, 1.8), (-1.0, 1.0)); ax.set_aspect('equal')
    _efield(ax, (-1.8, 1.8), (-1.0, 1.0), [(-0.8, 0, 2), (0.8, 0, 1)], nper=16, r0=0.17, mask_r=0.13, lw=2.2, maxlen=60)
    _q(ax, -0.8, 0, 1, r=0.13); _q(ax, 0.8, 0, 1, r=0.13)
    nx = -0.8 + 1.6 * (np.sqrt(2) / (1 + np.sqrt(2)))
    ax.scatter([nx], [0], s=260, marker='X', color=YELLOW, zorder=8, edgecolor=BG); ax.text(nx, -0.22, 'neutral\npoint', color=YELLOW, fontsize=17, ha='center', va='top')
    bullets(fig, ['Like charges: lines push apart', 'Neutral point between them,\ncloser to the weaker charge', 'Far away: looks like one big charge',
                  'Point charges give radial lines,\nnot the circles of a wire'], 4, 0.62, 0.72, size=22, gap=0.02)


def we_field(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: total field from two charges')
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.03, 0.27, 0.50, 0.53], (-0.09, 0.09), (-0.03, 0.17)); ax.set_aspect('equal')
    A, B, P = (-0.05, 0.0), (0.05, 0.0), (0.0, 0.0866)
    _q(ax, *A, 1, r=0.007); _q(ax, *B, -1, r=0.007)
    ax.scatter([P[0]], [P[1]], s=120, color=YELLOW, zorder=7, edgecolor=BG); ax.text(0.003, 0.0925, 'P', color=YELLOW, fontsize=22)
    for u, v in [(A, B), (A, P), (B, P)]:
        ax.plot([u[0], v[0]], [u[1], v[1]], color=MUT, lw=1.5, ls=':')
    ax.text(-0.052, -0.012, 'A  +6.0 nC', color=SOFT, fontsize=17, ha='center'); ax.text(0.052, -0.012, 'B  −2.0 nC', color=SOFT, fontsize=17, ha='center')
    ax.text(0, 0.003, '0.10 m', color=MUT, fontsize=15, ha='center')
    EA, EB = 5400, 1800; k = 0.075 / 5400
    uA = np.array([0.5, 0.866]); uB = np.array([0.5, -0.866])
    if s == 0:
        card(fig, 0.56, 0.50, 0.40, 0.27, 'Question', 'A = +6.0 nC, B = −2.0 nC, 0.10 m apart. P is\n0.10 m from each. Find the magnitude and\ndirection of the total field at P.', tcol=C2, size=21)
        arrow(ax, P, (P[0] + EA * k * uA[0], P[1] + EA * k * uA[1]), color=PINK, lw=4, ms=22); ax.text(0.045, 0.145, 'E_A = 5400 N C⁻¹\naway from A', color=PINK, fontsize=17)
        arrow(ax, P, (P[0] + EB * k * uB[0], P[1] + EB * k * uB[1]), color=C1, lw=4, ms=22); ax.text(0.045, 0.045, 'E_B = 1800 N C⁻¹\ntowards B', color=C1, fontsize=17)
        T(fig, 0.56, 0.42, r'$E_A = \dfrac{9.00\times10^{9}\times 6.0\times10^{-9}}{0.10^2} = 5400$', size=22)
        T(fig, 0.56, 0.32, r'$E_B = \dfrac{9.00\times10^{9}\times 2.0\times10^{-9}}{0.10^2} = 1800$', size=22)
        return
    if s == 1:
        arrow(ax, P, (P[0] + EA * k * uA[0], P[1] + EA * k * uA[1]), color=PINK, lw=3, ms=18); arrow(ax, P, (P[0] + EB * k * uB[0], P[1] + EB * k * uB[1]), color=C1, lw=3, ms=18)
        tot = np.array([3600, 3117.7]) * k
        arrow(ax, P, (P[0] + tot[0], P[1] + tot[1]), color=GREEN, lw=5, ms=26); ax.text(0.04, 0.16, 'E total', color=GREEN, fontsize=19)
        T(fig, 0.56, 0.76, r'$E_x = 5400\times0.5 + 1800\times0.5 = 3600$', size=22)
        T(fig, 0.56, 0.67, r'$E_y = 5400\times0.866 - 1800\times0.866 = 3117.7$', size=22)
        T(fig, 0.56, 0.56, r'$E = \sqrt{3600^2 + 3117.7^2} = 4762.4\ \mathrm{N\,C^{-1}}$', size=24)
        _sf(fig, 0.56, 0.49, '= 4.8 × 10³ N C⁻¹ (2 s.f.)')
        T(fig, 0.56, 0.40, r'$\theta = \tan^{-1}\!\dfrac{3117.7}{3600} = 40.89^\circ$ above the line AB', size=22)
        _sf(fig, 0.56, 0.33, '= 41° (2 s.f.)')
        return
    ax2 = wax(fig, [0.55, 0.38, 0.42, 0.42], (-0.4, 6.0), (-2.6, 1.0)); ax2.set_aspect('equal')
    a = np.array([5.4, 0.0]); b = 1.8 * np.array([-0.5, -0.866])
    ax2.plot([0, a[0]], [0, a[1]], color=PINK, lw=3); ax2.plot([a[0], a[0] + b[0]], [a[1], a[1] + b[1]], color=C1, lw=3)
    arrow(ax2, (0, 0), (a[0] + b[0] - 0.05, a[1] + b[1] + 0.03), color=GREEN, lw=3.5, ms=20)
    ax2.text(2.7, 0.15, 'E_A', color=PINK, fontsize=18, ha='center'); ax2.text(5.35, -0.9, 'E_B', color=C1, fontsize=18, ha='right')
    ax2.add_patch(Arc((a[0], a[1]), 1.6, 1.6, theta1=180, theta2=240, color=YELLOW, lw=2)); ax2.text(4.5, -0.45, '60°', color=YELLOW, fontsize=18)
    ax2.text(2.5, -2.3, 'tip to tail: interior angle 60°', color=SOFT, fontsize=17, ha='center')
    T(fig, 0.05, 0.19, r'$E^2 = E_A^2 + E_B^2 - 2E_AE_B\cos 60^\circ \Rightarrow E = 4762.4$   (120° would wrongly give 6490)', size=22)
    T(fig, 0.05, 0.12, 'Draw the triangle, then read the angle off it. Components avoid the trap.', size=21, color=SOFT)
    T(fig, 0.56, 0.31, 'Force on −20 nC at P: F = qE,\nopposite to the field direction', size=21, color=SOFT)


def conductors(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Conductors, cages and sharp points')
    chip(fig, 'Element 1 · explain')
    if s == 0:
        ax = wax(fig, [0.03, 0.14, 0.52, 0.62], (-2.4, 2.4), (-1.3, 1.3)); ax.set_aspect('equal')
        for y in np.linspace(-1.0, 1.0, 6):
            arrow(ax, (-2.3, y), (-0.82, y), color=C1, lw=2.2, ms=16); arrow(ax, (0.82, y), (2.3, y), color=C1, lw=2.2, ms=16)
        ax.add_patch(Rectangle((-0.8, -0.8), 1.6, 1.6, fc=PANEL2, ec=YELLOW, lw=5, zorder=4))
        for y in np.linspace(-0.6, 0.6, 5):
            ax.text(-0.8, y, '−', color=C1, fontsize=24, ha='center', va='center', weight='bold', zorder=6)
            ax.text(0.8, y, '+', color=PINK, fontsize=24, ha='center', va='center', weight='bold', zorder=6)
        ax.text(0, 0, 'E = 0\ninside', color=GREEN, fontsize=26, ha='center', va='center', weight='bold', zorder=6)
        ax.text(0, -1.22, 'closed metal box (Faraday cage)', color=SOFT, fontsize=19, ha='center')
        bullets(fig, ['Free charges rearrange on the outside\nuntil the field inside is zero', 'Whole conductor at one potential:\nΔV = 0 inside, so E = V/d = 0',
                      'No field, so no force on a charge inside\n(an ion in a metal chamber just drifts)'], 3, 0.58, 0.72, size=22, gap=0.025)
        return
    if s == 1:
        ax = wax(fig, [0.03, 0.14, 0.52, 0.62], (-2.4, 2.4), (-1.3, 1.3)); ax.set_aspect('equal')
        th = np.linspace(0, TAU, 200)
        xs = np.where(np.cos(th) > 0, 1.6 * np.cos(th) ** 3 + 0.0, 1.0 * np.cos(th)); ys = 0.8 * np.sin(th) * (1 - 0.55 * np.maximum(np.cos(th), 0) ** 2)
        ax.fill(xs - 0.4, ys, fc=PANEL2, ec=YELLOW, lw=4, zorder=3)
        for a in np.linspace(-0.9, 0.9, 11):
            r0 = 1.0 + 0.0
            x = 1.15 + 0.2 * (1 - abs(a)) ; y = 0.18 * a
            ax.text(x, y, '+', color=PINK, fontsize=17, ha='center', va='center', zorder=6)
        for a in np.linspace(-2.4, 2.4, 5):
            ax.text(-0.4 + 0.95 * np.cos(2.4 + a * 0.55), 0.7 * np.sin(2.4 + a * 0.55), '+', color=PINK, fontsize=15, ha='center', va='center', zorder=6)
        for a in np.linspace(-0.55, 0.55, 12):
            arrow(ax, (1.3, 0.15 * a), (1.3 + 0.95 * np.cos(a), 0.15 * a + 0.95 * np.sin(a) * 1.0), color=C1, lw=2, ms=13)
        ax.text(2.0, -0.95, 'crowded lines:\nstrongest field', color=GREEN, fontsize=19, ha='center')
        ax.text(-0.4, -1.1, 'charge crowds onto the sharpest point', color=SOFT, fontsize=19, ha='center')
        bullets(fig, ['Air breaks down at about\n3 × 10⁶ V m⁻¹', 'Strongest field at the point: sparks and\nlightning start there', 'Hair standing up: charge on the head,\nstrong local field, strike more likely'], 3, 0.58, 0.72, size=22, gap=0.025)
        return
    ax = wax(fig, [0.03, 0.14, 0.55, 0.62], (-2.2, 2.4), (-1.3, 1.3)); ax.set_aspect('equal')
    _efield(ax, (-2.2, 2.4), (-1.3, 1.3), [(-1.0, 0, 3), (1.15, 0, -1.2)], nper=22, r0=0.25, mask_r=0.2, lw=1.8, maxlen=80, arrows=1.2)
    ax.add_patch(Circle((-1.0, 0), 0.7, fc=PANEL2, ec=YELLOW, lw=4, zorder=5)); ax.add_patch(Circle((1.15, 0), 0.4, fc=PANEL2, ec=YELLOW, lw=4, zorder=5))
    for a in np.linspace(0, TAU, 9)[:-1]:
        ax.text(-1.0 + 0.55 * np.cos(a), 0.55 * np.sin(a), '+', color=PINK, fontsize=17, ha='center', va='center', zorder=7)
    for a in np.linspace(-1.0, 1.0, 5):
        ax.text(1.15 + 0.27 * np.cos(np.pi + a), 0.27 * np.sin(np.pi + a), '−', color=C1, fontsize=18, ha='center', va='center', zorder=7, weight='bold')
    ax.text(-1.0, -0.9, 'dome', color=SOFT, fontsize=19, ha='center'); ax.text(1.15, -0.6, 'earthed\nsphere', color=SOFT, fontsize=19, ha='center')
    _note(fig, 0.03, 0.11, 'sketch idea only: induced charge crowds the lines across the gap')
    eq(fig, 0.62, 0.70, r'$V = Ed = 3.0\times10^{6}\times0.020$', size=24)
    T(fig, 0.62, 0.60, r'$= 6.0\times10^{4}\ \mathrm{V}$', size=26, color=YELLOW)
    bullets(fig, ['Nearby sphere: opposite charge is\ninduced on the near side', 'Lines are squeezed across the gap,\nso the field there exceeds breakdown', 'Sketch: crowded lines, induced charges,\nlines on the far side too'], 3, 0.62, 0.52, size=21, gap=0.02)


def potential(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Potential difference')
    if s == 0:
        ax = wax(fig, [0.03, 0.14, 0.45, 0.62], (-1.5, 2.2), (-0.2, 3.0)); ax.set_aspect('equal')
        _plates(ax, -1.2, 1.8, 2.6, 0.2); _unif(ax, -1.2, 1.8, 2.6, 0.2, n=5)
        ax.scatter([0.3], [0.6], s=200, color=PINK, zorder=7, edgecolor=BG); ax.text(0.3, 0.6, '+', color=BG, fontsize=18, ha='center', va='center', zorder=8, weight='bold')
        ax.scatter([0.3], [2.1], s=200, color=PINK, zorder=7, edgecolor=BG); ax.text(0.3, 2.1, '+', color=BG, fontsize=18, ha='center', va='center', zorder=8, weight='bold')
        arrow(ax, (0.6, 0.7), (0.6, 2.0), color=YELLOW, lw=4, ms=22); ax.text(0.75, 1.35, 'work done\nagainst field', color=YELLOW, fontsize=17)
        eeq(fig, 0.56, 0.72, r'$V = \dfrac{\Delta E_p}{q}$', size=44)
        bullets(fig, ['Pushed towards the + plate: gains\npotential energy', 'Released: it becomes kinetic energy', '1 V = 1 J C⁻¹'], 3, 0.56, 0.50, size=23, gap=0.02)
        return
    if s == 1:
        ax = wax(fig, [0.03, 0.14, 0.50, 0.62], (-1.5, 2.6), (-0.2, 3.0)); ax.set_aspect('equal')
        _plates(ax, -1.2, 2.2, 2.6, 0.2); _unif(ax, -1.2, 2.2, 2.6, 0.2, n=6)
        for k, v in enumerate([285, 214, 142, 71, 0]):
            y = 2.6 - k * 0.6; ax.plot([-1.2, 2.2], [y, y], color=MUT, lw=1.2, ls=':'); ax.text(2.3, y, f'{v} V', color=SOFT, fontsize=17, va='center')
        ax.annotate('', xy=(-1.0, 0.2), xytext=(-1.0, 2.6), arrowprops=dict(arrowstyle='<->', color=YELLOW, lw=2)); ax.text(-0.9, 1.4, 'd = 5.00 mm', color=YELLOW, fontsize=17, ha='left', va='center', bbox=dict(fc=BG, ec='none', pad=2))
        eeq(fig, 0.58, 0.70, r'$E = \dfrac{V}{d}$', size=44)
        T(fig, 0.58, 0.53, r'$E = \dfrac{285}{5.00\times10^{-3}} = 5.70\times10^{4}\ \mathrm{V\,m^{-1}}$', size=22)
        bullets(fig, ['Uniform field: same everywhere', '+ plate to − plate', 'd in metres'], 3, 0.58, 0.42, size=22, gap=0.015)
        return
    ax = wax(fig, [0.03, 0.30, 0.94, 0.42], (0, 12), (-1.6, 1.6))
    ax.plot([0.5, 0.5], [-0.9, 0.9], color=C1, lw=8); ax.text(0.5, 1.1, 'cathode −', color=C1, fontsize=19, ha='center')
    ax.plot([5.0, 5.0], [0.35, 0.9], color=PINK, lw=8); ax.plot([5.0, 5.0], [-0.9, -0.35], color=PINK, lw=8); ax.text(5.0, 1.1, 'anode +', color=PINK, fontsize=19, ha='center')
    for x, a in [(1.2, 0.0), (2.6, 0.0), (4.1, 0.0), (7.0, 0.0), (9.5, 0.0)]:
        ax.scatter([x], [0], s=120, color=C1, zorder=6, edgecolor=BG)
    for x, l in [(1.2, 0.4), (2.6, 0.9), (4.1, 1.4)]:
        arrow(ax, (x + 0.2, 0.0), (x + 0.2 + l, 0.0), color=GREEN, lw=3, ms=16)
    arrow(ax, (7.2, 0.0), (9.0, 0.0), color=GREEN, lw=4, ms=20); arrow(ax, (9.7, 0.0), (11.5, 0.0), color=GREEN, lw=4, ms=20)
    ax.text(8.3, -0.55, 'constant speed: no field', color=SOFT, fontsize=18, ha='center'); ax.text(2.7, -0.55, 'speeds up in the field', color=SOFT, fontsize=18, ha='center')
    ax.annotate('', xy=(5.0, -1.3), xytext=(0.5, -1.3), arrowprops=dict(arrowstyle='<->', color=YELLOW, lw=2)); ax.text(2.7, -1.5, 'V', color=YELLOW, fontsize=22, ha='center')
    learn_eq(fig, 0.05, 0.22, r'$qV = \frac{1}{2}mv^2$', size=40)
    bullets(fig, ['State: electric potential energy becomes kinetic', 'Use the particle’s own q and m (two e for a doubly charged ion)', 'Valid only if v is well below c'], 3, 0.40, 0.25, size=21, gap=0.012)


def _gunfig(fig, stage, rect=(0.03, 0.40, 0.94, 0.40)):
    C1, C2 = C()
    ax = wax(fig, list(rect), (0, 12.4), (-2.3, 2.5))
    ax.plot([0.4, 0.4], [-0.8, 0.8], color=C1, lw=7); ax.text(0.4, 1.0, '−', color=C1, fontsize=26, ha='center', weight='bold')
    ax.plot([2.6, 2.6], [0.3, 0.8], color=PINK, lw=7); ax.plot([2.6, 2.6], [-0.8, -0.3], color=PINK, lw=7); ax.text(2.6, 1.0, '+', color=PINK, fontsize=26, ha='center', weight='bold')
    ax.annotate('', xy=(2.6, -1.25), xytext=(0.4, -1.25), arrowprops=dict(arrowstyle='<->', color=YELLOW, lw=2)); ax.text(1.5, -1.65, '1.50 kV', color=YELLOW, fontsize=19, ha='center')
    ax.plot([4.8, 8.8], [1.1, 1.1], color=PINK, lw=7); ax.plot([4.8, 8.8], [-1.1, -1.1], color=C1, lw=7)
    ax.text(4.55, 1.1, '+', color=PINK, fontsize=24, ha='center', va='center', weight='bold'); ax.text(4.55, -1.1, '−', color=C1, fontsize=24, ha='center', va='center', weight='bold')
    ax.text(6.8, -1.65, '4.00 cm long, 2.00 cm apart, 300 V', color=SOFT, fontsize=18, ha='center')
    ax.plot([0.4, 4.8], [0, 0], color=GREEN, lw=3)
    xx = np.linspace(4.8, 8.8, 40); yy = 0.05 * (xx - 4.8) ** 2
    if stage == 4:
        ax.plot([4.8, 12.2], [0, 0], color=GREEN, lw=3, ls='--', zorder=4)
        ax.plot([4.8, 8.8], [0, 0], color=GREEN, lw=3)
        _symgrid(ax, [5.6, 6.8, 8.0], [-0.55, 0.55], False, size=220)
    else:
        ax.plot(xx, yy, color=GREEN, lw=3); ax.plot([8.8, 12.2], [0.8, 0.8 + 0.4 * 3.4], color=GREEN, lw=3, ls='--')
    ax.scatter([0.4], [0], s=140, color=C1, zorder=6, edgecolor=BG)
    if stage >= 2:
        if stage != 4:
            for x in (5.6, 6.8, 8.0):
                arrow(ax, (x, 1.0), (x, -1.0), color=C1, lw=1.8, ms=12)
        ax.text(9.0, 0.35, 'E ↓', color=C1, fontsize=20) if stage != 4 else None
        arrow(ax, (6.8, 0.0 if stage == 4 else 0.05 * 4), (6.8, 0.9 if stage == 4 else 0.05 * 4 + 0.7), color=GREEN, lw=4, ms=20)
        ax.text(7.05, 0.65, 'F_E', color=GREEN, fontsize=19)
    if stage == 4:
        arrow(ax, (6.8, 0.0), (6.8, -0.9), color=YELLOW, lw=4, ms=20); ax.text(7.05, -0.6, 'F_B', color=YELLOW, fontsize=19)
        ax.text(10.5, 1.2, 'B into the page', color=SOFT, fontsize=19, ha='center')
    return ax


def we_gun(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: an electron beam through plates')
    chip(fig, 'Element 2 · problems')
    ax = _gunfig(fig, s, (0.03, 0.40, 0.94, 0.38))
    if s == 0:
        card(fig, 0.05, 0.05, 0.62, 0.29, 'Question', 'An electron is accelerated from rest through 1.50 kV, then\nenters plates 4.00 cm long and 2.00 cm apart with 300 V\nacross them. Find its entry speed, its deflection angle, and\nthe B field that cancels the deflection.', tcol=C2, size=21)
        return
    if s == 1:
        T(fig, 0.05, 0.34, r'$qV = \frac{1}{2}mv^2 \Rightarrow v = \sqrt{\dfrac{2qV}{m}} = \sqrt{\dfrac{2(1.60\times10^{-19})(1500)}{9.11\times10^{-31}}}$', size=24)
        T(fig, 0.05, 0.24, r'$v = 2.2954\times10^{7}\ \mathrm{m\,s^{-1}}$', size=26, color=YELLOW)
        _sf(fig, 0.05, 0.17, '= 2.30 × 10⁷ m s⁻¹ (3 s.f.)')
        T(fig, 0.55, 0.24, 'Valid? v/c = 0.077: under 8% of the speed\nof light, so Newtonian physics is fine.', size=21, color=SOFT)
        return
    if s == 2:
        T(fig, 0.05, 0.34, r'$E = \dfrac{V}{d} = \dfrac{300}{0.0200} = 1.50\times10^{4}\ \mathrm{N\,C^{-1}}$  (downwards: + to −)', size=24)
        T(fig, 0.05, 0.25, r'$a = \dfrac{eE}{m} = \dfrac{(1.60\times10^{-19})(1.50\times10^{4})}{9.11\times10^{-31}} = 2.6345\times10^{15}\ \mathrm{m\,s^{-2}}$', size=24)
        _sf(fig, 0.05, 0.18, '= 2.63 × 10¹⁵ m s⁻² (3 s.f.), upwards: the force is opposite to E for an electron')
        return
    if s == 3:
        ax3 = wax(fig, [0.62, 0.08, 0.30, 0.26], (0, 5.5), (0, 2.2))
        ax3.plot([0.2, 5.0], [0.2, 0.2], color=GREEN, lw=3); arrow(ax3, (5.0, 0.2), (5.0, 1.0), color=PINK, lw=3, ms=16); arrow(ax3, (0.2, 0.2), (4.95, 0.98), color=YELLOW, lw=3, ms=18)
        ax3.text(2.6, 0.0, 'vₓ = 2.2954 × 10⁷', color=GREEN, fontsize=15, ha='center'); ax3.text(5.15, 0.6, 'v_y', color=PINK, fontsize=17)
        ax3.add_patch(Arc((0.2, 0.2), 1.6, 1.0, theta1=0, theta2=9, color=YELLOW, lw=2)); ax3.text(1.4, 0.35, 'θ', color=YELLOW, fontsize=17)
        T(fig, 0.05, 0.34, r'$t = \dfrac{0.0400}{2.2954\times10^{7}} = 1.7426\times10^{-9}\ \mathrm{s}$,  $v_y = at = 4.5908\times10^{6}\ \mathrm{m\,s^{-1}}$', size=22)
        _sf(fig, 0.05, 0.27, '= 1.74 × 10⁻⁹ s,  4.59 × 10⁶ m s⁻¹ (3 s.f.)')
        T(fig, 0.05, 0.20, r'$\theta = \tan^{-1}\dfrac{v_y}{v_x} = 11.31^\circ$', size=24); _sf(fig, 0.05, 0.13, '= 11.3° (3 s.f.)')
        T(fig, 0.30, 0.20, r'shift $\frac{1}{2}at^2 = 4.00\ \mathrm{mm} < 10\ \mathrm{mm}$: it escapes', size=22, color=SOFT)
        return
    T(fig, 0.05, 0.34, r'$qvB = qE \Rightarrow B = \dfrac{E}{v} = \dfrac{1.50\times10^{4}}{2.2954\times10^{7}} = 6.5348\times10^{-4}\ \mathrm{T}$', size=24)
    _sf(fig, 0.05, 0.27, '= 6.53 × 10⁻⁴ T (3 s.f.), using the full speed')
    T(fig, 0.05, 0.19, 'F_E is up, so F_B must be DOWN. Electron moving right, force down:\nB is into the page (reverse of the rule for a positive charge).', size=21, color=SOFT)


def _trajectory_plates(fig, kind, ph):
    C1, C2 = C()
    ax = wax(fig, [0.03, 0.12, 0.60, 0.66], (0, 10), (-2.6, 2.6))
    if kind == 'along':
        ax.plot([1.0, 1.0], [-1.0, 1.0], color=PINK, lw=8); ax.plot([6.0, 6.0], [0.35, 1.0], color=C1, lw=8); ax.plot([6.0, 6.0], [-1.0, -0.35], color=C1, lw=8)
        ax.text(1.0, 1.15, '+', color=PINK, fontsize=24, ha='center', weight='bold'); ax.text(6.0, 1.15, '−', color=C1, fontsize=24, ha='center', weight='bold')
        for y in (-0.7, 0, 0.7):
            arrow(ax, (1.2, y), (5.6, y), color=MUT, lw=1.5, ms=12)
        t = ph
        x = 1.4 + 4.6 * t ** 2 if t < 1 else 6.0
        ax.scatter([x], [0.0], s=170, color=PINK, zorder=6, edgecolor=BG); ax.text(x, 0.0, '+', color=BG, fontsize=15, ha='center', va='center', zorder=7, weight='bold')
        arrow(ax, (x, -0.45), (x + 0.4 + 1.5 * t, -0.45), color=GREEN, lw=3, ms=16)
        ax.text(3.5, 1.6, 'constant force: constant acceleration  a = qE/m', color=SOFT, fontsize=21, ha='center')
        ax.text(8.3, 0.0, 'beyond the plate:\nno field, constant speed', color=SOFT, fontsize=19, ha='center')
        return
    _plates(ax, 1.5, 8.5, 1.5, -1.5, '+', '−'); _unif(ax, 1.5, 8.5, 1.5, -1.5, n=6, color=MUT)
    if kind == 'perp':
        x = 1.5 + 7.0 * ph; y = -0.9 * ((x - 1.5) / 7.0) ** 2 * 1.0
        xs = np.linspace(1.5, 8.5, 60); ys = -1.0 * ((xs - 1.5) / 7.0) ** 2
        ax.plot(xs, ys, color=GREEN, lw=2.5, ls=':'); ax.plot([0.3, 1.5], [0, 0], color=GREEN, lw=2.5)
        y = -1.0 * ((x - 1.5) / 7.0) ** 2
        ax.scatter([x], [y], s=170, color=PINK, zorder=6, edgecolor=BG); ax.text(x, y, '+', color=BG, fontsize=15, ha='center', va='center', zorder=7, weight='bold')
        ax.text(5.0, 2.05, 'horizontal: constant speed   vertical: constant acceleration → parabola', color=SOFT, fontsize=19, ha='center')
        ax.text(5.0, -2.35, 'time links the two directions', color=SOFT, fontsize=19, ha='center')
        return
    xs = np.linspace(1.5, 8.5, 80); ys = 0.9 * (xs - 1.5) / 3.5 - 0.55 * ((xs - 1.5) / 3.5) ** 2 * 0.5 * 2
    ys = 0.8 * (xs - 1.5) - 0.12 * (xs - 1.5) ** 2
    ys = np.clip(ys, -1.45, 1.45)
    x = 1.5 + 7.0 * ph; y = float(np.clip(0.8 * (x - 1.5) - 0.12 * (x - 1.5) ** 2, -1.45, 1.45))
    ax.plot(xs, ys, color=GREEN, lw=2.5, ls=':')
    ax.scatter([x], [y], s=170, color=PINK, zorder=6, edgecolor=BG); ax.text(x, y, '+', color=BG, fontsize=15, ha='center', va='center', zorder=7, weight='bold')
    arrow(ax, (1.5, 0), (2.3, 0.6), color=YELLOW, lw=3, ms=16); arrow(ax, (1.5, 0), (2.5, 0), color=GREEN, lw=2, ms=12); arrow(ax, (1.5, 0), (1.5, 0.6), color=PINK, lw=2, ms=12)
    ax.text(5.0, 2.05, 'split v: along the field (accelerates) and across it (constant)', color=SOFT, fontsize=19, ha='center')
    ax.text(5.0, -2.35, 'check: does it hit a plate before it gets there?', color=SOFT, fontsize=19, ha='center')


def plates(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Charges in uniform electric fields')
    chip(fig, 'Element 2 · problems')
    _trajectory_plates(fig, ['along', 'perp', 'angle'][s], ph)
    items = [['Along the field: use a = qE/m with\nthe equations of motion', '+ speeds up along E,\n− the opposite way', 'After the anode hole the field\nis very weak: it coasts'],
             ['Across the field: horizontal speed\nconstant, vertical from zero', 'Handle the directions separately,\nlinked by time', 'Alpha: q = 2e, m = 6.64 × 10⁻²⁷ kg;\nstops when it strikes a plate'],
             ['Split the velocity into parts\nalong and across the field', 'Along: constant acceleration\nAcross: constant speed', 'Always give the field direction']][s]
    bullets(fig, items, 3, 0.65, 0.74, size=21, gap=0.025)


def tof(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Ions in a drift tube')
    ax = wax(fig, [0.03, 0.46, 0.94, 0.30], (0, 12.4), (-1.6, 1.8))
    ax.plot([1.6, 1.6], [0.3, 1.2], color=PINK, lw=7); ax.plot([1.6, 1.6], [-1.2, -0.3], color=PINK, lw=7)
    ax.plot([2.8, 2.8], [0.3, 1.2], color=C1, lw=7); ax.plot([2.8, 2.8], [-1.2, -0.3], color=C1, lw=7)
    ax.text(1.6, 1.4, 'A +', color=PINK, fontsize=19, ha='center'); ax.text(2.8, 1.4, 'B −', color=C1, fontsize=19, ha='center')
    ax.add_patch(Rectangle((3.4, -0.5), 8.4, 1.0, fc=PANEL2, ec=YELLOW, lw=4)); ax.text(7.6, 0.0, 'metal drift tube: no field inside', color=YELLOW, fontsize=19, ha='center', va='center')
    ax.scatter([0.5, 1.0], [0, 0], s=110, color=PINK, zorder=6); arrow(ax, (1.1, 0.0), (1.55, 0.0), color=GREEN, lw=3, ms=16)
    ax.text(0.7, -0.8, 'ions in', color=SOFT, fontsize=17, ha='center')
    ax.annotate('', xy=(3.4, -1.3), xytext=(3.4 + 8.4, -1.3), arrowprops=dict(arrowstyle='<->', color=SOFT, lw=2)); ax.text(7.6, -1.55, 'L = 0.800 m', color=SOFT, fontsize=18, ha='center')
    if s == 0:
        chip(fig, 'Element 1 · explain')
        bullets(fig, ['Between A and B: a potential difference, so an\nelectric field, so a force: the ions accelerate', 'Each ion gains kinetic energy qV',
                      'In the tube: NO potential difference, so no field,\nso no force: constant speed', 'Write about the field and the PD, not just\n“attraction and repulsion”'],
                4, 0.05, 0.40, size=22, gap=0.016)
        return
    chip(fig, 'Element 2 · problems')
    T(fig, 0.05, 0.40, r'$v = \dfrac{L}{t} = \dfrac{0.800}{1.55\times10^{-5}} = 5.1613\times10^{4}\ \mathrm{m\,s^{-1}}$', size=24); _sf(fig, 0.58, 0.40, '= 5.16 × 10⁴ m s⁻¹ (3 s.f.)')
    T(fig, 0.05, 0.31, r'$E_K = qV = (1.60\times10^{-19})(5.00\times10^{2}) = 8.00\times10^{-17}\ \mathrm{J}$', size=24)
    T(fig, 0.05, 0.22, r'$m = \dfrac{2E_K}{v^2} = \dfrac{2(8.00\times10^{-17})}{(5.1613\times10^{4})^2} = 6.006\times10^{-26}\ \mathrm{kg}$', size=24)
    _sf(fig, 0.05, 0.15, '= 6.01 × 10⁻²⁶ kg (3 s.f.)')
    T(fig, 0.50, 0.15, 'Watch: the square on v, and the factor of 2.', size=21, color=SOFT)


def millikan(fig, s, ph):
    C1, C2 = C()
    header(fig, "Millikan’s oil drop experiment")
    if s == 0:
        chip(fig, 'Element 1 · explain')
        ax = wax(fig, [0.03, 0.14, 0.45, 0.62], (-2, 2), (-2.2, 2.2)); ax.set_aspect('equal')
        _plates(ax, -1.5, 1.5, 1.8, -1.8, '+', '−'); _unif(ax, -1.5, 1.5, 1.8, -1.8, n=5, color=MUT)
        ax.scatter([0], [0], s=420, color=C1, zorder=6, edgecolor=BG)
        arrow(ax, (0, 0.3), (0, 1.2), color=GREEN, lw=5, ms=24); ax.text(0.2, 0.9, 'qE', color=GREEN, fontsize=22)
        arrow(ax, (0, -0.3), (0, -1.2), color=PINK, lw=5, ms=24); ax.text(0.2, -0.95, 'mg', color=PINK, fontsize=22)
        T(fig, 0.54, 0.72, 'Drop held still:  qE = mg', size=30, color=YELLOW, weight='bold')
        T(fig, 0.54, 0.62, r'$q = \dfrac{mg}{E},\qquad E = \dfrac{V}{d}$', size=30)
        bullets(fig, ['Negative drop held up: top plate positive', 'Plates, so E = V/d, not the point-charge field'], 2, 0.54, 0.46, size=22, gap=0.02)
        return
    chip(fig, 'Element 3 · data')
    rows = [['Ball', 'm (kg)', 'V (V)', 'E = V/d (N C⁻¹)', 'q = mg/E (C)']]
    rows += [['1', '4.90 × 10⁻¹⁶', '90.0', '15 000', '3.20 × 10⁻¹⁹'], ['2', '3.30 × 10⁻¹⁶', '120', '20 000', '1.62 × 10⁻¹⁹'], ['3', '6.10 × 10⁻¹⁶', '75.0', '12 500', '4.79 × 10⁻¹⁹']]
    cw = [0.07, 0.19, 0.11, 0.22, 0.22]
    if s == 2:
        rows[0].append('q / e'); cw = [0.06, 0.16, 0.09, 0.19, 0.19, 0.12]
        for i, v in enumerate(['2.00', '1.01', '2.99']):
            rows[i + 1].append(v)
    _tablegrid(fig, 0.05, 0.74, cw, 0.11, rows, size=21 if s == 2 else 22)
    T(fig, 0.05, 0.82, 'Plates 6.00 mm apart, g = 9.81 m s⁻²', size=20, color=MUT)
    if s == 1:
        T(fig, 0.05, 0.22, r'$E = \dfrac{V}{d} = \dfrac{90.0}{6.00\times10^{-3}} = 15\,000$,   $q = \dfrac{(4.90\times10^{-16})(9.81)}{15\,000} = 3.2046\times10^{-19}\ \mathrm{C}$', size=21)
        _sf(fig, 0.05, 0.14, '= 3.20 × 10⁻¹⁹ C (3 s.f.) for ball 1, and the same method for balls 2 and 3')
        return
    card(fig, 0.05, 0.10, 0.88, 0.18, 'Conclusion', 'Each q is close to a whole number of e (2, 1, 3): charge comes in whole-number multiples of a smallest unit.\nDivide each by its multiple and average: about 1.61 × 10⁻¹⁹ C. A bare “yes” earns nothing: say integer multiples.', tcol=GREEN, size=19)


def coulomb_graph(fig, s, ph):
    C1, C2 = C()
    header(fig, "Data: testing Coulomb’s law")
    chip(fig, 'Element 3 · data')
    r = np.array([2.0, 3.0, 4.0, 5.0]); F = np.array([9.0, 4.0, 2.25, 1.44])
    if s == 0:
        rows = [['r (cm)', 'F (mN)', 'r (m)', '1/r² (m⁻²)']]
        for a, b in zip(r, F):
            rows.append([f'{a:.1f}', f'{b:.2f}', f'{a / 100:.3f}', f'{1 / (a / 100) ** 2:,.0f}'.replace(',', ' ')])
        _tablegrid(fig, 0.05, 0.76, [0.11, 0.11, 0.11, 0.14], 0.095, rows, size=22)
        ax = gax(fig, [0.58, 0.22, 0.37, 0.50], (0, 6), (0, 10), 'r (cm)', 'F (mN)')
        rr = np.linspace(1.6, 5.6, 100); ax.plot(rr, 36 / rr ** 2, color=YELLOW, lw=2.5); _graph_pts(ax, r, F)
        ax.text(3.5, 7.5, 'a curve: not useful\nfor reading a value', color=SOFT, fontsize=18)
        T(fig, 0.05, 0.24, 'F = kQ² × (1/r²):   plot F against 1/r²', size=25, color=YELLOW, weight='bold')
        T(fig, 0.05, 0.16, 'Convert cm to m first. Straight line through the origin,\ngradient = kQ².', size=21, color=SOFT)
        return
    ax = gax(fig, [0.07, 0.20, 0.50, 0.55], (0, 3000), (0, 11), '1/r² (m⁻²)', 'F (mN)')
    x = 1 / (r / 100) ** 2; ax.plot([0, 2700], [0, 9.72], color=C1, lw=2.5); _graph_pts(ax, x, F)
    ax.plot([400, 2500, 2500], [1.44, 1.44, 9.0], color=GREEN, lw=2, ls='--'); ax.text(1450, 0.7, '2100', color=GREEN, fontsize=17, ha='center'); ax.text(2570, 5.2, '7.56', color=GREEN, fontsize=17)
    T(fig, 0.60, 0.74, r'gradient $= kQ^2 = \dfrac{(9.0-1.44)\times10^{-3}}{2500-400}$', size=23)
    T(fig, 0.60, 0.62, r'$= 3.6\times10^{-6}\ \mathrm{N\,m^2}$', size=26, color=YELLOW)
    T(fig, 0.60, 0.50, r'$Q = \sqrt{\dfrac{3.6\times10^{-6}}{9.00\times10^{9}}} = 2.0\times10^{-8}\ \mathrm{C}$', size=24)
    bullets(fig, ['Label axes with units', 'Best-fit line', 'Gradient from points far apart'], 3, 0.60, 0.38, size=21, gap=0.012)
    _note(fig, 0.07, 0.10, 'made-up data for practice, not from TASC')


def step_voltage(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Data: potential near a fallen power line')
    chip(fig, 'Element 3 · data')
    ax = gax(fig, [0.07, 0.18, 0.52, 0.58], (0, 10), (0, 4200), 'distance from the cable (m)', 'potential (V)')
    r = np.linspace(0.95, 10, 200); ax.plot(r, 4000 / r, color=YELLOW, lw=3)
    ax.set_yticks([0, 1000, 2000, 3000, 4000])
    for c0 in (2.0, 8.0):
        a, b = c0 - 0.4, c0 + 0.4
        ax.plot([a, b], [4000 / a, 4000 / b], color=GREEN, lw=3); _graph_pts(ax, [a, b], [4000 / a, 4000 / b], c=PINK, s=70)
    ax.annotate('feet at 1.6 m and 2.4 m\n2500 V and 1667 V:\nΔV = 833 V', xy=(2.4, 1667), xytext=(3.4, 2600), color=GREEN, fontsize=18, arrowprops=dict(arrowstyle='->', color=GREEN))
    ax.annotate('feet at 7.6 m and 8.4 m\nΔV = 50 V', xy=(8.0, 500), xytext=(6.0, 1400), color=GREEN, fontsize=18, arrowprops=dict(arrowstyle='->', color=GREEN))
    _note(fig, 0.07, 0.10, 'illustrative curve V = 4000 / r, not real measurements')
    if s == 0:
        bullets(fig, ['What matters is the DIFFERENCE between the\npotentials at the two feet', 'Reading the curve at the feet gives\nthe wrong quantity', 'Near the cable the curve is steep'], 3, 0.62, 0.74, size=21, gap=0.025)
        T(fig, 0.62, 0.40, 'Stride 0.80 m, centred at 2.0 m: 830 V\nStride 0.80 m, centred at 8.0 m: 50 V', size=21, color=YELLOW)
        return
    T(fig, 0.62, 0.74, r'$I = \dfrac{V}{R}$,   $R = 1.0\times10^{3}\ \Omega$', size=26)
    T(fig, 0.62, 0.64, r'near: $I = \dfrac{833}{1000} = 0.83\ \mathrm{A}$', size=24, color=PINK); T(fig, 0.62, 0.55, r'far: $I = \dfrac{50.1}{1000} = 0.050\ \mathrm{A}$', size=24, color=GREEN)
    card(fig, 0.62, 0.20, 0.33, 0.26, 'Safety advice', 'Shuffle away with small steps, feet\ntogether, so the potential difference\nbetween them stays small.', tcol=GREEN, size=19)


# ============================================================================ part 2: magnetic fields
def _dipole_lines(ax, R=1.0, Ls=(1.6, 2.1, 2.7, 3.4), arrows=True, color=None, lw=2.2):
    """Field lines of a dipole with its axis vertical; they leave the bottom and enter at the top."""
    color = color or C()[1]
    for L_ in Ls:
        th = np.linspace(0.12, np.pi - 0.12, 200); r = L_ * np.sin(th) ** 2
        for sg in (-1, 1):
            m = r > R
            x, y = sg * r * np.sin(th), r * np.cos(th)
            ax.plot(x[m], y[m], color=color, lw=lw, zorder=2)
            if arrows:
                i = np.where(m)[0][len(np.where(m)[0]) // 2 + 10]
                arrow(ax, (x[i + 1], y[i + 1]), (x[i], y[i]), color=color, lw=lw, ms=16)


def magnets(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Magnets and the Earth’s field')
    if s == 0:
        ax = wax(fig, [0.04, 0.30, 0.42, 0.30], (-2, 2), (-0.8, 0.8))
        ax.add_patch(Rectangle((-1.5, -0.4), 1.5, 0.8, fc=PINK, ec=BG, lw=3)); ax.add_patch(Rectangle((0, -0.4), 1.5, 0.8, fc=C1, ec=BG, lw=3))
        ax.text(-0.75, 0, 'N', color=BG, fontsize=40, ha='center', va='center', weight='bold'); ax.text(0.75, 0, 'S', color=BG, fontsize=40, ha='center', va='center', weight='bold')
        T(fig, 0.04, 0.24, 'Moving electrons inside the atoms of the metal\nmake its magnetic field.', size=22, color=SOFT)
        cards = [('Permanent magnet', 'keeps its magnetism', C1), ('Temporary magnet', 'soft iron: magnetic only while in a field', C2), ('Electromagnet', 'a current in a coil (often an iron core): can be switched off', PINK)]
        for i, (a, b, c) in enumerate(cards):
            card(fig, 0.52, 0.62 - i * 0.22, 0.43, 0.19, a, b, tcol=c, size=21)
        return
    if s == 1:
        ax = wax(fig, [0.04, 0.14, 0.52, 0.62], (-2.4, 2.4), (-1.3, 1.3)); ax.set_aspect('equal')
        _efield(ax, (-2.4, 2.4), (-1.3, 1.3), [(-0.7, 0, 1), (0.7, 0, -1)], nper=14, r0=0.25, mask_r=0.2, lw=2.2, color=C2, maxlen=60)
        ax.add_patch(Rectangle((-0.7, -0.22), 0.7, 0.44, fc=PINK, ec=BG, lw=2, zorder=8)); ax.add_patch(Rectangle((0, -0.22), 0.7, 0.44, fc=C1, ec=BG, lw=2, zorder=8))
        ax.text(-0.35, 0, 'N', color=BG, fontsize=22, ha='center', va='center', zorder=9, weight='bold'); ax.text(0.35, 0, 'S', color=BG, fontsize=22, ha='center', va='center', zorder=9, weight='bold')
        for (x, y) in [(-1.7, 0.7), (0.0, 0.8), (1.7, 0.7), (-1.5, -0.6), (1.5, -0.5), (0, -0.7)]:
            d = np.zeros(2)
            for qx, q in [(-0.7, 1), (0.7, -1)]:
                v = np.array([x - qx, y]); d += q * v / np.linalg.norm(v) ** 3
            d /= np.linalg.norm(d)
            ax.add_patch(FancyArrowPatch((x - 0.17 * d[0], y - 0.17 * d[1]), (x + 0.17 * d[0], y + 0.17 * d[1]), arrowstyle='simple,head_length=7,head_width=9,tail_width=4', color=YELLOW, zorder=9))
        bullets(fig, ['Lines run N to S outside the magnet,\nin closed loops', 'Never cross; closer = stronger', 'Field direction = the way a compass\nnorth pole points'], 3, 0.60, 0.72, size=22, gap=0.025)
        return
    ax = wax(fig, [0.04, 0.10, 0.50, 0.70], (-3.2, 3.2), (-2.6, 2.6)); ax.set_aspect('equal')
    _dipole_lines(ax, 1.0, (1.5, 2.0, 2.7), arrows=True, color=C2)
    ax.add_patch(Circle((0, 0), 1.0, fc=PANEL2, ec=SOFT, lw=3, zorder=5)); ax.text(0, 0, 'Earth', color=SOFT, fontsize=22, ha='center', va='center', zorder=6)
    th0 = np.radians(142); Lm = 1.0 / np.sin(th0) ** 2
    px, py = np.sin(th0), np.cos(th0)
    dth = -1; r_ = Lm * np.sin(th0) ** 2
    dr = 2 * Lm * np.sin(th0) * np.cos(th0); dd = np.array([dr * np.sin(th0) + r_ * np.cos(th0), dr * np.cos(th0) - r_ * np.sin(th0)]) * dth
    dd /= np.linalg.norm(dd)
    hor = np.array([np.cos(th0), -np.sin(th0)])   # local horizontal (tangent), pointing towards the north pole side
    hor = hor if hor @ dd > 0 else -hor
    dip = np.degrees(np.arccos(np.clip(abs(hor @ dd), 0, 1)))
    ax.scatter([px], [py], s=120, color=YELLOW, zorder=9)
    arrow(ax, (px, py), (px + 0.9 * dd[0], py + 0.9 * dd[1]), color=GREEN, lw=4, ms=22)
    ax.plot([px, px + 0.9 * hor[0]], [py, py + 0.9 * hor[1]], color=YELLOW, lw=2.5, ls='--', zorder=8)
    ax.text(px - 0.15, py - 0.1, 'Tasmania', color=YELLOW, fontsize=18, ha='right')
    ax.text(px + 1.25, py + 0.15, f'B', color=GREEN, fontsize=22)
    ax.text(-3.1, -2.45, f'sketch: dip ≈ {dip:.0f}° here, field points up out of the ground', color=MUT, fontsize=16)
    bullets(fig, ['Angle of dip: the angle between\nthe field and the horizontal', 'B_horizontal = B cos(dip)\nB_vertical = B sin(dip)', 'A compass senses only the\nhorizontal part'], 3, 0.58, 0.72, size=22, gap=0.025)


def we_compass(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a compass beside a wire')
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.03, 0.12, 0.45, 0.66], (-1.2, 2.0), (-1.0, 2.6)); ax.set_aspect('equal')
    ax.text(-1.1, 2.4, 'top view  (N ↑, E →)', color=MUT, fontsize=17)
    _note(fig, 0.03, 0.10, 'field and dip values are illustrative, not measured data', 17)
    _wire(ax, 0, 1.6, True, r=0.13, label_=None); ax.text(0.25, 1.6, 'wire, current up\n(out of the page)', color=SOFT, fontsize=17, va='center')
    ax.annotate('', xy=(0, 0.1), xytext=(0, 1.45), arrowprops=dict(arrowstyle='<->', color=MUT, lw=1.5)); ax.text(-0.1, 0.8, '0.25 m', color=MUT, fontsize=16, ha='right')
    ax.scatter([0], [0], s=160, color=YELLOW, zorder=8, edgecolor=BG); ax.text(0.12, -0.18, 'compass', color=YELLOW, fontsize=18)
    arrow(ax, (0, 0), (0, 1.0), color=C1, lw=4, ms=22); ax.text(-0.1, 0.55, 'B_H 1.9 × 10⁻⁵', color=C1, fontsize=17, ha='right')
    arrow(ax, (0, 0), (0.5, 0), color=PINK, lw=4, ms=22); ax.text(0.55, 0.0, 'B_wire 9.6 × 10⁻⁶', color=PINK, fontsize=17, va='center')
    if s == 0:
        T(fig, 0.52, 0.76, r'$B_H = B\cos 72^\circ = 6.2\times10^{-5}\times\cos72^\circ = 1.916\times10^{-5}\ \mathrm{T}$', size=21)
        _sf(fig, 0.52, 0.70, '= 1.9 × 10⁻⁵ T (2 s.f.), pointing north')
        T(fig, 0.52, 0.60, r'$B_{wire} = \dfrac{k_B I}{r} = \dfrac{(2\times10^{-7})(12)}{0.25} = 9.6\times10^{-6}\ \mathrm{T}$', size=23)
        T(fig, 0.52, 0.48, 'Direction: right hand rule. Thumb up, fingers curl\nanticlockwise from above: south of the wire\nthe field points EAST.', size=21, color=SOFT)
        card(fig, 0.52, 0.12, 0.43, 0.20, 'Question', 'Earth field 6.2 × 10⁻⁵ T at dip 72°. A vertical wire\ncarries 12 A up; a compass is 0.25 m south of it.\nWhich way does the needle point?', tcol=C2, size=19)
        return
    arrow(ax, (0, 0), (0.5, 1.0), color=GREEN, lw=5, ms=26)
    ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=63.4, theta2=90, color=YELLOW, lw=2.5)); ax.text(0.12, 1.28, 'φ', color=YELLOW, fontsize=20)
    T(fig, 0.52, 0.74, r'$\tan\varphi = \dfrac{B_{wire}}{B_H} = \dfrac{9.6\times10^{-6}}{1.916\times10^{-5}}$', size=24)
    T(fig, 0.52, 0.62, r'$\varphi = 26.6^\circ$ east of north', size=26, color=YELLOW); _sf(fig, 0.52, 0.55, '= 27° east of north (2 s.f.)')
    T(fig, 0.52, 0.44, 'The two fields are at right angles: use a vector\ndiagram. State the direction of the wire’s field first\n(many students lost marks here).', size=21, color=SOFT)


def wire_field(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The magnetic field of a current')
    if s == 0:
        for i, out in enumerate([True, False]):
            ax = wax(fig, [0.04 + i * 0.30, 0.18, 0.28, 0.55], (-1.1, 1.1), (-1.1, 1.1)); ax.set_aspect('equal')
            _bwires(ax, (-1.1, 1.1), (-1.1, 1.1), [(0, 0, 1 if out else -1)], nper=4, r0=0.25, mask_r=0.13, lw=2.5, color=C2)
            _wire(ax, 0, 0, out, r=0.11); ax.text(0, -1.05, 'current out: anticlockwise' if out else 'current in: clockwise', color=SOFT, fontsize=18, ha='center')
        bullets(fig, ['Right hand rule: thumb along\nthe current, fingers curl\nthe way B goes', 'Circles centred on the wire', 'Closer lines = stronger field'], 3, 0.66, 0.74, size=22, gap=0.025)
        return
    if s == 1:
        beq(fig, 0.05, 0.72, r'$B = \dfrac{k_B I}{r}$', size=46)
        T(fig, 0.05, 0.545, 'k_B = 2 × 10⁻⁷ N A⁻²  (on the sheet)', size=22, color=SOFT)
        bullets(fig, ['I in amps, r in metres from the wire', 'r is NOT squared', 'B is a vector: give its direction', 'Units: tesla (T)'], 4, 0.05, 0.46, size=23, gap=0.018)
        ax = gax(fig, [0.58, 0.20, 0.36, 0.52], (0, 4.2), (0, 4.2), 'distance r', 'B', ticks=False)
        r = np.linspace(0.3, 4.2, 200); ax.plot(r, 1.1 / r, color=YELLOW, lw=3.5); ax.text(2.2, 2.5, 'B ∝ 1/r', color=SOFT, fontsize=21)
        _note(fig, 0.58, 0.14, 'illustrative shape')
        return
    ax = wax(fig, [0.03, 0.12, 0.60, 0.66], (-2.4, 2.4), (-1.3, 1.3)); ax.set_aspect('equal')
    _bwires(ax, (-2.4, 2.4), (-1.3, 1.3), [(-0.8, 0, 2), (0.8, 0, 1)], nper=5, r0=0.2, mask_r=0.13, lw=2, color=C2, maxlen=70, arrows=1.3)
    _wire(ax, -0.8, 0, True, r=0.11); _wire(ax, 0.8, 0, True, r=0.11)
    x0 = -0.8 + 1.6 * 2 / 3
    ax.scatter([x0], [0], s=240, marker='X', color=GREEN, zorder=9, edgecolor=BG); ax.text(x0, -0.25, 'B = 0', color=GREEN, fontsize=19, ha='center', va='top')
    ax.text(-0.8, 0.35, '2I', color=SOFT, fontsize=18, ha='center'); ax.text(0.8, 0.35, 'I', color=SOFT, fontsize=18, ha='center')
    bullets(fig, ['Same direction: fields oppose between\nthe wires; null point nearer the weaker', 'Outside: the fields point the same way and add',
                  'Opposite currents: the other way round', 'Good sketch: arrows, no crossings,\ndenser round the bigger current'], 4, 0.65, 0.76, size=20, gap=0.02)


def _wirepair(ax, x1, x2, same, y0=-1.0, y1=1.0):
    for x, up in [(x1, True), (x2, same)]:
        a, b = ((y0, y1) if up else (y1, y0))
        ax.plot([x, x], [y0, y1], color=YELLOW, lw=5, zorder=4); arrow(ax, (x, (a + b) / 2 - 0.0), (x, (a + b) / 2 + (0.45 if up else -0.45)), color=YELLOW, lw=5, ms=26)


def wire_force(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Force between parallel currents')
    chip(fig, 'Element 2 · problems')
    for i, (same, nm) in enumerate([(True, 'same direction: ATTRACT'), (False, 'opposite directions: REPEL')]):
        ax = wax(fig, [0.04 + i * 0.24, 0.30, 0.22, 0.46], (-1.2, 1.2), (-1.4, 1.4))
        _wirepair(ax, -0.5, 0.5, same)
        sg = 1 if same else -1
        arrow(ax, (-0.45, 0.0), (-0.45 + sg * 0.3, 0.0), color=GREEN, lw=4, ms=20); arrow(ax, (0.45, 0.0), (0.45 - sg * 0.3, 0.0), color=GREEN, lw=4, ms=20)
        ax.text(0, -1.35, nm, color=SOFT, fontsize=18, ha='center', va='top')
    beq(fig, 0.54, 0.72, r'$F_B = \dfrac{k_B I_1 I_2\, \ell}{r}$', size=40)
    T(fig, 0.54, 0.52, 'l: length of wire    r: distance between the wires', size=21, color=SOFT)
    if s == 0:
        bullets(fig, ['One wire’s field acts on the current in the other', 'Opposite to charges: like (same-way) currents attract'], 2, 0.54, 0.42, size=22, gap=0.02)
        return
    bullets(fig, ['r is not squared', 'Errors in 2021: squaring r, halving it,\nignoring l', 'Per unit length: F/l = k_B I₁I₂ / r\n(units N m⁻¹), not “l = 1”', 'Justify attract or repel'], 4, 0.54, 0.42, size=21, gap=0.012)


def we_wires(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: two parallel wires')
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.03, 0.40, 0.94, 0.38], (-0.12, 0.78), (-0.5, 0.9))
    for x, nm in [(0.0, 'P  8.0 A'), (0.40, 'Q  2.0 A')]:
        _wire_pt(ax, x, 0, True); ax.text(x, -0.1, nm, color=SOFT, fontsize=18, ha='center', va='top')
    ax.plot([0, 0.40], [-0.3, -0.3], color=MUT, lw=1.5); ax.text(0.2, -0.35, '0.40 m', color=MUT, fontsize=16, ha='center', va='top')
    if s == 0:
        ax.scatter([0.60], [0], s=140, color=YELLOW, zorder=8, edgecolor=BG); ax.text(0.60, -0.1, 'Z', color=YELLOW, fontsize=20, ha='center', va='top')
        arrow(ax, (0.60, 0.0), (0.60, 0.40), color=C1, lw=4, ms=20); ax.text(0.62, 0.2, 'B_P', color=C1, fontsize=18)
        arrow(ax, (0.60, 0.40), (0.60, 0.70), color=PINK, lw=4, ms=20); ax.text(0.62, 0.55, 'B_Q', color=PINK, fontsize=18)
        T(fig, 0.05, 0.34, r'$B_P = \dfrac{(2\times10^{-7})(8.0)}{0.60} = 2.667\times10^{-6}\ \mathrm{T}$    $B_Q = \dfrac{(2\times10^{-7})(2.0)}{0.20} = 2.0\times10^{-6}\ \mathrm{T}$', size=21)
        T(fig, 0.05, 0.25, r'both point up, so add:  $B = 4.667\times10^{-6}\ \mathrm{T}$ upward', size=24, color=YELLOW); _sf(fig, 0.05, 0.18, '= 4.7 × 10⁻⁶ T (2 s.f.), upward')
        return
    if s == 1:
        x0 = 0.32
        ax.scatter([x0], [0], s=260, marker='X', color=GREEN, zorder=9, edgecolor=BG); ax.text(x0, 0.12, 'B = 0', color=GREEN, fontsize=19, ha='center')
        arrow(ax, (x0, 0.0), (x0, 0.3), color=C1, lw=3, ms=16); arrow(ax, (x0 - 0.02, 0.0), (x0 - 0.02, -0.3), color=PINK, lw=3, ms=16)
        T(fig, 0.05, 0.34, r'null point:  $\dfrac{8.0}{x} = \dfrac{2.0}{0.40-x}$  $\Rightarrow$  $x = 0.32\ \mathrm{m}$ from P,  0.08 m from Q', size=23)
        T(fig, 0.05, 0.24, r'check:  $8.0/0.32 = 25$  and  $2.0/0.08 = 25$.   Nearer the weaker current, as expected.', size=22, color=SOFT)
        return
    arrow(ax, (0.03, 0.2), (0.36, 0.2), color=GREEN, lw=4, ms=20); arrow(ax, (0.37, 0.2), (0.04, 0.2), color=GREEN, lw=4, ms=20)
    ax.text(0.2, 0.3, 'attraction', color=GREEN, fontsize=19, ha='center')
    T(fig, 0.05, 0.34, r'$\dfrac{F_B}{l} = \dfrac{k_B I_1 I_2}{r} = \dfrac{(2\times10^{-7})(8.0)(2.0)}{0.40} = 8.0\times10^{-6}\ \mathrm{N\,m^{-1}}$', size=24)
    _sf(fig, 0.05, 0.27, '= 8.0 × 10⁻⁶ N m⁻¹ (2 s.f.)')
    T(fig, 0.05, 0.19, 'Same direction: attraction. Each wire feels the same size of force,\nin opposite directions (Newton’s third law).', size=21, color=SOFT)


def perp_wires(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Wires at right angles')
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.03, 0.12, 0.48, 0.66], (-0.1, 0.18), (-0.1, 0.18)); ax.set_aspect('equal')
    ax.plot([-0.08, 0.17], [0, 0], color=YELLOW, lw=5); arrow(ax, (0.08, 0), (0.15, 0), color=YELLOW, lw=5, ms=26); ax.text(0.17, 0.012, '6.0 A', color=YELLOW, fontsize=18, ha='right')
    ax.plot([0, 0], [-0.08, 0.17], color=YELLOW, lw=5); arrow(ax, (0, 0.08), (0, 0.15), color=YELLOW, lw=5, ms=26); ax.text(0.006, 0.17, '8.0 A', color=YELLOW, fontsize=18, va='top')
    ax.scatter([0.05], [0.05], s=130, color=GREEN, zorder=8, edgecolor=BG); ax.text(0.057, 0.043, 'X', color=GREEN, fontsize=20, va='top')
    ax.plot([0.05, 0.05], [0, 0.05], color=MUT, lw=1.5, ls=':'); ax.plot([0, 0.05], [0.05, 0.05], color=MUT, lw=1.5, ls=':'); ax.text(0.057, 0.022, '0.050 m', color=MUT, fontsize=15)
    _sym(ax, 0.085, 0.085, True, size=420, color=C1); ax.text(0.095, 0.098, 'B₁ out: 2.4 × 10⁻⁵ T', color=C1, fontsize=17)
    _sym(ax, 0.085, 0.052, False, size=420, color=PINK); ax.text(0.095, 0.052, 'B₂ in: 3.2 × 10⁻⁵ T', color=PINK, fontsize=17, va='center')
    if s == 0:
        T(fig, 0.54, 0.74, r'$B_1 = \dfrac{(2\times10^{-7})(6.0)}{0.050} = 2.4\times10^{-5}\ \mathrm{T}$,  out of the page', size=22)
        T(fig, 0.54, 0.62, r'$B_2 = \dfrac{(2\times10^{-7})(8.0)}{0.050} = 3.2\times10^{-5}\ \mathrm{T}$,  into the page', size=22)
        T(fig, 0.54, 0.48, 'Right hand rule for each wire, at X:', size=21, color=SOFT)
        return
    T(fig, 0.54, 0.74, 'Both fields lie along the same line\n(out of / into the page): SUBTRACT', size=23, color=SOFT)
    T(fig, 0.54, 0.58, r'$B = 3.2\times10^{-5} - 2.4\times10^{-5} = 8.0\times10^{-6}\ \mathrm{T}$', size=24, color=YELLOW)
    _sf(fig, 0.54, 0.51, '= 8.0 × 10⁻⁶ T (2 s.f.), into the page')
    T(fig, 0.54, 0.40, 'Wrong: Pythagoras would give 4.0 × 10⁻⁵ T.\nOnly use a right-angled triangle if the fields\nthemselves point at right angles.', size=21, color=PINK)


def force_current(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Force on a current in a field')
    if s == 0:
        ax = wax(fig, [0.03, 0.14, 0.46, 0.62], (-2, 2), (-1.4, 1.8)); ax.set_aspect('equal')
        _symgrid(ax, np.linspace(-1.6, 1.6, 5), np.linspace(-1.0, 1.5, 4), False, size=260, color=MUT)
        ax.plot([-1.5, 1.5], [0, 0], color=YELLOW, lw=7, zorder=5); arrow(ax, (0.2, 0), (1.0, 0), color=YELLOW, lw=7, ms=28, zorder=6)
        arrow(ax, (0, 0.1), (0, 1.1), color=GREEN, lw=5, ms=26, zorder=7); ax.text(0.15, 0.85, 'F', color=GREEN, fontsize=26, zorder=8)
        ax.text(-1.5, -0.3, 'I →', color=YELLOW, fontsize=22); ax.text(1.5, -1.3, 'B into the page', color=SOFT, fontsize=19, ha='right')
        beq(fig, 0.54, 0.76, r'$F_B = I\,\ell\,B\sin\theta$', size=38)
        learn_eq(fig, 0.54, 0.54, r'$B = \dfrac{F_B}{I_T\, \ell\sin\theta}$', size=36)
        T(fig, 0.54, 0.34, 'l: length of wire IN the field\nθ: angle between the wire and the field\nNo force when the wire is parallel to B', size=21, color=SOFT)
        return
    ax = wax(fig, [0.03, 0.14, 0.40, 0.60], (-2, 2), (-1.6, 1.8)); ax.set_aspect('equal')
    for y in np.linspace(-1.3, 1.5, 5):
        arrow(ax, (-1.9, y), (1.9, y), color=MUT, lw=1.5, ms=14)
    ax.plot([-1.0, 1.0 * np.cos(np.radians(35))], [-0.0, 1.0 * np.sin(np.radians(35))], color=YELLOW, lw=7, zorder=5)
    ax.plot([-1.0, 1.9], [0, 0], color=MUT, lw=0.5)
    ax.add_patch(Arc((-1.0, 0), 1.2, 1.2, theta1=0, theta2=35, color=GREEN, lw=3)); ax.text(-0.15, 0.16, 'θ', color=GREEN, fontsize=22)
    ax.text(1.0, -1.45, 'B', color=SOFT, fontsize=20)
    T(fig, 0.46, 0.74, 'Direction: right hand', size=26, color=YELLOW, weight='bold')
    bullets(fig, ['Fingers along the current, curl them\ntowards B: thumb gives the force', 'Use the right hand (markers advise\nagainst the left hand rule)', 'θ is the angle between wire and field,\nnot an angle of rotation',
                  'Many turns: length in the field\nis N times the side length'], 4, 0.46, 0.65, size=21, gap=0.018)


def motor(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Motors and meters')
    if s == 0:
        chip(fig, 'Element 2 · problems')
        ax = wax(fig, [0.03, 0.12, 0.50, 0.66], (-2.6, 2.6), (-1.8, 1.8)); ax.set_aspect('equal')
        ax.add_patch(Rectangle((-2.5, -0.9), 0.9, 1.8, fc=PINK, ec=BG, lw=3)); ax.add_patch(Rectangle((1.6, -0.9), 0.9, 1.8, fc=C1, ec=BG, lw=3))
        ax.text(-2.05, 0, 'N', color=BG, fontsize=34, ha='center', va='center', weight='bold'); ax.text(2.05, 0, 'S', color=BG, fontsize=34, ha='center', va='center', weight='bold')
        for y in (-0.6, 0, 0.6):
            arrow(ax, (-1.5, y), (1.5, y), color=MUT, lw=1.5, ms=13)
        a = np.radians(20); lx, ly = -0.9 * np.cos(a), 0.9 * np.sin(a)
        ax.plot([lx, -lx], [ly, -ly], color=YELLOW, lw=4, zorder=5)
        _sym(ax, lx, ly, True, size=420, color=YELLOW); _sym(ax, -lx, -ly, False, size=420, color=YELLOW)
        arrow(ax, (lx, ly + 0.15), (lx, ly + 0.95), color=GREEN, lw=4, ms=20); arrow(ax, (-lx, -ly - 0.15), (-lx, -ly - 0.95), color=GREEN, lw=4, ms=20)
        ax.text(lx - 0.1, ly + 0.55, 'F', color=GREEN, fontsize=20, ha='right'); ax.text(-lx + 0.1, -ly - 0.55, 'F', color=GREEN, fontsize=20)
        ax.text(0, -1.6, 'end view: coil turns clockwise', color=SOFT, fontsize=18, ha='center')
        T(fig, 0.56, 0.76, r'$F = N\,B\,I\,\ell$', size=34, color=YELLOW)
        T(fig, 0.56, 0.64, r'$= 40\times0.15\times2.0\times0.060 = 0.72\ \mathrm{N}$', size=24); _sf(fig, 0.56, 0.58, '= 0.72 N (2 s.f.) on each side, opposite ways')
        card(fig, 0.56, 0.20, 0.40, 0.22, 'Question', '40-turn coil, 6.0 cm sides, B = 0.15 T,\nI = 2.0 A. Force on one side?', tcol=C2, size=19)
        return
    if s == 1:
        chip(fig, 'Element 1 · explain')
        ax = wax(fig, [0.03, 0.14, 0.44, 0.62], (-1.5, 1.5), (-1.3, 1.3)); ax.set_aspect('equal')
        for a0, a1, col in [(105, 255, PINK), (-75, 75, C1)]:
            ax.add_patch(Arc((0, 0), 1.6, 1.6, theta1=a0, theta2=a1, color=col, lw=14))
        for sx in (-1, 1):
            ax.add_patch(Rectangle((sx * 1.1 - 0.12, -0.09), 0.24, 0.18, fc=SOFT, ec=BG, zorder=6))
        ax.plot([-1.3, -1.1], [0.0, 0.0], color=SOFT, lw=3); ax.plot([1.1, 1.3], [0.0, 0.0], color=SOFT, lw=3)
        ax.text(0, 0, 'split ring', color=SOFT, fontsize=18, ha='center', va='center'); ax.text(-1.3, 0.25, 'brush', color=SOFT, fontsize=16, ha='center'); ax.text(1.3, 0.25, 'brush', color=SOFT, fontsize=16, ha='center')
        ax.text(0, -1.25, 'gaps at the top and bottom', color=MUT, fontsize=16, ha='center')
        bullets(fig, ['Without it, the forces reverse after half a turn', 'The commutator flips the current each\nhalf turn; the gaps let it stop briefly\nas the coil passes vertical', 'So the force always turns the coil the\nsame way', 'To give the sense of rotation: right\nhand rule on one side, with a reason'], 4, 0.52, 0.74, size=21, gap=0.02)
        return
    for i, nm in enumerate(['Moving-coil meter', 'Faraday’s motor (1821)']):
        x0 = 0.04 + i * 0.47
        box(fig, x0, 0.18, 0.44, 0.62)
        T(fig, x0 + 0.02, 0.77, nm, size=24, color=[C1, C2][i], weight='bold')
        ax = wax(fig, [x0 + 0.02, 0.36, 0.40, 0.36], (-1.5, 1.5), (-1.2, 1.2)); ax.set_aspect('equal')
        if i == 0:
            ax.add_patch(Wedge((0, 0), 1.2, 150, 210, width=0.35, fc=PINK)); ax.add_patch(Wedge((0, 0), 1.2, -30, 30, width=0.35, fc=C1))
            ax.add_patch(Circle((0, 0), 0.4, fc=PANEL2, ec=SOFT, lw=2))
            _sym(ax, 0.0, 0.62, True, size=260, color=YELLOW); _sym(ax, 0.0, -0.62, False, size=260, color=YELLOW)
            arrow(ax, (0, 0), (0.4, 0.85), color=GREEN, lw=3, ms=16)
        else:
            ax.add_patch(Rectangle((-0.12, -1.0), 0.24, 1.5, fc=PINK, ec=BG)); ax.add_patch(Rectangle((-0.12, -1.0), 0.24, 0.5, fc=C1, ec=BG))
            ax.plot([0.5, 0.0], [1.0, 0.5], color=YELLOW, lw=4); th = np.linspace(0, TAU * 0.75, 40); ax.plot(0.75 * np.cos(th), 0.75 * np.sin(th) + 0.9, color=GREEN, lw=2, ls=':')
        T(fig, x0 + 0.02, 0.33, ['Radial field: force on each side always\nat 90° to the field, so no sin θ needed;\nsprings balance it; deflection ∝ current', 'Force on the wire is always sideways,\nso it keeps circling the magnet: the\nfirst push is not the whole story'][i], size=19, color=SOFT)


def balance_data(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Data: measuring B with a balance')
    chip(fig, 'Element 3 · data')
    I = np.array([1.0, 2.0, 3.0, 4.0]); m = np.array([0.204, 0.408, 0.612, 0.815]); Fn = m * 1e-3 * 9.81
    if s == 0:
        rows = [['I (A)', 'reading (g)', 'F = mg (mN)']] + [[f'{a:.1f}', f'{b:.3f}', f'{c * 1e3:.3f}'] for a, b, c in zip(I, m, Fn)]
        _tablegrid(fig, 0.05, 0.76, [0.10, 0.17, 0.17], 0.10, rows, size=22)
        ax = wax(fig, [0.55, 0.26, 0.40, 0.46], (-2, 2), (-1.5, 1.8)); ax.set_aspect('equal')
        ax.add_patch(Rectangle((-1.6, -1.2), 3.2, 0.35, fc=PANEL2, ec=SOFT, lw=2)); ax.text(0, -1.03, 'balance', color=SOFT, fontsize=18, ha='center', va='center')
        ax.add_patch(Rectangle((-1.4, -0.8), 0.7, 1.2, fc=PINK, ec=BG)); ax.add_patch(Rectangle((0.7, -0.8), 0.7, 1.2, fc=C1, ec=BG))
        ax.plot([-0.7, 0.7], [0.0, 0.0], color=YELLOW, lw=6); ax.text(0, 0.25, 'wire, 2.5 cm', color=YELLOW, fontsize=17, ha='center')
        for y in (-0.5, 0, 0.3):
            pass
        ax.text(0, 0.9, 'wire pushed one way,\nmagnet the other', color=SOFT, fontsize=18, ha='center')
        T(fig, 0.05, 0.22, 'grams → kg, then × 9.81 to get newtons', size=23, color=YELLOW, weight='bold')
        _note(fig, 0.05, 0.14, 'made-up data for practice, not from TASC')
        return
    ax = gax(fig, [0.07, 0.20, 0.48, 0.55], (0, 4.6), (0, 9), 'I (A)', 'F (mN)')
    ax.plot([0, 4.4], [0, 4.4 * 2.0], color=C1, lw=2.5); _graph_pts(ax, I, Fn * 1e3)
    ax.plot([1, 4, 4], [2.0, 2.0, 8.0], color=GREEN, lw=2, ls='--')
    T(fig, 0.60, 0.74, r'$F = (B\ell)\,I$:  gradient $= B\ell$', size=26)
    T(fig, 0.60, 0.64, r'gradient $= \dfrac{(7.995-2.001)\times10^{-3}}{3.0} = 1.998\times10^{-3}\ \mathrm{N\,A^{-1}}$', size=21)
    T(fig, 0.60, 0.53, r'$B = \dfrac{1.998\times10^{-3}}{0.025} = 0.0799\ \mathrm{T}$', size=26, color=YELLOW); _sf(fig, 0.60, 0.46, '= 0.080 T (2 s.f.)')
    T(fig, 0.60, 0.36, 'Wire at 30° to B: gradient × sin 30° = ½.\nIn 2023, force against sin θ: gradient = I l B.', size=21, color=SOFT)


def moving_charge(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Force on a moving charge')
    ax = wax(fig, [0.03, 0.12, 0.48, 0.68], (-1.8, 1.8), (-1.7, 1.7)); ax.set_aspect('equal')
    _symgrid(ax, np.linspace(-1.5, 1.5, 7), np.linspace(-1.4, 1.4, 7), False, size=200, color=GRID)
    R_ = [0.8, 0.8, 0.8][s]
    phi = -np.pi / 2 + TAU * ph
    if s == 1:
        ax.add_patch(Circle((0, 0), 0.8, fill=False, ec=MUT, lw=2)); ax.add_patch(Circle((0, 0), 1.4, fill=False, ec=MUT, lw=1.5, ls='--'))
        ax.text(0, -1.62, 'faster / heavier: bigger circle', color=SOFT, fontsize=17, ha='center')
        p2 = (1.4 * np.cos(phi), 1.4 * np.sin(phi)); ax.scatter([p2[0]], [p2[1]], s=150, color=SOFT, zorder=6, edgecolor=BG)
    else:
        ax.add_patch(Circle((0, 0), R_, fill=False, ec=MUT, lw=2))
    px, py = R_ * np.cos(phi), R_ * np.sin(phi)
    ax.scatter([px], [py], s=240, color=PINK, zorder=7, edgecolor=BG); ax.text(px, py, '+', color=BG, fontsize=16, ha='center', va='center', zorder=8, weight='bold')
    v = np.array([-np.sin(phi), np.cos(phi)]); fdir = -np.array([np.cos(phi), np.sin(phi)])
    arrow(ax, (px, py), (px + 0.5 * v[0], py + 0.5 * v[1]), color=YELLOW, lw=3.5, ms=20); arrow(ax, (px, py), (px + 0.4 * fdir[0], py + 0.4 * fdir[1]), color=GREEN, lw=3.5, ms=20)
    ax.text(-1.75, 1.55, 'B into the page', color=SOFT, fontsize=17)
    ax.text(-1.75, 1.38, 'yellow: v   green: F (to the centre)', color=MUT, fontsize=16)
    if s == 0:
        beq(fig, 0.56, 0.74, r'$F_B = q\,v\,B\sin\theta$', size=38)
        bullets(fig, ['At right angles to both v and B: right\nhand rule (reverse for a negative charge)', 'No force on a charge at rest, or moving along B', 'Force is at 90° to v: it does no work'], 3, 0.56, 0.52, size=22, gap=0.02)
        return
    if s == 1:
        beq(fig, 0.56, 0.74, r'$r = \dfrac{m\,v\sin\theta}{q\,B}$', size=38)
        T(fig, 0.56, 0.54, 'At 90°:  qvB = mv²/r  ⇒  r = mv / qB', size=23, color=SOFT)
        bullets(fig, ['Bigger v or m: bigger circle', 'Bigger B or q: smaller circle'], 2, 0.56, 0.44, size=23, gap=0.02)
        return
    for i, (nm, a, b, c) in enumerate([('electron', 'm = 9.11 × 10⁻³¹ kg', 'q = 1.60 × 10⁻¹⁹ C', C1), ('proton', 'm = 1.67 × 10⁻²⁷ kg', 'q = 1.60 × 10⁻¹⁹ C', PINK)]):
        card(fig, 0.56 + i * 0.20, 0.54, 0.19, 0.24, nm, a + '\n' + b, tcol=c, size=17)
    T(fig, 0.56, 0.44, 'Common errors: the electron’s mass for a proton,\nq = 1 instead of 1.60 × 10⁻¹⁹ C', size=20, color=PINK)
    learn_eq(fig, 0.56, 0.28, r'$f = \dfrac{qB}{2\pi m}$', size=32)
    T(fig, 0.80, 0.30, 'independent of speed', size=19, color=SOFT)


def helix(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Helices and the van Allen belts')
    if s == 0:
        ax = wax(fig, [0.03, 0.24, 0.60, 0.50], (0, 10), (-1.8, 1.8))
        t = np.linspace(0, 3 * TAU, 300); ax.plot(0.5 + t * 0.5, np.sin(t), color=PINK, lw=3)
        arrow(ax, (0.2, -1.5), (9.8, -1.5), color=C2, lw=3, ms=20); ax.text(9.8, -1.3, 'B', color=C2, fontsize=22, ha='right')
        arrow(ax, (0.5, 0.0), (2.2, 0.0), color=YELLOW, lw=3, ms=16); ax.text(1.0, 0.15, 'v along B', color=YELLOW, fontsize=19)
        ax.text(5.0, 1.55, 'helix: a circle (from the perpendicular part of v) drifting along B (from the parallel part)', color=SOFT, fontsize=20, ha='center')
        ax2 = wax(fig, [0.66, 0.40, 0.28, 0.32], (0, 3), (0, 2.2))
        ax2.plot([0.2, 2.6], [0.3, 0.3], color=PINK, lw=3); arrow(ax2, (0.2, 0.3), (2.6, 0.3), color=PINK, lw=3, ms=16)
        arrow(ax2, (0.2, 0.3), (2.6, 1.7), color=YELLOW, lw=4, ms=22); arrow(ax2, (2.6, 0.3), (2.6, 1.65), color=GREEN, lw=3, ms=16)
        ax2.text(1.3, 0.05, 'v cos θ  (along B)', color=PINK, fontsize=16, ha='center'); ax2.text(2.7, 1.0, 'v sin θ', color=GREEN, fontsize=16)
        ax2.text(1.2, 1.2, 'v', color=YELLOW, fontsize=20); ax2.add_patch(Arc((0.2, 0.3), 1.2, 1.2, theta1=0, theta2=30, color=YELLOW, lw=2)); ax2.text(0.85, 0.42, 'θ', color=YELLOW, fontsize=17)
        T(fig, 0.05, 0.18, 'Radius: only the perpendicular part.  Time along B: only the parallel part.', size=22, color=YELLOW)
        return
    if s == 1:
        chip(fig, 'Element 2 · problems')
        T(fig, 0.05, 0.76, 'Proton, v = 3.0 × 10⁶ m s⁻¹ at 30° to B = 0.050 T', size=26, color=SOFT)
        T(fig, 0.05, 0.66, r'$v_\perp = v\sin30^\circ = 1.5\times10^{6}$,   $v_\parallel = v\cos30^\circ = 2.598\times10^{6}\ \mathrm{m\,s^{-1}}$', size=24)
        T(fig, 0.05, 0.55, r'$r = \dfrac{m v_\perp}{qB} = \dfrac{(1.67\times10^{-27})(1.5\times10^{6})}{(1.60\times10^{-19})(0.050)} = 0.3131\ \mathrm{m}$', size=24); _sf(fig, 0.05, 0.47, '= 0.31 m (2 s.f.)')
        T(fig, 0.05, 0.38, r'$T = \dfrac{2\pi r}{v_\perp} = 1.3116\times10^{-6}\ \mathrm{s}$,   pitch $= v_\parallel T = 3.408\ \mathrm{m}$', size=24); _sf(fig, 0.05, 0.30, '= 1.31 × 10⁻⁶ s, 3.4 m (2 s.f. for the pitch)')
        return
    chip(fig, 'Element 4 · predictions')
    ax = wax(fig, [0.03, 0.10, 0.50, 0.70], (-3.2, 3.2), (-2.6, 2.6)); ax.set_aspect('equal')
    _dipole_lines(ax, 1.0, (1.8, 2.5), arrows=False, color=MUT)
    ax.add_patch(Circle((0, 0), 1.0, fc=PANEL2, ec=SOFT, lw=3, zorder=5)); ax.text(0, 0, 'Earth', color=SOFT, fontsize=20, ha='center', va='center', zorder=6)
    th = np.linspace(0.78, np.pi - 0.78, 900); r = 2.5 * np.sin(th) ** 2; xs, ys = -r * np.sin(th), r * np.cos(th)
    dx, dy = np.gradient(xs), np.gradient(ys); nrm = np.hypot(dx, dy); nx, ny = -dy / nrm, dx / nrm
    amp = 0.20 * np.sin(th) ** 2; off = amp * np.sin(th * 34)
    ax.plot(xs + off * nx, ys + off * ny, color=PINK, lw=2.2)
    ax.plot(xs, ys, color=C2, lw=1.5, ls=':')
    arrow(ax, (xs[440], ys[440]), (xs[452], ys[452]), color=C2, lw=2, ms=18)
    ax.text(-3.1, -2.45, 'sketch: the spiral tightens near the poles', color=MUT, fontsize=16)
    bullets(fig, ['Trapped charges spiral along field lines,\nbouncing between the poles', 'Near the poles the lines squeeze together:\nthe force (at 90° to B) has a component\nback along the field', 'So the particle slows its advance and turns round',
                  'A proton’s radius is huge in a weak field,\nso it escapes; electrons stay'], 4, 0.56, 0.76, size=20, gap=0.02)


def _plates_v(ax, ytop=1.2, ybot=-1.2, x0=0.0, x1=6.0):
    C1, _ = C()
    ax.plot([x0, x1], [ytop, ytop], color=C1, lw=8); ax.plot([x0, x1], [ybot, ybot], color=PINK, lw=8)
    ax.text(x0 - 0.15, ytop, '−', color=C1, fontsize=28, ha='right', va='center', weight='bold'); ax.text(x0 - 0.15, ybot, '+', color=PINK, fontsize=28, ha='right', va='center', weight='bold')


def filter(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Velocity filters and mass spectrometers')
    if s == 2:
        ax = wax(fig, [0.03, 0.12, 0.58, 0.68], (-1.6, 4.4), (-4.0, 1.0)); ax.set_aspect('equal')
        _symgrid(ax, np.linspace(0.5, 3.8, 6), np.linspace(-3.5, 0.4, 6), True, size=150, color=GRID)
        ax.plot([0, 0], [0.3, -4.0], color=SOFT, lw=4)
        arrow(ax, (-1.5, 0), (-0.3, 0), color=GREEN, lw=3, ms=18); ax.text(-1.5, 0.2, 'ions from the\nvelocity filter', color=SOFT, fontsize=16)
        for rr, c, nm in [(1.0, PINK, 'lighter'), (1.7, YELLOW, 'heavier')]:
            psi = np.linspace(0, np.pi, 100); ax.plot(rr * np.sin(psi), -rr + rr * np.cos(psi), color=c, lw=3)
            ax.scatter([0], [-2 * rr], s=120, color=c, zorder=6); ax.text(0.15, -2 * rr, nm, color=c, fontsize=17, va='center')
        ax.text(4.3, -3.9, 'B out of the page', color=SOFT, fontsize=16, ha='right')
        beq(fig, 0.64, 0.74, r'$r = \dfrac{m\,v\sin\theta}{q\,B}$', size=36)
        bullets(fig, ['Speed known: r depends on mass', 'Heavier ion: bigger semicircle,\nlands further away', 'Use q = e (1.60 × 10⁻¹⁹ C),\nnot 1 coulomb'], 3, 0.64, 0.56, size=21, gap=0.02)
        return
    ax = wax(fig, [0.03, 0.14, 0.52, 0.64], (-1.0, 7.0), (-2.2, 2.2))
    _plates_v(ax, 1.5, -1.5, 0.5, 6.0)
    _symgrid(ax, np.linspace(1.2, 5.4, 5), [-0.9, 0.0, 0.9], True, size=170, color=GRID)
    ax.scatter([1.0], [0], s=240, color=PINK, zorder=7, edgecolor=BG); ax.text(1.0, 0, '+', color=BG, fontsize=16, ha='center', va='center', zorder=8, weight='bold')
    arrow(ax, (1.3, 0), (2.5, 0), color=GREEN, lw=4, ms=22); ax.text(2.6, 0.12, 'v', color=GREEN, fontsize=21)
    arrow(ax, (1.0, 0.15), (1.0, 1.1), color=C1, lw=4, ms=20); ax.text(1.12, 0.8, 'F_E = qE', color=C1, fontsize=19)
    arrow(ax, (1.0, -0.15), (1.0, -1.1), color=YELLOW, lw=4, ms=20); ax.text(1.12, -0.8, 'F_B = qvB', color=YELLOW, fontsize=19)
    ax.text(6.9, -1.95, 'B out of the page', color=SOFT, fontsize=17, ha='right')
    if s == 0:
        beq(fig, 0.60, 0.74, r'$v = \dfrac{E}{B}$', size=42)
        bullets(fig, ['Pass straight through when\nqE = qvB', 'The charge cancels: it selects speed', 'Direct formula is quicker than\nstarting from forces'], 3, 0.60, 0.52, size=21, gap=0.02)
        return
    chip(fig, 'Element 4 · predictions')
    bullets(fig, ['Forces must be OPPOSITE', 'Right hand rule gives F_B (here: down)', 'So F_E is up: E points up, the bottom\nplate is +, the top is −',
                  'The plates exist to BALANCE the\nmagnetic force, not to repel the ions'], 4, 0.60, 0.76, size=21, gap=0.02)


def we_filter(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a mass spectrometer')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        T(fig, 0.05, 0.74, 'Velocity filter: 90.0 V across plates 6.00 mm apart, B = 0.100 T', size=26, color=SOFT)
        T(fig, 0.05, 0.62, r'$E = \dfrac{V}{d} = \dfrac{90.0}{6.00\times10^{-3}} = 1.50\times10^{4}\ \mathrm{N\,C^{-1}}$', size=28)
        T(fig, 0.05, 0.48, r'$v = \dfrac{E}{B} = \dfrac{1.50\times10^{4}}{0.100} = 1.50\times10^{5}\ \mathrm{m\,s^{-1}}$', size=28, color=YELLOW)
        T(fig, 0.05, 0.34, 'Units check: (N C⁻¹) / T = m s⁻¹', size=23, color=SOFT)
        return
    ax = wax(fig, [0.03, 0.26, 0.40, 0.52], (-1.2, 1.6), (-2.4, 0.5)); ax.set_aspect('equal')
    psi = np.linspace(0, np.pi, 100); ax.plot(np.sin(psi), -1 + np.cos(psi), color=YELLOW, lw=3)
    ax.plot([0, 0], [0.3, -2.3], color=SOFT, lw=4); ax.scatter([0], [-2.0], s=130, color=PINK, zorder=6); ax.text(-0.1, -2.0, 'detector', color=PINK, fontsize=16, ha='right', va='center')
    ax.plot([0, 1.0], [-1.0, -1.0], color=MUT, lw=1.5, ls='--'); ax.text(0.5, -0.92, 'r = 0.155 m', color=YELLOW, fontsize=17, ha='center', va='bottom')
    arrow(ax, (-1.1, 0), (-0.2, 0), color=GREEN, lw=3, ms=16)
    T(fig, 0.05, 0.22, r'$m = \dfrac{qBr}{v} = \dfrac{(1.60\times10^{-19})(0.100)(0.155)}{1.50\times10^{5}} = 1.6533\times10^{-26}\ \mathrm{kg}$', size=22)
    _sf(fig, 0.05, 0.14, '= 1.65 × 10⁻²⁶ kg (3 s.f.): about 9.9 proton masses')
    T(fig, 0.52, 0.66, 'The ion has charge +e, and the same B as the filter.', size=21, color=SOFT)
    T(fig, 0.52, 0.56, 'ratio to a proton: 1.65 × 10⁻²⁶ / 1.67 × 10⁻²⁷ ≈ 9.9\n(an ion of mass number about 10)', size=21, color=SOFT)


def em_wave(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Light as crossing fields')
    chip(fig, 'Element 1 · explain')
    ax = wax(fig, [0.03, 0.30, 0.94, 0.46], (0, 12.4), (-2.0, 2.0))
    x = np.linspace(0.3, 12, 300); w = TAU * ph
    E = np.sin(x * 1.2 - w)
    ax.plot(x, E, color=C1, lw=3)
    for xi in np.linspace(0.6, 11.8, 20):
        ei = np.sin(xi * 1.2 - w)
        if abs(ei) > 0.1:
            arrow(ax, (xi, 0), (xi, ei), color=C1, lw=1.5, ms=9)
        _sym(ax, xi, -1.7, ei > 0, size=60 + 150 * abs(ei), color=C2)
    ax.text(0.3, 1.75, 'E (up and down)', color=C1, fontsize=20); ax.text(0.3, -1.45, 'B (dots / crosses, out of and into the page)', color=C2, fontsize=17)
    arrow(ax, (9.0, 1.9), (12.0, 1.9), color=SOFT, lw=3, ms=18); ax.text(10.5, 1.65, 'beam', color=SOFT, fontsize=18, ha='center')
    pos = s == 0
    xc = 6.0; ec = np.sin(xc * 1.2 - w)
    y = (0.5 * ec) * (1 if pos else -1)
    col = PINK if pos else C1
    ax.scatter([xc], [y], s=330, color=col, zorder=8, edgecolor=BG); ax.text(xc, y, '+' if pos else '−', color=BG, fontsize=18, ha='center', va='center', zorder=9, weight='bold')
    arrow(ax, (xc + 0.35, y), (xc + 1.6, y), color=GREEN, lw=3, ms=16)
    ax.text(xc + 1.7, y + 0.1, 'F_B', color=GREEN, fontsize=18)
    if s == 0:
        T(fig, 0.05, 0.24, 'Force from E:  F = qE  (not Coulomb’s law: that is for two charges)', size=22)
        T(fig, 0.05, 0.17, 'Force from B:  F = qvB sin θ  (the charge is moving because of E)', size=22)
        T(fig, 0.05, 0.10, 'E sets the charge oscillating along the E axis. B then pushes it at 90° to both.', size=21, color=SOFT)
        return
    T(fig, 0.05, 0.24, 'Negative charge: the E push reverses, so v reverses.', size=22)
    T(fig, 0.05, 0.17, 'Reversed q and reversed v: F_B points the SAME way, along the beam.', size=22, color=GREEN)
    T(fig, 0.05, 0.10, 'So light pushes charges along its direction of travel: a comet’s ion tail points away from the Sun.', size=21, color=SOFT)


# ============================================================================ part 3: induction
def _rails(ax, x0=-2.4, x1=2.4, y=1.0, resistor=True):
    ax.plot([x0, x1], [y, y], color=SOFT, lw=4); ax.plot([x0, x1], [-y, -y], color=SOFT, lw=4)
    if resistor:
        ax.plot([x0, x0], [-y, y], color=SOFT, lw=4)
        ax.add_patch(Rectangle((x0 - 0.18, -0.35), 0.36, 0.7, fc=PANEL2, ec=PINK, lw=3, zorder=5)); ax.text(x0 - 0.3, 0, 'R', color=PINK, fontsize=22, ha='right', va='center')


def induction(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Induced emf in a moving conductor')
    if s == 0:
        ax = wax(fig, [0.03, 0.14, 0.46, 0.62], (-2, 2), (-1.7, 1.7)); ax.set_aspect('equal')
        _symgrid(ax, np.linspace(-1.7, 1.7, 6), np.linspace(-1.4, 1.4, 5), False, size=240, color=GRID)
        ax.plot([0, 0], [-1.0, 1.0], color=YELLOW, lw=9, zorder=5); ax.text(0.15, 1.2, '+', color=PINK, fontsize=30, weight='bold', zorder=7); ax.text(0.15, -1.3, '−', color=C1, fontsize=30, weight='bold', zorder=7)
        arrow(ax, (0.3, 0), (1.5, 0), color=GREEN, lw=4, ms=24); ax.text(1.0, 0.18, 'v', color=GREEN, fontsize=24)
        arrow(ax, (-0.25, -0.6), (-0.25, 0.6), color=PINK, lw=3, ms=18); ax.text(-0.4, 0.0, 'F on +', color=PINK, fontsize=17, ha='right', va='center')
        ax.text(0, -1.58, 'B into the page; open circuit: this is the emf', color=SOFT, fontsize=17, ha='center')
        ieq(fig, 0.54, 0.74, r'$emf = v\,\ell\,B\sin\theta$', size=38)
        bullets(fig, ['The magnetic force pushes free charges\nto one end: a potential difference', 'emf = the PD when no current flows', 'l: length in the field   θ: angle between\nvelocity and field', 'Units: volts'], 4, 0.54, 0.54, size=21, gap=0.015)
        return
    if s == 1:
        ax = wax(fig, [0.03, 0.18, 0.40, 0.58], (-2, 2), (-1.7, 1.7)); ax.set_aspect('equal')
        arrow(ax, (-1.2, -0.6), (1.2, -0.6), color=MUT, lw=3, ms=20); ax.text(1.3, -0.6, 'B', color=MUT, fontsize=22, va='center')
        arrow(ax, (-1.2, -0.6), (0.2, 0.8), color=GREEN, lw=4, ms=22); ax.text(0.3, 0.85, 'v', color=GREEN, fontsize=24)
        ax.add_patch(Arc((-1.2, -0.6), 1.2, 1.2, theta1=0, theta2=45, color=YELLOW, lw=3)); ax.text(-0.45, -0.45, 'θ', color=YELLOW, fontsize=22)
        ax.text(0, -1.4, 'θ: between v and B', color=SOFT, fontsize=19, ha='center')
        bullets(fig, ['Angle errors were the most common loss in 2021', 'Direction: right hand rule on positive charges\nin the conductor; that end is positive', 'Explain it: “positive charge is pushed this\nway, so this end is positive”', 'Units of emf are volts'], 4, 0.46, 0.74, size=22, gap=0.025)
        return
    ax = wax(fig, [0.03, 0.14, 0.48, 0.62], (-2.8, 2.2), (-1.6, 1.6)); ax.set_aspect('equal')
    _rails(ax, -2.4, 2.0)
    ax.plot([0.5, 0.5], [-1.0, 1.0], color=YELLOW, lw=9, zorder=5); ax.text(0.6, 1.1, '+', color=PINK, fontsize=26, weight='bold'); ax.text(0.6, -1.3, '−', color=C1, fontsize=26, weight='bold')
    arrow(ax, (0.3, -0.5), (0.3, 0.5), color=GREEN, lw=4, ms=20); ax.text(0.15, 0, 'inside the source:\n− to +', color=GREEN, fontsize=15, ha='right', va='center')
    arrow(ax, (-0.5, 1.0), (-1.5, 1.0), color=GREEN, lw=4, ms=20); arrow(ax, (-2.4, -0.5), (-2.4, -0.1), color=GREEN, lw=0, ms=1) if False else None
    ax.text(-0.5, 1.25, 'outside: + to −', color=GREEN, fontsize=15, ha='center')
    bullets(fig, ['A moving conductor is like a battery', 'Inside a source: current runs − to +', 'Outside: + to −. Don’t mix these up (2020)', 'With a resistor: V = IR, P = VI'], 4, 0.55, 0.74, size=21, gap=0.025)


def we_rod(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a rod on rails')
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.02, 0.46, 0.55, 0.34], (-3.0, 3.0), (-1.5, 1.5)); ax.set_aspect('equal')
    _symgrid(ax, np.linspace(-1.9, 2.6, 6), [-0.55, 0.55], False, size=150, color=GRID)
    _rails(ax, -2.4, 2.6)
    ax.plot([0.5, 0.5], [-1.0, 1.0], color=YELLOW, lw=8, zorder=5); ax.text(0.6, 1.1, '+', color=PINK, fontsize=22, weight='bold'); ax.text(0.6, -1.3, '−', color=C1, fontsize=22, weight='bold')
    arrow(ax, (0.8, 0), (1.9, 0), color=GREEN, lw=4, ms=20); ax.text(1.9, 0.15, 'v = 2.50 m/s', color=GREEN, fontsize=16)
    if s >= 1:
        arrow(ax, (0.2, -0.5), (-0.9, -0.5), color=PINK, lw=4, ms=20); ax.text(-0.9, -0.8, 'F opposes\nthe motion', color=PINK, fontsize=16, ha='center', va='top')
    T(fig, 0.03, 0.43, 'rod 0.300 m, B = 0.200 T into the page, R = 0.500 Ω', size=19, color=MUT)
    if s == 0:
        card(fig, 0.60, 0.50, 0.37, 0.27, 'Question', 'A 0.300 m rod moves at 2.50 m/s at right\nangles to a 0.200 T field (into the page,\nrod moving right). Find the emf and which\nend is positive.', tcol=C2, size=19)
        T(fig, 0.05, 0.34, r'$emf = v\ell B = 2.50\times0.300\times0.200 = 0.150\ \mathrm{V}$', size=27, color=YELLOW); _sf(fig, 0.05, 0.27, '= 0.150 V (3 s.f.)')
        T(fig, 0.05, 0.19, 'Positive charges are pushed up the page: the top end is positive.', size=21, color=SOFT)
        return
    if s == 1:
        T(fig, 0.05, 0.34, r'$I = \dfrac{emf}{R} = \dfrac{0.150}{0.500} = 0.300\ \mathrm{A}$', size=26)
        T(fig, 0.05, 0.24, r'$F = BI\ell = 0.200\times0.300\times0.300 = 0.0180\ \mathrm{N}$,  to the left', size=26, color=YELLOW); _sf(fig, 0.05, 0.16, '= 0.0180 N (3 s.f.)')
        return
    if s == 2:
        T(fig, 0.03, 0.34, r'push:  $P = Fv = 0.0180\times2.50 = 0.0450\ \mathrm{W}$', size=25)
        T(fig, 0.03, 0.24, r'electrical:  $P = emf\times I = 0.150\times0.300 = 0.0450\ \mathrm{W}$', size=25)
        card(fig, 0.60, 0.46, 0.37, 0.22, 'Validity check', 'Mechanical power in = electrical\npower out: energy is conserved.', tcol=GREEN, size=20)
        return
    rows = [['rod', 'R (Ω)', 'emf (V)', 'I (A)', 'F (N)'], ['original', '0.500', '0.150', '0.300', '0.0180'], ['better conductor', '0.250', '0.150', '0.600', '0.0360']]
    _tablegrid(fig, 0.03, 0.37, [0.20, 0.10, 0.11, 0.10, 0.11], 0.07, rows, size=19, colors={(2, 3): GREEN, (2, 4): GREEN})
    T(fig, 0.03, 0.14, 'Same emf (v, l, B unchanged), lower R: larger current, larger force.', size=20, color=SOFT)


def _coil_side(ax, cx, cy, w=0.5, h=1.0, n=5):
    for k in range(n):
        ax.add_patch(Ellipse((cx + 0.14 * k, cy), 0.35, h, fill=False, ec=YELLOW, lw=3, zorder=5))


def lenz(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Changing fields and Lenz’s law')
    chip(fig, 'Element 1 · explain')
    if s == 0:
        ax = wax(fig, [0.03, 0.18, 0.55, 0.56], (-3.4, 2.0), (-1.3, 1.3)); ax.set_aspect('equal')
        _coil_side(ax, 0.5, 0, h=1.8, n=6)
        ax.add_patch(Rectangle((-3.0, -0.3), 1.2, 0.6, fc=PINK, ec=BG, lw=3)); ax.add_patch(Rectangle((-1.8, -0.3), 1.2, 0.6, fc=C1, ec=BG, lw=3))
        ax.text(-1.8, 0, '', color=BG); ax.text(-2.4, 0, 'S', color=BG, fontsize=24, ha='center', va='center', weight='bold'); ax.text(-1.2, 0, 'N', color=BG, fontsize=24, ha='center', va='center', weight='bold')
        arrow(ax, (-0.5, 0.65), (0.2, 0.65), color=GREEN, lw=4, ms=20); ax.text(-0.3, 0.8, 'moving in', color=GREEN, fontsize=17, ha='center')
        ax.text(0.2, -1.2, 'coil makes its own N pole here: it pushes back', color=SOFT, fontsize=17, ha='center')
        bullets(fig, ['Steady field: no induced current', 'Changing field: a current appears', 'Lenz: the induced field OPPOSES\nthe change that caused it', 'Push N in: coil makes N to repel.\nPull away: coil makes S to attract', 'Energy conservation: you do work'], 5, 0.60, 0.74, size=21, gap=0.018)
        return
    if s == 1:
        ax = wax(fig, [0.03, 0.14, 0.50, 0.62], (-2.4, 2.4), (-1.7, 1.7)); ax.set_aspect('equal')
        ax.add_patch(Rectangle((-2.3, -1.4), 2.3, 2.8, fc=PANEL, ec=MUT, lw=2)); _symgrid(ax, np.linspace(-2.0, -0.3, 4), np.linspace(-1.1, 1.1, 4), False, size=200, color=SOFT)
        ax.add_patch(Rectangle((-1.0, -0.7), 1.8, 1.4, fill=False, ec=YELLOW, lw=5, zorder=6)); arrow(ax, (0.8, 0.0), (1.8, 0.0), color=GREEN, lw=4, ms=20)
        arrow(ax, (-0.6, 0.7), (0.3, 0.7), color=PINK, lw=4, ms=20, zorder=8); arrow(ax, (0.8, 0.45), (0.8, -0.45), color=PINK, lw=4, ms=20, zorder=8); arrow(ax, (0.3, -0.7), (-0.6, -0.7), color=PINK, lw=4, ms=20, zorder=8)
        ax.text(-2.2, 1.55, 'B into the page', color=SOFT, fontsize=17); ax.text(1.0, 0.85, 'I clockwise', color=PINK, fontsize=18)
        steps = ['1  What is the applied field doing?\n    (into the page, and decreasing)', '2  So which way must the induced field\n    point to oppose that? (into the page)', '3  Right hand rule for a coil: field into\n    the page = clockwise current', '4  Write it up and name Lenz’s law']
        bullets(fig, steps, 4, 0.56, 0.74, size=20, gap=0.02, mark='›')
        return
    if s == 2:
        ax = wax(fig, [0.03, 0.14, 0.50, 0.62], (-2.6, 2.6), (-1.7, 1.7)); ax.set_aspect('equal')
        ax.add_patch(Rectangle((-2.5, -1.5), 3.0, 3.0, fc=PANEL, ec=MUT, lw=2)); _symgrid(ax, np.linspace(-2.2, 0.3, 4), np.linspace(-1.2, 1.2, 4), False, size=200, color=SOFT)
        ax.add_patch(Rectangle((-1.2, -1.0), 3.0, 2.0, fc='none', ec=YELLOW, lw=4, zorder=6))
        th = np.linspace(0, TAU, 200); ax.plot(0.0 + 0.7 * np.cos(th), 0.0 + 0.7 * np.sin(th), color=PINK, lw=3, zorder=7)
        arrow(ax, (0.7 * np.cos(-0.5), 0.7 * np.sin(-0.5)), (0.7 * np.cos(-0.7), 0.7 * np.sin(-0.7)), color=PINK, lw=3, ms=18, zorder=8)
        arrow(ax, (1.8, 1.5), (2.5, 1.5), color=GREEN, lw=4, ms=20); ax.text(2.0, 1.6, 'pulled out', color=GREEN, fontsize=17, ha='center')
        ax.text(-1.2, 1.5, 'Q: positive (top)', color=PINK, fontsize=16, ha='left')
        steps = ['Eddy currents loop through the metal', 'Lenz: they oppose the motion, so the\nplate slows rapidly', 'Draw them circular, part in the field\nand part out of it', 'Energy: kinetic → electrical → heat']
        bullets(fig, steps, 4, 0.56, 0.74, size=21, gap=0.02)
        return
    ax = wax(fig, [0.03, 0.12, 0.50, 0.66], (-2.6, 2.6), (-1.0, 2.6))
    for k in range(7):
        ax.add_patch(Ellipse((-1.2 + 0.4 * k, 0.1), 0.25, 0.5, fill=False, ec=YELLOW, lw=3))
    ax.add_patch(Rectangle((-1.8, 1.5), 3.6, 0.3, fc=PANEL2, ec=SOFT, lw=2)); ax.text(-1.8, 2.05, 'aluminium plate', color=SOFT, fontsize=16, ha='left', va='center')
    ax.text(0, -0.4, 'coil: alternating current', color=YELLOW, fontsize=17, ha='center')
    for x in (-0.9, 0.9):
        arrow(ax, (x, 0.5), (x, 1.3), color=C2, lw=2.5, ms=16)
    th = np.linspace(0, TAU, 100); ax.plot(0.6 * np.cos(th) - 0.9, 0.12 * np.sin(th) + 1.65, color=PINK, lw=2.5)
    arrow(ax, (0, 1.95), (0, 2.5), color=GREEN, lw=5, ms=24); ax.text(0.15, 2.3, 'repelled', color=GREEN, fontsize=18)
    for i, (a, b, c) in enumerate([('AC coil', 'changing B → eddy currents →\nopposing field → plate repelled', GREEN), ('DC coil', 'no change in B → no induction →\nthe plate stays put', PINK), ('Steel plate', 'iron becomes a temporary magnet:\nattracted to the coil', YELLOW)]):
        card(fig, 0.57, 0.60 - i * 0.215, 0.39, 0.19, a, b, tcol=c, size=18)


def transformer(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Transformers')
    chip(fig, 'Element 1 · principles')
    ax = wax(fig, [0.03, 0.14, 0.55, 0.62], (-3.2, 3.2), (-2.2, 2.2)); ax.set_aspect('equal')
    ax.add_patch(Rectangle((-2.0, -1.5), 4.0, 3.0, fill=False, ec=SOFT, lw=22, zorder=3)); ax.text(0, 0, 'laminated\niron core', color=SOFT, fontsize=19, ha='center', va='center')
    for k in range(6):
        ax.add_patch(Ellipse((-2.0, -0.75 + 0.3 * k), 0.8, 0.28, fc='none', ec=YELLOW, lw=3, zorder=6)); ax.add_patch(Ellipse((2.0, -0.45 + 0.18 * k), 0.8, 0.18, fc='none', ec=PINK, lw=3, zorder=6))
    ax.text(-2.0, 1.95, 'primary (AC in)', color=YELLOW, fontsize=17, ha='center'); ax.text(2.0, 1.95, 'secondary (AC out)', color=PINK, fontsize=17, ha='center')
    ax.text(0, -2.05, 'changing field in the core links both coils', color=SOFT, fontsize=17, ha='center')
    ieq(fig, 0.62, 0.74, r'$P = VI$', size=36)
    bullets(fig, ['AC in the primary: changing field in the core', 'Changing field links the secondary:\nan alternating emf is induced', 'Steady current: no change, no induction', 'More secondary turns: bigger voltage\n(step up); power conserved, so less current', 'Laminated core: limits eddy currents'], 5, 0.62, 0.58, size=19, gap=0.014)


def generator(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Generators')
    ax = wax(fig, [0.03, 0.40, 0.38, 0.40], (-2, 2), (-1.7, 1.7)); ax.set_aspect('equal')
    ax.add_patch(Rectangle((-2.0, -0.8), 0.5, 1.6, fc=PINK, ec=BG)); ax.add_patch(Rectangle((1.5, -0.8), 0.5, 1.6, fc=C1, ec=BG))
    for y in (-0.5, 0, 0.5):
        arrow(ax, (-1.4, y), (1.4, y), color=MUT, lw=1.3, ms=11)
    a = TAU * ph
    lx, ly = -0.9 * np.cos(a), 0.9 * np.sin(a) * 0 + 0.9 * np.sin(a)
    ax.plot([lx, -lx], [ly, -ly], color=YELLOW, lw=4, zorder=5)
    for sgn in (1, -1):
        ax.scatter([sgn * lx], [sgn * ly], s=300, color=YELLOW, zorder=6, edgecolor=BG)
    ax.text(0, -1.55, 'end view of the turning coil', color=SOFT, fontsize=17, ha='center')
    gx = gax(fig, [0.50, 0.42, 0.45, 0.34], (0, 1), (-1.3, 1.3), 'time (one turn)', 'emf', ticks=False)
    t = np.linspace(0, 1, 200)
    if s == 0:
        gx.plot(t, np.cos(TAU * t), color=C2, lw=3); gx.scatter([ph], [np.cos(TAU * ph)], s=140, color=YELLOW, zorder=6)
        gx.text(0.5, 1.2, 'starts at a peak: sides moving at 90° to B', color=SOFT, fontsize=16, ha='center'); gx.text(0.5, -1.25, 'slip rings: alternating current', color=SOFT, fontsize=16, ha='center')
        bullets(fig, ['Side speed v = 2πr f', 'Sides cut across B: emf; greatest when moving at 90° to B,\nzero when moving along B', 'N turns multiply the wire length in the field'], 3, 0.04, 0.33, size=20, gap=0.008)
        return
    gx.plot(t, np.where(np.abs(np.sin(TAU * t)) < 0.12, 0.0, np.abs(np.sin(TAU * t))), color=C2, lw=3, ls='-')
    gx.plot(t, np.sin(TAU * t), color=MUT, lw=2, ls=':')
    gx.text(0.5, 1.2, 'dotted: slip rings. solid: commutator', color=SOFT, fontsize=16, ha='center')
    gx.scatter([ph], [abs(np.sin(TAU * ph)) if abs(np.sin(TAU * ph)) >= 0.12 else 0.0], s=140, color=YELLOW, zorder=6)
    bullets(fig, ['Read the starting position: peak or zero', 'Mark the period on the axis', 'Commutator: output stays one sign (arches,\nwith small gaps as the brushes cross)', 'Not horizontal lines, triangles or square waves'], 4, 0.04, 0.33, size=20, gap=0.006)


def we_gen(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a hand-turned generator')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        ax = wax(fig, [0.03, 0.30, 0.34, 0.46], (-1.6, 1.6), (-1.4, 1.4)); ax.set_aspect('equal')
        ax.add_patch(Circle((0, 0), 1.0, fill=False, ec=MUT, lw=2, ls='--')); ax.plot([-1.0, 1.0], [0, 0], color=YELLOW, lw=4)
        ax.scatter([0], [0], s=60, color=SOFT); ax.scatter([1.0], [0], s=200, color=YELLOW, zorder=6)
        arrow(ax, (1.0, 0.1), (1.0, 0.95), color=GREEN, lw=4, ms=20); ax.text(1.12, 0.5, 'v', color=GREEN, fontsize=20)
        ax.annotate('', xy=(-1.0, -1.2), xytext=(1.0, -1.2), arrowprops=dict(arrowstyle='<->', color=SOFT, lw=2)); ax.text(0, -1.38, 'width 5.00 cm', color=SOFT, fontsize=16, ha='center')
        T(fig, 0.40, 0.76, '120 turns, active sides 8.00 cm long, width 5.00 cm,\n25.0 Hz, B = 0.300 T', size=22, color=SOFT)
        T(fig, 0.40, 0.62, r'$T = \dfrac{1}{f} = \dfrac{1}{25.0} = 0.0400\ \mathrm{s}$', size=26)
        T(fig, 0.40, 0.50, r'$v = \dfrac{2\pi r}{T} = \pi d f = \pi\times0.0500\times25.0 = 3.927\ \mathrm{m\,s^{-1}}$', size=24); _sf(fig, 0.40, 0.43, '= 3.93 m s⁻¹ (3 s.f.)')
        T(fig, 0.40, 0.33, 'Convert cm to m. Use the period, not 50.', size=21, color=SOFT)
        return
    gx = gax(fig, [0.07, 0.16, 0.52, 0.55], (0, 0.08), (-14, 14), 'time (s)', 'emf of one side (V)')
    t = np.linspace(0, 0.08, 400); gx.plot(t, 11.31 * np.sin(TAU * 25 * t), color=C2, lw=3)
    gx.set_xticks([0, 0.02, 0.04, 0.06, 0.08]); gx.set_yticks([-11.3, 0, 11.3]); gx.axhline(11.31, color=GRID, lw=1, ls='--')
    T(fig, 0.62, 0.74, r'$emf_{max} = N\,v\,\ell\,B$', size=26)
    T(fig, 0.62, 0.64, r'$= 120\times3.927\times0.0800\times0.300$', size=22); T(fig, 0.62, 0.55, r'$= 11.31\ \mathrm{V}$', size=26, color=YELLOW); _sf(fig, 0.62, 0.48, '= 11.3 V (3 s.f.), one side')
    T(fig, 0.62, 0.38, 'Both active sides add in series:\n22.6 V for the whole coil.\nSay which one you are finding.', size=21, color=SOFT)
    _note(fig, 0.07, 0.09, 'sketch starts at zero: coil plane at 90° to B')


def back_emf(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Induction working against a motor')
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.02, 0.46, 0.55, 0.34], (-3.0, 3.0), (-1.5, 1.5)); ax.set_aspect('equal')
    _symgrid(ax, np.linspace(-1.2, 2.4, 5), [-0.55, 0.55], True, size=150, color=GRID)
    ax.plot([-2.4, 2.6], [1.0, 1.0], color=SOFT, lw=4); ax.plot([-2.4, 2.6], [-1.0, -1.0], color=SOFT, lw=4); ax.plot([-2.4, -2.4], [-1.0, 1.0], color=SOFT, lw=4)
    ax.add_patch(Rectangle((-2.55, -0.25), 0.3, 0.5, fc=PANEL2, ec=PINK, lw=3, zorder=6)); ax.text(-2.75, 0.55, '−', color=C1, fontsize=20, ha='right'); ax.text(-2.75, -0.55, '+', color=PINK, fontsize=20, ha='right')
    ax.plot([0.5, 0.5], [-1.0, 1.0], color=YELLOW, lw=9, zorder=5)
    arrow(ax, (0.7, 0.0), (1.8, 0.0), color=PINK, lw=4, ms=20); ax.text(1.0, 0.18, 'F_B', color=PINK, fontsize=18)
    arrow(ax, (0.3, -0.5), (0.3, 0.5), color=GREEN, lw=3, ms=16); ax.text(0.18, 0.0, 'I', color=GREEN, fontsize=18, ha='right')
    ax.text(2.6, -1.35, 'B out of the page', color=SOFT, fontsize=16, ha='right')
    T(fig, 0.03, 0.43, 'rails 0.15 m apart, B = 0.40 T, supply 6.0 V, roller 0.30 Ω', size=19, color=MUT)
    if s == 0:
        T(fig, 0.03, 0.34, r'$I = \dfrac{V}{R} = \dfrac{6.0}{0.30} = 20\ \mathrm{A}$', size=26)
        T(fig, 0.03, 0.24, r'$F = BI\ell = 0.40\times20\times0.15 = 1.2\ \mathrm{N}$, along the rails, away from the battery', size=24, color=YELLOW); _sf(fig, 0.03, 0.15, '= 1.2 N (2 s.f.)')
        card(fig, 0.60, 0.50, 0.37, 0.27, 'Question', 'A roller across rails 0.15 m apart in a\n0.40 T field is connected to 6.0 V, 0.30 Ω.\nWhat is the starting force on it?', tcol=C2, size=19)
        return
    gx = gax(fig, [0.64, 0.52, 0.31, 0.25], (0, 1), (0, 1.2), 'time', '', ticks=False)
    t = np.linspace(0, 1, 100); gx.plot(t, 1 - np.exp(-4 * t), color=C2, lw=3); gx.text(0.5, 1.05, 'speed → 100 m/s', color=C2, fontsize=15, ha='center')
    gy = gax(fig, [0.64, 0.14, 0.31, 0.25], (0, 1), (0, 1.2), 'time', '', ticks=False)
    gy.plot(t, np.exp(-4 * t), color=PINK, lw=3); gy.text(0.5, 1.05, 'current → 0', color=PINK, fontsize=15, ha='center')
    T(fig, 0.03, 0.34, r'stops accelerating when $v\ell B = V$:', size=22, color=SOFT)
    T(fig, 0.03, 0.25, r'$v = \dfrac{V}{B\ell} = \dfrac{6.0}{0.40\times0.15} = 100\ \mathrm{m\,s^{-1}}$,  and then $I = 0$', size=25, color=YELLOW)
    _sf(fig, 0.03, 0.15, '= 1.0 × 10² m s⁻¹ (2 s.f.)')


def ind_contexts(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Induction in the real world')
    if s == 0:
        chip(fig, 'Element 2 · problems')
        ax = wax(fig, [0.03, 0.14, 0.46, 0.62], (-1.6, 1.6), (-1.5, 1.5)); ax.set_aspect('equal')
        _symgrid(ax, np.linspace(-1.2, 1.2, 5), np.linspace(-1.2, 1.2, 5), False, size=160, color=GRID)
        ax.add_patch(Circle((0, 0), 1.2, fc=PANEL2, ec=YELLOW, lw=4, zorder=2, alpha=0.6)); ax.plot([0, 1.2], [0, 0], color=YELLOW, lw=7, zorder=5)
        ax.scatter([0], [0], s=160, color=SOFT, zorder=6); ax.text(0.0, -0.18, 'contact', color=SOFT, fontsize=15, ha='center', va='top'); ax.text(1.25, 0.0, 'contact', color=SOFT, fontsize=15, va='center')
        ax.add_patch(Arc((0, 0), 2.7, 2.7, theta1=20, theta2=70, color=GREEN, lw=3)); arrow(ax, (1.25 * np.cos(1.1), 1.25 * np.sin(1.1)), (1.2 * np.cos(1.25), 1.2 * np.sin(1.25)), color=GREEN, lw=3, ms=18)
        T(fig, 0.54, 0.74, r'$emf = v\ell B$ along a radius', size=28, color=YELLOW)
        bullets(fig, ['Right hand rule on positive charge: say\nwhich contact is positive, and why', 'With a current there is a force BIl\nopposing the turning', 'The applied force must be in the direction\nof motion: give its direction (2018)'], 3, 0.54, 0.62, size=21, gap=0.02)
        return
    chip(fig, 'Element 4 · predictions')
    ax = wax(fig, [0.03, 0.14, 0.50, 0.62], (-3, 3), (-1.8, 1.8)); ax.set_aspect('equal')
    ax.add_patch(Ellipse((0, 0), 3.4, 0.38, fc=SOFT, ec=BG, zorder=4))
    for sg in (1, -1):
        ax.add_patch(Polygon([[0.5, sg * 0.1], [-0.2, sg * 1.5], [-0.65, sg * 1.5], [-0.35, sg * 0.1]], fc=SOFT, ec=BG, zorder=3))
        ax.add_patch(Polygon([[-1.5, sg * 0.05], [-1.7, sg * 0.5], [-1.9, sg * 0.5], [-1.75, sg * 0.05]], fc=SOFT, ec=BG, zorder=3))
    ax.text(-0.4, 1.7, '−', color=C1, fontsize=30, ha='center', weight='bold'); ax.text(-0.4, -1.7, '+', color=PINK, fontsize=30, ha='center', weight='bold', va='top')
    arrow(ax, (1.4, 0), (2.7, 0), color=GREEN, lw=4, ms=22); ax.text(2.0, 0.2, 'east', color=GREEN, fontsize=18, ha='center')
    ax.text(-2.8, 1.6, 'N ↑', color=SOFT, fontsize=18); ax.text(-2.8, 1.2, 'top view', color=MUT, fontsize=15)
    T(fig, 0.56, 0.76, r'$emf = v\,\ell\,B\sin(\mathrm{dip})$', size=24)
    T(fig, 0.56, 0.66, r'$= 250\times40.0\times6.2\times10^{-5}\times\sin72^\circ = 0.5897\ \mathrm{V}$', size=19); _sf(fig, 0.56, 0.60, '= 0.59 V (2 s.f.)')
    bullets(fig, ['Only the vertical part of the field counts', 'Flying east: the right wing is positive', 'No steady current for the electronics:\nthey move with the plane, so the same\nPD appears across them all'], 3, 0.56, 0.50, size=20, gap=0.015)


# ============================================================================ part 4 and finish
def contexts(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Contexts named in the course')
    chip(fig, 'Element 4 · predictions')
    if s == 0:
        card(fig, 0.05, 0.36, 0.44, 0.42, 'Medical imaging (MRI)', 'Very strong magnetic fields magnetise nuclei in the body;\nthe images show soft tissue clearly, with no ionising\nradiation. The strong field is a hazard near metal\nimplants, so safety procedures matter.', tcol=C1, size=21)
        card(fig, 0.52, 0.36, 0.44, 0.42, 'Superconductivity', 'Zero resistance below a critical temperature, and the\nMeissner effect: magnetic flux is expelled from inside.\nSuperconducting coils make the strong fields in MRI\nmachines and particle accelerators.', tcol=PINK, size=21)
        return
    card(fig, 0.05, 0.36, 0.44, 0.42, 'Wave theory of light', 'Maxwell (1860s): changing electric and magnetic fields\ntravel through space as waves, at the speed of light.\nSo light is an electromagnetic wave.', tcol=C2, size=21)
    card(fig, 0.52, 0.36, 0.44, 0.42, 'Link back to the big idea', 'An oscillating charge emits waves at its own frequency:\nthe principle behind aerials. Accelerators use electric\nfields to speed charges up and magnetic fields to steer.', tcol=GREEN, size=21)


def exam_contexts(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Unfamiliar contexts')
    chip(fig, 'Element 4 · predictions')
    if s == 0:
        ax = wax(fig, [0.03, 0.14, 0.42, 0.62], (-2, 2), (-2, 2)); ax.set_aspect('equal')
        ax.add_patch(Circle((0, 0), 1.0, fc=PANEL2, ec=SOFT, lw=3)); ax.text(0, 0, 'Earth\n(charge at\nthe centre)', color=SOFT, fontsize=17, ha='center', va='center')
        for a in np.linspace(0, TAU, 9)[:-1]:
            arrow(ax, (1.05 * np.cos(a), 1.05 * np.sin(a)), (1.5 * np.cos(a), 1.5 * np.sin(a)), color=C1, lw=2, ms=14)
        ax.text(0, -1.85, 'field: 150 V/m, 60 km of atmosphere', color=SOFT, fontsize=17, ha='center')
        T(fig, 0.50, 0.74, r'$V = Ed = 150\times60\times10^{3} = 9.0\times10^{6}\ \mathrm{V}$', size=24)
        T(fig, 0.50, 0.62, r'$Q = \dfrac{E r^2}{k_E} = \dfrac{150\times(6.4\times10^{6})^2}{9.00\times10^{9}} = 6.8\times10^{5}\ \mathrm{C}$', size=24); _sf(fig, 0.50, 0.53, '= 6.8 × 10⁵ C (2 s.f.), r in metres')
        T(fig, 0.50, 0.43, 'Radius from the centre, converted to metres:\nthe 2020 report saw wrong radii and unit slips.', size=21, color=SOFT)
        return
    card(fig, 0.05, 0.50, 0.44, 0.28, 'Lightning strike (2025 style)', 'Minimum PD: V = E d with the ionising field.\nCharge: Q = I t.  Energy: E = V Q.\nThe field is given: use it, and “minimum” matters.', tcol=PINK, size=20)
    card(fig, 0.52, 0.50, 0.44, 0.28, 'Accelerator ring', 'p = 450 GeV/c = 450 × 10⁹ × 1.60 × 10⁻¹⁹ / 3.00 × 10⁸\n= 2.4 × 10⁻¹⁶ kg m s⁻¹ (given c = 3.00 × 10⁸ m s⁻¹).', tcol=C1, size=20)
    T(fig, 0.06, 0.40, r'$B = \dfrac{p}{qr} = \dfrac{2.4\times10^{-16}}{(1.60\times10^{-19})(1000)} = 1.5\ \mathrm{T}$', size=26, color=YELLOW)
    T(fig, 0.06, 0.28, 'p = mv would give v ≈ 1.4 × 10¹¹ m s⁻¹, faster than light:\nNewtonian mechanics fails at these energies.', size=21, color=SOFT)


def _tips(fig, tips, start, n, title, rows=5):
    C1, C2 = C()
    header(fig, title)
    cols = [C1, C2, PINK, GREEN, YELLOW]
    for i in range(n):
        x = 0.05 + (i // rows) * 0.46; y = 0.67 - (i % rows) * 0.118
        box(fig, x, y, 0.44, 0.10, fc=PANEL)
        T(fig, x + 0.015, y + 0.05, str(start + i), size=30, color=cols[i % 5], weight='bold', va='center')
        T(fig, x + 0.065, y + 0.05, tips[i], size=20, va='center')
    _note(fig, 0.05, 0.10, 'From examiners’ comments in TASC assessment reports')


def exam_tips(fig, s, ph):
    tips = ['Give a direction with every force,\nfield and current', 'Vectors: draw tip to tail and\ntake the angle from the picture',
            'Convert first: cm, mm, μC, g, kV\nbefore you substitute', 'Right formula: Coulomb for forces,\nE = V/d for plates, kq/r² for points',
            'Use e, not 1, and the proton\nmass, not the electron’s', 'Right hand rule: say what thumb and\nfingers show (never the left hand)',
            'Lenz: what changes, what the induced\nfield does, then the current', 'Sketches: arrows, no crossings, line\ndensity, asymmetry', 'Data: straight-line variable, labels,\nbest fit, far-apart gradient',
            'State your energy equation, and\ncheck the answer is sensible']
    _tips(fig, tips, 1, [2, 5, 8, 10][s], 'Tips from examiners', rows=5)


def more_tips(fig, s, ph):
    tips = ['Explain, don’t just state: no field in\na cage, because no potential difference', 'Force per unit length: divide by l,\ndon’t put in 1 metre', 'Coils: count the turns in the length',
            'Sign of a charge: from the force\nand the field direction', 'The angle in emf and force formulas:\nbetween v (or the wire) and B', 'An emf is a potential difference;\nit is not a force',
            'Circle at 90°: use v. At an angle:\nonly v sin θ', 'Carry unrounded values forward;\nuse your own value, not the given one']
    _tips(fig, tips, 11, [4, 8][s], 'More tips from examiners', rows=4)


def summary_panel(fig, ph):
    C1, C2 = C()
    header(fig, 'Criterion 6 in one screen')
    chips_ = [('F = kq₁q₂/r²', C1), ('E = F/q', C1), ('E = kq/r²', C1), ('E = V/d', C1), ('V = ΔEp/q', C1), ('qV = ½mv²', C1),
              ('F = kB I₁I₂ l/r', C2), ('B = kB I/r', C2), ('F = BIl sinθ', C2), ('F = qvB sinθ', C2), ('r = mv sinθ/qB', C2), ('v = E/B', C2),
              ('emf = vlB sinθ', PINK), ("Lenz's law", PINK), ('eddy currents', PINK), ('generators', PINK),
              ('right hand rule', GREEN), ('vector diagrams', GREEN), ('field sketches', GREEN), ('give directions', GREEN)]
    x, y = 0.06, 0.75
    for t, c in chips_:
        w = len(t) * 0.0092 + 0.016
        if x + w > 0.95:
            x = 0.06; y -= 0.10
        chip(fig, t, color=c, size=24, x=x, y=y, ha='left')
        x += w + 0.015
    T(fig, 0.06, 0.20, 'Know what is on the sheet, give every direction, and always say WHY.', size=30, color=YELLOW, weight='bold')


def summary(fig, s, ph):
    summary_panel(fig, ph)



