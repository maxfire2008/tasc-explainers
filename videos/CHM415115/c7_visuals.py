"""Draw functions for CHM415115 Criterion 7 (organic and inorganic matter: gases, organic chemistry, the periodic table).
draw(fig, s, ph): s = step index, ph = animation phase."""
import numpy as np
from matplotlib.patches import Rectangle, Circle, Polygon, RegularPolygon

from explainer import layout as L
from explainer.layout import (header, T, bullets, box, card, chip, wax, gax, frac, FG, SOFT, MUT, GRID, PANEL, PANEL2, BG,
                              PINK, GREEN, YELLOW, TAU)
from explainer.spec import import_sibling

_CC = import_sibling(__file__, 'chm_common.py')
Slide, Seq, C, ch, fit, sheet_tag = _CC.Slide, _CC.Seq, _CC.C, _CC.ch, _CC.fit, _CC.sheet_tag


def side_notes(fig, notes, s, x=0.64, w=0.32, size=21, y=0.78, per=1):
    n = min(len(notes), (s + 1) * per)
    for i in range(n):
        t = fit(ch(notes[i]), w, size)
        T(fig, x, y, t, size=size, color=FG if i == n - 1 else SOFT)
        y -= frac(size) * (t.count('\n') + 1) + 0.03


# ============================================================================ structural formulae
def mol(ax, nodes, x0=0.0, y0=0.0, dx=1.0, fs=17, col=None, name=None, name_y=-1.9):
    """Full structural formula along a horizontal backbone.  nodes: list of dicts
         a      atom label for the backbone ('C' default, 'O', 'N')
         up, dn substituent drawn above / below: 'H', 'OH', 'Cl', '=O', 'CH3', 'NH2' ... (None = nothing)
         bond   bond order to the NEXT backbone atom (1 default; 2 double)
         left, right   substituent drawn at the far ends (first / last node only)
    Returns the x position of the right end."""
    col = col or FG
    n = len(nodes)
    xs = [x0 + i * dx for i in range(n)]

    def lab(x, y, t, c=col):
        ax.text(x, y, t, color=c, fontsize=fs, ha='center', va='center', zorder=5, bbox=dict(fc=BG, ec='none', pad=0.6))

    def seg(x1, y1, x2, y2, order=1, horizontal=True):
        off = 0.07
        if order == 1:
            ax.plot([x1, x2], [y1, y2], color=col, lw=2.2, zorder=2)
            return
        for k in (-1, 1):
            if horizontal:
                ax.plot([x1, x2], [y1 + k * off, y2 + k * off], color=col, lw=2.2, zorder=2)
            else:
                ax.plot([x1 + k * off, x2 + k * off], [y1, y2], color=col, lw=2.2, zorder=2)

    for i, nd in enumerate(nodes):
        x = xs[i]
        lab(x, y0, nd.get('a', 'C'))
        for key, sgn in (('up', 1), ('dn', -1)):
            sub = nd.get(key, 'H')
            if sub:
                order = 2 if sub.startswith('=') else 1
                t = sub.lstrip('=')
                seg(x, y0 + sgn * 0.17, x, y0 + sgn * 0.78, order, horizontal=False)
                lab(x, y0 + sgn * 0.95, ch(t))
        if i < n - 1:
            seg(x + 0.15, y0, xs[i + 1] - 0.15, y0, nd.get('bond', 1), horizontal=True)
    left = nodes[0].get('left', 'H')
    right = nodes[-1].get('right', 'H')
    if left:
        order = 2 if left.startswith('=') else 1
        seg(xs[0] - 0.8, y0, xs[0] - 0.15, y0, order)
        lab(xs[0] - 0.95, y0, ch(left.lstrip('=')))
    if right:
        order = 2 if right.startswith('=') else 1
        seg(xs[-1] + 0.15, y0, xs[-1] + 0.8, y0, order)
        lab(xs[-1] + 0.95, y0, ch(right.lstrip('=')))
    if name:
        ax.text((xs[0] + xs[-1]) / 2, y0 + name_y, name, color=YELLOW, fontsize=fs + 2, ha='center', va='center', weight='bold')
    return xs[-1] + 1.0


def alk(n, subs=None, bonds=None, left='H', right='H', atoms=None):
    """n backbone carbons, hydrogens everywhere, with overrides: subs {i: dict(up=, dn=)}, bonds {i: order}, atoms {i: 'O'}."""
    subs = subs or {}
    bonds = bonds or {}
    atoms = atoms or {}
    nodes = []
    for i in range(1, n + 1):
        d = dict(a=atoms.get(i, 'C'), up='H', dn='H', bond=bonds.get(i, 1))
        d.update(subs.get(i, {}))
        nodes.append(d)
    nodes[0]['left'] = left
    nodes[-1]['right'] = right
    return nodes


class mol_slide:
    """A scene that shows structural formulae (items: (nodes, name, caption)) a few at a time.
    A class, so that its repr (and so the clip cache key) follows the content."""
    def __init__(self, items, title, chip_text, fs=16, per=1, cols=2, notes=None, note_size=21):
        self.items, self.title, self.chip_text, self.fs, self.per, self.cols = items, title, chip_text, fs, per, cols
        self.notes, self.note_size = notes, note_size

    def __repr__(self):
        return f'mol_slide({self.items!r}, {self.title!r}, {self.chip_text!r}, {self.fs}, {self.per}, {self.cols}, {self.notes!r})'

    def __call__(self, fig, s, ph):
        items, cols = self.items, self.cols
        header(fig, self.title)
        chip(fig, self.chip_text)
        n = min(len(items), (s + 1) * self.per)
        rows = (len(items) + cols - 1) // cols
        for i in range(n):
            nodes, name, cap = items[i][:3]
            r, k = divmod(i, cols)
            w = 0.90 / cols
            ax = wax(fig, [0.05 + k * w, 0.76 - (r + 1) * (0.56 / rows), w, 0.54 / rows], (-1.6, 6.4), (-2.6, 1.9))
            mol(ax, nodes, 0.2, 0.0, 1.0, fs=self.fs, name=name, name_y=-1.75)
            if cap:
                T(fig, 0.05 + k * w + w / 2, 0.76 - (r + 1) * (0.56 / rows) + 0.012, ch(cap), size=18, color=MUT, ha='center')
        if self.notes:
            T(fig, 0.05, 0.17, fit(ch(self.notes[min(s, len(self.notes) - 1)]), 0.9, self.note_size), size=self.note_size, color=SOFT)


# ============================================================================ organic: table-like diagrams
def reaction_map(fig, s, ph):
    """The organic reaction map from the information sheet (p7), built up in four stages."""
    C1, C2 = C()
    header(fig, 'Organic reactions: the map')
    chip(fig, 'Element 3 · equations')
    ax = wax(fig, [0.03, 0.13, 0.94, 0.68], (0, 100), (0, 62))
    pos = dict(alkane=(10, 52), alkene=(10, 28), halide=(46, 52), alcohol=(46, 28), aldehyde=(46, 8), acid=(76, 8),
               ketone=(88, 40), ester=(88, 22), polymer=(10, 7), amine=(88, 56), salt=(104, 8))
    names = dict(alkane='Alkane', alkene='Alkene', halide='Alkyl halide', alcohol='Alcohol', aldehyde='Aldehyde',
                 acid='Carboxylic acid', ketone='Ketone', ester='Ester', polymer='Polymer', amine='Amine')
    cols = dict(alkane=C1, alkene=C1, polymer=C1, halide=PINK, alcohol=C2, aldehyde=GREEN, ketone=GREEN, acid=YELLOW, ester=YELLOW, amine=PINK)

    def node(k):
        x, y = pos[k]
        ax.text(x, y, names[k], color=BG, fontsize=17, weight='bold', ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.35', fc=cols[k], ec='none'), zorder=4)

    def arr(a, b, txt, side=1.6, rad=0.0, tx=None, ty=None):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        ax.annotate('', (x2, y2), (x1, y1), arrowprops=dict(arrowstyle='-|>', color=SOFT, lw=2, shrinkA=22, shrinkB=22, connectionstyle=f'arc3,rad={rad}'))
        ax.text(tx if tx is not None else (x1 + x2) / 2, ty if ty is not None else (y1 + y2) / 2 + side, txt, color=YELLOW, fontsize=15, ha='center', va='center',
                bbox=dict(fc=BG, ec='none', pad=0.8), zorder=3)
    stages = [
        (['alkane', 'alkene', 'halide', 'alcohol'], [('alkene', 'alkane', 'H₂'), ('alkene', 'alcohol', 'H₂O (steam)'), ('alcohol', 'alkene', '−H₂O, conc H₂SO₄', -2.5),
                                                    ('halide', 'alcohol', 'dilute NaOH(aq)'), ('alkene', 'halide', 'HX')]),
        (['aldehyde', 'acid', 'ketone'], [('alcohol', 'aldehyde', 'primary: [O], mild'), ('aldehyde', 'acid', '[O]'), ('alcohol', 'ketone', 'secondary: [O]'),
                                         ('alcohol', 'acid', 'primary: [O], excess strong', 2.5, -0.25)]),
        (['ester', 'amine'], [('alcohol', 'ester', 'RCOOH, conc H₂SO₄', 2.0, 0.1), ('ester', 'acid', 'hydrolysis'), ('halide', 'amine', 'NH₃')]),
        (['polymer'], [('alkene', 'polymer', 'addition polymerisation')]),
    ]
    for k in range(min(4, s + 1)):
        nodes, arrows = stages[k]
        for nme in nodes:
            node(nme)
        for a in arrows:
            arr(*a)
    if s >= 1:
        node('alkane'); node('alkene'); node('halide'); node('alcohol')


# ============================================================================ spectra
def ir_axes(fig, rect, peaks, title, label_peaks=True):
    ax = gax(fig, rect, (4000, 500), (0, 105), 'Wavenumber (cm⁻¹)', 'Transmittance (%)')
    ax.set_yticks([0, 50, 100]); ax.set_xticks([4000, 3000, 2000, 1500, 1000, 500])
    x = np.linspace(4000, 500, 1500)
    t = np.full_like(x, 92.0)
    for c, d, w, lab_ in peaks:
        t -= d * np.exp(-((x - c) / w) ** 2)
    t += 1.2 * np.sin(x / 37.0) * (x < 1500)
    ax.plot(x, np.clip(t, 2, 100), color=C()[0], lw=3)
    ax.set_title(title, color=FG, fontsize=20, loc='left')
    if label_peaks:
        for c, d, w, lab_ in peaks:
            if lab_:
                ax.annotate(lab_, (c, 92 - d), (c, max(6, 92 - d - 14)), color=YELLOW, fontsize=16, ha='center',
                            arrowprops=dict(arrowstyle='-', color=YELLOW, lw=1.2), zorder=6)
    return ax


IR_SETS = {
    'ethanol': ([(3350, 70, 260, 'O–H'), (2950, 25, 90, ''), (1050, 55, 50, '')], 'Alcohol (ethanol): broad O–H near 3350'),
    'acid': ([(2950, 78, 520, 'O–H (acid)'), (1710, 82, 45, 'C=O'), (1250, 40, 60, '')], 'Carboxylic acid: very broad O–H and C=O'),
    'ester': ([(2950, 25, 90, ''), (1740, 82, 40, 'C=O'), (1200, 55, 60, '')], 'Ester: C=O, but NO O–H'),
    'ketone': ([(2950, 25, 90, ''), (1715, 80, 40, 'C=O')], 'Ketone or aldehyde: C=O only'),
}


def ir_scene(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Reading an infrared spectrum')
    chip(fig, 'Element 2 · analytical data')
    keys = ['ethanol', 'acid', 'ester', 'ketone']
    k = keys[min(s, 3)]
    ir_axes(fig, [0.06, 0.15, 0.55, 0.60], IR_SETS[k][0], IR_SETS[k][1])
    sheet_tag(fig, 0.64, 0.80, 'Frequencies of important IR stretching vibrations')
    rows = [('O–H (alcohol)', '3650–3200', 'strong, broad'), ('O–H (carboxylic acid)', '3300–2500', 'strong, very broad'),
            ('C=O (carbonyl)', '1780–1650', 'strong')]
    y = 0.74
    for i, r in enumerate(rows):
        hl = (k in ('ethanol',) and i == 0) or (k == 'acid' and i in (1, 2)) or (k in ('ester', 'ketone') and i == 2)
        box(fig, 0.64, y - 0.055, 0.32, 0.075, fc=PANEL2 if hl else PANEL)
        T(fig, 0.65, y - 0.005, r[0], size=18, color=YELLOW if hl else SOFT, weight='bold')
        T(fig, 0.65, y - 0.035, f'{r[1]} cm⁻¹   {r[2]}', size=17, color=FG if hl else MUT)
        y -= 0.09
    T(fig, 0.64, 0.45, 'Illustrative shapes, not measured spectra', size=16, color=MUT)
    notes = ['Say the wavenumber and the bond: “broad absorption at about 3350 cm⁻¹ is an alcohol O–H”',
             'Both an O–H and a C=O: a carboxylic acid. An alcohol or aldehyde alone would not have both',
             'A C=O with no O–H band: an ester (or aldehyde, or ketone). Not an acid',
             'Aldehyde and ketone both show only C=O on this sheet, so other evidence is needed to tell them apart']
    T(fig, 0.64, 0.38, fit(notes[min(s, 3)], 0.31, 20), size=20, color=FG)


def ms_scene(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Mass spectrometry of an organic molecule')
    chip(fig, 'Element 2 · analytical data')
    ax = gax(fig, [0.06, 0.15, 0.55, 0.60], (10, 70), (0, 110), 'm/z', 'Relative abundance (%)')
    peaks = {27: 12, 28: 8, 29: 35, 30: 15, 31: 100, 42: 10, 59: 14, 60: 12}
    for mz, h in peaks.items():
        col = C1
        if mz == 60:
            col = PINK
        if s >= 2 and mz == 31:
            col = GREEN
        ax.vlines(mz, 0, h, color=col, lw=5)
    ax.annotate('M⁺ (molecular ion)\nm/z = 60', (60, 14), (54, 55), color=PINK, fontsize=18, ha='center',
                arrowprops=dict(arrowstyle='-|>', color=PINK))
    if s >= 1:
        ax.annotate('base peak, m/z = 31\nCH₂OH⁺ fragment', (31, 100), (45, 90), color=GREEN, fontsize=18, ha='center',
                    arrowprops=dict(arrowstyle='-|>', color=GREEN))
    ax.set_title('Propan-1-ol (illustrative pattern)', color=FG, fontsize=20, loc='left')
    notes = ['The molecular ion peak is the whole molecule minus one electron: its m/z equals the relative molecular mass. Propan-1-ol, C₃H₈O: 60',
             'Fragments appear at lower m/z. A peak at 31 fits CH₂OH⁺, which suggests a primary alcohol. Look for differences of 15 (CH₃), 17 (OH), 29 (C₂H₅)',
             'Compare with the alternative: propanoic acid, C₃H₆O₂ has M = 74, so a peak at 60 as the top of the pattern rules it out',
             'Mass spectrometry also analyses isotopes: each isotope gives its own peak, so relative abundances give the relative atomic mass']
    T(fig, 0.64, 0.78, fit(ch(notes[min(s, 3)]), 0.31, 21), size=21, color=FG)
    T(fig, 0.64, 0.22, 'Instrument details are not examined', size=17, color=MUT)


# ============================================================================ periodic table
def ie_graph(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Successive ionisation energies: evidence for shells')
    chip(fig, 'Element 4 · electron configuration')
    ax = gax(fig, [0.07, 0.15, 0.50, 0.62], (0.5, 8.5), (0, 24000), 'Number of electrons removed', 'Ionisation energy (kJ mol⁻¹)')
    mg = [738, 1451, 7733, 10543, 13630, 17995, 21703, 25656]
    mg = mg[:7]
    ax.scatter(range(1, 8), mg, color=C1, s=170, zorder=5)
    ax.set_xticks(range(1, 8)); ax.set_ylim(0, 24500)
    ax.text(1.1, 20500, 'magnesium, 2,8,2', color=SOFT, fontsize=18)
    if s >= 1:
        ax.annotate('large jump: the 3rd electron\ncomes from an inner shell', (3, 7733), (3.8, 3000), color=YELLOW, fontsize=17,
                    arrowprops=dict(arrowstyle='-|>', color=YELLOW))
    ax.text(5.0, 11500, 'Reference data, not from TASC', color=MUT, fontsize=14)
    notes = ['Remove electrons one at a time from gaseous atoms: the energy needed rises each time, because the remaining electrons are held more tightly',
             'A very large jump marks a move to a shell closer to the nucleus: it has less shielding and a stronger attraction. Two small steps then a huge one: two valence electrons',
             'It is evidence for shells. Do not confuse this with the trend across a period: this graph is for ONE element']
    side_notes(fig, notes, s, x=0.60, w=0.35, size=21)


def trend_scene(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Periodic trends: periods 2 and 3')
    chip(fig, 'Element 5 · valence theory')
    p2 = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
    p3 = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
    ax = wax(fig, [0.04, 0.22, 0.60, 0.50], (0, 100), (0, 50))
    for r, row in enumerate((p2, p3)):
        for i, sym in enumerate(row):
            x = 8 + i * 11.2; y = 36 - r * 14
            ax.add_patch(Rectangle((x - 4.6, y - 5), 9.2, 10, fc=PANEL2, ec=GRID, lw=1.5))
            ax.text(x, y, sym, color=FG, fontsize=20, weight='bold', ha='center', va='center')
    ax.text(2, 44, 'Period 2', color=SOFT, fontsize=15); ax.text(2, 30, 'Period 3', color=SOFT, fontsize=15)
    if s >= 0:
        ax.annotate('', (96, 7), (6, 7), arrowprops=dict(arrowstyle='-|>', color=C1, lw=4))
        ax.text(50, 2.5, 'nuclear charge increases; shielding about constant', color=C1, fontsize=17, ha='center')
    if s >= 1:
        ax.annotate('', (100, 10), (100, 42), arrowprops=dict(arrowstyle='-|>', color=PINK, lw=4))
        ax.text(98, 26, 'more shells', color=PINK, fontsize=15, ha='right', rotation=90, va='center')
    items = ['ACROSS a period (left to right): more protons, same shell, so the core charge rises. Atomic radius DECREASES, ionisation energy and electronegativity INCREASE',
             'DOWN a group: more shells and more shielding, so the outer electrons are further out and less tightly held. Radius INCREASES, ionisation energy and electronegativity DECREASE',
             'So metals get LESS reactive across a period (they hold electrons more tightly) and non-metals MORE reactive; down a group metals get MORE reactive and non-metals LESS']
    side_notes(fig, items, s, x=0.67, w=0.29, size=19)
    sheet_tag(fig, 0.05, 0.145, 'General periodic trends')


def anomaly_graph(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Period 3: ionisation energy and radius')
    chip(fig, 'Element 5 · valence theory')
    el = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl']
    ie = [496, 738, 578, 787, 1012, 1000, 1251]
    rad = [186, 160, 143, 118, 110, 104, 99]
    ax = gax(fig, [0.07, 0.15, 0.40, 0.60], (-0.5, 6.5), (400, 1400), 'Period 3 element', 'First ionisation energy (kJ mol⁻¹)')
    ax.set_xticks(range(7)); ax.set_xticklabels(el)
    ax.plot(range(7), ie, color=C1, lw=3, marker='o', ms=11)
    if s >= 1:
        ax.annotate('Al lower than Mg:\n3p electron is further out\nand shielded by the 3s', (2, 578), (2.2, 430), color=YELLOW, fontsize=15, ha='center',
                    arrowprops=dict(arrowstyle='-|>', color=YELLOW))
    ax2 = gax(fig, [0.55, 0.15, 0.40, 0.60], (-0.5, 6.5), (60, 200), 'Period 3 element', 'Atomic radius (pm)')
    ax2.set_xticks(range(7)); ax2.set_xticklabels(el)
    ax2.plot(range(7), rad, color=PINK, lw=3, marker='o', ms=11)
    T(fig, 0.07, 0.10, 'Reference data, not from TASC. First ionisation energy rises overall, with dips at Al and S', size=16, color=MUT)
    if s >= 2:
        T(fig, 0.55, 0.80, 'Radius falls steadily: protons rise, shielding is constant', size=19, color=GREEN)


def radius_ions(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Isoelectronic ions: the same electrons, different nuclei')
    chip(fig, 'Element 4 · electron configuration')
    ions = [('P³⁻', 15, 212), ('S²⁻', 16, 184), ('Cl⁻', 17, 181), ('K⁺', 19, 138), ('Ca²⁺', 20, 100), ('Sc³⁺', 21, 75)]
    ax = wax(fig, [0.05, 0.22, 0.62, 0.52], (0, 100), (0, 60))
    ax.set_aspect('equal')
    n = min(len(ions), 6)
    for i, (nm, z, r) in enumerate(ions):
        x = 10 + i * 15.5
        ax.add_patch(Circle((x, 26), r / 9.0, fc='none', ec=C1 if z < 19 else C2, lw=3))
        ax.text(x, 26, nm, color=FG, fontsize=18, weight='bold', ha='center', va='center')
        ax.text(x, 4, f'{z} protons', color=SOFT, fontsize=14, ha='center')
        ax.text(x, 0, f'{r} pm', color=MUT, fontsize=14, ha='center')
    notes = ['Each has 18 electrons: 1s² 2s² 2p⁶ 3s² 3p⁶. They are isoelectronic',
             'Same electron arrangement, so the same shielding. The only difference is the nuclear charge',
             'More protons pull the same electrons closer: radius falls from P³⁻ (15 protons) to Sc³⁺ (21 protons). Ionisation energy rises the same way',
             'Compare ions, not atoms: question after question went wrong by ordering the neutral atoms']
    side_notes(fig, notes, s, x=0.05, w=0.9, size=21, y=0.17, per=1)
    T(fig, 0.05, 0.075, 'Ionic radii: reference data, not from TASC', size=15, color=MUT)


def ladder(fig, s, ph):
    """Sub-shell energy ladder with electron boxes."""
    C1, C2 = C()
    header(fig, 'Filling the sub-shells')
    chip(fig, 'Element 4 · electron configuration')
    order = [('1s', 1, 2), ('2s', 1, 2), ('2p', 3, 6), ('3s', 1, 2), ('3p', 3, 6), ('4s', 1, 2), ('3d', 5, 10)]
    ys = {'1s': 0, '2s': 1, '2p': 1.45, '3s': 2.4, '3p': 2.85, '4s': 3.8, '3d': 4.25}
    fill_by_step = {0: 0, 1: 16, 2: 27}
    nel = fill_by_step[min(s, 2)]
    seq = ['1s', '2s', '2p', '3s', '3p', '4s', '3d']
    left = nel
    cap = {'1s': 2, '2s': 2, '2p': 6, '3s': 2, '3p': 6, '4s': 2, '3d': 10}
    occ = {}
    for k in seq:
        take = min(left, cap[k]); occ[k] = take; left -= take
    ax = wax(fig, [0.05, 0.12, 0.50, 0.68], (0, 100), (-0.6, 5.2))
    ax.annotate('', (3, 4.9), (3, -0.4), arrowprops=dict(arrowstyle='<|-', color=MUT, lw=2.5))
    ax.text(5.5, 4.95, 'higher energy', color=MUT, fontsize=15)
    for k in seq:
        y = ys[k]
        nb = 1 if k.endswith('s') else (3 if k.endswith('p') else 5)
        ax.text(10, y, k, color=SOFT, fontsize=20, weight='bold', va='center')
        for b in range(nb):
            x = 22 + b * 9
            ax.add_patch(Rectangle((x, y - 0.18), 8, 0.36, fc=PANEL2, ec=GRID, lw=2))
        e = occ[k]
        # Hund: one in each box first, then pair up
        ups = min(e, nb); downs = max(0, e - nb)
        for b in range(nb):
            x = 22 + b * 9 + 4
            if b < ups:
                ax.text(x - 1.2, y, '↑', color=YELLOW, fontsize=20, ha='center', va='center')
            if b < downs:
                ax.text(x + 1.2, y, '↓', color=YELLOW, fontsize=20, ha='center', va='center')
    notes = ['Sub-shell capacity: s holds 2 electrons, p holds 6, d holds 10. Fill from the lowest energy up. Note that 4s fills BEFORE 3d',
             'Sulfur, 16 electrons: 1s² 2s² 2p⁶ 3s² 3p⁴. In a p sub-shell, electrons go into separate orbitals first, then pair up',
             'Iron-like d-block atoms: 4s fills first (2 electrons), then 3d. Cobalt, 27 electrons: 1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁷ 4s². In the ION the 4s electrons are lost first']
    side_notes(fig, notes, s, x=0.58, w=0.37, size=21)
    T(fig, 0.58, 0.20, 'Use s, p, d notation in full: shorthand such as [Ar] is only accepted when the question allows it', size=17, color=MUT)


def bohr_scene(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Energy levels and spectra')
    chip(fig, 'Element 4 · evidence for shells')
    ax = wax(fig, [0.05, 0.14, 0.45, 0.66], (0, 100), (0, 100))
    lv = {1: 5, 2: 55, 3: 68, 4: 74, 5: 78}
    for n, y in lv.items():
        ax.plot([30, 80], [y, y], color=SOFT, lw=3)
        ax.text(26, y, f'n = {n}', color=FG, fontsize=17, ha='right', va='center')
    ax.text(55, 90, 'Hydrogen energy levels (not to scale)', color=SOFT, fontsize=15, ha='center')
    k = (ph * 1.0) % 1.0
    if s >= 1:
        ax.annotate('', (45, lv[1] + 1), (45, lv[3]), arrowprops=dict(arrowstyle='<|-', color=PINK, lw=3))
        ax.annotate('', (62, lv[2] + 1), (62, lv[3]), arrowprops=dict(arrowstyle='<|-', color=GREEN, lw=3))
        ax.text(45, 35, 'large ΔE\nultraviolet', color=PINK, fontsize=15, ha='center')
        ax.text(70, 60, 'smaller ΔE\nvisible', color=GREEN, fontsize=15, ha='left')
    ax2 = wax(fig, [0.55, 0.52, 0.40, 0.22], (400, 700), (0, 1))
    ax2.add_patch(Rectangle((400, 0), 300, 1, fc='#101a30', ec=GRID))
    for w, c in ((410, '#a78bfa'), (434, '#6366f1'), (486, '#22d3ee'), (656, '#f15bb5')):
        ax2.vlines(w, 0, 1, color=c, lw=5)
    ax2.text(550, 1.15, 'emission lines (visible)', color=SOFT, fontsize=15, ha='center')
    notes = ['Electrons occupy fixed energy levels (shells). In the Bohr model of hydrogen, an electron stays in its level until it gains or loses energy',
             'Excited atoms release the energy as light when electrons drop to a lower level. ΔE gives ONE wavelength per jump, so a line spectrum shows the levels exist',
             'The model also has sub-shells (s, p, d) and orbitals within each shell. Different lines for one element are evidence for sub-shells, not one level per element']
    side_notes(fig, notes, s, x=0.55, w=0.40, size=20, y=0.45)


# ============================================================================ gases
def kmt_box(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Kinetic theory of gases')
    chip(fig, 'Element 6 · gases')
    ax = wax(fig, [0.05, 0.14, 0.42, 0.66], (0, 100), (0, 66))
    ax.add_patch(Rectangle((2, 2), 96, 62, fc='none', ec=FG, lw=4))
    rng = np.random.RandomState(7)
    amp = 1.0 if s != 1 else 1.0
    n = 22
    for i in range(n):
        cx, cy = rng.uniform(15, 85), rng.uniform(12, 54)
        ax_, ay_ = rng.uniform(8, 14), rng.uniform(5, 9)
        kx, ky = rng.randint(1, 3 + (2 if s >= 1 else 0)), rng.randint(1, 3 + (2 if s >= 1 else 0))
        ph1, ph2 = rng.uniform(0, 1), rng.uniform(0, 1)
        x = cx + ax_ * np.sin(TAU * (kx * ph + ph1)); y = cy + ay_ * np.sin(TAU * (ky * ph + ph2))
        ax.add_patch(Circle((x, y), 1.8, fc=C1 if i % 4 else PINK, ec='none'))
    if s >= 2:
        ax.annotate('force on wall = pressure', (98, 35), (80, 60), color=YELLOW, fontsize=15, ha='center', arrowprops=dict(arrowstyle='-|>', color=YELLOW))
    items = ['Particles are tiny compared with the distances between them: negligible volume',
             'They move randomly in straight lines, and collide elastically with each other and the walls',
             'No attraction or repulsion between particles: no intermolecular forces',
             'Average kinetic energy is proportional to the absolute temperature (kelvin)']
    side_notes(fig, items, s, x=0.52, w=0.43, size=22, per=2)
    T(fig, 0.52, 0.18, 'Not part of the definition: “no mass”. The particles have mass', size=19, color=PINK)


def gas_graphs(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Boyle, Charles and the combined gas law')
    chip(fig, 'Element 6 · gases')
    V = np.linspace(1, 5, 100)
    ax = gax(fig, [0.06, 0.15, 0.27, 0.58], (0, 5), (0, 5), 'Volume', 'Pressure', ticks=False)
    ax.plot(V, 5 / V, color=C1, lw=4); ax.text(2.2, 4.4, "Boyle: P ∝ 1/V\n(T, n constant)", color=C1, fontsize=17)
    if s >= 1:
        ax2 = gax(fig, [0.38, 0.15, 0.27, 0.58], (-300, 100), (0, 5), 'Temperature (°C)', 'Volume', ticks=False)
        t = np.linspace(-273.15, 100, 50)
        ax2.plot(t, 1.0 + (t + 273.15) / 100 * 1.0 * 0.9, color=PINK, lw=4)
        ax2.plot(np.linspace(-273.15, -150, 5), 1.0 * 0.0 + (np.linspace(-273.15, -150, 5) + 273.15) / 100 * 0.9, color=PINK, lw=2, ls=':')
        ax2.axvline(-273.15, color=MUT, ls='--', lw=1.5); ax2.text(-262, 4.0, '−273 °C\n= 0 K', color=MUT, fontsize=15)
        ax2.text(-20, 1.0, 'Charles: V ∝ T (in kelvin)\n(P, n constant)', color=PINK, fontsize=16)
    if s >= 1:
        ax3 = gax(fig, [0.70, 0.15, 0.27, 0.58], (0, 5), (0, 5), 'Temperature (K)', 'Pressure', ticks=False)
        tt = np.linspace(0, 5, 20); ax3.plot(tt, tt, color=GREEN, lw=4)
        ax3.text(0.3, 4.2, 'P ∝ T (in kelvin)\n(V, n constant)', color=GREEN, fontsize=16)
    notes = ['Boyle: at constant temperature, pressure and volume are inversely proportional: P₁V₁ = P₂V₂',
             'Charles: at constant pressure, volume is proportional to ABSOLUTE temperature (kelvin); at constant volume, pressure is proportional to it too. Extended back, volume would reach zero at 0 K']
    T(fig, 0.06, 0.09, fit(ch(notes[min(s, 1)]), 0.9, 21), size=21, color=FG)


class GasLaws:
    """Steps 0-1: the gas-law graphs; later steps: the information-sheet equations."""
    def __init__(self, eq_slide):
        self.eq = eq_slide

    def __repr__(self):
        return f'GasLaws({self.eq!r}, {gas_graphs.__code__.co_code!r})'

    def __call__(self, fig, s, ph):
        if s < 2:
            gas_graphs(fig, s, ph)
        else:
            self.eq(fig, s - 2, ph)


def real_gas(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Real gases and ideal gases')
    chip(fig, 'Element 6 · gases')
    ax = gax(fig, [0.07, 0.15, 0.50, 0.62], (0, 10), (0, 1.6), 'Pressure', 'PV / nRT', ticks=False)
    p = np.linspace(0, 10, 200)
    ax.axhline(1.0, color=C1, lw=4); ax.text(7.8, 1.07, 'ideal gas', color=C1, fontsize=18)
    if s >= 1:
        ax.plot(p, 1 - 0.09 * p + 0.0075 * p ** 2 + 0.0 * p, color=PINK, lw=4)
        ax.text(1.0, 0.45, 'real gas, low T:\nintermolecular forces\npull it below 1', color=PINK, fontsize=16)
    if s >= 2:
        ax.text(6.2, 1.35, 'very high P: particle\nvolume matters, so above 1', color=YELLOW, fontsize=16)
    notes = ['An ideal gas obeys PV = nRT at every pressure and temperature. It has negligible particle volume and no intermolecular forces',
             'Real gases behave ideally at HIGH temperature and LOW pressure. At low temperature, attractions pull particles away from the walls: pressure is lower and volume smaller than predicted',
             'At very high pressure the particles’ own volume is no longer negligible. A gas with more electrons or polar molecules (SO₂ against helium) departs more']
    side_notes(fig, notes, s, x=0.60, w=0.35, size=21)


# ============================================================================ title and thumbnail
def _title_art(fig, rect, ph=0):
    C1, C2 = C()
    ax = wax(fig, rect, (-1.6, 1.6), (-1.6, 1.6))
    ax.set_aspect('equal')
    ax.add_patch(RegularPolygon((0, 0), 6, radius=1.0, orientation=0, fc='none', ec=C1, lw=14))
    ax.add_patch(Circle((0, 0), 0.58, fc='none', ec=YELLOW, lw=10))
    for k in range(6):
        a = TAU * k / 6 + np.pi / 6
        ax.plot([np.cos(a) * 1.0, np.cos(a) * 1.28], [np.sin(a) * 1.0, np.sin(a) * 1.28], color=C1, lw=8)
        ax.scatter([np.cos(a) * 1.0], [np.sin(a) * 1.0], s=1600, color=PINK if k % 2 else C1, edgecolor=BG, linewidth=4, zorder=5)
    for k in range(6):
        a = TAU * (k / 6 + ph) + np.pi / 6
        ax.scatter([np.cos(a) * 1.5], [np.sin(a) * 1.5], s=700, color=GREEN, edgecolor=BG, linewidth=3, zorder=6)


def thumbnail(fig):
    C1, C2 = C()
    fig.text(0.04, 0.87, 'CRITERION 7', ha='left', va='center', color=C1, fontsize=64, weight='bold')
    fig.text(0.04, 0.65, 'Organic,', ha='left', va='center', color=FG, fontsize=130, weight='bold')
    fig.text(0.04, 0.44, 'atoms &', ha='left', va='center', color=FG, fontsize=130, weight='bold')
    fig.text(0.04, 0.23, 'gases', ha='left', va='center', color=FG, fontsize=130, weight='bold')
    _title_art(fig, [0.58, 0.17, 0.40, 0.78])
