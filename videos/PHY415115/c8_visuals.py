"""Draw functions for PHY415115 Criterion 8 (wave-particle nature of light, atomic and nuclear physics).

Every function has the signature draw(fig, s, ph):
  s  = step index within the scene (the slide builds up as s increases)
  ph = animation phase in [0, 1) for animated steps (Step.anim), 0 for stills.
Animations must loop seamlessly: anything periodic must complete a whole number of
cycles as ph goes 0 -> 1.
Colours: C1 = course accent, C2 = module accent (from the theme), PINK/GREEN/YELLOW are semantic.
"""
import numpy as np
from matplotlib.patches import Circle, Rectangle, Polygon, FancyArrowPatch, Arc, Ellipse

from explainer import layout as L
from explainer.layout import (header, T, bullets, box, card, eq, sheet_eq, learn_eq, chip, wax, gax, darrow, arrow,
                              label, frac, FG, SOFT, MUT, GRID, PANEL, PANEL2, BG, PINK, GREEN, YELLOW, TAU)


def C():
    return L.A1(), L.A2()


def _sheet(section, fig, x, y, s, **kw):
    """sheet_eq with the real section heading: this criterion uses several sections of the sheet."""
    L.ctx['sheet_section'] = section
    return sheet_eq(fig, x, y, s, **kw)


def qeq(fig, x, y, s, **kw):
    return _sheet('Quantum', fig, x, y, s, **kw)


def neq(fig, x, y, s, **kw):
    return _sheet('Nuclear', fig, x, y, s, **kw)


def extend(base, n, *extras):
    """Add steps after a finished scene: steps 0..n-1 use base, later steps use extras in turn."""
    def draw(fig, s, ph):
        if s < n:
            return base(fig, s, ph)
        return extras[s - n](fig, 0, ph)
    return draw


def _lines(fig, x, y, rows, size=26, gap=0.085):
    """Lines of working: (text, colour) from y downwards.  Returns the y below the last line."""
    for st, c in rows:
        T(fig, x, y, st, size=size, color=c)
        y -= gap
    return y


def _sf(fig, x, y, s):
    """The rounded answer, shown under the unrounded one.  On screen only: never narrated."""
    T(fig, x, y, s, size=21, color=GREEN)


# ============================================================================ overview
def _title_art(fig, rect, ph, scale=1):
    """Wave packets: a photon is both a wave and a particle."""
    C1, C2 = C()
    ax = wax(fig, rect, (0, 10), (-1.5, 1.5))
    x = np.linspace(0, 10, 1400)
    for c, a, off, m, lw in [(C1, 1.25, 0.0, 22, 4), (PINK, 0.8, 0.36, 36, 3), (C2, 0.5, 0.68, 58, 2.5)]:
        env = np.exp(7 * (np.cos(TAU * (x / 10 - ph - off)) - 1))
        ax.plot(x, a * env * np.sin(TAU * m * (x / 10 - ph)), color=c, lw=lw * scale, alpha=0.95)


def thumbnail(fig):
    """The title card's look, with fewer and larger words so it reads at small sizes."""
    C1, C2 = C()
    fig.text(0.5, 0.86, 'CRITERION 8', ha='center', va='center', color=C1, fontsize=64, weight='bold')
    fig.text(0.5, 0.63, 'Quantum & nuclear', ha='center', va='center', color=FG, fontsize=130, weight='bold')
    fig.text(0.5, 0.43, 'TASC Physics revision', ha='center', va='center', color=SOFT, fontsize=58)
    _title_art(fig, [0, 0.07, 1, 0.28], 0.15, scale=2.5)


def title_card(fig, s, ph):
    intro(fig, 0, ph)


def overview(fig, s, ph):
    intro(fig, s + 1, ph)


def intro(fig, s, ph):
    C1, C2 = C()
    if s == 0:
        fig.text(0.5, 0.76, 'CRITERION 8', ha='center', color=C1, fontsize=30, weight='bold')
        fig.text(0.5, 0.60, 'Wave-particle nature of light,\natomic and nuclear physics', ha='center', va='center',
                 color=FG, fontsize=62, weight='bold', linespacing=1.15)
        fig.text(0.5, 0.445, 'TASC Physics  PHY415115   ·   revision for class tests and the exam', ha='center',
                 color=SOFT, fontsize=26)
        _title_art(fig, [0, 0.06, 1, 0.28], ph)
        return
    if s == 1:
        header(fig, 'How Criterion 8 is assessed')
        card(fig, 0.05, 0.50, 0.40, 0.25, 'Internal', 'Your teacher: class tests, practicals\nand tasks during the year',
             tcol=GREEN)
        card(fig, 0.05, 0.20, 0.40, 0.25, 'External', 'End-of-year TASC exam:\nSection D is all Criterion 8', tcol=C2)
        tiles = [('≈45 min', 'suggested time'), ('45', 'marks'), ('5–7', 'compulsory questions'),
                 ('Info sheet', '+ approved calculator')]
        for i, (big, small) in enumerate(tiles):
            x = 0.52 + (i % 2) * 0.225; y = 0.50 - (i // 2) * 0.30
            box(fig, x, y, 0.205, 0.25, fc=PANEL2)
            T(fig, x + 0.1025, y + 0.16, big, size=46 if len(big) < 8 else 36, color=YELLOW, weight='bold', ha='center',
              va='center')
            T(fig, x + 0.1025, y + 0.06, small, size=21, color=SOFT, ha='center', va='center')
        T(fig, 0.52, 0.16, 'Section D of the exam (external assessment specifications)', size=18, color=MUT)
        return
    if s == 2:
        header(fig, 'The four elements of Criterion 8')
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
    parts = [('Part 1', 'Light as particles: black bodies, photoelectric effect, X-rays', C1),
             ('Part 2', 'Matter as waves, and the energy levels of atoms', C2),
             ('Part 3', 'Radioactivity, decay equations and half-life', PINK),
             ('Part 4', 'Mass-energy, binding energy, fission, fusion, quarks', GREEN),
             ('Part 5', 'Internal only: relativity, bosons and contexts', YELLOW),
             ('Finish', 'Tests & exam technique, and a one-screen summary', FG)]
    for i, (a, b, c) in enumerate(parts):
        y = 0.73 - i * 0.112
        box(fig, 0.05, y - 0.047, 0.90, 0.094)
        T(fig, 0.07, y, a, size=28, color=c, weight='bold', va='center')
        T(fig, 0.17, y, b, size=27, color=FG, va='center')


# ============================================================================ part 1: black bodies
def _planck(lam_nm, T_):
    lam = lam_nm * 1e-9
    return 1.0 / (lam ** 5 * (np.exp(6.63e-34 * 3e8 / (lam * 1.38e-23 * T_)) - 1))


def _visible(ax, top):
    x = np.linspace(400, 700, 60)
    for a, b in zip(x[:-1], x[1:]):
        ax.fill_between([a, b], 0, top, color=_wl_rgb((a + b) / 2), alpha=0.22, lw=0)


def _wl_rgb(w):
    """Approximate colour of light of wavelength w (nm)."""
    if w < 440: r, g, b = (440 - w) / 60, 0, 1
    elif w < 490: r, g, b = 0, (w - 440) / 50, 1
    elif w < 510: r, g, b = 0, 1, (510 - w) / 20
    elif w < 580: r, g, b = (w - 510) / 70, 1, 0
    elif w < 645: r, g, b = 1, (645 - w) / 65, 0
    else: r, g, b = 1, 0, 0
    return (max(r, 0), max(g, 0), max(b, 0))


def blackbody(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Hot objects and the black body problem')
    ax = gax(fig, [0.07, 0.18, 0.50, 0.58], (0, 3000), (0, 1.15), 'wavelength (nm)', 'intensity', ticks=False)
    ax.set_xticks([0, 1000, 2000, 3000])
    lam = np.linspace(30, 3000, 800)
    n0 = _planck(483.3, 6000.)
    _visible(ax, 1.15)
    for T_, c in [(6000, C1), (5000, C2), (4000, PINK)]:
        ax.plot(lam, _planck(lam, float(T_)) / n0, color=c, lw=3.5)
        pk = 2.90e6 / T_
        ax.text(pk + 190, _planck(pk, float(T_)) / n0 - 0.03, f'{T_} K', color=c, fontsize=19, va='bottom', zorder=6, bbox=dict(fc=PANEL, ec='none', pad=1.5))
    if s >= 1:
        l2 = np.linspace(560, 3000, 300)
        ax.plot(l2, (800 / l2) ** 4 * 0.62, color=YELLOW, lw=3, ls='--')
        ax.text(1150, 1.0, 'classical prediction:\nendless rise at short λ', color=YELLOW, fontsize=19, va='center')
    it = ['Hot objects give a continuous spectrum:\nevery wavelength, not separate lines']
    if s >= 1: it += ['Classical physics could not explain the\nintensity at short wavelengths']
    if s >= 2: it += ['Black body: completely absorbs, and\nemits, all wavelengths (e.g. a cavity\nwith a small hole)',
                      'Planck: energy comes in discrete\npackets. Quantum physics begins']
    bullets(fig, it, len(it), 0.60, 0.77, size=23)


def photon_energy(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Photon energy')
    qeq(fig, 0.07, 0.68, r'$E = hf$', size=52, color=GREEN)
    T(fig, 0.07, 0.56, 'E = photon energy,  f = frequency,  h = Planck’s constant', size=21, color=SOFT)
    qeq(fig, 0.07, 0.43, r'$h = 6.63\times10^{-34}\ \mathrm{J\ s} = 4.14\times10^{-15}\ \mathrm{eV\ s}$', size=30)
    if s >= 1:
        card(fig, 0.05, 0.07, 0.42, 0.22, 'Combine with $c = f\\lambda$',
             'E = hc / λ   so shorter λ, more energy\nhc = 1.24 × 10⁻⁶ eV m', tcol=C2, size=23)
    ax = wax(fig, [0.53, 0.40, 0.43, 0.40], (0, 10), (-3.4, 3.4))
    x = np.linspace(0, 10, 900)
    for y0, ll, c, nm in [(2, 2.2, '#ff3b3b', 'red, 700 nm: 1.77 eV'), (-1.4, 1.26, '#3b8bff', 'violet, 400 nm: 3.11 eV')]:
        env = np.exp(-((x - 5) / 2.6) ** 2)
        ax.plot(x, y0 + 0.8 * env * np.sin(TAU * x / ll), color=c, lw=3.5)
        label(ax, 5, y0 + 1.15, nm, size=21, color=FG)
    if s >= 1:
        chip(fig, 'Element 2 · problems')
        T(fig, 0.54, 0.395, 'Green light, 530 nm:', size=22, color=SOFT)
        T(fig, 0.54, 0.345, r'$E = \dfrac{(6.63\times10^{-34})(3.00\times10^{8})}{530\times10^{-9}} = 3.7528\times10^{-19}\ \mathrm{J}$', size=22)
        _sf(fig, 0.54, 0.26, '= 3.75 × 10⁻¹⁹ J (3 s.f.)')
        T(fig, 0.54, 0.205, 'Same photon, using eV s:  2.3434 eV', size=22)
        _sf(fig, 0.54, 0.16, '= 2.34 eV (3 s.f.)')


def wien(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Peak wavelength and temperature')
    qeq(fig, 0.07, 0.69, r'$\lambda_p T = 2.90\times10^{-3}\ \mathrm{m\ K}$', size=38, color=GREEN)
    bullets(fig, ['This is Wien’s law', 'T must be absolute: kelvin, so add 273 to °C', 'Hotter → shorter peak λ',
                  'Hotter → brighter at every wavelength'], 4, 0.07, 0.57, size=24, dim=False)
    ax = gax(fig, [0.57, 0.38, 0.38, 0.40], (0, 2000), (0, 1.15), 'wavelength (nm)', 'intensity', ticks=False)
    ax.set_xticks([0, 1000, 2000])
    lam = np.linspace(30, 2000, 600)
    n0 = _planck(2.9e6 / 6000, 6000.)
    _visible(ax, 1.15)
    ax.plot(lam, _planck(lam, 6000.) / n0, color=C1, lw=3.5); ax.plot(lam, _planck(lam, 4500.) / n0, color=PINK, lw=3.5)
    ax.text(600, 1.03, 'hotter', color=C1, fontsize=19, va='center', ha='left'); ax.text(1200, 0.28, 'cooler: peak moves right\nand the curve stays below', color=PINK, fontsize=17)
    if s == 1:
        chip(fig, 'Element 2 · problems')
        T(fig, 0.07, 0.31, r'Coffee at 80 °C:  $T = 80 + 273 = 353\ \mathrm{K}$', size=25)
        T(fig, 0.07, 0.235, r'$\lambda_p = \dfrac{2.90\times10^{-3}}{353} = 8.2153\times10^{-6}\ \mathrm{m}$  (infrared)', size=25)
        _sf(fig, 0.07, 0.155, '= 8.2 × 10⁻⁶ m (2 s.f.)')
    if s >= 2:
        chip(fig, 'Element 4 · predictions')
        card(fig, 0.05, 0.07, 0.90, 0.19, 'A peak is not the whole spectrum',
             'A 12 000 K star has λp = 242 nm, in the ultraviolet. It still emits strongly across the visible, with more at the blue end,\nso it looks blue-white. A 3500 K star peaks at 829 nm, just in the infrared, and looks red.',
             tcol=PINK, size=21)


def bb_contexts(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Black bodies in real-world contexts')
    chip(fig, 'Element 4 · predictions')
    panels = [('Same temperature, dimmer?', 'Each square metre emits the same,\nso the dim star must be smaller.\nA strong line in its spectrum means\nplenty of that element.', C1),
              ('Finding people with infrared', 'A body at 37 °C (310 K) peaks near\n9.4 μm. Detection is best when the\nsurroundings are much cooler, so\nthe person stands out.', C2),
              ('Forehead thermometer', 'Sensor range 8–12 μm suits about\n240–360 K. The Sun’s surface at about\n5800 K peaks near 500 nm: well outside\nthe range, so the reading is not valid.', GREEN),
              ('Cold space telescope', 'Light from far galaxies is stretched\nfrom visible into infrared. A warm\ntelescope glows in infrared itself, which\nswamps the signal: so it is cooled.', YELLOW)]
    n = [2, 4][s]
    for i in range(n):
        nm, b, c = panels[i]
        x = 0.05 + (i % 2) * 0.46; y = 0.48 - (i // 2) * 0.35
        card(fig, x, y, 0.44, 0.31, nm, b, tcol=c, size=22)


# ============================================================================ part 1: photoelectric effect
def _phototube(fig, rect, ph, reverse=False, electrons=True, f_label='light'):
    """Curved metal plate, collector wire, and an external circuit."""
    C1, C2 = C()
    ax = wax(fig, rect, (0, 10), (0, 10))
    ax.add_patch(Ellipse((5, 6.2), 7.4, 7.2, fc=PANEL2, ec=SOFT, lw=2))
    ax.add_patch(Arc((5, 6.2), 5.4, 5.2, theta1=100, theta2=260, color=FG, lw=7))
    ax.scatter([5.2], [6.2], s=120, color=YELLOW, zorder=6)
    label(ax, 2.6, 1.6, 'metal plate', size=18, color=FG, ha='left')
    label(ax, 5.5, 7.1, 'collector', size=18, color=YELLOW, ha='left')
    xx = np.linspace(0, 1, 200)
    p0 = np.array([9.8, 9.6]); p1 = np.array([2.9, 7.0])
    d = p1 - p0; n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
    w = 0.22 * np.sin(TAU * (9 * xx - 2 * ph))
    ax.plot(p0[0] + d[0] * xx + n[0] * w, p0[1] + d[1] * xx + n[1] * w, color=C2, lw=2.5)
    label(ax, 7.9, 9.7, f_label, size=18, color=C2, ha='left')
    if electrons:
        for k in range(3):
            t = (ph * 2 + k / 3) % 1
            ax.scatter([2.7 + 2.3 * t], [6.2 + (k - 1) * 1.1 * (1 - t)], s=80, color=C1, zorder=6)
    # circuit
    ax.plot([2.3, 2.3, 8.8, 8.8], [4.3, 0.6, 0.6, 2.0], color=MUT, lw=2)
    ax.plot([5.2, 5.2], [6.2, 2.8], color=MUT, lw=2)
    ax.plot([5.2, 5.2, 8.8, 8.8], [2.8, 2.2, 2.2, 2.0], color=MUT, lw=2)
    ax.add_patch(Circle((7.0, 2.2), 0.55, fc=BG, ec=FG, lw=2)); label(ax, 7.0, 2.2, 'A', size=18)
    ax.add_patch(Rectangle((4.3, 0.15), 1.9, 0.9, fc=BG, ec=FG, lw=2)); label(ax, 5.25, 0.6, 'variable V', size=15)
    if reverse:
        label(ax, 4.65, 3.4, '−', size=28, color=PINK, ha='right', weight='bold')
        label(ax, 2.0, 3.4, '+', size=28, color=GREEN, ha='right', weight='bold')
    return ax


def photoelectric(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The photoelectric effect')
    _phototube(fig, [0.03, 0.10, 0.44, 0.72], ph)
    if s == 0:
        bullets(fig, ['Light ejects electrons from a metal', 'Discovered by Hertz', 'Those electrons form a measurable current',
                      'Classical wave physics got it wrong'], 4, 0.50, 0.76, size=26, dim=False)
    elif s == 1:
        rows = [('Classical prediction', 'What is observed', C2),
                ('Any colour works\nif bright enough', 'No electrons below a threshold\nfrequency, however bright', FG),
                ('Brighter light,\nfaster electrons', 'Brighter: more electrons, same\nmaximum kinetic energy', FG),
                ('Dim light:\na long delay', 'Emission is effectively instant', FG)]
        for i, (a, b, c) in enumerate(rows):
            y = 0.76 - i * 0.145
            if i: box(fig, 0.49, y - 0.11, 0.47, 0.135, fc=PANEL if i % 2 else PANEL2)
            T(fig, 0.50, y - (0.03 if i else -0.01), a, size=20 if i else 22, color=PINK if i else C2, weight='bold' if not i else 'normal', va='top' if not i else 'top')
            T(fig, 0.725, y - (0.03 if i else -0.01), b, size=20 if i else 22, color=GREEN if i else C2, weight='bold' if not i else 'normal')
    else:
        qeq(fig, 0.51, 0.69, r'$E_K(\mathrm{max}) = eV = hf - W$', size=36, color=GREEN)
        bullets(fig, ['One photon gives all its energy to one electron', 'W = work function: least energy to escape the metal',
                      'Threshold: hf₀ = W.  Below f₀, no electrons', 'Intensity = number of photons, not their energy'], 4, 0.50, 0.565,
                size=22, dim=False)
        T(fig, 0.50, 0.21, 'Tip: red fails not because it is dim, but because\neach red photon has too little energy.', size=22, color=YELLOW)


def stopping(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Millikan’s method: stopping voltage')
    _phototube(fig, [0.03, 0.10, 0.44, 0.72], ph, reverse=True, electrons=s < 2)
    if s == 0:
        bullets(fig, ['Collector made NEGATIVE, to repel electrons', 'Raise V until the fastest electron just turns back',
                      'Ammeter then reads exactly zero', 'That V is the stopping voltage'], 4, 0.50, 0.76, size=24, dim=False)
        T(fig, 0.50, 0.42, 'Filters or a spectral lamp supply one\nwavelength at a time. A lamp with known\nspectral lines is more precise than filters.', size=23, color=SOFT)
    if s == 1:
        qeq(fig, 0.51, 0.70, r'$E_K(\mathrm{max}) = eV$', size=40, color=GREEN)
        T(fig, 0.50, 0.57, 'kinetic energy lost = charge × stopping voltage', size=23, color=SOFT)
        card(fig, 0.50, 0.24, 0.46, 0.25, 'The electron-volt', 'Energy gained by one electron across 1 V\n1 eV = 1.60 × 10⁻¹⁹ J\n(eV → J: multiply.  J → eV: divide.)', tcol=C2, size=23)
        T(fig, 0.50, 0.17, 'Stopping voltage 1.3 V  ↔  maximum energy 1.3 eV', size=23, color=YELLOW)
    if s == 2:
        bullets(fig, ['All photons have the same energy, hf', 'Electrons near the surface need just W to escape',
                      'Deeper electrons lose extra energy on the way out', 'So kinetic energies range from 0 up to the maximum'], 4, 0.50, 0.76, size=23, dim=False)
        card(fig, 0.50, 0.26, 0.46, 0.20, 'Careful', 'The photon always gives ALL its energy.\nThe range comes from the electrons.', tcol=PINK, size=23)


def we_photo(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: magnesium')
    chip(fig, 'Element 2 · problems')
    card(fig, 0.05, 0.60, 0.90, 0.20, 'Question', 'Magnesium has a work function of 3.70 eV. Find its threshold frequency and threshold wavelength. For 250 nm\nultraviolet, find the maximum kinetic energy, the stopping voltage and the fastest electron’s speed.', tcol=C2, size=22)
    y = 0.56
    if s >= 0:
        T(fig, 0.06, y, r'$f_0 = \dfrac{W}{h} = \dfrac{3.70}{4.14\times10^{-15}} = 8.9372\times10^{14}\ \mathrm{Hz}$', size=26)
        _sf(fig, 0.06, 0.49, '= 8.94 × 10¹⁴ Hz (3 s.f.)')
        T(fig, 0.56, y, r'$\lambda_0 = \dfrac{c}{f_0} = 335.68\ \mathrm{nm}$', size=26)
        _sf(fig, 0.56, 0.49, '= 336 nm (3 s.f.)')
    if s >= 1:
        T(fig, 0.06, 0.435, r'photon: $E = \dfrac{hc}{\lambda} = \dfrac{1.242\times10^{-6}}{250\times10^{-9}} = 4.968\ \mathrm{eV}$', size=26)
        T(fig, 0.06, 0.345, r'$E_K(\mathrm{max}) = 4.968 - 3.70 = 1.268\ \mathrm{eV}$', size=26)
        _sf(fig, 0.06, 0.30, '= 1.27 eV (3 s.f.)')
        T(fig, 0.56, 0.345, r'stopping voltage $= 1.268\ \mathrm{V}$', size=26)
        _sf(fig, 0.56, 0.30, '= 1.27 V (3 s.f.)')
    if s >= 2:
        T(fig, 0.06, 0.255, r'$1.268\ \mathrm{eV} = 2.0288\times10^{-19}\ \mathrm{J}$    $\Rightarrow$    $v = \sqrt{\dfrac{2E_K}{m_e}} = 6.6738\times10^{5}\ \mathrm{m\ s^{-1}}$', size=25)
        _sf(fig, 0.06, 0.175, '= 6.67 × 10⁵ m s⁻¹ (3 s.f.)')
        T(fig, 0.06, 0.125, 'Check: 250 nm is below the 336 nm threshold wavelength, so electrons are emitted. ½mv² needs joules.', size=21, color=YELLOW)


def pe_graph(fig, s, ph):
    C1, C2 = C()
    if s <= 2:
        header(fig, 'The graph of maximum kinetic energy')
        chip(fig, 'Element 3 · data')
        ax = gax(fig, [0.07, 0.14, 0.50, 0.64], (0, 16), (-5, 4), 'frequency (×10¹⁴ Hz)', r'$E_K(\mathrm{max})$ (eV)')
        ax.set_xticks([0, 4, 8, 12, 16]); ax.set_yticks([-4, -2, 0, 2, 4])
        h = 4.14e-15 * 1e14
        f = np.linspace(0, 16, 100)
        W = 2.2
        y = h * f - W
        ax.plot(f[y >= 0], y[y >= 0], color=C1, lw=4)
        ax.plot(f[y < 0], y[y < 0], color=C1, lw=2.5, ls='--')
        f0 = W / h
        ax.scatter([f0], [0], s=120, color=YELLOW, zorder=5); ax.scatter([0], [-W], s=120, color=PINK, zorder=5, clip_on=False)
        ax.text(f0 - 0.2, 0.45, 'f₀', color=YELLOW, fontsize=24, ha='center'); ax.text(0.5, -W - 0.05, '−W', color=PINK, fontsize=24, va='center')
        if s >= 1:
            W2 = 4.0; y2 = h * f - W2
            ax.plot(f[y2 >= 0], y2[y2 >= 0], color=GREEN, lw=4); ax.plot(f[y2 < 0], y2[y2 < 0], color=GREEN, lw=2.5, ls='--')
            ax.text(14.2, 0.9, 'metal 2', color=GREEN, fontsize=19, ha='left'); ax.text(9.6, 2.75, 'metal 1', color=C1, fontsize=19, ha='right')
        if s == 0:
            bullets(fig, ['Straight line: y = mx + c', 'Gradient = h, for every metal', 'x-intercept = threshold f₀', 'y-intercept = −W',
                          'Gradient needs eV on the y-axis\nto give h in eV s'], 5, 0.60, 0.76, size=24, dim=False)
        if s == 1:
            bullets(fig, ['Larger W: line shifts right', 'SAME gradient: parallel lines', 'Use a ruler, and label the intercept',
                          'Brighter light: same graph\n(only the current grows)'], 4, 0.60, 0.76, size=24, dim=False)
        if s == 2:
            bullets(fig, ['Read f for a given wavelength\nusing f = c / λ', 'Trace up to the line and across', 'e.g. 240 nm: f = 12.5 × 10¹⁴ Hz\nmetal 1: 2.98 eV (3 s.f.)', 'Below f₀: no electrons, not\nnegative energy'], 4, 0.60, 0.76, size=24, dim=False)
        return
    header(fig, 'If the x-axis is wavelength')
    chip(fig, 'Element 3 · data')
    ax = gax(fig, [0.07, 0.14, 0.50, 0.64], (0, 800), (0, 11), 'wavelength (nm)', r'$E_K(\mathrm{max})$ (eV)')
    ax.set_xticks([0, 200, 400, 600, 800])
    for W, c, nm in [(2.2, C1, 'W = 2.2 eV'), (4.0, GREEN, 'W = 4.0 eV')]:
        l0 = 1242 / W
        l = np.linspace(110, l0, 200)
        ax.plot(l, 1242 / l - W, color=c, lw=4); ax.scatter([l0], [0], s=100, color=c, zorder=5, clip_on=False)
        ax.text(l0 + 12, 0.35, f'{int(l0 + 0.5)} nm', color=c, fontsize=19)
    bullets(fig, ['A curve: E = hc/λ − W', 'Never reaches the y-axis:\nit climbs as λ falls', 'Larger W: x-intercept moves left', 'Label the new x-intercept:\nλ₀ = hc / W'], 4, 0.60, 0.76, size=24, dim=False)


def millikan_data(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Using stopping-voltage data')
    chip(fig, 'Element 3 · data')
    rows = [('λ (nm)', 'f (×10¹⁴ Hz)', 'V (V)'), ('500', '6.00', '0.28'), ('400', '7.50', '0.91'), ('300', '10.0', '1.94')]
    for j, r in enumerate(rows):
        y = 0.79 - j * 0.065
        box(fig, 0.05, y - 0.03, 0.40, 0.06, fc=PANEL if j % 2 else PANEL2)
        for k, (x, t) in enumerate(zip((0.08, 0.20, 0.37), r)):
            if k == 1 and s == 0 and j > 0: t = '?'
            T(fig, x, y, t, size=23, color=C2 if j == 0 else FG, va='center', weight='bold' if j == 0 else 'normal')
    if s == 0:
        T(fig, 0.05, 0.42, r'$f = \dfrac{c}{\lambda} = \dfrac{3.00\times10^{8}}{500\times10^{-9}} = 6.00\times10^{14}\ \mathrm{Hz}$', size=25)
        T(fig, 0.05, 0.31, 'Convert nanometres to metres first.', size=23, color=SOFT)
    ax = gax(fig, [0.53, 0.16, 0.42, 0.62], (0, 12), (-2.6, 2.6), 'frequency (×10¹⁴ Hz)', 'stopping voltage (V)')
    ax.set_xticks([0, 2, 4, 6, 8, 10, 12]); ax.set_yticks([-2, -1, 0, 1, 2])
    if s >= 1:
        ax.scatter([6, 7.5, 10], [0.28, 0.91, 1.94], s=120, color=YELLOW, zorder=5)
    if s >= 2:
        f = np.linspace(0, 12, 50); ax.plot(f, 0.415 * f - 2.21, color=C1, lw=3)
        ax.plot([6, 10, 10], [0.28, 0.28, 1.94], color=C2, lw=2, ls='--')
    if s == 1:
        T(fig, 0.05, 0.42, 'Plot with care, on the scale given.\nThen rule one straight line of best fit.', size=24)
        learn_eq(fig, 0.06, 0.25, r'$V = \dfrac{h}{e}f - \dfrac{W}{e}$', size=32)
    if s >= 2:
        learn_eq(fig, 0.06, 0.475, r'$V = \dfrac{h}{e}f - \dfrac{W}{e}$', size=24)
        _lines(fig, 0.05, 0.37, [(r'gradient $= \dfrac{1.94-0.28}{4.00\times10^{14}} = 4.15\times10^{-15}\ \mathrm{V\ s}$', FG),
                                  (r'so $h = 4.15\times10^{-15}\ \mathrm{eV\ s}$ (3 s.f.)', GREEN),
                                  (r'$y$-intercept $\approx -2.2\ \mathrm{V}$, so $W = 2.2\ \mathrm{eV}$ (2 s.f.)', GREEN),
                                  (r'$x$-intercept: $f_0 \approx 5.3\times10^{14}\ \mathrm{Hz}$ (2 s.f.)', GREEN)], size=23, gap=0.068)


# ============================================================================ part 1: X-rays
def _tube(fig, rect, ph):
    C1, C2 = C()
    ax = wax(fig, rect, (0, 12), (0, 8))
    ax.add_patch(Ellipse((6, 4.4), 10.6, 4.6, fc=PANEL2, ec=SOFT, lw=2))
    label(ax, 6, 6.2, 'vacuum', size=17, color=MUT)
    # cathode
    xx = np.linspace(1.6, 2.6, 60); ax.plot(xx, 4.4 + 0.3 * np.sin(TAU * 4 * (xx - 1.6)), color=YELLOW, lw=3)
    label(ax, 3.4, 3.35, 'hot filament\n(cathode −)', size=15, color=YELLOW)
    # anode
    ax.add_patch(Polygon([[8.2, 3.3], [9.6, 3.3], [9.6, 5.4], [8.8, 5.4]], fc=C2, ec=FG, lw=1.5))
    ax.add_patch(Rectangle((9.6, 4.0), 2.0, 0.7, fc=SOFT, ec=FG, lw=1.5))
    label(ax, 7.1, 5.85, 'tungsten anode (+)', size=15, color=C2, ha='left')
    for k in range(5):
        t = (ph * 2 + k / 5) % 1
        ax.scatter([2.8 + 5.6 * t], [4.4 + 0.2 * np.sin(k * 2.1)], s=55, color=C1, zorder=6)
    label(ax, 5.4, 5.0, 'electrons', size=17, color=C1)
    for dx in (-0.2, 0.5):
        p0 = np.array([8.6 + dx, 3.5]); p1 = np.array([7.4 + dx * 1.4, 0.6])
        t = np.linspace(0, 1, 120); d = p1 - p0; n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
        w = 0.14 * np.sin(TAU * (7 * t - 2 * ph))
        ax.plot(p0[0] + d[0] * t + n[0] * w, p0[1] + d[1] * t + n[1] * w, color=PINK, lw=2.2)
    label(ax, 9.0, 1.1, 'X-rays', size=19, color=PINK, ha='left')
    ax.plot([1.0, 1.0, 11.6, 11.6], [4.4, 7.5, 7.5, 4.7], color=MUT, lw=2)
    label(ax, 6, 7.5, ' high voltage: tens of kV ', size=17, color=FG, bbox=dict(fc=BG, ec=MUT, pad=3))
    ax.plot([1.0, 1.6], [4.4, 4.4], color=MUT, lw=2)


def xray_tube(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Producing X-rays')
    _tube(fig, [0.03, 0.14, 0.52, 0.66], ph)
    if s == 0:
        bullets(fig, ['Filament heated by a low-voltage current:\nit releases electrons', 'High voltage accelerates them',
                      'They strike a heavy metal target', 'Most of the energy becomes heat,\nso the anode is cooled'], 4, 0.58, 0.76, size=23, dim=False)
    else:
        learn_eq(fig, 0.60, 0.70, r'$hf_{\mathrm{max}} = eV$', size=42, color=GREEN)
        bullets(fig, ['Einstein: one electron gives ALL its\nenergy to one photon', 'V sets the maximum frequency',
                      'The tube current does not change it:\ncurrent is how many electrons,\nnot how energetic each one is'], 3, 0.58, 0.55, size=23, dim=False)


def _xs(l, V_kV, cur=1.0, lines=True):
    """Illustrative tube spectrum: l in pm, V in kV."""
    lmin = 1242.0 / V_kV
    y = np.where(l > lmin, cur * (l / lmin - 1) / l ** 2 * 1800, 0.0)
    y = y * (1 - np.exp(-((l / 60) ** -3)))
    if lines and V_kV > 20:
        s = cur * (V_kV / 20 - 1) ** 1.2
        y = y + s * 0.85 * np.exp(-((l - 72.6) / 1.1) ** 2) + s * 0.4 * np.exp(-((l - 63.7) / 1.1) ** 2)
    return y


def xray_spectrum(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The X-ray spectrum')
    ax = gax(fig, [0.07, 0.15, 0.50, 0.63], (0, 150), (0, 2.1), 'wavelength (pm)', 'intensity', ticks=False)
    ax.set_xticks([0, 50, 100, 150])
    l = np.linspace(5, 150, 2000)
    ax.text(148, 2.0, 'illustrative shapes, not measured data', color=MUT, fontsize=17, ha='right', va='top')
    ax.plot(l, _xs(l, 35), color=C1, lw=3.5)
    if s == 0:
        ax.annotate('sharp cut-off: λmin', (35.5, 0.02), (6, 0.85), color=YELLOW, fontsize=18, arrowprops=dict(arrowstyle='-|>', color=YELLOW, lw=2))
        ax.text(112, 0.62, 'continuous', color=C1, fontsize=20, ha='center')
        bullets(fig, ['Continuous: electrons pass near nuclei', 'Electric attraction to the nucleus\nswerves them: a large acceleration',
                      'Accelerated charge radiates a photon', 'Sharper swerve, more energy lost', 'Called braking radiation (bremsstrahlung)'], 5, 0.60, 0.76, size=22, dim=False)
    if s == 1:
        ax.annotate('Kβ', (63.7, float(_xs(np.array([63.7]), 35)[0])), (48, 1.2), color=PINK, fontsize=22, arrowprops=dict(arrowstyle='-|>', color=PINK))
        ax.annotate('Kα', (72.6, float(_xs(np.array([72.6]), 35)[0])), (88, 1.3), color=PINK, fontsize=22, arrowprops=dict(arrowstyle='-|>', color=PINK))
        ax.text(112, 0.62, 'continuous', color=C1, fontsize=20, ha='center')
        bullets(fig, ['Characteristic: fixed lines of the target', 'Incoming electron knocks out an inner\natomic electron',
                      'An outer electron falls into the gap,\nemitting one photon', 'K lines: fall to n = 1.  L lines: fall to n = 2',
                      'Different metal → different lines'], 5, 0.60, 0.76, size=22, dim=False)
    if s == 2:
        ax.plot(l, _xs(l, 35, 1.8), color=GREEN, lw=3)
        ax.axvline(35.5, color=YELLOW, lw=1.5, ls=':', ymax=0.3)
        bullets(fig, ['More tube CURRENT', 'More electrons: more X-rays everywhere', 'Same λmin', 'Lines stay at the same wavelengths'], 4, 0.60, 0.76, size=24, dim=False)
        T(fig, 0.60, 0.42, 'green = larger current', size=22, color=GREEN)
    if s == 3:
        l2 = l
        ax.plot(l2, _xs(l2, 50), color=GREEN, lw=3)
        bullets(fig, ['Higher VOLTAGE', 'More energetic electrons:\nλmin moves to shorter wavelengths', 'More energy per electron: the whole\ncurve grows too',
                      'Lines stay at the same wavelengths,\nbut get taller'], 4, 0.60, 0.77, size=22, gap=0.014, dim=False)
        ax.text(148, 1.84, 'green = larger voltage', color=GREEN, fontsize=19, ha='right', va='top')
        T(fig, 0.60, 0.445, 'Too low to eject an inner electron: no lines.', size=20, color=SOFT)
        card(fig, 0.60, 0.13, 0.36, 0.27, 'Marking note', 'The 2023 marking guide says intensity\ndoesn’t rise unless the current does.\nPhysically it does. Give both effects,\neach with a reason.', tcol=PINK, size=20)


def we_xray(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: an 80 kV tube')
    chip(fig, 'Element 2 · problems')
    card(fig, 0.05, 0.62, 0.90, 0.18, 'Question', 'An X-ray tube runs at 80.0 kV. Find the shortest wavelength it produces, and the momentum of that photon.', tcol=C2, size=24)
    T(fig, 0.06, 0.56, r'Electron energy: $eV = (1.60\times10^{-19})(80\times10^{3}) = 1.28\times10^{-14}\ \mathrm{J}$', size=26)
    T(fig, 0.06, 0.46, r'$\lambda_{\mathrm{min}} = \dfrac{hc}{eV} = \dfrac{(6.63\times10^{-34})(3.00\times10^{8})}{1.28\times10^{-14}} = 1.5539\times10^{-11}\ \mathrm{m}$', size=26)
    _sf(fig, 0.06, 0.385, '= 1.55 × 10⁻¹¹ m (3 s.f.)')
    if s == 0:
        T(fig, 0.06, 0.32, 'Quick check in eV: 80.0 keV photon, λ = (1.242 × 10⁻⁶) / (80.0 × 10³) = 1.55 × 10⁻¹¹ m', size=23, color=SOFT)
        T(fig, 0.06, 0.24, 'Use h in J s with joules, and h in eV s with electron-volts.', size=24, color=YELLOW)
    if s >= 1:
        T(fig, 0.06, 0.335, r'$p = \dfrac{h}{\lambda} = \dfrac{6.63\times10^{-34}}{1.5539\times10^{-11}} = 4.2667\times10^{-23}\ \mathrm{kg\ m\ s^{-1}}$', size=26)
        _sf(fig, 0.06, 0.262, '= 4.27 × 10⁻²³ kg m s⁻¹ (3 s.f.)')
        card(fig, 0.05, 0.06, 0.90, 0.15, 'Why most photons are longer', 'Most electrons pass further from a nucleus, or lose energy in stages, so few give up all their energy at once.', tcol=PINK, size=22)


def xray_sketch(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Sketching an X-ray spectrum')
    chip(fig, 'Element 3 · data')
    # energy levels of an illustrative target
    ax = wax(fig, [0.05, 0.14, 0.33, 0.66], (0, 10), (-22, 2))
    for E, n, c in [(0, 'free', MUT), (-0.5, 'n = 3', SOFT), (-2.9, 'n = 2', SOFT), (-20, 'n = 1', FG)]:
        ax.plot([2.2, 9.5], [E, E], color=c, lw=3)
    label(ax, 1.9, 1.0, 'free', size=18, color=MUT, ha='right'); label(ax, 1.9, -0.9, 'n = 3', size=18, color=SOFT, ha='right')
    label(ax, 1.9, -2.9, 'n = 2', size=18, color=SOFT, ha='right'); label(ax, 1.9, -20, 'n = 1', size=18, color=FG, ha='right')
    arrow(ax, (4, -2.9), (4, -19.8), color=PINK); arrow(ax, (7, -0.5), (7, -19.8), color=YELLOW)
    label(ax, 4.3, -11, '17.1 keV', size=19, color=PINK, ha='left'); label(ax, 7.3, -8, '19.5\nkeV', size=19, color=YELLOW, ha='left')
    label(ax, 2.4, -21.4, 'removing an n = 1 electron takes 20 keV', size=15, color=SOFT, ha='left')
    ax2 = gax(fig, [0.45, 0.30, 0.50, 0.48], (0, 120), (0, 2.1), 'wavelength (pm)', 'intensity', ticks=False)
    ax2.set_xticks([0, 40, 80, 120])
    l = np.linspace(5, 120, 2000)
    ax2.plot(l, _xs(l, 35), color=C1, lw=3.5)
    ax2.text(118, 2.0, 'made-up target, illustrative shape', color=MUT, fontsize=17, ha='right', va='top')
    ax2.text(36, 0.1, '35.5', color=YELLOW, fontsize=18, ha='right')
    for w_, c_, ha_, dx in [(63.7, YELLOW, 'right', -1.5), (72.6, PINK, 'left', 1.5)]:
        ax2.text(w_ + dx, float(_xs(np.array([w_]), 35)[0]) + 0.02, f'{w_}', color=c_, fontsize=18, ha=ha_)
    T(fig, 0.45, 0.205, r'$\lambda = \dfrac{1.24\times10^{-6}}{E}$:  17.1 keV → 72.6 pm,  19.5 keV → 63.7 pm,  35 keV → 35.5 pm', size=19)
    T(fig, 0.45, 0.15, 'Each wavelength to 3 s.f.', size=19, color=GREEN)
    T(fig, 0.45, 0.11, 'Label λmin and both lines. Mark the wavelengths you calculated.', size=21, color=YELLOW)


# ============================================================================ part 1: momentum
def photon_momentum(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Photons carry momentum')
    qeq(fig, 0.07, 0.69, r'$p = \dfrac{h}{\lambda}$', size=50, color=GREEN)
    learn_eq(fig, 0.30, 0.69, r'$p = \dfrac{E}{c}$', size=42)
    if s >= 1:
        T(fig, 0.06, 0.53, 'Where it comes from: combine two energy equations', size=25, color=C2, weight='bold')
        _lines(fig, 0.06, 0.47, [(r'$E = mc^2$   and   $E = \dfrac{hc}{\lambda}$', FG),
                                 (r'$\Rightarrow\ mc^2 = \dfrac{hc}{\lambda}$', FG),
                                 (r'$\Rightarrow\ p = mc = \dfrac{h}{\lambda}$', GREEN)], size=27, gap=0.105)
    ax = wax(fig, [0.55, 0.26, 0.41, 0.52], (0, 10), (-3, 3))
    x = np.linspace(0, 6, 300)
    ax.plot(x, 0.7 * np.exp(-((x - 3) / 1.6) ** 2) * np.sin(TAU * (x / 0.8 - 2 * ph)), color=PINK, lw=3.5)
    arrow(ax, (6.0, 0), (7.6, 0), color=PINK)
    ax.add_patch(Rectangle((8.0, -2.2), 0.5, 4.4, fc=SOFT, ec=FG)); label(ax, 5, -2.0, 'photon strikes a surface', size=20, color=SOFT)
    label(ax, 3, 1.3, 'massless, but p ≠ 0', size=21, color=YELLOW)
    T(fig, 0.56, 0.25, 'Photons have no rest mass, yet they\nstill push on what they hit. Use p = h/λ,\nnot p = mv with v = c.', size=20, color=SOFT)
    if s >= 1:
        T(fig, 0.56, 0.135, 'From keV: 50 keV = 8.0 × 10⁻¹⁵ J, so\np = E/c = 2.7 × 10⁻²³ kg m s⁻¹ (2 s.f.)', size=20, color=GREEN)


def laser_force(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: the force of a laser beam')
    chip(fig, 'Element 2 · problems')
    card(fig, 0.05, 0.62, 0.90, 0.18, 'Question', 'A 5.00 mW laser shines 532 nm light onto a surface. How many photons arrive each second?\nWhat force do they exert on a black surface, and on a perfect mirror?', tcol=C2, size=22)
    T(fig, 0.06, 0.56, r'one photon: $E = \dfrac{hc}{\lambda} = 3.7387\times10^{-19}\ \mathrm{J}$', size=26)
    T(fig, 0.47, 0.56, r'photons per second $= \dfrac{5.00\times10^{-3}}{3.7387\times10^{-19}} = 1.3374\times10^{16}$', size=24)
    _sf(fig, 0.47, 0.485, '= 1.34 × 10¹⁶ (3 s.f.)')
    if s >= 1:
        T(fig, 0.06, 0.45, r'one photon: $p = \dfrac{h}{\lambda} = 1.2462\times10^{-27}\ \mathrm{kg\ m\ s^{-1}}$', size=26)
        T(fig, 0.06, 0.365, r'absorbed: $F = \dfrac{\Delta p}{\Delta t} = (1.3374\times10^{16})(1.2462\times10^{-27}) = 1.6667\times10^{-11}\ \mathrm{N}$', size=25)
        _sf(fig, 0.06, 0.295, '= 1.67 × 10⁻¹¹ N (3 s.f.)')
    if s >= 2:
        T(fig, 0.06, 0.245, r'reflected: $\Delta p$ doubles, since $p$ reverses, so $F = 3.3333\times10^{-11}\ \mathrm{N}$', size=25, color=YELLOW)
        _sf(fig, 0.06, 0.195, '= 3.33 × 10⁻¹¹ N (3 s.f.)')
        T(fig, 0.06, 0.135, 'Tiny, but with no air drag it can change a spacecraft’s momentum over months. (Beyond the course: a solar sail.)', size=22, color=SOFT)


def compton(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Compton scattering')
    ax = wax(fig, [0.04, 0.34, 0.52, 0.46], (0, 12), (-4, 4))
    arrow(ax, (0.4, 0), (4.6, 0), color=PINK); label(ax, 2.5, 0.65, 'X-ray, λ', size=22, color=PINK)
    ax.scatter([5.2], [0], s=260, color=C1, zorder=5); label(ax, 5.2, -0.8, 'electron', size=19, color=C1)
    arrow(ax, (5.6, 0.4), (8.6, 3.5), color=YELLOW); label(ax, 9.9, 2.4, 'photon, longer λ′', size=21, color=YELLOW)
    arrow(ax, (5.6, -0.4), (9, -2.3), color=C1); label(ax, 9.9, -3.0, 'recoiling electron', size=21, color=C1)
    ax.plot([5.2, 10], [0, 0], color=MUT, ls='--', lw=1.5)
    bullets(fig, ['An X-ray photon collides with an electron, like a ball', 'Total momentum and energy are conserved',
                  'The photon loses energy: longer wavelength', 'Evidence that light has particle properties'],
            4, 0.06, 0.30, size=23, gap=0.012, dim=False)
    card(fig, 0.59, 0.42, 0.37, 0.38, 'Method', '1. Find p = h/λ before and after\n2. Draw a VECTOR diagram of\n    momentum, not the apparatus\n3. Solve: Pythagoras, or the cosine rule\n4. Find v = p/m if asked', tcol=C2, size=22)
    if s >= 1:
        card(fig, 0.59, 0.09, 0.37, 0.28, 'Traps', 'Label the vectors as momenta\nPut the angle in the right place\nDirection is part of the answer\nUse h in J s here', tcol=PINK, size=22)


def compton90(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: scattering through 90°')
    chip(fig, 'Element 2 · problems')
    card(fig, 0.05, 0.60, 0.50, 0.20, 'Question', 'An X-ray with λ = 2.00 × 10⁻¹¹ m scatters through 90°,\nleaving with λ′ = 2.24 × 10⁻¹¹ m. Find the electron’s\nmomentum, direction and speed.', tcol=C2, size=20)
    T(fig, 0.06, 0.555, r'$p = \dfrac{h}{\lambda} = 3.315\times10^{-23}$', size=23)
    T(fig, 0.27, 0.555, r"$p' = \dfrac{h}{\lambda'} = 2.9598\times10^{-23}$ kg m s⁻¹", size=23)
    ax = wax(fig, [0.59, 0.20, 0.37, 0.60], (-1.4, 6), (-1.2, 5))
    if s >= 1:
        a = 3.315 * 1.2; b = 2.96 * 1.2
        # head to tail: p (before) = p' (photon after) + p_e
        arrow(ax, (0, 0), (a, 0), color=PINK); label(ax, a / 2, -0.45, 'p: photon before', size=19, color=PINK)
        arrow(ax, (0, 0), (0, b), color=YELLOW); label(ax, -0.15, b / 2, "p′\nphoton\nafter", size=18, color=YELLOW, ha='right')
        arrow(ax, (0, b), (a, 0), color=GREEN); label(ax, a / 2 + 0.45, b / 2 + 0.3, 'pₑ', size=26, color=GREEN)
        ax.add_patch(Rectangle((0, 0), 0.3, 0.3, fill=False, ec=SOFT))
        ax.add_patch(Arc((a, 0), 2.0, 2.0, theta1=180 - 41.8, theta2=180, color=C2, lw=2)); label(ax, a - 1.5, 0.42, '41.8°', size=18, color=C2)
        label(ax, 2.2, -1.0, "p = p′ + pₑ (vector sum)", size=20, color=FG)
        T(fig, 0.06, 0.475, r'$p_e = \sqrt{(3.315)^2 + (2.9598)^2}\times10^{-23} = 4.4441\times10^{-23}\ \mathrm{kg\ m\ s^{-1}}$', size=23)
        _sf(fig, 0.06, 0.425, '= 4.44 × 10⁻²³ kg m s⁻¹ (3 s.f.)')
    if s >= 2:
        T(fig, 0.06, 0.38, r'angle: $\tan\theta = 2.9598\,/\,3.315$, so $\theta = 41.76^\circ$ from the original direction', size=23)
        _sf(fig, 0.06, 0.335, '= 41.8° (3 s.f.)')
        T(fig, 0.06, 0.29, r'$v = \dfrac{p_e}{m_e} = \dfrac{4.4441\times10^{-23}}{9.11\times10^{-31}} = 4.8782\times10^{7}\ \mathrm{m\ s^{-1}}$', size=23)
        _sf(fig, 0.06, 0.215, '= 4.88 × 10⁷ m s⁻¹ (3 s.f.)')


def compton180(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a head-on bounce')
    chip(fig, 'Element 2 · problems')
    card(fig, 0.05, 0.62, 0.90, 0.18, 'Question', 'An X-ray with λ = 3.00 × 10⁻¹¹ m, moving east, hits a free electron and bounces straight back\nwith λ′ = 3.485 × 10⁻¹¹ m. Find the speed of the electron.', tcol=C2, size=22)
    T(fig, 0.06, 0.56, r'$p = 2.21\times10^{-23}$ east', size=26, color=PINK); T(fig, 0.38, 0.56, r"$p' = 1.90\times10^{-23}$ WEST", size=26, color=YELLOW)
    T(fig, 0.72, 0.56, 'kg m s⁻¹', size=24, color=SOFT)
    if s >= 1:
        T(fig, 0.06, 0.47, r'Conservation, east positive:  $+2.21 = -1.90 + p_e$', size=26)
        T(fig, 0.06, 0.40, r'$p_e = 4.1124\times10^{-23}\ \mathrm{kg\ m\ s^{-1}}$ east    $\Rightarrow$    $v = 4.5142\times10^{7}\ \mathrm{m\ s^{-1}}$', size=26)
        _sf(fig, 0.06, 0.345, '= 4.11 × 10⁻²³ kg m s⁻¹ east, and 4.51 × 10⁷ m s⁻¹ (3 s.f.)')
        T(fig, 0.06, 0.295, 'Momentum is a vector: the two photon momenta ADD here. State the law you are using.', size=22, color=YELLOW)
    if s >= 2:
        card(fig, 0.05, 0.06, 0.90, 0.19, 'Checking validity (A-standard)', 'Photon energy lost: 6.63 × 10⁻¹⁵ − 5.707 × 10⁻¹⁵ = 9.23 × 10⁻¹⁶ J.   Electron’s ½mv² = 9.28 × 10⁻¹⁶ J.  Close, but not exact.\nv = 0.15c, so ½mv² runs slightly high: it leaves out a small relativistic effect. Say so.', tcol=C2, size=21)


# ============================================================================ part 2: matter waves
def debroglie(fig, s, ph):
    C1, C2 = C()
    header(fig, 'De Broglie: particles are waves too')
    qeq(fig, 0.07, 0.70, r'$p = \dfrac{h}{\lambda}$', size=44, color=GREEN)
    _sheet('Motion…, Momentum, Force', fig, 0.32, 0.70, r'$p = mv$', size=40)
    learn_eq(fig, 0.62, 0.70, r'$\lambda = \dfrac{h}{mv}$', size=44)
    if s >= 1:
        ax = wax(fig, [0.05, 0.27, 0.50, 0.29], (0, 12), (-3, 3))
        ax.plot([6.5, 6.5], [-3, -0.6], color=SOFT, lw=5); ax.plot([6.5, 6.5], [0.6, 3], color=SOFT, lw=5)
        ax.scatter([1], [0], s=90, color=C1)
        arrow(ax, (1.5, 0), (5.8, 0), color=C1); label(ax, 3.6, 0.8, 'electrons', size=20, color=C1)
        for r in (1.2, 2.4, 3.6, 4.8):
            ax.add_patch(Arc((6.5, 0), 2 * r, 2 * r, theta1=-55, theta2=55, color=GREEN, lw=2))
        label(ax, 3.4, -1.7, 'they diffract and\ninterfere', size=20, color=GREEN)
        bullets(fig, ['Electrons diffract through crystals, as X-rays do', 'Needs a gap near λ: about 10⁻¹⁰ m, the spacing of atoms'], 2, 0.05, 0.23, size=23, gap=0.012, dim=False)
    if s >= 2:
        card(fig, 0.58, 0.24, 0.38, 0.28, 'Quantum mechanics', 'Schrödinger turned this into a\nwave equation for the electron.\nQualitative only in this course.', tcol=C2, size=22)


def we_debroglie(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: electron wavelength')
    chip(fig, 'Element 2 · problems')
    card(fig, 0.05, 0.64, 0.90, 0.16, 'Question', 'Electrons are accelerated from rest through 150 V. Find their de Broglie wavelength.', tcol=C2, size=25)
    _lines(fig, 0.06, 0.59, [(r'$E_K = eV = (1.60\times10^{-19})(150) = 2.40\times10^{-17}\ \mathrm{J}$', FG),
                             (r'$\frac{1}{2}mv^2 = E_K\ \Rightarrow\ v = 7.3\times10^{6}\ \mathrm{m\ s^{-1}}$  (2.4% of c: ignore relativity)', FG),
                             (r'$\lambda = \dfrac{h}{mv} = \dfrac{6.63\times10^{-34}}{(9.11\times10^{-31})(7.2587\times10^{6})} = 1.0026\times10^{-10}\ \mathrm{m}$', FG)], size=25, gap=0.085)
    _sf(fig, 0.06, 0.345, '= 1.00 × 10⁻¹⁰ m (3 s.f.)')
    if s >= 1:
        card(fig, 0.05, 0.06, 0.44, 0.235, 'Trap: electron ≠ photon', 'A 150 eV photon has λ = hc/E = 8.28 nm (3 s.f.).\nElectrons don’t travel at c: never\nuse E = hc/λ for an electron.', tcol=PINK, size=21)
        card(fig, 0.51, 0.06, 0.44, 0.235, 'A thrown ball', '0.058 kg at 40 m/s:\nλ = 2.9 × 10⁻³⁴ m (2 s.f.).  Far too small for any\ngap: no wave behaviour can be seen.', tcol=YELLOW, size=21)


def duality(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Wave-particle duality')
    ax = wax(fig, [0.05, 0.47, 0.90, 0.33], (0, 12), (-2.2, 2.6))
    x = np.linspace(0, 12, 2500)
    freq = 0.6 * np.exp(0.33 * x)
    ax.plot(x, 0.9 * np.sin(np.cumsum(freq) * (x[1] - x[0]) * TAU * 0.4), color=C1, lw=2)
    label(ax, 0.9, 1.7, 'radio', size=22, color=C1); label(ax, 11.2, 1.7, 'gamma', size=22, color=PINK)
    arrow(ax, (2.5, 1.7), (9.6, 1.7), color=YELLOW, lw=2.5)
    label(ax, 6, 2.3, 'more momentum and energy → more particle-like', size=22, color=YELLOW)
    label(ax, 2, -1.6, 'very wavelike', size=21, color=C1); label(ax, 10, -1.6, 'very particle-like', size=21, color=PINK)
    bullets(fig, ['EM spectrum on your information sheet: radio to gamma', 'High momentum and energy: particle-like, wavelength too small to show',
                  'Low momentum and energy: wave-like effects are easy to see'], 3, 0.06, 0.44, size=23, gap=0.012, dim=False)
    if s >= 1:
        chip(fig, 'Element 2 · problems')
        card(fig, 0.05, 0.07, 0.90, 0.20, 'Same wavelength, same momentum',
              'An electron at 2.0 × 10⁵ m/s has λ = 3.6 × 10⁻⁹ m and p = 1.8 × 10⁻²⁵ kg m/s (2 s.f.): near UV / X-ray.\nA photon with that λ has exactly the same momentum: p = h/λ holds for both.', tcol=GREEN, size=21)


# ---------------------------------------------------------------------------- spectra
def _rainbow(ax, x0, x1, y0, y1, lmin=380, lmax=720):
    im = np.array([[_wl_rgb(w) for w in np.linspace(lmin, lmax, 340)]])
    ax.imshow(im, extent=(x0, x1, y0, y1), aspect='auto')


H_LINES = (656, 486, 434, 410)


def spectra(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Line spectra')
    ax = wax(fig, [0.05, 0.46, 0.90, 0.34], (380, 720), (0, 11))
    _rainbow(ax, 380, 720, 8.2, 10.4)
    label(ax, 382, 11.1, 'continuous: hot solid', size=20, color=SOFT, ha='left')
    if s >= 0:
        ax.add_patch(Rectangle((380, 4.2), 340, 2.2, fc='black', ec=GRID))
        for w in H_LINES: ax.plot([w, w], [4.2, 6.4], color=_wl_rgb(w), lw=4)
        label(ax, 382, 7.1, 'emission: bright lines on dark (hydrogen)', size=20, color=SOFT, ha='left')
    if s >= 1:
        _rainbow(ax, 380, 720, 0.2, 2.4)
        for w in H_LINES: ax.plot([w, w], [0.2, 2.4], color='black', lw=4)
        label(ax, 382, 3.1, 'absorption: dark lines at the SAME wavelengths', size=20, color=SOFT, ha='left')
    ax.set_xlim(380, 720); ax.set_ylim(0, 11.7)
    it = ['Emission: a low-pressure gas, excited, gives only certain wavelengths']
    if s >= 1: it += ['Absorption: white light through a cool gas loses those same wavelengths']
    if s >= 2: it += ['Each element has its own lines, like a fingerprint',
                      'Classical physics could not explain this: an orbiting electron\nshould radiate continuously and spiral into the nucleus']
    bullets(fig, it, len(it), 0.06, 0.42, size=23, gap=0.012)


def _atom(ax, ph, jump=True):
    C1, C2 = C()
    for r in (1.2, 2.2, 3.2):
        ax.add_patch(Circle((0, 0), r, fill=False, ec=GRID, lw=2))
    ax.add_patch(Circle((0, 0), 0.35, fc=PINK, ec=FG, lw=1.5))
    label(ax, 0, 0, '+', size=20, color=BG, weight='bold')
    a = TAU * ph
    ax.scatter([3.2 * np.cos(a * 2)], [3.2 * np.sin(a * 2)], s=110, color=C1, zorder=5)
    ax.set_aspect('equal')


def bohr(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The Bohr-Rutherford atom')
    ax = wax(fig, [0.04, 0.12, 0.42, 0.68], (-4.6, 4.6), (-4.6, 4.6))
    _atom(ax, ph)
    label(ax, 0, -4.1, 'allowed orbits only, around a tiny nucleus', size=18, color=SOFT)
    bullets(fig, ['Rutherford: small, positive, massive nucleus', 'Bohr: electrons only in certain allowed energy levels',
                  'No radiation while staying in a level'], 3, 0.50, 0.76, size=24, dim=False)
    if s >= 1:
        bullets(fig, ['Fall to a lower level: one photon emitted', 'Rise to a higher level: one photon absorbed'], 2, 0.50, 0.53, size=24, dim=False, mcol=GREEN)
        learn_eq(fig, 0.52, 0.345, r'$hf = E_{\mathrm{high}} - E_{\mathrm{low}}$', size=36, color=GREEN)
        T(fig, 0.50, 0.215, 'Fixed level gaps → fixed photon energies →\na line spectrum', size=23, color=YELLOW)
        arrow(ax, (2.2 * np.cos(0.9), 2.2 * np.sin(0.9)), (1.2 * np.cos(0.9), 1.2 * np.sin(0.9)), color=GREEN, lw=3, ms=18)
        t = np.linspace(0, 1, 120); w = 0.13 * np.sin(TAU * 6 * t)
        ax.plot(1.2 + 2.9 * t + 0.6 * w, 1.7 + 1.6 * t - w, color=YELLOW, lw=2.2)
        label(ax, 3.3, 3.7, 'photon', size=18, color=YELLOW)


LEVELS = [(0.0, 'n = 1  ground'), (2.4, 'n = 2'), (3.6, 'n = 3'), (4.5, 'n = 4')]


def _levels(fig, rect, ion=True):
    ax = wax(fig, rect, (0, 10), (-0.5, 6.9))
    ax.add_patch(Rectangle((1.5, 6.0), 8, 0.8, fc=PANEL2, ec='none'))
    ax.plot([1.5, 9.5], [6, 6], color=FG, lw=2)
    label(ax, 5.5, 6.45, 'ionised: 6.0 eV', size=18, color=SOFT)
    for E, nm in LEVELS:
        ax.plot([1.5, 9.5], [E, E], color=FG, lw=3)
        label(ax, 1.3, E, f'{E:.2f}', size=19, color=SOFT, ha='right')
        label(ax, 9.45, E + 0.22, nm, size=15, color=MUT, ha='right')
    label(ax, 0.1, 6.45, 'eV', size=18, color=SOFT, ha='left')
    return ax


def levels(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Energy-level diagrams')
    ax = _levels(fig, [0.05, 0.10, 0.45, 0.70])
    T(fig, 0.05, 0.095, 'a made-up atom, for illustration', size=18, color=MUT)
    bullets(fig, ['Horizontal lines = allowed energies', 'Exam diagrams often set ground state = 0 eV,\nor measure downward as negatives', 'Only the differences matter'], 3, 0.54, 0.77, size=23, dim=False)
    if s >= 1:
        chip(fig, 'Element 2 · problems')
        arrow(ax, (3, 3.6), (3, 2.4), color=PINK); label(ax, 3.2, 3.0, '1.20 eV', size=18, color=PINK, ha='left')
        arrow(ax, (5, 2.4), (5, 0.03), color=GREEN); label(ax, 5.2, 1.2, '2.40 eV', size=18, color=GREEN, ha='left')
        arrow(ax, (7.2, 4.5), (7.2, 2.4), color=YELLOW); label(ax, 7.4, 3.45, '2.10 eV', size=18, color=YELLOW, ha='left')
        T(fig, 0.54, 0.50, r'$\lambda = \dfrac{hc}{\Delta E} = \dfrac{1.24\times10^{-6}}{\Delta E\ (\mathrm{eV})}$', size=28)
        rows = [('2.40 eV', '517.5 nm', '= 518 nm (3 s.f.)', 'green', GREEN), ('2.10 eV', '591.4 nm', '= 591 nm (3 s.f.)', 'orange', YELLOW),
                ('1.20 eV', '1035 nm', '= 1040 nm (3 s.f.)', 'infrared', PINK)]
        for i, (a, b, r_, c_, col) in enumerate(rows):
            y = 0.37 - i * 0.055
            T(fig, 0.54, y, a, size=20, color=col); T(fig, 0.615, y, b, size=20, color=col); T(fig, 0.70, y, r_, size=20, color=GREEN); T(fig, 0.875, y, c_, size=20, color=col)
    if s >= 2:
        T(fig, 0.54, 0.185, 'Working backwards: given λ, find ΔE, then find\nthe ONE pair of levels with that gap. Name both.', size=22, color=YELLOW)


def regions(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Which part of the spectrum?')
    chip(fig, 'Element 4 · predictions')
    ax = wax(fig, [0.05, 0.54, 0.90, 0.26], (0, 12), (-1.5, 3))
    segs = [(0, 3.2, 'X-rays', PINK), (3.2, 5.6, 'ultraviolet', C2), (5.6, 8.0, '', None), (8.0, 12, 'infrared', C1)]
    for a, b, n, c in segs:
        if c: ax.add_patch(Rectangle((a, 0), b - a, 1.5, fc=PANEL2, ec=c, lw=2)); label(ax, (a + b) / 2, 0.75, n, size=23, color=c)
    im = np.array([[_wl_rgb(w) for w in np.linspace(400, 700, 200)]])
    ax.imshow(im, extent=(5.6, 8.0, 0, 1.5), aspect='auto'); ax.set_xlim(0, 12); ax.set_ylim(-1.5, 3)
    label(ax, 6.8, 2.1, 'visible', size=23)
    for x, t in [(5.6, '400 nm'), (8.0, '700 nm'), (3.2, 'about 10 nm')]:
        label(ax, x, -0.7, t, size=20, color=SOFT)
    arrow(ax, (10.2, 2.4), (1.8, 2.4), color=YELLOW, lw=2)
    label(ax, 3.0, 2.8, 'more energy per photon', size=18, color=YELLOW)
    bullets(fig, ['Look it up: the EM spectrum diagram is on your information sheet', '200 nm is ultraviolet, not X-ray. 776 nm is infrared, not red: 700 nm is the visible limit',
                  'Big drops, to n = 1 in hydrogen: ultraviolet. Middle drops, to n = 2: visible. Small drops, to n = 3: infrared',
                  'Name the region. A colour on its own only works between 400 and 700 nm'], 4, 0.06, 0.50, size=22, gap=0.018, dim=False)


def excitation(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Exciting an atom: photons vs electrons')
    chip(fig, 'Element 4 · predictions')
    ax = _levels(fig, [0.04, 0.10, 0.40, 0.70])
    T(fig, 0.05, 0.095, 'a made-up atom, for illustration', size=18, color=MUT)
    if s == 0:
        arrow(ax, (3, 0.03), (3, 2.4), color=GREEN); label(ax, 3.2, 1.2, '2.4 eV photon\nabsorbed', size=16, color=GREEN, ha='left')
        ax.plot([7, 7], [0, 3.0], color=PINK, lw=3, ls=':'); label(ax, 7.2, 1.6, '3.0 eV photon\npasses through', size=16, color=PINK, ha='left')
        card(fig, 0.47, 0.50, 0.49, 0.30, 'A PHOTON: all or nothing', 'It is absorbed only if its energy EXACTLY\nmatches the gap between two levels.\nOtherwise it passes straight through.', tcol=GREEN, size=23)
    if s == 1:
        arrow(ax, (3, 0.03), (3, 2.4), color=C1); label(ax, 3.2, 1.2, '3.0 eV electron\nraises it to 2.4', size=16, color=C1, ha='left')
        card(fig, 0.47, 0.50, 0.49, 0.30, 'An ELECTRON: gives some energy', 'It can hand over just part of its kinetic\nenergy, then scatter with what remains.\n3.0 eV − 2.4 eV = 0.6 eV left over.', tcol=C1, size=23)
        T(fig, 0.47, 0.42, 'Hot gases and electric discharge excite atoms like this.\nThe scattered electron’s energy is NOT the photon energy.', size=21, color=SOFT)
    if s == 2:
        arrow(ax, (4, 0.03), (4, 6.5), color=YELLOW); label(ax, 4.2, 3.0, 'ionised', size=20, color=YELLOW, ha='left')
        card(fig, 0.47, 0.50, 0.49, 0.30, 'Ionisation: any energy above 6.0 eV', 'A 7.0 eV photon removes the electron\nand leaves it 1.0 eV of kinetic energy.\nHigh-energy photons ionise atoms.', tcol=YELLOW, size=23)
        T(fig, 0.47, 0.42, 'Ionisation energy in joules: 6.0 × 1.60 × 10⁻¹⁹ = 9.6 × 10⁻¹⁹ J (2 s.f.)', size=22, color=GREEN)
    if s == 3:
        arrow(ax, (2.2, 4.5), (2.2, 3.6), color=PINK, ms=16); arrow(ax, (3.2, 4.5), (3.2, 2.4), color=YELLOW, ms=16); arrow(ax, (4.2, 4.5), (4.2, 0.03), color=GREEN, ms=16)
        arrow(ax, (5.3, 3.6), (5.3, 2.4), color=PINK, ms=16); arrow(ax, (6.2, 3.6), (6.2, 0.03), color=C1, ms=16); arrow(ax, (7.1, 2.4), (7.1, 0.03), color=C2, ms=16)
        card(fig, 0.47, 0.50, 0.49, 0.30, 'Coming back down', 'Excited by a 5.0 eV electron, the atom reaches\nn = 4. It can then drop in any steps: six\ndifferent lines are possible from four levels.', tcol=C2, size=23)
        T(fig, 0.47, 0.42, 'Going up: treat it as one jump from the ground state.\nA 10 eV electron can’t make a 10 eV photon here: the largest\nphoton from a bound level has less than 6.0 eV.', size=21, color=YELLOW)
    if s == 0:
        T(fig, 0.47, 0.40, 'Same 3.0 eV, from an electron, gives a different outcome: next.', size=23, color=PINK)


def standing_atom(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Electron standing waves')
    ax = wax(fig, [0.03, 0.16, 0.30, 0.62], (-3.4, 3.4), (-3.4, 3.4)); ax.set_aspect('equal')
    t = np.linspace(0, TAU, 600)
    r = 2.3 + 0.55 * np.cos(4 * t) * np.cos(TAU * ph)
    ax.add_patch(Circle((0, 0), 2.3, fill=False, ec=GRID, lw=2)); ax.plot(r * np.cos(t), r * np.sin(t), color=GREEN, lw=3.5)
    ax.add_patch(Circle((0, 0), 0.25, fc=PINK))
    label(ax, 0, -3.3, 'whole wavelengths fit: allowed', size=17, color=GREEN)
    ax = wax(fig, [0.34, 0.16, 0.30, 0.62], (-3.4, 3.4), (-3.4, 3.4)); ax.set_aspect('equal')
    t = np.linspace(0, TAU * 1, 600)
    r = 2.3 + 0.55 * np.cos(3.5 * t) * np.cos(TAU * ph)
    ax.add_patch(Circle((0, 0), 2.3, fill=False, ec=GRID, lw=2)); ax.plot(r * np.cos(t), r * np.sin(t), color=PINK, lw=3.5)
    ax.add_patch(Circle((0, 0), 0.25, fc=PINK))
    label(ax, 0, -3.3, 'doesn’t join up: not allowed', size=17, color=PINK)
    bullets(fig, ['Link to Criterion 7: only\ncertain standing waves fit', 'Each fit is one allowed level', 'Explains WHY energy is quantised'], 3, 0.66, 0.76, size=22, dim=False)
    if s >= 1:
        T(fig, 0.66, 0.47, 'Qualitative only.', size=23, color=YELLOW)
        T(fig, 0.66, 0.41, 'Modern picture: not a neat\norbit but an electron “cloud”,\nshowing the probability of\nfinding the electron.', size=22, color=SOFT)


# ============================================================================ part 3: radioactivity
def rutherford(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Discovering the nucleus')
    ax = wax(fig, [0.04, 0.14, 0.50, 0.66], (0, 12), (-5, 5))
    ax.add_patch(Rectangle((0.1, -1.1), 1.6, 2.2, fc=PANEL2, ec=SOFT)); label(ax, 0.9, -1.7, 'α source', size=18, color=SOFT, zorder=8, bbox=dict(fc=BG, ec='none', pad=2))
    ax.scatter([6.5] * 7, np.linspace(-3.6, 3.6, 7), s=70, color=PINK, zorder=5)
    for y in (-3.0, -1.8, -0.6, 0.6, 1.8, 3.0):
        off = 0.13 if abs(y) < 1 else 0.03
        sg = np.sign(y) * off
        xx = np.linspace(1.7, 11.8, 100)
        ax.plot(xx, y + sg * (xx > 6.5) * (xx - 6.5), color=C1, lw=1.8)
    ax.plot([1.7, 6.2, 2.0], [0.06, 0.06, 1.6], color=YELLOW, lw=2.5)
    label(ax, 6.5, 4.5, 'gold foil nuclei (not to scale)', size=17, color=PINK)
    label(ax, 3.6, 3.7, 'a very few\nbounce back', size=17, color=YELLOW, zorder=8, bbox=dict(fc=BG, ec='none', pad=2))
    label(ax, 10, -4.1, 'most go straight through', size=17, color=C1)
    bullets(fig, ['Rutherford’s team, 1909: alpha\nparticles fired at thin gold foil', 'Most passed straight through:\nthe atom is mostly empty space',
                  'A few bounced back: a tiny, massive,\npositive nucleus'], 3, 0.57, 0.77, size=24, dim=False)
    if s >= 1:
        card(fig, 0.57, 0.12, 0.39, 0.26, 'Radioactivity', 'An unstable nucleus emits radiation\nspontaneously, changing to a\nmore stable state.', tcol=C2, size=23)


def radiation(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Alpha, beta and gamma')
    cols = [0.05, 0.215, 0.42, 0.635, 0.80]
    head = ['', 'what it is', 'charge', 'stopped by', 'ionising']
    rows = [('α', 'helium nucleus', '+2', 'paper, skin\n(cm of air)', 'strongly', YELLOW),
            ('β', 'fast electron or\npositron', '−1 or +1', 'a few mm\nof aluminium', 'moderately', C1),
            ('γ', 'high-energy\nphoton', '0', 'lead reduces it,\nnever completely', 'weakly', PINK)]
    for x, h_ in zip(cols, head): T(fig, x, 0.79, h_, size=22, color=C2, weight='bold')
    for j, (a, b, c_, d, e, col) in enumerate(rows):
        y = 0.725 - j * 0.115
        box(fig, 0.04, y - 0.10, 0.92, 0.105, fc=PANEL if j % 2 == 0 else PANEL2)
        T(fig, 0.06, y - 0.047, a, size=36, color=col, weight='bold', va='center')
        for x, t in zip(cols[1:], (b, c_, d, e)):
            T(fig, x, y - 0.047, t, size=21, va='center')
    if s >= 1:
        bullets(fig, ['Alpha is mostly from large nuclei: too many nucleons', 'Beta minus: a neutron becomes a proton', 'Beta plus: a proton becomes a neutron'], 3, 0.06, 0.36, size=24, gap=0.012, dim=False)
    if s >= 2:
        chip(fig, 'Element 4 · predictions')
        card(fig, 0.55, 0.07, 0.41, 0.29, 'Which one finds a lost source?', 'Gamma: long range and it ionises\nso detectors see it. Beta’s range in air\nis short; neutrinos barely interact.\nHeavier doesn’t mean more penetrating.', tcol=YELLOW, size=20)


def particles(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The other particles')
    data = [('Neutron', r'$^{1}_{0}n$', 'no charge, about the mass of a proton\nfound in nuclei, released in fission', C1),
            ('Positron', r'$^{0}_{+1}e$', 'like an electron, with positive charge\nemitted in beta-plus decay', YELLOW),
            ('Neutrino', r'$^{0}_{0}\nu$', 'zero charge, very tiny mass, very fast\nemitted with beta-plus decay', GREEN),
            ('Antineutrino', r'$^{0}_{0}\bar{\nu}$', 'the neutrino’s antiparticle\nemitted with beta-minus decay', PINK)]
    n = [2, 4, 4][s]
    for i in range(n):
        nm, sym, b, c = data[i]
        x = 0.05 + (i % 2) * 0.46; y = 0.58 - (i // 2) * 0.235
        box(fig, x, y, 0.44, 0.215)
        T(fig, x + 0.018, y + 0.185, nm, size=27, color=c, weight='bold')
        T(fig, x + 0.33, y + 0.185, sym, size=32, color=FG)
        T(fig, x + 0.018, y + 0.12, b, size=21, color=SOFT)
    if s >= 2:
        chip(fig, 'Element 2 · problems')
        T(fig, 0.05, 0.20, r'Annihilation: $e^+ + e^- \to 2\gamma$.   Each γ carries at least $0.000549\ \mathrm{u}\times931\ \mathrm{MeV\ u^{-1}} = 0.5111\ \mathrm{MeV}$', size=25)
        _sf(fig, 0.05, 0.145, '= 0.511 MeV (3 s.f.)')


def background(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Activity and background radiation')
    card(fig, 0.05, 0.56, 0.42, 0.24, 'Activity, A', 'Decays per second, in becquerel (Bq).\n1 Bq = 1 decay each second.', tcol=C2, size=24)
    card(fig, 0.05, 0.27, 0.42, 0.25, 'Background radiation', 'Ionising radiation not from your source:\nrocks and soil, radon gas, cosmic rays,\nfood, and medical uses.', tcol=C1, size=23)
    if s >= 1:
        chip(fig, 'Element 4 · predictions')
        T(fig, 0.51, 0.79, 'Would a detector notice a weak sample?', size=26, color=YELLOW, weight='bold')
        _lines(fig, 0.51, 0.72, [('Sample activity: 20 Bq = 1200 decays per minute', FG), ('Background count: about 24 counts per minute', FG),
                                 ('Radiation spreads out, so most misses the tube', SOFT),
                                 ('If it catches 1%: about 12 counts per minute', FG)], size=23, gap=0.065)
        T(fig, 0.51, 0.44, 'Only a small rise above 24, so hard to notice\nwithout a long count.', size=24, color=GREEN)
        T(fig, 0.51, 0.33, 'Count rate is not activity: the detector records\nonly some of the decays.', size=24, color=PINK)
        T(fig, 0.05, 0.20, 'In experiments: subtract the background first.', size=23, color=SOFT)


def isotopes(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Isotopes and notation')
    fig.text(0.10, 0.60, r'$^{A}_{Z}\mathrm{X}$', fontsize=90, color=YELLOW, va='center')
    T(fig, 0.05, 0.42, 'A = mass number: protons + neutrons (nucleons)\nZ = atomic number: protons\nA − Z = neutrons', size=23)
    bullets(fig, ['Isotopes: same Z, different number of neutrons', r'e.g.  $^{12}_{6}\mathrm{C}$  and  $^{14}_{6}\mathrm{C}$', 'Radioisotope: an unstable isotope, which decays',
                  'Atomic mass unit u (or dalton): 1/12 the\nmass of a carbon-12 atom'], 4, 0.50, 0.77, size=25, dim=False)
    neq(fig, 0.51, 0.335, r'$m_p = 1.007276\ \mathrm{u}$', size=25)
    neq(fig, 0.745, 0.335, r'$m_n = 1.008665\ \mathrm{u}$', size=25)
    T(fig, 0.51, 0.215, r'and $m_e = 0.000549\ \mathrm{u}$, in the same section', size=23, color=SOFT)


def equations(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Writing decay equations')
    chip(fig, 'Element 1 · principles')
    rows = [('α', r'$^{241}_{95}\mathrm{Am}\ \to\ ^{237}_{93}\mathrm{Np}\ +\ ^{4}_{2}\mathrm{He}$', 'no neutrino in alpha decay', YELLOW),
            ('β⁻', r'$^{90}_{38}\mathrm{Sr}\ \to\ ^{90}_{39}\mathrm{Y}\ +\ ^{0}_{-1}e\ +\ ^{0}_{0}\bar{\nu}$', 'n → p: Z rises, antineutrino', C1),
            ('β⁺', r'$^{18}_{9}\mathrm{F}\ \to\ ^{18}_{8}\mathrm{O}\ +\ ^{0}_{+1}e\ +\ ^{0}_{0}\nu$', 'p → n: Z falls, neutrino', GREEN),
            ('γ', r'$^{99m}_{43}\mathrm{Tc}\ \to\ ^{99}_{43}\mathrm{Tc}\ +\ \gamma$', 'metastable: A and Z don’t change', PINK)]
    n = [1, 3, 4, 4][s]
    for i in range(n):
        a, e, note, c = rows[i]
        y = 0.73 - i * 0.135
        box(fig, 0.05, y - 0.06, 0.90, 0.12, fc=PANEL if i % 2 == 0 else PANEL2)
        T(fig, 0.07, y, a, size=34, color=c, weight='bold', va='center')
        T(fig, 0.15, y, e, size=30, va='center')
        T(fig, 0.62, y, note, size=22, color=SOFT, va='center')
    if s == 0:
        bullets(fig, ['Parent nucleus → daughter nucleus + radiation: a transmutation', 'A and Z must each balance on both sides'], 2, 0.06, 0.53, size=25, dim=False)
    if s >= 3:
        T(fig, 0.06, 0.20, 'Common errors: leaving out the neutrino or antineutrino · an equals sign instead of an arrow · unbalanced\nnumbers · labelling a positron as a neutron · writing X without A and Z · quoting a half-life formula instead.', size=22, color=PINK)


def series(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Decay series')
    ax = gax(fig, [0.07, 0.15, 0.50, 0.63], (81, 90), (211, 228), 'atomic number Z', 'mass number A')
    ax.set_xticks(range(82, 90)); ax.set_yticks([214, 218, 222, 226])
    pts = [(88, 226, 'Ra'), (86, 222, 'Rn'), (84, 218, 'Po'), (82, 214, 'Pb'), (83, 214, 'Bi'), (84, 214, 'Po')]
    for a, b in zip(pts[:-1], pts[1:]):
        col = YELLOW if b[1] != a[1] else C1
        arrow(ax, (a[0], a[1]), (b[0], b[1]), color=col, lw=3, ms=20, shrinkA=18, shrinkB=18)
    for z, a_, n in pts:
        ax.scatter([z], [a_], s=1100, color=PANEL2, edgecolor=FG, zorder=5)
        ax.text(z, a_, n, color=FG, fontsize=17, ha='center', va='center', zorder=6)
    bullets(fig, ['One daughter may itself be unstable', 'Each decay in the chain: a new element', 'Alpha: A falls by 4, Z falls by 2', 'Beta minus: A same, Z rises by 1',
                  'The chain ends on a stable isotope'], 5, 0.60, 0.76, size=24, dim=False)
    T(fig, 0.60, 0.35, 'yellow = alpha,  blue = beta minus', size=22, color=SOFT)
    T(fig, 0.60, 0.28, 'Gamma may follow as the new nucleus\nsettles. A daughter with no gamma has\nalready reached its stable state.', size=22, color=SOFT)


def halflife(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Half-life and activity')
    ax = gax(fig, [0.07, 0.15, 0.42, 0.63], (0, 5), (0, 1.1), 'time (half-lives)', 'A / A₀ or N / N₀', ticks=False)
    ax.set_xticks(range(6)); ax.set_yticks([0, 0.125, 0.25, 0.5, 1]); ax.set_yticklabels(['0', '⅛', '¼', '½', '1'])
    t = np.linspace(0, 5, 200); ax.plot(t, 2 ** -t, color=C1, lw=4)
    for k in range(1, 4):
        ax.plot([k, k, 0], [0, 2.0 ** -k, 2.0 ** -k], color=C2, ls='--', lw=1.5)
    T(fig, 0.53, 0.805, 'Half-life: time for half of the nuclei to decay', size=23)
    neq(fig, 0.53, 0.665, r'$-\dfrac{dN}{dt} = \lambda N = A$', size=31, color=GREEN)
    neq(fig, 0.79, 0.665, r'$\lambda = \dfrac{0.693}{T_{1/2}}$', size=31)
    if s >= 1:
        neq(fig, 0.53, 0.47, r'$\dfrac{N}{N_0} = e^{-\lambda t} = \dfrac{A}{A_0} = \dfrac{\mathrm{Count\ Rate}}{\mathrm{Orig\ Count\ Rate}}$', size=26, color=GREEN)
    if s >= 2:
        learn_eq(fig, 0.53, 0.30, r'$\dfrac{N}{N_0} = \dfrac{m}{m_0} = 2^{-t/T_{1/2}}$', size=27)
        neq(fig, 0.78, 0.30, r'$N = \dfrac{mN_A}{M}$', size=23)
        T(fig, 0.53, 0.165, 'm in grams here.  λ is the decay constant: don’t\nconfuse it with wavelength.', size=21, color=YELLOW)


def we_activity(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a medical isotope')
    chip(fig, 'Element 2 · problems')
    card(fig, 0.05, 0.62, 0.90, 0.18, 'Question', 'Iodine-131 has a half-life of 8.02 days. A sample has an activity of 5.0 MBq. How many atoms does it contain,\nand what is its mass? What is its activity 20.0 days later, and what was it 10.0 days earlier?', tcol=C2, size=22)
    T(fig, 0.06, 0.56, r'$\lambda = \dfrac{0.693}{8.02\times24\times3600\ \mathrm{s}} = 1.0001\times10^{-6}\ \mathrm{s^{-1}}$', size=25)
    T(fig, 0.55, 0.56, r'$N = \dfrac{A}{\lambda} = 4.9995\times10^{12}$ atoms', size=25)
    _sf(fig, 0.55, 0.495, '= 5.0 × 10¹² atoms (2 s.f.)')
    if s >= 1:
        T(fig, 0.06, 0.475, r'$m = \dfrac{NM}{N_A} = \dfrac{(4.9995\times10^{12})(131)}{6.02\times10^{23}} = 1.0879\times10^{-9}\ \mathrm{g}$', size=24)
        _sf(fig, 0.06, 0.405, '= 1.1 × 10⁻⁹ g (2 s.f.)')
        T(fig, 0.55, 0.43, 'A becquerel is per SECOND,\nso λ must be in s⁻¹ for N.', size=23, color=YELLOW)
    if s >= 2:
        T(fig, 0.06, 0.335, r'$\lambda t = \dfrac{0.693\times20.0}{8.02} = 1.728$   (days cancel)    $A = 5.0\,e^{-1.728} = 0.8880\ \mathrm{MBq}$', size=24)
        _sf(fig, 0.06, 0.27, '= 0.89 MBq (2 s.f.)')
        T(fig, 0.06, 0.23, r'Earlier: $A_0 = A\,e^{+\lambda t} = 5.0\,e^{+0.864} = 11.864\ \mathrm{MBq}$   (more than now, as it should be)', size=24)
        _sf(fig, 0.06, 0.18, '= 12 MBq (2 s.f.)')
        T(fig, 0.06, 0.13, 'Check: 20.0 days is about 2.5 half-lives, so about 18% should remain. 0.89 / 5.0 = 18% ✓', size=23, color=YELLOW)


def we_age(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Finding a time: natural logs')
    chip(fig, 'Element 2 · problems')
    card(fig, 0.05, 0.62, 0.90, 0.18, 'Question', 'Old wood has 40% of the carbon-14 activity of living wood (half-life 5730 years). How old is it?', tcol=C2, size=24)
    _lines(fig, 0.06, 0.56, [(r'$0.40 = e^{-\lambda t}\ \ \Rightarrow\ \ \ln(0.40) = -\lambda t$', FG),
                             (r'$\lambda = \dfrac{0.693}{5730} = 1.2094\times10^{-4}\ \mathrm{y^{-1}}$', FG),
                             (r'$t = \dfrac{0.9163}{1.2094\times10^{-4}} = 7576$ years', FG)], size=25, gap=0.09)
    _sf(fig, 0.06, 0.315, '= 7600 years (2 s.f.)')
    if s >= 1:
        card(fig, 0.05, 0.06, 0.44, 0.215, 'Percentages', '“73% less” means 27% remains.\nA fraction: divide by 100 first.\ne.g. 0.50% of 3.0 g is 0.015 g.', tcol=PINK, size=21)
        card(fig, 0.51, 0.06, 0.44, 0.215, 'Two decay routes', 'If a nucleus can decay in two ways,\nuse the half-life for the route the\nquestion asks about.', tcol=YELLOW, size=21)
        T(fig, 0.55, 0.53, 'Back in time: an isotope now 2.0% of an\nelement, half-life 1.0 × 10⁹ y. Two half-lives ago,\nwith the other isotopes unchanged:', size=22, color=SOFT)
        T(fig, 0.55, 0.40, r'$2.0\,e^{+\lambda t} = 2.0\,e^{+1.386} = 7.998\%$', size=26)
        _sf(fig, 0.55, 0.345, '= 8.0% (2 s.f.)')


def we_power(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Worked example: a nuclear battery')
    chip(fig, 'Element 4 · predictions')
    card(fig, 0.05, 0.62, 0.90, 0.18, 'Question', 'A deep-space probe needs 0.50 W of electrical power from americium-241 (half-life 432 y, 5.6 MeV per decay),\nat 5.0% efficiency. Why not use solar panels? How much americium does it need?', tcol=C2, size=22)
    T(fig, 0.06, 0.56, 'Far from the Sun, sunlight’s intensity falls with the square of distance: too weak.', size=24, color=SOFT)
    T(fig, 0.06, 0.49, r'Total power: $\dfrac{0.50}{0.050} = 10\ \mathrm{W}$', size=25)
    if s >= 1:
        T(fig, 0.42, 0.49, r'one decay: $5.6\times10^{6}\times1.60\times10^{-19} = 8.96\times10^{-13}\ \mathrm{J}$', size=25)
        T(fig, 0.06, 0.38, r'decays per second: $A = \dfrac{10}{8.96\times10^{-13}} = 1.1161\times10^{13}\ \mathrm{Bq}$', size=25)
        _sf(fig, 0.60, 0.375, '= 1.1 × 10¹³ Bq (2 s.f.)')
    if s >= 2:
        T(fig, 0.06, 0.295, r'$\lambda = \dfrac{0.693}{432\times365\times24\times3600} = 5.0868\times10^{-11}\ \mathrm{s^{-1}}$,   $N = \dfrac{A}{\lambda} = 2.1941\times10^{23}$', size=24)
        T(fig, 0.06, 0.205, r'$m = \dfrac{NM}{N_A} = \dfrac{(2.1941\times10^{23})(241)}{6.02\times10^{23}} = 87.84\ \mathrm{g}$', size=24)
        _sf(fig, 0.06, 0.135, '= 88 g (2 s.f.)')
        T(fig, 0.56, 0.20, 'Over 70 years, m/m₀ = e^(−λt) = 0.89.\nThe formula gives grams: that is 0.088 kg.', size=21, color=YELLOW)


def decay_data(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Half-life from experimental data')
    chip(fig, 'Element 3 · data')
    rows = [('t (min)', 'counts/min', 'net'), ('0', '430', '400'), ('2', '313', '283'), ('4', '230', '200'), ('6', '171', '141'), ('8', '130', '100')]
    for j, r in enumerate(rows):
        y = 0.75 - j * 0.066
        box(fig, 0.05, y - 0.03, 0.34, 0.06, fc=PANEL if j % 2 else PANEL2)
        for k, (x, t) in enumerate(zip((0.075, 0.17, 0.32), r)):
            if k == 2 and s == 0 and j > 0: t = ''
            T(fig, x, y, t, size=22, va='center', color=C2 if j == 0 else (GREEN if k == 2 else FG), weight='bold' if j == 0 else 'normal')
    T(fig, 0.05, 0.33, 'Background: 30 counts/min.\nSubtract it from every reading.', size=23, color=YELLOW)
    ax = gax(fig, [0.47, 0.17, 0.48, 0.61], (0, 10), (0, 450), 'time (min)', 'net count rate (counts/min)')
    tt = np.array([0, 2, 4, 6, 8.]); net = np.array([400, 283, 200, 141, 100.])
    if s >= 1:
        t = np.linspace(0, 10, 200); ax.plot(t, 400 * 2 ** (-t / 4), color=C1, lw=3)
        ax.scatter(tt, net, s=110, color=YELLOW, zorder=5)
        ax.plot([0, 4, 4], [200, 200, 0], color=C2, ls='--', lw=2); ax.plot([0, 8, 8], [100, 100, 0], color=C2, ls='--', lw=2)
        T(fig, 0.05, 0.245, r'400 → 200 takes 4.0 min;  200 → 100 takes 4.0 more', size=19, color=SOFT)
        T(fig, 0.05, 0.19, r'$T_{1/2} = 4.0\ \mathrm{min}$,  $\lambda = \dfrac{0.693}{4.0} = 0.1733\ \mathrm{min^{-1}}$', size=23)
        _sf(fig, 0.05, 0.12, '= 0.17 min⁻¹ (2 s.f.)')


# ============================================================================ part 4: mass and energy
def emc2(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Mass-energy equivalence')
    neq(fig, 0.07, 0.68, r'$E = mc^2$', size=50, color=GREEN)
    neq(fig, 0.42, 0.68, r'$931\ \mathrm{MeV} = 1\ \mathrm{u}$', size=38)
    bullets(fig, ['Mass and energy are equivalent. Mass-energy is conserved in every reaction', 'Use E = mc² with kg and joules',
                  'Use × 931 with u and MeV.  Multiply: don’t divide'], 3, 0.06, 0.53, size=25, dim=False)
    if s >= 1:
        chip(fig, 'Element 2 · problems')
        card(fig, 0.05, 0.07, 0.90, 0.22, 'A star radiating 1.2 × 10²⁷ W', 'Each second:  m = E/c² = (1.2 × 10²⁷)/(3.00 × 10⁸)² = 1.3 × 10¹⁰ kg (2 s.f.) lost as radiation.\nA star losing mass this fast compared with the Sun uses up its fuel sooner: expect a shorter life.', tcol=GREEN, size=23)


def _ball_cluster(ax, cx, cy, n, r, seed=1):
    rng = np.random.RandomState(seed)
    for i in range(n):
        a = rng.uniform(0, TAU); d = r * np.sqrt(rng.uniform(0, 1))
        ax.scatter([cx + d * np.cos(a)], [cy + d * np.sin(a)], s=170, color=PINK if i % 2 else C()[0], edgecolor=BG, zorder=4)


def binding(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Mass defect and binding energy')
    ax = wax(fig, [0.04, 0.42, 0.46, 0.38], (0, 12), (0, 7))
    for k in range(6):
        ax.scatter([0.9 + k * 0.75], [5.8 - (k % 2) * 0.8], s=170, color=PINK if k % 2 else C1, edgecolor=BG)
    label(ax, 2.7, 3.9, 'separate nucleons:\nmore mass', size=19, color=FG)
    arrow(ax, (5.2, 5.2), (7.5, 5.2), color=YELLOW); label(ax, 6.35, 5.9, 'energy out', size=18, color=YELLOW)
    arrow(ax, (7.5, 4.2), (5.2, 4.2), color=GREEN); label(ax, 6.35, 3.5, 'energy in', size=18, color=GREEN)
    _ball_cluster(ax, 9.5, 5.2, 6, 0.45)
    label(ax, 9.5, 3.9, 'nucleus:\nless mass', size=19, color=FG)
    bullets(fig, ['Mass defect: mass of parts − mass of the whole', 'Binding energy: energy to separate it completely', 'It is NOT energy stored in the nucleus'], 3, 0.05, 0.40, size=23, gap=0.012, dim=False)
    chip(fig, 'Element 2 · problems')
    card(fig, 0.53, 0.60, 0.42, 0.20, 'Example', 'Nickel-62 atom (Z = 28) has a mass of\n61.928345 u. Find its binding energy per nucleon.\n(Mass: reference data, not from TASC.)', tcol=C2, size=20)
    if s >= 1:
        _lines(fig, 0.54, 0.565, [('parts:  28(1.007276 + 0.000549) + 34(1.008665)', FG), ('          = 62.513710 u', FG),
                                 ('Δm = 62.513710 − 61.928345 = 0.585365 u', GREEN)], size=20, gap=0.04)
    if s >= 2:
        _lines(fig, 0.54, 0.445, [('BE = 0.585365 × 931 = 544.97 MeV', FG), ('= 545 MeV (3 s.f.)', GREEN), ('per nucleon = 544.97 / 62 = 8.7899 MeV', FG), ('= 8.79 MeV per nucleon (3 s.f.)', GREEN)], size=20, gap=0.036)
        card(fig, 0.53, 0.07, 0.42, 0.22, 'Common errors', 'Converting the whole atom’s mass to energy\nAssuming the parts add to exactly 62 u\nDividing by Z or by 931, not by A', tcol=PINK, size=20)
        T(fig, 0.05, 0.15, 'A quoted atomic mass includes electrons, so add\nZ electrons. If it is the nucleus only, leave them out.', size=21, color=YELLOW)


BE_DATA = [(2, 1.11), (3, 2.57), (4, 7.07), (6, 5.33), (7, 5.61), (9, 6.46), (12, 7.68), (16, 7.98), (20, 8.03), (28, 8.45), (40, 8.55),
           (56, 8.79), (62, 8.79), (84, 8.72), (100, 8.6), (120, 8.5), (138, 8.39), (160, 8.2), (184, 7.98), (208, 7.87), (235, 7.59), (238, 7.57)]


def be_curve(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The binding energy per nucleon curve')
    ax = gax(fig, [0.07, 0.15, 0.53, 0.63], (0, 250), (0, 10.5), 'mass number A', 'BE per nucleon (MeV)')
    A, B = zip(*BE_DATA)
    ax.plot(A, B, color=C1, lw=3.5)
    ax.text(245, 0.35, 'approximate reference values, not from TASC', color=MUT, fontsize=17, ha='right')
    ax.scatter([56], [8.79], s=130, color=YELLOW, zorder=5); ax.text(56, 9.25, 'iron-56 region: most stable', color=YELLOW, fontsize=18, ha='left')
    for (a_, b_, n) in [(4, 7.07, 'He-4'), (235, 7.59, 'U-235')]:
        ax.scatter([a_], [b_], s=80, color=FG, zorder=5); ax.text(a_ + (6 if a_ < 100 else -2), b_ - 0.65, n, color=FG, fontsize=17, ha='left' if a_ < 100 else 'center')
    if s >= 1:
        arrow(ax, (7, 3.5), (40, 7.4), color=GREEN); ax.text(30, 4.4, 'FUSION\nreleases energy', color=GREEN, fontsize=19)
        arrow(ax, (225, 6.5), (120, 7.6), color=PINK); ax.text(150, 5.0, 'FISSION\nreleases energy', color=PINK, fontsize=19)
    it = ['Higher on the curve: more tightly\nbound, more stable', 'Peak near iron-56']
    if s >= 1: it += ['Energy is released by moving UP the curve:\nfrom either side, towards the peak',
                      'Products have more BE than the reactants\nhad, so mass drops, and energy comes out']
    if s >= 2: it += ['Near iron: either direction goes downhill,\nso energy must be put in. Fusion beyond\niron can’t sustain itself in stars']
    bullets(fig, it, len(it), 0.63, 0.78, size=20, gap=0.014, dim=False)


def reaction_energy(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Energy from a mass difference')
    chip(fig, 'Element 2 · problems')
    T(fig, 0.60, 0.785, 'Masses: reference data, not from TASC', size=18, color=MUT)
    T(fig, 0.06, 0.78, r'Fusion:  $^{2}_{1}\mathrm{H} + ^{3}_{1}\mathrm{H}\ \to\ ^{4}_{2}\mathrm{He} + ^{1}_{0}n$', size=28, color=C2)
    _lines(fig, 0.06, 0.70, [('before: 2.013553 + 3.015501 = 5.029054 u   (nuclear masses)', FG),
                             ('after:  4.001506 + 1.008665 = 5.010171 u', FG),
                             ('Δm = 0.018883 u    E = 0.018883 × 931 = 17.580 MeV released', FG),
                             ('= 17.6 MeV (3 s.f.)', GREEN)], size=23, gap=0.046)
    if s >= 1:
        T(fig, 0.06, 0.515, r'Fission:  $^{235}_{92}\mathrm{U} + ^{1}_{0}n\ \to\ ^{141}_{56}\mathrm{Ba} + ^{92}_{36}\mathrm{Kr} + 3\,^{1}_{0}n$', size=28, color=C2)
        _lines(fig, 0.06, 0.445, [('236.052593 u → 235.866572 u   (atomic masses; electrons cancel)', FG), ('Δm = 0.186021 u    E = 173.19 MeV released, per fission', FG),
                                 ('= 173 MeV (3 s.f.)', GREEN)], size=23, gap=0.046)
    if s >= 2:
        card(fig, 0.05, 0.07, 0.90, 0.24, 'The sign tells you the direction', 'Products lighter: energy released.  Products HEAVIER: energy must be supplied, e.g. a photon or a fast particle’s kinetic energy.\nEnergy leaves as gamma photons or kinetic energy. Ignore a neutrino’s mass.\nTASC beta minus: treat given masses as nuclear and subtract the electron’s 0.000549 u. Told “atomic masses”? It cancels.', tcol=PINK, size=20)


def stars(fig, s, ph):
    C1, C2 = C()
    if s <= 1:
        header(fig, 'Fusion in stars')
        chip(fig, 'Element 4 · predictions')
        T(fig, 0.06, 0.78, r'Net result in the Sun:  $4\,^{1}_{1}p\ \to\ ^{4}_{2}\mathrm{He} + 2\,^{0}_{+1}e + 2\,\nu$', size=28, color=C2)
        _lines(fig, 0.06, 0.70, [(r'Δm = 4(1.007276) − 4.001506 − 2(0.000549) = 0.0265 u, so 24.67 MeV = 24.7 MeV (3 s.f.)', FG)], size=24)
        ax = wax(fig, [0.60, 0.20, 0.36, 0.45], (-5, 5), (-5, 5)); ax.set_aspect('equal')
        ax.add_patch(Circle((0, 0), 1.0, fc=YELLOW, ec='none'))
        for r_ in (2.0, 3.2, 4.4):
            ax.add_patch(Circle((0, 0), r_, fill=False, ec=C2, lw=1.5, ls='--'))
        label(ax, 3.0, 3.8, 'r', size=22, color=C1); ax.plot([0, 3.11], [0, 3.11], color=C1, lw=2)
        if s == 0:
            bullets(fig, ['Temperature: very fast nuclei overcome\nelectric repulsion', 'High density: collisions are frequent', 'Enough energy to reach the short-range\nstrong force'], 3, 0.06, 0.60, size=23, dim=False)
        else:
            T(fig, 0.06, 0.635, 'Measured 590 W per m² at r = 2.28 × 10¹¹ m:', size=23, color=SOFT)
            T(fig, 0.06, 0.585, r'$P = 590\times4\pi r^2 = 3.8542\times10^{26}\ \mathrm{W}$', size=23)
            _sf(fig, 0.06, 0.54, '= 3.9 × 10²⁶ W (2 s.f.)')
            T(fig, 0.06, 0.48, r'mass loss $= \dfrac{P}{c^2} = 4.2824\times10^{9}\ \mathrm{kg\ s^{-1}}$', size=23)
            _sf(fig, 0.06, 0.41, '= 4.3 × 10⁹ kg s⁻¹ (2 s.f.)')
            T(fig, 0.06, 0.36, r'reactions $= \dfrac{P}{24.7\ \mathrm{MeV}} = 9.7525\times10^{37}\ \mathrm{s^{-1}}$', size=23)
            _sf(fig, 0.06, 0.29, '= 9.8 × 10³⁷ s⁻¹ (2 s.f.)')
        return
    header(fig, 'Building heavier elements in stars')
    chip(fig, 'Element 4 · predictions')
    T(fig, 0.06, 0.78, r'$^{4}_{2}\mathrm{He} + ^{4}_{2}\mathrm{He}\ \to\ ^{8}_{4}\mathrm{Be}$   then   $^{8}_{4}\mathrm{Be} + ^{4}_{2}\mathrm{He}\ \to\ ^{12}_{6}\mathrm{C} + \gamma$', size=30, color=C2)
    bullets(fig, ['Mass goes UP in the first step: an energy input, from the star’s heat', 'Mass goes DOWN in the second: energy released, as gamma and kinetic energy',
                  'It works in a giant star’s core because of huge temperature and density: collisions are\nfast and frequent enough to catch a short-lived Be-8 nucleus',
                  'Explain the reason, don’t just list the factor'], 4, 0.06, 0.68, size=24, dim=False)
    card(fig, 0.05, 0.10, 0.90, 0.16, 'Same idea on Earth', 'Rutherford’s reaction of alpha particles with nitrogen also has heavier products, so it absorbs energy.', tcol=C1, size=22)


def fission(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Fission and chain reactions')
    ax = wax(fig, [0.03, 0.14, 0.55, 0.66], (0, 12), (-5.5, 5.5)); ax.set_aspect('equal')
    def nuc(x, y, sc=0.55, c=C2):
        ax.add_patch(Circle((x, y), sc, fc=c, ec=FG, lw=1, zorder=4))
    def n_(x0, y0, x1, y1):
        arrow(ax, (x0, y0), (x1, y1), color=C1, lw=2, ms=14)
    n_(0.2, 0, 1.3, 0); nuc(1.9, 0)
    for (x, y) in [(4.2, 3.2), (4.2, 0), (4.2, -3.2)]:
        n_(2.4, y * 0.1, x - 0.65, y); nuc(x, y)
    if s >= 1:
        for (x0, y0) in [(4.2, 3.2), (4.2, 0), (4.2, -3.2)]:
            for dy in (-1.05, 0, 1.05):
                n_(x0 + 0.5, y0 + dy * 0.15, 6.6, y0 + dy); nuc(7.1, y0 + dy, sc=0.38)
        label(ax, 10.2, 0, 'each generation\nmultiplies', size=21, color=PINK)
    for dy in (1.0, -1.0):
        ax.add_patch(Circle((2.9, dy * 1.3), 0.32, fc=GREEN, ec=FG, lw=1, zorder=4))
    label(ax, 1.2, -3.0, 'two smaller\nnuclei', size=15, color=GREEN)
    label(ax, 1.5, -0.95, 'U-235', size=18, color=C2)
    it = ['Neutron + U-235: splits into two smaller nuclei\nand 2 or 3 more neutrons', 'A large nucleus can also split spontaneously,\nthough rarely']
    if s >= 1: it += ['Chain reaction: those neutrons cause\nmore fissions', 'Critical mass: the least mass that sustains a\nchain reaction. Too small: neutrons escape']
    bullets(fig, it, len(it), 0.60, 0.77, size=21, gap=0.016)


def reactor(fig, s, ph):
    C1, C2 = C()
    header(fig, 'A fission reactor')
    ax = wax(fig, [0.03, 0.14, 0.56, 0.66], (0, 14), (0, 10))
    ax.add_patch(Rectangle((1, 1.5), 5.2, 7, fc=PANEL2, ec=SOFT, lw=3))
    for x in (1.8, 3.2, 4.6):
        ax.add_patch(Rectangle((x, 2.2), 0.55, 4.6, fc=YELLOW, ec='none'))
    for x in (2.55, 3.95):
        ax.add_patch(Rectangle((x, 4.0 + 1.5 * np.sin(TAU * ph)), 0.35, 5.0, fc=PINK, ec='none'))
    label(ax, 3.6, 1.0, 'fuel rods in moderator (water or graphite)', size=15, color=YELLOW)
    label(ax, 4.6, 9.3, 'control rods', size=17, color=PINK, ha='left')
    ax.plot([6.2, 8.2, 8.2], [7, 7, 6.2], color=PINK, lw=3); ax.plot([8.2, 8.2, 6.2], [3.0, 2.4, 2.4], color=C1, lw=3)
    ax.add_patch(Rectangle((7.2, 3), 2.0, 3.2, fc=PANEL2, ec=SOFT, lw=2)); label(ax, 8.2, 4.6, 'heat\nexchanger', size=15)
    arrow(ax, (9.2, 5.4), (11, 5.4), color=FG); label(ax, 10.0, 5.95, 'steam', size=16, color=SOFT)
    ax.add_patch(Polygon([[11, 3.6], [11, 6.4], [13.2, 7], [13.2, 3]], fc=BG, ec=FG, lw=2)); label(ax, 12.1, 5, 'turbine', size=15)
    cards = [('Moderator', 'slows fast neutrons, so they\ncan cause more fissions', YELLOW), ('Control rods', 'absorb neutrons: push in to\nslow the reaction, or shut it down', PINK),
             ('Heat exchange', 'coolant carries heat out, to make\nsteam and drive a turbine', C1)]
    for i, (nm, b, c) in enumerate(cards):
        card(fig, 0.61, 0.60 - i * 0.215, 0.35, 0.195, nm, b, tcol=c, size=19)
    if s >= 1:
        T(fig, 0.61, 0.15, 'Waste stays radioactive for a long time:\nstored safely, as the risks are debated.', size=19, color=SOFT)


def strong_force(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Why the nucleus holds together')
    chip(fig, 'Element 4 · predictions')
    card(fig, 0.05, 0.58, 0.48, 0.22, 'Question', 'An alpha particle and a carbon nucleus (Z = 6) sit\n5.0 fm apart. Find the electric force, and explain\nwhat this suggests about the nucleus.', tcol=C2, size=21)
    T(fig, 0.06, 0.53, r'$F = \dfrac{k_E q_1 q_2}{r^2} = \dfrac{(9.00\times10^{9})(2e)(6e)}{(5.0\times10^{-15})^2} = 110.59\ \mathrm{N}$', size=24)
    _sf(fig, 0.06, 0.46, '= 1.1 × 10² N (2 s.f.)')
    T(fig, 0.06, 0.40, 'Huge for such tiny masses. Charges come from Z, not mass.\nSquare r. Yet nuclei stay together.', size=23, color=SOFT)
    ax = gax(fig, [0.60, 0.25, 0.35, 0.53], (0, 6), (-2.5, 2.5), 'separation (fm)', 'force (+ repulsive)', ticks=False)
    r = np.linspace(0.6, 6, 400); ax.plot(r, 0.9 / r ** 1.0, color=PINK, lw=3)
    st = 2.5 * np.exp(-(r - 1.0) ** 2 / 0.3) * (-1) * (r > 0.8) + 2.5 * (r <= 0.8) * (0.8 - r) / 0.2
    ax.plot(r, np.clip(st, -2.4, 2.4), color=GREEN, lw=3.5)
    ax.text(5.9, 2.25, 'illustrative shape', color=MUT, fontsize=17, ha='right', va='top'); ax.text(3.2, 0.5, 'electric', color=PINK, fontsize=19); ax.text(1.65, -1.75, 'strong force', color=GREEN, fontsize=19)
    if s >= 1:
        bullets(fig, ['Strong nuclear force: an attraction,\nstronger than the electric repulsion', 'Very short range: about the size of a nucleus', 'Acts only on protons and neutrons, not electrons'], 3, 0.06, 0.30, size=22, gap=0.012, dim=False)


def quarks(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Inside the nucleon: quarks')
    def nucleon(rect, qs, nm, ch):
        ax = wax(fig, rect, (-3, 3), (-3, 3)); ax.set_aspect('equal')
        ax.add_patch(Circle((0, 0), 2.7, fc=PANEL, ec=SOFT, lw=2))
        cols = ['#ff5a5a', '#5ad06a', '#5a8cff']
        pos = [(-1.15, -0.8), (1.15, -0.8), (0, 1.25)]
        for i, (p, q) in enumerate(zip(pos, qs)):
            a = pos[(i + 1) % 3]; xx = np.linspace(p[0], a[0], 80); yy = np.linspace(p[1], a[1], 80)
            d = np.array([a[0] - p[0], a[1] - p[1]]); n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
            w = 0.14 * np.sin(np.linspace(0, TAU * 5, 80) + TAU * ph * 2)
            ax.plot(xx + n[0] * w, yy + n[1] * w, color=YELLOW, lw=1.8, zorder=2)
            ax.add_patch(Circle(p, 0.62, fc=cols[i], ec=FG, zorder=3)); ax.text(p[0], p[1], q, color=BG, fontsize=23, weight='bold', ha='center', va='center', zorder=4)
        T(fig, rect[0] + rect[2] / 2, rect[1] - 0.005, f'{nm}: {ch}', size=23, ha='center', color=FG)
    nucleon([0.03, 0.34, 0.25, 0.46], 'uud', 'proton', '+⅔ +⅔ −⅓ = +1')
    nucleon([0.30, 0.34, 0.25, 0.46], 'udd', 'neutron', '+⅔ −⅓ −⅓ = 0')
    bullets(fig, ['Protons and neutrons are made of\nup quarks and down quarks', 'Up: charge +⅔ e.  Down: charge −⅓ e'], 2, 0.58, 0.77, size=23, dim=False)
    if s >= 1:
        bullets(fig, ['Colour charge: a property of quarks\n(red, green, blue), nothing to do with colour', 'Gluons carry the force between quarks', 'Qualitative only'], 3, 0.58, 0.58, size=23, dim=False, mcol=YELLOW)
        T(fig, 0.05, 0.20, 'Part of the Standard Model. In this course, stick to protons and neutrons: no mesons.', size=23, color=SOFT)


# ============================================================================ part 5: internal only
def relativity(fig, s, ph):
    C1, C2 = C()
    if s == 0:
        header(fig, 'Internal only: the Standard Model’s force carriers')
        chip(fig, 'Internal assessment only', color=YELLOW)
        rows = [('Gluons', 'strong force', C2), ('W and Z bosons', 'weak force', PINK), ('Photons', 'electromagnetic force', C1)]
        for i, (a, b, c) in enumerate(rows):
            box(fig, 0.05 + i * 0.31, 0.45, 0.28, 0.30)
            T(fig, 0.19 + i * 0.31, 0.65, a, size=30, color=c, weight='bold', ha='center')
            T(fig, 0.19 + i * 0.31, 0.55, b, size=24, ha='center')
        T(fig, 0.06, 0.36, 'These are the gauge bosons: each kind carries one force.', size=27)
        T(fig, 0.06, 0.27, 'Qualitative, and not in the external exam: but it can appear in your class work.', size=24, color=YELLOW)
        return
    header(fig, 'Internal only: special relativity')
    chip(fig, 'Internal assessment only', color=YELLOW)
    if s == 1:
        bullets(fig, ['At very high speeds, Newtonian physics fails', 'Muons from the upper atmosphere reach the ground:\ntheir half-life is dilated by their high speed',
                      'Particles in accelerators have more momentum than mv'], 3, 0.06, 0.77, size=25, dim=False)
        card(fig, 0.05, 0.10, 0.90, 0.26, 'Einstein’s two postulates', 'The speed of light in a vacuum is an absolute constant.\nAll inertial reference frames are equivalent.', tcol=C2, size=27)
        return
    ax = gax(fig, [0.07, 0.16, 0.44, 0.62], (0, 1.1), (0, 5), 'speed (fractions of c)', 'momentum (units of mc)', ticks=False)
    ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 1, 2, 3, 4, 5])
    v = np.linspace(0, 0.98, 300); ax.plot(v, v / np.sqrt(1 - v ** 2), color=PINK, lw=3.5); ax.plot([0, 1.1], [0, 1.1], color=C1, lw=3, ls='--')
    ax.axvline(1, color=YELLOW, ls=':', lw=2)
    ax.text(0.57, 2.9, 'relativistic', color=PINK, fontsize=20); ax.text(0.67, 0.28, 'Newtonian', color=C1, fontsize=20)
    bullets(fig, ['Motion is measured relative to an observer', 'Length and time depend on your reference frame', 'Relativistic momentum rises without limit,\nso nothing with mass can reach c',
                  'Mass-energy equivalence comes from\nthis theory: the source of nuclear energy', 'Close to c, results differ strongly from Newton'], 5, 0.55, 0.77, size=23, dim=False)


def contexts(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Contexts named in the course')
    sets = [[('Development of the quantum model', 'Planck, Einstein, then Bohr’s model, explaining\nhydrogen’s lines; later, orbitals and probability', C1),
             ('Black body radiation & greenhouse effect', 'Earth radiates infrared; atmospheric molecules\nabsorb it, so Earth is warmer than predicted', PINK),
             ('Radioisotopes and radiometric dating', 'Half-lives of carbon, uranium, potassium and\nargon isotopes date rocks and objects', YELLOW),
             ('Particle accelerators', 'Electric and magnetic fields speed up charges:\nresearch, medical isotopes, synchrotron light', GREEN)],
            [('Harnessing nuclear power', 'Long-term energy with no burning of fossil fuels,\nweighed against accidents and radioactive waste', C1),
             ('Nuclear reactors', 'Power, propulsion, research and medical isotopes:\nsafety is still debated', PINK),
             ('Nuclear fusion in stars', 'Hydrogen to helium powers the Sun. Elements\nheavier than helium were formed by fusion in stars', YELLOW),
             ('The Big Bang', 'Evidence: cosmic background radiation, light\nelement abundance, and galaxy red shift', GREEN)],
            [('Special relativity’s development', 'Michelson, Lorentz, Poincaré, Einstein: built on\nMaxwell, tested by Michelson-Morley and Fizeau', C1),
             ('Ring laser gyroscopes', 'Timing differences of light going both ways\naround a ring: navigation with no moving parts', PINK),
             ('The Higgs boson', 'Predicted in the 1960s, it helps explain why\nparticles have mass; seen at CERN’s collider', YELLOW)]]
    for i, (nm, b, c) in enumerate(sets[s]):
        x = 0.05 + (i % 2) * 0.46; y = 0.50 - (i // 2) * 0.30
        card(fig, x, y, 0.44, 0.28, nm, b, tcol=c, size=20)
    T(fig, 0.05, 0.14 if s < 2 else 0.20, 'Useful for internal tasks and Criterion 4. Details beyond the course content are not examined externally.', size=21, color=MUT)


# ============================================================================ finish
def exam_tips(fig, s, ph):
    C1, C2 = C()
    if s >= 4:
        summary_panel(fig, ph)
        return
    header(fig, 'Tips from examiners')
    tips = ['Two values of h: J s with joules,\neV s with electron-volts', 'Convert first: nm, pm, keV, MeV, kV,\ndays and years, before substituting',
            'Half-life and λ in matching units;\nseconds if you need becquerel', 'Photon vs electron: E = hc/λ is for\nphotons, λ = h/mv for electrons',
            'Momentum is a vector: show the\ndiagram, the direction, the signs', 'Grams in N = mNA/M, and use\nthe activity, not the count rate',
            '“Show that”: show every step, then\nuse your own value afterwards', 'Decay equations: arrow, A and Z\nbalance, include the neutrino']
    n = [2, 4, 6, 8][s]
    cols = [C1, C2, PINK, GREEN, YELLOW, C1, C2, PINK]
    for i in range(n):
        x = 0.05 + (i % 2) * 0.46; y = 0.66 - (i // 2) * 0.165
        box(fig, x, y, 0.44, 0.145, fc=PANEL)
        T(fig, x + 0.015, y + 0.0725, str(i + 1), size=36, color=cols[i], weight='bold', va='center')
        T(fig, x + 0.07, y + 0.0725, tips[i], size=21, va='center')
    T(fig, 0.05, 0.13, 'From examiners’ comments in TASC assessment reports', size=18, color=MUT)


def more_tips(fig, s, ph):
    C1, C2 = C()
    header(fig, 'More tips from examiners')
    tips = ['Spectrum sketches: wavelength axis,\nsharp λmin, labelled lines', 'Intensity changes the number of\nelectrons, not their energy',
            'Excitation jumps from the ground\nstate; photons need an exact match', 'Answer all parts: read the stem,\nit applies to every part',
            'Cooler black body: below the hotter\ncurve at every wavelength', 'Binding energy is per nucleon?\nDivide by A: not by Z or 931',
            'Mass difference ≠ binding energy:\ncheck the marks on offer', 'Check your region: don’t call 200 nm\nX-ray, or 776 nm red']
    n = [4, 8][s]
    cols = [C1, C2, PINK, GREEN, YELLOW, C1, C2, PINK]
    for i in range(n):
        x = 0.05 + (i % 2) * 0.46; y = 0.66 - (i // 2) * 0.165
        box(fig, x, y, 0.44, 0.145, fc=PANEL)
        T(fig, x + 0.015, y + 0.0725, str(i + 9), size=36, color=cols[i], weight='bold', va='center')
        T(fig, x + 0.07, y + 0.0725, tips[i], size=21, va='center')
    T(fig, 0.05, 0.13, 'From examiners’ comments in TASC assessment reports', size=18, color=MUT)


def summary_panel(fig, ph):
    C1, C2 = C()
    header(fig, 'Criterion 8 in one screen')
    chips_ = [('E = hf', C1), ('λpT = 2.90 × 10⁻³ m K', C1), ('EK(max) = eV = hf − W', C1), ('hf(max) = eV', C1), ('p = h/λ = E/c', C1),
              ('λ = h/mv', C2), ('hf = ΔE', C2), ('line spectra', C2), ('standing waves', C2),
              ('α β γ', PINK), ('A and Z balance', PINK), ('A = λN', PINK), ('λ = 0.693/T½', PINK), ('N/N₀ = e^(−λt)', PINK),
              ('E = mc²', GREEN), ('931 MeV = 1 u', GREEN), ('BE per nucleon', GREEN), ('fission & fusion', GREEN), ('strong force', GREEN), ('quarks', GREEN)]
    x, y = 0.06, 0.75
    for t, c in chips_:
        w = len(t) * 0.0105 + 0.012
        if x + w > 0.95:
            x = 0.06; y -= 0.10
        chip(fig, t, color=c, size=24, x=x, y=y, ha='left')
        x += w + 0.015
    T(fig, 0.06, 0.20, 'Know what is on the sheet, match your units, and always say WHY.', size=30, color=YELLOW, weight='bold')


def summary(fig, s, ph):
    summary_panel(fig, ph)
