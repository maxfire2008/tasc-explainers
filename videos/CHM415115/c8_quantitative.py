"""CHM415115 Chemistry, Criterion 8: Apply logical processes to solve quantitative chemical problems.

    uv run python -m explainer check   videos/CHM415115/c8_quantitative.py
    uv run python -m explainer preview videos/CHM415115/c8_quantitative.py
    uv run python -m explainer thumbnail videos/CHM415115/c8_quantitative.py
    uv run python -m explainer render  videos/CHM415115/c8_quantitative.py    # operator only
"""
import math

from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, InfoSheet, import_sibling

COURSE, MODULE = 'CHM415115', 'C8'
L.use(style.theme(COURSE, MODULE))
V = import_sibling(__file__, 'c8_visuals.py')
_CC = import_sibling(__file__, 'chm_common.py')
Slide, Seq, Phased, ch = _CC.Slide, _CC.Seq, _CC.Phased, _CC.ch

P0 = 'Criterion 8 · Overview'
P1 = 'Part 1 · Moles, formulas and solutions'
P2 = 'Part 2 · Reacting quantities and yield'
P3 = 'Part 3 · Volumetric analysis'
P4 = 'Part 4 · Gases and electrolysis'
P5 = 'Part 5 · Energy, equilibrium and pH calculations'
P6 = 'Part 6 · Chemical synthesis'
P7 = 'Finish · Tests & exam technique'

# --------------------------------------------------------------------------- references
COURSE_DOC = 'chm415115-9.html'
INFO = 'CHM415115-Chemistry-Information-Sheet.pdf'
SPEC = 'CHM415115-Chemistry-External-Assessment-Specifications.pdf'

EXAM_PAGES = {
    2021: {18: 47, 19: '48-49', 20: 50, 21: '52-53', 22: '54-55', 23: '56-57'},
    2022: {18: 47, 19: '48-49', 20: '50-51', 21: 52, 22: 53, 23: 54, 24: 55},
    2023: {17: 51, 18: 52, 19: 53, 20: '54-55', 21: '56-57', 22: 58, 23: 59},
    2024: {17: 47, 18: 47, 19: 48, 20: '49-50', 21: 51, 22: 52, 23: '53-54'},
    2025: {17: 52, 18: 53, 19: '54-55', 20: '56-57', 21: 58, 22: 59},
}
REPORT_PAGES = {
    2021: {18: 18, 19: 19, 20: '19-20', 21: 21, 22: 22, 23: 23},
    2022: {18: '21-22', 19: '22-23', 20: '23-24', 21: '24-25', 22: 25, 23: '25-26', 24: '26-27'},
    2023: {17: '19, 21', 18: '19, 21', 19: '19, 21', 20: '19, 22', 21: '20, 22-23', 22: '20, 23', 23: '20, 24'},
    2024: {17: '19, 22', 18: '20, 22', 19: '20, 22-23', 20: '20-21, 23', 21: '21, 24', 22: '21, 24-25', 23: '21, 25-26'},
    2025: {17: '22-23, 24', 18: '23, 25', 19: '23, 25-26', 20: '23, 26', 21: '23-24, 27', 22: '24, 28'},
}


def exam(y, q):
    section = 'Part 4' if y == 2021 else 'Section D'
    return Ref(f'CHM415115-Chemistry-TASC-Exam-Paper-{y}.pdf', f'{y} exam, {section}, Question {q}', EXAM_PAGES[y][q])


def report(y, q):
    return Ref(f'CHM415115-Chemistry-Assessment-Report-{y}.pdf', f'{y} assessment report, Criterion 8, Question {q}',
               REPORT_PAGES[y][q])


REFS = {
    'standards': Ref(COURSE_DOC, 'Course document, Criterion 8 standards (element table)'),
    'content': Ref(COURSE_DOC, 'Course document, Science Understanding: application of logical processes to solve quantitative chemical problems (Criterion 8)'),
    'appendix': Ref(COURSE_DOC, 'Course document, Appendix 1: contexts (breathalysers; chemical balance in wine)'),
    'info': Ref(INFO, 'Information sheet, Chemical Information (n = m/M, c = n/V, gas equations, q = It, E = mcΔT)', page=2),
    'info_data': Ref(INFO, 'Information sheet, Chemical Data and Constants (R, F, NA, STP, SLC, molar volumes)', page=1),
    'info_eq': Ref(INFO, 'Information sheet, Chemical Equilibrium Formulae (Kc, Kw, pH)', page=4),
    'info_sol': Ref(INFO, 'Information sheet, Solubility Table for Some Ionic Compounds', page=4),
    'info_ar': Ref(INFO, 'Information sheet, Table of Relative Atomic Masses', page=9),
    'spec': Ref(SPEC, 'External assessment specifications, Section D', page=4),
    'spec_q': Ref(SPEC, 'External assessment specifications, Appendix A (routine and non-routine questions)', page=5),
}
for _y, _qs in EXAM_PAGES.items():
    for _q in _qs:
        REFS[f'ex{_y % 100}q{_q}'] = exam(_y, _q)
for _y, _qs in REPORT_PAGES.items():
    for _q in _qs:
        REFS[f'ar{_y % 100}q{_q}'] = report(_y, _q)
REFS['ar21g'] = Ref('CHM415115-Chemistry-Assessment-Report-2021.pdf', '2021 assessment report, Criterion 8 general comments', 18)
REFS['ar22g'] = Ref('CHM415115-Chemistry-Assessment-Report-2022.pdf', '2022 assessment report, Section D general comments', 21)
REFS['ar23g'] = Ref('CHM415115-Chemistry-Assessment-Report-2023.pdf', '2023 assessment report, Section D general feedback', 19)
REFS['ar24g'] = Ref('CHM415115-Chemistry-Assessment-Report-2024.pdf', '2024 assessment report, Criterion 8 general feedback', 19)
REFS['ar25g'] = Ref('CHM415115-Chemistry-Assessment-Report-2025.pdf', '2025 assessment report, Section D general comments', 22)
REFS['ar25gen'] = Ref('CHM415115-Chemistry-Assessment-Report-2025.pdf', '2025 assessment report, General Comments (numerical answers)', 1)

# --------------------------------------------------------------------------- coverage targets
SYLLABUS = {
    'M1': ('Review of calculations from the earlier Physical Sciences course: moles, molar mass, particles, concentration', 'content'),
    'M2': ('Masses of reactants or products when reactions go to completion', 'content'),
    'M3': ('Gravimetric analysis: mass of product from a precipitation reaction', 'content'),
    'M4': ('Percentage purity and percentage yield of a reaction product', 'content'),
    'M5': ('Water of crystallisation of a hydrated compound', 'content'),
    'M6': ('Properties of primary standard substances', 'content'),
    'M7': ('Preparation of primary standard solutions', 'content'),
    'M8': ('Concentration of a solution after dilution', 'content'),
    'M9': ('Identify the limiting reagent from masses or concentrations and volumes', 'content'),
    'M10': ('Mass, concentration or volume of a product or reactant when a limiting reagent is identified', 'content'),
    'V1': ('Acid-base titrations rely on an equivalence point seen as a pH change, with indicators or pH meters', 'content'),
    'V2': ('Acid-base indicators are weak acids or bases whose acid and base forms differ in colour', 'content'),
    'V3': ('Calculations for acid-base titrations', 'content'),
    'V4': ('Calculations for redox titrations', 'content'),
    'V5': ('Concentration of an unknown solution from volumetric data', 'content'),
    'Y1': ('Chemical synthesis: choosing reagents to form a product with specific properties', 'content'),
    'Y2': ('Design a synthesis: reagents and conditions to maximise yield and purity', 'content'),
    'Y3': ('Yield of a synthesis from stoichiometric and actual quantities', 'content'),
    'G1': ('Gas laws: molar volume of an ideal gas, absolute temperature conversions', 'content'),
    'G2': ('Molar volume at STP and SLC, and gases collected over a vapour pressure equilibrium', 'content'),
    'G3': ('Combined gas equation and ideal gas equation calculations', 'content'),
    'X1': ("Criterion 5, 6 and 7 calculations examined within Criterion 8, such as Faraday's laws", 'content'),
    'A1': ('Context: breathalysers and the measurement of blood alcohol (redox analysis)', 'appendix'),
    'A2': ('Context: chemical balance in wine (titration and gas chromatography)', 'appendix'),
}

ELEMENTS = {
    1: ('Performs organic and inorganic stoichiometric calculations for volumetric analysis, including acid-base and redox titrations, with familiar and unfamiliar reactants', 'standards'),
    2: ('Performs stoichiometric calculations for masses or volumes of reactants and products, including gases, solutions and limiting quantities', 'standards'),
}

EXAM_TOPICS = {
    'X21-18': ('Acid-base titration with sodium carbonate; mass of a hydrated solid for a standard solution', 'ex21q18'),
    'X21-19': ('Ethanol: theoretical heat from a volume using density; experimental ΔH from a spirit burner; incomplete combustion by Hess', 'ex21q19'),
    'X21-20': ('Permanganate and hydrogen peroxide: mass reacting per millilitre, percentage by mass in a disinfectant to correct sig figs', 'ex21q20'),
    'X21-21': ('pH of sodium in water; magnesium in excess over acid; concentration of the cation', 'ex21q21'),
    'X21-22': ('Weak acid: show the solution is not at equilibrium using Q; amounts at equilibrium; Kc', 'ex21q22'),
    'X21-23': ('Gas from heating potassium chlorate; verifying a battery capacity claim with Faraday and molar volume', 'ex21q23'),
    'X22-18': ('Enthalpy of formation of benzene by Hess; heat from burning a mass', 'ex22q18'),
    'X22-19': ('Empirical formula with water of hydration; permanganate titration of iron(II) with dilution and aliquots', 'ex22q19'),
    'X22-20': ('Silver sulfate precipitation: concentration, moles, limiting reagent and mass; base needed for the leftover acid', 'ex22q20'),
    'X22-21': ('Dissociation of a gas: Kc from initial and equilibrium amounts; Q to test a mixture', 'ex22q21'),
    'X22-22': ('Two electrolytic cells in series: time for a copper mass, gold mass', 'ex22q22'),
    'X22-23': ('Carbon dioxide cylinder: moles, pressure, number of molecules', 'ex22q23'),
    'X22-24': ('Barium hydroxide and hydrochloric acid mixed: moles, excess, pH of the final solution', 'ex22q24'),
    'X23-17': ('Mass of chromium by electrolysis from current and time', 'ex23q17'),
    'X23-18': ('Gas moles and a new volume with changed pressure and temperature', 'ex23q18'),
    'X23-19': ('Identify a metal from the mass of a hydroxide precipitate', 'ex23q19'),
    'X23-20': ('Ammonia production: limiting reagent, percentage yield, Kc from equilibrium amounts', 'ex23q20'),
    'X23-21': ('Propanol: Hess for ΔH, final temperature of heated water, volume of carbon dioxide at SLC', 'ex23q21'),
    'X23-22': ('pH after mixing an acid with a base in excess; pH of a weak acid with stated assumptions', 'ex23q22'),
    'X23-23': ('Iodine and thiosulfate back-calculation to a copper(II) concentration', 'ex23q23'),
    'X24-17': ('Empirical formula from percentage composition', 'ex24q17'),
    'X24-18': ('Concentration of a vitamin from micrograms in a volume, to the right significant figures', 'ex24q18'),
    'X24-19': ('Volume of carbon dioxide at SLC with the limiting reagent identified', 'ex24q19'),
    'X24-20': ('Chromium electrolysis: mass, oxygen collected over water with vapour pressure, efficiency and a reason for loss', 'ex24q20'),
    'X24-21': ('Ethanol combustion enthalpy by Hess to steam; heat released from a litre', 'ex24q21'),
    'X24-22': ('Weak acid pH with an approximation, percentage dissociation, effect of dilution', 'ex24q22'),
    'X24-23': ('Disinfectant: pH of sodium hydroxide, iodine titration, amount of iodine, percentage of hypochlorite', 'ex24q23'),
    'X25-17': ('Borax solution concentration including water of crystallisation; total sodium ion concentration after mixing', 'ex25q17'),
    'X25-18': ('Hess enthalpy of a sulfur reaction; heat released forming a mass of sulfur', 'ex25q18'),
    'X25-19': ('Ammonia and oxygen: limiting reagent, mass of excess, pressure of the gas collected', 'ex25q19'),
    'X25-20': ('Primary standard properties; standardising permanganate with oxalate; iron percentage in a mineral', 'ex25q20'),
    'X25-21': ('Contact process: Kc from initial amounts, reaction quotient and direction', 'ex25q21'),
    'X25-22': ('Final pH after mixing hydrochloric acid with barium hydroxide', 'ex25q22'),
}

# Every number spoken or shown in a worked example, recomputed.
F = 96500
M = dict(Mg=24.31, S=32.06, O=16.00, H=1.008, C=12.01, N=14.01, Na=22.99, Fe=55.85, Cu=63.55, Ba=137.3, Cl=35.45, Ag=107.9,
         K=39.10, I=126.9, Ca=40.08, Cr=52.00, Zn=65.38)
M_H2O = 2 * M['H'] + M['O']
M_MGSO4 = M['Mg'] + M['S'] + 4 * M['O']
M_NA2CO3 = 2 * M['Na'] + M['C'] + 3 * M['O']
M_NH3 = M['N'] + 3 * M['H']
M_H2SO4 = 2 * M['H'] + M['S'] + 4 * M['O']
M_NH42SO4 = 2 * (M['N'] + 4 * M['H']) + M['S'] + 4 * M['O']
M_BASO4 = M['Ba'] + M['S'] + 4 * M['O']
M_AGCL = M['Ag'] + M['Cl']
M_ETOH = 2 * M['C'] + 6 * M['H'] + M['O']
M_CH3COOH = 2 * M['C'] + 4 * M['H'] + 2 * M['O']
M_KIO3 = M['K'] + M['I'] + 3 * M['O']
M_CACO3 = M['Ca'] + M['C'] + 3 * M['O']
M_ASPIRIN = 9 * M['C'] + 8 * M['H'] + 4 * M['O']
M_SAL = 7 * M['C'] + 6 * M['H'] + 3 * M['O']
M_C6H14 = 6 * M['C'] + 14 * M['H']


def hydrate_x():
    n_w = (2.463 - 1.203) / M_H2O
    n_s = 1.203 / M_MGSO4
    return n_w / n_s


def lim_react():
    n_nh3 = 34.0 / M_NH3
    n_h2so4 = 90.0 / M_H2SO4
    return n_nh3, n_h2so4, n_nh3 / 2, n_h2so4


def vinegar_pct():
    avg = (18.42 + 18.38 + 18.40) / 3
    n = 0.1012 * avg / 1000
    n_orig = n * (100.0 / 25.00)
    m = n_orig * M_CH3COOH
    return m / (10.00 * 1.01) * 100


def iron_pct():
    n = 0.01000 * 0.02135 * 5 * 10
    return n * M['Fe'] / 1.265 * 100


def wine_g100():
    n = 0.06000 * 0.01840 * 1.5 * (250.0 / 25.0)
    return n * M_ETOH / 10.00 * 100


def salt_kio3_mg_per_kg():
    n_i2 = 0.00200 * 0.01480 / 2
    n_io3 = n_i2 / 3
    return n_io3 * M_KIO3 * 1000 / 10.0 * 1000


CHECKS = [
    ('water mass in hydrate', lambda: 2.463 - 1.203, 1.260, 1e-9),
    ('water moles', lambda: (2.463 - 1.203) / M_H2O, 0.06994, 1e-3),
    ('MgSO4 moles', lambda: 1.203 / M_MGSO4, 0.009994, 1e-3),
    ('hydrate x', hydrate_x, 7.00, 2e-3),
    ('C moles ethanol-type', lambda: 52.14 / M['C'], 4.342, 1e-3),
    ('H moles ethanol-type', lambda: 13.13 / M['H'], 13.03, 1e-3),
    ('O moles ethanol-type', lambda: 34.73 / M['O'], 2.171, 1e-3),
    ('Na2CO3 molar mass', lambda: M_NA2CO3, 105.99, 1e-3),
    ('standard conc', lambda: 1.325 / M_NA2CO3 / 0.2500, 0.05000, 2e-3),
    ('diluted conc', lambda: 1.325 / M_NA2CO3 / 0.2500 * 25.00 / 250.0, 0.005000, 2e-3),
    ('decahydrate molar mass', lambda: M_NA2CO3 + 10 * M_H2O, 286.14, 1e-3),
    ('sodium ions in sulfate', lambda: 0.0500 * 0.200 * 2, 0.0200, 1e-9),
    ('sodium ions in chloride', lambda: 0.100 * 0.150, 0.0150, 1e-9),
    ('total sodium conc', lambda: (0.0200 + 0.0150) / 0.150, 0.2333, 1e-3),
    ('NH3 moles', lambda: lim_react()[0], 1.9965, 1e-3),
    ('H2SO4 moles', lambda: lim_react()[1], 0.9175, 1e-3),
    ('H2SO4 needed', lambda: lim_react()[0] / 2, 0.9983, 1e-3),
    ('ammonium sulfate molar mass', lambda: M_NH42SO4, 132.16, 1e-3),
    ('ammonium sulfate theoretical', lambda: lim_react()[1] * M_NH42SO4, 121.3, 1e-3),
    ('NH3 used', lambda: 2 * lim_react()[1], 1.835, 1e-3),
    ('NH3 left mol', lambda: lim_react()[0] - 2 * lim_react()[1], 0.1615, 5e-3),
    ('NH3 left g', lambda: (lim_react()[0] - 2 * lim_react()[1]) * M_NH3, 2.75, 5e-3),
    ('yield percent', lambda: 98.0 / (lim_react()[1] * M_NH42SO4) * 100, 80.8, 2e-3),
    ('BaSO4 moles', lambda: 0.6112 / M_BASO4, 2.619e-3, 2e-3),
    ('sulfate conc', lambda: 0.6112 / M_BASO4 / 0.02500, 0.1048, 2e-3),
    ('AgCl molar mass', lambda: M_AGCL, 143.35, 1e-3),
    ('AgCl moles', lambda: 4.136 / M_AGCL, 0.028853, 1e-3),
    ('MCl2 moles', lambda: 4.136 / M_AGCL / 2, 0.014427, 1e-3),
    ('MCl2 molar mass', lambda: 3.000 / (4.136 / M_AGCL / 2), 207.9, 1e-3),
    ('M metal molar mass', lambda: 3.000 / (4.136 / M_AGCL / 2) - 2 * M['Cl'], 137.0, 2e-3),
    ('concordant average', lambda: (18.42 + 18.38 + 18.40) / 3, 18.40, 1e-9),
    ('NaOH moles', lambda: 0.1012 * 0.01840, 1.862e-3, 1e-3),
    ('acid moles in 100 mL', lambda: 0.1012 * 0.01840 * 4, 7.448e-3, 1e-3),
    ('acid mass', lambda: 0.1012 * 0.01840 * 4 * M_CH3COOH, 0.4473, 1e-3),
    ('vinegar percent', vinegar_pct, 4.43, 3e-3),
    ('MnO4 moles', lambda: 0.01000 * 0.02135, 2.135e-4, 1e-3),
    ('Fe2+ moles aliquot', lambda: 0.01000 * 0.02135 * 5, 1.0675e-3, 1e-3),
    ('Fe moles total', lambda: 0.01000 * 0.02135 * 5 * 10, 1.0675e-2, 1e-3),
    ('Fe mass', lambda: 0.01000 * 0.02135 * 5 * 10 * M['Fe'], 0.5962, 1e-3),
    ('iron percent', iron_pct, 47.13, 2e-3),
    ('dichromate moles', lambda: 0.06000 * 0.01840, 1.104e-3, 1e-3),
    ('ethanol moles aliquot', lambda: 0.06000 * 0.01840 * 1.5, 1.656e-3, 1e-3),
    ('ethanol moles total', lambda: 0.06000 * 0.01840 * 1.5 * 10, 1.656e-2, 1e-3),
    ('ethanol mass', lambda: 0.06000 * 0.01840 * 1.5 * 10 * M_ETOH, 0.7629, 1e-3),
    ('ethanol g per 100 mL', wine_g100, 7.63, 3e-3),
    ('thiosulfate moles', lambda: 0.00200 * 0.01480, 2.96e-5, 1e-3),
    ('iodine moles', lambda: 0.00200 * 0.01480 / 2, 1.48e-5, 1e-3),
    ('iodate moles', lambda: 0.00200 * 0.01480 / 2 / 3, 4.933e-6, 1e-3),
    ('KIO3 molar mass', lambda: M_KIO3, 214.0, 1e-3),
    ('KIO3 mg', lambda: 0.00200 * 0.01480 / 2 / 3 * M_KIO3 * 1000, 1.056, 2e-3),
    ('KIO3 mg per kg', salt_kio3_mg_per_kg, 105.6, 2e-3),
    ('CaCO3 moles', lambda: 8.00 / M_CACO3, 0.07993, 1e-3),
    ('HCl moles', lambda: 0.0600 * 1.50, 0.0900, 1e-9),
    ('HCl needed', lambda: 8.00 / M_CACO3 * 2, 0.1599, 1e-3),
    ('CO2 moles limiting', lambda: 0.0900 / 2, 0.0450, 1e-9),
    ('CO2 volume SLC', lambda: 0.0900 / 2 * 24.5, 1.1025, 1e-3),
    ('H2 partial pressure', lambda: 100.8 - 2.64, 98.16, 1e-9),
    ('H2 moles over water', lambda: 98.16 * 0.0500 / (8.31 * (273.15 + 22.0)), 2.001e-3, 2e-3),
    ('Zn mass', lambda: 98.16 * 0.0500 / (8.31 * 295.15) * M['Zn'], 0.1308, 3e-3),
    ('Cu moles', lambda: 1.50 / M['Cu'], 0.023603, 1e-3),
    ('electron moles Cu', lambda: 1.50 / M['Cu'] * 2, 0.047207, 1e-3),
    ('time Cu', lambda: 1.50 / M['Cu'] * 2 * F / 2.00, 2277.6, 1e-3),
    ('time minutes', lambda: 1.50 / M['Cu'] * 2 * F / 2.00 / 60, 37.96, 1e-3),
    ('Cr moles series', lambda: 1.50 / M['Cu'] * 2 / 3, 0.015736, 1e-3),
    ('Cr mass series', lambda: 1.50 / M['Cu'] * 2 / 3 * M['Cr'], 0.8183, 1e-3),
    ('benzene-like formation Hess', lambda: 2 * -393.5 + 3 * -285.8 - (-1560), -84.4, 1e-9),
    ('hexane moles', lambda: 2.00 / M_C6H14, 0.023207, 2e-3),
    ('hexane heat kJ', lambda: 2.00 / M_C6H14 * 4163, 96.61, 2e-3),
    ('water temperature rise', lambda: 2.00 / M_C6H14 * 4163 * 1000 / (1000.0 * 4.184), 23.09, 2e-3),
    ('final temperature', lambda: 18.0 + 2.00 / M_C6H14 * 4163 * 1000 / (1000.0 * 4.184), 41.1, 2e-3),
    ('Kc N2O4', lambda: 0.0600 ** 2 / (0.200 - 0.0300), 0.02118, 2e-3),
    ('Q N2O4', lambda: 0.0200 ** 2 / 0.100, 4.0e-3, 1e-9),
    ('excess H+ moles', lambda: 0.0500 * 0.0800 - 2 * 0.0300 * 0.0600, 4.00e-4, 1e-9),
    ('mixture H+ conc', lambda: (0.0500 * 0.0800 - 2 * 0.0300 * 0.0600) / 0.0800, 5.000e-3, 1e-9),
    ('mixture pH', lambda: -math.log10(5.000e-3), 2.30, 1e-3),
    ('propanoic x', lambda: math.sqrt(1.35e-5 * 0.200), 1.643e-3, 1e-3),
    ('propanoic pH', lambda: -math.log10(math.sqrt(1.35e-5 * 0.200)), 2.78, 2e-3),
    ('propanoic percent', lambda: math.sqrt(1.35e-5 * 0.200) / 0.200 * 100, 0.822, 2e-3),
    ('diluted percent', lambda: math.sqrt(1.35e-5 * 0.0200) / 0.0200 * 100, 2.60, 2e-3),
    ('salicylic moles', lambda: 5.00 / M_SAL, 0.03620, 1e-3),
    ('aspirin theoretical', lambda: 5.00 / M_SAL * M_ASPIRIN, 6.522, 1e-3),
    ('aspirin yield', lambda: 4.85 / (5.00 / M_SAL * M_ASPIRIN) * 100, 74.4, 2e-3),
    ('limestone CO2 moles', lambda: 0.4120 / 24.5, 0.016816, 1e-3),
    ('limestone purity', lambda: 0.4120 / 24.5 * M_CACO3 / 2.000 * 100, 84.2, 2e-3),
    ('N2 mol', lambda: 2.0, 2.0, 1e-9),
]

# --------------------------------------------------------------------------- scenes
S = Step
SCENES = [
Scene('title', P0, 'Welcome', Slide('title', kicker='CRITERION 8', name='Quantitative\nchemical problems', art=V._title_art, size=62), [
    S("Welcome. This video is a complete briefing on Criterion 8 of TASC Chemistry, C H M four one five, one one five: apply "
      "logical processes to solve quantitative chemical problems. It is the calculations criterion, and it draws on the content from "
      "all the others. Use it to revise for class tests and for the end of year exam. We will work through the methods, "
      "with original worked examples.", refs=['standards'], anim=4),
]),
Scene('intro', P0, 'How Criterion 8 is assessed', Seq(
    Slide('assess', internal='Your teacher: class tests, practicals\nand investigations during the year',
          external='End-of-year TASC exam:\nSection D is all Criterion 8', section='Section D'),
    Slide('elements', title='The two elements of Criterion 8', items=[
        ('Volumetric analysis', 'organic and inorganic stoichiometry for titrations, acid-base and redox, familiar and unfamiliar reactants'),
        ('Reacting quantities', 'masses or volumes of reactants and products: gases, solutions, limiting quantities')]),
    Slide('standards', title='What the standards ask for', rows=[
        ('E1 Volumetric analysis', 'routine, familiar organic and inorganic', 'acid-base and redox, familiar reactants', 'acid-base and redox, unfamiliar reactants'),
        ('E2 Reacting quantities', 'routine: masses or volumes, incl. gases', 'masses or volumes with solutions and limiting quantities', 'complex calculations')]),
    Slide('roadmap', title='Roadmap', parts=[
        ('Part 1', 'Moles, formulas, hydrates, standards and dilution'), ('Part 2', 'Reacting quantities, limiting reagents, yield'),
        ('Part 3', 'Volumetric analysis: titrations'), ('Part 4', 'Gases and electrolysis'),
        ('Part 5', 'Energy, equilibrium and pH calculations'), ('Part 6', 'Synthesis and yield'),
        ('Finish', 'Tests and exam technique, and a summary')])), [
    S("Criterion 8 is assessed in two ways. Your teacher assesses it during the year, in tests, practicals and investigations. It "
      "is also assessed in Section D of the end of year exam: about forty five minutes, forty five marks, and between five and "
      "seven compulsory questions. You may use the information sheet and an approved calculator. The course says that the calculations of "
      "criteria five, six and seven are also examined here.", refs=['standards', 'spec', 'content']),
    S("The criterion has two elements, numbered as in the standards table. Element one is volumetric analysis: acid base and "
      "redox titrations, in organic and inorganic chemistry. Element two is stoichiometric calculations for masses or volumes of reactants "
      "and products, including gases, solutions and limiting quantities.", refs=['standards'], elements=[1, 2]),
    S("The standards step up from C to A. At C you do routine calculations in familiar chemistry. At B the calculations have "
      "more steps and cover acid base and redox titrations with familiar reactants. At A they are complex, and the titrations involve "
      "unfamiliar reactants, given in the question. So set your working out logically, step by step.", refs=['standards'], elements=[1, 2]),
    S("The roadmap. Moles, formulas and solutions. Reacting quantities and yield. Titrations. Gases and electrolysis. Energy, "
      "equilibrium and pH calculations. Synthesis. Then technique for tests and the exam.", refs=['content']),
]),

# ------------------------------------------------------------------ Part 1
Scene('roadmap_moles', P1, 'The moles roadmap', V.roadmap, [
    S("Every calculation goes through moles. Mass to moles uses n equals m over M, with the molar mass built from the relative "
      "atomic masses in the table on your information sheet. The sheet's chemical information section gives n equals m over M "
      "as the first formula.", refs=['info', 'info_ar', 'content'], covers=['M1'], elements=[2]),
    S("For solutions, concentration equals moles over volume, and the volume must be in litres. So moles of solute equal the "
      "concentration times the volume. Convert millilitres by dividing by a thousand.", refs=['info', 'content'], covers=['M1'], elements=[1, 2]),
    S("Particles: N equals n times Avogadro's constant, from the data page of the sheet. For gases, use the ideal gas "
      "equation, or the molar volume: twenty four point five litres per mole at standard laboratory conditions, and twenty two "
      "point four at standard temperature and pressure. Convert units before you substitute.",
      refs=['info', 'info_data', 'content', 'ex22q23', 'ar22q23'], covers=['M1', 'G2'], elements=[2], exam=['X22-23']),
]),
Scene('method', P1, 'A method and how to set it out', V.stoich_steps, [
    S("Use the same five steps for nearly every problem. First, write the balanced equation. Second, convert what is given into "
      "moles of one species. Third, use the mole ratio from the equation to find the moles of the species you want.",
      refs=['content', 'ar24g', 'ar22g'], covers=['M1'], elements=[1, 2]),
    S("Fourth, convert to the quantity asked for. Fifth, check units and significant figures, and whether the answer is realistic. "
      "Markers want each step on a separate line, with units, and with a label for what each number is: n of H C l, not just n. "
      "Combining steps can save time, but many errors were seen.", refs=['ar24g', 'ar23g', 'ar22g'], covers=['M1'], elements=[1, 2]),
    S("Tip: examiners also ask you to show that a value is about a given number. Then calculate your own value to an "
      "appropriate number of significant figures, show it, and use that value, not the rounded number in the question, in later parts. "
      "Using the approximate value often gave wrong results.", refs=['ar22q23', 'ar25g', 'ar22q20'], covers=['M1'], elements=[1, 2], exam=['X22-23']),
    S("Numbers need context and units: a markers' general comment said numerical answers in every section need them, and a final "
      "answer without a unit lost half a mark. Also write mol per litre, not capital M. Keep unrounded values until the end, and "
      "give the final answer to the number of significant figures of the least precise data.", refs=['ar25gen', 'ar24g', 'ar22g'], covers=['M1'], elements=[1, 2]),
]),
Scene('sigfigs', P1, 'Significant figures', Slide('bullets', title='Significant figures in the exam', chip='Element 2 · stoichiometry', size=25, counts=[1, 2, 3, 4], items=[
    'Round the FINAL answer to the least number of significant figures in the data (2.0 mol and 3.456 g gives 2 s.f.). Keep extra digits in the working',
    'When the question says “to the correct number of significant figures”, it is marked: in 2021 and 2022 an answer to a wrong number lost half a mark',
    'In a “show that” part, show your own unrounded value, then say it is about the given one; use YOUR value later',
    'Markers penalised −0.5 once for misuse (five or six figures, or one figure) and −0.5 for early rounding. A pH is given to decimal places equal to the s.f. of the concentration']), [
    S("Significant figures matter. Keep extra digits in your working, and round the final answer to the least number of "
      "significant figures in the data. Two point oh moles with three point four five six grams gives two significant figures. "
      "Where the question states a precision, such as two decimal places for a pH, follow it.",
      refs=['ar21q20', 'ar24g', 'ex21q20'], covers=['M1'], elements=[1, 2], exam=['X21-20']),
    S("Some questions state the precision they want, and then it is marked. Others do "
      "not, and in those, minor deviations were not penalised, although misuse was. Giving six figures, or rounding to a single digit, "
      "lost half a mark. In 2024, a vitamin concentration needed two significant figures, because the dose of twenty five micrograms has two.",
      refs=['ar22g', 'ar22q22', 'ar24q18', 'ex24q18', 'ar21q20'], covers=['M1'], elements=[2], exam=['X24-18', 'X21-20']),
    S("In a show that question, calculate to an appropriate number of figures, show it is close to the stated value, and use your "
      "own value afterwards. In 2025, markers applied a half mark penalty once for misuse of significant figures, and once for "
      "inappropriate rounding. Avoid rounding within calculations.", refs=['ar25g', 'ar22q20'], covers=['M1'], elements=[1, 2], exam=['X22-23']),
    S("Source note: two inconsistencies exist across reports. The 2021 report expected two significant figures for the disinfectant, "
      "because of the smallest data value, but later years said minor deviations were not penalised. The safe approach is the least "
      "number of significant figures in the data, and never fewer or more than that without a reason. In this video, each answer is shown "
      "unrounded and then rounded.", refs=['ar21q20', 'ar22g', 'ar24g'], covers=['M1'], elements=[1, 2], exam=['X21-20']),
]),
Scene('we_hydrate', P1, 'Hydrates and empirical formulas', Slide('worked', title='Worked example 1: water of crystallisation', chip='Element 2 · stoichiometry',
    q='A 2.463 g sample of hydrated magnesium sulfate is heated to constant mass, leaving 1.203 g of anhydrous MgSO₄. Find x in MgSO₄·xH₂O. Then a compound is 52.14% C, 13.13% H and 34.73% O by mass: find its empirical formula.',
    rows=[dict(s=0, t='m(H₂O) = 2.463 − 1.203 = 1.260 g;   n(H₂O) = 1.260 / 18.016 = 0.06994 mol', col='#eef2f8'),
          dict(s=0, t='n(MgSO₄) = 1.203 / 120.37 = 0.009994 mol', col='#eef2f8'),
          dict(s=1, t='x = n(H₂O) / n(MgSO₄) = 0.06994 / 0.009994 = 7.00', col='#ffd166'),
          dict(s=1, sf='x = 7.00 (3 s.f.): MgSO₄·7H₂O', t='', gap=0),
          dict(s=2, t='Assume 100 g:  n(C) = 52.14/12.01 = 4.342;  n(H) = 13.13/1.008 = 13.03;  n(O) = 34.73/16.00 = 2.171', col='#eef2f8', size=23),
          dict(s=3, t='Divide by the smallest (2.171):  C : H : O = 2.000 : 6.00 : 1.000   so empirical formula C₂H₆O', col='#9bde7e', size=23),
          dict(s=3, t='If the molar mass is 46 g mol⁻¹, the molecular formula is also C₂H₆O.', col='#b3c0d4', size=22)]), [
    S("Worked example one. To find water of crystallisation, heat a hydrate to constant mass. The mass lost is water. Here, "
      "two point four six three minus one point two oh three is one point two six oh grams of water, or zero point oh six nine nine "
      "four moles. The anhydrous salt is zero point oh oh nine nine nine four moles.",
      refs=['content', 'info_ar', 'ex22q19', 'ar22q19'], covers=['M5', 'M1'], elements=[2], exam=['X22-19'],
      problem='A 2.463 g sample of MgSO₄·xH₂O leaves 1.203 g of MgSO₄ after heating. Find x.'),
    S("The ratio of moles of water to salt is seven point oh oh, so the formula is magnesium sulfate heptahydrate. Many "
      "students in 2022 found the empirical formula but could not show the degree of hydration.", refs=['ar22q19'], covers=['M5'], elements=[2], exam=['X22-19']),
    S("For an empirical formula from percentages, assume one hundred grams and convert each mass to moles. Carbon is four point "
      "three four two, hydrogen thirteen point oh three, oxygen two point one seven one.",
      refs=['ex24q17', 'ar24q17', 'content'], covers=['M1'], elements=[2], exam=['X24-17'],
      problem='A compound is 52.14% C, 13.13% H and 34.73% O by mass. What is its empirical formula?'),
    S("Divide by the smallest: two, six and one. The empirical formula is C two H six O. Present it as a table or in columns "
      "if you wish, and use the atomic masses from the sheet. Note that this is not a combustion question, which threw some students in 2022.",
      refs=['ar24q17', 'ar22q19'], covers=['M1'], elements=[2], exam=['X24-17', 'X22-19']),
]),
Scene('we_solutions', P1, 'Standard solutions and dilution', Slide('worked', title='Worked example 2: standards, dilution, mixing', chip='Element 2 · stoichiometry',
    q='(a) 1.325 g of Na₂CO₃ is dissolved to make 250.0 mL of solution. Find its concentration. (b) 25.00 mL of it is diluted to 250.0 mL. Find the new concentration. (c) 50.0 mL of 0.200 mol L⁻¹ Na₂SO₄ is mixed with 100.0 mL of 0.150 mol L⁻¹ NaCl. Find [Na⁺].',
    size=23,
    rows=[dict(s=0, t='M(Na₂CO₃) = 2(22.99) + 12.01 + 3(16.00) = 105.99 g mol⁻¹;   n = 1.325 / 105.99 = 0.012501 mol', col='#eef2f8', size=22),
          dict(s=0, t='c = n / V = 0.012501 / 0.2500 = 0.05000 mol L⁻¹', col='#9bde7e'),
          dict(s=0, sf='= 5.000 × 10⁻² mol L⁻¹ (4 s.f.)', t='', gap=0),
          dict(s=1, t='Dilution: moles unchanged:  c₁V₁ = c₂V₂,   c₂ = 0.05000 × 25.00 / 250.0 = 0.005000 mol L⁻¹', col='#9bde7e', size=22),
          dict(s=1, t='If the solid were Na₂CO₃·10H₂O (M = 286.14), the mass needed is 2.7 times bigger: include the water.', col='#f15bb5', size=21),
          dict(s=2, t='n(Na⁺) from Na₂SO₄ = 0.0500 × 0.200 × 2 = 0.0200 mol;   from NaCl = 0.100 × 0.150 = 0.0150 mol', col='#eef2f8', size=22),
          dict(s=3, t='[Na⁺] = (0.0200 + 0.0150) / (0.0500 + 0.100) = 0.2333 mol L⁻¹', col='#9bde7e'),
          dict(s=3, sf='= 0.233 mol L⁻¹ (3 s.f.)', t='', gap=0)]), [
    S("A primary standard is a substance used to make a solution of exactly known concentration. It must be pure, stable and "
      "not change in air, so not absorb water or carbon dioxide, have a known formula, have a high molar mass so weighing errors are small, "
      "and dissolve. Sodium carbonate and sodium oxalate are examples. Students confused these with the properties of a standard solution.",
      refs=['content', 'ex25q20', 'ar25q20'], covers=['M6'], elements=[1], exam=['X25-20']),
    S("To prepare it, weigh the solid accurately, dissolve it in a beaker with some water, transfer it fully to a volumetric flask, and "
      "make it up to the mark. Worked example two. One point three two five grams in two hundred and fifty millilitres of "
      "sodium carbonate gives zero point oh five oh oh moles per litre.",
      refs=['content', 'info', 'info_ar', 'ex21q18', 'ar21q18'], covers=['M7', 'M1'], elements=[1, 2], exam=['X21-18'],
      problem='1.325 g of Na₂CO₃ is made up to 250.0 mL. What is the concentration?'),
    S("Dilution keeps the moles of solute the same, so c one V one equals c two V two. Taking twenty five millilitres to "
      "two hundred and fifty gives a tenfold dilution: zero point oh oh five oh oh moles per litre. If the solid is a hydrate, "
      "such as the decahydrate, the molar mass must include the water: many students ignored it in 2021 and lost a mark.",
      refs=['content', 'ex21q18', 'ar21q18', 'ex22q19', 'ar22q19'], covers=['M8', 'M5'], elements=[1, 2], exam=['X21-18', 'X22-19'],
      problem='25.00 mL of 0.05000 mol L⁻¹ solution is diluted to 250.0 mL. What is the new concentration?'),
    S("When solutions are mixed, work with moles of the ion, then divide by the total volume. Sodium sulfate has two sodium ions per "
      "formula. The two sources give zero point oh two and zero point oh one five moles, a total of zero point oh three five, in one hundred "
      "and fifty millilitres: zero point two three three moles per litre. In 2025, a common error was neglecting the water in borax's molar mass.",
      refs=['ex25q17', 'ar25q17', 'ar25g'], covers=['M8', 'M5'], elements=[2], exam=['X25-17'],
      problem='50.0 mL of 0.200 mol L⁻¹ Na₂SO₄ and 100.0 mL of 0.150 mol L⁻¹ NaCl are mixed. What is the total [Na⁺]?'),
]),

# ------------------------------------------------------------------ Part 2
Scene('limiting', P2, 'Limiting reagents', V.limiting, [
    S("When two reactants are given, one may run out first. That is the limiting reagent, and it sets how much product forms. "
      "To find it, compare what is given with what each reactant needs from the mole ratio of the equation. For nitrogen and hydrogen making "
      "ammonia, two moles of nitrogen needs six of hydrogen.",
      refs=['content', 'ex23q20', 'ar23q20', 'ex24q19', 'ar24q19'], covers=['M9'], elements=[2], exam=['X23-20', 'X24-19']),
    S("Only five moles of hydrogen are available, so hydrogen is limiting. Do not just say which is limiting. Markers "
      "required a calculation showing it, such as moles needed against moles given. Some students used the original amounts "
      "at equilibrium instead.", refs=['ar23q20', 'ar24q19', 'ar25q19'], covers=['M9', 'M10'], elements=[2], exam=['X23-20', 'X24-19', 'X25-19']),
    S("The limiting reagent decides the amounts of product and of the excess left over. Use it for everything afterwards. Work out the "
      "excess by subtracting the amount that reacted from the amount given. A frequent mistake was subtracting moles "
      "given in the wrong place, or applying the ratio to the wrong substance.", refs=['ar22q24', 'ar25q19', 'content'], covers=['M10', 'M9'], elements=[2], exam=['X22-24', 'X25-19']),
]),
Scene('we_limiting', P2, 'Worked example: ammonium sulfate', Slide('worked', title='Worked example 3: limiting reagent and yield', chip='Element 2 · stoichiometry',
    q='34.0 g of ammonia reacts with 90.0 g of sulfuric acid: 2NH₃ + H₂SO₄ → (NH₄)₂SO₄. Find the limiting reagent, the mass of (NH₄)₂SO₄ formed, the mass of excess reagent left, and the percentage yield if 98.0 g is actually obtained.',
    size=22,
    rows=[dict(s=0, t='n(NH₃) = 34.0 / 17.03 = 1.9965 mol;      n(H₂SO₄) = 90.0 / 98.09 = 0.9175 mol', col='#eef2f8'),
          dict(s=0, t='n(H₂SO₄) needed for the NH₃ = 1.9965 / 2 = 0.9983 mol  >  0.9175 mol available', col='#eef2f8'),
          dict(s=0, t='so H₂SO₄ is the LIMITING reagent', col='#ffd166'),
          dict(s=1, t='n((NH₄)₂SO₄) = n(H₂SO₄) = 0.9175 mol;   m = 0.9175 × 132.16 = 121.3 g', col='#9bde7e'),
          dict(s=1, sf='= 121 g (3 s.f.): the theoretical yield', t='', gap=0),
          dict(s=2, t='NH₃ used = 2 × 0.9175 = 1.835 mol;   NH₃ left = 1.9965 − 1.835 = 0.1615 mol = 2.75 g', col='#ffd166'),
          dict(s=3, t='% yield = actual / theoretical × 100 = 98.0 / 121.3 × 100 = 80.8%', col='#9bde7e'),
          dict(s=3, sf='= 80.8 % (3 s.f.)', t='', gap=0)]), [
    S("Worked example three. Thirty four grams of ammonia and ninety grams of sulfuric acid. The moles are one point nine nine six five "
      "of ammonia and zero point nine one seven five of acid. The ammonia needs half as many moles of acid, zero point nine nine "
      "eight three, which is more than is available. So sulfuric acid is limiting.",
      refs=['info_ar', 'content', 'ex25q19', 'ar25q19'], covers=['M9', 'M2'], elements=[2], exam=['X25-19'],
      problem='34.0 g of NH₃ reacts with 90.0 g of H₂SO₄ (2NH₃ + H₂SO₄ → (NH₄)₂SO₄). Which is limiting, and what mass of product forms?'),
    S("The product's moles equal the acid's, zero point nine one seven five, and the molar mass of ammonium sulfate is "
      "one thirty two point one six, so the theoretical mass is about one hundred and twenty one grams.",
      refs=['info_ar'], covers=['M10', 'M2'], elements=[2], exam=['X25-19']),
    S("The excess reagent is ammonia. It used two times zero point nine one seven five, one point eight three five, so "
      "zero point one six one five moles, or about two point seven five grams, is left. The 2025 question asked for the "
      "mass remaining, and most errors were in the moles consumed.", refs=['ar25q19', 'ex25q19'], covers=['M10'], elements=[2], exam=['X25-19'],
      problem='In the same reaction, what mass of excess NH₃ remains?'),
    S("Percentage yield is actual over theoretical times one hundred: ninety eight divided by one twenty one point three, eighty "
      "point eight percent. In the 2023 ammonia question, the actual yield was fifty eight kilograms against a theoretical seventy six "
      "point six, about seventy five point seven percent. Make sure the theoretical mass comes from the limiting reagent.",
      refs=['ex23q20', 'ar23q20', 'content'], covers=['M4', 'M10'], elements=[2], exam=['X23-20'],
      problem='98.0 g of (NH₄)₂SO₄ is obtained against a theoretical 121.3 g. What is the percentage yield?'),
]),
Scene('we_gravimetric', P2, 'Precipitates and gravimetric analysis', Slide('worked', title='Worked example 4: gravimetric analysis', chip='Element 2 · stoichiometry',
    q='(a) Excess BaCl₂ is added to 25.00 mL of sodium sulfate solution. The dried BaSO₄ precipitate has a mass of 0.6112 g. Find [SO₄²⁻]. (b) A 3.000 g sample of a group 2 chloride, MCl₂, gives 4.136 g of AgCl with excess silver nitrate. Identify M. (c) A 2.000 g limestone sample gives 0.4120 L CO₂ at SLC with excess acid. Find the % purity of CaCO₃.',
    size=20,
    rows=[dict(s=0, t='Check the solubility table on the sheet: BaSO₄ is insoluble, so it precipitates. Ba²⁺ + SO₄²⁻ → BaSO₄(s)', col='#b3c0d4', size=21),
          dict(s=0, t='n(BaSO₄) = 0.6112 / 233.4 = 2.619 × 10⁻³ mol = n(SO₄²⁻);   c = 2.619 × 10⁻³ / 0.02500 = 0.1048 mol L⁻¹', col='#9bde7e'),
          dict(s=1, t='n(AgCl) = 4.136 / 143.35 = 0.02885 mol;   n(MCl₂) = ½ × 0.02885 = 0.01443 mol', col='#eef2f8'),
          dict(s=1, t='M(MCl₂) = 3.000 / 0.01443 = 207.9;   M(M) = 207.9 − 2(35.45) = 137.0 g mol⁻¹: barium', col='#9bde7e'),
          dict(s=2, t='n(CO₂) = 0.4120 / 24.5 = 0.01682 mol;   n(CaCO₃) = same (1 : 1)', col='#eef2f8'),
          dict(s=2, t='m(CaCO₃) = 0.01682 × 100.09 = 1.683 g;   % purity = 1.683 / 2.000 × 100 = 84.2%', col='#9bde7e'),
          dict(s=3, sf='= 84.2 % (3 s.f.)', t='', gap=0)]), [
    S("Gravimetric analysis finds an amount from the mass of a precipitate. Check solubility, using the solubility table on "
      "the information sheet, to decide what precipitates. Barium sulfate is insoluble. Worked example four. Zero point six one one "
      "two grams of barium sulfate is two point six two times ten to the minus three moles, which equals the moles of sulfate, so "
      "the concentration is zero point one oh four eight moles per litre.",
      refs=['info_sol', 'content', 'info_ar', 'ex22q20', 'ar22q20'], covers=['M3', 'M2'], elements=[2], exam=['X22-20'],
      problem='0.6112 g of BaSO₄ forms from 25.00 mL of sulfate solution with excess Ba²⁺. What is [SO₄²⁻]?'),
    S("To identify a metal, find the molar mass of the compound from its mass and moles, then subtract the rest. Silver "
      "chloride is four point one three six over one forty three point three five, zero point oh two eight eight five moles. "
      "There are two chlorides per formula, so M C l two is half that. The molar mass of the metal is about one hundred and thirty seven, barium. "
      "In 2023, a hydroxide precipitate identified potassium in the same way.",
      refs=['ex23q19', 'ar23q19', 'info_ar'], covers=['M3', 'M2'], elements=[2], exam=['X23-19'],
      problem='3.000 g of MCl₂ gives 4.136 g of AgCl. Identify the metal M.'),
    S("Percentage purity is the mass of pure substance over the mass of the sample, times one hundred. A limestone sample "
      "of two grams gives zero point four one two litres of carbon dioxide, at standard laboratory conditions, which is zero point oh "
      "one six eight two moles. That is one point six eight three grams of calcium carbonate, eighty four point two percent pure.",
      refs=['content', 'info_data'], covers=['M4', 'G2'], elements=[2],
      problem='A 2.000 g limestone sample gives 0.4120 L of CO₂ at SLC with excess acid. What is the % purity of CaCO₃?'),
    S("Keep the logic the same each time: balanced equation, moles of the measured substance, mole ratio, then the quantity "
      "asked. In silver sulfate in 2022, you needed the limiting reagent first, then the mass of product, and finally the base to neutralise "
      "the remaining acid: the hydrogen ion amount is unchanged by the reaction.",
      refs=['ex22q20', 'ar22q20'], covers=['M3', 'M9', 'M10'], elements=[2], exam=['X22-20']),
]),

# ------------------------------------------------------------------ Part 3: titrations
Scene('apparatus', P3, 'Titration technique and terms', V.apparatus, [
    S("Volumetric analysis finds a concentration by measuring volumes of solutions that react. A pipette delivers an exact aliquot "
      "of one solution into a conical flask, with a few drops of indicator. The burette delivers the other solution, the titrant.",
      refs=['content'], covers=['V1', 'V5'], elements=[1]),
    S("Add titrant until the indicator just changes colour, the end point, which should match the equivalence point, where "
      "the reactants have been mixed in exactly the ratio of the equation. The drop in the burette is the last one that is needed.",
      refs=['content'], covers=['V1'], elements=[1], anim=2),
    S("Repeat until three titres agree within about a tenth of a millilitre, which are called concordant. Average those only, and "
      "ignore an outlier. Rinse the burette with the titrant and the pipette with the solution it will deliver, but rinse "
      "the flask with water only, since its moles of analyte do not change.", refs=['content', 'ex22q19', 'ar22q19'], covers=['V5'], elements=[1], exam=['X22-19']),
    S("The titrant's concentration is often found by first standardising it against a primary standard, as in the 2025 "
      "permanganate and oxalate question. A solution of known concentration then finds an unknown. Use the average titre, in litres, "
      "for the moles.", refs=['ex25q20', 'ar25q20', 'content'], covers=['V5', 'M6'], elements=[1], exam=['X25-20'], anim=2),
]),
Scene('indicators', P3, 'Indicators and equivalence points', V.ph_curve, [
    S("Acid base titrations are followed by the change in pH. At the equivalence point the pH jumps sharply. Indicators are "
      "weak acids or bases, where the acid form is a different colour from the base form, so the colour changes over a narrow pH range.",
      refs=['content'], covers=['V1', 'V2'], elements=[1]),
    S("Pick an indicator that changes colour on the steep part of the curve. For strong acid with strong base, both "
      "phenolphthalein and methyl orange change within the jump. A pH meter can record the whole curve.", refs=['content'], covers=['V1', 'V2'], elements=[1]),
    S("When a weak acid is titrated with a strong base, the equivalence point is above seven, because the salt is basic, "
      "so phenolphthalein suits and methyl orange does not. These curves are illustrative, and indicator ranges are reference data.",
      refs=['content'], covers=['V2', 'V1'], elements=[1]),
]),
Scene('we_acidbase', P3, 'Acid-base titration calculation', Slide('worked', title='Worked example 5: vinegar', chip='Element 1 · volumetric analysis',
    q='10.00 mL of vinegar (density 1.01 g mL⁻¹) is diluted to 100.0 mL. 25.00 mL aliquots are titrated with 0.1012 mol L⁻¹ NaOH: titres 18.42, 18.38, 18.40 and 18.61 mL. CH₃COOH + NaOH → CH₃COONa + H₂O. Find the percentage by mass of ethanoic acid in the vinegar.',
    size=22,
    rows=[dict(s=0, t='Concordant titres: 18.42, 18.38, 18.40 (outlier 18.61 dropped).   Mean = 18.40 mL', col='#eef2f8'),
          dict(s=1, t='n(NaOH) = c × V = 0.1012 × 0.01840 = 1.862 × 10⁻³ mol = n(CH₃COOH) in the 25.00 mL aliquot', col='#ffd166'),
          dict(s=2, t='Aliquot is 25.00 of 100.0 mL: n in the 100.0 mL = 1.862 × 10⁻³ × (100.0 / 25.00) = 7.448 × 10⁻³ mol', col='#ffd166'),
          dict(s=2, t='That all came from the 10.00 mL of vinegar:  m = 7.448 × 10⁻³ × 60.05 = 0.4473 g', col='#eef2f8'),
          dict(s=3, t='Mass of vinegar = 10.00 mL × 1.01 g mL⁻¹ = 10.10 g;   % = 0.4473 / 10.10 × 100 = 4.43%', col='#9bde7e'),
          dict(s=3, sf='= 4.43 % by mass (3 s.f.)', t='', gap=0)]), [
    S("Worked example five, an acid base titration. First choose the concordant titres, here eighteen point four two, eighteen point "
      "three eight and eighteen point four oh. The outlier is dropped. The mean is eighteen point four oh millilitres.",
      refs=['content', 'ex21q18', 'ar21q18'], covers=['V3', 'V5'], elements=[1], exam=['X21-18'],
      problem='Titres of 18.42, 18.38, 18.40 and 18.61 mL of 0.1012 mol L⁻¹ NaOH neutralise 25.00 mL aliquots of diluted vinegar. Find the mass percentage of ethanoic acid.'),
    S("Moles of sodium hydroxide are concentration times volume in litres, one point eight six two times ten to the minus "
      "three. The equation is one to one, so that is the moles of ethanoic acid in the aliquot. In the 2021 question, the "
      "ratio was two to one, because sodium carbonate takes two hydrogen ions.", refs=['info', 'content', 'ar21q18', 'ex21q18'], covers=['V3'], elements=[1], exam=['X21-18']),
    S("Scale up for the aliquot fraction. Twenty five of one hundred millilitres is a factor of four, so there are seven point "
      "four four eight times ten to the minus three moles in the flask, all from the ten millilitres of vinegar. "
      "A flow chart helps with aliquots and dilutions, a report suggested. The mass is zero point four four seven three grams.",
      refs=['ar22q19', 'content'], covers=['V3', 'V5', 'M8'], elements=[1], exam=['X22-19']),
    S("Divide by the mass of vinegar, from the density: ten point one grams. The answer is four point four three percent "
      "ethanoic acid by mass. Labelling the species at each step, as in n of C H three C O O H, earns the communication marks.",
      refs=['ar23g', 'ar24g'], covers=['V3', 'V5', 'M4'], elements=[1]),
]),
Scene('we_redox', P3, 'Redox titration: iron', Slide('worked', title='Worked example 6: redox titration', chip='Element 1 · volumetric analysis',
    q='An iron tablet of mass 1.265 g is dissolved in acid and made up to 250.0 mL. 25.00 mL aliquots need a mean of 21.35 mL of 0.01000 mol L⁻¹ KMnO₄: MnO₄⁻ + 5Fe²⁺ + 8H⁺ → Mn²⁺ + 5Fe³⁺ + 4H₂O. Find the percentage of iron by mass in the tablet.',
    rows=[dict(s=0, t='n(MnO₄⁻) = 0.01000 × 0.02135 = 2.135 × 10⁻⁴ mol', col='#ffd166'),
          dict(s=1, t='Ratio 1 : 5:   n(Fe²⁺) in the aliquot = 5 × 2.135 × 10⁻⁴ = 1.0675 × 10⁻³ mol', col='#ffd166'),
          dict(s=2, t='Whole 250.0 mL = 10 aliquots:  n(Fe²⁺) = 1.0675 × 10⁻² mol;   m(Fe) = 1.0675 × 10⁻² × 55.85 = 0.5962 g', col='#eef2f8'),
          dict(s=3, t='% Fe = 0.5962 / 1.265 × 100 = 47.13%', col='#9bde7e'),
          dict(s=3, sf='= 47.1 % by mass (4 s.f. data, 3 s.f. shown)', t='', gap=0),
          dict(s=3, t='Use the CONCENTRATION or moles from the right step, not the mass of the sample, to find the moles.', col='#f15bb5', size=22)]), [
    S("Redox titrations use the mole ratio from the overall equation, which you combine from half-equations if needed. Worked example six. "
      "Permanganate reacts with iron two plus in a one to five ratio. The moles of permanganate are zero point oh one oh oh times "
      "zero point oh two one three five, two point one three five times ten to the minus four.",
      refs=['content', 'ex22q19', 'ar22q19', 'ex25q20', 'ar25q20'], covers=['V4', 'V5'], elements=[1], exam=['X22-19', 'X25-20'],
      problem='A 1.265 g iron tablet is made up to 250.0 mL; 25.00 mL needs 21.35 mL of 0.01000 mol L⁻¹ KMnO₄. What is the % of iron by mass?'),
    S("Multiply by five for the iron two plus in the aliquot: one point oh six seven five times ten to the minus three moles. "
      "A common error was not using the five to one ratio.", refs=['ar25q20', 'ar22q19'], covers=['V4'], elements=[1], exam=['X25-20', 'X22-19']),
    S("The aliquot was a tenth of the solution, so ten times that is in the tablet: zero point oh one oh six eight moles, and zero "
      "point five nine six two grams of iron. In 2025, many students used the moles in the aliquot with the whole mass. "
      "Using the concentration from the previous part, rather than a rounded value, is also important.",
      refs=['ar25q20', 'ar25g'], covers=['V4', 'V5'], elements=[1], exam=['X25-20']),
    S("The percentage of iron in the tablet is forty seven point one percent. Check that it is realistic, less than one hundred, "
      "and do not adjust your working to get a realistic value: markers penalised students who manipulated an error to get one.",
      refs=['ar25q20'], covers=['V4', 'M4'], elements=[1], exam=['X25-20']),
]),
Scene('we_unfamiliar', P3, 'Unfamiliar reactants: ethanol in wine', Slide('worked', title='Worked example 7: an unfamiliar redox titration', chip='Element 1 · A standard',
    q='10.00 mL of wine is diluted to 250.0 mL. A 25.00 mL aliquot reacts with 18.40 mL of 0.06000 mol L⁻¹ K₂Cr₂O₇ (acidified): 3C₂H₅OH + 2Cr₂O₇²⁻ + 16H⁺ → 3CH₃COOH + 4Cr³⁺ + 11H₂O. Find the mass of ethanol in 100 mL of wine.',
    rows=[dict(s=0, t='The reaction is GIVEN: use its ratio, 3 ethanol : 2 dichromate.', col='#b3c0d4', size=22),
          dict(s=0, t='n(Cr₂O₇²⁻) = 0.06000 × 0.01840 = 1.104 × 10⁻³ mol', col='#ffd166'),
          dict(s=1, t='n(C₂H₅OH) in the aliquot = 1.104 × 10⁻³ × 3/2 = 1.656 × 10⁻³ mol', col='#ffd166'),
          dict(s=2, t='Aliquot factor 250.0 / 25.00 = 10:  n = 1.656 × 10⁻² mol in 10.00 mL of wine', col='#eef2f8'),
          dict(s=2, t='m = 1.656 × 10⁻² × 46.07 = 0.7629 g in 10.00 mL', col='#eef2f8'),
          dict(s=3, t='Per 100 mL: 0.7629 × 10 = 7.63 g', col='#9bde7e'),
          dict(s=3, sf='= 7.63 g per 100 mL (3 s.f.)', t='', gap=0),
          dict(s=3, t='Ratio from the equation; half-equation check: ethanol → ethanoic acid loses 4 e⁻, Cr₂O₇²⁻ gains 6 e⁻ (3 × 4 = 2 × 6).', col='#b3c0d4', size=21)]), [
    S("At A standard, the reactants are unfamiliar, and the equation is given. Breathalysers and the analysis of wine rely "
      "on redox reactions like this, one of the course contexts. Here, ethanol is oxidised by acidified dichromate to ethanoic "
      "acid. The ratio is three ethanol to two dichromate.", refs=['standards', 'content', 'appendix'], covers=['V4', 'A1', 'A2'], elements=[1],
      problem='A 25.00 mL aliquot of 10.00 mL of wine diluted to 250.0 mL needs 18.40 mL of 0.06000 mol L⁻¹ Cr₂O₇²⁻ (3C₂H₅OH : 2Cr₂O₇²⁻). Find the ethanol in 100 mL of wine.'),
    S("Moles of dichromate are one point one oh four times ten to the minus three. Multiply by three over two for ethanol: "
      "one point six five six times ten to the minus three moles in the aliquot. Always use the ratio, and do not assume one to one.",
      refs=['ar24q20', 'content'], covers=['V4', 'V5'], elements=[1], exam=['X24-20']),
    S("The aliquot was one tenth of the diluted solution, which came from ten millilitres of wine. So there are one point six five "
      "six times ten to the minus two moles of ethanol, and zero point seven six three grams, in ten millilitres.", refs=['content'], covers=['V5', 'M8'], elements=[1]),
    S("Per one hundred millilitres, that is seven point six three grams. As a check on the stoichiometry, ethanol loses four electrons "
      "each and dichromate gains six: three times four equals two times six. This is how you can build the ratio from half-equations.",
      refs=['content', 'standards'], covers=['V4', 'A2'], elements=[1]),
]),
Scene('we_iodometric', P3, 'A two-stage titration', Slide('worked', title='Worked example 8: a chain of reactions', chip='Element 1 · A standard',
    q='A 10.0 g sample of iodised salt is dissolved and treated with excess KI and acid: IO₃⁻ + 5I⁻ + 6H⁺ → 3I₂ + 3H₂O. The iodine formed needs 14.80 mL of 0.00200 mol L⁻¹ thiosulfate: I₂ + 2S₂O₃²⁻ → 2I⁻ + S₄O₆²⁻. Find the mass of KIO₃ per kilogram of salt.',
    rows=[dict(s=0, t='Link the two equations through I₂:   S₂O₃²⁻  →  I₂  →  IO₃⁻', col='#b3c0d4', size=22),
          dict(s=0, t='n(S₂O₃²⁻) = 0.00200 × 0.01480 = 2.96 × 10⁻⁵ mol', col='#ffd166'),
          dict(s=1, t='n(I₂) = ½ × 2.96 × 10⁻⁵ = 1.48 × 10⁻⁵ mol;     n(IO₃⁻) = ⅓ × 1.48 × 10⁻⁵ = 4.933 × 10⁻⁶ mol', col='#ffd166'),
          dict(s=2, t='m(KIO₃) = 4.933 × 10⁻⁶ × 214.0 = 1.056 × 10⁻³ g = 1.056 mg in 10.0 g of salt', col='#eef2f8'),
          dict(s=3, t='Per kilogram: 1.056 mg × (1000 / 10.0) = 105.6 mg', col='#9bde7e'),
          dict(s=3, sf='= 106 mg per kg (3 s.f.; illustrative numbers)', t='', gap=0)]), [
    S("Some analyses use two reactions. Iodate frees iodine from iodide, and the iodine is then titrated with thiosulfate. "
      "The idea is to follow the moles along the chain: thiosulfate to iodine to iodate. In 2023 and 2024, copper and hypochlorite "
      "were analysed this way.", refs=['ex23q23', 'ar23q23', 'ex24q23', 'ar24q23', 'content'], covers=['V4', 'V5'], elements=[1], exam=['X23-23', 'X24-23'],
      problem='14.80 mL of 0.00200 mol L⁻¹ thiosulfate titrates the I₂ formed from KIO₃ in 10.0 g of salt (IO₃⁻ → 3I₂; I₂ → 2S₂O₃²⁻). Find the mg of KIO₃ per kg of salt.'),
    S("Thiosulfate is two point nine six times ten to the minus five moles. Divide by two for iodine, then by three for iodate. "
      "The amount of iodine was asked for specifically in 2024: the word amount means moles, not mass or volume.",
      refs=['ar24q23', 'ar24g'], covers=['V4'], elements=[1], exam=['X24-23']),
    S("Multiply by the molar mass, two fourteen, to get one point oh five six milligrams in ten grams. Watch for the extra step "
      "when a dilution is involved: in the copper question, students added unnecessary steps to the dilution.", refs=['ar23q23', 'info_ar'], covers=['V5', 'M8'], elements=[1], exam=['X23-23']),
    S("Scaled to a kilogram, that is about one hundred and six milligrams. The numbers are illustrative. Show the chain "
      "clearly, with each species labelled, and you can earn part marks even if the final value is wrong.", refs=['ar24g'], covers=['V4', 'V5'], elements=[1]),
]),

# ------------------------------------------------------------------ Part 4: gases and electrolysis
Scene('we_gases', P4, 'Gas calculations', Slide('worked', title='Worked example 9: gases in reactions', chip='Element 2 · gases',
    q='(a) 8.00 g of CaCO₃ reacts with 60.0 mL of 1.50 mol L⁻¹ HCl: CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂. Find the volume of CO₂ at SLC. (b) 50.0 mL of H₂ is collected over water at 22.0 °C and 100.8 kPa total pressure (vapour pressure of water 2.64 kPa, reference data). Find n(H₂) and the mass of zinc that reacted (Zn + 2H⁺ → Zn²⁺ + H₂).',
    size=20,
    rows=[dict(s=0, t='n(CaCO₃) = 8.00 / 100.09 = 0.07993 mol;   n(HCl) = 0.0600 × 1.50 = 0.0900 mol', col='#eef2f8'),
          dict(s=0, t='HCl needed for all the CaCO₃ = 2 × 0.07993 = 0.1599 mol > 0.0900:  HCl is limiting', col='#ffd166'),
          dict(s=1, t='n(CO₂) = ½ × 0.0900 = 0.0450 mol;   V = n × Vm = 0.0450 × 24.5 = 1.1025 L', col='#9bde7e'),
          dict(s=1, sf='= 1.10 L (3 s.f.): the question asks for VOLUME', t='', gap=0),
          dict(s=2, t='p(H₂) = 100.8 − 2.64 = 98.16 kPa;   T = 22.0 + 273.15 = 295.15 K;   V = 0.0500 L', col='#eef2f8'),
          dict(s=2, t='n = pV / RT = 98.16 × 0.0500 / (8.31 × 295.15) = 2.001 × 10⁻³ mol   (NOT the combined gas law)', col='#ffd166'),
          dict(s=3, t='n(Zn) = n(H₂) = 2.001 × 10⁻³ mol;   m = 2.001 × 10⁻³ × 65.38 = 0.1308 g', col='#9bde7e'),
          dict(s=3, sf='= 0.131 g (3 s.f.)', t='', gap=0)]), [
    S("Gases join the stoichiometry through the molar volume or the ideal gas equation. The sheet gives twenty four point five "
      "litres per mole at standard laboratory conditions. Worked example nine, part a. Calcium carbonate and hydrochloric acid: "
      "check which is limiting, with a calculation. All the carbonate would need zero point one six oh moles of acid, but only zero point oh nine oh is given, so the acid is limiting.",
      refs=['info_data', 'ex24q19', 'ar24q19', 'ex23q21', 'ar23q21'], covers=['G2', 'M9', 'M10'], elements=[2], exam=['X24-19', 'X23-21'],
      problem='8.00 g of CaCO₃ reacts with 60.0 mL of 1.50 mol L⁻¹ HCl. What volume of CO₂ forms at SLC?'),
    S("The carbon dioxide is half the moles of acid, zero point oh four five oh moles, which is one point one oh litres. The question "
      "asked for the volume of carbon dioxide, and many students gave the mass or concentration. The ideal gas equation could be used "
      "instead, with the temperature in kelvin.", refs=['ar24q19', 'info'], covers=['G2', 'G3'], elements=[2], exam=['X24-19']),
    S("Part b. A gas collected over water is mixed with water vapour. Subtract the vapour pressure to get the pressure of the "
      "gas: ninety eight point one six kilopascals. Use P V equals n R T with R as eight point three one and the "
      "temperature in kelvin. The majority of students in 2024 did not account for the vapour pressure, and the combined gas equation is wrong here.",
      refs=['info', 'info_data', 'ex24q20', 'ar24q20'], covers=['G2', 'G3', 'G1'], elements=[2], exam=['X24-20'],
      problem='50.0 mL of H₂ is collected over water at 22.0 °C and a total pressure of 100.8 kPa (vapour pressure 2.64 kPa). How many moles of H₂?'),
    S("The moles of hydrogen equal the moles of zinc, so the mass is zero point one three one grams. For other questions, "
      "ammonia and oxygen in 2025 gave a gas pressure from moles using the ideal gas equation. And in 2023, changes in "
      "pressure and temperature of a gas used the combined equation. Match R to your pressure units, and convert temperatures.",
      refs=['ar25q19', 'ex25q19', 'ex23q18', 'ar23q18', 'ex22q23', 'ar22q23'], covers=['G3', 'G1'], elements=[2], exam=['X25-19', 'X23-18', 'X22-23']),
]),
Scene('we_faraday', P4, "Faraday's laws", Slide('worked', title='Worked example 10: electrolysis calculations', chip='Element 2 · electrolysis',
    q='Copper(II) and chromium(III) solutions are electrolysed in two cells in series with a steady current of 2.00 A. 1.50 g of copper is deposited. (a) For how long did the current flow? (b) What mass of chromium is deposited at the same time?',
    rows=[dict(s=0, t='Cu²⁺ + 2e⁻ → Cu:   n(Cu) = 1.50 / 63.55 = 0.02360 mol;   n(e⁻) = 2 × 0.02360 = 0.04721 mol', col='#eef2f8'),
          dict(s=1, t='n(e⁻) = It / F   so   t = n(e⁻) × F / I = 0.04721 × 96 500 / 2.00 = 2278 s', col='#ffd166'),
          dict(s=1, sf='= 2.28 × 10³ s = 38.0 min (3 s.f.)', t='', gap=0),
          dict(s=2, t='Cr³⁺ + 3e⁻ → Cr:   same n(e⁻) in series:  n(Cr) = 0.04721 / 3 = 0.01574 mol', col='#eef2f8'),
          dict(s=3, t='m(Cr) = 0.01574 × 52.00 = 0.8183 g', col='#9bde7e'),
          dict(s=3, sf='= 0.818 g (3 s.f.)', t='', gap=0),
          dict(s=3, t='Do not use “m = M I t / zF” without showing how z (electrons per ion) is found.', col='#f15bb5', size=22)]), [
    S("Faraday's laws link charge to moles of electrons: n of electrons equals I t over F, on your information sheet, with F "
      "equal to ninety six thousand five hundred coulombs per mole. Worked example ten. Copper two plus needs two electrons "
      "per atom, so one point five grams of copper is zero point oh four seven two one moles of electrons.",
      refs=['info', 'info_data', 'content', 'ex22q22', 'ar22q22'], covers=['X1'], elements=[2], exam=['X22-22'],
      problem='A current of 2.00 A deposits 1.50 g of copper from Cu²⁺. For how long did it flow?'),
    S("The time is moles of electrons times F over the current: about two thousand two hundred and seventy eight seconds, or thirty eight "
      "minutes. Convert hours and minutes to seconds. This was a common error in 2024.",
      refs=['ar24q20', 'ar22q22'], covers=['X1'], elements=[2], exam=['X24-20', 'X22-22']),
    S("In cells in series, the same charge passes through both, so the moles of electrons are equal. Chromium three plus "
      "needs three electrons per atom, so the moles of chromium are a third of the electrons. Markers noted a three over two "
      "fraction error when students compared copper to gold directly.",
      refs=['ar22q22', 'ex22q22', 'ex23q17', 'ar23q17'], covers=['X1'], elements=[2], exam=['X22-22', 'X23-17']),
    S("Multiply by the molar mass of chromium for zero point eight one eight grams. Remember that the efficiency is the actual "
      "mass over the theoretical mass. In 2024, a ninety nine percent efficiency and a reason for loss was asked: a specific "
      "reason, such as chromium not sticking to the cathode. Human error was not accepted.",
      refs=['ex24q20', 'ar24q20', 'ex21q23', 'ar21q23'], covers=['X1', 'M4'], elements=[2], exam=['X24-20', 'X21-23']),
]),

# ------------------------------------------------------------------ Part 5
Scene('we_hess', P5, 'Hess and calorimetry', Slide('worked', title='Worked example 11: energy calculations', chip='Element 2 · energy',
    q='(a) Use C(s) + O₂ → CO₂ (−393.5), H₂(g) + ½O₂ → H₂O(l) (−285.8) and C₂H₆(g) + 3½O₂ → 2CO₂ + 3H₂O(l) (−1560) kJ mol⁻¹ (reference data) to find ΔH for 2C(s) + 3H₂(g) → C₂H₆(g). (b) 2.00 g of hexane (ΔH of combustion −4163 kJ mol⁻¹) heats 1000.0 g of water from 18.0 °C. Find the final temperature.',
    size=22,
    rows=[dict(s=0, t='Write the manipulations: ×2 on the first, ×3 on the second, REVERSE the third (sign flips)', col='#b3c0d4', size=21),
          dict(s=0, t='2C + 2O₂ → 2CO₂   −787.0       3H₂ + 1½O₂ → 3H₂O   −857.4       2CO₂ + 3H₂O → C₂H₆ + 3½O₂   +1560', col='#eef2f8', size=21),
          dict(s=1, t='ΔH = −787.0 − 857.4 + 1560 = −84.4 kJ mol⁻¹', col='#9bde7e'),
          dict(s=2, t='n(C₆H₁₄) = 2.00 / 86.18 = 0.02321 mol;   E = 0.02321 × 4163 = 96.61 kJ released', col='#eef2f8'),
          dict(s=3, t='E = mcΔT:   ΔT = 96 610 / (1000.0 × 4.184) = 23.09 K;   final T = 18.0 + 23.1 = 41.1 °C', col='#9bde7e'),
          dict(s=3, sf='= 41.1 °C (the water must be WARMER: a drop would be unrealistic)', t='', gap=0)]), [
    S("Section D also tests calculations from criterion six. Hess's law appeared every year. Write out how you manipulate each "
      "equation, by words, equations or algebra, and sum them. Here, multiply the first by two and the second by three, and "
      "reverse the combustion of ethane, changing its sign. The enthalpy of formation is minus eighty four point four kilojoules per mole.",
      refs=['content', 'ex22q18', 'ar22q18', 'ex23q21', 'ar23q21', 'ex24q21', 'ar24q21', 'ex25q18', 'ar25q18'], covers=['X1'], elements=[2], exam=['X22-18', 'X23-21', 'X24-21', 'X25-18'],
      problem='Use ΔH of combustion of C, H₂ and C₂H₆ to find ΔH of formation of C₂H₆ from 2C + 3H₂.'),
    S("Be careful about which enthalpy a later part wants. In 2022, most students used the enthalpy of formation instead of "
      "the enthalpy of combustion that the question stated, to find the heat from burning benzene. And when a question says use your "
      "answer to the previous part, you must, rather than the backup value given.",
      refs=['ar22q18', 'ar24q21', 'ex22q18'], covers=['X1'], elements=[2], exam=['X22-18', 'X24-21']),
    S("For heating water, find the moles of fuel, multiply by the enthalpy of combustion for the heat, and then use m c "
      "delta T from the information sheet. Two grams of hexane releases ninety six point six kilojoules. In 2025, the energy "
      "per mole of reaction was asked for forming forty grams of sulfur, so apply the ratio to the heat of reaction carefully.",
      refs=['info', 'ar23q21', 'ar25q18', 'ex25q18'], covers=['X1'], elements=[2], exam=['X23-21', 'X25-18', 'X21-19']),
    S("Then the temperature rise is twenty three point one degrees, so the final temperature is forty one point one degrees. A "
      "drop in temperature is not realistic for a combustion, and the question asked for the final temperature, not "
      "just the rise. Convert joules and kilojoules consistently.", refs=['ar23q21', 'ar21q19', 'ex21q19'], covers=['X1'], elements=[2], exam=['X23-21', 'X21-19']),
]),
Scene('we_equilibrium', P5, 'Equilibrium and pH calculations', Slide('worked', title='Worked example 12: K, Q and pH', chip='Element 2 · equilibrium and pH',
    q='(a) N₂O₄ ⇌ 2NO₂: 0.500 mol of N₂O₄ is placed in 2.50 L; at equilibrium 0.0300 mol L⁻¹ of N₂O₄ has reacted. Find Kc, and the direction when [N₂O₄] = 0.100 and [NO₂] = 0.0200 mol L⁻¹. (b) 50.00 mL of 0.0800 mol L⁻¹ HCl is mixed with 30.00 mL of 0.0600 mol L⁻¹ Ba(OH)₂. Find the pH.',
    size=20,
    rows=[dict(s=0, t='[N₂O₄]₀ = 0.500 / 2.50 = 0.200;   at equilibrium [N₂O₄] = 0.170, [NO₂] = 2 × 0.0300 = 0.0600 mol L⁻¹', col='#eef2f8'),
          dict(s=0, t='Kc = [NO₂]² / [N₂O₄] = 0.0600² / 0.170 = 0.02118 mol L⁻¹', col='#9bde7e'),
          dict(s=0, sf='Kc = 2.12 × 10⁻² mol L⁻¹ (3 s.f.)', t='', gap=0),
          dict(s=1, t='Q = 0.0200² / 0.100 = 4.0 × 10⁻³ < Kc:  not at equilibrium; the FORWARD reaction is favoured', col='#ffd166'),
          dict(s=2, t='n(H⁺) = 0.0500 × 0.0800 = 4.000 × 10⁻³ mol;   n(OH⁻) = 2 × 0.0300 × 0.0600 = 3.600 × 10⁻³ mol', col='#eef2f8'),
          dict(s=2, t='H⁺ + OH⁻ → H₂O:  excess n(H⁺) = 4.00 × 10⁻⁴ mol in 0.0800 L:   [H⁺] = 5.000 × 10⁻³ mol L⁻¹', col='#ffd166'),
          dict(s=3, t='pH = −log(5.000 × 10⁻³) = 2.30', col='#9bde7e'),
          dict(s=3, sf='= 2.30 (2 d.p.)', t='', gap=0),
          dict(s=3, t='If the BASE is in excess: [OH⁻] = excess / total V, then [H⁺] = Kw / [OH⁻].', col='#b3c0d4', size=21)]), [
    S("Equilibrium calculations: convert amounts to concentrations at equilibrium. Initial concentration is zero point two, "
      "and zero point oh three oh reacted, so dinitrogen tetroxide is zero point one seven oh and nitrogen dioxide is twice "
      "zero point oh three, zero point oh six. K c is zero point oh six squared over zero point one seven, about two point one two "
      "times ten to the minus two. Use equilibrium values, not the initial ones.",
      refs=['info_eq', 'ar23q20', 'ex22q21', 'ar22q21', 'ex25q21', 'ar25q21'], covers=['X1'], elements=[2], exam=['X22-21', 'X23-20', 'X25-21'],
      problem='0.500 mol of N₂O₄ in 2.50 L; 0.0300 mol L⁻¹ reacts to give 2NO₂. What is Kc?'),
    S("For the reaction quotient, use the same expression with the given concentrations, and compare with K. Q is four times "
      "ten to the minus three, less than K, so the forward reaction is favoured. Do not compare Q with zero. The expression "
      "must be Q, not K c, and a statement that Q is not equal to K shows the mixture is not at equilibrium.",
      refs=['ar22q21', 'ar25q21', 'ar21q22', 'ex21q22', 'ex25q21'], covers=['X1'], elements=[2], exam=['X22-21', 'X25-21', 'X21-22']),
    S("For pH after mixing, first find the moles of each reagent, taking account of the formula: barium hydroxide gives two "
      "hydroxides. Find which is in excess. The hydrogen ion is in excess here, by four times ten to the minus four moles, in "
      "eighty millilitres. Most students in 2025 failed to find the excess correctly, since there was no scaffolding.",
      refs=['ar25q22', 'ex25q22', 'ex22q24', 'ar22q24', 'ex23q22', 'ar23q22', 'info_eq'], covers=['X1'], elements=[2], exam=['X25-22', 'X22-24', 'X23-22'],
      problem='50.00 mL of 0.0800 mol L⁻¹ HCl is mixed with 30.00 mL of 0.0600 mol L⁻¹ Ba(OH)₂. What is the pH?'),
    S("The pH is minus log of five times ten to the minus three, two point three oh. When the base is in excess, find "
      "the hydroxide concentration and use Kw, or the p O H route, which markers accepted equally. The final pH should be "
      "acidic if acid is in excess, and basic otherwise: do not use the moles of H plus for an excess of base.",
      refs=['ar23q22', 'ar22q24', 'ar21q21', 'ex21q21'], covers=['X1'], elements=[2], exam=['X23-22', 'X22-24', 'X21-21']),
]),
Scene('we_weak_acid', P5, 'Weak acids: assumptions and dilution', Slide('worked', title='Worked example 13: a weak acid', chip='Element 2 · pH',
    q='Propanoic acid has Ka = 1.35 × 10⁻⁵ mol L⁻¹ (reference data). (a) Find the pH of 0.200 mol L⁻¹ propanoic acid, stating your assumption. (b) What percentage is ionised? (c) The solution is diluted to 0.0200 mol L⁻¹: does the percentage ionised increase or decrease?',
    rows=[dict(s=0, t='CH₃CH₂COOH ⇌ H⁺ + CH₃CH₂COO⁻:   Ka = [H⁺][A⁻] / [HA] = x² / (0.200 − x)', col='#eef2f8'),
          dict(s=0, t='Assume x << 0.200, so 0.200 − x ≈ 0.200:   x = √(1.35×10⁻⁵ × 0.200) = 1.643 × 10⁻³ mol L⁻¹', col='#ffd166'),
          dict(s=1, t='pH = −log(1.643 × 10⁻³) = 2.78 (2 d.p.)', col='#9bde7e'),
          dict(s=1, t='% ionised = 1.643 × 10⁻³ / 0.200 × 100 = 0.822%  (assumption fine: < 5%)', col='#9bde7e'),
          dict(s=2, t='Diluted to 0.0200:  x = √(1.35×10⁻⁵ × 0.0200) = 5.196 × 10⁻⁴;   % = 2.60%', col='#eef2f8'),
          dict(s=3, t='The percentage INCREASES on dilution: Le Chatelier: more particles on the right, so dilution favours ionisation.', col='#9bde7e', size=22)]), [
    S("Weak acid calculations need the expression first. Many students lost marks in 2024 for not writing the equilibrium "
      "expression. For propanoic acid, K a is x squared over zero point two minus x. The most important assumption is that x is "
      "much smaller than the starting concentration, so zero point two minus x is about zero point two. That avoids a quadratic.",
      refs=['ar24q22', 'ex24q22', 'ex23q22', 'ar23q22', 'info_eq'], covers=['X1'], elements=[2], exam=['X24-22', 'X23-22'],
      problem='What is the pH of 0.200 mol L⁻¹ propanoic acid, Ka = 1.35 × 10⁻⁵?'),
    S("Then x is one point six four times ten to the minus three, and the pH is two point seven eight, to two decimal places as "
      "requested. The percentage ionised is x over the starting concentration times a hundred: zero point eight two two percent, "
      "so the assumption of a small x holds.", refs=['ar24q22'], covers=['X1'], elements=[2], exam=['X24-22']),
    S("If the solution is diluted to a tenth, x is five point one nine six times ten to the minus four, and the percentage "
      "ionised rises to two point six percent. The question asks about the percentage of dissociation, not about the value of K a, "
      "which stays the same. Support the maths with an equilibrium argument, as markers wanted.",
      refs=['ar24q22', 'ex24q22'], covers=['X1'], elements=[2], exam=['X24-22'],
      problem='0.200 mol L⁻¹ propanoic acid is diluted to 0.0200 mol L⁻¹. Does the percentage ionised increase or decrease?'),
    S("Explain it with Le Chatelier's principle: diluting lowers all concentrations, and the equilibrium shifts towards the side with "
      "more dissolved particles, so more acid ionises. That is the explanation, with the calculation, that a good answer to part c gave.",
      refs=['ar24q22'], covers=['X1'], elements=[2], exam=['X24-22']),
]),

# ------------------------------------------------------------------ Part 6
Scene('synthesis', P6, 'Synthesis and percentage yield', V.synthesis, [
    S("Chemical synthesis is making a product with specific properties, such as a drug, a fuel, a cosmetic or a cleaning "
      "product. You choose reagents that give the product you want, and which are cheap, available and safe. The course marks this as new content, "
      "compared with the earlier chemistry course.", refs=['content'], covers=['Y1'], elements=[2]),
    S("To maximise yield, use an excess of the cheaper reagent, remove a product as it forms, and choose conditions that favour the "
      "products, using the Le Chatelier ideas from criterion six, while keeping the rate workable. Control the temperature, since a high "
      "temperature can also cause side reactions.", refs=['content'], covers=['Y2'], elements=[2]),
    S("To maximise purity, separate and purify the product by filtration, recrystallisation or distillation, wash and dry it, "
      "and start with pure reagents. Then calculate the percentage yield from the theoretical mass, found from the limiting reagent, "
      "and the actual mass obtained.", refs=['content'], covers=['Y2', 'Y3', 'M4'], elements=[2]),
    S("In many industries, including pharmaceuticals, these choices balance cost, yield, purity, safety and environmental impact. "
      "A reaction with an excellent yield is not useful if the product cannot be separated from by-products.", refs=['content', 'standards'], covers=['Y1', 'Y2'], elements=[2]),
]),
Scene('we_yield', P6, 'Worked example: making aspirin', Slide('worked', title='Worked example 14: percentage yield', chip='Element 2 · yield',
    q='Aspirin (C₉H₈O₄, M = 180.16) is made from salicylic acid (C₇H₆O₃, M = 138.12) with excess ethanoic anhydride: C₇H₆O₃ + (CH₃CO)₂O → C₉H₈O₄ + CH₃COOH. 5.00 g of salicylic acid gives 4.85 g of purified product. Find the percentage yield.',
    rows=[dict(s=0, t='n(salicylic acid) = 5.00 / 138.12 = 0.03620 mol   (the anhydride is in excess: salicylic acid is limiting)', col='#eef2f8'),
          dict(s=1, t='Ratio 1 : 1:   theoretical n(aspirin) = 0.03620 mol;   m = 0.03620 × 180.16 = 6.522 g', col='#ffd166'),
          dict(s=2, t='% yield = actual / theoretical × 100 = 4.85 / 6.522 × 100 = 74.4%', col='#9bde7e'),
          dict(s=2, sf='= 74.4 % (3 s.f.)', t='', gap=0),
          dict(s=3, t='Why less than 100%: incomplete reaction (equilibrium), side reactions, losses in filtering, washing and transfers.', col='#b3c0d4', size=22)]), [
    S("Worked example fourteen. Aspirin is made from salicylic acid and an excess of ethanoic anhydride. Because the anhydride is in "
      "excess, the salicylic acid is limiting. Five grams is zero point oh three six two oh moles.",
      refs=['content', 'info_ar'], covers=['Y3', 'M9'], elements=[2],
      problem='5.00 g of salicylic acid (C₇H₆O₃) with excess anhydride gives 4.85 g of aspirin (C₉H₈O₄). What is the percentage yield?'),
    S("The ratio is one to one, so the theoretical yield is zero point oh three six two oh moles, times one eighty point "
      "one six, six point five two two grams.", refs=['content'], covers=['Y3', 'M2'], elements=[2]),
    S("Percentage yield is four point eight five over six point five two two, seventy four point four percent. The actual yield is always "
      "at most the theoretical one. Reasons for a lower yield are incomplete reaction, side reactions, and losses when filtering "
      "and transferring.", refs=['ex24q20', 'ar24q20', 'content'], covers=['Y3', 'M4'], elements=[2], exam=['X24-20']),
    S("If you can improve the yield, say how: use an excess of the cheaper reagent, remove the by-product, recrystallise carefully to "
      "avoid losing product, and dry fully. A reason must be specific. Non-specific answers such as human error earned no marks.",
      refs=['ar24q20', 'content'], covers=['Y2', 'Y3'], elements=[2], exam=['X24-20']),
]),

# ------------------------------------------------------------------ finish
Scene('exam_tips', P7, 'Tips for tests and the exam', Slide('tips', title='Tips from examiners', counts=[2, 4, 6, 8], tips=[
    'Write each step on its own line, with\nunits and what each number is: n(HCl)',
    'Use YOUR unrounded value from a “show\nthat”, not the rounded one in the question',
    'Final answers need units; use mol L⁻¹,\nnot capital M. s.f. as the data allow',
    'Limiting reagent: show a calculation of\nmoles needed against moles given',
    'Read the question: volume, mass or\nconcentration; “amount” means moles',
    'Titrations: use mean of concordant titres,\nthe mole ratio, and the aliquot factor',
    'Gases: kelvin, the right R, and subtract\nvapour pressure if collected over water',
    'Hess: show how you manipulate each\nequation; reverse means flip the sign']), [
    S("Finally, technique for tests and the exam, from examiners' reports. One: set out each step on its own line, with "
      "units and with a label for the species, such as n of H C l. Two: in a show that question, use your own unrounded value in the following "
      "parts, not the rounded one in the question.", refs=['ar24g', 'ar23g', 'ar22q23', 'ar25g']),
    S("Three: put units on every final answer, write mole per litre rather than capital M, and give the number of significant figures the "
      "data allow. Four: for a limiting reagent, show the calculation. Five: read what the question asks for, such as a volume rather than a "
      "mass, and remember that amount means moles.", refs=['ar25gen', 'ar24g', 'ar24q19', 'ar25q19', 'ar24q23']),
    S("Six: for titrations, use the mean of concordant titres, the mole ratio, and the factor for the aliquot. Seven: for gases, "
      "convert to kelvin, use the matching R, and subtract the vapour pressure for a gas collected over water. Eight: for Hess's "
      "law, show how you manipulate each equation, and remember that reversing flips the sign.",
      refs=['ar22q19', 'ar25q20', 'ar24q20', 'ar25q18', 'ar22q18']),
]),
Scene('more_tips', P7, 'More examiner tips', Slide('tips', title='More tips from examiners', start=9, counts=[4, 8], tips=[
    'Use the right enthalpy: formation or\ncombustion? Check what the question gives',
    'Faraday: moles of electrons first, then the\nratio from the half-equation (z)',
    'Equilibrium: write the expression, use\nequilibrium amounts converted to mol L⁻¹',
    'Q is compared with K: less than K means\nthe forward reaction is favoured',
    'Weak acid: state the assumption x << c,\nand check it. pH to the decimal places asked',
    'Excess reagent: find the moles that\nREACTED, then subtract from those given',
    'Do not manipulate working to reach a\n“realistic” answer; carry errors forward',
    'Source errors exist: if a “show that” value\nis inconsistent, use your own value']), [
    S("More tips. Nine: use the right enthalpy, formation or combustion, as the question gives it. Ten: for Faraday's laws, "
      "find the moles of electrons first and then use the ratio from the half-equation. Eleven: for equilibrium, write the expression "
      "and use equilibrium concentrations. Twelve: if Q is less than K, the forward reaction is favoured.",
      refs=['ar22q18', 'ar24q20', 'ar25q21', 'ar22q21']),
    S("Thirteen: for a weak acid, state the assumption that x is much smaller than the concentration, and check it. Fourteen: for "
      "an excess, find the moles that reacted, and subtract. Fifteen: never alter your working to reach a realistic answer: "
      "markers allow error carried forward. Sixteen: there were errors in a 2024 question, so if a show that value does not match, use your own.",
      refs=['ar24q22', 'ar25q19', 'ar25q20', 'ar24q23']),
]),
Scene('summary', P7, 'Summary', Slide('summary', title='Criterion 8 in one screen', chips=[
    ('n = m / M', '1'), ('c = n / V', '1'), ('N = nNA', '1'), ('PV = nRT', '1'), ('P₁V₁/T₁ = P₂V₂/T₂', '1'),
    ('mole ratio from the equation', '2'), ('limiting reagent: show it', '2'), ('% yield = actual / theoretical', '2'),
    ('% purity', '2'), ('hydrates: include H₂O', '2'), ('c₁V₁ = c₂V₂', 'p'), ('primary standards', 'p'), ('concordant titres', 'p'),
    ('aliquot factor', 'p'), ('redox ratios', 'p'), ('n(e⁻) = It / F', 'g'), ('Hess', 'g'), ('Kc, Q', 'g'), ('pH = −log[H⁺]', 'g'),
    ('units and s.f.', 'y')],
    close='Balanced equation, moles, ratio, answer, units. Show every step.'), [
    S("That is the whole of Criterion 8. Every calculation goes through moles: balanced equation, moles of what is given, "
      "the mole ratio, then the quantity asked for. Check for a limiting reagent, handle hydrates, dilutions and aliquots, and use the "
      "ratio in titrations, including unfamiliar ones, which are given in the question. Gases need kelvin and the matching R. "
      "Faraday, Hess, equilibrium and pH calculations are examined here too. Show each step with units, and you will be ready for "
      "your tests and for Section D. Good luck."),
]),
]

_used = {r for sc in SCENES for st in sc.steps for r in st.refs} | {t[1] for t in EXAM_TOPICS.values()} \
    | {t[1] for t in SYLLABUS.values()} | {t[1] for t in ELEMENTS.values()} | {'info', 'info_data', 'info_ar'}
REFS = {k: r for k, r in REFS.items() if k in _used}

VIDEO = Video(
    id='CHM415115_C8_quantitative',
    course=COURSE, course_name='Chemistry', module=MODULE,
    module_name='Criterion 8: Apply logical processes to solve quantitative chemical problems',
    title='Criterion 8: quantitative chemistry, complete revision',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Chemical Information'),
    checks=CHECKS,
    thumbnail=V.thumbnail,
    allowed_overlaps=['apply logical processes to solve quantitative chemical problems'],
    keywords=['mole', 'molar mass', 'concentration', 'dilution', 'primary standard', 'limiting reagent', 'percentage yield',
              'percentage purity', 'gravimetric analysis', 'titration', 'titre', 'concordant', 'aliquot', 'equivalence point',
              'indicator', 'redox titration', 'molar volume', 'ideal gas', 'vapour pressure', 'Faraday', "Hess's law",
              'reaction quotient', 'significant figures', 'synthesis', 'hydrate'],
    description=('A complete revision explainer for TASC Chemistry (CHM415115) Criterion 8: apply logical processes to '
                 'solve quantitative chemical problems. For class tests and the end-of-year exam (Section D). Formulas and '
                 'data from the TASC information sheet are labelled on screen.'),
)
