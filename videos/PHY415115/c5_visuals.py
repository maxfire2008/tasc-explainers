"""Draw functions for PHY415115 Criterion 5 (Newtonian mechanics including gravitational fields).

Every function has the signature draw(fig, s, ph):
  s  = step index within the scene (the slide builds up as s increases)
  ph = animation phase in [0, 1) for animated steps (Step.anim), 0 for stills.
Animations must loop seamlessly: anything periodic must complete a whole number of
cycles as ph goes 0 -> 1.
Colours: C1 = course accent, C2 = module accent (from the theme), PINK/GREEN/YELLOW are semantic.
"""
import math

import numpy as np
from matplotlib.patches import Circle, Rectangle, Polygon, Arc, Ellipse, FancyBboxPatch

from explainer import layout as L
from explainer.layout import (header, T, bullets, box, card, eq, sheet_eq, learn_eq, chip, wax, gax, darrow, arrow,
                              label, frac, FG, SOFT, MUT, GRID, PANEL, PANEL2, BG, PINK, GREEN, YELLOW, TAU)

g = 9.81
G_ = 6.67e-11
RAD = math.radians


def C():
    return L.A1(), L.A2()


def _sheet(section, fig, x, y, s, **kw):
    """sheet_eq with the real section heading: this criterion uses several sections of the sheet."""
    L.ctx['sheet_section'] = section
    return sheet_eq(fig, x, y, s, **kw)


def meq(fig, x, y, s, **kw):
    return _sheet('Motion in a Straight Line, Momentum,\nForce, Centripetal Force', fig, x, y, s, **kw)


def weq(fig, x, y, s, **kw):
    return _sheet('Work, Energy and Power', fig, x, y, s, **kw)


def geq(fig, x, y, s, **kw):
    return _sheet('Gravity, Kepler’s Law', fig, x, y, s, **kw)


def teq(fig, x, y, s, **kw):
    return _sheet('Trigonometry Identities', fig, x, y, s, **kw)


def extend(base, n, *extras):
    """Add steps after a finished scene: steps 0..n-1 use base, later steps use extras in turn."""
    def draw(fig, s, ph):
        if s < n:
            return base(fig, s, ph)
        return extras[s - n](fig, 0, ph)
    return draw


def _lines(fig, x, y, rows, size=26, gap=0.075):
    """Lines of working: (text, colour) from y downwards.  Returns the y below the last line."""
    for st, c in rows:
        T(fig, x, y, st, size=size, color=c)
        y -= gap
    return y


def _sf(fig, x, y, s):
    """The rounded answer, shown under the unrounded one.  On screen only: never narrated."""
    T(fig, x, y, s, size=21, color=GREEN)


def _q(fig, text, y=0.64, h=0.18, title='Question', size=22):
    card(fig, 0.05, y, 0.90, h, title, text, tcol=C()[1], size=size)


def _vec(ax, p0, p1, color=FG, lw=3.5, ms=26, text=None, tp=None, size=19, **kw):
    """Arrow with an optional label placed at tp (data coordinates)."""
    arrow(ax, p0, p1, color=color, lw=lw, ms=ms, **kw)
    if text:
        if tp is None:
            tp = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
        label(ax, tp[0], tp[1], text, size=size, color=color, bbox=dict(fc=BG, ec='none', pad=1.5))


# ============================================================================ title card, overview, thumbnail
def _title_orbit(fig, rect, ph=0):
    """The title card and thumbnail graphic: a planet with orbits, a satellite and a thrown-ball arc, so it can't be
    mistaken for Criterion 7's waves or Criterion 8's atom."""
    C1, C2 = C()
    ax = wax(fig, rect, (-1.2, 1.2), (-1.0, 1.15))
    ax.set_aspect('equal')
    ax.add_patch(Circle((0, -0.05), 0.42, fc=C2, ec=BG, lw=5, zorder=3))
    ax.add_patch(Arc((-0.17, 0.02), 0.5, 0.4, theta1=100, theta2=200, color=BG, lw=6, alpha=0.35, zorder=4))
    for rr, c in [(0.72, C1), (1.0, C1)]:
        ax.add_patch(Circle((0, -0.05), rr, fill=False, ec=c, lw=6 if rr < 0.9 else 4, alpha=0.9 if rr < 0.9 else 0.6, zorder=2))
    a = TAU * ph + 0.8
    sx, sy = 0.72 * np.cos(a), -0.05 + 0.72 * np.sin(a)
    ax.scatter([sx], [sy], s=1500, color=YELLOW, edgecolor=BG, linewidth=4, zorder=6)
    ux, uy = -np.cos(a), -np.sin(a)
    ax.annotate('', xy=(sx + 0.30 * ux, sy + 0.30 * uy), xytext=(sx, sy),
                arrowprops=dict(arrowstyle='-|>', color=PINK, lw=7, mutation_scale=40), zorder=7)
    xs = np.linspace(-1.1, -0.3, 60)
    ax.plot(xs, 0.7 - 1.2 * (xs + 0.7) ** 2 * 1.6 + 0.0, color=GREEN, lw=5, ls=(0, (2, 2.2)), zorder=1)
    ax.scatter([-0.62], [0.7], s=900, color=GREEN, edgecolor=BG, linewidth=4, zorder=6)


def thumbnail(fig):
    """The title card's colours, with fewer and larger words so it reads at small sizes."""
    C1, C2 = C()
    fig.text(0.04, 0.87, 'CRITERION 5', ha='left', va='center', color=C1, fontsize=64, weight='bold')
    fig.text(0.04, 0.65, 'Forces', ha='left', va='center', color=FG, fontsize=150, weight='bold')
    fig.text(0.04, 0.42, '& gravity', ha='left', va='center', color=FG, fontsize=150, weight='bold')
    fig.text(0.04, 0.22, 'TASC Physics revision', ha='left', va='center', color=SOFT, fontsize=58)
    _title_orbit(fig, [0.55, 0.19, 0.44, 0.7467])


def title_card(fig, s, ph):
    intro(fig, 0, ph)


def overview(fig, s, ph):
    intro(fig, s + 1, ph)


def intro(fig, s, ph):
    C1, C2 = C()
    if s == 0:
        fig.text(0.04, 0.76, 'CRITERION 5', ha='left', va='center', color=C1, fontsize=40, weight='bold')
        fig.text(0.04, 0.53, 'Newtonian mechanics\nincluding gravitational\nfields', ha='left', va='center',
                 color=FG, fontsize=58, weight='bold', linespacing=1.15)
        fig.text(0.04, 0.27, 'TASC Physics  PHY415115\nRevision for class tests and the exam', ha='left', va='center',
                 color=SOFT, fontsize=26, linespacing=1.4)
        _title_orbit(fig, [0.55, 0.14, 0.44, 0.7467], ph)
        return
    if s == 1:
        header(fig, 'How Criterion 5 is assessed')
        card(fig, 0.05, 0.50, 0.40, 0.25, 'Internal', 'Your teacher: class tests, practicals\nand tasks during the year',
             tcol=GREEN)
        card(fig, 0.05, 0.20, 0.40, 0.25, 'External', 'End-of-year TASC exam:\nSection A is all Criterion 5', tcol=C2)
        tiles = [('≈45 min', 'suggested time'), ('45', 'marks'), ('5–7', 'compulsory questions'),
                 ('Info sheet', '+ approved calculator')]
        for i, (big, small) in enumerate(tiles):
            x = 0.52 + (i % 2) * 0.225; y = 0.50 - (i // 2) * 0.30
            box(fig, x, y, 0.205, 0.25, fc=PANEL2)
            T(fig, x + 0.1025, y + 0.16, big, size=46 if len(big) < 8 else 36, color=YELLOW, weight='bold', ha='center',
              va='center')
            T(fig, x + 0.1025, y + 0.06, small, size=21, color=SOFT, ha='center', va='center')
        T(fig, 0.52, 0.16, 'Section A of the exam (external assessment specifications)', size=18, color=MUT)
        return
    if s == 2:
        header(fig, 'The four elements of Criterion 5')
        items = [('Element 1', 'Principles', 'identify, describe and\nexplain fundamental\nprinciples'),
                 ('Element 2', 'Problems', 'select and apply\nformulas to solve\nnumerical problems'),
                 ('Element 3', 'Data', 'interpret and analyse\ngraphs and tables'),
                 ('Element 4', 'Predictions', 'interpret problems and\npredict in real-world\ncontexts')]
        for i, (n, t, b) in enumerate(items):
            x = 0.05 + i * 0.228
            box(fig, x, 0.22, 0.21, 0.50)
            T(fig, x + 0.02, 0.69, n, size=34, color=[C1, C2, PINK, GREEN][i], weight='bold')
            T(fig, x + 0.02, 0.54, t, size=32, color=FG, weight='bold')
            T(fig, x + 0.02, 0.46, b, size=21, color=SOFT)
        T(fig, 0.05, 0.16, 'Numbered in the order they appear in the course document’s standards table', size=19,
          color=MUT)
        return
    if s == 3:
        header(fig, 'What the standards ask for')
        cols = [(0.30, 'C', GREEN), (0.51, 'B', C1), (0.72, 'A', C2)]
        for x, l, c in cols:
            T(fig, x, 0.80, l, size=40, color=c, weight='bold')
        rows = [('E1 Principles', 'identifies', 'describes', 'explains'),
                ('E2 Problems', 'straightforward', 'several steps', 'complex, and\nanalyses validity'),
                ('E3 Data', 'interprets', 'analyses to generate\nnew information', 'analyses, evaluates,\ngeneralises'),
                ('E4 Predictions', 'familiar contexts', 'plausible, in\nunfamiliar contexts',
                 'reasoned and plausible,\nin unfamiliar contexts')]
        for j, r in enumerate(rows):
            y = 0.70 - j * 0.145
            box(fig, 0.05, y - 0.105, 0.90, 0.125, fc=PANEL if j % 2 == 0 else PANEL2)
            T(fig, 0.065, y - 0.042, r[0], size=26, color=FG, weight='bold', va='center')
            for (x, _, c), txt in zip(cols, r[1:]):
                T(fig, x, y - 0.042, txt, size=22, color=SOFT if c != C2 else FG, va='center')
        return
    header(fig, 'Roadmap')
    parts = [('Part 1', 'Describing motion: graphs and the equations of motion', C1),
             ('Part 2', 'Projectile motion', C2),
             ('Part 3', 'Forces and Newton’s three laws', PINK),
             ('Part 4', 'Momentum, impulse and collisions', GREEN),
             ('Part 5', 'Circular motion', YELLOW),
             ('Part 6', 'Work, energy and power', C1),
             ('Part 7', 'Gravity, fields and orbits', C2),
             ('Finish', 'Tests & exam technique, and a one-screen summary', FG)]
    for i, (a, b, c) in enumerate(parts):
        y = 0.755 - i * 0.092
        box(fig, 0.05, y - 0.038, 0.90, 0.076)
        T(fig, 0.07, y, a, size=26, color=c, weight='bold', va='center')
        T(fig, 0.17, y, b, size=25, color=FG, va='center')


# ============================================================================ part 1: describing motion
def motion(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Distance, displacement, speed, velocity', 'Acceleration', 'Displacement at any angle'][s])
    if s == 0:
        chip(fig, 'Element 2 · problems')
        learn_eq(fig, 0.06, 0.70, r'average speed $= \dfrac{\mathrm{total\ distance}}{\mathrm{total\ time}}$', size=28)
        learn_eq(fig, 0.06, 0.44, r'average velocity $= \dfrac{\mathrm{total\ displacement}}{\mathrm{total\ time}}$', size=28)
        bullets(fig, ['Distance, speed: size only (scalars)', 'Displacement, velocity: size and direction (vectors)'],
                2, 0.06, 0.25, size=22, dim=False)
        ax = wax(fig, [0.58, 0.20, 0.38, 0.55], (-0.5, 4.2), (-0.6, 4.8))
        ax.set_aspect('equal')
        arrow(ax, (0, 0), (3, 0), color=C1, lw=4); arrow(ax, (3, 0), (3, 4), color=C1, lw=4)
        arrow(ax, (0, 0), (3, 4), color=GREEN, lw=4)
        label(ax, 1.5, -0.4, '3 km east', size=20, color=C1); label(ax, 3.1, 2.0, '4 km\nnorth', size=20, color=C1, ha='left')
        label(ax, 0.75, 3.2, 'displacement\n5 km at 53°\nN of E', size=19, color=GREEN)
        T(fig, 0.60, 0.185, 'distance 7 km; time 2.0 h\nspeed 3.5 km/h; velocity 2.5 km/h at 53° N of E', size=19, color=SOFT)
    elif s == 1:
        learn_eq(fig, 0.06, 0.70, r'$a = \dfrac{\Delta v}{\Delta t} = \dfrac{v - u}{\Delta t}$', size=36)
        bullets(fig, ['A vector: the sign gives\nthe direction', 'Unit: m s⁻² (metres per second,\nper second)',
                      'Velocity changes in size, in\ndirection, or both: any change\nmeans acceleration'], 3, 0.06, 0.50, size=22, dim=False)
        ax = wax(fig, [0.52, 0.18, 0.44, 0.60], (0, 10), (0, 10))
        rows = [(8.3, 'speeding up:\na is positive', GREEN), (5.4, 'slowing down:\na is negative', PINK)]
        for y, txt, c in rows:
            arrow(ax, (0.4, y), (2.2, y), color=FG, lw=3)
            arrow(ax, (2.4, y), (4.3, y), color=c, lw=3.2, ms=30)
            label(ax, 4.9, y, txt, size=19, color=c, ha='left')
        ax.add_patch(Circle((1.6, 1.7), 1.2, fill=False, ec=MUT, lw=2, ls='--'))
        ax.add_patch(Circle((1.6, 2.9), 0.14, fc=YELLOW, ec='none'))
        arrow(ax, (1.6, 2.9), (3.0, 2.9), color=FG, lw=3)
        label(ax, 3.6, 1.9, 'constant speed round a circle:\nthe direction of v changes,\nso it still accelerates', size=18, color=YELLOW, ha='left')
    else:
        chip(fig, 'Element 2 · problems')
        teq(fig, 0.06, 0.70, r'$a^2 = b^2 + c^2 - 2bc\cos A$', size=34)
        _lines(fig, 0.06, 0.52, [(r'$R^2 = 5^2 + 8^2 - 2(5)(8)\cos 120^\circ = 129$', FG),
                                 (r'$R = 11.358\ \mathrm{km}$', FG)], size=24, gap=0.08)
        _sf(fig, 0.06, 0.36, '= 11.4 km (3 s.f.)')
        T(fig, 0.06, 0.29, 'Components agree: east 5 + 8cos60° = 9.0 km\nnorth 8sin60° = 6.93 km', size=22, color=SOFT)
        T(fig, 0.06, 0.15, 'Use the angle INSIDE the triangle (120°), not the turn (60°).', size=22, color=YELLOW)
        ax = wax(fig, [0.55, 0.14, 0.41, 0.62], (-0.5, 11), (-0.5, 8))
        ax.set_aspect('equal')
        p1 = (5, 0); p2 = (5 + 8 * math.cos(RAD(60)), 8 * math.sin(RAD(60)))
        arrow(ax, (0, 0), p1, color=C1, lw=4); arrow(ax, p1, p2, color=C2, lw=4); arrow(ax, (0, 0), p2, color=GREEN, lw=4)
        label(ax, 2.5, -0.5, '5.0 km', size=20, color=C1); label(ax, 8.6, 1.9, '8.0 km', size=20, color=C2)
        label(ax, 4.4, 4.3, 'R', size=24, color=GREEN)
        ax.add_patch(Arc(p1, 1.6, 1.6, theta1=60, theta2=180, color=YELLOW, lw=3))
        label(ax, 4.4, 1.0, '120°', size=19, color=YELLOW)


def _mini_graph(fig, rect, ylab, kind, size=17):
    """Constant-acceleration s-t, v-t or a-t graph from rest, axes unlabelled by numbers."""
    ax = gax(fig, rect, (0, 4.6), (-0.1, 8.3), 'time', ylab, ticks=False)
    t = np.linspace(0, 4, 100)
    if kind == 's':
        ax.plot(t, 0.5 * t ** 2, color=L.A1(), lw=4)
    elif kind == 'v':
        ax.plot(t, 2 * t / 2 * 1.0 + 0 * t, color=L.A1(), lw=4)
    else:
        ax.plot(t, 0 * t + 2.0, color=L.A1(), lw=4)
    return ax


def graphs(fig, s, ph):
    C1, C2 = C()
    if s == 2:
        header(fig, 'Sketching and reading graphs')
        bullets(fig, ['Area above the time axis: displacement one way', 'Area below it: displacement the other way (subtracts from\ndisplacement, adds to distance)',
                      'Straight ruled lines for constant acceleration', 'Label axes with units; mark intercepts and turning points',
                      'Going back? A new gradient: not a mirror image'], 5, 0.05, 0.78, size=23, dim=False)
        ax = gax(fig, [0.60, 0.20, 0.35, 0.50], (0, 5), (-3, 3.5), 'time (s)', 'velocity (m s⁻¹)', ticks=False)
        ax.plot([0, 2, 5], [3, 0, -2.4], color=GREEN, lw=4)
        ax.plot([2, 5], [0, -3 * 1.0], color=PINK, lw=2.5, ls='--')
        label(ax, 3.8, 1.3, 'correct: different\ngradient on return', size=17, color=GREEN)
        label(ax, 3.2, -2.3, 'mirror image: wrong', size=17, color=PINK)
        return
    header(fig, ['Constant acceleration, three graphs', 'How the graphs link'][s])
    ax1 = _mini_graph(fig, [0.06, 0.34, 0.26, 0.44], 'displacement', 's')
    ax2 = _mini_graph(fig, [0.37, 0.34, 0.26, 0.44], 'velocity', 'v')
    ax3 = _mini_graph(fig, [0.68, 0.34, 0.26, 0.44], 'acceleration', 'a')
    for ax, t_ in [(ax1, 'curve, getting steeper'), (ax2, 'straight line'), (ax3, 'flat line')]:
        ax.set_title(t_, color=FG, fontsize=20, pad=8)
    if s == 0:
        T(fig, 0.06, 0.24, 'Constant acceleration from rest:  s–t is a parabola,  v–t is a straight line,  a–t is flat.', size=24, color=FG)
        T(fig, 0.06, 0.16, 'The v–t graph is the one used most.', size=22, color=SOFT)
    else:
        fig.text(0.345, 0.69, 'gradient →', color=YELLOW, fontsize=20, ha='center', weight='bold')
        fig.text(0.655, 0.69, 'gradient →', color=YELLOW, fontsize=20, ha='center', weight='bold')
        fig.text(0.345, 0.64, '← area', color=GREEN, fontsize=20, ha='center', weight='bold')
        fig.text(0.655, 0.64, '← area', color=GREEN, fontsize=20, ha='center', weight='bold')
        T(fig, 0.06, 0.24, 'gradient of s–t = velocity     gradient of v–t = acceleration', size=24, color=YELLOW)
        T(fig, 0.06, 0.16, 'area under v–t = displacement     area under a–t = change in velocity', size=24, color=GREEN)
        t = np.linspace(0, 4, 40)
        ax2.fill_between(t, 0, t, color=GREEN, alpha=0.25)


def _van(t):
    t = np.asarray(t, float)
    v = np.where(t < 8, 2.5 * t, np.where(t < 18, 20.0, 20.0 - 4.0 * (t - 18)))
    return v


def we_graph(fig, s, ph):
    C1, C2 = C()
    if s == 2:
        header(fig, 'Worked example: building the other graphs')
        chip(fig, 'Element 3 · data')
        t = np.linspace(0, 23, 400)
        ts = [0, 8, 18, 23]
        ax1 = gax(fig, [0.06, 0.30, 0.28, 0.46], (0, 23), (0, 340), 'time (s)', 'displacement (m)')
        sdisp = np.where(t < 8, 1.25 * t ** 2, np.where(t < 18, 80 + 20 * (t - 8), 280 + 20 * (t - 18) - 2 * (t - 18) ** 2))
        ax1.plot(t, sdisp, color=C1, lw=4); ax1.set_xticks([0, 8, 18, 23]); ax1.set_yticks([0, 80, 280, 330])
        ax2 = gax(fig, [0.37, 0.30, 0.28, 0.46], (0, 23), (0, 24), 'time (s)', 'velocity (m s⁻¹)')
        ax2.plot(t, _van(t), color=C2, lw=4); ax2.set_xticks([0, 8, 18, 23]); ax2.set_yticks([0, 20])
        ax3 = gax(fig, [0.68, 0.30, 0.28, 0.46], (0, 23), (-6, 4), 'time (s)', 'acceleration (m s⁻²)')
        ax3.plot([0, 8], [2.5, 2.5], color=GREEN, lw=4); ax3.plot([8, 18], [0, 0], color=GREEN, lw=4); ax3.plot([18, 23], [-4, -4], color=GREEN, lw=4)
        ax3.set_xticks([0, 8, 18, 23]); ax3.set_yticks([-4, 0, 2.5])
        for ax in (ax1, ax2, ax3):
            for x in (8, 18):
                ax.axvline(x, color=GRID, lw=1.5, ls='--')
        T(fig, 0.06, 0.20, 'slope of s–t → v–t:  steeper, constant, flattening          slope of v–t → a–t:  +2.5, 0, −4.0 m s⁻²', size=21, color=SOFT)
        T(fig, 0.06, 0.13, 'Check the pieces join without jumps: the s–t graph is smooth.', size=21, color=YELLOW)
        return
    header(fig, 'Worked example: reading a journey')
    chip(fig, 'Element 3 · data')
    _q(fig, 'A van speeds up uniformly from rest to 20.0 m s⁻¹ in 8.00 s, travels at that steady speed for 10.0 s, then brakes\nuniformly to rest in 5.00 s. Find its displacement and its average velocity.', y=0.64, h=0.18)
    ax = gax(fig, [0.07, 0.12, 0.42, 0.42], (0, 23), (0, 24), 'time (s)', 'velocity (m s⁻¹)')
    t = np.linspace(0, 23, 300)
    ax.plot(t, _van(t), color=C2, lw=4); ax.set_xticks([0, 8, 18, 23]); ax.set_yticks([0, 20])
    ax.fill_between(t[t <= 8], 0, _van(t[t <= 8]), color=C1, alpha=0.3)
    if s >= 0:
        ax.fill_between(t[(t >= 8) & (t <= 18)], 0, 20, color=GREEN, alpha=0.25)
        ax.fill_between(t[t >= 18], 0, _van(t[t >= 18]), color=PINK, alpha=0.3)
    rows = [('area 1 = ½ × 8.00 × 20.0 = 80.0 m', C1), ('area 2 = 10.0 × 20.0 = 200 m', GREEN), ('area 3 = ½ × 5.00 × 20.0 = 50.0 m', PINK),
            ('displacement = 80 + 200 + 50 = 330 m', YELLOW)]
    n = 4
    if s == 0:
        _lines(fig, 0.54, 0.52, rows[:n], size=24, gap=0.075)
        _sf(fig, 0.54, 0.205, 'all inputs 3 s.f.: 330 m')
    else:
        _lines(fig, 0.54, 0.52, rows, size=24, gap=0.075)
        T(fig, 0.54, 0.235, r'average velocity $= \dfrac{330}{23.0} = 14.348\ \mathrm{m\ s^{-1}}$', size=26)
        _sf(fig, 0.54, 0.145, '= 14.3 m s⁻¹ (3 s.f.)')


def suvat(fig, s, ph):
    C1, C2 = C()
    header(fig, ['The equations of motion', 'Choosing an equation', 'Vertical motion under gravity'][s])
    if s <= 1:
        for k, e in enumerate([r'$v = u + at$', r'$s = ut + \frac{1}{2}at^2$', r'$2as = v^2 - u^2$']):
            meq(fig, 0.06, 0.70 - k * 0.17, e, size=34)
    if s == 0:
        card(fig, 0.52, 0.28, 0.43, 0.50, 'The letters', 'u  initial velocity\nv  final velocity\na  acceleration\ns  displacement\nt  time\n\nOnly for CONSTANT acceleration\nin a straight line',
             tcol=C2, size=23)
    elif s == 1:
        card(fig, 0.52, 0.30, 0.43, 0.48, 'Which one?', 'no final v:   s = ut + ½at²\nno time:       2as = v² − u²\nno displacement:   v = u + at\n\nPick a positive direction first;\nconvert km h⁻¹ ÷ 3.6 → m s⁻¹',
             tcol=C2, size=22)
        chip(fig, 'Element 2 · problems')
    else:
        geq(fig, 0.06, 0.70, r'$g = 9.81\ \mathrm{m\ s^{-2}}$', size=34)
        bullets(fig, ['Up positive: a = −9.81 m s⁻²', 'At the top v = 0, but a is still g', 'Back at the start, same speed as launch',
                      'Same time up as down (no air)'], 4, 0.06, 0.52, size=23, dim=False)
        ax = gax(fig, [0.58, 0.20, 0.37, 0.54], (0, 4.4), (-14, 14), 'time', 'velocity (up +)', ticks=False)
        ax.plot([0, 4], [12, -12], color=C1, lw=4)
        ax.scatter([2], [0], s=140, color=YELLOW, zorder=6)
        label(ax, 2.1, 2.6, 'top: v = 0', size=17, color=YELLOW, ha='left')
        label(ax, 0.2, 13.0, 'gradient = −g', size=17, color=FG, ha='left')
        ax.fill_between([0, 2], 0, [12, 0], color=GREEN, alpha=0.25); ax.fill_between([2, 4], 0, [0, -12], color=PINK, alpha=0.25)


def we_vertical(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a stone thrown upward')
    chip(fig, 'Element 2 · problems')
    _q(fig, 'A stone is thrown straight up at 12.0 m s⁻¹ from a bridge 30.0 m above a river. Find the speed with which it\nhits the water and how long it takes to get there. Up is positive.', y=0.64, h=0.18)
    rows = [(r'$u = +12.0$,  $a = -9.81$,  $s = -30.0$', SOFT)]
    if s >= 0:
        rows += [(r'$v^2 = u^2 + 2as = 144.0 + 588.6 = 732.6$', FG), (r'$v = -27.067\ \mathrm{m\ s^{-1}}$  (down)', FG)]
    y = _lines(fig, 0.06, 0.58, rows, size=24, gap=0.07)
    if s == 0:
        _sf(fig, 0.06, y + 0.015, 'speed = 27.1 m s⁻¹ (3 s.f.)')
    if s >= 1:
        _sf(fig, 0.06, y + 0.015, 'speed = 27.1 m s⁻¹ (3 s.f.)')
        T(fig, 0.06, y - 0.045, r'$t = \dfrac{v - u}{a} = \dfrac{-27.067 - 12.0}{-9.81} = 3.9823\ \mathrm{s}$', size=24)
        _sf(fig, 0.06, y - 0.135, '= 3.98 s (3 s.f.)')
    if s >= 2:
        T(fig, 0.06, y - 0.205, 'Check: up 1.22 s to 7.34 m; fall 37.3 m in 2.76 s: ½ g t² = 37.3 m ✓', size=22, color=YELLOW)
    ax = wax(fig, [0.70, 0.08, 0.26, 0.50], (0, 4), (-0.5, 7))
    ax.add_patch(Rectangle((0.2, 4.8), 2.4, 0.3, fc=MUT, ec='none'))
    ax.add_patch(Rectangle((0, 0), 4, 0.5, fc=C1, alpha=0.5, ec='none'))
    label(ax, 3.2, 0.25, 'river', size=17, color=FG)
    label(ax, 1.4, 5.4, 'bridge', size=17, color=FG)
    arrow(ax, (1.0, 5.1), (1.0, 6.7), color=GREEN, lw=3.5)
    label(ax, 1.9, 6.2, 'u = 12.0', size=17, color=GREEN)
    ax.annotate('', xy=(3.3, 4.8), xytext=(3.3, 0.55), arrowprops=dict(arrowstyle='<|-|>', color=YELLOW, lw=2.5))
    label(ax, 3.45, 2.7, '30.0 m', size=17, color=YELLOW, ha='left')


def terminal(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Terminal velocity', 'Opening a parachute'][s])
    ax = gax(fig, [0.06, 0.18, 0.40, 0.60], (0, 10), (0, 1.35), 'time', 'speed', ticks=False)
    t = np.linspace(0, 10, 200)
    k = 0.5 - 0.5 * math.cos(TAU * ph)
    if s == 0:
        ax.plot(t, np.tanh(t / 2.5), color=C1, lw=4)
        ax.axhline(1.0, color=YELLOW, lw=2, ls='--'); label(ax, 8.2, 1.1, 'terminal velocity', size=17, color=YELLOW)
        tt = 9.5 * k; v = math.tanh(tt / 2.5); D = v
    else:
        pre = np.tanh(t[t <= 4] / 2.0)
        ax.plot(t[t <= 4], pre, color=C1, lw=4)
        post = 0.55 + (pre[-1] - 0.55) * np.exp(-(t[t > 4] - 4) / 1.2)
        ax.plot(t[t > 4], post, color=GREEN, lw=4)
        ax.axhline(1.0, color=MUT, lw=1.5, ls='--'); ax.axhline(0.55, color=YELLOW, lw=2, ls='--')
        label(ax, 8.0, 0.40, 'new, smaller terminal velocity', size=16, color=YELLOW)
        label(ax, 2.0, 1.1, 'before opening', size=16, color=C1); label(ax, 7.2, 0.85, 'after opening', size=16, color=GREEN)
        tt = 4 + 5.5 * k; v = 0.55 + (pre[-1] - 0.55) * math.exp(-(tt - 4) / 1.2); D = v / 0.55
    ax.scatter([tt], [v], s=170, color=PINK, zorder=7)
    ax2 = wax(fig, [0.50, 0.16, 0.14, 0.64], (-1, 1), (-2.6, 2.6))
    ax2.add_patch(Circle((0, 0), 0.3, fc=FG, ec='none'))
    arrow(ax2, (0, -0.3), (0, -1.5), color=C2, lw=5)
    arrow(ax2, (0, 0.3), (0, 0.3 + 1.2 * min(D, 1.9)), color=PINK, lw=5)
    label(ax2, 0, -2.2, 'weight', size=19, color=C2); label(ax2, 0, 2.4, 'air resistance', size=19, color=PINK)
    if s == 0:
        bullets(fig, ['Weight is constant;\nair resistance rises with speed', 'Net force and acceleration\nfall to zero', 'Forces balanced:\nconstant speed', 'The acceleration reaches\nzero, not the speed'],
                4, 0.67, 0.76, size=20, dim=False)
    else:
        bullets(fig, ['Parachute: resistance is\ngreater than weight, so the\nnet force is up', 'Slows down; resistance falls', 'Balanced again at a lower\nterminal velocity'], 3, 0.67, 0.76, size=20, dim=False)
        chip(fig, 'Element 4 · predictions')


# ============================================================================ part 2: projectiles
def _arc(u, th, H=0.0):
    vx, vy = u * math.cos(RAD(th)), u * math.sin(RAD(th))
    tf = (vy + math.sqrt(vy ** 2 + 2 * g * H)) / g
    return vx, vy, tf


def _work(fig, x, y, items, size=23, gap=0.068, sfgap=0.043):
    """Working lines: (text, colour, rounded-answer-or-None).  Returns the y below the last line."""
    for st, c, sf in items:
        T(fig, x, y, st, size=size, color=c)
        y -= gap
        if sf:
            _sf(fig, x, y + 0.012, sf)
            y -= sfgap
    return y


def _ground_axes(fig, rect, xlim, ylim):
    ax = wax(fig, rect, xlim, ylim)
    ax.set_aspect('equal')
    ax.plot([xlim[0], xlim[1]], [0, 0], color=MUT, lw=3)
    return ax


def projectile(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Two independent motions', 'Components of the launch velocity', 'Time of flight, range and greatest height'][s])
    u, th = 22.0, 35.0
    vx, vy, tf = _arc(u, th)
    R = vx * tf
    ax = _ground_axes(fig, [0.04, 0.14, 0.58, 0.62], (-3, 54), (-3, 22))
    tt = np.linspace(0, tf, 120)
    ax.plot(vx * tt, vy * tt - 0.5 * g * tt ** 2, color=MUT, lw=2.5, ls='--')
    for k in range(1, 10):                      # equal time steps: equal horizontal gaps
        t_ = tf * k / 10
        ax.scatter([vx * t_], [vy * t_ - 0.5 * g * t_ ** 2], s=70, color=SOFT, zorder=4)
        ax.scatter([vx * t_], [0], s=40, color=C1, zorder=4)
    if s == 0:
        t_ = tf * ph
        bx, by = vx * t_, vy * t_ - 0.5 * g * t_ ** 2
        ax.scatter([bx], [by], s=420, color=YELLOW, edgecolor=BG, linewidth=3, zorder=8)
        ax.scatter([bx], [-1.2], s=150, color=C1, zorder=8)
        ax.scatter([R + 4], [by], s=150, color=PINK, zorder=8)
        ax.plot([R + 4, R + 4], [0, 12], color=PINK, lw=1.5, alpha=0.5)
        label(ax, 24, -2.4, 'horizontal shadow: equal gaps', size=17, color=C1)
        label(ax, R + 4.0, 13.6, 'vertical shadow:\nup, then down', size=17, color=PINK)
        bullets(fig, ['Horizontal: no force, so\nconstant velocity', 'Vertical: constant\nacceleration g, downward', 'Time is the link between\nthe two parts'],
                3, 0.65, 0.70, size=22, dim=False)
    else:
        arrow(ax, (0, 0), (vx * 0.9, vy * 0.9), color=YELLOW, lw=4)
        ax.plot([0, vx * 0.9], [0, 0], color=C1, lw=4); ax.plot([vx * 0.9, vx * 0.9], [0, vy * 0.9], color=PINK, lw=4)
        label(ax, vx * 0.45, -1.6, 'u cos θ', size=20, color=C1); label(ax, vx * 0.9 + 3.6, vy * 0.45, 'u sin θ', size=20, color=PINK)
        label(ax, 5.2, 4.3, 'u', size=22, color=YELLOW); ax.add_patch(Arc((0, 0), 12, 12, theta1=0, theta2=35, color=FG, lw=2.5)); label(ax, 8.0, 1.5, 'θ', size=19)
    if s == 1:
        learn_eq(fig, 0.64, 0.70, r'$v_x = u\cos\theta$  (constant)', size=26)
        learn_eq(fig, 0.64, 0.52, r'$v_y = u\sin\theta - gt$', size=26)
        T(fig, 0.64, 0.33, 'speed = √(vx² + vy²)\ndirection: tan⁻¹(vy / vx)\nat the top, vy = 0', size=22, color=SOFT)
    if s == 2:
        learn_eq(fig, 0.64, 0.72, r'$t = \dfrac{2u\sin\theta}{g}$', size=28)
        learn_eq(fig, 0.64, 0.50, r'$\mathrm{range} = u\cos\theta \times t$', size=26)
        learn_eq(fig, 0.64, 0.30, r'$H = \dfrac{(u\sin\theta)^2}{2g}$', size=28)
        T(fig, 0.64, 0.14, 'Level ground only. Different height:\nuse the full equations of motion.', size=20, color=YELLOW)
        ax.annotate('', xy=(R, -2.6), xytext=(0, -2.6), arrowprops=dict(arrowstyle='<|-|>', color=GREEN, lw=2.5))
        label(ax, R / 2, -2.2, 'range', size=18, color=GREEN)


def we_proj(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a kicked rugby ball')
    chip(fig, 'Element 2 · problems')
    _q(fig, 'A rugby ball is kicked at 79.2 km h⁻¹, 35.0° above the horizontal, over level ground. Find its velocity components,\nthe time of flight, the range and the greatest height. Ignore air resistance.', y=0.66, h=0.16, size=21)
    vx, vy, tf = _arc(22.0, 35.0)
    R = vx * tf
    ax = _ground_axes(fig, [0.03, 0.08, 0.42, 0.50], (-2, 52), (-3, 14))
    tt = np.linspace(0, tf, 100)
    ax.plot(vx * tt, vy * tt - 0.5 * g * tt ** 2, color=C1, lw=4)
    arrow(ax, (0, 0), (vx * 0.6, vy * 0.6), color=YELLOW, lw=3.5)
    label(ax, 5, 4.5, '22.0 m s⁻¹', size=17, color=YELLOW)
    ax.add_patch(Arc((0, 0), 9, 9, theta1=0, theta2=35, color=FG, lw=2)); label(ax, 8.2, 1.4, '35.0°', size=16)
    items = [('u = 79.2 ÷ 3.6 = 22.0 m s⁻¹', SOFT, None),
             (r'$u_x = 22.0\cos 35.0^\circ = 18.021\ \mathrm{m\ s^{-1}}$', FG, '= 18.0 m s⁻¹ (3 s.f.)'),
             (r'$u_y = 22.0\sin 35.0^\circ = 12.619\ \mathrm{m\ s^{-1}}$', FG, '= 12.6 m s⁻¹ (3 s.f.)')]
    if s >= 1:
        items = [(r'$u_x = 18.021$,  $u_y = 12.619\ \mathrm{m\ s^{-1}}$ (unrounded)', SOFT, None),
                 (r'$t = \dfrac{2u_y}{g} = \dfrac{2(12.619)}{9.81} = 2.5726\ \mathrm{s}$', FG, '= 2.57 s (3 s.f.)'),
                 (r'range $= u_x t = 18.021\times 2.5726 = 46.362\ \mathrm{m}$', FG, '= 46.4 m (3 s.f.)')]
    if s >= 2:
        items = [(r'$H = \dfrac{u_y^2}{2g} = \dfrac{12.619^2}{2(9.81)} = 8.1158\ \mathrm{m}$', FG, '= 8.12 m (3 s.f.)'),
                 ('At the top: speed = ux = 18.0 m s⁻¹ (vy = 0)', YELLOW, None),
                 ('Lands at 22.0 m s⁻¹, 35.0° below the horizontal', YELLOW, None)]
    _work(fig, 0.48, 0.58, items, size=22, gap=0.075, sfgap=0.042)
    if s >= 2:
        ax.scatter([vx * tf / 2], [vy ** 2 / (2 * g)], s=200, color=PINK, zorder=7)
        label(ax, vx * tf / 2, vy ** 2 / (2 * g) + 1.6, 'top', size=17, color=PINK)


def proj_levels(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Landing at a different height')
    chip(fig, 'Element 2 · problems')
    cx, cy, tc = *_arc(15.0, 40.0, 12.0)[:2], _arc(15.0, 40.0, 12.0)[2]
    if s == 0:
        _q(fig, 'A ball is thrown at 15.0 m s⁻¹, 40.0° above the horizontal, from the top of a cliff 12.0 m above the sea. Find the\ntime in the air, the range, and the speed and angle at which it hits the sea.', y=0.66, h=0.16, size=21)
    ax = wax(fig, [0.03, 0.06, 0.46, 0.56 if s == 0 else 0.70], (-4, 37), (-3, 19 if s == 0 else 22))
    ax.set_aspect('equal')
    ax.add_patch(Rectangle((-4, 0), 4, 12, fc=MUT, ec='none')); ax.plot([-4, 37], [0, 0], color=C1, lw=4)
    tt = np.linspace(0, tc, 100)
    ax.plot(cx * tt, 12 + cy * tt - 0.5 * g * tt ** 2, color=C2, lw=4)
    arrow(ax, (0, 12), (cx * 0.5, 12 + cy * 0.5), color=YELLOW, lw=3.5)
    if s >= 1:
        ax.scatter([cx * cy / g], [12 + cy ** 2 / (2 * g)], s=170, color=PINK, zorder=7)
        label(ax, cx * cy / g, 12 + cy ** 2 / (2 * g) + 1.9, 'top: 4.74 m above cliff', size=16, color=PINK)
    if s == 0:
        _work(fig, 0.52, 0.60, [(r'$u_x = 15.0\cos 40.0^\circ = 11.491\ \mathrm{m\ s^{-1}}$', FG, '= 11.5 m s⁻¹ (3 s.f.)'),
                                (r'$u_y = 15.0\sin 40.0^\circ = 9.6418\ \mathrm{m\ s^{-1}}$', FG, '= 9.64 m s⁻¹ (3 s.f.)')], size=22, gap=0.075)
        T(fig, 0.52, 0.30, 'Launch BELOW the horizontal?\nThen uy is negative. Keep every sign\nconsistent with one positive direction.', size=21, color=YELLOW)
    elif s == 1:
        T(fig, 0.52, 0.80, 'Method A: rise, then fall', size=24, color=C1, weight='bold')
        _work(fig, 0.52, 0.72, [(r'rise: $t = \dfrac{9.6418}{9.81} = 0.9829\ \mathrm{s}$,  $h = 4.738\ \mathrm{m}$', FG, None),
                                (r'fall $= 12.0 + 4.738 = 16.738\ \mathrm{m}$', FG, None),
                                (r'$t = \sqrt{\dfrac{2(16.738)}{9.81}} = 1.8473\ \mathrm{s}$', FG, None),
                                (r'total $= 0.9829 + 1.8473 = 2.8301\ \mathrm{s}$', YELLOW, '= 2.83 s (3 s.f.)')], size=22, gap=0.075)
        T(fig, 0.52, 0.19, 'Method B (quadratic): −12.0 = 9.6418t − 4.905t²\ngives the same t, with more places to slip.', size=19, color=SOFT)
    else:
        _work(fig, 0.52, 0.80, [('range = ux × t = 11.491 × 2.8301 = 32.520 m', FG, '= 32.5 m (3 s.f.)'),
                                (r'$v_y = 9.6418 - 9.81(2.8301) = -18.122\ \mathrm{m\ s^{-1}}$', FG, None),
                                (r'speed $= \sqrt{11.491^2 + 18.122^2} = 21.458\ \mathrm{m\ s^{-1}}$', FG, '= 21.5 m s⁻¹ (3 s.f.)'),
                                (r'angle $= \tan^{-1}\dfrac{18.122}{11.491} = 57.622^\circ$ below horizontal', FG, '= 57.6° (3 s.f.)')], size=21, gap=0.075)
        T(fig, 0.52, 0.22, 'Check by energy: v = √(15.0² + 2 × 9.81 × 12.0)\n= 21.5 m s⁻¹ ✓', size=21, color=YELLOW)
        chip(fig, 'Element 2 · validity')


def proj_derive(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Deriving a launch speed', 'A result that does not depend on g', 'The same shot on another world'][s])
    if s == 0:
        chip(fig, 'Element 2 · problems')
        _work(fig, 0.06, 0.78, [('Horizontal:   u cosθ = R / t', FG, None),
                                ('Vertical, level ground:   u sinθ = g (t/2) = 4.905 t', FG, None),
                                ('Eliminate t:   u² = g R / (2 sinθ cosθ)', FG, None),
                                ('R = 90.0 m, θ = 30.0°:   u² = 1019.5', FG, None),
                                (r'$u = 31.929\ \mathrm{m\ s^{-1}}$', FG, '= 31.9 m s⁻¹ (3 s.f.)')], size=25, gap=0.085)
        T(fig, 0.06, 0.18, 'Equate two expressions for the same component, then eliminate t.', size=22, color=YELLOW)
        ax = _ground_axes(fig, [0.62, 0.20, 0.34, 0.45], (-3, 100), (-3, 40))
        xs = np.linspace(0, 90, 80)
        ax.plot(xs, xs * math.tan(RAD(30)) - g * xs ** 2 / (2 * 31.929 ** 2 * math.cos(RAD(30)) ** 2), color=C1, lw=4)
        label(ax, 45, -3.0, 'R = 90.0 m', size=19, color=GREEN); ax.add_patch(Arc((0, 0), 20, 20, theta1=0, theta2=30, color=FG, lw=2)); label(ax, 20, 3.0, '30.0°', size=16)
    elif s == 1:
        chip(fig, 'Element 1 · principles')
        ax = wax(fig, [0.06, 0.14, 0.44, 0.64], (-1, 12), (-1.5, 9))
        ax.set_aspect('equal')
        th = np.linspace(0, math.pi / 2, 50)
        ax.plot(5 - 4 * np.cos(th), 8 - 4 * np.sin(th), color=MUT, lw=5)
        ax.add_patch(Rectangle((5, 3.9), 2.2, 0.35, fc=MUT, ec='none')); ax.add_patch(Rectangle((6.4, 0), 0.5, 3.9, fc=MUT, ec='none'))
        ax.plot([-1, 12], [0, 0], color=MUT, lw=3)
        tt = np.linspace(0, 1.6, 60)
        ax.plot(7.2 + 3.4 * tt, 4.25 - 2.08 * tt ** 2, color=C1, lw=4, ls='--')
        label(ax, 1.5, 8.7, 'drop D', size=19, color=YELLOW, ha='left'); label(ax, 8.9, 2.3, 'h', size=19, color=YELLOW)
        label(ax, 10.0, 0.5, 'x', size=19, color=GREEN)
        _work(fig, 0.54, 0.78, [(r'energy:  $\frac{1}{2}mv^2 = mgD \Rightarrow v = \sqrt{2gD}$', FG, None),
                                (r'fall:  $h = \frac{1}{2}gt^2 \Rightarrow t = \sqrt{2h/g}$', FG, None),
                                (r'$x = vt = \sqrt{2gD}\,\sqrt{2h/g} = 2\sqrt{Dh}$', GREEN, None)], size=24, gap=0.095)
        T(fig, 0.54, 0.40, 'No g in the answer: v and t both depend on g,\nbut the effects cancel. So x is the same on the Moon.', size=22, color=YELLOW)
    else:
        chip(fig, 'Element 4 · predictions')
        rows = [('', 'Earth', 'Mars'), ('g (m s⁻²)', '9.81', '3.72'), ('time of flight', 't', '2.64 t'), ('range', 'R', '2.64 R')]
        for i, r in enumerate(rows):
            y = 0.72 - i * 0.105
            box(fig, 0.05, y - 0.045, 0.50, 0.085, fc=PANEL if i % 2 else PANEL2)
            for j, c in enumerate(r):
                T(fig, [0.07, 0.27, 0.41][j], y, c, size=24, color=[SOFT, C1, C2][j] if i == 0 else FG, va='center', weight='bold' if i == 0 else 'normal')
        T(fig, 0.05, 0.24, 't ∝ 1/g and range ∝ 1/g (same speed and angle)', size=22, color=YELLOW)
        bullets(fig, ['Weaker g: the vertical velocity\nchanges more slowly', 'So the object stays up longer', 'Horizontal velocity unchanged:\nit goes further'],
                3, 0.60, 0.72, size=22, dim=False)
        T(fig, 0.60, 0.30, 'Say all of it: a bare ratio is only\na partial answer.', size=22, color=PINK)


# ============================================================================ part 3: forces
def _block(ax, c, w=1.6, h=1.0, ang=0.0, fc=PANEL2, ec=FG, lw=3):
    """Rectangle centred at c, rotated by ang degrees."""
    a = RAD(ang)
    pts = []
    for dx, dy in [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]:
        pts.append((c[0] + dx * math.cos(a) - dy * math.sin(a), c[1] + dx * math.sin(a) + dy * math.cos(a)))
    ax.add_patch(Polygon(pts, fc=fc, ec=ec, lw=lw, zorder=3))


def forces(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Free body diagrams', 'Newton’s first law and balanced forces', 'Several forces on a slope'][s])
    if s == 0:
        ax = wax(fig, [0.04, 0.14, 0.50, 0.62], (-4, 6), (-3, 4))
        ax.set_aspect('equal')
        ax.plot([-4, 6], [-1, -1], color=MUT, lw=3)
        _block(ax, (1, -0.4), 1.6, 1.2)
        _vec(ax, (1, -0.4), (1, -2.4), color=C2, text='weight', tp=(2.1, -2.0))
        _vec(ax, (1, -0.4), (1, 1.6), color=GREEN, text='normal', tp=(2.0, 1.4))
        _vec(ax, (1.8, -0.4), (4.4, -0.4), color=YELLOW, text='push', tp=(3.4, 0.0))
        _vec(ax, (0.2, -0.4), (-1.0, -0.4), color=PINK, text='friction', tp=(-1.2, 0.15))
        bullets(fig, ['One object, an arrow for every force on it', 'Arrows start on the object; label each one',
                      'Roughly to scale: balanced forces look balanced', 'No forces the object exerts on others',
                      'Never draw net or centripetal force as an extra arrow'], 5, 0.56, 0.76, size=21, dim=False)
        T(fig, 0.56, 0.20, 'Here: weight = normal (no vertical motion),\npush > friction (accelerates right).', size=20, color=SOFT)
        chip(fig, 'Element 1 · principles')
    elif s == 1:
        ax = wax(fig, [0.04, 0.34, 0.50, 0.42], (-4, 6), (-2, 3))
        ax.set_aspect('equal')
        ax.plot([-4, 6], [-1, -1], color=MUT, lw=3)
        _block(ax, (1, -0.3), 2.6, 1.0)
        _vec(ax, (2.3, -0.3), (4.5, -0.3), color=YELLOW, text='engine', tp=(3.5, 0.2))
        _vec(ax, (-0.3, -0.3), (-2.5, -0.3), color=PINK, text='drag', tp=(-1.4, 0.2))
        _vec(ax, (1, -0.3), (1, 1.7), color=GREEN, text='normal', tp=(2.0, 1.5))
        _vec(ax, (1, -0.3), (1, -2.3), color=C2, text='weight', tp=(2.0, -2.0))
        T(fig, 0.06, 0.28, 'A car at steady speed: balanced forces,\nso the acceleration is zero (velocity constant).', size=22, color=FG)
        box(fig, 0.57, 0.20, 0.38, 0.56)
        T(fig, 0.59, 0.73, 'Balanced:  ΣF = 0', size=24, color=GREEN, weight='bold')
        T(fig, 0.59, 0.66, 'a = 0:  at rest, or constant velocity', size=20, color=SOFT)
        T(fig, 0.59, 0.55, 'Unbalanced:  ΣF ≠ 0', size=24, color=PINK, weight='bold')
        T(fig, 0.59, 0.48, 'acceleration, in the direction of ΣF', size=20, color=SOFT)
        T(fig, 0.59, 0.36, 'In 2D: balance each direction\nseparately (horizontal, vertical)', size=20, color=FG)
        T(fig, 0.59, 0.25, 'Name the law and the object.', size=20, color=YELLOW)
    else:
        chip(fig, 'Element 1 · principles')
        th = 30.0
        ax = wax(fig, [0.03, 0.12, 0.58, 0.66], (-1, 12), (-1.5, 7))
        ax.set_aspect('equal')
        L_ = 11.0
        ax.fill([0, L_ * math.cos(RAD(th)), L_ * math.cos(RAD(th))], [0, L_ * math.sin(RAD(th)), 0], color=PANEL, zorder=1)
        ax.plot([0, L_ * math.cos(RAD(th))], [0, L_ * math.sin(RAD(th))], color=MUT, lw=4)
        u = np.array([math.cos(RAD(th)), math.sin(RAD(th))]); n = np.array([-u[1], u[0]])
        c = 5.5 * u + 0.55 * n
        _block(ax, c, 1.4, 1.1, th)
        _vec(ax, c, c + 2.6 * u, color=YELLOW, text='tension', tp=c + 3.4 * u + 0.5 * n)
        _vec(ax, c, c - 1.4 * u, color=PINK, text='friction', tp=c - 2.6 * u + 0.4 * n)
        _vec(ax, c, c + 2.0 * n, color=GREEN, text='normal', tp=c + 2.7 * n)
        _vec(ax, c, c + np.array([0, -2.6]), color=C2, text='weight', tp=c + np.array([0.9, -2.9]))
        bullets(fig, ['Weight: straight down', 'Normal force: at right angles to the slope', 'Friction: along the slope, against the motion',
                      'Tension: along the rope', 'Constant velocity: balanced along\nand across the slope'], 5, 0.63, 0.76, size=20, dim=False)


def incline(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Weight components on a slope', 'Checking sine and cosine'][s])
    th = 30.0
    u = np.array([math.cos(RAD(th)), math.sin(RAD(th))]); n = np.array([-u[1], u[0]])
    if s == 0:
        chip(fig, 'Element 1 · principles')
        ax = wax(fig, [0.03, 0.10, 0.56, 0.70], (-1, 12), (-1.5, 7.5))
        ax.set_aspect('equal')
        L_ = 11.0
        ax.fill([0, L_ * u[0], L_ * u[0]], [0, L_ * u[1], 0], color=PANEL, zorder=1)
        ax.plot([0, L_ * u[0]], [0, L_ * u[1]], color=MUT, lw=4)
        c = 6.0 * u + 0.55 * n
        _block(ax, c, 1.4, 1.1, th)
        W = np.array([0, -3.2])
        _vec(ax, c, c + W, color=C2, text='mg', tp=c + W + np.array([0.5, -0.4]))
        _vec(ax, c, c - 1.6 * u, color=PINK, lw=3, text='mg sin θ', tp=c - 2.9 * u + 0.5 * n, size=17)
        _vec(ax, c, c - 2.77 * n, color=YELLOW, lw=3, text='mg cos θ', tp=c - 3.3 * n + 0.9 * u, size=17)
        ax.plot([c[0] + W[0], c[0] - 1.6 * u[0] + 0], [c[1] + W[1], c[1] - 1.6 * u[1]], color=GRID, lw=1.5, ls='--')
        ax.add_patch(Arc((0, 0), 4.2, 4.2, theta1=0, theta2=th, color=FG, lw=2.5)); label(ax, 2.7, 0.5, 'θ', size=20)
        learn_eq(fig, 0.62, 0.74, r'$mg\sin\theta$  along the slope', size=24)
        learn_eq(fig, 0.62, 0.52, r'$mg\cos\theta$  into the slope', size=24)
        T(fig, 0.62, 0.31, 'Normal force balances mg cosθ.\nFriction acts along the slope.\nNormal and friction are the two\ncomponents of the contact force.', size=20, color=SOFT)
    else:
        for k, (ang, txt, c) in enumerate([(0, 'flat: θ = 0\nalong the slope: 0\n= mg sin 0 ✓', GREEN), (90, 'vertical: θ = 90°\nwhole weight along it\n= mg sin 90° ✓', YELLOW)]):
            ax = wax(fig, [0.04 + k * 0.24, 0.40, 0.22, 0.38], (-1, 5), (-1, 5))
            ax.set_aspect('equal')
            uu = np.array([math.cos(RAD(ang)), math.sin(RAD(ang))])
            ax.plot([0, 4.5 * uu[0]], [0, 4.5 * uu[1]], color=MUT, lw=4)
            _vec(ax, (2.0 * uu[0] + 0.6 * (-uu[1]), 2.0 * uu[1] + 0.6 * uu[0]), (2.0 * uu[0] + 0.6 * (-uu[1]), 2.0 * uu[1] + 0.6 * uu[0] - 1.8), color=C2, lw=3)
            T(fig, 0.05 + k * 0.24, 0.35, txt, size=19, color=c)
        bullets(fig, ['Friction opposes sliding', 'Up the slope: friction AND mg sinθ both slow the cart', 'Down the slope: friction points up the slope,\nso the net force is smaller',
                      'The way down is not a mirror image of the way up'], 4, 0.52, 0.76, size=21, dim=False)
        T(fig, 0.05, 0.18, 'The wrong trigonometric ratio is a common slip: sketch the triangle.', size=22, color=YELLOW)


def we_incline(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a crate on a slope')
    chip(fig, 'Element 2 · problems')
    th = 30.0
    u = np.array([math.cos(RAD(th)), math.sin(RAD(th))]); n = np.array([-u[1], u[0]])
    if s == 0:
        _q(fig, 'A crate of 8.50 kg is pulled up a 30.0° slope at constant speed by a rope that pulls with 60.0 N along the slope.\nFind the friction force.', y=0.66, h=0.16, size=21)
    if s <= 1:
        ax = wax(fig, [0.03, 0.06, 0.44, 0.52 if s == 0 else 0.70], (-1, 11), (-1.5, 6.5 if s == 0 else 8.5))
        ax.set_aspect('equal')
        L_ = 10.0
        ax.fill([0, L_ * u[0], L_ * u[0]], [0, L_ * u[1], 0], color=PANEL, zorder=1)
        ax.plot([0, L_ * u[0]], [0, L_ * u[1]], color=MUT, lw=4)
        c = 5.0 * u + 0.55 * n
        _block(ax, c, 1.3, 1.0, th)
        if s == 0:
            _vec(ax, c, c + 2.8 * u, color=YELLOW, text='60.0 N', tp=c + 3.7 * u + 0.5 * n, size=17)
            _vec(ax, c, c - 1.6 * u, color=PINK, text='f', tp=c - 2.3 * u + 0.5 * n, size=17)
            _vec(ax, c, c + np.array([0, -2.5]), color=C2, lw=3, text='mg', tp=c + np.array([0.7, -2.7]), size=17)
            _vec(ax, c, c + 1.9 * n, color=GREEN, lw=3, text='N', tp=c + 2.4 * n, size=17)
        else:
            _vec(ax, c, c - 2.4 * u, color=C2, text='mg sin θ', tp=c - 3.6 * u + 0.5 * n, size=16)
            _vec(ax, c + 0.5 * n, c + 0.5 * n - 1.4 * u, color=PINK, text='f', tp=c - 2.4 * u + 1.2 * n, size=16)
            label(ax, 7.5, 6.8, 'rope cut: moving up at 2.40 m s⁻¹', size=16, color=YELLOW)
    if s == 0:
        _work(fig, 0.50, 0.58, [('Constant speed: forces along the slope balance', SOFT, None),
                                (r'$T - mg\sin\theta - f = 0$', FG, None),
                                (r'$mg\sin\theta = 8.50\times 9.81\times\sin 30.0^\circ = 41.69\ \mathrm{N}$', FG, None),
                                (r'$f = 60.0 - 41.69 = 18.308\ \mathrm{N}$  down the slope', FG, '= 18.3 N (3 s.f.)')], size=22, gap=0.075)
    elif s == 1:
        _work(fig, 0.50, 0.78, [('Net force along the slope, both down the slope:', SOFT, None),
                                (r'$F = mg\sin\theta + f = 41.69 + 18.308 = 60.0\ \mathrm{N}$', FG, None),
                                (r'$a = 60.0 / 8.50 = 7.0588\ \mathrm{m\ s^{-2}}$ (slowing)', FG, '= 7.06 m s⁻² (3 s.f.)'),
                                (r'$s = \dfrac{u^2}{2a} = \dfrac{2.40^2}{2(7.0588)} = 0.40800\ \mathrm{m}$', FG, '= 0.408 m (3 s.f.)')], size=22, gap=0.095)
    else:
        header_ = None
        ax = gax(fig, [0.07, 0.14, 0.42, 0.60], (0, 1.0), (-2.2, 3.0), 'time since the cut (s)', 'velocity (m s⁻¹, up +)')
        ax.plot([0, 0.34], [2.40, 0], color=C1, lw=4); ax.plot([0.34, 0.8846], [0, -1.4983], color=GREEN, lw=4)
        ax.scatter([0, 0.34, 0.8846], [2.40, 0, -1.4983], s=90, color=YELLOW, zorder=6)
        label(ax, 0.17, 1.65, 'a = −7.06', size=16, color=C1); label(ax, 0.66, -0.4, 'a = −2.75', size=16, color=GREEN)
        ax.set_xticks([0, 0.34, 0.88]); ax.set_yticks([-1.5, 0, 2.4])
        _work(fig, 0.53, 0.76, [(r'down: $a = \dfrac{mg\sin\theta - f}{m} = \dfrac{41.69 - 18.308}{8.50}$', FG, None),
                                (r'$a = 2.7512\ \mathrm{m\ s^{-2}}$', FG, '= 2.75 m s⁻² (3 s.f.)'),
                                (r'$v = \sqrt{2(2.7512)(0.408)} = 1.4983\ \mathrm{m\ s^{-1}}$', FG, '= 1.50 m s⁻¹ (3 s.f.)')], size=22, gap=0.075)
        T(fig, 0.53, 0.30, 'Two straight lines, two gradients.\n1.50 < 2.40: friction removed energy ✓', size=21, color=YELLOW)


def newton2(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Newton’s second law', 'Momentum form, mass and weight', 'Worked example: scales in a lift'][s])
    if s == 0:
        meq(fig, 0.06, 0.70, r'$F_{net} = \dfrac{\Delta(mv)}{\Delta t} = ma$', size=36)
        geq(fig, 0.06, 0.42, r'$F_g = mg$,   $g = 9.81\ \mathrm{N\ kg^{-1}}$', size=32)
        bullets(fig, ['F_net: the vector sum of ALL the forces', 'a points the same way as F_net', 'Mass in kg (tonnes × 1000); force in N'], 3, 0.06, 0.24, size=22, dim=False)
        ax = wax(fig, [0.62, 0.20, 0.34, 0.55], (-2, 4), (-3, 3.5))
        ax.set_aspect('equal')
        _block(ax, (0.5, 0), 1.6, 1.2)
        _vec(ax, (1.3, 0), (3.6, 0), color=GREEN, lw=5, text='F_net', tp=(2.5, 0.5))
        _vec(ax, (0.5, 1.5), (2.8, 1.5), color=YELLOW, lw=3, text='a (same direction)', tp=(1.5, 2.0), size=16)
    elif s == 1:
        learn_eq(fig, 0.06, 0.70, r'$F = \dfrac{m(v-u)}{\Delta t}$   (m constant: $= ma$)', size=28)
        bullets(fig, ['Double the net force: double the acceleration', 'Double the mass: half the acceleration',
                      'Mass (kg) does not change in a lift', 'Weight (N) and the push of the floor are forces',
                      'Scales read the force from the floor'], 5, 0.06, 0.50, size=23, dim=False)
        chip(fig, 'Element 1 · principles')
    else:
        chip(fig, 'Element 2 · problems')
        _q(fig, 'A 70.0 kg person stands on scales in a lift. The scales read 76.5 kg. Find the lift’s acceleration.', y=0.68, h=0.14, size=21)
        ax = wax(fig, [0.04, 0.08, 0.30, 0.56], (-2, 3), (-3, 3))
        ax.set_aspect('equal')
        ax.add_patch(Rectangle((-1.3, -2.4), 2.6, 4.8, fc=PANEL, ec=MUT, lw=3))
        ax.add_patch(Circle((0, 1.4), 0.4, fc=FG, ec='none')); ax.plot([0, 0], [1.0, -0.5], color=FG, lw=6)
        arrow(ax, (0.8, -0.5), (0.8, 1.7), color=GREEN, lw=4); label(ax, 1.9, 1.0, 'N 750 N', size=15, color=GREEN)
        arrow(ax, (-0.8, -0.5), (-0.8, -2.0), color=C2, lw=4); label(ax, -1.6, -1.6, 'mg 687 N', size=15, color=C2)
        _work(fig, 0.38, 0.58, [(r'scales: $N = 76.5\times 9.81 = 750.5\ \mathrm{N}$ up', FG, None),
                                (r'weight $= 70.0\times 9.81 = 686.7\ \mathrm{N}$', FG, None),
                                (r'$F_{net} = 750.5 - 686.7 = 63.8\ \mathrm{N}$ up', FG, None),
                                (r'$a = \dfrac{63.8}{70.0} = 0.91093\ \mathrm{m\ s^{-2}}$ up', FG, '= 0.911 m s⁻² (3 s.f.)')], size=22, gap=0.07)
        T(fig, 0.38, 0.22, 'Element 4: either speeding up while going up,\nor slowing down while going down.', size=21, color=YELLOW)


def _rocket(ax, x, y, color=FG):
    ax.add_patch(Polygon([(x - 0.35, y - 1.2), (x + 0.35, y - 1.2), (x + 0.35, y + 0.8), (x, y + 1.6), (x - 0.35, y + 0.8)], fc=PANEL2, ec=color, lw=3, zorder=3))


def we_rocket(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a rocket')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        _q(fig, 'A 420 t rocket accelerates upward at 3.00 m s⁻² at lift-off. Find the thrust of its engines.', y=0.68, h=0.14, size=21)
    ax = wax(fig, [0.04, 0.06, 0.22, 0.60 if s == 0 else 0.74], (-2, 2), (-4.5, 4.5 if s else 4.5))
    ax.set_aspect('equal')
    thrust, wt = (5.38, 4.12) if s != 1 else (5.38, 5.38 / 1.2181)
    sc = 0.5
    _rocket(ax, 0, 0.2)
    arrow(ax, (0.0, 0.2), (0.0, 0.2 + thrust * sc * 0.95 + 1.4), color=YELLOW, lw=5)
    arrow(ax, (0.45, 0.2), (0.45, 0.2 - wt * sc * 0.95 - 1.4), color=C2, lw=5)
    label(ax, -0.9, 0.2 + thrust * sc * 0.95 + 1.3, 'thrust', size=16, color=YELLOW)
    label(ax, 1.2, 0.2 - wt * sc * 0.95 - 1.4, 'mg', size=16, color=C2)
    if s == 0:
        _work(fig, 0.32, 0.60, [(r'$F_{thrust} - mg = ma$', SOFT, None),
                                (r'$F_{thrust} = m(a+g) = 4.20\times 10^5\times(3.00 + 9.81)$', FG, None),
                                (r'$= 5.3802\times 10^{6}\ \mathrm{N}$', FG, '= 5.38 × 10⁶ N (3 s.f.)')], size=23, gap=0.085)
        T(fig, 0.32, 0.25, 'Most common error: forgetting the weight.\n420 t = 4.20 × 10⁵ kg first.', size=21, color=PINK)
    elif s == 1:
        _work(fig, 0.32, 0.78, [('Later: same thrust, less mass, a = 12.0 m s⁻²', SOFT, None),
                                (r'$m = \dfrac{F_{thrust}}{a+g} = \dfrac{5.3802\times 10^6}{12.0 + 9.81}$', FG, None),
                                (r'$= 2.4669\times 10^{5}\ \mathrm{kg}$', FG, '= 2.47 × 10⁵ kg (3 s.f.)')], size=23, gap=0.09)
        T(fig, 0.32, 0.38, 'Do not subtract g: gravity still pulls\ndown. Net force is still thrust − weight.', size=21, color=PINK)
    else:
        _work(fig, 0.32, 0.78, [(r'net force $= ma = 4.20\times10^5\times 3.00 = 1.26\times 10^{6}\ \mathrm{N}$', FG, None),
                                (r'thrust − weight $= 5.38\times10^6 - 4.12\times10^6 = 1.26\times10^6\ \mathrm{N}$ ✓', FG, None),
                                (r'thrust / weight $= 5.38 / 4.12 = 1.31 > 1$', YELLOW, None)], size=22, gap=0.09)
        T(fig, 0.32, 0.40, 'Lift-off needs thrust greater than weight.\nDraw the thrust arrow visibly longer.', size=22, color=SOFT)
        chip(fig, 'Element 2 · validity')


def newton3(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Newton’s third law', 'A common mix-up'][s])
    if s == 0:
        chip(fig, 'Element 1 · principles')
        ax = wax(fig, [0.04, 0.30, 0.52, 0.46], (-1, 11), (-2, 3))
        ax.set_aspect('equal')
        for x0, col, nm in [(0, C1, 'A'), (6, C2, 'B')]:
            ax.add_patch(Circle((x0 + 1.2, 0.5), 1.1, fc=PANEL2, ec=col, lw=4)); label(ax, x0 + 1.2, 0.5, nm, size=28, color=col)
        _vec(ax, (2.4, 0.9), (5.4, 0.9), color=GREEN, text='A on B', tp=(3.9, 1.5))
        _vec(ax, (6.0, 0.1), (3.0, 0.1), color=PINK, text='B on A', tp=(4.5, -0.6))
        bullets(fig, ['Equal in size', 'Opposite in direction', 'Same type of force', 'Act on DIFFERENT objects: they never\ncancel on one object'], 4, 0.58, 0.74, size=22, dim=False)
        T(fig, 0.06, 0.22, 'Rocket pushes gas down, gas pushes rocket up.\nBullet pushes plate, plate pushes bullet back.', size=22, color=SOFT)
    else:
        chip(fig, 'Element 1 · principles')
        ax = wax(fig, [0.04, 0.16, 0.46, 0.62], (-3, 4), (-3, 3.5))
        ax.set_aspect('equal')
        ax.plot([-3, 4], [0, 0], color=MUT, lw=4)
        _block(ax, (0.5, 0.6), 1.6, 1.2)
        _vec(ax, (0.2, 0.6), (0.2, -1.6), color=C2, text='weight\n(Earth on book)', tp=(-1.3, -0.9), size=15)
        _vec(ax, (0.8, 0.6), (0.8, 2.6), color=GREEN, text='normal\n(table on book)', tp=(2.3, 2.1), size=15)
        _vec(ax, (2.6, -1.6), (2.6, 0.4), color=PINK, text='pair of weight:\nbook on Earth', tp=(2.2, -2.3), size=15)
        bullets(fig, ['Weight and normal force are equal and\nopposite, but both act on the book,\nand they are different types', 'The pair of the book’s weight is the book\npulling the Earth upward', 'Probe past a planet: the planet gets the\nsame Δp in the opposite direction'], 3, 0.54, 0.74, size=20, dim=False)


# ============================================================================ part 4: momentum
def impulse(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Momentum and impulse', 'Force-time and momentum-time graphs', 'Why a longer stopping time helps'][s])
    if s == 0:
        meq(fig, 0.06, 0.72, r'$p = mv$', size=38)
        meq(fig, 0.06, 0.50, r'$F_{net} = \dfrac{\Delta(mv)}{\Delta t}$', size=34)
        learn_eq(fig, 0.06, 0.27, r'impulse:  $F\Delta t = \Delta p$', size=30)
        bullets(fig, ['Momentum: a vector, kg m s⁻¹,\nin the direction of motion', 'Impulse: N s = kg m s⁻¹', 'Net force = rate of change of momentum'],
                3, 0.52, 0.74, size=23, dim=False)
    elif s == 1:
        chip(fig, 'Element 3 · data')
        ax = gax(fig, [0.07, 0.38, 0.40, 0.40], (0, 0.05), (0, 380), 'time (s)', 'force (N)')
        ax.fill([0, 0.02, 0.04], [0, 300, 0], color=C1, alpha=0.4); ax.plot([0, 0.02, 0.04], [0, 300, 0], color=C1, lw=4)
        ax.set_xticks([0, 0.02, 0.04]); ax.set_yticks([0, 300]); label(ax, 0.02, 120, 'area = impulse', size=18, color=FG)
        ax2 = gax(fig, [0.55, 0.38, 0.40, 0.40], (0, 0.05), (0, 8), 'time (s)', 'momentum (kg m s⁻¹)', ticks=False)
        tt = np.linspace(0, 0.04, 60); pp = np.where(tt < 0.02, 6.0 * (tt / 0.02) ** 2 / 2 * 2 / 2 * 2 / 2 * 2, 6.0 - 6.0 * ((0.04 - tt) / 0.02) ** 2 / 1.0 * 0.5 * 2)
        pp = 6.0 * np.where(tt < 0.02, 0.5 * (tt / 0.02) ** 2, 1 - 0.5 * ((0.04 - tt) / 0.02) ** 2)
        ax2.plot(tt, pp, color=C2, lw=4); label(ax2, 0.012, 6.8, 'gradient = force', size=18, color=FG)
        _work(fig, 0.06, 0.30, [(r'impulse $= \frac{1}{2}\times 0.040\times 300 = 6.00\ \mathrm{N\ s}$,   $v = \dfrac{6.00}{0.200} = 30.0\ \mathrm{m\ s^{-1}}$', FG, None)], size=22)
        T(fig, 0.06, 0.20, 'Kicked ball, 0.200 kg from rest: triangular force pulse, peak 300 N for 0.040 s.\nUse the AREA, not the peak height. Answers exact: 6.00 N s, 30.0 m s⁻¹ (3 s.f.).', size=19, color=SOFT)
    else:
        chip(fig, 'Element 4 · predictions')
        ax = gax(fig, [0.07, 0.26, 0.46, 0.52], (0, 1.0), (0, 1.3), 'time', 'force', ticks=False)
        tt = np.linspace(0, 1, 200)
        ax.plot(tt, 1.2 * np.exp(-((tt - 0.12) / 0.07) ** 2), color=PINK, lw=4)
        ax.plot(tt, 0.34 * np.exp(-((tt - 0.4) / 0.25) ** 2), color=GREEN, lw=4)
        label(ax, 0.2, 1.15, 'short time:\nbig force', size=17, color=PINK, ha='left'); label(ax, 0.72, 0.5, 'long time:\nsmall force', size=17, color=GREEN)
        T(fig, 0.07, 0.19, 'Same area = same change in momentum', size=23, color=YELLOW)
        bullets(fig, ['Air bags, crumple zones, helmets:\nlonger stopping time, smaller average force', 'Catching a fast ball: pull your hands back', 'The change in momentum is fixed\nby the situation: more time, less force'],
                3, 0.58, 0.74, size=22, dim=False)


def _tri_axes(fig, rect, xlim=(-2.4, 2.0), ylim=(-0.7, 2.0)):
    ax = wax(fig, rect, xlim, ylim)
    ax.set_aspect('equal')
    return ax


def dp_vector(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Change in momentum: subtract', 'Solving the triangle', 'One dimension: mind the sign'][s])
    pi = np.array([1.45, 0.0]); pf = np.array([-1.690, 0.615])
    if s == 0:
        learn_eq(fig, 0.06, 0.72, r'$\Delta\vec{p} = \vec{p}_f - \vec{p}_i$', size=36)
        T(fig, 0.06, 0.52, '✗  NOT  p_i + p_f  head to tail\n(earns no marks)', size=24, color=PINK)
        T(fig, 0.06, 0.38, 'Write the vector statement first, then draw both\nmomenta from one point. Δp joins the TIP of p_i\nto the TIP of p_f.', size=22, color=SOFT)
        chip(fig, 'Element 1 · principles')
        ax = _tri_axes(fig, [0.50, 0.12, 0.47, 0.64])
        _vec(ax, (0, 0), tuple(pi), color=C1, text='p_i', tp=(0.7, -0.25), size=20)
        _vec(ax, (0, 0), tuple(pf), color=C2, text='p_f', tp=(-0.9, 0.12), size=20)
        _vec(ax, tuple(pi), tuple(pf), color=GREEN, text='Δp = p_f − p_i', tp=(-0.15, 0.95), size=20)
    elif s == 1:
        teq(fig, 0.06, 0.72, r'$a^2 = b^2 + c^2 - 2bc\cos A$', size=34)
        bullets(fig, ['90° between the vectors: Pythagoras', 'Otherwise: the cosine rule, using the\nangle INSIDE the triangle',
                      'Sine rule or tan⁻¹ for the direction', 'Give the direction relative to something clear\n(e.g. the initial momentum)',
                      'Draw it roughly to scale'], 5, 0.06, 0.52, size=21, dim=False)
        ax = _tri_axes(fig, [0.50, 0.12, 0.47, 0.64])
        _vec(ax, (0, 0), tuple(pi), color=C1, text='p_i', tp=(0.7, -0.25), size=20)
        _vec(ax, (0, 0), tuple(pf), color=C2, text='p_f', tp=(-0.9, 0.12), size=20)
        _vec(ax, tuple(pi), tuple(pf), color=GREEN, text='Δp', tp=(-0.15, 0.95), size=22)
        ax.add_patch(Arc((0, 0), 1.0, 1.0, theta1=0, theta2=160, color=YELLOW, lw=3)); label(ax, 0.05, 0.62, 'angle between\nthe vectors 160°', size=15, color=YELLOW)
    else:
        chip(fig, 'Element 2 · problems')
        ax = wax(fig, [0.05, 0.38, 0.55, 0.30], (-12, 12), (-2, 2))
        ax.plot([-12, 12], [0, 0], color=MUT, lw=2)
        ax.plot([8, 8], [-1.8, 1.8], color=MUT, lw=6)
        _vec(ax, (-3, 0.8), (3, 0.8), color=C1, text='before: +10 m s⁻¹', tp=(-5.2, 1.5), size=17)
        _vec(ax, (3, -0.8), (-3, -0.8), color=C2, text='after: −10 m s⁻¹', tp=(-5.2, -1.5), size=17)
        learn_eq(fig, 0.06, 0.20, r'$\Delta v = (-10) - (+10) = -20\ \mathrm{m\ s^{-1}}$', size=26)
        bullets(fig, ['Not zero, and not 10', 'Never subtract speeds as if all positive', 'A scalar difference earns half marks'], 3, 0.64, 0.68, size=20, dim=False)


def we_bounce(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a tennis return')
    chip(fig, 'Element 2 · problems')
    pi = np.array([1.45, 0.0]); pf = np.array([-1.690, 0.615])
    if s == 0:
        _q(fig, 'A 0.0580 kg ball moving east at 25.0 m s⁻¹ is returned at 31.0 m s⁻¹, 20.0° above the horizontal, heading west.\nFind its change in momentum and the average force for a contact time of 5.00 ms.', y=0.66, h=0.16, size=21)
    ax = _tri_axes(fig, [0.02, 0.06, 0.50, 0.58 if s == 0 else 0.72], (-2.4, 2.0), (-0.8, 1.6 if s == 0 else 2.0))
    _vec(ax, (0, 0), tuple(pi), color=C1, text='p_i 1.45', tp=(0.8, -0.3), size=18)
    _vec(ax, (0, 0), tuple(pf), color=C2, text='p_f 1.80', tp=(-1.0, 0.1), size=18)
    ax.add_patch(Arc((0, 0), 0.9, 0.9, theta1=0, theta2=160, color=YELLOW, lw=3)); label(ax, 0.0, 0.62, '160°', size=16, color=YELLOW)
    if s >= 1:
        _vec(ax, tuple(pi), tuple(pf), color=GREEN, text='Δp', tp=(-0.2, 1.0), size=20)
    if s >= 2:
        ax.plot([pf[0], pi[0]], [0, 0], color=GRID, lw=2, ls='--'); ax.plot([pf[0], pf[0]], [0, pf[1]], color=GRID, lw=2, ls='--')
    if s == 0:
        _work(fig, 0.55, 0.60, [(r'$p_i = 0.0580\times 25.0 = 1.45\ \mathrm{kg\ m\ s^{-1}}$ east', FG, None),
                                (r'$p_f = 0.0580\times 31.0 = 1.798\ \mathrm{kg\ m\ s^{-1}}$', FG, None),
                                ('Both drawn from one point: the angle between\nthem is 180° − 20.0° = 160°', SOFT, None)], size=21, gap=0.085)
        T(fig, 0.55, 0.30, 'Write  Δp = p_f − p_i  before drawing.', size=22, color=YELLOW)
    elif s == 1:
        _work(fig, 0.55, 0.78, [(r'$\Delta p^2 = p_i^2 + p_f^2 - 2p_ip_f\cos 160^\circ$', FG, None),
                                (r'$\Delta p = \sqrt{1.45^2 + 1.798^2 + 2(1.45)(1.798)(0.9397)}$', FG, None),
                                (r'$\Delta p = 3.1992\ \mathrm{kg\ m\ s^{-1}}$', FG, '= 3.20 kg m s⁻¹ (3 s.f.)')], size=21, gap=0.085)
        T(fig, 0.55, 0.40, 'cos 160° is negative, so the two products ADD.\nA bigger angle between the vectors gives a\nbigger change.', size=21, color=SOFT)
    else:
        _work(fig, 0.55, 0.78, [(r'$\tan\phi = \dfrac{0.615}{3.140} \Rightarrow \phi = 11.1^\circ$ above west', FG, None),
                                ('from the initial momentum: 180° − 11.1° = 169°', FG, None),
                                (r'$F = \dfrac{\Delta p}{\Delta t} = \dfrac{3.1992}{0.00500} = 639.85\ \mathrm{N}$', FG, '= 640 N (3 s.f.)')], size=21, gap=0.085)
        T(fig, 0.55, 0.37, 'Force on the ball points the way Δp points.\nBy Newton’s third law, the racket feels the\nsame force the other way.', size=21, color=SOFT)


def _blocks(ax, x, y, m1, m2, c1, c2):
    ax.add_patch(Rectangle((x, y), 1.0 * m1, 1.0, fc=c1, ec='none')); ax.add_patch(Rectangle((x + 1.6, y), 1.0 * m2, 1.0, fc=c2, ec='none'))


def conserve(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Conservation of momentum', 'Elastic and inelastic collisions', 'Why 90°?', 'Proving it from Newton’s laws'][s])
    if s == 0:
        chip(fig, 'Element 1 · principles')
        learn_eq(fig, 0.06, 0.72, r'$\sum p_{before} = \sum p_{after}$', size=34)
        bullets(fig, ['No outside force on the system', 'A vector law: in 2D, each direction separately', 'Collision: objects meet, bounce or stick',
                      'Explosion: start together (often at rest),\nfly apart: momenta cancel as vectors'], 4, 0.06, 0.50, size=23, dim=False)
        ax = wax(fig, [0.58, 0.20, 0.38, 0.58], (0, 10), (0, 10))
        ax.add_patch(Rectangle((0.5, 8.0), 1.4, 1.0, fc=C1)); ax.add_patch(Rectangle((4.0, 8.0), 1.4, 1.0, fc=C2))
        arrow(ax, (1.2, 7.7), (3.2, 7.7), color=FG, lw=2.5)
        ax.add_patch(Rectangle((1.2, 5.2), 1.4, 1.0, fc=C1)); ax.add_patch(Rectangle((2.6, 5.2), 1.4, 1.0, fc=C2))
        label(ax, 7.4, 8.5, 'collision', size=18, color=SOFT, ha='left'); label(ax, 6.6, 5.7, 'collision: stick', size=18, color=SOFT, ha='left')
        ax.add_patch(Rectangle((3.2, 2.2), 1.8, 1.0, fc=PANEL2, ec=FG))
        arrow(ax, (3.1, 2.7), (1.3, 2.7), color=C1, lw=3.5); arrow(ax, (5.1, 2.7), (7.1, 2.7), color=C2, lw=3.5)
        label(ax, 7.6, 3.4, 'explosion', size=18, color=SOFT, ha='left')
    elif s == 1:
        chip(fig, 'Element 1 · principles')
        rows = [('', 'Momentum', 'Kinetic energy'), ('Elastic', 'conserved', 'conserved'), ('Inelastic', 'conserved', 'NOT conserved')]
        for i, r in enumerate(rows):
            y = 0.72 - i * 0.12
            box(fig, 0.05, y - 0.05, 0.62, 0.10, fc=PANEL if i % 2 else PANEL2)
            for j, c in enumerate(r):
                col = SOFT if i == 0 or j == 0 else (GREEN if c == 'conserved' else PINK)
                T(fig, [0.07, 0.24, 0.44][j], y, c, size=24, color=col, va='center', weight='bold' if i == 0 else 'normal')
        bullets(fig, ['Test: total KE before and after', 'Equal: elastic.  Less: inelastic', 'Quote the numbers, then state the conclusion',
                      '“Momentum is conserved” does not decide it'], 4, 0.06, 0.40, size=22, dim=False)
    elif s == 2:
        chip(fig, 'Element 1 · principles')
        ax = _tri_axes(fig, [0.04, 0.10, 0.50, 0.66], (-0.3, 2.2), (-0.3, 1.5))
        _vec(ax, (0, 0), (1.8, 0), color=C1, text='p₀', tp=(0.9, -0.2), size=20)
        _vec(ax, (0, 0), (0.648, 0.864), color=C2, text='p_A', tp=(0.15, 0.55), size=20)
        _vec(ax, (0.648, 0.864), (1.8, 0), color=GREEN, text='p_B', tp=(1.45, 0.62), size=20)
        ax.plot([0.648, 0.648 + 0.12 * 0.8], [0.864, 0.864 - 0.12 * 0.6], color=YELLOW, lw=2)
        label(ax, 0.82, 0.74, '90°', size=16, color=YELLOW)
        bullets(fig, ['Equal masses, one at rest, elastic', 'KE = p² / 2m, so p₀² = p_A² + p_B²', 'That is Pythagoras: a right angle'], 3, 0.57, 0.74, size=22, dim=False)
        card(fig, 0.57, 0.20, 0.38, 0.28, 'Marking note', 'The 2018 report credits momentum alone for\nthe 90°. Physically energy must be conserved\ntoo: state both.', tcol=PINK, size=19)
    else:
        chip(fig, 'Element 1 · principles')
        _work(fig, 0.06, 0.76, [('Third law: F₁ = −F₂, for the same contact time Δt', FG, None),
                                ('Second law: m₁Δv₁ / Δt = −m₂Δv₂ / Δt', FG, None),
                                ('So  m₁Δv₁ + m₂Δv₂ = 0,   i.e.  Δp₁ + Δp₂ = 0', FG, None),
                                ('Total change in momentum = 0: momentum is conserved', GREEN, None)], size=25, gap=0.095)
        T(fig, 0.06, 0.30, 'Conclude with Δp_total = 0.\n“Δp₁ = Δp₂” is not enough, and “p₁ = p₂” misreads the Δ.', size=22, color=PINK)


def we_puck(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: two pucks')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        _q(fig, 'A 0.200 kg puck at 1.80 m s⁻¹ strikes an identical puck at rest. The first puck leaves at 1.08 m s⁻¹ and the pucks\nseparate at 90°. Find the second puck’s speed, the angles, and whether the collision is elastic.', y=0.66, h=0.16, size=21)
    ax = _tri_axes(fig, [0.03, 0.06, 0.46, 0.58 if s == 0 else 0.70], (-0.3, 2.1), (-0.4, 1.3 if s == 0 else 1.5))
    _vec(ax, (0, 0), (1.8, 0), color=C1, text='1.80', tp=(0.9, -0.2), size=18)
    _vec(ax, (0, 0), (0.648, 0.864), color=C2, text='1.08', tp=(0.15, 0.52), size=18)
    _vec(ax, (0.648, 0.864), (1.8, 0), color=GREEN, text='v_B', tp=(1.5, 0.55), size=18)
    if s >= 1:
        ax.add_patch(Arc((0, 0), 0.8, 0.8, theta1=0, theta2=53.13, color=YELLOW, lw=3)); label(ax, 0.62, 0.17, '53.1°', size=15, color=YELLOW)
        ax.add_patch(Arc((1.8, 0), 0.8, 0.8, theta1=143.13, theta2=180, color=PINK, lw=3)); label(ax, 1.35, 0.14, '36.9°', size=15, color=PINK)
    if s == 0:
        _work(fig, 0.52, 0.58, [('Right angle: the original momentum is the hypotenuse', SOFT, None),
                                (r'$v_B = \sqrt{1.80^2 - 1.08^2} = 1.44\ \mathrm{m\ s^{-1}}$', FG, None)], size=22, gap=0.085)
        T(fig, 0.52, 0.34, '(equal masses: velocity triangle = momentum triangle)\nExact inputs: 1.44 m s⁻¹ (3 s.f.)', size=20, color=SOFT)
    elif s == 1:
        _work(fig, 0.52, 0.78, [(r'$\cos\theta_A = \dfrac{1.08}{1.80} = 0.600 \Rightarrow \theta_A = 53.13^\circ$', FG, '= 53.1° (3 s.f.)'),
                                (r'$\theta_B = 90^\circ - 53.1^\circ = 36.9^\circ$ on the other side', FG, None)], size=22, gap=0.085)
        T(fig, 0.52, 0.42, 'A tidy diagram helps: untidy ones led to\nwrong trigonometric ratios.', size=21, color=PINK)
    else:
        _work(fig, 0.52, 0.78, [(r'before: $\frac{1}{2}(0.200)(1.80)^2 = 0.324\ \mathrm{J}$', FG, None),
                                (r'after: $\frac{1}{2}(0.200)(1.08^2 + 1.44^2) = 0.324\ \mathrm{J}$', FG, None),
                                ('Equal, so the collision is elastic', GREEN, None)], size=22, gap=0.085)
        T(fig, 0.52, 0.42, 'Show both calculations: a bare “yes”\nearns half marks. Less afterwards would mean\ninelastic.', size=21, color=SOFT)


def we_skate(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Worked example: skaters', 'Worked example: an explosion'][s])
    chip(fig, 'Element 2 · problems')
    if s == 0:
        _q(fig, 'A 70.0 kg skater moving north at 4.00 m s⁻¹ collides with a 55.0 kg skater moving east at 5.00 m s⁻¹. They cling\ntogether. Find their velocity just after.', y=0.66, h=0.16, size=21)
        ax = wax(fig, [0.03, 0.06, 0.40, 0.58], (-0.4, 3.2), (-0.4, 3.2)); ax.set_aspect('equal')
        _vec(ax, (0, 0), (0, 2.8), color=C1, text='280 N', tp=(-0.35, 1.4), size=17)
        _vec(ax, (0, 2.8), (2.75, 2.8), color=C2, text='275 E', tp=(1.4, 3.05), size=17)
        _vec(ax, (0, 0), (2.75, 2.8), color=GREEN, text='total', tp=(1.7, 1.2), size=18)
        _work(fig, 0.47, 0.58, [(r'$p_N = 70.0\times 4.00 = 280$,  $p_E = 55.0\times 5.00 = 275$', FG, None),
                                (r'$p = \sqrt{280^2 + 275^2} = 392.46\ \mathrm{kg\ m\ s^{-1}}$', FG, '= 392 kg m s⁻¹ (3 s.f.)'),
                                (r'$v = \dfrac{392.46}{125.0} = 3.1397\ \mathrm{m\ s^{-1}}$', FG, '= 3.14 m s⁻¹ (3 s.f.)'),
                                (r'direction $= \tan^{-1}\dfrac{275}{280} = 44.5^\circ$ east of north', FG, None)], size=21, gap=0.072)
        T(fig, 0.47, 0.14, 'Kinetic energy: 1247.5 J before, 616.1 J after (about half lost):\ninelastic. Momentum is still conserved.', size=19, color=YELLOW)
    else:
        _q(fig, 'A 4.50 kg launcher at rest fires a 0.0600 kg dart at 90.0 m s⁻¹. Find the launcher’s recoil velocity.', y=0.68, h=0.14, size=21)
        ax = wax(fig, [0.03, 0.08, 0.40, 0.50], (0, 10), (0, 5))
        ax.add_patch(Rectangle((2.8, 1.8), 2.4, 1.2, fc=PANEL2, ec=FG, lw=3))
        arrow(ax, (2.7, 2.4), (0.6, 2.4), color=C1, lw=4); arrow(ax, (5.3, 2.4), (9.3, 2.4), color=C2, lw=4)
        label(ax, 1.6, 3.2, '1.20 m s⁻¹', size=17, color=C1); label(ax, 7.4, 3.2, '90.0 m s⁻¹', size=17, color=C2)
        _work(fig, 0.47, 0.60, [(r'start: $p = 0$,  so $0 = 0.0600(90.0) - 4.50\,V$', FG, None),
                                (r'$V = \dfrac{5.40}{4.50} = 1.20\ \mathrm{m\ s^{-1}}$ the other way', FG, None),
                                (r'KE after $= 243 + 3.24 = 246\ \mathrm{J}$; before $= 0$', FG, None)], size=21, gap=0.085)
        T(fig, 0.47, 0.30, 'Kinetic energy rises in an explosion: it comes\nfrom stored chemical or elastic energy.', size=21, color=SOFT)
        chip(fig, 'Element 4 · predictions')


def mass_flow(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Force from a moving stream', 'Hoses, helicopters, jets and wind', 'Ion drives'][s])
    if s <= 1:
        chip(fig, 'Element 1 · principles')
    if s == 0:
        ax = wax(fig, [0.04, 0.16, 0.50, 0.58], (0, 10), (0, 6))
        ax.add_patch(Rectangle((1, 1.6), 7, 2.8, fc=C1, alpha=0.35, ec=C1, lw=3))
        ax.add_patch(Ellipse((1, 3.0), 0.7, 2.8, fc=C1, ec=FG, lw=3))
        arrow(ax, (1.4, 5.0), (8.0, 5.0), color=YELLOW, lw=3)
        label(ax, 4.7, 5.5, 'length v  (one second)', size=19, color=YELLOW); label(ax, 4.6, 3.0, 'area A', size=20, color=FG)
        learn_eq(fig, 0.58, 0.72, r'$\dot{m} = \rho A v$', size=32)
        learn_eq(fig, 0.58, 0.50, r'$F = \dfrac{\Delta m}{\Delta t}v = \rho A v^2$', size=30)
        T(fig, 0.58, 0.27, 'Mass per second = density × volume per\nsecond; volume per second = area × speed.\nThe stream starts at rest.', size=20, color=SOFT)
    elif s == 1:
        bullets(fig, ['Force on the fluid ⇒ equal and opposite force\non the machine (third law)', 'Hovering: not accelerating, so force on air = weight',
                      'Wind slowing from u to v: change in KE per second\n= ½ (Δm/Δt)(u² − v²)'], 3, 0.05, 0.76, size=22, dim=False)
        learn_eq(fig, 0.06, 0.40, r'power to the stream $= \frac{1}{2}\dot{m}v^2$', size=30)
        T(fig, 0.06, 0.20, 'Not F × (air speed): that is twice too big.\nUse the kinetic energy given to the air each second.', size=22, color=PINK)
    else:
        chip(fig, 'Element 4 · predictions')
        ax = wax(fig, [0.04, 0.30, 0.50, 0.40], (0, 10), (0, 4))
        ax.add_patch(Rectangle((1, 1.2), 2.4, 1.6, fc=PANEL2, ec=FG, lw=3)); ax.add_patch(Polygon([(3.4, 1.4), (4.2, 1.0), (4.2, 3.0), (3.4, 2.6)], fc=MUT))
        for k in range(5):
            ax.scatter([4.8 + 0.9 * k], [2.0], s=90, color=YELLOW, zorder=6)
        arrow(ax, (4.4, 2.0), (9.5, 2.0), color=YELLOW, lw=2.5); arrow(ax, (1.0, 0.5), (0.2, 0.5), color=GREEN, lw=4)
        label(ax, 7.0, 3.0, 'ions out fast', size=19, color=YELLOW); label(ax, 2.2, 0.35, 'thrust', size=18, color=GREEN)
        _work(fig, 0.58, 0.72, [(r'$F = \dfrac{\Delta m}{\Delta t}v = (5.0\times10^{-6})(3.0\times10^{4}) = 0.15\ \mathrm{N}$', FG, None),
                                (r'$a = \dfrac{0.15}{500} = 3.0\times10^{-4}\ \mathrm{m\ s^{-2}}$', FG, None),
                                (r'one year: $\Delta v \approx 9.5\times10^{3}\ \mathrm{m\ s^{-1}}$', FG, None)], size=20, gap=0.085)
        T(fig, 0.06, 0.20, 'A tiny force that never stops adds up: about 9.5 km s⁻¹ after a year\n(inputs 2 s.f.: 0.15 N, 3.0 × 10⁻⁴ m s⁻², 9.5 km s⁻¹).', size=21, color=YELLOW)


def we_drone(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a hovering drone')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        _q(fig, 'A drone pushes air downward at 9.00 m s⁻¹ through rotors of total area 0.250 m². The air density is 1.20 kg m⁻³.\nFind the mass of air pushed down each second, the drone’s mass if it hovers, and the fraction of 280 W given to the air.', y=0.64, h=0.18, size=20)
    ax = wax(fig, [0.03, 0.06, 0.28, 0.56], (-2, 2), (-4, 2.5))
    ax.add_patch(Rectangle((-0.5, 0.8), 1.0, 0.4, fc=PANEL2, ec=FG, lw=3)); ax.plot([-1.5, 1.5], [1.2, 1.2], color=FG, lw=4)
    ax.add_patch(Polygon([(-1.5, 0.8), (1.5, 0.8), (1.2, -3.4), (-1.2, -3.4)], fc=C1, alpha=0.25, ec='none'))
    arrow(ax, (0, 0.5), (0, -2.6), color=C1, lw=4)
    label(ax, 1.0, -1.5, '9.00\nm s⁻¹', size=16, color=C1)
    items = [(r'volume per second $= 0.250\times 9.00 = 2.25\ \mathrm{m^3\ s^{-1}}$', FG, None),
             (r'mass per second $= 1.20\times 2.25 = 2.70\ \mathrm{kg\ s^{-1}}$', FG, None)]
    if s >= 1:
        items = [(r'$F = \dfrac{\Delta p}{\Delta t} = 2.70\times 9.00 = 24.3\ \mathrm{N}$ (on the air)', FG, None),
                 (r'hover: $mg = F \Rightarrow m = \dfrac{24.3}{9.81} = 2.4771\ \mathrm{kg}$', FG, '= 2.48 kg (3 s.f.)')]
    if s >= 2:
        items = [(r'power to air $= \frac{1}{2}(2.70)(9.00)^2 = 109.35\ \mathrm{W}$', FG, None),
                 (r'percentage $= \dfrac{109.35}{280}\times 100 = 39.054\ \%$', FG, '= 39.1 % (3 s.f.)')]
    _work(fig, 0.34, 0.60, items, size=22, gap=0.09)
    if s == 0:
        T(fig, 0.34, 0.30, 'Mass flow rate = density × area × speed.', size=22, color=SOFT)
    if s == 1:
        T(fig, 0.34, 0.28, 'Force on the drone is upward (third law).\nHovering means balanced forces.', size=21, color=SOFT)
    if s == 2:
        T(fig, 0.34, 0.26, 'Multiply by 100 for a percentage. The rest is\nlost as heat and in the motors.', size=21, color=SOFT)


# ============================================================================ part 5: circular motion
def circ(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Moving in a circle', 'Centripetal acceleration and force', 'Tips for circular motion'][s])
    if s <= 1:
        ax = wax(fig, [0.03, 0.10, 0.46, 0.66], (-2.6, 2.6), (-2.2, 2.2))
        ax.set_aspect('equal')
        ax.add_patch(Circle((0, 0), 1.6, fill=False, ec=MUT, lw=3, ls='--'))
        a = TAU * ph + 0.6
        px, py = 1.6 * math.cos(a), 1.6 * math.sin(a)
        ax.scatter([px], [py], s=500, color=YELLOW, edgecolor=BG, linewidth=3, zorder=6)
        arrow(ax, (px, py), (px - 1.0 * math.sin(a), py + 1.0 * math.cos(a)), color=C1, lw=4)
        arrow(ax, (px, py), (px - 0.8 * math.cos(a), py - 0.8 * math.sin(a)), color=PINK, lw=4)
        label(ax, px - 1.45 * math.sin(a), py + 1.45 * math.cos(a), 'v', size=22, color=C1)
        label(ax, px - 1.2 * math.cos(a), py - 1.2 * math.sin(a), 'a', size=22, color=PINK)
        ax.scatter([0], [0], s=60, color=FG)
    if s == 0:
        chip(fig, 'Element 1 · principles')
        eq(fig, 0.54, 0.72, r'$v = \dfrac{2\pi r}{T}$', size=34)
        T(fig, 0.54, 0.52, 'circumference ÷ period (derived on the next slide).\nVelocity is along the tangent.\nIt changes direction, so there is acceleration.', size=21, color=SOFT)
        ax2 = wax(fig, [0.60, 0.08, 0.34, 0.34], (-0.2, 2.2), (-0.2, 1.4)); ax2.set_aspect('equal')
        _vec(ax2, (0, 0), (1.6, 0.25), color=C1, text='v₁', tp=(0.8, -0.18), size=16)
        _vec(ax2, (0, 0), (1.5, 0.7), color=C1, text='v₂', tp=(0.5, 0.55), size=16, lw=2.0)
        _vec(ax2, (1.6, 0.25), (1.5, 0.7), color=PINK, text='Δv', tp=(1.85, 0.5), size=16, lw=3)
        T(fig, 0.54, 0.40, 'Small Δθ:  Δv ≈ vΔθ,  and Δθ/Δt = v/r\nso  a = v²/r, towards the centre', size=19, color=YELLOW)
    elif s == 1:
        meq(fig, 0.54, 0.76, r'$a_c = \dfrac{v^2}{r} = \dfrac{4\pi^2 r}{T^2}$', size=30)
        meq(fig, 0.54, 0.50, r'$F_c = \dfrac{mv^2}{r} = \dfrac{4\pi^2 mr}{T^2}$', size=30)
        T(fig, 0.54, 0.31, 'Derive the speed formula from the sheet:\nv²/r = 4π²r/T²  →  v² = 4π²r²/T²  →  v = 2πr/T', size=21, color=GREEN)
        T(fig, 0.54, 0.16, 'F_c is the NET force to the centre (tension, gravity,\nfriction, a component…): not a new kind of force.', size=19, color=YELLOW)
        chip(fig, 'Element 1 · principles')
    else:
        chip(fig, 'Element 2 · problems')
        bullets(fig, ['Given the period: use 4π²r / T² directly', 'r is the radius: not the diameter, nor the circumference', 'Square the speed (or the period); root where needed',
                      'Draw real forces only; say their sum points to the centre', 'A dashed net-force arrow is fine; a solid\n“centripetal force” arrow is not'], 5, 0.05, 0.76, size=22, dim=False)
        ax = wax(fig, [0.62, 0.20, 0.34, 0.50], (-2, 2), (-3, 2)); ax.set_aspect('equal')
        ax.plot([0, 1.4], [1.6, -1.0], color=FG, lw=3)
        ax.scatter([1.4], [-1.0], s=400, color=YELLOW, zorder=5)
        arrow(ax, (1.4, -1.0), (0.78, 0.62), color=PINK, lw=3.5); arrow(ax, (1.4, -1.0), (1.4, -2.5), color=C2, lw=3.5)
        arrow(ax, (1.4, -1.0), (0.2, -1.0), color=GREEN, lw=2.5, ls='--')
        label(ax, 0.3, 0.2, 'tension', size=15, color=PINK); label(ax, 1.75, -2.2, 'weight', size=15, color=C2); label(ax, 0.55, -1.35, 'net (dashed)', size=14, color=GREEN)


def we_conical(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a bob circling horizontally')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        _q(fig, 'A 0.250 kg bob on a 1.20 m string circles horizontally, with the string at 30.0° to the vertical. Find the tension,\nthe speed and the period.', y=0.66, h=0.16, size=21)
    th = 30.0
    ax = wax(fig, [0.03, 0.06, 0.38, 0.58 if s == 0 else 0.74], (-2.2, 2.2), (-3.6, 1.0 if s == 0 else 1.6)); ax.set_aspect('equal')
    ax.plot([-1.2, 1.2], [0.7, 0.7], color=MUT, lw=5)
    bx, by = 1.2 * math.sin(RAD(th)) * 2.2, 0.7 - 1.2 * math.cos(RAD(th)) * 2.2
    ax.plot([0, bx], [0.7, by], color=FG, lw=3)
    ax.plot([0, 0], [0.7, by], color=MUT, lw=1.5, ls='--')
    ax.add_patch(Ellipse((0, by), 2 * bx, 0.5, fill=False, ec=MUT, lw=2, ls='--'))
    ax.scatter([bx], [by], s=450, color=YELLOW, zorder=6)
    _vec(ax, (bx, by), (bx * 0.55, by + (0.7 - by) * 0.55), color=PINK, text='T', tp=(bx * 0.3, by + 0.8 * (0.7 - by) * 0.6), size=17)
    _vec(ax, (bx, by), (bx, by - 1.2), color=C2, text='mg', tp=(bx + 0.35, by - 1.0), size=17)
    ax.add_patch(Arc((0, 0.7), 1.2, 1.2, theta1=-90, theta2=-60, color=YELLOW, lw=3)); label(ax, 0.38, -0.3, '30°', size=15, color=YELLOW)
    if s >= 1:
        _vec(ax, (bx, by), (bx - 1.0, by), color=GREEN, text='net', tp=(bx - 0.5, by + 0.22), size=15, lw=3)
        label(ax, bx / 2, by - 0.38, 'r', size=17, color=GREEN)
    if s == 0:
        _work(fig, 0.44, 0.60, [('Only two forces: tension and weight', SOFT, None),
                                (r'vertical balance: $T\cos 30.0^\circ = mg$', FG, None),
                                (r'$T = \dfrac{0.250\times 9.81}{\cos 30.0^\circ} = 2.8319\ \mathrm{N}$', FG, '= 2.83 N (3 s.f.)')], size=22, gap=0.085)
    elif s == 1:
        _work(fig, 0.44, 0.78, [(r'net (horizontal) $= T\sin\theta = mg\tan\theta = 1.4160\ \mathrm{N}$', FG, '= 1.42 N (3 s.f.)'),
                                (r'$r = 1.20\sin 30.0^\circ = 0.600\ \mathrm{m}$', FG, None),
                                (r'$mg\tan\theta = \dfrac{mv^2}{r} \Rightarrow v = \sqrt{rg\tan\theta} = 1.8434\ \mathrm{m\ s^{-1}}$', FG, '= 1.84 m s⁻¹ (3 s.f.)')], size=21, gap=0.082)
    else:
        _work(fig, 0.44, 0.78, [(r'$T_{period} = \dfrac{2\pi r}{v} = \dfrac{2\pi(0.600)}{1.8434} = 2.0450\ \mathrm{s}$', FG, '= 2.05 s (3 s.f.)'),
                                (r'check: $a = g\tan 30.0^\circ = 5.66\ \mathrm{m\ s^{-2}}$', FG, None),
                                (r'$\dfrac{4\pi^2 r}{T^2} = \dfrac{4\pi^2(0.600)}{2.0450^2} = 5.66\ \mathrm{m\ s^{-2}}$ ✓', FG, None)], size=21, gap=0.082)
        T(fig, 0.44, 0.30, 'Two routes, same answer: the working is valid.', size=21, color=YELLOW)


def circ_apps(fig, s, ph):
    C1, C2 = C()
    header(fig, ['A banked aircraft', 'Net force and radius of the turn', 'Where else this works'][s])
    chip(fig, 'Element 2 · problems' if s < 2 else 'Element 4 · predictions')
    th = 25.0
    if s <= 1:
        ax = wax(fig, [0.03, 0.10, 0.44, 0.64], (-3, 3), (-3, 3)); ax.set_aspect('equal')
        a = RAD(th)
        wl = np.array([math.cos(a), math.sin(a)]); nl = np.array([-wl[1], wl[0]])
        ax.plot([-2.4 * wl[0], 2.4 * wl[0]], [-2.4 * wl[1], 2.4 * wl[1]], color=FG, lw=8)
        ax.scatter([0], [0], s=300, color=YELLOW, zorder=6)
        L_ = 3.0
        _vec(ax, (0, 0), tuple(L_ * nl), color=GREEN, text='lift', tp=tuple(L_ * nl * 1.12 + np.array([0.3, 0])), size=18)
        _vec(ax, (0, 0), (0, -L_ * nl[1]), color=C2, text='mg', tp=(0.4, -L_ * nl[1] * 0.8), size=18)
        ax.plot([0, 0], [0, L_ * nl[1]], color=GRID, lw=1.5, ls='--'); ax.plot([0, L_ * nl[0]], [L_ * nl[1], L_ * nl[1]], color=GRID, lw=1.5, ls='--')
        if s == 1:
            _vec(ax, (0, 0), (L_ * nl[0], 0), color=PINK, text='net', tp=(L_ * nl[0] / 2, 0.35), size=17, lw=3)
        ax.add_patch(Arc((0, 0), 2.0, 2.0, theta1=0, theta2=th, color=YELLOW, lw=3)); label(ax, 1.5, 0.35, '25°', size=14, color=YELLOW)
    if s == 0:
        _work(fig, 0.50, 0.76, [('Lift is at right angles to the wings.', SOFT, None),
                                ('Vertical part balances the weight:', SOFT, None),
                                (r'$L\cos 25.0^\circ = mg$', FG, None),
                                (r'$L = \dfrac{600\times 9.81}{\cos 25.0^\circ} = 6494.5\ \mathrm{N}$', FG, '= 6.49 × 10³ N (3 s.f.)')], size=22, gap=0.085)
        T(fig, 0.50, 0.25, 'The horizontal part of the lift is the net force to\nthe centre. 600 kg glider, banked at 25.0°.', size=20, color=SOFT)
    elif s == 1:
        _work(fig, 0.50, 0.78, [(r'net $= mg\tan 25.0^\circ = 2744.7\ \mathrm{N}$ inward', FG, '= 2.74 × 10³ N (3 s.f.)'),
                                (r'$\dfrac{mv^2}{r} = mg\tan\theta \Rightarrow r = \dfrac{v^2}{g\tan\theta}$', FG, None),
                                (r'$r = \dfrac{40.0^2}{9.81\times\tan 25.0^\circ} = 349.77\ \mathrm{m}$', FG, '= 350 m (3 s.f.)')], size=21, gap=0.085)
        T(fig, 0.50, 0.22, 'A wrong value of 4410 N in a similar exam question\nis m g sinθ, not m g tanθ: draw the force triangle.', size=19, color=PINK)
    else:
        cards = [('Banked road, leaning cyclist', 'The same triangle: tanθ = v² / (rg).', C1), ('Child swung by the arms', 'Parent’s force: weight + net inward force.', C2),
                 ('Charm in a car', 'Angle gives the acceleration: tanθ = a / g,\nspeeding up or turning.', GREEN), ('Prediction', 'Same bank angle, double the speed:\nradius ×4 (v²). Bigger angle: tighter turn.', PINK)]
        for i, (a_, b_, c_) in enumerate(cards):
            x = 0.05 + (i % 2) * 0.46; y = 0.46 - (i // 2) * 0.33
            card(fig, x, y, 0.44, 0.30, a_, b_, tcol=c_, size=21)


def spin(fig, s, ph):
    C1, C2 = C()
    header(fig, ['A person on the equator', 'Why the Earth bulges', 'A small, fast-spinning world'][s])
    chip(fig, ['Element 2 · problems', 'Element 4 · predictions', 'Element 4 · predictions'][s])
    ax = wax(fig, [0.03, 0.10, 0.42, 0.66], (-2.6, 2.6), (-2.2, 2.2)); ax.set_aspect('equal')
    rr = 1.55 if s < 2 else 0.9
    ax.add_patch(Ellipse((0, 0), 2 * rr * (1.0 if s == 0 else 1.1), 2 * rr, fc=C1, alpha=0.45, ec=FG, lw=3))
    ax.add_patch(Arc((0, 0), 4.6, 4.2, theta1=60, theta2=130, color=YELLOW, lw=3)); ax.annotate('', xy=(-0.4, 2.15), xytext=(0.4, 2.15), arrowprops=dict(arrowstyle='-|>', color=YELLOW, lw=3))
    label(ax, 1.9, 1.9, 'rotation', size=15, color=YELLOW)
    ex = rr * (1.0 if s == 0 else 1.1)
    ax.scatter([ex], [0], s=250, color=FG, zorder=6)
    arrow(ax, (ex, 0), (ex - 1.2, 0), color=C2, lw=4); label(ax, ex - 0.55, 0.35, 'gravity', size=15, color=C2)
    arrow(ax, (ex, 0), (ex + 0.9 * (0.5 if s < 2 else 0.9), 0), color=GREEN, lw=4)
    label(ax, ex + 0.55, -0.35, 'push of ground', size=14, color=GREEN)
    if s == 0:
        weq_ = None
        _work(fig, 0.50, 0.76, [(r'$a_c = \dfrac{4\pi^2 R}{T^2}$,  $N = m(g - a_c)$', FG, None),
                                (r'Earth: $v = 2\pi(6.378\times10^6)/86400 = 464\ \mathrm{m\ s^{-1}}$', FG, None),
                                (r'$a_c = 0.0337\ \mathrm{m\ s^{-2}}$ (3 s.f.), vs $g = 9.81$', FG, None)], size=21, gap=0.085)
        T(fig, 0.50, 0.50, 'Mars: R = 3.39 × 10⁶ m, T = 24.6 h', size=22, color=C2, weight='bold')
        _work(fig, 0.50, 0.42, [(r'$a_c = \dfrac{4\pi^2(3.39\times10^6)}{(24.6\times3600)^2} = 0.017064\ \mathrm{m\ s^{-2}}$', FG, '= 0.0171 m s⁻² (3 s.f.)')], size=21, gap=0.085)
        T(fig, 0.50, 0.22, 'That is 0.46 % of Mars’s 3.72 m s⁻²: a small drop in apparent weight.', size=19, color=SOFT)
    elif s == 1:
        bullets(fig, ['Spin: material wants to go in a straight line\n(Newton’s first law), so it spreads outward', 'The equator bulges: larger radius, weaker field\n(g = GM/r²)', 'The spin also needs a net inward force,\nso the ground pushes LESS on you',
                      'At the poles: no circular motion, smaller radius'], 4, 0.50, 0.76, size=21, dim=False)
        T(fig, 0.50, 0.24, 'Link the spin to the force of the ground,\nnot just to “a centripetal force”.', size=20, color=YELLOW)
    else:
        bullets(fig, ['Small body, fast spin: a_c at the equator can\napproach the local g', 'Then N = m(g − a_c) is nearly zero:\nthe surface is almost in orbit', 'Apparent g is LESS than the field strength,\nnot more (a common mix-up)', 'Spin faster still: loose material lifts off'],
                4, 0.50, 0.76, size=21, dim=False)


# ============================================================================ part 6: work, energy and power
def work(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Work done by a force', 'Force-distance graphs', 'Potential and kinetic energy'][s])
    if s == 0:
        weq(fig, 0.06, 0.72, r'$W = \Delta\mathrm{Energy} = Fs\cos\theta$', size=34)
        bullets(fig, ['θ is the angle between the force and the displacement', 'Only the component along the movement does work',
                      'A force at right angles does none (gravity on level\nmotion; centripetal force on a circle)', 'Unit: joule.  A scalar'], 4, 0.06, 0.50, size=22, dim=False)
        ax = wax(fig, [0.60, 0.16, 0.36, 0.56], (-1, 8), (-1, 5)); ax.set_aspect('equal')
        ax.plot([0, 8], [0, 0], color=MUT, lw=3); _block(ax, (3.5, 0.5), 1.6, 1.0)
        arrow(ax, (3.5, 0.5), (6.2, 2.2), color=YELLOW, lw=4); arrow(ax, (3.5, 0.5), (6.2, 0.5), color=GREEN, lw=3, ls='--')
        label(ax, 6.5, 2.5, 'F', size=22, color=YELLOW); label(ax, 4.9, 0.1, 'F cosθ', size=17, color=GREEN)
        ax.add_patch(Arc((3.5, 0.5), 2.4, 2.4, theta1=0, theta2=32, color=FG, lw=2)); label(ax, 5.0, 0.95, 'θ', size=17)
    elif s == 1:
        chip(fig, 'Element 3 · data')
        ax = gax(fig, [0.07, 0.24, 0.50, 0.54], (0, 0.45), (0, 120), 'distance (m)', 'force (N)')
        pts = [(0, 0), (0.10, 60), (0.30, 100), (0.40, 90)]
        xs, ys = zip(*pts)
        ax.fill_between(xs, 0, ys, color=C1, alpha=0.35); ax.plot(xs, ys, color=C1, lw=4); ax.set_xticks([0, 0.1, 0.2, 0.3, 0.4]); ax.set_yticks([0, 60, 90, 100])
        label(ax, 0.2, 40, 'work = area', size=20)
        bullets(fig, ['Work = area under the graph', 'Triangles and rectangles, or count squares', 'Read the scale exactly: not the biggest force × s',
                      'Convert cm to m first'], 4, 0.62, 0.74, size=21, dim=False)
        T(fig, 0.07, 0.15, 'Areas: ½(0.10)(60) = 3.0 J,  ½(60+100)(0.20) = 16.0 J,  ½(100+90)(0.10) = 9.5 J', size=20, color=SOFT)
    else:
        weq(fig, 0.06, 0.72, r'$E_p = mgh$', size=36)
        weq(fig, 0.06, 0.48, r'$E_K = \frac{1}{2}mv^2$', size=36)
        bullets(fig, ['E_p depends on the height CHANGE', 'On a slope, h = distance along it × sinθ', 'Work done on an object = change in its energy',
                      'Compare launchers by the area (stored energy)\nand by the force at full draw (how hard to hold)'], 4, 0.50, 0.74, size=21, dim=False)


def we_work(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Worked example: work at an angle', 'Worked example: a launcher'][s])
    chip(fig, 'Element 2 · problems' if s == 0 else 'Element 3 · data')
    if s == 0:
        _q(fig, 'A sled is pulled 12.0 m along level snow by a rope that pulls with 80.0 N at 35.0° above the horizontal.\nHow much work does the rope do?', y=0.66, h=0.16, size=21)
        ax = wax(fig, [0.03, 0.06, 0.44, 0.52], (-1, 14), (-1, 6)); ax.set_aspect('equal')
        ax.plot([0, 14], [0, 0], color=MUT, lw=3); _block(ax, (3, 0.6), 2.4, 1.2)
        arrow(ax, (3, 0.6), (8.0, 3.4), color=YELLOW, lw=4); arrow(ax, (3, 0.6), (8.0, 0.6), color=GREEN, lw=3, ls='--')
        label(ax, 8.8, 3.6, '80.0 N', size=17, color=YELLOW); label(ax, 5.6, 0.15, 'F cos 35.0°', size=15, color=GREEN)
        ax.add_patch(Arc((3, 0.6), 4.0, 4.0, theta1=0, theta2=35, color=FG, lw=2)); label(ax, 5.3, 1.3, '35.0°', size=14)
        _work(fig, 0.50, 0.56, [(r'$W = Fs\cos\theta = 80.0\times 12.0\times\cos 35.0^\circ$', FG, None),
                                (r'$W = 786.39\ \mathrm{J}$', FG, '= 786 J (3 s.f.)')], size=23, gap=0.085)
        T(fig, 0.50, 0.26, 'Ask: which angle is between the force and\nthe movement? Here the horizontal component\ndoes the work.', size=21, color=SOFT)
    else:
        _q(fig, 'A launcher’s force-distance graph has straight lines through (0, 0), (0.10 m, 60 N), (0.30 m, 100 N) and (0.40 m, 90 N).\n70 % of the energy goes to a 0.0450 kg ball. Find its speed.', y=0.66, h=0.16, size=21)
        ax = gax(fig, [0.07, 0.10, 0.38, 0.46], (0, 0.45), (0, 120), 'distance (m)', 'force (N)')
        pts = [(0, 0), (0.10, 60), (0.30, 100), (0.40, 90)]; xs, ys = zip(*pts)
        ax.fill_between(xs, 0, ys, color=C1, alpha=0.35); ax.plot(xs, ys, color=C1, lw=4); ax.set_xticks([0, 0.1, 0.3, 0.4]); ax.set_yticks([0, 60, 90, 100])
        _work(fig, 0.50, 0.56, [('area = 3.0 + 16.0 + 9.5 = 28.5 J', FG, None),
                                ('ball: 0.70 × 28.5 = 19.95 J', FG, None),
                                (r'$v = \sqrt{\dfrac{2(19.95)}{0.0450}} = 29.777\ \mathrm{m\ s^{-1}}$', FG, '= 29.8 m s⁻¹ (3 s.f.)')], size=22, gap=0.085)


def energy(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Conservation of energy', 'Elastic or inelastic?', 'Use the right law for each stage'][s])
    if s == 0:
        chip(fig, 'Element 1 · principles')
        bullets(fig, ['Energy is never created or destroyed:\nit changes form', 'Pick a start and an end; write the total energy at each',
                      'No friction or drag: KE + PE stays constant', 'With friction: energy lost = work against it'], 4, 0.05, 0.76, size=23, dim=False)
        learn_eq(fig, 0.06, 0.30, r'drop from $h$:  $v = \sqrt{2gh}$', size=30)
        ax = wax(fig, [0.60, 0.20, 0.36, 0.56], (0, 10), (0, 10))
        ax.plot([1, 3, 9], [8.5, 8.5, 1.5], color=MUT, lw=4); ax.plot([1, 9], [1.5, 1.5], color=MUT, lw=3, alpha=0.5)
        ax.scatter([2], [9.1], s=350, color=YELLOW, zorder=6); ax.scatter([8.2], [2.3], s=350, color=YELLOW, zorder=6, alpha=0.6)
        label(ax, 4.2, 9.5, 'E_p large, E_K small', size=17, color=C1, ha='left'); label(ax, 5.4, 3.0, 'E_p small,\nE_K large', size=17, color=C2, ha='left')
    elif s == 1:
        chip(fig, 'Element 2 · problems')
        rows = [('Elastic', 'KE before = KE after'), ('Inelastic', 'KE after < KE before')]
        for i, (a_, b_) in enumerate(rows):
            card(fig, 0.05 + i * 0.46, 0.50, 0.44, 0.26, a_, b_, tcol=[GREEN, PINK][i], size=24)
        bullets(fig, ['Calculate total KE before and after, then compare', 'Quote both numbers and state the conclusion',
                      'Percentage lost = (KE before − KE after) / KE before × 100'], 3, 0.05, 0.40, size=22, dim=False)
    else:
        chip(fig, 'Element 1 · principles')
        ax = wax(fig, [0.04, 0.18, 0.54, 0.56], (0, 12), (0, 7))
        ax.plot([3, 3, 7, 7], [5.2, 6.5, 6.5, 5.2], color=MUT, lw=3)
        ax.add_patch(Rectangle((5.6, 3.8), 1.4, 1.1, fc=PANEL2, ec=FG, lw=3)); ax.plot([4.0, 5.6], [4.3, 4.3], color=YELLOW, lw=6)
        arrow(ax, (0.3, 4.3), (3.8, 4.3), color=YELLOW, lw=3)
        label(ax, 1.5, 4.9, 'dart', size=17, color=YELLOW); label(ax, 6.3, 3.4, 'block', size=17, color=FG)
        label(ax, 3.2, 1.6, 'stage 1: collision → momentum\nstage 2: swing → energy', size=19, color=GREEN)
        bullets(fig, ['Embedding is a collision:\nmomentum is conserved, energy is not', 'The swing afterwards: kinetic energy\nbecomes potential energy', 'Label the stages: each has its own law'], 3, 0.60, 0.74, size=21, dim=False)


def we_dart(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a dart and a block')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        _q(fig, 'A 0.0250 kg dart moving at 40.0 m s⁻¹ embeds in a 0.475 kg block hanging from strings. Find the speed just after,\nthe percentage of kinetic energy lost, and how high the block swings.', y=0.66, h=0.16, size=21)
    ax = wax(fig, [0.03, 0.06, 0.34, 0.54], (0, 10), (0, 6))
    ax.plot([2, 8], [5.6, 5.6], color=MUT, lw=4); ax.plot([3, 5], [5.6, 3.6], color=FG, lw=2); ax.plot([7, 5], [5.6, 3.6], color=FG, lw=2)
    ax.add_patch(Rectangle((4.0, 2.6), 2.0, 1.0, fc=PANEL2, ec=FG, lw=3)); arrow(ax, (0.2, 3.1), (3.8, 3.1), color=YELLOW, lw=4)
    label(ax, 1.5, 3.7, '40.0 m s⁻¹', size=17, color=YELLOW)
    if s == 0:
        _work(fig, 0.40, 0.58, [('Collision: momentum is conserved', SOFT, None),
                                (r'$0.0250\times 40.0 = (0.0250 + 0.475)\,v$', FG, None),
                                (r'$v = \dfrac{1.00}{0.500} = 2.00\ \mathrm{m\ s^{-1}}$', FG, None)], size=23, gap=0.085)
        T(fig, 0.40, 0.28, 'Inputs 3 s.f., so 2.00 m s⁻¹ exactly.', size=19, color=MUT)
    elif s == 1:
        _work(fig, 0.40, 0.78, [(r'before: $\frac{1}{2}(0.0250)(40.0)^2 = 20.0\ \mathrm{J}$', FG, None),
                                (r'after: $\frac{1}{2}(0.500)(2.00)^2 = 1.00\ \mathrm{J}$', FG, None),
                                (r'lost $= 19.0\ \mathrm{J}$, which is $95.0\ \%$', GREEN, None)], size=23, gap=0.085)
        T(fig, 0.40, 0.46, 'Inelastic: the energy went to heat, sound and\ndeformation. Momentum was still conserved.', size=21, color=SOFT)
        chip(fig, 'Element 2 · validity')
    else:
        ax.plot([5, 5], [3.6, 3.6], alpha=0)
        _work(fig, 0.40, 0.78, [(r'swing: $\frac{1}{2}mv^2 = mgh \Rightarrow h = \dfrac{v^2}{2g}$', FG, None),
                                (r'$h = \dfrac{2.00^2}{2(9.81)} = 0.20387\ \mathrm{m}$', FG, '= 0.204 m (3 s.f.)')], size=23, gap=0.085)
        T(fig, 0.40, 0.42, 'Check: using the dart’s 20 J would give a height\n20 times too big. Only 1.00 J is left:\n1.00 / (0.500 × 9.81) = 0.204 m ✓', size=21, color=YELLOW)


def power(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Power', 'Efficiency and energy per second'][s])
    if s == 0:
        weq(fig, 0.06, 0.72, r'$P = \dfrac{W}{t}$', size=38)
        T(fig, 0.06, 0.52, '= ΔE / t.  Unit: watt = joule per second.  1 kW = 1000 W', size=22, color=SOFT)
        learn_eq(fig, 0.06, 0.38, r'steady force at constant speed:  $P = Fv$', size=26)
        T(fig, 0.06, 0.20, 'Not for a stream of fluid being accelerated:\nthere, use the kinetic energy given to it each second.', size=21, color=PINK)
        ax = wax(fig, [0.62, 0.20, 0.34, 0.56], (0, 10), (0, 10))
        ax.add_patch(Rectangle((1, 1), 8, 3, fc=PANEL2, ec=FG, lw=3)); label(ax, 5, 2.5, 'energy per second\n= power', size=21, color=YELLOW)
        label(ax, 5, 6.5, 'work out the energy\nEACH SECOND', size=22, color=GREEN)
    else:
        chip(fig, 'Element 2 · problems')
        learn_eq(fig, 0.06, 0.72, r'efficiency $= \dfrac{\mathrm{useful\ output}}{\mathrm{total\ input}}\times 100\ \%$', size=28)
        bullets(fig, ['Don’t forget the × 100', 'Constant speed: no change in KE', 'Engine power = PE gained per second\n+ work against resistance per second',
                      'Resistance “a fraction of the weight”: use weight, not mass'], 4, 0.06, 0.50, size=22, dim=False)


def we_power(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a car on a hill')
    chip(fig, 'Element 2 · problems')
    th = 8.0
    if s == 0:
        _q(fig, 'A 1200 kg car climbs an 8.00° slope at a constant 15.0 m s⁻¹ against a constant resistance of 600 N. Find the useful\npower it needs, and the percentage of a 45.0 kW engine output that this represents.', y=0.66, h=0.16, size=21)
    ax = wax(fig, [0.03, 0.06, 0.40, 0.52], (-1, 14), (-0.5, 4.0)); ax.set_aspect('equal')
    ax.fill([0, 13, 13], [0, 13 * math.tan(RAD(th)) * 1.0, 0], color=PANEL, zorder=1)
    ax.plot([0, 13], [0, 13 * math.tan(RAD(th))], color=MUT, lw=4)
    ax.annotate('', xy=(10.0 * 0.99, 10.0 * math.tan(RAD(th))), xytext=(10.0 * 0.99 - 15 * 0.0, 0), arrowprops=dict(arrowstyle='<|-|>', color=YELLOW, lw=2))
    label(ax, 11.4, 1.0, '15 sin 8°\n= 2.09 m', size=15, color=YELLOW)
    ax.add_patch(Arc((0, 0), 5, 5, theta1=0, theta2=th, color=FG, lw=2)); label(ax, 3.2, 0.2, '8.00°', size=14)
    if s == 0:
        _work(fig, 0.46, 0.58, [('In one second the car moves 15.0 m along the slope.', SOFT, None),
                                (r'height gained $= 15.0\sin 8.00^\circ = 2.0877\ \mathrm{m}$', FG, None),
                                (r'$E_p$ per second $= mgh = 1200\times 9.81\times 2.0877$', FG, None),
                                (r'$= 24575\ \mathrm{J\ s^{-1}} = 24575\ \mathrm{W}$', FG, '= 2.46 × 10⁴ W (3 s.f.)')], size=21, gap=0.075)
    elif s == 1:
        _work(fig, 0.46, 0.78, [(r'resistance: $600\times 15.0 = 9000\ \mathrm{J\ s^{-1}}$ = 9.00 kW', FG, None),
                                ('KE is not changing: it adds nothing', SOFT, None),
                                (r'total $= 24575 + 9000 = 33575\ \mathrm{W}$', FG, '= 3.36 × 10⁴ W (3 s.f.)')], size=22, gap=0.08)
    else:
        _work(fig, 0.46, 0.78, [(r'efficiency $= \dfrac{33575}{45000}\times 100 = 74.611\ \%$', FG, '= 74.6 % (3 s.f.)'),
                                ('Check: below 100 %. The other 11.4 kW is lost\nas heat and sound.', YELLOW, None)], size=22, gap=0.09)


# ============================================================================ part 7: gravity
def _planet(ax, c=(0, 0), r=1.0, color=None):
    ax.add_patch(Circle(c, r, fc=color or L.A2(), ec=BG, lw=3, zorder=3, alpha=0.9))


def grav_law(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Universal gravitation', 'Weight, field strength and g = GM/r²', 'Testing the inverse square law'][s])
    if s == 0:
        chip(fig, 'Element 1 · principles')
        geq(fig, 0.06, 0.72, r'$F_g = \dfrac{Gm_1m_2}{r^2}$', size=38)
        geq(fig, 0.06, 0.46, r'$G = 6.67\times10^{-11}\ \mathrm{N\ m^2\ kg^{-2}}$', size=28)
        T(fig, 0.06, 0.26, 'r: distance between the CENTRES.  The two forces are\nequal and opposite (third law).  Double r: force ÷ 4.', size=21, color=SOFT)
        ax = wax(fig, [0.58, 0.45, 0.38, 0.30], (0, 10), (0, 4))
        ax.add_patch(Circle((2, 2), 1.2, fc=C1, ec=BG)); ax.add_patch(Circle((8, 2), 0.8, fc=C2, ec=BG))
        arrow(ax, (3.4, 2.0), (5.0, 2.0), color=GREEN, lw=4); arrow(ax, (7.1, 2.0), (5.5, 2.0), color=GREEN, lw=4)
        ax.annotate('', xy=(8, 0.35), xytext=(2, 0.35), arrowprops=dict(arrowstyle='<|-|>', color=YELLOW, lw=2)); label(ax, 5, 0.0, 'r', size=18, color=YELLOW)
        ax2 = gax(fig, [0.62, 0.12, 0.32, 0.26], (0, 4), (0, 1.2), 'r', 'F', ticks=False)
        rr = np.linspace(0.8, 4, 80); ax2.plot(rr, 1.0 / rr ** 2 * 0.75, color=C1, lw=3.5)
    elif s == 1:
        chip(fig, 'Element 1 · principles')
        geq(fig, 0.06, 0.74, r'$F_g = mg$', size=32)
        geq(fig, 0.06, 0.54, r'$g = \dfrac{F_g}{m}$  (definition)', size=30)
        geq(fig, 0.06, 0.34, r'$g = \dfrac{GM}{r^2}$', size=34)
        bullets(fig, ['Weight: the gravitational force on a body', 'A mass M creates a gravitational field around it', 'Field strength: force per kilogram, N kg⁻¹ = m s⁻²',
                      'g is the free-fall acceleration at that point', 'M sets the field; the small mass doesn’t matter'], 5, 0.48, 0.76, size=21, dim=False)
    else:
        chip(fig, 'Element 2 · problems')
        T(fig, 0.06, 0.78, 'Show that gravity follows an inverse square law', size=26, color=C2, weight='bold')
        ax = wax(fig, [0.04, 0.10, 0.32, 0.58], (-4, 4), (-4, 4)); ax.set_aspect('equal')
        _planet(ax, (0, 0), 1.0, C1); ax.add_patch(Circle((0, 0), 2.3, fill=False, ec=MUT, lw=2, ls='--'))
        ax.scatter([2.3 * 0.7], [2.3 * 0.7], s=250, color=YELLOW, zorder=6)
        label(ax, 0.0, -1.5, 'R = 6.37 × 10⁶ m', size=14, color=FG); label(ax, 1.5, 3.1, 'r = 7.20 × 10⁶ m', size=14, color=YELLOW)
        _work(fig, 0.40, 0.70, [(r'orbit: $a_c = \dfrac{4\pi^2 r}{T^2} = \dfrac{4\pi^2(7.20\times10^6)}{(6.08\times10^3)^2}$', FG, None),
                                (r'$= 7.6892\ \mathrm{m\ s^{-2}}$', FG, '= 7.69 m s⁻² (3 s.f.)'),
                                (r'inverse square: $9.81\left(\dfrac{6.37\times10^6}{7.20\times10^6}\right)^2 = 7.6786$', FG, '= 7.68 m s⁻² (3 s.f.)')], size=20, gap=0.085)
        T(fig, 0.40, 0.28, 'The two agree to 3 s.f.: so g ∝ 1/r². Or show that\ng × r² is the same constant at both places.', size=21, color=YELLOW)


def we_g(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: field strength at altitude')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        _q(fig, 'A satellite orbits 560 km above Earth’s surface. Earth’s radius is 6.37 × 10⁶ m and g at the surface is 9.81 N kg⁻¹.\nFind g at the satellite.', y=0.66, h=0.16, size=21)
    ax = wax(fig, [0.03, 0.06, 0.30, 0.56 if s == 0 else 0.70], (-4, 4), (-4, 4)); ax.set_aspect('equal')
    _planet(ax, (0, 0), 1.6, C1); ax.add_patch(Circle((0, 0), 1.6 * 6.93 / 6.37, fill=False, ec=MUT, lw=2, ls='--'))
    ax.scatter([0, 1.74 * 0.7], [0, 1.74 * 0.7], s=[40, 250], color=[FG, YELLOW], zorder=6)
    ax.plot([0, 1.74 * 0.7], [0, 1.74 * 0.7], color=YELLOW, lw=2)
    label(ax, 2.2, 0.9, 'r from the\ncentre', size=14, color=YELLOW)
    if s == 0:
        _work(fig, 0.36, 0.58, [(r'$r = 6.37\times10^6 + 0.560\times10^6 = 6.93\times10^6\ \mathrm{m}$', FG, None),
                                (r'$g \propto \dfrac{1}{r^2}$:  $g = 9.81\left(\dfrac{6.37}{6.93}\right)^2$', FG, None),
                                (r'$g = 8.2886\ \mathrm{N\ kg^{-1}}$', FG, '= 8.29 N kg⁻¹ (3 s.f.)')], size=22, gap=0.085)
        T(fig, 0.36, 0.25, 'r is measured from the centre of the Earth:\nadd the altitude to the radius.', size=21, color=PINK)
    else:
        _work(fig, 0.36, 0.78, [(r'check: $g = \dfrac{GM}{r^2} = \dfrac{6.67\times10^{-11}\times5.97\times10^{24}}{(6.93\times10^6)^2}$', FG, None),
                                (r'$= 8.29\ \mathrm{N\ kg^{-1}}$ ✓', FG, None)], size=21, gap=0.085)
        T(fig, 0.36, 0.52, 'The ratio method avoids needing Earth’s mass.\nCommon slips: altitude used as r; the Moon’s\nradius mixed with Earth’s g; diameter for radius.', size=21, color=SOFT)
        T(fig, 0.36, 0.26, 'At 560 km, g is still 85 % of its surface value\n(inputs 3 s.f.: 8.29 / 9.81 = 0.845).', size=21, color=YELLOW)


def _field_lines(ax, masses, nlines, color, rmax=3.8):
    """Gravitational field lines: traced outward from each mass against the field, with an arrow pointing inward."""
    for (mx, my, m), n in zip(masses, nlines):
        for k in range(n):
            a = TAU * (k + 0.5) / n
            p = np.array([mx + 0.18 * math.cos(a), my + 0.18 * math.sin(a)])
            pts = [p.copy()]
            for _ in range(900):
                f = np.zeros(2)
                for (qx, qy, mm) in masses:
                    d = np.array([qx, qy]) - p; r = np.hypot(*d)
                    f += mm * d / r ** 3
                step = -f / np.hypot(*f) * 0.03
                p = p + step
                if abs(p[0]) > rmax * 1.6 or abs(p[1]) > rmax or any(np.hypot(p[0] - qx, p[1] - qy) < 0.17 for (qx, qy, _) in masses if (qx, qy) != (mx, my)):
                    break
                pts.append(p.copy())
            pts = np.array(pts)
            ax.plot(pts[:, 0], pts[:, 1], color=color, lw=2.2)
            j = min(len(pts) - 1, 40)
            if j > 5:
                ax.annotate('', xy=pts[j - 4], xytext=pts[j], arrowprops=dict(arrowstyle='-|>', color=color, lw=2.2, mutation_scale=22))


def fields(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Gravitational fields', 'Fields around two masses', 'Adding fields'][s])
    if s == 0:
        chip(fig, 'Element 1 · principles')
        ax = wax(fig, [0.03, 0.08, 0.50, 0.72], (-3.6, 3.6), (-2.6, 2.6)); ax.set_aspect('equal')
        _field_lines(ax, [(0, 0, 1.0)], [12], C1, rmax=3.0)
        _planet(ax, (0, 0), 0.5, C2)
        k = 1.0 - 0.55 * ph
        ax.scatter([2.4 * k * 0.8], [2.4 * k * 0.6], s=240, color=YELLOW, zorder=7)
        bullets(fig, ['Strength and direction at every point', 'Lines point toward the mass', 'Closer lines: stronger field', 'One mass: straight, evenly spaced lines',
                      'Near the surface: parallel and\nevenly spaced'], 5, 0.56, 0.74, size=22, dim=False)
    elif s == 1:
        chip(fig, 'Element 1 · principles')
        ax = wax(fig, [0.02, 0.06, 0.58, 0.76], (-4.2, 4.2), (-3.0, 3.0)); ax.set_aspect('equal')
        masses = [(-1.6, 0.0, 4.0), (1.6, 0.0, 1.0)]
        _field_lines(ax, masses, [16, 4], C1, rmax=3.6)
        _planet(ax, (-1.6, 0), 0.5, C2); _planet(ax, (1.6, 0), 0.28, C2)
        ax.scatter([0.533], [0], s=160, color=YELLOW, zorder=8); label(ax, 0.53, 0.45, 'neutral\npoint', size=15, color=YELLOW)
        bullets(fig, ['Lines run INTO both masses', 'More lines end on the bigger mass', 'Lines never cross', 'A neutral point between them,\ncloser to the smaller mass',
                      'The boundary curves round the\nsmaller mass', 'Far away: looks like one mass'], 6, 0.62, 0.76, size=20, dim=False)
    else:
        chip(fig, 'Element 2 · problems')
        ax = wax(fig, [0.03, 0.10, 0.46, 0.66], (-1, 5), (-1, 4.4)); ax.set_aspect('equal')
        _planet(ax, (4.6, 0.5), 0.25, C2); _planet(ax, (0.6, 3.9), 0.25, C1)
        ax.scatter([0.6], [0.5], s=200, color=YELLOW, zorder=6); label(ax, 0.2, 0.0, 'P', size=19, color=YELLOW)
        _vec(ax, (0.6, 0.5), (2.6, 0.5), color=C2, text='g from the right-hand mass', tp=(2.8, 0.05), size=15)
        _vec(ax, (0.6, 0.5), (0.6, 2.1), color=C1, text='g from the upper mass', tp=(1.9, 2.0), size=15)
        _vec(ax, (0.6, 0.5), (2.6, 2.1), color=GREEN, text='total', tp=(2.3, 1.45), size=17)
        ax.plot([2.6, 2.6], [0.5, 2.1], color=GRID, lw=1.5, ls='--'); ax.plot([0.6, 2.6], [2.1, 2.1], color=GRID, lw=1.5, ls='--')
        card(fig, 0.53, 0.46, 0.42, 0.30, 'Each field', 'g = GM / r², toward its OWN mass.\nCalculate each, with its direction.', tcol=C1, size=21)
        bullets(fig, ['Add as vectors: in a line, with signs;\nat an angle, head to tail', 'Add fields, not forces', 'State the direction of the answer'], 3, 0.53, 0.38, size=20, dim=False)


def we_two(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: adding two fields')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        _q(fig, 'Planet A (9.00 × 10²⁴ kg) is 3.00 × 10⁸ m from point P, and planet B (1.20 × 10²⁵ kg) is 4.00 × 10⁸ m from P.\nThe angle at P between the two planets is 90°. Find the total gravitational field at P.', y=0.66, h=0.16, size=21)
    ax = wax(fig, [0.03, 0.04, 0.38, 0.58 if s == 0 else 0.72], (-1, 6.5), (-1, 7.5 if s else 5)); ax.set_aspect('equal')
    _planet(ax, (4.5, 0), 0.38, C1); _planet(ax, (0, 6.0 if s else 4.0), 0.5, C2)
    ax.scatter([0], [0], s=200, color=YELLOW, zorder=6); label(ax, -0.4, -0.5, 'P', size=19, color=YELLOW)
    label(ax, 4.5, -0.75, 'A', size=18, color=C1); label(ax, 0.8, 6.0 if s else 4.0, 'B', size=18, color=C2)
    ax.plot([0, 4.5], [0, 0], color=GRID, lw=1.5, ls=':'); ax.plot([0, 0], [0, 6.0 if s else 4.0], color=GRID, lw=1.5, ls=':')
    sa, sb = 0.55, 0.55
    _vec(ax, (0, 0), (6.67 * sa, 0), color=C1, text='g_A', tp=(2.0, -0.45), size=16)
    _vec(ax, (0, 0), (0, 5.0 * sb), color=C2, text='g_B', tp=(-0.5, 1.4), size=16)
    if s >= 1:
        _vec(ax, (0, 0), (6.67 * sa, 5.0 * sb), color=GREEN, text='total', tp=(2.4, 2.0), size=17)
        ax.plot([6.67 * sa, 6.67 * sa], [0, 5.0 * sb], color=GRID, lw=1.5, ls='--')
    if s == 0:
        _work(fig, 0.45, 0.58, [(r'$g_A = \dfrac{GM_A}{r^2} = \dfrac{6.67\times10^{-11}\times9.00\times10^{24}}{(3.00\times10^8)^2}$', FG, None),
                                (r'$= 6.67\times10^{-3}\ \mathrm{N\ kg^{-1}}$ toward A', FG, None),
                                (r'$g_B = \dfrac{6.67\times10^{-11}\times1.20\times10^{25}}{(4.00\times10^8)^2} = 5.00\times10^{-3}$ toward B', FG, None)], size=20, gap=0.085)
        T(fig, 0.45, 0.20, '(exact: 6.670 × 10⁻³ and 5.0025 × 10⁻³ N kg⁻¹, 3 s.f.)', size=17, color=MUT)
    elif s == 1:
        _work(fig, 0.45, 0.78, [(r'right angle: $g = \sqrt{g_A^2 + g_B^2}$', FG, None),
                                (r'$= \sqrt{(6.67\times10^{-3})^2 + (5.0025\times10^{-3})^2} = 8.3375\times10^{-3}\ \mathrm{N\ kg^{-1}}$', FG, '= 8.34 × 10⁻³ N kg⁻¹ (3 s.f.)'),
                                (r'$\tan\phi = \dfrac{5.0025}{6.67}$, $\phi = 36.9^\circ$ from g_A toward B', FG, None)], size=20, gap=0.085)
    else:
        bullets(fig, ['Two fields 60° apart (equilateral layout):\nthe head to tail triangle has an inside angle of 120°', 'Using 60° in the cosine rule was the most\ncommon error', 'Keep enough s.f. in the middle: when two fields\nalmost cancel, early rounding can give zero'],
                3, 0.45, 0.76, size=21, dim=False)
        T(fig, 0.45, 0.32, 'Label which field is which, and draw the triangle.', size=21, color=YELLOW)


def neutral(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Where the field is zero', 'Checking the neutral point'][s])
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.04, 0.50, 0.92, 0.26], (0, 10), (0, 4))
    ax.plot([1, 9], [1.5, 1.5], color=MUT, lw=2, ls=':')
    ax.add_patch(Circle((1, 1.5), 0.55, fc=C1, ec=BG)); ax.add_patch(Circle((9, 1.5), 0.3, fc=C2, ec=BG))
    label(ax, 1, 2.4, 'A  9.00 × 10²⁴ kg', size=17, color=C1); label(ax, 9, 2.4, 'B  1.00 × 10²⁴ kg', size=17, color=C2)
    xn = 1 + 8 * 0.75
    ax.scatter([xn], [1.5], s=220, color=YELLOW, zorder=6)
    if s == 1:
        arrow(ax, (xn, 1.5), (xn - 1.3, 1.5), color=C1, lw=4); arrow(ax, (xn, 1.5), (xn + 1.3, 1.5), color=C2, lw=4)
        label(ax, xn - 0.7, 0.8, 'g_A', size=15, color=C1); label(ax, xn + 0.7, 0.8, 'g_B', size=15, color=C2)
    ax.annotate('', xy=(xn, 0.55), xytext=(1, 0.55), arrowprops=dict(arrowstyle='<|-|>', color=YELLOW, lw=1.8)); label(ax, (1 + xn) / 2, 0.2, 'r = 4.5 × 10⁸ m', size=16, color=YELLOW)
    ax.annotate('', xy=(9, 0.55), xytext=(xn, 0.55), arrowprops=dict(arrowstyle='<|-|>', color=GREEN, lw=1.8)); label(ax, (xn + 9) / 2, 0.2, '1.5 × 10⁸ m', size=16, color=GREEN)
    if s == 0:
        _work(fig, 0.06, 0.44, [(r'$\dfrac{GM_A}{r^2} = \dfrac{GM_B}{(d - r)^2}$   cancel G, then take the square root:', FG, None),
                                (r'$\dfrac{\sqrt{M_A}}{r} = \dfrac{\sqrt{M_B}}{d - r}\ \Rightarrow\ r = d\,\dfrac{\sqrt{M_A}}{\sqrt{M_A} + \sqrt{M_B}}$', FG, None),
                                (r'$\sqrt{9.00}:\sqrt{1.00} = 3:1 \Rightarrow r = \frac{3}{4}(6.0\times10^8) = 4.5\times10^8\ \mathrm{m}$ from A', GREEN, None)], size=21, gap=0.085)
    else:
        _work(fig, 0.06, 0.44, [(r'from A: $\dfrac{6.67\times10^{-11}\times9.00\times10^{24}}{(4.5\times10^8)^2} = 2.96\times10^{-3}\ \mathrm{N\ kg^{-1}}$', FG, None),
                                (r'from B: $\dfrac{6.67\times10^{-11}\times1.00\times10^{24}}{(1.5\times10^8)^2} = 2.96\times10^{-3}\ \mathrm{N\ kg^{-1}}$', FG, None),
                                ('Equal and opposite: they cancel ✓. Prediction: the neutral point is\nmuch closer to the smaller mass, where the sketch’s boundary curves.', YELLOW, None)], size=21, gap=0.085)


def kepler(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Kepler’s third law', 'The ratio form', 'Geosynchronous satellites'][s])
    if s == 0:
        chip(fig, 'Element 1 · principles')
        geq(fig, 0.06, 0.72, r'$T^2 = \dfrac{4\pi^2 r^3}{GM}$', size=38)
        T(fig, 0.06, 0.52, 'Gravity is the centripetal force:\nGMm / r² = 4π²mr / T²   (the satellite’s mass cancels)', size=21, color=SOFT)
        bullets(fig, ['r: orbit radius, from the CENTRE of the central body', 'M: the central body’s mass, not the satellite’s', 'T in seconds'], 3, 0.06, 0.34, size=21, dim=False)
        ax = wax(fig, [0.56, 0.14, 0.40, 0.62], (-3, 3), (-2.6, 2.6)); ax.set_aspect('equal')
        _planet(ax, (0, 0), 0.7, C2); ax.add_patch(Circle((0, 0), 2.0, fill=False, ec=MUT, lw=2, ls='--'))
        a = TAU * ph + 0.5
        sx, sy = 2.0 * math.cos(a), 2.0 * math.sin(a)
        ax.scatter([sx], [sy], s=260, color=YELLOW, zorder=6)
        arrow(ax, (sx, sy), (sx * 0.55, sy * 0.55), color=PINK, lw=4); arrow(ax, (sx, sy), (sx - 0.8 * math.sin(a), sy + 0.8 * math.cos(a)), color=C1, lw=3.5)
        ax.plot([0, sx], [0, sy], color=YELLOW, lw=1.5, ls=':'); label(ax, sx * 0.3 + 0.35, sy * 0.3 - 0.3, 'r', size=18, color=YELLOW)
    elif s == 1:
        chip(fig, 'Element 2 · problems')
        eq(fig, 0.06, 0.72, r'$\left(\dfrac{T_1}{T_2}\right)^2 = \left(\dfrac{r_1}{r_2}\right)^3$', size=36)
        bullets(fig, ['Derived from the sheet formula: T²/r³ = 4π²/GM,\nthe same for bodies orbiting the same mass', 'No G or M needed: given one orbit, find another', 'Square the periods, cube the radii',
                      'Only for orbits around the SAME body'], 4, 0.06, 0.46, size=22, dim=False)
        ax = gax(fig, [0.62, 0.20, 0.32, 0.50], (0, 5), (0, 130), 'r³', 'T²', ticks=False)
        rr = np.linspace(0, 5, 50); ax.plot(rr, 25 * rr, color=C1, lw=4)
    else:
        chip(fig, 'Element 2 · problems')
        ax = wax(fig, [0.03, 0.08, 0.52, 0.72], (-7.6, 7.6), (-7.0, 7.0)); ax.set_aspect('equal')
        _planet(ax, (0, 0), 1.0, C1); ax.add_patch(Circle((0, 0), 6.63, fill=False, ec=MUT, lw=2.5, ls='--'))
        a = 0.5 + 0.0 * ph
        ax.scatter([6.63 * math.cos(a)], [6.63 * math.sin(a)], s=260, color=YELLOW, zorder=6)
        ax.scatter([math.cos(a)], [math.sin(a)], s=70, color=FG, zorder=6); ax.plot([math.cos(a), 6.63 * math.cos(a)], [math.sin(a), 6.63 * math.sin(a)], color=GRID, lw=1.5, ls=':')
        label(ax, 0, -3.4, 'geosynchronous: T = 24 h', size=17, color=YELLOW)
        _work(fig, 0.58, 0.76, [(r'$r^3 = \dfrac{GMT^2}{4\pi^2}$, $T = 86400\ \mathrm{s}$', FG, None),
                                (r'$r = 4.2227\times10^7\ \mathrm{m}$ from the centre', FG, '= 4.22 × 10⁷ m (3 s.f.)'),
                                ('altitude: 4.22 × 10⁷ − 6.37 × 10⁶ = 3.59 × 10⁷ m', FG, None),
                                (r'$v = 2\pi r/T = 3.07\times10^{3}\ \mathrm{m\ s^{-1}}$', FG, None)], size=19, gap=0.075)
        T(fig, 0.58, 0.28, 'Geostationary: also over the equator, same\ndirection: it hangs over one point. The height\nis fixed. Lower orbits: faster, shorter periods.', size=19, color=SOFT)


def we_orbit(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: moons of Mars')
    chip(fig, 'Element 2 · problems')
    if s == 0:
        _q(fig, 'Deimos orbits Mars at 2.346 × 10⁷ m with period 1.262 days. Phobos orbits at 9.38 × 10⁶ m. Find the period of\nPhobos, then use Deimos to find the mass of Mars.', y=0.66, h=0.16, size=21)
    ax = wax(fig, [0.03, 0.06, 0.30, 0.56 if s == 0 else 0.70], (-3.2, 3.2), (-3.2, 3.2)); ax.set_aspect('equal')
    _planet(ax, (0, 0), 0.5, C2); ax.add_patch(Circle((0, 0), 1.38, fill=False, ec=MUT, lw=2)); ax.add_patch(Circle((0, 0), 3.45 * 0.9, fill=False, ec=MUT, lw=2))
    ax.scatter([1.38 * 0.7], [1.38 * 0.7], s=130, color=YELLOW, zorder=6); ax.scatter([-3.1 * 0.7], [3.1 * 0.7 * 0.0 + 0.0], s=170, color=GREEN, zorder=6)
    label(ax, 1.4, 1.75, 'Phobos', size=14, color=YELLOW); label(ax, -2.2, 0.5, 'Deimos', size=14, color=GREEN)
    T(fig, 0.36, 0.115, 'Reference data for real moons: not from TASC.', size=15, color=MUT)
    if s == 0:
        _work(fig, 0.36, 0.58, [('Same central body: use the ratio form', SOFT, None),
                                (r'$T_P = 1.262\left(\dfrac{9.38\times10^6}{2.346\times10^7}\right)^{3/2}$', FG, None),
                                (r'$= 0.31906\ \mathrm{days}$', FG, '= 0.319 days = 7.66 h (3 s.f.)')], size=22, gap=0.085)
    elif s == 1:
        _work(fig, 0.36, 0.78, [(r'$T = 1.262\times86400 = 1.09\times10^{5}\ \mathrm{s}$', FG, None),
                                (r'$M = \dfrac{4\pi^2 r^3}{GT^2} = \dfrac{4\pi^2(2.346\times10^7)^3}{6.67\times10^{-11}\,(1.0904\times10^5)^2}$', FG, None),
                                (r'$= 6.4279\times10^{23}\ \mathrm{kg}$', FG, '= 6.43 × 10²³ kg (3 s.f.)')], size=21, gap=0.09)
        T(fig, 0.36, 0.34, 'r is the orbit radius, not the planet’s radius.\nUse each body’s own period: not the asteroid’s year\nfor a probe’s orbit.', size=20, color=PINK)
    else:
        _work(fig, 0.36, 0.78, [('0.107 of Earth’s mass (5.97 × 10²⁴ kg): plausible for\na much smaller planet ✓', FG, None),
                                (r'back-check: $2\pi\sqrt{\dfrac{(9.38\times10^6)^3}{GM}} = 0.319\ \mathrm{days}$ ✓', FG, None)], size=21, gap=0.12)
        T(fig, 0.36, 0.40, 'Two independent routes agree: the best evidence\nthat there is no slip in the working.', size=21, color=YELLOW)


def grav_data(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Linearising orbit data', 'Gradient and mass', 'Linearising force data'][s])
    chip(fig, 'Element 3 · data')
    if s <= 1:
        r3 = [0.1, 0.8, 2.7, 6.4]; T2 = [0.0591, 0.475, 1.60, 3.79]
        hdr = ['r (10⁸ m)', 'T (10⁴ s)', 'r³ (10²⁵ m³)', 'T² (10¹¹ s²)']
        rows = [['1.00', '7.69', '0.100', '0.0591'], ['2.00', '21.8', '0.800', '0.475'], ['3.00', '40.0', '2.70', '1.60'], ['4.00', '61.6', '6.40', '3.79']]
        for j, h_ in enumerate(hdr):
            T(fig, 0.05 + j * 0.115, 0.78, h_, size=15, color=C1 if j < 2 else GREEN, weight='bold')
        for i, rw in enumerate(rows):
            for j, v in enumerate(rw):
                T(fig, 0.05 + j * 0.115, 0.72 - i * 0.055, v, size=18, color=FG)
        T(fig, 0.05, 0.115, 'Made-up data for four moons of one planet: illustrative, not measured.', size=16, color=MUT)
        ax = gax(fig, [0.54, 0.16, 0.41, 0.58], (0, 7), (0, 4.4), 'r³ (10²⁵ m³)', 'T² (10¹¹ s²)')
        ax.scatter(r3, T2, s=130, color=YELLOW, zorder=6)
        ax.plot([0, 6.8], [0, 0.5929 * 6.8], color=C1, lw=3.5); ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([0, 1, 2, 3, 4])
        if s == 1:
            ax.plot([0.1, 6.4], [0.0591, 0.0591], color=GREEN, lw=2.5, ls='--'); ax.plot([6.4, 6.4], [0.0591, 3.79], color=GREEN, lw=2.5, ls='--')
            label(ax, 3.3, 0.35, 'run 6.3', size=16, color=GREEN); label(ax, 5.5, 2.0, 'rise\n3.7', size=16, color=GREEN)
        if s == 0:
            bullets(fig, ['T² ∝ r³: plot T² against r³', 'A straight line through the origin', 'Convert to seconds and metres first'], 3, 0.05, 0.36, size=21, dim=False)
        else:
            _work(fig, 0.05, 0.45, [(r'gradient $= \dfrac{3.7\times10^{11}}{6.3\times10^{25}} = 5.93\times10^{-15}$', FG, None),
                                    (r'$\mathrm{gradient} = \dfrac{4\pi^2}{GM} \Rightarrow M = \dfrac{4\pi^2}{G\times\mathrm{gradient}}$', FG, None),
                                    (r'$M = 9.982\times10^{25}\ \mathrm{kg}$', FG, '= 9.98 × 10²⁵ kg (3 s.f.)')], size=19, gap=0.075)
    else:
        for j, h_ in enumerate(['r (m)', 'F (10⁻⁹ N)', '1/r² (m⁻²)']):
            T(fig, 0.05 + j * 0.15, 0.78, h_, size=16, color=C1 if j < 2 else GREEN, weight='bold')
        for i, rw in enumerate([['0.100', '400', '100'], ['0.150', '178', '44.4'], ['0.200', '100', '25.0'], ['0.250', '64.0', '16.0']]):
            for j, v in enumerate(rw):
                T(fig, 0.05 + j * 0.15, 0.72 - i * 0.055, v, size=18)
        T(fig, 0.05, 0.115, 'Made-up data: a 5.0 kg and a 12 kg mass: illustrative, not measured.', size=16, color=MUT)
        ax = gax(fig, [0.54, 0.16, 0.41, 0.58], (0, 110), (0, 450), '1/r² (m⁻²)', 'F (10⁻⁹ N)')
        ax.scatter([100, 44.4, 25.0, 16.0], [400, 178, 100, 64.0], s=130, color=YELLOW, zorder=6); ax.plot([0, 105], [0, 4.0 * 105], color=C1, lw=3.5)
        _work(fig, 0.05, 0.40, [(r'$F = Gm_1m_2\times\dfrac{1}{r^2}$: gradient $= Gm_1m_2$', FG, None),
                                (r'gradient $= \dfrac{400 - 64.0}{100 - 16.0} = 4.0\times10^{-9}\ \mathrm{N\ m^2}$', FG, None),
                                (r'$G = \dfrac{4.0\times10^{-9}}{5.0\times12} = 6.67\times10^{-11}$', FG, '= 6.67 × 10⁻¹¹ N m² kg⁻² (3 s.f.)')], size=18, gap=0.07)


def weightless(fig, s, ph):
    C1, C2 = C()
    header(fig, ['Weightlessness is a sensation', 'Orbiting is free fall'][s])
    chip(fig, 'Element 1 · principles' if s == 0 else 'Element 4 · predictions')
    if s == 0:
        ax = wax(fig, [0.04, 0.12, 0.36, 0.66], (-2, 2), (-3, 3)); ax.set_aspect('equal')
        ax.add_patch(Rectangle((-1.5, -2.6), 3.0, 5.2, fc=PANEL, ec=MUT, lw=3))
        ax.add_patch(Circle((0, 0.6), 0.4, fc=FG, ec='none')); ax.plot([0, 0], [0.2, -1.0], color=FG, lw=6)
        ax.add_patch(Rectangle((-0.9, -2.3), 1.8, 0.3, fc=MUT, ec='none')); label(ax, 0, -1.7, 'scales: 0', size=16, color=YELLOW)
        arrow(ax, (1.0, 0.0), (1.0, -1.4), color=C2, lw=4); label(ax, 1.25, -0.6, 'g', size=17, color=C2)
        bullets(fig, ['You feel weight when a surface pushes up on you', 'If only gravity acts: nothing pushes back, so\nyou feel weightless', 'Free-falling lift: apparent weight\nm(g − a) = 0 when a = g',
                      'Gravity has NOT gone away'], 4, 0.44, 0.74, size=22, dim=False)
    else:
        ax = wax(fig, [0.03, 0.06, 0.54, 0.76], (-4, 4), (-3.6, 3.6)); ax.set_aspect('equal')
        _planet(ax, (0, 0), 2.0, C1)
        ax.add_patch(Rectangle((-0.12, 1.9), 0.24, 0.3, fc=FG, ec='none'))
        th = np.linspace(0, 1, 60)
        ax.plot(0.2 + 2.5 * th, 2.1 + 0.0 * th - 2.2 * th ** 2 * 0.0 - 0.8 * th ** 2 * 1.0, color=GREEN, lw=3, ls='--')
        ax.plot(0.2 + 3.7 * th, 2.1 - 1.0 * th ** 2 * 0.5 * 2.0, color=YELLOW, lw=3, ls='--')
        ax.add_patch(Circle((0, 0), 2.2, fill=False, ec=PINK, lw=3, ls='--'))
        a = TAU * ph + math.pi / 2
        ax.scatter([2.2 * math.cos(a)], [2.2 * math.sin(a)], s=260, color=PINK, zorder=6)
        label(ax, -3.0, 2.8, 'faster shot: lands further…', size=16, color=GREEN, ha='left'); label(ax, -3.0, -3.2, '…fast enough: the ground curves away\nas fast as it falls: an orbit', size=16, color=PINK, ha='left')
        bullets(fig, ['In orbit, gravity is still about 85 % of its\nsurface value (at 560 km)', 'Astronauts are in free fall, so they feel\nweightless', 'An orbit: a projectile so fast that it keeps\nmissing the ground'], 3, 0.60, 0.74, size=20, dim=False)


def _panel(fig, x, y, w, h, title, body, color, size=20):
    card(fig, x, y, w, h, title, body, tcol=color, size=size)


def grav_contexts(fig, s, ph):
    C1, C2 = C()
    if s == 2:
        header(fig, 'Contexts named in the course')
        chip(fig, 'Element 4 · predictions')
        cards = [('Forensic ballistics', 'Path predicted from gravity\nand air resistance; flight data\nmatched to weapons.', C1),
                 ('Artificial satellites', 'Low, medium, high Earth orbit;\nequatorial, polar. Debris can\nhit working satellites.', C2),
                 ('Planetary motion', 'Ptolemy: Earth-centred.\nCopernicus, Galileo: Sun-centred.\nKepler’s three laws; Newton\nshowed gravity explains them.', GREEN)]
        for i, (a_, b_, c_) in enumerate(cards):
            _panel(fig, 0.05 + i * 0.31, 0.38, 0.29, 0.40, a_, b_, c_, size=18)
        T(fig, 0.05, 0.22, 'Good topics for internal tasks and Criterion 4: the ideas you need are all in this video.', size=21, color=MUT)
        return
    header(fig, ['A comet near a huge planet', 'Slingshots, hidden masses and hot planets'][s])
    chip(fig, 'Element 4 · predictions')
    if s == 0:
        ax = wax(fig, [0.03, 0.12, 0.54, 0.66], (-2.0, 9.5), (-3, 3)); ax.set_aspect('equal')
        _planet(ax, (0.0, 0), 1.6, C2)
        ax.add_patch(Ellipse((5.3, 0), 3.9, 1.5, fill=False, ec=MUT, lw=2, ls='--'))
        for x, ln, nm in [(3.7, 1.0, 'C (near)'), (5.0, 0.62, 'B'), (6.4, 0.4, 'A (far)')]:
            ax.scatter([x], [0], s=300, color=YELLOW, zorder=6)
            arrow(ax, (x, 0.0), (x - ln * 1.2, 0.0), color=PINK, lw=4)
            label(ax, x, -1.1, nm, size=15, color=FG)
        label(ax, 5.3, 1.3, 'comet', size=15, color=SOFT)
        bullets(fig, ['Field stronger on the near side,\nand NOT linear (1/r²)', 'So C accelerates more than B,\nB more than A', 'Differences pull the comet apart if\nthey beat its own cohesion', 'In orbit: only B has the right\nspeed, so it is stretched'],
                4, 0.60, 0.74, size=19, dim=False)
    else:
        cards = [('Gravity assist', 'Probe and planet get equal and\nopposite changes in momentum.\nPlanet’s Δv: negligible.\nPass behind: probe speeds up.\nPass ahead: slows down.', C1),
                 ('A hidden central mass', 'From a star’s orbit:\nM = 4π²r³ / (GT²)  or  v²r / G.\nHuge mass, tiny region:\nsuggests a black hole.', C2),
                 ('A planet very near its star', 'Kepler gives the orbit radius\nfrom the period. Compare with\nEarth and Mercury: very close\nmeans too hot for life.', GREEN)]
        for i, (a_, b_, c_) in enumerate(cards):
            _panel(fig, 0.05 + i * 0.31, 0.38, 0.29, 0.40, a_, b_, c_, size=18)


# ============================================================================ finish
def exam_tips(fig, s, ph):
    C1, C2 = C()
    if s >= 4:
        summary_panel(fig, ph)
        return
    header(fig, 'Tips from examiners')
    tips = ['Changes in momentum and vector sums:\ndraw the vector diagram; give directions', 'Convert before substituting: km/h ÷ 3.6,\nkm → m, days → s, tonnes → kg',
            'Forces from the object, roughly to scale;\nno centripetal arrow', 'Explain: name the law and the object;\nuse nouns, not “it”',
            'Don’t round in the middle; write the\nnumbers you substitute', '“Show that”: your own value to 3 s.f.;\nuse the given one only if you can’t',
            'Check every square, square root and cube;\nperiod squared, radius cubed', 'Orbits: r is from the centre:\nadd the altitude to the radius']
    n = [2, 4, 6, 8][s]
    cols = [C1, C2, PINK, GREEN, YELLOW, C1, C2, PINK]
    for i in range(n):
        x = 0.05 + (i % 2) * 0.46; y = 0.66 - (i // 2) * 0.165
        box(fig, x, y, 0.44, 0.145, fc=PANEL)
        T(fig, x + 0.015, y + 0.0725, str(i + 1), size=36, color=cols[i], weight='bold', va='center')
        T(fig, x + 0.07, y + 0.0725, tips[i], size=21, va='center')
    T(fig, 0.05, 0.13, 'From markers’ comments in TASC assessment reports', size=18, color=MUT)


def more_tips(fig, s, ph):
    C1, C2 = C()
    header(fig, 'More tips from examiners')
    tips = ['Power and energy rates: energy each second;\nnot a force × a fluid’s speed', 'Graphs: exact scale readings, areas not F × s,\nstraight ruled lines',
            'Collision: momentum. Swing afterwards:\nenergy. Label the stages', 'Vertical motion: include the weight;\nkeep the signs consistent',
            'Cosine rule on fields or momenta: use the\nangle inside the triangle', 'Neutral point: cancel G, take the\nsquare root at once',
            'Elastic or inelastic: compare kinetic\nenergies, not momenta', 'Read the marks: one mark, one step;\n“derive” needs every step']
    n = [4, 8][s]
    cols = [C1, C2, PINK, GREEN, YELLOW, C1, C2, PINK]
    for i in range(n):
        x = 0.05 + (i % 2) * 0.46; y = 0.66 - (i // 2) * 0.165
        box(fig, x, y, 0.44, 0.145, fc=PANEL)
        T(fig, x + 0.015, y + 0.0725, str(i + 9), size=36, color=cols[i], weight='bold', va='center')
        T(fig, x + 0.07, y + 0.0725, tips[i], size=21, va='center')
    T(fig, 0.05, 0.13, 'From markers’ comments in TASC assessment reports', size=18, color=MUT)


def summary_panel(fig, ph):
    C1, C2 = C()
    header(fig, 'Criterion 5 in one screen')
    chips_ = [('v = u + at', C1), ('s = ut + ½at²', C1), ('2as = v² − u²', C1), ('graphs: slope, area', C1),
              ('F = ma = Δp/Δt', C2), ('p = mv', C2), ('Δp = p_f − p_i', C2), ('Σp conserved', C2),
              ('a = v²/r = 4π²r/T²', PINK), ('F_c = mv²/r', PINK),
              ('W = Fs cosθ', GREEN), ('E_p = mgh', GREEN), ('E_K = ½mv²', GREEN), ('P = W/t', GREEN),
              ('F = Gm₁m₂/r²', YELLOW), ('g = GM/r²', YELLOW), ('T² = 4π²r³/GM', YELLOW), ('(T₁/T₂)² = (r₁/r₂)³', YELLOW), ('weightlessness', YELLOW)]
    x, y = 0.06, 0.75
    for t, c in chips_:
        w = len(t) * 0.0105 + 0.012
        if x + w > 0.95:
            x = 0.06; y -= 0.10
        chip(fig, t, color=c, size=24, x=x, y=y, ha='left')
        x += w + 0.015
    T(fig, 0.06, 0.22, 'Know what is on the sheet, draw the diagram, keep your signs,\nand always say WHY.', size=28, color=YELLOW, weight='bold')


def summary(fig, s, ph):
    summary_panel(fig, ph)
