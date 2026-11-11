"""PHY415115 Physics, Criterion 7: Identify and apply general principles of wave motion.

Worked example of a full video spec.  Build with:
    uv run python -m explainer check   videos/PHY415115/c7_wave_motion.py
    uv run python -m explainer preview videos/PHY415115/c7_wave_motion.py
    uv run python -m explainer thumbnail videos/PHY415115/c7_wave_motion.py
    uv run python -m explainer render  videos/PHY415115/c7_wave_motion.py    # operator only: narration, video, docs
"""
import math

from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, InfoSheet, import_sibling

COURSE, MODULE = 'PHY415115', 'C7'
L.use(style.theme(COURSE, MODULE))
V = import_sibling(__file__, 'c7_visuals.py')

P0 = 'Criterion 7 · Overview'
P1 = 'Part 1 · What waves are'
P2 = 'Part 2 · Boundaries: reflection & refraction'
P3 = 'Part 3 · Superposition'
P4 = 'Part 4 · Interference, diffraction & polarisation'
P5 = 'Finish · Tests & exam technique'

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
    2018: {13: 31, 14: 32, 15: 33, 16: '33-35', 17: '36-37', 18: '37-39'},
    2019: {13: 27, 14: '28-29', 15: '30-31', 16: '32-33', 17: '34-35', 18: 36},
    2020: {13: 28, 14: 29, 15: '30-31', 16: 32, 17: 33, 18: '34-35'},
    2021: {12: '31-32', 13: 33, 14: '34-35', 15: '36-37', 16: '38-39', 17: '40-41'},
    2022: {13: '31-32', 14: 33, 15: '34-35', 16: 36, 17: '37-38', 18: 39},
    2023: {13: 39, 14: '40-41', 15: '42-43', 16: '44-45', 17: '46-47', 18: '48-49'},
    2024: {13: '36-37', 14: '38-39', 15: '40-41', 16: '42-43', 17: '44-45', 18: 46},
    2025: {12: '31-32', 13: '33-34', 14: 35, 15: '36-37', 16: '38-39', 17: '40-41'},
}
REPORT_PAGES = {
    2018: {13: 4, 14: '4-5', 15: 5, 16: 5, 17: 5, 18: 6},
    2019: {13: 15, 14: '15-16', 15: 16, 16: '16-17', 17: 17, 18: 18},
    2020: {13: '4, 12', 14: '4, 12', 15: '5, 12-13', 16: '5, 14', 17: '5, 14', 18: '5, 14'},
    2021: {12: '11-12', 13: '12-13', 14: '13-14', 15: '14-15', 16: '15-16', 17: '16-17'},
    2022: {13: '17-19', 14: '19-21', 15: '21-23', 16: '23-24', 17: '24-26', 18: '26-28'},
    2023: {13: '18-19', 14: '19-21', 15: '21-23', 16: '23-24', 17: '25-26', 18: '26-27'},
    2024: {13: '18-19', 14: '19-21', 15: '21-23', 16: '23-25', 17: '25-27', 18: '27-29'},
    2025: {12: '8, 37-38', 13: '8-9, 39-40', 14: '9, 41', 15: '9-10, 42-43', 16: '10, 44-45', 17: '10-11, 46-47'},
}


def exam(y, q):
    name = EXAM_FILES.get(y, f'PHY415115-Physics-TASC-Exam-Paper-{y}.pdf')
    section = 'Part 3' if y <= 2021 else 'Section C'
    return Ref(name, f'{y} exam, {section}, Question {q}', EXAM_PAGES[y][q])


def report(y, q):
    name = REPORT_FILES.get(y, f'PHY415115-Physics-Assessment-Report-{y}.pdf')
    return Ref(name, f'{y} assessment report, Criterion 7, Question {q}', REPORT_PAGES[y][q])


REFS = {
    'standards': Ref(COURSE_DOC, 'Course document, Criterion 7 standards (element table)'),
    'content': Ref(COURSE_DOC, 'Course document, Science Understanding: General principles of wave motion (Criterion 7)'),
    'appendix': Ref(COURSE_DOC, 'Course document, Appendix 1: contexts (earthquakes and tsunamis; noise and acoustic design; wave theory of light)'),
    'info': Ref(INFO, 'Information sheet, Oscillations, Waves section', page=2),
    'info_g': Ref(INFO, "Information sheet, Gravity, Kepler's Law section", page=1),
    'spec': Ref(SPEC, 'External assessment specifications, Section C', page=3),
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
    'W1': ('Waves are periodic oscillations that transfer energy', 'content'),
    'W2': ('Transverse and longitudinal waves, by oscillation direction relative to wave velocity', 'content'),
    'W3': ('Qualitative link to simple harmonic motion as the basic oscillation of waves', 'content'),
    'W4': ('Sound is a mechanical, longitudinal wave', 'content'),
    'W5': ('Light is an electromagnetic wave: transverse qualities, travels through a vacuum', 'content'),
    'W6': ('Wavelength, frequency, period, amplitude and velocity: v = λf, f = 1/T', 'content'),
    'W7': ('Reflection and transmission at fixed and free boundaries in 1D', 'content'),
    'W7b': ('Phase change during reflection at fixed ends', 'content'),
    'W8': ('Reflection in two dimensions: angle of incidence equals angle of reflection', 'content'),
    'W9': ("Refraction across a boundary and Snell's law", 'content'),
    'W10': ('Relative refractive index, as a ratio of sines and of speeds', 'content'),
    'W10b': ('Relative refractive index as a ratio of wavelengths', 'content'),
    'W10c': ('Absolute refractive index of light, relative to a vacuum', 'content'),
    'W11': ("Snell's law across a variety of boundaries: internal reflection and critical angle", 'content'),
    'W12': ('Principle of superposition, including 1D pulse diagrams', 'content'),
    'W13': ('Beats from two waves of similar frequency', 'content'),
    'W14': ('Resonance: energy builds up when driven at a natural frequency', 'content'),
    'W14b': ('Energy is transferred efficiently into a system driven at a natural frequency', 'content'),
    'W15': ('Transverse and longitudinal standing waves from superposition of two waves', 'content'),
    'W15b': ('Nodes and antinodes in closed and open pipes and strings', 'content'),
    'W15c': ('Harmonics and overtones', 'content'),
    'W15e': ('Standing wave theory applied to string and wind instruments and other situations', 'content'),
    'W15d': ('Calculating frequencies of strings and pipes', 'content'),
    'W16': ('Stretched wires of known tension and linear density: v = √(T/μ)', 'content'),
    'W17': ('Two-source interference of light and sound at a large distance from the sources', 'content'),
    'W17b': ('Coherence: pinhole sources, or a laser-like source, for clear interference', 'content'),
    'W17c': ('Path difference as the means of quantitative analysis', 'content'),
    'W17d': ('Band width, node to node: w = λx/d', 'content'),
    'W18': ('Diffraction (qualitative): the greater the wavelength, the more diffraction', 'content'),
    'W18b': ('Diffraction around corners or objects: most obvious when the target is comparable to λ', 'content'),
    'W18c': ('Implications for communication, such as microwaves for mobile phones', 'content'),
    'W18d': ('Implications for image resolution in microscopes', 'content'),
    'W18e': ('Single-slit diffraction interference pattern, observationally', 'content'),
    'W19': ('Polarisation of electromagnetic waves (qualitative)', 'content'),
    'W19b': ('Polarisation of mechanical transverse waves', 'content'),
    'W19c': ('Partial polarisation', 'content'),
    'W19d': ('Polarisation by reflection: light from water or glass', 'content'),
    'W19e': ('Polarisation by transmission: through water, glass or a Polaroid filter', 'content'),
    'W19f': ('Polarisation by scattering in air', 'content'),
    'A1': ('Context: monitoring earthquakes and tsunamis', 'appendix'),
    'A2': ('Context: noise pollution and acoustic design', 'appendix'),
    'A3': ('Context: development of the wave theory of light', 'appendix'),
}

# Elements numbered by row order in the standards table (Element 1 = first row).
ELEMENTS = {
    1: ('Identifies, describes and explains general principles of wave motion', 'standards'),
    2: ('Solves numerical problems (straightforward → complex, checking validity)', 'standards'),
    3: ('Interprets and analyses graphical and tabular data', 'standards'),
    4: ('Makes predictions in familiar and unfamiliar (real-world) contexts', 'standards'),
}

# What past Section C questions examined (in our own words).  Never copy question text.
EXAM_TOPICS = {
    'X18-13': ('Sea-wave speeds from a given formula; superposing two waves of different wavelengths', 'ex18q13'),
    'X18-14': ('Violin string: λ, tension from μ, a warmed string going flat and beating', 'ex18q14'),
    'X18-15': ('Optical fibre: speed in glass, travel time, critical angle, entry angle using 90° − θ', 'ex18q15'),
    'X18-16': ('Resonance of a wine glass: standing waves around the rim, overtone, rim wave speed', 'ex18q16'),
    'X18-17': ('Phased-array radar: number of antinodal lines, steering by delaying one source', 'ex18q17'),
    'X18-18': ('Radio range: wavelength and Earth curvature, ionosphere reflection, polarisation on reflection', 'ex18q18'),
    'X19-13': ('Pulses at free and fixed ends, explained with forces', 'ex19q13'),
    'X19-14': ('Open organ pipe: fundamental, length, frequency change with temperature', 'ex19q14'),
    'X19-15': ('Rainbow droplet: refraction, critical angle, reflection, exit angle, dispersion', 'ex19q15'),
    'X19-16': ('Microwave oven: wavelength, standing waves between metal walls, hot spots', 'ex19q16'),
    'X19-17': ('Single slit: monochromatic, coherent, how the pattern forms', 'ex19q17'),
    'X19-18': ('X-ray interference from crystal layers: path difference 2d sin θ', 'ex19q18'),
    'X20-13': ('Sound in ocean layers: Snell with speeds, critical angle, long-range channel', 'ex20q13'),
    'X20-14': ('Mobile phones: wavelengths, antenna standing wave and length, diffraction and coverage', 'ex20q14'),
    'X20-15': ('Wire under tension: f against √T, straightening a graph, finding μ', 'ex20q15'),
    'X20-16': ('Woodwind: open or closed from resonances, fundamental, length', 'ex20q16'),
    'X20-17': ('Circular motion components as models of sound and EM waves; which cannot be polarised', 'ex20q17'),
    'X20-18': ('Calcite polariser: two refractive indices, TIR of one ray, why the output is faint', 'ex20q18'),
    'X21-12': ('Mirage: curved ray, refractive index of air with temperature, Snell reasoning', 'ex21q12'),
    'X21-13': ('Active noise control: cancelling wave, principle of superposition, frequency from a graph', 'ex21q13'),
    'X21-14': ('Pipe open then closed: length, new fundamental, second overtone, no fourth harmonic', 'ex21q14'),
    'X21-15': ('Polarisation by reflection and refraction: dots and arrows, sunglasses, windows, rainbow', 'ex21q15'),
    'X21-16': ('Double slit: purpose of single slit, band width, number of fringes, single-slit envelope', 'ex21q16'),
    'X21-17': ('Apparent depth of a stone in a pond', 'ex21q17'),
    'X22-13': ('Particle motion on a travelling wave: velocity, acceleration; pulse at a light-heavy boundary', 'ex22q13'),
    'X22-14': ('Closed-pipe model of the voice: harmonics sequence, effective length, a different gas', 'ex22q14'),
    'X22-15': ("Deriving Snell's law from a wavefront crossing a boundary", 'ex22q15'),
    'X22-16': ('Gem: critical angle, two internal reflections, partial reflection at a smaller angle', 'ex22q16'),
    'X22-17': ('Two loudspeakers: beats from two generators, coherence conditions, frequency from band width', 'ex22q17'),
    'X22-18': ('Diffraction past a sea wall; visible wavelength; microscope limit and shorter wavelengths', 'ex22q18'),
    'X23-13': ('Standing waves on a piano string: v from f and L, mass from tension, lower tension → lower f, beats', 'ex23q13'),
    'X23-14': ('Polarisation: slit, amplitude component at 45°, third filter between crossed filters', 'ex23q14'),
    'X23-15': ('Sound y–t graph: period, f, λ; particle velocity by tangent; closed tube length:λ and sketch', 'ex23q15'),
    'X23-16': ('Two antennas, distant point source: coherence, λ = c/f, zero-angle maximum, first minimum PD and angle', 'ex23q16'),
    'X23-17': ('Prism: refraction angles at two faces, critical angle, TIR, ray sketch', 'ex23q17'),
    'X23-18': ('Radio reflection from an aircraft: λ, metal vs wood, path-difference expression, fluctuating signal', 'ex23q18'),
    'X24-13': ('Pipes: explain standing-wave formation, end correction, overtones vs harmonics, open vs closed', 'ex24q13'),
    'X24-14': ('Water waves through two gaps: circular wavefronts, λ unchanged, path difference, fringe-formula limits', 'ex24q14'),
    'X24-15': ('Refraction across perpendicular surfaces (90° − θ), TIR test, two successive refractions', 'ex24q15'),
    'X24-16': ('Pulses on strings: reflections, speed with g/m conversion, speed change, transmission at a boundary', 'ex24q16'),
    'X24-17': ('Seismic waves: S-waves and liquids, restoring force, refraction sketch, speed change, curved paths', 'ex24q17'),
    'X24-18': ('Superposition regions, identifying a beat, beat frequency from a graph, two possible frequencies', 'ex24q18'),
    'X25-12': ('Prism dispersion: blue vs red paths, incidence angle from data, critical angle', 'ex25q12'),
    'X25-13': ('Sonometer: fundamental from tension and μ, harmonics, frequencies from beats, tensioning mass', 'ex25q13'),
    'X25-14': ("Young's double slit: coherence, fringe width for two colours, fringe positions, wavelengths in a PD", 'ex25q14'),
    'X25-15': ('Water waves from a graph: amplitude, period, wavelength, speed, direction of travel', 'ex25q15'),
    'X25-16': ('Polarisation by reflection and scattering; polarising sunglasses', 'ex25q16'),
    'X25-17': ('Closed-pipe resonance model of the ear canal; link to hearing sensitivity', 'ex25q17'),
}

# Every number spoken or shown in a worked example, recomputed.  check fails on a mismatch.
CHECKS = [
    ('buoy f', lambda: 1 / 4.0, 0.25, 1e-9),
    ('buoy v', lambda: 0.25 * 18, 4.5, 1e-9),
    ('buoy particle velocity at t=4.5 s', lambda: 0.4 * 2 * math.pi / 4 * math.cos(2 * math.pi * 4.5 / 4), 0.44, 0.02),
    ('string mu', lambda: 0.012 / 1.5, 0.008, 1e-9),
    ('string v', lambda: math.sqrt(80 / 0.008), 100, 1e-9),
    ('glass-water critical angle', lambda: math.degrees(math.asin(1.33 / 1.52)), 61.0, 0.002),
    ('glass-water refraction', lambda: math.degrees(math.asin(1.52 * math.sin(math.radians(55)) / 1.33)), 69.4, 0.002),
    ('glass-air critical angle', lambda: math.degrees(math.asin(1 / 1.5)), 41.8, 0.002),
    ('corner: refraction at top face', lambda: math.degrees(math.asin(math.sin(math.radians(40)) / 1.5)), 25.4, 0.003),
    ('corner: incidence at side face', lambda: 90 - math.degrees(math.asin(math.sin(math.radians(40)) / 1.5)), 64.6, 0.002),
    ('epicentre distance', lambda: 20 / (1 / 4.5 - 1 / 8.0), 206, 0.005),
    ('guitar v', lambda: 196 * 1.30, 255, 0.002),
    ('guitar tension', lambda: 0.0012 * (196 * 1.30) ** 2, 78, 0.005),
    ('guitar new f', lambda: 196 * math.sqrt(1.04), 200, 0.002),
    ('closed pipe f1', lambda: 344 / 0.80, 430, 1e-9),
    ('closed pipe overtone', lambda: 3 * 344 / 0.80, 1290, 1e-9),
    ('open pipe f1', lambda: 344 / 0.40, 860, 1e-9),
    ('ear canal f1', lambda: 344 / 0.10, 3440, 1e-9),
    ('speakers lambda', lambda: 344 / 686, 0.50, 0.005),
    ('speakers PD in wavelengths', lambda: 1.25 / (344 / 686), 2.5, 0.005),
    ('fringe width', lambda: 532e-9 * 2.0 / 0.25e-3, 4.3e-3, 0.015),
    ('three filters amplitude', lambda: math.cos(math.radians(45)) ** 2, 0.50, 1e-9),
    ('ear canal first overtone', lambda: 3 * 344 / 0.10, 10320, 1e-9),
    ('recorders v', lambda: 12 / 2.0, 6.0, 1e-9),
    ('recorders lambda', lambda: 6.0 * 8.0, 48, 1e-9),
    ('fibre v', lambda: 3.00e8 / 1.46, 2.05e8, 0.003),
    ('fibre time', lambda: 4.00e6 / (3.00e8 / 1.46), 19.5e-3, 0.003),
    ('fibre critical angle', lambda: math.degrees(math.asin(1.44 / 1.46)), 80.5, 0.002),
    ('fibre entry angle', lambda: math.degrees(math.asin(1.46 * math.sin(math.radians(90 - math.degrees(math.asin(1.44 / 1.46)))))), 13.9, 0.005),
    ('sound refraction', lambda: math.degrees(math.asin(math.sin(math.radians(40)) * 1510 / 1480)), 41.0, 0.002),
    ('sound critical angle', lambda: math.degrees(math.asin(1480 / 1510)), 78.6, 0.002),
    ('pipe X fundamental', lambda: 400 - 320, 80, 1e-9),
    ('pipe X length', lambda: 344 / (2 * 80), 2.15, 1e-9),
    ('pipe Y fundamental', lambda: (350 - 250) / 2, 50, 1e-9),
    ('pipe Y length', lambda: 344 / (4 * 50), 1.72, 1e-9),
    ('wire f at 20 N', lambda: math.sqrt(20 / 0.002) / 1.2, 83.3, 0.001),
    ('wire f at 40 N', lambda: math.sqrt(40 / 0.002) / 1.2, 117.9, 0.001),
    ('wire f at 80 N', lambda: math.sqrt(80 / 0.002) / 1.2, 166.7, 0.001),
    ('wire gradient', lambda: (166.7 ** 2 - 83.3 ** 2) / 60, 347, 0.003),
    ('wire mu', lambda: 1 / (4 * 0.60 ** 2 * 347), 2.0e-3, 0.002),
    ('antinodal limit', lambda: 0.90 / 0.40, 2.25, 1e-9),
    ('speaker lambda', lambda: 1.1 * 2.0 / 8.0, 0.275, 1e-9),
    ('speaker f', lambda: 344 / 0.275, 1250, 0.001),
    ('phone 900 MHz lambda', lambda: 3.00e8 / 9.00e8, 0.33, 0.02),
    ('phone 28 GHz lambda', lambda: 3.00e8 / 2.8e10, 11e-3, 0.03),
    ('phone 900 MHz lambda, unrounded', lambda: 3.00e8 / 9.00e8, 0.3333, 1e-3),
    ('phone 28 GHz lambda, unrounded', lambda: 3.00e8 / 2.8e10, 0.01071, 1e-3),
    ('buoy particle velocity, unrounded', lambda: 0.4 * 2 * math.pi / 4 * math.cos(2 * math.pi * 4.5 / 4), 0.444, 0.002),
    ('recorders f', lambda: 1 / 8.0, 0.125, 1e-9),
    ('glass-water sin critical', lambda: 1.33 / 1.52, 0.875, 1e-3),
    ('glass-water critical angle, unrounded', lambda: math.degrees(math.asin(1.33 / 1.52)), 61.04, 1e-4),
    ('glass-water sin refraction', lambda: 1.52 * math.sin(math.radians(55)) / 1.33, 0.936, 1e-3),
    ('glass-water refraction, unrounded', lambda: math.degrees(math.asin(1.52 * math.sin(math.radians(55)) / 1.33)), 69.42, 1e-4),
    ('fibre v, unrounded', lambda: 3.00e8 / 1.46, 2.0548e8, 1e-4),
    ('fibre time, unrounded', lambda: 4.00e6 / (3.00e8 / 1.46), 19.467e-3, 1e-4),
    ('fibre critical angle, unrounded', lambda: math.degrees(math.asin(1.44 / 1.46)), 80.51, 1e-4),
    ('fibre angle to axis', lambda: 90 - math.degrees(math.asin(1.44 / 1.46)), 9.49, 1e-3),
    ('fibre entry angle, unrounded', lambda: math.degrees(math.asin(1.46 * math.sin(math.radians(90 - math.degrees(math.asin(1.44 / 1.46)))))), 13.94, 5e-4),
    ('sound refraction, unrounded', lambda: math.degrees(math.asin(math.sin(math.radians(40)) * 1510 / 1480)), 40.98, 1e-4),
    ('sound critical angle, unrounded', lambda: math.degrees(math.asin(1480 / 1510)), 78.56, 1e-4),
    ('epicentre distance, unrounded', lambda: 20 / (1 / 4.5 - 1 / 8.0), 205.7, 1e-4),
    ('beat frequency, 4 beats in 1 s', lambda: 4 / 1.00, 4, 1e-9),
    ('unknown fork, upper', lambda: 440 + 4, 444, 1e-9),
    ('unknown fork, lower', lambda: 440 - 4, 436, 1e-9),
    ('guitar lambda', lambda: 2 * 0.65, 1.30, 1e-9),
    ('guitar v, unrounded', lambda: 196 * 1.30, 254.8, 1e-4),
    ('guitar tension, unrounded', lambda: 0.0012 * 254.8 ** 2, 77.91, 1e-4),
    ('guitar frequency factor', lambda: math.sqrt(1.04), 1.02, 1e-3),
    ('guitar new f, unrounded', lambda: 196 * math.sqrt(1.04), 199.88, 1e-4),
    ('guitar beat', lambda: 196 * math.sqrt(1.04) - 196, 3.88, 1e-3),
    ('closed pipe lambda', lambda: 4 * 0.20, 0.80, 1e-9),
    ('open pipe lambda', lambda: 2 * 0.20, 0.40, 1e-9),
    ('speakers lambda, unrounded', lambda: 344 / 686, 0.5015, 1e-4),
    ('speakers second PD in wavelengths', lambda: 1.50 / (344 / 686), 3.0, 0.005),
    ('wire gradient, unrounded', lambda: (166.7 ** 2 - 83.3 ** 2) / 60, 347.5, 1e-3),
    ('wire mu, unrounded', lambda: 1 / (4 * 0.60 ** 2 * 347.5), 1.998e-3, 1e-3),
    ('fringe width, unrounded', lambda: 532e-9 * 2.0 / 0.25e-3, 4.256e-3, 1e-4),
    ('speaker f, unrounded', lambda: 344 / 0.275, 1250.9, 1e-4),
    ('filter amplitude', lambda: math.cos(math.radians(45)), 0.7071, 1e-3),
]

# --------------------------------------------------------------------------- scenes
S = Step
SCENES = [
Scene('title', P0, 'Welcome', V.title_card, [
    S("Welcome. This video is a complete briefing on Criterion 7 of TASC Physics, PHY415115: identify and apply general "
      "principles of wave motion. Use it to revise for your class tests on waves and for the end of year exam. By the end, "
      "you should know every part of the waves content, which formulas are on your information sheet and where to find "
      "them, and the traps that examiners keep seeing in student answers.", refs=['standards'], anim=4),
]),
Scene('intro', P0, 'How Criterion 7 is assessed', V.overview, [
    S("Criterion 7 is assessed in two ways. Your teacher assesses it during the year, through class tests, practicals and "
      "other tasks. It's also assessed externally, in Section C of the end of year exam. That's about forty five minutes, "
      "forty five marks, and five to seven compulsory questions. In the exam you can use the TASC information sheet and an "
      "approved calculator.", refs=['standards', 'spec']),
    S("The criterion has four elements. We'll number them in the order they appear in the standards table. Element one is "
      "describing and explaining the principles of waves. Element two is solving numerical problems. Element three is "
      "working with data in graphs and tables. And element four is making predictions, including in unfamiliar, real world "
      "contexts. Throughout the video, you'll see a tag in the corner when an example is practising a particular element.",
      refs=['standards'], elements=[1, 2, 3, 4]),
    S("The standards step up from C to A. At C level you identify principles, solve straightforward problems, interpret "
      "data and predict in familiar contexts. At B, you describe principles, solve multi step problems, and analyse data "
      "to get new information. At A, you explain; you solve complex problems and check whether your answer is valid; you "
      "evaluate data and generalise; and you make reasoned predictions in unfamiliar, real world situations. So we'll focus "
      "not just on formulas, but on explaining why.", refs=['standards'], elements=[1, 2, 3, 4]),
    S("Here's the roadmap. Part one: what waves are, and how we describe them. Part two: what happens at boundaries, "
      "meaning reflection, transmission and refraction. Part three: superposition, beats, standing waves and resonance. "
      "Part four: two source interference, diffraction, polarisation, and how we learned that light is a wave. Then we "
      "finish with technique for tests and the exam. Let's get started."),
]),
Scene('transverse', P1, 'What a wave is: transverse waves', V.transverse, [
    S("A wave is a periodic oscillation that transfers energy from one place to another, without transferring matter. "
      "Watch the highlighted particle. It just moves up and down about its rest position. The pattern moves along, but "
      "the particle doesn't travel with it.", refs=['content'], covers=['W1'], elements=[1], anim=2),
    S("This is a transverse wave. The particles oscillate perpendicular to the direction the wave travels. Waves on a "
      "string, ripples on water, and the S waves from an earthquake are all transverse.", refs=['content'],
      covers=['W2'], elements=[1], anim=2),
]),
Scene('longitudinal', P1, 'Longitudinal waves, sound and light', V.longitudinal, [
    S("In a longitudinal wave, the particles oscillate parallel to the direction of travel. That creates compressions, "
      "where particles are bunched together, and rarefactions, where they're spread apart. Sound is a longitudinal wave, "
      "and so are the P waves from earthquakes.", refs=['content'], covers=['W2', 'W4'], elements=[1], anim=2),
    S("Sound is a mechanical wave. It needs a medium, like air, water or rock, because it travels by particles pushing on "
      "their neighbours. That's why there's no sound in space.", refs=['content'], covers=['W4'], elements=[1], anim=2),
    S("Light is different. It's an electromagnetic wave: an electric field and a magnetic field oscillate together, each "
      "perpendicular to the other and to the direction of travel. So light behaves as a transverse wave, and it needs no medium. It crosses the "
      "vacuum of space at the speed of light, three point zero zero times ten to the eight metres per second. That value "
      "is on your information sheet, in the oscillations and waves section.", refs=['content'], covers=['W5'], elements=[1], anim=2),
]),
Scene('shm', P1, 'Simple harmonic motion', V.shm, [
    S("Underneath every wave is simple harmonic motion. Each particle in the medium oscillates like a mass on a spring. If "
      "you follow a point moving steadily around a circle, and watch only its height, you get exactly the same motion. "
      "Plotted against time, it traces out a sine curve. Its up and down shadow behaves like a transverse field, and its "
      "side to side shadow behaves like a particle in a sound wave.", refs=['content', 'ex20q17'], covers=['W3'],
      elements=[1], exam=['X20-17'], anim=4),
    S("The largest displacement from rest is the amplitude, A. One full trip around the circle takes one period, T. This "
      "course treats simple harmonic motion qualitatively, so you don't need an equation for it. You just need the picture, "
      "and the link between the circle and the sine curve.", refs=['content'], covers=['W3'], elements=[1], anim=4),
    S("The key idea is that the restoring force always points back towards the rest position. The further a particle is "
      "displaced, the stronger the pull back. That's what keeps the oscillation going, and it's what lets a medium carry a "
      "wave at all. Keep that idea of a restoring force in mind. We'll need it later, for earthquakes.",
      refs=['content'], covers=['W3'], elements=[1], anim=4),
]),
Scene('quantities', P1, 'Describing a wave: A, λ, T, f, v', V.quantities, [
    S("To describe a wave, we use five quantities. Amplitude, A, is the maximum displacement from the rest position, "
      "measured in metres. Wavelength, lambda, is the distance between two neighbouring points that are in phase, such as "
      "crest to crest. That's also in metres.", refs=['content'], covers=['W6'], elements=[1]),
    S("Period, T, is the time for one complete oscillation, in seconds. Frequency, f, is the number of oscillations each "
      "second, in hertz. Frequency and period are reciprocals: f equals one over T. You'll find that on your information "
      "sheet, in the oscillations and waves section.", refs=['content'], covers=['W6'], elements=[1]),
    S("And wave speed, v, links them all together: v equals lambda f, also on the information sheet. In one period, the "
      "wave moves forward exactly one wavelength. So the speed is wavelength divided by period, which is lambda f.",
      refs=['content'], covers=['W6'], elements=[1], anim=2),
    S("One important fact: the frequency of a wave is set by its source. When a wave moves into a new medium, its speed "
      "and wavelength can change, but its frequency stays the same. Those formulas, from the information sheet, still "
      "apply in each medium.", refs=['content'], covers=['W6'], elements=[1], anim=2),
]),
Scene('graphs', P1, 'Displacement–distance vs displacement–time graphs', V.graphs, [
    S("Questions love wave graphs, and there are two kinds that look almost identical. A displacement distance graph is a "
      "snapshot. It shows the whole wave at one instant. The distance between crests on this graph is the wavelength.",
      covers=['W6'], elements=[3], exam=['X23-15', 'X25-15'], refs=['ex23q15', 'ex25q15']),
    S("A displacement time graph follows one single point over time. The time between crests on this graph is the "
      "period, not the wavelength. Always check the horizontal axis before you read anything off.",
      covers=['W6'], elements=[3], exam=['X23-15', 'X25-15']),
    S("Here's an example for element three. A buoy bobs up and down on the sea. Its displacement time graph shows an "
      "amplitude of zero point four metres, and a period of four seconds. A snapshot of the sea surface shows crests "
      "eighteen metres apart.", covers=['W6'], elements=[3],
      problem="A buoy's displacement-time graph has a period of 4.0 s, and crests on the sea surface are 18 m apart. What are the frequency and the wave speed?"),
    S("So the frequency is one over four, which is zero point two five hertz. And the wave speed is lambda f: zero point "
      "two five times eighteen, which is four point five metres per second. Notice that we needed both graphs: one for the "
      "period, and one for the wavelength.", covers=['W6'], elements=[2, 3]),
    S("You might also be asked for the velocity of the particle itself, at some moment. That's the gradient of the "
      "displacement time graph. Draw a tangent, pick two well separated points on it, and calculate rise over run. Here "
      "it's about zero point four four metres per second. Show the tangent and your points clearly, and include units.",
      covers=['W6'], elements=[3], exam=['X23-15'], refs=['ar23q15'],
      problem='How do you find the velocity of a buoy at t = 4.5 s from its displacement-time graph, if its amplitude is 0.40 m and its period is 4.0 s?'),
]),
Scene('direction', P1, 'Which way is the wave travelling?', V.direction, [
    S("A common question: which way is the wave travelling? A snapshot on its own can't tell you, because a wave moving "
      "left and a wave moving right can look identical at one instant. You need to know how one point is moving next, for "
      "example from its displacement time graph.", covers=['W6'], elements=[3], exam=['X25-15'], refs=['ex25q15']),
    S("Here's a reliable trick. Imagine shifting the snapshot a tiny distance in one direction, say to the right. Then see "
      "where point P must go to sit on the shifted curve. For this snapshot, shifting right would make P move down.",
      covers=['W6'], elements=[3],
      problem='Given a snapshot of a wave and the displacement-time graph of one point, which way is the wave travelling?'),
    S("Now check P's displacement time graph. Just after time zero, P moves down. That matches the right shift, so the "
      "wave is travelling to the right. If P had moved up instead, the wave would be travelling to the left. Always say "
      "which graph features you used, because that's the analysis that element three rewards.",
      covers=['W6'], elements=[3, 4], exam=['X25-15']),
]),
Scene('particles', P1, 'Particle motion on a travelling wave', V.particle_motion, [
    S("Now zoom in on the particles of a travelling wave. Use the same shifting trick to find which way each one moves. "
      "With this wave moving right, Q and S, at the crest and trough, are momentarily at rest. The particles at the rest "
      "position, P, R and U, are moving fastest, some up and some down, depending on the slope.",
      refs=['ex22q13', 'ar22q13'], covers=['W3', 'W6'], elements=[1, 3], exam=['X22-13'],
      problem='On a snapshot of a wave travelling right, which way is each marked particle moving, and which is moving fastest?'),
    S("Acceleration is the opposite. It's greatest at the crest and trough, where the displacement and the restoring force "
      "are largest, and it points towards the rest position. At the rest position it's zero. Examiners see students treat "
      "this as a standing wave. In a travelling wave, every particle reaches full amplitude.",
      refs=['ar22q13'], covers=['W3'], elements=[1, 4], exam=['X22-13'],
      problem='Which particles on a travelling wave have the greatest acceleration, and in which direction?'),
    S("Sometimes you get two graphs, from recorders at different places. Here, B is twelve metres east of A, and B copies A "
      "two seconds later. So the wave travels from A to B, which is east, at twelve over two, or six metres per second. The "
      "period is eight seconds, so the frequency is zero point one two five hertz, and lambda, which is v over f, is forty eight metres. Start from the separation and the lag.",
      refs=['ex25q15', 'ar25q15'], covers=['W6'], elements=[2, 3], exam=['X25-15'],
      problem='Recorder B is 12 m east of recorder A and copies its motion 2.0 s later, with a period of 8.0 s. Which way does the wave travel, and what are its speed and wavelength?'),
]),
Scene('pulses', P2, 'Pulses at fixed and free ends, and between strings', V.pulses, [
    S("Part two. What happens when a wave reaches a boundary? Start with a pulse on a string tied to a wall. This is a "
      "fixed end. When the pulse arrives, the string pulls up on the wall, and the wall pulls down on the string. So the "
      "reflected pulse comes back inverted. We call that a phase change of half a cycle, or one hundred and eighty "
      "degrees.", refs=['content'], covers=['W7', 'W7b'], elements=[1], exam=['X24-16', 'X19-13'], anim=4),
    S("Now a free end. The end of the string is attached to a light ring that slides freely up and down a pole. The end "
      "overshoots, then the tension pulls it back, so the reflected pulse comes back the right way up. There's no phase "
      "change.", refs=['content', 'ar19q13'], covers=['W7'], elements=[1], exam=['X19-13'], anim=4),
    S("Most boundaries are in between. Here, a light string joins a heavier string. Part of the pulse is transmitted, and "
      "part is reflected. Because the heavy string behaves a bit like a fixed end, the reflected pulse is inverted. The "
      "transmitted pulse stays upright, but it travels more slowly, so it's squashed into a shorter length. Both pulses are "
      "smaller than the original, because the energy is shared between them. If you're asked why it's slower, use the wave "
      "speed formula: the tension is the same, but mu is bigger.",
      refs=['content', 'ex24q16', 'ar22q13'], covers=['W7'], elements=[1, 4], exam=['X24-16', 'X22-13'], anim=4),
    S("Going from heavy to light, it's the other way around. The light string acts more like a free end, so the reflected "
      "pulse is upright, and the transmitted pulse moves faster.", covers=['W7'], elements=[1, 4], anim=4),
    S("When you sketch these, in a test or the exam, draw an arrow to show which way each pulse moves. Never draw a "
      "reflected pulse bigger than the original. If the pulse is lopsided, remember that reflection flips it front to back. "
      "And show the slower pulse closer to the boundary, since it has covered less distance in the same time.",
      refs=['ar24q16'], covers=['W7'], elements=[1], exam=['X24-16'], anim=4),
]),
Scene('string_speed', P2, 'Wave speed on a stretched string', V.string_speed, [
    S("The speed of a wave on a stretched string depends on two things: the tension, T, and the linear mass density, mu, "
      "which is the mass per metre of string. The formula, v equals the square root of T over mu, is on your information "
      "sheet, in the oscillations and waves section. Tighter strings carry faster waves. Heavier strings carry slower "
      "waves.", refs=['content'], covers=['W16'], elements=[1]),
    S("Careful. In this information sheet formula, T is the tension in newtons, not the period. And mu must be in kilograms "
      "per metre. Examiners regularly see students forget to convert from grams.", refs=['ar24q16'], covers=['W16'],
      elements=[2], exam=['X24-16']),
    S("Example, for element two. A string is one point five metres long, has a mass of twelve grams, and is under a "
      "tension of eighty newtons. First, convert: twelve grams is zero point zero one two kilograms. So mu is zero point "
      "zero one two divided by one point five, which is zero point zero zero eight kilograms per metre. We're using the "
      "information sheet formula next.", covers=['W16'], elements=[2],
      problem='A string 1.5 m long with a mass of 12 g is under a tension of 80 N. What is the wave speed?'),
    S("v equals the square root of eighty over zero point zero zero eight, from the information sheet. That's the square "
      "root of ten thousand, which is one hundred metres per second.", covers=['W16'], elements=[2]),
    S("In a lab, the tension often comes from a hanging mass, as on a sonometer. The tension equals m g, the weight of the "
      "mass. Your information sheet has that as F g equals m g, in the gravity section, with g equal to nine point eight one metres per second squared. Add more mass, the tension rises, the wave speed rises, and so does the pitch. Working backwards from a "
      "required frequency, you can find the mass needed. Examiners often see the mass itself used as the tension, so "
      "remember to multiply by g. And when the tension changes, so does the wave speed.", covers=['W16'], elements=[2, 4], exam=['X25-13'], refs=['ex25q13', 'ar25q13', 'info_g']),
]),
Scene('huygens', P2, "Wavefronts and Huygens' principle", V.huygens, [
    S("In two dimensions we draw wavefronts: lines joining points that are in phase, such as along each crest. Huygens' "
      "principle says that every point on a wavefront acts as a source of small circular wavelets. The new wavefront is "
      "the line that touches all of those wavelets. Rays show the direction of travel, at right angles to the wavefronts.",
      refs=['content'], elements=[1], exam=['X24-14']),
    S("So when a wave passes through a small gap, or spreads from a point source, the wavefronts become circles centred on "
      "the gap. In the same medium the speed doesn't change, so neither does the wavelength. Draw the circles evenly "
      "spaced, with the same spacing as the incoming waves. That's a mark examiners look for.",
      refs=['ar24q14'], covers=['W18'], elements=[1], exam=['X24-14']),
]),
Scene('refraction', P2, "Reflection, refraction and Snell's law", V.extend(V.refraction, 4, V.huygens_snell), [
    S("We measure every angle from the normal: the line perpendicular to the surface. The law of reflection says that the "
      "angle of incidence equals the angle of reflection. It's on your information sheet, in the oscillations and waves "
      "section, as theta i equals theta r.", refs=['content'], covers=['W8'], elements=[1]),
    S("Refraction is the change in direction when a wave crosses into a medium where it travels at a different speed. The "
      "frequency stays the same, so if the speed drops, the wavelength gets shorter. The part of each wavefront that "
      "crosses first slows down first, so the wavefront swings around. Slowing down bends the ray towards the normal. "
      "Speeding up bends it away.", refs=['content'], covers=['W9'], elements=[1], anim=2),
    S("For light, we describe a medium by its absolute refractive index, n. That's the speed of light in a vacuum, "
      "divided by the speed of light in the medium. That equation isn't on your sheet, so learn it. Glass has n of about "
      "one point five, so light travels at about two thirds of its vacuum speed in glass. A higher n means slower light.", refs=['content'], covers=['W10c', 'W10'],
      elements=[1], anim=2),
    S("Snell's law connects the angles. On your information sheet, in the oscillations and waves section, it's written as "
      "n i sine theta i equals n r sine theta r, where i means the incident medium and r the refracting medium. The sheet "
      "also gives the ratio of the sines, which equals v i over v r, and calls that n: the relative refractive index, going "
      "from the first medium into the second. It also equals n r over n i. And because frequency doesn't change, it equals "
      "the wavelength ratio, lambda i over lambda r. Those last two forms aren't on the sheet.", refs=['content'], covers=['W10b', 'W9', 'W10'], elements=[1], anim=2),
    S("You could be asked to show where the sine ratio comes from. A wavefront AB reaches the boundary. In the same time t, "
      "one end travels v i t in the first medium, and the other end travels v r t in the second. Angle B A Y equals theta i, and angle A Y X equals theta r. Each sine is one of those "
      "distances over the shared side AY. Divide them, and you get the ratio from your information sheet.",
      refs=['ex22q15', 'ar22q15'], covers=['W9', 'W10'], elements=[1], exam=['X22-15']),
]),
Scene('tir', P2, 'Critical angle and total internal reflection', V.extend(V.tir, 4, V.tir_partial), [
    S("When light goes from a slower medium into a faster one, like glass into air, it bends away from the normal. As you "
      "increase the angle of incidence, the refracted ray swings closer and closer to the surface.", covers=['W11'],
      elements=[1], anim=6),
    S("At the critical angle, the refracted ray runs exactly along the surface, at ninety degrees to the normal. Put theta "
      "r equals ninety degrees into Snell's law, and you get: sine of the critical angle equals n r over n i. This one "
      "is not on the sheet, so learn it, or derive it from Snell's law.", covers=['W11'], elements=[1]),
    S("Beyond the critical angle, no light is refracted at all. All of it reflects back into the first medium. That's "
      "total internal reflection. It only happens going from a higher n to a lower n. It's how optical fibres keep light "
      "trapped over long distances.", covers=['W11'], elements=[1]),
    S("Tip: when you explain this, name it. It's not enough to say the angle is bigger than the critical angle. Say that "
      "the angle of incidence exceeds the critical angle, so total internal reflection occurs.", refs=['ar23q17'],
      covers=['W11'], elements=[1], exam=['X23-17']),
    S("Below the critical angle, both things happen. Most light refracts out, and some reflects back. So no total internal "
      "reflection doesn't mean no reflection at all, a mistake examiners keep seeing. Above the critical angle, all the "
      "light reflects, which is why a well cut gem returns a bright ray after two reflections at forty five degrees.",
      refs=['ar25q12', 'ar22q16'], covers=['W11'], elements=[1, 4], exam=['X25-12', 'X22-16']),
]),
Scene('we_refraction', P2, 'Worked example: glass to water', V.we_refraction, [
    S("Let's do a worked example for element two. Light travelling through glass, with n equals one point five two, meets "
      "a boundary with water, n equals one point three three, at an angle of incidence of fifty five degrees. Does it "
      "escape into the water?", covers=['W9', 'W11'], elements=[2],
      problem='Light in glass (n = 1.52) meets water (n = 1.33) at an angle of incidence of 55°. Does it escape, and at what angle?'),
    S("First, find the critical angle. Sine theta c equals one point three three over one point five two, which is zero "
      "point eight seven five. So the critical angle is sixty one point zero degrees.", covers=['W11'], elements=[2]),
    S("Fifty five degrees is below the critical angle, so the light does refract into the water. Snell's law, from the "
      "information sheet, gives sine theta r equals one point five two times sine fifty five degrees, all divided by one "
      "point three three. That's zero point nine three six, so theta r is about sixty nine point four degrees. It bends away "
      "from the normal, as it should, because it's speeding up.", covers=['W9'], elements=[2]),
    S("And if the angle of incidence were increased to sixty five degrees? That's above the critical angle, so there'd be "
      "total internal reflection. Notice how to check validity here, which is what an A rating needs. A refracted angle "
      "bigger than the incident angle makes sense when light speeds up. And if your calculator ever gives a sine bigger "
      "than one, that's Snell's law telling you there's total internal reflection.", covers=['W11'], elements=[2, 4],
      exam=['X24-15']),
]),
Scene('two_surfaces', P2, 'Refraction at two surfaces', V.extend(V.two_surfaces, 3, V.parallel_layers), [
    S("Many questions send light through two surfaces, like a block or a prism. Here, light in air hits the top of a glass "
      "block, n equals one point five zero, at forty degrees. Snell's law gives a refracted angle of twenty five point four "
      "degrees inside the glass.", covers=['W9'], elements=[2], exam=['X24-15', 'X23-17'], refs=['ex24q15', 'ex23q17'],
      problem='Light in air hits the top of a glass block (n = 1.50) at 40°. Does it escape through the side face?'),
    S("The ray now hits the side face. Because the side is at right angles to the top, the normals are at right angles "
      "too, so the new angle of incidence is ninety degrees minus twenty five point four, which is sixty four point six "
      "degrees. Missing this ninety minus theta step is a common way to lose a mark.", refs=['ar24q15'], covers=['W9'],
      elements=[2], exam=['X24-15']),
    S("The critical angle for glass to air is forty one point eight degrees. Sixty four point six is bigger, so there's "
      "total internal reflection at the side face. The method always works: draw the normal at every surface, use the "
      "angle sums in the triangle, then apply Snell's law or the critical angle again.", covers=['W11'], elements=[2],
      exam=['X23-17']),
    S("Here's a useful shortcut for flat, parallel layers, such as light going from air through a thin glass wall into "
      "water. Write Snell's law at each boundary, and the middle layer's term cancels. So n sine theta is the same in "
      "every layer, and the glass doesn't change the final angle. It only shifts the ray sideways a little.",
      refs=['ex24q15', 'ar24q15'], covers=['W9'], elements=[2, 4], exam=['X24-15'],
      problem='Light passes from air through a thin, flat glass wall into water. Does the glass change the final angle?'),
]),
Scene('fibre', P2, 'Worked example: an optical fibre', V.fibre_example, [
    S("An element two example using several of these ideas. A fibre has a core with n equals one point four six, and a "
      "cladding with n equals one point four four. The speed in the core is c over n, about two point zero five times ten "
      "to the eight metres per second. So a signal takes nineteen point five milliseconds to travel four thousand kilometres.",
      refs=['ex18q15'], covers=['W10c', 'W11'], elements=[2], exam=['X18-15'],
      problem='How long does a signal take to travel 4000 km along a fibre with a core of n = 1.46?'),
    S("The critical angle is the inverse sine of one point four four over one point four six, which is eighty point five "
      "degrees. The largest entry angle then uses that ninety minus theta step again. Inside the fibre, the ray makes nine "
      "point five degrees with the axis. Snell's law at the entry face gives thirteen point nine degrees in air.",
      refs=['ar18q15'], covers=['W11'], elements=[2], exam=['X18-15'],
      problem='A fibre has a core of n = 1.46 and a cladding of n = 1.44. What are the critical angle and the entry angle in air that just gives it?'),
]),
Scene('dispersion', P2, 'Dispersion in a prism', V.dispersion, [
    S("One more refraction idea: dispersion. In glass, the refractive index is slightly higher for blue light than for red "
      "light. So when white light enters a prism, blue bends more than red at both surfaces, and the colours spread out into a spectrum. "
      "Each colour also has its own critical angle, so in some situations one colour can escape while another is totally "
      "internally reflected. That's a nice element four prediction to look out for.", covers=['W9', 'W11'],
      elements=[1, 4], exam=['X25-12'], refs=['ex25q12']),
]),
Scene('refraction_contexts', P2, 'Refraction in unfamiliar contexts', V.refraction_contexts, [
    S("Two quick contexts for element four. Light from a stone under water bends away from the normal as it leaves, so the "
      "stone looks closer to the surface than it is. And in a mirage over cold water, air's refractive index falls with "
      "height, so light curves gradually back down to the eye. Draw the normal first, and reason with Snell's law.",
      refs=['ex21q17', 'ex21q12', 'ar21q17', 'ar21q12'], covers=['W9'], elements=[4], exam=['X21-17', 'X21-12']),
    S("In a raindrop, light refracts in, partly reflects at the back, and refracts out. Blue has a higher n than red, so it "
      "separates. Calcite has two refractive indices, one for each polarisation, so the two rays can behave differently: "
      "one may be totally internally reflected while the other passes through. Apply Snell's law to each in turn. The light that gets through is faint, because one ray is lost and more reflects at each surface.",
      refs=['ex19q15', 'ex20q18', 'ar19q15', 'ar20q18'], covers=['W9', 'W11'], elements=[4], exam=['X19-15', 'X20-18']),
]),
Scene('seismic', P2, 'Seismic waves inside the Earth', V.extend(V.seismic, 4, V.sound_snell), [
    S("Refraction isn't just for light. Every wave refracts when its speed changes. Earthquakes send out P waves, which "
      "are longitudinal, and S waves, which are transverse. Inside the Earth's mantle, their speed generally increases "
      "with depth.", refs=['appendix'], covers=['W2', 'W9', 'A1'], elements=[1], exam=['X24-17'], ),
    S("Going deeper, the density and the wave speed both rise gradually, so the wave refracts gradually too. It keeps bending away from the normal, away "
      "from the faster region, so the ray paths curve back up towards the surface.", refs=['ar24q17'],
      covers=['W9', 'A1'], elements=[1, 4], exam=['X24-17']),
    S("S waves can't pass through the Earth's liquid outer core. Why? A transverse wave needs a restoring force to pull "
      "each layer back when it's displaced sideways. A liquid can't resist that sideways shearing. Its layers just slide "
      "past each other. With no restoring force, there's no S wave. This leaves an S wave shadow on the far side of the "
      "Earth, and it's how we know the outer core is liquid. P waves do enter the outer core. They bend towards the normal at that boundary, which shows that they slow down.", refs=['ar24q17'], covers=['A1', 'W3'], elements=[1],
      exam=['X24-17']),
    S("Tip: for sound and seismic waves, reason using wave speed, not refractive index, and don't assume that denser means "
      "slower. Refractive index and optical density are ideas for light.", refs=['ar24q17'], covers=['A1'],
      elements=[1], exam=['X24-17']),
    S("Sound obeys the same law, using the speed form on your information sheet. Suppose sound in water meets a faster "
      "layer at forty degrees. Sine forty over sine theta r equals fourteen eighty over fifteen ten, so theta r is about forty one "
      "degrees. Going from slow to fast also has a critical angle, here seventy eight point six degrees. A slow "
      "layer between faster ones can trap sound, so it travels a very long way.",
      refs=['ex20q13', 'ar20q13'], covers=['W9', 'W10', 'W11'], elements=[2, 4], exam=['X20-13'],
      problem='Sound in water at 1480 m/s meets a layer at 1510 m/s at 40°. What are the angle of refraction and the critical angle?'),
]),
Scene('fast_slow', P2, 'Fast and slow media', V.fast_slow, [
    S("Whenever a wave changes medium, you need to know which side is fast and which is slow. Learn it for each type of wave. Light is fastest in air, slower in water, and slower again in glass. "
      "A higher refractive index means slower light. Sound is the other way around: it's slowest in air, faster in water, and faster again in a solid such as steel.",
      refs=['content', 'ar24q17'], covers=['W9', 'W10c'], elements=[1, 4], exam=['X24-17']),
    S("On strings at the same tension, the heavier string is slower, because mu is bigger. In the Earth's mantle, going deeper, the denser rock carries faster waves. And a tsunami is fast in deep water, and slow in shallow water. "
      "So there's no single rule about density: a heavier string is slower, but deeper rock is faster. Work out which case you're in, then decide which way the wave bends.",
      refs=['ar22q13', 'ar24q17', 'appendix'], covers=['W16', 'W7', 'A1'], elements=[1, 4], exam=['X22-13', 'X24-17']),
]),
Scene('quakes', P2, 'Monitoring earthquakes and tsunamis', V.quakes, [
    S("The course also asks you to apply waves to monitoring earthquakes and tsunamis. P waves are faster, so they reach a "
      "seismometer first, and the S waves arrive later. The further away the earthquake, the bigger that delay. Using "
      "three stations, seismologists can locate the epicentre.", refs=['appendix'], covers=['A1'], elements=[1, 3]),
    S("Here's an element two problem. P waves travel at eight point zero kilometres per second and S waves at four point "
      "five. The S waves arrive twenty seconds after the P waves. The S wave travel time minus the P wave travel time is "
      "twenty seconds, so the distance is twenty divided by one over four point five minus one over eight. That's about two "
      "hundred and six kilometres.", covers=['A1'], elements=[2],
      problem='P waves travel at 8.0 km/s and S waves at 4.5 km/s, and the S waves arrive 20 s later. How far away is the earthquake?'),
    S("Tsunamis are ocean waves with very long wavelengths. In deep ocean they travel fast with a small amplitude. Near the "
      "coast the water gets shallower, so they slow down. The frequency stays the same, so by v equals lambda f the "
      "wavelength shortens, the energy bunches up, and the amplitude grows. That's why a tsunami that's barely noticeable "
      "at sea can be devastating at the shore. Seismographs and computer models use these ideas to predict when a tsunami will arrive, and how much damage it could do.", refs=['appendix'], covers=['A1', 'W6'], elements=[1, 4], anim=2),
]),
Scene('superposition', P3, 'Superposition and pulse diagrams', V.extend(V.superposition, 3, V.super_mixed), [
    S("Part three. When two waves meet in the same place, they don't bounce off each other. They pass straight through. "
      "While they overlap, the total displacement at each point is the sum of the individual displacements. This is the "
      "principle of superposition.", refs=['content'], covers=['W12'], elements=[1], anim=4),
    S("If two crests overlap, they add up. That's constructive interference. If a crest meets an equal trough, they cancel "
      "for an instant. That's destructive interference. Afterwards, each pulse carries on, completely unchanged.",
      refs=['content'], covers=['W12'], elements=[1], exam=['X24-18'], anim=4),
    S("To draw a superposition diagram, add the displacements point by point. Take a few key points, add their heights "
      "with signs, plus above the line and minus below it, then join them with a smooth curve. When you label regions of "
      "constructive and destructive interference, keep the labels clear and don't let them overlap.",
      refs=['ar24q18'], covers=['W12'], elements=[3], exam=['X24-18']),
    S("The waves don't have to match. Add a long wave and a short wave, point by point, and the result keeps both wiggles. "
      "It isn't just a taller copy of one wave. If their speeds differ, and a question may give you a formula for that, the "
      "pattern changes as they move.", refs=['ex18q13', 'ar18q13'], covers=['W12'], elements=[3, 4], exam=['X18-13']),
]),
Scene('beats', P3, 'Beats', V.beats, [
    S("Now let two sound waves with slightly different frequencies overlap. Sometimes they're in step, and add up. "
      "Sometimes they're out of step, and cancel. So the loudness rises and falls regularly. These are beats.",
      refs=['content'], covers=['W13'], elements=[1]),
    S("On a graph, you see a fast wave inside a slowly changing envelope. One beat is one full cycle of loudness, from one "
      "envelope maximum to the next. Be careful not to measure between the peaks of the fast wave. And when you label a beat graph, constructive regions are where the envelope is largest, not simply where the wave is above the axis.", refs=['ar24q18'],
      covers=['W13'], elements=[3], exam=['X24-18']),
    S("The beat frequency is the difference between the two frequencies. f beat equals f one minus f two, taking the "
      "positive value. This is not on the information sheet, so learn it. The pitch you actually hear is the average of the "
      "two.", covers=['W13'], elements=[1]),
    S("Example, for element three. A four hundred and forty hertz tuning fork is sounded together with a note of unknown "
      "frequency. To reduce reading error, measure across several beats. Here, four beats take one second, so the beat "
      "frequency is four hertz. If the time axis is in milliseconds, remember to convert to seconds.", refs=['ar24q18'],
      covers=['W13'], elements=[3], exam=['X24-18'],
      problem='A 440 Hz tuning fork and an unknown note give four beats per second. What is the unknown frequency?'),
    S("So the unknown frequency is either four hundred and forty four, or four hundred and thirty six hertz. One "
      "measurement can't tell you which. Here's how to decide. Stick a little blu tack on the unknown fork, which makes it "
      "vibrate more slowly. If the beats get faster, its frequency has moved further away from four forty, so it must have "
      "started below: four hundred and thirty six hertz. That's the kind of reasoned prediction element four rewards.",
      covers=['W13'], elements=[4], exam=['X24-18', 'X25-13', 'X23-13'],
      problem='How can you tell whether an unknown fork is 436 Hz or 444 Hz, using a 440 Hz fork?'),
]),
Scene('standing', P3, 'Standing waves', V.standing, [
    S("A standing wave forms when two identical waves travel in opposite directions and superpose. Usually, that's a wave "
      "and its own reflection. The pattern doesn't travel. Some points, called nodes, never move at all. Halfway between "
      "them are the antinodes, where the oscillation is biggest.", refs=['content'], covers=['W15', 'W12'],
      elements=[1], anim=2),
    S("Neighbouring nodes are half a wavelength apart, and a node to the next antinode is a quarter of a wavelength. "
      "Between two nodes, every point moves in phase. Across a node, the phase flips.", refs=['content'],
      covers=['W15'], elements=[1], anim=2),
    S("If you're asked to explain how a standing wave forms, use the key words. The wave reflects from the ends. The "
      "incident and reflected waves superpose, with constructive interference at the antinodes and destructive "
      "interference at the nodes. And at certain frequencies, the system resonates. Answers that mention resonance, "
      "reflection and standing waves do best.", refs=['ar24q13'], covers=['W15', 'W14'], elements=[1],
      exam=['X24-13'], anim=2),
]),
Scene('strings', P3, 'Strings: harmonics and overtones', V.strings, [
    S("On a string fixed at both ends, both ends must be nodes. The simplest pattern, called the fundamental or first "
      "harmonic, is a single loop. That's half a wavelength, so lambda equals two L. Not L. That's a very common mistake, "
      "and you can avoid it: the oscillations and waves section of your information sheet has a small diagram of this "
      "pattern, labelled lambda equals two L.", refs=['ar23q13'], covers=['W15b', 'W15', 'W15e'], elements=[1],
      exam=['X23-13'], anim=2),
    S("The next patterns have two, three, and four loops. In general, the n th harmonic has a wavelength of two L over n, "
      "and a frequency of n times v over two L. Those general forms aren't on the sheet, so learn them. The harmonic "
      "frequencies are whole number multiples of the fundamental.",
      covers=['W15c', 'W15d', 'W15'], elements=[1], anim=2),
    S("Watch the words. The first harmonic is the fundamental. The first overtone is the next frequency above the "
      "fundamental, which on a string is the second harmonic. So the second overtone is the third harmonic. Harmonics and "
      "overtones are counted differently, so read the question carefully.", refs=['ar24q13', 'ar25q13'], covers=['W15c'], elements=[1], exam=['X24-13'], anim=2),
]),
Scene('we_string', P3, 'Worked example: a guitar string', V.we_string, [
    S("Worked example, covering elements two and four. A guitar string is sixty five centimetres long, and its fundamental "
      "frequency is one hundred and ninety six hertz. Its linear mass density is one point two grams per metre. Find the "
      "wave speed, and the tension.", covers=['W15', 'W16'], elements=[2], exam=['X23-13', 'X25-13'],
      refs=['ex23q13', 'ex25q13'],
      problem='A guitar string 65 cm long has a fundamental of 196 Hz and a linear density of 1.2 g/m. What are the wave speed and the tension?'),
    S("The fundamental wavelength is two L, which is one point three zero metres. So, using v equals lambda f, v is one "
      "ninety six times one point three zero, which is about two hundred and fifty five metres per second.",
      covers=['W15'], elements=[2]),
    S("Rearranging the string speed formula gives T equals mu v squared. With mu equal to zero point zero zero one two "
      "kilograms per metre, the tension comes out at about seventy eight newtons.", covers=['W16'], elements=[2]),
    S("Now, a prediction. If the tension increases by four percent, how does the pitch change? Frequency is proportional "
      "to wave speed, which is proportional to the square root of tension. So the frequency rises by a factor of root one "
      "point zero four, which is about one point zero two. The new frequency is about two hundred hertz. Played alongside a "
      "one ninety six hertz tuning fork, you'd hear roughly four beats per second. Using a ratio like this is quicker, and "
      "avoids rounding errors. In reverse, a string that warms up and slackens goes flat, so its frequency is the note "
      "minus the beat frequency.", covers=['W16', 'W13'], elements=[4], exam=['X23-13', 'X18-14'], refs=['ar18q14'],
      problem="If that guitar string's tension rises by 4%, what are its new frequency and the beat frequency with a 196 Hz fork?"),
]),
Scene('linearise', P3, 'Straightening a graph to find mu', V.linearise, [
    S("Element three often asks you to generate new data. A wire zero point six metres long is tested at its fundamental, "
      "with tensions of twenty, forty and eighty newtons. The frequencies are eighty three point three, one hundred and "
      "seventeen point nine, and one hundred and sixty six point seven hertz. Plotted directly, that's a curve.",
      covers=['W16'], elements=[3], exam=['X20-15'],
      problem='A 0.60 m wire has fundamental frequencies of 83.3, 117.9 and 166.7 Hz at tensions of 20, 40 and 80 N. What is its linear density?'),
    S("A curve is hard to use, so we straighten it. Combine f equals v over two L with the string speed formula. Squaring "
      "gives f squared equals T, over four L squared mu. So a graph of f squared against T should be a straight line "
      "through the origin. You could also plot f against root T.",
      refs=['ar20q15'], covers=['W16', 'W15d'], elements=[3], exam=['X20-15']),
    S("The gradient is about three hundred and forty seven hertz squared per newton. It equals one over four L squared mu. "
      "So mu is two point zero times ten to the minus three kilograms per metre. Use the gradient of your line, not a single "
      "point, because that averages out the measurement errors. That's the generalising that an A rating looks for.",
      covers=['W16'], elements=[2, 3], exam=['X20-15']),
]),
Scene('pipes', P3, 'Pipes: open, closed and end correction', V.extend(V.pipes, 6, V.pipe_id, V.pipe_id), [
    S("Air in pipes forms standing waves too. Here we draw the displacement of the air. At a closed end, the air can't "
      "move, so there's a displacement node. At an open end, the air moves most freely, so there's a displacement antinode.",
      refs=['content'], covers=['W15b', 'W15', 'W15e'], elements=[1]),
    S("In a pipe open at both ends, there are antinodes at both ends. The fundamental is half a wavelength, so lambda "
      "equals two L, as the diagram in the oscillations and waves section of your information sheet shows. Just like a "
      "string, all harmonics are possible.", covers=['W15'], elements=[1], exam=['X24-13']),
    S("In a pipe closed at one end, there's a node at the closed end, and an antinode at the open end. The fundamental is "
      "just a quarter of a wavelength, so lambda equals four L, also on the information sheet. And only odd harmonics are possible: the first, third, "
      "fifth, and so on. So the first overtone of a closed pipe is the third harmonic. If you're given the length and the wavelength, divide them first. A ratio of three quarters means the third harmonic, not the fundamental.", refs=['ar23q15'],
      covers=['W15'], elements=[1], exam=['X23-15', 'X24-13']),
    S("In reality, the antinode sits slightly outside each open end. This is the end correction: the pipe behaves as if "
      "it's a little longer than it really is. Apply it at every open end: once for a closed pipe, and twice for an open "
      "pipe. And when you sketch, put the antinodes just outside the opening, not inside the pipe.", refs=['ar24q13'],
      covers=['W15'], elements=[1], exam=['X24-13']),
    S("Example, for element two. A pipe twenty centimetres long is closed at one end. Ignoring end correction, lambda one "
      "is four L, which is zero point eight metres. The speed of sound in air, three hundred and forty four metres per "
      "second, is in the oscillations and waves section of your information sheet. So f one is three forty four over zero point eight, which is four hundred and "
      "thirty hertz. The first overtone is the third harmonic, at twelve hundred and ninety hertz. If we open up the closed "
      "end, the fundamental doubles, to eight hundred and sixty hertz.", covers=['W15d', 'W15'], elements=[2],
      problem='A pipe 20 cm long is closed at one end. What are its fundamental and first overtone, and its fundamental if opened?'),
    S("A real world prediction. Your ear canal is roughly a pipe about two and a half centimetres long, closed at the "
      "eardrum. Its fundamental is about three hundred and forty four over zero point one, or roughly three thousand four "
      "hundred hertz. Resonance boosts sounds near that frequency, which is why our ears are especially sensitive around "
      "three to four kilohertz. The first overtone, the third harmonic, is near ten kilohertz, which gives a second "
      "sensitive range. Mention both for a full answer. A shorter canal, like a child's, resonates at a higher frequency.",
      covers=['W15', 'W14'], elements=[4], exam=['X25-17'], refs=['ex25q17', 'ar25q17'],
      problem='Modelling a 2.5 cm ear canal as a closed pipe, which frequencies should the ear be most sensitive to?'),
    S("For element three, you may have to work out the pipe type from its resonances. Find the spacing between them. Pipe X "
      "resonates at two forty, three twenty and four hundred hertz. The spacing is eighty, so f one is eighty hertz, and "
      "these are harmonics three, four and five. An even harmonic means it's open, so its length is two point one five metres.",
      refs=['ar20q16'], covers=['W15', 'W15d'], elements=[3], exam=['X20-16', 'X21-14'],
      problem='A pipe resonates at 240, 320 and 400 Hz. Is it open or closed, and how long is it?'),
    S("Pipe Y resonates at one fifty, two fifty and three fifty hertz. The spacing is one hundred hertz, which is twice f "
      "one, so f one is fifty hertz. These are harmonics three, five and seven, so it's closed, and its length is one point "
      "seven two metres. To justify this, refer to the ends: a node at the closed end and an antinode at the open end let "
      "only odd numbers of quarter wavelengths fit. Just saying odd harmonics only earns part marks.",
      refs=['ar21q14'], covers=['W15b'], elements=[1, 3], exam=['X21-14', 'X20-16'],
      problem='A pipe resonates at 150, 250 and 350 Hz. Is it open or closed, and how long is it?'),
]),
Scene('standing_contexts', P3, 'Standing waves in unfamiliar contexts', V.standing_contexts, [
    S("The same rules apply elsewhere. Around a wine glass rim, a whole number of wavelengths must fit the circumference. In "
      "a microwave oven, metal walls are nodes, and nodes half a wavelength apart leave cold spots, so a turntable moves the "
      "food. A phone antenna holds a quarter wave, with a node at the tip, so its length is lambda over four.",
      refs=['ex18q16', 'ex19q16', 'ex20q14', 'ar18q16', 'ar20q14'], covers=['W15', 'W14', 'W15e'], elements=[4],
      exam=['X18-16', 'X19-16', 'X20-14']),
    S("And for a pipe, the length fixes the wavelength. So if the wave speed changes, the frequency changes in proportion. "
      "A warmer room raises the pitch of an organ. A lungful of helium, where sound travels much faster, raises the pitch of "
      "a voice. Use any speed the question gives you, not the information sheet value.",
      refs=['ex19q14', 'ex22q14', 'ar22q14'], covers=['W15d'], elements=[4], exam=['X19-14', 'X22-14']),
]),
Scene('resonance', P3, 'Resonance', V.resonance, [
    S("Every object has natural frequencies at which it tends to oscillate. When a periodic driving force matches one of "
      "those natural frequencies, energy is transferred in efficiently, so it builds up and the amplitude grows very large. That's resonance. It's why a singer "
      "can make a wine glass ring, why a guitar body amplifies its strings, and why engineers worry about bridges and "
      "buildings in wind and earthquakes. Damping and flexible suspension help protect them.", refs=['content', 'appendix'],
      covers=['W14', 'W14b'], elements=[1]),
    S("For strings and pipes, the natural frequencies are exactly the standing wave frequencies we just found. So "
      "resonance and standing waves go together: a standing wave builds up strongly when the driving frequency matches one "
      "of the harmonics.", covers=['W14', 'W15'], elements=[1]),
]),
Scene('noise', P3, 'Noise pollution and acoustic design', V.noise, [
    S("Waves also help us control noise, another context named in the course. Noise cancelling headphones use a "
      "microphone to sample the incoming noise, then play an inverted copy. The two superpose destructively, so the noise "
      "is largely cancelled. It works best for steady, low frequency sounds like engine hum. If you're asked which "
      "principle this uses, name superposition, not just interference. And read the noise graph carefully: find one full "
      "period, and convert milliseconds to seconds before you calculate the frequency.", refs=['appendix', 'ar21q13'],
      covers=['A2', 'W12'], elements=[1, 3, 4], exam=['X21-13']),
    S("Acoustic design uses every idea in this criterion. Soft, porous materials absorb sound and reduce reflections and "
      "echo. Heavy barriers reflect sound, but low frequencies, with long wavelengths, diffract over and around walls, "
      "which is why you still hear the bass of traffic. Engineers avoid resonance by mounting machines on soft supports, "
      "and they shape rooms so that reflections send sound where it's wanted. Road designers also use noise barriers, quieter surfaces and lower speeds, and ear protection is compulsory in noisy industrial work.", refs=['appendix'],
      covers=['A2', 'W14', 'W18'], elements=[1, 4]),
]),
Scene('two_source', P4, 'Two-source interference and path difference', V.two_source, [
    S("Part four. When two sources send out waves that overlap, they create an interference pattern. Here, two dippers "
      "make ripples in a tank. Along some lines the water moves strongly. Along others, it's almost still.",
      refs=['content'], covers=['W17'], elements=[1], anim=1),
    S("You only get a stable pattern if the sources are coherent. Coherent sources have the same frequency, and a "
      "constant phase relationship. Two separate light bulbs aren't coherent, so for light we usually split one source into "
      "two, for example by using two narrow slits. Similarly, waves from a single distant point source arrive at two "
      "receivers with a fixed phase relationship, so they can interfere.", refs=['content', 'ar23q16'],
      covers=['W17b', 'W17'], elements=[1], exam=['X23-16', 'X25-14'], anim=1),
    S("What decides loud or quiet is the path difference: how much further the wave from one source travels than the wave "
      "from the other. To find it, simply subtract one path length from the other. You don't need Pythagoras or "
      "trigonometry, unless you're asked for an angle.", refs=['ar24q14'], covers=['W17c', 'W17'], elements=[1],
      exam=['X24-14']),
    S("If the path difference is a whole number of wavelengths, n lambda, the waves arrive in phase. That's constructive "
      "interference, a maximum. If the path difference is a whole number minus a half, times lambda, the waves arrive "
      "completely out of phase. That's destructive interference, a minimum. These conditions aren't on the sheet, so learn them. Equal paths, at zero angle, always give a "
      "maximum for in-phase sources. For a distant source, the path difference is d sine theta, so the first minimum is where that equals half a wavelength.", covers=['W17'], elements=[1], exam=['X23-16', 'X24-14']),
    S("Example, for element two. Two speakers are driven in phase at six hundred and eighty six hertz. The wavelength is "
      "three forty four over six eight six, which is about zero point five zero metres. You stand five metres from speaker "
      "A, and six point two five metres from speaker B. The path difference is one point two five metres, which is two and "
      "a half wavelengths. So you're at a quiet spot. Step to where the path difference is one point five metres, three "
      "whole wavelengths, and it's loud again.", covers=['W17'], elements=[2],
      problem='Two speakers in phase at 686 Hz are 5.00 m and 6.25 m from you. Is your position loud or quiet?'),
]),
Scene('coherence', P4, 'Getting coherent sources', V.extend(V.coherence, 1, V.coherent_phase), [
    S("How do we get coherent light? Light from an ordinary lamp first goes through a narrow slit or pinhole, which acts as "
      "a single source. It diffracts, so one wavefront reaches both slits. A laser does the same job, because its light is "
      "already coherent. The single slit doesn't select a colour. Monochromatic means one wavelength. And coherent sources "
      "have a constant phase relationship, which doesn't have to mean in phase.",
      refs=['content', 'ar21q16', 'ar19q17', 'ar25q14'], covers=['W17b'], elements=[1], exam=['X21-16', 'X19-17', 'X25-14']),
    S("Coherent and in phase are different ideas, and examiners want you to keep them apart. In phase means there's no phase difference. Coherent means the same frequency, and a phase difference that stays constant. "
      "In a two source pattern, the phase difference between the arriving waves is constant at each point, but it depends on where you are. At the loud spots they're in phase, and at the quiet spots they're out of phase. "
      "So if you're asked for the conditions for interference, write: the same frequency, and a constant phase relationship.",
      refs=['ar25q14', 'ar22q17', 'ar23q16'], covers=['W17b', 'W17'], elements=[1], exam=['X25-14', 'X22-17', 'X23-16']),
]),
Scene('antinodal', P4, 'Counting antinodal lines and steering a beam', V.antinodal_lines, [
    S("How many antinodal lines are there? The largest possible path difference is the source separation, d. So with d equal "
      "to zero point nine metres and lambda equal to zero point four metres, n can be at most two point two five. That means "
      "n is zero, plus or minus one, or plus or minus two: five antinodal lines. Draw a sketch to check.",
      refs=['ar18q17'], covers=['W17', 'W17c'], elements=[2], exam=['X18-17'],
      problem='Two in-phase sources are 0.90 m apart with a wavelength of 0.40 m. How many antinodal lines are there?'),
    S("Radar can steer its beam this way. Delay one source, and the waves are equal in phase away from the centre line. If "
      "one wave has a head start of some distance, sine theta equals that distance over d. Adding more sources makes the "
      "beam narrower and stronger.", refs=['ex18q17'], covers=['W17c'], elements=[4], exam=['X18-17']),
]),
Scene('radar', P4, 'Two paths: radio waves and aircraft', V.extend(V.radar, 3, V.bragg), [
    S("The same reasoning works whenever a wave reaches a receiver by two paths. Radio waves are electromagnetic, and "
      "metal reflects them strongly, because its free electrons re-radiate the wave. Wood and plastic mostly let radio "
      "waves through. So a metal aircraft gives a strong reflected signal.", covers=['W17', 'W5'], elements=[1],
      exam=['X23-18'], refs=['ex23q18']),
    S("A receiver picks up the direct wave and the wave reflected from the aircraft. The path difference is the path via "
      "the aircraft minus the direct path. And for the wavelength, use lambda equals c over f, with three times ten to the "
      "eight metres per second, not the speed of sound. Examiners regularly see the speed of sound used for radio waves.",
      refs=['ar23q18', 'ar23q16'], covers=['W17'], elements=[2], exam=['X23-18', 'X23-16']),
    S("As the aircraft moves, the path difference keeps changing. When it's a whole number of wavelengths, the signal is "
      "strong. When it's a half number, the signal is weak. So the received signal rises and falls as the plane flies "
      "over: a prediction you can explain using interference.", refs=['ar23q18'], covers=['W17'], elements=[4],
      exam=['X23-18'], anim=4),
    S("X rays reflecting from layers of atoms in a crystal are another two path case. The ray from the lower layer travels "
      "two extra lengths of d sine theta, where d is the layer spacing and theta is measured from the layer. When that path "
      "difference equals a whole number of wavelengths, you see a bright spot.",
      refs=['ex19q18', 'ar19q18'], covers=['W17c'], elements=[1, 4], exam=['X19-18']),
]),
Scene('youngs', P4, "Young's double slit and fringe width", V.extend(V.youngs, 5, V.youngs_derive_a, V.youngs_derive_b, V.youngs_derive_c, V.youngs_sound), [
    S("Young's double slit experiment shows light interfering. Light passes through two narrow slits, a distance d apart, "
      "onto a screen a distance x away. You see evenly spaced bright and dark fringes.", refs=['content', 'ex25q14'],
      covers=['W17'], elements=[1], exam=['X25-14']),
    S("The band width, w, is the distance from one node to the next. You may also hear it called the fringe width. It "
      "equals lambda x over d. That's the form on your information sheet, in the oscillations and waves section, so use "
      "its letters: x is the distance to the screen, and d is the slit separation. A bigger wavelength, a more distant "
      "screen, or slits closer together all give wider fringes. This experiment was crucial "
      "evidence that light is a wave.", covers=['W17d', 'W17'], elements=[1]),
    S("Example, for element two. A green laser, with a wavelength of five hundred and thirty two nanometres, shines on two "
      "slits zero point two five millimetres apart, with a screen two metres away. Using the information sheet formula, w "
      "equals five hundred and thirty two times ten to the minus nine, times two, divided by zero point two five times ten "
      "to the minus three. That's about four point three millimetres. Switch to a red laser, with its longer wavelength, "
      "and the fringes spread further apart.", covers=['W17'], elements=[2], exam=['X25-14'],
      problem='Light of wavelength 532 nm passes through slits 0.25 mm apart onto a screen 2.0 m away. What is the band width?'),
    S("Where are the fringes? The central bright fringe has zero path difference. The n th bright fringe is n band "
      "widths from the centre, where the path difference is n wavelengths. The dark fringes sit halfway between, where the "
      "path difference is a whole number minus a half, times lambda.", covers=['W17'], elements=[1, 3],
      exam=['X25-14']),
    S("Is the answer valid? The formula relies on a small angle approximation. It only works when the distance to the "
      "screen is much bigger than the band width and the slit separation. Here, it's a few millimetres compared with two "
      "metres, so it's fine. If you're asked about the limitations of this formula, that's the answer, and vague "
      "references to other factors don't earn marks.", refs=['ar24q14'], covers=['W17'], elements=[2],
      exam=['X24-14']),
    S("Where does the formula come from? Take a point on the screen far away, so the two rays from the slits are almost parallel. "
      "The extra distance the lower ray travels is the path difference. In the right angled triangle, the hypotenuse is the slit "
      "separation d, so the path difference equals d sine theta. This one isn't on the information sheet, so learn it.",
      refs=['content', 'ar23q16', 'ar24q14', 'ar21q16'], covers=['W17', 'W17c', 'W17d'], elements=[1], exam=['X23-16', 'X24-14', 'X21-16']),
    S("A bright fringe needs a path difference of n lambda, so d sine theta equals n lambda. For a small angle, sine theta is "
      "nearly the same as tan theta, which is y over x, where y is how far the fringe is from the centre. So d y over x equals "
      "n lambda, and y equals n lambda x over d.", refs=['ar24q14', 'ar23q16'], covers=['W17', 'W17d'], elements=[1], exam=['X24-14', 'X23-16']),
    S("Neighbouring fringes have n values one apart, so they are one lambda x over d apart. That is the band width. The same working "
      "shows the limits: the angle must be small, and the screen must be much further away than the slit separation. "
      "Tip: if you are asked why the formula is limited, or to explain where it comes from, use this reasoning. The course only gives you "
      "the result, but the reports credit students who show they understand it.", refs=['ar24q14', 'ar21q16'], covers=['W17', 'W17d'], elements=[1, 4], exam=['X24-14', 'X21-16']),
    S("The band width formula works for sound too. Two speakers two metres apart are driven by one signal generator. Eight "
      "metres away, loud spots are one point one metres apart. So lambda is w d over x, which is zero point two seven five "
      "metres, and the frequency is about twelve hundred and fifty hertz. Speakers moved closer give a bigger band width. "
      "A shorter wavelength gives narrower bands, so more of them fit on a screen. With two separate generators, you'd likely hear beats instead of a steady pattern.",
      refs=['ex22q17', 'ar22q17', 'ar24q14', 'ar21q16'], covers=['W17', 'W17d'], elements=[2, 4], exam=['X22-17', 'X21-16'],
      problem='Speakers 2.0 m apart give loud spots 1.1 m apart at a distance of 8.0 m. What is the frequency of the sound?'),
]),
Scene('diffraction', P4, 'Diffraction', V.diffraction, [
    S("Diffraction is the spreading of a wave as it passes through a gap, or around an obstacle. In this course, it's "
      "treated qualitatively. The spreading is most noticeable when the gap is similar in size to the wavelength. With a "
      "wide gap, the wave goes mostly straight through. With a narrow gap, it spreads out in curved wavefronts.",
      refs=['content'], covers=['W18b', 'W18'], elements=[1], anim=1),
    S("So longer wavelengths diffract more. That's why you can hear someone around a corner, but not see them. Sound "
      "wavelengths are around a metre, while light wavelengths are less than a millionth of a metre. It's also why long "
      "wave radio bends around hills when shorter wavelengths can't. Note that the wavelength doesn't change as the wave "
      "diffracts, so keep the spacing between wavefronts the same in your sketches.", refs=['content'],
      covers=['W18'], elements=[1, 4], exam=['X24-14'], anim=1),
]),
Scene('single_slit', P4, 'Single-slit diffraction', V.single_slit, [
    S("A single slit lit by coherent light also makes a pattern: a wide, bright central band, with fainter bands either side. "
      "Light from different parts of the slit has path differences, so it interferes. You only need to treat this "
      "observationally. A narrower slit or a longer wavelength spreads the pattern further.",
      refs=['content', 'ex19q17', 'ar19q17'], covers=['W18e'], elements=[1], exam=['X19-17']),
    S("Real double slits have width too, so each one diffracts. The double slit fringes sit inside the single slit pattern, "
      "which is why they can fade, vanish and then faintly return further out. If you're asked what that extra effect is, "
      "name single slit diffraction.", refs=['ar21q16'], covers=['W18e'], elements=[1, 4], exam=['X21-16']),
]),
Scene('diffraction_uses', P4, 'Diffraction: walls, phones and microscopes', V.diffraction_uses, [
    S("When waves pass the end of a wall, they bend into the region behind it, keeping the same wavelength. But some of that "
      "region stays calm. Show that shadow area in your sketch, because students often leave it out.",
      refs=['content', 'ar22q18'], covers=['W18b'], elements=[1], exam=['X22-18']),
    S("Diffraction matters for communication. A phone signal at nine hundred megahertz has a wavelength of about a third of a "
      "metre, so it bends around buildings. At twenty eight gigahertz, the wavelength is about eleven millimetres, so there's "
      "little diffraction, and shadows form behind buildings. That means many small transmitters. Very long radio waves bend "
      "around the Earth's curve, and the ionosphere can reflect them too.",
      refs=['content', 'ar20q14', 'ex18q18', 'ar18q18'], covers=['W18c'], elements=[1, 4], exam=['X20-14', 'X18-18'],
      problem='What are the wavelengths of 900 MHz and 28 GHz phone signals, and how do they affect coverage?'),
    S("It also limits microscopes. The E M spectrum on your "
      "information sheet shows that visible light runs from about four hundred to seven hundred nanometres. A one hundred "
      "nanometre virus is much smaller than that, so light diffracts around it and no clear image forms. Say that, because just "
      "saying the wavelength is bigger earns few marks. A shorter wavelength diffracts less around it, such as X rays or an electron beam.",
      refs=['content', 'info', 'ex22q18', 'ar22q18'], covers=['W18d'], elements=[1, 4], exam=['X22-18'],
      problem="Why can't a visible-light microscope resolve a 100 nm virus?"),
]),
Scene('polar_string', P4, 'Polarisation with a string', V.polar_string, [
    S("Polarisation starts with mechanical waves. Shake a string in all directions and pass it through a vertical slit. Only "
      "the vertical oscillation gets through, so the wave beyond the slit is polarised. A sound wave has only one "
      "oscillation direction, along its travel, so it can't be polarised.",
      refs=['content', 'ex23q14'], covers=['W19b', 'W2'], elements=[1], exam=['X23-14', 'X20-17'], anim=2),
]),
Scene('polarisation', P4, 'Polarisation', V.polarisation, [
    S("Polarisation is the strongest evidence that light is a transverse wave. In unpolarised light, the electric field "
      "oscillates in all directions perpendicular to the direction of travel. A polarising filter only lets through the "
      "component along its transmission axis. What comes out is plane polarised, oscillating in just one direction.",
      refs=['content'], covers=['W19'], elements=[1], exam=['X23-14']),
    S("Longitudinal waves can't be polarised, because they only oscillate along the direction of travel. There's no "
      "sideways direction to filter out. So polarisation tells transverse waves apart from longitudinal ones.",
      refs=['content'], covers=['W19', 'W2'], elements=[1], exam=['X20-17']),
    S("If polarised light meets a second filter at an angle theta, resolve the amplitude like a vector. The component "
      "along the new axis is A cos theta, and that's what gets through. Strictly, the course only asks for polarisation qualitatively, and this isn't on the sheet, but the 2023 exam asked for it, so learn it. Use "
      "cosine, not sine, when theta is measured from the polarisation direction.", refs=['ar23q14'], covers=['W19'], elements=[1, 2], exam=['X23-14']),
    S("Two filters at ninety degrees to each other, called crossed filters, block everything, since cos ninety is zero. "
      "But put a third filter between them at forty five degrees, and some light gets through. The middle filter passes A "
      "cos forty five, about zero point seven one A, now polarised at forty five degrees. The last filter is forty five "
      "degrees from that, so it passes zero point seven one of that again. That's half the original amplitude.", refs=['ar23q14'], covers=['W19'], elements=[2, 4], exam=['X23-14'],
      problem='Three polarising filters are set at 0°, 45° and 90°. What fraction of the amplitude gets through?'),
    S("Light reflected off water or a road is partly polarised, mostly horizontally. Polarising sunglasses have vertical "
      "transmission axes, so they block much of that glare. Tilt your head ninety degrees, and the glare comes back.",
      covers=['W19c', 'W19d', 'W19'], elements=[4], exam=['X25-16'], refs=['ex25q16']),
    S("Light scattered by air molecules is polarised too. Sunlight scattered at ninety degrees is mostly plane polarised, "
      "so if you look at that part of the sky through a polarising filter and rotate it, the sky brightens and darkens. "
      "Reflection, scattering and filters all point the same way: light is a transverse wave.", covers=['W19f', 'W19', 'W5'],
      elements=[1, 4], exam=['X25-16']),
]),
Scene('polar_partial', P4, 'Partial polarisation', V.polar_partial, [
    S("Diagrams show polarisation with dots and arrows. Dots are the field out of the page, and arrows are the field in the "
      "page. Unpolarised light has equal amounts. When it hits water or glass, the reflected ray has mostly dots, and the "
      "transmitted ray has mostly arrows. Both remain, so we call this partial polarisation. Polarising sunglasses cut that surface glare, which helps someone see fish under the water. Rainbow light is polarised too, because it has reflected and refracted at the surfaces of the droplet.",
      refs=['content', 'ar21q15', 'ar18q18'], covers=['W19c', 'W19d', 'W19e'], elements=[1, 3], exam=['X21-15', 'X18-18', 'X25-16']),
    S("Reflected light is polarised parallel to the surface that reflected it. Water is horizontal, so vertical axis "
      "sunglasses block the glare. A shop window is vertical, so its reflection is vertically polarised, and the sunglasses "
      "let it through. For full marks, state each step: the water's reflection is horizontal, the lenses block horizontal, the window's reflection is vertical, so it gets through.",
      refs=['ar25q16', 'ar21q15'], covers=['W19d', 'W19e'], elements=[4], exam=['X25-16', 'X21-15'],
      problem='Do polarising sunglasses reduce reflections from water and from a shop window?'),
    S("Now look at light scattered through ninety degrees, through a rotating polarising filter. Lined up with the scattered "
      "light's polarisation, it's brightest. Rotate ninety degrees, and it's darkest. Rotate a hundred and eighty degrees, "
      "and it's back to the start. Say which way the scattered light is polarised, then describe what happens along the way, not just at the end.",
      refs=['ar25q16'], covers=['W19f'], elements=[4], exam=['X25-16']),
]),
Scene('light_history', P4, 'How we learned light is a wave', V.light_history, [
    S("The course also asks you to understand how the wave theory of light developed. Newton favoured a particle model, "
      "which explained reflection and straight line travel. Robert Hooke and Christiaan Huygens proposed waves and wavelets, which explained "
      "refraction, but only if light travels more slowly in glass.", refs=['appendix'], covers=['A3'], elements=[1]),
    S("In eighteen oh one, Young's double slit experiment showed interference fringes, which particles couldn't explain. Young also developed the ideas of coherence and superposition of light. "
      "Polarisation then showed that light must be a transverse wave. A medium called the aether was proposed to carry it, "
      "but experiments such as Michelson and Morley's later ruled that out.", refs=['appendix'], covers=['A3', 'W17', 'W19'],
      elements=[1]),
    S("In the eighteen sixties, Maxwell predicted electromagnetic waves travelling at about three times ten to the eight "
      "metres per second, matching the measured speed of light. So light is an electromagnetic wave. Each step used a wave "
      "property from this criterion. In Criterion 8, you'll see that light also shows particle behaviour.",
      refs=['appendix'], covers=['A3', 'W5'], elements=[1]),
]),
Scene('exam_tips', P5, 'Tips for tests and the exam', V.exam_tips, [
    S("Finally, technique for your tests and the exam. These points come from what examiners have reported in recent "
      "years. One: radio, light and radar are electromagnetic waves, so use three times ten to the eight metres per second. "
      "The speed of sound, three hundred and forty four metres per second, is for sound only.",
      refs=['ar23q16', 'ar23q18']),
    S("Two: convert your units. Milliseconds to seconds, grams to kilograms, and centimetres, millimetres and nanometres to "
      "metres. Three: for a string fixed at both ends, the fundamental wavelength is two L, not L. For a pipe closed at one "
      "end, it's four L.", refs=['ar24q16', 'ar24q18', 'ar23q13']),
    S("Four: draw smooth sine shapes, not zig zags. Label nodes, antinodes, angles and rays, and add arrows for direction. "
      "Five: harmonics and overtones are counted differently. Six: find a path difference by simple subtraction.",
      refs=['ar24q13', 'ar24q14', 'ar23q17']),
    S("Seven: answer the question that's asked. Describe means say what happens. Explain means say why it happens, using "
      "physics ideas like restoring force, superposition, or a change in speed. And eight: use your earlier answers. If you "
      "get part a wrong, keep going. Markers usually carry the error forward, and still give you method marks. So show your working, and keep extra digits until the end, because rounding too early causes errors.",
      refs=['ar24q16', 'ar23q15', 'ar25q13']),

]),
Scene('more_tips', P5, 'More examiner tips', V.more_tips, [
    S("Here are more common errors. Nine: no total internal reflection doesn't mean no reflection. Ten: justify a closed "
      "pipe using the node and antinode at its ends. Eleven: a hanging mass gives a tension of m g. Twelve: the second "
      "overtone of a string is the third harmonic.", refs=['ar25q12', 'ar21q14', 'ar25q13']),
    S("Thirteen: name the principle of superposition. Fourteen: a single slit doesn't select a colour, and coherent doesn't "
      "mean in phase. Fifteen: draw the normal at every boundary. Sixteen: in a diffraction sketch, keep the wavelength the "
      "same and show the shadow area.", refs=['ar21q13', 'ar21q16', 'ar25q14', 'ar25q12', 'ar22q18']),
]),
Scene('summary', P5, 'Summary', V.summary, [
    S("That's every part of Criterion 7. Waves transfer energy. They're described by amplitude, wavelength, period, "
      "frequency and speed. They reflect, refract and superpose. They form beats and standing waves, they interfere and "
      "diffract, and if they're transverse, they can be polarised. Practise explaining each idea in words, as well as with "
      "numbers, and you'll be ready for your tests and for Section C. Good luck."),
]),
]

# Report references that no slide cites are left out of the reference list.
_used = {r for sc in SCENES for st in sc.steps for r in st.refs} | {t[1] for t in EXAM_TOPICS.values()} \
    | {t[1] for t in SYLLABUS.values()} | {t[1] for t in ELEMENTS.values()} | {'info'}
REFS = {k: r for k, r in REFS.items() if k in _used}

VIDEO = Video(
    id='PHY415115_C7_wave_motion',
    course=COURSE, course_name='Physics', module=MODULE,
    module_name='Criterion 7: Identify and apply general principles of wave motion',
    title='Criterion 7: wave motion, complete revision',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Oscillations, Waves'),
    checks=CHECKS,
    thumbnail=V.thumbnail,
    allowed_overlaps=['identify and apply general principles of wave motion'],
    keywords=['band width', 'antinodal', 'monochromatic', 'partial polarisation', 'wavelength', 'frequency', 'amplitude', 'period', 'wave speed', 'transverse', 'longitudinal',
              'superposition', 'constructive', 'destructive', 'standing wave', 'node', 'antinode', 'harmonic',
              'overtone', 'fundamental', 'resonance', 'refraction', 'reflection', "Snell's law", 'critical angle',
              'total internal reflection', 'refractive index', 'path difference', 'coherent', 'diffraction',
              'polarisation', 'polarised', 'beats', 'beat frequency', 'end correction', 'restoring force',
              'linear mass density', 'tension', 'fringe width'],
    description=('A complete revision explainer for TASC Physics (PHY415115) Criterion 7: identify and apply general '
                 'principles of wave motion. For class tests and the end-of-year exam (Section C). Formulas from the '
                 'TASC information sheet are labelled on screen.'),
)
