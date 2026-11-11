"""CHM415115 Chemistry, Criterion 6: Identify and apply principles and theories of thermochemistry, kinetics and equilibrium.

    uv run python -m explainer check   videos/CHM415115/c6_thermo_kinetics_equilibrium.py
    uv run python -m explainer preview videos/CHM415115/c6_thermo_kinetics_equilibrium.py
    uv run python -m explainer thumbnail videos/CHM415115/c6_thermo_kinetics_equilibrium.py
    uv run python -m explainer render  videos/CHM415115/c6_thermo_kinetics_equilibrium.py    # operator only
"""
import math

from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, InfoSheet, import_sibling

COURSE, MODULE = 'CHM415115', 'C6'
L.use(style.theme(COURSE, MODULE))
V = import_sibling(__file__, 'c6_visuals.py')
_CC = import_sibling(__file__, 'chm_common.py')
Slide, Seq, Phased, ch = _CC.Slide, _CC.Seq, _CC.Phased, _CC.ch

P0 = 'Criterion 6 · Overview'
P1 = 'Part 1 · Thermochemistry'
P2 = 'Part 2 · Reaction rates'
P3 = 'Part 3 · Chemical equilibrium'
P4 = 'Part 4 · Acids, bases and pH'
P5 = 'Finish · Tests & exam technique'

# --------------------------------------------------------------------------- references
COURSE_DOC = 'chm415115-9.html'
INFO = 'CHM415115-Chemistry-Information-Sheet.pdf'
SPEC = 'CHM415115-Chemistry-External-Assessment-Specifications.pdf'

EXAM_PAGES = {
    2021: {6: 19, 7: '20-21', 8: '22-23', 9: '24-25', 10: 26},
    2022: {6: 15, 7: '16-17', 8: '18-19', 9: '20-21', 10: '22-23'},
    2023: {6: 19, 7: '20-22', 8: 23, 9: '24-25', 10: '26-27'},
    2024: {6: 19, 7: '20-21', 8: '22-24', 9: 25, 10: '26-27'},
    2025: {7: 19, 8: '20-21', 9: '22-23', 10: '24-27', 11: '28-29'},
}
REPORT_PAGES = {
    2021: {6: 7, 7: 8, 8: 9, 9: 10, 10: 11},
    2022: {6: '6-7', 7: '7-8', 8: '8-9', 9: '9-11', 10: '11-12'},
    2023: {6: '6, 7-8', 7: '6, 8-9', 8: '7, 9', 9: '7, 10', 10: '7, 11'},
    2024: {6: '7, 9', 7: '7, 9-10', 8: '8, 10-11', 9: '8, 11-12', 10: '8, 12-13'},
    2025: {7: '9, 11', 8: '10, 12', 9: '10, 12-13', 10: '10-11, 13-14', 11: '11, 14-15'},
}


def exam(y, q):
    section = 'Part 2' if y == 2021 else 'Section B'
    return Ref(f'CHM415115-Chemistry-TASC-Exam-Paper-{y}.pdf', f'{y} exam, {section}, Question {q}', EXAM_PAGES[y][q])


def report(y, q):
    return Ref(f'CHM415115-Chemistry-Assessment-Report-{y}.pdf', f'{y} assessment report, Criterion 6, Question {q}',
               REPORT_PAGES[y][q])


REFS = {
    'standards': Ref(COURSE_DOC, 'Course document, Criterion 6 standards (element table)'),
    'content': Ref(COURSE_DOC, 'Course document, Science Understanding: thermochemistry, kinetics and equilibrium (Criterion 6)'),
    'appendix': Ref(COURSE_DOC, 'Course document, Appendix 1: contexts (enzymes; collision theory; chemical balance in wine; carbon dioxide in the atmosphere and hydrosphere)'),
    'info': Ref(INFO, 'Information sheet, Chemical Information (E = mcΔT, Cf = VIt/ΔT, n = m/M, c = n/V)', page=2),
    'info_eq': Ref(INFO, 'Information sheet, Chemical Equilibrium Formulae (Kc, Kw, pH)', page=4),
    'info_data': Ref(INFO, 'Information sheet, Chemical Data and Constants (specific heat of water, molar volumes, SLC)', page=1),
    'info_ar': Ref(INFO, 'Information sheet, Table of Relative Atomic Masses', page=9),
    'spec': Ref(SPEC, 'External assessment specifications, Section B', page=3),
}
for _y, _qs in EXAM_PAGES.items():
    for _q in _qs:
        REFS[f'ex{_y % 100}q{_q}'] = exam(_y, _q)
for _y, _qs in REPORT_PAGES.items():
    for _q in _qs:
        REFS[f'ar{_y % 100}q{_q}'] = report(_y, _q)
REFS['ar25g'] = Ref('CHM415115-Chemistry-Assessment-Report-2025.pdf', '2025 assessment report, General Comments', 1)
REFS['ar22b'] = Ref('CHM415115-Chemistry-Assessment-Report-2022.pdf', '2022 assessment report, Section B, Criterion 6 comments', 6)
REFS['ar23b'] = Ref('CHM415115-Chemistry-Assessment-Report-2023.pdf', '2023 assessment report, Section B, Criterion 6 comments', 6)
REFS['ar25b'] = Ref('CHM415115-Chemistry-Assessment-Report-2025.pdf', '2025 assessment report, Section B, Criterion 6 comments', 9)

# --------------------------------------------------------------------------- coverage targets
SYLLABUS = {
    'T1': ('Heat content and enthalpy of chemical reactions', 'content'),
    'T2': ('Forming bonds releases and breaking bonds absorbs energy', 'content'),
    'T3': ('Exothermic reactions release energy and endothermic reactions absorb heat', 'content'),
    'T4': ('Construct enthalpy (potential energy) diagrams including activation energy', 'content'),
    'T5': ('Thermochemical equations: ΔH notation and kJ', 'content'),
    'T6': ('Heat energy released or absorbed for a known mass of reactant or product', 'content'),
    'T7': ('Calibrate a calorimeter', 'content'),
    'T8': ('Heat for a mass of substance with a measured temperature change, E = mcΔT', 'content'),
    'T9': ('Heat required for a change of state, solid to liquid or liquid to gas', 'content'),
    'T10': ('Use the techniques of calorimetry to measure a heat of reaction', 'content'),
    'T11': ('Define bond energy', 'content'),
    'T12': ('Heat of reaction from a table of bond energies', 'content'),
    'T13': ("Hess's Law: ΔH for unknown reactions by summing thermochemical equations", 'content'),
    'K1': ('Define reaction rate as product produced or reactant consumed per time', 'content'),
    'K2': ('Average rate from change in amount: Δn(product) / t', 'content'),
    'K3': ('Average rate from change in concentration: Δc(product) / t', 'content'),
    'K4': ('Collision theory: concentration of reactants, or pressure for gases', 'content'),
    'K5': ('Collision theory: surface area', 'content'),
    'K6': ('Collision theory: temperature', 'content'),
    'K7': ('Collision theory: nature of reactants, bonds to break, complexity such as precipitation', 'content'),
    'K8': ('Collision theory: presence of a catalyst', 'content'),
    'K9': ('Diagram of the distribution of kinetic energy of molecules at a temperature', 'content'),
    'K10': ('Rate rises with temperature because more molecules have enough kinetic energy to react', 'content'),
    'K11': ('Potential energy diagram showing a catalyst giving a lower activation energy by a different pathway', 'content'),
    'K12': ('An enzyme is a biological catalyst', 'content'),
    'Q1': ('Open and closed systems; physical changes and chemical reactions', 'content'),
    'Q2': ('Not all reactions go to completion; products can convert back to reactants', 'content'),
    'Q3': ('Equilibrium is a compromise between minimum enthalpy and maximum entropy', 'content'),
    'Q4': ('Recognise equilibrium: significant reactants and products, no change in concentrations', 'content'),
    'Q5': ('At equilibrium the forward and reverse rates are equal', 'content'),
    'Q6': ('Reversibility explained by the activation energies of the forward and reverse reactions', 'content'),
    'Q7': ('Temperature changes on equilibrium explained by the enthalpy changes of the two reactions', 'content'),
    'Q8': ('Predict effects on rates of competing reactions: concentration, catalyst, volume, partial pressure, inert substance', 'content'),
    'Q9': ("Le Chatelier's Principle for temperature, concentration and pressure", 'content'),
    'Q10': ("Limitations of Le Chatelier's Principle", 'content'),
    'Q11': ('The law of equilibrium as a consequence of equal rates; equilibrium constant from the coefficients', 'content'),
    'Q12': ('Pure substances (solids, liquids) are not included in K', 'content'),
    'Q13': ('The size of K measures the extent of reaction', 'content'),
    'Q14': ('Calculate concentrations of reactants or products using K', 'content'),
    'Q15': ('The reaction quotient Q gives the direction of change to reach equilibrium', 'content'),
    'B1': ('Acids as proton donors, bases as proton acceptors; monoprotic and polyprotic', 'content'),
    'B2': ('Strength of acids by degree of ionisation; strong and weak acids in water', 'content'),
    'B3': ('Define Ka for a monoprotic acid', 'content'),
    'B4': ('Kw = [H⁺][OH⁻] = 10⁻¹⁴ at 25 °C', 'content'),
    'B5': ('Brønsted-Lowry model: transfer of hydrogen ions, with equations', 'content'),
    'B6': ('pH is logarithmic; use Kw to find [H⁺] from [OH⁻]', 'content'),
    'B7': ('Calculate pH of strong monoprotic acids', 'content'),
    'B8': ('Calculate pH of weak monoprotic acids', 'content'),
    'B9': ('Calculate pH of strong bases', 'content'),
    'A1': ('Context: the importance of enzymes', 'appendix'),
    'A2': ('Context: development of collision theory', 'appendix'),
    'A3': ('Context: chemical balance in wine', 'appendix'),
    'A4': ('Context: carbon dioxide in the atmosphere and hydrosphere', 'appendix'),
}

ELEMENTS = {
    1: ('Explains fundamental principles and theories of thermochemistry, kinetics and equilibrium', 'standards'),
    2: ('Constructs and analyses energy diagrams; enthalpy of reaction from making and breaking bonds', 'standards'),
    3: ('Predicts and explains variation in reaction rates using collision theory, catalysis and the energy distribution', 'standards'),
    4: ('Identifies a system at equilibrium, predicts and explains the effects of changes, states limitations of Le Chatelier', 'standards'),
    5: ('Performs calculations on thermochemistry, reaction rates and equilibrium', 'standards'),
}

EXAM_TOPICS = {
    'X21-6': ('Three incorrect internet statements: pH of concentrated hydrochloric acid below zero, the temperature condition for pH 7.0, why UV light is not a catalyst', 'ex21q6'),
    'X21-7': ('Methanol synthesis: enthalpy and entropy driving forces, pressure and Le Chatelier, distribution curve at a higher temperature, compromise temperature', 'ex21q7'),
    'X21-8': ('Ammonia: energy profile with activation energy, define bond energy, theoretical ΔH from bond energies, Brønsted-Lowry acid, dynamic equilibrium in an open and closed bottle', 'ex21q8'),
    'X21-9': ('Autocatalytic permanganate and oxalate reaction: measurable properties, rate from a graph, role of Mn²⁺, shape of the curve', 'ex21q9'),
    'X21-10': ('Hypochlorous acid: Ka expression and dominant species, why Ka for HCl is not listed, chlorine water equilibrium, effect of low pH', 'ex21q10'),
    'X22-6': ('Equilibrium constant expression for a gas decomposition; direction favouring entropy; whether it is endothermic', 'ex22q6'),
    'X22-7': ('Haber-Bosch: temperature on rate and yield, industrial compromise, concentration-time sketch after adding a reactant', 'ex22q7'),
    'X22-8': ('Butan-1-ol combustion: calorimetry result in kJ per mole, bond-energy calculation, one limitation of each method', 'ex22q8'),
    'X22-9': ('Sulfur trioxide formation: thermochemical equation, energy profile, catalyst, ΔH unchanged, how a catalyst raises the rate', 'ex22q9'),
    'X22-10': ('Calcium carbonate and ethanoic acid: limiting reagent time, rate from a graph, another way to speed it up with collision theory, sketch, pH of a weak acid', 'ex22q10'),
    'X23-6': ('Magnesium and hydrochloric acid gas-volume graph: rate change over time by collision theory; conditions for a second curve', 'ex23q6'),
    'X23-7': ('Ammonia oxidation: energy diagram, bond energy of N-O from ΔH, catalyst on a distribution curve and collision theory', 'ex23q7'),
    'X23-8': ('Dissolving two salts, one endothermic and one exothermic: temperature changes and bond strength explanation', 'ex23q8'),
    'X23-9': ('Carbon dioxide in water: ocean acidity, effect of temperature, stronger acid from Ka values, amphiprotic species', 'ex23q9'),
    'X23-10': ('Nitrogen oxides equilibrium: driving forces, Kc expression, table of effects on Q, K and amount, best conditions', 'ex23q10'),
    'X24-6': ('ATP and ADP: whether breaking a bond releases energy; relative bond strengths from an exothermic reaction', 'ex24q6'),
    'X24-7': ('Propane combustion: bonds broken and formed, energy diagram and its shape, ΔH from bond energies, difference from a literature value', 'ex24q7'),
    'X24-8': ('Calcium carbonate and hydrochloric acid: meaning of gradient, average and instantaneous rates in mol per second, sketch for stronger acid, other ways to change the rate', 'ex24q8'),
    'X24-9': ('Driving forces for a decomposition and a dimerisation; conditions to favour each reaction as written', 'ex24q9'),
    'X24-10': ('Heterogeneous equilibrium: Kc, adding the gas, adding the solid, catalyst, inert gas, temperature', 'ex24q10'),
    'X25-7': ('Linked carbon dioxide equilibria: effect on ocean pH, and on calcium carbonate shells', 'ex25q7'),
    'X25-8': ('Methyl salicylate: energy curve, best conditions for rate, best conditions for equilibrium', 'ex25q8'),
    'X25-9': ('Cobalt chloride colour equilibrium: Kc, rates when unchanged, adding chloride, effect on K, dilution, silver ions', 'ex25q9'),
    'X25-10': ('Wood combustion in a bomb calorimeter: spark and activation energy, calibration factor, heat of combustion per gram, rate from a graph, surface area, sketch', 'ex25q10'),
    'X25-11': ('Water evaporation equilibrium: why liquid is omitted, Kc and temperature, Kc from vapour pressure, mass left after evaporation', 'ex25q11'),
}

# Every number spoken or shown in a worked example, recomputed.
M_CH4 = 12.01 + 4 * 1.008
M_ETOH = 2 * 12.01 + 6 * 1.008 + 16.00
M_GLU = 6 * 12.01 + 12 * 1.008 + 6 * 16.00
M_H2O = 2 * 1.008 + 16.00
M_HCL = 1.008 + 35.45


def v_ml(t, vinf=120.0, tau=25.0):
    return vinf * (1 - math.exp(-t / tau))


def avg_rate_mol():
    return v_ml(40.0) / 1000 / 24.5 / 40.0


def inst_rate_mol():
    return 120.0 / 25.0 * math.exp(-20.0 / 25.0) / 1000 / 24.5


def kc_hi():
    h = (1.00 - 0.780 * 2.00 / 2) / 2.00
    return 0.780 ** 2 / h ** 2


CHECKS = [
    ('CH4 molar mass', lambda: M_CH4, 16.04, 1e-3),
    ('CH4 mol in 5.00 g', lambda: 5.00 / M_CH4, 0.3117, 1e-3),
    ('CH4 heat released', lambda: 5.00 / M_CH4 * 890, 277.4, 1e-3),
    ('ethanol molar mass', lambda: M_ETOH, 46.07, 1e-3),
    ('calorimetry heat J', lambda: 150.0 * 4.184 * 10.4, 6527, 1e-3),
    ('calorimetry heat kJ', lambda: 150.0 * 4.184 * 10.4 / 1000, 6.527, 1e-3),
    ('ethanol mol', lambda: 0.480 / M_ETOH, 0.010419, 1e-3),
    ('ethanol delta H', lambda: -(150.0 * 4.184 * 10.4 / 1000) / (0.480 / M_ETOH), -626.4, 1e-3),
    ('calibration energy', lambda: 12.0 * 3.00 * 150, 5400, 1e-9),
    ('calibration factor', lambda: 12.0 * 3.00 * 150 / 1.50, 3600, 1e-9),
    ('glucose heat kJ', lambda: 3.600 * 6.50, 23.4, 1e-9),
    ('glucose kJ per gram', lambda: 3.600 * 6.50 / 1.50, 15.6, 1e-9),
    ('glucose molar mass', lambda: M_GLU, 180.16, 1e-3),
    ('glucose delta H per mole', lambda: -(3.600 * 6.50 / 1.50) * M_GLU, -2810.4, 1e-3),
    ('ice moles', lambda: 50.0 / M_H2O, 2.7753, 1e-3),
    ('ice melting heat kJ', lambda: 50.0 / M_H2O * 6.01, 16.68, 1e-3),
    ('warming water kJ', lambda: 50.0 * 4.184 * 20.0 / 1000, 4.184, 1e-9),
    ('ice total kJ', lambda: 50.0 / M_H2O * 6.01 + 50.0 * 4.184 * 20.0 / 1000, 20.86, 1e-3),
    ('ethene bonds broken', lambda: 614 + 436, 1050, 1e-9),
    ('ethene bonds formed', lambda: 347 + 2 * 413, 1173, 1e-9),
    ('ethene hydrogenation', lambda: 1050 - 1173, -123, 1e-9),
    ('water O-H', lambda: (2 * 436 + 498 + 484) / 4, 463.5, 1e-9),
    ('hess CO', lambda: -393.5 - (-283.0), -110.5, 1e-9),
    ('V at 40 s', lambda: v_ml(40.0), 95.77, 1e-3),
    ('average rate mL/s', lambda: v_ml(40.0) / 40.0, 2.394, 1e-3),
    ('moles gas at 40 s', lambda: v_ml(40.0) / 1000 / 24.5, 3.909e-3, 1e-3),
    ('average rate mol/s', avg_rate_mol, 9.77e-5, 1e-3),
    ('V at 20 s', lambda: v_ml(20.0), 66.08, 1e-3),
    ('tangent gradient mL/s', lambda: 120.0 / 25.0 * math.exp(-20.0 / 25.0), 2.157, 1e-3),
    ('tangent gradient from points', lambda: (131 - 23) / 50.0, 2.16, 5e-3),
    ('instantaneous rate mol/s', inst_rate_mol, 8.80e-5, 1e-3),
    ('Kc HI', kc_hi, 50.28, 1e-3),
    ('H2 at equilibrium', lambda: (1.00 - 0.780 * 2.00 / 2) / 2.00, 0.110, 1e-9),
    ('HI at equilibrium', lambda: 1.56 / 2.00, 0.780, 1e-9),
    ('K=64 solution x', lambda: 0.800, 0.800, 1e-9),
    ('K=64 check', lambda: (2 * 0.800) ** 2 / (1 - 0.800) ** 2, 64, 1e-9),
    ('Q for HI mixture', lambda: 3.00 ** 2 / (0.50 * 0.50), 36, 1e-9),
    ('weak acid H+', lambda: math.sqrt(1.74e-5 * 0.100), 1.319e-3, 1e-3),
    ('weak acid pH', lambda: -math.log10(math.sqrt(1.74e-5 * 0.100)), 2.88, 2e-3),
    ('weak acid percent ionised', lambda: math.sqrt(1.74e-5 * 0.100) / 0.100 * 100, 1.32, 1e-2),
    ('strong acid pH', lambda: -math.log10(0.0250), 1.602, 1e-3),
    ('conc HCl molarity', lambda: 1000 * 1.18 * 0.360 / M_HCL, 11.65, 1e-3),
    ('conc HCl pH', lambda: -math.log10(1000 * 1.18 * 0.360 / M_HCL), -1.066, 1e-3),
    ('Ba(OH)2 OH', lambda: 2 * 0.0100, 0.0200, 1e-9),
    ('Ba(OH)2 H+', lambda: 1.00e-14 / 0.0200, 5.00e-13, 1e-9),
    ('Ba(OH)2 pH', lambda: -math.log10(1.00e-14 / 0.0200), 12.30, 1e-3),
    ('NaOH pH', lambda: -math.log10(1.00e-14 / 0.0150), 12.176, 1e-3),
    ('vapour Kc', lambda: 4.25 / (8.31 * 303), 1.688e-3, 1e-3),
    ('vapour moles', lambda: 4.25 / (8.31 * 303) * 3.00, 5.064e-3, 1e-3),
    ('vapour mass', lambda: 4.25 / (8.31 * 303) * 3.00 * M_H2O, 0.09123, 2e-3),
    ('liquid left', lambda: 0.100 - 4.25 / (8.31 * 303) * 3.00 * M_H2O, 0.0088, 2e-2),
    ('pure water pH', lambda: -math.log10(math.sqrt(1.00e-14)), 7.0, 1e-9),
]

# --------------------------------------------------------------------------- scenes
S = Step
SCENES = [
Scene('title', P0, 'Welcome', Slide('title', kicker='CRITERION 6', name='Thermochemistry,\nkinetics and\nequilibrium', art=V._title_art, size=56), [
    S("Welcome. This video is a complete briefing on Criterion 6 of TASC Chemistry, C H M four one five, one one five: "
      "identify and apply principles and theories of thermochemistry, kinetics and equilibrium. Use it to revise for your class "
      "tests and for the end of year exam. By the end you should be able to draw and explain energy diagrams, "
      "explain reaction rates with collision theory, predict changes to an equilibrium, and do the calculations.",
      refs=['standards'], anim=4),
]),
Scene('intro', P0, 'How Criterion 6 is assessed', Seq(
    Slide('assess', internal='Your teacher: class tests, practicals\nand investigations during the year',
          external='End-of-year TASC exam:\nSection B is all Criterion 6', section='Section B'),
    Slide('elements', title='The five elements of Criterion 6', items=[
        ('Principles', 'identify, describe and explain principles of thermochemistry, kinetics and equilibrium'),
        ('Energy diagrams', 'construct and analyse diagrams; enthalpy from making and breaking bonds'),
        ('Rates', 'collision theory, catalysis and the distribution of energy'),
        ('Equilibrium', 'identify a system, predict and explain changes, limits of Le Chatelier'),
        ('Calculations', 'thermochemistry, reaction rates and equilibrium')]),
    Slide('standards', title='What the standards ask for', rows=[
        ('E1 Principles', 'identifies', 'describes', 'explains'),
        ('E2 Energy diagrams', 'constructs and identifies key features', 'constructs and uses them to explain bonds', 'constructs and analyses'),
        ('E3 Rates', 'discusses using collision theory and catalysis', 'explains, with energy distribution', 'predicts and explains'),
        ('E4 Equilibrium', 'identifies and predicts effects', 'also explains the effects', 'also states the limitations of Le Chatelier'),
        ('E5 Calculations', 'routine', 'standard', 'complex')]),
    Slide('roadmap', title='Roadmap', parts=[
        ('Part 1', 'Thermochemistry: energy diagrams, calorimetry, bond energies, Hess'), ('Part 2', 'Reaction rates: collision theory, catalysts, graphs'),
        ('Part 3', 'Equilibrium: K, Q, Le Chatelier and industry'), ('Part 4', 'Acids, bases and pH'),
        ('Finish', 'Tests and exam technique, and a one-screen summary')])), [
    S("Criterion 6 is assessed in two ways. Your teacher assesses it during the year, through tests, practical work "
      "and investigations. It is also assessed in Section B of the end of year exam: about forty five minutes, forty five "
      "marks, and between five and seven compulsory questions. You may use the information sheet and an approved calculator.",
      refs=['standards', 'spec']),
    S("There are five elements, numbered in the order of the standards table. Element one is explaining the principles. "
      "Element two is energy diagrams and bonds. Element three is reaction rates. Element four is equilibrium. And element five "
      "is the calculations. A tag in the corner shows which element a slide is practising.", refs=['standards'], elements=[1, 2, 3, 4, 5]),
    S("The standards step up from C to A. At C you identify and discuss. At B you explain, with collision theory and the energy "
      "distribution. At A you predict and explain, analyse energy diagrams, state the limitations of Le Chatelier's principle, "
      "and handle complex calculations. So practise explaining in full sentences, with the key chemical words.",
      refs=['standards'], elements=[1, 2, 3, 4, 5]),
    S("The roadmap. Part one: thermochemistry. Part two: reaction rates. Part three: equilibrium. Part four: acids, bases "
      "and pH. Then technique for tests and the exam. Let's begin.", refs=['content']),
]),

# ------------------------------------------------------------------ Part 1
Scene('energy_basics', P1, 'Enthalpy, bonds and heat', Slide('cards', title='Energy in chemical reactions', chip='Element 1 · principles', cols=2, counts=[1, 2, 3, 4], size=21, cards=[
    ('Enthalpy (heat content)', 'The chemical energy stored in a substance. The enthalpy change ΔH is the heat exchanged with the surroundings at constant pressure, in kJ.', '#a78bfa'),
    ('Breaking bonds', 'Always ABSORBS energy. Bonds do not “release energy when they break”: energy is needed to pull atoms apart.', '#fb923c'),
    ('Forming bonds', 'Always RELEASES energy. The products are lower in energy than the separate atoms.', '#9bde7e'),
    ('Exothermic or endothermic', 'Exothermic: more energy released making bonds than absorbed breaking them. ΔH < 0, surroundings warm. Endothermic: the reverse. ΔH > 0, surroundings cool.', '#f15bb5')]), [
    S("Thermochemistry starts with enthalpy, the heat content of a system. When a reaction happens at constant pressure, the "
      "heat exchanged with the surroundings is the enthalpy change, called delta H, measured in kilojoules. "
      "Every reaction involves breaking some bonds and forming others.", refs=['content'], covers=['T1'], elements=[1]),
    S("Breaking bonds always absorbs energy. A recent exam asked whether breaking the bond in A T P releases energy. "
      "The answer is no. Examiners wanted students to say that breaking bonds absorbs energy, and the reaction is exothermic because "
      "more energy is released forming new bonds.", refs=['content', 'ex24q6', 'ar24q6'], covers=['T2'], elements=[1], exam=['X24-6']),
    S("Forming bonds releases energy. If the bonds formed in the products are stronger overall than the bonds "
      "broken in the reactants, then energy is released: the reaction is exothermic. Note the exam asked about bonds inside molecules, not the "
      "forces between molecules.", refs=['content', 'ar24q6'], covers=['T2', 'T3'], elements=[1], exam=['X24-6']),
    S("An exothermic reaction has a negative delta H, and warms its surroundings. An endothermic reaction has a positive delta H, "
      "and cools them. Dissolving calcium chloride is endothermic, so the water cools. Dissolving potassium hydroxide is "
      "exothermic, so the water warms. Say temperature changes, not just the words endothermic and exothermic, and compare the bond strengths.",
      refs=['content', 'ex23q8', 'ar23q8'], covers=['T3', 'T1', 'T2'], elements=[1], exam=['X23-8', 'X24-6']),
]),
Scene('pe_exo', P1, 'Energy diagrams', V.pe_exo, [
    S("An energy diagram, or potential energy diagram, shows enthalpy against reaction coordinate. Reactants start at one level. "
      "Energy must go up by the activation energy, Ea, to reach the peak, because bonds must break first. Draw it with the species "
      "labelled with states and coefficients, such as methane plus two oxygen.",
      refs=['content', 'ex22q9', 'ex23q7', 'ex24q7', 'ex25q8'], covers=['T4'], elements=[2], exam=['X22-9', 'X23-7', 'X24-7', 'X25-8']),
    S("Then forming bonds releases energy, and the products end lower than the reactants. The vertical distance between "
      "reactants and products is delta H, and it is negative for an exothermic reaction. Draw delta H and Ea as arrows, and label "
      "them. The shape explains itself: the hump is the energy needed to start the reaction, and the drop is the net energy released.",
      refs=['content', 'ex24q7', 'ar24q7'], covers=['T4', 'T2', 'T3'], elements=[2, 1], exam=['X24-7']),
    S("Tip: examiners say sloppy diagrams lose marks. Label the actual reactants and products, not the words reactants and "
      "products, with their states. Give delta H a value or scale, and draw the arrows to the right levels. Do not start the "
      "reactants at zero. And when you are asked to explain the shape, refer to the shape.",
      refs=['ar23q7', 'ar25q8', 'ar24q7'], covers=['T4'], elements=[2], exam=['X23-7', 'X25-8', 'X24-7']),
]),
Scene('pe_endo', P1, 'Endothermic reactions', V.pe_endo, [
    S("For an endothermic reaction the products end higher than the reactants. Delta H is positive. More energy is absorbed breaking the "
      "bonds than is released forming new ones. There is still an activation energy, and it is bigger than the delta H.",
      refs=['content', 'ex25q8'], covers=['T4', 'T3'], elements=[2], exam=['X25-8']),
    S("This links to the dissolving question. The water cools when calcium chloride dissolves, because the system absorbs heat "
      "from it. And bond breaking always absorbs energy.", refs=['ex23q8', 'ar23q8'], covers=['T3', 'T2'], elements=[1, 2], exam=['X23-8']),
    S("A last tip on notation. Write delta H with its units, kilojoules per mole, and a negative sign for exothermic. If a "
      "reaction is written in reverse, the sign of delta H flips. If the equation is doubled, delta H doubles.",
      refs=['content', 'ar22q9'], covers=['T5'], elements=[2], exam=['X22-9']),
]),
Scene('thermo_eq', P1, 'Thermochemical equations and heat from a mass', Slide('worked', title='Worked example 1: heat from a mass of fuel', chip='Element 5 · calculations',
    q='Methane burns: CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l), ΔH = −890 kJ mol⁻¹ (reference data, not from TASC). How much heat is released when 5.00 g of methane burns completely?',
    rows=[dict(s=0, t='Thermochemical equation:  `CH4(g) + 2O2(g) -> CO2(g) + 2H2O(l)`     ΔH = −890 kJ', col='#ffd166'),
          dict(s=0, t='ΔH is the heat per mole of reaction AS WRITTEN: 890 kJ released per mole of CH₄', col='#b3c0d4', size=22),
          dict(s=1, t='M(CH₄) = 12.01 + 4(1.008) = 16.042 g mol⁻¹', col='#eef2f8'),
          dict(s=1, t='n = m / M = 5.00 / 16.042 = 0.31168 mol', col='#eef2f8'),
          dict(s=2, t='Heat released = 0.31168 × 890 = 277.4 kJ', col='#9bde7e'),
          dict(s=2, sf='= 277 kJ (3 s.f.)', t='', gap=0),
          dict(s=2, t='If the equation is written with 2CH₄, ΔH is −1780 kJ: the number of moles matters.', col='#b3c0d4', size=22)]), [
    S("A thermochemical equation is a balanced equation with its delta H, in kilojoules. The delta H is for the "
      "amounts shown. Here, burning one mole of methane releases eight hundred and ninety kilojoules. "
      "Write the heat as part of the equation, or as delta H with the units.",
      refs=['content', 'ex22q9'], covers=['T5'], elements=[2, 5], exam=['X22-9']),
    S("Worked example one. How much heat is released burning five grams of methane? Find the moles first. The molar mass, "
      "from the relative atomic masses on the information sheet, is sixteen point oh four. Five divided by sixteen point oh "
      "four is about zero point three one two moles.", refs=['info', 'info_ar'], covers=['T6'], elements=[5],
      problem='How much heat is released burning 5.00 g of methane if ΔH = −890 kJ mol⁻¹?'),
    S("Multiply by the heat per mole: about two hundred and seventy seven kilojoules released. Always keep to the "
      "ratio in the equation: if the equation was written with two methane, delta H would double.",
      refs=['info'], covers=['T6', 'T5'], elements=[5]),
]),
Scene('calorimetry', P1, 'Calorimetry: E = mcΔT', V.calorimeter, [
    S("Calorimetry measures heat by the temperature change of water. The heat gained by the water is E equals m c delta T, "
      "which is on your information sheet, in the chemical information section. Use the mass of the water, the specific "
      "heat of water, four point one eight four joules per gram per kelvin, and the temperature change.",
      refs=['info', 'info_data', 'content'], covers=['T8', 'T10'], elements=[5]),
    S("Then find the moles of fuel with n equals m over M, and divide: heat per mole. A temperature rise means the "
      "reaction was exothermic, so delta H is negative. Many students forgot the negative sign, and a missing sign cost a mark.",
      refs=['info', 'ex22q8', 'ar22q8'], covers=['T10', 'T6'], elements=[5], exam=['X22-8']),
    S("Convert joules to kilojoules. A temperature change in degrees Celsius is the same size as in kelvin, so never add "
      "two hundred and seventy three to a difference. And use the mass of the water in m c delta T, not the mass of "
      "the fuel or wood.", refs=['ar25q10', 'info'], covers=['T8', 'T10'], elements=[5], exam=['X25-10']),
    S("The result is usually lower than the book value, because heat is lost to the air and the apparatus, and the "
      "fuel may burn incompletely. That is the limitation of calorimetry. Bond energies have a different limitation, "
      "which we meet shortly.", refs=['ar22q8', 'ex22q8'], covers=['T10'], elements=[5, 1], exam=['X22-8']),
]),
Scene('we_calorimetry', P1, 'Worked example: a fuel in a calorimeter', Slide('worked', title='Worked example 2: heat of combustion', chip='Element 5 · calculations',
    q='A spirit burner burns 0.480 g of ethanol (C₂H₅OH). The heat warms 150.0 g of water from 21.0 °C to 31.4 °C. Calculate ΔH of combustion in kJ mol⁻¹.',
    rows=[dict(s=0, t='ΔT = 31.4 − 21.0 = 10.4 K   (a difference: no +273)', col='#eef2f8'),
          dict(s=0, t='E = mcΔT = 150.0 × 4.184 × 10.4 = 6527 J = 6.527 kJ', col='#ffd166'),
          dict(s=1, t='M(C₂H₅OH) = 2(12.01) + 6(1.008) + 16.00 = 46.068 g mol⁻¹', col='#eef2f8'),
          dict(s=1, t='n = 0.480 / 46.068 = 0.010419 mol', col='#eef2f8'),
          dict(s=2, t='ΔH = −E / n = −6.527 / 0.010419 = −626.4 kJ mol⁻¹', col='#9bde7e'),
          dict(s=2, sf='= −626 kJ mol⁻¹ (3 s.f.)', t='', gap=0),
          dict(s=3, t='Illustrative lab result: much smaller in size than the data-book value (about −1370), because of heat losses.', col='#b3c0d4', size=22)]), [
    S("Worked example two. Zero point four eight grams of ethanol heat one hundred and fifty grams of water from twenty one "
      "to thirty one point four degrees. The change is ten point four. E equals one hundred and fifty times four point "
      "one eight four times ten point four, about six thousand five hundred and twenty seven joules.",
      refs=['info', 'info_data'], covers=['T8', 'T10'], elements=[5],
      problem='0.480 g of ethanol heats 150.0 g of water from 21.0 °C to 31.4 °C. What is ΔH of combustion in kJ mol⁻¹?'),
    S("Moles of ethanol: zero point four eight over forty six point oh six eight, about zero point oh one oh four moles. "
      "Heat per mole is six point five two seven kilojoules over that.", refs=['info', 'info_ar'], covers=['T6', 'T10'], elements=[5]),
    S("The answer is about minus six hundred and twenty six kilojoules per mole, with the negative sign for exothermic. "
      "Give the units. This is an illustrative school result. It is well below the accepted size, because heat escapes.",
      refs=['info'], covers=['T10'], elements=[5]),
    S("Tip: this is typical of the question the 2022 exam asked, with a different fuel, and a bond energy "
      "calculation as well. Follow the path: energy, then moles, then delta H, then sign.", refs=['ex22q8', 'ar22q8'], covers=['T10', 'T6'], elements=[5], exam=['X22-8']),
]),
Scene('we_calibration', P1, 'Calibrating a calorimeter', Slide('worked', title='Worked example 3: calibration factor', chip='Element 5 · calculations',
    q='A bomb calorimeter is calibrated with an electric heater: 12.0 V, 3.00 A for 150 s raises the temperature by 1.50 K. Then 1.50 g of glucose is burned and the temperature rises by 6.50 K. Find the calibration factor and the heat of combustion of glucose in kJ g⁻¹ and kJ mol⁻¹.', size=23,
    rows=[dict(s=0, t='Electrical energy  E = VIt = 12.0 × 3.00 × 150 = 5400 J', col='#ffd166'),
          dict(s=0, t='Cf = VIt / ΔT = 5400 / 1.50 = 3600 J K⁻¹', col='#ffd166'),
          dict(s=0, sf='= 3.60 × 10³ J K⁻¹ (3 s.f.)', t='', gap=0),
          dict(s=1, t='Sample:  E = Cf × ΔT = 3.600 × 6.50 = 23.4 kJ', col='#ffd166'),
          dict(s=1, t='Per gram:  23.4 / 1.50 = 15.6 kJ g⁻¹    so  ΔH = −15.6 kJ g⁻¹', col='#9bde7e'),
          dict(s=2, t='M(C₆H₁₂O₆) = 180.16 g mol⁻¹:   ΔH = −15.6 × 180.16 = −2810 kJ mol⁻¹', col='#9bde7e'),
          dict(s=2, sf='= −2.81 × 10³ kJ mol⁻¹ (3 s.f.)', t='', gap=0),
          dict(s=3, t='Do NOT use mcΔT with the sample mass: the calorimeter, not the sample, is heated.', col='#f15bb5', size=22)]), [
    S("Calibration finds how much energy raises the whole calorimeter by one kelvin. Pass a known electrical energy through "
      "it. On your information sheet, E equals V I t, and the calibration factor, C f, equals V I t over delta T, in joules per "
      "kelvin. Here, twelve volts at three amps for a hundred and fifty seconds is five thousand four hundred joules.",
      refs=['info', 'ex25q10', 'ar25q10'], covers=['T7'], elements=[5], exam=['X25-10'],
      problem='A calorimeter is heated electrically with 12.0 V, 3.00 A for 150 s and warms 1.50 K. What is its calibration factor?'),
    S("Divided by the one point five kelvin rise, the calibration factor is three thousand six hundred joules per kelvin. "
      "Now burn the sample. The energy is C f times delta T, three point six kilojoules per kelvin times six point five, which "
      "is twenty three point four kilojoules. For one point five grams, that is fifteen point six kilojoules per gram.",
      refs=['info', 'ar25q10'], covers=['T7', 'T10', 'T6'], elements=[5], exam=['X25-10'],
      problem='Using Cf = 3.60 kJ K⁻¹, 1.50 g of glucose raises the temperature by 6.50 K. What is ΔH in kJ g⁻¹ and kJ mol⁻¹?'),
    S("Multiply by the molar mass to get kilojoules per mole, about minus two thousand eight hundred and ten. Note that the answer "
      "can be left in kilojoules per gram, if the question asks for it. A notable number of students instead looked for "
      "a mole value of the wood, and used the wrong molar mass.", refs=['ar25q10', 'info_ar'], covers=['T6', 'T10'], elements=[5], exam=['X25-10']),
    S("Do not use m c delta T with the mass of the sample and the specific heat of water: that is a common error. And "
      "a temperature change in Celsius and in kelvin is the same number.", refs=['ar25q10'], covers=['T7', 'T8'], elements=[5], exam=['X25-10']),
]),
Scene('we_state', P1, 'Changes of state', Slide('worked', title='Worked example 4: melting and warming', chip='Element 5 · calculations',
    q='How much heat is needed to melt 50.0 g of ice at 0 °C and then warm the water to 20.0 °C? (ΔH of fusion of ice = 6.01 kJ mol⁻¹: reference data, not from TASC.)',
    rows=[dict(s=0, t='Melting: n = 50.0 / 18.016 = 2.7753 mol', col='#eef2f8'),
          dict(s=0, t='Heat = n × ΔH(fusion) = 2.7753 × 6.01 = 16.68 kJ   (no temperature change)', col='#ffd166'),
          dict(s=1, t='Warming the liquid:  E = mcΔT = 50.0 × 4.184 × 20.0 = 4184 J = 4.184 kJ', col='#ffd166'),
          dict(s=2, t='Total = 16.68 + 4.184 = 20.86 kJ', col='#9bde7e'),
          dict(s=2, sf='= 20.9 kJ (3 s.f.)', t='', gap=0),
          dict(s=2, t='Melting needs far more heat than warming: bonds between particles are overcome, not temperature raised.', col='#b3c0d4', size=22)]), [
    S("Heat for a change of state is different. While ice melts, the temperature stays at zero. The heat goes into overcoming "
      "the forces between particles. For this you need the molar enthalpy of fusion, which will be given in a question, because "
      "it is not on the information sheet. Heat equals moles times that value.",
      refs=['content', 'info'], covers=['T9', 'T6'], elements=[5],
      problem='How much heat is needed to melt 50.0 g of ice and warm the water to 20.0 °C, if ΔH(fusion) = 6.01 kJ mol⁻¹?'),
    S("Fifty grams of ice is two point seven seven five moles, so melting needs about sixteen point seven kilojoules. Then, "
      "warming the liquid water uses m c delta T, about four point one eight kilojoules.", refs=['info', 'info_data'], covers=['T9', 'T8'], elements=[5]),
    S("The total is about twenty point nine kilojoules. Do each stage separately, in order, because the temperature "
      "formula only applies when the temperature is changing.", refs=['info'], covers=['T9', 'T8'], elements=[5]),
]),
Scene('bonds', P1, 'Bond energies', Slide('worked', title='Worked example 5: ΔH from bond energies', chip='Element 5 · calculations',
    q='Use these average bond energies (kJ mol⁻¹), given in the question: C=C 614, H–H 436, C–C 347, C–H 413. Find ΔH for ethene + hydrogen → ethane. Then: for 2H₂ + O₂ → 2H₂O(g), ΔH = −484 kJ. Using H–H 436 and O=O 498, find the O–H bond energy.',
    size=24,
    rows=[dict(s=0, t='Bond energy: the energy needed to break one mole of a particular bond (gas phase).', col='#b3c0d4', size=22),
          dict(s=1, t='Broken: C=C + H–H = 614 + 436 = 1050 kJ        Formed: C–C + 2(C–H) = 347 + 826 = 1173 kJ', col='#eef2f8', size=23),
          dict(s=1, t='ΔH = broken − formed = 1050 − 1173 = −123 kJ mol⁻¹   (exothermic)', col='#9bde7e'),
          dict(s=2, t='Broken: 2(436) + 498 = 1370 kJ.   Formed: 4 × (O–H) = 4x', col='#eef2f8', size=23),
          dict(s=2, t='−484 = 1370 − 4x   so   x = 1854 / 4 = 463.5 kJ mol⁻¹', col='#9bde7e'),
          dict(s=2, sf='= 464 kJ mol⁻¹ (3 s.f.)', t='', gap=0),
          dict(s=3, t='Count every bond (C=O in CO₂ twice per molecule!). Bond energies are AVERAGES, so the result is approximate.', col='#f15bb5', size=22)]), [
    S("Bond energy is the energy needed to break one mole of a particular bond, in the gas phase. You are given a table, because bond "
      "energies are not on the information sheet. The method: add the energy to break all bonds in the reactants, "
      "then subtract the energy released forming all bonds in the products.",
      refs=['content', 'ex21q8', 'ex22q8', 'ex24q7'], covers=['T11', 'T12'], elements=[2, 5], exam=['X21-8', 'X22-8', 'X24-7']),
    S("Example. Ethene plus hydrogen makes ethane. Broken: a carbon carbon double bond and a hydrogen hydrogen bond, "
      "one thousand and fifty kilojoules. Formed: a carbon carbon single bond and two carbon hydrogen bonds, "
      "one thousand one hundred and seventy three. Delta H is broken minus formed: minus one hundred and twenty three kilojoules per mole.",
      refs=['info'], covers=['T12'], elements=[2, 5], problem='Use bond energies to find ΔH for C₂H₄ + H₂ → C₂H₆ (C=C 614, H–H 436, C–C 347, C–H 413 kJ mol⁻¹).'),
    S("Now work backwards, as a 2023 question did. The reaction is two hydrogen plus oxygen making steam, minus four hundred "
      "and eighty four. Bonds broken total one thousand three hundred and seventy. Four oxygen hydrogen bonds form, so "
      "minus four eighty four equals one thousand three seventy minus four x. The oxygen hydrogen bond energy is about four hundred and sixty four.",
      refs=['ex23q7', 'ar23q7'], covers=['T12', 'T11'], elements=[2, 5], exam=['X23-7'],
      problem='2H₂ + O₂ → 2H₂O(g) has ΔH = −484 kJ. Using H–H 436 and O=O 498 kJ mol⁻¹, what is the O–H bond energy?'),
    S("Common errors were forgetting bonds, such as the two carbon carbon bonds in propane, using the wrong bond types, and "
      "sign errors. Count every bond in each molecule. Bond energies are averages, and a calculation for steam differs from "
      "a book value for liquid water, because condensing steam releases more energy. Name that reason.",
      refs=['ar22q8', 'ar24q7', 'ex24q7', 'ex21q8', 'ar21q8'], covers=['T12'], elements=[2, 5, 1], exam=['X22-8', 'X24-7', 'X21-8']),
]),
Scene('hess', P1, "Hess's Law", Slide('worked', title="Worked example 6: Hess's Law", chip='Element 5 · calculations',
    q='Given (reference data, not from TASC): (1) C(s) + O₂(g) → CO₂(g), ΔH₁ = −393.5 kJ; (2) CO(g) + ½O₂(g) → CO₂(g), ΔH₂ = −283.0 kJ. Find ΔH for C(s) + ½O₂(g) → CO(g).',
    rows=[dict(s=0, t="Hess's Law: ΔH for a reaction is the same whichever route it takes, so sum the steps.", col='#b3c0d4', size=22),
          dict(s=1, t='Target has C and CO on different sides:  keep (1),  REVERSE (2)', col='#eef2f8'),
          dict(s=1, t='`C(s) + O2(g) -> CO2(g)`                       ΔH = −393.5', col='#ffd166'),
          dict(s=1, t='`CO2(g) -> CO(g) + 1/2 O2(g)`            ΔH = +283.0   (sign flips)', col='#ffd166'),
          dict(s=2, t='Add:  `C(s) + 1/2 O2(g) -> CO(g)`', col='#eef2f8'),
          dict(s=2, t='ΔH = −393.5 + 283.0 = −110.5 kJ', col='#9bde7e'),
          dict(s=3, t='Reverse a reaction: flip the sign. Multiply an equation: multiply ΔH. Cancel what appears on both sides.', col='#b3c0d4', size=22)]), [
    S("Hess's law says the enthalpy change for a reaction is the same whichever route it takes, so you can add thermochemical "
      "equations to get one you cannot measure directly. A catalyst does not change delta H for this reason: it changes the "
      "route, not the start and finish.", refs=['content', 'ex22q9', 'ar22q9'], covers=['T13'], elements=[2, 5], exam=['X22-9']),
    S("Worked example six. We want carbon and half an oxygen making carbon monoxide. Keep the first equation. Reverse the "
      "second, so carbon dioxide gives carbon monoxide, and the sign flips to plus two hundred and eighty three.",
      refs=['content'], covers=['T13'], elements=[5], problem="Use Hess's Law: C + O₂ → CO₂ (−393.5 kJ) and CO + ½O₂ → CO₂ (−283.0 kJ). Find ΔH for C + ½O₂ → CO."),
    S("Add them, and cancel the carbon dioxide on both sides. Delta H is minus three ninety three point five plus two "
      "eighty three, minus one hundred and ten point five kilojoules. The rules: reverse means flip the sign, multiply means "
      "multiply delta H, and cancel species that appear on both sides.", refs=['content'], covers=['T13', 'T5'], elements=[5]),
]),

# ------------------------------------------------------------------ Part 2
Scene('rate_def', P2, 'What is a reaction rate?', V.rate_graph, [
    S("Reaction rate is how fast a reactant is used up or a product is made. The average rate is the change in amount, delta n, "
      "of a product divided by time, or the change in concentration, delta c, divided by time. From a gas volume, "
      "convert to moles first, using the molar volume on the information sheet.",
      refs=['content', 'info_data', 'ex24q8', 'ar24q8'], covers=['K1', 'K2', 'K3'], elements=[3, 5], exam=['X24-8'], anim=None),
    S("The rate at one moment, the instantaneous rate, is the gradient of a tangent to the curve. Draw the tangent, and use "
      "two points on the tangent, not on the curve. Many students did not draw a tangent, and others used the concentration "
      "of the acid to find moles of gas.", refs=['ar24q8', 'ar21q9', 'ex21q9'], covers=['K1'], elements=[3, 5], exam=['X24-8', 'X21-9']),
    S("When the graph goes flat, a reactant has been used up. That is the limiting reagent, and the instantaneous rate is "
      "zero. It does not mean equilibrium. A report said many students believed the reaction had reached equilibrium, and "
      "some thought the magnesium was in solution.", refs=['ar23q6', 'ar24q8', 'ex22q10', 'ar22q10'], covers=['K1', 'Q1'], elements=[3, 4], exam=['X23-6', 'X24-8', 'X22-10']),
]),
Scene('we_rate', P2, 'Worked example: average and instantaneous rates', Slide('worked', title='Worked example 7: rates from a graph', chip='Element 5 · calculations',
    q='In an investigation, 95.8 mL of gas is collected in the first 40 s, and the tangent at 20 s passes through (0 s, 23 mL) and (50 s, 131 mL). Use Vm = 24.5 L mol⁻¹ (SLC). Find the average rate for the first 40 s and the instantaneous rate at 20 s, in mol s⁻¹.',
    rows=[dict(s=0, t='n(gas) = V / Vm = 0.0958 L / 24.5 L mol⁻¹ = 3.909 × 10⁻³ mol', col='#eef2f8'),
          dict(s=0, t='Average rate = Δn / t = 3.909 × 10⁻³ / 40 = 9.77 × 10⁻⁵ mol s⁻¹', col='#9bde7e'),
          dict(s=0, sf='= 9.77 × 10⁻⁵ mol s⁻¹ (3 s.f.)', t='', gap=0),
          dict(s=1, t='Tangent gradient = (131 − 23) / (50 − 0) = 2.16 mL s⁻¹ = 2.16 × 10⁻³ L s⁻¹', col='#eef2f8'),
          dict(s=1, t='Rate = 2.16 × 10⁻³ / 24.5 = 8.8 × 10⁻⁵ mol s⁻¹   (rate of gas formation at 20 s)', col='#9bde7e'),
          dict(s=2, t='Two different quantities: an average over an INTERVAL, and a rate at ONE MOMENT (a gradient).', col='#b3c0d4', size=22)]), [
    S("Worked example seven. A student collects ninety five point eight millilitres of gas in forty seconds. Convert to litres, "
      "then divide by the molar volume, twenty four point five litres per mole at standard laboratory conditions. That is "
      "three point nine times ten to the minus three moles. Divided by forty seconds, the average rate is nine point seven seven times ten "
      "to the minus five moles per second.", refs=['info_data', 'info', 'ex24q8'], covers=['K2', 'K1'], elements=[5, 3], exam=['X24-8'],
      problem='95.8 mL of gas (Vm = 24.5 L mol⁻¹) is collected in the first 40 s. What is the average rate in mol s⁻¹?'),
    S("For the instantaneous rate at twenty seconds, draw a tangent. It passes through zero, twenty three, and fifty, one "
      "thirty one millilitres. The gradient is two point one six millilitres per second. Convert to moles per second: about eight point eight "
      "times ten to the minus five.", refs=['ar24q8', 'info_data'], covers=['K1', 'K2'], elements=[5, 3], exam=['X24-8'],
      problem='A tangent at 20 s passes through (0 s, 23 mL) and (50 s, 131 mL), Vm = 24.5 L mol⁻¹. What is the instantaneous rate in mol s⁻¹?'),
    S("Notice that the two rates are different. The instantaneous rate is the gradient at one moment, and the average "
      "is over an interval. The curve is steepest at the start, so the rate falls as reactants are used up. "
      "That fall is explained by collision theory: fewer reactant particles mean fewer collisions.",
      refs=['ar23q6', 'ar24q8'], covers=['K4', 'K1'], elements=[3], exam=['X23-6', 'X24-8']),
]),
Scene('collision', P2, 'Collision theory', Slide('cards', title='Collision theory: what changes the rate', chip='Element 3 · rates and catalysis', cols=1, counts=[1, 2, 3, 4, 5], h=0.125, size=20, bump=0, cards=[
    ('Concentration or pressure', 'More particles per volume: more frequent collisions, so more effective collisions per second.', '#fb923c'),
    ('Surface area', 'Smaller pieces expose more particles to the other reactant: more collisions per second.', '#a78bfa'),
    ('Temperature', 'Faster particles: more frequent AND higher-energy collisions, so a larger proportion exceed Ea.', '#f15bb5'),
    ('Nature of reactants', 'More bonds to break means a higher Ea and a slower reaction. Ions combining (precipitation) are fast; complex reactions are slow.', '#9bde7e'),
    ('Catalyst', 'Lowers Ea by a different pathway: the same collisions, but a bigger share are effective.', '#38bdf8')]), [
    S("Collision theory says particles react only when they collide with enough energy, at least the activation energy, "
      "and with a suitable orientation. Such collisions are called effective or successful collisions. The rate depends on how "
      "many effective collisions happen per second. Never say rate depends on the number of collisions alone.",
      refs=['content', 'ar25q10', 'ar23q7'], covers=['K4', 'A2'], elements=[3, 1], exam=['X25-10']),
    S("Concentration. For gases, use pressure. More particles in the same volume means more frequent collisions, and so "
      "more effective collisions per second. A concentration change is not accepted as another method, if the question "
      "already changed concentration.", refs=['content', 'ar24q8', 'ex23q6'], covers=['K4'], elements=[3], exam=['X24-8', 'X23-6']),
    S("Surface area. Crushing a solid exposes more particles, so more collisions per second. That is why powdered "
      "calcium carbonate reacts faster than a lump, and why smaller pieces of wood burn faster. Say surface area increases, "
      "more frequent collisions, and so a faster rate.", refs=['ar22q10', 'ar25q10', 'ex25q10'], covers=['K5'], elements=[3], exam=['X22-10', 'X25-10']),
    S("Temperature. Particles move faster, so collisions are both more frequent and more energetic, and a larger proportion "
      "reach the activation energy. Nature of the reactants also matters: reactions that need more bonds broken are slower, "
      "while ions that simply combine to form a precipitate are very fast.",
      refs=['content', 'ar22q7', 'ar21q7'], covers=['K6', 'K7'], elements=[3], exam=['X22-7', 'X21-7']),
    S("Pressure and the container volume only matter for gases. A report gave no marks to students who answered a question about "
      "calcium carbonate and acid with pressure or temperature when the question asked for another reactant condition. "
      "Read the question, then choose a method it allows.", refs=['ar22q10', 'ex22q10'], covers=['K4', 'K5'], elements=[3], exam=['X22-10']),
]),
Scene('distribution', P2, 'The energy distribution', V.distribution, [
    S("Molecules in a sample have a range of kinetic energies. Draw the distribution with the number of molecules against "
      "kinetic energy. It starts at zero, rises to a peak, and has a long tail to the right. Mark the activation energy. Only the "
      "shaded molecules, with at least Ea, can react.", refs=['content', 'ex21q7', 'ex23q7', 'ar21q7'], covers=['K9', 'K10'], elements=[3], exam=['X21-7', 'X23-7']),
    S("When the temperature rises, the peak moves right and lowers, but the area under the curve stays the same, because "
      "there are the same number of molecules. The curve is not a semicircle, and it is skewed to the right. A much larger share "
      "of molecules is now above Ea, so a small rise in temperature gives a large rise in rate.",
      refs=['ar21q7', 'content'], covers=['K9', 'K10', 'K6'], elements=[3], exam=['X21-7']),
    S("A catalyst leaves the curve alone and lowers the activation energy. Draw the new Ea line to the left, and shade the "
      "greater area. Almost half the students in one year drew a higher temperature curve instead. And say that the "
      "frequency of collisions is unchanged, but the frequency of effective collisions rises.",
      refs=['ar23q7', 'ex23q7', 'content'], covers=['K8', 'K9', 'K10'], elements=[3], exam=['X23-7']),
    S("The abbreviation M B D is not accepted, so write out the full name. This diagram also explains why a spark starts a fire. "
      "At normal temperature few molecules have enough energy. The spark gives a few molecules enough, the exothermic "
      "reaction releases energy, so more molecules exceed Ea, and the reaction accelerates.", refs=['ar23q7', 'ex25q10', 'ar25q10'], covers=['K10', 'K6'], elements=[3, 1], exam=['X25-10']),
]),
Scene('catalyst', P2, 'Catalysts and enzymes', V.pe_cat, [
    S("A catalyst increases the rate of a reaction without being consumed. It provides an alternative pathway, or mechanism, "
      "with a lower activation energy. On an energy diagram, draw a second dashed hump below the first, with the same "
      "reactants and products.", refs=['content', 'ex22q9', 'ar22q9'], covers=['K8', 'K11'], elements=[3, 2], exam=['X22-9']),
    S("The start and finish levels are the same, so delta H does not change. A strong answer used Hess's law: the energy "
      "released depends on the enthalpy of reactants and products, not on the pathway.", refs=['ar22q9', 'ex22q9'], covers=['K11', 'T13'], elements=[3, 2], exam=['X22-9']),
    S("A catalyst lowers the activation energy for both the forward and the reverse reaction, so it speeds up both. "
      "It makes equilibrium reached sooner, but it does not change the position of equilibrium or the value of K.",
      refs=['ar24q10', 'ex24q10'], covers=['K8', 'Q8'], elements=[3, 4], exam=['X24-10']),
    S("A statement that UV light acts as a catalyst for hydrogen peroxide decomposition is wrong. A catalyst is not "
      "consumed and is a substance that provides a lower energy pathway. Light supplies energy. Also, do not say a catalyst "
      "provides a surface: that is only true for heterogeneous catalysts.", refs=['ex21q6', 'ar21q6'], covers=['K8'], elements=[3, 1], exam=['X21-6']),
]),
Scene('autocatalysis', P2, 'Enzymes and autocatalysis', Slide('cards', title='Catalysts in action', chip='Context · enzymes', cols=1, counts=[1, 2, 3], h=0.20, size=20, bump=0, cards=[
    ('Enzymes', 'Biological catalysts: protein molecules that lower the activation energy of one particular reaction, in digestion and respiration. Pasteur’s work on fermentation was the start; the molecular structure explains their action.', '#9bde7e'),
    ('Autocatalysis', 'A product that is also a catalyst. Rate: slow at first (little catalyst), then fast (catalyst builds up), then slow again as reactants run out. A graph of reactant against time is an S shape.', '#38bdf8'),
    ('Collision theory’s history', 'Trautz (1916) and Lewis (1918) developed collision theory independently. Chemical engineers use it to design safe, efficient processes.', '#a78bfa')]), [
    S("Enzymes are biological catalysts. They are protein molecules, specific to one reaction, and they lower the activation "
      "energy. They are important in digestion and respiration, and the course names them as a context. Their structure explains "
      "how they work, which is why the molecular geometry of enzymes earned a Nobel Prize.", refs=['content', 'appendix'], covers=['K12', 'A1'], elements=[1]),
    S("Autocatalysis is a reaction where a product acts as a catalyst, as manganese two plus did in a permanganate and oxalate "
      "reaction in a past exam. The rate is slow at first, because there is little catalyst, then fast as the catalyst builds, "
      "then slow again as reactants are used. Explain each section, not just the shape.",
      refs=['ex21q9', 'ar21q9'], covers=['K8', 'K1'], elements=[3, 1], exam=['X21-9']),
    S("The first measurable property in that question could be a colour change, a gas volume, or the mass of the flask. "
      "Name the property, not just the substance. Finally, collision theory itself was developed by Max Trautz in "
      "nineteen sixteen and William Lewis in nineteen eighteen, working apart, and engineers still use it today.",
      refs=['ar21q9', 'appendix'], covers=['A2', 'K1'], elements=[1, 3], exam=['X21-9']),
]),
Scene('rate_sketch', P2, 'Sketching a changed reaction rate', V.rate_sketch, [
    S("Sketching questions ask what a graph looks like after a change. A faster reaction with the same amount of limiting "
      "reagent has a steeper start and reaches the same final volume. Stronger acid, smaller pieces, or higher temperature "
      "all do that. Explain both differences: steeper, and earlier plateau.", refs=['ex24q8', 'ar24q8', 'ex22q10', 'ar22q10'], covers=['K4', 'K5', 'K6'], elements=[3], exam=['X24-8', 'X22-10']),
    S("If there is half the limiting reagent, the starting gradient is the same, but the plateau is at half the volume. "
      "A report described that Reaction two in a magnesium question made half as much hydrogen, so it used a smaller mass, and was slower, "
      "so the acid was probably more dilute.", refs=['ar23q6', 'ex23q6'], covers=['K1', 'K4'], elements=[3], exam=['X23-6']),
    S("Both changes together. Smaller pieces and half the amount: a steeper start, and a plateau at half. Draw on the graph "
      "you are given, from the same origin. Students who redrew their own graph made it impossible to see if the initial rate was faster.",
      refs=['ar25q10', 'ex25q10'], covers=['K5', 'K1'], elements=[3], exam=['X25-10']),
]),

# ------------------------------------------------------------------ Part 3
Scene('reversible', P3, 'Reversible reactions and dynamic equilibrium', V.eq_dynamic, [
    S("A system can be open, exchanging matter and energy with its surroundings, or closed, exchanging only energy. Physical "
      "changes are all reversible, but only some chemical reactions are. Many do not go to completion: the products can "
      "convert back to reactants.", refs=['content'], covers=['Q1', 'Q2'], elements=[1, 4]),
    S("In a closed system, a reversible reaction reaches dynamic equilibrium. You recognise it by significant amounts of "
      "reactants and products, with no change in their concentrations over time. Both reactions are still happening, and the forward and reverse "
      "rates are equal, not zero. Many students said the forward reaction was faster in a solution that had reached equilibrium.",
      refs=['content', 'ex25q9', 'ar25q9'], covers=['Q4', 'Q5'], elements=[4, 1], exam=['X25-9']),
    S("Example: ammonia in a sealed bottle of water is at dynamic equilibrium. With the lid on, the forward and reverse rates are equal. "
      "Remove the lid and it is an open system, ammonia escapes, so the reaction shifts to make more ammonia. That is the smell. "
      "Many students forgot to describe the lid-on case.", refs=['ex21q8', 'ar21q8'], covers=['Q1', 'Q5', 'Q4'], elements=[4], exam=['X21-8']),
]),
Scene('drivers', P3, 'Why there is an equilibrium', Slide('table', title='The two driving forces', chip='Element 4 · equilibrium',
    head=['Driving force', 'Favours', 'In practice'], widths=[0.25, 0.30, 0.37], size=22, counts=[1, 2, 3, 4], rows=[
        ['Minimum enthalpy', 'Exothermic direction (ΔH < 0)', 'Energy is released, the surroundings gain energy'],
        ['Maximum entropy', 'More disorder: more moles of gas, solids to gases, dissolving', '3 mol gas → 2 mol gas: entropy falls'],
        ['They agree', 'Reaction goes to completion in that direction', 'e.g. exothermic AND more gas moles'],
        ['They oppose', 'EQUILIBRIUM: a compromise', 'e.g. exothermic but fewer gas moles']]), [
    S("Why do reactions reach an equilibrium? There are two natural driving forces. One is a tendency to minimise "
      "enthalpy, so exothermic reactions are favoured. The other is a tendency to maximise entropy, which means more randomness, "
      "such as more moles of gas. An equilibrium is a compromise between them.",
      refs=['content', 'ex21q7', 'ex23q10', 'ar23q10'], covers=['Q3'], elements=[1, 4], exam=['X21-7', 'X23-10']),
    S("Entropy is easy to spot. A solid becoming a gas, or a reaction producing more moles of gas, increases entropy. In the "
      "decomposition of N O C l into N O and chlorine, there are three moles of gas on the right and two on the left, so the "
      "forward reaction favours maximum entropy. Name the mole ratio.",
      refs=['ex22q6', 'ar22q6'], covers=['Q3'], elements=[4, 1], exam=['X22-6']),
    S("Then deduce the enthalpy. If the forward reaction favours maximum entropy, the reverse must favour minimum "
      "enthalpy, so the reverse is exothermic and the forward reaction is endothermic. Just writing endothermic earned no marks, "
      "and an explanation using bond breaking earned none either.", refs=['ar22q6', 'ex22q6', 'ar23q10'], covers=['Q3', 'Q7'], elements=[4, 1], exam=['X22-6', 'X23-10']),
    S("If both forces favour the same direction, the reaction goes essentially to completion that way, so do not explain it as an equilibrium. "
      "In a question about a one way reaction, a report said many students overcomplicated it. For the conditions, "
      "high temperature or low pressure favours the entropy driven reaction, and low temperature or high pressure favours the other.",
      refs=['ex24q9', 'ar24q9'], covers=['Q3', 'Q9'], elements=[4], exam=['X24-9']),
]),
Scene('kc', P3, 'The equilibrium constant', Slide('eqs', title='The equilibrium constant, K', chip='Element 5 · calculations', counts=[1, 2, 3], gap=0.22, size=30, nx=0.58, y=0.72, section='Chemical Equilibrium Formulae', items=[
    ('sheet', '$K_c = \\dfrac{[R]^z[S]^w}{[P]^x[Q]^y}$', 'for xP + yQ ⇌ zR + wS: concentrations in mol L⁻¹, raised to the coefficients'),
    ('eq', '$CaCO_3(s) \\rightleftharpoons CaO(s) + CO_2(g)$     $K_c = [CO_2]$', 'Solids and pure liquids are left out: their concentration is constant'),
    ('eq', 'K large → mostly products', 'K small → mostly reactants. K changes only with TEMPERATURE')]), [
    S("The equilibrium constant, K c, is written from the coefficients. Your information sheet gives it, in the chemical "
      "equilibrium formulae section: products' concentrations raised to their coefficients, over the reactants' concentrations "
      "raised to theirs. Start with K c equals, use square brackets, and do not turn the fraction upside down.",
      refs=['info_eq', 'content', 'ex22q6', 'ar22q6', 'ex25q9', 'ar25q9'], covers=['Q11'], elements=[4, 5], exam=['X22-6', 'X25-9']),
    S("The sheet says the expression is for when no component is a solid. Pure solids and pure liquids are not "
      "included, because their concentrations are constant. For calcium carbonate breaking down, K c is just the concentration of carbon "
      "dioxide. A common mistake was including the solids. For water evaporating, liquid water is left out, and say why: it is "
      "effectively constant.", refs=['info_eq', 'ex24q10', 'ar24q10', 'ex25q11', 'ar25q11'], covers=['Q12', 'Q11'], elements=[4, 5], exam=['X24-10', 'X25-11']),
    S("The size of K shows how far the reaction goes: a large K, mostly products, and a small K, mostly reactants. K changes "
      "only with temperature. Adding more hydrochloric acid to a cobalt chloride equilibrium does not change K, which "
      "many students got wrong.", refs=['content', 'ar25q9', 'ex25q9'], covers=['Q13', 'Q11'], elements=[4], exam=['X25-9']),
]),
Scene('we_kc', P3, 'Worked example: equilibrium calculations', Slide('worked', title='Worked example 8: K and concentrations', chip='Element 5 · calculations',
    q='(a) 1.00 mol each of H₂ and I₂ are sealed in a 2.00 L vessel. At equilibrium there is 1.56 mol of HI: H₂ + I₂ ⇌ 2HI. Find Kc. (b) At the same temperature, with [H₂] = [I₂] = 1.00 mol L⁻¹ initially and Kc = 64, find the equilibrium concentrations.',
    size=24,
    rows=[dict(s=0, t='[HI] = 1.56 / 2.00 = 0.780;   HI formed from 0.78 mol of each, so each H₂ and I₂ lost 0.78 mol', col='#eef2f8', size=23),
          dict(s=0, t='[H₂] = [I₂] = (1.00 − 0.78) / 2.00 = 0.110 mol L⁻¹', col='#eef2f8'),
          dict(s=1, t='Kc = [HI]² / ([H₂][I₂]) = 0.780² / (0.110 × 0.110) = 50.3', col='#9bde7e'),
          dict(s=1, sf='Kc = 50.3 (3 s.f.; no units, as the concentrations cancel)', t='', gap=0),
          dict(s=2, t='(b) Let x mol L⁻¹ of each react:  [H₂] = [I₂] = 1 − x,   [HI] = 2x', col='#eef2f8'),
          dict(s=2, t='64 = (2x)² / (1 − x)²   so   8 = 2x / (1 − x)   (take the square root)', col='#ffd166'),
          dict(s=3, t='8 − 8x = 2x   so   x = 0.800', col='#ffd166'),
          dict(s=3, t='[H₂] = [I₂] = 0.200 mol L⁻¹,   [HI] = 1.60 mol L⁻¹', col='#9bde7e'),
          dict(s=3, t='Check: 1.60² / 0.200² = 64 ✓', col='#b3c0d4', size=22)]), [
    S("Worked example eight. One mole each of hydrogen and iodine in two litres make one point five six moles of hydrogen "
      "iodide. First convert to concentrations. Hydrogen iodide is zero point seven eight zero. Making that used up zero point "
      "seven eight moles of each reactant, so each is zero point one one zero moles per litre at equilibrium.",
      refs=['info_eq', 'info', 'content'], covers=['Q14', 'Q11'], elements=[5],
      problem='1.00 mol H₂ and 1.00 mol I₂ in 2.00 L form 1.56 mol HI at equilibrium (H₂ + I₂ ⇌ 2HI). What is Kc?'),
    S("K c is zero point seven eight squared over zero point one one squared, about fifty point three. In this reaction the units "
      "cancel. Check units in your own question. Then use a table: initial, change, equilibrium.", refs=['info_eq'], covers=['Q14', 'Q13'], elements=[5]),
    S("Now go the other way. If K is sixty four and we start with one mole per litre of each reactant, let x react. "
      "Hydrogen iodide is two x. Then sixty four equals two x squared over one minus x squared. Both sides are perfect squares, "
      "so take the root: eight equals two x over one minus x.",
      refs=['content'], covers=['Q14'], elements=[5],
      problem='H₂ + I₂ ⇌ 2HI, Kc = 64. Starting from 1.00 mol L⁻¹ each of H₂ and I₂ (no HI), what are the equilibrium concentrations?'),
    S("Solve for x: zero point eight. So hydrogen and iodine are zero point two each, and hydrogen iodide is one point six. "
      "Check by substituting back. Sixty four. Concentrations can be asked for in the whole question or as a part, so always "
      "set the working out in a table.", refs=['content', 'info_eq'], covers=['Q14'], elements=[5]),
]),
Scene('quotient', P3, 'The reaction quotient, Q', Slide('table', title='Q compared with K: which way does it go?', chip='Element 4 · equilibrium',
    head=['Comparison', 'Meaning', 'Direction'], widths=[0.20, 0.42, 0.30], size=23, counts=[1, 2, 3, 4], rows=[
        ['Q < K', 'Too many reactants, not enough products', 'FORWARD, to make products'],
        ['Q = K', 'At equilibrium', 'No net change'],
        ['Q > K', 'Too many products', 'REVERSE, to make reactants'],
        ['Example: H₂ 0.50, I₂ 0.50, HI 3.00 mol L⁻¹, K = 64', 'Q = 3.00² / (0.50 × 0.50) = 36', 'Q < K: moves forward']]), [
    S("The reaction quotient, Q, has the same expression as K but uses the concentrations at any moment. Compare Q with K. If "
      "Q is less than K, there is too little product, so the reaction goes forward. If Q is greater than K, it goes in reverse.",
      refs=['content'], covers=['Q15'], elements=[4, 5]),
    S("At equilibrium, Q equals K, and nothing changes overall. Q is useful when a change is made to a system. When "
      "something is added or removed, Q changes first, K does not, and the system moves until Q equals K again.",
      refs=['content', 'ex23q10', 'ar23q10'], covers=['Q15', 'Q9'], elements=[4], exam=['X23-10']),
    S("Example: with hydrogen and iodine at zero point five and hydrogen iodide at three, Q is thirty six, less than "
      "sixty four, so more hydrogen iodide forms. Temperature is the exception: it changes K itself.",
      refs=['info_eq'], covers=['Q15', 'Q14'], elements=[4, 5], problem='H₂ + I₂ ⇌ 2HI, K = 64. A mixture has [H₂] = 0.50, [I₂] = 0.50 and [HI] = 3.00 mol L⁻¹. Which way does it go?'),
    S("Tip: in a table of effects, the initial Q, the value of K and the amount of a substance are separate answers. "
      "Removing a product lowers Q and does not change K. Raising the temperature does not change Q at that moment, "
      "but it changes K. Very few students got all six boxes right.",
      refs=['ex23q10', 'ar23q10'], covers=['Q15', 'Q9', 'Q13'], elements=[4], exam=['X23-10']),
]),
Scene('lechatelier', P3, "Le Chatelier's Principle", Slide('table', title="Le Chatelier: 2SO₂ + O₂ ⇌ 2SO₃ (ΔH < 0)", chip='Element 4 · equilibrium',
    head=['Change', 'Shift', 'Explanation (rates)', 'K'], widths=[0.20, 0.13, 0.43, 0.14], size=20, counts=[1, 2, 3, 4, 5, 6], rows=[
        ['Add O₂', 'Right', 'Forward rate rises first; reverse catches up, using up O₂', 'same'],
        ['Remove SO₃', 'Right', 'Reverse rate falls; forward is faster until balanced', 'same'],
        ['Increase pressure (smaller volume)', 'Right', 'Side with fewer gas moles (2 versus 3): that rate is boosted', 'same'],
        ['Increase temperature', 'Left', 'Favours the endothermic (reverse) direction', 'falls'],
        ['Add a catalyst', 'None', 'Both rates rise equally; equilibrium is reached sooner', 'same'],
        ['Add an inert gas (constant volume)', 'None', 'Partial pressures of reacting gases unchanged', 'same']]), [
    S("Le Chatelier's principle says that if a change is imposed on a system at equilibrium, the system shifts to partly "
      "oppose the change. Use it to predict shifts, and then explain them. Tip: state the effect clearly first, such as "
      "shifts right, then the reason. Some students restated the change instead of describing the response.",
      refs=['content', 'ar24q10', 'ex24q10'], covers=['Q9'], elements=[4, 1], exam=['X24-10']),
    S("Here is the table for sulfur dioxide and oxygen making sulfur trioxide, which is exothermic. Adding oxygen shifts it right, as "
      "the system uses up some of it. Removing sulfur trioxide shifts it right as well. In an explanation by rates, "
      "adding a species increases the rate of the reaction that uses it, until the rates are equal again.",
      refs=['content', 'ar24q10', 'ex25q9'], covers=['Q9', 'Q8'], elements=[4], exam=['X24-10', 'X25-9']),
    S("Increasing the pressure by shrinking the volume shifts the equilibrium to the side with fewer moles of gas, here the "
      "right. A smaller volume increases the concentrations of all gases. Competing reactions increase, but by different amounts.",
      refs=['content', 'ex21q7', 'ex23q10'], covers=['Q9', 'Q8'], elements=[4], exam=['X21-7', 'X23-10']),
    S("A temperature increase shifts the equilibrium in the endothermic direction, here to the left. It is the only "
      "change that alters K. And for the exothermic reaction, the reverse reaction has the larger activation energy, so it benefits "
      "more from the heat. Say that.", refs=['content', 'ar22q7', 'ex22q7', 'ex23q10', 'ar25q9'], covers=['Q7', 'Q9', 'Q6'], elements=[4, 1], exam=['X22-7', 'X23-10']),
    S("A catalyst speeds up the forward and reverse reactions equally. There is no shift, and K is unchanged. Say that the equilibrium "
      "is reached faster. Not mentioning that rates of both directions rise cost marks in a recent exam.",
      refs=['ar24q10', 'ex24q10'], covers=['Q8', 'K8'], elements=[4], exam=['X24-10']),
    S("Adding an inert gas at constant volume changes the total pressure, but not the partial pressures of the reacting gases, so there is "
      "no effect. Most students assumed it would shift the equilibrium. And adding more of a solid, such as calcium carbonate, "
      "changes nothing, because solids are not in the expression.",
      refs=['ar24q10', 'ex24q10'], covers=['Q8', 'Q12'], elements=[4], exam=['X24-10']),
]),
Scene('eq_graph', P3, 'Concentration–time graphs', V.eq_disturb, [
    S("An equilibrium graph shows concentration against time. Before time A, all lines are flat. At A, extra oxygen is added, so "
      "only oxygen jumps up. The other lines do not change at that instant.",
      refs=['ex22q7', 'ar22q7'], covers=['Q9', 'Q8'], elements=[4, 3], exam=['X22-7']),
    S("Then the system shifts forward. Oxygen falls by x, sulfur dioxide falls by two x, and sulfur trioxide rises by two x, "
      "following the coefficients, in curves, not straight lines. Examiners said writing x, two x and three x is not enough: "
      "the curves need to be approximately to scale.", refs=['ar22q7'], covers=['Q9', 'Q14'], elements=[4, 5], exam=['X22-7']),
    S("At B the lines are flat again, a new equilibrium, and they stay flat until C. Oxygen ends higher than it started, "
      "because the shift only partly undoes the change. It does not finish below the original amount.",
      refs=['ar22q7'], covers=['Q9', 'Q10'], elements=[4], exam=['X22-7']),
]),
Scene('limits', P3, 'Limitations of Le Chatelier', Slide('bullets', title="Limitations of Le Chatelier's Principle", chip='Element 4 · A standard', size=26, counts=[1, 2, 3, 4], items=[
    'It is qualitative: it gives the DIRECTION of a shift, not how far. For amounts, use K',
    'It only applies to systems at equilibrium that are disturbed, not to reactions in progress',
    'It cannot predict the rate or how fast equilibrium is regained',
    'Complex or competing equilibria (such as CO₂, carbonate and shells) can have effects in opposite directions, so the net result needs care']), [
    S("An A standard answer states the limitations of Le Chatelier's principle. First, it is qualitative. It predicts the "
      "direction of a shift, but not how far. For amounts, you need the equilibrium constant.",
      refs=['standards', 'content'], covers=['Q10'], elements=[4, 1]),
    S("Second, it applies only to systems at equilibrium that are disturbed. It says nothing about the speed of the "
      "response, which depends on kinetics. And for temperature, K itself changes, so the shift is explained with enthalpy.",
      refs=['content', 'standards'], covers=['Q10', 'Q9'], elements=[4, 1]),
    S("Third, with several linked equilibria, one change can push in more than one direction. In the carbon dioxide question, "
      "hydrogen carbonate rises in one step and falls in the next, so the net effect must be argued, not simply stated.",
      refs=['ar25q7', 'ex25q7'], covers=['Q10', 'Q9'], elements=[4, 1], exam=['X25-7']),
    S("Also, the principle does not apply when conditions force a large change, or to systems far from equilibrium. When "
      "you meet a surprising result, say what the principle predicts, and then name the limitation that explains why the "
      "observation differs.", refs=['standards'], covers=['Q10'], elements=[4, 1]),
]),
Scene('reverse_ea', P3, 'Reversibility and activation energy', V.pe_reverse, [
    S("The reversibility of a reaction can be explained by the activation energies. The forward reaction has an activation "
      "energy. So does the reverse reaction, because products can also collide with enough energy to climb back over the hill.",
      refs=['content'], covers=['Q6', 'Q2'], elements=[4, 2]),
    S("For an exothermic reaction, the reverse activation energy is larger, by the size of delta H. So when the temperature rises, the "
      "reverse reaction speeds up more than the forward one, and the equilibrium shifts to the endothermic side.",
      refs=['content', 'ar22q7'], covers=['Q6', 'Q7'], elements=[4, 2], exam=['X22-7']),
    S("Use this idea when you explain temperature effects on equilibrium: it links energy diagrams, collision theory and "
      "Le Chatelier together. That is the sort of connection A standard answers make.", refs=['standards'], covers=['Q7', 'K10'], elements=[4, 3, 2]),
]),
Scene('industry', P3, 'Compromise conditions in industry', Slide('table', title='Rate against yield: choosing conditions', chip='Element 4 · equilibrium',
    head=['Condition', 'Best for yield*', 'Best for rate', 'Industry'], widths=[0.17, 0.30, 0.24, 0.20], size=20, counts=[1, 2, 3, 4], rows=[
        ['Temperature', 'LOW', 'HIGH', 'Moderate: a compromise'],
        ['Pressure', 'HIGH', 'HIGH', 'High, limited by cost and safety'],
        ['Catalyst', 'No effect on yield', 'Raises rate', 'Always used'],
        ['Remove product', 'Raises yield', '–', 'If it can be done continuously']], note='* for an exothermic reaction that makes fewer moles of gas (SO₃, NH₃, methanol)'), [
    S("Industrial processes balance rate and yield. Methanol, ammonia and sulfur trioxide are all exothermic and produce fewer moles "
      "of gas. A low temperature gives a higher yield, but is too slow. A high temperature gives a fast rate, but a "
      "low yield. So industry uses a moderate temperature. Just writing the word compromise, without naming temperature, scored nothing.",
      refs=['ex21q7', 'ex22q7', 'ex23q10', 'ar22q7', 'ar23q10'], covers=['Q9', 'Q7', 'K6'], elements=[4, 3], exam=['X21-7', 'X22-7', 'X23-10']),
    S("A high pressure helps both the yield, by shifting to fewer gas moles, and the rate, by raising concentrations. It is limited "
      "by cost and safety. A catalyst raises the rate without changing the yield, so it allows a lower temperature. And "
      "removing the product keeps shifting the equilibrium forward.", refs=['ex21q7', 'ar21q7', 'ex23q10'], covers=['Q9', 'K8', 'Q8'], elements=[4, 3], exam=['X21-7', 'X23-10']),
    S("Question parts ask for rate and equilibrium separately. In a methyl salicylate question, the rate answer was high "
      "temperature, with collision theory. The equilibrium answer was a low temperature for this exothermic reaction, or an excess "
      "of methanol, or removing water. Marks went to naming a valid change, stating the Le Chatelier shift, and linking it to more product. "
      "Do not add pressure for liquids.", refs=['ex25q8', 'ar25q8', 'ar25b'], covers=['Q9', 'K6', 'Q8'], elements=[4, 3], exam=['X25-8']),
    S("For the rate part, do not use equilibrium ideas, and for the equilibrium part, do not use collision theory. And "
      "state which result is desirable, such as more product.", refs=['ar25q8', 'ex25q8'], covers=['Q9', 'K6'], elements=[4, 3], exam=['X25-8']),
]),
Scene('colour_eq', P3, 'A colour-change equilibrium', Slide('worked', title='Worked example 9: predicting colour changes', chip='Element 4 · equilibrium',
    q='Fe³⁺(aq) (pale yellow) + SCN⁻(aq) (colourless) ⇌ FeSCN²⁺(aq) (deep red). Predict the colour change when (a) more Fe³⁺ is added; (b) silver ions are added (AgSCN is insoluble); (c) the mixture is diluted with water.',
    rows=[dict(s=0, t='(a) Add Fe³⁺: more reactant. Forward rate rises. Shifts RIGHT: more FeSCN²⁺, deeper red.', col='#eef2f8', size=23),
          dict(s=1, t='(b) Ag⁺ + SCN⁻ → AgSCN(s): SCN⁻ is removed (a reactant). Shifts LEFT: red fades.', col='#eef2f8', size=23),
          dict(s=2, t='(c) Dilute: all concentrations fall. Q = [FeSCN²⁺]/([Fe³⁺][SCN⁻]) rises above K, as the', col='#eef2f8', size=23),
          dict(s=2, t='denominator falls more (2 particles on the left): Q > K, so it shifts LEFT. Not just “less intense”.', col='#eef2f8', size=23),
          dict(s=3, t='K is unchanged in all three: only temperature changes K.', col='#9bde7e', size=24)]), [
    S("Colour changes make good test questions. This system has iron three plus, colourless thiocyanate, and a deep red "
      "product. Adding more iron three plus adds a reactant, so the forward reaction speeds up, the equilibrium shifts right, "
      "and the solution gets redder.", refs=['ex25q9', 'ar25q9', 'content'], covers=['Q9', 'Q8'], elements=[4], exam=['X25-9'],
      problem='Fe³⁺ + SCN⁻ ⇌ FeSCN²⁺ (red). What happens to the colour when more Fe³⁺ is added?'),
    S("Silver ions bind thiocyanate in an insoluble solid. Removing a reactant shifts the equilibrium left, and the red fades. "
      "In a related exam question, precipitating chloride shifted the system and changed the colour. Explain by naming the "
      "species removed and the shift.", refs=['ar25q9', 'ex25q9'], covers=['Q9', 'Q8'], elements=[4], exam=['X25-9'],
      problem='Silver ions are added to Fe³⁺ + SCN⁻ ⇌ FeSCN²⁺. What happens to the colour, and why?'),
    S("Dilution lowers all concentrations, but not equally. The left side has two dissolved particles and the right has "
      "one, so Q rises above K and the system shifts left. Many students just said the colour became less intense. "
      "A good answer discusses the shift. Finally, K stays the same, because the temperature did not change.",
      refs=['ar25q9', 'ex25q9'], covers=['Q9', 'Q15', 'Q13'], elements=[4], exam=['X25-9'],
      problem='The Fe³⁺ + SCN⁻ ⇌ FeSCN²⁺ mixture is diluted with water. What happens to the position of equilibrium and to K?'),
    S("A related exam system was chlorine water: chlorine reacting with water to make hydrogen ions, chloride ions and hypochlorous "
      "acid, in an equilibrium. At a low pH there are many hydrogen ions, so Le Chatelier's principle shifts the equilibrium left, and "
      "chlorine is the most abundant of the chlorine species. Write the equation with an equilibrium arrow, and do not confuse "
      "the chlorine molecule with chloride ions.", refs=['ex21q10', 'ar21q10'], covers=['Q9', 'Q8'], elements=[4, 1], exam=['X21-10']),
    S("Contexts using equilibrium include wine making. Sulfur dioxide is added to wine to bind acetaldehyde, a reversible "
      "reaction, so the winemaker uses equilibrium ideas to control the chemical balance of acidity, alcohol, sugar and colour.",
      refs=['appendix'], covers=['A3'], elements=[1]),
]),
Scene('ocean', P3, 'Carbon dioxide and the oceans', V.co2_chain, [
    S("Carbon dioxide dissolving in the ocean is a set of linked equilibria. Carbon dioxide dissolves, and reacts "
      "with water to make carbonic acid. When the atmospheric concentration rises, Le Chatelier's principle shifts the first "
      "equilibria right, making more carbonic acid.", refs=['appendix', 'ex25q7', 'ex23q9', 'ar23q9'], covers=['A4', 'Q9'], elements=[1, 4], exam=['X25-7', 'X23-9']),
    S("Carbonic acid is a weak acid. It ionises to give hydrogen ions and hydrogen carbonate, and that ionises again. The extra "
      "hydrogen ions lower the pH. The question asked about temperature too: if the dissolving is endothermic, "
      "warmer water shifts it right and raises the acidity. Many students forgot to explain how the acid ionises to release hydrogen ions.",
      refs=['ar23q9', 'ar25q7', 'content'], covers=['A4', 'Q7', 'B2'], elements=[4, 1], exam=['X23-9', 'X25-7']),
    S("Shells and plankton contain calcium carbonate. Extra hydrogen ions shift the last equilibrium right, so calcium "
      "carbonate dissolves. The report noted the trap: hydrogen carbonate rises in one step but is used up in the "
      "next, so use the rise in hydrogen ions to argue the shift, then link it back to the shellfish.",
      refs=['ar25q7', 'ex25q7'], covers=['A4', 'Q9', 'Q10'], elements=[4, 1], exam=['X25-7']),
]),

# ------------------------------------------------------------------ Part 4
Scene('bl_acids', P4, 'Acids, bases and conjugate pairs', Slide('cards', title='The Brønsted-Lowry model', chip='Element 1 · principles', cols=2, counts=[1, 2, 3, 4], size=21, cards=[
    ('Definitions', 'An acid DONATES a proton (H⁺). A base ACCEPTS one. Monoprotic acids donate one proton (HCl), polyprotic more (H₂SO₄, H₂CO₃).', '#a78bfa'),
    ('Conjugate pairs', 'After donating, the acid becomes its conjugate base: HA + H₂O ⇌ H₃O⁺ + A⁻. HA / A⁻ and H₃O⁺ / H₂O are conjugate pairs.', '#fb923c'),
    ('Amphiprotic species', 'Can act as both: HCO₃⁻ donates H⁺ (to CO₃²⁻) or accepts H⁺ (to H₂CO₃). Water is also amphiprotic.', '#9bde7e'),
    ('Ammonia in water', 'NH₃ + H₂O ⇌ NH₄⁺ + OH⁻. Water donates a proton, so water is the acid; NH₃ is the base.', '#f15bb5')]), [
    S("The Brønsted Lowry model defines acids as proton donors, and bases as proton acceptors. A proton is a hydrogen ion. "
      "Monoprotic acids donate one proton per molecule, and polyprotic acids donate more than one. When an acid donates a "
      "proton, what remains is its conjugate base.", refs=['content', 'ex21q8', 'ex23q9'], covers=['B1', 'B5'], elements=[1], exam=['X21-8', 'X23-9']),
    S("Equations show this as a transfer. An acid, H A, plus water gives hydronium and the conjugate base A minus. On "
      "the information sheet, the hydrogen ion and the hydronium ion are treated as the same. Label which species is the acid and "
      "which is the base on each side.", refs=['content', 'info_eq'], covers=['B5'], elements=[1]),
    S("Some species can act as both. Hydrogen carbonate gives a proton in one step, and takes a proton in the other, so it "
      "is amphiprotic. Less than half the students could show both. Note carbonate cannot donate protons.",
      refs=['ex23q9', 'ar23q9'], covers=['B1', 'B5'], elements=[1], exam=['X23-9']),
    S("In the ammonia equation, water donates a proton to ammonia, so water is the acid and ammonia is the base. "
      "Justify with the definition: Brønsted Lowry acids donate protons.", refs=['ex21q8', 'ar21q8'], covers=['B5', 'B1'], elements=[1], exam=['X21-8']),
]),
Scene('ka', P4, 'Strength, Ka and Kw', Phased((3, V.acid_particles), (1, Slide('eqs', title='Ka, Kw and pH', chip='Element 5 · pH and acids', counts=[2], gap=0.19, size=32, nx=0.58, y=0.72, section='Chemical Equilibrium Formulae', items=[
    ('sheet', '$K_w = [H^+][OH^-] = 1.00\\times10^{-14}\\ \\mathrm{mol^2\\,L^{-2}}$ at 25 °C', ''),
    ('sheet', '$pH = -\\log[H^+]$        $[H^+] = 10^{-pH}$', 'on the sheet: [H⁺] means [H₃O⁺]')]))), [
    S("Strength is about how far an acid ionises, not how concentrated it is. A strong acid ionises completely in water. "
      "A weak acid ionises only slightly, so most molecules stay as they were. Strong acids such as hydrochloric acid are fully "
      "ionised, so a Ka for them is not usually given.", refs=['content', 'ex21q10', 'ar21q10'], covers=['B2', 'B3'], elements=[1], exam=['X21-10']),
    S("The acid ionisation constant is K a, the concentration of hydrogen ions times the conjugate base, over the acid. It is "
      "not on the information sheet, so learn it, and write it right way up with square brackets. A small K a means a weak "
      "acid, and in the exam question, the species with the greatest concentration at equilibrium was the unionised acid.",
      refs=['content', 'ex21q10', 'ar21q10', 'ex23q9', 'ar23q9'], covers=['B3', 'B2'], elements=[1, 5], exam=['X21-10', 'X23-9']),
    S("A weak acid with the same concentration as a strong acid has fewer hydrogen ions, so a higher pH. A larger K a "
      "means a stronger acid: of the two steps of carbonic acid, the first, with the bigger K a, is the stronger acid.",
      refs=['ar23q9', 'ex22q10', 'ar22q10'], covers=['B2', 'B3'], elements=[1], exam=['X23-9', 'X22-10']),
    S("Water ionises slightly, and on your information sheet, in the chemical equilibrium formulae section, K w is hydrogen ion "
      "concentration times hydroxide ion concentration, one point oh oh times ten to the minus fourteen at twenty five degrees. "
      "The sheet also gives pH as minus log of the hydrogen ion concentration, and the reverse.",
      refs=['info_eq', 'content'], covers=['B4', 'B6'], elements=[5, 1]),
]),
Scene('we_ph', P4, 'Worked examples: pH', Slide('worked', title='Worked example 10: pH of acids and bases', chip='Element 5 · pH and acids',
    q='Find the pH of: (a) 0.0250 mol L⁻¹ HNO₃; (b) 0.100 mol L⁻¹ ethanoic acid (Ka = 1.74 × 10⁻⁵, reference data, not from TASC); (c) 0.0100 mol L⁻¹ Ba(OH)₂; (d) concentrated HCl, 36.0% by mass, density 1.18 g mL⁻¹. Use Kw = 1.00 × 10⁻¹⁴.',
    size=23,
    rows=[dict(s=0, t='(a) Strong, monoprotic: [H⁺] = 0.0250.   pH = −log(0.0250) = 1.602', col='#ffd166'),
          dict(s=0, sf='= 1.60 (2 d.p., as the concentration has 3 s.f.)', t='', gap=0),
          dict(s=1, t='(b) Weak: Ka = x² / 0.100  (x small),  x = √(1.74×10⁻⁵ × 0.100) = 1.319×10⁻³', col='#ffd166'),
          dict(s=1, t='pH = −log(1.319×10⁻³) = 2.88.   Check: x / 0.100 = 1.3% < 5%, so the approximation holds', col='#9bde7e'),
          dict(s=2, t='(c) [OH⁻] = 2 × 0.0100 = 0.0200.   [H⁺] = Kw / [OH⁻] = 1.00×10⁻¹⁴ / 0.0200 = 5.00×10⁻¹³', col='#ffd166'),
          dict(s=2, t='pH = −log(5.00×10⁻¹³) = 12.30', col='#9bde7e'),
          dict(s=3, t='(d) c = 1000 × 1.18 × 0.360 / 36.46 = 11.65 mol L⁻¹.   pH = −log(11.65) = −1.07', col='#ffd166'),
          dict(s=3, t='So the pH scale is not limited to 0 to 14. Pure water is pH 7.0 only at 25 °C (SLC).', col='#b3c0d4', size=22)]), [
    S("Worked example ten. For a strong monoprotic acid, the hydrogen ion concentration equals the acid concentration. "
      "Zero point oh two five moles per litre of nitric acid gives a pH of minus log zero point oh two five, one point six oh "
      "two, about one point six oh.", refs=['info_eq', 'content'], covers=['B7', 'B6'], elements=[5],
      problem='What is the pH of 0.0250 mol L⁻¹ nitric acid?'),
    S("For a weak acid, K a is x squared over the starting concentration, if x is small. Zero point one moles per litre of "
      "ethanoic acid with a K a of one point seven four times ten to the minus five gives x of one point three two times ten to "
      "the minus three, and a pH of two point eight eight. Check that x is small compared with zero point one, so "
      "the approximation is fair.", refs=['content', 'ex22q10', 'ar22q10'], covers=['B8', 'B3'], elements=[5, 1], exam=['X22-10'],
      problem='What is the pH of 0.100 mol L⁻¹ ethanoic acid if Ka = 1.74 × 10⁻⁵?'),
    S("For a strong base, use the stoichiometry and K w. Barium hydroxide has two hydroxides per formula, so the hydroxide "
      "concentration is zero point oh two. Then hydrogen ion concentration is K w divided by that, five times ten to the "
      "minus thirteen, and the pH is twelve point three oh.", refs=['info_eq', 'content'], covers=['B9', 'B4', 'B6'], elements=[5],
      problem='What is the pH of 0.0100 mol L⁻¹ barium hydroxide (Kw = 1.00 × 10⁻¹⁴)?'),
    S("A 2021 question asked students to show that the pH scale is not limited to zero to fourteen, using concentrated "
      "hydrochloric acid. Here, the concentration is eleven point six five moles per litre, giving a pH of minus one point "
      "oh seven. Show each step. Also, pure water is pH seven only at twenty five degrees, standard laboratory conditions. "
      "Standard temperature and pressure was not accepted.", refs=['ex21q6', 'ar21q6', 'info_eq'], covers=['B7', 'B6', 'B4'], elements=[5, 1], exam=['X21-6'],
      problem='Calculate the pH of concentrated HCl that is 36.0% HCl by mass with a density of 1.18 g mL⁻¹.'),
]),
Scene('evap', P4, 'Equilibrium from a vapour pressure', Slide('worked', title='Worked example 11: equilibrium of a physical change', chip='Element 5 · calculations',
    q='For H₂O(l) ⇌ H₂O(g), Kc = [H₂O(g)]. The vapour pressure of water at 30 °C (303 K) is 4.25 kPa (reference data, not from TASC). Find Kc. Then find the mass of liquid left if 0.100 g of water is sealed in a dry 3.00 L flask at 30 °C. (R = 8.31 L kPa K⁻¹ mol⁻¹.)',
    size=24,
    rows=[dict(s=0, t='[H₂O(g)] = n / V = P / RT = 4.25 / (8.31 × 303) = 1.688 × 10⁻³ mol L⁻¹ = Kc', col='#ffd166'),
          dict(s=0, sf='= 1.69 × 10⁻³ mol L⁻¹ (3 s.f.)', t='', gap=0),
          dict(s=0, t='(the liquid is left out of Kc because its concentration is effectively constant)', col='#b3c0d4', size=21),
          dict(s=1, t='n(vapour) = 1.688×10⁻³ × 3.00 = 5.064×10⁻³ mol;   m = 5.064×10⁻³ × 18.016 = 0.09123 g', col='#eef2f8'),
          dict(s=2, t='Liquid left = 0.100 − 0.0912 = 0.0088 g  (liquid remains, so it IS at equilibrium)', col='#9bde7e'),
          dict(s=2, sf='= 0.009 g (limited by the 3 d.p. of 0.100 g)', t='', gap=0)]), [
    S("A physical change can be an equilibrium too. For water evaporating, the expression is K c equals the concentration of "
      "water vapour. From the gas equation on the information sheet, P V equals n R T, so concentration is P over R T. With "
      "a vapour pressure of four point two five kilopascals at thirty degrees, K c is about one point six nine times ten to the minus three.",
      refs=['info', 'info_data', 'ex25q11', 'ar25q11'], covers=['Q12', 'Q14', 'Q11'], elements=[5, 4], exam=['X25-11'],
      problem='The vapour pressure of water at 303 K is 4.25 kPa. Find Kc for H₂O(l) ⇌ H₂O(g) (R = 8.31 L kPa K⁻¹ mol⁻¹).'),
    S("Now a sealed three litre flask with a drop of water of zero point one oh oh grams. The vapour needs five point oh six "
      "times ten to the minus three moles to reach this concentration, which is zero point oh nine one grams. So "
      "the mass of liquid water remaining is the difference, about zero point oh oh nine grams.",
      refs=['ar25q11', 'info_ar'], covers=['Q14', 'Q12'], elements=[5], exam=['X25-11'],
      problem='0.100 g of water is sealed in a dry 3.00 L flask at 303 K with Kc = 1.69 × 10⁻³ mol L⁻¹. What mass of liquid water remains?'),
    S("Read the wording: many students found the mass of the vapour, but the question asked for the liquid remaining. "
      "Another point: the calculation only works if there is liquid left. If all the water evaporated, it would not be an equilibrium.",
      refs=['ar25q11'], covers=['Q14'], elements=[5], exam=['X25-11']),
]),

# ------------------------------------------------------------------ finish
Scene('exam_tips', P5, 'Tips for tests and the exam', Slide('tips', title='Tips from examiners', counts=[2, 4, 6, 8], tips=[
    'Bond breaking ABSORBS energy;\nbond forming RELEASES it',
    'Energy diagrams: label real species\nand states, Ea and ΔH, sensible scale',
    'Rates: effective collisions per second;\nnever just “more collisions”',
    'Catalyst: lower Ea, both directions,\nno change to ΔH, K or the position',
    'Distribution curve: skewed, same area,\nnot a semicircle',
    'Calorimetry: mass of WATER in mcΔT;\nΔT in °C = K; sign and units',
    'Equilibrium: rates equal, not zero.\nK changes only with temperature',
    'Heterogeneous K: leave out solids\nand liquids; inert gas: no shift']), [
    S("Finally, technique for tests and the exam, from examiners' reports. One: bond breaking absorbs energy, and bond forming "
      "releases it. Two: on energy diagrams, label the real species with states, the activation energy and delta H, "
      "with a sensible scale, and do not start at zero.", refs=['ar24q6', 'ar23q7', 'ar25q8']),
    S("Three: for rates, talk about effective collisions per second. Four: a catalyst lowers the activation energy for both directions. "
      "It does not change delta H, K or the position of equilibrium. Five: draw the distribution curve skewed, with the "
      "same area, not a semicircle.", refs=['ar23q7', 'ar22q9', 'ar24q10', 'ar21q7']),
    S("Six: in calorimetry, use the mass of the water, and a temperature change in Celsius equals the same in kelvin. Give "
      "the sign and units. Seven: at equilibrium the rates are equal, not zero, and K changes only with temperature. Eight: for "
      "heterogeneous equilibria, leave out solids and liquids, and remember an inert gas does not shift the equilibrium.",
      refs=['ar25q10', 'ar25q9', 'ar24q10']),
]),
Scene('more_tips', P5, 'More examiner tips', Slide('tips', title='More tips from examiners', start=9, counts=[4, 8], tips=[
    'Graphs: tangent for instantaneous rate;\nmoles from volume, then divide by time',
    'A flat graph = reactant used up,\nnot equilibrium; sketch to scale',
    'Explain, not restate: say the SHIFT\nand the reason, then the effect',
    'Asked for rate? Use kinetics. Asked for\nyield? Use equilibrium. Keep them apart',
    'Industrial compromise: name the\ntemperature, and why',
    'Weak acid pH is above a strong\nacid of the same concentration',
    'Name the species: “chloride ions”,\nnot “chlorine”; write “K =” and states',
    'Read the whole question: facts in\nthe stem apply to every part']), [
    S("More tips. Nine: for rates from graphs, draw a tangent and convert volume to moles first. Ten: a flat graph "
      "means a reactant is used up, not equilibrium, and sketch to scale. Eleven: state the shift, then the reason, then the "
      "effect, and do not just restate the change. Twelve: when asked about rate, use kinetics, and when asked about yield, use equilibrium.",
      refs=['ar24q8', 'ar23q6', 'ar22q7', 'ar25q8']),
    S("Thirteen: for an industrial compromise, name the temperature and say why. Fourteen: a weak acid has a higher pH than a strong "
      "acid of the same concentration. Fifteen: name species exactly, write K c equals, and include states, because "
      "markers deduct for missing states. Sixteen: read the whole question, because information in the stem applies to every part.",
      refs=['ar22q7', 'ar22q10', 'ar21q10', 'ar25g']),
]),
Scene('summary', P5, 'Summary', Slide('summary', title='Criterion 6 in one screen', chips=[
    ('bond breaking absorbs', '1'), ('ΔH < 0 exothermic', '1'), ('Ea and ΔH diagram', '1'), ('E = mcΔT', '2'), ('Cf = VIt/ΔT', '2'),
    ('bond energies', '2'), ("Hess's Law", '2'), ('effective collisions', 'p'), ('energy distribution', 'p'), ('catalyst: lower Ea', 'p'),
    ('rate = Δn / t', 'p'), ('dynamic equilibrium', 'g'), ('Kc = products / reactants', 'g'), ('Q vs K', 'g'), ("Le Chatelier", 'g'),
    ('Ka and Kw', 'y'), ('pH = −log[H⁺]', 'y')],
    close='Rate is kinetics. Yield is equilibrium. Always say WHY.'), [
    S("That is the whole of Criterion 6. Bond breaking absorbs energy, bond forming releases it, and energy diagrams show Ea and "
      "delta H. Calorimetry, bond energies and Hess's law give enthalpy changes. Collision theory and the energy distribution "
      "explain rates, and catalysts lower the activation energy. Equilibrium is dynamic, K and Q predict direction, and Le "
      "Chatelier predicts shifts, within its limits. Then acids, bases and pH. Practise explaining each idea in words, and "
      "you will be ready for your tests and for Section B. Good luck."),
]),
]

_used = {r for sc in SCENES for st in sc.steps for r in st.refs} | {t[1] for t in EXAM_TOPICS.values()} \
    | {t[1] for t in SYLLABUS.values()} | {t[1] for t in ELEMENTS.values()} | {'info', 'info_eq', 'info_data'}
REFS = {k: r for k, r in REFS.items() if k in _used}

VIDEO = Video(
    id='CHM415115_C6_thermo_kinetics_equilibrium',
    course=COURSE, course_name='Chemistry', module=MODULE,
    module_name='Criterion 6: Identify and apply principles and theories of thermochemistry, kinetics and equilibrium',
    title='Criterion 6: thermochemistry, kinetics and equilibrium, complete revision',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Chemical Information'),
    checks=CHECKS,
    thumbnail=V.thumbnail,
    allowed_overlaps=['identify and apply principles and theories of thermochemistry, kinetics and equilibrium'],
    keywords=['enthalpy', 'exothermic', 'endothermic', 'activation energy', 'collision theory', 'effective collisions',
              'catalyst', 'equilibrium', 'dynamic equilibrium', "Le Chatelier's principle", 'reaction quotient',
              'equilibrium constant', 'calorimetry', 'calibration factor', 'bond energy', "Hess's law", 'entropy',
              'Brønsted-Lowry', 'conjugate base', 'pH', 'strong acid', 'weak acid', 'surface area', 'limiting reagent'],
    description=('A complete revision explainer for TASC Chemistry (CHM415115) Criterion 6: identify and apply principles '
                 'and theories of thermochemistry, kinetics and equilibrium. For class tests and the end-of-year exam '
                 '(Section B). Items from the TASC information sheet are labelled on screen.'),
)
