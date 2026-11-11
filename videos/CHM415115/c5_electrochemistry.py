"""CHM415115 Chemistry, Criterion 5: Identify and apply fundamental principles and theories of electrochemistry.

    uv run python -m explainer check   videos/CHM415115/c5_electrochemistry.py
    uv run python -m explainer preview videos/CHM415115/c5_electrochemistry.py
    uv run python -m explainer thumbnail videos/CHM415115/c5_electrochemistry.py
    uv run python -m explainer render  videos/CHM415115/c5_electrochemistry.py    # operator only
"""
import math

from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, InfoSheet, import_sibling

COURSE, MODULE = 'CHM415115', 'C5'
L.use(style.theme(COURSE, MODULE))
V = import_sibling(__file__, 'c5_visuals.py')
_CC = import_sibling(__file__, 'chm_common.py')
Slide, Seq, ch = _CC.Slide, _CC.Seq, _CC.ch

P0 = 'Criterion 5 · Overview'
P1 = 'Part 1 · Redox'
P2 = 'Part 2 · The electrochemical series'
P3 = 'Part 3 · Galvanic cells'
P4 = 'Part 4 · Electrolysis'
P5 = 'Part 5 · Corrosion'
P6 = 'Finish · Tests & exam technique'

# --------------------------------------------------------------------------- references
COURSE_DOC = 'chm415115-9.html'
INFO = 'CHM415115-Chemistry-Information-Sheet.pdf'
SPEC = 'CHM415115-Chemistry-External-Assessment-Specifications.pdf'

EXAM_PAGES = {
    2021: {1: '4-5', 2: '6-7', 3: '8-9', 4: '10-11', 5: 12},
    2022: {1: '4-5', 2: 6, 3: 7, 4: 8, 5: '9-10'},
    2023: {1: 3, 2: '4-5', 3: 6, 4: '8-9', 5: '10-11'},
    2024: {1: 4, 2: 5, 3: '6-7', 4: '8-9', 5: '10-11'},
    2025: {1: '3-4', 2: 5, 3: '6-7', 4: '8-9', 5: 10, 6: '12-14'},
}
REPORT_PAGES = {
    2021: {1: '1-2', 2: '2-3', 3: '3-4', 4: '4-5', 5: 6},
    2022: {1: '1-2', 2: 2, 3: 3, 4: '3-4', 5: '4-5'},
    2023: {1: 1, 2: 2, 3: 3, 4: '3-4', 5: '4-5'},
    2024: {1: '1, 3', 2: '1, 3-4', 3: '2, 4-5', 4: '2, 5-6', 5: '3, 6'},
    2025: {1: '2, 4-5', 2: '2, 5', 3: '2-3, 5-6', 4: '3, 6-7', 5: '3, 7-8', 6: '3, 8'},
}


def exam(y, q):
    section = 'Part 1' if y == 2021 else 'Section A'
    return Ref(f'CHM415115-Chemistry-TASC-Exam-Paper-{y}.pdf', f'{y} exam, {section}, Question {q}', EXAM_PAGES[y][q])


def report(y, q):
    return Ref(f'CHM415115-Chemistry-Assessment-Report-{y}.pdf', f'{y} assessment report, Criterion 5, Question {q}',
               REPORT_PAGES[y][q])


REFS = {
    'standards': Ref(COURSE_DOC, 'Course document, Criterion 5 standards (element table)'),
    'content': Ref(COURSE_DOC, 'Course document, Science Understanding: electrochemistry and corrosion (Criterion 5)'),
    'appendix': Ref(COURSE_DOC, 'Course document, Appendix 1: contexts (cost of corrosion; breathalysers; fuel cells; electrochemistry for clean water)'),
    'info': Ref(INFO, 'Information sheet, Chemical Information (n(e⁻) = q/F = It/F)', page=2),
    'info_data': Ref(INFO, "Information sheet, Chemical Data and Constants (Faraday's constant)", page=1),
    'info_srp': Ref(INFO, 'Information sheet, Standard Reduction Potentials, Aqueous Ions', page=8),
    'info_ar': Ref(INFO, 'Information sheet, Table of Relative Atomic Masses', page=9),
    'spec': Ref(SPEC, 'External assessment specifications, Section A', page=2),
    'spec_q': Ref(SPEC, 'External assessment specifications, Appendix A (types of questions)', page=5),
}
for _y, _qs in EXAM_PAGES.items():
    for _q in _qs:
        REFS[f'ex{_y % 100}q{_q}'] = exam(_y, _q)
for _y, _qs in REPORT_PAGES.items():
    for _q in _qs:
        REFS[f'ar{_y % 100}q{_q}'] = report(_y, _q)
REFS['ar25g'] = Ref('CHM415115-Chemistry-Assessment-Report-2025.pdf', '2025 assessment report, General Comments', 1)
REFS['ar25a'] = Ref('CHM415115-Chemistry-Assessment-Report-2025.pdf', '2025 assessment report, Section A, Criterion 5 comments', 2)
REFS['ar23a'] = Ref('CHM415115-Chemistry-Assessment-Report-2023.pdf', '2023 assessment report, Section A, Criterion 5 comments', 1)
REFS['ar21a'] = Ref('CHM415115-Chemistry-Assessment-Report-2021.pdf', '2021 assessment report, Criterion 5, General Comments', 1)

# --------------------------------------------------------------------------- coverage targets
SYLLABUS = {
    'R1': ('Define a redox reaction: oxidation as loss and reduction as gain of electrons, shown in half-equations', 'content'),
    'R2': ('Use clues such as element to compound to spot a redox reaction', 'content'),
    'R3': ('Assign oxidation states for hydrogen and oxygen, including metal hydrides and peroxides', 'content'),
    'R4': ('Calculate oxidation states in molecules, molecular ions and compounds', 'content'),
    'R5': ('Identify the substances oxidised and reduced in a redox reaction', 'content'),
    'R6': ('Use the electrochemical series to identify oxidisers and reducers and to predict spontaneous reactions', 'content'),
    'R7': ('Identify oxidisers and reducers from the oxidation states of their atoms', 'content'),
    'R8': ('Identify the strongest oxidiser or reducer from a group, for example IO3⁻, I2 and I⁻', 'content'),
    'R9': ('Balance redox reactions in the presence of hydrogen ions', 'content'),
    'R10': ('Construct half-equations using H2O(l), H⁺(aq) and electrons', 'content'),
    'R11': ('Write overall equations by adding half-equations', 'content'),
    'R12': ('Gain or loss of electrons explained by valence electrons, energy and stability', 'content'),
    'R13': ('Gain or loss of electrons predicted from the position in the periodic table', 'content'),
    'R14': ('Relative strengths of oxidisers and reducers from standard electrode potentials', 'content'),
    'G1': ('Terms: electrode, anode, cathode, electrolyte, salt bridge, porous barrier, anions, cations, internal and external circuit', 'content'),
    'G2': ('Sketch labelled diagrams of galvanic cells', 'content'),
    'G3': ('Predict the movement of ions in the internal circuit and electrons in the external circuit', 'content'),
    'G4': ('Role of the salt bridge or porous barrier in maintaining electroneutrality', 'content'),
    'G5': ('How an electrochemical cell produces electrical energy from a spontaneous redox reaction', 'content'),
    'G6': ('Chemical shorthand (cell diagrams) for cells, including inert electrodes', 'content'),
    'G7': ('Convention: anode on the left and cathode on the right', 'content'),
    'G8': ('Cells not made of metals in solutions of their ions: inert electrodes and species with different oxidation states', 'content'),
    'G9': ('Chemicals and materials needed to construct a non-galvanic (electrolytic) cell', 'content'),
    'G10': ('How the electrochemical series was devised using the hydrogen half-cell', 'content'),
    'G11': ('Predict which electrode is the anode or cathode', 'content'),
    'G12': ('Calculate the standard EMF of a cell, E°', 'content'),
    'E1': ('Electrolytic cells use an external potential difference for non-spontaneous reactions, in small and industrial uses', 'content'),
    'E2': ('Predict the products of electrolysis of molten salts', 'content'),
    'E3': ('Predict the products of electrolysis of aqueous solutions with inert or reactive electrodes', 'content'),
    'E4': ('Anions with elements in their maximum oxidation states cannot be oxidised further', 'content'),
    'E5': ('Competing reactions when concentrations are non-standard', 'content'),
    'E6': ('Use the electrochemical series to predict electrolysis products and know its limitations', 'content'),
    'E7': ('Electrorefining', 'content'),
    'E7b': ('Electroplating', 'content'),
    'E8': ("Faraday's laws: calculate the mass of product, the current or the time of electrolysis", 'content'),
    'K1': ('Substances in the environment corrode metals by oxidation', 'content'),
    'K2': ('Steel has metallic bonding and rust has ionic bonding', 'content'),
    'K3': ('Contrast the physical properties of steel and rust', 'content'),
    'K4': ('Why rust occupies a much greater volume than the steel it came from', 'content'),
    'K5': ('Electrochemical nature of rusting: likely sites of oxidation and reduction', 'content'),
    'K6': ('Stress increases the likelihood of anode formation', 'content'),
    'K7': ('Cathodes tend to form where the concentration of O2 is highest', 'content'),
    'K8': ('Variation in O2 concentration can form an electrochemical cell', 'content'),
    'K9': ('Dissolved ions accelerate corrosion', 'content'),
    'K10': ('Predict the anode and cathode when two metals are in contact with an electrolyte', 'content'),
    'K11': ('Compare corrosion prevention: painting, lubrication, noble and sacrificial metal coatings, cathodic protection, polymer coatings', 'content'),
    'A1': ('Context: the cost of corrosion', 'appendix'),
    'A2': ('Context: breathalysers and redox', 'appendix'),
    'A3': ('Context: fuel cells and their uses, wet cells, dry cells, alkaline batteries', 'appendix'),
    'A4': ('Context: electrochemistry for clean water', 'appendix'),
}

ELEMENTS = {
    1: ('Explains fundamental principles and theories related to electrochemistry', 'standards'),
    2: ('Constructs half-equations to balance redox equations and predicts reactions between oxidisers and reducers', 'standards'),
    3: ('Uses the electrochemical series to predict reactions with more than two species, and suggests why variations occur', 'standards'),
    4: ('Draws cell diagrams with movement of ions and electrons and half-equations, in familiar and unfamiliar cells', 'standards'),
    5: ('Explains corrosion, describes prevention methods and identifies the most appropriate', 'standards'),
}

EXAM_TOPICS = {
    'X21-1': ('Vanadium ions: half-equations for zinc reducing an oxidiser; strongest oxidiser from oxidation numbers; why aluminium is a reducer; overall equation from two half-equations', 'ex21q1'),
    'X21-2': ('Copper concentration cell: half-equation and polarity, half-cell potential from a measured EMF, non-standard conditions, EMF falling to zero, unsuitable salt-bridge solutions, swapping an electrode', 'ex21q2'),
    'X21-3': ('Which pair can coexist; ordering three unknown metals from experiments; cell shorthand; placing half-equations in series order against hydrogen', 'ex21q3'),
    'X21-4': ('Copper sheathing held on by iron nails: explanation and an insulating layer; pitting of a galvanised tank, differential aeration', 'ex21q4'),
    'X21-5': ('Zinc from aqueous zinc sulfate but aluminium only from a melt; which electrode is aluminium', 'ex21q5'),
    'X22-1': ('Platinum and copper cell: complete labelled diagram, half-equations, maximum voltage, effect of swapping a half-cell', 'ex22q1'),
    'X22-2': ('Disproportionation of molten chlorate: oxidation states, half-equations, net ionic equation, why a melt reacts', 'ex22q2'),
    'X22-3': ('Galvanic against electrolytic cells in terms of energy; why aluminium cannot come from aqueous ions; a salt giving the same products molten or aqueous', 'ex22q3'),
    'X22-4': ('Electrolysis of molten, dilute and concentrated sodium chloride: products table, half-equations, net equations', 'ex22q4'),
    'X22-5': ('Electroplating zinc on iron: term, labelled diagram; nail corrosion by differential aeration; protection when the coating is damaged', 'ex22q5'),
    'X23-1': ('Vanadium oxidation numbers, strongest reducer, oxidation or reduction, balancing by the half-equation method', 'ex23q1'),
    'X23-2': ('Chromium and copper cell: labels, polarity, observations, initial EMF, salt-bridge chemical, replacing a half-cell with an inert electrode', 'ex23q2'),
    'X23-3': ('Table of spontaneous reactions between metals and ion solutions; zinc in iron(III) over time', 'ex23q3'),
    'X23-4': ('Steel boats in fresh water, salt water and deep water: ranking, explanation, diagram of the waterline, effect of attached zinc', 'ex23q4'),
    'X23-5': ('Electrolysis of sodium chloride: gases and half-equations, effect of lower concentration, copper electrodes', 'ex23q5'),
    'X24-1': ('Manganese oxidation states in three species; strongest oxidiser', 'ex24q1'),
    'X24-2': ('Periodate oxidising manganese dioxide: oxidation half-equation, net ionic equation, why hydrochloric acid is unwise', 'ex24q2'),
    'X24-3': ('Two roles of a salt bridge; lead-acid cell without a salt bridge; anode potential from a cell voltage; cell diagram', 'ex24q3'),
    'X24-4': ('Electrolysis of zinc sulfate with an aluminium cathode: diagram, half-equations, voltage; magnesium attempt; molten magnesium chloride and steel anodes', 'ex24q4'),
    'X24-5': ('Factors in iron corrosion, how paint works, alternatives, joining different metals, magnesium rod in a hot water cylinder', 'ex24q5'),
    'X25-1': ('Permanganate and sulfite half-equations and net ionic equation; zinc in copper sulfate; iron(III) with tin(II)', 'ex25q1'),
    'X25-2': ('Oxidation states of titanium including a hydride; why titanium tetrachloride is an oxidising agent', 'ex25q2'),
    'X25-3': ('Lithium-ion cell: labels, polarity, overall equation, purpose of the membrane, half-cell potential from the EMF', 'ex25q3'),
    'X25-4': ('Platinum electrolysis of sodium chloride solution with observations; effect of adding iron(II) chloride', 'ex25q4'),
    'X25-5': ("Zinc electrolysis: mass from current and time, time at a stated yield, gas formed at the cathode", 'ex25q5'),
    'X25-6': ('Steel pole rusting below ground, concrete cracking, why a tin post fails, an alternative method', 'ex25q6'),
}

# Every number spoken or shown in a worked example, recomputed.
F = 96500
M_NI, M_ZN = 58.69, 65.38


def _ni_mass():
    return 2.50 * 45.0 * 60 / F / 2 * M_NI


def _ni_time():
    return 5.00 / M_NI * 2 * F / 2.50 / 0.920


def _charge_balance(species):
    return sum(n * q for n, q in species)


CHECKS = [
    ('ON S in sulfate', lambda: -2 + 4 * 2, 6, 1e-9),
    ('ON Cr in dichromate', lambda: (-2 + 14) / 2, 6, 1e-9),
    ('ON Mn in KMnO4', lambda: 4 * 2 - 1, 7, 1e-9),
    ('ON N in ammonium', lambda: 1 - 4, -3, 1e-9),
    ('ON Cl in KClO3', lambda: 6 - 1, 5, 1e-9),
    ('dichromate net charge left', lambda: _charge_balance([(1, -2), (14, 1), (6, 2)]), 24, 1e-9),
    ('dichromate net charge right', lambda: _charge_balance([(2, 3), (6, 3)]), 24, 1e-9),
    ('dichromate E cell', lambda: 1.36 - 0.77, 0.59, 1e-9),
    ('permanganate peroxide charge left', lambda: _charge_balance([(2, -1), (6, 1)]), 4, 1e-9),
    ('permanganate peroxide charge right', lambda: _charge_balance([(2, 2)]), 4, 1e-9),
    ('permanganate peroxide H left', lambda: 5 * 2 + 6, 16, 1e-9),
    ('permanganate peroxide H right', lambda: 8 * 2, 16, 1e-9),
    ('permanganate peroxide O left', lambda: 2 * 4 + 5 * 2, 18, 1e-9),
    ('permanganate peroxide O right', lambda: 5 * 2 + 8, 18, 1e-9),
    ('permanganate peroxide E cell', lambda: 1.49 - 0.68, 0.81, 1e-9),
    ('peroxide disproportionation E cell', lambda: 1.78 - 0.68, 1.10, 1e-9),
    ('Cu in Ag+ E cell', lambda: 0.80 - 0.34, 0.46, 1e-9),
    ('Cu in H+ E cell', lambda: 0.00 - 0.34, -0.34, 1e-9),
    ('Fe3+ with Br- E cell', lambda: 0.77 - 1.09, -0.32, 1e-9),
    ('Mg with Cu2+', lambda: 0.34 + 2.38, 2.72, 1e-9),
    ('Mg with Zn2+', lambda: -0.76 + 2.38, 1.62, 1e-9),
    ('Ag Sn4+ cell E', lambda: 0.80 - 0.15, 0.65, 1e-9),
    ('Zn Cu cell E', lambda: 0.34 + 0.76, 1.10, 1e-9),
    ('missing half-cell E', lambda: 1.20 - 2.10, -0.90, 1e-9),
    ('PbBr2 minimum voltage', lambda: 1.09 + 0.13, 1.22, 1e-9),
    ('KI minimum voltage', lambda: 0.83 + 0.54, 1.37, 1e-9),
    ('CuSO4 inert minimum voltage', lambda: 1.23 - 0.34, 0.89, 1e-9),
    ('Ni charge', lambda: 2.50 * 45.0 * 60, 6750, 1e-9),
    ('Ni mol electrons', lambda: 2.50 * 45.0 * 60 / F, 0.06995, 1e-3),
    ('Ni mol Ni', lambda: 2.50 * 45.0 * 60 / F / 2, 0.034974, 1e-3),
    ('Ni mass', _ni_mass, 2.053, 1e-3),
    ('Ni mol for 5.00 g', lambda: 5.00 / M_NI, 0.08519, 1e-3),
    ('Ni mol electrons for 5.00 g', lambda: 5.00 / M_NI * 2, 0.17039, 1e-3),
    ('Ni charge for 5.00 g', lambda: 5.00 / M_NI * 2 * F, 16443, 1e-3),
    ('Ni time at 100 percent', lambda: 5.00 / M_NI * 2 * F / 2.50, 6577, 1e-3),
    ('Ni time at 92.0 percent', _ni_time, 7149, 1e-3),
    ('Ni time in minutes', lambda: _ni_time() / 60, 119.2, 1e-3),
    ('yield wrong way', lambda: 5.00 / M_NI * 2 * F / 2.50 * 0.920, 6051, 1e-3),
    ('zinc 2025 style mol e', lambda: 50.5 * 3600 / F, 1.884, 1e-3),
    ('zinc mass check', lambda: 50.5 * 3600 / F / 2 * M_ZN, 61.6, 2e-3),
]

# --------------------------------------------------------------------------- scenes
S = Step
SCENES = [
Scene('title', P0, 'Welcome', Slide('title', kicker='CRITERION 5', name='Fundamental principles\nand theories of\nelectrochemistry', art=V._title_cell, size=54), [
    S("Welcome. This video is a complete briefing on Criterion 5 of TASC Chemistry, C H M four one five, one one five: "
      "identify and apply fundamental principles and theories of electrochemistry. Use it to revise for class tests and "
      "for the end of year exam. By the end you should be able to balance redox equations, predict reactions from the "
      "electrochemical series, draw cells and write their half-equations, and explain corrosion and how to prevent it.",
      refs=['standards'], anim=4),
]),
Scene('intro', P0, 'How Criterion 5 is assessed', Seq(
    Slide('assess', internal='Your teacher: class tests, practicals\nand investigations during the year',
          external='End-of-year TASC exam:\nSection A is all Criterion 5', section='Section A'),
    Slide('elements', title='The five elements of Criterion 5', items=[
        ('Principles', 'identify, describe and explain electrochemical principles and theories'),
        ('Redox equations', 'build half-equations, balance redox equations, predict reactions'),
        ('The series', 'use the electrochemical series with more than two species; explain variations'),
        ('Cell diagrams', 'draw cells with ions, electrons and half-equations at each electrode'),
        ('Corrosion', 'explain corrosion, describe prevention, choose the most suitable')]),
    Slide('standards', title='What the standards ask for', rows=[
        ('E1 Principles', 'identifies', 'describes', 'explains'),
        ('E2 Redox', 'uses given half-equations', 'constructs half-equations from species', 'complex equations from species'),
        ('E3 Series', 'two species', 'more than two species', 'more than two, and suggests why variations occur'),
        ('E4 Cells', 'draws diagram and half-equations, familiar cells', 'adds movement of ions and electrons', 'does this in unfamiliar cells'),
        ('E5 Corrosion', 'steel: identifies the process, describes one method', 'describes the process and two or more methods', 'explains, and picks the most appropriate method')]),
    Slide('roadmap', title='Roadmap', parts=[
        ('Part 1', 'Redox: oxidation numbers and half-equations'), ('Part 2', 'The electrochemical series and predictions'),
        ('Part 3', 'Galvanic cells, salt bridges and cell diagrams'), ('Part 4', 'Electrolysis, plating and Faraday calculations'),
        ('Part 5', 'Corrosion and how to prevent it'), ('Finish', 'Tests and exam technique, and a one-screen summary')])), [
    S("Criterion 5 is assessed in two ways. Your teacher assesses it during the year, through class tests, practical work and "
      "investigations. It is also assessed externally, in Section A of the end of year exam: about forty five minutes, "
      "forty five marks, and between five and seven compulsory questions. You may use the information sheet and an approved "
      "calculator.", refs=['standards', 'spec']),
    S("The criterion has five elements, numbered here in the order they appear in the standards table. Element one is "
      "explaining the principles. Element two is building half-equations, balancing redox equations and predicting "
      "reactions. Element three is using the electrochemical series when more than two species are present. Element four "
      "is drawing cells. And element five is corrosion. A tag in the corner shows which element a slide is practising.",
      refs=['standards'], elements=[1, 2, 3, 4, 5]),
    S("The standards step up from C to A. At C you identify and describe, using given information. At B you construct your own half-equations, "
      "add the movement of ions and electrons, and describe two or more ways to prevent corrosion. At A you explain, handle complex "
      "equations and unfamiliar cells, suggest why results can vary from prediction, and choose the most appropriate "
      "method of corrosion prevention. So aim to explain, not just recall.", refs=['standards'], elements=[1, 2, 3, 4, 5]),
    S("Here is the roadmap. Part one: redox, oxidation numbers and half-equations. Part two: the electrochemical series. "
      "Part three: galvanic cells. Part four: electrolysis, including calculations with Faraday's laws. Part five: "
      "corrosion. Then technique for tests and the exam. Let's begin.", refs=['content']),
]),

# ------------------------------------------------------------------ Part 1
Scene('redox_def', P1, 'What redox means', V.redox_def, [
    S("Oxidation is the loss of electrons, and reduction is the gain of electrons. They always happen together, so a "
      "reaction with both is a redox reaction. A memory aid is O I L R I G: oxidation is loss, reduction is gain. We write each "
      "part as a half-equation, with the electrons shown.", refs=['content'], covers=['R1'], elements=[1]),
    S("Watch zinc give two electrons to a copper ion. Zinc loses electrons, so zinc is oxidised. It is the reducer, because "
      "it makes the other substance reduced. The copper ion gains them, so it is reduced. It is the oxidiser. A useful clue "
      "that a reaction is redox is an element turning into a compound, or a compound turning back into an element.",
      refs=['content'], covers=['R1', 'R2', 'R5'], elements=[1], anim=2),
    S("Tip: examiners keep seeing the same mistake. Metals are reducers and metal ions are oxidisers. A metal is never "
      "an oxidiser. Back every explanation with half-equations, even when the question does not ask for them.",
      refs=['ar21a', 'ar23a', 'ar25a'], covers=['R1'], elements=[1], anim=2),
]),
Scene('shells', P1, 'Why atoms lose or gain electrons', V.shells, [
    S("Why do atoms lose or gain electrons? It comes down to valence electrons and stability. Sodium has one outer "
      "electron. Losing it leaves the stable arrangement of neon, so sodium is a reducer. Chlorine is one electron short of a full "
      "shell, so it gains one and is an oxidiser.", refs=['content'], covers=['R12', 'R13'], elements=[1]),
    S("Aluminium, with electron arrangement two, eight, three, gives up all three outer electrons. Oxygen, two, six, gains two. "
      "In an answer, name the actual electron structure, and say that a reducer is the species that loses electrons. "
      "Examiners noted that many students did not do either.", refs=['content', 'ex21q1', 'ar21q1'], covers=['R12'],
      elements=[1], exam=['X21-1']),
    S("The periodic table predicts this. Metals on the left lose electrons easily, so they are reducers. Non-metals on the "
      "right gain electrons, so they are oxidisers. Going down a group, the outer electrons are further from the nucleus and "
      "more shielded, so metals lose them more easily and are stronger reducers.", refs=['content'], covers=['R13', 'R12'],
      elements=[1]),
]),
Scene('ox_rules', P1, 'Oxidation numbers: the rules', Slide('table', title='Oxidation number rules', chip='Element 2 · half-equations',
    head=['Rule', 'Example'], widths=[0.55, 0.35], size=24, counts=[3, 5, 7], rows=[
        ['An uncombined element is 0', 'Zn, O₂, Cl₂: 0'],
        ['A simple ion: its charge', 'Fe³⁺: +3,  Cl⁻: −1'],
        ['Total of a species = its overall charge', 'SO₄²⁻: total −2'],
        ['Oxygen is −2, except in peroxides (−1)', 'H₂O₂: O is −1'],
        ['Hydrogen is +1, except in metal hydrides (−1)', 'NaH: H is −1'],
        ['Group 1 is +1, group 2 is +2', 'K in KCl: +1'],
        ['Halogens are −1 in halides', 'Cl in NaCl: −1']]), [
    S("Oxidation numbers let us track electrons. An uncombined element is zero. A simple ion has its charge. The numbers in a "
      "species add up to its overall charge. Write the sign before the number, as plus seven, not seven plus. "
      "Charge and oxidation number are not the same thing.", refs=['content', 'ar24q1'], covers=['R4'], elements=[1, 2]),
    S("Oxygen is minus two, except in peroxides, where it is minus one. Hydrogen is plus one, except in metal hydrides, "
      "where it is minus one. Titanium hydride was a trap in a recent exam, because the hydrogen is minus one there, "
      "so titanium is plus two.", refs=['content', 'ex25q2', 'ar25q2'], covers=['R3'], elements=[1, 2], exam=['X25-2']),
    S("Group one metals are plus one, group two are plus two, and halogens are minus one in their halides. Use these "
      "to find the one unknown number.", refs=['content'], covers=['R3', 'R4'], elements=[2]),
]),
Scene('ox_calc', P1, 'Calculating oxidation numbers', Slide('table', title='Working out oxidation numbers', chip='Element 2 · half-equations',
    head=['Species', 'Working', 'Answer'], widths=[0.25, 0.45, 0.20], size=26, per=1, rows=[
        ['SO₄²⁻', 'S + 4(−2) = −2, so S = +6', 'S: +6'],
        ['Cr₂O₇²⁻', '2Cr + 7(−2) = −2, so 2Cr = +12', 'Cr: +6'],
        ['KMnO₄', '(+1) + Mn + 4(−2) = 0, so Mn = +7', 'Mn: +7'],
        ['NH₄⁺', 'N + 4(+1) = +1, so N = −3', 'N: −3'],
        ['KClO₃', '(+1) + Cl + 3(−2) = 0, so Cl = +5', 'Cl: +5'],
        ['H₂O₂', '2(+1) + 2O = 0, so O = −1', 'O: −1 (peroxide)']]), [
    S("Let's calculate. In the sulfate ion, four oxygens give minus eight, and the total is minus two, so sulfur is plus six. "
      "In the dichromate ion, seven oxygens give minus fourteen, the total is minus two, so two chromiums add to plus twelve: each is plus six.",
      refs=['content'], covers=['R4'], elements=[2], problem='What is the oxidation number of S in SO₄²⁻ and of Cr in Cr₂O₇²⁻?'),
    S("In potassium permanganate, potassium is plus one and four oxygens are minus eight, so manganese is plus seven. In the "
      "ammonium ion, four hydrogens give plus four, the total is plus one, so nitrogen is minus three.",
      refs=['content'], covers=['R4'], elements=[2], problem='What is the oxidation number of Mn in KMnO₄ and of N in NH₄⁺?'),
    S("In potassium chlorate, chlorine is plus five. In hydrogen peroxide, each hydrogen is plus one, so each oxygen is minus one: it "
      "is a peroxide. Watch for a formula with a repeated group, such as brackets with a subscript, because the group counts twice, "
      "and the number you find is for one atom.", refs=['content', 'ar24q1'], covers=['R3', 'R4'], elements=[2],
      exam=['X24-1', 'X23-1'], problem='What is the oxidation number of O in H₂O₂ and of Cl in KClO₃?'),
]),
Scene('ox_ident', P1, 'Oxidisers and reducers from oxidation numbers', Slide('worked', title='Strongest oxidiser or reducer?',
    chip='Element 1 · principles', q='Bromine can be found as BrO₃⁻, Br₂ and Br⁻. Using oxidation numbers, which is the strongest oxidiser, which is the strongest reducer, and which can act as both?',
    rows=[dict(s=0, t='Oxidation numbers of Br:   BrO₃⁻ = +5,    Br₂ = 0,    Br⁻ = −1', col='#eef2f8'),
          dict(s=1, t='BrO₃⁻ is at the HIGHEST oxidation number: it can only be reduced', col='#9bde7e'),
          dict(s=1, t='so it is the strongest oxidiser (greatest capacity to gain electrons)', col='#eef2f8'),
          dict(s=2, t='Br⁻ is at the LOWEST oxidation number: it can only be oxidised', col='#9bde7e'),
          dict(s=2, t='so it is the strongest reducer', col='#eef2f8'),
          dict(s=3, t='Br₂ is in between: it can be reduced (to Br⁻) or oxidised (to BrO₃⁻)', col='#ffd166'),
          dict(s=3, t='Say WHY: do not just state the number.', col='#f15bb5', size=22)]), [
    S("Here is a typical question. Bromine appears as bromate, BrO three minus, as the element, and as bromide. Their oxidation "
      "numbers are plus five, zero and minus one.", refs=['content', 'ex23q1', 'ex24q1'], covers=['R7', 'R8'], elements=[1, 2],
      exam=['X23-1', 'X24-1'], problem='For BrO₃⁻, Br₂ and Br⁻, which is the strongest oxidiser and which is the strongest reducer?'),
    S("Bromate is at the highest oxidation number. It cannot lose more electrons, it can only gain them, so it has the greatest "
      "capacity to be reduced: it is the strongest oxidiser. Saying only that it has the highest number is not enough for the "
      "mark. You must give that reason.", refs=['ar24q1', 'content'], covers=['R7', 'R8'], elements=[1, 2], exam=['X24-1']),
    S("Bromide is at the lowest oxidation number, so it can only be oxidised. It is the strongest reducer. Do not say the "
      "species with the highest charge is the strongest reducer. Oxidation state is not charge.",
      refs=['ar24q1', 'ex23q1', 'ar23q1'], covers=['R7', 'R8'], elements=[1, 2], exam=['X23-1']),
    S("The element, with oxidation number zero, sits in the middle. It can be reduced to bromide or oxidised to bromate, so it can "
      "act as an oxidiser or as a reducer. The same logic tells you whether a substance in a reaction is oxidised: if its "
      "oxidation number goes up, it has been oxidised.", refs=['content'], covers=['R5', 'R7', 'R8'], elements=[1, 2]),
]),
Scene('halfeq_method', P1, 'Balancing half-equations in acid', Slide('bullets', title='The half-equation method', chip='Element 2 · half-equations',
    size=26, items=['1. Write the species that change, and balance the atom being oxidised or reduced',
                    '2. Balance oxygen by adding H₂O(l)', '3. Balance hydrogen by adding H⁺(aq)',
                    '4. Balance charge by adding electrons e⁻', '5. Multiply so the electrons match, add, and cancel',
                    'Check: atoms and charge are the same on both sides']), [
    S("To balance a redox equation in acid, use the half-equation method. Write each half separately. One: balance the "
      "atom that changes. Two: balance oxygen by adding water. Three: balance hydrogen by adding hydrogen ions. Four: balance charge by "
      "adding electrons.", refs=['content'], covers=['R9', 'R10'], elements=[2], exam=['X23-1']),
    S("Five: multiply the halves so the electrons match, add them, and cancel anything that appears on both sides, "
      "such as water or hydrogen ions. Then check atoms and charge. A net ionic equation is the full redox equation. Do not break "
      "species into separate ions or remove parts of it.", refs=['content', 'ar24q2'], covers=['R9', 'R11'], elements=[2],
      exam=['X24-2', 'X25-1']),
]),
Scene('we_halfeq1', P1, 'Worked example: dichromate and iron(II)', Slide('worked', title='Worked example 1', chip='Element 2 · half-equations',
    q='Acidified dichromate ions, Cr₂O₇²⁻, oxidise iron(II) ions to iron(III) ions and are reduced to chromium(III) ions, Cr³⁺. Write the balanced net ionic equation and find E°cell.',
    rows=[dict(s=0, t='Reduction:   Cr₂O₇²⁻ → 2Cr³⁺                            (balance Cr)', col='#eef2f8'),
          dict(s=0, t='   + 7H₂O on the right,  + 14H⁺ on the left,  + 6e⁻ on the left', col='#b3c0d4'),
          dict(s=0, t='`Cr2O7^2-(aq) + 14H^+(aq) + 6e^- -> 2Cr^3+(aq) + 7H2O(l)`', col='#ffd166'),
          dict(s=1, t='Oxidation:   `Fe^2+(aq) -> Fe^3+(aq) + e^-`          × 6', col='#ffd166'),
          dict(s=2, t='`Cr2O7^2-(aq) + 14H^+(aq) + 6Fe^2+(aq) -> 2Cr^3+(aq) + 6Fe^3+(aq) + 7H2O(l)`', col='#9bde7e'),
          dict(s=2, t='Charge: left −2 + 14 + 12 = +24,  right 6 + 18 = +24  ✓', col='#b3c0d4', size=22),
          dict(s=3, t='E°cell = E°(oxidiser) − E°(reducer) = 1.36 − 0.77 = +0.59 V: spontaneous', col='#9bde7e')]), [
    S("Worked example one. Dichromate ions oxidise iron two plus ions in acid. Start with the reduction. Dichromate "
      "becomes two chromium three plus ions. Seven water molecules balance the oxygen, fourteen hydrogen ions balance the "
      "hydrogen, and six electrons balance the charge.", refs=['content', 'info_srp'], covers=['R9', 'R10'], elements=[2],
      problem='Balance the equation for acidified Cr₂O₇²⁻ oxidising Fe²⁺ to Fe³⁺ (Cr³⁺ formed).'),
    S("The oxidation is simple: iron two plus loses one electron to give iron three plus. Multiply it by six, so that six "
      "electrons are released, matching the six that dichromate gains.", refs=['content'], covers=['R10', 'R5'], elements=[2]),
    S("Add the halves. The electrons cancel. This is the net ionic equation. Always check charge: left side minus two plus "
      "fourteen plus twelve is twenty four, and the right side is six plus eighteen, also twenty four. It balances.",
      refs=['content'], covers=['R11'], elements=[2]),
    S("The dichromate half-equation and the iron half-equation are both on the information sheet, in the standard reduction "
      "potentials table. The cell E zero is one point three six minus zero point seven seven, which is positive "
      "zero point five nine volts, so the reaction is spontaneous.", refs=['info_srp'], covers=['R6', 'R14'], elements=[2, 3]),
]),
Scene('we_halfeq2', P1, 'Worked example: permanganate and peroxide', Slide('worked', title='Worked example 2: complex equation', chip='Element 2 · half-equations',
    q='Acidified permanganate, MnO₄⁻, reacts with hydrogen peroxide, H₂O₂. The products are manganese(II) ions and oxygen gas. Construct the balanced equation. (Peroxide is the reducer.)',
    rows=[dict(s=0, t='Reduction:  `MnO4^-(aq) + 8H^+(aq) + 5e^- -> Mn^2+(aq) + 4H2O(l)`        × 2', col='#ffd166'),
          dict(s=0, t='Oxidation:   `H2O2(aq) -> O2(g) + 2H^+(aq) + 2e^-`                                × 5', col='#ffd166'),
          dict(s=1, t='O in H₂O₂ is −1 and goes up to 0 in O₂: oxidised.   10 e⁻ each side.', col='#b3c0d4', size=22),
          dict(s=2, t='`2MnO4^-(aq) + 5H2O2(aq) + 6H^+(aq) -> 2Mn^2+(aq) + 5O2(g) + 8H2O(l)`', col='#9bde7e'),
          dict(s=2, t='Check:  charge +4 = +4;   H: 16 = 16;   O: 18 = 18  ✓', col='#b3c0d4', size=22),
          dict(s=3, t='E°cell = 1.49 − 0.68 = +0.81 V.  Also, H₂O₂ is an oxidiser (1.78 V)', col='#9bde7e'),
          dict(s=3, t='when it meets a weaker reducer: here it is the reducer, as MnO₄⁻ is stronger.', col='#b3c0d4', size=22)]), [
    S("Worked example two, a complex equation. You are given the species: permanganate and peroxide, in acid, making "
      "manganese two plus and oxygen. First the reduction. Manganese goes from plus seven to plus two, so five electrons. "
      "Four waters take the oxygen and eight hydrogen ions balance the hydrogen.", refs=['content', 'info_srp'], covers=['R9', 'R10'],
      elements=[2], problem='Construct the balanced equation for acidified MnO₄⁻ reacting with H₂O₂ to give Mn²⁺ and O₂.',
      exam=['X25-1']),
    S("Now the oxidation. Oxygen in peroxide goes from minus one to zero, giving oxygen gas, two hydrogen ions and two electrons. "
      "The lowest common multiple of five and two is ten, so multiply the reduction by two and the oxidation by five.",
      refs=['content', 'ar24q2'], covers=['R10', 'R5'], elements=[2], exam=['X24-2']),
    S("Add them, then cancel the electrons and the hydrogen ions that appear on both sides. Left over: two permanganate, "
      "five peroxide and six hydrogen ions make two manganese two plus, five oxygen and eight water. Check atoms and charge, "
      "both are balanced.", refs=['content'], covers=['R11', 'R9'], elements=[2]),
    S("The standard potentials give a positive cell potential of zero point eight one volts, so this does occur. "
      "Peroxide is unusual: it can be an oxidiser, as in the table at one point seven eight volts, or a reducer, as here. "
      "Which one it is depends on what it meets.", refs=['info_srp'], covers=['R6', 'R14'], elements=[2, 3]),
]),
Scene('disprop', P1, 'Disproportionation and molten reactions', Slide('worked', title='One species oxidised and reduced', chip='Element 2 · half-equations',
    q='Hydrogen peroxide decomposes: it is both oxidised and reduced. Show this with half-equations, and decide if it is spontaneous.',
    rows=[dict(s=0, t='Reduction:  `H2O2(aq) + 2H^+(aq) + 2e^- -> 2H2O(l)`        E° = +1.78 V', col='#ffd166'),
          dict(s=0, t='Oxidation:   `H2O2(aq) -> O2(g) + 2H^+(aq) + 2e^-`           (reverse of E° = +0.68 V)', col='#ffd166'),
          dict(s=1, t='`2H2O2(aq) -> 2H2O(l) + O2(g)`', col='#9bde7e'),
          dict(s=1, t='E°cell = 1.78 − 0.68 = +1.10 V: spontaneous (but slow without a catalyst)', col='#9bde7e'),
          dict(s=2, t='Molten ionic compounds react too: the ions are free to move and collide.', col='#b3c0d4', size=23),
          dict(s=2, t='Chlorate (+5) → chloride (−1) and perchlorate (+7): chlorine does both.', col='#b3c0d4', size=23)]), [
    S("In a disproportionation reaction, one species is both oxidised and reduced. Hydrogen peroxide is the classic example. "
      "It is reduced to water, and oxidised to oxygen. Add the half-equations and you get two peroxide making two water and "
      "oxygen. The potentials are one point seven eight and zero point six eight, a spontaneous difference of one point one "
      "zero volts.", refs=['content', 'info_srp', 'ex22q2'], covers=['R5', 'R11'], elements=[1, 2], exam=['X22-2'],
      problem='Show that H₂O₂ can be both oxidised and reduced, and find E°cell for its decomposition.'),
    S("Spontaneous does not mean fast, as we will see. In a recent exam, molten chlorate disproportionated, with chlorine going "
      "from plus five to plus seven in perchlorate and to minus one in chloride. For the net equation, balance each half, and "
      "cancel the water and hydrogen ions from the sum.", refs=['ar22q2'], covers=['R5', 'R9', 'R11'], elements=[2], exam=['X22-2']),
    S("Why can this happen with no water? In a melt the ions are free to move, so they can collide and react. The key "
      "words are molten, mobile ions, and collisions.", refs=['ar22q2'], elements=[1, 2], exam=['X22-2']),
]),

# ------------------------------------------------------------------ Part 2
Scene('ecs', P2, 'Using the electrochemical series', V.ecs, [
    S("Now the electrochemical series. On your information sheet, the standard reduction potentials table lists reduction "
      "half-equations from the strongest oxidisers at the top to the weakest at the bottom, with the standard potential, E zero, in "
      "volts. These values are for one mole per litre solutions at twenty five degrees. Species on the left of an equation are oxidisers.",
      refs=['info_srp', 'content'], covers=['R6', 'R14'], elements=[3]),
    S("The species on the right are reducers. The higher a reduction half-equation is on the table, the stronger its oxidiser on "
      "the left; the lower it is, the stronger its reducer on the right. A reaction is spontaneous when an oxidiser reacts with a "
      "reducer from a lower half-equation. Silver ions are above copper, so silver ions oxidise copper metal.",
      refs=['info_srp', 'content'], covers=['R6', 'R14'], elements=[3]),
    S("Tip: compare species correctly. Zinc is a reducer, and copper ions are an oxidiser, so you cannot compare their strengths "
      "directly. Compare the strengths of zinc and copper, or of zinc ions and copper ions. Talk about oxidising and reducing "
      "strength rather than position on the table, and say which species is the oxidiser.",
      refs=['info_srp', 'ar25q1', 'ar25a'], covers=['R6'], elements=[3, 1], exam=['X25-1']),
]),
Scene('she', P2, 'Where the series comes from', V.she, [
    S("Where do the numbers come from? Chemists chose one half-cell as the reference, the standard hydrogen half-cell: a "
      "platinum electrode, hydrogen gas at one atmosphere, and hydrogen ions at one mole per litre. They defined it as exactly "
      "zero volts.", refs=['content'], covers=['G10'], elements=[1]),
    S("Connect any other half-cell, also at standard conditions, and the voltage you measure is its standard potential. Zinc "
      "pushes electrons towards the hydrogen half-cell, so it reads minus zero point seven six volts. Copper ions take electrons from it, "
      "so copper reads plus zero point three four. Line them all up and you have the series.",
      refs=['content', 'info_srp'], covers=['G10', 'R14'], elements=[1, 3]),
    S("Remember the sign convention. The potentials are for reduction. To use a half-equation for oxidation, reverse it and "
      "change the sign. The sum of an oxidation potential and a reduction potential is the cell potential.",
      refs=['content'], covers=['R14', 'G12'], elements=[1, 3]),
]),
Scene('ecell', P2, 'Cell potential', Slide('eqs', title='Cell potential, E°cell', chip='Element 3 · series and data',
    counts=[1, 2, 3], gap=0.20, size=34, nx=0.55, items=[
        ('learn', '$E^\\circ_{cell} = E^\\circ_{reduction} - E^\\circ_{(other\\ half,\\ as\\ reduction)}$', 'Subtract the reducer’s listed value from the oxidiser’s'),
        ('learn', '$E^\\circ_{cell} = E^\\circ_{oxidation} + E^\\circ_{reduction}$', 'Or reverse the oxidation half and add: the same answer'),
        ('eq', '$E^\\circ_{cell} > 0\\ \\Rightarrow\\ $ spontaneous', 'A negative value: not spontaneous')]), [
    S("To predict a reaction, calculate the standard cell potential. This formula is not on the information sheet, so learn "
      "it. Take the reduction potential of the oxidiser, and subtract the reduction potential of the reducer's half-equation.",
      refs=['content'], covers=['G12', 'R6'], elements=[3]),
    S("Or reverse the oxidation half-equation, change its sign, and add the two. The answer is the same. A report "
      "described this second method, so use whichever is easiest, but always put the sign and the unit, volts, in your answer.",
      refs=['ar21q2', 'ar22q1'], covers=['G12'], elements=[3]),
    S("A positive result means the reaction is spontaneous under standard conditions. A negative result means it is not, and the reverse reaction would be. "
      "Examiners accept an explanation using relative oxidising and reducing strengths as well as a positive cell potential, "
      "but a negative cell potential cannot support a spontaneous reaction.", refs=['ar23a', 'ar25q1'], covers=['R6', 'G12'], elements=[3]),
]),
Scene('we_predict', P2, 'Worked example: will it react?', Slide('worked', title='Worked example 3: predicting reactions', chip='Element 3 · series and data',
    q='Using the information sheet, decide whether each mixture reacts under standard conditions: (a) copper metal in silver nitrate solution; (b) copper metal in 1 mol L⁻¹ hydrochloric acid; (c) iron(III) ions with bromide ions.',
    rows=[dict(s=0, t='(a)  Ag⁺ (0.80 V) oxidiser,  Cu reducer (0.34 V):    E°cell = 0.80 − 0.34 = +0.46 V', col='#eef2f8'),
          dict(s=0, t='`2Ag^+(aq) + Cu(s) -> 2Ag(s) + Cu^2+(aq)`   spontaneous: silver deposits, solution turns blue', col='#9bde7e', size=23),
          dict(s=1, t='(b)  H⁺ (0.00 V) oxidiser,  Cu reducer (0.34 V):    E°cell = 0.00 − 0.34 = −0.34 V', col='#eef2f8'),
          dict(s=1, t='not spontaneous: copper does not dissolve in dilute hydrochloric acid', col='#9bde7e', size=23),
          dict(s=2, t='(c)  Fe³⁺ (0.77 V) oxidiser,  Br⁻ reducer (Br₂ 1.09 V):    E°cell = 0.77 − 1.09 = −0.32 V', col='#eef2f8'),
          dict(s=2, t='not spontaneous: Fe³⁺ is not strong enough to oxidise Br⁻', col='#9bde7e', size=23),
          dict(s=2, t='Spontaneous reaction questions: do not use the words anode or cathode.', col='#f15bb5', size=22)]), [
    S("Worked example three. First, copper in silver nitrate. Silver ions are the oxidiser at zero point eight zero volts and "
      "copper is the reducer at zero point three four. The cell potential is plus zero point four six volts, so it is "
      "spontaneous. You would see silver coat the copper and the solution turn blue.",
      refs=['info_srp', 'ex25q1', 'ex23q3', 'ex21q3'], covers=['R6', 'R14'], elements=[2, 3], exam=['X25-1', 'X23-3', 'X21-3'],
      problem='Will Cu(s) react with 1.0 mol L⁻¹ AgNO₃(aq) under standard conditions? Find E°cell.'),
    S("Second, copper in dilute hydrochloric acid. Hydrogen ions are at zero. The cell potential is zero minus zero point "
      "three four, negative, so copper does not dissolve in this acid. Copper sits below hydrogen in reactivity.",
      refs=['info_srp'], covers=['R6'], elements=[2, 3], problem='Will Cu(s) react with 1.0 mol L⁻¹ hydrochloric acid? Find E°cell.'),
    S("Third, iron three plus with bromide ions. Iron three plus is at zero point seven seven, but bromine is at one point "
      "zero nine, so iron three plus is too weak to oxidise bromide. No reaction. In a question like this, which is about a "
      "reaction and not a cell, never name an anode or a cathode.", refs=['info_srp', 'ar25q1', 'ex21q3'], covers=['R6'],
      elements=[2, 3], exam=['X25-1', 'X21-3'], problem='Will Fe³⁺(aq) oxidise Br⁻(aq) under standard conditions? Find E°cell.'),
]),
Scene('we_multi', P2, 'More than two species', Slide('worked', title='Worked example 4: several species', chip='Element 3 · series and data',
    q='Excess magnesium powder is added to a solution containing 1 mol L⁻¹ copper(II) ions and 1 mol L⁻¹ zinc ions. Predict what happens and in which order.',
    rows=[dict(s=0, t='Oxidisers present:  Cu²⁺ (+0.34 V),   Zn²⁺ (−0.76 V),   (H₂O: −0.83 V)', col='#eef2f8'),
          dict(s=0, t='Reducer:  Mg (Mg²⁺ is −2.38 V, lower than all of them)', col='#eef2f8'),
          dict(s=1, t='Strongest oxidiser reacts first:  Cu²⁺ + Mg:   E°cell = 0.34 + 2.38 = +2.72 V', col='#ffd166'),
          dict(s=1, t='`Cu^2+(aq) + Mg(s) -> Cu(s) + Mg^2+(aq)`   blue fades, brown copper forms', col='#9bde7e', size=23),
          dict(s=2, t='Then Zn²⁺ + Mg:   E°cell = −0.76 + 2.38 = +1.62 V', col='#ffd166'),
          dict(s=2, t='`Zn^2+(aq) + Mg(s) -> Zn(s) + Mg^2+(aq)`   grey zinc forms', col='#9bde7e', size=23),
          dict(s=3, t='Mg²⁺ is the product, so nothing further: the strongest reducer has finished.', col='#b3c0d4', size=23)]), [
    S("Worked example four has more than two species. Magnesium powder is added to a mixture of copper two plus and zinc two plus. "
      "List the oxidisers: copper ions at plus zero point three four, zinc ions at minus zero point seven six. "
      "Magnesium is the reducer, and its ions sit at the bottom, at minus two point three eight.",
      refs=['info_srp', 'ex23q3'], covers=['R6', 'R14'], elements=[3], exam=['X23-3'],
      problem='Excess Mg is added to Cu²⁺(aq) and Zn²⁺(aq), each 1 mol L⁻¹. What happens, and in what order?'),
    S("The strongest oxidiser reacts first. Copper ions are stronger, so they react first, with a cell potential of two point "
      "seven two volts. The blue colour fades and brown copper forms.", refs=['info_srp'], covers=['R6'], elements=[3]),
    S("Magnesium is in excess, so it carries on and reacts with the zinc ions, with a cell potential of one point six two volts. Grey "
      "zinc forms. Whenever a reducer is in excess, keep going down the table, as with zinc in iron three plus, where the iron "
      "three plus goes first to iron two plus, and later to iron metal.", refs=['info_srp', 'ar23q3'], covers=['R6'],
      elements=[3], exam=['X23-3']),
    S("Finally, magnesium ions are the product, and nothing in the mixture is a stronger reducer than magnesium metal. "
      "So the process stops. For an A, say it in terms of strengths: the strongest oxidiser meets the strongest reducer "
      "first, then the next.", refs=['info_srp'], covers=['R6', 'R14'], elements=[3, 1]),
]),
Scene('we_order', P2, 'Working out the series from experiments', Slide('worked', title='Worked example 5: from experiments to the series', chip='Element 3 · series and data',
    q='Metals X, Y and Z, each as 1 mol L⁻¹ solutions of their 2+ ions. Test 1: Z metal dissolves in a solution of Y²⁺, and Y metal forms. Test 2: a cell with X and Z has X as the anode. Test 3: only X reacts with dilute hydrochloric acid. Put the half-equations in series order, with hydrogen.',
    rows=[dict(s=0, t='Test 3: X reacts with H⁺, so X²⁺|X is BELOW 2H⁺|H₂.   Y and Z do not: they are above.', col='#eef2f8', size=23),
          dict(s=1, t='Test 1: Z reduces Y²⁺, so Y²⁺ is the stronger oxidiser: Y²⁺|Y is above Z²⁺|Z', col='#eef2f8', size=23),
          dict(s=1, t='Test 2: the anode is the stronger reducer: X is below Z   (consistent)', col='#eef2f8', size=23),
          dict(s=2, t='Y²⁺ + 2e⁻ ⇌ Y          strongest oxidiser (top)', col='#ffd166'),
          dict(s=2, t='2H⁺ + 2e⁻ ⇌ H₂', col='#ffd166'),
          dict(s=2, t='Z²⁺ + 2e⁻ ⇌ Z', col='#ffd166'),
          dict(s=2, t='X²⁺ + 2e⁻ ⇌ X          strongest reducer (bottom)', col='#ffd166'),
          dict(s=3, t='Cell shorthand for test 2:   `X(s)|X^2+(aq) || Z^2+(aq)|Z(s)`', col='#9bde7e')]), [
    S("Worked example five turns experiments into a series. Metals X, Y and Z are tested. Test three: only X reacts with "
      "dilute acid, so X is a stronger reducer than hydrogen, and sits below hydrogen. Y and Z do not react, so they sit above it. "
      "Always include the hydrogen half-equation as a reference.", refs=['ex21q3', 'ar21q3', 'content'], covers=['R6', 'R14', 'G10'],
      elements=[3], exam=['X21-3'],
      problem='From three experiments on metals X, Y and Z, place their half-equations and the H⁺|H₂ half-equation in series order.'),
    S("Test one: Z metal reduces Y two plus, so Y two plus is the stronger oxidiser and is higher. Test two: in a cell, the anode "
      "is the stronger reducer, so X is below Z. This agrees with the other tests.", refs=['ar21q3'], covers=['R14', 'G11'],
      elements=[3, 4], exam=['X21-3']),
    S("Write the half-equations as reductions, with equilibrium arrows, strongest oxidiser at the top: Y, hydrogen, Z, then X. "
      "A report encouraged students to say if the list is in increasing or decreasing oxidising strength.",
      refs=['ar21q3'], covers=['R14'], elements=[3], exam=['X21-3']),
    S("The cell for test two, written with the anode on the left, is X solid, X two plus, a double line, Z two plus, Z solid. "
      "Include state symbols, and leave out spectator ions.", refs=['ar21q3'], covers=['G6', 'G7'], elements=[3, 4], exam=['X21-3']),
]),
Scene('variations', P2, 'Why real results can differ', V.variations, [
    S("A-standard answers can say why observed results sometimes differ from prediction. The series assumes standard "
      "conditions. If concentrations are different, the potentials shift, so a weak oxidiser that is dilute becomes weaker still.",
      refs=['standards', 'content'], covers=['R14'], elements=[3]),
    S("A reaction that is spontaneous can still be so slow that nothing is seen, because of activation energy. Aluminium is a strong "
      "reducer, but its oxide layer stops it reacting. And producing a gas at an electrode may need more voltage than the table "
      "suggests. The table is a good guide, but not a guarantee.", refs=['standards', 'content'], covers=['R6', 'R14'], elements=[3, 1]),
]),

# ------------------------------------------------------------------ Part 3
Scene('galvanic', P3, 'A galvanic cell', V.galvanic, [
    S("A galvanic cell turns the energy of a spontaneous redox reaction into electrical energy. Each half-cell has an electrode "
      "in an electrolyte, a solution of ions. Here, a zinc electrode is in zinc sulfate, and a copper electrode is in copper sulfate. "
      "Everything inside the solutions and the salt bridge is the internal circuit. The wire is the external circuit.",
      refs=['content', 'info_srp'], covers=['G1', 'G2', 'G5'], elements=[4]),
    S("Zinc is the stronger reducer, so it is oxidised. Oxidation happens at the anode, so zinc is the anode. Copper ions are "
      "reduced at the cathode. In a galvanic cell the anode is negative and the cathode is positive. Write the half-equation "
      "at each electrode, and label them.", refs=['content', 'ex23q2', 'ex25q3'], covers=['G1', 'G11', 'G5'], elements=[4],
      exam=['X23-2', 'X25-3']),
    S("Electrons leave the anode and flow through the external circuit to the cathode. Draw them moving along the wire, "
      "not through the air or the solution. Draw the label lines for anode and cathode so that they touch the electrode.",
      refs=['content', 'ar25q3'], covers=['G3', 'G2'], elements=[4], exam=['X25-3'], anim=2),
    S("Inside the cell, ions carry the current. Anions move towards the anode, and cations move towards the cathode, "
      "through the salt bridge. Name the actual ions that move, such as nitrate and potassium, not just cations and anions. "
      "That earns marks that a general label does not.", refs=['content', 'ar22q1', 'ex22q1', 'ex21q2'], covers=['G3', 'G4'],
      elements=[4], exam=['X22-1', 'X21-2'], anim=2),
    S("Under standard conditions the voltmeter reads the cell potential: copper's zero point three four, minus zinc's "
      "minus zero point seven six, is one point one zero volts. The spontaneous redox reaction supplies the energy. "
      "Draw the diagram large, label everything, and include only species that are really there.",
      refs=['info_srp', 'content', 'ar24q3'], covers=['G5', 'G12', 'G2'], elements=[4, 2], exam=['X24-3', 'X21-2'], anim=2),
]),
Scene('salt_bridge', P3, 'The salt bridge', Slide('cards', title='What a salt bridge does', chip='Element 4 · cell diagrams', cols=2, counts=[1, 2, 3, 4], size=21, cards=[
    ('Completes the circuit', 'Ions flowing through the bridge carry charge in the internal circuit,\nso electrons can flow in the wire.', '#a78bfa'),
    ('Keeps electroneutrality', 'Without it, the anode half-cell gains positive ions and the cathode\nhalf-cell loses them, and the flow stops almost at once.', '#38bdf8'),
    ('Choose the solution carefully', 'Soluble, unreactive ions: KNO₃ or Na₂SO₄. Not an ion that forms\na precipitate with the cell’s ions (BaCl₂ with sulfate).', '#f15bb5'),
    ('Must contain ions', 'Ethanol solution has no ions to carry charge, so it is\nunsuitable. A porous barrier does the same job.', '#9bde7e')]), [
    S("The salt bridge does two main jobs. First, it completes the circuit, because ions in the bridge carry charge through the "
      "internal circuit. Second, it keeps each half-cell electrically neutral, by letting anions and cations move, which is "
      "called maintaining electroneutrality. The same is done by a porous barrier.", refs=['content', 'ex24q3', 'ar24q3'],
      covers=['G4', 'G1'], elements=[4], exam=['X24-3']),
    S("Without it, positive ions would build up where oxidation makes them, and negative charge would build up where "
      "they are used, so the flow would stop almost straight away.", refs=['content', 'ar24q3'], covers=['G4'], elements=[4]),
    S("Choosing the solution is a favourite question. It must be soluble, with ions that do not react with the cell's ions. "
      "Barium chloride in a sulfate cell forms a barium sulfate precipitate, which blocks the movement. Potassium nitrate is "
      "a good choice.", refs=['ex21q2', 'ar21q2', 'ex23q2', 'ar23q2'], covers=['G4'], elements=[4], exam=['X21-2', 'X23-2']),
    S("Ethanol solution is unsuitable too, because it contains no ions at all, so no charge can flow. If you give a reason, "
      "mention the absence of ions. A choice with no reason scores no marks.", refs=['ar21q2'], covers=['G4'], elements=[4], exam=['X21-2']),
]),
Scene('shorthand', P3, 'Cell shorthand', Slide('eqs', title='Chemical shorthand for cells', chip='Element 4 · cell diagrams', counts=[1, 2, 3], gap=0.15, size=30, nx=0.06, items=[
    ('eq', '`Zn(s)|Zn^2+(aq) || Cu^2+(aq)|Cu(s)`', ''),
    ('eq', '`Pt(s)|Sn^2+(aq),Sn^4+(aq) || Ag^+(aq)|Ag(s)`', ''),
    ('eq', '`Pt(s)|H2(g)|H^+(aq) || Cu^2+(aq)|Cu(s)`', '')],
    side=['Anode on the LEFT, cathode on the RIGHT', 'Single line | = a phase boundary', 'Double line || = the salt bridge',
          'Include state symbols; leave out spectator ions', 'An inert electrode (Pt) goes at the outside edge'], side_counts=[0, 3, 5]), [
    S("Chemists write a cell in shorthand. The anode half-cell goes on the left, and the cathode on the right. A single line "
      "is a boundary between phases, and a double line is the salt bridge. The zinc copper cell is zinc solid, zinc two plus, "
      "double line, copper two plus, copper solid.", refs=['content', 'ar21q3'], covers=['G6', 'G7'], elements=[4], exam=['X21-3']),
    S("When the half-cell has no solid metal, as with tin two plus and tin four plus, use an inert electrode, "
      "such as platinum. Both ions go in the same section, separated by a comma, and the platinum goes at the outer end.",
      refs=['content', 'ar21q3'], covers=['G6', 'G8'], elements=[4], exam=['X21-3']),
    S("The hydrogen half-cell is platinum, hydrogen gas, hydrogen ions. Include the state symbols. Spectator ions "
      "are left out, and so, a report said, the species are in a well structured order.", refs=['ar21q3', 'content'], covers=['G6'],
      elements=[4], exam=['X21-3']),
]),
Scene('inert_cell', P3, 'A cell with an inert electrode', V.inert_cell, [
    S("Not every cell has a metal in a solution of its own ions. This one has a platinum rod in a solution of tin two plus and "
      "tin four plus ions, joined to a silver electrode in silver nitrate. Platinum is inert: it only carries electrons.",
      refs=['content', 'ex22q1', 'ex23q2'], covers=['G8', 'G2'], elements=[4], exam=['X22-1', 'X23-2'],
      problem='Draw the cell with a Pt rod in Sn²⁺ and Sn⁴⁺ and an Ag electrode in AgNO₃(aq), and find E°cell.'),
    S("Silver ions are the stronger oxidiser, at zero point eight zero volts, so silver is the cathode. Tin two plus is "
      "oxidised to tin four plus at the platinum, the anode. Draw the polarities, the half-equations, and the arrows.",
      refs=['info_srp', 'content', 'ar22q1'], covers=['G8', 'G11', 'G2'], elements=[4, 2], exam=['X22-1']),
    S("Electrons flow from platinum to silver, nitrate moves towards the anode, and sodium moves towards the cathode. The "
      "cell potential is zero point eight zero minus zero point one five, which is zero point six five volts.",
      refs=['info_srp', 'ar22q1'], covers=['G3', 'G12'], elements=[4, 2], exam=['X22-1']),
]),
Scene('we_missing', P3, 'Cell potentials: working backwards', Slide('worked', title='Worked example 6: one half-cell unknown', chip='Element 2 · calculations',
    q='A cell has an EMF of 2.10 V. Its cathode half-reaction has E° = +1.20 V. Find E° (as a reduction) for the anode half-reaction. Then, if the same anode is swapped to the cell with the Pt|Fe²⁺,Fe³⁺ half-cell (0.77 V) as the cathode, what is the new EMF?',
    rows=[dict(s=0, t='E°cell = E°(cathode, reduction) − E°(anode, reduction)', col='#ffd166'),
          dict(s=0, t='2.10 = 1.20 − E°(anode)    so    E°(anode) = 1.20 − 2.10 = −0.90 V', col='#9bde7e'),
          dict(s=1, t='New cell:  E°cell = 0.77 − (−0.90) = +1.67 V', col='#9bde7e'),
          dict(s=1, t='Check the logic: the anode is the SAME stronger reducer, the cathode is a weaker oxidiser, so a smaller EMF.', col='#b3c0d4', size=23),
          dict(s=2, t='Anode reduction potential comes from the information sheet table where possible.', col='#b3c0d4', size=23),
          dict(s=2, t='Units: volts, and the sign matters.', col='#f15bb5', size=23)]), [
    S("Sometimes the cell potential is given and a half-cell is missing. A cell has an EMF of two point one zero volts, "
      "and its cathode is plus one point two zero. The EMF equals the cathode value minus the anode value, so the anode's "
      "reduction potential is one point two minus two point one, which is minus zero point nine volts.",
      refs=['ex24q3', 'ar24q3', 'ex25q3', 'ar25q3', 'content'], covers=['G12', 'R14'], elements=[2, 4], exam=['X24-3', 'X25-3'],
      problem='A cell has EMF 2.10 V and a cathode with E° = +1.20 V. What is E° (as reduction) of the anode half-reaction?'),
    S("Use the same anode with a different cathode of zero point seven seven volts, and the EMF is one point six seven. "
      "In the lithium cell question, many students used the wrong half-equation, so check which reaction on the sheet "
      "is the one in the cell, and whether the question asks for a reduction or oxidation value. Include volts, with a sign.",
      refs=['ar25q3', 'ar24q3'], covers=['G12'], elements=[2, 4], exam=['X25-3', 'X24-3'],
      problem='The same anode is joined to a cathode of E° = +0.77 V. What is the new cell EMF?'),
    S("Finally, whichever value you use, take it from the standard reduction table when you can. Then check that your "
      "answer makes physical sense: the strongest reducer is always the anode.", refs=['info_srp'], covers=['G12', 'G11'], elements=[2, 4]),
]),
Scene('nonstandard', P3, 'Non-standard conditions', Slide('cards', title='Non-standard cells', chip='Element 3 · series and data', cols=2, counts=[1, 2, 3, 4], size=21, cards=[
    ('Different concentrations', 'The same metal in two different concentrations of its ions:\nthe E° cell is 0 V only at EQUAL concentrations.', '#38bdf8'),
    ('Which side is the anode?', 'The half-cell with the lower [Cu²⁺] is the anode: it has the\nweaker oxidiser, so copper is oxidised there. Cell Q is the cathode.', '#a78bfa'),
    ('Why the voltage drops to zero', 'Oxidation raises one concentration, reduction lowers the other,\nuntil they are equal: equilibrium, EMF = 0 V. Not “the electrode ran out”.', '#9bde7e'),
    ('Replacing an electrode', 'Cu replaced by Ag in the Cu²⁺ half-cell: E°cell (Ag|Ag⁺ vs Cu|Cu²⁺)\nwould be reversed, so the cell would not run as written.', '#f15bb5')]), [
    S("Now cells that are not at standard conditions. Two copper half-cells with different concentrations make a cell, because "
      "the concentrations are different. At equal concentrations the EMF would be zero.", refs=['ex21q2', 'ar21q2', 'content'],
      covers=['G12', 'G11'], elements=[3, 4], exam=['X21-2']),
    S("The half-cell with the lower concentration of copper ions has the weaker oxidiser, so copper metal is oxidised "
      "there and it is the anode. The other half-cell is the cathode. Its electrode does not have a potential of plus zero point "
      "three four, because the solution is not one mole per litre.", refs=['ar21q2'], covers=['G11', 'R14'], elements=[3, 4], exam=['X21-2']),
    S("Over time the EMF falls to zero. Oxidation raises the concentration in one half-cell and reduction lowers the other, "
      "until they are equal and the cell reaches equilibrium. Do not say the electrode has been used up: examiners gave no marks "
      "for that, and many students thought one electrode would fully oxidise.", refs=['ar21q2'], covers=['G5', 'G12'], elements=[3, 4], exam=['X21-2']),
    S("If one copper electrode is replaced by silver, silver ions do not exist there, and copper ions are not a strong enough "
      "oxidiser to make silver the anode. So the cell would not operate as before. Again, remember that metal ions are "
      "oxidisers and metals are reducers.", refs=['ar21q2'], covers=['R6', 'G11'], elements=[3, 4], exam=['X21-2']),
]),
Scene('lead_acid', P3, 'A cell with one electrolyte', V.lead_acid, [
    S("The lead acid battery in a car is a set of galvanic cells. Each has a lead anode and a lead dioxide cathode in the same "
      "sulfuric acid. That one shared electrolyte is why no salt bridge is needed: ions can move straight between the "
      "electrodes. It is not an electrolytic cell, and does not need a porous barrier.",
      refs=['ex24q3', 'ar24q3', 'content'], covers=['G2', 'G4', 'G5', 'A3'], elements=[4], exam=['X24-3'], anim=2),
    S("When you draw it, label the anode and cathode with their materials and polarity. Show electron flow in the wire, "
      "and show the hydrogen sulfate and hydrogen ions moving in the acid. Do not draw species that are not in the cell, such as "
      "lead ions or oxide ions. Use the space you have: some students drew cells too small to read. "
      "Six cells in series add up to about thirteen and a half volts.",
      refs=['ar24q3'], covers=['G2', 'G3', 'A3'], elements=[4], exam=['X24-3'], anim=2),
]),
Scene('batteries', P3, 'Cells in everyday life', Slide('cards', title='Galvanic cells you use', chip='Context · fuel cells and batteries', cols=2, counts=[1, 2, 3, 4], size=21, cards=[
    ('Dry and alkaline cells', 'Zinc is the anode, manganese dioxide the cathode.\nThe paste electrolyte replaces a liquid salt bridge.', '#a78bfa'),
    ('Lead-acid (wet) cells', 'Car batteries: rechargeable. Discharge is galvanic;\ncharging runs the reaction backwards by electrolysis.', '#38bdf8'),
    ('Lithium-ion', 'Li ⇄ Li⁺ moves between electrodes; a porous polymer\nmembrane keeps the half-cells apart but lets ions pass.', '#9bde7e'),
    ('Fuel cells', 'H₂ is oxidised at one electrode, O₂ reduced at the other,\nfed continuously: H₂ + ½O₂ → H₂O. A cleaner energy source.', '#f9a03f')]), [
    S("Galvanic cells power everyday devices. In dry and alkaline cells, zinc is the anode, and a paste of electrolyte replaces "
      "the salt bridge. In a car's wet cell, the lead acid battery can be recharged, by running the reaction backwards "
      "using a power supply, which is electrolysis.", refs=['appendix', 'content'], covers=['A3', 'G5'], elements=[1]),
    S("In a lithium ion cell, lithium ions move through the electrolyte, and a porous polymer membrane separates the two half-cells "
      "while letting ions pass. Its purpose is to keep the electrolytes from mixing and to complete the circuit by allowing "
      "ion movement. Any one valid purpose earns the mark, but the words salt bridge alone did not.",
      refs=['ex25q3', 'ar25q3', 'appendix'], covers=['A3', 'G4'], elements=[1, 4], exam=['X25-3']),
    S("A fuel cell is a galvanic cell that uses up a fuel, such as hydrogen, fed in continuously. Hydrogen is oxidised at "
      "the anode, and oxygen is reduced at the cathode, with only water as the product. Fuel cells were first demonstrated "
      "in the eighteen forties, and now power buses, boats, trains and cars.", refs=['appendix'], covers=['A3'], elements=[1]),
    S("The breathalyser context is redox as well. In an alcohol sensor, ethanol is oxidised at platinum electrodes, and the "
      "electrical signal it produces measures the blood alcohol level. Older tests used acidified dichromate, whose colour changes "
      "from orange to green, as chromium three plus forms.", refs=['appendix', 'info_srp'], covers=['A2'], elements=[1]),
]),

# ------------------------------------------------------------------ Part 4
Scene('galv_vs_elec', P4, 'Galvanic against electrolytic cells', Slide('table', title='Galvanic and electrolytic cells compared', chip='Element 1 · principles',
    head=['', 'Galvanic', 'Electrolytic'], widths=[0.22, 0.34, 0.34], size=24, counts=[1, 2, 3, 4, 5], rows=[
        ['Energy', 'Spontaneous reaction PRODUCES electrical energy', 'Needs electrical energy to drive a non-spontaneous reaction'],
        ['Anode', 'Oxidation, negative (−)', 'Oxidation, positive (+)'],
        ['Cathode', 'Reduction, positive (+)', 'Reduction, negative (−)'],
        ['E°cell', 'Positive', 'Negative: the supply must exceed it'],
        ['Used for', 'Batteries, fuel cells, sensors', 'Extracting metals, plating, refining, making chemicals']]), [
    S("Now electrolytic cells. The key difference between the two kinds of cell is energy. A galvanic cell produces electrical energy "
      "from a spontaneous reaction. An electrolytic cell uses electrical energy from an external supply to force a non-spontaneous "
      "reaction. To get the mark, compare the two.", refs=['content', 'ex22q3', 'ar22q3'], covers=['E1', 'G5'], elements=[1],
      exam=['X22-3']),
    S("In both, oxidation happens at the anode and reduction at the cathode. But the polarities swap. In an electrolytic cell "
      "the anode is positive and the cathode is negative, because the supply pulls electrons off the anode and pushes them "
      "onto the cathode.", refs=['content'], covers=['E1', 'G11'], elements=[1, 4]),
    S("The calculated cell potential is negative, meaning the reaction is not spontaneous. The supply must provide at least "
      "that many volts. Many students forgot to say that it is the minimum voltage.", refs=['ar24q4', 'ex24q4'],
      covers=['E1', 'G12'], elements=[1, 2], exam=['X24-4']),
    S("Electrolysis is used on the industrial scale: aluminium and zinc are both produced in Tasmania this way, as are "
      "chlorine and sodium hydroxide from brine. It is also used at small scales: electroplating a key, or refining copper.",
      refs=['content', 'ex21q5', 'ex22q4'], covers=['E1'], elements=[1], exam=['X21-5', 'X22-4']),
    S("To build an electrolytic cell you need: a power supply, two electrodes, an electrolyte, which can be a melt or a "
      "solution, and a wire. Inert electrodes such as graphite or platinum only carry electrons. Do not forget the power supply, "
      "and draw its symbol the right way round.", refs=['ar24q4', 'content'], covers=['G9', 'E1'], elements=[4], exam=['X24-4']),
]),
Scene('electrolytic', P4, 'Molten salts', V.electrolytic, [
    S("Start with a molten salt. Molten lead two bromide contains only lead ions and bromide ions, nothing else. The "
      "power supply makes the left electrode positive, the anode, and the right electrode negative, the cathode.",
      refs=['content', 'info_srp', 'ex24q4'], covers=['E2', 'G9', 'G2'], elements=[4], exam=['X24-4'],
      problem='What are the products of electrolysing molten lead(II) bromide with graphite electrodes, and what is the minimum voltage?'),
    S("Electrons travel from the anode, through the supply, to the cathode. Oxidation is still at the anode and reduction at "
      "the cathode. Remember it as An Ox, Red Cat.", refs=['ar24q4'], covers=['E2', 'G3'], elements=[4], exam=['X24-4'], anim=2),
    S("Inside, cations move to the cathode, anions to the anode. The ions in a melt are state liquid, not aqueous. "
      "Writing aqueous in a molten salt loses marks.", refs=['ar24q4'], covers=['E2', 'G3'], elements=[4], exam=['X24-4'], anim=2),
    S("At the cathode, lead ions gain electrons to give liquid lead. At the anode, bromide ions give up electrons to make "
      "bromine. Adding the two potentials, minus one point oh nine and minus zero point one three, gives a cell potential of minus one "
      "point two two volts, so the supply needs more than that. Molten magnesium chloride works in the same way. If "
      "the anodes are steel, iron is oxidised first, not chloride, because iron is the stronger reducer.",
      refs=['info_srp', 'ex24q4', 'ar24q4', 'ex22q4'], covers=['E2', 'E1'], elements=[4, 2], exam=['X24-4', 'X22-4'], anim=2),
]),
Scene('aq_rules', P4, 'Aqueous solutions: who wins?', Slide('table', title='Predicting electrolysis products', chip='Element 3 · series and data',
    head=['Where', 'Candidates', 'Rule'], widths=[0.16, 0.34, 0.40], size=23, counts=[1, 2, 3, 4, 5], rows=[
        ['Cathode (−)', 'metal ions, H⁺ or H₂O', 'Strongest OXIDISER is reduced. Na⁺, K⁺, Ca²⁺, Mg²⁺, Al³⁺ lose to water: H₂ forms'],
        ['Anode (+)', 'anions, H₂O, or the electrode', 'Strongest REDUCER is oxidised'],
        ['Cannot be oxidised', 'SO₄²⁻, NO₃⁻, CO₃²⁻, PO₄³⁻ …', 'Elements already at maximum oxidation state: water is oxidised instead, giving O₂ + H⁺'],
        ['Concentration', 'Cl⁻ in brine, dilute NaCl', 'Concentrated NaCl: Cl₂. Dilute: O₂ (the series’ ranking)'],
        ['Electrode', 'inert (Pt, graphite) or active (Cu)', 'An active metal anode can be oxidised itself']]), [
    S("For aqueous solutions, water is always present, so there is competition. At the cathode, the strongest oxidiser is "
      "reduced. Sodium, potassium, calcium, magnesium and aluminium ions are all weaker oxidisers than water, so water is "
      "reduced instead, giving hydrogen gas and hydroxide ions. A common mistake was reducing sodium ions in solution.",
      refs=['content', 'info_srp', 'ar22q4', 'ex21q5', 'ex22q3'], covers=['E3', 'E6'], elements=[3], exam=['X21-5', 'X22-3', 'X22-4']),
    S("At the anode, the strongest reducer is oxidised. The candidates are the anions, water, and the electrode itself if "
      "it is not inert.", refs=['content', 'ar24q4'], covers=['E3', 'E6'], elements=[3], exam=['X24-4']),
    S("Anions whose central element is already at its maximum oxidation state, such as sulfate, nitrate, carbonate and "
      "phosphate, cannot be oxidised any further. So at the anode, water is oxidised instead, giving oxygen and hydrogen ions.",
      refs=['content', 'info_srp'], covers=['E4', 'E3'], elements=[3], exam=['X24-4']),
    S("Concentration matters, which is the competing reactions idea. In concentrated sodium chloride, chloride is oxidised "
      "and chlorine forms. In a dilute or half molar solution, water is oxidised instead, and oxygen forms, as the exam "
      "convention goes. The table is a guide for standard conditions only, and that is its limitation.",
      refs=['content', 'ar23q5', 'ar22q4'], covers=['E5', 'E6'], elements=[3, 1], exam=['X23-5', 'X22-4']),
    S("With a reactive electrode, such as copper, the electrode can itself be the strongest reducer. A copper anode "
      "is oxidised to copper two plus, which turns the solution blue, while the cathode still reduces whatever is the "
      "strongest oxidiser.", refs=['content', 'ar23q5', 'ex23q5'], covers=['E3'], elements=[3, 4], exam=['X23-5']),
]),
Scene('conc_note', P4, 'A marking note on concentration', Slide('cards', title='Chloride or water at the anode?', chip='Marking note', cols=1, h=0.58, size=24, cards=[
    ('What the papers do', 'Concentrated NaCl (brine) with inert electrodes: chlorine at the anode (2022, 2023).\nA 0.5 mol L⁻¹ solution: oxygen (2023). In 2025 a 1.0 mol L⁻¹ solution was marked as oxygen.\nSo follow the series: only call it chlorine when the question says concentrated.', '#fb923c'),
    ('What real chemistry does', 'Oxygen is hard to make at an electrode (overpotential), so even 1 mol L⁻¹ chloride\nmostly gives chlorine in practice. The exam convention is a simplification:\nuse it, and state your reasoning from the E° values.', '#f15bb5')],
    note='Marking convention differs from industrial practice: follow the question’s wording, and give half-equations.'), [
    S("A marking note. Past papers treat sodium chloride like this. Concentrated sodium chloride, with inert electrodes, gives "
      "chlorine at the anode. A half molar solution gave oxygen in two thousand and twenty three, and in two thousand and twenty five, a "
      "one molar solution was marked with oxygen as well. So only name chlorine when the question says concentrated.",
      refs=['ar22q4', 'ar23q5', 'ar25q4', 'ex25q4'], covers=['E5', 'E6'], elements=[3, 1], exam=['X25-4', 'X23-5']),
    S("In real chemistry, making oxygen at an electrode needs extra voltage, called overpotential, so even one molar chloride "
      "gives mostly chlorine in practice. That is a disagreement between the exam convention and industry. Follow "
      "the question's wording, and always show your half-equations and your reasoning from the series.",
      refs=['ar25q4'], covers=['E6'], elements=[3, 1], exam=['X25-4']),
]),
Scene('we_elec', P4, 'Worked example: electrolysis products', Slide('worked', title='Worked example 7: aqueous electrolysis', chip='Element 3 · series and data',
    q='Predict the products, with half-equations, when 1 mol L⁻¹ potassium iodide solution is electrolysed using platinum electrodes. Find the minimum voltage.',
    rows=[dict(s=0, t='Species: K⁺, I⁻, H₂O.   Cathode: K⁺ (−2.92 V) or H₂O (−0.83 V)?', col='#eef2f8'),
          dict(s=0, t='Water is the stronger oxidiser:  `2H2O(l) + 2e^- -> 2OH^-(aq) + H2(g)`', col='#ffd166'),
          dict(s=1, t='Anode: I⁻ (I₂/I⁻ 0.54 V) or H₂O (O₂/H₂O 1.23 V)?  Lower E° = stronger reducer: I⁻', col='#eef2f8'),
          dict(s=1, t='`2I^-(aq) -> I2(s) + 2e^-`', col='#ffd166'),
          dict(s=2, t='Net:  `2I^-(aq) + 2H2O(l) -> I2(s) + H2(g) + 2OH^-(aq)`', col='#9bde7e'),
          dict(s=2, t='Observe: bubbles at the cathode; brown colour at the anode; the solution turns alkaline.', col='#b3c0d4', size=23),
          dict(s=3, t='Minimum voltage:  E°cell = −0.83 − 0.54 = −1.37 V,  so more than 1.37 V.', col='#9bde7e')]), [
    S("Worked example seven. A potassium iodide solution is electrolysed with platinum electrodes. Present: potassium ions, "
      "iodide ions and water. At the cathode, potassium is at minus two point nine two volts, water at minus zero point eight three. Water is the "
      "stronger oxidiser, so hydrogen gas and hydroxide ions form.",
      refs=['info_srp', 'content'], covers=['E3', 'E6'], elements=[3, 4],
      problem='What are the products of electrolysing 1 mol L⁻¹ KI(aq) with Pt electrodes? Give half-equations and the minimum voltage.'),
    S("At the anode, iodine is at zero point five four volts, and oxygen from water is at one point two three. The lower value "
      "is the stronger reducer, so iodide is oxidised, making iodine.", refs=['info_srp'], covers=['E3', 'E6'], elements=[3, 4]),
    S("Add the halves for the net equation. Observations are things you can see: bubbles of gas at the cathode and a brown "
      "colour at the anode. A pop test, or a pH test, is not an observation. Say what you see, not what you suspect.",
      refs=['ar25q4'], covers=['E3'], elements=[3, 4], exam=['X25-4']),
    S("The minimum voltage is the cell potential, minus zero point eight three, minus zero point five four, which is "
      "minus one point three seven. The supply must be above one point three seven volts. When there are two ions that can "
      "be reduced, such as iron two plus in the mixture, check both: it can be oxidised or reduced, because it appears on "
      "the table on both sides.", refs=['info_srp', 'ar25q4', 'ar24q4'], covers=['E6', 'E3', 'G12'], elements=[3, 2], exam=['X25-4', 'X24-4']),
]),
Scene('refine_plate', P4, 'Refining and plating', V.plating, [
    S("Electroplating coats an object with a thin layer of metal. Here, a steel key is the cathode, a nickel bar is the anode, and the "
      "electrolyte is nickel sulfate. Nickel is oxidised at the anode and deposits at the cathode. Include the power supply "
      "and the half-equations.", refs=['content', 'ex22q5', 'ar22q5'], covers=['E7b', 'E1'], elements=[4], exam=['X22-5']),
    S("Electrorefining uses the same idea to purify a metal. Impure copper is the anode, pure copper is the cathode, in copper sulfate. "
      "Copper dissolves from the anode, and pure copper plates on the cathode. Less reactive impurities fall to the bottom as sludge, and "
      "more reactive ones stay in solution.", refs=['content'], covers=['E7', 'E3'], elements=[4, 3]),
    S("A galvanised object has a zinc coating. The report did not accept sacrificial anode as the term for it. We will see "
      "in the corrosion part why zinc protects steel even when scratched.", refs=['ar22q5', 'ex22q5'], covers=['E7b', 'K11'], elements=[4, 5], exam=['X22-5']),
]),
Scene('we_faraday', P4, "Faraday's laws", Slide('worked', title='Worked example 8: how much metal?', chip='Element 2 · calculations',
    q='A steel key is nickel plated for 45.0 minutes using a steady current of 2.50 A. The cathode half-equation is Ni²⁺ + 2e⁻ → Ni. (a) What mass of nickel is deposited? (b) How long to deposit 5.00 g, if only 92.0% of the charge deposits nickel?',
    rows=[dict(s=0, t='n(e⁻) = It / F = 2.50 × (45.0 × 60) / 96 500 = 0.069948 mol', col='#ffd166'),
          dict(s=0, sf='= 0.0699 mol (3 s.f.)', t='n(Ni) = n(e⁻) / 2 = 0.034974 mol', col='#ffd166'),
          dict(s=1, t='m(Ni) = n × M = 0.034974 × 58.69 = 2.0527 g', col='#ffd166'),
          dict(s=1, sf='= 2.05 g (3 s.f.)', t='', col='#9bde7e', gap=0),
          dict(s=2, t='(b)  n(Ni) = 5.00 / 58.69 = 0.085193 mol,  so n(e⁻) = 0.17039 mol', col='#ffd166'),
          dict(s=2, t='t at 100% = n(e⁻)F / I = 0.17039 × 96 500 / 2.50 = 6577 s', col='#ffd166'),
          dict(s=3, t='Only 92.0% is useful, so the time is LONGER: DIVIDE by 0.920', col='#f15bb5'),
          dict(s=3, t='t = 6577 / 0.920 = 7149 s', col='#ffd166'),
          dict(s=3, sf='= 7.15 × 10³ s (3 s.f.), about 119 min', t='', col='#9bde7e', gap=0)]), [
    S("Faraday's laws link the amount of electricity to the amount of product. The information sheet, in the chemical "
      "information section, gives the amount of electrons as q over F, which is also current times time over F. F is "
      "Faraday's constant, ninety six thousand five hundred coulombs per mole, on the sheet's data page.",
      refs=['info', 'info_data', 'content'], covers=['E8'], elements=[2]),
    S("Worked example eight. Current two point five amps for forty five minutes is two thousand seven hundred seconds, so the "
      "electrons are zero point zero six nine nine mole. Two moles of electrons make one mole of nickel, so halve it. Multiply by the "
      "molar mass from the sheet's atomic mass table to get about two point oh five grams.",
      refs=['info', 'info_ar', 'ex25q5', 'ar25q5'], covers=['E8'], elements=[2], exam=['X25-5'],
      problem='A steady current of 2.50 A flows for 45.0 min depositing nickel (Ni²⁺ + 2e⁻ → Ni). What mass of Ni is deposited?'),
    S("Now work backwards. To deposit five grams, we need zero point one seven moles of electrons. That is a charge "
      "of sixteen thousand four hundred and forty three coulombs, and at two point five amps it takes six thousand five hundred "
      "and seventy seven seconds, if every electron made nickel.", refs=['info'], covers=['E8'], elements=[2], exam=['X25-5'],
      problem='How long at 2.50 A to deposit 5.00 g of nickel with 100% efficiency?'),
    S("But only ninety two percent of the charge made nickel. So it takes longer: divide by zero point nine two, giving about "
      "seven thousand one hundred and fifty seconds, or one hundred and nineteen minutes. In the 2025 exam, a large number of students "
      "multiplied by the yield and made it worse. Check: does your answer make sense? Include context and units.",
      refs=['ar25q5', 'ar25g', 'ex25q5'], covers=['E8'], elements=[2], exam=['X25-5'],
      problem='Only 92.0% of the charge deposits nickel. How long to deposit 5.00 g at 2.50 A?'),
    S("Part c of that question asked why a gas formed at the cathode. Water, with a potential of minus zero point eight three, "
      "is close to zinc ions at minus zero point seven six, so as the zinc concentration falls, some water is reduced, "
      "giving hydrogen. The gas does not come from the sulfate.", refs=['ar25q5', 'info_srp'], covers=['E5', 'E8', 'E6'], elements=[3, 2], exam=['X25-5']),
]),

# ------------------------------------------------------------------ Part 5
Scene('rust_props', P5, 'Steel and rust', Slide('table', title='Steel and rust compared', chip='Element 5 · corrosion',
    head=['', 'Steel', 'Rust'], widths=[0.20, 0.36, 0.36], size=24, counts=[1, 2, 3, 4], rows=[
        ['Bonding', 'Metallic: a lattice of ions in a sea of electrons', 'Ionic: Fe²⁺/Fe³⁺ with O²⁻ and OH⁻'],
        ['Conductivity', 'Conducts electricity (mobile electrons)', 'Does not conduct (ions locked in place)'],
        ['Strength', 'Strong, malleable, ductile', 'Brittle, flaky, crumbles'],
        ['Volume', 'Compact', 'Much larger for the same amount of iron: it pushes outwards']]), [
    S("First, the materials. Steel is mostly iron, with metallic bonding: positive ions in a sea of delocalised electrons. "
      "That is why steel conducts, is strong and can be shaped. Rust is iron oxide with water, and it has ionic bonding. "
      "Ions are locked in a lattice, so rust does not conduct, and it is brittle and flaky.", refs=['content', 'ar25q6'],
      covers=['K2', 'K3'], elements=[5], exam=['X25-6']),
    S("The volume of rust is much greater than the volume of the iron that made it. Iron atoms combine with oxygen and "
      "water, and the lattice of ions takes up more space. In a recent exam, cracked concrete around a steel pole was the evidence. "
      "Few students linked the cracking to the change from metallic to ionic bonding, and the greater volume.",
      refs=['content', 'ex25q6', 'ar25q6'], covers=['K4', 'K2', 'K1'], elements=[5, 1], exam=['X25-6']),
]),
Scene('rust_cell', P5, 'The electrochemistry of rusting', V.rust_cell, [
    S("Rusting needs three things: iron, oxygen and water. Dissolved ions, in the water, make it faster. Corrosion is the "
      "oxidation of the metal by substances in the environment, and it works as a tiny galvanic cell on the surface.",
      refs=['content', 'ar25q6'], covers=['K1', 'K5', 'K9'], elements=[5, 1], exam=['X25-6']),
    S("Where the oxygen concentration is high, as at the edge of a water drop, oxygen is reduced: that is the cathode. Where it "
      "is low, in the middle, or below the ground, or deep in a crevice, iron is oxidised: that is the anode. This is "
      "differential aeration. The cathode is where oxygen is highest.",
      refs=['content', 'ar21q4', 'ar22q5', 'ar25q6'], covers=['K7', 'K8', 'K5'], elements=[5], exam=['X21-4', 'X22-5', 'X25-6']),
    S("At the anode, iron gives up electrons to make iron two plus. At the cathode, oxygen and water take them and form "
      "hydroxide ions. Electrons move through the metal. Ions move through the water, with hydroxide towards the anode and iron "
      "two plus towards the cathode. The iron two plus is then oxidised further to rust. Do not talk about a change in the "
      "concentration of water: examiners marked it as wrong.", refs=['content', 'ar25q6', 'ar21q4'], covers=['K5', 'K1'], elements=[5, 1],
      exam=['X25-6', 'X21-4']),
]),
Scene('corrosion_factors', P5, 'What speeds corrosion up', Slide('cards', title='Factors in corrosion', chip='Element 5 · corrosion', cols=2, counts=[1, 2, 3, 4], size=21, cards=[
    ('Stress', 'Bends, cuts and welds strain the metal.\nStressed metal becomes the anode.', '#38bdf8'),
    ('Dissolved ions', 'Salt water is a better electrolyte, so it carries current\nwell and corrodes faster than fresh water.', '#a78bfa'),
    ('Oxygen differences', 'Waterline: lots of O₂ above, little below.\nDeep underwater: too little O₂ for the cathode: slow.', '#9bde7e'),
    ('Contact with another metal', 'The stronger reducer is oxidised faster. Iron is the anode\nwhen joined to copper, and is protected by zinc or magnesium.', '#f15bb5')]), [
    S("Stress also matters. Bent, cut or welded metal is under strain, and stressed regions are more likely to become the anode. "
      "Dissolved ions speed things up, because they carry charge: salt water corrodes steel faster than fresh water.",
      refs=['content', 'ex23q4', 'ar23q4'], covers=['K6', 'K9'], elements=[5], exam=['X23-4']),
    S("Ranking three boats: the one at the saltwater waterline corrodes fastest, because it has oxygen and many ions. The "
      "freshwater boat at the waterline is next. The boat deep underwater is slowest, because there is little oxygen for the "
      "cathode reaction. Always include the cathode half-equation in the reasoning.",
      refs=['ex23q4', 'ar23q4'], covers=['K7', 'K9', 'K8'], elements=[5, 4], exam=['X23-4'],
      problem='Three steel boats: A at a fresh-water waterline, B at a sea waterline, C deep in a fresh-water lake. Rank their corrosion rates.'),
    S("Dissimilar metals are the last factor. When two metals are in contact in an electrolyte, the stronger reducer is the "
      "anode, so it is oxidised. Here the steel pipe is the anode and the copper is the cathode. This is why joining "
      "dissimilar metals in pipework is best avoided.", refs=['content', 'ex24q5', 'ar21q4', 'ex21q4'], covers=['K10'], elements=[5, 3],
      exam=['X24-5', 'X21-4']),
    S("Two more points from the reports. A wooden hull with copper plates held by iron nails corroded the nails, "
      "because the nails were the anode. Nails with paper, hair or wool trapped under their heads corroded less, because "
      "those are insulators, so there was no electrical contact. And Fe two plus does appear on the table, so for iron "
      "think about both oxidising and reducing.", refs=['ex21q4', 'ar21q4', 'ar25q4'], covers=['K10', 'K5'], elements=[5, 4], exam=['X21-4']),
]),
Scene('two_metals', P5, 'Two metals in contact', V.two_metals, [
    S("Here is a steel pipe joined to a copper pipe in damp conditions. It is a galvanic cell. Iron is the stronger reducer, "
      "so the steel is the anode, and it is oxidised: iron to iron two plus. The copper is the cathode, where oxygen is "
      "reduced to hydroxide ions.", refs=['content', 'ex24q5', 'ex21q4'], covers=['K10', 'K5'], elements=[5, 4], exam=['X24-5', 'X21-4']),
    S("Electrons flow from the steel to the copper through the metal contact. Ions move through the water. The iron wastes "
      "away, and the copper is protected, so the corrosion of the steel is faster than it would have been alone.",
      refs=['content', 'ar21q4'], covers=['K10'], elements=[5]),
    S("Break the electrical contact and the cell stops. Rubbing a coating of paper between metals does that. Also, the same "
      "idea gives sacrificial protection, which we use next.", refs=['ar21q4'], covers=['K10', 'K11'], elements=[5], exam=['X21-4']),
]),
Scene('pitting', P5, 'Pitting in a galvanised tank', Slide('bullets', title='Pitting: a hole that keeps growing', chip='Element 5 · corrosion', size=25, counts=[1, 2, 3, 4], items=[
    'A small hole opens in the zinc coating of a galvanised steel tank',
    'Anode: the exposed edges of the hole, where little O₂ reaches. Cathode: the surface around it, rich in O₂',
    'Electrons flow in the metal from anode to cathode. Cations move through the water, not through the metal',
    'Oxidation removes iron (and zinc), so the metal thins and the hole gets deeper: a differential aeration cell']), [
    S("Pitting corrosion is a harder variation. In a galvanised tank, a small hole in the protective zinc exposes the steel. "
      "Corrosion then spreads from that hole.", refs=['ex21q4', 'ar21q4'], covers=['K5', 'K8'], elements=[5], exam=['X21-4']),
    S("The exposed area at the hole has less oxygen, so it is the anode, and the surrounding surface is the cathode. "
      "Label the diagram with the anode area, the cathode area, electron flow and cation flow.", refs=['ar21q4'], covers=['K7', 'K5'], elements=[5, 4], exam=['X21-4']),
    S("A common error was to show electrons travelling through the water, and ions through the metal. Electrons move in "
      "the metal, ions move in the solution. Keep the anode and cathode spaced apart.", refs=['ar21q4'], covers=['K5'], elements=[5, 4], exam=['X21-4']),
    S("The hole grows because oxidation removes metal at the anode. Mention the oxygen concentration gradient, which is "
      "differential aeration, and the loss of iron. Very few students did.", refs=['ar21q4'], covers=['K8', 'K5'], elements=[5], exam=['X21-4']),
]),
Scene('prevention', P5, 'Preventing corrosion', Slide('table', title='Corrosion prevention compared', chip='Element 5 · prevention',
    head=['Method', 'How it works', 'If scratched?'], widths=[0.25, 0.43, 0.22], size=22, counts=[1, 2, 3, 4, 5, 6], rows=[
        ['Paint, lubricants, polymers', 'Exclude O₂ and H₂O: a physical barrier', 'Fails where broken'],
        ['Noble metal coating (tin, chromium)', 'Barrier, and the coating is less reactive than steel', 'Worse: steel becomes the anode'],
        ['Sacrificial coating (zinc: galvanising)', 'Barrier; Zn is the stronger reducer', 'Still protects: Zn is oxidised'],
        ['Sacrificial anode (Mg, Zn)', 'A more reactive metal is connected: it is oxidised, steel is the cathode', 'Replace the anode'],
        ['Applied EMF (impressed current)', 'Steel is made the cathode by a supply; the anode is inert', 'Works while powered'],
        ['Alloys (stainless steel)', 'Oxide layer: not a coating method here', 'Not in the course list']]), [
    S("Now preventing corrosion. Some methods work by excluding the environment, which is oxygen and water. Painting creates "
      "a physical barrier. Lubricants, such as grease, and polymer coatings do the same. They all fail if the coating is damaged.",
      refs=['content', 'ex24q5', 'ar24q5'], covers=['K11'], elements=[5], exam=['X24-5']),
    S("Metal coatings are of two kinds. A noble coating, such as tin on steel, protects while it is intact. But if it is "
      "scratched, the steel is the stronger reducer, so the steel becomes the anode and corrodes faster. In a recent exam, "
      "a tin post connected to a steel pole failed for the same reason.", refs=['content', 'ex25q6', 'ar25q6'], covers=['K11'], elements=[5], exam=['X25-6']),
    S("A sacrificial coating, such as zinc, is the stronger reducer. Even if it is scratched, the zinc is oxidised in "
      "preference to the iron, and the iron is the site of reduction. Galvanising is the name for a zinc coating "
      "specifically. If the coating is magnesium or aluminium, it is not called galvanising.",
      refs=['content', 'ex22q5', 'ar22q5', 'ar24q5'], covers=['K11'], elements=[5], exam=['X22-5', 'X24-5']),
    S("Cathodic protection connects the steel to a stronger reducer, such as magnesium, which is called a sacrificial anode. "
      "It is oxidised, and the steel gets the electrons. The magnesium rod in a hot water cylinder is an example. A common mistake "
      "was writing half-equations for both metals separately. The magnesium is oxidised, and the steel is where oxygen or water "
      "is reduced, because they are connected.", refs=['content', 'ex24q5', 'ar24q5', 'ex23q4', 'ar23q4'], covers=['K11', 'K5'],
      elements=[5, 4], exam=['X24-5', 'X23-4']),
    S("Applied EMF does the same job with a power supply. The steel is joined to the negative terminal, so it is the cathode, "
      "and an inert or scrap anode to the positive terminal. It is used on buried pipelines and wharves. Two practical "
      "alternatives to painting are sacrificial anodes and applied EMF. Making an alloy was not accepted as one of them.",
      refs=['content', 'ar24q5', 'ex25q6', 'ar25q6'], covers=['K11'], elements=[5], exam=['X24-5', 'X25-6']),
    S("Remember how each one fails, because that is how examiners test it: paint fails when scratched, a noble coating "
      "makes things worse when scratched, and a sacrificial coating still works.", refs=['ar25q6', 'ar22q5'], covers=['K11'], elements=[5], exam=['X25-6', 'X22-5']),
]),
Scene('cathodic', P5, 'Two ways of cathodic protection', V.protect_diagram, [
    S("Here are the two kinds of cathodic protection for a buried steel pipe. Left: a sacrificial anode. A magnesium block "
      "is wired to the pipe. Magnesium is the stronger reducer, so it is oxidised, and electrons flow to the steel, which is the "
      "cathode.", refs=['content', 'ar24q5'], covers=['K11'], elements=[5, 4], exam=['X24-5']),
    S("Right: an applied EMF. A DC supply has its negative terminal connected to the pipe and its positive terminal to an inert "
      "anode in the soil. The pipe becomes the cathode, so it cannot be oxidised. Choose by the situation: a sacrificial "
      "anode needs no power but wears out, while an applied supply needs electricity but lasts.", refs=['content', 'ex25q6'],
      covers=['K11'], elements=[5], exam=['X25-6']),
]),
Scene('choose', P5, 'Choosing the most suitable method', Slide('table', title='Which method, and why?', chip='Element 5 · A standard',
    head=['Situation', 'Best choice', 'Why'], widths=[0.25, 0.28, 0.37], size=22, counts=[1, 2, 3, 4, 5], rows=[
        ['Underground steel pipeline', 'Sacrificial anodes, or applied EMF', 'Paint alone cannot be inspected or repaired; the soil is an electrolyte'],
        ['Ship hull in sea water', 'Paint plus zinc or aluminium anodes', 'Salt water speeds corrosion; the paint is damaged by impacts'],
        ['Garden fence or roof sheet', 'Galvanised steel', 'Cheap; zinc still protects at scratches'],
        ['Moving machine parts', 'Lubrication (oil or grease)', 'A rigid coating would wear away'],
        ['Food can', 'Tin plus a polymer lacquer', 'Tin is non-toxic; it must stay intact, as steel would corrode faster if it is scratched']]), [
    S("For an A, you must choose the most appropriate method, and justify it. Match the method to the situation. For a "
      "buried pipeline, use sacrificial anodes or an applied supply, because paint alone cannot be inspected or repaired.",
      refs=['standards', 'content', 'ex25q6'], covers=['K11', 'A1'], elements=[5], exam=['X25-6'],
      problem='Which corrosion prevention method suits a buried steel pipeline, and why?'),
    S("A ship's hull is in salt water, which is a good electrolyte. Use paint, plus blocks of zinc or aluminium, which are "
      "oxidised in preference to the steel.", refs=['content', 'ex23q4'], covers=['K11', 'K9'], elements=[5], exam=['X23-4'],
      problem='Which corrosion prevention method suits a ship hull in sea water, and why?'),
    S("A garden fence is best galvanised, since zinc still protects the steel where it is scratched. Moving machine parts "
      "need lubrication, since a rigid coating would wear off.", refs=['content'], covers=['K11'], elements=[5]),
    S("And a food can uses tin with a polymer lacquer: tin is safe, but the coating must not be scratched. In every answer, "
      "name the method, say how it works with half-equations or the relative reducing strengths, and say why it suits the situation.",
      refs=['standards', 'content'], covers=['K11'], elements=[5, 4]),
    S("The cost of corrosion is a context in the course. Corrosion of steel pipes caused the Varanus Island gas explosion in "
      "Western Australia, and corroded bridge cables are a safety issue. Maintenance decisions weigh cost, safety, and heritage "
      "value. Extending the life of metals saves money and reduces environmental impact.", refs=['appendix'], covers=['A1'], elements=[5, 1]),
]),
Scene('clean_water', P5, 'Electrochemistry for clean water', Slide('bullets', title='Context: clean water from electrolysis', chip='Context · course appendix', size=25, counts=[1, 2, 3], items=[
    'Bore water can contain dissolved iron and manganese, which make it undrinkable',
    'A current through the water oxidises chloride ions at the anode: 2Cl⁻ → Cl₂ + 2e⁻',
    'The chlorine oxidises the iron and manganese ions so they precipitate out, and it also disinfects the water',
    'Only a small current is needed: a 12 V car battery is enough, so it can work in rural areas']), [
    S("A final context from the course. Some bore water has dissolved iron and manganese that make it undrinkable. New Zealand "
      "scientists used a small electric current to oxidise chloride ions to chlorine at an anode.", refs=['appendix', 'info_srp'],
      covers=['A4'], elements=[1, 4]),
    S("The chlorine is a strong oxidiser. It oxidises the iron and manganese ions, which then precipitate, and it disinfects. "
      "The process needs only a twelve volt car battery, making it cheap for remote communities, an example of electrochemistry "
      "solving a real problem. In an unfamiliar context like this, use the series to reason.",
      refs=['appendix', 'info_srp'], covers=['A4', 'E3'], elements=[1, 4, 3]),
]),

# ------------------------------------------------------------------ finish
Scene('exam_tips', P6, 'Tips for tests and the exam', Slide('tips', title='Tips from examiners', counts=[2, 4, 6, 8], tips=[
    'Metals are reducers, metal ions are\noxidisers. Metals are never oxidisers',
    'Support every explanation with\nhalf-equations, even if not asked',
    'Compare the right pairs, and say\noxidising or reducing strength',
    'Oxidation number: sign first (+7).\nGive the reason, not just the number',
    'A net ionic equation is the full\nredox equation: do not split it',
    'Diagrams: big, labelled lines touching\nelectrodes, e⁻ in the wire, named ions',
    'Electrolysis voltage is a MINIMUM;\nmolten ions are (l), not (aq)',
    'Observations are what you can see;\nspontaneous reactions have no anode']), [
    S("Finally, technique for tests and the exam, drawn from examiners' reports. One: metals are reducers, and metal "
      "ions are oxidisers. Two: back every explanation with half-equations, even when they are not requested, and refer "
      "to oxidising and reducing strength, not just position on the series.",
      refs=['ar21a', 'ar23a', 'ar25a', 'ar25g']),
    S("Three: compare the right pairs, for example zinc against copper, not zinc against copper two plus. Four: write the "
      "sign first when giving an oxidation number, and give the reason it makes something an oxidiser or reducer. "
      "Five: a net ionic equation is the full redox equation, with states and with water and hydrogen ions cancelled.",
      refs=['ar25q1', 'ar24q1', 'ar24q2']),
    S("Six: draw diagrams large, with label lines touching the electrodes, electrons in the wire, and the actual ions named, "
      "such as sodium and nitrate. Only draw species that are present. Seven: the voltage needed for electrolysis is a minimum, "
      "and ions in a melt are state liquid.", refs=['ar22q1', 'ar24q3', 'ar24q4', 'ar25q3']),
    S("Eight: observations are what you can see, such as bubbles, a colour fading or a deposit, not what you think "
      "the product is, and not a pop test. In a question about a spontaneous reaction rather than a cell, do not use the words "
      "anode or cathode. And always give units and context for numerical answers.", refs=['ar25q1', 'ar25q4', 'ar25g']),
]),
Scene('more_tips', P6, 'More examiner tips', Slide('tips', title='More tips from examiners', start=9, counts=[4, 8], tips=[
    'Yield: divide to scale UP to\n100%; never multiply',
    'Fe²⁺ is on the table as an oxidiser\nAND a reducer: consider both',
    'Sacrificial anode: the protected metal\nis the site of reduction',
    'Galvanising means zinc only; tin is\nnoble: fails if scratched',
    'Rust cracks concrete: ionic bonding and\nlarger volume, not water concentration',
    'Use the spare diagram, turn every\npage, answer in blue or black pen',
    'Show working: part marks need steps,\nand numbers need units',
    'Contradictory statements lose marks:\ndo not hedge with extra answers']), [
    S("More tips. Nine: when scaling for yield, divide to get the amount at one hundred percent, never multiply. Ten: "
      "iron two plus appears on the table as an oxidiser and as a reducer, so consider both roles. Eleven: with "
      "a sacrificial anode, the protected metal is where reduction happens. Twelve: galvanising means zinc, and a noble "
      "coating fails if it is scratched.", refs=['ar25q4', 'ar25q5', 'ar24q5']),
    S("Thirteen: when rust cracks concrete, it is because of ionic bonding and a larger volume, not water concentration. "
      "Fourteen: use the spare diagrams, turn every page, and write in blue or black pen. Fifteen: show working, with units and "
      "context. Sixteen: do not add extra or contradictory answers, because markers deduct for each incorrect statement.",
      refs=['ar25q6', 'ar25g']),
]),
Scene('summary', P6, 'Summary', Slide('summary', title='Criterion 5 in one screen', chips=[
    ('OIL RIG', '1'), ('oxidation numbers', '1'), ('reducer loses e⁻', '1'), ('half-equations', '2'), ('balance: H₂O, H⁺, e⁻', '2'),
    ('E°cell = E°ox + E°red', '2'), ('more than 2 species', '2'), ('anode (−): oxidation', 'p'), ('cathode (+): reduction', 'p'),
    ('salt bridge', 'p'), ('cell shorthand', 'p'), ('electrolytic: anode +', 'g'), ('water competes', 'g'), ('q = It, n(e⁻) = It/F', 'g'),
    ('differential aeration', 'y'), ('sacrificial anode', 'y'), ('applied EMF', 'y')],
    close='Strongest oxidiser meets strongest reducer. Always say WHY.'), [
    S("That is the whole of Criterion 5. Oxidation is loss of electrons, and reduction is gain. Oxidation numbers and half-equations "
      "let you balance redox equations. The electrochemical series predicts what reacts. Galvanic cells make electricity, with oxidation at the anode, "
      "and electrolytic cells use it, with the polarity reversed. Faraday's law links charge, moles and mass. And corrosion "
      "is a cell too, with prevention by barriers, sacrificial metals or an applied supply. Practise explaining with "
      "half-equations as well as predicting, and you will be ready for your tests and for Section A. Good luck."),
]),
]

_used = {r for sc in SCENES for st in sc.steps for r in st.refs} | {t[1] for t in EXAM_TOPICS.values()} \
    | {t[1] for t in SYLLABUS.values()} | {t[1] for t in ELEMENTS.values()} | {'info', 'info_data', 'info_srp', 'spec_q'}
REFS = {k: r for k, r in REFS.items() if k in _used}

VIDEO = Video(
    id='CHM415115_C5_electrochemistry',
    course=COURSE, course_name='Chemistry', module=MODULE,
    module_name='Criterion 5: Identify and apply fundamental principles and theories of electrochemistry',
    title='Criterion 5: electrochemistry, complete revision',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Chemical Information'),
    checks=CHECKS,
    thumbnail=V.thumbnail,
    allowed_overlaps=['identify and apply fundamental principles and theories of electrochemistry'],
    keywords=['oxidiser', 'reducer', 'oxidation', 'reduction', 'half-equation', 'oxidation number', 'oxidation state',
              'electrochemical series', 'galvanic', 'electrolytic', 'anode', 'cathode', 'salt bridge', 'electroneutrality',
              'electrolyte', 'differential aeration', 'sacrificial anode', 'applied EMF', 'galvanising', 'spontaneous',
              'minimum voltage', 'net ionic equation', 'Faraday', 'corrosion', 'rust', 'inert electrode'],
    description=('A complete revision explainer for TASC Chemistry (CHM415115) Criterion 5: identify and apply fundamental '
                 'principles and theories of electrochemistry. For class tests and the end-of-year exam (Section A). '
                 'Items from the TASC information sheet are labelled on screen.'),
)
