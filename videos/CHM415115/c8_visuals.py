"""Draw functions for CHM415115 Criterion 8 (quantitative chemical problems).  draw(fig, s, ph): s = step, ph = phase."""
import numpy as np
from matplotlib.patches import Rectangle, Polygon, Circle, FancyBboxPatch

from explainer import layout as L
from explainer.layout import (header, T, bullets, box, card, chip, wax, gax, frac, FG, SOFT, MUT, GRID, PANEL, PANEL2, BG,
                              PINK, GREEN, YELLOW, TAU)
from explainer.spec import import_sibling

_CC = import_sibling(__file__, 'chm_common.py')
Slide, Seq, Phased, C, ch, fit = _CC.Slide, _CC.Seq, _CC.Phased, _CC.C, _CC.ch, _CC.fit


def side_notes(fig, notes, s, x=0.62, w=0.34, size=21, y=0.78, per=1):
    n = min(len(notes), (s + 1) * per)
    for i in range(n):
        t = fit(ch(notes[i]), w, size)
        T(fig, x, y, t, size=size, color=FG if i == n - 1 else SOFT)
        y -= frac(size) * (t.count('\n') + 1) + 0.03


# ============================================================================ the moles roadmap
def roadmap(fig, s, ph):
    C1, C2 = C()
    header(fig, 'The moles roadmap')
    chip(fig, 'Element 2 · stoichiometry')
    ax = wax(fig, [0.04, 0.14, 0.58, 0.64], (0, 100), (0, 64))
    boxes = {'m': (12, 50, 'mass, m (g)'), 'n': (50, 32, 'amount, n (mol)'), 'V': (88, 50, 'solution volume, V (L)'),
             'c': (88, 14, 'concentration, c'), 'N': (12, 14, 'particles, N'), 'g': (50, 6, 'gas: V, P, T')}
    show = {0: ['n', 'm'], 1: ['n', 'm', 'V', 'c'], 2: ['n', 'm', 'V', 'c', 'N', 'g']}[min(s, 2)]
    for k in show:
        x, y, t = boxes[k]
        ax.text(x, y, t, color=BG, fontsize=17, weight='bold', ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.4', fc=C1 if k != 'n' else C2, ec='none'), zorder=4)

    def ar(a, b, lab, off=(0, 2.4)):
        (x1, y1), (x2, y2) = boxes[a][:2], boxes[b][:2]
        ax.annotate('', (x2, y2), (x1, y1), arrowprops=dict(arrowstyle='<|-|>', color=SOFT, lw=2.2, shrinkA=30, shrinkB=30))
        ax.text((x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1], lab, color=YELLOW, fontsize=16, ha='center', va='center',
                bbox=dict(fc=BG, ec='none', pad=0.8))
    ar('m', 'n', 'n = m / M')
    if s >= 1:
        ar('n', 'c', 'c = n / V', off=(1.5, 0)) if False else None
        ar('c', 'V', 'n = c × V', off=(4.5, 0))
        ar('n', 'V', '', off=(0, 0)) if False else None
        ax.annotate('', (80, 28), (60, 32), arrowprops=dict(arrowstyle='<|-|>', color=SOFT, lw=2.2))
        ax.text(70, 33, 'n = cV', color=YELLOW, fontsize=16, ha='center', bbox=dict(fc=BG, ec='none', pad=0.8))
    if s >= 2:
        ar('n', 'N', 'N = n × NA', off=(0, 3))
        ar('n', 'g', 'PV = nRT\nor n = V / Vm', off=(10, 0))
    notes = ['Everything goes through moles. Mass to moles with the molar mass from the information sheet, n = m / M',
             'For solutions: c = n / V with the volume in LITRES. Moles of solute = concentration × volume. Include the water in a hydrate’s molar mass',
             'Particles: N = n × NA. Gases: PV = nRT, or molar volume 24.5 L at SLC and 22.4 L at STP (also on the sheet). Always convert units first']
    side_notes(fig, notes, s, x=0.65, w=0.31)
    _CC.sheet_tag(fig, 0.65, 0.19, 'Chemical Information')


def stoich_steps(fig, s, ph):
    C1, C2 = C()
    header(fig, 'A method for every calculation')
    chip(fig, 'Element 2 · stoichiometry')
    steps = [('1', 'Write the balanced equation (and the half-equations if redox)', C1),
             ('2', 'Convert what is GIVEN to moles of one species: n = m/M, c × V, PV/RT', C2),
             ('3', 'Use the mole RATIO from the equation to find moles of the species WANTED', PINK),
             ('4', 'Convert to the quantity asked: mass, concentration, volume, percentage', GREEN),
             ('5', 'Check: units, sign, s.f., and is it realistic? Write the value with its unit', YELLOW)]
    n = min(5, s + 2) if s < 3 else 5
    for i in range(n):
        y = 0.72 - i * 0.115
        box(fig, 0.05, y - 0.047, 0.90, 0.094, fc=PANEL)
        T(fig, 0.07, y, steps[i][0], size=32, color=steps[i][2], weight='bold', va='center')
        T(fig, 0.11, y, fit(ch(steps[i][1]), 0.82, 24), size=24, va='center')
    T(fig, 0.05, 0.12, 'Write what each number is: n(HCl), c(NaOH), m(Fe). Numbers without context lose marks', size=21, color=YELLOW)


# ============================================================================ titration
def apparatus(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Titration apparatus and terms')
    chip(fig, 'Element 1 · volumetric analysis')
    ax = wax(fig, [0.03, 0.12, 0.40, 0.70], (0, 60), (0, 80))
    # burette
    ax.add_patch(Rectangle((26, 36), 6, 40, fc='#13304f', ec=FG, lw=2.5))
    for k in range(9):
        ax.plot([26, 28], [38 + 4 * k, 38 + 4 * k], color=FG, lw=1.5)
    ax.plot([26, 32], [36, 36], color=FG, lw=2)
    ax.add_patch(Polygon([[28, 36], [30, 36], [29.2, 31], [28.8, 31]], fc=FG, ec='none'))
    ax.text(40, 66, 'burette\n(titrant)', color=SOFT, fontsize=17, ha='left')
    # drop
    if s >= 1:
        y = 30 - (ph * 4 if s >= 1 else 0)
        ax.add_patch(Circle((29, y), 0.9, fc=C1, ec='none'))
    # flask
    ax.add_patch(Polygon([[21, 24], [37, 24], [44, 4], [14, 4]], fc='#2a5f8f' if s < 3 else '#a8326c', ec=FG, lw=2.5, alpha=0.9))
    ax.plot([24, 24, 34, 34], [24, 28, 28, 24], color=FG, lw=2.5)
    ax.text(29, 13, 'analyte +\nindicator', color=FG, fontsize=16, ha='center', va='center', weight='bold')
    ax.text(8, 20, 'conical\nflask', color=SOFT, fontsize=17, ha='center')
    # pipette
    ax.add_patch(Rectangle((2, 44), 3, 30, fc='#13304f', ec=FG, lw=2))
    ax.add_patch(Circle((3.5, 56), 3.6, fc='#13304f', ec=FG, lw=2))
    ax.text(3.5, 78, 'pipette\n(aliquot)', color=SOFT, fontsize=16, ha='center')
    items = ['A pipette measures an exact volume of one solution (the aliquot) into a conical flask, with a few drops of indicator. The burette delivers the other solution',
             'Add titrant until the indicator just changes colour: the END POINT. It should match the EQUIVALENCE POINT, where the reactants are in exactly the mole ratio of the equation',
             'Repeat until three titres agree (concordant, within about 0.1 mL). Average only those. Rinse the burette with the titrant and the pipette with its own solution',
             'Primary standard: weighed accurately to make a standard solution of known concentration, used to find the concentration of the titrant']
    side_notes(fig, items, s, x=0.47, w=0.49, size=21)


def ph_curve(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Indicators and the equivalence point')
    chip(fig, 'Element 1 · volumetric analysis')
    ax = gax(fig, [0.07, 0.15, 0.50, 0.62], (0, 40), (0, 14), 'Volume of NaOH added (mL)', 'pH')
    v = np.linspace(0.1, 40, 600)
    # strong acid / strong base: 25 mL of 0.1 M HCl with 0.1 M NaOH
    n_h = 25 * 0.1; n_oh = v * 0.1
    tot = 25 + v
    h = np.where(n_h > n_oh, (n_h - n_oh) / tot, 1e-14 / ((n_oh - n_h) / tot + 1e-30))
    h = np.where(np.abs(n_h - n_oh) < 1e-4, 1e-7, h)
    ph_sa = -np.log10(h)
    ax.plot(v, ph_sa, color=C1, lw=4)
    ax.text(3, 1.6, 'strong acid + strong base', color=C1, fontsize=17)
    ax.axvline(25, color=GRID, lw=1.5, ls=':')
    ax.text(25.6, 1.0, 'equivalence point', color=YELLOW, fontsize=16)
    if s >= 1:
        ax.axhspan(8.2, 10.0, color=PINK, alpha=0.25); ax.text(1, 9.0, 'phenolphthalein 8.2–10', color=PINK, fontsize=16)
        ax.axhspan(3.1, 4.4, color=GREEN, alpha=0.25); ax.text(1, 3.4, 'methyl orange 3.1–4.4', color=GREEN, fontsize=16)
    if s >= 2:
        ka = 1.74e-5
        va = np.linspace(0.1, 40, 600)
        # weak acid HA 25 mL 0.1 M with 0.1 M NaOH (approximation, Henderson-Hasselbalch before EP)
        n_ha = 2.5; n_b = va * 0.1
        ph_wa = np.where(n_b < n_ha - 1e-6, -np.log10(ka) + np.log10(np.maximum(n_b, 1e-6) / (n_ha - n_b)),
                         14 + np.log10(np.maximum((n_b - n_ha) / (25 + va), 1e-6) + 1e-12))
        eqp = va > 24.98
        ph_wa = np.where(np.abs(va - 25) < 0.15, 8.7, ph_wa)
        ph_wa[0] = 2.9
        ph_wa = np.clip(ph_wa, 0, 13.0)
        ax.plot(va[va < 24.98], np.clip(ph_wa[va < 24.98], 2.8, 14), color=PINK, lw=3, ls='--')
        ax.plot(va[va > 25.02], ph_wa[va > 25.02], color=PINK, lw=3, ls='--')
        ax.text(26, 5.5, 'weak acid + strong base:\nequivalence above pH 7', color=PINK, fontsize=16)
    ax.set_ylim(0, 14.5)
    notes = ['Acid-base indicators are weak acids or bases, with the acid form a different colour from the base form. The colour changes over a narrow pH range',
             'Choose an indicator whose range lies on the steep part of the curve, where the pH jumps at the equivalence point. A pH meter can record the whole curve',
             'Weak acid with strong base: the equivalence point is above 7, so phenolphthalein (not methyl orange) suits. Illustrative curves, not measured data']
    side_notes(fig, notes, s, x=0.60, w=0.36)


def limiting(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Limiting reagent')
    chip(fig, 'Element 2 · stoichiometry')
    ax = gax(fig, [0.07, 0.15, 0.42, 0.62], (0, 3.2), (0, 7.5), '', 'Amount (mol)', ticks=False)
    ax.set_xticks([0.7, 2.3]); ax.set_xticklabels(['N₂ given', 'H₂ given'], color=SOFT, fontsize=17)
    ax.bar([0.7], [2.0], width=0.9, color=C1)
    ax.bar([2.3], [5.0], width=0.9, color=C2)
    ax.text(0.7, 2.2, '2.0 mol', color=FG, fontsize=17, ha='center'); ax.text(2.3, 5.2, '5.0 mol', color=FG, fontsize=17, ha='center')
    if s >= 1:
        ax.bar([0.7], [0], width=0.9)
        ax.hlines(6.0, 1.9, 2.75, color=YELLOW, lw=4)
        ax.text(1.05, 6.35, 'H₂ needed for 2.0 mol N₂ = 6.0 mol: NOT available', color=YELLOW, fontsize=15)
    if s >= 2:
        ax.hlines(1.67, 0.25, 1.15, color=GREEN, lw=4)
        ax.text(1.4, 1.2, 'N₂ needed for 5.0 mol H₂ = 1.67 mol: available', color=GREEN, fontsize=14, ha='left')
    notes = ['N₂ + 3H₂ → 2NH₃. Compare what is GIVEN with what each reactant NEEDS: use the mole ratio from the equation',
             '2.0 mol N₂ needs 3 × 2.0 = 6.0 mol H₂, but only 5.0 mol is given: H₂ is the limiting reagent',
             'The limiting reagent is used up first and sets the yield. Show a calculation as evidence: stating “O₂ is limiting” alone was not enough. Find the excess left by subtraction']
    side_notes(fig, notes, s, x=0.55, w=0.40)


# ============================================================================ synthesis
def synthesis(fig, s, ph):
    C1, C2 = C()
    header(fig, 'Designing a synthesis')
    chip(fig, 'Element 2 · yield')
    items = [('Choose reagents', 'Pick reagents that give the product with the properties needed (a drug, a fuel, a cleaner) and are cheap, available and safe', C1),
             ('Maximise yield', 'Use an excess of the cheaper reagent; remove a product as it forms; choose conditions that favour products (Le Chatelier) at a workable rate; control temperature', C2),
             ('Maximise purity', 'Separate and purify: filtration, recrystallisation, distillation, washing; dry the product; use pure reagents; avoid side reactions', PINK),
             ('Calculate the yield', '% yield = (actual mass / theoretical mass) × 100. Theoretical mass comes from the LIMITING reagent and the equation', GREEN)]
    n = min(4, s + 1)
    for i in range(n):
        x = 0.05 + (i % 2) * 0.46; y = 0.48 - (i // 2) * 0.32
        card(fig, x, y, 0.44, 0.30, items[i][0], fit(ch(items[i][1]), 0.40, 21), tcol=items[i][2], size=21)


# ============================================================================ title and thumbnail
def _title_art(fig, rect, ph=0):
    C1, C2 = C()
    ax = wax(fig, rect, (0, 100), (0, 110))
    ax.add_patch(Rectangle((44, 52), 12, 54, fc='#13304f', ec=FG, lw=6))
    for k in range(11):
        ax.plot([44, 48], [56 + 4.5 * k, 56 + 4.5 * k], color=FG, lw=3)
    ax.add_patch(Polygon([[47, 52], [53, 52], [51, 44], [49, 44]], fc=FG, ec='none'))
    yd = 40 - 14 * ((ph * 1.0) % 1.0)
    ax.add_patch(Circle((50, yd), 2.6, fc=YELLOW, ec='none'))
    ax.add_patch(Polygon([[36, 28], [64, 28], [86, 2], [14, 2]], fc='#a8326c', ec=FG, lw=6))
    ax.plot([40, 40, 60, 60], [28, 36, 36, 28], color=FG, lw=6)
    ax.text(50, 14, 'mol', color=FG, fontsize=60, weight='bold', ha='center', va='center')


def thumbnail(fig):
    C1, C2 = C()
    fig.text(0.04, 0.87, 'CRITERION 8', ha='left', va='center', color=C1, fontsize=64, weight='bold')
    fig.text(0.04, 0.65, 'Chemical', ha='left', va='center', color=FG, fontsize=130, weight='bold')
    fig.text(0.04, 0.44, 'calcul-', ha='left', va='center', color=FG, fontsize=130, weight='bold')
    fig.text(0.04, 0.23, 'ations', ha='left', va='center', color=FG, fontsize=130, weight='bold')
    _title_art(fig, [0.60, 0.17, 0.38, 0.78])
