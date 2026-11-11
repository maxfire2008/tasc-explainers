"""PHY415115 Physics, Criterion 6: Identify and apply principles and theories of electricity and magnetism.

Build with:
    uv run python -m explainer check   videos/PHY415115/c6_electromagnetism.py
    uv run python -m explainer preview videos/PHY415115/c6_electromagnetism.py
    uv run python -m explainer thumbnail videos/PHY415115/c6_electromagnetism.py
    uv run python -m explainer render  videos/PHY415115/c6_electromagnetism.py    # operator only: narration, video, docs
"""
import math

from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, InfoSheet, import_sibling

COURSE, MODULE = 'PHY415115', 'C6'
L.use(style.theme(COURSE, MODULE))
V = import_sibling(__file__, 'c6_visuals.py')

P0 = 'Criterion 6 · Overview'
P1 = 'Part 1 · Electric charge, fields and potential'
P2 = 'Part 2 · Magnetic fields and forces'
P3 = 'Part 3 · Induction'
P4 = 'Part 4 · Contexts'
P5 = 'Finish · Tests & exam technique'

# --------------------------------------------------------------------------- references
COURSE_DOC = 'phy415115-9.html'
INFO = 'PHY415115-Physics-Information-sheet.pdf'
SPEC = 'PHY415115-Physics-External-Assessment-Specifications.pdf'

EXAM_FILES = {2018: 'PHY415115 Physics TASC Exam Paper 2018.pdf', 2019: 'PHY415115 Physics TASC Exam Paper 2019.pdf',
              2020: 'PHY415115 Physics TASC Exam Paper 2020.pdf'}
REPORT_FILES = {2018: 'PHY415115 - Assessment Panel Report 2018.pdf', 2019: 'PHY415115 Assessment Report 2019.pdf',
                2020: 'PHY415115 Assessment Report 2020.pdf'}
# Question -> PDF pages for this criterion's section of each paper and report (from the cached PDFs).
EXAM_PAGES = {
    2018: {7: 19, 8: '20-21', 9: 22, 10: 24, 11: 25, 12: 26},
    2019: {7: 15, 8: '16-17', 9: 18, 10: 19, 11: '20-21', 12: 22},
    2020: {7: 16, 8: 17, 9: 18, 10: 19, 11: '20-21', 12: 22},
    2021: {7: '16-17', 8: '18-19', 9: 20, 10: '22-23', 11: '24-25'},
    2022: {7: 15, 8: 16, 9: '17-18', 10: '19-20', 11: '21-22', 12: '23-24'},
    2023: {7: '20-21', 8: '22-23', 9: '24-25', 10: '26-27', 11: 28, 12: 29},
    2024: {7: 20, 8: 21, 9: '22-23', 10: '24-25', 11: '26-27', 12: '28-29'},
    2025: {6: '16-17', 7: '18-19', 8: '20-21', 9: '22-23', 10: 24, 11: 25},
}
REPORT_PAGES = {
    2018: {7: 3, 8: 3, 9: 3, 10: 3, 11: 4, 12: 4},
    2019: {7: '11-12', 8: '12-13', 9: 13, 10: '13-14', 11: 14, 12: 14},
    2020: {7: 3, 8: 3, 9: 3, 10: 4, 11: 4, 12: 4},
    2021: {7: '5-6', 8: '7-8', 9: '8-9', 10: '9-10', 11: '10-11'},
    2022: {7: '10-11', 8: '12-13', 9: '13-15', 10: '15-16', 11: 16, 12: '16-17'},
    2023: {7: '8-10', 8: '10-12', 9: '12-14', 10: '14-16', 11: '16-17', 12: '17-18'},
    2024: {7: '10-11', 8: '11-12', 9: '12-13', 10: 14, 11: '15-16', 12: '16-18'},
    2025: {6: '5, 26-27', 7: '5-6, 28-29', 8: '6, 30-31', 9: '6-7, 32-33', 10: '7, 34', 11: '7, 35'},
}


def exam(y, q):
    name = EXAM_FILES.get(y, f'PHY415115-Physics-TASC-Exam-Paper-{y}.pdf')
    section = 'Part 2' if y <= 2021 else 'Section B'
    return Ref(name, f'{y} exam, {section}, Question {q}', EXAM_PAGES[y][q])


def report(y, q):
    name = REPORT_FILES.get(y, f'PHY415115-Physics-Assessment-Report-{y}.pdf')
    return Ref(name, f'{y} assessment report, Criterion 6, Question {q}', REPORT_PAGES[y][q])


REFS = {
    'standards': Ref(COURSE_DOC, 'Course document, Criterion 6 standards (element table)'),
    'content': Ref(COURSE_DOC, 'Course document, Science Understanding: principles and theories of electromagnetism (Criterion 6)'),
    'appendix': Ref(COURSE_DOC, 'Course document, Appendix 1: examples in context for C6 & C4'),
    'info': Ref(INFO, 'Information sheet, Electrostatics, Magnetism and Induction sections', page=1),
    'spec': Ref(SPEC, 'External assessment specifications, Section B and Appendix A', page='3, 5'),
}
for _y, _qs in EXAM_PAGES.items():
    for _q in _qs:
        REFS[f'ex{_y % 100}q{_q}'] = exam(_y, _q)
for _y, _qs in REPORT_PAGES.items():
    for _q in _qs:
        REFS[f'ar{_y % 100}q{_q}'] = report(_y, _q)

# --------------------------------------------------------------------------- coverage targets
SYLLABUS = {
    'P1': ('Underlying principle: stationary charges lead to electrostatic effects', 'content'),
    'P2': ('Underlying principle: moving charges lead to magnetic effects', 'content'),
    'P3': ('Underlying principle: accelerating charges lead to electromagnetic radiation; oscillating charges emit continuous waves at the oscillation frequency', 'content'),
    'E1': ('Two forms of charge, positive and negative, carried by electrons and protons', 'content'),
    'E2': ('Macroscopic objects can be charged in various ways including friction', 'content'),
    'E3': ("Electrostatic force between charged objects: Coulomb's law F = kQ1Q2/r²", 'content'),
    'E4': ('The constant kE = 9 × 10⁹ N m² C⁻²', 'content'),
    'E5': ('Solving problems using free body diagrams, vector diagrams, graphing and other techniques', 'content'),
    'E6': ('Point charges produce an electric field; field theory attributes the force to the field', 'content'),
    'E7': ('Definition of electric field strength: force on a small positive charge per unit charge, E = F/q', 'content'),
    'E8': ('Total electric field strength near a single point charge and two point charges, using 2D diagrams', 'content'),
    'E9': ('Field of a point charge E = kQ/r²', 'content'),
    'E10': ('Sketching qualitative electrostatic fields around single and double point charges', 'content'),
    'E11': ('Electric fields cannot enter closed conducting hollow objects (Faraday cages)', 'content'),
    'E12': ('Moving a charge in an electric field changes its potential energy: work done on or by the field', 'content'),
    'E13': ('Potential difference defined: V = work done / q = ΔEnergy / q', 'content'),
    'E14': ('Potential difference related to field strength: E = V/d', 'content'),
    'E15': ('Movement of a charged particle across a potential difference, e.g. the electron gun', 'content'),
    'E16': ('Charged particles in uniform electric fields: along, perpendicular to and at an angle to the field', 'content'),
    'E17': ("Millikan's oil drop experiment: balancing electric and gravitational forces", 'content'),
    'M1': ('Magnetic effects are caused by the movement of charges, even in metal magnets', 'content'),
    'M2': ('Qualitative magnetism: poles, temporary, permanent and electromagnets; field direction defined by a compass', 'content'),
    'M3': ("Earth's magnetic field, including the angle of dip", 'content'),
    'M4': ('Currents attract and repel each other: F = kB I1 I2 l / r', 'content'),
    'M5': ('The constant kB = 2 × 10⁻⁷ N A⁻²', 'content'),
    'M6': ('Magnetic field near a single current-carrying wire, with a rule for its direction', 'content'),
    'M7': ('Definition of magnetic flux density B using the force on a test current', 'content'),
    'M8': ('Magnetic force on a current in a field, F = BIl sinθ, with a rule for direction', 'content'),
    'M9': ('Application to simple currents in wires and simple rotating DC motors', 'content'),
    'M10': ('Magnetic flux density of a single straight wire, B = kB I / r', 'content'),
    'M11': ('Flux density for single currents and for pairs of currents, parallel and at right angles', 'content'),
    'M12': ('Sketching B field lines around one wire or two parallel wires, currents either way', 'content'),
    'M13': ('Magnetic force on moving charges, including direction: F = qvB sinθ', 'content'),
    'M14': ('Circular and helical motion of charges in a field, r = mv sinθ/(qB); van Allen belts', 'content'),
    'M15': ('Bainbridge mass spectrometer and the radius of an ion path, r = mv/(qB)', 'content'),
    'M16': ('Velocity filter: balanced forces in crossed electric and magnetic fields, v = E/B', 'content'),
    'I1': ('Induction of electrical effects: induced E fields, potential differences and currents', 'content'),
    'I2': ("Faraday's law limited to moving conductors in B fields; emf is the potential difference when no current flows", 'content'),
    'I3': ('emf = vlB sinθ', 'content'),
    'I4': ('Potential difference and current (through a resistor) in a conductor drawn through a B field', 'content'),
    'I5': ('Rotating AC generator, with no internal resistance, not extended to DC motors as generators', 'content'),
    'I6': ('Qualitative induction when B changes: transformers, eddy currents and similar', 'content'),
    'I7': ("Lenz's law to predict induced currents from a changing applied magnetic field", 'content'),
    'I8': ('Energy transfer in induction seen as an opposing force on the moving conductor', 'content'),
    'K1': ('Context: medical imaging (MRI)', 'appendix'),
    'K2': ('Context: superconductivity and the Meissner effect', 'appendix'),
    'K3': ('Context: development of the wave theory of light (Maxwell and electromagnetic waves)', 'appendix'),
}

# Elements numbered by row order in the standards table (Element 1 = first row).
ELEMENTS = {
    1: ('Identifies, describes and explains fundamental principles and theories', 'standards'),
    2: ('Selects, applies and manipulates formulae to solve numerical problems (straightforward → complex, analysing validity)', 'standards'),
    3: ('Interprets and analyses data in graphical and tabular form', 'standards'),
    4: ('Applies principles to interpret problems and make predictions in real-world contexts', 'standards'),
}

# What past Criterion 6 questions examined (in our own words).  Never copy question text.
EXAM_TOPICS = {
    'X18-7': ('Charged ball hanging beside a large charged sphere: force diagram, force from the angle, field at the ball, charge on the sphere', 'ex18q7'),
    'X18-8': ('Electron accelerator: field lines, field from PD and gap, why electrons leave the anode unaffected, balanced fields, speed from PD', 'ex18q8'),
    'X18-9': ('Protons in a solar prominence: velocity components, time along the field, radius of gyration', 'ex18q9'),
    'X18-10': ('Faraday disc: sign of charge at a contact, emf, force needed to keep turning at a current', 'ex18q10'),
    'X18-11': ("Faraday's 1821 motors: field of a wire and of a magnet, continued rotation of a wire or magnet", 'ex18q11'),
    'X18-12': ('Compass under a current-carrying wire in the Earth field: wire field, direction by vector diagram', 'ex18q12'),
    'X19-7': ('Charged rod lifting paper: polarisation and inverse square; why a closed charged cage has no inside field', 'ex19q7'),
    'X19-8': ('Two unlike charges: total field at a triangle vertex, force on a test charge, sketching the field', 'ex19q8'),
    'X19-9': ('Three charges: force from one given another, total force vector, direction to a line', 'ex19q9'),
    'X19-10': ('Aircraft in the Earth field: PD across the wing with dip, charge on a wing, why it cannot power electronics', 'ex19q10'),
    'X19-11': ('Wire in a magnet on a balance: slope in newtons per amp from grams, B from slope, effect of rotating the wire', 'ex19q11'),
    'X19-12': ('Electrons accelerated then circling in a field: speed, force, radius, orbit frequency', 'ex19q12'),
    'X20-7': ('Millikan-style balls: electric force, completing a table of fields and charges, consistency with a unit of charge', 'ex20q7'),
    'X20-8': ('Bainbridge spectrometer: plate polarity, field from PD, speed, mass from radius', 'ex20q8'),
    'X20-9': ('Plate swinging through a field: emf, polarity, eddy current sketch, why it stops', 'ex20q9'),
    'X20-10': ('Two perpendicular wires: field magnitude and direction at a point, force per metre on a third wire', 'ex20q10'),
    'X20-11': ('Van de Graaff spark gap: PD from breakdown field, charge, field without the second sphere, why the spark appears, field and charge sketch', 'ex20q11'),
    'X20-12': ('Earth and ionosphere: charge from the field, PD across the atmosphere, current per unit area', 'ex20q12'),
    'X21-7': ('Rod moving in a field at an angle: emf, positive end, force, better conductor, coil leaving a field', 'ex21q7'),
    'X21-8': ('Charged balloon: how it charges, field lines, surface field, electroscope near and touching', 'ex21q8'),
    'X21-9': ('Three point charges in a right-angled arrangement: forces, vector sketch, resultant', 'ex21q9'),
    'X21-10': ('Parallel wires: force, attraction or repulsion, field lines, field at a point, proton radius', 'ex21q10'),
    'X21-11': ('Alpha particle between plates: field, force, distance travelled before striking, field to travel straight', 'ex21q11'),
    'X22-7': ('Millikan-type ball: sphere volume, weight from density, field sketch and size, charge, charge unit', 'ex22q7'),
    'X22-8': ('Fallen power line: PD between feet from a potential graph, body current, safety advice', 'ex22q8'),
    'X22-9': ("Coulomb's experiment data: choosing a variable for a straight line, plotting, charge from the gradient", 'ex22q9'),
    'X22-10': ('Moving-coil meter: current direction, force from spring turn, field from turns', 'ex22q10'),
    'X22-11': ('Vertical wire and compass: wire field and direction, Earth horizontal field, total field from dip', 'ex22q11'),
    'X22-12': ('Van Allen belts: gyroradius at an angle, why electrons sit in the weaker belt, helix sketch, force at converging field lines', 'ex22q12'),
    'X23-7': ('Charged ball between plates: force diagram, force from the angle, field, charge and sign', 'ex23q7'),
    'X23-8': ('Two like charges: force, field from each at a point, total field, field sketch', 'ex23q8'),
    'X23-9': ('Parallel wires: force per length, field of each at a point with directions, total field, field-line sketch', 'ex23q9'),
    'X23-10': ('Force-against-angle experiment: force equation, sine row, plot, B from gradient', 'ex23q10'),
    'X23-11': ('Accelerator protons: momentum units, apparent speed above light, field from radius, repulsion of nearby protons', 'ex23q11'),
    'X23-12': ('Magneto generator: field lines in the iron core, rising or falling field, induced current direction and Lenz justification', 'ex23q12'),
    'X24-7': ('Calcium ion: force on an electron; time-of-flight spectrometer speed, energy and mass', 'ex24q7'),
    'X24-8': ('Aluminium plate levitated over an alternating coil: explanation, direct current case, steel plate', 'ex24q8'),
    'X24-9': ('Electron in a vacuum tube: speed from PD, field between plates, emergence angle, magnetic field to cancel it', 'ex24q9'),
    'X24-10': ('Rectangular motor coil: force on a side with turns, rotation sense, why commutator strips are partial', 'ex24q10'),
    'X24-11': ('Same coil as generator: side speed, peak emf, PD-time sketch, opposing force at a load', 'ex24q11'),
    'X24-12': ('Two like charges: field sketch, total field by vector diagram with direction, force on a test charge', 'ex24q12'),
    'X25-6': ('Thundercloud: ground charge, field sketch, sharp points, hair standing up, minimum PD, charge and energy of a strike', 'ex25q6'),
    'X25-7': ('Ions between plates and in a metal chamber: why acceleration occurs or not, energy, speed, mass', 'ex25q7'),
    'X25-8': ('Rail motor: initial current, force and direction, speed at which acceleration stops, current then', 'ex25q8'),
    'X25-9': ('Light as crossing fields acting on a charge: force formulas, axes of acceleration, negative charge, comet ion tail', 'ex25q9'),
    'X25-10': ('Metal sheet pulled from a field: polarity, eddy current sketch, energy transfers', 'ex25q10'),
    'X25-11': ('Parallel wires out of the page: field sketch, force per length, field at a point', 'ex25q11'),
}

_k, _e, _me, _mp, _kB, _g = 9.00e9, 1.60e-19, 9.11e-31, 1.67e-27, 2e-7, 9.81
# worked-example inputs
_F31 = _k * 5.0e-6 * 1.0e-6 / 0.40 ** 2
_F32 = _k * 2.0e-6 * 1.0e-6 / 0.50 ** 2
_fx, _fy = _F32 * 0.6, _F31 - _F32 * 0.8
_EA, _EB = _k * 6.0e-9 / 0.10 ** 2, _k * 2.0e-9 / 0.10 ** 2
_ex, _ey = (_EA + _EB) * 0.5, (_EA - _EB) * math.sqrt(3) / 2
_vg = math.sqrt(2 * _e * 1.50e3 / _me)
_a = _e * 1.50e4 / _me
_t = 0.0400 / _vg
_vy = _a * _t
_qm = [4.90e-16 * _g / (90.0 / 6.00e-3), 3.30e-16 * _g / (120.0 / 6.00e-3), 6.10e-16 * _g / (75.0 / 6.00e-3)]
_BH = 6.2e-5 * math.cos(math.radians(72))
_bal = [m * 1e-3 * _g for m in (0.204, 0.408, 0.612, 0.815)]
_bsl = (_bal[3] - _bal[0]) / 3.0
_vh = 3.0e6 * math.sin(math.radians(30))
_rh = _mp * _vh / (_e * 0.050)
_th = 2 * math.pi * _rh / _vh
_vside = math.pi * 0.0500 * 25.0
_vtof = 0.800 / 1.55e-5
_ptev = 450e9 * _e / 3.00e8

# Every number spoken or shown in a worked example, recomputed.  check fails on a mismatch.
CHECKS = [
    # three charges
    ('F31', lambda: _F31, 0.28125, 1e-6), ('F32', lambda: _F32, 0.0720, 1e-6),
    ('F3 x', lambda: _fx, 0.0432, 1e-4), ('F3 y', lambda: _fy, 0.22365, 1e-4),
    ('F3 total', lambda: math.hypot(_fx, _fy), 0.2278, 1e-3), ('F3 total 2sf', lambda: math.hypot(_fx, _fy), 0.23, 0.01),
    ('F3 angle', lambda: math.degrees(math.atan2(_fy, _fx)), 79.07, 1e-3), ('F3 angle 2sf', lambda: math.degrees(math.atan2(_fy, _fx)), 79, 0.002),
    ('F3 from vertical', lambda: 90 - math.degrees(math.atan2(_fy, _fx)), 10.93, 1e-3),
    ('Q3 distance', lambda: math.hypot(0.30, 0.40), 0.50, 1e-9),
    # two-charge field
    ('EA', lambda: _EA, 5400, 1e-6), ('EB', lambda: _EB, 1800, 1e-6),
    ('E x', lambda: _ex, 3600, 1e-6), ('E y', lambda: _ey, 3117.7, 1e-4),
    ('E total', lambda: math.hypot(_ex, _ey), 4762.4, 1e-4), ('E total 2sf', lambda: math.hypot(_ex, _ey), 4800, 0.01),
    ('E angle', lambda: math.degrees(math.atan2(_ey, _ex)), 40.89, 1e-3), ('E angle 2sf', lambda: math.degrees(math.atan2(_ey, _ex)), 41, 0.01),
    ('E cosine rule', lambda: math.sqrt(_EA ** 2 + _EB ** 2 - 2 * _EA * _EB * math.cos(math.radians(60))), 4762.4, 1e-4),
    ('E cosine rule wrong', lambda: math.sqrt(_EA ** 2 + _EB ** 2 - 2 * _EA * _EB * math.cos(math.radians(120))), 6490, 1e-3),
    # hanging ball
    ('ball weight', lambda: 2.50e-6 * _g, 2.4525e-5, 1e-4), ('ball E', lambda: 400. / 0.0500, 8000, 1e-9),
    ('ball Fe', lambda: 2.50e-6 * _g * math.tan(math.radians(25.0)), 1.1437e-5, 1e-3),
    ('ball Fe 3sf', lambda: 2.50e-6 * _g * math.tan(math.radians(25.0)), 1.14e-5, 0.005),
    ('ball q', lambda: 2.50e-6 * _g * math.tan(math.radians(25.0)) / 8000, 1.4296e-9, 1e-3),
    ('ball q 3sf', lambda: 2.50e-6 * _g * math.tan(math.radians(25.0)) / 8000, 1.43e-9, 0.003),
    ('ball tension', lambda: 2.50e-6 * _g / math.cos(math.radians(25.0)), 2.706e-5, 1e-3),
    # gun and plates
    ('gun v', lambda: _vg, 2.2954e7, 1e-4), ('gun v 3sf', lambda: _vg, 2.30e7, 0.003), ('gun v/c', lambda: _vg / 3.00e8, 0.0765, 0.002),
    ('plate E', lambda: 300. / 0.0200, 1.50e4, 1e-9),
    ('plate a', lambda: _a, 2.6345e15, 1e-4), ('plate a 3sf', lambda: _a, 2.63e15, 0.003),
    ('plate t', lambda: _t, 1.7426e-9, 1e-4), ('plate t 3sf', lambda: _t, 1.74e-9, 0.004),
    ('plate vy', lambda: _vy, 4.5908e6, 1e-4), ('plate vy 3sf', lambda: _vy, 4.59e6, 0.003),
    ('plate angle', lambda: math.degrees(math.atan(_vy / _vg)), 11.31, 1e-3), ('plate angle 3sf', lambda: math.degrees(math.atan(_vy / _vg)), 11.3, 0.005),
    ('plate shift', lambda: 0.5 * _a * _t ** 2, 4.00e-3, 1e-3), ('half gap', lambda: 0.0200 / 2, 0.0100, 1e-9),
    ('cancel B', lambda: 1.50e4 / _vg, 6.5348e-4, 1e-4), ('cancel B 3sf', lambda: 1.50e4 / _vg, 6.53e-4, 0.003),
    # Millikan
    ('mill E1', lambda: 90.0 / 6.00e-3, 15000, 1e-9), ('mill E2', lambda: 120. / 6.00e-3, 20000, 1e-9), ('mill E3', lambda: 75.0 / 6.00e-3, 12500, 1e-9),
    ('mill q1', lambda: _qm[0], 3.2046e-19, 1e-4), ('mill q1 3sf', lambda: _qm[0], 3.20e-19, 0.002),
    ('mill q2', lambda: _qm[1], 1.6187e-19, 1e-4), ('mill q2 3sf', lambda: _qm[1], 1.62e-19, 0.002),
    ('mill q3', lambda: _qm[2], 4.7873e-19, 1e-4), ('mill q3 3sf', lambda: _qm[2], 4.79e-19, 0.002),
    ('mill n1', lambda: _qm[0] / _e, 2.00, 0.002), ('mill n2', lambda: _qm[1] / _e, 1.01, 0.002), ('mill n3', lambda: _qm[2] / _e, 2.99, 0.002),
    ('mill unit', lambda: (_qm[0] / 2 + _qm[1] + _qm[2] / 3) / 3, 1.6056e-19, 1e-4), ('mill unit 3sf', lambda: (_qm[0] / 2 + _qm[1] + _qm[2] / 3) / 3, 1.61e-19, 0.004),
    # time of flight
    ('tof v', lambda: _vtof, 5.1613e4, 1e-4), ('tof v 3sf', lambda: _vtof, 5.16e4, 0.002),
    ('tof KE', lambda: _e * 5.00e2, 8.00e-17, 1e-9),
    ('tof m', lambda: 2 * _e * 5.00e2 / _vtof ** 2, 6.006e-26, 1e-3), ('tof m 3sf', lambda: 2 * _e * 5.00e2 / _vtof ** 2, 6.01e-26, 0.002),
    # Coulomb data
    ('cd F 2cm', lambda: 3.6e-6 / 0.020 ** 2, 9.0e-3, 1e-6), ('cd F 3cm', lambda: 3.6e-6 / 0.030 ** 2, 4.0e-3, 1e-6),
    ('cd F 4cm', lambda: 3.6e-6 / 0.040 ** 2, 2.25e-3, 1e-6), ('cd F 5cm', lambda: 3.6e-6 / 0.050 ** 2, 1.44e-3, 1e-6),
    ('cd x 2cm', lambda: 1 / 0.020 ** 2, 2500, 1e-9), ('cd x 3cm', lambda: 1 / 0.030 ** 2, 1111, 0.001),
    ('cd x 4cm', lambda: 1 / 0.040 ** 2, 625, 1e-9), ('cd x 5cm', lambda: 1 / 0.050 ** 2, 400, 1e-9),
    ('cd slope', lambda: (9.0e-3 - 1.44e-3) / (2500 - 400), 3.6e-6, 1e-6), ('cd Q', lambda: math.sqrt(3.6e-6 / _k), 2.0e-8, 1e-6),
    # step voltage
    ('sv V 1.6', lambda: 4.0e3 / 1.6, 2500, 1e-9), ('sv V 2.4', lambda: 4.0e3 / 2.4, 1666.7, 1e-4),
    ('sv near', lambda: 4.0e3 / 1.6 - 4.0e3 / 2.4, 833.3, 1e-4), ('sv near 2sf', lambda: 4.0e3 / 1.6 - 4.0e3 / 2.4, 830, 0.005),
    ('sv far', lambda: 4.0e3 / 7.6 - 4.0e3 / 8.4, 50.1, 1e-3), ('sv far 2sf', lambda: 4.0e3 / 7.6 - 4.0e3 / 8.4, 50, 0.003),
    ('sv I near', lambda: (4.0e3 / 1.6 - 4.0e3 / 2.4) / 1.0e3, 0.8333, 1e-3), ('sv I far', lambda: (4.0e3 / 7.6 - 4.0e3 / 8.4) / 1.0e3, 0.0501, 1e-3),
    ('sv slope', lambda: 4.0e3 / 2.0 ** 2, 1000, 1e-9),
    # spark and Earth
    ('spark V', lambda: 3.0e6 * 0.020, 6.0e4, 1e-9),
    ('earth V', lambda: 150 * 60e3, 9.0e6, 1e-9), ('earth Q', lambda: 150 * (6.4e6) ** 2 / _k, 6.83e5, 0.002),
    # compass
    ('compass BH', lambda: _BH, 1.916e-5, 1e-3), ('compass Bw', lambda: _kB * 12 / 0.25, 9.6e-6, 1e-9),
    ('compass angle', lambda: math.degrees(math.atan(_kB * 12 / 0.25 / _BH)), 26.6, 2e-3), ('compass angle 2sf', lambda: math.degrees(math.atan(_kB * 12 / 0.25 / _BH)), 27, 0.02),
    # wires
    ('wire BP', lambda: _kB * 8.0 / 0.60, 2.667e-6, 1e-3), ('wire BQ', lambda: _kB * 2.0 / 0.20, 2.0e-6, 1e-6),
    ('wire Bz', lambda: _kB * 8.0 / 0.60 + _kB * 2.0 / 0.20, 4.667e-6, 1e-3), ('wire Bz 2sf', lambda: _kB * 8.0 / 0.60 + _kB * 2.0 / 0.20, 4.7e-6, 0.01),
    ('wire null', lambda: 0.40 * 8.0 / (8.0 + 2.0), 0.32, 1e-9), ('wire null Q', lambda: 0.40 - 0.32, 0.08, 1e-9),
    ('wire null check P', lambda: 8.0 / 0.32, 25, 1e-9), ('wire null check Q', lambda: 2.0 / 0.08, 25, 1e-9),
    ('wire F per m', lambda: _kB * 8.0 * 2.0 / 0.40, 8.0e-6, 1e-9),
    ('perp B1', lambda: _kB * 6.0 / 0.050, 2.4e-5, 1e-9), ('perp B2', lambda: _kB * 8.0 / 0.050, 3.2e-5, 1e-9),
    ('perp net', lambda: abs(_kB * 6.0 / 0.050 - _kB * 8.0 / 0.050), 8.0e-6, 1e-6), ('perp wrong', lambda: math.hypot(2.4e-5, 3.2e-5), 4.0e-5, 1e-6),
    # balance
    ('bal F1', lambda: _bal[0], 2.001e-3, 1e-3), ('bal F4', lambda: _bal[3], 7.995e-3, 1e-3),
    ('bal slope', lambda: _bsl, 1.998e-3, 1e-3), ('bal B', lambda: _bsl / 0.025, 0.0799, 2e-3), ('bal B 2sf', lambda: _bsl / 0.025, 0.080, 0.01),
    ('bal 30 deg', lambda: _bsl * math.sin(math.radians(30)), 9.99e-4, 2e-3),
    # motor
    ('motor F', lambda: 40 * 0.15 * 2.0 * 0.060, 0.72, 1e-9),
    # helix
    ('helix vperp', lambda: _vh, 1.5e6, 1e-9), ('helix vpar', lambda: 3.0e6 * math.cos(math.radians(30)), 2.598e6, 1e-3),
    ('helix r', lambda: _rh, 0.3131, 1e-3), ('helix r 2sf', lambda: _rh, 0.31, 0.015),
    ('helix T', lambda: _th, 1.3116e-6, 1e-3), ('helix pitch', lambda: 3.0e6 * math.cos(math.radians(30)) * _th, 3.408, 1e-3),
    ('helix pitch 2sf', lambda: 3.0e6 * math.cos(math.radians(30)) * _th, 3.4, 0.01),
    # filter
    ('filter E', lambda: 90.0 / 6.00e-3, 1.50e4, 1e-9), ('filter v', lambda: 90.0 / 6.00e-3 / 0.100, 1.50e5, 1e-9),
    ('filter m', lambda: _e * 0.100 * 0.155 / (90.0 / 6.00e-3 / 0.100), 1.6533e-26, 1e-4), ('filter m 3sf', lambda: _e * 0.100 * 0.155 / 1.50e5, 1.65e-26, 0.004),
    ('filter ratio', lambda: _e * 0.100 * 0.155 / 1.50e5 / _mp, 9.90, 0.002),
    # rod
    ('rod emf', lambda: 2.50 * 0.300 * 0.200, 0.150, 1e-9), ('rod I', lambda: 2.50 * 0.300 * 0.200 / 0.500, 0.300, 1e-9),
    ('rod F', lambda: 0.200 * 0.300 * 0.300, 0.0180, 1e-9), ('rod P mech', lambda: 0.200 * 0.300 * 0.300 * 2.50, 0.0450, 1e-9),
    ('rod P elec', lambda: 0.150 * 0.300, 0.0450, 1e-9),
    ('rod I2', lambda: 0.150 / 0.250, 0.600, 1e-9), ('rod F2', lambda: 0.200 * 0.600 * 0.300, 0.0360, 1e-9),
    # generator
    ('gen v', lambda: _vside, 3.927, 1e-3), ('gen v 3sf', lambda: _vside, 3.93, 0.003),
    ('gen emf', lambda: 120 * _vside * 0.0800 * 0.300, 11.31, 1e-3), ('gen emf 3sf', lambda: 120 * _vside * 0.0800 * 0.300, 11.3, 0.005),
    ('gen emf both', lambda: 2 * 120 * _vside * 0.0800 * 0.300, 22.6, 0.003), ('gen period', lambda: 1 / 25.0, 0.0400, 1e-9),
    # rail motor
    ('rail I', lambda: 6.0 / 0.30, 20, 1e-9), ('rail F', lambda: 0.40 * 20 * 0.15, 1.2, 1e-9), ('rail v', lambda: 6.0 / (0.40 * 0.15), 100, 1e-9),
    # contexts
    ('plane BV', lambda: 6.2e-5 * math.sin(math.radians(72)), 5.90e-5, 2e-3), ('plane emf', lambda: 250 * 40.0 * 6.2e-5 * math.sin(math.radians(72)), 0.5897, 1e-3),
    ('plane emf 2sf', lambda: 250 * 40.0 * 6.2e-5 * math.sin(math.radians(72)), 0.59, 0.005),
    ('lhc p', lambda: _ptev, 2.4e-16, 1e-6), ('lhc B', lambda: _ptev / (_e * 1000), 1.5, 1e-6), ('lhc v', lambda: _ptev / _mp, 1.44e11, 0.005),
]

# --------------------------------------------------------------------------- scenes
S = Step
SCENES = [
Scene('title', P0, 'Welcome', V.title_card, [
    S("Welcome. This video is a complete briefing on Criterion 6 of TASC Physics, PHY415115: electricity and magnetism. Use it to revise for your class tests and for Section B of the end of year exam. You'll learn to use every formula on your information sheet, draw the field diagrams, get directions right, and avoid the traps that examiners keep reporting.", refs=['standards'], anim=4),
]),
Scene('intro', P0, 'How Criterion 6 is assessed', V.overview, [
    S("Criterion 6 is assessed twice. Your teacher assesses it during the year, through class tests, practical work and other tasks. It's also assessed externally, in Section B of the exam: about forty five minutes, forty five marks, and five to seven compulsory questions, with the information sheet and an approved calculator.", refs=['standards', 'spec']),
    S("There are four elements, numbered as in the standards table. Element one: identify, describe and explain principles and theories. Element two: solve numerical problems. Element three: work with graphs and tables. Element four: apply principles to make predictions, including in real world contexts. A tag in the corner shows which element an example practises.", refs=['standards'], elements=[1, 2, 3, 4]),
    S("The standards step up from C to A. At C you identify, solve straightforward problems and interpret data. At B you describe, handle several steps and analyse data. At A you explain, solve complex problems and check validity, evaluate data, and make reasoned predictions in unfamiliar contexts. So we'll keep asking why, as well as how much.", refs=['standards'], elements=[1, 2, 3, 4]),
    S("Here's the roadmap. Part one: charge, Coulomb's law, electric fields and potential difference. Part two: magnetic fields, forces on currents and moving charges, and the mass spectrometer. Part three: induction and Lenz's law. Part four: the course's contexts. Then exam technique. Many marks here depend on directions, so watch for those."),
]),
# ------------------------------------------------------------------- part 1
Scene('principles', P1, 'Charge: the big picture', V.principles, [
    S("Part one. Electromagnetism rests on one principle. Stationary charges lead to electrostatic effects. Moving charges lead to magnetic effects. Accelerating charges lead to electromagnetic radiation. In particular, a charge oscillating back and forth emits a continuous wave with the same frequency as the oscillation. That's how radio waves are made.",
      refs=['content', 'appendix'], covers=['P1', 'P2', 'P3', 'M1', 'K3'], elements=[1]),
    S("Charge comes in two forms, positive and negative, carried by protons and electrons. Matter is normally neutral. Rubbing two materials together, which is friction, moves electrons from one surface to the other. The one that gains electrons becomes negative. Only electrons move, and charge is conserved. Like charges repel; unlike charges attract.",
      refs=['content', 'ex21q8', 'ar21q8', 'ex19q7'], covers=['E1', 'E2'], elements=[1], exam=['X21-8', 'X19-7']),
]),
Scene('polarise', P1, 'Charged objects attract neutral ones', V.polarise, [
    S("Why does a charged rod pick up scraps of neutral paper? The paper's charges shift a little. A negative rod pushes electrons away, leaving the near side slightly positive. The attraction to the near side beats the repulsion from the far side, because force falls with distance, by Coulomb's inverse square law. So there's a net pull. Use a diagram, and name the law.",
      refs=['ex19q7', 'ar19q7', 'content'], covers=['E1', 'E3'], elements=[1], exam=['X19-7'], problem='Explain, with a diagram, how a charged rod can lift small pieces of neutral paper.'),
    S("A gold leaf electroscope works the same way. Bring a negative balloon near the cap without touching. Electrons are pushed down into the leaves, so both become negative, repel, and spread apart. Take the balloon away and they fall. In a metal, it's the electrons that move.",
      refs=['ex21q8', 'ar21q8'], covers=['E1', 'E2'], elements=[1], exam=['X21-8'],
      problem='Explain why the leaves of a neutral electroscope separate when a charged balloon is brought near its cap.'),
    S("Now touch the balloon to the cap, then move it away. Charge has transferred, so the electroscope keeps a net charge and the leaves stay apart. The 2021 report says this part was poorly answered. Near is induction, and temporary. Touching leaves a lasting charge.",
      refs=['ex21q8', 'ar21q8'], covers=['E2'], elements=[1, 4], exam=['X21-8']),
]),
Scene('coulomb', P1, "Coulomb's law", V.coulomb, [
    S("Coulomb's law is on your information sheet, in the electrostatics section: F E equals k E q one q two over r squared, with k E equal to nine times ten to the nine. Use the sizes of the charges, then decide the direction yourself: like charges repel, unlike attract. Double the distance, and the force falls to a quarter.",
      refs=['content', 'info'], covers=['E3', 'E4'], elements=[1, 2]),
    S("Three habits protect your marks. Convert to coulombs and metres first. Square the distance. And measure r between centres: a charged sphere acts like a point charge at its centre, so a ball two metres from the surface of a twenty centimetre radius sphere is two point two metres away. Examiners saw that radius forgotten. And always say attraction or repulsion.",
      refs=['ar18q7', 'ar23q8', 'ar24q7', 'ar21q10'], covers=['E3'], elements=[1, 2], exam=['X18-7', 'X23-8', 'X24-7']),
]),
Scene('we_ball', P1, 'Worked example: a hanging charged ball', V.we_ball, [
    S("Element two. A ball of mass two point five zero milligrams hangs between plates five point zero zero centimetres apart, with four hundred volts across them. It settles twenty five degrees from the vertical, towards the right hand plate. Find the electric force, the charge and its sign. First draw the forces: weight, tension, and one electric force. Examiners saw tension left out, and two electric forces drawn.",
      refs=['ex23q7', 'ar23q7', 'ex18q7', 'ar18q7'], covers=['E5', 'E3'], elements=[2], exam=['X23-7', 'X18-7'],
      problem='A 2.50 mg ball hangs between plates 5.00 cm apart with 400 V across them, 25.0° from the vertical. Find the electric force, the charge on the ball, and its sign.'),
    S("In equilibrium the forces form a closed triangle, so tan of the angle is the electric force over the weight. The weight is two point five times ten to the minus six, times nine point eight one. The electric force is that times tan twenty five degrees: about one point one four times ten to the minus five newtons, towards the right hand plate.",
      refs=['ar23q7', 'ar18q7'], covers=['E5'], elements=[2], exam=['X23-7', 'X18-7']),
    S("The field is V over d: eight thousand newtons per coulomb. The charge is force over field: one point four three times ten to the minus nine coulombs. Is it negative? The ball is pulled towards the positive plate, so yes: the force is opposite to the field. The report says students missed this sign.",
      refs=['ar23q7', 'ex23q7'], covers=['E14', 'E7'], elements=[2, 4], exam=['X23-7']),
]),
Scene('we_coulomb', P1, 'Worked example: forces from two charges', V.we_coulomb, [
    S("Element two, for vector skills. Q one is plus five point zero microcoulombs, at the origin. Q two is minus two point zero microcoulombs, zero point three zero metres to its right. A plus one point zero microcoulomb charge sits zero point four zero metres directly above Q one. Find the force on it: each force separately, then add them as vectors.",
      refs=['ex21q9', 'ar21q9', 'ex19q9', 'ar19q9'], covers=['E5', 'E3'], elements=[2], exam=['X21-9', 'X19-9'],
      problem='Charges of +5.0 μC at the origin and −2.0 μC at 0.30 m to its right. Find the force on a +1.0 μC charge 0.40 m directly above the first charge.'),
    S("The distance to Q two is zero point five zero metres, by Pythagoras. From Q one, the force is zero point two eight one two five newtons, repelling: straight up. From Q two, zero point zero seven two zero newtons, attracting: down and to the right. Sketch both arrows from the charge, the bigger force longer.",
      refs=['ar21q9', 'ar19q9'], covers=['E3', 'E5'], elements=[2], exam=['X21-9', 'X19-9']),
    S("Split the second force using the three, four, five triangle: cosine zero point six, sine zero point eight. Horizontally, zero point zero four three two newtons. Vertically, zero point two eight one two five minus zero point zero five seven six: zero point two two three six five. Add the components for each direction, not the magnitudes.",
      refs=['ar21q9', 'ar24q12'], covers=['E5'], elements=[2], exam=['X21-9', 'X24-12']),
    S("The resultant is about zero point two three newtons, at seventy nine degrees above the horizontal, eleven degrees from the vertical. Check: it's close to the big upward force, tilted towards Q two, as it should be. The 2021 report says few students got full marks, from scalar addition or a wrong angle. State the direction.",
      refs=['ar21q9', 'ar19q9'], covers=['E5'], elements=[2, 4], exam=['X21-9', 'X19-9']),
]),
Scene('field', P1, 'Electric field strength', V.field, [
    S("A charge produces an electric field, and the force on another charge is due to that field. Field strength is defined by the force on a small positive test charge, per unit charge: E equals F over q. It's on your information sheet, in the electrostatics section. Units are newtons per coulomb, and the direction is the way a positive charge would be pushed.",
      refs=['content', 'info'], covers=['E6', 'E7'], elements=[1]),
    S("For a point charge, the sheet gives E equals k E q over r squared: away from a positive charge, towards a negative one. A sphere acts as a point charge at its centre. The force on any charge is q E, reversed for a negative charge. A balloon of radius one point five metres carrying plus twenty five microcoulombs has a surface field of about one times ten to the five newtons per coulomb, outward.",
      refs=['content', 'info', 'ex21q8', 'ar21q8', 'ex24q7', 'ar24q7'], covers=['E9', 'E6'], elements=[2], exam=['X21-8', 'X24-7'],
      problem='What is the electric field strength at the surface of a balloon of radius 1.5 m carrying +25 μC?'),
    S("Pick the formula carefully. E equals k q over r squared is for a point charge. E equals V over d is for the uniform field between plates. In 2022 the main error was using the point charge field in a plates question. Between charges, find each field at the point first, with direction, as if a positive test charge were there.",
      refs=['ar22q7', 'ar23q8'], covers=['E9', 'E14'], elements=[1, 2], exam=['X22-7', 'X23-8']),
]),
Scene('field_sketch', P1, 'Sketching electric fields', V.field_sketch, [
    S("Learn the sketch rules; they earn marks. Field lines start on positive charges and end on negative ones, or go off to infinity. They never cross. Arrows show the way a positive charge would move. Closer lines mean a stronger field. Around a single charge, draw evenly spaced straight lines.",
      refs=['content', 'ex21q8', 'ar21q8'], covers=['E10'], elements=[1], exam=['X21-8']),
    S("For two opposite charges, lines leave the positive one and curve into the negative one. If one charge is bigger, draw more lines from it and show the asymmetry. The reports say sketches lost marks for symmetry with unequal charges, missing arrows, and too few lines on the far side.",
      refs=['ex19q8', 'ar19q8', 'ar23q8', 'ar24q12', 'ex23q8'], covers=['E10', 'E8'], elements=[1], exam=['X19-8', 'X23-8']),
    S("For two like charges, the lines push apart, with a neutral point between them where the fields cancel, closer to the weaker charge. Far away, it looks like one big charge. Don't draw point charges as wires: the 2024 report saw that. Point charges give radial lines; wires give circles.",
      refs=['ex24q12', 'ar24q12', 'ex23q8'], covers=['E10', 'E8'], elements=[1], exam=['X24-12', 'X23-8']),
]),
Scene('we_field', P1, 'Worked example: total field from two charges', V.we_field, [
    S("Element two. Charge A is plus six point zero nanocoulombs, and B is minus two point zero nanocoulombs, zero point one zero metres apart. Point P makes an equilateral triangle with them. The field from A is five thousand four hundred newtons per coulomb, away from A. From B it's one thousand eight hundred, towards B, because B is negative.",
      refs=['ex19q8', 'ar19q8', 'ex24q12', 'ex23q8', 'ar23q8'], covers=['E8', 'E9'], elements=[2], exam=['X19-8', 'X24-12', 'X23-8'],
      problem='A = +6.0 nC and B = −2.0 nC are 0.10 m apart. Point P is 0.10 m from each (an equilateral triangle). Find the magnitude and direction of the total field at P.'),
    S("Add them as vectors, using sixty degrees. Horizontally: five thousand four hundred times a half, plus one thousand eight hundred times a half, is three thousand six hundred. Vertically the parts oppose, leaving about three thousand one hundred and eighteen. The total is about four thousand eight hundred newtons per coulomb, forty one degrees above the horizontal.",
      refs=['ar24q12', 'ar23q8', 'ar19q8'], covers=['E8', 'E5'], elements=[2], exam=['X24-12', 'X23-8', 'X19-8']),
    S("The trap is the angle in the cosine rule. Draw the arrows tip to tail and use the angle inside the triangle: here sixty degrees, giving the same answer as the components. A hundred and twenty degrees would give six and a half thousand. In 2023 students used sixty where one hundred and twenty was needed. So draw the triangle every time, then state the direction.",
      refs=['ar23q8', 'ar24q12', 'ex24q12'], covers=['E8', 'E5'], elements=[2, 4], exam=['X23-8', 'X24-12']),
]),
Scene('conductors', P1, 'Conductors, cages and sharp points', V.conductors, [
    S("Electric fields can't enter a closed hollow conductor: a Faraday cage. Free charges rearrange on the outside until the field inside is zero. Explain it two ways: charges on opposite sides cancel at any inside point; or the conductor is all at one potential, so the potential difference inside is zero, and E equals V over d is zero. With no field there's no force: an ion in a metal chamber just drifts.",
      refs=['content', 'ex19q7', 'ar19q7', 'ex25q7', 'ar25q7'], covers=['E11'], elements=[1, 4], exam=['X19-7', 'X25-7'],
      problem='Why is there no electric field inside a closed, charged metal cage?'),
    S("Charge crowds onto sharp points, so the field is strongest there. Air breaks down at about three million volts per metre, so sparks and lightning start from points. Hair standing on end under a thundercloud means charge is building on the head and the local field is strong, so a strike is more likely. The report says many students gave the cause but not the danger.",
      refs=['ex25q6', 'ar25q6', 'ex20q11', 'ar20q11'], covers=['E11', 'E6'], elements=[1, 4], exam=['X25-6'],
      problem='Why does lightning tend to start from sharp points on the ground, and why is hair standing on end a danger sign?'),
    S("A spark can appear even when the dome's field is below breakdown, because a nearby earthed sphere changes the field. Opposite charge is induced on its near side, squeezing the field lines together across the gap above the breakdown value. For the spark, V equals E d: three million volts per metre across two centimetres is sixty thousand volts. Sketch crowded lines and the induced charges.",
      refs=['ex20q11', 'ar20q11'], covers=['E14', 'E10', 'E2'], elements=[1, 2], exam=['X20-11'],
      problem='Air breaks down at 3.0 × 10⁶ V/m. What potential difference across a 2.0 cm gap gives a spark?'),
]),
Scene('potential', P1, 'Potential difference', V.potential, [
    S("Moving a charge in an electric field takes work, or gives it back. Push a positive charge towards a positive plate and it gains potential energy; release it and that becomes kinetic energy. Potential difference is energy change per unit charge: V equals delta E p over q, on your information sheet, in the electrostatics section. One volt is one joule per coulomb.",
      refs=['content', 'info'], covers=['E12', 'E13'], elements=[1]),
    S("For a uniform field between parallel plates, the sheet gives E equals V over d. The field is the same everywhere between the plates, from positive to negative, in volts per metre, which equals newtons per coulomb. Convert the gap to metres: two hundred and eighty five volts across five millimetres gives fifty seven thousand volts per metre.",
      refs=['content', 'info', 'ex22q7', 'ar22q7', 'ex18q8', 'ar18q8'], covers=['E14'], elements=[2], exam=['X22-7', 'X18-8']),
    S("An electron gun accelerates charge through a potential difference. All the electric potential energy becomes kinetic: q V equals half m v squared. State that equation: the 2024 report says marks go to students who do. Use the particle's own charge and mass, two e for a doubly charged ion. And the speed is only valid well below the speed of light.",
      refs=['content', 'ar24q9', 'ar24q7', 'ex24q9', 'ex25q7', 'ex18q8'], covers=['E15', 'E12'], elements=[2], exam=['X24-9', 'X25-7', 'X18-8']),
]),
Scene('we_gun', P1, 'Worked example: an electron beam through plates', V.we_gun, [
    S("Element two, at A standard. An electron starts from rest and is accelerated through one point five zero kilovolts. It enters horizontal plates, four centimetres long and two centimetres apart, with three hundred volts across them. Find its entry speed, its deflection angle, and the magnetic field that cancels the deflection.",
      refs=['ex24q9', 'ar24q9', 'ex21q11', 'ex18q8'], covers=['E15', 'E16'], elements=[2], exam=['X24-9', 'X21-11', 'X18-8'],
      problem='An electron is accelerated from rest through 1.50 kV, then enters plates 4.00 cm long and 2.00 cm apart with 300 V across them. Find its entry speed, its deflection angle, and the B field that cancels the deflection.'),
    S("Energy first: q V equals half m v squared, so v is the root of two q V over m, which comes to two point three zero times ten to the seven metres per second. Validity: that's under eight percent of the speed of light, so Newtonian physics is fine.",
      refs=['ar24q9', 'ar24q7', 'info'], covers=['E15'], elements=[2], exam=['X24-9', 'X18-8']),
    S("Between the plates, E is V over d: one point five zero times ten to the four newtons per coulomb, pointing down. The electron feels e E, upward, opposite the field. Its acceleration is two point six three times ten to the fifteen metres per second squared. State the field direction: the report says students forgot.",
      refs=['ar24q9', 'ar18q8'], covers=['E16', 'E14'], elements=[2], exam=['X24-9', 'X18-8']),
    S("Horizontally the speed is constant, so the time in the plates is length over speed: one point seven four nanoseconds. The sideways velocity is a t: four point five nine times ten to the six. The angle is tan inverse of v y over v x: eleven point three degrees. Draw the triangle with velocities, not distances. The sideways shift is four millimetres, under a centimetre, so the electron escapes.",
      refs=['ar24q9', 'ar21q11'], covers=['E16'], elements=[2], exam=['X24-9', 'X21-11']),
    S("To cancel the deflection, balance the forces: q v B equals q E, so B is E over v: six point five three times ten to the minus four tesla. Use the full speed. For direction, the electric force on the electron is up, so the magnetic force must be down. With the electron moving right, B points into the page. Many students got this backwards, forgetting it's an electron.",
      refs=['ar24q9', 'ex24q9', 'ar21q11', 'ex21q11'], covers=['E16', 'M16'], elements=[2, 4], exam=['X24-9', 'X21-11']),
]),
Scene('plates', P1, 'Charges in uniform electric fields', V.plates, [
    S("Three cases cover charges in a uniform field. First, along the field: constant force, so constant acceleration, a equals q E over m, with the usual equations. A positive charge speeds up along the field, a negative one against it. Past the anode hole, the field is very weak, so the electron coasts.",
      refs=['content', 'ar18q8', 'ex18q8'], covers=['E16'], elements=[1, 2], exam=['X18-8'], anim=3),
    S("Second, across the field. Horizontally there's no force, so speed is constant. Vertically there's a constant force, so it accelerates from zero. Treat the directions separately, linked by time. The path is a parabola. An alpha particle has charge two e and mass six point six four times ten to the minus twenty seven, so it bends far less than an electron.",
      refs=['content', 'ex21q11', 'ar21q11'], covers=['E16'], elements=[2, 4], exam=['X21-11'], anim=3),
    S("Third, at an angle: split the velocity into a part along the field and a part across it. Along the field there's constant acceleration; across it, constant speed. Then check the particle really reaches where you calculated. Does it hit a plate first?",
      refs=['content', 'ar21q11', 'ex21q11'], covers=['E16'], elements=[2], exam=['X21-11'], anim=3),
]),
Scene('tof', P1, 'Ions in a drift tube', V.tof, [
    S("Time of flight spectrometers combine all this. Ions are accelerated through a potential difference, gaining kinetic energy q V. Then they drift through a field free tube. Why no acceleration there? No potential difference, so no field, so no force. Marks need that reasoning; the report says many students only wrote about attraction and repulsion between plates.",
      refs=['ex25q7', 'ar25q7', 'ex24q7', 'ar24q7'], covers=['E15', 'E11'], elements=[1], exam=['X25-7', 'X24-7']),
    S("Element two. Ions of charge plus e are accelerated through five hundred volts, then drift zero point eight zero zero metres in one point five five times ten to the minus five seconds. Speed: about five point one six times ten to the four metres per second. Kinetic energy is q V. So the mass is two E K over v squared: six point zero one times ten to the minus twenty six kilograms. Watch the square and the factor of two.",
      refs=['ar24q7', 'ar25q7', 'ex24q7', 'ex25q7'], covers=['E15'], elements=[2], exam=['X24-7', 'X25-7'],
      problem='Singly charged ions are accelerated through 5.00 × 10² V, then drift 0.800 m in 1.55 × 10⁻⁵ s. What is their mass?'),
]),
Scene('millikan', P1, "Millikan's oil drop experiment", V.millikan, [
    S("Millikan measured the smallest unit of charge. A tiny charged drop is held still between horizontal plates, so the electric force up balances the weight: q E equals m g. The charge is m g over E, with E equal to V over d. The field direction gives the sign: a negative drop held up needs a positive top plate. Use V over d, not the point charge field, as the 2022 report warned.",
      refs=['content', 'ex22q7', 'ar22q7', 'ex20q7', 'ar20q7'], covers=['E17', 'E14'], elements=[1, 2], exam=['X22-7', 'X20-7']),
    S("Element three, a table. The plates are six millimetres apart. Three balls of known mass are each held still, by ninety, one hundred and twenty and seventy five volts. The fields, V over d, are fifteen thousand, twenty thousand, and twelve and a half thousand newtons per coulomb. Then q equals m g over E gives charges of three point two, one point six two and four point seven nine, times ten to the minus nineteen coulombs.",
      refs=['ex20q7', 'ar20q7', 'ex22q7'], covers=['E17', 'E7'], elements=[2, 3], exam=['X20-7', 'X22-7'],
      problem='Balls of mass 4.90, 3.30 and 6.10 × 10⁻¹⁶ kg are held still between plates 6.00 mm apart by 90.0 V, 120 V and 75.0 V. Find each charge and say what the results suggest.'),
    S("Are these consistent with a smallest unit? Divide each by one point six zero times ten to the minus nineteen: about two, one and three. So charge comes in whole number multiples of one unit. The report says a bare yes or no earns nothing: justify with integer multiples. Dividing each charge by its multiple and averaging gives one point six one times ten to the minus nineteen coulombs.",
      refs=['ar20q7', 'ar22q7', 'ex22q7'], covers=['E17'], elements=[3, 4], exam=['X20-7', 'X22-7']),
]),
Scene('coulomb_graph', P1, "Data: testing Coulomb's law", V.coulomb_graph, [
    S("Element three. A student measures the force between two identical charged spheres at two, three, four and five centimetres: nine point zero, four, two point two five and one point four four millinewtons. Force against distance is a curve. Use the formula to choose what to plot: F equals k Q squared times one over r squared, so plot F against one over r squared. Convert to metres first.",
      refs=['ex22q9', 'ar22q9', 'content'], covers=['E5', 'E3'], elements=[3], exam=['X22-9'],
      problem='Forces between two identical charged spheres are 9.0, 4.0, 2.25 and 1.44 mN at 2.0, 3.0, 4.0 and 5.0 cm. How do you plot a straight line, and what is the charge on each sphere?'),
    S("Plot the points, label both axes with units, and draw a best fit line through the origin. The gradient is k Q squared. Use points far apart: nine minus one point four four millinewtons, over two thousand one hundred, gives three point six times ten to the minus six. Then Q is the root of the gradient over k E: two point zero times ten to the minus eight coulombs. Missing units and best fit lines were the main losses.",
      refs=['ar22q9', 'ex22q9'], covers=['E5'], elements=[2, 3], exam=['X22-9']),
]),
Scene('step_voltage', P1, 'Data: potential near a fallen power line', V.step_voltage, [
    S("Element three, and a real safety question. A fallen live cable leaks charge into the ground, so potential falls with distance, as in this curve. A walker's feet are at different distances, so there's a potential difference between them: not the height of the curve, but the difference between two heights. Two metres out, with feet point eight metres apart, it's about eight hundred and thirty volts. At eight metres, it's only fifty.",
      refs=['ex22q8', 'ar22q8', 'content'], covers=['E13', 'E14', 'E5'], elements=[3, 2], exam=['X22-8'],
      problem='Near a fallen cable the potential is 4.0 × 10³ V m / r. Find the PD between feet 0.80 m apart centred at 2.0 m and at 8.0 m, and the body current if resistance is 1.0 kΩ.'),
    S("With a body resistance of a thousand ohms, I equals V over R gives about zero point eight three amps near the cable, and only zero point zero five zero far away. That's why the advice is to shuffle away with small steps, feet together. The report says many students read the potential at two distances instead of finding the difference, and a few suggested dangerous actions.",
      refs=['ar22q8', 'ex22q8'], covers=['E13', 'E14'], elements=[3, 4], exam=['X22-8'],
      problem='Why should you shuffle with small steps when walking away from a fallen power line?'),
]),
# ------------------------------------------------------------------- part 2
Scene('magnets', P2, 'Magnets and the Earth’s field', V.magnets, [
    S("Part two: magnetism. Magnetic effects are caused by moving charges, even in the metal magnets on your fridge, where electrons moving inside atoms make the field. Every magnet has north and south poles: like poles repel, unlike attract. A permanent magnet keeps its magnetism. A temporary magnet, like soft iron, is magnetic only while in a field. An electromagnet is a current in a coil, often round an iron core.",
      refs=['content'], covers=['M1', 'M2'], elements=[1]),
    S("Field lines run from north to south outside a magnet, in closed loops that never cross, closer where the field is stronger. The direction of a field is defined by a compass: the way a small compass needle's north pole points.",
      refs=['content', 'ex18q11', 'ar18q11'], covers=['M2'], elements=[1], exam=['X18-11']),
    S("The Earth has a field too, and it isn't horizontal everywhere. The angle of dip is the angle between the field and the horizontal. In Tasmania the field points up out of the ground at about seventy degrees. The horizontal part, which a compass senses, is B cosine of the dip; the vertical part is B sine of the dip.",
      refs=['content', 'ex22q11', 'ar22q11', 'ex19q10'], covers=['M3'], elements=[1, 2], exam=['X22-11', 'X19-10']),
]),
Scene('we_compass', P2, 'Worked example: a compass beside a wire', V.we_compass, [
    S("Element two. The Earth's total field is six point two times ten to the minus five tesla at a dip of seventy two degrees. The horizontal part is the total times cosine seventy two: about one point nine times ten to the minus five tesla, north. A vertical wire carries twelve amps upward, and a compass sits zero point two five metres south of it. The wire's field there is nine point six times ten to the minus six tesla.",
      refs=['ex22q11', 'ar22q11', 'ex18q12', 'ar18q12', 'info'], covers=['M3', 'M10', 'M11'], elements=[2], exam=['X22-11', 'X18-12'],
      problem='The Earth field is 6.2 × 10⁻⁵ T at a dip of 72°. A vertical wire carries 12 A upward and a compass is 0.25 m south of it. Which way does the needle point?'),
    S("Which way? Right hand rule: thumb up, fingers curl anticlockwise from above, so south of the wire the field points east. The two fields are at right angles, so the needle points along the total: tan inverse of nine point six over nineteen point two, about twenty seven degrees east of north. The reports say students missed the wire field's direction, and the vector diagram.",
      refs=['ar22q11', 'ar18q12', 'ex18q12'], covers=['M6', 'M11', 'M3'], elements=[2, 4], exam=['X22-11', 'X18-12']),
]),
Scene('wire_field', P2, 'The magnetic field of a current', V.wire_field, [
    S("A current is moving charge, so it makes a magnetic field. Around a straight wire, the lines are circles centred on the wire. Right hand rule: thumb along the conventional current, fingers curl the way the field goes. Current out of the page: anticlockwise. Into the page: clockwise. The lines are closer near the wire, where the field is stronger.",
      refs=['content', 'ar22q11', 'ar25q11', 'ex21q10', 'ar21q10'], covers=['M6', 'M12'], elements=[1], exam=['X21-10', 'X25-11']),
    S("On your information sheet, in the magnetism section: B equals k B I over r, with k B two times ten to the minus seven. I is in amps and r is the distance from the wire in metres. Double the current and the field doubles; double the distance and it halves. Notice r is not squared. B is a vector: give its direction.",
      refs=['content', 'info'], covers=['M10', 'M5', 'M11'], elements=[1, 2]),
    S("With two parallel wires, add the fields as vectors. Between currents in the same direction the fields oppose, so there's a null point, nearer the weaker current. Outside both wires they add. With opposite currents, it's the other way round. The 2025 report lists what a good sketch shows: anticlockwise lines, denser round the bigger current, cancellation between, and the null point nearer the smaller current.",
      refs=['ex25q11', 'ar25q11', 'ex23q9', 'ar23q9', 'ex21q10', 'ar21q10'], covers=['M12', 'M11'], elements=[1, 3], exam=['X25-11', 'X23-9', 'X21-10']),
]),
Scene('wire_force', P2, 'Force between parallel currents', V.wire_force, [
    S("Currents attract and repel. Wires with currents in the same direction attract; opposite directions repel: the reverse of charges. On your information sheet, in the magnetism section: F B equals k B I one I two l over r, where l is the length of wire and r is the distance between the wires.",
      refs=['content', 'info', 'ex21q10', 'ar21q10'], covers=['M4', 'M5'], elements=[1, 2], exam=['X21-10']),
    S("Again, the distance is not squared. The 2021 report lists the errors: squaring the distance, halving it, and ignoring the length. For a force per unit length, divide by l first, so the units are newtons per metre. Don't just put in one metre: the 2025 report says that gives the right number with the wrong working. And justify attract or repel.",
      refs=['ar21q10', 'ar25q11', 'ar23q9', 'ex23q9'], covers=['M4'], elements=[2], exam=['X21-10', 'X23-9', 'X25-11']),
]),
Scene('we_wires', P2, 'Worked example: two parallel wires', V.we_wires, [
    S("Element two. Wire P carries eight amps and wire Q two amps, both out of the page, zero point four metres apart. Find the field at Z, zero point two metres beyond Q. P gives two point seven times ten to the minus six tesla, from zero point six metres. Q gives two point zero times ten to the minus six. Both point up, so they add: about four point seven times ten to the minus six tesla, upward.",
      refs=['ex25q11', 'ar25q11', 'ex23q9', 'ar23q9', 'ex21q10'], covers=['M11', 'M10', 'M12'], elements=[2], exam=['X25-11', 'X23-9', 'X21-10'],
      problem='Wires P (8.0 A) and Q (2.0 A) carry currents out of the page, 0.40 m apart. Find the total field at point Z, 0.20 m beyond Q on the line through them.'),
    S("Where is the field zero? Between the wires. Eight over x equals two over zero point four minus x, so x is zero point three two metres from P and zero point zero eight from Q. Check: eight over zero point three two and two over zero point zero eight are both twenty five. The null point is nearer the weaker current, as predicted.",
      refs=['ar25q11', 'ex25q11'], covers=['M11'], elements=[2, 4], exam=['X25-11']),
    S("The force per unit length is k B I one I two over r: eight point zero times ten to the minus six newtons per metre. The currents are in the same direction, so it's an attraction. Each wire feels the same size of force, in opposite directions, by Newton's third law.",
      refs=['ar25q11', 'ar23q9', 'ex23q9'], covers=['M4', 'M11'], elements=[2], exam=['X25-11', 'X23-9'],
      problem='Wires carrying 8.0 A and 2.0 A in the same direction are 0.40 m apart. What is the force per metre between them, and is it attractive or repulsive?'),
]),
Scene('perp_wires', P2, 'Wires at right angles', V.perp_wires, [
    S("The course also includes wires at right angles. One wire runs along the x axis with six amps to the right; another along the y axis with eight amps upward. Take the point zero point zero five metres from each, up and to the right. The first gives two point four times ten to the minus five tesla, out of the page by the right hand rule. The second gives three point two times ten to the minus five, into the page.",
      refs=['ex20q10', 'ar20q10', 'ex23q9', 'ar23q9'], covers=['M11', 'M6'], elements=[2], exam=['X20-10', 'X23-9'],
      problem='A wire along the x axis carries 6.0 A to the right and another along the y axis carries 8.0 A upward. Find the total field at the point 0.050 m from each wire, up and to the right.'),
    S("Both fields lie along one line, out of or into the page, so subtract: eight times ten to the minus six tesla, into the page. The 2020 report says some students used Pythagoras here, but these fields lie along one line. Only if the fields themselves point at right angles, as in 2023, do you use a right angled triangle. Draw both fields first.",
      refs=['ar20q10', 'ar23q9', 'ex23q9'], covers=['M11', 'M12'], elements=[2, 4], exam=['X20-10', 'X23-9']),
]),
Scene('force_current', P2, 'Force on a current in a field', V.force_current, [
    S("Magnetic flux density B is defined using a test current: put a wire at right angles to the field and measure the force. B equals F over I l sine theta; the unit is the tesla. That isn't on the sheet, so learn it. On your information sheet, in the magnetism section, is F B equals I l B sine theta: l is the length in the field and theta is the angle between wire and field. No force when the wire is parallel.",
      refs=['content', 'info', 'ex19q11', 'ar19q11', 'ex23q10'], covers=['M7', 'M8'], elements=[1, 2], exam=['X19-11', 'X23-10']),
    S("For direction, use a right hand rule: fingers along the current, curl them towards the field, and the thumb gives the force, perpendicular to both. Markers don't recommend the left hand version. Common errors: using an angle of rotation instead of the angle between wire and field, and, with many turns, forgetting the length in the field is N times the side.",
      refs=['ar22q10', 'ar20q9', 'ar24q10', 'ex22q10', 'ex24q10'], covers=['M8'], elements=[1, 2], exam=['X22-10', 'X24-10']),
]),
Scene('motor', P2, 'Motors and meters', V.motor, [
    S("A simple DC motor is a coil in a field. Current goes up one side and down the other, so the forces on the sides are opposite and the coil turns. Each side feels N B I l. Element two: forty turns, sides six centimetres, zero point one five tesla, two amps: zero point seven two newtons on each side. The 2024 report says students forgot the turns.",
      refs=['ex24q10', 'ar24q10', 'content'], covers=['M9', 'M8'], elements=[2], exam=['X24-10'],
      problem='A motor coil has 40 turns, sides 6.0 cm long, in a 0.15 T field with a current of 2.0 A. What force acts on one side?'),
    S("Without a commutator the coil would swing round and stop, since after half a turn the forces would slow it. The commutator is a split ring that flips the current each half turn. Its gaps let the current stop briefly as the coil passes vertical, then flow the other way, so the force always turns the coil the same way. To give the sense of rotation, apply the right hand rule to one side, with a reason.",
      refs=['ex24q10', 'ar24q10'], covers=['M9'], elements=[1, 4], exam=['X24-10'],
      problem='What is the purpose of the gaps in the split-ring commutator of a DC motor?'),
    S("Two more devices use this force. A moving coil meter has a coil in a radial field, so the force on each side is always perpendicular to the field, and springs balance it: deflection shows the current. Sine isn't needed, as the 2022 report notes. And in Faraday's 1821 motors the force on a wire near a magnet pole is always sideways, so the wire keeps circling. Students saw the first push but not that it continues.",
      refs=['ex22q10', 'ar22q10', 'ex18q11', 'ar18q11'], covers=['M9', 'M8', 'M12'], elements=[1, 4], exam=['X22-10', 'X18-11']),
]),
Scene('balance_data', P2, 'Data: measuring B with a balance', V.balance_data, [
    S("Element three. A magnet sits on a balance with a two point five centimetre wire at right angles to its field. For one, two, three and four amps, the readings are point two zero four, point four zero eight, point six one two and point eight one five grams. Convert grams to kilograms and multiply by g to get newtons.",
      refs=['ex19q11', 'ar19q11', 'ex23q10', 'ar23q10'], covers=['M8', 'E5'], elements=[3], exam=['X19-11', 'X23-10'],
      problem='A 2.5 cm wire at right angles to a magnet on a balance carries 1.0 to 4.0 A, giving readings of 0.204, 0.408, 0.612 and 0.815 g. What is the flux density B?'),
    S("Plot force against current. F equals B l times I, so the gradient is B l: about two times ten to the minus three newtons per amp, and B is zero point zero eight zero tesla. Rotate the wire to thirty degrees and the gradient halves, a factor of sine thirty. In 2023, force was plotted against sine theta: the gradient is I l B. Many students didn't link their formula to the table.",
      refs=['ar19q11', 'ar23q10', 'ex23q10', 'ex19q11'], covers=['M8', 'M7'], elements=[2, 3], exam=['X19-11', 'X23-10']),
]),
Scene('moving_charge', P2, 'Force on a moving charge', V.moving_charge, [
    S("A moving charge feels a magnetic force: F B equals q v B sine theta, on your information sheet, in the magnetism section. It's the force on a current, per charge. It's perpendicular to both velocity and field: use the right hand rule for a positive charge and reverse it for a negative one. No force on a charge at rest, or one moving along the field.",
      refs=['content', 'info', 'ar25q9'], covers=['M13'], elements=[1, 2], anim=3),
    S("The force is always perpendicular to the velocity, so it does no work: it changes direction, not speed. A charge at right angles to a uniform field moves in a circle, with the magnetic force as the centripetal force. From q v B equals m v squared over r, the radius is m v over q B; the sheet's version has sine theta, which is one at ninety degrees. Faster or heavier: bigger circle. Stronger field: smaller.",
      refs=['content', 'info', 'ex19q12', 'ar19q12', 'ex21q10', 'ar21q10'], covers=['M14', 'M13'], elements=[1, 2], exam=['X19-12', 'X21-10'], anim=3),
    S("Use the right mass and charge: a proton's mass is one point six seven times ten to the minus twenty seven kilograms, an electron's nine point one one times ten to the minus thirty one, and the charge is one point six times ten to the minus nineteen coulombs, not one. Reports from 2021 and 2022 saw both errors. The orbit frequency is q B over two pi m: it doesn't depend on speed.",
      refs=['ar21q10', 'ar22q12', 'ar20q8', 'ar19q12', 'ex22q12'], covers=['M14'], elements=[2], exam=['X19-12', 'X22-12'], anim=3),
]),
Scene('helix', P2, 'Helices and the van Allen belts', V.helix, [
    S("If the velocity is at an angle to the field, split it. The perpendicular part makes a circle; the parallel part is unchanged. Together: a helix. The radius uses only the perpendicular part, r equals m v sine theta over q B, which is the sheet's form. The time along the field uses the parallel part. In 2018 students used the total speed for that time.",
      refs=['content', 'info', 'ex18q9', 'ar18q9', 'ex22q12', 'ar22q12'], covers=['M14'], elements=[1, 2], exam=['X18-9', 'X22-12']),
    S("Element two. A proton moves at three times ten to the six metres per second, at thirty degrees to a field of zero point zero five zero tesla. The perpendicular part is one point five times ten to the six; the parallel part, two point six times ten to the six. The radius is about zero point three one metres. One turn takes one point three one microseconds, in which it advances along the field about three point four metres.",
      refs=['ar22q12', 'ar18q9', 'ex18q9'], covers=['M14', 'M13'], elements=[2], exam=['X18-9', 'X22-12'],
      problem='A proton moves at 3.0 × 10⁶ m/s at 30° to a 0.050 T field. Find the radius of its circular motion and how far it advances along the field in one turn.'),
    S("Charged particles in the van Allen belts spiral along field lines between the poles. Near the poles the lines squeeze together, so the force, perpendicular to B, has a component back along the field: the particle slows its advance, turns round, and spirals back. Protons have huge radii in weak fields, so they escape; electrons stay in the outer belt. Few students gave reasons, the report says.",
      refs=['ex22q12', 'ar22q12', 'content'], covers=['M14'], elements=[1, 4], exam=['X22-12'],
      problem='Why does a charged particle spiralling along converging field lines near the poles turn around?'),
]),
Scene('filter', P2, 'Velocity filters and mass spectrometers', V.filter, [
    S("A velocity filter uses electric and magnetic fields at right angles. The electric force q E acts one way, the magnetic force q v B the other. Particles pass straight through when they balance: v equals E over B, on your information sheet, in the magnetism section. The charge cancels, so it selects speed. Many students worked from basic forces, which is fine, but the formula is quicker.",
      refs=['content', 'info', 'ex21q11', 'ar21q11', 'ex18q8', 'ar18q8', 'ex20q8'], covers=['M16'], elements=[1, 2], exam=['X21-11', 'X18-8', 'X20-8']),
    S("Direction is the tricky part. The forces must be opposite. Find the magnetic force by the right hand rule, then put the electric force the other way: for positive ions, that tells you which plate is positive. In 2020 some students thought the plate should be positive to repel the ions on their circular path: the report calls it a fundamental misunderstanding. The plates balance the magnetic force.",
      refs=['ar20q8', 'ex20q8', 'ar18q8'], covers=['M16', 'M13'], elements=[1, 4], exam=['X20-8', 'X18-8'],
      problem='In a velocity filter with positive ions moving right and B out of the page, which plate must be positive?'),
    S("A Bainbridge spectrometer sends the selected ions into a chamber with only a magnetic field. Speed is known, so the radius depends on mass: r equals m v over q B, from your information sheet. Heavier ions make bigger semicircles. Measure the radius and you can find the mass. Use the ion's charge, e for a singly charged ion; students who used one coulomb lost half marks.",
      refs=['content', 'ex20q8', 'ar20q8'], covers=['M15'], elements=[1, 2], exam=['X20-8']),
]),
Scene('we_filter', P2, 'Worked example: a mass spectrometer', V.we_filter, [
    S("Element two. A velocity filter has ninety volts across plates six millimetres apart, and B of zero point one zero zero tesla. The field is V over d: fifteen thousand newtons per coulomb. The speed is E over B: one point five times ten to the five metres per second. Units check: newtons per coulomb divided by tesla is metres per second.",
      refs=['ex20q8', 'ar20q8', 'ex21q11'], covers=['M16', 'E14'], elements=[2], exam=['X20-8', 'X21-11'],
      problem='A velocity filter has 90.0 V across plates 6.00 mm apart, and B = 0.100 T. What speed passes straight through?'),
    S("In the separation chamber, with the same B, an ion with a single charge lands at a radius of zero point one five five metres. Mass is q B r over v: about one point six five times ten to the minus twenty six kilograms, roughly ten times a proton's mass, so an ion of mass number about ten.",
      refs=['ar20q8', 'ex20q8', 'info'], covers=['M15'], elements=[2, 4], exam=['X20-8'],
      problem='A singly charged ion that passed the filter above (B = 0.100 T) lands at a radius of 0.155 m. What is its mass?'),
]),
Scene('em_wave', P2, 'Light as crossing fields', V.em_wave, [
    S("A light wave is an electric and a magnetic field, at right angles, both changing quickly. Take a positive charge hit by the wave. The electric force is q E, and the magnetic force is q v B sine theta. Not Coulomb's law, which is for two charges. E pushes the charge back and forth along the E axis. Then B acts on that moving charge, at right angles to its velocity and to B.",
      refs=['ex25q9', 'ar25q9', 'content'], covers=['P3', 'M13', 'E7'], elements=[1, 4], exam=['X25-9']),
    S("Which way is the magnetic force? The right hand rule says: along the beam. For a negative charge, the electric push reverses, so the velocity reverses; reversed charge and reversed velocity cancel, so the magnetic force is again along the beam. So the beam pushes charges the way it travels, which is how sunlight can push a comet's ions into a tail pointing away from the Sun.",
      refs=['ar25q9', 'ex25q9'], covers=['P3', 'M13'], elements=[1, 4], exam=['X25-9'],
      problem='Explain how light from the Sun can make the ion tail of a comet point away from the Sun.'),
]),
# ------------------------------------------------------------------- part 3
Scene('induction', P3, 'Induced emf in a moving conductor', V.induction, [
    S("Part three: induction. Push a conductor through a magnetic field and its free charges feel a magnetic force, so they move to one end. That sets up a potential difference along the conductor: induction. The emf is the potential difference when no current flows. On your information sheet, in the induction section: emf equals v l B sine theta, where l is the length in the field and theta is the angle between velocity and field.",
      refs=['content', 'info', 'ex21q7', 'ar21q7'], covers=['I1', 'I2', 'I3'], elements=[1, 2], exam=['X21-7']),
    S("Emf is measured in volts, which some students mixed up. The common error in 2021 was the angle. For direction, use the right hand rule on positive charges in the conductor: that end becomes positive. Explain it, naming the way positive charge is pushed; markers want more than 'by the right hand rule'.",
      refs=['ar18q10', 'ar21q7', 'ex18q10', 'ar20q9', 'ex20q9', 'ar25q10', 'ex25q10'], covers=['I2', 'I3'], elements=[1, 2, 4], exam=['X18-10', 'X21-7', 'X20-9', 'X25-10']),
    S("A moving conductor is like a battery, so take care with polarity. Inside a source, positive charge is pushed from the negative terminal to the positive. The 2020 report says some students confused this with the current direction in an outside circuit, where current runs from positive to negative. Connect a resistor and a current flows: from the sheet, V equals I R and P equals V I.",
      refs=['ar20q9', 'ar25q10', 'ex20q9', 'info', 'ex25q10'], covers=['I4', 'I1'], elements=[1, 2, 4], exam=['X20-9', 'X25-10']),
]),
Scene('we_rod', P3, 'Worked example: a rod on rails', V.we_rod, [
    S("Element two, with an energy check. A rod zero point three metres long moves at two point five metres per second, at right angles to a field of zero point two tesla. The emf is v l B: about zero point one five volts. With the field into the page and the rod moving right, positive charges are pushed up the page, so the top end is positive.",
      refs=['ex21q7', 'ar21q7', 'ex18q10', 'ex20q9'], covers=['I3', 'I2'], elements=[2], exam=['X21-7', 'X18-10', 'X20-9'],
      problem='A 0.300 m rod moves at 2.50 m/s at right angles to a 0.200 T field. Find the emf, and say which end is positive when the field is into the page and the rod moves right.'),
    S("Connect a zero point five ohm resistor. The current is emf over R: zero point three amps. The rod carries a current in a field, so it feels a force B I l: about zero point zero one eight newtons. By Lenz's law it opposes the motion, so it points left, and you must push with that force to keep the speed. Give that direction; the 2018 report says it was often missing.",
      refs=['ar21q7', 'ar18q10', 'ex21q7'], covers=['I4', 'I8'], elements=[2, 4], exam=['X21-7', 'X18-10']),
    S("Check the energy. You push with zero point zero one eight newtons through two point five metres each second: zero point zero four five watts. The electrical power, emf times current, is also zero point zero four five watts. They match, so energy is conserved. The opposing force is just the cost of the electrical energy.",
      refs=['content'], covers=['I8', 'I4'], elements=[2, 4]),
    S("Replace the rod with a better conductor, half the resistance, at the same speed. The emf depends only on v, l and B, so it's unchanged. But the current doubles, so the force doubles: about zero point zero three six newtons. A better conductor is harder to push. The 2021 report gave the same reasoning.",
      refs=['ex21q7', 'ar21q7'], covers=['I4', 'I8'], elements=[2, 4], exam=['X21-7'],
      problem='The rod above is replaced by a conductor of half the resistance at the same speed. Is the force needed larger, smaller or the same, and why?'),
]),
Scene('lenz', P3, "Changing fields and Lenz's law", V.lenz, [
    S("Induced effects also appear when a field changes. A steady field gives nothing. Move a magnet into a coil, or a coil out of a field, and a current appears briefly. Lenz's law gives its direction: the induced current's own field opposes the change that caused it. Push a north pole towards a coil and the coil makes a north pole to push back; pull it away and it makes a south pole to hold on. That's energy conservation again.",
      refs=['content', 'ex21q7', 'ar21q7', 'ex23q12', 'ar23q12'], covers=['I1', 'I7', 'I6', 'I8'], elements=[1], exam=['X21-7', 'X23-12']),
    S("To use it, follow four steps. One: what is the applied field doing? Two: so which way must the induced field point to oppose that? Three: right hand rule for a coil, to turn that field into a current. Four: write it up, naming Lenz's law. In 2021 few students quoted the law correctly. The 2023 magneto question also needed the iron core as a temporary magnet, whose field rises as a pole approaches.",
      refs=['ar21q7', 'ar23q12', 'ex23q12'], covers=['I7'], elements=[1, 4], exam=['X21-7', 'X23-12'],
      problem='A coil is pulled out of a region with field into the page. Which way does the induced current flow?'),
    S("Eddy currents are induced currents looping through a lump of metal. Move a plate through a field and they form, and by Lenz's law they oppose the motion, so the plate slows rapidly. Say the induced current makes a field, whose force opposes the motion; or use energy: kinetic to electrical to heat. Draw the loops circular, partly in the field and partly out of it: the reports say many students didn't.",
      refs=['ex20q9', 'ar20q9', 'ex25q10', 'ar25q10'], covers=['I6', 'I7', 'I8'], elements=[1, 3], exam=['X20-9', 'X25-10'],
      problem='A metal sheet is pulled out of a field directed into the page. Which way do the eddy currents circulate, and what energy transfers occur?'),
    S("Eddy currents also explain a levitating aluminium plate. A coil carries alternating current, so its field keeps changing, inducing eddy currents in the plate whose field opposes the coil's, so the plate is repelled upward. With direct current the field doesn't change, so there's no induction. A thin steel plate would be attracted, as iron becomes a temporary magnet. Students lost marks using weight, or electric charge, in their explanations.",
      refs=['ex24q8', 'ar24q8', 'content'], covers=['I6', 'I7'], elements=[1, 4], exam=['X24-8'],
      problem='Why does an aluminium plate levitate above a coil carrying alternating current, but not direct current?'),
]),
Scene('transformer', P3, 'Transformers', V.transformer, [
    S("A transformer is a qualitative topic here. Alternating current in the primary coil makes a changing field in the iron core, which links the secondary coil, inducing an alternating emf. A steady current changes nothing, so transformers need alternating current. More turns on the secondary gives a bigger voltage; power is conserved, so P equals V I, from your information sheet, means the current falls. Thin layers in the core limit eddy currents.",
      refs=['content', 'info'], covers=['I6', 'I1'], elements=[1]),
]),
Scene('generator', P3, 'Generators', V.generator, [
    S("A generator turns this around. Spin a coil in a field and its sides cut across the field, inducing an emf. The side's speed is two pi r times the frequency. The emf is greatest when the side moves at right angles to the field and zero when it moves along it, so it varies like a sine wave at the rotation frequency. With slip rings the output alternates. N turns multiply the wire length.",
      refs=['content', 'ex24q11', 'ar24q11', 'ex23q12'], covers=['I5', 'I3'], elements=[1, 2], exam=['X24-11', 'X23-12'], anim=4),
    S("To sketch emf against time, read where the coil starts: moving across the field, a peak; moving along it, zero. Mark the period on the axis. With a commutator the output stays one sign, in arches. In 2024 many shapes were marked wrong: horizontal lines, triangles, square waves, full sine waves. The course doesn't extend DC motors as generators, but that exam had a commutator, and its solution was arches with small gaps.",
      refs=['ar24q11', 'ex24q11', 'content'], covers=['I5'], elements=[3, 1], exam=['X24-11'],
      problem='Sketch the potential difference against time for a coil rotating in a field with slip rings, and for the same coil with a commutator.'),
]),
Scene('we_gen', P3, 'Worked example: a hand-turned generator', V.we_gen, [
    S("Element two. A coil of one hundred and twenty turns has active sides eight centimetres long and a width of five centimetres. It turns at twenty five hertz in a field of zero point three tesla. The period is zero point zero four seconds; don't use fifty. The side's speed is pi times the width times the frequency: about three point nine three metres per second, with metres, not centimetres. Both mistakes appeared in 2024.",
      refs=['ex24q11', 'ar24q11'], covers=['I5', 'I3'], elements=[2], exam=['X24-11'],
      problem='A 120-turn coil with 8.00 cm active sides and 5.00 cm width turns at 25.0 Hz in a 0.300 T field. How fast do the sides move, and what is the peak emf of one side?'),
    S("The peak emf of one side is N v l B: about eleven point three volts. The other side adds the same in series, so the whole coil gives about twenty two point six volts. Say which you're calculating. Use your own value from earlier parts, not the examiner's, if you can. And with a load, the current feels an opposing force, just as for the rod.",
      refs=['ar24q11', 'ex24q11'], covers=['I5', 'I3', 'I8'], elements=[2, 4], exam=['X24-11']),
]),
Scene('back_emf', P3, 'Induction working against a motor', V.back_emf, [
    S("Induction also acts inside motors. A rail motor has a roller across two rails in a field, with a battery. Element two: six volts across a zero point three ohm roller gives a starting current of twenty amps. The force is B I l: about one point two newtons, along the rails, away from the battery. Give the direction; the report says it was often missing or unclear.",
      refs=['ex25q8', 'ar25q8', 'content'], covers=['M8', 'M9', 'I4'], elements=[2], exam=['X25-8'],
      problem='A roller across rails 0.15 m apart in a 0.40 T field is connected to 6.0 V, resistance 0.30 Ω. What is the starting force on it?'),
    S("As the roller speeds up, it's a conductor moving in a field, so it generates an emf that opposes the supply. Acceleration stops when it equals the supply: v l B equals six, so v is a hundred metres per second. Then there's no net voltage, so no current and no force: a steady speed, not a stop. The 2025 report says many students confused the emf with the force.",
      refs=['ar25q8', 'ex25q8'], covers=['I8', 'I3', 'I4'], elements=[2, 4], exam=['X25-8'],
      problem='For the rail motor above, at what speed does the roller stop accelerating, and what is the current then?'),
]),
Scene('ind_contexts', P3, 'Induction in the real world', V.ind_contexts, [
    S("The Faraday disc is the simplest generator. A strip of the disc, of length l, moves at speed v through the field, so the emf between centre and rim is v l B. Use the right hand rule on positive charge to say which contact is positive, and explain it. A current brings a force B I l opposing the turning, so you must apply a force in the direction of motion; the report says students forgot that direction.",
      refs=['ex18q10', 'ar18q10'], covers=['I3', 'I8', 'I2'], elements=[2, 4], exam=['X18-10']),
    S("An aircraft is a conductor too. Only the vertical part of the Earth's field counts: B sine of the dip. At two hundred and fifty metres per second, with a forty metre wingspan, where the field is six point two times ten to the minus five tesla at a dip of seventy two degrees, the wings have about zero point five nine volts across them. Flying east, the right wing is positive. It can't power the electronics: they move with the plane, so the same potential difference appears across them all, and no steady current flows.",
      refs=['ex19q10', 'ar19q10'], covers=['I3', 'I2', 'M3'], elements=[2, 4], exam=['X19-10'],
      problem='A plane flies east at 250 m/s with a 40.0 m wingspan where the Earth field is 6.2 × 10⁻⁵ T at a dip of 72°. What potential difference appears across the wings, and why can it not power the plane?'),
]),
# ------------------------------------------------------------------- part 4
Scene('contexts', P4, 'Contexts named in the course', V.contexts, [
    S("The course names three contexts. Magnetic resonance imaging, or MRI, uses very strong magnetic fields to magnetise nuclei in the body, and builds images of soft tissue without ionising radiation; the fields make metal implants a danger. Superconductivity is zero electrical resistance below a critical temperature, with the Meissner effect: magnetic flux is expelled from the inside. Superconducting coils make the strong fields in MRI machines.",
      refs=['appendix'], covers=['K1', 'K2'], elements=[4]),
    S("The third context is the wave theory of light. In the eighteen sixties, Maxwell showed that changing electric and magnetic fields travel through space as waves at the speed of light. So light is an electromagnetic wave, which links back to the principle we began with: an oscillating charge makes waves at its own frequency, which is how an aerial works. Accelerators use electric fields to speed charges up and magnetic fields to steer them.",
      refs=['appendix', 'content'], covers=['K3', 'P3'], elements=[1, 4]),
]),
Scene('exam_contexts', P4, 'Unfamiliar contexts', V.exam_contexts, [
    S("Real world contexts in the exam use the same physics. Treat the Earth as a sphere with its charge at the centre. E equals k E q over r squared gives the charge, and V equals E d the potential difference across the atmosphere. A hundred and fifty volts per metre over sixty kilometres is nine million volts; the charge is E r squared over k, about six point eight times ten to the five coulombs. Use the radius in metres: the 2020 report saw wrong radii and unit slips.",
      refs=['ex20q12', 'ar20q12', 'ex25q6', 'ar25q6'], covers=['E9', 'E14', 'E13'], elements=[2, 4], exam=['X20-12', 'X25-6'],
      problem='Near the ground the Earth\'s field is 150 V/m, and the atmosphere layer is 60 km thick. Find the potential difference across it and the charge on the Earth (radius 6.4 × 10⁶ m).'),
    S("In a lightning strike, the minimum potential difference is the ionising field times the length; charge is current times time; energy is charge times potential difference. The 2025 report notes students missed that the field was given, and that the question asked for the minimum. In an accelerator, momentum is often quoted as energy over c: four hundred and fifty gigaelectronvolts per c is two point four times ten to the minus sixteen kilogram metres per second. A one kilometre ring then needs one point five tesla. And p equals m v would exceed light speed, showing Newtonian mechanics failing.",
      refs=['ex23q11', 'ar23q11', 'ex25q6', 'ar25q6'], covers=['E13', 'M14'], elements=[2, 4], exam=['X23-11', 'X25-6'],
      problem='A proton beam has momentum 450 GeV/c in a ring of radius 1.0 km. What is its momentum in kg m/s and what field is needed to bend it round the ring?'),
]),
# ------------------------------------------------------------------- finish
Scene('exam_tips', P5, 'Tips for tests and the exam', V.exam_tips, [
    S("Finally, technique, from what examiners have reported over several years. One: give a direction whenever you give a force, field or current: the most common lost mark. Two: add vectors with a diagram, tip to tail, and decide the angle from the picture.",
      refs=['ar23q8', 'ar23q9', 'ar24q12', 'ar25q7', 'ar25q8', 'ar18q12']),
    S("Three: convert first: centimetres, millimetres, microcoulombs, grams, kilovolts. Four: choose the right formula: Coulomb for forces between charges, E equals V over d between plates, k q over r squared for a point charge. Five: use e, not one, and the proton's mass, not the electron's.",
      refs=['ar24q7', 'ar21q10', 'ar22q12', 'ar20q8', 'ar22q7', 'ar24q9']),
    S("Six: for magnetic force and induced emf, use a right hand rule, and say what thumb and fingers show. Seven: Lenz's law needs a full answer: what changes, what the induced field does, then the current. Eight: sketches need arrows, no crossings, line density for strength, and asymmetry for unequal sources.",
      refs=['ar20q9', 'ar21q7', 'ar23q8', 'ar23q9', 'ar24q12', 'ar25q11', 'ar23q12']),
    S("Nine: in data questions, choose the variable that gives a straight line, label axes, draw the best fit, and take the gradient from far apart points. Ten: state your energy equation when you equate energies. And check every answer: is the speed below light, is the sign right, do the energies balance?",
      refs=['ar22q9', 'ar24q9', 'ar23q10', 'ar22q8']),
]),
Scene('more_tips', P5, 'More examiner tips', V.more_tips, [
    S("Here are more. Eleven: explain, don't just state: no field in a cage because there's no potential difference. Twelve: for force per unit length, divide by the length. Thirteen: for a coil, count the turns. Fourteen: the sign of a charge comes from the force and the field.",
      refs=['ar25q7', 'ar25q11', 'ar24q10', 'ar23q7', 'ar24q9']),
    S("Fifteen: the angle in the emf and force formulas is between the velocity or wire and the field. Sixteen: an emf is a potential difference, not a force. Seventeen: in a circle, use v at ninety degrees, but only the perpendicular part at an angle. Eighteen: carry your own unrounded values forward.",
      refs=['ar21q7', 'ar25q8', 'ar18q9', 'ar22q10', 'ar24q9']),
]),
Scene('summary', P5, 'Summary', V.summary, [
    S("That's every part of Criterion 6. Stationary charges make electric fields, with Coulomb's law and potential difference. Moving charges make magnetic fields, which push on currents and on moving charges, in circles, helices and the mass spectrometer. Moving conductors and changing fields induce emfs, and Lenz's law opposes the change. Practise directions, vector diagrams and explanations as well as numbers, and you'll be ready for your tests and Section B. Good luck."),
]),
]

# Report references that no slide cites are left out of the reference list.
_used = {r for sc in SCENES for st in sc.steps for r in st.refs} | {t[1] for t in EXAM_TOPICS.values()} \
    | {t[1] for t in SYLLABUS.values()} | {t[1] for t in ELEMENTS.values()} | {'info'}
REFS = {k: r for k, r in REFS.items() if k in _used}

VIDEO = Video(
    id='PHY415115_C6_electromagnetism',
    course=COURSE, course_name='Physics', module=MODULE,
    module_name='Criterion 6: Identify and apply principles and theories of electricity and magnetism',
    title='Criterion 6: electricity and magnetism, complete revision',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Electrostatics, Magnetism, Induction'),
    checks=CHECKS,
    thumbnail=V.thumbnail,
    allowed_overlaps=['identify and apply principles and theories of electricity and magnetism'],
    keywords=['electric field', 'field strength', 'potential difference', 'Coulomb', 'Faraday cage', 'electron gun', 'Millikan',
              'magnetic field', 'flux density', 'right hand rule', 'velocity filter', 'mass spectrometer', 'commutator', 'helix',
              'emf', 'induction', 'induced', 'Lenz', 'eddy current', 'generator', 'transformer', 'tesla', 'angle of dip'],
    description=('A complete revision explainer for TASC Physics (PHY415115) Criterion 6: electricity and magnetism, covering '
                 'electrostatics, electric fields and potential, magnetic fields and forces, and induction. For class tests and the '
                 'end-of-year exam (Section B). Formulas from the TASC information sheet are labelled on screen.'),
)
