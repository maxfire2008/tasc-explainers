"""PHY415115 Physics, Criterion 8: Identify and apply principles of the wave-particle nature of light,
atomic and nuclear physics and models of the nucleus and nuclear processes.

Build with:
    uv run python -m explainer check   videos/PHY415115/c8_quantum_nuclear.py
    uv run python -m explainer preview videos/PHY415115/c8_quantum_nuclear.py
    uv run python -m explainer thumbnail videos/PHY415115/c8_quantum_nuclear.py
    uv run python -m explainer render  videos/PHY415115/c8_quantum_nuclear.py    # operator only: narration, video, docs
"""
import math

from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, InfoSheet, import_sibling

COURSE, MODULE = 'PHY415115', 'C8'
L.use(style.theme(COURSE, MODULE))
V = import_sibling(__file__, 'c8_visuals.py')

P0 = 'Criterion 8 · Overview'
P1 = 'Part 1 · Light as particles'
P2 = 'Part 2 · Matter waves and atoms'
P3 = 'Part 3 · Radioactivity and decay'
P4 = 'Part 4 · Mass, energy and the nucleus'
P5 = 'Part 5 · Internal only'
P6 = 'Finish · Tests & exam technique'

# --------------------------------------------------------------------------- references
# Source NAMES from sources/PHY415115/content.csv (list them with: uv run python -m explainer sources PHY415115).
COURSE_DOC = 'phy415115-9.html'
INFO = 'PHY415115-Physics-Information-sheet.pdf'
SPEC = 'PHY415115-Physics-External-Assessment-Specifications.pdf'

EXAM_FILES = {2018: 'PHY415115 Physics TASC Exam Paper 2018.pdf', 2019: 'PHY415115 Physics TASC Exam Paper 2019.pdf',
              2020: 'PHY415115 Physics TASC Exam Paper 2020.pdf'}
REPORT_FILES = {2018: 'PHY415115 - Assessment Panel Report 2018.pdf', 2019: 'PHY415115 Assessment Report 2019.pdf',
                2020: 'PHY415115 Assessment Report 2020.pdf'}
# Question -> PDF pages for this criterion's section of each paper and report (from the cached PDFs).
EXAM_PAGES = {
    2018: {19: '47-48', 20: 49, 21: 51, 22: 52, 23: 53, 24: '53-54'},
    2019: {19: '44-45', 20: '46-47', 21: '48-49', 22: '50-51', 23: 52, 24: 53},
    2020: {19: 44, 20: 45, 21: '46-47', 22: 48, 23: 49, 24: 50},
    2021: {18: '48-49', 19: '50-51', 20: '52-53', 21: '54-55', 22: 56},
    2022: {19: '47-48', 20: 49, 21: 50, 22: '51-52', 23: 53, 24: 54},
    2023: {19: 56, 20: 57, 21: 58, 22: 59, 23: '60-61', 24: '62-63'},
    2024: {19: '56-57', 20: '58-59', 21: 60, 22: 61, 23: '62-63', 24: 64},
    2025: {18: 47, 19: '48-49', 20: 50, 21: 51, 22: '52-53', 23: 54},
}
REPORT_PAGES = {
    2018: {19: 6, 20: 6, 21: 6, 22: '6-7', 23: 7, 24: 7},
    2019: {19: '5, 18', 20: '6, 18-19', 21: '6, 19', 22: '6, 20', 23: '6, 20', 24: '7, 21'},
    2020: {19: '5, 15', 20: '5, 16', 21: '6, 16', 22: '6, 17', 23: '6, 17', 24: '6, 17'},
    2021: {18: 17, 19: 18, 20: 19, 21: '20-21', 22: 21},
    2022: {19: '28-30', 20: '30-31', 21: '31-32', 22: '32-34', 23: 34, 24: 35},
    2023: {19: '27-28', 20: '29-30', 21: '30-31', 22: '31-33', 23: '34-36', 24: '37-38'},
    2024: {19: '29-31', 20: '31-33', 21: '33-34', 22: '34-35', 23: '35-36', 24: '36-38'},
    2025: {18: 12, 19: 12, 20: '12-13', 21: 13, 22: '13-14', 23: 14},
}


def exam(y, q):
    name = EXAM_FILES.get(y, f'PHY415115-Physics-TASC-Exam-Paper-{y}.pdf')
    section = 'Part 4' if y <= 2021 else 'Section D'
    return Ref(name, f'{y} exam, {section}, Question {q}', EXAM_PAGES[y][q])


def report(y, q):
    name = REPORT_FILES.get(y, f'PHY415115-Physics-Assessment-Report-{y}.pdf')
    return Ref(name, f'{y} assessment report, Criterion 8, Question {q}', REPORT_PAGES[y][q])


REFS = {
    'standards': Ref(COURSE_DOC, 'Course document, Criterion 8 standards (element table)'),
    'content': Ref(COURSE_DOC, 'Course document, Science Understanding: wave-particle nature of light, atomic and nuclear physics (Criterion 8)'),
    'internal': Ref(COURSE_DOC, 'Course document, The theory of relativity and the Standard Model (internally assessed dot points)'),
    'appendix': Ref(COURSE_DOC, 'Course document, Appendix 1: examples in context for C8 & C4'),
    'info': Ref(INFO, 'Information sheet, Quantum and Nuclear sections', page=2),
    'info1': Ref(INFO, 'Information sheet, Motion in a Straight Line, Momentum, Force, Centripetal Force section', page=1),
    'info1e': Ref(INFO, 'Information sheet, Electrostatics section', page=1),
    'spec': Ref(SPEC, 'External assessment specifications, Section D and Appendix A', page='3-5'),
}
for _y, _qs in EXAM_PAGES.items():
    for _q in _qs:
        REFS[f'ex{_y % 100}q{_q}'] = exam(_y, _q)
for _y, _qs in REPORT_PAGES.items():
    for _q in _qs:
        REFS[f'ar{_y % 100}q{_q}'] = report(_y, _q)

# --------------------------------------------------------------------------- coverage targets
# Every dot point of the course content for this criterion.  check fails if one is uncovered.
SYLLABUS = {
    'L1': ('Why hot objects produce a continuous spectrum', 'content'),
    'L2': ('Failure of classical physics to explain the intensity of the continuous spectrum', 'content'),
    'L3': ('Planck, black bodies (completely absorb or emit all wavelengths) and cavity radiators', 'content'),
    'L4': ("Wien's law: peak wavelength and absolute temperature", 'content'),
    'L5': ('Photon energy E = hf', 'content'),
    'L6': ('Photoelectric effect discovered by Hertz; failure of classical physics to explain it', 'content'),
    'L7': ("Einstein's explanation: Ek(max) = eV = hf − W, W = work function", 'content'),
    'L8': ("Link of the equation to Millikan's arrangement with stopping voltages", 'content'),
    'L9': ('Introduction of the electron-volt', 'content'),
    'L10': ('Quantitative use of the equation in graphical, numerical and tabular form', 'content'),
    'X1': ('Production of X-rays: potential-difference-based maximum frequency, hf(max) = eV', 'content'),
    'X2': ('X-ray tube construction', 'content'),
    'X3': ('Types of X-rays: continuous and characteristic', 'content'),
    'X4': ('Maximum photon frequency is independent of tube current', 'content'),
    'C1': ('Momentum of individual photons: p = h/λ = E/c', 'content'),
    'C2': ('Compton scattering of X-rays with electrons: simple collisions obeying momentum rules', 'content'),
    'D1': ("De Broglie's wavelength for particles: p = mv = h/λ", 'content'),
    'D2': ('Implications for interference of electrons; qualitative link to Schrödinger and quantum mechanics', 'content'),
    'D3': ('Calculating wavelengths of electrons and other particles', 'content'),
    'D4': ('More particle-like as momentum/energy increases; more wavelike as it decreases', 'content'),
    'D5': ('Electrons and small particles show interference and diffraction like X-rays; typical dimensions', 'content'),
    'D6': ('EM spectrum from very wavelike radio to very particle-like gamma rays', 'content'),
    'A1': ('Description of emission and absorption line spectra', 'content'),
    'A2': ('Failure of classical physics to explain line spectra', 'content'),
    'A3': ('Qualitative Bohr-Rutherford atom', 'content'),
    'A4': ('Recognition of energy levels of electrons in atoms', 'content'),
    'A5': ('Transitions between levels are associated with photon absorption or production', 'content'),
    'A6': ('Evaluating photon energies, frequencies and wavelengths from transitions', 'content'),
    'A7': ('Excitation by electron bombardment: through heat, electrically or other means', 'content'),
    'A8': ('Excitation by photons, and ionisation by high-energy photons', 'content'),
    'A9': ('Characteristic X-ray spectra: energy changes to n = 1 (K lines) or n = 2 (L lines) in heavy elements', 'content'),
    'A10': ('Qualitative electron standing wave patterns in the Bohr-Rutherford atom', 'content'),
    'A11': ('Very elementary idea of the electron "cloud" model of the atom', 'content'),
    'N1': ('Discovery of the nucleus by the Rutherford team in 1909', 'content'),
    'N2': ('Definition of radioactivity; properties of alpha, beta and gamma radiation', 'content'),
    'N3': ('Alpha radiation is associated with large nuclei', 'content'),
    'N4': ('Beta radiation is due to decay of protons or neutrons in unstable nuclei', 'content'),
    'N5': ('Positrons, neutrinos, antineutrinos and neutrons', 'content'),
    'N6': ('Background radiation and its sources', 'content'),
    'N7': ('Unit of activity A: the becquerel', 'content'),
    'R1': ('Isotopes and the radioisotope', 'content'),
    'R2': ('Transmutations, parent and daughter nuclei, decay series', 'content'),
    'R3': ('Decay equations for alpha and beta decay, including gamma radiation and neutrinos', 'content'),
    'R4': ('Half-life of a radioisotope', 'content'),
    'R5': ('Activity and decay constant: A = −dN/dt = λN, λ = 0.693/T½', 'content'),
    'R6': ('Half-life calculations including exponential treatment', 'content'),
    'R7': ('Atomic number, mass number, atomic mass unit (dalton)', 'content'),
    'R8': ('Strong nuclear force: very short range, acts only on protons and neutrons', 'content'),
    'M1': ('Equivalence of mass and energy; conservation of mass-energy: E = mc²', 'content'),
    'M2': ('Mass defect calculations, binding energy and stability of nuclei', 'content'),
    'M3': ('Mass differences in nuclear reactions, and energy released or required', 'content'),
    'M4': ('BE per nucleon curve: fusion on one side of the maximum, fission on the other', 'content'),
    'M5': ('Fission: chain reaction and critical mass', 'content'),
    'M6': ('Basic components of a fission reactor: moderator, control rods, heat exchange', 'content'),
    'M7': ('Qualitative Standard Model: quarks, colour charge, gluons; up and down quarks in protons and neutrons', 'content'),
    'S1': ('Internal only: gauge bosons: gluons, W and Z bosons, photons', 'internal'),
    'S2': ('Internal only: high-speed observations Newtonian physics cannot explain (muons, accelerators)', 'internal'),
    'S3': ('Internal only: special relativity differs from Newtonian physics approaching the speed of light', 'internal'),
    'S4': ('Internal only: the two postulates of special relativity', 'internal'),
    'S5': ('Internal only: motion is relative; length and time depend on the frame of reference', 'internal'),
    'S6': ('Internal only: relativistic momentum prevents an object from reaching the speed of light', 'internal'),
    'S7': ('Internal only: mass-energy equivalence emerged from special relativity', 'internal'),
    'K1': ('Context: radioisotopes and radiometric dating', 'appendix'),
    'K2': ('Context: harnessing nuclear power', 'appendix'),
    'K3': ('Context: nuclear fusion in stars', 'appendix'),
    'K4': ('Context: development of the quantum model', 'appendix'),
    'K5': ('Context: black body radiation and the greenhouse effect', 'appendix'),
    'K6': ('Context: development of the special theory of relativity', 'appendix'),
    'K7': ('Context: ring laser gyroscopes and navigation', 'appendix'),
    'K8': ('Context: nuclear reactors', 'appendix'),
    'K9': ('Context: evidence for the Higgs boson particle', 'appendix'),
    'K10': ('Context: particle accelerators', 'appendix'),
    'K11': ('Context: the Big Bang theory', 'appendix'),
}

# Elements numbered by row order in the standards table (Element 1 = first row).
ELEMENTS = {
    1: ('Identifies, describes and explains fundamental principles', 'standards'),
    2: ('Selects, applies and manipulates formulae to solve numerical problems (straightforward → complex, analysing validity)', 'standards'),
    3: ('Interprets and analyses data in graphical and tabular form', 'standards'),
    4: ('Interprets problems and makes predictions in real-world contexts', 'standards'),
}

# What past Criterion 8 questions examined (in our own words).  Never copy question text.
EXAM_TOPICS = {
    'X18-19': ('Star peak wavelength and colour; dim star at equal temperature; strong hydrogen lines; levels for a given line', 'ex18q19'),
    'X18-20': ('Caesium Ek-frequency graph: work function, threshold wavelength, parallel line for another metal, reading off', 'ex18q20'),
    'X18-21': ('X-ray photon momentum; 90° scattering momentum diagram; electron velocity', 'ex18q21'),
    'X18-22': ('Proton-proton cycle: equation, energy, Sun output from solar constant, mass loss, reactions per second', 'ex18q22'),
    'X18-23': ('Tungsten spectrum: cut-off wavelength at a voltage, process for the curve, process for K lines', 'ex18q23'),
    'X18-24': ('Potassium-40 in food: percentage mass, activity, beta equation, comparison with background count', 'ex18q24'),
    'X19-19': ('Phototube: filters, better wavelength source, polarity of the wire, ammeter at stopping voltage', 'ex19q19'),
    'X19-20': ('Plutonium power source: why not solar, energy per decay, efficiency, decays per second, atoms, mass', 'ex19q20'),
    'X19-21': ('Iron-56 binding energy and per nucleon; energy from light and heavy elements on the curve', 'ex19q21'),
    'X19-22': ('Tungsten levels: line energies and wavelengths, 100 kV cut-off, sketching the spectrum', 'ex19q22'),
    'X19-23': ('De Broglie wavelength of slow electrons, spectrum region, comparing photon and electron momentum', 'ex19q23'),
    'X19-24': ('Peak wavelength of a human body; best conditions for infrared detection', 'ex19q24'),
    'X20-19': ('Bremsstrahlung: why electrons accelerate, path sketch, 50 kV cut-off, why most photons are longer', 'ex20q19'),
    'X20-20': ('Mercury lines in eV, drawing a transition, 5 eV electron, ionisation in a fluorescent tube', 'ex20q20'),
    'X20-21': ('U-235: atoms in the critical mass, activity for two decay routes, percentage in the distant past', 'ex20q21'),
    'X20-22': ('Gamma removing a neutron: mass difference, minimum energy, beta-plus equation, annihilation photons', 'ex20q22'),
    'X20-23': ('Sunlight on a probe: photon energy, photons per second, force with reflection, long-term effect', 'ex20q23'),
    'X20-24': ('Black body absorption and emission; background radiation: region and temperature from peak', 'ex20q24'),
    'X21-18': ('Hydrogen discharge: how current gives a spectrum, identifying a transition, photon vs electron collision', 'ex21q18'),
    'X21-19': ('Sodium on an Ek-wavelength graph: W, stopping voltage, threshold reasoning, intensity, second metal curve', 'ex21q19'),
    'X21-20': ('Plutonium-238: activity, age from activity, beta equation, decay energy, neutrino properties, BE per nucleon', 'ex21q20'),
    'X21-21': ('60 kV electrons: energy, de Broglie, X-ray limit, continuous and characteristic mechanisms, raised current', 'ex21q21'),
    'X21-22': ('Black body definition, the theory it led to, temperature from peak, sketching a cooler curve', 'ex21q22'),
    'X22-19': ('Triple-alpha process: equations, mass difference, energy in or out, BE per nucleon, conditions for fusion', 'ex22q19'),
    'X22-20': ('Polonium-210: mass from activity; earlier activity', 'ex22q20'),
    'X22-21': ('Phototube: effect of intensity; threshold frequency; Ek; why infrared cannot be detected this way', 'ex22q21'),
    'X22-22': ('Hydrogen levels: ionisation energy in joules, emission wavelength, marking a line, regions by final level', 'ex22q22'),
    'X22-23': ('Infrared space telescope: peak at low temperature, wavelength stretching, why it must be cooled', 'ex22q23'),
    'X22-24': ('X-ray tube minimum wavelength, photon momentum, effect of current and of voltage', 'ex22q24'),
    'X23-19': ('Lost caesium source: beta equation, atoms from activity, metastable gamma decay', 'ex23q19'),
    'X23-20': ('Decay mass difference, maximum electron energy, which radiation the detectors found', 'ex23q20'),
    'X23-21': ('Stars: peak wavelength and colour, brightness and size, mass loss from power, lifetime reasoning', 'ex23q21'),
    'X23-22': ('Deriving photon momentum; momentum from keV; scattered photon and its vector diagram', 'ex23q22'),
    'X23-23': ('Sketching the spectrum; continuous and characteristic mechanisms; voltage effects; minimum wavelength', 'ex23q23'),
    'X23-24': ('Why classical photoelectric predictions fail; photon energy and work function from a stopping voltage', 'ex23q24'),
    'X24-19': ('Beta decay battery: equation, activity for a power, mass, mass remaining, what no gamma implies', 'ex24q19'),
    'X24-20': ('Stopping voltage table: frequencies, plotting, why they are related, experimental h, W and cut-off', 'ex24q20'),
    'X24-21': ('Iron-56 mass defect and BE per nucleon; why fusion beyond iron cannot be sustained', 'ex24q21'),
    'X24-22': ('Laser: photon energy, photons per second, photon momentum, force of an absorbed beam', 'ex24q22'),
    'X24-23': ('Aurora: wavelength from a transition, minimum electron energy, spectrum region for a small drop', 'ex24q23'),
    'X24-24': ('X-ray bounces straight back: momenta with direction, electron recoil speed', 'ex24q24'),
    'X25-18': ('Infrared thermometer: temperature range from wavelengths; would it work on the Sun', 'ex25q18'),
    'X25-19': ("Rutherford's transmutation: mass difference, energy absorbed, electric force and the case for a nuclear force", 'ex25q19'),
    'X25-20': ('Backscattered photon: momenta, electron speed, apparent energy mismatch and relativity', 'ex25q20'),
    'X25-21': ('Radium-224 therapy: alpha equation, atoms from activity, later activity', 'ex25q21'),
    'X25-22': ('Sodium levels: excitation energy, possible transitions, scattered electrons, highest photon, level pair for a line', 'ex25q22'),
    'X25-23': ('Aluminium: spectrum region, Ek, why a range of energies exists, threshold frequency', 'ex25q23'),
}

_h, _he, _c, _e, _me = 6.63e-34, 4.14e-15, 3.00e8, 1.60e-19, 9.11e-31
_mp, _mn, _mel, _NA, _yr = 1.007276, 1.008665, 0.000549, 6.02e23, 365 * 24 * 3600
_ni = 28 * (_mp + _mel) + 34 * _mn - 61.928345
_am_A = 10 / (5.6e6 * _e)
_am_l = 0.693 / (432 * _yr)
_i_l = 0.693 / (8.02 * 86400)
_sun = 590 * 4 * math.pi * 2.28e11 ** 2
_p1, _p2 = _h / 2.00e-11, _h / 2.24e-11
_b1, _b2 = _h / 3.00e-11, _h / 3.485e-11

# Every number spoken or shown in a worked example, recomputed.  check fails on a mismatch.
CHECKS = [
    ('red photon eV', lambda: _he * _c / 700e-9, 1.77, 0.005),
    ('violet photon eV', lambda: _he * _c / 400e-9, 3.11, 0.002),
    ('hc in eV m', lambda: _he * _c, 1.24e-6, 0.002),
    ('green photon J', lambda: _h * _c / 530e-9, 3.75e-19, 0.002),
    ('green photon eV', lambda: _he * _c / 530e-9, 2.34, 0.002),
    ('coffee peak', lambda: 2.90e-3 / (80 + 273), 8.2e-6, 0.005),
    ('hot star peak', lambda: 2.90e-3 / 12000, 242e-9, 0.002),
    ('red star peak', lambda: 2.90e-3 / 3500, 829e-9, 0.002),
    ('body peak', lambda: 2.90e-3 / 310, 9.4e-6, 0.005),
    ('thermometer high T', lambda: 2.90e-3 / 8e-6, 360, 0.01),
    ('thermometer low T', lambda: 2.90e-3 / 12e-6, 240, 0.01),
    ('sun peak', lambda: 2.90e-3 / 5800, 500e-9, 0.001),
    ('Mg f0', lambda: 3.70 / _he, 8.94e14, 0.001),
    ('Mg lambda0', lambda: _c / (3.70 / _he), 336e-9, 0.002),
    ('250 nm photon', lambda: _he * _c / 250e-9, 4.97, 0.002),
    ('Mg Ek', lambda: _he * _c / 250e-9 - 3.70, 1.27, 0.002),
    ('Mg Ek J', lambda: 1.27 * _e, 2.03e-19, 0.002),
    ('Mg v', lambda: math.sqrt(2 * 2.03e-19 / _me), 6.7e5, 0.005),
    ('240 nm f', lambda: _c / 240e-9, 12.5e14, 1e-6),
    ('240 nm Ek metal 1', lambda: _he * 12.5e14 - 2.2, 2.98, 0.005),
    ('lambda0 W=2.2', lambda: 1242 / 2.2, 565, 0.002),
    ('lambda0 W=4.0', lambda: 1242 / 4.0, 311, 0.002),
    ('table f 500', lambda: _c / 500e-9, 6.00e14, 1e-6),
    ('table f 400', lambda: _c / 400e-9, 7.50e14, 1e-6),
    ('table f 300', lambda: _c / 300e-9, 10.0e14, 1e-6),
    ('table V 500', lambda: _he * 6.00e14 - 2.2, 0.28, 0.02),
    ('table V 400', lambda: _he * 7.50e14 - 2.2, 0.91, 0.01),
    ('table V 300', lambda: _he * 10.0e14 - 2.2, 1.94, 0.002),
    ('table gradient', lambda: (1.94 - 0.28) / 4.00e14, 4.15e-15, 0.001),
    ('table intercept', lambda: 0.28 - 4.15e-15 * 6.00e14, -2.21, 0.002),
    ('table f0', lambda: 2.2 / 4.15e-15, 5.3e14, 0.001),
    ('80 kV energy', lambda: _e * 80e3, 1.28e-14, 1e-6),
    ('80 kV lambda', lambda: _h * _c / (_e * 80e3), 1.55e-11, 0.003),
    ('80 kV p', lambda: _e * 80e3 / _c, 4.27e-23, 0.002),
    ('K alpha gap', lambda: 20 - 2.9, 17.1, 1e-6),
    ('K beta gap', lambda: 20 - 0.5, 19.5, 1e-6),
    ('K alpha', lambda: _he * _c / 17.1e3, 72.6e-12, 0.001),
    ('K beta', lambda: _he * _c / 19.5e3, 63.7e-12, 0.001),
    ('35 kV cut-off', lambda: _he * _c / 35e3, 35.5e-12, 0.001),
    ('laser photon', lambda: _h * _c / 532e-9, 3.74e-19, 0.001),
    ('laser n', lambda: 5.0e-3 / (_h * _c / 532e-9), 1.34e16, 0.002),
    ('laser p', lambda: _h / 532e-9, 1.25e-27, 0.004),
    ('laser F', lambda: 5.0e-3 / (_h * _c / 532e-9) * _h / 532e-9, 1.67e-11, 0.002),
    ('laser F via P/c', lambda: 5.0e-3 / _c, 1.67e-11, 0.002),
    ('mirror F', lambda: 2 * 5.0e-3 / _c, 3.33e-11, 0.002),
    ('comp90 p', lambda: _p1, 3.32e-23, 0.002),
    ('comp90 p2', lambda: _p2, 2.96e-23, 0.001),
    ('comp90 pe', lambda: math.hypot(_p1, _p2), 4.44e-23, 0.002),
    ('comp90 angle', lambda: math.degrees(math.atan(_p2 / _p1)), 41.8, 0.002),
    ('comp90 v', lambda: math.hypot(_p1, _p2) / _me, 4.88e7, 0.001),
    ('comp180 p', lambda: _b1, 2.21e-23, 0.001),
    ('comp180 p2', lambda: _b2, 1.90e-23, 0.001),
    ('comp180 pe', lambda: _b1 + _b2, 4.11e-23, 0.001),
    ('comp180 v', lambda: (_b1 + _b2) / _me, 4.51e7, 0.001),
    ('comp180 v/c', lambda: (_b1 + _b2) / _me / _c, 0.15, 0.005),
    ('comp180 E1', lambda: _h * _c / 3.00e-11, 6.63e-15, 0.001),
    ('comp180 E2', lambda: _h * _c / 3.485e-11, 5.707e-15, 0.001),
    ('comp180 loss', lambda: _h * _c / 3.00e-11 - _h * _c / 3.485e-11, 9.23e-16, 0.001),
    ('comp180 KE', lambda: 0.5 * _me * ((_b1 + _b2) / _me) ** 2, 9.28e-16, 0.001),
    ('150 V energy', lambda: _e * 150, 2.40e-17, 1e-6),
    ('150 V speed', lambda: math.sqrt(2 * 2.40e-17 / _me), 7.26e6, 0.001),
    ('150 V percent of c', lambda: 100 * 7.26e6 / _c, 2.4, 0.01),
    ('150 V lambda', lambda: _h / (_me * 7.26e6), 1.0e-10, 0.003),
    ('150 eV photon', lambda: _he * _c / 150, 8.28e-9, 0.001),
    ('ball lambda', lambda: _h / (0.058 * 40), 2.9e-34, 0.02),
    ('slow electron lambda', lambda: _h / (_me * 2.0e5), 3.6e-9, 0.02),
    ('slow electron p', lambda: _me * 2.0e5, 1.8e-25, 0.02),
    ('gap 2.4', lambda: _he * _c / 2.4, 518e-9, 0.002),
    ('gap 2.1', lambda: _he * _c / 2.1, 591e-9, 0.001),
    ('gap 1.2', lambda: _he * _c / 1.2, 1035e-9, 0.001),
    ('electron left over', lambda: 3.0 - 2.4, 0.6, 1e-6),
    ('ionise left over', lambda: 7.0 - 6.0, 1.0, 1e-6),
    ('ionisation J', lambda: 6.0 * _e, 9.6e-19, 1e-6),
    ('annihilation', lambda: _mel * 931, 0.511, 0.001),
    ('20 Bq per minute', lambda: 20 * 60, 1200, 1e-9),
    ('1 percent of 1200', lambda: 0.01 * 1200, 12, 1e-9),
    ('I-131 lambda', lambda: _i_l, 1.00e-6, 0.001),
    ('I-131 N', lambda: 5.0e6 / _i_l, 5.0e12, 0.001),
    ('I-131 m', lambda: 5.0e12 * 131 / _NA, 1.09e-9, 0.002),
    ('I-131 lambda t', lambda: 0.693 * 20.0 / 8.02, 1.73, 0.002),
    ('I-131 later', lambda: 5.0 * math.exp(-0.693 * 20 / 8.02), 0.89, 0.005),
    ('I-131 remaining percent', lambda: 100 * math.exp(-0.693 * 20 / 8.02), 18, 0.02),
    ('I-131 earlier exponent', lambda: 0.693 * 10.0 / 8.02, 0.864, 0.001),
    ('I-131 earlier', lambda: 5.0 * math.exp(0.693 * 10 / 8.02), 12, 0.02),
    ('C-14 lambda', lambda: 0.693 / 5730, 1.21e-4, 0.001),
    ('ln 0.40', lambda: -math.log(0.40), 0.916, 0.001),
    ('C-14 age', lambda: 5730 * -math.log(0.40) / 0.693, 7600, 0.005),
    ('percent of a mass', lambda: 3.0 * 0.50 / 100, 0.015, 1e-9),
    ('isotope in the past', lambda: 2.0 * math.exp(0.693 * 2), 8.0, 0.002),
    ('exponent two half-lives', lambda: 0.693 * 2, 1.386, 1e-6),
    ('probe total power', lambda: 0.50 / 0.050, 10, 1e-9),
    ('Am per decay', lambda: 5.6e6 * _e, 8.96e-13, 1e-6),
    ('Am activity', lambda: _am_A, 1.1e13, 0.02),
    ('Am lambda', lambda: _am_l, 5.09e-11, 0.002),
    ('Am N', lambda: _am_A / _am_l, 2.2e23, 0.005),
    ('Am mass', lambda: _am_A / _am_l * 241 / _NA, 88, 0.005),
    ('Am after 70 y', lambda: math.exp(-0.693 * 70 / 432), 0.89, 0.005),
    ('net 0', lambda: 430 - 30, 400, 1e-9),
    ('net half-life point', lambda: 230 - 30, 200, 1e-9),
    ('data decay constant', lambda: 0.693 / 4.0, 0.17, 0.02),
    ('star mass loss', lambda: 1.2e27 / _c ** 2, 1.3e10, 0.03),
    ('Ni-62 parts', lambda: _ni + 61.928345, 62.513710, 1e-7),
    ('Ni-62 defect', lambda: _ni, 0.585365, 1e-5),
    ('Ni-62 BE', lambda: _ni * 931, 545, 0.001),
    ('Ni-62 per nucleon', lambda: _ni * 931 / 62, 8.79, 0.001),
    ('DT before', lambda: 2.013553 + 3.015501, 5.029054, 1e-7),
    ('DT after', lambda: 4.001506 + 1.008665, 5.010171, 1e-7),
    ('DT defect', lambda: 5.029054 - 5.010171, 0.018883, 1e-4),
    ('DT energy', lambda: 0.018883 * 931, 17.6, 0.002),
    ('fission before', lambda: 235.043928 + _mn, 236.052593, 1e-7),
    ('fission after', lambda: 140.914404 + 91.926173 + 3 * _mn, 235.866572, 1e-7),
    ('fission defect', lambda: 236.052593 - 235.866572, 0.186021, 1e-4),
    ('fission energy', lambda: 0.186021 * 931, 173, 0.002),
    ('4p defect', lambda: 4 * _mp - 4.001506 - 2 * _mel, 0.0265, 0.001),
    ('4p energy', lambda: 0.0265 * 931, 24.7, 0.002),
    ('sun power', lambda: _sun, 3.9e26, 0.02),
    ('sun mass loss', lambda: _sun / _c ** 2, 4.3e9, 0.01),
    ('sun reactions', lambda: _sun / (24.7e6 * _e), 9.8e37, 0.01),
    ('fission vs fusion per reaction', lambda: 173 / 17.6, 10, 0.02),
    ('50 keV in joules', lambda: 50e3 * _e, 8.0e-15, 1e-6),
    ('50 keV momentum', lambda: 50e3 * _e / _c, 2.7e-23, 0.015),
    ('americium in kg', lambda: 88 / 1000, 0.088, 1e-9),
    # Unrounded values shown on screen above each rounded answer.
    ('shown: green photon', lambda: _h * _c / 530e-9, 3.7528e-19, 1e-4),
    ('shown: coffee', lambda: 2.90e-3 / 353, 8.2153e-6, 1e-4),
    ('shown: Mg f0', lambda: 3.70 / _he, 8.9372e14, 1e-4),
    ('shown: Mg lambda0', lambda: _he * _c / 3.70, 335.68e-9, 1e-4),
    ('shown: Mg Ek', lambda: _he * _c / 250e-9 - 3.70, 1.268, 1e-4),
    ('shown: Mg v', lambda: math.sqrt(2 * 1.268 * _e / _me), 6.6738e5, 1e-4),
    ('shown: 80 kV lambda', lambda: _h * _c / (_e * 80e3), 1.5539e-11, 1e-4),
    ('shown: laser n', lambda: 5.00e-3 / (_h * _c / 532e-9), 1.3374e16, 1e-4),
    ('shown: laser F', lambda: 5.00e-3 / _c, 1.6667e-11, 1e-4),
    ('shown: comp90 pe', lambda: math.hypot(_p1, _p2), 4.4441e-23, 1e-4),
    ('shown: comp180 pe', lambda: _b1 + _b2, 4.1124e-23, 1e-4),
    ('shown: 150 V lambda', lambda: _h / math.sqrt(2 * _me * _e * 150), 1.0026e-10, 1e-4),
    ('shown: 150 V speed', lambda: math.sqrt(2 * _e * 150 / _me), 7.2587e6, 1e-4),
    ('shown: annihilation', lambda: _mel * 931, 0.5111, 1e-3),
    ('shown: I-131 N', lambda: 5.0e6 / _i_l, 4.9995e12, 1e-4),
    ('shown: I-131 m', lambda: 5.0e6 / _i_l * 131 / _NA, 1.0879e-9, 1e-4),
    ('shown: I-131 later', lambda: 5.0 * math.exp(-0.693 * 20 / 8.02), 0.8880, 1e-3),
    ('shown: I-131 earlier', lambda: 5.0 * math.exp(0.693 * 10 / 8.02), 11.864, 1e-3),
    ('shown: C-14', lambda: 0.9163 / (0.693 / 5730), 7576, 1e-3),
    ('shown: Am activity', lambda: _am_A, 1.1161e13, 1e-4),
    ('shown: Am N', lambda: _am_A / _am_l, 2.1941e23, 1e-4),
    ('shown: Am m', lambda: _am_A / _am_l * 241 / _NA, 87.84, 1e-3),
    ('shown: Ni-62 BE', lambda: _ni * 931, 544.97, 1e-4),
    ('shown: DT', lambda: 0.018883 * 931, 17.580, 1e-3),
    ('shown: fission', lambda: 0.186021 * 931, 173.19, 1e-3),
    ('shown: star P', lambda: _sun, 3.8542e26, 1e-4),
    ('shown: star mass', lambda: _sun / _c ** 2, 4.2824e9, 1e-4),
    ('shown: star reactions', lambda: _sun / (24.7e6 * _e), 9.7525e37, 1e-4),
    ('shown: electric force', lambda: 9.00e9 * (2 * _e) * (6 * _e) / (5.0e-15) ** 2, 110.59, 1e-3),
    ('electric force', lambda: 9.00e9 * (2 * _e) * (6 * _e) / (5.0e-15) ** 2, 110, 0.01),
]

# --------------------------------------------------------------------------- scenes
S = Step
SCENES = [
Scene('title', P0, 'Welcome', V.title_card, [
    S("Welcome. This video is a complete briefing on Criterion 8 of TASC Physics, PHY415115: how light behaves as both a wave "
      "and a particle, the structure of atoms, and the physics of the nucleus. Use it to revise for your class tests and for the end of year exam. By the "
      "end, you should know every part of this content, which formulas are on your information sheet and where to find "
      "them, and the traps that examiners keep seeing in student answers.", refs=['standards'], anim=4),
]),
Scene('intro', P0, 'How Criterion 8 is assessed', V.overview, [
    S("Criterion 8 is assessed in two ways. Your teacher assesses it during the year, through class tests, practicals and "
      "other tasks. It's also assessed externally, in Section D of the end of year exam. That's about forty five minutes, "
      "forty five marks, and five to seven compulsory questions. In the exam you can use the TASC information sheet and an "
      "approved calculator.", refs=['standards', 'spec']),
    S("The criterion has four elements. We'll number them in the order they appear in the standards table. Element one is "
      "identifying, describing and explaining the principles. Element two is solving numerical problems. Element three is "
      "working with data in graphs and tables. And element four is interpreting problems and making predictions, including "
      "in unfamiliar, real world contexts. You'll see a tag in the corner when an example practises a particular element.",
      refs=['standards'], elements=[1, 2, 3, 4]),
    S("The standards step up from C to A. At C level you identify principles, solve straightforward problems, interpret "
      "data and predict in familiar contexts. At B, you describe principles, solve problems with several steps, and analyse "
      "data to get new information. At A, you explain; you solve complex problems and check whether your answer is valid; "
      "you evaluate data and generalise; and you make reasoned predictions in unfamiliar contexts. So we'll focus on why, "
      "not just on formulas.", refs=['standards'], elements=[1, 2, 3, 4]),
    S("Here's the roadmap. Part one: light behaving as particles, through black bodies, the photoelectric effect and X rays. "
      "Part two: matter behaving as waves, and the energy levels of atoms. Part three: radioactivity and half life. Part "
      "four: mass and energy, binding energy, fission, fusion and quarks. Part five is a short look at relativity and the "
      "course's contexts, for internal assessment. Then we finish with technique. Let's get started."),
]),
# ------------------------------------------------------------------- part 1
Scene('blackbody', P1, 'Hot objects and black bodies', V.blackbody, [
    S("Part one. By the end of the eighteen hundreds, physics seemed nearly complete, but a few things refused to fit. "
      "First: hot objects. Heat a solid and it glows with a continuous spectrum, containing every wavelength. Heat it more, "
      "and the peak moves to shorter wavelengths.", refs=['content'], covers=['L1'], elements=[1]),
    S("Classical wave physics couldn't explain the intensity of this spectrum. It predicted that the intensity would keep "
      "rising as the wavelength got shorter, without any limit. That's the dashed curve. Real objects don't do that: the "
      "intensity reaches a peak and then falls away.", refs=['content'], covers=['L2'], elements=[1]),
    S("The answer came from Max Planck, studying black bodies. A black body completely absorbs all wavelengths, with no "
      "reflection, and is also a perfect emitter of them. A good real example is a cavity with a small hole in it. Planck "
      "could only match the curve by assuming that energy comes in discrete packets. That idea led to quantum physics. "
      "If you're asked what theory this led to, say quantum: just saying light is a particle isn't enough.",
      refs=['content', 'ex21q22', 'ar21q22', 'ex20q24', 'ar20q24'], covers=['L3', 'L2'], elements=[1], exam=['X21-22', 'X20-24']),
]),
Scene('photon_energy', P1, 'Photon energy', V.photon_energy, [
    S("We now call those packets of light photons. The energy of one photon is E equals h f. It's on your information sheet, "
      "in the quantum section, along with Planck's constant, h. The sheet gives h twice: six point six three times ten to "
      "the minus thirty four joule seconds, and four point one four times ten to the minus fifteen electron volt seconds. "
      "Higher frequency means more energy per photon.", refs=['content'], covers=['L5'], elements=[1]),
    S("Since c equals f lambda, you can also write E equals h c over lambda. Take green light at five hundred and thirty "
      "nanometres. In joules, that's three point seven five times ten to the minus nineteen. In electron volts, that's two "
      "point three four. Pick the value of h that matches the units you want. Using the wrong one is among the most common "
      "errors in the reports. The product h c is about one point two four times ten to the minus six electron volt metres, "
      "a handy shortcut you can work out yourself.",
      refs=['ar23q22', 'ar22q21', 'ar21q18', 'ar25q23'], covers=['L5'], elements=[2], exam=['X20-23', 'X24-22'],
      problem='What is the energy of a 530 nm photon, in joules and in electron-volts?'),
]),
Scene('wien', P1, "Wien's law", V.wien, [
    S("The peak of a black body curve obeys Wien's law. On your information sheet, in the quantum section, it's lambda p "
      "times T equals two point nine zero times ten to the minus three metre kelvin. T is the absolute temperature, so "
      "always use kelvin. A hotter body peaks at a shorter wavelength. It's also brighter at every wavelength, so a "
      "cooler curve sits entirely below a hotter one, without crossing it. Examiners see many sketches where the curves cross.",
      refs=['content', 'ar21q22', 'ex21q22'], covers=['L4', 'L1'], elements=[1, 3], exam=['X21-22', 'X22-23']),
    S("An element two example. What's the peak wavelength of a cup of coffee at eighty degrees Celsius? Add two hundred and "
      "seventy three to get three hundred and fifty three kelvin. Then lambda p is two point nine zero times ten to the "
      "minus three, over three hundred and fifty three. That's eight point two times ten to the minus six metres: infrared. "
      "So you can't see the glow of coffee, but an infrared camera can. Forgetting to convert to kelvin is a common error.",
      refs=['ar19q24', 'ar20q24', 'ex19q24', 'ex20q24'], covers=['L4'], elements=[2], exam=['X19-24', 'X20-24'],
      problem='What is the peak wavelength emitted by coffee at 80 °C?'),
    S("Tip: naming a star's colour takes a little more thought. A star at twelve thousand kelvin peaks at two hundred and "
      "forty two nanometres, which is ultraviolet. But it doesn't look ultraviolet. It also emits across the whole visible "
      "range, with more at the blue end, so it appears blue white. Examiners note that students often assume all the light "
      "is at the peak wavelength. A star at thirty five hundred kelvin peaks at eight hundred and twenty nine nanometres, and "
      "looks red.", refs=['ar18q19', 'ex18q19', 'ar23q21', 'ex23q21'], covers=['L4', 'L1'], elements=[4], exam=['X18-19', 'X23-21'],
      problem='A star has a surface temperature of 12 000 K. Where is its peak wavelength, and what colour does it look?'),
]),
Scene('bb_contexts', P1, 'Black bodies in context', V.bb_contexts, [
    S("Here are some element four predictions. If two stars have the same temperature, but one is much dimmer, each square "
      "metre emits the same power, so the dimmer star must be much smaller. In a star's spectrum, a very strong line of an "
      "element tells you there's plenty of that element. And to find a person using infrared, you need cool surroundings, "
      "like night time or open water, so that the body at three hundred and ten kelvin, peaking near nine point four "
      "micrometres, stands out.",
      refs=['ex18q19', 'ar23q21', 'ex19q24', 'ex23q21'], covers=['L4'], elements=[4], exam=['X18-19', 'X23-21', 'X19-24'],
      problem='Two stars have the same temperature, but one is far dimmer. What does that tell you about its size?'),
    S("A remote thermometer sensing eight to twelve micrometres works for peaks between about two hundred and forty and three "
      "hundred and sixty kelvin. The Sun's surface, near fifty eight hundred kelvin, peaks near five hundred nanometres, so "
      "it's out of range. Back up a claim like that with a calculation. Light from very distant galaxies is stretched, from "
      "visible towards infrared. A space telescope detecting that must be very cold, or its own infrared glow would swamp "
      "the faint signal. It isn't cooled so that it can emit.",
      refs=['ex25q18', 'ar25q18', 'ex22q23', 'ar22q23'], covers=['L4', 'L1'], elements=[2, 4], exam=['X25-18', 'X22-23'],
      problem='A thermometer senses peaks from 8 to 12 μm. What temperatures can it measure, and would it work on the Sun?'),
]),
Scene('photoelectric', P1, 'The photoelectric effect', V.photoelectric, [
    S("The second puzzle is the photoelectric effect, discovered by Heinrich Hertz. Light shining on a clean metal surface "
      "can eject electrons. In a vacuum tube, those electrons travel to a collector, and they form a current that we can "
      "measure.", refs=['content'], covers=['L6'], elements=[1], anim=2),
    S("If light were only a wave, three things should be true. Any colour should work if it's bright enough. Brighter light "
      "should give faster electrons. And dim light should cause a delay while energy builds up. All three are wrong. Below a "
      "threshold frequency, no electrons come out, however bright the light. Brighter light gives more electrons, not faster "
      "ones. And emission is effectively instant.",
      refs=['content', 'ex23q24', 'ar23q24'], covers=['L6'], elements=[1], exam=['X23-24', 'X22-21', 'X21-19'], anim=2),
    S("Einstein explained this using photons. From your information sheet, in the quantum section: E K max equals e V equals "
      "h f minus W. One photon gives all of its energy to one electron. The work function, W, is the least energy "
      "needed to escape from the metal, and what's left is kinetic energy. If h f is less than W, nothing is emitted. Being "
      "one to one, it's also effectively instantaneous. Intensity only sets how many photons arrive. So red light fails on "
      "some metals because each red photon has too little energy, and that's also why infrared detectors can't work this "
      "way. Link it to energy and the work function, not just the word threshold.",
      refs=['content', 'ar23q24', 'ar21q19', 'ex22q21', 'ar22q21'], covers=['L7', 'L6'], elements=[1, 4], exam=['X23-24', 'X21-19', 'X22-21'], anim=2),
]),
Scene('stopping', P1, 'Stopping voltage and the electron-volt', V.stopping, [
    S("Millikan tested this with stopping voltages. Make the collector negative, so it repels the electrons. Now raise the "
      "voltage until even the fastest electron just turns back. The ammeter then reads exactly zero. That's the stopping "
      "voltage. Examiners note that many students can't say why the collector is negative: it's to repel electrons, so that "
      "you can measure their maximum kinetic energy. To supply one wavelength at a time, you can use filters. A spectral "
      "lamp with known lines, or a laser, is more precise.",
      refs=['content', 'ex19q19', 'ar19q19'], covers=['L8'], elements=[1], exam=['X19-19', 'X21-19'], anim=2),
    S("The electron loses all its kinetic energy climbing that voltage, so E K max equals e V, as on your information sheet "
      "in the quantum section. This introduces a new unit, the electron volt: the energy one electron gains across one volt. "
      "One electron volt is one point six zero times ten to the minus nineteen joules. Multiply to go to joules, and divide "
      "to go back. So a stopping voltage of one point three volts means a maximum energy of one point three electron volts.",
      refs=['content', 'ar22q22', 'ar23q24'], covers=['L9', 'L8'], elements=[1, 2], exam=['X23-24'], anim=2),
    S("Why is there a range of electron energies, from zero up to the maximum? It's a favourite explain question. All the "
      "photons are the same, and each one gives up all its energy. The range comes from the electrons. Those at the "
      "surface only need W to escape. Those deeper in lose extra energy on the way out, so they emerge slower. Examiners "
      "report answers saying not all the photon's energy is transferred, and that's wrong.",
      refs=['ex25q23', 'ar25q23'], covers=['L7'], elements=[1], exam=['X25-23'], anim=2,
      problem='Why do photoelectrons from one wavelength of light have a range of kinetic energies?'),
]),
Scene('we_photo', P1, 'Worked example: magnesium', V.we_photo, [
    S("An example for element two. Magnesium has a work function of three point seven zero electron volts. At threshold, h f "
      "equals W. So f zero is three point seven zero, over four point one four times ten to the minus fifteen: eight point nine "
      "four times ten to the fourteen hertz. Dividing c by that gives a threshold wavelength of three hundred and thirty six "
      "nanometres. Note that W was in electron volts, so we used h in electron volt seconds.",
      refs=['ex22q21', 'ar22q21', 'ex25q23'], covers=['L7', 'L10'], elements=[2], exam=['X22-21', 'X25-23'],
      problem='Magnesium has a work function of 3.70 eV. What are its threshold frequency and threshold wavelength?'),
    S("Now shine two hundred and fifty nanometre ultraviolet on it. A photon has an energy of four point nine seven electron "
      "volts. Subtract the work function: the maximum kinetic energy is one point two seven electron volts. So the stopping "
      "voltage is one point two seven volts. There's no need to convert to joules along the way. Unnecessary conversions just "
      "cause errors.", refs=['ar25q23', 'ex25q23', 'ex23q24', 'ar23q24'], covers=['L7', 'L8', 'L10'], elements=[2],
      exam=['X25-23', 'X23-24'],
      problem='Ultraviolet light of 250 nm falls on magnesium (W = 3.70 eV). What are the maximum kinetic energy and the stopping voltage?'),
    S("For the speed, you do need joules, because a half m v squared uses SI units. One point two seven electron volts is two "
      "point zero three times ten to the minus nineteen joules. Then v is the square root of two E K over m, which is about six "
      "point seven times ten to the five metres per second. Check validity: two hundred and fifty nanometres is shorter than "
      "the threshold wavelength, so electrons really are emitted.", covers=['L9', 'L10'], elements=[2],
      problem='What is the speed of the fastest photoelectron if its kinetic energy is 1.27 eV?'),
]),
Scene('pe_graph', P1, 'Photoelectric graphs', V.pe_graph, [
    S("Now element three. Plot maximum kinetic energy against frequency, and you get a straight line. Compare it with y equals "
      "m x plus c. The gradient is Planck's constant, the same for every metal. The x intercept is the threshold frequency. "
      "And extending the line back to the y axis, the intercept is minus W. Read the work function straight off the graph.",
      refs=['content', 'ex18q20', 'ar18q20'], covers=['L10', 'L7'], elements=[3], exam=['X18-20'],
      problem='From a graph of maximum kinetic energy against frequency, how do you find h, W and the threshold frequency?'),
    S("A metal with a bigger work function gives a parallel line, shifted to the right, because h doesn't change. If you're "
      "asked to add one, use a ruler, keep the gradient the same, and mark the new intercept. And if the light is made more "
      "intense, the graph doesn't change at all. Only the current grows.",
      refs=['ex18q20', 'ex21q19', 'ar21q19'], covers=['L10'], elements=[3, 4], exam=['X18-20', 'X21-19']),
    S("You can also read values off it. For two hundred and forty nanometre light, f is c over lambda, which is twelve point "
      "five times ten to the fourteen hertz. Go up to metal one's line and across: two point nine eight electron volts. "
      "Left of the threshold, the dashed part isn't real. There are simply no electrons, rather than ones with negative energy.",
      refs=['ex18q20'], covers=['L10'], elements=[3], exam=['X18-20'],
      problem='On an energy-frequency graph with W = 2.2 eV, what is the maximum kinetic energy for 240 nm light?'),
    S("Some questions plot energy against wavelength instead. That's a curve, not a line, because E is h c over lambda minus W. "
      "It reaches zero at the threshold wavelength, and climbs steeply as the wavelength falls. It never touches the y axis. "
      "For a metal with a larger work function, the x intercept moves left. Calculate that intercept and label it, since "
      "few students do. And you can use the formula rather than estimating from the graph.",
      refs=['ex21q19', 'ar21q19'], covers=['L10'], elements=[3, 4], exam=['X21-19']),
]),
Scene('millikan_data', P1, 'Using stopping-voltage data', V.millikan_data, [
    S("Here's a data question for element three. A student measures stopping voltages at three wavelengths: zero point two "
      "eight volts at five hundred nanometres, zero point nine one at four hundred, and one point nine four at three hundred. "
      "First find each frequency using f equals c over lambda. Convert nanometres to metres first. That gives six, seven point "
      "five and ten times ten to the fourteen hertz.",
      refs=['ex24q20', 'ar24q20'], covers=['L10', 'L8'], elements=[3], exam=['X24-20'],
      problem='Stopping voltages are 0.28 V at 500 nm, 0.91 V at 400 nm and 1.94 V at 300 nm. What are h, W and the threshold frequency?'),
    S("Plot the points accurately on the given scale, then rule a line of best fit. Why are they related? Divide Einstein's "
      "equation by e: V equals h over e times f, minus W over e. This rearranged form isn't on your sheet, so learn it. A "
      "higher frequency means more kinetic energy per electron, so a bigger voltage is needed to stop it. Stating the "
      "relationship alone earned no marks in the report. You have to give that chain of reasoning.",
      refs=['ar24q20'], covers=['L10', 'L8'], elements=[1, 3], exam=['X24-20']),
    S("The gradient is the rise, one point six six volts, over the run, four times ten to the fourteen hertz. That's four "
      "point one five times ten to the minus fifteen. Since the voltage is in volts, this is h directly, in electron volt "
      "seconds. The intercept on the y axis gives a work function of two point two electron volts. The x intercept gives a "
      "threshold of about five point three times ten to the fourteen hertz. Use your line, not one point: the question asks "
      "for experimental values, so calculating them from the known h earns no marks.",
      refs=['ar24q20', 'ex24q20'], covers=['L10'], elements=[2, 3], exam=['X24-20']),
]),
Scene('xray_tube', P1, 'Producing X-rays', V.xray_tube, [
    S("Next, X rays. In an X ray tube, a heated filament, the cathode, releases electrons. A high voltage of tens of kilovolts "
      "accelerates them through a vacuum, and they slam into a heavy metal target, such as tungsten, the anode. Most of the "
      "energy just heats the target, which is why it has to be cooled. A small part emerges as X rays.",
      refs=['content', 'ex23q23'], covers=['X2'], elements=[1], exam=['X23-23', 'X21-21'], anim=2),
    S("Einstein also explained the upper limit of X ray frequency. At best, one electron gives all of its kinetic energy, e V, "
      "to one photon. So h f max equals e V. This form isn't on your information sheet, so learn it. Notice what's missing: "
      "the tube current. Current is how many electrons arrive each second, not how much energy each one has. So the maximum "
      "frequency doesn't depend on the current.",
      refs=['content'], covers=['X1', 'X4'], elements=[1], exam=['X22-24'], anim=2),
]),
Scene('xray_spectrum', P1, 'The X-ray spectrum', V.xray_spectrum, [
    S("The spectrum has two parts. The smooth curve is the continuous spectrum. As an electron passes close to a nucleus, the "
      "strong electric attraction swerves it. That's a large acceleration, and an accelerating charge radiates. The closer "
      "the pass, the sharper the swerve, and the more energy goes into the photon. So you get a continuous range of energies, "
      "ending at a sharp cut off. Note that the electron loses energy, and is attracted, not repelled. A diagram really helps "
      "here. The cut off is rare, because few electrons give up everything at once; most pass further away.",
      refs=['content', 'ex20q19', 'ar20q19', 'ar21q21', 'ar23q23'], covers=['X3'], elements=[1], exam=['X20-19', 'X23-23', 'X21-21', 'X18-23'],
      problem='Why do X-ray tubes produce a continuous spectrum, and why do few photons have the shortest wavelength?'),
    S("The spikes are the characteristic spectrum. An incoming electron knocks an inner electron right out of a target atom. "
      "An outer electron then falls into the gap, and one photon carries off the energy difference. K lines come from falls to "
      "n equals one, and L lines from falls to n equals two. Their wavelengths are set by the target metal. A common "
      "error is to think it's the same electron going up and back down. Mention that one electron is knocked out, and another falls in.",
      refs=['content', 'ar18q23', 'ar23q23', 'ar21q21', 'ex18q23'], covers=['X3', 'A9'], elements=[1], exam=['X18-23', 'X21-21', 'X23-23']),
    S("Increase the current, and there are more electrons, so there are more X rays at every wavelength. The cut off stays put, and "
      "so do the spikes. They just get taller. A common sketching error is to move the cut off, or move the spikes.",
      refs=['ar21q21', 'ex21q21', 'ex22q24'], covers=['X4', 'X3'], elements=[3, 4], exam=['X21-21', 'X22-24'],
      problem='What happens to an X-ray spectrum when the tube current is increased?'),
    S("Increase the voltage, and each electron has more energy. So the cut off moves to a shorter wavelength, and the whole "
      "curve grows as well, because each electron brings more energy. The spikes don't move, as they belong to the target, though they do get taller. And if the voltage is too low "
      "to eject an inner electron, those lines don't appear at all. A note on marking: the 2023 marking guide says intensity doesn't rise unless the current changes, but physically it does. "
      "So give both effects, each with a reason: the cut off moves to a shorter wavelength, and the intensity rises.",
      refs=['ar22q24', 'ex22q24', 'ex23q23', 'ar23q23', 'ex18q23'], covers=['X1', 'X3'], elements=[3, 4], exam=['X22-24', 'X23-23', 'X18-23'],
      problem='What happens to an X-ray spectrum when the tube voltage is increased?'),
]),
Scene('we_xray', P1, 'Worked example: an 80 kV tube', V.extend(V.we_xray, 2, V.xray_sketch), [
    S("An element two example. An X ray tube runs at eighty kilovolts. Each electron has e V of energy: one point six zero "
      "times ten to the minus nineteen, times eighty thousand, or one point two eight times ten to the minus fourteen joules. "
      "The shortest wavelength is h c over e V, which is one point five five times ten to the minus eleven metres. Match your "
      "constant to your units: use joules with h in joule seconds, or electron volts with the other one.",
      refs=['ex22q24', 'ar23q23', 'ex19q22', 'ar19q22', 'ex23q23'], covers=['X1'], elements=[2], exam=['X22-24', 'X23-23', 'X19-22', 'X20-19'],
      problem='An X-ray tube runs at 80.0 kV. What is the shortest wavelength it produces?'),
    S("The momentum of that photon is h over lambda, about four point two seven times ten to the minus twenty three kilogram metres "
      "per second. And remember why most X rays have a longer wavelength than this limit: most electrons don't lose all their "
      "energy in one event.", refs=['ex22q24', 'ar22q24', 'ar20q19'], covers=['X1', 'C1'], elements=[2], exam=['X22-24', 'X20-19'],
      problem='What is the momentum of an X-ray photon of wavelength 1.55 × 10⁻¹¹ m?'),
    S("Here's a sketching example, for element three. A target's energy levels show that falls to n equals one release seventeen "
      "point one and nineteen point five kiloelectron volts. Those give lines at seventy two point six and sixty three point "
      "seven picometres. With thirty five kilovolts on the tube, the cut off is thirty five point five picometres. Put wavelength on the "
      "x axis, with a sharp start at the cut off, and label both spikes. Some students forget that the cut off belongs on the "
      "graph too. Remember to find every line, not just one or two.",
      refs=['ex19q22', 'ar19q22', 'ar23q23', 'ex23q23'], covers=['A9', 'X3', 'A6'], elements=[2, 3], exam=['X19-22', 'X23-23'],
      problem='A target has falls of 17.1 keV and 19.5 keV, in a 35 kV tube. Sketch the spectrum with its wavelengths.'),
]),
Scene('photon_momentum', P1, 'Photons carry momentum', V.photon_momentum, [
    S("Photons also carry momentum, even with no rest mass. On your information sheet, in the quantum section, p equals h over "
      "lambda. Another form, p equals E over c, isn't on the sheet, so learn it or derive it. Use those, and don't use m v with v "
      "equals c.", refs=['content'], covers=['C1'], elements=[1], exam=['X23-22'], anim=2),
    S("You might be asked to show where this comes from. Take two energy equations: E equals m c squared, and E equals h c over "
      "lambda. Set them equal. Cancel one c, and m c equals h over lambda. Since m c is a momentum, p equals h over lambda. "
      "Don't start from a half m v squared. Given a photon's energy, say fifty kiloelectron volts, convert to joules and divide by c: "
      "two point seven times ten to the minus twenty three kilogram metres per second.",
      refs=['ex23q22', 'ar23q22'], covers=['C1'], elements=[1, 2], exam=['X23-22'], anim=2,
      problem='By combining two energy equations, show that the momentum of a photon is p = h/λ.'),
]),
Scene('laser_force', P1, 'Worked example: the force of a laser', V.laser_force, [
    S("An element two example. A five milliwatt laser emits light of wavelength five hundred and thirty two nanometres. Each "
      "photon has three point seven four times ten to the minus nineteen joules. Five milliwatts means five times ten to the "
      "minus three joules each second. Dividing, that's one point three four times ten to the sixteen photons per second. "
      "Take care: milli is not mega.", refs=['ex24q22', 'ar24q22', 'ex20q23', 'ar20q23'], covers=['L5'], elements=[2], exam=['X24-22', 'X20-23'],
      problem='A 5.00 mW laser emits 532 nm light. How many photons does it emit each second?'),
    S("Force is the change in momentum each second. Each photon has a momentum of one point two five times ten to the minus "
      "twenty seven. On a black surface the photons are absorbed, so each one transfers all of that. Multiply by the number per second to get one "
      "point six seven times ten to the minus eleven newtons. Don't forget to include the number of photons.",
      refs=['ar24q22'], covers=['C1'], elements=[2], exam=['X24-22'],
      problem='What force does a beam of 1.34 × 10¹⁶ photons per second exert on a black surface, if each has a momentum of 1.25 × 10⁻²⁷ kg m/s?'),
    S("If the surface is a perfect mirror, each photon reverses, so its change in momentum doubles. The force is three point "
      "three three times ten to the minus eleven newtons. Many students miss that factor of two. It's a tiny force. But a spacecraft "
      "has no air drag, so over many months, sunlight on it can change its momentum noticeably. And don't use power equals force "
      "times velocity here: it doesn't apply.",
      refs=['ar20q23', 'ex20q23'], covers=['C1'], elements=[2, 4], exam=['X20-23'],
      problem='A laser beam exerts 1.67 × 10⁻¹¹ N when absorbed. What force does it exert on a perfect mirror, and what would sunlight do to a spacecraft over months?'),
]),
Scene('compton', P1, 'Compton scattering', V.compton, [
    S("In nineteen twenty three, Compton fired X rays at electrons, and found that scattered X rays have a longer wavelength. "
      "Treat it as a simple collision, like two balls. The photon loses energy to the electron, and total momentum is conserved. "
      "A longer wavelength means less energy and less momentum. That's strong evidence of light's particle nature.",
      refs=['content', 'ex23q22'], covers=['C2'], elements=[1], exam=['X23-22', 'X18-21']),
    S("The method: find each momentum using h over lambda, using the joule second value of h. Then draw a vector diagram. "
      "Examiners report students drawing a picture of the apparatus, or a free body diagram. What you need is momentum "
      "vectors, labelled as momenta, with the angle in the correct position. Then solve it, using Pythagoras or the cosine rule, "
      "and give the direction too.",
      refs=['ar18q21', 'ar23q22', 'ex18q21', 'ex23q22'], covers=['C2'], elements=[1, 2], exam=['X18-21', 'X23-22']),
]),
Scene('compton90', P1, 'Worked example: scattering through 90°', V.compton90, [
    S("Element two. An X ray with a wavelength of two point zero zero times ten to the minus eleven metres scatters through ninety "
      "degrees, and leaves with a wavelength of two point two four times ten to the minus eleven. Its momentum before is three "
      "point three two times ten to the minus twenty three. Its momentum after is two point nine six times ten to the minus twenty three.",
      refs=['ex18q21'], covers=['C2', 'C1'], elements=[2], exam=['X18-21'],
      problem='An X-ray of wavelength 2.00 × 10⁻¹¹ m scatters through 90°, leaving with 2.24 × 10⁻¹¹ m. What are the momentum, direction and speed of the electron?'),
    S("Total momentum is conserved. So the original momentum equals the scattered photon's momentum plus the electron's "
      "momentum, as a vector sum. Draw them head to tail: the two photon vectors are at right angles, and the electron's "
      "momentum closes the triangle. By Pythagoras, it's four point four four times ten to the minus twenty three.",
      refs=['ar18q21'], covers=['C2'], elements=[2], exam=['X18-21', 'X23-22']),
    S("Finish it. The angle has a tangent of two point nine six over three point three two, which is forty one point eight "
      "degrees from the original direction, on the opposite side to the photon. Then convert momentum to speed, as some "
      "students forget: divide by the electron mass, to get four point eight eight times ten to the seven metres per second.",
      refs=['ar18q21'], covers=['C2'], elements=[2], exam=['X18-21']),
]),
Scene('compton180', P1, 'Worked example: a head-on bounce', V.compton180, [
    S("The simplest version has the photon bouncing straight back. An X ray moving east has a wavelength of three point zero "
      "zero times ten to the minus eleven metres, and returns with three point four eight five times ten to the minus eleven. Its "
      "momenta are two point two one, east, and one point nine zero, west, both times ten to the minus twenty three. Always "
      "state the direction, because momentum is a vector.",
      refs=['ex24q24', 'ar24q24', 'ex25q20', 'ar25q20'], covers=['C2'], elements=[2], exam=['X24-24', 'X25-20'],
      problem='An X-ray of 3.00 × 10⁻¹¹ m moving east bounces straight back with 3.485 × 10⁻¹¹ m. What is the speed of the electron?'),
    S("Take east as positive. Plus two point two one equals minus one point nine zero, plus the electron's momentum. So the electron "
      "has four point one one times ten to the minus twenty three, going east: the two values add. Most errors "
      "come from treating them both as positive and subtracting. Dividing by the mass gives four point five one times ten to the "
      "seven metres per second. In a show that question, state the conservation law too.",
      refs=['ar24q24', 'ar25q20'], covers=['C2'], elements=[2], exam=['X24-24', 'X25-20']),
    S("Now check validity, for an A rating. The photon loses nine point two three times ten to the minus sixteen joules. The electron's "
      "half m v squared comes to nine point two eight times ten to the minus sixteen. That's very close, but not exact. At fifteen percent of "
      "the speed of light, half m v squared runs slightly high, because it leaves out a small relativistic effect. Relativity isn't assessable in the exam, "
      "but it's the best reason to give.",
      refs=['ar25q20', 'ex25q20'], covers=['C2', 'S3'], elements=[2, 4], exam=['X25-20']),
]),
# ------------------------------------------------------------------- part 2
Scene('debroglie', P2, 'De Broglie: particles are waves too', V.debroglie, [
    S("Part two. If light can act like a particle, can particles act like waves? De Broglie said yes. On your information sheet, "
      "the quantum section has p equals h over lambda. The momentum section, on the first page, has p equals m v. Put them "
      "together, and every moving particle has a wavelength: lambda equals h over m v. Learn that combined form.",
      refs=['content', 'info1'], covers=['D1'], elements=[1], exam=['X19-23']),
    S("So electrons should diffract and interfere, and they do. Electrons fired at a crystal diffract just as X rays do. As "
      "you saw in Criterion 7, diffraction is clearest when the gap is about the size of the wavelength. For these effects, "
      "that's around ten to the minus ten metres, the spacing of atoms in a crystal. That's a typical dimension worth knowing.",
      refs=['content'], covers=['D2', 'D5'], elements=[1]),
    S("This idea led on to quantum mechanics. Schrodinger described electrons using a wave equation. In this course that's "
      "qualitative only: you need the idea, not the mathematics. And it's a fair question to ask what electrons really are. "
      "Neither a wave nor a particle alone gives the whole picture.",
      refs=['content'], covers=['D2'], elements=[1]),
]),
Scene('we_debroglie', P2, 'Worked example: electron wavelength', V.we_debroglie, [
    S("Element two. Electrons are accelerated from rest through one hundred and fifty volts. Their kinetic energy is e V, or two "
      "point four zero times ten to the minus seventeen joules. Then a half m v squared gives a speed of seven point two six "
      "times ten to the six metres per second, about two point four percent of the speed of light. So we can ignore relativity. "
      "Lambda is h over m v, which is about one times ten to the minus ten metres. That's the spacing of atoms!",
      refs=['ex21q21', 'ar21q21', 'ex19q23'], covers=['D3', 'D5'], elements=[2], exam=['X21-21', 'X19-23'],
      problem='Electrons are accelerated from rest through 150 V. What is their de Broglie wavelength?'),
    S("Here's the classic trap. A one hundred and fifty electron volt photon has a much longer wavelength, of eight point two eight "
      "nanometres. Examiners report many students don't distinguish between the two, using the photon formula for electrons, or "
      "treating the electrons as if they travel at c. And for a contrast: a fifty eight gram ball at forty metres per second "
      "has a wavelength around ten to the minus thirty four metres. Nothing is that small, so it never shows wave behaviour.",
      refs=['ar21q21'], covers=['D3', 'D4'], elements=[2, 4], exam=['X21-21'],
      problem='What is the wavelength of a 0.058 kg ball moving at 40 m/s, and could its wave behaviour be seen?'),
]),
Scene('duality', P2, 'Wave-particle duality', V.duality, [
    S("So we can place everything on a scale. As momentum and energy increase, things act more like particles, and as they "
      "decrease, more like waves. The diagram of the electromagnetic spectrum on your information sheet runs from radio waves, "
      "which are very wavelike, to gamma rays, which are very particle like: they hit like tiny bullets, and their wavelengths "
      "are too small to show interference easily.",
      refs=['content'], covers=['D4', 'D6'], elements=[1]),
    S("And photons and electrons obey the same rule. An electron at two times ten to the five metres per second has a wavelength "
      "of three point six times ten to the minus nine metres, near the boundary of ultraviolet and X rays. A photon with the same "
      "wavelength has exactly the same momentum, since p is h over lambda for both. Examiners say some students don't "
      "realise photons have momentum at all.",
      refs=['ex19q23', 'ar19q23'], covers=['D3', 'C1', 'D6'], elements=[2, 4], exam=['X19-23'],
      problem='An electron moves at 2.0 × 10⁵ m/s. What is its wavelength, and how does its momentum compare with a photon of the same wavelength?'),
]),
Scene('spectra', P2, 'Line spectra', V.spectra, [
    S("A hot solid gives a continuous spectrum. But pass a current through a low pressure gas, and it emits only certain "
      "wavelengths. That's an emission spectrum: bright lines on a dark background. Here are the visible lines of hydrogen.",
      refs=['content', 'ex21q18'], covers=['A1'], elements=[1], exam=['X21-18']),
    S("Now shine white light through a cool gas, and those same wavelengths go missing, leaving dark lines. That's an absorption "
      "spectrum. The gas absorbs exactly the wavelengths that it can emit.", refs=['content'], covers=['A1'], elements=[1]),
    S("Each element has its own set of lines, a kind of fingerprint, which is how we know what stars are made of. Classical "
      "physics couldn't explain this. An electron orbiting a nucleus is accelerating, so it should radiate continuously, and "
      "spiral into the nucleus. That would give a continuous spectrum, and no stable atoms.",
      refs=['content'], covers=['A1', 'A2'], elements=[1]),
]),
Scene('bohr', P2, 'The Bohr-Rutherford atom', V.bohr, [
    S("Bohr combined Rutherford's nucleus with Planck's quantum idea. Electrons can only have certain allowed energies, called "
      "energy levels. In one of these, an electron doesn't radiate. This course treats the model qualitatively, so you don't "
      "need formulas for the orbits.", refs=['content', 'appendix'], covers=['A3', 'A4', 'K4'], elements=[1], anim=4),
    S("When an electron falls to a lower level, one photon is emitted. To rise, it must absorb one photon. The energy of "
      "that photon equals the gap between the levels: h f equals E high minus E low. This form isn't on your sheet, so learn it. "
      "Since the gaps are fixed, the photon energies are fixed, and so you get a line spectrum. That solves the puzzle.",
      refs=['content'], covers=['A5', 'A4'], elements=[1], anim=4),
]),
Scene('levels', P2, 'Energy-level diagrams', V.levels, [
    S("An energy level diagram shows each allowed energy as a horizontal line. Often the ground state is drawn as zero, and "
      "ionisation at the top. Other diagrams use negative values, with zero at ionisation. Only the differences matter. Here's "
      "a made up atom, with levels at zero, two point four, three point six and four point five electron volts.",
      refs=['content'], covers=['A4'], elements=[3]),
    S("Find a wavelength in two steps. Take the difference between two levels, then use lambda equals h c over the difference. "
      "A drop of two point four electron volts gives five hundred and eighteen nanometres: green. A drop of two point one gives "
      "five hundred and ninety one: orange. And a drop of one point two gives one thousand and thirty five: infrared. Use h in "
      "electron volt seconds here, and don't convert to joules unless you're asked.",
      refs=['ar21q18', 'ar25q22', 'ex20q20', 'ex24q23', 'ex22q22', 'ar22q22'], covers=['A6', 'A5'], elements=[2, 3], exam=['X20-20', 'X24-23', 'X22-22'],
      problem='An atom has levels at 0, 2.4, 3.6 and 4.5 eV. What wavelengths come from drops of 2.4, 2.1 and 1.2 eV?'),
    S("Questions also work backwards. Given a line, find its energy, then look for the one pair of levels with that exact gap. "
      "Name both levels. Draw an arrow between them, pointing down for emission. Students often show the energy but not the "
      "transition, or draw between two unrelated lines. Use the diagram provided, and not the picture of the spectrum.",
      refs=['ar18q19', 'ar20q20', 'ar25q22', 'ar22q22', 'ex25q22', 'ex18q19', 'ex21q18'], covers=['A6'], elements=[2, 3], exam=['X18-19', 'X20-20', 'X25-22', 'X21-18', 'X22-22'],
      problem='Given the wavelength of a spectral line, how do you find which two energy levels produced it?'),
]),
Scene('regions', P2, 'Which part of the spectrum?', V.regions, [
    S("You'll often need to name the region of the spectrum, and the diagram on your information sheet shows it. Visible light "
      "runs from about four hundred to seven hundred nanometres. Two hundred nanometres is ultraviolet, though many students call it X "
      "ray. And seven hundred and seventy six nanometres is infrared, not red. In hydrogen, drops to n equals one are "
      "ultraviolet; drops to n equals two include the visible; and drops to n equals three are infrared.",
      refs=['ar25q23', 'ar24q23', 'ar22q22', 'ex22q22', 'ex24q23', 'ex25q23'], covers=['A6', 'D6'], elements=[3, 4], exam=['X22-22', 'X24-23', 'X25-23', 'X20-24']),
]),
Scene('excitation', P2, 'Exciting an atom: photons vs electrons', V.excitation, [
    S("How do atoms get excited in the first place? By photons, or by collisions, and the difference is a favourite question. A "
      "photon must be absorbed whole. So it can only excite an atom if its energy exactly matches a gap. In our atom, a two point "
      "four electron volt photon is absorbed. A three electron volt photon matches no gap, so nothing happens. It passes through.",
      refs=['content', 'ar21q18', 'ex21q18'], covers=['A8', 'A5'], elements=[1, 4], exam=['X21-18'],
      problem='An atom has levels at 0, 2.4 and 3.6 eV. What happens if a 3.0 eV photon strikes it in its ground state?'),
    S("An electron is different. It can hand over only part of its kinetic energy, then carry on. A three electron volt electron "
      "can lift the atom to the two point four level, and scatter with zero point six left over. This is how heat and electric "
      "currents excite gases, as in a fluorescent tube or the aurora. Students often say the scattered electron's energy equals "
      "the photon's. Subtract instead. And the common wrong answer of nothing happening is a mix up with the photon case.",
      refs=['content', 'ar21q18', 'ar25q22', 'ex21q18', 'ex25q22', 'ar20q20', 'ex20q20', 'ex24q23'], covers=['A7', 'A5'], elements=[1, 4], exam=['X21-18', 'X25-22', 'X20-20', 'X24-23'],
      problem='An atom has levels at 0, 2.4 and 3.6 eV. What happens if a 3.0 eV electron strikes it in its ground state?'),
    S("Give enough energy, and the electron leaves completely. That's ionisation. Here it takes six electron volts from the "
      "ground state, which is nine point six times ten to the minus nineteen joules. A photon above that energy can ionise, and any "
      "excess becomes kinetic energy: a seven electron volt photon leaves one electron volt. Likewise, an applied voltage that gives "
      "electrons far more energy than the ionisation level will highly ionise a gas. High energy photons ionise atoms.",
      refs=['content', 'ar22q22', 'ex22q22', 'ar20q20', 'ex20q20'], covers=['A8'], elements=[2, 4], exam=['X22-22', 'X20-20'],
      problem='An atom has an ionisation energy of 6.0 eV. What is that in joules, and what happens if a 7.0 eV photon strikes it?'),
    S("Coming back down, the atom can drop in any combination of steps. Starting from the fourth level, there are six possible lines, "
      "so check you've drawn them all. In this course, excitation goes up in one jump from the ground state, while steps "
      "happen only on the way down. And a very energetic electron doesn't make an equally energetic photon. The largest "
      "photon is limited by the levels, so don't answer ten electron volts. Read carefully: two energy levels means one transition.",
      refs=['ar24q23', 'ar25q22', 'ex25q22', 'ex24q23'], covers=['A5', 'A6', 'A7'], elements=[2, 4], exam=['X24-23', 'X25-22'],
      problem='An atom is excited to its fourth level. How many different photon energies can it emit as it returns to the ground state?'),
]),
Scene('standing_atom', P2, 'Electron standing waves', V.standing_atom, [
    S("De Broglie's idea explains why only certain levels are allowed. Think of the electron as a wave around the nucleus. As with a "
      "string from Criterion 7, only certain standing waves fit: a whole number of wavelengths must fit around the orbit. "
      "If it doesn't join up, it cancels itself out. Each pattern that fits gives one allowed energy level.",
      refs=['content'], covers=['A10'], elements=[1], anim=2),
    S("This is qualitative only. The modern quantum model goes further. It doesn't describe a neat orbit, but an electron cloud, "
      "which shows how likely you are to find the electron in each place. The course only asks for that very simple picture, "
      "so don't worry about going further than this.",
      refs=['content', 'appendix'], covers=['A11', 'A10', 'K4'], elements=[1], anim=2),
]),
# ------------------------------------------------------------------- part 3
Scene('rutherford', P3, 'Discovering the nucleus', V.rutherford, [
    S("Part three moves into the nucleus. In nineteen oh nine, Rutherford's team fired alpha particles at thin gold foil. Most "
      "went straight through, so the atom is mainly empty space. But a very small number bounced almost straight back. Only a "
      "tiny, massive, positive centre could do that: the nucleus.", refs=['content'], covers=['N1'], elements=[1]),
    S("Some nuclei are unstable. Radioactivity is when an unstable nucleus spontaneously emits radiation, as it changes to a more "
      "stable state. We can't predict when one particular nucleus will decay, only how a large number behave.",
      refs=['content'], covers=['N2'], elements=[1]),
]),
Scene('radiation', P3, 'Alpha, beta and gamma', V.radiation, [
    S("There are three main types. An alpha particle is a helium nucleus: charge plus two, stopped by paper or a few centimetres of air, "
      "and strongly ionising. A beta particle is a fast electron or positron, moderately ionising, and stopped by a little "
      "aluminium. Gamma is a high energy photon, with no charge. It's weakly ionising, and very penetrating: lead reduces it, but never stops it completely.",
      refs=['content'], covers=['N2'], elements=[1]),
    S("Where do they come from? Alpha decay is associated with large nuclei, which have too many nucleons. Beta decay comes from a "
      "change inside the nucleus. In beta minus, a neutron becomes a proton and an electron. In beta plus, a proton becomes a neutron "
      "and a positron. So electrons in beta decay don't come from the atom's own shells.",
      refs=['content'], covers=['N3', 'N4'], elements=[1]),
    S("Now a prediction, for element four. A sealed source falls off a truck. Which radiation lets a detector in a moving vehicle find it? "
      "Rule out the others, too. Neutrinos barely interact. Beta particles and alpha particles have too short a range. "
      "Gamma has a long range in air and still ionises enough to be detected. Don't assume the heaviest particle goes furthest.",
      refs=['ex23q20', 'ar23q20'], covers=['N2'], elements=[4], exam=['X23-20'],
      problem='A lost radioactive source emits beta, gamma and antineutrinos. Which of these lets a vehicle-mounted detector find it?'),
]),
Scene('particles', P3, 'Neutrons, positrons and neutrinos', V.particles, [
    S("You also need to know some other particles. The neutron has no charge, and about the same mass as a proton. It lives in the nucleus, and it's released in fission. "
      "The positron is like an electron, but with positive charge. It has charge plus one and mass number zero, "
      "so don't label it a neutron, as students sometimes do.",
      refs=['content', 'ar18q22'], covers=['N5'], elements=[1], exam=['X18-22']),
    S("The neutrino has zero charge, a very tiny mass and very high speed. It's not massless, though many students say so. It barely "
      "interacts with anything. A neutrino comes out with beta plus decay, and its antiparticle, the antineutrino, comes out with "
      "beta minus decay. Learn all three properties: mass, charge and speed.",
      refs=['content', 'ar21q20', 'ex21q20'], covers=['N5'], elements=[1], exam=['X21-20']),
    S("When a positron meets an electron, they annihilate, and produce two gamma photons. Their mass becomes energy. Each photon has at least "
      "the mass energy of one electron: zero point zero zero zero five four nine atomic mass units, times nine hundred and thirty one. "
      "That's zero point five one one mega electron volts. As an aside beyond the course, that's the basis of P E T scans.",
      refs=['ex20q22', 'ar20q22'], covers=['N5', 'M1'], elements=[2], exam=['X20-22'],
      problem='A positron and an electron annihilate, producing two identical photons. What is the minimum energy of each?'),
]),
Scene('background', P3, 'Activity and background radiation', V.background, [
    S("We measure a source using its activity, A: the number of decays each second. The unit is the becquerel, where one "
      "becquerel is one decay per second. Background radiation is ionising radiation that doesn't come from the source being "
      "studied. It's always there: from rocks and soil, radon gas, cosmic rays, food, and medical uses.",
      refs=['content'], covers=['N6', 'N7'], elements=[1]),
    S("Will a detector notice a weak sample? A sample of twenty becquerel has twelve hundred decays each minute. That sounds like "
      "plenty, against a background of twenty four counts per minute. But radiation goes in all directions, and the tube catches only a "
      "small part. If it catches one percent, that's twelve counts per minute, which is a small rise. Activity isn't the same as count "
      "rate. In any experiment, subtract the background first.",
      refs=['ar18q24', 'ex18q24'], covers=['N6', 'N7'], elements=[4], exam=['X18-24'],
      problem='A 20 Bq sample sits by a Geiger tube that catches 1% of decays, with a background of 24 counts/min. Would you notice it?'),
]),
Scene('isotopes', P3, 'Isotopes and notation', V.isotopes, [
    S("Now the notation. A is the mass number: protons plus neutrons, together called nucleons. Z is the atomic number, the number of "
      "protons. Isotopes have the same Z but different numbers of neutrons. A radioisotope is an unstable isotope. The atomic "
      "mass unit, u, also called the dalton, is one twelfth of the mass of a carbon twelve atom. The nuclear section of your "
      "information sheet lists masses in u for the proton, neutron and electron.",
      refs=['content'], covers=['R1', 'R7'], elements=[1]),
]),
Scene('equations', P3, 'Writing decay equations', V.equations, [
    S("A decay is a transmutation: the parent nucleus changes into a daughter nucleus, usually a new element. In every "
      "equation, A must balance, and so must Z. For alpha decay, A falls by four and Z falls by two. For americium two four one, that "
      "gives neptunium two three seven, plus helium four. There's no neutrino in alpha decay.",
      refs=['content', 'ar25q21', 'ex25q21'], covers=['R2', 'R3'], elements=[1], exam=['X25-21'],
      problem='Write the alpha decay equation for americium-241 (Z = 95).'),
    S("In beta minus decay, A stays the same, and Z goes up by one. Strontium ninety becomes yttrium ninety, plus an electron, plus "
      "an antineutrino. In beta plus decay, Z goes down by one. Fluorine eighteen becomes oxygen eighteen, plus a positron, plus a "
      "neutrino. The most common lost mark in reports is leaving out the neutrino or antineutrino.",
      refs=['content', 'ar23q19', 'ar24q19', 'ar20q22', 'ar18q22', 'ex23q19', 'ex24q19', 'ex18q24', 'ex21q20'], covers=['R3', 'N4'], elements=[1],
      exam=['X23-19', 'X24-19', 'X20-22', 'X18-24', 'X21-20'],
      problem='Write the decay equations for strontium-90 (beta minus, Z = 38) and fluorine-18 (beta plus, Z = 9).'),
    S("Gamma decay changes neither A nor Z. A nucleus left in an excited, metastable state, marked with a small m, gives out a gamma "
      "photon as it settles. So technetium ninety nine m becomes technetium ninety nine, plus gamma. This is what a medical "
      "scan detects. Remember to show the metastable marker on the left side.",
      refs=['content', 'ar23q19', 'ex23q19'], covers=['R3'], elements=[1], exam=['X23-19']),
    S("The common errors: leaving out a neutrino, an equals sign instead of an arrow, numbers that don't balance, leaving the "
      "metastable marker off, or writing the daughter as just X with no numbers. Asked for a decay equation, students sometimes "
      "copy the half life formula from the information sheet. And if you include an energy term, put it on the correct side.",
      refs=['ar23q19', 'ar25q21', 'ar24q19', 'ar22q19'], covers=['R3'], elements=[1], exam=['X25-21', 'X23-19']),
]),
Scene('series', P3, 'Decay series', V.series, [
    S("A daughter can be unstable too, so one decay can follow another, in a decay series. Here's the start of radium two two six's "
      "chain. Alpha decays step diagonally, while beta minus decays step across. It carries on until it reaches a stable isotope. "
      "If a decay produces no gamma, it suggests the daughter was formed in its stable state, with no excess energy to shed. "
      "The other reasonable answer: it's metastable and will release that energy later.",
      refs=['content', 'ex24q19', 'ar24q19'], covers=['R2'], elements=[1, 4], exam=['X24-19']),
]),
Scene('halflife', P3, 'Half-life and activity', V.halflife, [
    S("Half life is the time for half the nuclei in a sample to decay. On your information sheet, in the nuclear section: minus d N d t "
      "equals lambda N equals A. So activity is proportional to the number of nuclei. Lambda here is the decay constant, not a "
      "wavelength. And lambda equals zero point six nine three over the half life. Forgetting that zero point six nine three is a common error.",
      refs=['content', 'ar19q20'], covers=['R4', 'R5'], elements=[1], exam=['X19-20']),
    S("Also from the sheet, for any time: N over N zero equals e to the minus lambda t. Activity and count rate fall in just the "
      "same way. The trap is rearranging it incorrectly. Examiners see A equals e to the minus lambda t over A zero, which is wrong. "
      "A equals A zero, times e to the minus lambda t.",
      refs=['content', 'ar25q21', 'ex25q21'], covers=['R6'], elements=[1, 2], exam=['X25-21']),
    S("Two more forms. Mass falls in the same ratio, m over m zero. So does two to the minus t over T: that's useful for whole half lives. "
      "These two aren't on your sheet, so learn them. And to go between atoms and mass, the sheet has N equals m N A over M, with m "
      "in grams. Remember to convert kilograms to grams, as many students lost marks there.",
      refs=['content', 'ar20q21', 'ar19q20', 'ex20q21'], covers=['R6'], elements=[1, 2], exam=['X20-21']),
]),
Scene('we_activity', P3, 'Worked example: a medical isotope', V.we_activity, [
    S("Element two. Iodine one three one has a half life of eight point zero two days, and a sample has an activity of five "
      "megabecquerels. A becquerel is per second, so the decay constant has to be in per second. That's zero point six nine three, "
      "over eight point zero two days in seconds, which is one times ten to the minus six. Then N is A over lambda: five times ten "
      "to the twelve atoms. Unit errors here are the commonest in the reports. Also, don't reach for the molar mass formula: you don't need it for N.",
      refs=['ar22q20', 'ar23q19', 'ex22q20', 'ex23q19', 'ex25q21', 'ar25q21'], covers=['R5', 'R6'], elements=[2], exam=['X22-20', 'X23-19', 'X25-21'],
      problem='A sample of iodine-131 (half-life 8.02 days) has an activity of 5.0 MBq. How many atoms does it contain?'),
    S("For the mass, use N equals m N A over M from the sheet, rearranged. That's five times ten to the twelve, times one hundred "
      "and thirty one, over Avogadro's number: about one times ten to the minus nine grams. That tiny mass gives five million decays "
      "each second, which is why a small dose can be so dangerous.",
      refs=['ex22q20', 'ex21q20', 'ar21q20', 'ex20q21', 'ar20q21', 'ex24q19'], covers=['R5', 'R6'], elements=[2], exam=['X22-20', 'X21-20', 'X20-21'],
      problem='What is the mass of 5.0 × 10¹² atoms of iodine-131?'),
    S("What about twenty days later? Time and half life are both in days, so lambda t is one point seven three, and the days cancel. "
      "A is five times e to the minus one point seven three, or zero point eight nine megabecquerels. Going ten days back, reverse the "
      "sign, to get about twelve. It should be bigger, and it is. Check: twenty days is about two and a half half lives, so "
      "about eighteen percent should remain.",
      refs=['ar22q20', 'ar25q21', 'ex22q20', 'ex24q19', 'ar24q19'], covers=['R6'], elements=[2], exam=['X22-20', 'X25-21', 'X24-19'],
      problem='An iodine-131 sample (half-life 8.02 days) now has 5.0 MBq. What will its activity be in 20.0 days, and what was it 10.0 days ago?'),
]),
Scene('we_age', P3, 'Finding a time: natural logs', V.we_age, [
    S("To find a time, you need natural logs. Radiometric dating is the classic case. Old wood has forty percent of the carbon "
      "fourteen activity of living wood, and the half life is five thousand seven hundred and thirty years. So zero point four "
      "zero equals e to the minus lambda t. Take natural logs: lambda t is zero point nine one six. Dividing by lambda gives about "
      "seven thousand six hundred years.",
      refs=['ex21q20', 'ar21q20', 'appendix'], covers=['R6', 'K1'], elements=[2], exam=['X21-20'],
      problem='Old wood has 40% of the carbon-14 activity of living wood (half-life 5730 y). How old is it?'),
    S("Watch the wording. Seventy three percent less means twenty seven percent remains. A percentage of a mass needs care: zero point "
      "five percent of three grams is zero point zero one five grams, which many students get wrong. To go back in time, flip the sign. An "
      "isotope now at two percent of an element, with half life ten to the nine years, was eight percent two half lives ago, if "
      "the other isotopes don't decay. And if a nucleus has two decay routes, use the half life for the route being asked about.",
      refs=['ex20q21', 'ar20q21', 'ar21q20', 'ar18q24', 'ex18q24'], covers=['R6'], elements=[2, 4], exam=['X20-21', 'X18-24', 'X21-20'],
      problem='An isotope is now 2.0% of an element, with half-life 1.0 × 10⁹ y. What was its percentage 2.0 × 10⁹ y ago, if the other isotopes do not decay?'),
]),
Scene('we_power', P3, 'Worked example: a nuclear battery', V.we_power, [
    S("Here's a multi step problem, for element four. A deep space probe needs zero point five zero watts of electrical power, from "
      "americium two four one, at five percent efficiency. First, why not solar panels? Because far from the Sun, sunlight has "
      "spread out and is too weak. It isn't that something blocks it. The total power needed is zero point five zero, over "
      "zero point zero five zero: ten watts.",
      refs=['ex19q20', 'ar19q20'], covers=['R5'], elements=[2, 4], exam=['X19-20', 'X24-19'],
      problem='A probe needs 0.50 W of electricity from Am-241 (half-life 432 y, 5.6 MeV per decay) at 5.0% efficiency. Why not use solar panels, and what mass is needed?'),
    S("Each decay releases five point six mega electron volts. Converting needs care: mega to electron volts first, then to joules, which "
      "gives eight point nine six times ten to the minus thirteen. Ten joules each second means an activity of one point one times "
      "ten to the thirteen becquerel. Activity is simply power divided by energy per decay.",
      refs=['ar19q20', 'ex24q19', 'ar24q19'], covers=['R5', 'N7'], elements=[2], exam=['X19-20', 'X24-19']),
    S("The half life in seconds gives lambda, five point zero nine times ten to the minus eleven per second. N is A over lambda: two "
      "point two times ten to the twenty three atoms. Then the mass is N M over N A, about eighty eight grams. The formula gives "
      "grams, so convert if you need kilograms: a slip here puts you out by a factor of a thousand. After seventy years, about eighty nine percent remains, so the power falls very slowly.",
      refs=['ar19q20', 'ar24q19', 'ex24q19', 'ex19q20', 'ex21q20'], covers=['R5', 'R6'], elements=[2], exam=['X19-20', 'X24-19', 'X21-20']),
]),
Scene('decay_data', P3, 'Half-life from experimental data', V.decay_data, [
    S("Element three. A Geiger counter records four hundred and thirty, three hundred and thirteen, two hundred and thirty, one hundred "
      "and seventy one and one hundred and thirty counts per minute, every two minutes. The background is thirty counts per minute. Before "
      "you do anything else, subtract the background from every reading.",
      refs=['content'], covers=['R4', 'N6'], elements=[3],
      problem='Count rates are 430, 313, 230, 171 and 130 counts/min at 2-minute intervals, with a background of 30 counts/min. What is the half-life?'),
    S("Now plot the net count rate. Read the half life off by finding the time to halve, from any starting point. Four hundred down "
      "to two hundred takes four minutes, and two hundred down to one hundred takes four more. So the half life is a constant four "
      "minutes, and that constancy is your evidence of exponential decay. The decay constant is zero point six nine three over four: about zero point one seven per minute.",
      refs=['content'], covers=['R4', 'R6'], elements=[2, 3]),
]),
# ------------------------------------------------------------------- part 4
Scene('emc2', P4, 'Mass-energy equivalence', V.emc2, [
    S("Part four. E equals m c squared, in the nuclear section of your information sheet, says mass and energy are equivalent. In every "
      "reaction, the total of mass and energy is conserved. Use it with kilograms and joules. For nuclear work, the same section gives a "
      "conversion: nine hundred and thirty one mega electron volts for each atomic mass unit. Multiply by nine hundred and thirty one. "
      "The commonest errors are dividing instead, and rounding it to nine hundred and forty.",
      refs=['content', 'ar22q19', 'ar23q20'], covers=['M1'], elements=[1], exam=['X22-19', 'X23-20']),
    S("Suppose a star radiates one point two times ten to the twenty seven watts. Each second, it loses mass equal to E over c "
      "squared: one point three times ten to the ten kilograms. Include the per second in your unit. A star that's losing mass far "
      "faster than the Sun, using up its fuel quickly, should have a shorter life. That's a reasoned prediction.",
      refs=['ex23q21', 'ar23q21', 'ex18q22'], covers=['M1'], elements=[2, 4], exam=['X23-21', 'X18-22'],
      problem='A star radiates 1.2 × 10²⁷ W. How much mass does it lose each second, and what does that suggest about its lifetime?'),
]),
Scene('binding', P4, 'Mass defect and binding energy', V.binding, [
    S("Here's a surprise. Weigh a nucleus, and it has less mass than its separate protons and neutrons. The difference is the mass "
      "defect. The equivalent energy is the binding energy: the energy you must supply to pull the nucleus completely apart. "
      "The more binding energy per nucleon, the more stable the nucleus.",
      refs=['content'], covers=['M2'], elements=[1]),
    S("Example for element two. A nickel sixty two atom, Z equals twenty eight, has a mass of sixty one point nine two eight "
      "three four five u. The parts are twenty eight protons, twenty eight electrons, and thirty four neutrons, using the sheet's "
      "masses: sixty two point five one three seven one u. Subtract to get a mass defect of zero point five eight five three six five u.",
      refs=['ex19q21', 'ar19q21', 'ex24q21', 'ar24q21', 'ex21q20', 'ar21q20'], covers=['M2'], elements=[2], exam=['X19-21', 'X24-21', 'X21-20'],
      problem='A nickel-62 atom (Z = 28) has a mass of 61.928345 u. What is its binding energy per nucleon?'),
    S("Multiply by nine hundred and thirty one to get five hundred and forty five mega electron volts. Divide by sixty two nucleons, to "
      "get eight point seven nine per nucleon. Common errors: converting the whole atom's mass to energy, assuming the parts add to a "
      "whole number, and dividing by Z or by nine hundred and thirty one. Read carefully: a quoted atomic mass includes electrons, so "
      "add them, but for a mass given for the nucleus, don't. And check whether you've been asked for the total, or per nucleon.",
      refs=['ar19q21', 'ar24q21', 'ar22q19', 'ar21q20', 'ex22q19'], covers=['M2'], elements=[2], exam=['X19-21', 'X24-21', 'X22-19', 'X21-20']),
]),
Scene('be_curve', P4, 'The binding energy per nucleon curve', V.be_curve, [
    S("Plot binding energy per nucleon against mass number, and you get this famous curve. It rises steeply, peaks near iron, then "
      "slowly falls. Higher on the curve means more tightly bound and more stable, which is why iron and nickel are so stable.",
      refs=['content', 'ex19q21'], covers=['M4', 'M2'], elements=[3], exam=['X19-21']),
    S("Energy is released by moving up the curve, from either side. Light nuclei join together: that's fusion. Heavy nuclei split: that's "
      "fission. In both cases the products are more tightly bound, have less total mass, and so energy is released. Examiners say many "
      "students can place fission and fusion, but few can explain how binding energy relates to the energy obtained. So explain it.",
      refs=['content', 'ar19q21'], covers=['M4'], elements=[1, 3], exam=['X19-21']),
    S("Why does it stop at iron? Fusing beyond iron moves down the curve, so the products are less tightly bound. That needs an input of energy "
      "rather than releasing it, so it can't be sustained in typical stars. In your answer, talk about the elements after iron, not "
      "iron itself. Elements around iron can't give energy by either process.",
      refs=['ex24q21', 'ar24q21', 'ex19q21'], covers=['M4'], elements=[1, 4], exam=['X24-21', 'X19-21'],
      problem='Why can fusion producing elements heavier than iron not be sustained in typical stars?'),
]),
Scene('reaction_energy', P4, 'Energy from a mass difference', V.reaction_energy, [
    S("For a reaction, compare the total mass before and after. Take deuterium plus tritium, which makes helium four and a neutron. The "
      "mass goes from five point zero two nine zero five four u down to five point zero one zero one seven one u. The difference is "
      "zero point zero one eight eight eight three u, which, times nine hundred and thirty one, is seventeen point six mega electron volts.",
      refs=['content'], covers=['M3', 'M1'], elements=[2], exam=['X18-22'],
      problem='Deuterium (2.013553 u) and tritium (3.015501 u) fuse into helium-4 (4.001506 u) and a neutron (1.008665 u). How much energy is released?'),
    S("Fission works the same way. Uranium two three five plus a neutron splits into barium, krypton and three neutrons. The total "
      "falls by zero point one eight six zero two one u, which releases one hundred and seventy three mega electron volts. Notice that this is ten "
      "times the fusion figure per reaction, but fusion gives more per nucleon.",
      refs=['content'], covers=['M3', 'M5'], elements=[2],
      problem='The fission of U-235 + n → Ba-141 + Kr-92 + 3n has a mass drop of 0.186021 u. How much energy is released?'),
    S("Then check the sign. If the products are lighter, energy is released, as gamma photons or kinetic energy. If the products are "
      "heavier, energy must be supplied. For instance, a gamma photon needs a minimum energy to knock a neutron out of a nucleus. "
      "Students often claim energy is released when the mass shows otherwise. Count every particle. In TASC beta minus questions, treat the given masses as nuclear "
      "masses, and subtract the electron's zero point zero zero zero five four nine u. The 2023 report names leaving it out as a common mistake. The exception is if the question explicitly says "
      "atomic masses: then the electron's mass cancels. And don't work out separate mass defects if a simple total will do.",
      refs=['ex20q22', 'ar20q22', 'ex23q20', 'ar23q20', 'ar22q19', 'ex25q19', 'ar25q19', 'ex19q20', 'ex21q20', 'ar21q20'], covers=['M3'], elements=[2, 4],
      exam=['X20-22', 'X23-20', 'X22-19', 'X25-19', 'X19-20', 'X21-20']),
]),
Scene('stars', P4, 'Fusion in stars', V.stars, [
    S("Stars are powered by fusion, which is the course's context here. In the Sun, the net result is four protons becoming a "
      "helium nucleus, two positrons and two neutrinos, releasing about twenty five mega electron volts. Only very hot, dense cores can "
      "do this. Very high speeds let nuclei overcome their electric repulsion, and high density makes collisions frequent. Fusion is "
      "the source of almost all the energy we use on Earth.",
      refs=['ex18q22', 'ar18q22', 'appendix', 'ex22q19'], covers=['M3', 'K3'], elements=[1, 4], exam=['X18-22', 'X22-19']),
    S("Here's an element two chain. At a distance of two point two eight times ten to the eleven metres from a star, each square "
      "metre receives five hundred and ninety watts. Multiply by the area of the whole sphere, four pi r squared, to get a total power "
      "of three point nine times ten to the twenty six watts. E equals m c squared gives four point three times ten to the nine kilograms lost each "
      "second. Dividing the power by the energy per reaction gives about ten to the thirty eight reactions per second. Lay it out clearly.",
      refs=['ex18q22', 'ar18q22', 'ex23q21'], covers=['M1', 'K3'], elements=[2], exam=['X18-22', 'X23-21'],
      problem='A star delivers 590 W/m² at a distance of 2.28 × 10¹¹ m. What are its total power, its mass loss each second and its reactions per second at 24.7 MeV each?'),
    S("In giant stars, helium goes on to form carbon. Two helium nuclei make beryllium eight, which is very short lived, and that step "
      "takes in energy, as its mass is slightly higher. If another helium hits it in time, you get carbon twelve, and energy is released. "
      "It's only possible because the temperature and density are so high. Explain why, don't just list them. And when Rutherford's alpha "
      "particles hit nitrogen, the products were also heavier, so energy was absorbed.",
      refs=['ex22q19', 'ar22q19', 'ex25q19', 'ar25q19'], covers=['M3', 'K3'], elements=[1, 4], exam=['X22-19', 'X25-19'],
      problem='How can short-lived beryllium-8 absorb another helium nucleus to form carbon inside a giant star?'),
]),
Scene('fission', P4, 'Fission and chain reactions', V.fission, [
    S("Fission is when a heavy nucleus splits into two smaller ones, plus some neutrons. A neutron striking uranium two three five "
      "usually triggers it. Uranium can also split on its own, though very rarely. Each fission releases two or three more neutrons.",
      refs=['content', 'ex20q21'], covers=['M5'], elements=[1], exam=['X20-21']),
    S("Those neutrons can then split more nuclei, giving a chain reaction. In a small lump, too many neutrons escape through the surface, and "
      "the reaction dies out. The critical mass is the smallest mass that keeps the chain going. Above it, the rate can grow very quickly.",
      refs=['content', 'ex20q21'], covers=['M5'], elements=[1, 4], exam=['X20-21']),
]),
Scene('reactor', P4, 'A fission reactor', V.reactor, [
    S("A fission reactor keeps the chain reaction under control. It has fuel rods surrounded by a moderator, such as water or graphite. "
      "The moderator slows the fast neutrons, because slow neutrons are far more likely to cause fission. Control rods absorb neutrons: "
      "push them in to slow the reaction, or pull them out to speed it up. And a heat exchanger passes the heat from the coolant to make steam, which drives a turbine.",
      refs=['content', 'appendix'], covers=['M6', 'K8'], elements=[1], anim=2),
    S("Nuclear power produces electricity without burning fossil fuels, but it has also caused serious accidents, and the waste "
      "stays radioactive for a long time. Weighing those risks and benefits is a scientific and a political question, and it's a "
      "good topic for internal tasks.",
      refs=['appendix'], covers=['K2', 'K8'], elements=[4], anim=2),
]),
Scene('strong_force', P4, 'Why the nucleus holds together', V.strong_force, [
    S("Protons repel each other, so why doesn't the nucleus fly apart? Try a calculation, which also needs Coulomb's law from the electrostatics "
      "section of your sheet. An alpha particle and a carbon nucleus, five femtometres apart, have charges of two e and six e. The force "
      "is about one hundred and ten newtons. That's enormous for such tiny masses. Take charges from the atomic number, not the mass, "
      "and remember to square the distance.",
      refs=['ex25q19', 'ar25q19', 'info1e'], covers=['R8'], elements=[2, 4], exam=['X25-19'],
      problem='An alpha particle and a carbon nucleus (Z = 6) are 5.0 fm apart. What is the electric force, and what does it suggest about nuclei?'),
    S("So something stronger must hold nuclei together: the strong nuclear force. It's very short range, reaching only about the size of "
      "a nucleus, so it doesn't reach outside. And it only acts on protons and neutrons, not on electrons. That's what you need to "
      "know.", refs=['content'], covers=['R8'], elements=[1], exam=['X25-19']),
]),
Scene('quarks', P4, 'Inside the nucleon: quarks', V.quarks, [
    S("Protons and neutrons are not fundamental. In the Standard Model, each one is made of three quarks. In this course, you only need "
      "up quarks, with charge plus two thirds, and down quarks, with charge minus one third. A proton is up, up, down, for a total charge "
      "of plus one. A neutron is up, down, down, with a total of zero.",
      refs=['content'], covers=['M7'], elements=[1], anim=2),
    S("Quarks have a property called colour charge, which has nothing to do with actual colour. It comes in three kinds, called red, green and "
      "blue. Gluons carry the force between quarks. It's all qualitative, and limited to protons and neutrons, so there's no need "
      "to study mesons.", refs=['content'], covers=['M7'], elements=[1], anim=2),
]),
# ------------------------------------------------------------------- part 5
Scene('relativity', P5, 'Relativity and force carriers', V.relativity, [
    S("Part five is for internal assessment only. These dot points are qualitative, and they won't be in the external exam. The Standard "
      "Model recognises different gauge bosons, each carrying a force. Gluons carry the strong force, W and Z bosons carry the weak "
      "force, and photons carry the electromagnetic force.",
      refs=['internal'], covers=['S1'], elements=[1]),
    S("At very high speeds, Newtonian physics fails. Muons created high in the atmosphere should mostly decay before reaching the ground, "
      "but they arrive in large numbers, because their half life is dilated. Particles in accelerators have more momentum than m v predicts. "
      "Einstein's theory rests on two postulates. The speed of light in a vacuum is an absolute constant, and all inertial reference frames are equivalent.",
      refs=['internal'], covers=['S2', 'S4'], elements=[1]),
    S("It follows that motion can only be measured relative to an observer. Length and time depend on your frame of reference. As speeds "
      "approach c, the results are very different from Newton's. Relativistic momentum increases without limit, which stops an object from reaching the "
      "speed of light. And mass energy equivalence came from this theory: it explains the source of nuclear energy.",
      refs=['internal'], covers=['S3', 'S5', 'S6', 'S7'], elements=[1]),
]),
Scene('contexts', P5, 'Contexts named in the course', V.contexts, [
    S("Finally, the course lists contexts to explore, which are useful for internal tasks and Criterion 4. Details beyond the content "
      "aren't examined externally. The development of the quantum model runs from Planck and Einstein to Bohr and then to orbitals. Black "
      "body radiation explains the greenhouse effect: Earth's surface radiates infrared, which atmospheric molecules absorb. Radiometric dating "
      "uses half lives. And particle accelerators use electric and magnetic fields to speed up charged particles, for research and medical isotopes.",
      refs=['appendix'], covers=['K4', 'K5', 'K1', 'K10'], elements=[4]),
    S("Harnessing nuclear power, and reactors themselves, raise questions of risk and benefit. Fusion in stars powers the Sun and built "
      "the elements heavier than helium. The Big Bang theory has evidence from cosmic background radiation, the abundance of light "
      "elements, and the red shift of galaxies.",
      refs=['appendix'], covers=['K2', 'K8', 'K3', 'K11'], elements=[4]),
    S("Special relativity grew from the work of Michelson, Lorentz, Einstein and others. Ring laser gyroscopes navigate using tiny "
      "timing differences between light travelling both ways around a ring. And the Higgs boson, predicted in the nineteen sixties, helps "
      "to explain why particles have mass. A particle consistent with it was observed at the Large Hadron Collider.",
      refs=['appendix'], covers=['K6', 'K7', 'K9'], elements=[4]),
]),
# ------------------------------------------------------------------- finish
Scene('exam_tips', P6, 'Tips for tests and the exam', V.exam_tips, [
    S("Finally, technique for tests and the exam. These come from what examiners have reported over several years. One: there are "
      "two values of h. Match them to your units. Two: convert before you substitute: nanometres, picometres, kilo and mega electron volts, days and years.",
      refs=['ar23q22', 'ar22q24', 'ar23q23', 'ar19q20']),
    S("Three: match the units of half life and decay constant, and use seconds if you need becquerels. Four: keep photons and electrons "
      "apart. E equals h c over lambda is only for photons. Lambda equals h over m v is for particles.",
      refs=['ar25q21', 'ar23q19', 'ar21q21']),
    S("Five: momentum is a vector, so draw the diagram and show directions and signs. Six: use grams in N equals m N A over M, and "
      "remember that count rate isn't activity.",
      refs=['ar24q24', 'ar18q21', 'ar20q21', 'ar18q24']),
    S("Seven: in a show that question, you must write out the working, and then use your own value afterwards if you can. Eight: "
      "for a decay equation, use an arrow, balance A and Z, and include the neutrino. Markers carry errors forward, so keep going, and show your working clearly.",
      refs=['ar22q24', 'ar22q22', 'ar23q19', 'ar19q20']),
]),
Scene('more_tips', P6, 'More examiner tips', V.more_tips, [
    S("Here are more. Nine: sketch X ray spectra with wavelength on the axis, a sharp cut off and labelled lines. Ten: intensity changes "
      "the number of electrons, not their energy. Eleven: excitation goes up from the ground state, and photons need an exact match. Twelve: "
      "the opening text of a question applies to all of its parts.",
      refs=['ar23q23', 'ar21q19', 'ar24q23', 'ar25q23']),
    S("Thirteen: when you sketch a cooler black body, keep it below the hotter one everywhere. Fourteen: for binding energy per nucleon, "
      "divide by A. Fifteen: check the marks on offer before starting: a one mark mass difference doesn't need several mass defects. And "
      "sixteen: check your spectrum region. Don't call two hundred nanometres X ray, or seven hundred and seventy six nanometres red.",
      refs=['ar21q22', 'ar19q21', 'ar25q19', 'ar25q23', 'ar24q23']),
]),
Scene('summary', P6, 'Summary', V.summary, [
    S("That's every part of Criterion 8. Light comes in photons, with energy and momentum. Particles have wavelengths. Atoms have energy "
      "levels, and those give line spectra. Unstable nuclei decay, with half lives you can calculate. And mass and energy are equivalent, "
      "which drives both fission and fusion. Practise explaining each idea in words, as well as with numbers, and you'll be ready for your "
      "tests and for Section D. Good luck."),
]),
]

# Report references that no slide cites are left out of the reference list.
_used = {r for sc in SCENES for st in sc.steps for r in st.refs} | {t[1] for t in EXAM_TOPICS.values()} \
    | {t[1] for t in SYLLABUS.values()} | {t[1] for t in ELEMENTS.values()} | {'info'}
REFS = {k: r for k, r in REFS.items() if k in _used}

VIDEO = Video(
    id='PHY415115_C8_quantum_nuclear',
    course=COURSE, course_name='Physics', module=MODULE,
    module_name='Criterion 8: Identify and apply principles of the wave-particle nature of light, atomic and nuclear physics '
                'and models of the nucleus and nuclear processes',
    title='Criterion 8: quantum and nuclear physics, complete revision',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Quantum, Nuclear'),
    checks=CHECKS,
    thumbnail=V.thumbnail,
    allowed_overlaps=['identify and apply principles of the wave-particle nature of light, atomic and nuclear physics'],
    keywords=['photon', 'black body', 'work function', 'threshold frequency', 'stopping voltage', 'electron volt', 'photoelectric',
              'continuous spectrum', 'characteristic', 'cut off', 'momentum', 'Compton', 'de Broglie', 'energy level', 'ground state',
              'ionisation', 'emission', 'absorption', 'half life', 'decay constant', 'activity', 'becquerel', 'isotope', 'neutrino',
              'antineutrino', 'positron', 'mass defect', 'binding energy', 'fission', 'fusion', 'chain reaction', 'critical mass',
              'moderator', 'control rods', 'strong nuclear force', 'quark', 'gluon'],
    description=('A complete revision explainer for TASC Physics (PHY415115) Criterion 8: the wave-particle nature of light, atomic '
                 'and nuclear physics, and models of the nucleus and nuclear processes. For class tests and the end-of-year exam '
                 '(Section D). Formulas from the TASC information sheet are labelled on screen.'),
)
