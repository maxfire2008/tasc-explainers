"""Draw functions for PHY415115 Criterion 7 (wave motion).

Every function has the signature draw(fig, s, ph):
  s  = step index within the scene (the slide builds up as s increases)
  ph = animation phase in [0, 1) for animated steps (Step.anim), 0 for stills.
Animations must loop seamlessly: anything periodic must complete a whole number of
cycles as ph goes 0 -> 1.
Colours: C1 = course accent, C2 = module accent (from the theme), PINK/GREEN/YELLOW are semantic.
"""
import numpy as np
from matplotlib.patches import Circle, Rectangle, Polygon, FancyArrowPatch, Arc

from explainer import layout as L
from explainer.layout import (header, T, bullets, box, card, eq, sheet_eq, learn_eq, chip, wax, gax, darrow, arrow,
                              label, frac, FG, SOFT, MUT, GRID, PANEL, PANEL2, BG, PINK, GREEN, YELLOW, CM_WAVE, TAU)


def C():
    return L.A1(), L.A2()


# ============================================================================ overview
def title_card(fig, s, ph):
    intro(fig, 0, ph)


def overview(fig, s, ph):
    intro(fig, s + 1, ph)


def intro(fig, s, ph):
    C1, C2 = C()
    if s == 0:
        fig.text(0.5, 0.74, 'CRITERION 7', ha='center', color=C1, fontsize=30, weight='bold')
        fig.text(0.5, 0.60, 'Identify and apply general\nprinciples of wave motion', ha='center', va='center',
                 color=FG, fontsize=66, weight='bold', linespacing=1.15)
        fig.text(0.5, 0.445, 'TASC Physics  PHY415115   ·   revision for class tests and the exam', ha='center',
                 color=SOFT, fontsize=26)
        ax = wax(fig, [0, 0.06, 1, 0.28], (0, 10), (-1.6, 1.6))
        x = np.linspace(0, 10, 900)
        for c, a, k, n, lw in [(C1, 1.0, TAU / 5, 1, 4), (PINK, 0.55, TAU / 2.5, 2, 3), (C2, 0.3, TAU / 1.25, 4, 2.5)]:
            ax.plot(x, a * np.sin(k * x - TAU * n * ph), color=c, lw=lw, alpha=0.9)
        return
    if s == 1:
        header(fig, 'How Criterion 7 is assessed')
        card(fig, 0.05, 0.50, 0.40, 0.25, 'Internal', 'Your teacher: class tests, practicals\nand tasks during the year',
             tcol=GREEN)
        card(fig, 0.05, 0.20, 0.40, 0.25, 'External', 'End-of-year TASC exam:\nSection C is all Criterion 7', tcol=C2)
        tiles = [('≈45 min', 'suggested time'), ('45', 'marks'), ('5–7', 'compulsory questions'),
                 ('Info sheet', '+ approved calculator')]
        for i, (big, small) in enumerate(tiles):
            x = 0.52 + (i % 2) * 0.225; y = 0.50 - (i // 2) * 0.30
            box(fig, x, y, 0.205, 0.25, fc=PANEL2)
            T(fig, x + 0.1025, y + 0.16, big, size=46 if len(big) < 8 else 36, color=YELLOW, weight='bold', ha='center',
              va='center')
            T(fig, x + 0.1025, y + 0.06, small, size=21, color=SOFT, ha='center', va='center')
        T(fig, 0.52, 0.16, 'Section C of the exam (external assessment specifications)', size=18, color=MUT)
        return
    if s == 2:
        header(fig, 'The four elements of Criterion 7')
        items = [('Element 1', 'Principles', 'identify, describe and\nexplain wave principles'),
                 ('Element 2', 'Problems', 'solve numerical\nproblems'),
                 ('Element 3', 'Data', 'interpret and analyse\ngraphs and tables'),
                 ('Element 4', 'Predictions', 'predict in familiar and\nunfamiliar contexts')]
        for i, (n, t, b) in enumerate(items):
            x = 0.05 + i * 0.228
            box(fig, x, 0.22, 0.21, 0.50)
            T(fig, x + 0.02, 0.69, n, size=34, color=[C1, C2, PINK, GREEN][i], weight='bold')
            T(fig, x + 0.02, 0.47, t, size=32, color=FG, weight='bold')
            T(fig, x + 0.02, 0.40, b, size=22, color=SOFT)
        T(fig, 0.05, 0.16, 'Numbered in the order they appear in the course document’s standards table', size=19,
          color=MUT)
        return
    if s == 3:
        header(fig, 'What the standards ask for')
        cols = [(0.30, 'C', GREEN), (0.51, 'B', C1), (0.72, 'A', C2)]
        for x, l, c in cols:
            T(fig, x, 0.77, l, size=40, color=c, weight='bold')
        rows = [('E1 Principles', 'identifies', 'describes', 'explains'),
                ('E2 Problems', 'straightforward', 'multi-step', 'complex, and\nchecks validity'),
                ('E3 Data', 'interprets', 'analyses to get\nnew information', 'analyses, evaluates,\ngeneralises'),
                ('E4 Predictions', 'familiar contexts', 'unfamiliar contexts',
                 'reasoned predictions in\nunfamiliar, real-world contexts')]
        for j, r in enumerate(rows):
            y = 0.665 - j * 0.145
            box(fig, 0.05, y - 0.105, 0.90, 0.125, fc=PANEL if j % 2 == 0 else PANEL2)
            T(fig, 0.065, y - 0.042, r[0], size=26, color=FG, weight='bold', va='center')
            for (x, _, c), txt in zip(cols, r[1:]):
                T(fig, x, y - 0.042, txt, size=22, color=SOFT if c != C2 else FG, va='center')
        return
    header(fig, 'Roadmap')
    parts = [('Part 1', 'What waves are, and how we describe them', C1),
             ('Part 2', 'Boundaries: reflection, transmission, refraction', C2),
             ('Part 3', 'Superposition, beats, standing waves, resonance', PINK),
             ('Part 4', 'Interference, diffraction, polarisation, light', GREEN),
             ('Finish', 'Tests & exam technique, and a one-screen summary', YELLOW)]
    for i, (a, b, c) in enumerate(parts):
        y = 0.70 - i * 0.125
        box(fig, 0.05, y - 0.05, 0.90, 0.10)
        T(fig, 0.07, y, a, size=30, color=c, weight='bold', va='center')
        T(fig, 0.20, y, b, size=30, color=FG, va='center')


# ============================================================================ part 1
def transverse(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Transverse waves')
    ax = wax(fig, [0.05, 0.36, 0.90, 0.44], (0, 12), (-2.2, 2.2))
    lam, A = 4.0, 1.3
    x = np.linspace(0.3, 11.7, 39)
    y = A * np.sin(TAU / lam * x - TAU * ph)
    ax.axhline(0, color=GRID, lw=1.5, ls='--')
    xx = np.linspace(0.3, 11.7, 600)
    ax.plot(xx, A * np.sin(TAU / lam * xx - TAU * ph), color=MUT, lw=1.5, alpha=0.6)
    ax.scatter(x, y, s=170, color=C1, zorder=3)
    i = 13
    ax.plot([x[i], x[i]], [-A, A], color=PINK, lw=2, ls=':', alpha=0.8)
    ax.scatter([x[i]], [y[i]], s=420, color=PINK, zorder=4, edgecolor=FG, lw=2)
    arrow(ax, (7.0, 1.95), (10.5, 1.95), color=C2)
    label(ax, 6.8, 1.95, 'direction of travel', size=22, color=C2, ha='right')
    if s >= 1:
        darrow(ax, (x[i] + 0.55, -1.1), (x[i] + 0.55, 1.1), color=PINK)
        label(ax, x[i] - 0.75, 0.25, 'particle\nmotion', size=20, color=PINK, ha='right', zorder=10, bbox=dict(fc=BG, ec='none', pad=2))
    items = ['A wave transfers energy, not matter: each particle\noscillates about its rest position']
    if s >= 1:
        items += ['Transverse: particles oscillate ⊥ to the direction of travel',
                  'e.g. waves on strings · water ripples · seismic S-waves']
    bullets(fig, items, len(items), 0.06, 0.30, size=26)


def longitudinal(fig, s, ph):
    C1, C2 = C()
    if s <= 1:
        header(fig, 'Longitudinal waves')
        ax = wax(fig, [0.05, 0.40, 0.90, 0.40], (0, 12), (-1.6, 2.2))
        lam, a = 4.0, 0.38
        x0 = np.arange(0.15, 12, 0.22)
        xs = x0 + a * np.sin(TAU / lam * x0 - TAU * ph)
        for r in np.linspace(-1.2, 0.9, 6):
            ax.scatter(xs, np.full_like(xs, r), s=38, color=C1, alpha=0.85)
        j = 27
        ax.scatter(xs[j] * np.ones(6), np.linspace(-1.2, 0.9, 6), s=90, color=PINK, zorder=4)
        darrow(ax, (x0[j] - a, -1.48), (x0[j] + a, -1.48), color=PINK, ms=16)
        for m in range(-1, 4):
            xc = (0.5 + ph + m) * lam; xr = (ph + m) * lam
            if 0.3 < xc < 11.7: label(ax, xc, 1.35, 'C', size=24, color=YELLOW, weight='bold')
            if 0.3 < xr < 11.7: label(ax, xr, 1.35, 'R', size=24, color=SOFT, weight='bold')
        arrow(ax, (7.0, 1.95), (10.5, 1.95), color=C2)
        label(ax, 6.8, 1.95, 'direction of travel', size=22, color=C2, ha='right')
        bullets(fig, ['Particles oscillate ∥ to the direction of travel', 'Compressions (C) and rarefactions (R)',
                      'e.g. sound · seismic P-waves'], 3, 0.06, 0.33, size=26)
        if s == 1:
            card(fig, 0.58, 0.10, 0.37, 0.22, 'Mechanical wave', 'needs a medium (air, water, rock)\n→ no sound in space',
                 tcol=GREEN, size=23)
        return
    header(fig, 'Light: an electromagnetic wave')
    ax = wax(fig, [0.04, 0.36, 0.92, 0.47], (-0.5, 12.5), (-2.4, 2.4))
    lam = 4.0
    x = np.linspace(0, 12, 400)
    E = 1.7 * np.sin(TAU / lam * x - TAU * ph)
    zx, zy = -0.55, -0.42
    ax.plot([0, 12], [0, 0], color=MUT, lw=1.5)
    ax.plot(x, E, color=PINK, lw=3.5); ax.plot(x + zx * E, zy * E, color=C1, lw=3.5)
    for xi in x[::8]:
        e = 1.7 * np.sin(TAU / lam * xi - TAU * ph)
        ax.plot([xi, xi], [0, e], color=PINK, lw=1, alpha=0.5)
        ax.plot([xi, xi + zx * e], [0, zy * e], color=C1, lw=1, alpha=0.5)
    label(ax, -0.2, 2.0, 'E field', size=24, color=PINK, ha='left')
    label(ax, 0.3, -1.95, 'B field', size=24, color=C1, ha='left')
    arrow(ax, (12.0, 0), (12.5, 0), color=C2)
    bullets(fig, ['Oscillating electric and magnetic fields, ⊥ to each other and to travel',
                  'Behaves as a transverse wave · needs no medium'], 2, 0.06, 0.31, size=26)
    sheet_eq(fig, 0.62, 0.15, r'$c = 3.00\times10^{8}\ \mathrm{m\ s^{-1}}$', size=34)


def shm(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Simple harmonic motion underlies every wave')
    ax = wax(fig, [0.04, 0.26, 0.92, 0.54], (0, 23), (-4, 4))
    R = 2.5; th = TAU * 2 * ph; py = R * np.sin(th)
    ax.add_patch(Circle((3, 0), R, fill=False, ec=MUT, lw=2))
    ax.plot([3, 3 + R * np.cos(th)], [0, py], color=MUT, lw=1.5)
    ax.scatter([3 + R * np.cos(th)], [py], s=220, color=C1, zorder=4)
    ax.axhline(0, color=GRID, lw=1.2, ls='--')
    top, mx = 3.9, 8
    ys = np.linspace(top, py + 0.45, 40)
    zz = np.where(np.arange(40) % 2 == 0, -0.3, 0.3); zz[0] = zz[-1] = 0
    ax.plot([mx - 0.8, mx + 0.8], [top, top], color=SOFT, lw=4)
    ax.plot(mx + zz, ys, color=SOFT, lw=2)
    ax.add_patch(Rectangle((mx - 0.45, py - 0.45), 0.9, 0.9, fc=PINK, ec=FG, lw=1.5, zorder=4))
    u = np.linspace(0, 1, 500); gx = 11 + 11.5 * u; gy = R * np.sin(TAU * 2 * u)
    ax.plot(gx, gy, color=MUT, lw=2, alpha=0.4)
    k = u <= ph
    ax.plot(gx[k], gy[k], color=C1, lw=3.5)
    cx = 11 + 11.5 * ph
    ax.scatter([cx], [py], s=150, color=C1, zorder=4)
    ax.plot([3 + R * np.cos(th), cx], [py, py], color=C1, lw=1.2, ls=':', alpha=0.8)
    arrow(ax, (11, -3.3), (22.8, -3.3), color=SOFT, lw=2, ms=18)
    label(ax, 22.6, -3.75, 'time', size=18, color=SOFT, ha='right')
    if s >= 1:
        darrow(ax, (11 + 11.5 * 0.125, 0), (11 + 11.5 * 0.125, R), color=YELLOW, ms=16)
        label(ax, 11 + 11.5 * 0.125 + 0.3, R / 2, 'A', size=26, color=YELLOW, ha='left', weight='bold')
        T(fig, 0.06, 0.20, 'A = amplitude: largest displacement from rest\nOne trip around the circle = one period, T', size=24, color=SOFT)
    if s >= 2:
        F = -0.75 * py
        if abs(F) > 0.12:
            arrow(ax, (mx + 1.0, py), (mx + 1.0, py + F), color=C2, lw=4, ms=24)
        label(ax, 0.2, -3.5, 'restoring force → towards rest', size=20, color=C2, ha='left')
        card(fig, 0.62, 0.05, 0.33, 0.175, 'Restoring force', 'always points back to rest;\nbigger displacement → bigger force',
             tcol=C2, size=21)


def quantities(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Describing a wave')
    ax = wax(fig, [0.05, 0.40, 0.52, 0.40], (0, 10), (-1.9, 1.9))
    lam, A = 4.0, 1.2
    shift = ph if s >= 2 else 0
    x = np.linspace(0, 10, 600)
    ax.axhline(0, color=GRID, lw=1.5, ls='--')
    ax.plot(x, A * np.sin(TAU / lam * (x - lam * shift)), color=C1, lw=4)
    xc = lam / 4 + lam * shift
    while xc > 3.0: xc -= lam
    if xc < 0.6: xc += lam
    darrow(ax, (xc, 1.55), (xc + lam, 1.55), color=C2, ms=18)
    for q in (xc, xc + lam): ax.plot([q, q], [A, 1.55], color=C2, lw=1.2, ls=':')
    label(ax, xc + lam / 2, 1.8, 'λ', size=30, color=C2, weight='bold')
    xa = xc + 2 * lam if xc + 2 * lam < 9.6 else xc + lam
    darrow(ax, (xa, 0), (xa, A), color=YELLOW, ms=18)
    label(ax, xa + 0.3, A / 2, 'A', size=30, color=YELLOW, ha='left', weight='bold')
    rows = [('A', 'amplitude', 'max displacement', 'm', YELLOW), ('λ', 'wavelength', 'crest to crest', 'm', C2),
            ('T', 'period', 'time for one cycle', 's', C1), ('f', 'frequency', 'cycles per second', 'Hz', PINK),
            ('v', 'wave speed', '', 'm s⁻¹', GREEN)]
    n = [2, 4, 5, 5][s]
    for i in range(n):
        sym, name, desc, unit, c = rows[i]
        y = 0.75 - i * 0.105
        box(fig, 0.61, y - 0.085, 0.34, 0.09)
        T(fig, 0.625, y - 0.04, sym, size=34, color=c, weight='bold', va='center')
        T(fig, 0.665, y - 0.025, name, size=24, color=FG, va='center')
        T(fig, 0.665, y - 0.062, desc, size=17, color=SOFT, va='center')
        T(fig, 0.94, y - 0.04, unit, size=24, color=SOFT, va='center', ha='right')
    if s >= 1: sheet_eq(fig, 0.07, 0.29, r'$f = \dfrac{1}{T}$', size=40)
    if s >= 2: sheet_eq(fig, 0.31, 0.29, r'$v = \lambda f$', size=48, color=GREEN)
    if s >= 3:
        card(fig, 0.05, 0.05, 0.52, 0.115, 'f is set by the source', 'new medium → v and λ change, f stays the same',
             tcol=PINK, size=19)


def graphs(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Two graphs that look the same')
    t = np.linspace(0, 12, 600); xx = np.linspace(0, 54, 600)
    a1 = gax(fig, [0.56, 0.53, 0.39, 0.27], (0, 54), (-0.65, 0.65), 'distance x (m)', 'y (m)')
    a1.plot(xx, 0.4 * np.sin(TAU * xx / 18), color=C1, lw=3)
    darrow(a1, (4.5, 0.52), (22.5, 0.52), color=C2, ms=16)
    a1.text(13.5, 0.585, 'λ = 18 m', color=C2, fontsize=18, ha='center', va='center')
    a1.set_title('displacement–distance: a snapshot', color=FG, fontsize=20, loc='left')
    if s >= 1:
        a2 = gax(fig, [0.56, 0.13, 0.39, 0.27], (0, 12), (-0.65, 0.65), 'time t (s)', 'y (m)')
        a2.plot(t, 0.4 * np.sin(TAU * t / 4), color=PINK, lw=3)
        darrow(a2, (1, 0.52), (5, 0.52), color=C2, ms=16)
        a2.text(3, 0.585, 'T = 4.0 s', color=C2, fontsize=18, ha='center', va='center')
        a2.set_title('displacement–time: one point', color=FG, fontsize=20, loc='left')
        if s >= 4:
            t0, m, y0 = 4.5, 0.4443, 0.2828
            tt = np.array([3.7, 5.2])
            a2.plot(tt, y0 + m * (tt - t0), color=YELLOW, lw=2.5)
            a2.plot([3.7, 5.2, 5.2], [y0 + m * (3.7 - t0)] * 2 + [y0 + m * (5.2 - t0)], color=YELLOW, lw=1.5, ls='--')
            a2.scatter(tt, y0 + m * (tt - t0), color=YELLOW, s=60, zorder=5)
    if s <= 1:
        it = ['Displacement–distance graph = snapshot\nof the whole wave at one instant', 'Crest to crest = wavelength λ']
        if s == 1: it += ['Displacement–time graph = one point\nfollowed over time', 'Crest to crest = period T',
                          'Check the x-axis first!']
        bullets(fig, it, len(it), 0.06, 0.76, size=26)
        return
    chip(fig, 'Element 3 · data')
    card(fig, 0.05, 0.53, 0.47, 0.25, 'Example: a buoy at sea',
         'y–t graph: amplitude 0.40 m, period 4.0 s\nsnapshot: crests 18 m apart\nFind the frequency and the wave speed.',
         tcol=C2, size=23)
    if s >= 3:
        T(fig, 0.06, 0.47, r'$f = \dfrac{1}{T} = \dfrac{1}{4.0} = 0.25\ \mathrm{Hz}$', size=30, color=FG)
        T(fig, 0.06, 0.37, r'$v = \lambda f = 0.25\times18 = 4.5\ \mathrm{m\ s^{-1}}$', size=30, color=GREEN)
    if s >= 4:
        bullets(fig, ['Particle velocity = gradient of the y–t graph', 'Tangent at t = 4.5 s: ≈ 0.44 m s⁻¹',
                      'Use two far-apart points · show them · units'], 3, 0.06, 0.25, size=22, gap=0.012, dim=False,
                mcol=YELLOW)


def direction(fig, s, ph):
    """Which way is the wave travelling? (snapshot + y-t graph of one point)."""
    C1, C2 = C()
    header(fig, 'Which way is the wave travelling?')
    ax = gax(fig, [0.06, 0.45, 0.50, 0.32], (0, 12), (-1.5, 1.5), 'distance x (m)', 'y', ticks=False)
    x = np.linspace(0, 12, 600)
    ax.plot(x, np.sin(TAU * x / 8), color=C1, lw=3.5)
    ax.set_title('snapshot at t = 0', color=FG, fontsize=20, loc='left')
    xp = 7.0; yp = np.sin(TAU * xp / 8)
    ax.scatter([xp], [yp], s=160, color=YELLOW, zorder=5); label(ax, xp + 0.4, yp - 0.35, 'P', size=24, color=YELLOW)
    if s >= 1:
        ax.plot(x, np.sin(TAU * (x - 0.6) / 8), color=C2, lw=2.5, ls='--')
        yp2 = np.sin(TAU * (xp - 0.6) / 8)
        arrow(ax, (xp - 0.25, yp), (xp - 0.25, yp2), color=YELLOW, lw=3, ms=18)
        label(ax, 10.6, -1.2, 'shifted right a little', size=17, color=C2)
    if s >= 2:
        a2 = gax(fig, [0.06, 0.09, 0.50, 0.26], (0, 4), (-1.5, 1.5), 'time t (s)', 'y of P', ticks=False)
        tt = np.linspace(0, 4, 400)
        a2.plot(tt, np.sin(TAU * 7 / 8 - TAU * tt / 2), color=PINK, lw=3)
        a2.set_title('P over time: moves DOWN just after t = 0', color=FG, fontsize=19, loc='left')
    if s == 0:
        bullets(fig, ['A snapshot alone can’t tell you', 'Find how ONE point moves next', '(e.g. from its y–t graph)'],
                3, 0.60, 0.76, size=25, dim=False)
    elif s == 1:
        bullets(fig, ['Trick: shift the snapshot slightly\nin a guessed direction', 'See which way P must move',
                      'Shifted right → P moves down'], 3, 0.60, 0.76, size=25, dim=False)
    else:
        chip(fig, 'Element 3 · data')
        bullets(fig, ['y–t graph: P moves down next', 'Matches the right-shift', '∴ wave travels to the RIGHT (+x)',
                      'Moved up instead? → travelling left'], 4, 0.60, 0.72, size=25, dim=False)


# ============================================================================ part 2
def _pulse(u):
    return np.where(u > 0, np.exp(-u ** 2 / (2 * 0.22 ** 2)), np.exp(-u ** 2 / (2 * 0.6 ** 2)))


def pulses(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Pulses at boundaries')
    ax = wax(fig, [0.05, 0.42, 0.90, 0.38], (0, 10), (-1.45, 1.6))
    t = 4 * ph
    x = np.linspace(0, 10, 1500)
    ax.axhline(0, color=GRID, lw=1.2, ls='--')
    if s <= 1:
        Lw = 9.4; v = 2 * (Lw - 1.4) / 4; c = 1.4 + v * t
        sg = -1 if s == 0 else 1
        xs = x[x <= Lw]
        y = _pulse(xs - c) + sg * _pulse(2 * Lw - xs - c)
        ax.plot(xs, y, color=C1, lw=4)
        if s == 0:
            ax.add_patch(Rectangle((Lw, -1.4), 0.6, 2.8, fc=PANEL2, ec=SOFT, hatch='//', lw=1.5))
            label(ax, Lw + 0.3, 1.5, 'fixed end', size=20, color=SOFT)
        else:
            ax.plot([Lw, Lw], [-1.4, 1.45], color=SOFT, lw=5)
            ax.add_patch(Rectangle((Lw - 0.12, y[-1] - 0.12), 0.24, 0.24, fc=YELLOW, ec=FG, zorder=5))
            label(ax, Lw, 1.55, 'free end (ring on pole)', size=20, color=SOFT, ha='right')
        if t < 2: arrow(ax, (c - 0.3, 1.2), (c + 0.7, 1.2), color=C2, lw=2.5, ms=20)
        else:
            cr = 2 * Lw - c; arrow(ax, (cr + 0.3, 1.2 * sg), (cr - 0.7, 1.2 * sg), color=C2, lw=2.5, ms=20)
        txt = (['Fixed end → reflected pulse inverted\n(phase change of ½ cycle, 180°)'] if s == 0 else
               ['Free end → reflected pulse upright (no phase change)'])
        bullets(fig, txt, 1, 0.06, 0.34, size=27)
        return
    heavy_first = (s == 3)
    xb, c0 = 5.0, 1.0
    if not heavy_first: v1 = 2.25; v2 = v1 / 2
    else: v1 = 1.6; v2 = 2 * v1
    Z1, Z2 = 1 / v1, 1 / v2
    r = (Z1 - Z2) / (Z1 + Z2); tau = 2 * Z1 / (Z1 + Z2)
    c = c0 + v1 * t
    xl = x[x < xb]; xr = x[x >= xb]
    yl = _pulse(xl - c) + r * _pulse(2 * xb - xl - c)
    yr = tau * _pulse(xb + (xr - xb) * v1 / v2 - c)
    lw1, lw2 = (2.5, 6) if not heavy_first else (6, 2.5)
    ax.plot(xl, yl, color=C1, lw=lw1); ax.plot(xr, yr, color=GREEN, lw=lw2)
    ax.axvline(xb, color=MUT, lw=1.5, ls=':')
    label(ax, 2.5, -1.3, 'heavy string' if heavy_first else 'light string', size=20, color=C1)
    label(ax, 7.5, -1.3, 'light string' if heavy_first else 'heavy string', size=20, color=GREEN)
    t1 = (xb - c0) / v1
    if t < t1: arrow(ax, (c - 0.3, 1.25), (c + 0.7, 1.25), color=C2, lw=2.5, ms=20)
    else:
        cr = 2 * xb - c; ct = xb + (c - xb) * v2 / v1
        if cr > 0.4: arrow(ax, (cr + 0.3, 0.75 * np.sign(r)), (cr - 0.7, 0.75 * np.sign(r)), color=C2, lw=2.5, ms=20)
        if ct < 9.6: arrow(ax, (ct - 0.3, 1.25), (ct + 0.7, 1.25), color=C2, lw=2.5, ms=20)
    if s == 2:
        bullets(fig, ['Light → heavy: reflected pulse inverted', 'Transmitted pulse upright, slower, shorter',
                      'Both smaller: energy is shared'], 3, 0.06, 0.34, size=27)
    elif s == 3:
        bullets(fig, ['Heavy → light: reflected pulse upright', 'Transmitted pulse faster, longer'], 2, 0.06, 0.34,
                size=27)
    else:
        card(fig, 0.05, 0.07, 0.90, 0.29, 'Sketching tips',
             '→  arrows show which way each pulse moves\n→  a reflected pulse is never bigger than the original\n'
             '→  reflection flips a lopsided pulse front-to-back\n→  the slower pulse sits closer to the boundary',
             tcol=YELLOW, size=24)


def string_speed(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Wave speed on a stretched string')
    sheet_eq(fig, 0.06, 0.685, r'$v = \sqrt{\dfrac{T}{\mu}}$', size=46, color=GREEN)
    bullets(fig, ['T = tension (N)', 'μ = linear mass density (kg m⁻¹)\n= mass ÷ length',
                  'tighter → faster;  heavier → slower'], 3, 0.06, 0.50, size=25, dim=False)
    if s >= 1:
        card(fig, 0.05, 0.06, 0.40, 0.19, 'Careful!', 'T here is tension, not period\nconvert g → kg before dividing',
             tcol=PINK, size=22)
    if s <= 1:
        ax = wax(fig, [0.50, 0.30, 0.46, 0.45], (0, 10), (-3, 3))
        xx = np.linspace(1, 9, 400)
        ax.plot(xx, 1.2 * np.sin(TAU * (xx - 1) / 4), color=C1, lw=3)
        for q in (1, 9): ax.add_patch(Circle((q, 0), 0.2, color=SOFT))
        arrow(ax, (1, 0), (-0.2, 0), color=C2, lw=4); arrow(ax, (9, 0), (10.2, 0), color=C2, lw=4)
        label(ax, 0.3, 0.5, 'T', size=30, color=C2, weight='bold'); label(ax, 9.7, 0.5, 'T', size=30, color=C2, weight='bold')
        label(ax, 5, -2.2, 'μ = m / l', size=28, color=SOFT)
        return
    if s in (2, 3):
        chip(fig, 'Element 2 · problems')
        card(fig, 0.50, 0.58, 0.45, 0.20, 'Example', 'l = 1.5 m,  m = 12 g,  T = 80 N.\nFind the wave speed.', tcol=C2, size=24)
        T(fig, 0.51, 0.52, r'$m = 12\ \mathrm{g} = 0.012\ \mathrm{kg}$', size=30)
        T(fig, 0.51, 0.43, r'$\mu = \dfrac{0.012}{1.5} = 0.008\ \mathrm{kg\ m^{-1}}$', size=30)
        if s >= 3:
            T(fig, 0.51, 0.31, r'$v = \sqrt{\dfrac{80}{0.008}} = \sqrt{10\,000}$', size=30)
            eq(fig, 0.51, 0.15, r'$v = 100\ \mathrm{m\ s^{-1}}$', size=36, color=GREEN)
        return
    # s == 4: sonometer / hanging mass
    ax = wax(fig, [0.50, 0.28, 0.46, 0.50], (0, 12), (-5, 2))
    ax.add_patch(Rectangle((0.3, -0.6), 10, 0.5, fc=PANEL2, ec=SOFT))
    ax.plot([1, 10.3], [0.4, 0.4], color=C1, lw=3)
    for q in (1.5, 8.5): ax.add_patch(Polygon([[q - 0.3, -0.1], [q + 0.3, -0.1], [q, 0.4]], color=SOFT))
    ax.add_patch(Circle((10.6, 0.1), 0.35, fc=PANEL2, ec=SOFT))
    ax.plot([10.95, 10.95], [0.1, -3.0], color=C1, lw=2)
    ax.add_patch(Rectangle((10.45, -4.0), 1.0, 1.0, fc=C2, ec=FG))
    label(ax, 10.95, -3.5, 'm', size=24, color=BG, weight='bold')
    darrow(ax, (1.5, 1.2), (8.5, 1.2), color=YELLOW, ms=14); label(ax, 5, 1.6, 'vibrating length l', size=20, color=YELLOW)
    label(ax, 5, -1.5, 'sonometer: tension from a hanging mass', size=20, color=SOFT)
    eq(fig, 0.52, 0.20, r'$T = mg$', size=40)
    T(fig, 0.70, 0.235, 'g = 9.8 m s⁻²\n→ more mass, higher pitch', size=22, color=SOFT)


def huygens(fig, s, ph):
    C1, C2 = C()
    header(fig, "Wavefronts and Huygens' principle")
    ax = wax(fig, [0.04, 0.12, 0.54, 0.68], (-1, 11), (-5, 5))
    if s == 0:
        for x0 in (1, 3, 5):
            ax.plot([x0, x0], [-4.5, 4.5], color=C1, lw=3)
        for yy in np.linspace(-4, 4, 9):
            ax.add_patch(Arc((5, yy), 2.4, 2.4, theta1=-90, theta2=90, color=C2, lw=1.5, alpha=0.8))
            ax.scatter([5], [yy], s=30, color=C2)
        ax.plot([6.2, 6.2], [-4.5, 4.5], color=C1, lw=3, ls='--')
        arrow(ax, (7.5, 0), (10, 0), color=YELLOW, lw=3); label(ax, 8.7, 0.6, 'ray', size=22, color=YELLOW)
        label(ax, 3, -4.9, 'wavefronts (crests), λ apart', size=19, color=C1)
    else:
        ax.add_patch(Rectangle((0, 0.6), 0.35, 4.4, color=SOFT)); ax.add_patch(Rectangle((0, -5), 0.35, 4.4, color=SOFT))
        ax.plot([-0.6, -0.6], [-4.5, 4.5], color=C1, lw=3)
        for r in (1.6, 3.4, 5.2, 7.0, 8.8):
            ax.add_patch(Arc((0.35, 0), 2 * r, 2 * r, theta1=-75, theta2=75, color=C1, lw=3))
        darrow(ax, (2.0, -4.2), (3.8, -4.2), color=C2, ms=12); label(ax, 2.9, -3.7, 'same λ', size=20, color=C2)
        label(ax, 1.5, 4.8, 'barrier with a small gap', size=18, color=SOFT, ha='left', zorder=10, bbox=dict(fc=BG, ec='none', pad=2))
    if s == 0:
        bullets(fig, ['Wavefront: line joining points in phase\n(e.g. along a crest)',
                      'Every point on a wavefront acts as a\nsource of circular wavelets',
                      'New wavefront = line touching all\nthe wavelets', 'Rays ⊥ wavefronts'], 4, 0.61, 0.77, size=24, dim=False)
    else:
        bullets(fig, ['Small gap or point source →\ncircular wavefronts', 'Same medium → same speed → same λ',
                      'Draw evenly spaced curves, centred\non the gap'], 3, 0.61, 0.77, size=24, dim=False)


def _ray_diagram(ax, top, bot, tint=True):
    ax.add_patch(Rectangle((-6, -6), 12, 6, fc='#1a3150' if tint else BG, ec='none', zorder=0))
    ax.axhline(0, color=SOFT, lw=2)
    ax.plot([0, 0], [-3.7, 3.7], color=MUT, lw=1.5, ls='--')
    label(ax, -4.6, 3.3, top, size=20, color=SOFT, ha='left')
    label(ax, -4.6, -3.3, bot, size=20, color=SOFT, ha='left')


def _angle_arc(ax, d0, ang, r, color, txt, txtr=None):
    a0, a1 = min(d0, d0 + ang), max(d0, d0 + ang)
    ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=a0, theta2=a1, color=color, lw=2))
    m = np.radians((a0 + a1) / 2); rr = txtr or r + 0.45
    label(ax, rr * np.cos(m), rr * np.sin(m), txt, size=22, color=color)


def refraction(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Reflection and refraction' if s else 'Reflection in two dimensions')
    ax = wax(fig, [0.03, 0.10, 0.52, 0.72], (-5, 5), (-3.9, 3.9))
    if s == 0:
        _ray_diagram(ax, 'medium 1', 'surface')
        th = np.radians(40); Lr = 4
        arrow(ax, (-Lr * np.sin(th), Lr * np.cos(th)), (-0.05, 0.05), color=YELLOW, lw=3.5)
        arrow(ax, (0, 0), (Lr * np.sin(th), Lr * np.cos(th)), color=YELLOW, lw=3.5)
        _angle_arc(ax, 90, 40, 1.4, C2, 'θᵢ'); _angle_arc(ax, 90, -40, 1.4, C2, 'θᵣ')
        label(ax, 0.15, 3.55, 'normal', size=18, color=MUT, ha='left')
        bullets(fig, ['Rays: direction of travel, ⊥ to wavefronts', 'Angles measured from the normal'], 2, 0.58, 0.76,
                size=25, dim=False)
        sheet_eq(fig, 0.60, 0.48, r'$\theta_i = \theta_r$', size=48)
        return
    _ray_diagram(ax, 'medium 1: fast', 'medium 2: slow')
    th1 = np.radians(40); th2 = np.arcsin(0.6 * np.sin(th1)); l1, l2 = 1.1, 0.66
    for m in range(-12, 14):
        yy = np.linspace(0, 3.9, 50); ax.plot((l1 * (m + ph) + yy * np.cos(th1)) / np.sin(th1), yy, color=C1, lw=2, alpha=0.75)
        yy = np.linspace(-3.9, 0, 50); ax.plot((l2 * (m + ph) + yy * np.cos(th2)) / np.sin(th2), yy, color=GREEN, lw=2, alpha=0.75)
    Lr = 4.2
    arrow(ax, (-Lr * np.sin(th1), Lr * np.cos(th1)), (0, 0), color=YELLOW, lw=4)
    arrow(ax, (0, 0), (Lr * np.sin(th2), -Lr * np.cos(th2)), color=YELLOW, lw=4)
    _angle_arc(ax, 90, 40, 1.3, C2, 'θᵢ'); _angle_arc(ax, -90, np.degrees(th2), 1.6, C2, 'θᵣ', txtr=2.0)
    if s == 1:
        bullets(fig, ['Speed changes → direction changes', 'f stays the same, so λ ∝ v',
                      'Slower → bends towards the normal', 'Faster → bends away from the normal'], 4, 0.58, 0.76,
                size=25, dim=False)
    if s >= 2:
        learn_eq(fig, 0.60, 0.72, r'$n = \dfrac{c}{v}$', size=40)
        for i, (m_, nv) in enumerate([('air', '1.00'), ('water', '1.33'), ('glass', '≈ 1.5')]):
            T(fig, 0.82, 0.77 - i * 0.055, m_, size=24, color=SOFT); T(fig, 0.955, 0.77 - i * 0.055, nv, size=24, ha='right')
        T(fig, 0.60, 0.585, 'absolute n: compared with a vacuum\nhigher n → slower light', size=20, color=SOFT)
    if s >= 3:
        sheet_eq(fig, 0.60, 0.46, r'$n_i\sin\theta_i = n_r\sin\theta_r$', size=30, color=GREEN)
        sheet_eq(fig, 0.60, 0.31, r'$\dfrac{\sin\theta_i}{\sin\theta_r} = \dfrac{v_i}{v_r} = n$', size=28)
        learn_eq(fig, 0.60, 0.155, r'relative $n = \dfrac{n_r}{n_i} = \dfrac{\lambda_i}{\lambda_r}$', size=26)


def _tir_draw(ax, thd, n1=1.5, show_vals=True, C2=None):
    _ray_diagram(ax, 'air  (n = 1.00)', 'glass  (n = 1.50)')
    th = np.radians(thd); Lr = 4.2
    sint = n1 * np.sin(th)
    arrow(ax, (-Lr * np.sin(th), -Lr * np.cos(th)), (0, 0), color=YELLOW, lw=4)
    thc = np.degrees(np.arcsin(1 / n1))
    if sint < 1:
        t2 = np.arcsin(sint); a = 0.25 + 0.75 * (thd / thc) ** 6
        arrow(ax, (0, 0), (Lr * np.sin(t2), Lr * np.cos(t2)), color=YELLOW, lw=4 * (1 - 0.7 * a))
        ax.add_patch(FancyArrowPatch((0, 0), (Lr * np.sin(th), -Lr * np.cos(th)), arrowstyle='-|>', mutation_scale=24,
                                     color=C2, lw=4, alpha=min(1, a)))
        _angle_arc(ax, 90, -np.degrees(t2), 1.5, L.A1(), 'θᵣ', txtr=2.0)
    else:
        arrow(ax, (0, 0), (Lr * np.sin(th), -Lr * np.cos(th)), color=C2, lw=4)
    _angle_arc(ax, -90, -thd, 1.3, C2, 'θᵢ', txtr=1.8)
    if show_vals:
        st = 'refraction + weak reflection' if sint < 1 else 'TOTAL INTERNAL REFLECTION'
        label(ax, 4.8, 3.3, f'θᵢ = {thd:4.1f}°', size=24, color=FG, ha='right')
        label(ax, 4.8, -3.3, st, size=21, color=C2 if sint >= 1 else SOFT, ha='right', weight='bold')


def tir(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Critical angle and total internal reflection')
    ax = wax(fig, [0.03, 0.10, 0.52, 0.72], (-5, 5), (-3.9, 3.9))
    thc = np.degrees(np.arcsin(1 / 1.5))
    if s == 0:
        _tir_draw(ax, 37.5 - 17.5 * np.cos(TAU * ph), C2=C2)
        bullets(fig, ['Slower → faster medium:\nbends away from normal', 'Increase θᵢ → refracted ray\nnears the surface'],
                2, 0.58, 0.76, size=25, dim=False)
    elif s == 1:
        _tir_draw(ax, thc, show_vals=False, C2=C2)
        label(ax, 4.8, 3.3, f'θᵢ = θc = {thc:.1f}°', size=24, color=FG, ha='right')
        learn_eq(fig, 0.60, 0.68, r'$\sin\theta_c = \dfrac{n_r}{n_i}$', size=46, color=GREEN)
        T(fig, 0.60, 0.53, 'from Snell’s law with θᵣ = 90°\nglass → air: θc = 41.8°', size=24, color=SOFT)
    else:
        _tir_draw(ax, 55, C2=C2)
        bullets(fig, ['θᵢ > θc → all light reflects', 'Only from higher n to lower n', 'Optical fibres trap light this way'],
                3, 0.58, 0.76, size=25, dim=False)
        a2 = wax(fig, [0.58, 0.30, 0.38, 0.22], (0, 10), (-1.5, 1.5))
        a2.add_patch(Rectangle((0, -1), 10, 2, fc='#1a3150', ec=SOFT, lw=2))
        a2.plot([0, 1.2, 3.6, 6.0, 8.4, 9.6], [0, 1, -1, 1, -1, -0.33], color=YELLOW, lw=3)
        if s == 3:
            card(fig, 0.58, 0.07, 0.38, 0.19, 'Exam tip: name it', '“θᵢ exceeds θc, so total\ninternal reflection occurs”',
                 tcol=PINK, size=22)


def we_refraction(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: glass to water')
    chip(fig, 'Element 2 · problems')
    card(fig, 0.05, 0.60, 0.48, 0.20, 'Question', 'Light in glass (n = 1.52) meets water (n = 1.33)\nat θᵢ = 55°. Does it escape into the water?',
         tcol=C2, size=22)
    ax = wax(fig, [0.56, 0.12, 0.40, 0.68], (-5, 5), (-4.5, 4.5))
    _ray_diagram(ax, 'water  n = 1.33', 'glass  n = 1.52')
    Lr = 4.0; th = np.radians(55)
    arrow(ax, (-Lr * np.sin(th), -Lr * np.cos(th)), (0, 0), color=YELLOW, lw=4)
    _angle_arc(ax, -90, -55, 1.3, C2, '55°', txtr=1.9)
    if s >= 2:
        t2 = np.radians(69.4)
        arrow(ax, (0, 0), (Lr * np.sin(t2), Lr * np.cos(t2)), color=YELLOW, lw=4)
        _angle_arc(ax, 90, -69.4, 1.5, C1, '69.4°', txtr=2.2)
    if s >= 3:
        t3 = np.radians(65)
        ax.plot([-Lr * np.sin(t3), 0], [-Lr * np.cos(t3), 0], color=PINK, lw=3, ls='--')
        ax.add_patch(FancyArrowPatch((0, 0), (Lr * np.sin(t3), -Lr * np.cos(t3)), arrowstyle='-|>', mutation_scale=22,
                                     color=PINK, lw=3, ls='--'))
        label(ax, 3.2, -3.9, '65°: TIR', size=20, color=PINK)
    y = 0.53
    if s >= 1:
        T(fig, 0.06, y, r'$\sin\theta_c = \dfrac{1.33}{1.52} = 0.875\ \ \Rightarrow\ \ \theta_c = 61.0^\circ$', size=27); y -= 0.11
    if s >= 2:
        T(fig, 0.06, y, '55° < 61.0°, so it refracts:', size=24, color=SOFT); y -= 0.06
        T(fig, 0.06, y, r'$\sin\theta_r = \dfrac{1.52\,\sin 55^\circ}{1.33} = 0.936\ \ \Rightarrow\ \ \theta_r = 69.4^\circ$',
          size=27, color=GREEN); y -= 0.12
    if s >= 3:
        bullets(fig, ['65° > 61.0° → total internal reflection', 'Check: speeding up → θᵣ > θᵢ ✓',
                      'sin θᵣ > 1 on a calculator ⇒ TIR'], 3, 0.06, y, size=23, gap=0.01, dim=False, mcol=PINK)


def two_surfaces(fig, s, ph):
    """Refraction then a second surface at right angles (geometry 90° - θ)."""
    C1, C2 = C()
    header(fig, 'Two surfaces: use the geometry')
    ax = wax(fig, [0.04, 0.10, 0.50, 0.72], (-1, 9), (-7.5, 3))
    ax.add_patch(Rectangle((0, -7), 7, 7, fc='#1a3150', ec=SOFT, lw=2))
    label(ax, 0.3, -0.6, 'glass n = 1.50', size=18, color=SOFT, ha='left')
    th1 = np.radians(40); th2 = np.arcsin(np.sin(th1) / 1.5)
    P = np.array([4.5, 0.0]); d = np.array([np.sin(th2), -np.cos(th2)])
    tq = (7 - P[0]) / d[0]; Q = P + tq * d
    ax.plot([P[0] - 2.6 * np.sin(th1), P[0]], [2.6 * np.cos(th1), 0], color=YELLOW, lw=4)
    ax.plot([P[0], Q[0]], [P[1], Q[1]], color=YELLOW, lw=4)
    ax.plot([P[0], P[0]], [-2.2, 2.6], color=MUT, ls='--', lw=1.5)
    ax.add_patch(Arc(P, 2.2, 2.2, theta1=90, theta2=130, color=C2, lw=2)); label(ax, P[0] - 0.6, 1.6, '40°', size=19, color=C2)
    ax.add_patch(Arc(P, 2.6, 2.6, theta1=270, theta2=270 + np.degrees(th2), color=C1, lw=2))
    label(ax, P[0] + 0.45, -1.75, f'{np.degrees(th2):.1f}°', size=19, color=C1)
    if s >= 1:
        ax.plot([5.2, 8.6], [Q[1], Q[1]], color=MUT, ls='--', lw=1.5)
        a_in = 90 - np.degrees(th2)
        ax.add_patch(Arc(Q, 2.4, 2.4, theta1=90 + np.degrees(th2), theta2=180, color=PINK, lw=2))
        label(ax, Q[0] - 1.7, Q[1] + 0.6, f'{a_in:.1f}°', size=19, color=PINK)
    if s >= 2:
        r = d * np.array([-1, 1])
        ax.plot([Q[0], Q[0] + 1.8 * r[0]], [Q[1], Q[1] + 1.8 * r[1]], color=YELLOW, lw=4)
        label(ax, 3.2, -6.4, 'TIR at the side face', size=20, color=PINK)
    chip(fig, 'Element 2 · problems')
    y = 0.76
    lines = [(r'top face: $\sin\theta_r = \dfrac{\sin 40^\circ}{1.50} \Rightarrow \theta_r = 25.4^\circ$', FG),
             (r'faces at 90°: new $\theta_i = 90^\circ - 25.4^\circ = 64.6^\circ$', PINK),
             (r'$\theta_c = 41.8^\circ$ and $64.6^\circ > \theta_c$ → TIR', GREEN)]
    for k in range(min(s + 1, 3)):
        T(fig, 0.58, y, lines[k][0], size=25, color=lines[k][1]); y -= 0.12
    if s >= 2:
        bullets(fig, ['Draw the normal at EVERY surface', 'Use angle sums in the triangle', 'Then apply Snell / θc again'],
                3, 0.58, 0.40, size=23, dim=False, mcol=YELLOW)


def _refr(d, N, n1, n2):
    ci = -np.dot(N, d); eta = n1 / n2; k = 1 - eta ** 2 * (1 - ci ** 2)
    return eta * d + (eta * ci - np.sqrt(k)) * N


def dispersion(fig, s, ph):
    header(fig, 'Dispersion')
    ax = wax(fig, [0.03, 0.12, 0.60, 0.70], (-3.2, 3.6), (-0.9, 2.6))
    P1, P2, P3 = np.array([-1.0, 0]), np.array([1.0, 0]), np.array([0, np.sqrt(3)])
    ax.add_patch(Polygon([P1, P2, P3], fc='#1a3150', ec=SOFT, lw=2, alpha=0.95))
    hit = P1 + 0.45 * (P3 - P1)
    d0 = np.array([np.cos(np.radians(18)), np.sin(np.radians(18))])
    ax.plot([hit[0] - 3 * d0[0], hit[0]], [hit[1] - 3 * d0[1], hit[1]], color='white', lw=4)
    Nl = np.array([-np.sqrt(3) / 2, 0.5]); Nr = np.array([np.sqrt(3) / 2, 0.5])
    for c, n in [('#ff3b3b', 1.50), ('#ff9a2e', 1.512), ('#ffe23b', 1.524), ('#4bd66a', 1.536), ('#3b8bff', 1.548),
                 ('#9b5bff', 1.56)]:
        t = _refr(d0, Nl, 1.0, n)
        lam_, _ = np.linalg.solve(np.array([t, -(P2 - P3)]).T, P3 - hit)
        q = hit + lam_ * t
        ax.plot([hit[0], q[0]], [hit[1], q[1]], color=c, lw=2, alpha=0.8)
        o = _refr(t, -Nr, n, 1.0)
        ax.plot([q[0], q[0] + 3 * o[0]], [q[1], q[1] + 3 * o[1]], color=c, lw=3.5)
    label(ax, -2.6, 0.85, 'white light', size=20, color=FG)
    label(ax, 0, -0.45, 'spread exaggerated for clarity', size=17, color=MUT)
    bullets(fig, ['n is slightly higher for blue\nthan for red', 'Blue bends more → colours spread\ninto a spectrum',
                  'Each colour has its own critical angle:\none colour can escape while another\nis totally internally reflected'],
            3, 0.64, 0.74, size=24, dim=False)


def seismic(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Seismic waves: refraction inside the Earth')
    ax = wax(fig, [0.04, 0.07, 0.46, 0.74], (-1.18, 1.18), (-1.08, 1.08))
    ax.add_patch(Circle((0, 0), 1.0, fc='#3a2a4a', ec=SOFT, lw=2))
    ax.add_patch(Circle((0, 0), 0.55, fc='#7a4a1e', ec=C2, lw=2))
    ax.add_patch(Circle((0, 0), 0.20, fc='#b8862f', ec=YELLOW, lw=1.5))
    label(ax, 0, -0.78, 'mantle', size=18, color=SOFT); label(ax, 0, -0.38, 'liquid outer core', size=18)
    label(ax, 0, 0, 'inner\ncore', size=15, color=BG)
    ax.scatter([0], [1.0], marker='*', s=900, color=YELLOW, zorder=6, edgecolor=BG)
    if s >= 1:
        for D in [25, 50, 75, 100]:
            for sg in (1, -1):
                d = np.radians(D); A = np.array([0, 1.0]); B = np.array([sg * np.sin(d), np.cos(d)])
                M = (A + B) / 2; u = M / np.linalg.norm(M); Cc = 2 * (np.cos(d / 2) - 0.07) * u - M
                tt = np.linspace(0, 1, 80)[:, None]
                Pp = (1 - tt) ** 2 * A + 2 * tt * (1 - tt) * Cc + tt ** 2 * B
                ax.plot(Pp[:, 0], Pp[:, 1], color=PINK, lw=2.5, alpha=0.9)
    if s >= 2:
        for sg in (1, -1):
            a = np.radians(np.linspace(104, 180, 60)); ax.plot(sg * 1.04 * np.sin(a), 1.04 * np.cos(a), color=PINK, lw=6, alpha=0.5)
        label(ax, 0, -1.03, 'S-wave shadow zone', size=18, color=PINK, va='top')
    it = ['P-waves: longitudinal', 'S-waves: transverse', 'Speed increases with depth in the mantle']
    if s >= 1: it += ['Gradual speed change → gradual refraction', 'Bends away from normal → paths curve back up']
    if s >= 2: it += ['Liquid core: no restoring force for\nsideways (shear) motion → no S-waves']
    bullets(fig, it, len(it), 0.54, 0.78, size=23, gap=0.014)
    if s >= 3:
        card(fig, 0.54, 0.06, 0.42, 0.18, 'Exam tip', 'use wave speed, not refractive index\ndenser ≠ slower for seismic waves',
             tcol=YELLOW, size=21)


def quakes(fig, s, ph):
    """Earthquakes & tsunamis in the real world (course context)."""
    C1, C2 = C()
    header(fig, 'Monitoring earthquakes and tsunamis')
    if s <= 1:
        ax = gax(fig, [0.06, 0.40, 0.50, 0.36], (0, 60), (-1.6, 1.6), 'time after the earthquake (s)', 'seismometer', ticks=False)
        ax.set_xticks([0, 20, 26, 46, 60])
        t = np.linspace(0, 60, 3000)
        y = np.where(t > 26, 0.5 * np.sin(TAU * 1.5 * t) * np.exp(-(t - 26) / 12), 0)
        y += np.where((t > 46), 1.2 * np.sin(TAU * 0.8 * t) * np.exp(-(t - 46) / 10), 0)
        ax.plot(t, y, color=C1, lw=1.5)
        label(ax, 26, 1.35, 'P arrives', size=18, color=C1); label(ax, 46, 1.35, 'S arrives', size=18, color=PINK)
        darrow(ax, (26, -1.35), (46, -1.35), color=YELLOW, ms=14); label(ax, 36, -1.05, 'Δt = 20 s', size=18, color=YELLOW)
        chip(fig, 'Element 2 · problems', color=C2)
        bullets(fig, ['P-waves are faster → arrive first', 'The S–P delay grows with distance',
                      'Three stations → locate the epicentre'], 3, 0.60, 0.76, size=24, dim=False)
        if s == 1:
            T(fig, 0.06, 0.31, r'$\dfrac{d}{v_S} - \dfrac{d}{v_P} = \Delta t$', size=30)
            T(fig, 0.06, 0.20, r'$d = \dfrac{20}{1/4.5 - 1/8.0} \approx 206\ \mathrm{km}$', size=30, color=GREEN)
            T(fig, 0.34, 0.29, 'vP = 8.0 km s⁻¹\nvS = 4.5 km s⁻¹', size=22, color=SOFT)
        return
    ax = wax(fig, [0.04, 0.30, 0.92, 0.48], (0, 20), (-4, 2.5))
    xs = np.linspace(0, 20, 800)
    depth = np.where(xs < 11, -3.8, -3.8 + (xs - 11) * 0.42)
    ax.fill_between(xs, depth, -4, color='#3a2a1a'); ax.fill_between(xs, depth, 0, color='#123a63', alpha=0.6)
    amp = 0.12 * (3.8 / np.maximum(-depth, 0.25)) ** 0.5
    k = np.where(xs < 11, TAU / 6, TAU / 6 * (3.8 / np.maximum(-depth, 0.3)) ** 0.5)
    phase = np.cumsum(k) * (xs[1] - xs[0])
    ax.plot(xs, amp * np.sin(phase - TAU * ph), color=C1, lw=3)
    arrow(ax, (2, 1.6), (6, 1.6), color=C2); label(ax, 4, 2.1, 'towards shore', size=20, color=C2)
    label(ax, 4, -2.6, 'deep ocean: fast, long λ, small amplitude', size=20, color=SOFT)
    label(ax, 15.5, -0.9, 'shallow: slower, shorter λ, taller', size=20, color=YELLOW)
    bullets(fig, ['Frequency stays the same (set by the source)', 'Shallower → slower → λ shortens (v = λf)',
                  'Energy bunches up → amplitude grows'], 3, 0.06, 0.25, size=24, dim=False)


# ============================================================================ part 3
def superposition(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The principle of superposition')
    x = np.linspace(0, 10, 800)
    g = lambda u: np.exp(-u ** 2 / 0.45)
    c1 = 1 + 8 * ph; c2 = 9 - 8 * ph
    if s <= 1:
        rows = [(1, 'crest meets crest: constructive', [0.05, 0.54, 0.56, 0.26])]
        if s == 1: rows.append((-1, 'crest meets trough: destructive', [0.05, 0.16, 0.56, 0.26]))
        for sg, tt, rect in rows:
            ax = wax(fig, rect, (0, 10), (-1.3, 2.3))
            y1 = g(x - c1); y2 = sg * g(x - c2)
            ax.axhline(0, color=GRID, lw=1.2, ls='--')
            ax.plot(x, y1, color=C1, lw=2, ls='--'); ax.plot(x, y2, color=C2, lw=2, ls='--')
            ax.plot(x, y1 + y2, color=FG, lw=4)
            label(ax, 0, 2.15, tt, size=21, color=SOFT, ha='left')
        it = ['Waves pass through each other', 'Total displacement = sum of the\nindividual displacements']
        if s == 1: it += ['Crest + crest → constructive', 'Crest + equal trough → destructive', 'Afterwards: pulses unchanged']
        bullets(fig, it, len(it), 0.64, 0.78, size=24)
        eq(fig, 0.66, 0.16, r'$y = y_1 + y_2$', size=40)
        return
    ax = wax(fig, [0.05, 0.16, 0.56, 0.62], (0, 10), (-1.4, 2.0))
    y1 = 1.2 * g((x - 4.2) / 1.1); y2 = -0.8 * g((x - 5.6) / 0.9)
    ax.axhline(0, color=GRID, lw=1.2)
    ax.plot(x, y1, color=C1, lw=2.5, ls='--'); ax.plot(x, y2, color=C2, lw=2.5, ls='--'); ax.plot(x, y1 + y2, color=FG, lw=4)
    for xi in np.arange(3.0, 7.6, 0.5):
        a = 1.2 * g((xi - 4.2) / 1.1); b = -0.8 * g((xi - 5.6) / 0.9)
        ax.plot([xi, xi], [0, a], color=C1, lw=3, alpha=0.7); ax.plot([xi + 0.06, xi + 0.06], [0, b], color=C2, lw=3, alpha=0.7)
        ax.scatter([xi], [a + b], s=70, color=YELLOW, zorder=5)
    bullets(fig, ['1. Pick key points', '2. Add heights with signs\n(+ above, − below)', '3. Join with a smooth curve',
                  '4. Label clearly; don’t let\nlabelled regions overlap'], 4, 0.64, 0.74, size=25, mark='', dim=False)


def beats(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Beats')
    if s <= 2:
        t = np.linspace(0, 1, 3000)
        y1 = np.sin(TAU * 20 * t); y2 = np.sin(TAU * 24 * t)
        for i, (y, c, lab) in enumerate([(y1, C1, 'f₁'), (y2, C2, 'f₂')]):
            ax = wax(fig, [0.05, 0.66 - i * 0.13, 0.56, 0.11], (0, 1), (-1.2, 1.2))
            ax.plot(t, y, color=c, lw=2); label(ax, -0.02, 0, lab, size=24, color=c, ha='right')
        ax = wax(fig, [0.05, 0.14, 0.56, 0.34], (0, 1), (-2.6, 2.9))
        ax.plot(t, y1 + y2, color=FG, lw=2); label(ax, -0.02, 0, 'sum', size=22, ha='right')
        if s >= 1:
            env = 2 * np.abs(np.cos(np.pi * 4 * t))
            ax.plot(t, env, color=YELLOW, lw=2, ls='--'); ax.plot(t, -env, color=YELLOW, lw=2, ls='--')
            darrow(ax, (0.25, 2.5), (0.5, 2.5), color=PINK, ms=16); label(ax, 0.375, 2.85, '1 beat', size=20, color=PINK)
        it = ['Slightly different frequencies overlap', 'In step → loud; out of step → quiet']
        if s >= 1: it += ['1 beat = one cycle of the envelope\n(max to max)']
        bullets(fig, it, len(it), 0.64, 0.78, size=24)
        if s >= 2:
            learn_eq(fig, 0.66, 0.32, r'$f_{beat} = |\,f_1 - f_2\,|$', size=36, color=GREEN)
            T(fig, 0.66, 0.19, r'pitch heard $= \dfrac{f_1 + f_2}{2}$', size=26, color=SOFT)
        return
    t = np.linspace(0, 1000, 4000)
    ax = gax(fig, [0.07, 0.20, 0.53, 0.50], (0, 1000), (-2.6, 3.1), 'time (ms)', 'displacement', ticks=False)
    ax.set_xticks([0, 250, 500, 750, 1000])
    ax.plot(t, np.sin(TAU * 0.040 * t) + np.sin(TAU * 0.044 * t), color=FG, lw=1.6)
    darrow(ax, (0, 2.6), (1000, 2.6), color=PINK, ms=16); label(ax, 500, 2.85, '4 beats in 1000 ms', size=20, color=PINK)
    label(ax, 990, -2.4, 'carrier not to scale', size=14, color=MUT, ha='right')
    chip(fig, 'Element 3 · data' if s == 3 else 'Element 4 · predictions')
    card(fig, 0.63, 0.58, 0.33, 0.22, 'Example', '440 Hz fork + unknown note.\nFind the unknown frequency.', tcol=C2, size=22)
    T(fig, 0.64, 0.52, r'$f_{beat} = \dfrac{4}{1.00\ \mathrm{s}} = 4\ \mathrm{Hz}$', size=28, color=GREEN)
    if s >= 4:
        T(fig, 0.64, 0.41, 'f = 440 ± 4 → 444 Hz or 436 Hz', size=24)
        bullets(fig, ['Blu-Tack on unknown fork → its f drops', 'Beats get faster → further from 440', '∴ f = 436 Hz'],
                3, 0.64, 0.33, size=21, gap=0.01, dim=False, mcol=YELLOW)


def standing(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Standing waves')
    x = np.linspace(0, 12, 800); k = TAU / 4; w = TAU * ph
    a1 = wax(fig, [0.04, 0.58, 0.58, 0.22], (0, 12), (-1.3, 1.3))
    a1.axhline(0, color=GRID, lw=1, ls='--')
    a1.plot(x, np.sin(k * x - w), color=C1, lw=2.5); a1.plot(x, np.sin(k * x + w), color=C2, lw=2.5)
    arrow(a1, (9.5, 1.15), (11.5, 1.15), color=C1, lw=2, ms=16); arrow(a1, (2.5, 1.15), (0.5, 1.15), color=C2, lw=2, ms=16)
    a2 = wax(fig, [0.04, 0.12, 0.58, 0.40], (0, 12), (-2.9, 2.6))
    a2.axhline(0, color=GRID, lw=1, ls='--')
    a2.plot(x, 2 * np.sin(k * x), color=MUT, lw=1.2, ls=':'); a2.plot(x, -2 * np.sin(k * x), color=MUT, lw=1.2, ls=':')
    a2.plot(x, np.sin(k * x - w) + np.sin(k * x + w), color=FG, lw=4)
    for xn in range(0, 13, 2):
        a2.scatter([xn], [0], s=90, color=PINK, zorder=5); label(a2, xn, -0.5, 'N', size=18, color=PINK)
    for xa in range(1, 12, 2): label(a2, xa, 2.35, 'A', size=18, color=YELLOW)
    if s >= 1:
        darrow(a2, (2, -1.6), (4, -1.6), color=GREEN, ms=14); label(a2, 3, -2.1, 'λ/2', size=20, color=GREEN)
        darrow(a2, (6, -1.6), (7, -1.6), color=GREEN, ms=14); label(a2, 6.5, -2.1, 'λ/4', size=20, color=GREEN)
    if s == 0:
        bullets(fig, ['Two identical waves,\nopposite directions', 'Usually a wave + its reflection', 'The pattern does not travel',
                      'Nodes (N): never move', 'Antinodes (A): biggest oscillation'], 5, 0.65, 0.78, size=23, dim=False)
    elif s == 1:
        bullets(fig, ['N to N = λ/2', 'N to A = λ/4', 'Between nodes: all in phase', 'Across a node: phase flips'], 4, 0.65,
                0.78, size=24, dim=False)
    else:
        card(fig, 0.65, 0.22, 0.31, 0.56, 'Explain it with:',
             '✓ reflection at the ends\n\n✓ superposition of\n   incident + reflected\n\n✓ constructive → antinodes\n'
             '   destructive → nodes\n\n✓ resonance at particular\n   frequencies', tcol=YELLOW, size=22)


def _string(ax, n, ph, Lx=10, A=0.8, col=None):
    x = np.linspace(0, Lx, 400)
    ax.plot(x, A * np.sin(n * np.pi * x / Lx), color=MUT, lw=1, ls=':'); ax.plot(x, -A * np.sin(n * np.pi * x / Lx), color=MUT, lw=1, ls=':')
    ax.plot(x, A * np.sin(n * np.pi * x / Lx) * np.cos(TAU * n * ph), color=col or L.A1(), lw=3.5)
    for q in (0, Lx): ax.add_patch(Rectangle((q - 0.12, -1), 0.24, 2, color=SOFT))


def strings(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Standing waves on strings')
    if s == 0:
        ax = wax(fig, [0.05, 0.36, 0.56, 0.36], (-0.5, 10.5), (-1.6, 1.4))
        _string(ax, 1, ph, A=1.0)
        darrow(ax, (0, -1.35), (10, -1.35), color=C2, ms=16); label(ax, 5, -1.15, 'l', size=24, color=C2)
        label(ax, 5, 1.25, 'one loop = λ/2', size=24, color=YELLOW)
        bullets(fig, ['Fixed ends → nodes', 'Fundamental (1st harmonic): one loop'], 2, 0.64, 0.76, size=25, dim=False)
        sheet_eq(fig, 0.66, 0.52, r'$\lambda = 2l$', size=46, color=GREEN)
        T(fig, 0.66, 0.38, 'not l !', size=28, color=PINK, weight='bold')
        return
    for n in range(1, 5):
        ax = wax(fig, [0.05, 0.70 - (n - 1) * 0.165, 0.46, 0.13], (-0.5, 10.5), (-1.1, 1.1))
        _string(ax, n, ph, A=0.85, col=[C1, GREEN, C2, PINK][n - 1])
        fig.text(0.53, 0.765 - (n - 1) * 0.165, f'n = {n}', color=FG, fontsize=22, va='center')
    if s == 1:
        learn_eq(fig, 0.64, 0.68, r'$\lambda_n = \dfrac{2l}{n}$', size=38, color=GREEN)
        learn_eq(fig, 0.64, 0.46, r'$f_n = \dfrac{n\,v}{2l} = n f_1$', size=38, color=GREEN)
        T(fig, 0.64, 0.31, 'whole-number multiples\nof the fundamental', size=24, color=SOFT)
    else:
        rows = [('f₁', '1st harmonic', 'fundamental'), ('2f₁', '2nd harmonic', '1st overtone'),
                ('3f₁', '3rd harmonic', '2nd overtone'), ('4f₁', '4th harmonic', '3rd overtone')]
        for i, r in enumerate(rows):
            y = 0.765 - i * 0.165
            box(fig, 0.63, y - 0.05, 0.33, 0.10, fc=PANEL if i % 2 == 0 else PANEL2)
            T(fig, 0.64, y, r[0], size=24, color=YELLOW, va='center'); T(fig, 0.69, y, r[1], size=22, va='center')
            T(fig, 0.83, y, r[2], size=22, va='center', color=C2)


def we_string(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a guitar string')
    chip(fig, 'Elements 2 & 4')
    card(fig, 0.05, 0.56, 0.42, 0.24, 'Question', 'l = 65 cm,  f₁ = 196 Hz,\nμ = 1.2 g m⁻¹.\nFind v and the tension T.', tcol=C2, size=24)
    if s >= 3:
        card(fig, 0.05, 0.20, 0.42, 0.30, 'Prediction', 'Tension increases by 4%.\nNew frequency? Beats with\na 196 Hz tuning fork?',
             tcol=PINK, size=24)
    y = 0.78
    if s >= 1:
        T(fig, 0.52, y, r'$\lambda_1 = 2l = 2\times0.65 = 1.30\ \mathrm{m}$', size=28); y -= 0.09
        T(fig, 0.52, y, r'$v = \lambda f = 196\times1.30 \approx 255\ \mathrm{m\ s^{-1}}$', size=28, color=GREEN); y -= 0.11
    if s >= 2:
        T(fig, 0.52, y, r'$T = \mu v^2 = 0.0012\times255^2 \approx 78\ \mathrm{N}$', size=28, color=GREEN); y -= 0.12
    if s >= 3:
        T(fig, 0.52, y, r'$f \propto v \propto \sqrt{T}$', size=28); y -= 0.09
        T(fig, 0.52, y, r'$f_{new} = 196\times\sqrt{1.04} \approx 200\ \mathrm{Hz}$', size=28, color=GREEN); y -= 0.09
        T(fig, 0.52, y, r'$f_{beat} \approx 200 - 196 = 4\ \mathrm{Hz}$', size=28, color=GREEN); y -= 0.08
        T(fig, 0.52, y, 'ratio method: quicker, fewer rounding errors', size=21, color=SOFT)


def _pipe(ax, x0, y0, Lp, closed, n, col, ext=0.0, h=0.9):
    ax.plot([x0, x0 + Lp], [y0 + h / 2] * 2, color=SOFT, lw=3); ax.plot([x0, x0 + Lp], [y0 - h / 2] * 2, color=SOFT, lw=3)
    if closed: ax.plot([x0, x0], [y0 - h / 2, y0 + h / 2], color=SOFT, lw=7)
    if n == 0: return
    Le = Lp + ext * (1 if closed else 2)
    xs = np.linspace(0, Le, 300)
    a = np.sin(n * np.pi * xs / (2 * Le)) if closed else np.cos(n * np.pi * xs / Le)
    X = x0 + xs - (0 if closed else ext)
    ax.fill_between(X, y0 + a * h * 0.42, y0 - a * h * 0.42, color=col, alpha=0.3, lw=0)
    ax.plot(X, y0 + a * h * 0.42, color=col, lw=2.5); ax.plot(X, y0 - a * h * 0.42, color=col, lw=2.5)


def pipes(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Standing waves in pipes')
    if s == 0:
        ax = wax(fig, [0.05, 0.30, 0.90, 0.45], (0, 20), (-3, 3))
        _pipe(ax, 4, 0, 12, True, 1, C1, h=2.0)
        label(ax, 4, -1.6, 'N', size=30, color=PINK, weight='bold'); label(ax, 16.2, -1.6, 'A', size=30, color=YELLOW, weight='bold')
        label(ax, 3.6, 2.2, 'closed end: air can’t move\n→ displacement node', size=22, color=PINK, ha='left')
        label(ax, 16.4, 2.2, 'open end: air moves freely\n→ displacement antinode', size=22, color=YELLOW, ha='right')
        T(fig, 0.5, 0.22, 'shaded = how far the air oscillates (displacement)', size=22, color=SOFT, ha='center')
        return
    if s in (1, 2):
        cols_ = [(False, 'Open at both ends', 'all harmonics',
                  [(1, 'λ = 2l', 'f₁'), (2, 'λ = l', '2f₁'), (3, 'λ = 2l/3', '3f₁')], 0.05)]
        if s == 2: cols_.append((True, 'Closed at one end', 'odd harmonics only',
                                 [(1, 'λ = 4l', 'f₁'), (3, 'λ = 4l/3', '3f₁'), (5, 'λ = 4l/5', '5f₁')], 0.52))
        sheet_eq(fig, 0.26, 0.775, r'$\lambda = 2l$', size=22)
        if s == 2: sheet_eq(fig, 0.72, 0.775, r'$\lambda = 4l$', size=22)
        for closed, title, sub, rows, x0 in cols_:
            T(fig, x0, 0.79, title, size=28, color=C2 if closed else C1, weight='bold')
            T(fig, x0, 0.73, sub, size=21, color=SOFT)
            for i, (n, l1, l2) in enumerate(rows):
                ax = wax(fig, [x0, 0.52 - i * 0.17, 0.27, 0.15], (-0.3, 10.3), (-0.8, 0.8))
                _pipe(ax, 0, 0, 10, closed, n, C2 if closed else C1, h=1.1)
                T(fig, x0 + 0.29, 0.62 - i * 0.17, l1, size=22); T(fig, x0 + 0.29, 0.575 - i * 0.17, l2, size=22, color=YELLOW)
        return
    if s == 3:
        ax = wax(fig, [0.05, 0.40, 0.90, 0.38], (0, 24), (-2.2, 2.2))
        _pipe(ax, 1, 0, 9, True, 1, C2, ext=1.0, h=1.6); _pipe(ax, 13.5, 0, 9, False, 1, C1, ext=1.0, h=1.6)
        darrow(ax, (1, -1.3), (11, -1.3), color=YELLOW, ms=14); label(ax, 6, -1.75, 'l + e', size=22, color=YELLOW)
        darrow(ax, (12.5, -1.3), (23.5, -1.3), color=YELLOW, ms=14); label(ax, 18, -1.75, 'l + 2e', size=22, color=YELLOW)
        label(ax, 6, 1.6, 'closed pipe: one open end', size=20, color=SOFT); label(ax, 18, 1.6, 'open pipe: two open ends', size=20, color=SOFT)
        bullets(fig, ['End correction e: the antinode sits just outside each open end', 'Pipe acts slightly longer than it is',
                      'Sketch antinodes just outside the opening, not inside'], 3, 0.06, 0.33, size=24, dim=False)
        return
    if s == 4:
        chip(fig, 'Element 2 · problems')
        card(fig, 0.05, 0.58, 0.42, 0.22, 'Example', 'Pipe, l = 20 cm, closed at one end.\nFind f₁ and the first overtone.\n(Ignore end correction.)',
             tcol=C2, size=22)
        sheet_eq(fig, 0.06, 0.45, r'$v_{sound} = 344\ \mathrm{m\ s^{-1}}$ (air, 20 °C)', size=26)
        ax = wax(fig, [0.06, 0.12, 0.38, 0.22], (-0.5, 10.5), (-1, 1))
        _pipe(ax, 0, 0, 10, True, 1, C2, h=1.3)
        y = 0.78
        for st, c in [(r'$\lambda_1 = 4l = 4\times0.20 = 0.80\ \mathrm{m}$', FG),
                      (r'$f_1 = \dfrac{v}{\lambda_1} = \dfrac{344}{0.80} = 430\ \mathrm{Hz}$', GREEN),
                      (r'first overtone $= 3f_1 = 1290\ \mathrm{Hz}$', GREEN),
                      (r'open both ends: $\lambda_1 = 2l = 0.40\ \mathrm{m}$', FG), (r'$\Rightarrow f_1 = 860\ \mathrm{Hz}$ (doubles)', GREEN)]:
            T(fig, 0.52, y, st, size=27, color=c); y -= 0.12 if 'dfrac' in st else 0.09
        return
    # s == 5: real-world closed pipe (ear canal)
    chip(fig, 'Element 4 · predictions')
    ax = wax(fig, [0.05, 0.36, 0.45, 0.40], (0, 12), (-3, 3))
    _pipe(ax, 1, 0, 9, True, 1, C2, h=2.2)
    label(ax, 0.6, -1.8, 'eardrum\n(closed end)', size=19, color=SOFT, ha='left')
    label(ax, 10.3, -1.8, 'open end', size=19, color=SOFT, ha='left')
    darrow(ax, (1, 1.6), (10, 1.6), color=YELLOW, ms=14); label(ax, 5.5, 2.1, 'l ≈ 2.5 cm', size=22, color=YELLOW)
    bullets(fig, ['Ear canal ≈ pipe closed at one end', r'$\lambda_1 = 4l = 0.10\ \mathrm{m}$',
                  r'$f_1 = 344 / 0.10 \approx 3400\ \mathrm{Hz}$', 'Resonance → ears are extra sensitive\naround 3–4 kHz, and near 10 kHz (3f₁)',
                  'Shorter canal (children) → higher f₁'], 5, 0.55, 0.76, size=24, dim=False)


def resonance(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Resonance')
    ax = gax(fig, [0.07, 0.18, 0.50, 0.58], (0, 4), (0, 1.15), 'driving frequency', 'amplitude', ticks=False)
    f = np.linspace(0.01, 4, 1000)
    if s == 0:
        A = 1 / np.sqrt((1 - f ** 2) ** 2 + (0.12 * f) ** 2); A /= A.max()
        ax.plot(f, A, color=C1, lw=3.5); ax.axvline(1, color=YELLOW, lw=1.5, ls='--')
        ax.set_xticks([1]); ax.set_xticklabels(['natural frequency f₀'])
        bullets(fig, ['Driving f matches a natural f\n→ amplitude grows very large', 'Wine glass shattered by a voice',
                      'Guitar body amplifies the strings', 'Bridges & buildings:\nwind, earthquakes'], 4, 0.62, 0.76, size=24)
    else:
        A = sum(1 / np.sqrt((n ** 2 - f ** 2) ** 2 + (0.15 * f) ** 2) / n for n in (1, 2, 3)); A /= A.max()
        ax.plot(f, A, color=C1, lw=3.5); ax.set_xticks([1, 2, 3]); ax.set_xticklabels(['f₁', '2f₁', '3f₁'])
        bullets(fig, ['Natural frequencies of strings and pipes\n= their standing-wave frequencies',
                      'Standing wave builds up when the\ndriving f matches a harmonic'], 2, 0.62, 0.76, size=24, dim=False)


def noise(fig, s, ph):
    """Noise pollution and acoustic design (course context)."""
    C1, C2 = C()
    header(fig, 'Noise pollution and acoustic design')
    if s == 0:
        ax = wax(fig, [0.05, 0.22, 0.52, 0.56], (0, 10), (-3.0, 3.9))
        x = np.linspace(0, 10, 600)
        ax.plot(x, 0.75 * np.sin(TAU * x / 3) + 2.2, color=C1, lw=3); label(ax, 0, 3.5, 'noise', size=20, color=C1, ha='left')
        ax.plot(x, -0.75 * np.sin(TAU * x / 3), color=C2, lw=3); label(ax, 0, 1.15, 'anti-noise (inverted)', size=20, color=C2, ha='left')
        ax.plot(x, 0 * x - 2.2, color=FG, lw=4); label(ax, 0, -1.55, 'sum: near silence', size=20, color=FG, ha='left')
        bullets(fig, ['Noise-cancelling headphones', 'Microphone samples the noise', 'Speaker adds an inverted copy',
                      'Destructive superposition', 'Works best for steady,\nlow-frequency hum'], 5, 0.61, 0.77, size=24)
        return
    items = [('Absorb', 'soft, porous panels turn sound energy into heat → fewer reflections, less echo', C1),
             ('Block', 'heavy, sealed barriers reflect sound; low frequencies (long λ) diffract over walls', C2),
             ('Avoid resonance', 'soft mounts for machines; natural frequencies kept away from common sources',
              PINK),
             ('Shape the room', 'reflections from curved or angled surfaces direct sound where it is wanted', GREEN)]
    for i, (t, b, c) in enumerate(items):
        y = 0.72 - i * 0.15
        box(fig, 0.05, y - 0.06, 0.90, 0.13)
        T(fig, 0.07, y + 0.035, t, size=28, color=c, weight='bold')
        T(fig, 0.07, y - 0.005, b, size=21, color=SOFT)


# ============================================================================ part 4
_cache = {}


def _field(key, xs, ys, srcs, k):
    if key not in _cache:
        X, Y = np.meshgrid(xs, ys); U = np.zeros_like(X, dtype=complex)
        for sx, sy, a in srcs:
            r = np.hypot(X - sx, Y - sy) + 0.25; U += a * np.exp(1j * k * r) / np.sqrt(r)
        _cache[key] = U
    return _cache[key]


def two_source(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Two-source interference')
    if s <= 1:
        ax = fig.add_axes([0.03, 0.08, 0.55, 0.75]); ax.axis('off')
        xs = np.linspace(-6, 6, 560); ys = np.linspace(-0.6, 8.8, 440)
        U = _field('ts', xs, ys, [(-1.5, 0, 1), (1.5, 0, 1)], TAU)
        ax.imshow(np.real(U * np.exp(-1j * TAU * ph)), extent=(-6, 6, -0.6, 8.8), origin='lower', cmap=CM_WAVE, vmin=-1.6,
                  vmax=1.6, interpolation='bilinear', aspect='auto')
        ax.scatter([-1.5, 1.5], [0, 0], s=200, color=YELLOW, zorder=5, edgecolor=BG, lw=2)
        it = ['Two sources, overlapping waves', 'Maxima: strong motion', 'Minima (nodal lines): nearly still']
        if s >= 1: it += ['Coherent: same f and a\nconstant phase difference', 'Light: split one source,\ne.g. two narrow slits',
                          'A distant point source sends\ncoherent waves to two receivers']
        bullets(fig, it, len(it), 0.62, 0.78, size=23)
        return
    ax = wax(fig, [0.04, 0.12, 0.50, 0.68], (-1, 10), (-1.2, 7.5))
    S1, S2, P = (0, 3.6), (0, 1.0), (8.5, 5.5)
    names = ('S₁', 'S₂') if s < 4 else ('A', 'B')
    ax.plot([S1[0], P[0]], [S1[1], P[1]], color=C1, lw=3); ax.plot([S2[0], P[0]], [S2[1], P[1]], color=C2, lw=3)
    for q, nm in zip((S1, S2), names):
        ax.scatter(*q, s=260, color=YELLOW, zorder=5); label(ax, q[0] - 0.6, q[1], nm, size=26, color=YELLOW)
    ax.scatter(*P, s=200, color=FG, zorder=5); label(ax, P[0] + 0.5, P[1] + 0.4, 'P', size=26)
    if s < 4:
        label(ax, 4.0, 5.3, 'r₁', size=26, color=C1); label(ax, 4.6, 2.5, 'r₂', size=26, color=C2)
    else:
        label(ax, 3.8, 5.3, '5.00 m', size=24, color=C1); label(ax, 4.8, 2.4, '6.25 m', size=24, color=C2)
    eq(fig, 0.08, 0.17, 'path difference = r₂ − r₁', size=30, color=FG)
    if s == 2:
        bullets(fig, ['Just subtract the path lengths', 'No Pythagoras or trig needed\n(unless asked for an angle)'], 2, 0.60,
                0.76, size=25, dim=False)
    if s == 3:
        box(fig, 0.59, 0.53, 0.37, 0.23, fc=PANEL)
        T(fig, 0.61, 0.73, 'Constructive (maximum)', size=25, color=GREEN, weight='bold')
        T(fig, 0.61, 0.66, r'$\mathrm{PD} = n\lambda$', size=36); T(fig, 0.61, 0.585, 'waves arrive in phase', size=21, color=SOFT)
        box(fig, 0.59, 0.25, 0.37, 0.23, fc=PANEL)
        T(fig, 0.61, 0.45, 'Destructive (minimum)', size=25, color=PINK, weight='bold')
        T(fig, 0.61, 0.38, r'$\mathrm{PD} = (n-\frac{1}{2})\lambda$', size=36)
        T(fig, 0.61, 0.305, 'waves arrive completely out of phase', size=21, color=SOFT)
    if s == 4:
        chip(fig, 'Element 2 · problems')
        T(fig, 0.60, 0.78, 'Speakers in phase, f = 686 Hz', size=24, color=C2, weight='bold')
        y = 0.71
        for st, c in [(r'$\lambda = \dfrac{344}{686} = 0.50\ \mathrm{m}$', FG), (r'PD $= 6.25 - 5.00 = 1.25\ \mathrm{m}$', FG),
                      (r'$= 2.5\lambda\ \Rightarrow$ destructive: quiet', PINK), (r'PD $= 1.50\ \mathrm{m} = 3\lambda\ \Rightarrow$ loud', GREEN)]:
            T(fig, 0.60, y, st, size=27, color=c); y -= 0.12 if 'dfrac' in st else 0.085


def radar(fig, s, ph):
    """Direct + reflected radio wave: path difference and fluctuating signal."""
    C1, C2 = C()
    header(fig, 'Two paths: radio waves and a reflecting aircraft')
    ax = wax(fig, [0.04, 0.26, 0.52, 0.54], (-1, 13), (-1, 8))
    Tx, Rx = (0, 0), (12, 0)
    px = 3 + 6 * ph if s >= 2 else 6
    Pp = (px, 6)
    ax.plot([-1, 13], [-0.3, -0.3], color=MUT, lw=2)
    ax.plot([Tx[0], Rx[0]], [Tx[1], Rx[1]], color=C1, lw=3)
    ax.plot([Tx[0], Pp[0], Rx[0]], [Tx[1], Pp[1], Rx[1]], color=C2, lw=3)
    ax.add_patch(Polygon([[Pp[0] - 0.9, 6], [Pp[0] + 0.9, 6], [Pp[0] + 0.3, 6.4], [Pp[0] - 0.3, 6.4]], color=FG))
    label(ax, 0, 0.6, 'T', size=26, color=YELLOW); label(ax, 12, 0.6, 'R', size=26, color=YELLOW)
    label(ax, 6, -0.9, 'direct path TR', size=19, color=C1); label(ax, Pp[0], 7.2, 'aircraft', size=19)
    eq(fig, 0.06, 0.15, 'PD = TA + AR − TR', size=30, color=FG)
    label(ax, Pp[0] + 1.3, 6.2, 'A', size=26, color=YELLOW)
    if s == 0:
        bullets(fig, ['Metal reflects radio waves strongly\n(free electrons re-radiate)', 'Wood / plastic mostly let them through',
                      '→ a metal aircraft gives a strong\nreflected signal'], 3, 0.60, 0.76, size=24, dim=False)
    elif s == 1:
        bullets(fig, ['Receiver gets direct + reflected waves', 'Path difference: subtract lengths',
                      'λ = c / f  (EM wave: use 3.00 × 10⁸)'], 3, 0.60, 0.76, size=24, dim=False)
    else:
        bullets(fig, ['As the aircraft moves, PD changes', 'PD = nλ → strong signal', 'PD = (n − ½)λ → weak signal',
                      '→ the signal rises and falls'], 4, 0.60, 0.76, size=24, dim=False)
        a2 = wax(fig, [0.60, 0.12, 0.35, 0.18], (0, 1), (-1.2, 1.2))
        u = np.linspace(0, 1, 400); a2.plot(u, np.cos(TAU * 4 * u), color=GREEN, lw=2.5)
        a2.scatter([ph], [np.cos(TAU * 4 * ph)], s=80, color=YELLOW, zorder=5)
        label(a2, 0.5, 1.35, 'received signal strength', size=17, color=SOFT)


def youngs(fig, s, ph):
    C1, C2 = C()
    header(fig, "Young's double-slit experiment")
    ax = wax(fig, [0.03, 0.40, 0.94, 0.43], (0, 22), (-4.2, 4.2))
    ax.add_patch(Rectangle((0.3, -0.5), 1.8, 1.0, fc=PANEL2, ec=SOFT)); label(ax, 1.2, -0.9, 'laser', size=18, color=SOFT)
    ax.plot([2.1, 5], [0, 0], color=GREEN, lw=4)
    for y0, y1 in [(-4, -0.75), (-0.45, 0.45), (0.75, 4)]:
        ax.plot([5, 5], [y0, y1], color=SOFT, lw=6)
    ax.add_patch(Rectangle((17.5, -4), 0.35, 8, fc='#0a0f18', ec=SOFT))
    yy = np.linspace(-4, 4, 400); I = np.cos(np.pi * yy / 1.1) ** 2
    for yi, ii in zip(yy, I):
        ax.plot([17.5, 17.85], [yi, yi], color=GREEN, lw=1.6, alpha=ii * 0.95)
    ax.plot(18.1 + 1.4 * I, yy, color=GREEN, lw=2)
    for ys_ in (0.6, -0.6):
        ax.plot([5, 17.5], [ys_, 2.2], color=GREEN, lw=1, alpha=0.5)
    darrow(ax, (4.3, -0.6), (4.3, 0.6), color=YELLOW, ms=12); label(ax, 3.8, 0, 'd', size=24, color=YELLOW)
    darrow(ax, (5, -3.6), (17.5, -3.6), color=YELLOW, ms=14); label(ax, 11.2, -3.15, 'x', size=24, color=YELLOW)
    darrow(ax, (20.1, 0), (20.1, 1.1), color=YELLOW, ms=12); label(ax, 20.5, 0.55, 'w', size=24, color=YELLOW, ha='left')
    label(ax, 17.7, 4.15, 'screen', size=18, color=SOFT)
    if s >= 1:
        sheet_eq(fig, 0.05, 0.27, r'$w = \dfrac{\lambda x}{d}$', size=46, color=GREEN)
    if s == 1:
        bullets(fig, ['w = band width: node to node (fringe spacing)', 'x = slits to screen,  d = slit separation',
                      'λ ↑, x ↑ or d ↓  → wider fringes', 'evidence that light is a wave'], 4, 0.30, 0.35, size=22, gap=0.006, dim=False)
    if s == 2:
        chip(fig, 'Element 2 · problems')
        T(fig, 0.30, 0.33, 'λ = 532 nm,  d = 0.25 mm,  x = 2.0 m', size=23, color=C2)
        T(fig, 0.30, 0.26, r'$w = \dfrac{532\times10^{-9}\times2.0}{0.25\times10^{-3}} = 4.3\times10^{-3}\ \mathrm{m} = 4.3\ \mathrm{mm}$', size=26)
        T(fig, 0.30, 0.15, 'red laser (longer λ) → fringes further apart', size=22, color=SOFT)
    if s == 3:
        bullets(fig, ['Central bright fringe: PD = 0', 'nth bright fringe: PD = nλ, at n × w from the centre',
                      'Dark fringes halfway: PD = (n − ½)λ'], 3, 0.30, 0.35, size=23, gap=0.008, dim=False)
    if s == 4:
        box(fig, 0.30, 0.07, 0.55, 0.26, fc=PANEL2)
        T(fig, 0.32, 0.31, 'Is the answer valid?', size=26, color=PINK, weight='bold')
        T(fig, 0.32, 0.25, 'Formula assumes small angles:\nx much bigger than w and d\n4.3 mm and 0.25 mm ≪ 2.0 m ✓', size=23)


def diffraction(fig, s, ph):
    header(fig, 'Diffraction')
    for j, (g, title) in enumerate([(5.0, 'gap ≫ λ: little spreading'), (0.8, 'gap ≈ λ: strong spreading')]):
        ax = fig.add_axes([0.04 + j * 0.48, 0.29, 0.44, 0.47]); ax.axis('off')
        xs = np.linspace(-3, 9, 480); ys = np.linspace(-4, 4, 320)
        X, Y = np.meshgrid(xs, ys)
        key = ('df', g)
        if key not in _cache:
            src = [(0.0, yy, 1.0) for yy in np.linspace(-g / 2, g / 2, max(3, int(g * 8)))]
            U = _field(key + ('h',), xs, ys, src, TAU)
            U = U / np.abs(U[np.argmin(np.abs(ys)), np.argmin(np.abs(xs - 4))])
            _cache[key] = np.where(X < 0, np.exp(1j * TAU * X), U)
        Z = np.real(_cache[key] * np.exp(-1j * TAU * ph))
        Z = np.where((X < 0.25) & (X > -0.25) & (np.abs(Y) > g / 2), np.nan, Z)
        ax.imshow(Z, extent=(-3, 9, -4, 4), origin='lower', cmap=CM_WAVE, vmin=-1.3, vmax=1.3, interpolation='bilinear', aspect='auto')
        ax.add_patch(Rectangle((-0.2, g / 2), 0.4, 4, color=SOFT)); ax.add_patch(Rectangle((-0.2, -4), 0.4, 4 - g / 2, color=SOFT))
        ax.set_title(title, color=FG, fontsize=22, loc='left')
    if s == 0:
        bullets(fig, ['Spreading through a gap or around an obstacle (qualitative)', 'Most noticeable when the gap ≈ wavelength'],
                2, 0.06, 0.24, size=24, dim=False)
    else:
        bullets(fig, ['Longer λ → more diffraction: hear around corners; long-wave radio bends around hills',
                      'λ doesn’t change: keep wavefront spacing the same in sketches'], 2, 0.06, 0.24, size=24, dim=False)


def _filter(ax, x, y, ang, r=1.6, col=YELLOW):
    ax.add_patch(Circle((x, y), r, fc=PANEL2, ec=SOFT, lw=2))
    a = np.radians(ang)
    for o in np.linspace(-0.9, 0.9, 7) * r:
        dx, dy = np.sin(a), np.cos(a); px, py = x + o * np.cos(a), y - o * np.sin(a)
        Ln = np.sqrt(max(r ** 2 - o ** 2, 0)) * 0.92
        ax.plot([px - Ln * dx, px + Ln * dx], [py - Ln * dy, py + Ln * dy], color=MUT, lw=1.5)
    darrow(ax, (x - 1.25 * r * np.sin(a), y - 1.25 * r * np.cos(a)), (x + 1.25 * r * np.sin(a), y + 1.25 * r * np.cos(a)),
           color=col, ms=16)


def polarisation(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Polarisation')
    if s <= 1:
        ax = wax(fig, [0.04, 0.42, 0.92, 0.40], (0, 22), (-3, 3))
        for a in np.arange(0, 180, 22.5):
            r = np.radians(a); darrow(ax, (3 - 1.6 * np.cos(r), -1.6 * np.sin(r)), (3 + 1.6 * np.cos(r), 1.6 * np.sin(r)), color=C1, ms=12, lw=2)
        _filter(ax, 11, 0, 0)
        darrow(ax, (19, -1.6), (19, 1.6), color=C1, ms=16, lw=3)
        arrow(ax, (5.2, 0), (8.8, 0), color=C2); arrow(ax, (13.2, 0), (17.5, 0), color=C2)
        label(ax, 3, -2.6, 'unpolarised', size=22, color=SOFT); label(ax, 11, -2.6, 'polarising filter', size=22, color=SOFT)
        label(ax, 19, -2.6, 'plane polarised', size=22, color=SOFT)
        bullets(fig, ['Unpolarised: E-field oscillates in all directions ⊥ to travel',
                      'Filter passes only the component along its transmission axis'], 2, 0.06, 0.36, size=25, dim=False)
        if s == 1:
            card(fig, 0.05, 0.06, 0.90, 0.14, 'Only transverse waves can be polarised',
                 'longitudinal waves oscillate along the direction of travel → nothing to filter → light must be transverse',
                 tcol=GREEN, size=22)
        return
    if s == 2:
        ax = wax(fig, [0.05, 0.12, 0.42, 0.68], (-2, 4), (-0.8, 4.6))
        th = np.radians(30)
        arrow(ax, (0, 0), (0, 4), color=C1, lw=4); label(ax, -0.35, 2.0, 'A', size=30, color=C1, weight='bold')
        ax.plot([-1.2 * np.sin(th), 4.5 * np.sin(th)], [-1.2 * np.cos(th), 4.5 * np.cos(th)], color=YELLOW, lw=2, ls='--')
        p = 4 * np.cos(th)
        arrow(ax, (0, 0), (p * np.sin(th), p * np.cos(th)), color=C2, lw=5)
        ax.plot([0, p * np.sin(th)], [4, p * np.cos(th)], color=MUT, lw=1.5, ls=':')
        ax.add_patch(Arc((0, 0), 2.4, 2.4, theta1=60, theta2=90, color=FG, lw=2)); label(ax, 0.42, 1.5, 'θ', size=26)
        label(ax, 2.3, 2.55, 'A cos θ', size=28, color=C2, ha='left'); label(ax, 2.4, 4.0, 'filter axis', size=20, color=YELLOW, ha='left')
        learn_eq(fig, 0.52, 0.68, r'amplitude through $= A\cos\theta$', size=30, color=C2)
        learn_eq(fig, 0.52, 0.49, r'$I = I_0\cos^2\theta$', size=32, color=GREEN)
        bullets(fig, ['cos (not sin) when θ is measured\nfrom the polarisation direction', 'intensity ∝ amplitude²'], 2, 0.52,
                0.36, size=23, dim=False)
        return
    if s == 3:
        ax = wax(fig, [0.04, 0.36, 0.92, 0.44], (0, 24), (-3.2, 3.2))
        for x, a, nm in [(4, 0, '0°'), (12, 45, '45°'), (20, 90, '90°')]:
            _filter(ax, x, 0, a); label(ax, x, -2.6, nm, size=24, color=YELLOW)
        arrow(ax, (6.2, 0), (9.8, 0), color=C2); arrow(ax, (14.2, 0), (17.8, 0), color=C2); arrow(ax, (22.2, 0), (23.9, 0), color=C2)
        label(ax, 8, 0.8, 'A', size=26); label(ax, 16, 0.8, '0.71 A', size=26); label(ax, 23.2, 1.1, '0.50 A', size=24, color=GREEN)
        label(ax, 8, -0.8, 'I₀', size=22, color=SOFT); label(ax, 16, -0.8, '0.50 I₀', size=22, color=SOFT)
        label(ax, 23.2, -1.1, '0.25 I₀', size=22, color=GREEN)
        bullets(fig, ['Crossed filters (0° and 90°) alone: cos 90° = 0 → nothing', 'Add a 45° filter between: A × cos45° × cos45° = 0.50 A'],
                2, 0.06, 0.30, size=25, dim=False)
        return
    if s == 4:
        ax = wax(fig, [0.04, 0.14, 0.55, 0.66], (0, 12), (-1, 8))
        ax.add_patch(Rectangle((0, -1), 12, 2.2, fc='#173a5c', ec='none')); label(ax, 1.2, -0.3, 'water', size=20, color=SOFT)
        ax.add_patch(Circle((1.5, 7), 0.7, color=YELLOW))
        ax.plot([2, 6], [6.5, 1.2], color=YELLOW, lw=3); arrow(ax, (6, 1.2), (10, 6.2), color=YELLOW, lw=3)
        for t in (0.35, 0.6, 0.85):
            px, py = 6 + 4 * t, 1.2 + 5 * t
            darrow(ax, (px - 0.6, py), (px + 0.6, py), color=C2, ms=10, lw=2)
        label(ax, 9.2, 3.0, 'glare: mostly\nhorizontal', size=20, color=C2, ha='left')
        _filter(ax, 10.6, 6.9, 0, r=0.8)
        bullets(fig, ['Reflected light is partly polarised,\nmostly horizontally', 'Polarising sunglasses: vertical axis\n→ block much of the glare',
                      'Tilt your head 90° → glare returns'], 3, 0.62, 0.76, size=24)
        return
    # s == 5: scattering
    ax = wax(fig, [0.04, 0.14, 0.55, 0.66], (0, 12), (0, 8))
    arrow(ax, (0.5, 4), (5.6, 4), color=YELLOW, lw=4); label(ax, 2.5, 4.6, 'unpolarised sunlight', size=19, color=YELLOW)
    ax.add_patch(Circle((6, 4), 0.35, color=C1)); label(ax, 6, 3.2, 'air molecule', size=17, color=SOFT)
    arrow(ax, (6, 4.4), (6, 7.6), color=C2, lw=3); label(ax, 6.4, 7.3, 'scattered at 90°', size=19, color=C2, ha='left')
    for yy in (5.4, 6.4):
        darrow(ax, (5.4, yy), (6.6, yy), color=GREEN, ms=10, lw=2)
    label(ax, 7.0, 5.9, 'polarised ⊥ to the\nplane of scattering', size=17, color=GREEN, ha='left')
    bullets(fig, ['Light scattered at 90° is (mostly)\nplane polarised', 'Rotate a polarising filter: the sky\nbrightens and darkens',
                  'Reflection, scattering and filters\nall show light is transverse'], 3, 0.62, 0.76, size=24, dim=False)


def light_history(fig, s, ph):
    """Development of the wave theory of light (course context)."""
    C1, C2 = C()
    header(fig, 'How we learned light is a wave')
    ev = [('1600s', 'Newton', 'particles:\nreflection,\nstraight lines', MUT),
          ('1678', 'Huygens', 'waves & wavelets:\nrefraction (slower\nin glass)', C1),
          ('1801', 'Young', 'double slit:\ninterference\n→ a wave', GREEN),
          ('1810s', 'Malus, Fresnel', 'polarisation\n→ TRANSVERSE\nwave', C2),
          ('1860s', 'Maxwell', 'EM waves at\n≈ 3 × 10⁸ m s⁻¹\n→ light is EM', YELLOW)]
    n = [2, 4, 5][s]
    ax = wax(fig, [0.05, 0.66, 0.90, 0.08], (0, 10), (-1, 1))
    ax.plot([0.2, 9.8], [0, 0], color=GRID, lw=4)
    for i in range(n):
        x = 0.05 + i * 0.182
        ax.scatter([1 + i * 2], [0], s=200, color=ev[i][3], zorder=4)
        T(fig, x, 0.62, ev[i][0], size=26, color=ev[i][3], weight='bold')
        T(fig, x, 0.555, ev[i][1], size=24, color=FG, weight='bold')
        T(fig, x, 0.495, ev[i][2], size=20, color=SOFT)
    if s == 2:
        card(fig, 0.05, 0.08, 0.90, 0.20, 'Why it matters for you',
             'Each piece of evidence is a wave property from this criterion: refraction, interference,\n'
             'polarisation and wave speed. Later (Criterion 8) light also shows particle behaviour.', tcol=C2, size=22)


# ============================================================================ finish
def exam_tips(fig, s, ph):
    C1, C2 = C()
    if s <= 3:
        header(fig, 'Tips for tests and the exam')
        tips = ['EM waves (light, radio, radar): c = 3.00 × 10⁸ m s⁻¹.\n344 m s⁻¹ is for sound only',
                'Convert units: ms → s, g → kg,\ncm, mm, nm → m', 'String: λ₁ = 2l (not l)\nClosed pipe: λ₁ = 4l',
                'Smooth sine shapes. Label N, A,\nangles and rays; add arrows', 'Harmonics ≠ overtones',
                'Path difference = simple subtraction', '“Describe” = what happens\n“Explain” = why (use physics ideas)',
                'Keep going: errors are carried\nforward for method marks']
        n = [1, 3, 6, 8][s]
        cols = [C1, C2, PINK, GREEN, YELLOW, C1, C2, PINK]
        for i in range(n):
            x = 0.05 + (i % 2) * 0.46; y = 0.66 - (i // 2) * 0.165
            box(fig, x, y, 0.44, 0.145, fc=PANEL if i < n - [1, 2, 3, 2][s] else PANEL2)
            T(fig, x + 0.015, y + 0.0725, str(i + 1), size=40, color=cols[i], weight='bold', va='center')
            T(fig, x + 0.06, y + 0.0725, tips[i], size=21, va='center')
        T(fig, 0.05, 0.13, 'From examiners’ comments in TASC assessment reports', size=18, color=MUT)
        return
    header(fig, 'Criterion 7 in one screen')
    chips = [('energy transfer', C1), ('A · λ · T · f · v', C1), ('transverse / longitudinal', C1), ('SHM · graphs', C1),
             ('reflection · pulses', C2), ('refraction · Snell', C2), ('critical angle · TIR', C2), ('v = √(T/μ)', C2),
             ('superposition · beats', PINK), ('standing waves', PINK), ('strings & pipes', PINK), ('resonance', PINK),
             ('interference · PD', GREEN), ('w = λx/d', GREEN), ('diffraction', GREEN), ('polarisation', GREEN)]
    for i, (t, c) in enumerate(chips):
        x = 0.05 + (i % 4) * 0.228; y = 0.66 - (i // 4) * 0.15
        box(fig, x, y, 0.21, 0.11, fc=PANEL, ec=c, lw=2)
        T(fig, x + 0.105, y + 0.055, t, size=23, ha='center', va='center')
    T(fig, 0.5, 0.12, 'Practise explaining each idea in words, as well as with numbers.', size=26, color=YELLOW, ha='center')


# ============================================================================ added steps and scenes
def extend(base, n, *extras):
    """A scene drawn by `base` for its first n steps, then by one extra draw function per further step."""
    def draw(fig, s, ph):
        return base(fig, s, ph) if s < n else extras[s - n](fig, s - n, ph)
    return draw


def _panel(fig, x, y, w, h, title, col=None):
    """Titled panel for a mini diagram; returns the figure rect for its drawing area."""
    box(fig, x, y, w, h)
    T(fig, x + 0.012, y + h - 0.015, title, size=23, color=col or L.A2(), weight='bold')
    return [x + 0.01, y + 0.01, w - 0.02, h - 0.075]


def particle_motion(fig, s, ph):
    """Particle velocity and acceleration on a travelling wave."""
    C1, C2 = C()
    if s < 2:
        header(fig, 'What are the particles doing?')
        ax = wax(fig, [0.04, 0.26, 0.56, 0.54], (0, 10), (-2.3, 2.3))
        x = np.linspace(0, 10, 500)
        ax.axhline(0, color=GRID, lw=1.5, ls='--')
        ax.plot(x, 1.3 * np.sin(TAU * x / 8), color=C1, lw=4)
        arrow(ax, (3.6, 2.05), (6.4, 2.05), color=SOFT); label(ax, 5, 2.27, 'wave travels right', size=18, color=SOFT)
        pts = [(0.0, 'P', 0), (2.0, 'Q', 1), (4.0, 'R', 0), (6.0, 'S', -1), (8.0, 'U', 0)]
        for px, nm, side in pts:
            py = 1.3 * np.sin(TAU * px / 8)
            ax.scatter([px + 0.06], [py], s=150, color=YELLOW, zorder=5)
            label(ax, px + 0.42, py + (0.35 if side >= 0 else -0.35), nm, size=22, color=YELLOW)
            if s == 0 and side == 0:
                vy = -1.0 if px in (0.0, 8.0) else 1.0
                arrow(ax, (px + 0.06, py), (px + 0.06, py + vy), color=GREEN, lw=4)
            if s == 1 and side != 0:
                arrow(ax, (px, py), (px, py - 0.95 * side), color=PINK, lw=4)
        if s == 0:
            bullets(fig, ['Shift the curve slightly in the\ndirection of travel', 'Crest and trough: velocity zero',
                          'Rest position: greatest speed'], 3, 0.63, 0.76, size=24, dim=False)
            T(fig, 0.06, 0.20, 'green arrows = particle velocity', size=22, color=GREEN)
        else:
            bullets(fig, ['Crest and trough: greatest\nacceleration, towards rest', 'Rest position: zero acceleration',
                          'The biggest restoring force is at\nthe biggest displacement'], 3, 0.63, 0.76, size=24, dim=False)
            T(fig, 0.06, 0.20, 'pink arrows = particle acceleration', size=22, color=PINK)
            card(fig, 0.63, 0.10, 0.32, 0.185, 'Check', 'travelling wave, not a\nstanding wave', tcol=PINK, size=21)
        return
    header(fig, 'Two recorders, one wave')
    chip(fig, 'Element 3 · data')
    for i, (lag, nm, col) in enumerate([(0, 'Recorder A', C1), (2, 'Recorder B (12 m further east)', GREEN)]):
        ax = gax(fig, [0.07, 0.50 - i * 0.33, 0.50, 0.25], (0, 24), (-1.5, 1.5), 'time (s)' if i else '', 'y (m)')
        t = np.linspace(0, 24, 500)
        ax.plot(t, np.sin(TAU * (t - lag) / 8), color=col, lw=3.5)
        ax.set_title(nm, color=col, fontsize=19, loc='left')
        ax.set_yticks([-1, 0, 1]); ax.set_xticks([0, 8, 16, 24])
        if i == 0: ax.set_xticklabels([])
    y = 0.77
    for st, c in [('B copies A 2.0 s later', SOFT), ('→ the wave travels from A to B: east', GREEN),
                  (r'$v = \dfrac{12}{2.0} = 6.0\ \mathrm{m\ s^{-1}}$', FG), (r'$T = 8.0\ \mathrm{s}$', FG),
                  (r'$\lambda = vT = 48\ \mathrm{m}$', GREEN)]:
        T(fig, 0.62, y, st, size=25, color=c); y -= 0.12 if 'dfrac' in st else 0.075
    card(fig, 0.62, 0.13, 0.33, 0.17, 'Use what you are given', 'separation and time lag first,\nnot the wave equation', tcol=PINK, size=21)


def huygens_snell(fig, s, ph):
    """Snell's law from a wavefront crossing a boundary."""
    C1, C2 = C()
    header(fig, "Where Snell's law comes from")
    ax = wax(fig, [0.04, 0.12, 0.50, 0.68], (-1, 9), (-5, 5))
    ax.axhline(0, color=SOFT, lw=2)
    label(ax, 8.9, 0.45, 'speed vᵢ', size=20, color=SOFT, ha='right'); label(ax, 8.9, -0.45, 'speed vᵣ', size=20, color=SOFT, ha='right')
    A_, Y = (1.5, 0), (6.5, 0)
    ti, tr = np.radians(40), np.arcsin(0.6 * np.sin(np.radians(40)))
    AY = 5
    B = (A_[0] + AY * np.cos(ti) ** 2, AY * np.cos(ti) * np.sin(ti))
    X = (A_[0] + AY * np.sin(tr) ** 2, -AY * np.sin(tr) * np.cos(tr))
    ax.plot([A_[0], B[0]], [A_[1], B[1]], color=C1, lw=4); ax.plot([X[0], Y[0]], [X[1], Y[1]], color=GREEN, lw=4)
    arrow(ax, B, Y, color=YELLOW); arrow(ax, A_, X, color=YELLOW)
    for q, nm, dx, dy in [(A_, 'A', -0.3, 0.4), (B, 'B', 0.1, 0.45), (Y, 'Y', 0.4, 0.4), (X, 'X', -0.25, -0.45)]:
        label(ax, q[0] + dx, q[1] + dy, nm, size=25, color=YELLOW)
    label(ax, 6.3, 1.5, 'vᵢt', size=24, color=YELLOW); label(ax, 1.2, -1.1, 'vᵣt', size=24, color=YELLOW, ha='right')
    y = 0.76
    for st, c in [('In the same time t:', SOFT), (r'$BY = v_i t,\quad AX = v_r t$', FG),
                  (r'$\sin\theta_i = \dfrac{v_i t}{AY}$', FG), (r'$\sin\theta_r = \dfrac{v_r t}{AY}$', FG),
                  (r'$\dfrac{\sin\theta_i}{\sin\theta_r} = \dfrac{v_i}{v_r}$', GREEN)]:
        T(fig, 0.60, y, st, size=29, color=c); y -= 0.12 if 'dfrac' in st else 0.08


def tir_partial(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Below the critical angle: both happen')
    ax = wax(fig, [0.03, 0.10, 0.52, 0.72], (-5, 5), (-3.9, 3.9))
    _tir_draw(ax, 28, C2=C2)
    bullets(fig, ['No total internal reflection does not\nmean no reflection', 'Below θc: refraction and a weak reflection',
                  'Above θc: all of the light reflects,\nso the ray stays bright'], 3, 0.58, 0.76, size=24, dim=False)
    a2 = wax(fig, [0.60, 0.10, 0.28, 0.30], (-3, 3), (-1, 3.2))
    a2.add_patch(Polygon([(-3, 2.8), (3, 2.8), (0, -0.2)], fc='#1a3150', ec=SOFT, lw=2))
    a2.plot([-1, -1, 1, 1], [3.2, 0.8, 0.8, 3.2], color=YELLOW, lw=3)
    arrow(a2, (-1, 3.2), (-1, 1.8), color=YELLOW, lw=3, ms=16); arrow(a2, (1, 1.6), (1, 3.1), color=YELLOW, lw=3, ms=16)
    T(fig, 0.60, 0.43, 'A gem cut to send light back: two reflections at 45°', size=19, color=SOFT)


def fibre_example(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: an optical fibre')
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.04, 0.46, 0.46, 0.34], (-2, 12), (-2.4, 2.4))
    ax.add_patch(Rectangle((1, -2), 11, 4, fc='#21395a', ec='none')); ax.add_patch(Rectangle((1, -1), 11, 2, fc='#1a4a6e', ec='none'))
    label(ax, 9.7, 1.5, 'cladding  n = 1.44', size=19, color=SOFT); label(ax, 9.7, 0, 'core  n = 1.46', size=19, color=FG)
    ax.plot([-1.6, 1, 5.2, 9.4, 12], [-1.0, 0, 1, -1, 0.0], color=YELLOW, lw=3)
    if s == 0:
        y = 0.40
        for st, c in [(r'$v = \dfrac{c}{n} = \dfrac{3.00\times10^{8}}{1.46} = 2.05\times10^{8}\ \mathrm{m\ s^{-1}}$', FG),
                      (r'$t = \dfrac{4.00\times10^{6}}{2.05\times10^{8}} = 19.5\ \mathrm{ms}$  for 4000 km', GREEN)]:
            T(fig, 0.06, y, st, size=28, color=c); y -= 0.14
        return
    T(fig, 0.06, 0.40, r'$\sin\theta_c = \dfrac{1.44}{1.46}\ \Rightarrow\ \theta_c = 80.5^\circ$', size=28)
    T(fig, 0.06, 0.26, r'angle to the axis $= 90^\circ - 80.5^\circ = 9.5^\circ$', size=28)
    T(fig, 0.06, 0.17, r'$1.00\,\sin\alpha = 1.46\,\sin 9.5^\circ\ \Rightarrow\ \alpha = 13.9^\circ$', size=28, color=GREEN)
    card(fig, 0.56, 0.42, 0.39, 0.34, 'The 90° − θ step',
         'θc is measured from the normal to\nthe core wall. The entry face is at\nright angles to that wall, so the\nray inside makes 90° − θc with\nthe normal to the entry face.', tcol=PINK, size=22)


def parallel_layers(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Flat parallel layers')
    ax = wax(fig, [0.04, 0.12, 0.48, 0.68], (-5, 5), (-5, 5))
    ax.add_patch(Rectangle((-5, -1.2), 10, 2.4, fc='#21395a', ec='none'))
    ax.add_patch(Rectangle((-5, -5), 10, 3.8, fc='#17304d', ec='none'))
    for yy in (1.2, -1.2): ax.plot([-5, 5], [yy, yy], color=SOFT, lw=2)
    p = [(-3.8, 5), (-1.3, 1.2), (-0.1, -1.2), (2.3, -5)]
    for a, b in zip(p, p[1:]): arrow(ax, a, b, color=YELLOW, lw=3.5, ms=20)
    label(ax, 3.2, 3.2, 'air', size=22, color=SOFT); label(ax, 3.2, 0, 'glass', size=22, color=SOFT); label(ax, 3.2, -3.2, 'water', size=22, color=SOFT)
    eq(fig, 0.55, 0.68, r'$n\,\sin\theta$ is the same in every layer', size=30, color=GREEN)
    bullets(fig, ['Write Snell’s law at each boundary', 'The middle layer’s term cancels', 'So thin parallel glass does not change\nthe final angle: it only shifts the ray sideways'],
            3, 0.55, 0.54, size=24, dim=False)


def refraction_contexts(fig, s, ph):
    """Brief unfamiliar contexts for refraction."""
    C1, C2 = C()
    header(fig, 'Refraction in unfamiliar contexts')
    chip(fig, 'Element 4 · predictions')
    r = _panel(fig, 0.05, 0.45, 0.44, 0.36, 'Apparent depth')
    ax = wax(fig, r, (0, 10), (0, 6))
    ax.add_patch(Rectangle((0, 0), 10, 3.6, fc='#173a5c', ec='none'))
    ax.scatter([3], [0.7], s=120, color=PINK, zorder=5); ax.scatter([3], [2.2], s=120, color=PINK, alpha=0.45, zorder=5)
    ax.plot([3, 5, 9], [0.7, 3.6, 5.6], color=YELLOW, lw=3); ax.plot([3, 5], [2.2, 3.6], color=YELLOW, lw=2, ls='--')
    label(ax, 1.5, 2.2, 'looks here', size=18, color=SOFT); label(ax, 1.5, 0.7, 'really here', size=18, color=SOFT)
    r = _panel(fig, 0.51, 0.45, 0.44, 0.36, 'Mirage over cold water')
    ax = wax(fig, r, (0, 10), (0, 6))
    xx = np.linspace(1, 9, 100); ax.plot(xx, 0.6 + 0.18 * (xx - 1) * (9 - xx), color=YELLOW, lw=3)
    ax.plot([5.8, 9], [5.2, 0.6], color=SOFT, lw=2, ls='--'); ax.scatter([1], [0.6], s=120, color=PINK, zorder=5)
    label(ax, 5.8, 5.55, 'seen up here', size=18, color=SOFT); label(ax, 9.3, 1.3, 'eye', size=18, color=SOFT); label(ax, 0.55, 1.15, 'ship', size=18, color=SOFT)
    ax.add_patch(Rectangle((0, 0), 10, 0.5, fc='#173a5c', ec='none'))
    if s == 0:
        return
    r = _panel(fig, 0.05, 0.08, 0.44, 0.34, 'Rainbow droplet')
    ax = wax(fig, r, (-5, 5), (-3.2, 3.2)); ax.set_aspect('equal')
    ax.add_patch(Circle((0, 0), 2.7, fc='#173a5c', ec=SOFT, lw=2))
    th = np.radians(40); P0 = (-2.7 * np.cos(th), 2.7 * np.sin(th)); Pb = (2.7 * np.cos(np.radians(10)), 2.7 * np.sin(np.radians(10))); P2 = (-2.7 * np.cos(np.radians(50)), -2.7 * np.sin(np.radians(50)))
    ax.plot([-5, P0[0]], [P0[1], P0[1]], color=FG, lw=3)
    ax.plot([P0[0], Pb[0], P2[0]], [P0[1], Pb[1], P2[1]], color=PINK, lw=2.5); ax.plot([P2[0], -5], [P2[1], -3.2], color=PINK, lw=2.5)
    ax.plot([P0[0], Pb[0] - 0.1, P2[0] - 0.35], [P0[1], Pb[1] - 0.25, P2[1] + 0.35], color=C1, lw=2.5); ax.plot([P2[0] - 0.35, -5], [P2[1] + 0.35, -2.2], color=C1, lw=2.5)
    label(ax, 3.9, -1.6, 'each angle\nby Snell', size=18, color=SOFT)
    r = _panel(fig, 0.51, 0.08, 0.44, 0.34, 'Calcite: two refractive indices')
    ax = wax(fig, r, (0, 10), (-3, 3))
    ax.add_patch(Rectangle((3, -2.8), 5, 5.6, fc='#21395a', ec=SOFT, lw=2))
    ax.plot([0, 3], [0.8, 0], color=FG, lw=3); ax.plot([3, 8, 10], [0, -0.8, -1.3], color=GREEN, lw=3); ax.plot([3, 8, 10], [0, -1.8, -2.5], color=YELLOW, lw=3)
    label(ax, 1.5, -1.3, 'each polarisation\nhas its own n', size=17, color=SOFT)


def sound_snell(fig, s, ph):
    C1, C2 = C()
    header(fig, "Snell's law for sound: use speeds")
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.04, 0.12, 0.48, 0.68], (0, 12), (0, 9))
    bands = [(6, 3, '#21395a', '1510 m s⁻¹'), (3, 3, '#173a5c', '1480 m s⁻¹'), (0, 3, '#21395a', '1510 m s⁻¹')]
    for y0, h, c, t in bands:
        ax.add_patch(Rectangle((0, y0), 12, h, fc=c, ec='none')); label(ax, 11.8, y0 + h - 0.45, t, size=19, color=SOFT, ha='right')
    ax.plot([0.5, 2.6, 5.0, 7.4, 9.8], [3.4, 5.9, 3.1, 5.9, 3.1], color=YELLOW, lw=3)
    label(ax, 6, 7.5, 'faster layer', size=20, color=SOFT); label(ax, 6, 1.2, 'faster layer', size=20, color=SOFT); label(ax, 2.5, 3.5, 'slow layer', size=20, color=FG)
    y = 0.77
    for st, c in [(r'$\dfrac{\sin 40^\circ}{\sin\theta_r} = \dfrac{1480}{1510}\ \Rightarrow\ \theta_r = 41.0^\circ$', FG),
                  (r'$\sin\theta_c = \dfrac{1480}{1510}\ \Rightarrow\ \theta_c = 78.6^\circ$', GREEN)]:
        T(fig, 0.55, y, st, size=29, color=c); y -= 0.15
    bullets(fig, ['Critical angle: going from slow to fast', 'Steep angles: sound is trapped in the\nslow layer and travels a long way',
                  'For sound, a slower layer acts like\nthe “optically denser” one'], 3, 0.55, 0.45, size=24, dim=False)


def super_mixed(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Superposing different wavelengths')
    x = np.linspace(0, 20, 800)
    a, b = np.sin(TAU * x / 10), 0.5 * np.sin(TAU * x / 2.5 + 0.7)
    for i, (yy, c, nm) in enumerate([(a, C1, 'long wave'), (b, GREEN, 'short wave'), (a + b, YELLOW, 'sum, added point by point')]):
        ax = wax(fig, [0.05, 0.60 - i * 0.21, 0.56, 0.19], (0, 20), (-1.7, 1.7))
        ax.axhline(0, color=GRID, lw=1.2); ax.plot(x, yy, color=c, lw=3.2)
        T(fig, 0.63, 0.72 - i * 0.21, nm, size=22, color=c)
    card(fig, 0.63, 0.06, 0.32, 0.205, 'Not a taller copy', 'the sum keeps both wiggles,\nand changes as the waves\nmove at different speeds', tcol=PINK, size=20)


def pipe_id(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Open or closed? Read the resonances')
    chip(fig, 'Element 3 · data')
    card(fig, 0.05, 0.50, 0.43, 0.30, 'Pipe X: 240, 320, 400 Hz', 'spacing 80 Hz, so f₁ = 80 Hz\n240 = 3f₁, 320 = 4f₁, 400 = 5f₁\nan even harmonic → OPEN', tcol=C1, size=24)
    T(fig, 0.06, 0.42, r'open:  $l = \dfrac{\lambda}{2} = \dfrac{344}{2\times80} = 2.15\ \mathrm{m}$', size=27)
    if s == 0:
        return
    card(fig, 0.52, 0.50, 0.43, 0.30, 'Pipe Y: 150, 250, 350 Hz', 'spacing 100 Hz = 2f₁, so f₁ = 50 Hz\n150 = 3f₁, 250 = 5f₁, 350 = 7f₁\nodd harmonics only → CLOSED', tcol=C2, size=24)
    T(fig, 0.53, 0.42, r'closed:  $l = \dfrac{\lambda}{4} = \dfrac{344}{4\times50} = 1.72\ \mathrm{m}$', size=27)
    card(fig, 0.05, 0.08, 0.90, 0.20, 'Justify with the ends',
         'A closed pipe needs a node at the closed end and an antinode at the open end, so only odd numbers of\nquarter wavelengths fit. That is why it has no even harmonics.', tcol=PINK, size=23)


def linearise(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Straightening a graph to find μ')
    chip(fig, 'Element 3 · data')
    Tn = np.array([20., 40., 80.]); f = np.array([83.3, 117.9, 166.7])
    ax = gax(fig, [0.07, 0.20, 0.25, 0.54], (0, 90), (0, 190), 'tension T (N)', 'f (Hz)')
    tt = np.linspace(0, 90, 200); ax.plot(tt, np.sqrt(tt / 0.002) / 1.2, color=C1, lw=3); ax.scatter(Tn, f, s=90, color=YELLOW, zorder=5)
    ax.set_title('a curve', color=C1, fontsize=20)
    if s >= 1:
        ax = gax(fig, [0.39, 0.20, 0.25, 0.54], (0, 90), (0, 32000), 'tension T (N)', 'f² (Hz²)')
        ax.plot(tt, tt * 347.2, color=GREEN, lw=3); ax.scatter(Tn, f ** 2, s=90, color=YELLOW, zorder=5)
        ax.set_title('a straight line', color=GREEN, fontsize=20)
    if s == 0:
        bullets(fig, ['Wire: l = 0.60 m, fundamental', 'T = 20 N → f = 83.3 Hz', 'T = 40 N → f = 117.9 Hz', 'T = 80 N → f = 166.7 Hz'], 4, 0.40, 0.72, size=25, dim=False)
    elif s == 1:
        T(fig, 0.68, 0.76, r'$f = \dfrac{1}{2l}\sqrt{\dfrac{T}{\mu}}$', size=30)
        T(fig, 0.68, 0.61, r'$f^2 = \dfrac{1}{4l^2\mu}\,T$', size=30, color=GREEN)
        T(fig, 0.68, 0.48, 'so plot f² against T', size=24, color=SOFT)
    else:
        T(fig, 0.68, 0.76, r'gradient $= 347\ \mathrm{Hz^2\ N^{-1}}$', size=25)
        T(fig, 0.68, 0.66, r'$\mu = \dfrac{1}{4l^2 \times \mathrm{gradient}}$', size=28)
        T(fig, 0.68, 0.51, r'$\mu = 2.0\times10^{-3}\ \mathrm{kg\ m^{-1}}$', size=25, color=GREEN)
        T(fig, 0.68, 0.42, 'use the line, not one point', size=22, color=SOFT)


def standing_contexts(fig, s, ph):
    """Brief unfamiliar contexts for standing waves."""
    C1, C2 = C()
    header(fig, 'Standing waves in unfamiliar contexts')
    chip(fig, 'Element 4 · predictions')
    r = _panel(fig, 0.05, 0.38, 0.28, 0.43, 'Glass rim')
    ax = wax(fig, r, (-3, 3), (-3, 3)); ax.set_aspect('equal')
    t = np.linspace(0, TAU, 300)
    ax.plot(2 * np.cos(t), 2 * np.sin(t), color=MUT, lw=2, ls='--')
    ax.plot((2 + 0.5 * np.cos(2 * t)) * np.cos(t), (2 + 0.5 * np.cos(2 * t)) * np.sin(t), color=C1, lw=3.5)
    T(fig, 0.06, 0.34, 'whole wavelengths fit\nthe circumference', size=20, color=SOFT)
    r = _panel(fig, 0.36, 0.38, 0.28, 0.43, 'Microwave oven')
    ax = wax(fig, r, (0, 10), (-3, 3))
    ax.add_patch(Rectangle((0.5, -2.2), 9, 4.4, fc='none', ec=SOFT, lw=4))
    x = np.linspace(0.5, 9.5, 300)
    for sg in (1, -1): ax.plot(x, sg * 1.6 * np.sin(np.pi * 3 * (x - 0.5) / 9), color=GREEN, lw=3)
    T(fig, 0.37, 0.34, 'metal walls are nodes\nnodes λ/2 apart: cold spots', size=20, color=SOFT)
    r = _panel(fig, 0.67, 0.38, 0.28, 0.43, 'Phone antenna')
    ax = wax(fig, r, (0, 10), (-3, 3))
    x = np.linspace(1, 9, 200)
    for sg in (1, -1): ax.plot(x, sg * 2 * np.cos(np.pi * (x - 1) / 16), color=C2, lw=3)
    ax.plot([1, 9], [0, 0], color=FG, lw=5); label(ax, 8.9, 0.6, 'N', size=22, color=PINK); label(ax, 1.5, 2.45, 'A', size=22, color=YELLOW)
    T(fig, 0.68, 0.34, 'quarter-wave standing wave:\nlength = λ/4', size=20, color=SOFT)
    if s >= 1:
        box(fig, 0.05, 0.08, 0.90, 0.17, fc=PANEL2)
        T(fig, 0.07, 0.225, 'Change the gas or the temperature in a pipe', size=25, color=C2, weight='bold')
        T(fig, 0.07, 0.165, 'Length fixes λ, so f = v/λ rises and falls with the wave speed.  Warmer air or helium → higher v → higher f.', size=21)


def coherence(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Getting coherent sources')
    ax = wax(fig, [0.04, 0.40, 0.92, 0.40], (0, 24), (-3, 3))
    ax.scatter([1], [0], s=500, color=YELLOW, zorder=5); label(ax, 1, -1.1, 'ordinary\nlamp', size=18, color=SOFT)
    for x0, gaps in [(6, [0]), (12, [-1.1, 1.1])]:
        edges = [-2.2] + [g + d for g in gaps for d in (-0.2, 0.2)] + [3]
        for a, b in zip(edges[0::2], edges[1::2]): ax.plot([x0, x0], [a, b], color=SOFT, lw=6)
    for r in (1.4, 2.6, 3.8): ax.add_patch(Arc((6, 0), 2 * r, 2 * r, theta1=-50, theta2=50, color=C1, lw=2))
    for y0 in (-1.1, 1.1):
        for r in (1.4, 2.6, 3.8, 5.0): ax.add_patch(Arc((12, y0), 2 * r, 2 * r, theta1=-40, theta2=40, color=GREEN, lw=2))
    label(ax, 6, -2.4, 'single slit\n(pinhole)', size=18, color=C1, va='top'); label(ax, 12, -2.4, 'double slit', size=18, color=GREEN, va='top')
    label(ax, 20.5, 2.2, 'or a laser: already coherent', size=20, color=YELLOW)
    ax.add_patch(Rectangle((18, -0.5), 4.8, 1.0, fc=PANEL2, ec=SOFT)); label(ax, 20.4, 0, 'laser', size=18, color=SOFT)
    for i, (nm, b, c) in enumerate([('Single slit', 'diffracts light so one wavefront\nreaches both slits. It does not\nselect a colour.', C1),
                                    ('Monochromatic', 'one wavelength\n(one colour).', YELLOW),
                                    ('Coherent', 'same frequency and a constant\nphase relationship. They need not\nbe in phase.', GREEN)]):
        card(fig, 0.05 + i * 0.31, 0.09, 0.28, 0.25, nm, b, tcol=c, size=20)


def antinodal_lines(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Steering a beam' if s else 'Counting antinodal lines')
    ax = wax(fig, [0.04, 0.12, 0.48, 0.68], (-6, 6), (-1, 8))
    S1, S2 = (-1, 0), (1, 0)
    ax.scatter(*zip(S1, S2), s=180, color=YELLOW, zorder=5)
    if s == 0:
        for sth, c in [(0, GREEN), (0.444, C1), (-0.444, C1), (0.889, C2), (-0.889, C2)]:
            ax.plot([0, 8.5 * sth], [0, 8.5 * np.sqrt(1 - sth ** 2)], color=c, lw=3)
        label(ax, 0.15, 7.7, 'n = 0', size=20, color=GREEN, ha='left')
        for sg in (1, -1): label(ax, sg * 2.5, 7.5, 'n = 1', size=20, color=C1); label(ax, sg * 5.3, 4.6, 'n = 2', size=20, color=C2)
        label(ax, 0, -0.65, 'd = 0.90 m,  λ = 0.40 m', size=20, color=YELLOW)
        chip(fig, 'Element 2 · problems')
        bullets(fig, ['Largest path difference = d', 'nλ ≤ d, so n ≤ 0.90 / 0.40 = 2.25', 'n can be 0, ±1 or ±2'], 3, 0.56, 0.76, size=26, dim=False)
        T(fig, 0.56, 0.48, '5 antinodal lines', size=38, color=GREEN, weight='bold')
        T(fig, 0.56, 0.38, 'Nodal lines lie between them.\nA quick sketch keeps the count honest.', size=23, color=SOFT)
    else:
        for sth, c in [(0.25, GREEN), (0.694, C1), (-0.194, C1)]:
            ax.plot([0, 8.5 * sth], [0, 8.5 * np.sqrt(1 - sth ** 2)], color=c, lw=3)
        ax.plot([0, 0], [0, 8], color=MUT, lw=2, ls='--')
        label(ax, 2.9, 7.5, 'central line turns', size=20, color=GREEN, ha='left')
        bullets(fig, ['Delay one source: the two waves start\nout of step', 'Equal arrival now happens off-centre',
                      r'$\sin\theta = \dfrac{\mathrm{head\ start}}{d}$', 'The beam steers with no moving parts', 'More sources → narrower, stronger beam'],
                5, 0.56, 0.76, size=25, dim=False)


def bragg(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Another two-path case: X-rays and crystals')
    ax = wax(fig, [0.04, 0.14, 0.50, 0.66], (0, 10), (0, 7))
    for yy in (2.2, 4.2):
        ax.plot([0.5, 9.5], [yy, yy], color=SOFT, lw=2, ls=(0, (1, 2)))
    label(ax, 9.2, 3.2, 'd', size=25, color=YELLOW); darrow(ax, (8.7, 2.2), (8.7, 4.2), color=YELLOW, ms=14)
    ax.plot([1.5, 4.1, 6.7], [6.2, 4.2, 6.2], color=C1, lw=3.5); ax.plot([1.5, 4.9, 8.3], [4.8, 2.2, 4.8], color=GREEN, lw=3.5)
    bullets(fig, ['Lower ray travels further:\ntwo extra lengths of d sin θ', r'path difference $= 2d\sin\theta$',
                  'Bright when that equals nλ', 'θ here is measured from the\nlayer, not from the normal'], 4, 0.58, 0.76, size=25, dim=False)


def youngs_sound(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The same formula for sound')
    chip(fig, 'Element 2 · problems')
    ax = wax(fig, [0.04, 0.34, 0.46, 0.46], (0, 12), (-5, 5))
    for y0 in (-1.6, 1.6): ax.add_patch(Rectangle((0.5, y0 - 0.4), 0.8, 0.8, fc=YELLOW, ec='none'))
    darrow(ax, (0.2, -1.6), (0.2, 1.6), color=YELLOW, ms=12); label(ax, 1.7, 0, 'd = 2.0 m', size=19, color=YELLOW, ha='left')
    ax.plot([11, 11], [-4.8, 4.8], color=SOFT, lw=2)
    for k in range(-3, 4): ax.scatter([11], [k * 1.4], s=120, color=GREEN, zorder=5)
    darrow(ax, (1.3, -4.3), (11, -4.3), color=C1, ms=12); label(ax, 6, -3.8, 'x = 8.0 m', size=19, color=C1)
    darrow(ax, (10.5, 0), (10.5, 1.4), color=PINK, ms=10); label(ax, 10.2, 0.7, 'w = 1.1 m', size=18, color=PINK, ha='right')
    y = 0.76
    for st, c in [(r'$\lambda = \dfrac{wd}{x} = \dfrac{1.1\times2.0}{8.0} = 0.275\ \mathrm{m}$', FG),
                  (r'$f = \dfrac{344}{0.275} \approx 1250\ \mathrm{Hz}$', GREEN)]:
        T(fig, 0.54, y, st, size=29, color=c); y -= 0.15
    bullets(fig, ['Don’t swap x and d', 'Speakers closer → d smaller → w bigger', 'Shorter λ → smaller w → more fringes fit'], 3, 0.54, 0.46, size=24, dim=False)
    card(fig, 0.05, 0.08, 0.90, 0.17, 'Two separate signal generators?', 'Slightly different frequencies give beats, not a steady pattern. One generator driving both speakers\ngives the same frequency and a fixed phase relationship.', tcol=PINK, size=21)


def single_slit(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Single-slit diffraction')
    ax = gax(fig, [0.07, 0.30, 0.52, 0.42], (-4, 4), (0, 1.08), 'position on screen', 'brightness', ticks=False)
    y = np.linspace(-4, 4, 1600); env = np.sinc(y / 1.4) ** 2
    if s == 0:
        ax.plot(y, env, color=GREEN, lw=3.5); ax.fill_between(y, env, color=GREEN, alpha=0.2)
        bullets(fig, ['Wide, bright central band', 'Fainter bands either side', 'Rays from across the slit have\npath differences, so they interfere',
                      'Narrower slit or longer λ → wider'], 4, 0.63, 0.76, size=24, dim=False)
        T(fig, 0.07, 0.17, 'Observational in this course: no calculation needed.', size=24, color=SOFT)
    else:
        ax.plot(y, env * np.cos(np.pi * y / 0.35) ** 2, color=GREEN, lw=2); ax.plot(y, env, color=YELLOW, lw=2.5, ls='--')
        bullets(fig, ['Two slits, real width', 'Each slit also diffracts', 'Double-slit fringes sit inside the\nsingle-slit envelope',
                      'So fringes fade, vanish, then\nfaintly return'], 4, 0.63, 0.76, size=24, dim=False)
        T(fig, 0.07, 0.17, 'dashed line = the single-slit pattern', size=24, color=YELLOW)


def diffraction_uses(fig, s, ph):
    C1, C2 = C()
    if s == 0:
        header(fig, 'Diffraction past a wall')
        ax = wax(fig, [0.04, 0.12, 0.54, 0.68], (0, 12), (0, 8))
        ax.plot([0, 6], [4, 4], color=SOFT, lw=7)
        for yy in (5.2, 6.2, 7.2): ax.plot([0, 12], [yy, yy], color=C1, lw=2.2)
        for r in (0.8, 1.8, 2.8, 3.8):
            ax.add_patch(Arc((6, 4), 2 * r, 2 * r, theta1=180, theta2=360, color=GREEN, lw=2.2))
        ax.add_patch(Polygon([(0, 3.9), (5.9, 3.9), (2.4, 0), (0, 0)], fc='#0a0f18', ec='none', alpha=0.7))
        label(ax, 1.4, 1.5, 'shadow\narea', size=21, color=SOFT)
        bullets(fig, ['Waves bend around the end of the wall', 'Keep λ the same', 'Show the calm shadow area\nthat remains', 'Gap or object similar to λ:\ndiffraction is most obvious'], 4, 0.61, 0.76, size=24, dim=False)
        return
    if s == 1:
        header(fig, 'Diffraction and communication')
        chip(fig, 'Element 4 · predictions')
        for i, (nm, f_, lam, b, c) in enumerate([('900 MHz', r'$\lambda = \dfrac{3.00\times10^{8}}{9.00\times10^{8}} = 0.33\ \mathrm{m}$', '', 'bends around buildings:\nwide coverage from few towers', GREEN),
                                                 ('28 GHz', r'$\lambda = \dfrac{3.00\times10^{8}}{2.8\times10^{10}} = 11\ \mathrm{mm}$', '', 'little diffraction, shadows behind\nbuildings: many small transmitters', PINK)]):
            box(fig, 0.05 + i * 0.46, 0.33, 0.44, 0.47)
            T(fig, 0.07 + i * 0.46, 0.77, nm, size=34, color=c, weight='bold')
            T(fig, 0.07 + i * 0.46, 0.67, f_, size=25)
            T(fig, 0.07 + i * 0.46, 0.51, b, size=24, color=SOFT)
        T(fig, 0.06, 0.25, 'Very long radio waves bend around the curve of the Earth.\nCharged layers high in the atmosphere (the ionosphere) can also reflect radio waves back down.', size=23, color=SOFT)
        return
    header(fig, 'Diffraction and image resolution')
    chip(fig, 'Element 4 · predictions')
    for j, (w_, t_, c) in enumerate([(0.5, 'object ≪ λ: blurred out', PINK), (6.0, 'object ≫ λ: clear edges', GREEN)]):
        ax = gax(fig, [0.07 + j * 0.26, 0.40, 0.22, 0.32], (-4, 4), (0, 1.15), 'position', 'brightness' if j == 0 else '', ticks=False)
        y = np.linspace(-4, 4, 500); edge = np.clip(1 - (np.abs(y) / (w_ / 2 + 0.01)) ** 8, 0, 1) if j else np.exp(-y ** 2 / 3.2) * 0.5
        ax.plot(y, edge, color=c, lw=3.2); ax.set_title(t_, color=c, fontsize=18)
    bullets(fig, ['Diffraction blurs detail about the\nsize of the wavelength', 'Visible light: 400–700 nm\n(EM spectrum on the information sheet)',
                  'A 100 nm virus is too small', 'Shorter λ → finer detail: electrons, X-rays'], 4, 0.61, 0.76, size=23, dim=False)


def polar_string(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Polarisation with a string')
    ax = wax(fig, [0.04, 0.36, 0.92, 0.44], (0, 24), (-3.2, 3.2))
    x = np.linspace(0, 11, 400)
    ax.plot(x, 1.3 * np.sin(TAU * (x / 3 - 2 * ph)), color=C1, lw=3.5, alpha=0.8)
    ax.plot(x, 1.3 * np.sin(TAU * (x / 3 - 2 * ph) + 1.2), color=C2, lw=3.5, alpha=0.8)
    ax.add_patch(Rectangle((11, -3), 0.5, 2.4, fc=SOFT, ec='none')); ax.add_patch(Rectangle((11, 0.6), 0.5, 2.4, fc=SOFT, ec='none'))
    label(ax, 11.25, -3.05, 'vertical slit', size=19, color=SOFT, va='top')
    x = np.linspace(11.5, 23.5, 400); ax.plot(x, 1.3 * np.sin(TAU * (x / 3 - 2 * ph)), color=GREEN, lw=4)
    label(ax, 17.5, 2.2, 'only the vertical oscillation gets through', size=21, color=GREEN)
    bullets(fig, ['A slit acts on a string as a filter acts on light', 'Oscillations across the slit are stopped',
                  'Works for transverse waves only: a sound wave has one oscillation direction, so it can’t be polarised'],
            3, 0.06, 0.32, size=25, dim=False)


def _dots_and_arrows(ax, p, q, nd, na, col):
    """Dots (field parallel to the surface) and arrows (in the plane of the page) on the ray p -> q."""
    p, q = np.array(p), np.array(q); d = (q - p) / np.linalg.norm(q - p); nrm = np.array([-d[1], d[0]])
    arrow(ax, tuple(p), tuple(q), color=col, lw=3)
    tot = nd + na
    for i in range(tot):
        c = p + (q - p) * (i + 0.8) / (tot + 0.8)
        if i % 2 == 0 and nd > 0 and i // 2 < nd or na == 0:
            ax.scatter(*c, s=85, color=FG, zorder=6)
        else:
            darrow(ax, tuple(c - nrm * 0.42), tuple(c + nrm * 0.42), color=FG, ms=10, lw=1.8)


def polar_partial(fig, s, ph):
    C1, C2 = C()
    if s == 0:
        header(fig, 'Partial polarisation: dots and arrows')
        ax = wax(fig, [0.04, 0.12, 0.52, 0.68], (-5, 5), (-4, 4))
        ax.add_patch(Rectangle((-5, -4), 10, 4, fc='#173a5c', ec='none')); ax.plot([-5, 5], [0, 0], color=SOFT, lw=2)
        _dots_and_arrows(ax, (-3.6, 3.8), (-0.05, 0.05), 3, 3, YELLOW)
        _dots_and_arrows(ax, (0, 0), (3.6, 3.8), 5, 1, YELLOW)
        _dots_and_arrows(ax, (0, 0), (2.2, -3.8), 1, 4, YELLOW)
        label(ax, -3.4, 1.8, 'unpolarised:\nequal dots\nand arrows', size=18, color=SOFT); label(ax, 4.5, 1.7, 'reflected:\nmostly dots', size=18, color=SOFT)
        label(ax, -1.6, -2.7, 'refracted:\nmostly arrows', size=18, color=FG)
        bullets(fig, ['Dot: field out of the page,\nparallel to the surface', 'Arrow: field in the page,\nperpendicular to the ray',
                      'Partial: both remain, in\nunequal amounts'], 3, 0.60, 0.76, size=24, dim=False)
        T(fig, 0.60, 0.33, 'Polaroid sunglasses cut surface glare,\nso it is easier to see down into water', size=22, color=SOFT)
        return
    if s == 1:
        header(fig, 'Which surface? Sunglasses and windows')
        chip(fig, 'Element 4 · predictions')
        for i, (nm, b, c) in enumerate([('Water or a road', 'horizontal surface\n→ glare polarised horizontally\n→ vertical-axis lenses block it', GREEN),
                                        ('Shop window', 'vertical surface\n→ reflection polarised vertically\n→ the lenses let it through', PINK)]):
            card(fig, 0.05 + i * 0.46, 0.45, 0.44, 0.33, nm, b, tcol=c, size=25)
        T(fig, 0.06, 0.33, 'Reflected light is polarised parallel to the surface that reflected it.', size=27, color=YELLOW)
        T(fig, 0.06, 0.24, 'Say all three: the direction of the reflection, the direction of the lens axis, and the result.', size=23, color=SOFT)
        return
    header(fig, 'Scattered light through a rotating filter')
    chip(fig, 'Element 4 · predictions')
    ax = gax(fig, [0.07, 0.22, 0.50, 0.50], (0, 180), (0, 1.1), 'filter rotation (degrees)', 'brightness seen', ticks=False)
    a = np.linspace(0, 180, 300)
    ax.plot(a, np.cos(np.radians(a)) ** 2, color=C1, lw=3.5); ax.set_xticks([0, 90, 180]); ax.set_xticklabels(['0', '90', '180'])
    bullets(fig, ['Sunlight scattered through 90°:\nmostly plane polarised', 'Filter lined up with it: brightest', 'Rotated 90°: darkest',
                  'Rotated 180°: bright again,\nthe same as at the start'], 4, 0.62, 0.76, size=24, dim=False)


def more_tips(fig, s, ph):
    C1, C2 = C()
    header(fig, 'More tips from examiners')
    tips = ['No total internal reflection doesn’t\nmean no reflection', 'Closed pipes: justify with the node\nand antinode at the ends',
            'Hanging mass: T = mg,\nnot the mass itself', 'Second overtone of a string is the\nthird harmonic',
            'Name the principle: “superposition”', 'A single slit doesn’t select a colour;\ncoherent doesn’t mean in phase',
            'Draw the normal at every boundary', 'Diffraction sketch: same λ,\nand show the shadow area']
    n = [4, 8][s]
    cols = [C1, C2, PINK, GREEN, YELLOW, C1, C2, PINK]
    for i in range(n):
        x = 0.05 + (i % 2) * 0.46; y = 0.66 - (i // 2) * 0.165
        box(fig, x, y, 0.44, 0.145, fc=PANEL)
        T(fig, x + 0.015, y + 0.0725, str(i + 9), size=36, color=cols[i], weight='bold', va='center')
        T(fig, x + 0.07, y + 0.0725, tips[i], size=21, va='center')
    T(fig, 0.05, 0.13, 'From examiners’ comments in TASC assessment reports', size=18, color=MUT)


def summary(fig, s, ph):
    exam_tips(fig, 4, ph)
