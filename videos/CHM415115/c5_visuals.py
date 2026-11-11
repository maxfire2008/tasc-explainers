"""Draw functions for CHM415115 Criterion 5 (electrochemistry).  Each is draw(fig, s, ph): s = step index, ph = animation phase."""
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Polygon, FancyArrowPatch

from explainer import layout as L
from explainer.layout import (header, T, bullets, box, card, eq, learn_eq, chip, wax, gax, darrow, arrow, label, frac,
                              FG, SOFT, MUT, GRID, PANEL, PANEL2, BG, PINK, GREEN, YELLOW, TAU)
from explainer.spec import import_sibling

_CC = import_sibling(__file__, 'chm_common.py')
Slide, Seq, C, ch, fit, sf, extend, sheet, sheet_tag, path_dots, lines = (
    _CC.Slide, _CC.Seq, _CC.C, _CC.ch, _CC.fit, _CC.sf, _CC.extend, _CC.sheet, _CC.sheet_tag, _CC.path_dots, _CC.lines)



def side_notes(fig, notes, s, x=0.66, w=0.30, size=21, y=0.78, per=1, last_bright=True):
    """Build-up notes in a right-hand column, wrapped to fit.  `per` notes are added per step."""
    n = min(len(notes), (s + 1) * per)
    for i in range(n):
        t = fit(ch(notes[i]), w, size)
        T(fig, x, y, t, size=size, color=FG if (i == n - 1 or not last_bright) else SOFT)
        y -= frac(size) * (t.count('\n') + 1) + 0.03

# ============================================================================ the reusable cell diagram
ELEC = '#aab6c8'
LIQ = '#1b3a5c'


def cell(fig, rect, cfg, show, ph=0.0):
    """Galvanic / electrolytic cell.  cfg: left, right (dicts), single, device, bridge.  show: set of tokens
    'vessel','electrodes','wire','roles','polarity','ions','eflow','bridge','ionflow','eq','device_val'."""
    C1, C2 = C()
    ax = wax(fig, rect, (0, 100), (0, 66))
    single = cfg.get('single', False)
    gal = cfg.get('mode', 'galvanic') == 'galvanic'
    xl, xr = (36, 64) if single else (25, 75)
    if 'vessel' in show:
        boxes = [(18, 82)] if single else [(6, 44), (56, 94)]
        for a, b in boxes:
            ax.add_patch(Rectangle((a, 4), b - a, 24, fc=LIQ, ec=MUT, lw=3, alpha=0.9, zorder=1))
            ax.add_patch(Rectangle((a, 28), b - a, 0, fc='none', ec=MUT, lw=3))
        for side, x in ((cfg['left'], xl), (cfg['right'], xr)):
            if side.get('sol'):
                ax.text(x if not single else 50, 7, side['sol'], color=SOFT, fontsize=16, ha='center', va='center')
                if single:
                    break
    if 'electrodes' in show:
        for side, x in ((cfg['left'], xl), (cfg['right'], xr)):
            ax.add_patch(Rectangle((x - 2, 8), 4, 32, fc=side.get('ecol', ELEC), ec=BG, lw=1.5, zorder=3))
            ax.text(x - 3.5 if x < 50 else x + 3.5, 46, side['name'], color=FG, fontsize=20, ha='right' if x < 50 else 'left',
                    va='center', weight='bold', zorder=5)
    if 'wire' in show:
        top = 58
        for x in (xl, xr):
            ax.plot([x, x], [40, top], color=FG, lw=3, zorder=2)
        ax.plot([xl, 44], [top, top], color=FG, lw=3, zorder=2)
        ax.plot([56, xr], [top, top], color=FG, lw=3, zorder=2)
        if gal:
            ax.add_patch(Circle((50, top), 6, fc=PANEL, ec=FG, lw=3, zorder=4))
            ax.text(50, top, 'V', color=YELLOW, fontsize=24, weight='bold', ha='center', va='center', zorder=5)
            if 'device_val' in show and cfg.get('volts'):
                ax.text(50, top + 9.5, cfg['volts'], color=GREEN, fontsize=22, weight='bold', ha='center', va='center')
        else:
            ax.plot([47, 47], [top - 4, top + 4], color=FG, lw=4, zorder=4)
            ax.plot([53, 53], [top - 2, top + 2], color=FG, lw=4, zorder=4)
            ax.plot([44, 47], [top, top], color=FG, lw=3); ax.plot([53, 56], [top, top], color=FG, lw=3)
            ax.text(43, top + 3.5, '+', color=FG, fontsize=20, ha='center', weight='bold')
            ax.text(57, top + 3.5, '−', color=FG, fontsize=22, ha='center', weight='bold')
            ax.text(50, top + 7, 'DC power supply', color=SOFT, fontsize=16, ha='center')
    if 'roles' in show:
        for side, x, col in ((cfg['left'], xl, C2), (cfg['right'], xr, GREEN)):
            ax.text(x, 33.5, side['role'].upper(), color=BG, fontsize=15, weight='bold', ha='center', va='center',
                    bbox=dict(boxstyle='round,pad=0.25', fc=col, ec='none'), zorder=6)
    if 'polarity' in show:
        for side, x in ((cfg['left'], xl), (cfg['right'], xr)):
            ax.text(x + (4.5 if not single else 4.5), 20, side['pol'], color=BG, fontsize=22, weight='bold', ha='center',
                    va='center', bbox=dict(boxstyle='circle,pad=0.12', fc=YELLOW, ec='none'), zorder=6)
    if 'ions' in show:
        for side in (cfg['left'], cfg['right']):
            for txt, kind, x, y in side.get('ions', []):
                ax.text(x, y, txt, color=C1 if kind == 'c' else SOFT, fontsize=18, ha='center', va='center', zorder=4,
                        bbox=dict(boxstyle='round,pad=0.15', fc=LIQ, ec='none'))
    if 'bridge' in show and not single:
        b = cfg.get('bridge')
        if b:
            ax.plot([35, 35, 65, 65], [22, 38, 38, 22], color='#8aa0c0', lw=14, solid_capstyle='butt', zorder=2)
            ax.plot([35, 35, 65, 65], [22, 38, 38, 22], color=LIQ, lw=8, solid_capstyle='butt', zorder=2)
            ax.text(50, 41.5, b['label'], color=SOFT, fontsize=16, ha='center', va='center')
    if 'eflow' in show:
        top = 58
        pts1 = [(xl, 40), (xl, top), (44, top)]
        pts2 = [(56, top), (xr, top), (xr, 40)]
        if gal:
            path_dots(ax, [(xl, 40), (xl, top), (xr, top), (xr, 40)], ph, n=7)
        else:
            path_dots(ax, [(xl, 40), (xl, top), (xr, top), (xr, 40)], ph, n=7)
        ax.text(50, top - 10, 'e⁻ flow  →', color=YELLOW, fontsize=18, ha='center', va='center', weight='bold')
    if 'ionflow' in show:
        if single:
            ax.annotate('', (xl + 5, 17), (xl + 13, 17), arrowprops=dict(arrowstyle='-|>', color=SOFT, lw=2.5))
            ax.text(xl + 9, 12.5, 'anions', color=SOFT, fontsize=15, ha='center')
            ax.annotate('', (xr - 5, 17), (xr - 13, 17), arrowprops=dict(arrowstyle='-|>', color=C1, lw=2.5))
            ax.text(xr - 9, 12.5, 'cations', color=C1, fontsize=15, ha='center')
        else:
            b = cfg.get('bridge', {})
            ax.annotate('', (40, 34.5), (50, 34.5), arrowprops=dict(arrowstyle='-|>', color=SOFT, lw=2.5))
            ax.text(45, 31.5, b.get('anion', 'anions'), color=SOFT, fontsize=15, ha='center')
            ax.annotate('', (60, 34.5), (50, 34.5), arrowprops=dict(arrowstyle='-|>', color=C1, lw=2.5))
            ax.text(55, 31.5, b.get('cation', 'cations'), color=C1, fontsize=15, ha='center')
    if 'eq' in show:
        for side, x in ((cfg['left'], xl), (cfg['right'], xr)):
            if side.get('eq'):
                ax.text(x, 0.5 if not single else 0.5, ch(side['eq']), color=YELLOW, fontsize=18, ha='center', va='center',
                        bbox=dict(boxstyle='round,pad=0.25', fc=PANEL, ec=GRID))
    return ax


# ---------------------------------------------------------------- title / thumbnail art
def _title_cell(fig, rect, ph=0):
    C1, C2 = C()
    ax = wax(fig, rect, (0, 100), (0, 110))
    for a, b in ((4, 42), (58, 96)):
        ax.add_patch(Rectangle((a, 6), b - a, 52, fc=LIQ, ec=C1, lw=8, zorder=1))
    for x, col in ((23, ELEC), (77, '#e0864f')):
        ax.add_patch(Rectangle((x - 3.5, 12), 7, 70, fc=col, ec=BG, lw=3, zorder=3))
    ax.plot([23, 23, 77, 77], [82, 100, 100, 82], color=FG, lw=9, zorder=2)
    ax.add_patch(Circle((50, 100), 8, fc=YELLOW, ec=FG, lw=5, zorder=4))
    ax.plot([34, 34, 66, 66], [46, 74, 74, 46], color='#8aa0c0', lw=26, solid_capstyle='butt', zorder=2)
    ax.plot([34, 34, 66, 66], [46, 74, 74, 46], color=LIQ, lw=16, solid_capstyle='butt', zorder=2)
    path_dots(ax, [(23, 82), (23, 100), (77, 100), (77, 82)], ph, n=6, size=900)
    for x, y, t, col in ((12, 40, '−', PINK), (88, 40, '+', GREEN), (11, 20, '2+', C1), (89, 20, '2+', C1)):
        ax.text(x, y, t, color=col, fontsize=56, weight='bold', ha='center', va='center')


def thumbnail(fig):
    C1, C2 = C()
    fig.text(0.04, 0.87, 'CRITERION 5', ha='left', va='center', color=C1, fontsize=64, weight='bold')
    fig.text(0.04, 0.65, 'Electro-', ha='left', va='center', color=FG, fontsize=150, weight='bold')
    fig.text(0.04, 0.42, 'chemistry', ha='left', va='center', color=FG, fontsize=150, weight='bold')
    fig.text(0.04, 0.22, 'TASC Chemistry revision', ha='left', va='center', color=SOFT, fontsize=58)
    _title_cell(fig, [0.60, 0.17, 0.38, 0.76])


# ============================================================================ Part 1: redox
def redox_def(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Oxidation and reduction')
    chip(fig, 'Element 1 · principles')
    items = ['Oxidation: loss of electrons', 'Reduction: gain of electrons', 'Both always happen together: a redox reaction',
             'OIL RIG: Oxidation Is Loss, Reduction Is Gain']
    bullets(fig, items, 4, 0.05, 0.78, size=27, dim=False)
    ax = wax(fig, [0.52, 0.18, 0.44, 0.58], (0, 100), (0, 70))
    # Zn atom gives two electrons to Cu2+ (animated, loops)
    f = (ph * 1.0) % 1.0
    ax.add_patch(Circle((22, 35), 10, fc=C2, ec=BG, lw=2, alpha=0.9))
    ax.text(22, 35, 'Zn', color=BG, fontsize=24, weight='bold', ha='center', va='center')
    ax.add_patch(Circle((78, 35), 10, fc=C1, ec=BG, lw=2, alpha=0.9))
    ax.text(78, 35, 'Cu²⁺', color=BG, fontsize=22, weight='bold', ha='center', va='center')
    if s >= 1:
        for k, off in enumerate((-3, 3)):
            x = 32 + (46 - 8) * np.clip(f * 1.2 - 0.1 * k, 0, 1)
            ax.scatter([x], [35 + off + 6 * np.sin(TAU * f + k)], s=200, color=YELLOW, edgecolor=BG, zorder=6)
        ax.text(50, 50, '2e⁻', color=YELLOW, fontsize=24, weight='bold', ha='center')
        ax.text(22, 18, 'REDUCER\nloses e⁻: oxidised', color=C2, fontsize=18, ha='center', va='center', weight='bold')
        ax.text(78, 18, 'OXIDISER\ngains e⁻: reduced', color=C1, fontsize=18, ha='center', va='center', weight='bold')
        ax.text(50, 5, ch('Zn -> Zn^2+ + 2e^-      Cu^2+ + 2e^- -> Cu'), color=SOFT, fontsize=19, ha='center')
    if s >= 2:
        card(fig, 0.05, 0.14, 0.44, 0.22, 'Careful', 'The reducer is oxidised; the oxidiser is reduced.\nMetals are reducers. Metal ions are oxidisers.', tcol=PINK, size=21)


def shells(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Why atoms lose or gain electrons')
    chip(fig, 'Element 1 · principles')
    ax = wax(fig, [0.05, 0.14, 0.50, 0.66], (0, 100), (0, 66))
    ax.set_aspect('equal')

    def atom(cx, cy, conf, name, col, ion=None):
        for i, n in enumerate(conf):
            r = 5 + 4.5 * (i + 1)
            ax.add_patch(Circle((cx, cy), r, fc='none', ec=GRID, lw=2))
            for k in range(n):
                a = TAU * k / max(n, 1) + i
                ax.scatter([cx + r * np.cos(a)], [cy + r * np.sin(a)], s=70, color=YELLOW if i == len(conf) - 1 else SOFT, zorder=5)
        ax.add_patch(Circle((cx, cy), 4, fc=col, ec=BG))
        ax.text(cx, cy, name, color=BG, fontsize=15, weight='bold', ha='center', va='center')
    if s == 0:
        atom(22, 33, [2, 8, 1], 'Na', C2); ax.text(22, 4, 'Na  2,8,1\nloses 1 e⁻ → Na⁺ (2,8)', color=FG, fontsize=17, ha='center')
        atom(70, 33, [2, 8, 7], 'Cl', C1); ax.text(70, 4, 'Cl  2,8,7\ngains 1 e⁻ → Cl⁻ (2,8,8)', color=FG, fontsize=17, ha='center')
    else:
        atom(22, 33, [2, 8, 3], 'Al', C2); ax.text(22, 4, 'Al  2,8,3\nloses 3 e⁻ → Al³⁺ (2,8)', color=FG, fontsize=17, ha='center')
        atom(70, 33, [2, 6], 'O', C1); ax.text(70, 4, 'O  2,6\ngains 2 e⁻ → O²⁻ (2,8)', color=FG, fontsize=17, ha='center')
    items = ['Valence (outer shell) electrons decide it', 'A full outer shell is stable: lower energy',
             'Few valence electrons: lose them, so a reducer (metals, left of the table)',
             'Nearly full shell: gain electrons, so an oxidiser (non-metals, right)',
             'Down a group, outer electrons are further out and\nshielded: easier to lose, so stronger reducers']
    n = [2, 3, 5][min(s, 2)] if s < 3 else 5
    n = {0: 2, 1: 3, 2: 5}.get(s, 5)
    bullets(fig, [fit(ch(i), 0.38, 22) for i in items], n, 0.57, 0.78, size=22, gap=0.018)


# ============================================================================ Part 2: electrochemical series
ECS = [('F₂ + 2e⁻ ⇌ 2F⁻', +2.87), ('MnO₄⁻ + 8H⁺ + 5e⁻ ⇌ Mn²⁺ + 4H₂O', +1.49), ('Cl₂ + 2e⁻ ⇌ 2Cl⁻', +1.36),
       ('O₂ + 4H⁺ + 4e⁻ ⇌ 2H₂O', +1.23), ('Ag⁺ + e⁻ ⇌ Ag', +0.80), ('Fe³⁺ + e⁻ ⇌ Fe²⁺', +0.77),
       ('Cu²⁺ + 2e⁻ ⇌ Cu', +0.34), ('2H⁺ + 2e⁻ ⇌ H₂', 0.00), ('Sn²⁺ + 2e⁻ ⇌ Sn', -0.14), ('Zn²⁺ + 2e⁻ ⇌ Zn', -0.76),
       ('2H₂O + 2e⁻ ⇌ 2OH⁻ + H₂', -0.83), ('Mg²⁺ + 2e⁻ ⇌ Mg', -2.38), ('Li⁺ + e⁻ ⇌ Li', -3.05)]


def _ecs_rows(fig, ax_x, y0, rows, hl=(), size=20, dy=0.047, w=0.55):
    for i, (t, e) in enumerate(rows):
        y = y0 - i * dy
        col = YELLOW if i in hl else SOFT
        if i in hl:
            box(fig, ax_x - 0.01, y - dy / 2 + 0.003, w, dy - 0.004, fc=PANEL2)
        T(fig, ax_x, y, t, size=size, color=col, va='center')
        T(fig, ax_x + w - 0.03, y, f'{e:+.2f}'.replace('-', '−') if e else '0.00', size=size, color=col, va='center', ha='right')


def ecs(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The electrochemical series')
    chip(fig, 'Element 3 · series and data')
    T(fig, 0.05, 0.805, 'Reduction half-equation', size=19, color=MUT)
    T(fig, 0.555, 0.805, 'E° (V)', size=19, color=MUT, ha='right')
    hl = {0: (), 1: (4, 6, 9), 2: (4, 6, 9)}[min(s, 2)]
    _ecs_rows(fig, 0.06, 0.755, ECS, hl=hl, size=20, dy=0.046)
    sheet_tag(fig, 0.05, 0.115, 'Standard reduction potentials')
    T(fig, 0.60, 0.805, 'an excerpt: the sheet has more rows', size=17, color=MUT)
    ax = wax(fig, [0.60, 0.12, 0.35, 0.62], (0, 100), (0, 100))
    ax.annotate('', (10, 8), (10, 92), arrowprops=dict(arrowstyle='-|>', color=C1, lw=4))
    ax.text(14, 90, 'stronger oxidisers\n(species on the left\nof the arrow)', color=C1, fontsize=17, va='top')
    ax.annotate('', (10, 92), (10, 8), arrowprops=dict(arrowstyle='-|>', color=C2, lw=4))
    ax.text(14, 12, 'stronger reducers\n(species on the right)', color=C2, fontsize=17, va='bottom')
    if s >= 1:
        ax.text(50, 56, ch('Ag^+ + Cu -> ?'), color=YELLOW, fontsize=23, ha='left')
        ax.text(50, 48, 'Ag⁺ is above Cu.\nOxidiser high,\nreducer lower:\nspontaneous', color=GREEN, fontsize=17, ha='left', va='top')


def she(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Where the series comes from')
    chip(fig, 'Element 1 · principles')
    ax = wax(fig, [0.04, 0.12, 0.50, 0.68], (0, 100), (0, 80))
    ax.add_patch(Rectangle((18, 6), 40, 40, fc=LIQ, ec=MUT, lw=3))
    ax.add_patch(Rectangle((36, 22), 4, 36, fc='#d9d9d9', ec=BG))
    ax.text(38, 62, 'platinum\nelectrode', color=FG, fontsize=17, ha='center', va='center')
    ax.add_patch(Rectangle((30, 40), 16, 14, fc='none', ec=SOFT, lw=2, ls='--'))
    ax.text(10, 42, 'H₂ gas\n1 atm', color=SOFT, fontsize=16, ha='center')
    ax.text(38, 12, ch('H^+(aq) 1 mol L^-1'), color=C1, fontsize=17, ha='center')
    for k in range(5):
        ax.scatter([38 + 2 + 2 * k % 5], [28 + 3 * ((k + int(ph * 4)) % 5)], s=40, color=SOFT)
    ax.text(38, 74, ch('2H^+(aq) + 2e^- <=> H_2(g)      E° = 0.00 V'), color=YELLOW, fontsize=19, ha='center')
    if s >= 1:
        ax.annotate('', (78, 40), (62, 40), arrowprops=dict(arrowstyle='<->', color=FG, lw=2.5))
        ax.text(78, 46, 'V', color=YELLOW, fontsize=24, ha='center', weight='bold')
    items = ['The standard hydrogen half-cell: Pt electrode, H₂ at 1 atm,\nH⁺ at 1 mol L⁻¹, 25 °C. Defined as 0.00 V',
             'Connect any other half-cell (1 mol L⁻¹, 25 °C) to it and\nmeasure the voltage: that is its E°',
             'Zn²⁺|Zn reads −0.76 V (Zn pushes electrons to H⁺).\nCu²⁺|Cu reads +0.34 V (Cu²⁺ takes them from H₂)',
             'Line up all the values: the electrochemical series']
    n = {0: 1, 1: 2, 2: 4}.get(s, 4)
    side_notes(fig, items, n - 1, x=0.57, w=0.38, size=21, last_bright=True)


def variations(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Why real results can differ from the series')
    chip(fig, 'Element 3 · series and data')
    cards = [('Not standard conditions', 'The series is for 1 mol L⁻¹, 25 °C, 1 atm. Other concentrations\nshift the potential: dilute oxidiser, weaker oxidiser.', C1),
             ('Spontaneous is not fast', 'E°cell > 0 only says a reaction can happen. Some are\nso slow that nothing is seen (activation energy).', C2),
             ('A surface layer', 'Aluminium is a strong reducer but a thin oxide layer\nstops it reacting, so it seems unreactive.', PINK),
             ('Overpotential', 'Producing a gas such as O₂ at an electrode can\nneed extra voltage, so the product predicted can differ.', GREEN)]
    n = min(4, s + 1)
    for i in range(n):
        x = 0.05 + (i % 2) * 0.46; y = 0.50 - (i // 2) * 0.32
        card(fig, x, y, 0.44, 0.29, cards[i][0], ch(cards[i][1]), tcol=cards[i][2], size=20)


# ============================================================================ Part 3: galvanic cells
ZN_CU = dict(mode='galvanic',
             left=dict(name='Zn(s)', role='anode', pol='−', sol=ch('ZnSO_4(aq)'), ecol='#9fb0c6',
                       ions=[('Zn²⁺', 'c', 15, 20), ('SO₄²⁻', 'a', 33, 14)], eq='Zn(s) → Zn²⁺(aq) + 2e⁻'),
             right=dict(name='Cu(s)', role='cathode', pol='+', sol=ch('CuSO_4(aq)'), ecol='#e0864f',
                        ions=[('Cu²⁺', 'c', 65, 20), ('SO₄²⁻', 'a', 85, 14)], eq='Cu²⁺(aq) + 2e⁻ → Cu(s)'),
             bridge=dict(label='salt bridge (KNO₃)', anion='NO₃⁻', cation='K⁺'), volts='+1.10 V')


def galvanic(fig, s, ph):
    C1, C2 = C()
    header(fig, 'A galvanic cell: zinc and copper')
    chip(fig, 'Element 4 · cell diagrams')
    sets = [{'vessel', 'electrodes'}, {'vessel', 'electrodes', 'roles', 'polarity', 'eq', 'ions', 'wire'},
            {'vessel', 'electrodes', 'roles', 'polarity', 'eq', 'ions', 'wire', 'eflow'},
            {'vessel', 'electrodes', 'roles', 'polarity', 'eq', 'ions', 'wire', 'eflow', 'bridge', 'ionflow'},
            {'vessel', 'electrodes', 'roles', 'polarity', 'eq', 'ions', 'wire', 'eflow', 'bridge', 'ionflow', 'device_val'}]
    cell(fig, [0.04, 0.10, 0.62, 0.70], ZN_CU, sets[min(s, 4)], ph)
    notes = [None, 'Anode: oxidation (Zn loses e⁻).\nCathode: reduction (Cu²⁺ gains e⁻).\nIn a galvanic cell the anode is −, the cathode +.',
             'Electrons leave the anode, travel\nthrough the external circuit (wire),\nand enter the cathode.',
             'Anions move towards the anode,\ncations towards the cathode, through\nthe salt bridge. This keeps each half-cell\nelectrically neutral and completes the circuit.',
             ch('E°cell = 0.34 − (−0.76) = 1.10 V\nA spontaneous redox reaction\nmakes the electrical energy.')]
    if s >= 1 and notes[min(s, 4)]:
        card(fig, 0.68, 0.30, 0.28, 0.42, 'Reading the diagram', fit(notes[min(s, 4)], 0.25, 20), tcol=C2, size=20)


def lead_acid(fig, s, ph):
    C1, C2 = C()
    header(fig, 'One electrolyte: no salt bridge needed')
    chip(fig, 'Element 4 · cell diagrams')
    cfg = dict(mode='galvanic', single=True,
               left=dict(name='Pb', role='anode', pol='−', ecol='#9fb0c6', sol=ch('H_2SO_4(aq)'),
                         ions=[('HSO₄⁻', 'a', 27, 17)]),
               right=dict(name='PbO₂ on Pb', role='cathode', pol='+', ecol='#6b3a3a', ions=[('H⁺', 'c', 73, 17)]),
               volts='+2.25 V')
    show = {'vessel', 'electrodes', 'roles', 'polarity', 'ions', 'wire'}
    if s >= 1:
        show |= {'eflow', 'ionflow', 'device_val'}
    cell(fig, [0.04, 0.10, 0.58, 0.70], cfg, show, ph)
    items = ['Both electrodes sit in the same sulfuric acid,\nso ions can move between them directly',
             'The two products (PbSO₄ solid) stay on the plates,\nso there is no mixing problem',
             'Cathode and anode still obey the same rules:\nanode −, oxidation; cathode +, reduction',
             'Draw only species that are really present:\nHSO₄⁻ and H⁺, not Pb²⁺ or O²⁻']
    n = {0: 2, 1: 4}.get(s, 4)
    side_notes(fig, items, n - 1, x=0.64, w=0.31, size=20)


def inert_cell(fig, s, ph):
    C1, C2 = C()
    header(fig, 'A cell with an inert electrode')
    chip(fig, 'Element 4 · unfamiliar cells')
    cfg = dict(mode='galvanic',
               left=dict(name='Pt', role='anode', pol='−', sol=ch('Sn^2+, Sn^4+'), ecol='#d9d9d9',
                         ions=[('Sn²⁺', 'c', 12, 22), ('Sn⁴⁺', 'c', 37, 15), ('Cl⁻', 'a', 12, 14)],
                         eq='Sn²⁺ → Sn⁴⁺ + 2e⁻'),
               right=dict(name='Ag(s)', role='cathode', pol='+', sol=ch('AgNO_3(aq)'), ecol='#e5e5e5',
                          ions=[('Ag⁺', 'c', 65, 20), ('NO₃⁻', 'a', 85, 14)], eq='Ag⁺ + e⁻ → Ag(s)'),
               bridge=dict(label='salt bridge (NaNO₃)', anion='NO₃⁻', cation='Na⁺'), volts='+0.65 V')
    sets = [{'vessel', 'electrodes', 'ions'}, {'vessel', 'electrodes', 'ions', 'roles', 'polarity', 'wire', 'eq'},
            {'vessel', 'electrodes', 'ions', 'roles', 'polarity', 'wire', 'eq', 'eflow', 'bridge', 'ionflow', 'device_val'}]
    cell(fig, [0.04, 0.10, 0.62, 0.70], cfg, sets[min(s, 2)], ph)
    items = ['Sn²⁺ and Sn⁴⁺ are both in solution, so there is\nno tin metal to use: a platinum rod carries the electrons',
             'Pt is inert: it does not react. It is only a conductor.',
             ch('Ag^+ is the stronger oxidiser (0.80 V), so Ag^+|Ag is\nthe cathode. Sn^2+ is oxidised at the Pt anode.')]
    side_notes(fig, items, s, x=0.68, w=0.28, size=20)


# ============================================================================ Part 4: electrolysis
def electrolytic(fig, s, ph):
    C1, C2 = C()
    header(fig, 'An electrolytic cell: molten lead(II) bromide')
    chip(fig, 'Element 4 · cell diagrams')
    cfg = dict(mode='electrolytic', single=True,
               left=dict(name='graphite', role='anode', pol='+', ecol='#444c5c', sol=ch('molten PbBr_2'),
                         ions=[('Br⁻', 'a', 29, 17)], eq='2Br⁻(l) → Br₂(g) + 2e⁻'),
               right=dict(name='graphite', role='cathode', pol='−', ecol='#444c5c', ions=[('Pb²⁺', 'c', 71, 17)],
                          eq='Pb²⁺(l) + 2e⁻ → Pb(l)'))
    sets = [{'vessel', 'electrodes', 'wire', 'ions'}, {'vessel', 'electrodes', 'wire', 'ions', 'roles', 'polarity', 'eflow'},
            {'vessel', 'electrodes', 'wire', 'ions', 'roles', 'polarity', 'eflow', 'ionflow'},
            {'vessel', 'electrodes', 'wire', 'ions', 'roles', 'polarity', 'eflow', 'ionflow', 'eq'}]
    cell(fig, [0.04, 0.10, 0.60, 0.70], cfg, sets[min(s, 3)], ph)
    items = ['A power supply drives a non-spontaneous reaction.\nIt pulls electrons off the anode and pushes\nthem onto the cathode',
             'So the polarity is the reverse of a galvanic cell:\nanode +, cathode −. Oxidation is still at the anode',
             'Cations go to the cathode, anions to the anode',
             ch('Minimum voltage: E°cell = (−1.09) + (−0.13)\n= −1.22 V, so the supply must exceed 1.22 V')]
    side_notes(fig, items, s, x=0.66, w=0.30, size=21)


def plating(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Electroplating: nickel on a steel key')
    chip(fig, 'Element 4 · unfamiliar cells')
    cfg = dict(mode='electrolytic', single=True,
               left=dict(name='Ni(s)', role='anode', pol='+', ecol='#c9d2c4', sol=ch('NiSO_4(aq)'),
                         ions=[('SO₄²⁻', 'a', 28, 17)], eq='Ni(s) → Ni²⁺(aq) + 2e⁻'),
               right=dict(name='steel key', role='cathode', pol='−', ecol='#7f8896', ions=[('Ni²⁺', 'c', 73, 17)],
                          eq='Ni²⁺(aq) + 2e⁻ → Ni(s)'))
    sets = [{'vessel', 'electrodes', 'wire', 'ions'}, {'vessel', 'electrodes', 'wire', 'ions', 'roles', 'polarity', 'eflow', 'ionflow', 'eq'}]
    cell(fig, [0.04, 0.10, 0.60, 0.70], cfg, sets[min(s, 1)], ph)
    items = ['The object to be coated is the cathode (−)', 'The plating metal is the anode (+)',
             'The electrolyte contains ions of the plating metal', 'Anode dissolves, and the same amount deposits on the cathode:\nthe solution stays about the same']
    side_notes(fig, items, s, x=0.66, w=0.30, size=21, per=2)


# ============================================================================ Part 5: corrosion
def rust_cell(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Rusting is an electrochemical cell')
    chip(fig, 'Element 5 · corrosion')
    ax = wax(fig, [0.04, 0.12, 0.58, 0.68], (0, 100), (0, 66))
    # iron surface with a water drop; centre = anode (low O2), edge = cathode (high O2)
    ax.add_patch(Rectangle((5, 6), 90, 12, fc='#6b7584', ec=BG, lw=2))
    ax.text(50, 12, 'iron / steel', color=FG, fontsize=20, ha='center', va='center')
    th = np.linspace(0, np.pi, 60)
    ax.fill(50 + 36 * np.cos(th), 18 + 22 * np.sin(th), color='#2a5f8f', alpha=0.75, zorder=2)
    ax.text(50, 46, 'water drop with dissolved ions', color=SOFT, fontsize=16, ha='center')
    if s >= 1:
        ax.text(14, 24, 'CATHODE', color=BG, fontsize=14, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=0.25', fc=GREEN, ec='none'), zorder=6)
        ax.text(86, 24, 'CATHODE', color=BG, fontsize=14, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=0.25', fc=GREEN, ec='none'), zorder=6)
        ax.text(50, 24, 'ANODE', color=BG, fontsize=14, weight='bold', ha='center', va='center', bbox=dict(boxstyle='round,pad=0.25', fc=C2, ec='none'), zorder=6)
        ax.text(14, 56, 'more O₂\n(drop edge)', color=SOFT, fontsize=16, ha='center'); ax.text(50, 58.5, 'less O₂ (centre)', color=SOFT, fontsize=16, ha='center')
        ax.annotate('', (16, 55), (22, 40), arrowprops=dict(arrowstyle='-|>', color=SOFT, lw=2))
    if s >= 2:
        ax.annotate('', (22, 8), (46, 8), arrowprops=dict(arrowstyle='<|-', color=YELLOW, lw=3))
        ax.text(34, 3.5, 'e⁻ through the metal', color=YELLOW, fontsize=15, ha='center')
        ax.text(31, 36, 'OH⁻', color=SOFT, fontsize=17, ha='center'); ax.annotate('', (44, 33), (35, 36), arrowprops=dict(arrowstyle='-|>', color=SOFT, lw=2))
        ax.text(69, 36, 'Fe²⁺', color=C1, fontsize=17, ha='center'); ax.annotate('', (62, 33), (66, 36), arrowprops=dict(arrowstyle='<|-', color=C1, lw=2))
        ax.text(50, 0.5, 'ions move through the water', color=SOFT, fontsize=15, ha='center')
    notes = ['Needs iron, oxygen, water.\nWater with ions (an electrolyte)\nspeeds it up.',
             'Where O₂ is plentiful the metal is the cathode.\nWhere O₂ is scarce it is the anode.\nThis is differential aeration.',
             ch('Anode (oxidation):\nFe(s) -> Fe^2+(aq) + 2e^-\nCathode (reduction):\nO_2(g) + 2H_2O(l) + 4e^- -> 4OH^-(aq)\nThen Fe^2+ is oxidised to rust.')]
    side_notes(fig, notes, s, x=0.64, w=0.32, size=22)


def two_metals(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Two metals in contact')
    chip(fig, 'Element 5 · corrosion')
    ax = wax(fig, [0.04, 0.12, 0.58, 0.68], (0, 100), (0, 66))
    ax.add_patch(Rectangle((5, 20), 42, 14, fc='#6b7584', ec=BG, lw=2)); ax.text(26, 27, 'steel pipe', color=FG, fontsize=20, ha='center', va='center')
    ax.add_patch(Rectangle((50, 20), 45, 14, fc='#c47a3f', ec=BG, lw=2)); ax.text(72, 27, 'copper pipe', color=BG, fontsize=20, weight='bold', ha='center', va='center')
    ax.add_patch(Rectangle((5, 12), 90, 8, fc='#2a5f8f', alpha=0.7)); ax.text(50, 14.5, 'water with dissolved ions (electrolyte)', color=FG, fontsize=15, ha='center')
    if s >= 1:
        ax.text(26, 40, ch('ANODE: Fe -> Fe^2+ + 2e^-'), color=BG, fontsize=15, weight='bold', ha='center', bbox=dict(boxstyle='round,pad=0.25', fc=C2, ec='none'))
        ax.text(72, 40, ch('CATHODE: O_2 + 2H_2O + 4e^- -> 4OH^-'), color=BG, fontsize=15, weight='bold', ha='center', bbox=dict(boxstyle='round,pad=0.25', fc=GREEN, ec='none'))
        ax.annotate('', (62, 36), (38, 36), arrowprops=dict(arrowstyle='-|>', color=YELLOW, lw=3)); ax.text(50, 47, 'e⁻ flow', color=YELLOW, fontsize=19, ha='center', weight='bold')
    if s >= 2:
        ax.text(26, 5, 'iron wastes away', color=PINK, fontsize=18, ha='center', weight='bold')
        ax.text(72, 5, 'copper is protected', color=GREEN, fontsize=18, ha='center', weight='bold')
    notes = ['Different metals in contact in a damp environment form a galvanic cell.',
             'The stronger reducer (more negative E°, so Fe not Cu) is oxidised: it is the anode. The other is the cathode.',
             'The contact must conduct: a layer of paper or wool between them breaks the circuit, so there is little extra corrosion.']
    side_notes(fig, notes, s, x=0.64, w=0.32, size=22)


def protect_diagram(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Cathodic protection')
    chip(fig, 'Element 5 · prevention')
    ax = wax(fig, [0.04, 0.14, 0.45, 0.60], (0, 100), (0, 60))
    ax.text(50, 56, 'Sacrificial anode', color=C2, fontsize=24, ha='center', weight='bold')
    ax.add_patch(Rectangle((2, 4), 96, 26, fc='#5a4a38', ec=BG)); ax.text(6, 7, 'soil (electrolyte)', color=SOFT, fontsize=17)
    ax.add_patch(Rectangle((8, 12), 64, 11, fc='#7f8896', ec=BG)); ax.text(40, 17.5, 'buried steel pipe', color=FG, fontsize=19, ha='center', va='center')
    ax.add_patch(Rectangle((84, 8), 8, 18, fc='#d7dbe6', ec=BG)); ax.text(88, 28.5, 'Mg block', color=FG, fontsize=17, ha='center')
    ax.plot([72, 84], [17.5, 17.5], color=FG, lw=3)
    ax.annotate('', (74, 40), (84, 40), arrowprops=dict(arrowstyle='<|-', color=YELLOW, lw=3)); ax.text(79, 44, 'e⁻', color=YELLOW, fontsize=20, ha='center', weight='bold')
    ax.text(50, 49, 'Mg is oxidised (anode); the steel is the cathode', color=SOFT, fontsize=17, ha='center')
    if s >= 1:
        ax2 = wax(fig, [0.52, 0.14, 0.45, 0.60], (0, 100), (0, 60))
        ax2.text(50, 56, 'Applied EMF', color=C1, fontsize=24, ha='center', weight='bold')
        ax2.add_patch(Rectangle((2, 4), 96, 26, fc='#5a4a38', ec=BG)); ax2.text(6, 7, 'soil', color=SOFT, fontsize=17)
        ax2.add_patch(Rectangle((8, 12), 56, 11, fc='#7f8896', ec=BG)); ax2.text(36, 17.5, 'steel pipe', color=FG, fontsize=19, ha='center', va='center')
        ax2.add_patch(Rectangle((82, 8), 8, 18, fc='#2f3745', ec=BG)); ax2.text(86, 28.5, 'inert anode', color=FG, fontsize=17, ha='center')
        ax2.plot([64, 70], [17.5, 17.5], color=FG, lw=3); ax2.plot([70, 70], [17.5, 40], color=FG, lw=3)
        ax2.plot([70, 86], [40, 40], color=FG, lw=3); ax2.plot([86, 86], [40, 26], color=FG, lw=3)
        ax2.plot([76, 76], [37, 43], color=FG, lw=4); ax2.plot([80, 80], [38.5, 41.5], color=FG, lw=4)
        ax2.text(73, 44.5, '−', color=FG, fontsize=20, ha='center', weight='bold'); ax2.text(82, 44.5, '+', color=FG, fontsize=20, ha='center', weight='bold')
        ax2.text(50, 49, 'DC supply: − to the pipe, + to the anode', color=SOFT, fontsize=17, ha='center')


# ============================================================================ finish
def tips_slide():
    pass
