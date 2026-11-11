"""CHM415115 Chemistry, Criterion 7: Demonstrate knowledge and understanding of properties and reactions of organic and inorganic matter.

    uv run python -m explainer check   videos/CHM415115/c7_organic_inorganic.py
    uv run python -m explainer preview videos/CHM415115/c7_organic_inorganic.py
    uv run python -m explainer thumbnail videos/CHM415115/c7_organic_inorganic.py
    uv run python -m explainer render  videos/CHM415115/c7_organic_inorganic.py    # operator only
"""
import math

from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, InfoSheet, import_sibling

COURSE, MODULE = 'CHM415115', 'C7'
L.use(style.theme(COURSE, MODULE))
V = import_sibling(__file__, 'c7_visuals.py')
_CC = import_sibling(__file__, 'chm_common.py')
Slide, Seq, Phased, ch = _CC.Slide, _CC.Seq, _CC.Phased, _CC.ch
alk, mol_slide = V.alk, V.mol_slide

P0 = 'Criterion 7 · Overview'
P1 = 'Part 1 · Gases'
P2 = 'Part 2 · Atoms and the periodic table'
P3 = 'Part 3 · Organic structures and names'
P4 = 'Part 4 · Properties of organic compounds'
P5 = 'Part 5 · Organic reactions'
P6 = 'Part 6 · Analysing structures'
P7 = 'Finish · Tests & exam technique'

# --------------------------------------------------------------------------- references
COURSE_DOC = 'chm415115-9.html'
INFO = 'CHM415115-Chemistry-Information-Sheet.pdf'
SPEC = 'CHM415115-Chemistry-External-Assessment-Specifications.pdf'

EXAM_PAGES = {
    2021: {11: 32, 12: 33, 13: 34, 14: 35, 15: '36-37', 16: 38, 17: '40-41'},
    2022: {11: 31, 12: '32-33', 13: '34-35', 14: 36, 15: 37, 16: '38-40', 17: 41},
    2023: {11: '36-37', 12: '38-39', 13: '40-41', 14: 42, 15: 43, 16: '44-45'},
    2024: {11: 36, 12: 37, 13: '38-39', 14: 40, 15: 41, 16: 42},
    2025: {12: '35-36', 13: '37-38', 14: '39-41', 15: '42-43', 16: 44},
}
REPORT_PAGES = {
    2021: {11: 12, 12: 13, 13: 13, 14: 14, 15: 15, 16: '15-16', 17: '16-17'},
    2022: {11: '13-14', 12: '14-15', 13: '15-16', 14: '16-17', 15: '17-18', 16: '18-20', 17: 20},
    2023: {11: '12, 14', 12: '12, 14-15', 13: '12, 15', 14: '12, 15-16', 15: '12, 16-17', 16: '13, 17-18'},
    2024: {11: '13-14', 12: '13, 15', 13: '13, 15-16', 14: '13, 17', 15: '13, 18', 16: '13, 18-19'},
    2025: {12: '15-16, 18', 13: '16, 18-19', 14: '16-17, 20-21', 15: '17, 21-22', 16: '17, 22'},
}


def exam(y, q):
    section = 'Part 3' if y == 2021 else 'Section C'
    return Ref(f'CHM415115-Chemistry-TASC-Exam-Paper-{y}.pdf', f'{y} exam, {section}, Question {q}', EXAM_PAGES[y][q])


def report(y, q):
    return Ref(f'CHM415115-Chemistry-Assessment-Report-{y}.pdf', f'{y} assessment report, Criterion 7, Question {q}',
               REPORT_PAGES[y][q])


REFS = {
    'standards': Ref(COURSE_DOC, 'Course document, Criterion 7 standards (element table)'),
    'content': Ref(COURSE_DOC, 'Course document, Science Understanding: properties and reactions of organic and inorganic matter (Criterion 7)'),
    'appendix': Ref(COURSE_DOC, 'Course document, Appendix 1: contexts (scuba diving and gases; functional groups and organic chemistry; green polymer chemistry)'),
    'info': Ref(INFO, 'Information sheet, Chemical Information (combined gas equation, PV = nRT)', page=2),
    'info_data': Ref(INFO, 'Information sheet, Chemical Data and Constants (R, STP, SLC, molar volumes)', page=1),
    'info_org': Ref(INFO, 'Information sheet, Organic Chemistry (stem names, side chains, prefixes)', page=5),
    'info_fg': Ref(INFO, 'Information sheet, Aliphatic Functional Groups', page=6),
    'info_rx': Ref(INFO, 'Information sheet, Some Organic Reactions of Aliphatic Compounds; IR stretching frequencies', page=7),
    'info_ar': Ref(INFO, 'Information sheet, Table of Relative Atomic Masses', page=9),
    'info_pt': Ref(INFO, 'Information sheet, General Periodic Trends', page=10),
    'spec': Ref(SPEC, 'External assessment specifications, Section C', page=3),
}
for _y, _qs in EXAM_PAGES.items():
    for _q in _qs:
        REFS[f'ex{_y % 100}q{_q}'] = exam(_y, _q)
for _y, _qs in REPORT_PAGES.items():
    for _q in _qs:
        REFS[f'ar{_y % 100}q{_q}'] = report(_y, _q)
REFS['ar21g'] = Ref('CHM415115-Chemistry-Assessment-Report-2021.pdf', '2021 assessment report, Criterion 7 general comments', 12)
REFS['ar22g'] = Ref('CHM415115-Chemistry-Assessment-Report-2022.pdf', '2022 assessment report, Section C general comments', 13)
REFS['ar24g'] = Ref('CHM415115-Chemistry-Assessment-Report-2024.pdf', '2024 assessment report, Criterion 7 general feedback', 13)
REFS['ar25g'] = Ref('CHM415115-Chemistry-Assessment-Report-2025.pdf', '2025 assessment report, Section C general comments', 15)

# --------------------------------------------------------------------------- coverage targets
SYLLABUS = {
    'G1': ("Properties of gases as described by Boyle's Law, Charles' Law and the ideal gas equation", 'content'),
    'G2': ('Kinetic theory explains gas properties, including gas mixtures and the non-ideal behaviour of real gases', 'content'),
    'O1': ('Define a functional group', 'content'),
    'O2': ('Name and draw structural formulae of organic molecules, including simple amines and amides', 'content'),
    'O3': ('Amino acids: an amine group and a carboxylic acid group on a hydrocarbon chain', 'content'),
    'O4': ('Characteristic properties and reactions of each class: addition, substitution, acid-base, oxidation; at most two functional groups externally', 'content'),
    'O5': ('Alkyl halides compared with alkanes: polarity, dipole-dipole and dispersion forces', 'content'),
    'O6': ('Alkyl halides undergo substitution more readily than alkanes', 'content'),
    'O7': ('Equations: alkyl halides forming primary, secondary and tertiary alcohols', 'content'),
    'O8': ('Structure of benzene: flat, symmetrical, bonds intermediate between single and double', 'content'),
    'O9': ('Hydrogen bonding raises melting and boiling points of alcohols compared with alkanes', 'content'),
    'O10': ('Alcohols are more soluble than alkanes in polar solvents', 'content'),
    'O11': ('Distinguish primary, secondary and tertiary alcohols', 'content'),
    'O12': ('Polyalcohols have much higher boiling points than simple alcohols', 'content'),
    'O13': ('Equations for alcohols with sodium and with carboxylic acids', 'content'),
    'O14': ('Primary alcohol to aldehyde: copper catalyst or limited acidified dichromate', 'content'),
    'O15': ('Primary alcohol to carboxylic acid with stronger oxidisers such as acidified permanganate', 'content'),
    'O16': ('Oxidation of secondary alcohols to ketones', 'content'),
    'O17': ('Tertiary alcohols do not undergo oxidation', 'content'),
    'O18': ('Alkanes and alkenes with halogens', 'content'),
    'O19': ('Alkanes undergo substitution reactions', 'content'),
    'O20': ('Combustion of hydrocarbons with excess and with insufficient oxygen', 'content'),
    'O21': ('Alkenes and alkynes undergo addition reactions', 'content'),
    'O22': ('Complete reactions of alkenes and alkynes with asymmetric molecules such as hydrogen halides and steam', 'content'),
    'O23': ('Identify the possible isomers from an asymmetric molecule adding to an unsaturated hydrocarbon', 'content'),
    'O24': ('Alkenes form addition polymers', 'content'),
    'O25': ('Polyesters formed from polyalcohols and polyacids', 'content'),
    'O26': ('Oxidation of aldehydes to carboxylic acids', 'content'),
    'O27': ('Aldehydes are less soluble in polar solvents than the alcohols they come from', 'content'),
    'O28': ('Ketones cannot be oxidised further', 'content'),
    'O29': ('Carboxylic acids are weak acids', 'content'),
    'O30': ('Carboxylic acids as monoacids or polyacids', 'content'),
    'O31': ('Carboxylic acid solutions have a higher pH than strong acids of the same concentration', 'content'),
    'O32': ('Carboxylic acids with carbonates, hydrogencarbonates, metal oxides, hydroxides, reactive metals and alkalis', 'content'),
    'O33': ('Carboxylic acid with a primary alcohol forms an ester', 'content'),
    'O34': ('Fuels from organic sources: addition, oxidation and esterification (brief)', 'content'),
    'O35': ('Esters are insoluble in water and have distinctive smells', 'content'),
    'O36': ('Hydrolysis of esters, including alkaline hydrolysis', 'content'),
    'O37': ('Amines and amides: hydrogen bonding raises melting and boiling points', 'content'),
    'O38': ('Amines and amides are more soluble than alkanes in polar solvents', 'content'),
    'S1': ('Mass spectroscopy: molecular ion peak, relative molecular mass, simple fragments', 'content'),
    'S2': ('Infrared spectroscopy: characteristic absorption bands for functional groups', 'content'),
    'S3': ('X-ray crystallography identifies simple molecular structures', 'content'),
    'S4': ('Structure determination often needs evidence from more than one technique', 'content'),
    'P1': ('Variation of ionisation energy as successive electrons are removed', 'content'),
    'P2': ('Emission and absorption spectra (qualitative)', 'content'),
    'P3': ('The Bohr model of the hydrogen atom', 'content'),
    'P4': ('Shells, sub-shells and orbitals (quantum numbers mentioned)', 'content'),
    'P5': ('Electron configurations of atoms and simple ions using s, p and d sub-shells', 'content'),
    'P6': ('Define and apply isoelectronic', 'content'),
    'P7': ('Predict the charges of ions from the main groups', 'content'),
    'P8': ('Valence theory explains the periodic variation of chemical properties of s and p block elements', 'content'),
    'P9': ('Trends and anomalies in the behaviour of elements', 'content'),
    'P10': ('Trends across periods and down groups: electronegativity, core charge, nuclear shielding', 'content'),
    'P11': ('Main-group metals get less reactive and non-metals more reactive from left to right', 'content'),
    'P12': ('Metals get more reactive and non-metals less reactive down a group', 'content'),
    'P13': ('Changes in atomic and ionic radii', 'content'),
    'P14': ('Mass spectroscopy analyses isotopic mixtures', 'content'),
    'A1': ('Context: scuba diving and the behaviour of gases', 'appendix'),
    'A2': ('Context: functional groups and organic chemistry', 'appendix'),
    'A3': ('Context: green polymer chemistry', 'appendix'),
}

ELEMENTS = {
    1: ('Draws and names organic molecules, including more than one functional group, isomers and polymers', 'standards'),
    2: ('Uses bond polarity to explain physical properties and uses properties and analytical data to identify functional groups', 'standards'),
    3: ('Writes equations for reactions of organic molecules with a range of functional groups and reagents', 'standards'),
    4: ('Writes electron configurations using sub-shells to make predictions about chemical activity', 'standards'),
    5: ('Uses valence theory to explain periodic variation, trends and anomalies', 'standards'),
    6: ('Explains behaviours of gases, mixtures and real gases using kinetic theory and applies the gas laws', 'standards'),
}

EXAM_TOPICS = {
    'X21-11': ('Propanol to propanamine by a structural equation; solubility from functional groups; why copper catalyst is better than dichromate for ethanal; type of polymer from lactic acid', 'ex21q11'),
    'X21-12': ('Naming three compounds from a halide to alcohol to oxidation product, using an infrared spectrum', 'ex21q12'),
    'X21-13': ('Why one benzene drawing is preferred; drawing an addition polymer of styrene', 'ex21q13'),
    'X21-14': ('Naming an alcohol, equation with sodium, functional groups, dehydration product, an isomer that cannot be oxidised', 'ex21q14'),
    'X21-15': ('Gas pressure and temperature in tyres by kinetic theory, air against nitrogen, tyres filled from a cylinder, molecular size', 'ex21q15'),
    'X21-16': ('Neon configuration, formula of a compound of isoelectronic ions, what occurs to give an emission spectrum', 'ex21q16'),
    'X21-17': ('Aluminium ionisation: equation, sketching the third ionisation energy, ion stability from configuration, least reactive period 3 metal and most electronegative non-metal', 'ex21q17'),
    'X22-11': ('Ground-state configuration from an excited one, identifying a transition element and its ion, ordering ionic radii', 'ex22q11'),
    'X22-12': ('Dive-tank gas calculations, partial pressure and oxygen toxicity, a PV graph deciding ideal or real', 'ex22q12'),
    'X22-13': ('Period 3 data: atomic radius trend, defining first ionisation energy, aluminium against magnesium, down group I', 'ex22q13'),
    'X22-14': ('Name, structure and empirical formula for two organic compounds, one cyclic', 'ex22q14'),
    'X22-15': ('Two isomers of C4H8 identified from bromine and steam tests; drawing and naming', 'ex22q15'),
    'X22-16': ('Ester preparation: sodium carbonate with ethanoic acid, identifying compounds from infrared spectra, preparing another ester, boiling points of an alkane and an alcohol', 'ex22q16'),
    'X22-17': ('Addition polymer segment from a monomer; deducing the monomer of a polyester', 'ex22q17'),
    'X23-11': ('Drawing from systematic names with a halogen and an amine; elements and ions from configurations including d-block', 'ex23q11'),
    'X23-12': ('Successive ionisation energy graph identifying an element; ionic radii of oxygen and magnesium ions', 'ex23q12'),
    'X23-13': ('Pressure in a bottle by kinetic theory; condensation or addition polymer for PET; its reactants', 'ex23q13'),
    'X23-14': ('Ideal gas assumptions; a real gas at low temperature compared with ideal predictions', 'ex23q14'),
    'X23-15': ('Products of a carboxylic acid and an alcohol with sodium; evaluating a prediction about hydrogen volumes', 'ex23q15'),
    'X23-16': ('Primary and secondary alcohols, solubility of two alcohols, oxidation products, infrared evidence, benzene structure', 'ex23q16'),
    'X24-11': ('Properties of an ideal gas; sketch of pressure against temperature; kinetic theory explanation', 'ex24q11'),
    'X24-12': ('Completing a table of empirical formula, name, structure and functional group', 'ex24q12'),
    'X24-13': ('Boiling points of alkyl halides against alkanes; propene and chlorine; hydrolysis of chloropropanes; oxidation products and a physical property comparison', 'ex24q13'),
    'X24-14': ('Structures for an empirical formula and an infrared spectrum to identify the compound', 'ex24q14'),
    'X24-15': ('Successive ionisation energies and spectra as evidence for shells and sub-shells', 'ex24q15'),
    'X24-16': ('Isoelectronic ions: configuration, ordering radii, highest ionisation energy', 'ex24q16'),
    'X25-12': ('Functional groups of aspirin; a better diagram of benzene; low solubility from intermolecular forces', 'ex25q12'),
    'X25-13': ('Drawing from names including an amide and an ester; why an amino acid melts high; its features; polymer of lactic acid', 'ex25q13'),
    'X25-14': ('A reaction scheme from propan-1-ol with infrared and mass spectra to confirm the compound', 'ex25q14'),
    'X25-15': ('Configurations of Al and Co; aluminium ionisation; jump between third and fourth ionisation energies; period 3 trend; Al against Mg', 'ex25q15'),
    'X25-16': ('Why a heated balloon expands; why sulfur dioxide departs from ideal behaviour more than helium', 'ex25q16'),
}

M_O2 = 32.00
M_CO2 = 12.01 + 2 * 16.00


def v_balloon():
    return 101.3 * 2000 * (273.15 - 35.0) / ((273.15 + 25.0) * 30.0)


def n_cyl():
    return 450 * 2.50 / (8.31 * (273.15 + 20.0))


CHECKS = [
    ('balloon volume', v_balloon, 5394, 2e-3),
    ('balloon T1', lambda: 273.15 + 25.0, 298.15, 1e-9),
    ('balloon T2', lambda: 273.15 - 35.0, 238.15, 1e-9),
    ('cylinder moles', n_cyl, 0.4618, 2e-3),
    ('CO2 molar mass', lambda: M_CO2, 44.01, 1e-3),
    ('cylinder mass', lambda: n_cyl() * M_CO2, 20.32, 2e-3),
    ('O2 partial air', lambda: 0.21 * 4.0, 0.84, 1e-9),
    ('O2 partial rich mix', lambda: 0.45 * 4.0, 1.80, 1e-9),
    ('depth pressure', lambda: 1.0 + 30.0 / 10.0, 4.0, 1e-9),
    ('chlorine isotopes', lambda: 35 * 0.758 + 37 * 0.242, 35.48, 1e-3),
    ('mol mass propan-1-ol', lambda: 3 * 12.01 + 8 * 1.008 + 16.00, 60.09, 1e-3),
    ('mol mass propanoic acid', lambda: 3 * 12.01 + 6 * 1.008 + 32.00, 74.08, 1e-3),
    ('empirical formula CH2O mass', lambda: 12.01 + 2 * 1.008 + 16.00, 30.03, 1e-3),
    ('C3H6O2 is 2x CH2O', lambda: 74.08 / 30.026, 2.467, 5e-2),
    ('isoelectronic electrons P3-', lambda: 15 + 3, 18, 1e-9),
    ('isoelectronic electrons Sc3+', lambda: 21 - 3, 18, 1e-9),
    ('Co electrons', lambda: 2 + 2 + 6 + 2 + 6 + 7 + 2, 27, 1e-9),
    ('S electrons', lambda: 2 + 2 + 6 + 2 + 4, 16, 1e-9),
    ('Ni2+ electrons', lambda: 28 - 2, 26, 1e-9),
]

# --------------------------------------------------------------------------- scenes
S = Step
SCENES = [
Scene('title', P0, 'Welcome', Slide('title', kicker='CRITERION 7', name='Properties and\nreactions of organic\nand inorganic matter', art=V._title_art, size=50), [
    S("Welcome. This video is a complete briefing on Criterion 7 of TASC Chemistry, C H M four one five, one one five: "
      "demonstrate knowledge and understanding of the properties and reactions of organic and inorganic matter. It covers "
      "gases, the periodic table and electron configurations, and the structure, names, properties and reactions of organic "
      "compounds. Use it to revise for class tests and for the end of year exam.", refs=['standards'], anim=4),
]),
Scene('intro', P0, 'How Criterion 7 is assessed', Seq(
    Slide('assess', internal='Your teacher: class tests, practicals\nand investigations during the year',
          external='End-of-year TASC exam:\nSection C is all Criterion 7', section='Section C'),
    Slide('elements', title='The six elements of Criterion 7', items=[
        ('Draw and name', 'organic molecules, with more than one functional group, isomers, polymers'),
        ('Properties', 'bond polarity explains physical properties; analytical data identify groups'),
        ('Reactions', 'equations for a range of functional groups and reagents'),
        ('Configurations', 'electron configurations in sub-shells; predict chemical activity'),
        ('Periodic table', 'valence theory explains periodic trends and anomalies'),
        ('Gases', 'kinetic theory, the gas laws, mixtures and real gases')]),
    Slide('standards', title='What the standards ask for', rows=[
        ('E1 Draw and name', 'one functional group', 'more than one', 'plus isomers and polymers'),
        ('E2 Properties', 'identifies variations', 'explains with bond polarity', 'analyses with polarity'),
        ('E3 Reactions', 'common reactions, limited groups', 'a range of groups', 'a range of groups and reagents'),
        ('E4 Configurations', 'writes them, predicts ion charges', 'predicts in familiar contexts', 'in unfamiliar contexts'),
        ('E5 Periodic table', 'identifies trends', 'describes and discusses', 'explains trends and anomalies'),
        ('E6 Gases', 'identifies behaviour', 'describes, incl. mixtures', 'explains, incl. real gases')]),
    Slide('roadmap', title='Roadmap', parts=[
        ('Part 1', 'Gases: kinetic theory, gas laws, real gases'), ('Part 2', 'Atoms and the periodic table'),
        ('Part 3', 'Organic structures and names'), ('Part 4', 'Properties of organic compounds'),
        ('Part 5', 'Organic reactions and polymers'), ('Part 6', 'Analysing structures: IR and mass spectra'),
        ('Finish', 'Tests and exam technique, and a summary')])), [
    S("Criterion 7 is assessed in two ways. Your teacher assesses it during the year, through tests and practical work. It is "
      "also assessed in Section C of the end of year exam: about forty five minutes, forty five marks, and between five and seven "
      "compulsory questions. You may use the information sheet and an approved calculator. For the exam, organic compounds are limited to "
      "two functional groups.", refs=['standards', 'spec', 'content']),
    S("There are six elements, in the order of the standards table. One: drawing and naming organic molecules. Two: using "
      "polarity to explain properties, and using data to identify groups. Three: equations for reactions. Four: electron "
      "configurations. Five: periodic trends. Six: gases. A tag in the corner shows the element a slide practises.",
      refs=['standards'], elements=[1, 2, 3, 4, 5, 6]),
    S("The standards step up from C to A. At C you identify and write common reactions with one functional group. At B you "
      "explain using bond polarity, and handle two groups. At A you add isomers and polymers, analyse, work in unfamiliar "
      "contexts, and explain trends and anomalies and real gas behaviour.", refs=['standards'], elements=[1, 2, 3, 4, 5, 6]),
    S("The roadmap. Gases, then atoms and the periodic table, then organic structures and names, properties, reactions, and "
      "analysis with spectra. Then technique for tests and the exam.", refs=['content']),
]),

# ------------------------------------------------------------------ Part 1: gases
Scene('kmt', P1, 'Kinetic theory of gases', V.kmt_box, [
    S("Start with gases. The kinetic theory describes an ideal gas: particles are tiny compared with the distances between them, "
      "so their volume is negligible. They move randomly in straight lines, and collide elastically with each other and the walls.",
      refs=['content', 'ex23q14', 'ar23q14'], covers=['G2'], elements=[6], exam=['X23-14'], anim=3),
    S("There are no attractions or repulsions between particles. And the average kinetic energy depends only on the absolute "
      "temperature. Careful: never say that the particles have no mass. Markers gave zero for that, and for saying negligible "
      "volume without clarifying it refers to the particles.", refs=['ar23q14', 'ar24q11', 'ex24q11'], covers=['G2'], elements=[6], exam=['X23-14', 'X24-11'], anim=3),
    S("Pressure is the force of the particles hitting the walls. Heat the gas and the particles move faster, with more "
      "kinetic energy. They hit the wall more often, and each hit is harder, so the force on the walls rises. Increasing kinetic "
      "energy raises the speed, not the other way round.", refs=['ex21q15', 'ar21q15', 'ar24q11', 'ex25q16', 'ar25q16'], covers=['G2'], elements=[6, 2], exam=['X21-15', 'X25-16'], anim=3),
    S("The same reasoning explains the helium balloon, which expands when heated, because the faster particles push harder, "
      "until the pressure outside balances. A pop top bottle lid lifts because more carbon dioxide particles mean more "
      "collisions with the lid. At constant temperature, the kinetic energy of carbon dioxide gas particles is the same as in the liquid. "
      "Do not mention effective collisions here: that is for reaction rates.", refs=['ex23q13', 'ar23q13', 'ar25q16'], covers=['G2'], elements=[6], exam=['X23-13', 'X25-16'], anim=3),
]),
Scene('gas_laws', P1, 'Boyle, Charles and the gas equations', Phased((2, V.gas_graphs), (2, Slide('eqs', title='Gas equations on the information sheet', chip='Element 6 · gases',
    counts=[1, 2], gap=0.25, size=34, nx=0.50, y=0.70, section='Chemical Information', items=[
        ('sheet', '$\\dfrac{P_1V_1}{T_1} = \\dfrac{P_2V_2}{T_2}$', 'Combined gas equation, for a fixed amount of gas'),
        ('sheet', '$PV = nRT$', 'R = 8.31 L kPa K⁻¹ mol⁻¹ (with kPa and L), or 0.0821 L atm K⁻¹ mol⁻¹, or 62.4 L mm Hg K⁻¹ mol⁻¹')]))), [
    S("Boyle's law says that at constant temperature, the pressure of a fixed amount of gas is inversely proportional to its volume. "
      "Squash it to half the volume and the pressure doubles. This is the P V constant relationship.",
      refs=['content', 'ex22q12', 'ar22q12'], covers=['G1'], elements=[6], exam=['X22-12']),
    S("Charles' law says that at constant pressure, volume is proportional to the absolute temperature, in kelvin. Extend "
      "the line back and the volume would reach zero at zero kelvin, minus two hundred and seventy three degrees. The same "
      "holds for pressure and temperature at constant volume, which a recent exam asked students to sketch: a straight line "
      "through the origin when the temperature is in kelvin.", refs=['content', 'ex24q11', 'ar24q11'], covers=['G1'], elements=[6, 2], exam=['X24-11']),
    S("Put them together: P one V one over T one equals P two V two over T two. It appears on the information sheet, in the "
      "chemical information section, as the combined gas equation, for a fixed amount of gas. The temperature must be in "
      "kelvin. Pressure and volume can be in any units, as long as both sides match.", refs=['info', 'info_data', 'ex22q12'], covers=['G1'], elements=[6], exam=['X22-12']),
    S("The ideal gas equation, P V equals n R T, is on the sheet too. Pick the value of R that matches your units: eight point "
      "three one with kilopascals and litres, or zero point oh eight two one with atmospheres. A report said some students used "
      "the wrong R, or forgot to convert degrees Celsius to kelvin.", refs=['info', 'info_data', 'ar22q12'], covers=['G1'], elements=[6], exam=['X22-12']),
]),
Scene('we_gas', P1, 'Worked examples with gases', Slide('worked', title='Worked example 1: gas calculations', chip='Element 6 · gases',
    q='(a) A balloon holds 2.00 × 10³ L at 101.3 kPa and 25.0 °C. At altitude the pressure is 30.0 kPa and the temperature −35.0 °C. What is its new volume? (b) How many moles, and what mass, of CO₂ are in a 2.50 L cylinder at 450 kPa and 20.0 °C? (c) A diver at 30 m breathes air at 4.0 atm. Find the partial pressure of O₂ (21% by volume), and for a 45% mix.',
    size=23,
    rows=[dict(s=0, t='T₁ = 25.0 + 273.15 = 298.15 K,   T₂ = −35.0 + 273.15 = 238.15 K', col='#b3c0d4', size=22),
          dict(s=0, t='V₂ = P₁V₁T₂ / (T₁P₂) = 101.3 × 2000 × 238.15 / (298.15 × 30.0) = 5394 L', col='#ffd166'),
          dict(s=0, sf='= 5.39 × 10³ L (3 s.f.)', t='', gap=0),
          dict(s=1, t='n = PV / RT = 450 × 2.50 / (8.31 × 293.15) = 0.4618 mol', col='#ffd166'),
          dict(s=1, t='m = n × M = 0.4618 × 44.01 = 20.32 g', col='#ffd166'),
          dict(s=1, sf='n = 0.462 mol;   m = 20.3 g (3 s.f.)', t='', gap=0),
          dict(s=2, t='Dalton: each gas contributes its share of the total pressure:  p(O₂) = fraction × P(total)', col='#eef2f8'),
          dict(s=2, t='Air:  0.21 × 4.0 = 0.84 atm          45% mix:  0.45 × 4.0 = 1.8 atm', col='#9bde7e'),
          dict(s=3, t='Commonly quoted limit about 1.6 atm (reference): the 45% mix is above it, so a toxicity risk.', col='#f15bb5', size=22)]), [
    S("Worked example one, part a. Use the combined gas equation. Convert both temperatures to kelvin: two ninety eight "
      "point one five, and two thirty eight point one five. The volume is about five thousand four hundred litres, nearly three times "
      "bigger, because the pressure fell a lot and the cooling only partly offsets it.",
      refs=['info', 'ex22q12', 'ar22q12', 'ex21q15', 'ar21q15'], covers=['G1'], elements=[6], exam=['X22-12', 'X21-15'],
      problem='A 2.00 × 10³ L balloon at 101.3 kPa and 25.0 °C rises to 30.0 kPa and −35.0 °C. What is its new volume?'),
    S("Part b. Use P V equals n R T with R as eight point three one, kilopascals and litres, and the temperature in kelvin. "
      "Four fifty times two point five over eight point three one times two ninety three point one five is "
      "zero point four six two moles. Multiply by the molar mass of carbon dioxide to get about twenty point three grams.",
      refs=['info', 'info_data', 'info_ar', 'ex22q12'], covers=['G1'], elements=[6], exam=['X22-12'],
      problem='How many moles and what mass of CO₂ are in 2.50 L at 450 kPa and 20.0 °C?'),
    S("Part c. In a mixture of gases, each gas contributes a partial pressure, which is its fraction times the total pressure. "
      "A diver at thirty metres is at about four atmospheres. Air, twenty one percent oxygen, gives zero point eight four "
      "atmospheres of oxygen. A forty five percent oxygen mix gives one point eight.",
      refs=['content', 'appendix', 'ex22q12', 'ar22q12'], covers=['G2', 'A1'], elements=[6], exam=['X22-12'],
      problem='At 4.0 atm total pressure, what is the partial pressure of O₂ in air (21%) and in a 45% O₂ mixture?'),
    S("In the exam question the limit for oxygen toxicity was given as one point six atmospheres. Compare your partial pressure "
      "with the limit in a sentence: the forty five percent mix is above it, so there is a risk. Divers need to know how gas "
      "volume changes with pressure, and the scuba context in the course covers this, with barotrauma and decompression sickness as consequences.",
      refs=['appendix', 'ar22q12'], covers=['A1', 'G2'], elements=[6], exam=['X22-12']),
]),
Scene('real_gas', P1, 'Real gases', V.real_gas, [
    S("Real gases differ from ideal gases. In the 2022 exam, a graph of P V against pressure showed a gas that was not "
      "ideal. For an ideal gas, P V is constant, so the line is horizontal, as Boyle's law says. Many students misread the graph, "
      "or did not decide whether the gas was ideal.", refs=['ex22q12', 'ar22q12', 'content'], covers=['G2', 'G1'], elements=[6], exam=['X22-12']),
    S("Real gases act ideally at high temperature and low pressure. At low temperatures, intermolecular forces pull particles "
      "away from the walls, so the actual pressure is lower than the ideal gas prediction, and the volume is a little smaller. "
      "Say that the prediction assumed ideal behaviour, which carbon dioxide does not show when cold.",
      refs=['ex23q14', 'ar23q14'], covers=['G2'], elements=[6], exam=['X23-14']),
    S("At very high pressure, the particles' own volume is no longer negligible, so a real gas takes up more room than predicted. "
      "Sulfur dioxide has a smaller molar volume than helium because it has stronger intermolecular forces: dipole-dipole forces, "
      "from the polar S O bonds, and bigger dispersion forces, from more electrons. Helium is nearly ideal.",
      refs=['ex25q16', 'ar25q16'], covers=['G2'], elements=[6, 2], exam=['X25-16']),
    S("A final kinetic theory point from 2021: oxygen molecules are smaller than nitrogen molecules although heavier. "
      "Oxygen's nuclear charge is greater, so electrons are held closer, and the shielding is similar, so the molecule is smaller. "
      "It is a periodic trends argument applied to a gas.", refs=['ex21q15', 'ar21q15'], covers=['G2', 'P10'], elements=[6, 5], exam=['X21-15']),
]),

# ------------------------------------------------------------------ Part 2: atoms
Scene('ie_shells', P2, 'Ionisation energies and shells', V.ie_graph, [
    S("Now atoms. The first ionisation energy is the energy needed to remove one mole of electrons from one mole of gaseous "
      "atoms. The state matters: an equation uses gas symbols, such as aluminium gas making aluminium plus gas plus an "
      "electron. The 2022 report gave only half the marks if the gas phase was not mentioned.",
      refs=['content', 'ex21q17', 'ex22q13', 'ar22q13', 'ar21q17', 'ex23q12', 'ar23q12'], covers=['P1'], elements=[4, 5], exam=['X21-17', 'X22-13', 'X23-12']),
    S("Successive ionisation energies rise, because the remaining electrons are held more tightly. The big jumps show shells. "
      "Magnesium has two small steps then a huge one: two outer electrons, then the third comes from an inner shell, closer "
      "to the nucleus with less shielding. A past graph could identify phosphorus from a jump after five electrons. The "
      "points are the values; not the lines joining them.", refs=['ex23q12', 'ar23q12', 'ex25q15', 'ar25q15', 'ex24q15', 'ar24q15'], covers=['P1', 'P4'], elements=[4, 5], exam=['X23-12', 'X25-15', 'X24-15']),
    S("For aluminium, the first three electrons come from the third shell, and the fourth from the second shell: a large jump. "
      "Say that the fourth electron is in a shell closer to the nucleus, with less shielding, so a much stronger "
      "electrostatic attraction. The third ionisation energy lies above the second, and well below the fourth. Do not confuse this "
      "with the trend across a period.", refs=['ex21q17', 'ar21q17', 'ex25q15', 'ar25q15', 'ar24q15'], covers=['P1', 'P9'], elements=[4, 5], exam=['X21-17', 'X25-15', 'X24-15']),
]),
Scene('spectra', P2, 'Energy levels and spectra', V.bohr_scene, [
    S("The Bohr model of the hydrogen atom has electrons in fixed energy levels, or shells. An electron stays in its level "
      "until it gains or loses a precise amount of energy. The levels are not evenly spaced and get closer together at higher energy.",
      refs=['content'], covers=['P3', 'P4'], elements=[4, 5], anim=3),
    S("An excited atom releases energy as a photon when an electron falls to a lower level. The photon's energy matches the "
      "gap, so each jump gives one wavelength, a line. That is why an element has a line spectrum, which identifies it. An "
      "absorption spectrum has dark lines at the same wavelengths. This is qualitative only.",
      refs=['content', 'ex21q16', 'ar21q16'], covers=['P2', 'P3'], elements=[4, 5], exam=['X21-16'], anim=3),
    S("The many lines of one element are evidence for several levels and for sub-shells within the shells: not one energy "
      "level per element, which is a common misconception. The modern picture has sub-shells, s, p and d, made of orbitals, with "
      "quantum numbers describing them. The course only asks you to mention them.", refs=['ar24q15', 'ex24q15', 'content'], covers=['P4', 'P2'], elements=[4, 5], exam=['X24-15'], anim=3),
]),
Scene('config', P2, 'Electron configurations', V.ladder, [
    S("Electron configurations use sub-shells. An s sub-shell holds two electrons, p holds six, and d holds ten. Fill from the lowest "
      "energy up. The order is one s, two s, two p, three s, three p, four s, then three d. The four s fills before three d.",
      refs=['content', 'ex22q11', 'ar22q11'], covers=['P4', 'P5'], elements=[4], exam=['X22-11']),
    S("Sulfur has sixteen electrons: one s two, two s two, two p six, three s two, three p four. In a p sub-shell, electrons spread into "
      "separate orbitals first before pairing. Use s, p, d notation, rather than shorthand, when it is asked for. And an excited "
      "state, such as one s two ... three p four four s one, goes back to the ground state by moving that outer electron to the lowest level.",
      refs=['ar22g', 'ex22q11', 'ex23q11', 'ar23q11'], covers=['P5'], elements=[4], exam=['X22-11', 'X23-11']),
    S("For d block atoms, four s fills before three d. Cobalt has twenty seven electrons: three p six, three d seven, four s two. "
      "In a positive ion, the four s electrons are lost first, so nickel two plus is three d eight. Copper is an exception, "
      "three d ten four s one. The course only asks for simple ions, but a report accepted both orders of writing three d and four s. "
      "For copper two plus, the correct answer is three d nine. One report also gave marks for three d eight four s one, because the course doesn't require transition metal ions, but don't rely on that: write three d nine.",
      refs=['ex22q11', 'ar22q11', 'ex23q11', 'ar23q11', 'ex25q15', 'ar25q15'], covers=['P5'], elements=[4], exam=['X22-11', 'X23-11', 'X25-15']),
]),
Scene('ions', P2, 'Ions and isoelectronic species', Slide('table', title='Ion charges from the periodic table', chip='Element 4 · predictions',
    head=['Group', 'Lose / gain', 'Ion', 'Configuration'], widths=[0.14, 0.26, 0.20, 0.32], size=24, counts=[1, 2, 3, 4, 5, 6], rows=[
        ['1', 'lose 1', 'Na⁺', '1s² 2s² 2p⁶ (neon)'], ['2', 'lose 2', 'Mg²⁺', '1s² 2s² 2p⁶ (neon)'],
        ['13', 'lose 3', 'Al³⁺', '1s² 2s² 2p⁶ (neon)'], ['15', 'gain 3', 'N³⁻', '1s² 2s² 2p⁶ (neon)'],
        ['16', 'gain 2', 'S²⁻', '1s² 2s² 2p⁶ 3s² 3p⁶ (argon)'], ['17', 'gain 1', 'Cl⁻', '1s² 2s² 2p⁶ 3s² 3p⁶ (argon)']]), [
    S("Main group atoms form ions with a full outer shell. Groups one, two and thirteen lose one, two and three electrons. "
      "Groups fifteen, sixteen and seventeen gain three, two and one. The group number tells you the valence electrons, and so the charge.",
      refs=['content', 'info_pt', 'ex21q16', 'ar21q16'], covers=['P7', 'P5'], elements=[4], exam=['X21-16']),
    S("Species with the same number of electrons are isoelectronic. Magnesium two plus, sodium plus, neon and nitride all have "
      "the neon configuration. To deduce a formula from isoelectronic two plus and three minus ions, balance the charges: "
      "three magnesium and two nitrogen make Mg three N two. Note: the number of electrons is what matters, not the element.",
      refs=['content', 'ex21q16', 'ar21q16', 'ex24q16', 'ar24q16'], covers=['P6', 'P7'], elements=[4, 5], exam=['X21-16', 'X24-16']),
    S("The ions P three minus, S two minus, chloride, potassium, calcium two plus and scandium three plus are all isoelectronic with "
      "argon: eighteen electrons. Write their configuration as one s two, two s two, two p six, three s two, three p six. "
      "A frequent error was giving the electron configuration of the neutral atom.", refs=['ex24q16', 'ar24q16', 'ex22q11', 'ar22q11'], covers=['P6', 'P5'], elements=[4], exam=['X24-16', 'X22-11']),
]),
Scene('radii', P2, 'Ionic radii', V.radius_ions, [
    S("Compare the ionic radii of isoelectronic ions. They all have eighteen electrons, which are the same arrangement and the "
      "same shielding. The only difference is the nuclear charge, from fifteen protons in phosphide to twenty one in scandium.",
      refs=['ex22q11', 'ar22q11', 'ex24q16', 'ar24q16'], covers=['P13', 'P6'], elements=[5, 4], exam=['X22-11', 'X24-16']),
    S("More protons pull the same electrons closer, so the radius falls from phosphide to scandium. State the number of "
      "protons, in the explanation: calcium has twenty, sulfur has sixteen. The same argument gives the highest ionisation energy "
      "for the scandium ion.", refs=['ar22q11', 'ar24q16', 'ex24q16'], covers=['P13', 'P10'], elements=[5], exam=['X22-11', 'X24-16']),
    S("Oxide and magnesium ions are isoelectronic too. The oxide ion is larger, because oxygen has only eight protons, and "
      "magnesium twelve. Always compare the ions, and not the atoms: students lost marks answering about oxygen and magnesium atoms. "
      "Cations are smaller than their atoms because they lose a shell or electrons; anions are larger than their atoms.",
      refs=['ex23q12', 'ar23q12', 'ar24q16'], covers=['P13', 'P6'], elements=[5, 4], exam=['X23-12', 'X24-16']),
]),
Scene('trends', P2, 'Periodic trends', V.trend_scene, [
    S("Across a period, left to right, the number of protons rises while the electrons are added to the same shell, so "
      "the shielding is about constant. Core charge increases. The outer electrons are pulled in closer: atomic radius "
      "decreases, while ionisation energy and electronegativity increase. These trends are on your information sheet, in the general "
      "periodic trends diagram.", refs=['info_pt', 'content', 'ex22q13', 'ar22q13'], covers=['P10', 'P13', 'P8'], elements=[5], exam=['X22-13']),
    S("Down a group, there are more shells. The outer electrons are further out, and shielded by more inner shells. So atomic "
      "radius increases, and ionisation energy and electronegativity decrease. Do not explain ionisation energy using "
      "electronegativity, and avoid personification. An atom does not want or desire anything.",
      refs=['info_pt', 'ar22q13', 'ar22g', 'ex22q13'], covers=['P10', 'P8', 'P12'], elements=[5], exam=['X22-13']),
    S("Reactivity follows. Metals lose electrons, so across a period they get less reactive as the electrons are held more "
      "tightly, while non-metals, which gain electrons, get more reactive. Down a group, metals get more reactive, and "
      "non-metals less. Among the period 3 metals, aluminium reacts least readily, because it has the highest nuclear charge of them and has to lose three "
      "electrons. Chlorine is the most electronegative, with the highest nuclear charge in period 3 and the strongest attraction for extra electrons.",
      refs=['content', 'ex21q17', 'ar21q17'], covers=['P11', 'P12', 'P9'], elements=[5], exam=['X21-17']),
]),
Scene('anomalies', P2, 'Anomalies in the trend', V.anomaly_graph, [
    S("Real data show the trends with anomalies. In period 3, the first ionisation energy generally rises, and the atomic radius falls. "
      "But aluminium's first ionisation energy is lower than magnesium's, though aluminium has more protons.",
      refs=['ex22q13', 'ar22q13', 'ex25q15', 'ar25q15'], covers=['P9', 'P10'], elements=[5], exam=['X22-13', 'X25-15']),
    S("The explanation uses sub-shells. Magnesium's outer electrons are in the 3s, and aluminium's outer electron is in a 3p. The 3p is "
      "slightly higher in energy and further out, and is shielded by the 3s electrons as well as the inner shells. So it is easier "
      "to remove. A good answer names the sub-shells, writes both configurations, and mentions the 12 and 13 protons.",
      refs=['ar22q13', 'ar25q15', 'ex25q15'], covers=['P9', 'P5', 'P4'], elements=[5, 4], exam=['X22-13', 'X25-15']),
    S("Radius, by contrast, falls steadily across the period: more protons and constant shielding. Down group one, "
      "ionisation energy falls, even though nuclear charge grows, because more full inner shells shield the valence electron. "
      "Use the data, and say both effects.", refs=['ar22q13', 'ex22q13', 'ex25q15'], covers=['P10', 'P13', 'P12'], elements=[5], exam=['X22-13', 'X25-15']),
]),
Scene('isotopes', P2, 'Isotopes and mass spectrometry', Slide('worked', title='Worked example 2: relative atomic mass from isotopes', chip='Element 5 · valence theory',
    q='Chlorine has two main isotopes: ³⁵Cl (75.8%) and ³⁷Cl (24.2%) (reference data, not from TASC). Find the relative atomic mass, and describe how a mass spectrometer shows this.',
    rows=[dict(s=0, t='A mass spectrometer separates isotopes by mass: each isotope gives a peak, and the height shows its abundance.', col='#b3c0d4', size=22),
          dict(s=1, t='Ar = (35 × 75.8 + 37 × 24.2) / 100 = (2653 + 895.4) / 100 = 35.48', col='#ffd166'),
          dict(s=1, sf='= 35.5 (using mass numbers); the information sheet gives 35.45 (exact isotope masses)', t='', gap=0),
          dict(s=2, t='The weighted average lies close to 35 because ³⁵Cl is about three times more abundant.', col='#b3c0d4', size=22)]), [
    S("Mass spectrometry is also used to analyse mixtures of isotopes. Isotopes of an element have the same number of "
      "protons but different numbers of neutrons. A mass spectrometer separates them by mass, and each gives a peak, whose height "
      "shows its abundance. The course notes this as new content compared with the earlier chemistry course.",
      refs=['content'], covers=['P14', 'S1'], elements=[5, 2]),
    S("Example: chlorine is seventy five point eight percent chlorine thirty five and twenty four point two percent chlorine thirty seven. "
      "The weighted average is about thirty five point five. The information sheet lists thirty five point four five, which uses exact "
      "isotope masses.", refs=['info_ar', 'content'], covers=['P14'], elements=[5],
      problem='Chlorine is 75.8% ³⁵Cl and 24.2% ³⁷Cl. What is its relative atomic mass?'),
    S("Check your answer is near the more abundant isotope. Question parts may ask you to read the relative abundances from peak "
      "heights, and the relative molecular mass of a molecule from its molecular ion, which we look at later.", refs=['content'], covers=['P14', 'S1'], elements=[5, 2]),
]),

# ------------------------------------------------------------------ Part 3: organic structures
Scene('func_groups', P3, 'Functional groups', Slide('table', title='Functional groups on the information sheet', chip='Element 1 · draw and name',
    head=['Class', 'Group', 'General formula', 'Example'], widths=[0.20, 0.20, 0.25, 0.27], size=22, counts=[2, 4, 6, 8], rows=[
        ['alkyl halides', '–F, –Cl, –Br, –I', 'CₙH₂ₙ₊₁X', '1-chlorobutane'], ['alcohols', '–OH', 'CₙH₂ₙ₊₂O', 'propan-1-ol'],
        ['aldehydes', '–CHO', 'CₙH₂ₙO', 'ethanal'], ['ketones', 'C=O between carbons', 'CₙH₂ₙO', 'pentan-3-one'],
        ['carboxylic acids', '–COOH', 'CₙH₂ₙO₂', 'butanoic acid'], ['esters', '–COO–', 'CₙH₂ₙO₂', 'methyl propanoate'],
        ['amines', '–NH₂', 'CₙH₂ₙ₊₃N', 'butan-2-amine'], ['amides', '–CONH₂', 'CₙH₂ₙ₊₁ON', 'ethanamide']]), [
    S("Organic molecules have a hydrocarbon skeleton and may contain functional groups. A functional group is an atom or group "
      "of atoms that gives a family of compounds its characteristic properties and reactions. The information sheet, in the "
      "aliphatic functional groups section, lists them with general formulas and examples. Learn to recognise each one.",
      refs=['content', 'info_fg', 'appendix'], covers=['O1', 'O4', 'A2'], elements=[1, 2]),
    S("Alkyl halides, with F, Cl, Br or I, and alcohols, with the hydroxyl group. Note that the general formula for "
      "a halide has one fewer hydrogen than the alkane.", refs=['info_fg'], covers=['O1', 'O2'], elements=[1]),
    S("Aldehydes have a carbonyl group at the end of a chain, and ketones have it in the middle, bonded to two carbons. Carboxylic "
      "acids have the carbonyl and a hydroxyl on the same carbon, and esters link an acid part and an alcohol part through an oxygen.",
      refs=['info_fg', 'ex25q12', 'ar25q12'], covers=['O1', 'O2'], elements=[1], exam=['X25-12']),
    S("Amines contain nitrogen, as N H two, and amides have the carbonyl next to the nitrogen. Amino acids, the building blocks of proteins, "
      "have both an amine group and a carboxylic acid group attached to a hydrocarbon chain. Name two groups: students who "
      "gave only carbonyl and hydroxyl for aspirin received half marks, because the groups are carboxylic acid and ester.",
      refs=['content', 'ar25q12', 'ex25q13', 'ar25q13'], covers=['O3', 'O1', 'O2'], elements=[1], exam=['X25-12', 'X25-13']),
]),
Scene('naming', P3, 'Naming organic compounds', Slide('table', title='Naming rules', chip='Element 1 · draw and name',
    head=['Step', 'Rule', 'Example'], widths=[0.10, 0.52, 0.30], size=24, counts=[1, 2, 3, 4, 5], rows=[
        ['1', 'Find the longest carbon chain that includes the functional group, and use the stem (meth-, eth-, prop-, but-…)', 'C₃: prop-'],
        ['2', 'Number from the end that gives the functional group the lowest number', 'propan-2-ol'],
        ['3', 'Suffix: -ol alcohol, -al aldehyde, -one ketone, -oic acid, -amine, -amide; -ene or -yne for double or triple bonds', 'but-1-ene'],
        ['4', 'Branches and halogens are prefixes (methyl, chloro…), in alphabetical order, each with a number', '2-chloro-3-methylpentane'],
        ['5', 'Esters: alkyl (from the alcohol) then alkanoate (from the acid)', 'ethyl ethanoate']]), [
    S("To name a compound, find the longest carbon chain that includes the functional group, and use the stem from the information "
      "sheet's organic chemistry section: meth, eth, prop, but, pent, hex, hept, oct, non and dec. The sheet also lists the "
      "side chains and the prefixes, such as di and tri.", refs=['info_org', 'content', 'ex23q11', 'ar23q11'], covers=['O2'], elements=[1], exam=['X23-11']),
    S("Number the chain from the end that gives the functional group the lowest number. Include the number: propan one ol, "
      "and propan two ol, are different compounds. Several students lost marks writing propanol, or leaving out a locant, "
      "and in 2023 a number of students put the chlorine on the fourth carbon.", refs=['ar24q13', 'ar23q11', 'ar21q12', 'ex21q12'], covers=['O2'], elements=[1], exam=['X24-13', 'X23-11', 'X21-12']),
    S("The suffix shows the class: ol for alcohols, al for aldehydes, one for ketones, oic acid for carboxylic acids, amine and "
      "amide. A double bond is ene, and a triple bond is yne. Compounds with two groups use a suffix for the main group, and a prefix for the other: "
      "hydroxy, amino, chloro.", refs=['content', 'info_fg', 'ex21q14', 'ar21q14'], covers=['O2', 'O4'], elements=[1], exam=['X21-14']),
    S("Branches and halogens go in front, in alphabetical order, each with its number, as in two chloro three methylpentanoic acid, "
      "which the 2023 exam asked students to draw. Write the hyphens and commas correctly. Cyclic compounds use cyclo, and "
      "the exam named one with two methyl groups on a five membered ring: one two dimethylcyclopentane.",
      refs=['ex23q11', 'ar23q11', 'ex22q14', 'ar22q14', 'info_org'], covers=['O2'], elements=[1], exam=['X23-11', 'X22-14']),
    S("An ester is named in two parts: the alkyl group from the alcohol, then the alkanoate from the acid. Ethanol and "
      "ethanoic acid give ethyl ethanoate. Propanol and methanoic acid give propyl methanoate. The 2025 exam also asked "
      "for pentyl propanoate and for an amide, butanamide.", refs=['ex25q13', 'ar25q13', 'ex22q16', 'ar22q16'], covers=['O2', 'O33'], elements=[1], exam=['X25-13', 'X22-16']),
]),
Scene('draw_alcohols', P3, 'Drawing structures: alcohols', mol_slide([
    (alk(3, right='OH'), 'propan-1-ol  (primary)', 'one carbon attached to the C–OH carbon'),
    (alk(3, subs={2: {'up': 'OH'}}), 'propan-2-ol  (secondary)', 'two carbons attached'),
    (alk(3, subs={2: {'up': 'OH', 'dn': 'CH3'}}, ), '2-methylpropan-2-ol  (tertiary)', 'three carbons attached'),
    (alk(2, right='NH2'), 'ethanamine  (amine)', '–NH₂'),
], 'Drawing structural formulae', 'Element 1 · draw and name', fs=17, per=1, cols=2,
    notes=['Draw EVERY hydrogen: “C–” is not the same as “C–H”. Count four bonds on each carbon',
           'Isomers have the same molecular formula (C₃H₈O) with the groups in different places',
           'Primary, secondary and tertiary: count the carbons attached to the carbon bearing the –OH',
           'Amines: –NH₂ on the chain. All hydrogens on the nitrogen are drawn too']), [
    S("Now drawing. Structural formulas show every atom and bond, with hydrogens included. Count the bonds: each carbon makes four. "
      "Markers repeat every year that C dash is not the same as C H. This is propan one ol, with the hydroxyl on the end "
      "carbon: a primary alcohol.", refs=['ar21g', 'ar22g', 'ar25g', 'content'], covers=['O2', 'O11'], elements=[1], exam=['X21-12']),
    S("Move the hydroxyl to the middle carbon and it is propan two ol, an isomer: the same molecular formula, C three H eight O, "
      "but a different structure. The carbon with the hydroxyl is attached to two other carbons, so it is a secondary alcohol.",
      refs=['content', 'ex21q14', 'ar21q14'], covers=['O2', 'O11'], elements=[1], exam=['X21-14']),
    S("Two methyl propan two ol is a tertiary alcohol, with three carbons attached to the carbon carrying the hydroxyl group. It is "
      "the isomer of butanol that cannot be oxidised, which a 2021 question asked students to draw.",
      refs=['ex21q14', 'ar21q14', 'content'], covers=['O11', 'O17', 'O2'], elements=[1, 3], exam=['X21-14']),
    S("A simple amine such as ethanamine has an N H two group on the chain. Amines and amides are limited to simple ones. "
      "Draw the hydrogens on the nitrogen as well. Be careful with orientation: when OH is drawn on the end of a chain, bond the carbon to "
      "the O, not to the H.", refs=['content', 'ar23q13', 'ar22q14'], covers=['O2', 'O1'], elements=[1], exam=['X23-13']),
]),
Scene('draw_carbonyl', P3, 'Drawing structures: carbonyl compounds', mol_slide([
    (alk(2, subs={2: {'up': '=O', 'dn': None}}), 'ethanal  (aldehyde)', 'C=O at the END of the chain'),
    (alk(3, subs={2: {'up': '=O', 'dn': None}}), 'propanone  (ketone)', 'C=O in the MIDDLE'),
    (alk(3, subs={3: {'up': '=O', 'dn': None}}, right='OH'), 'propanoic acid', '–COOH at the end'),
    (alk(5, subs={3: {'up': '=O', 'dn': None}, 4: {'up': None, 'dn': None}}, atoms={4: 'O'}), 'methyl propanoate  (ester)', 'acid part first in the chain, alcohol part after the O'),
], 'Drawing carbonyl compounds and esters', 'Element 1 · draw and name', fs=16, per=1, cols=2,
    notes=['An aldehyde: the carbonyl carbon is bonded to one hydrogen and one carbon (or two hydrogens in methanal)',
           'A ketone: the carbonyl carbon is bonded to two carbons. It has no hydrogen on the C=O carbon: a common error is to leave one on',
           'A carboxylic acid: the C=O and the O–H on the SAME carbon. Draw both',
           'An ester: C(=O)–O–C. Name it by the alcohol part (methyl) first, then the acid part (propanoate)']), [
    S("This is ethanal, an aldehyde. The carbonyl group is at the end of the chain, so the carbonyl carbon has a hydrogen. "
      "Propanone is the ketone with three carbons: the carbonyl is in the middle, and the carbonyl carbon has no hydrogen. A "
      "frequent mistake was to leave a hydrogen on the carbonyl carbon of propanone.",
      refs=['content', 'ar24q13', 'ex24q13', 'ex22q15', 'ar22q15'], covers=['O2', 'O1'], elements=[1], exam=['X24-13', 'X22-15']),
    S("A ketone like propanone has no hydrogen on the carbonyl carbon, which is why it cannot be oxidised further. Propanal, "
      "the aldehyde with the same formula, C three H six O, is an isomer of propanone. Say propanal, not propan one al.",
      refs=['ar24q12', 'ex24q12', 'content'], covers=['O2', 'O28', 'O23'], elements=[1], exam=['X24-12']),
    S("Propanoic acid has the carbonyl and the hydroxyl on the same end carbon. Its isomers methyl ethanoate and ethyl methanoate "
      "are esters. With the empirical formula C H two O, many students drew aldehydes and ketones. Remember the formula tells you "
      "the ratio, so ethanoic acid, with C two H four O two, also has the empirical formula C H two O.",
      refs=['ex24q14', 'ar24q14', 'ex24q12'], covers=['O2', 'O1'], elements=[1], exam=['X24-14', 'X24-12']),
    S("In an ester, the structure has C double bond O, then a single bond to an oxygen, then the alcohol part. Methyl propanoate has "
      "three carbons in the acid part and a methyl on the oxygen. In two thousand and twenty two, few students understood how an ester is "
      "built. A good check: hydrolysing it gives back an acid and an alcohol.",
      refs=['ex22q16', 'ar22q16', 'ex23q11', 'ar23q11', 'ex25q13'], covers=['O2', 'O33', 'O36'], elements=[1], exam=['X22-16', 'X23-11', 'X25-13']),
]),
Scene('isomers_benzene', P3, 'Empirical formulas, isomers and benzene', Slide('bullets', title='Formulas and isomers', chip='Element 1 · draw and name', size=25, counts=[1, 2, 3, 4, 5], items=[
    'Empirical formula: the simplest whole-number ratio. 1,2-dimethylcyclopentane is C₇H₁₄, so CH₂ (many students wrote C₇H₁₄)',
    'Molecular formula: the actual atoms. Ethanoic acid is C₂H₄O₂, empirical CH₂O',
    'Structural isomers: same molecular formula, different structure. Alcohols can be primary, secondary or tertiary',
    'Functional group isomers: propanal and propanone (C₃H₆O); propanoic acid and methyl ethanoate (C₃H₆O₂)',
    'Benzene C₆H₆: a flat, symmetrical ring, with all six C–C bonds equal in length and strength, between single and double. Delocalised electrons around the ring, drawn as a circle']), [
    S("Empirical formula is the simplest whole number ratio, which is different from the molecular formula. In 2022, most "
      "students could draw a cyclic compound but not write its empirical formula. Divide by the greatest common factor: C seven H "
      "fourteen becomes C H two.", refs=['ex22q14', 'ar22q14', 'ex24q12'], covers=['O2'], elements=[1], exam=['X22-14', 'X24-12']),
    S("A molecule with the empirical formula C H two O could have a molecular formula of C H two O, C two H four O two, "
      "or any multiple. The molecular formula needs the molar mass, which a mass spectrum provides.",
      refs=['ex24q14', 'ar24q14'], covers=['O2', 'S1'], elements=[1, 2], exam=['X24-14']),
    S("Isomers have the same molecular formula but different structures. Structural isomers have the groups in different "
      "places, such as the butanols. Functional group isomers have different groups altogether, such as an aldehyde and a ketone.",
      refs=['content', 'ex21q14', 'ex22q15'], covers=['O23', 'O2'], elements=[1], exam=['X21-14', 'X22-15']),
    S("When asked to draw isomers, change one thing at a time, and check the hydrogens. Isomers from addition reactions are "
      "important, which we meet in the reactions part.", refs=['content'], covers=['O23'], elements=[1]),
    S("Benzene is a flat, symmetrical ring of six carbons. The bonds between the carbons are all the same length, between single "
      "and double, with delocalised electrons shared around the whole ring, drawn as a circle. Do not say each carbon makes one and a half "
      "bonds, or that the bonds are one and a half times as long: examiners marked that wrong. This is why benzene is very stable, and it "
      "prefers substitution over addition.", refs=['content', 'ex21q13', 'ar21q13', 'ex25q12', 'ar25q12', 'ex23q16', 'ar23q16'], covers=['O8'], elements=[1, 2], exam=['X21-13', 'X25-12', 'X23-16']),
]),

# ------------------------------------------------------------------ Part 4: properties
Scene('imf', P4, 'Polarity and intermolecular forces', Slide('table', title='Boiling points and the forces behind them', chip='Element 2 · bond polarity',
    head=['Compound (reference data)', 'Boiling point', 'Strongest forces between molecules'], widths=[0.32, 0.16, 0.44], size=22, counts=[1, 2, 3, 4, 5, 6], rows=[
        ['propane, C₃H₈', '−42 °C', 'dispersion only: non-polar'],
        ['propanal, C₃H₆O', '49 °C', 'dipole-dipole (polar C=O) + dispersion'],
        ['propanone, C₃H₆O', '56 °C', 'dipole-dipole + dispersion'],
        ['propan-1-ol, C₃H₈O', '97 °C', 'hydrogen bonding (O–H) + dispersion'],
        ['propanoic acid, C₃H₆O₂', '141 °C', 'hydrogen bonding, strong (two sites)'],
        ['propanamide, C₃H₇NO', '213 °C', 'hydrogen bonding (N–H and C=O)']]), [
    S("Physical properties come from bond polarity and intermolecular forces. Alkanes are non-polar, and only have dispersion "
      "forces, which are weak and easily overcome, so they have low boiling points. Be specific: say dispersion forces, not weak "
      "forces, and not the general term van der Waals forces. A report asked chemistry students to name the force.",
      refs=['content', 'ex22q16', 'ar22q16', 'ar22g'], covers=['O9', 'O5'], elements=[2], exam=['X22-16']),
    S("Add a polar group and the boiling point rises. Alkyl halides and aldehydes have polar bonds, which give dipole-dipole forces "
      "as well as dispersion forces. Halogens are highly electronegative, so the carbon halogen bond is polar. Dipole-dipole forces "
      "are stronger than dispersion forces, so alkyl halides boil higher than the alkanes they came from.",
      refs=['content', 'ex24q13', 'ar24q13'], covers=['O5', 'O4'], elements=[2], exam=['X24-13']),
    S("Ketones also have dipole-dipole forces, from the polar C double bond O. They boil at a similar temperature to the aldehydes "
      "with the same formula, and a lot lower than alcohols.", refs=['content', 'ar24q13'], covers=['O4', 'O5'], elements=[2], exam=['X24-13']),
    S("Alcohols have hydrogen bonding, between the O H of one molecule and the oxygen of another. This is a much stronger "
      "intermolecular force, so alcohols have far higher melting and boiling points than alkanes of similar mass. The "
      "hydrogen bond is between molecules. Saying it is the O to H bond within a molecule loses marks.",
      refs=['content', 'ex22q16', 'ar22q16', 'ex25q12', 'ar25q12'], covers=['O9'], elements=[2], exam=['X22-16', 'X25-12']),
    S("Carboxylic acids can hydrogen bond at two sites, so their boiling points are higher again than alcohols with the same "
      "number of carbons. Polyalcohols, with several hydroxyl groups, such as ethane one two diol or glycerol, can form many hydrogen "
      "bonds per molecule, so their boiling points are much higher than simple alcohols.",
      refs=['content', 'ex24q13', 'ar24q13'], covers=['O12', 'O9'], elements=[2], exam=['X24-13']),
    S("Amines and amides also have hydrogen bonding, from the N H bonds, so they melt and boil higher than alkanes. "
      "The amino acid alanine has a high melting point, around two hundred and ninety seven degrees, because it has both an amine "
      "and a carboxylic acid group, and strong hydrogen bonds between molecules. The question was not about comparing it with lactic acid.",
      refs=['content', 'ex25q13', 'ar25q13'], covers=['O37', 'O3'], elements=[2, 1], exam=['X25-13']),
]),
Scene('solubility', P4, 'Solubility', Slide('cards', title='Solubility in water', chip='Element 2 · bond polarity', cols=2, counts=[1, 2, 3, 4], size=22, cards=[
    ('Alcohols, amines, amides', 'The polar group forms hydrogen bonds with water, so small molecules dissolve. As the non-polar chain gets longer, solubility falls: butan-1-ol is only slightly soluble, hexan-1-ol barely.', '#2dd4bf'),
    ('Alkanes', 'Non-polar, only dispersion forces. They cannot hydrogen bond with water, so they are insoluble.', '#fb923c'),
    ('Aldehydes, ketones, esters', 'Polar, but they have no O–H or N–H to give a hydrogen bond. Aldehydes are less soluble than alcohols; esters are insoluble and smell sweet or fruity.', '#a78bfa'),
    ('Big non-polar parts', 'Aspirin is only slightly soluble: its large non-polar benzene ring outweighs the polar groups. A less polar solvent like ethanol dissolves it better.', '#f15bb5')]), [
    S("Solubility follows polarity. Alcohols, amines and amides can form hydrogen bonds with water, so small ones dissolve well. "
      "The bond between the water molecule and the alcohol is the same kind as between water molecules. Drawing the hydrogen "
      "bonds between the molecules earned marks.", refs=['content', 'ex21q11', 'ar21q11'], covers=['O10', 'O38'], elements=[2], exam=['X21-11']),
    S("The non-polar chain gets in the way. Ethanol is more soluble than propan two ol, since the smaller chain means the hydrogen "
      "bonding has a greater influence. Saying that the hydroxyl is easier to reach did not earn marks. Alkanes, which are "
      "non-polar, are insoluble in water.", refs=['ex23q16', 'ar23q16'], covers=['O10', 'O4'], elements=[2], exam=['X23-16']),
    S("Aldehydes are less soluble than the alcohols they come from, because they can accept but cannot donate hydrogen bonds: they "
      "have no O H group. Esters are insoluble in water and have distinctive smells, which is why they are used in flavours and "
      "perfumes.", refs=['content', 'ex22q16', 'ar22q16'], covers=['O27', 'O35'], elements=[2], exam=['X22-16']),
    S("Aspirin dissolves poorly in water. Students saw the polar groups and thought of dipole-dipole forces, but the large non-polar "
      "aromatic ring is the reason. Two groups of molecules do not mix well when one is non-polar and big. And in a less polar solvent like "
      "ethanol, solubility increases.", refs=['ex25q12', 'ar25q12'], covers=['O10', 'O2'], elements=[2, 1], exam=['X25-12']),
]),
Scene('acids_ph', P4, 'Carboxylic acids as weak acids', Slide('bullets', title='Carboxylic acids', chip='Element 3 · equations', size=25, counts=[1, 2, 3, 4], items=[
    'Weak acids: they ionise only slightly, RCOOH ⇌ RCOO⁻ + H⁺, so their solutions have a HIGHER pH than a strong acid of the same concentration',
    'Monoacids have one –COOH (ethanoic acid); polyacids have more than one (ethanedioic acid, HOOC–COOH)',
    'Reactions of an acid: with carbonates, `2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2`',
    'With hydroxides and metal oxides, a salt and water; with reactive metals, a salt and hydrogen: `2CH3COOH + 2Na -> 2CH3COONa + H2`']), [
    S("Carboxylic acids are weak acids. They only ionise slightly in water, so a solution has fewer hydrogen ions than a "
      "strong acid of the same concentration, and a higher pH. Question after question needed this: ethanoic acid at zero point one "
      "mole per litre has a pH near three, not one.", refs=['content'], covers=['O29', 'O31'], elements=[2, 3], exam=['X22-16']),
    S("A monoacid has one carboxyl group, and a polyacid has more than one, like ethanedioic acid. Polyacids are needed for "
      "polyesters.", refs=['content'], covers=['O30', 'O25'], elements=[1, 3]),
    S("Carboxylic acids react with carbonates, giving a salt, water and carbon dioxide. In 2022, many students used the wrong "
      "formula for sodium carbonate, or gave the sodium salt without balancing, or left out states. Look at the formula on "
      "the sheet's reaction map, where the products are shown.", refs=['info_rx', 'ex22q16', 'ar22q16', 'content'], covers=['O32'], elements=[3], exam=['X22-16']),
    S("They react with hydroxides and metal oxides to give a salt and water, and with reactive metals like sodium to give a salt "
      "and hydrogen. Carboxylic acids and alcohols both react with sodium, giving hydrogen. A student predicted that more hydrogen atoms "
      "in the acid means more gas: wrong, because one hydroxyl group per molecule reacts, so equal sodium gives equal hydrogen.",
      refs=['content', 'ex23q15', 'ar23q15'], covers=['O32', 'O13'], elements=[3, 2], exam=['X23-15']),
]),

# ------------------------------------------------------------------ Part 5: reactions
Scene('rx_map', P5, 'The map of reactions', V.reaction_map, [
    S("This is the reaction map from your information sheet, in the section on some organic reactions of aliphatic compounds. "
      "Learn to read it. Alkenes add hydrogen to give alkanes, add steam to give alcohols, and add hydrogen halides to give alkyl "
      "halides. Alcohols lose water, with concentrated sulfuric acid, to give alkenes, and alkyl halides give alcohols with dilute sodium hydroxide.",
      refs=['info_rx', 'content', 'ex25q14', 'ar25q14'], covers=['O4', 'O21', 'O7'], elements=[3], exam=['X25-14']),
    S("Primary alcohols oxidise to aldehydes with a milder oxidiser, such as acidified dichromate, then to carboxylic acids. "
      "Secondary alcohols oxidise to ketones. The sheet shows an oxidation with an excess of a stronger oxidiser such as acidified "
      "permanganate going directly to the acid.", refs=['info_rx', 'content', 'ex21q11', 'ar21q11'], covers=['O14', 'O15', 'O16', 'O26'], elements=[3], exam=['X21-11']),
    S("Alcohols and carboxylic acids make esters, with concentrated sulfuric acid, and esters hydrolyse back. Alkyl "
      "halides react with ammonia to give amines. The 2025 exam gave a scheme from propan one ol, and most students got at least "
      "seven of nine marks, by following the sheet. The copper catalyst was the only reactant not on the sheet.",
      refs=['info_rx', 'ex25q14', 'ar25q14', 'content'], covers=['O33', 'O4', 'O36'], elements=[3], exam=['X25-14']),
    S("Finally, alkenes polymerise with a catalyst to make addition polymers. The sheet also shows an alcohol reacting with an "
      "active metal to give an alkoxide and hydrogen, and a carboxylic acid with a base, carbonate or metal. Use the sheet, and write the "
      "formulas of the products, including charges for ionic products.", refs=['info_rx', 'ar25q14'], covers=['O24', 'O13', 'O32'], elements=[3], exam=['X25-14']),
]),
Scene('rx_alkane_alkene', P5, 'Alkanes, alkenes and halogens', Slide('table', title='Alkanes and alkenes', chip='Element 3 · equations',
    head=['Reaction', 'Type', 'Equation (condensed formulas)'], widths=[0.24, 0.16, 0.50], size=21, counts=[1, 2, 3, 4, 5], rows=[
        ['Alkane + Cl₂ (UV light)', 'substitution', '`CH4 + Cl2 -> CH3Cl + HCl`'],
        ['Alkene + Br₂ (rapid, no light)', 'addition', '`CH2=CH2 + Br2 -> CH2BrCH2Br`  (bromine water decolourised)'],
        ['Alkene + HBr, asymmetric', 'addition', '`CH3CH=CH2 + HBr -> CH3CHBrCH3` (major) or `CH3CH2CH2Br`'],
        ['Complete combustion', 'oxidation', '`C3H8 + 5O2 -> 3CO2 + 4H2O`'],
        ['Incomplete combustion', 'oxidation', '`2C3H8 + 7O2 -> 6CO + 8H2O` (or C and CO)']]), [
    S("Alkanes are saturated, with only single bonds. They react with halogens by substitution, replacing a hydrogen with a "
      "halogen, and need ultraviolet light. Methane and chlorine make chloromethane and hydrogen chloride. Alkyl halides then "
      "undergo substitution more readily than the alkanes they came from.", refs=['content'], covers=['O18', 'O19', 'O6'], elements=[3]),
    S("Alkenes are unsaturated, so they undergo addition reactions across the double bond. They react immediately with "
      "bromine, and the brown colour disappears. Alkanes only react slowly, in light. That is the test the 2022 exam described, "
      "to tell an alkene from other hydrocarbons, and the formula showed it could not be an alkyne.",
      refs=['content', 'ex22q15', 'ar22q15'], covers=['O18', 'O21'], elements=[3, 2], exam=['X22-15']),
    S("When an asymmetric molecule such as a hydrogen halide or steam adds to an asymmetric alkene, two isomers are possible. "
      "Propene and hydrogen bromide give 2-bromopropane as the main product, and 1-bromopropane as the minor one. Name "
      "both isomers. Adding steam gives propan two ol or propan one ol.", refs=['content', 'ex24q13', 'ar24q13', 'info_rx'], covers=['O22', 'O23', 'O21'], elements=[3, 1], exam=['X24-13']),
    S("Hydrocarbons burn. With excess oxygen, the products are carbon dioxide and water. With insufficient oxygen, incomplete "
      "combustion produces carbon monoxide, or soot, which is carbon, as well as water. Balance the equation, and include states.",
      refs=['content'], covers=['O20'], elements=[3]),
    S("In a 2024 question, the printed text asked for chloropropane from propene with one molecule of chlorine. But chlorine adds across "
      "the double bond of propene to give dichloropropane, and the report said propane was meant, which would give two chloropropane "
      "isomers by substitution. That part was removed, and later parts were marked with error carried forward. If a question "
      "seems inconsistent, state your assumption and carry on.",
      refs=['ar24g', 'ar24q13', 'ex24q13'], covers=['O21', 'O18'], elements=[3], exam=['X24-13']),
]),
Scene('rx_halide', P5, 'Alkyl halides and alcohols', Slide('table', title='Alkyl halides and alcohols', chip='Element 3 · equations',
    head=['Reaction', 'Equation (condensed formulas)'], widths=[0.34, 0.56], size=21, counts=[1, 2, 3, 4, 5, 6], rows=[
        ['Alkyl halide + dilute NaOH(aq): substitution → primary alcohol', '`CH3CH2CH2Cl + NaOH -> CH3CH2CH2OH + NaCl`'],
        ['… secondary alcohol (halogen on a middle carbon)', '`CH3CHClCH3 + NaOH -> CH3CHOHCH3 + NaCl`'],
        ['Alcohol + sodium (alkoxide + hydrogen)', '`2CH3CH2OH + 2Na -> 2CH3CH2ONa + H2`'],
        ['Alcohol + carboxylic acid (conc. H₂SO₄, reversible): ester', '`CH3COOH + CH3CH2OH <=> CH3COOCH2CH3 + H2O`'],
        ['Dehydration (conc. H₂SO₄): alkene', '`CH3CH2OH -> CH2=CH2 + H2O`'],
        ['Alkyl halide + NH₃: amine', '`CH3CH2Br + 2NH3 -> CH3CH2NH2 + NH4Br`']]), [
    S("Alkyl halides undergo substitution with dilute sodium hydroxide: the halogen is replaced by the hydroxyl group. "
      "1-chloropropane makes propan-1-ol, a primary alcohol, and 2-chloropropane makes propan-2-ol, a secondary one. The "
      "sodium chloride is the second product, which many students left out.",
      refs=['info_rx', 'content', 'ex24q13', 'ar24q13'], covers=['O7', 'O6', 'O4'], elements=[3], exam=['X24-13']),
    S("A tertiary halide, with the halogen on a carbon holding three other carbons, gives a tertiary alcohol. Draw the "
      "structural equation, and read the question: when it asks for only the product of the other isomer, do not write a full equation.",
      refs=['ar24q13', 'content'], covers=['O7', 'O11'], elements=[3, 1], exam=['X24-13']),
    S("Alcohols react with sodium to give hydrogen and an alkoxide, the salt of an alcohol: ethoxide here. The "
      "reaction with sodium is a test for an O H group, but both alcohols and carboxylic acids react.",
      refs=['info_rx', 'ex21q14', 'ar21q14', 'ex23q15', 'ar23q15'], covers=['O13'], elements=[3], exam=['X21-14', 'X23-15']),
    S("An alcohol and a carboxylic acid make an ester and water, with a concentrated sulfuric acid catalyst. This is "
      "an equilibrium reaction, so use the double arrow, and include the acid catalyst. Few students in 2022 gave the "
      "catalyst, or recognised that esterification is reversible. Ethanol and ethanoic acid make ethyl ethanoate.",
      refs=['ex22q16', 'ar22q16', 'content'], covers=['O13', 'O33', 'O34'], elements=[3], exam=['X22-16']),
    S("An alcohol heated with concentrated sulfuric acid loses water to give an alkene. In 2021 this was asked for compound "
      "A, a butanol derivative, and the tertiary isomer of A that cannot be oxidised was also asked. Fuels can be made from "
      "organic sources using addition, oxidation and esterification, such as biodiesel: a brief treatment only.",
      refs=['ex21q14', 'ar21q14', 'info_rx', 'content'], covers=['O34', 'O17', 'O4'], elements=[3], exam=['X21-14']),
    S("Halides react with ammonia to give amines, according to the sheet. Amines and amides are limited to simple ones in this "
      "course, such as ethanamine and ethanamide.", refs=['info_rx', 'content'], covers=['O4', 'O1'], elements=[3]),
]),
Scene('oxidation', P5, 'Oxidising alcohols', Slide('table', title='Oxidation of alcohols', chip='Element 3 · equations',
    head=['Alcohol', 'Oxidiser', 'Product', 'Further?'], widths=[0.18, 0.34, 0.20, 0.18], size=22, counts=[1, 2, 3, 4], rows=[
        ['Primary', 'Cu catalyst (heat) or LIMITED acidified dichromate', 'aldehyde', 'Yes, to acid'],
        ['Primary', 'EXCESS acidified permanganate or dichromate', 'carboxylic acid', 'No'],
        ['Secondary', 'acidified dichromate or permanganate', 'ketone', 'No: no H on the C=O carbon'],
        ['Tertiary', 'any', 'no reaction', 'No H on the C–OH carbon']]), [
    S("Oxidation depends on the type of alcohol. A primary alcohol is oxidised to an aldehyde, with a copper catalyst when heated "
      "or with limited acidified dichromate. The aldehyde can be oxidised further to a carboxylic acid. Pure ethanal is best made "
      "with the copper catalyst, because the aldehyde does not reach the acid. With excess dichromate, the acid forms.",
      refs=['content', 'info_rx', 'ex21q11', 'ar21q11'], covers=['O14', 'O26'], elements=[3], exam=['X21-11']),
    S("A stronger oxidiser, such as acidified permanganate in excess, takes a primary alcohol straight to the carboxylic acid. Ethanol "
      "becomes ethanoic acid. The 2023 question asked for the organic products from ethanol and from propan-2-ol with acidified "
      "permanganate: ethanoic acid and propanone.", refs=['content', 'ex23q16', 'ar23q16'], covers=['O15', 'O26'], elements=[3], exam=['X23-16']),
    S("A secondary alcohol is oxidised to a ketone. Propan-2-ol makes propanone. The ketone has no hydrogen on the carbonyl carbon, "
      "so it cannot be oxidised any further. A common error was keeping a hydrogen on the carbonyl carbon of propanone.",
      refs=['ex23q16', 'ar24q13', 'ex24q13', 'content'], covers=['O16', 'O28'], elements=[3], exam=['X23-16', 'X24-13']),
    S("A tertiary alcohol has no hydrogen on the carbon bearing the hydroxyl, so it is not oxidised. To compare the products, "
      "choose a physical property: propanoic acid boils higher than propanone, because acid molecules hydrogen bond to each other, but "
      "propanone has only dipole-dipole forces. Do not discuss reactivity when asked for a physical property.",
      refs=['content', 'ex24q13', 'ar24q13', 'ex21q14'], covers=['O17', 'O11', 'O9'], elements=[3, 2], exam=['X24-13', 'X21-14']),
]),
Scene('hydrolysis', P5, 'Esters, hydrolysis and amines', Slide('table', title='Esters, acids and amides', chip='Element 3 · equations',
    head=['Reaction', 'Equation (condensed formulas)'], widths=[0.34, 0.56], size=21, counts=[1, 2, 3, 4], rows=[
        ['Ester hydrolysis (acid catalyst): acid + alcohol', '`CH3COOCH2CH3 + H2O <=> CH3COOH + CH3CH2OH`'],
        ['Alkaline hydrolysis: salt + alcohol (goes to completion)', '`CH3COOCH2CH3 + NaOH -> CH3COONa + CH3CH2OH`'],
        ['Ester smells', 'ethyl butanoate: pineapple; octyl ethanoate: orange (reference)'],
        ['Amine behaves as a base', '`CH3CH2NH2 + H2O <=> CH3CH2NH3^+ + OH^-`']]), [
    S("Esters hydrolyse, the reverse of esterification. With an acid catalyst, hydrolysis gives the carboxylic acid and the "
      "alcohol, and it is reversible. In alkaline hydrolysis, with sodium hydroxide, the products are the sodium salt of the acid and "
      "the alcohol. It goes to completion, because the acid is neutralised.", refs=['content', 'info_rx'], covers=['O36', 'O33'], elements=[3]),
    S("The salt is sodium ethanoate, written C H three C O O minus Na plus, as on the sheet. Remember that esters are "
      "insoluble in water and have distinctive smells, such as pineapple. That is why esters feature in flavours and "
      "perfumes.", refs=['info_rx', 'content', 'ex22q16'], covers=['O35', 'O36', 'O32'], elements=[3, 2], exam=['X22-16']),
    S("Amines contain a lone pair on nitrogen, so they act as bases and accept protons from water. They are the only organic "
      "compounds here which do. Amides do not behave like this. Amino acids have both groups, so they act as both an acid "
      "and a base.", refs=['content', 'ex25q13'], covers=['O3', 'O4', 'O37'], elements=[1, 3], exam=['X25-13']),
    S("An ester is easy to identify from IR: a carbonyl peak with no O H. That is what the question about ethyl ethanoate "
      "used, to tell the ester from the ethanol left in the product mixture. We return to this in the analysis part.",
      refs=['ex22q16', 'ar22q16'], covers=['O36', 'S2'], elements=[2, 3], exam=['X22-16']),
]),
Scene('polymers', P5, 'Polymers', mol_slide([
    (alk(6, subs={2: {'dn': 'CH3'}, 4: {'dn': 'CH3'}, 6: {'dn': 'CH3'}}, left='~', right='~'), 'poly(propene): addition polymer, three monomer units', 'monomer: `CH3CH=CH2`'),
], 'Addition and condensation polymers', 'Element 1 · polymers', fs=17, per=1, cols=1,
    notes=['Addition polymers: the C=C of each alkene monomer opens and joins to the next. The only product is the polymer. Show three units and that the chain continues (~)',
           'Condensation polymers: two different groups react and a small molecule, usually water, is lost. A polyester is made from a polyacid and a polyalcohol (or a hydroxy acid like lactic acid)',
           'n HOOC–COOH + n HOCH₂CH₂OH → [–OC–CO–OCH₂CH₂O–]n + 2n H₂O      n HOCH(CH₃)COOH → [–OCH(CH₃)CO–]n + n H₂O (PLA)']), [
    S("Alkenes form addition polymers. The double bond of each monomer opens, and the molecules link into a long chain, with no "
      "other product. Here is propene: draw three repeat units, with the methyl groups on alternate carbons, and show "
      "the chain continuing at both ends. Marks were lost for each error, and for not showing that it continues.",
      refs=['content', 'ex22q17', 'ar22q17', 'ex21q13', 'ar21q13'], covers=['O24'], elements=[1], exam=['X22-17', 'X21-13']),
    S("Condensation polymers form when monomers join and lose a small molecule such as water. Polyesters are made from a polyalcohol, "
      "a diol, and a polyacid, a diacid. The link is the ester group. PET, the polymer of water bottles, is a polyester, and the "
      "2023 question asked whether it was addition or condensation: condensation. Many wrote addition.",
      refs=['content', 'ex23q13', 'ar23q13'], covers=['O25', 'O24'], elements=[1], exam=['X23-13']),
    S("Lactic acid has a hydroxyl and a carboxyl group, so it can react with itself to make polylactic acid, a polyester. "
      "The type is condensation, justified by the loss of water and the ester links. Drawing it, the repeat unit has the ester "
      "group, with no stray oxygen on the ends. And working backwards from a polymer segment to the monomer, break at the ester link and add "
      "back the water. The monomer is two hydroxypropanoic acid.",
      refs=['ex21q11', 'ar21q11', 'ex22q17', 'ar22q17', 'ex25q13', 'ar25q13', 'content'], covers=['O25', 'O24'], elements=[1, 3], exam=['X21-11', 'X22-17', 'X25-13']),
    S("Green polymer chemistry is a context in the course. Many synthetic polymers come from fossil fuels and do not "
      "biodegrade. Polylactic acid is biodegradable, and made from plants, but there are issues of cost and using food crops. "
      "Research aims for sustainable polymers from renewable sources and waste.", refs=['appendix'], covers=['A3', 'O24'], elements=[1]),
]),
Scene('we_identify', P5, 'Worked example: a reaction puzzle', Slide('worked', title='Worked example 3: identify the compounds', chip='Element 2 · analytical data',
    q='Compound P (C₅H₁₀) decolourises bromine water at once. Reacting P with steam (H⁺ catalyst) gives two products, Q and R. Q is oxidised by acidified dichromate to a ketone. R is oxidised first to an aldehyde and then an acid. Identify P, Q and R.',
    size=23,
    rows=[dict(s=0, t='Fast bromine decolouration: unsaturated, an alkene (C₅H₁₀ fits CₙH₂ₙ, so not an alkyne).', col='#eef2f8'),
          dict(s=1, t='Two products with steam: the double bond is not in the middle of the chain (asymmetric).', col='#eef2f8'),
          dict(s=2, t='Q gives a ketone: secondary alcohol, so Q is pentan-2-ol → pentan-2-one.', col='#ffd166'),
          dict(s=2, t='R gives aldehyde then acid: primary alcohol, so R is pentan-1-ol → pentanal → pentanoic acid.', col='#ffd166'),
          dict(s=3, t='So P is pent-1-ene:  `CH2=CHCH2CH2CH3`  (C=C at the end of the chain)', col='#9bde7e'),
          dict(s=3, t='`CH2=CHCH2CH2CH3 + H2O -> CH3CHOHCH2CH2CH3` (main)  or  `HOCH2CH2CH2CH2CH3`', col='#9bde7e', size=22)]), [
    S("Worked example three. Compound P, C five H ten, decolourises bromine water immediately. That means it is an alkene: "
      "unsaturated. The formula fits C n H two n, so it is not an alkyne. Many students noticed the reaction but did not use "
      "the formula.", refs=['ex22q15', 'ar22q15', 'content'], covers=['O21', 'O23', 'S4'], elements=[1, 2, 3], exam=['X22-15'],
      problem='C₅H₁₀ decolourises bromine water. With steam it gives two alcohols: one oxidised to a ketone, the other to an aldehyde then an acid. Identify the compounds.'),
    S("Steam gives two products. A symmetrical alkene would give just one, so the double bond is not in the middle. A report "
      "said many students repeated the stimulus without relating it to the position of the double bond.",
      refs=['ar22q15', 'ex22q15'], covers=['O22', 'O23'], elements=[1, 2], exam=['X22-15']),
    S("The alcohol that gives a ketone is secondary: pentan two ol. The one that gives an aldehyde and then an acid is primary: "
      "pentan one ol. Use the oxidation results to classify each alcohol.", refs=['content', 'ar22q15'], covers=['O11', 'O14', 'O16', 'O26'], elements=[2, 3], exam=['X22-15']),
    S("Both alcohols come from pent one ene, with the double bond at the end of the chain. Steam adds to either end: the "
      "main product is the secondary alcohol, and the minor the primary. Name and draw, with all hydrogens, and carry errors "
      "forward carefully: markers allowed error carried forward.", refs=['content', 'ar22q15'], covers=['O22', 'O23', 'O2'], elements=[1, 3], exam=['X22-15']),
]),

# ------------------------------------------------------------------ Part 6: analysis
Scene('ir', P6, 'Infrared spectroscopy', V.ir_scene, [
    S("Infrared spectroscopy identifies functional groups from the absorption bands. The information sheet gives the "
      "frequencies of important IR stretching vibrations in a table, with three rows. An alcohol O H absorbs strongly and broadly "
      "between thirty six fifty and thirty two hundred. Quote the wavenumber and the bond.",
      refs=['info_rx', 'content', 'ex21q12', 'ex22q16', 'ar22q16'], covers=['S2'], elements=[2], exam=['X21-12', 'X22-16']),
    S("A carboxylic acid has a very broad O H, from thirty three hundred to twenty five hundred, and a strong carbonyl C double "
      "bond O, between seventeen eighty and sixteen fifty. Both are needed. In 2023 the answer was ethanoic acid, with a strong "
      "narrow peak near seventeen hundred, and a very broad peak from thirty three hundred to twenty five hundred.",
      refs=['info_rx', 'ex23q16', 'ar23q16', 'ex24q14', 'ar24q14'], covers=['S2'], elements=[2], exam=['X23-16', 'X24-14']),
    S("An ester has a carbonyl band but no O H. In the ethyl ethanoate question, one spectrum had the carbonyl near "
      "seventeen fifty, so it was the ester, and the other had the broad O H, so it was ethanol. Students disregarded the clue that "
      "the acid had been removed.", refs=['ex22q16', 'ar22q16'], covers=['S2', 'O36'], elements=[2], exam=['X22-16']),
    S("An aldehyde or a ketone shows a carbonyl band and no O H. Because the sheet's table is short, you often need "
      "other evidence. Do not disregard the broad O H just because it does not match your first structure: students who "
      "had drawn aldehydes ignored it.", refs=['ar24q14', 'ex24q14', 'ex21q12'], covers=['S2', 'S4'], elements=[2], exam=['X24-14', 'X21-12']),
]),
Scene('ms', P6, 'Mass spectrometry and X-ray crystallography', V.ms_scene, [
    S("In mass spectrometry, a molecule loses an electron to form a molecular ion. Its peak is at the highest mass, and its "
      "mass to charge ratio equals the relative molecular mass. Propan-1-ol, C three H eight O, has a molecular ion at sixty, "
      "which you can calculate from the atomic masses.",
      refs=['content', 'ex25q14', 'ar25q14', 'info_ar'], covers=['S1'], elements=[2], exam=['X25-14'],
      problem='What is the m/z of the molecular ion of propan-1-ol, C₃H₈O?'),
    S("The molecule also breaks into fragments, which appear at lower mass. For propan-1-ol, the base peak, the tallest, is at "
      "thirty one, which is C H two O H plus. A difference of fifteen is a methyl group, and seventeen is a hydroxyl. "
      "Instrument details are not examined.", refs=['ar25q14', 'content'], covers=['S1'], elements=[2], exam=['X25-14']),
    S("Use both spectra to confirm a structure. For propan one ol versus propanoic acid: propanoic acid has a molar mass of "
      "seventy four, so a molecular ion at sixty, with no strong carbonyl absorption in the IR, tells you it is the alcohol. "
      "A good answer quotes the wavenumbers, and the m over z values, with the structure.",
      refs=['ex25q14', 'ar25q14'], covers=['S1', 'S2', 'S4'], elements=[2], exam=['X25-14']),
    S("X-ray crystallography finds the arrangement of atoms in a crystal from the way X rays diffract, and so identifies simple "
      "molecular structures. Structure determination often needs evidence from more than one technique: IR for groups, mass spectrometry "
      "for the mass, and sometimes crystallography for the full structure. The course notes that features of the instruments are not studied.",
      refs=['content'], covers=['S3', 'S4'], elements=[2]),
]),
Scene('we_spectra', P6, 'Worked example: combining evidence', Slide('worked', title='Worked example 4: an unknown compound', chip='Element 2 · analytical data',
    q='An unknown compound has the formula C₃H₆O₂. Its infrared spectrum has a very broad absorption from 3300 to 2500 cm⁻¹ and a strong absorption at 1710 cm⁻¹. Its mass spectrum has a molecular ion at m/z 74. Identify it, and explain why two isomers are ruled out.',
    rows=[dict(s=0, t='M(C₃H₆O₂) = 3(12.01) + 6(1.008) + 2(16.00) = 74.08 g mol⁻¹: matches m/z 74', col='#ffd166'),
          dict(s=1, t='IR: 3300–2500 very broad = carboxylic acid O–H;   1710 = C=O.   Both together: –COOH', col='#eef2f8'),
          dict(s=2, t='Identity: propanoic acid,  `CH3CH2COOH`', col='#9bde7e'),
          dict(s=2, t='Ruled out: methyl ethanoate and ethyl methanoate (esters, C=O but NO broad O–H)', col='#eef2f8', size=23),
          dict(s=3, t='Name the bond, give the wavenumbers, then say why the alternatives fail.', col='#f15bb5', size=23)]), [
    S("Worked example four. An unknown has the formula C three H six O two. The mass spectrum shows a molecular ion at seventy "
      "four, which matches the molar mass, seventy four point oh eight. So the formula is confirmed as the molecular formula.",
      refs=['info_ar', 'content', 'ar25q14'], covers=['S1', 'S4'], elements=[2], problem='An unknown C₃H₆O₂ has IR bands at 3300–2500 (very broad) and 1710 cm⁻¹ and M⁺ at m/z 74. Identify it.'),
    S("The IR spectrum shows a very broad absorption from thirty three hundred to twenty five hundred, the O H of a "
      "carboxylic acid, and a strong peak at seventeen ten, a carbonyl. Together, they indicate a carboxylic acid group.",
      refs=['info_rx', 'ar23q16', 'ar25q14'], covers=['S2', 'S4'], elements=[2], exam=['X23-16']),
    S("The compound is propanoic acid. The esters methyl ethanoate and ethyl methanoate have the same formula and a carbonyl, but "
      "no broad O H band, so they are ruled out. Many students in 2024 ignored the hydroxyl band, because it did not match their "
      "drawn isomers.", refs=['ar24q14', 'ex24q14', 'ar25q14'], covers=['S2', 'S4', 'O23'], elements=[2, 1], exam=['X24-14']),
    S("The method: work out the formula with the mass spectrum, identify groups with the infrared, and check each alternative. "
      "Always quote wavenumbers. This shows that structures often need more than one technique.", refs=['content', 'ar25q14'], covers=['S4', 'S2', 'S1'], elements=[2], exam=['X25-14']),
]),

# ------------------------------------------------------------------ finish
Scene('exam_tips', P7, 'Tips for tests and the exam', Slide('tips', title='Tips from examiners', counts=[2, 4, 6, 8], tips=[
    'Draw EVERY hydrogen: C– is not C–H.\nCount four bonds on each carbon',
    'Name with locants: propan-1-ol, not\npropanol. Check the suffix and prefixes',
    'Name the force: dispersion, dipole-dipole,\nhydrogen bonding BETWEEN molecules',
    'IR: quote the wavenumber and the bond;\nalcohol O–H and acid O–H differ',
    'Ionisation energy: gaseous atoms, with\nstate symbols in the equation',
    'Compare ions, not atoms. Give the number\nof protons, and the shielding',
    'No personification: atoms do not\n“want” or “desire” electrons',
    'Ideal gas: negligible particle volume,\nno forces. Never “no mass”']), [
    S("Finally, technique for tests and the exam, from examiners' reports. One: draw every hydrogen. Two: name compounds with "
      "locants, so propan one ol, not propanol, and check the suffix and the prefixes.",
      refs=['ar21g', 'ar22g', 'ar24q13', 'ar25g']),
    S("Three: name the intermolecular force, dispersion, dipole-dipole or hydrogen bonding, and remember a hydrogen bond is "
      "between molecules. Four: for infrared spectra, quote the wavenumber and the bond, and tell an alcohol from an acid O H.",
      refs=['ar22q16', 'ar22g', 'ar25q12', 'ar23q16', 'ar25q14']),
    S("Five: ionisation energy is for gaseous atoms, and the equation needs state symbols. Six: compare ions, not atoms, and use "
      "the number of protons. Seven: avoid personification. Eight: an ideal gas has negligible particle volume and no "
      "intermolecular forces, never no mass.", refs=['ar22q13', 'ar23q12', 'ar24q16', 'ar22g', 'ar23q14']),
]),
Scene('more_tips', P7, 'More examiner tips', Slide('tips', title='More tips from examiners', start=9, counts=[4, 8], tips=[
    'Benzene: delocalised electrons around the\nring, equal bonds. Not “1.5 bonds”',
    'Esterification needs an acid catalyst and\nis reversible: use ⇌',
    'Polymers: show the chain continues. Polyesters\nare condensation polymers',
    'Show what was asked: empirical formula\nnot molecular; physical not chemical',
    'Use ALL the evidence: a “show that” value,\nthe IR, the stem of the question',
    'Explain trends with core charge, shells\nand shielding, not electronegativity',
    'Convert °C to K in every gas law. Check\nR matches the pressure unit',
    'Isomers: same formula, different structure.\nName all the products of an addition']), [
    S("More tips. Nine: benzene has delocalised electrons around the ring and equal bonds, not one and a half bonds. Ten: "
      "esterification needs an acid catalyst and is reversible. Eleven: show that a polymer chain continues, and remember "
      "polyesters are condensation polymers. Twelve: answer what was asked, such as the empirical formula and a physical property.",
      refs=['ar25q12', 'ar22q16', 'ar25q13', 'ar22q14', 'ar24q13']),
    S("Thirteen: use all the evidence in the stem and the spectra. Fourteen: explain trends with core charge, shells and "
      "shielding. Fifteen: convert degrees Celsius to kelvin for every gas law, and match R to the pressure unit. Sixteen: "
      "isomers have the same formula and different structures, and addition to an asymmetric alkene can make two products.",
      refs=['ar22q13', 'ar22q12', 'ar24q14', 'ar22q15']),
]),
Scene('summary', P7, 'Summary', Slide('summary', title='Criterion 7 in one screen', chips=[
    ('PV = nRT', '1'), ('P₁V₁/T₁ = P₂V₂/T₂', '1'), ('ideal: no forces, tiny volume', '1'), ('real gas: low T, high P', '1'),
    ('1s² 2s² 2p⁶ …', '2'), ('isoelectronic', '2'), ('core charge', '2'), ('shielding', '2'), ('ionisation energy jumps', '2'),
    ('functional groups', 'p'), ('name with locants', 'p'), ('draw every H', 'p'), ('H-bonds between molecules', 'p'),
    ('1°, 2°, 3° alcohols', 'g'), ('oxidation', 'g'), ('esters ⇌', 'g'), ('addition polymers', 'g'), ('condensation polymers', 'g'),
    ('IR bands', 'y'), ('M⁺ peak', 'y')],
    close='Draw it, name it, explain the force, and quote the evidence.'), [
    S("That is the whole of Criterion 7. Gases follow kinetic theory and the gas laws, and real gases depart at low temperature "
      "and high pressure. Electron configurations and the periodic table explain trends and anomalies using nuclear charge, "
      "shells and shielding. In organic chemistry, draw every hydrogen, name with locants, and explain properties with the "
      "intermolecular forces that bond polarity gives. Reactions follow the map on your information sheet, and spectra help identify "
      "structures. Practise explaining each idea in words, and you will be ready for your tests and for Section C. Good luck."),
]),
]

_used = {r for sc in SCENES for st in sc.steps for r in st.refs} | {t[1] for t in EXAM_TOPICS.values()} \
    | {t[1] for t in SYLLABUS.values()} | {t[1] for t in ELEMENTS.values()} | {'info', 'info_data'}
REFS = {k: r for k, r in REFS.items() if k in _used}

VIDEO = Video(
    id='CHM415115_C7_organic_inorganic',
    course=COURSE, course_name='Chemistry', module=MODULE,
    module_name='Criterion 7: Demonstrate knowledge and understanding of properties and reactions of organic and inorganic matter',
    title='Criterion 7: organic and inorganic matter, complete revision',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Chemical Information'),
    checks=CHECKS,
    thumbnail=V.thumbnail,
    allowed_overlaps=['demonstrate knowledge and understanding of properties and reactions of organic and inorganic matter'],
    keywords=['functional group', 'alcohol', 'aldehyde', 'ketone', 'carboxylic acid', 'ester', 'amine', 'amide', 'alkene',
              'addition polymer', 'condensation polymer', 'hydrogen bonding', 'dispersion forces', 'dipole-dipole',
              'electron configuration', 'isoelectronic', 'ionisation energy', 'core charge', 'shielding', 'electronegativity',
              'ideal gas', 'kinetic theory', 'infrared', 'mass spectrometry', 'molecular ion', 'benzene', 'delocalised',
              'esterification', 'oxidation', 'isomer'],
    description=('A complete revision explainer for TASC Chemistry (CHM415115) Criterion 7: properties and reactions of '
                 'organic and inorganic matter: gases, the periodic table, and organic chemistry. For class tests and '
                 'the end-of-year exam (Section C). Items from the TASC information sheet are labelled on screen.'),
)
