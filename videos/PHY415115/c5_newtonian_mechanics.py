"""PHY415115 Physics, Criterion 5: Identify and apply principles of Newtonian mechanics including gravitational fields.

Build with:
    uv run python -m explainer check   videos/PHY415115/c5_newtonian_mechanics.py
    uv run python -m explainer preview videos/PHY415115/c5_newtonian_mechanics.py
    uv run python -m explainer thumbnail videos/PHY415115/c5_newtonian_mechanics.py
    uv run python -m explainer render  videos/PHY415115/c5_newtonian_mechanics.py    # operator only: narration, video, docs
"""
import math

from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, InfoSheet, import_sibling

COURSE, MODULE = 'PHY415115', 'C5'
L.use(style.theme(COURSE, MODULE))
V = import_sibling(__file__, 'c5_visuals.py')

P0 = 'Criterion 5 · Overview'
P1 = 'Part 1 · Describing motion'
P2 = 'Part 2 · Projectile motion'
P3 = 'Part 3 · Forces and Newton’s laws'
P4 = 'Part 4 · Momentum and impulse'
P5 = 'Part 5 · Circular motion'
P6 = 'Part 6 · Work, energy and power'
P7 = 'Part 7 · Gravity, fields and orbits'
P8 = 'Finish · Tests & exam technique'

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
    2018: {1: '4-5', 2: '6-7', 3: 8, 4: 9, 5: '10-11', 6: '12-13'},
    2019: {1: 3, 2: 4, 3: 5, 4: '6-7', 5: '8-9', 6: 10},
    2020: {1: 3, 2: 4, 3: 5, 4: '6-7', 5: '8-9', 6: 10},
    2021: {1: 4, 2: 5, 3: 6, 4: '7-8', 5: 9, 6: 10},
    2022: {1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: '8-9'},
    2023: {1: 4, 2: 5, 3: '6-7', 4: '8-9', 5: '10-11', 6: 12},
    2024: {1: '4-5', 2: '6-7', 3: 8, 4: 9, 5: 10, 6: 11},
    2025: {1: 3, 2: '4-5', 3: '6-7', 4: '8-9', 5: '10-11'},
}
REPORT_PAGES = {
    2018: {1: 1, 2: '1-2', 3: 2, 4: 2, 5: 2, 6: '2-3'},
    2019: {1: '1, 8', 2: '1, 8-9', 3: '1, 9', 4: '2, 10', 5: '2, 10', 6: '2-3, 10-11'},
    2020: {1: '1, 7', 2: '1, 7', 3: '1-2, 7-8', 4: '2, 8', 5: '2, 8', 6: '3, 9'},
    2021: {1: '1-2', 2: 2, 3: '2-3', 4: '3-4', 5: 4, 6: '4-5'},
    2022: {1: '1-2', 2: '3-4', 3: '4-6', 4: '6-7', 5: '7-9', 6: 9},
    2023: {1: '1-2', 2: '2-3', 3: '3-4', 4: '5-6', 5: '6-7', 6: '7-8'},
    2024: {1: '1-3', 2: '3-5', 3: 5, 4: '6-7', 5: '7-8', 6: '8-9'},
    2025: {1: '2, 16', 2: '2-3', 3: 3, 4: '4, 21-22', 5: 4},
}


def exam(y, q):
    name = EXAM_FILES.get(y, f'PHY415115-Physics-TASC-Exam-Paper-{y}.pdf')
    section = 'Part 1' if y <= 2021 else 'Section A'
    return Ref(name, f'{y} exam, {section}, Question {q}', EXAM_PAGES[y][q])


def report(y, q):
    name = REPORT_FILES.get(y, f'PHY415115-Physics-Assessment-Report-{y}.pdf')
    return Ref(name, f'{y} assessment report, Criterion 5, Question {q}', REPORT_PAGES[y][q])


REFS = {
    'standards': Ref(COURSE_DOC, 'Course document, Criterion 5 standards (element table)'),
    'content': Ref(COURSE_DOC, 'Course document, Science Understanding: Newtonian mechanics including gravitational fields (Criterion 5)'),
    'appendix': Ref(COURSE_DOC, 'Course document, Appendix 1: examples in context for C5 & C4'),
    'info': Ref(INFO, 'Information sheet, Motion, Work and Gravity sections', page=1),
    'spec': Ref(SPEC, 'External assessment specifications, Section A and Appendix A', page='2, 5-8'),
}
for _y, _qs in EXAM_PAGES.items():
    for _q in _qs:
        REFS[f'ex{_y % 100}q{_q}'] = exam(_y, _q)
for _y, _qs in REPORT_PAGES.items():
    for _q in _qs:
        REFS[f'ar{_y % 100}q{_q}'] = report(_y, _q)


def X(*codes):
    """Refs for past questions and their reports: X('23q2', '18q1') -> exam and report refs for each."""
    return [f'{k}{c}' for c in codes for k in ('ex', 'ar')]


# --------------------------------------------------------------------------- coverage targets
# Every dot point of the course content for this criterion.  check fails if one is uncovered.
SYLLABUS = {
    'M1': ('Displacement and distance: solve displacement problems to any angled analysis', 'content'),
    'M2': ('Speed and average velocity: average speed = total distance / total time; average velocity = total displacement / total time', 'content'),
    'M3': ('Acceleration: a = Δv/Δt = (v − u)/Δt', 'content'),
    'M4': ('Construct and interpret constant acceleration cases of s-t, v-t and a-t graphs', 'content'),
    'M5': ('Construct v-t and a-t graphs using data from the slopes of s-t and v-t graphs', 'content'),
    'M6': ('Calculate displacement and/or distance from a v-t graph', 'content'),
    'M7': ('Equations of motion for constant straight-line acceleration: v = u + at, s = ut + ½at², v² = u² + 2as', 'content'),
    'M8': ('Vertical motion under gravity (a_g = 9.81 m s⁻²)', 'content'),
    'M9': ('Understand terminal velocity', 'content'),
    'M10': ('Projectiles: vertical and horizontal components of velocity (and hence velocity) at any point of the path', 'content'),
    'M11': ('Projectiles: time of flight', 'content'),
    'M12': ('Projectiles: horizontal and vertical displacement', 'content'),
    'M13': ('Projectiles: projection and landing at different levels and/or heights', 'content'),
    'P1': ('Momentum p = mv', 'content'),
    'P2': ('Conservation of momentum in one dimension: Σp_i = Σp_f', 'content'),
    'P3': ('Conservation of momentum in two dimensions at any angle', 'content'),
    'P4': ('Conservation of momentum in collision and explosion formats', 'content'),
    'N1': ('Identify forces in a free body diagram', 'content'),
    'N2': ('Identify balanced and unbalanced forces in two dimensions, including inclined slopes', 'content'),
    'N3': ('Many-force situations (up to four forces)', 'content'),
    'N4': ('Apply and illustrate Newton’s First Law', 'content'),
    'N5': ('Apply Newton’s Second Law to numerical and non-numerical problems, including weight problems and motion problems', 'content'),
    'N6': ('F_unbalanced = ma = m(v − u)/Δt = Δp/Δt', 'content'),
    'N7': ('Newton’s Second Law when velocity changes and in simple mass change situations, e.g. ion drives, water from a hose', 'content'),
    'N8': ('Apply and illustrate Newton’s Third Law', 'content'),
    'N9': ('Relate forces and momentum together in force-time graphs and momentum-time graphs', 'content'),
    'N10': ('Two-dimensional momentum changes and forces', 'content'),
    'C1': ('Circular motion: tangential speed and velocity, v = 2πr/T', 'content'),
    'C2': ('Centripetal acceleration and force as changes in velocity and momentum in time: F_c = mv²/r, a_c = v²/r', 'content'),
    'C3': ('Application to horizontal circular motion', 'content'),
    'E1': ('Work done as the area under force-distance graphs', 'content'),
    'E2': ('Work done when force and displacement are not colinear: WD = Fs cos θ', 'content'),
    'E3': ('Gravitational potential energy E_p = mgΔh', 'content'),
    'E4': ('Kinetic energy E_k = ½mv²', 'content'),
    'E5': ('Conservation of energy applied to numerical problems', 'content'),
    'E6': ('Determine whether a situation is elastic or inelastic from E_k calculations', 'content'),
    'E7': ('Power applied to numerical problems: P = ΔE/t = W/t', 'content'),
    'G1': ('Universal Law of Gravitation, F_g = GM₁M₂/r², and the value of G', 'content'),
    'G2': ('Weight as the gravitational force on a body, F_g = mg', 'content'),
    'G3': ('Masses produce a gravitational field; field theory attributes the force to the field', 'content'),
    'G4': ('Gravitational field strength defined as g = F_g/m', 'content'),
    'G5': ('Qualitative description of fields', 'content'),
    'G6': ('Gravitational field strength near a single mass, g = GM/r²', 'content'),
    'G7': ('Sum of two individual gravitational field strengths in two dimensions', 'content'),
    'G8': ('Sketch qualitative gravitational fields around single and double masses', 'content'),
    'G9': ('Kepler’s Third Law in Newtonian form, T² = 4π²r³/GM', 'content'),
    'G10': ('Kepler’s Third Law in ratio form, (T₁/T₂)² = (r₁/r₂)³', 'content'),
    'G11': ('Circular orbiting satellites, including geosynchronous (geostationary) satellites', 'content'),
    'G12': ('‘Weightlessness’ as a sensation when only gravity is operating on a body', 'content'),
    'K1': ('Context: forensic science, projectiles and ballistics', 'appendix'),
    'K2': ('Context: artificial satellites', 'appendix'),
    'K3': ('Context: developing understanding of planetary motion', 'appendix'),
}

# Elements numbered by row order in the standards table (Element 1 = first row).
ELEMENTS = {
    1: ('Identifies, describes and explains fundamental principles', 'standards'),
    2: ('Selects, applies and manipulates formulae to solve numerical problems (straightforward → complex, analysing validity)', 'standards'),
    3: ('Interprets and analyses data in graphical and tabular form', 'standards'),
    4: ('Interprets problems and makes predictions in real-world contexts', 'standards'),
}

# What past Criterion 5 questions examined (in our own words).  Never copy question text.
EXAM_TOPICS = {
    'X18-1': ('Two bows: comparing force-draw graphs, work done as an area, arrow speed from stored energy', 'ex18q1'),
    'X18-2': ('Billiard-style collision: momentum diagram, elastic test, separation angle', 'ex18q2'),
    'X18-3': ('Mortar projectile: components, greatest height, range to a target on higher ground', 'ex18q3'),
    'X18-4': ('Rally car on a slope: kinetic energy, potential energy gained, mechanical losses from engine power', 'ex18q4'),
    'X18-5': ('Jupiter’s moons: linearising period-radius data, graph through the origin, slope gives the mass', 'ex18q5'),
    'X18-6': ('Asteroid Ceres: surface field, equator speed, centripetal acceleration, apparent weight at the equator', 'ex18q6'),
    'X19-1': ('Block pulled up a rough ramp at constant speed: friction, work each second', 'ex19q1'),
    'X19-2': ('Charm in an accelerating then turning car: forces, acceleration from the angle, radius of the turn', 'ex19q2'),
    'X19-3': ('Gravity force-distance data: linearising against 1/r², graph, gradient gives G', 'ex19q3'),
    'X19-4': ('Planetary slingshot: momentum-change diagram, magnitude, average force, planet’s reaction, slowing a probe', 'ex19q4'),
    'X19-5': ('Star orbiting a hidden central mass: orbital speed, central mass, number of suns, what the object may be', 'ex19q5'),
    'X19-6': ('Golf shot on Earth and on the Moon: flight time, range, comparison', 'ex19q6'),
    'X20-1': ('Lift and bathroom scales: forces, weight versus reading, acceleration of the lift', 'ex20q1'),
    'X20-2': ('Wind turbine: mass of an air cylinder per second, its kinetic energy, power from the loss of speed', 'ex20q2'),
    'X20-3': ('Cricket bat hit: change-of-momentum diagram, magnitude, force, direction relative to initial motion', 'ex20q3'),
    'X20-4': ('Swinging egg then free fall: speed by energy conservation, fall time, range formula, effect of the Moon', 'ex20q4'),
    'X20-5': ('Asteroid and probe: Kepler ratio, orbital speed round a small body, surface field, equator speed and apparent gravity', 'ex20q5'),
    'X20-6': ('Person sliding down a muddy slope: forces to scale, normal and friction components, motion when friction drops', 'ex20q6'),
    'X21-1': ('Ball bouncing off the ground: vector diagram of the change in momentum, magnitude, force', 'ex21q1'),
    'X21-2': ('Golf on Mars: components, flight time, range, why the range is greater', 'ex21q2'),
    'X21-3': ('Deriving conservation of momentum from Newton’s second and third laws', 'ex21q3'),
    'X21-4': ('Helicopter on Mars: minimum force from weight, mass of air per second, power to the air, energy and efficiency', 'ex21q4'),
    'X21-5': ('Moon and falling apple: centripetal acceleration of the Moon, inverse-square check, mass of Earth', 'ex21q5'),
    'X21-6': ('Earth-Moon system: total field at a point between them, sketch of the field', 'ex21q6'),
    'X22-1': ('Sliding down a rope: forces, minimum acceleration to avoid breaking the rope, speed at the ground', 'ex22q1'),
    'X22-2': ('Billiard balls separating at 90°: vector diagram, second ball’s speed and angle, elastic or not', 'ex22q2'),
    'X22-3': ('Aircraft banking in a horizontal circle: why vertical forces balance, forces, unbalanced force, radius', 'ex22q3'),
    'X22-4': ('Asteroid Elektra and its moon: Kepler ratio for the orbit radius, moon’s acceleration, field, mass', 'ex22q4'),
    'X22-5': ('Truck up a hill at constant speed: forces, potential energy per second, work against resistance per second, percentage of power', 'ex22q5'),
    'X22-6': ('Comet near Jupiter: relative field strengths across the comet, why it breaks up, shape in orbit', 'ex22q6'),
    'X23-1': ('Arrow fired at a target: components, vertical miss distance', 'ex23q1'),
    'X23-2': ('Bow force graph: stored energy as an area, arrow speed with an efficiency', 'ex23q2'),
    'X23-3': ('Spinning Earth: why it bulges, field at equator versus poles, centripetal acceleration, force of the ground on a person', 'ex23q3'),
    'X23-4': ('Bullet bouncing off a plate: vector diagram, magnitude, angle, force on the plate and Newton’s third law', 'ex23q4'),
    'X23-5': ('Pellet into hanging plasticine: shared speed, loss of kinetic energy, average force, swing height', 'ex23q5'),
    'X23-6': ('Exoplanets: orbital radius from period, comment on habitability, ratio-form period', 'ex23q6'),
    'X24-1': ('Child swung in a circle: forces, force from the parent, net force, tangential speed, period', 'ex24q1'),
    'X24-2': ('Cart on an incline with friction: friction as part of the weight, acceleration with a vector diagram, maximum distance, velocity-time graph up and down', 'ex24q2'),
    'X24-3': ('Neutron star: surface field from the diameter, orbital period of a planet', 'ex24q3'),
    'X24-4': ('Cricket six: deriving horizontal and vertical component equations, initial speed', 'ex24q4'),
    'X24-5': ('Players colliding and tangling: total momentum with a vector diagram, final velocity', 'ex24q5'),
    'X24-6': ('Rocket lift-off: forces to scale, thrust from mass and acceleration, mass later with the same thrust', 'ex24q6'),
    'X25-1': ('Mountain-bike stream jump: components from a downward ramp, does the rider clear the gap', 'ex25q1'),
    'X25-2': ('Hockey ball struck: change of momentum from force and time, vector triangle, final speed, deflection angle', 'ex25q2'),
    'X25-3': ('Apple and Moon: orbital speed, centripetal acceleration, inverse-square demonstration, acceleration at a space station', 'ex25q3'),
    'X25-4': ('Two stars: field from each at a point, total field, zero-field point, field sketch', 'ex25q4'),
    'X25-5': ('Hovering helicopter: air volume and mass per second, change in momentum, helicopter mass, fraction of power', 'ex25q5'),
}

# --------------------------------------------------------------------------- scenes
S = Step
SCENES = [
Scene('title', P0, 'Welcome', V.title_card, [
    S("Welcome. This video is a complete briefing on Criterion 5 of TASC Physics, PHY415115: Newtonian mechanics, including "
      "gravitational fields. Use it to revise for your class tests and for Section A of the end of year exam. By the end, you "
      "should know every part of this content, which formulas are on your information sheet and which you must learn, and the "
      "traps that markers keep seeing in student answers.", refs=['standards'], anim=4),
]),
Scene('intro', P0, 'How Criterion 5 is assessed', V.overview, [
    S("Criterion 5 is assessed in two ways. Your teacher assesses it during the year, through class tests, practical work and "
      "other tasks. It's also assessed externally, in Section A of the end of year exam: about forty five minutes, forty five "
      "marks, and between five and seven compulsory questions. You can use the TASC information sheet and an approved calculator.",
      refs=['standards', 'spec']),
    S("The criterion has four elements, numbered in the order of the standards table. Element one is identifying, describing and "
      "explaining the principles. Element two is solving numerical problems. Element three is working with data in graphs and "
      "tables. Element four is interpreting problems and predicting, including in unfamiliar, real world contexts. A tag in the "
      "corner shows which element an example practises.", refs=['standards'], elements=[1, 2, 3, 4]),
    S("The standards step up from C to A. At C level you identify principles, solve straightforward problems, interpret data and "
      "predict in familiar contexts. At B, you describe, solve problems with several steps, and analyse data. At A, you explain; "
      "you solve complex problems and check whether the answer is valid; you evaluate data; and you make reasoned predictions in "
      "unfamiliar contexts. So we'll focus on why, not just on formulas.", refs=['standards'], elements=[1, 2, 3, 4]),
    S("Here's the roadmap. Part one: describing motion. Part two: projectiles. Part three: forces and Newton's laws. Part four: "
      "momentum and impulse. Part five: circular motion. Part six: work, energy and power. Part seven: gravity, fields and orbits. "
      "Then we finish with technique. This is the most numerical criterion, so we'll work through many examples. Let's begin."),
]),
# ------------------------------------------------------------------- part 1: describing motion
Scene('motion', P1, 'Displacement, velocity and acceleration', V.motion, [
    S("Part one. Distance is the length of the path. Displacement is the straight line change in position, with a "
      "direction. Average speed is distance over time; average velocity is displacement over time. Walk three "
      "kilometres east, then four north, in two hours. The distance is seven kilometres, so the speed is three point "
      "five kilometres per hour. The displacement is five kilometres at fifty three degrees north of east, so the "
      "velocity is two point five kilometres per hour that way. Learn these: they're not on the sheet.",
      refs=['content'], covers=['M1', 'M2'], elements=[1, 2],
      problem='A hiker walks 3.0 km east then 4.0 km north in 2.0 h. What are the distance, displacement, average speed and average velocity?'),
    S("Acceleration is the change in velocity per second: a equals delta v over delta t, which is v minus u over delta t. It's a "
      "vector, so slowing down is negative acceleration. Velocity can change in size, in direction, or both, and any change means "
      "acceleration. The unit is metres per second squared. This one isn't printed on the sheet either.",
      refs=['content'], covers=['M3'], elements=[1]),
    S("Displacements at any angle: resolve into components, or draw them head to tail and use the cosine rule, on your information "
      "sheet in the trigonometry identities section. Take a five kilometre leg, then an eight kilometre leg turned sixty degrees. "
      "The angle inside the triangle is one hundred and twenty degrees, giving eleven point four kilometres. Components agree: "
      "nine point zero east, six point nine three north. Use the inside angle, not the turn.",
      refs=['content', 'info'], covers=['M1'], elements=[2],
      problem='A walker goes 5.0 km, then turns 60° and goes 8.0 km. What is the size of the total displacement?'),
]),
Scene('graphs', P1, 'Motion graphs', V.graphs, [
    S("Motion graphs tell one story three ways. For constant acceleration from rest, the displacement time graph is a curve "
      "that gets steeper, the velocity time graph is a straight line, and the acceleration time graph is flat. The velocity "
      "graph is the one you'll use most.",
      refs=['content'], covers=['M4'], elements=[1, 3]),
    S("Each graph links to the next. The gradient of a displacement graph is velocity, and the gradient of a velocity graph is "
      "acceleration. Going the other way, the area between a velocity graph and the axis is displacement, and the area under an "
      "acceleration graph is the change in velocity. So you can build a velocity graph from the slopes of a displacement graph, "
      "and an acceleration graph from the slopes of a velocity graph.",
      refs=['content', 'ar24q2', 'ex24q2'], covers=['M4', 'M5', 'M6'], elements=[1, 3], exam=['X24-2']),
    S("Take care with areas. Area below the time axis is displacement the other way, so it subtracts from displacement but adds "
      "to distance. When you sketch, use ruled straight lines, label axes with units, and mark intercepts and turning points. "
      "Examiners report sketches showing only the way up, a mirror image on the way down, or curves. A return trip can have a "
      "different acceleration.",
      refs=['ar24q2', 'ex24q2', 'ar23q2'], covers=['M6', 'M4'], elements=[3], exam=['X24-2']),
]),
Scene('we_graph', P1, 'Worked example: reading a journey', V.we_graph, [
    S("Element three. A van speeds up uniformly from rest to twenty metres per second in eight seconds, travels at that speed for "
      "ten seconds, then brakes uniformly to rest in five. The displacement is the area under the velocity graph: a triangle of "
      "eighty metres, a rectangle of two hundred, and a triangle of fifty. The total is three hundred and thirty metres.",
      refs=['content'], covers=['M6', 'M4'], elements=[2, 3],
      problem='A van accelerates from rest to 20.0 m/s in 8.00 s, holds it for 10.0 s, then brakes to rest in 5.00 s. What is its displacement?'),
    S("The average velocity is the displacement over the whole twenty three seconds: fourteen point three metres per second. "
      "It's not halfway between zero and twenty, because most of the time was spent at full speed.",
      refs=['content'], covers=['M2', 'M6'], elements=[2, 3],
      problem='What is the van’s average velocity over the whole 23.0 s?'),
    S("Now build the other graphs from the slopes. The gradient is two point five metres per second squared at first, zero in the "
      "middle, and minus four point zero at the end, as the van slows. The displacement graph curves up, runs straight, then "
      "flattens to a stop. Check that the pieces join without jumps.",
      refs=['content'], covers=['M5', 'M3'], elements=[3],
      problem='From the same journey, find the acceleration in each section and sketch the a-t and s-t graphs.'),
]),
Scene('suvat', P1, 'Equations of motion', V.suvat, [
    S("For constant acceleration in a straight line there are three equations of motion, on your information sheet in the motion "
      "in a straight line section: v equals u plus a t; s equals u t plus a half a t squared; and two a s equals v squared minus "
      "u squared. Here u is the starting velocity, v the final velocity, a the acceleration, s the displacement and t the time. "
      "They only work for constant acceleration.",
      refs=['content', 'info'], covers=['M7'], elements=[1, 2]),
    S("To choose, list what you know and want, and pick the equation with exactly those quantities. No final velocity: use the "
      "second. No time: use the third. Choose a positive direction first, and give every vector its sign from it. Convert units "
      "before substituting: kilometres per hour divided by three point six gives metres per second. Reports from many years name "
      "that conversion as a common slip.",
      refs=['content', 'ar18q4', 'ar19q6', 'ar25q1'], covers=['M7'], elements=[2], exam=['X18-4', 'X19-6', 'X25-1']),
    S("Vertical motion under gravity is this case, with a equal to minus nine point eight one if up is positive. That value is on "
      "your information sheet in the gravity section. A ball thrown up stops at the top and returns with its launch speed, taking "
      "as long to fall as to rise, ignoring air. At the top, the velocity is zero but the acceleration is still g.",
      refs=['content', 'info', 'ar25q1'], covers=['M8', 'M7'], elements=[1, 2], exam=['X25-1']),
]),
Scene('we_vertical', P1, 'Worked example: a stone thrown upward', V.we_vertical, [
    S("Element two. A stone is thrown up at twelve point zero metres per second from a bridge thirty point zero metres "
      "above a river. Up is positive: u is plus twelve, a is minus nine point eight one, and s is minus thirty. No time "
      "is given, so use v squared equals u squared plus two a s: seven hundred and thirty two point six. So the speed "
      "is twenty seven point one metres per second.",
      refs=['content'], covers=['M7', 'M8'], elements=[2],
      problem='A stone is thrown up at 12.0 m/s from a bridge 30.0 m above a river. What is its speed when it hits the water?'),
    S("For the time, use v equals u plus a t: minus twenty seven point zero seven, minus twelve, over minus nine point eight one. "
      "That's three point nine eight seconds. The minus signs cancel. Keep your signs consistent.",
      refs=['content'], covers=['M7', 'M8'], elements=[2],
      problem='How long after it is thrown does the stone reach the river?'),
    S("Check validity, as an A response should. The stone rises for one point two two seconds, to seven point three four metres "
      "above the bridge. It then falls thirty seven point three metres in two point seven six seconds, and a half g t squared "
      "gives thirty seven point three. The halves agree.",
      refs=['content'], covers=['M8'], elements=[2, 4],
      problem='Check the answer by splitting the stone’s flight into the rise and the fall.'),
]),
Scene('terminal', P1, 'Terminal velocity', V.terminal, [
    S("Terminal velocity is what really happens when something falls through air. Weight stays the same, but air resistance grows "
      "with speed, so the net force and the acceleration fall. When the air resistance equals the weight, the forces balance, the "
      "acceleration is zero and the speed stops changing. That constant speed is the terminal velocity. It's the acceleration "
      "that reaches zero, not the speed.",
      refs=['content'], covers=['M9', 'N4'], elements=[1], anim=3),
    S("Now predict. A skydiver opens a parachute. The air resistance suddenly exceeds the weight, so the net force points up "
      "and the skydiver slows down. As the speed falls, so does the resistance, until the forces balance again at a new, much "
      "smaller terminal velocity. The same idea explains why real bullets fall short of the ideal path.",
      refs=['content', 'appendix'], covers=['M9', 'K1'], elements=[4], anim=3,
      problem='A skydiver at terminal velocity opens a parachute. Describe and explain the motion that follows.'),
]),
# ------------------------------------------------------------------- part 2: projectiles
Scene('projectile', P2, 'Projectile motion', V.projectile, [
    S("Part two. A projectile moves under gravity alone, so split its motion into two independent parts. Horizontally there's no "
      "force, so the velocity is constant. Vertically the acceleration is g, downward. The only thing the parts share is time. "
      "Watch the shadows: the horizontal one moves steadily, and the vertical one rises and falls.",
      refs=['content', 'info'], covers=['M10', 'M11', 'M12'], elements=[1], anim=3),
    S("Launch at speed u, angle theta above the horizontal. The horizontal component is u cosine theta, and the vertical component "
      "is u sine theta. Later, the horizontal velocity is unchanged, and the vertical velocity is u sine theta minus g t. Combine "
      "them with Pythagoras and the tangent to get the speed and direction at any point. At the top the vertical velocity is zero, "
      "so the speed is the horizontal component.",
      refs=['content', 'ex23q1', 'ar23q1'], covers=['M10'], elements=[1, 2], exam=['X23-1']),
    S("Landing at the launch height, the time of flight is twice the time to the top: two u sine theta over g. The range is "
      "the horizontal velocity times that time. These shortcuts aren't on the sheet, so learn them or derive them from the "
      "equations of motion. If it lands at a different height, use the full equations instead.",
      refs=['content', 'ex18q3', 'ar18q3'], covers=['M11', 'M12'], elements=[1, 2], exam=['X18-3']),
]),
Scene('we_proj', P2, 'Worked example: a kicked rugby ball', V.we_proj, [
    S("Element two. A rugby ball is kicked at seventy nine point two kilometres per hour, thirty five degrees above the horizontal, "
      "over level ground. Dividing by three point six gives twenty two point zero metres per second. The horizontal component is "
      "twenty two cosine thirty five: eighteen point zero. The vertical component is twenty two sine thirty five: twelve point six.",
      refs=['content', 'ex19q6', 'ar19q6', 'ex21q2', 'ar21q2'], covers=['M10', 'M7'], elements=[2], exam=['X19-6', 'X21-2'],
      problem='A rugby ball is kicked at 79.2 km/h, 35.0° above the horizontal, over level ground. What are its horizontal and vertical velocity components?'),
    S("The time of flight is two times twelve point six one nine, over nine point eight one: two point five seven seconds. The "
      "range is the horizontal velocity times the time: forty six point four metres. We used unrounded components and rounded "
      "only at the end.",
      refs=['ar19q6', 'ar21q2'], covers=['M11', 'M12'], elements=[2], exam=['X19-6', 'X21-2'],
      problem='For the same kick, what are the time of flight and the range?'),
    S("The greatest height uses v squared equals u squared plus two a s, with v zero at the top: eight point one two metres. "
      "Check validity: at the top the ball still moves at eighteen point zero metres per second, the horizontal component. And "
      "it lands at twenty two point zero, its launch speed, thirty five degrees below the horizontal.",
      refs=['ex18q3', 'ar18q3'], covers=['M10', 'M12'], elements=[2, 4], exam=['X18-3'],
      problem='What is the greatest height reached by the ball, and what is its speed at the top of its flight?'),
]),
Scene('proj_levels', P2, 'Landing at a different height', V.proj_levels, [
    S("When a projectile lands at a different height, the shortcuts fail, so use the equations with signs. A ball is thrown at "
      "fifteen point zero metres per second, forty degrees above the horizontal, from a cliff twelve point zero metres above the "
      "sea. The components are eleven point five horizontally and nine point six four vertically. If a launch is below the "
      "horizontal, the vertical component is negative.",
      refs=['content', 'ex18q3', 'ar18q3', 'ex25q1', 'ar25q1'], covers=['M13', 'M10'], elements=[2], exam=['X18-3', 'X25-1'],
      problem='A ball is thrown at 15.0 m/s, 40.0° above the horizontal, from a cliff 12.0 m above the sea. What are its velocity components at launch?'),
    S("For the time, the report says the easier route is the rise and the fall separately, because the quadratic caused many "
      "errors. The rise takes zero point nine eight three seconds, to four point seven four metres above the cliff. The fall is "
      "from sixteen point seven metres, taking one point eight five seconds. The total is two point eight three seconds. The "
      "quadratic gives the same.",
      refs=['ar18q3', 'ex18q3'], covers=['M13', 'M11'], elements=[2], exam=['X18-3'],
      problem='How long is the ball in the air, and what range does it reach?'),
    S("The range is eleven point five times two point eight three: thirty two point five metres. On landing, the vertical velocity "
      "is minus eighteen point one, so the speed is twenty one point five metres per second, fifty seven point six degrees below "
      "the horizontal. Check by energy: the root of fifteen squared plus two g times twelve is also twenty one point five.",
      refs=['content'], covers=['M13', 'M10', 'M12'], elements=[2, 4],
      problem='With what speed and at what angle does the ball hit the sea?'),
]),
Scene('proj_derive', P2, 'Deriving and comparing projectile results', V.proj_derive, [
    S("Some questions ask you to derive a result. Horizontally, u cosine theta equals the range over the time. Vertically, u sine "
      "theta equals g over two times the time. Eliminate the time. For a ninety metre range at thirty degrees, u squared is one "
      "thousand and nineteen, so u is thirty one point nine metres per second. Success came from equating two expressions for "
      "the same component.",
      refs=['ex24q4', 'ar24q4'], covers=['M11', 'M12', 'M10'], elements=[1, 2], exam=['X24-4'],
      problem='A ball is hit over level ground and lands 90.0 m away; it was struck at 30.0°. Show that u cos30° = 90.0/t and u sin30° = 4.905t, then find u.'),
    S("Another derivation. A ball rolls down a smooth curve through a drop D, then leaves a table edge horizontally at height "
      "h. Energy gives v equals the root of two g D. The fall time is the root of two h over g. Multiply: the distance is two "
      "times the root of D h. There's no g in it, so it's the same on the Moon. Both v and t depend on g, but the effects cancel.",
      refs=['ex20q4', 'ar20q4'], covers=['M12', 'M11', 'E5'], elements=[1, 2, 4], exam=['X20-4'],
      problem='A ball rolls down a smooth curve of vertical drop D then leaves a table at height h. Show that it lands 2√(Dh) away, and say what happens on the Moon.'),
    S("Now compare places. With the same speed and angle, the time of flight and the range are proportional to one over g. Mars "
      "has g of three point seven two, so the range is two point six four times Earth's. Explain: weaker gravity changes the "
      "vertical velocity more slowly, so the object stays up longer, while the horizontal velocity is unchanged. A bare ratio "
      "is only a partial answer.",
      refs=['ex19q6', 'ar19q6', 'ex21q2', 'ar21q2'], covers=['M11', 'M12'], elements=[4], exam=['X19-6', 'X21-2'],
      problem='The same golf shot is hit on Mars, where g is 3.72 m/s². Compare its range with that on Earth, and explain why.'),
]),
# ------------------------------------------------------------------- part 3: forces
Scene('forces', P3, 'Free body diagrams and Newton’s first law', V.forces, [
    S("Part three. A free body diagram shows one object and an arrow for every force acting on it. Draw each arrow from "
      "the object, label it, such as weight, normal force, tension, friction or drag, and make lengths roughly to "
      "scale, so balanced forces look balanced. Markers deduct when arrows are out of scale, point the wrong way or are "
      "repeated, and when a net or centripetal force is added as an extra arrow.",
      refs=['content', 'ar22q1', 'ar24q1', 'ar24q6', 'ex22q1', 'ex24q6'], covers=['N1'], elements=[1], exam=['X22-1', 'X24-1', 'X24-6'],
      problem='Draw and label the forces on a rocket during lift-off, showing their relative sizes.'),
    S("Newton's first law: an object keeps its velocity, at rest or constant, unless an unbalanced force acts. So balanced forces "
      "mean zero acceleration, not zero velocity. In two dimensions, balance each direction separately. In an explanation, name "
      "the law and apply it to the object. Writing that things in motion stay in motion isn't enough.",
      refs=['content', 'ar22q3', 'ex22q3'], covers=['N4', 'N2'], elements=[1], exam=['X22-3'],
      problem='An aircraft turns in a horizontal circle. Use Newton’s laws to justify that its vertical forces add to zero.'),
    S("With three or four forces, take care. A crate pulled up a rough slope by a rope has weight, straight down; the normal "
      "force, at right angles to the slope; friction, along the slope against the motion; and tension, along the rope. At "
      "constant velocity, the forces along the slope balance, and so do those across it.",
      refs=['content', 'ar20q6', 'ar22q5', 'ex20q6', 'ex22q5'], covers=['N3', 'N2', 'N1'], elements=[1, 2], exam=['X20-6', 'X22-5']),
]),
Scene('incline', P3, 'Forces on a slope', V.incline, [
    S("On a slope of angle theta, split the weight in two. The part along the slope is m g sine theta, and the part "
      "into the slope is m g cosine theta. The contact force has two components: the normal force, balancing the part "
      "into the slope, and friction, along it. Reports link untidy diagrams to the wrong trigonometric ratio, so sketch "
      "the triangle.",
      refs=['content', 'ar24q2', 'ex24q2', 'ar20q6', 'ex20q6'], covers=['N2', 'N3'], elements=[1, 2], exam=['X24-2', 'X20-6']),
    S("A quick check: on a flat slope, the part along it must be zero, which is sine of zero. On a vertical slope, the "
      "whole weight acts along it. Then remember friction opposes sliding. Up the slope, friction and the weight "
      "component both slow a cart. Down the slope, friction points up it, so the net force is smaller. The report says "
      "many failed to include friction properly, and drew the way down as a mirror image of the way up.",
      refs=['ar24q2', 'ex24q2', 'ar19q1', 'ex19q1'], covers=['N2', 'N5'], elements=[1, 2], exam=['X24-2', 'X19-1']),
]),
Scene('we_incline', P3, 'Worked example: a crate on a slope', V.we_incline, [
    S("Element two. A crate of eight point five zero kilograms is pulled up a thirty degree slope at constant speed by a rope "
      "pulling sixty point zero newtons along the slope. Forces along the slope balance. The weight component is forty one point "
      "seven newtons, so friction is sixty minus forty one point seven: eighteen point three newtons, down the slope.",
      refs=['ex19q1', 'ar19q1', 'ex22q5'], covers=['N2', 'N3', 'N4'], elements=[2], exam=['X19-1'],
      problem='A crate of 8.50 kg is pulled up a 30.0° slope at constant speed by a 60.0 N rope along the slope. What is the friction force?'),
    S("Now cut the rope while the crate moves up at two point four zero metres per second. Friction and the weight component both "
      "act down the slope: sixty newtons, so a deceleration of seven point zero six metres per second squared. From v squared "
      "equals u squared plus two a s with v zero, it slides zero point four zero eight metres further.",
      refs=['ar24q2', 'ex24q2'], covers=['N5', 'M7'], elements=[2], exam=['X24-2'],
      problem='The rope is cut when the crate is moving up at 2.40 m/s. How far up the slope does it go?'),
    S("Coming back down, friction reverses, so the acceleration is smaller: forty one point seven minus eighteen point three, over "
      "eight point five, is two point seven five. It returns at one point five zero metres per second. The velocity graph has two "
      "straight lines with different gradients. The return speed is below the launch speed, as it must be, because friction "
      "removed energy.",
      refs=['ar24q2', 'ex24q2'], covers=['N5', 'M4', 'M5'], elements=[2, 3, 4], exam=['X24-2'],
      problem='Sketch the velocity-time graph for the crate from the cut until it returns to the cut point, and find its return speed.'),
]),
Scene('newton2', P3, 'Newton’s second law', V.newton2, [
    S("Newton's second law: the net force equals mass times acceleration. On your information sheet, in the motion, momentum and "
      "force section, it's F net equals delta m v over delta t, equals m a. The net force is the vector sum of all the forces, "
      "and the acceleration points the same way. Weight is F g equals m g, in the gravity section, with g equal to nine point eight "
      "one newtons per kilogram. Convert tonnes to kilograms first.",
      refs=['content', 'info'], covers=['N5', 'N6', 'G2'], elements=[1, 2]),
    S("The momentum form is more general: force is the change in momentum per second. With constant mass, that's m times v minus u, "
      "over t, the same as m a. For explanations, use the relationship: double the net force doubles the acceleration, and double "
      "the mass halves it. And keep mass and weight apart. Your mass doesn't change in a lift. The force from the floor does, and "
      "that is what scales read.",
      refs=['content', 'ar20q1', 'ex20q1'], covers=['N6', 'N5'], elements=[1], exam=['X20-1']),
    S("Elements two and four. A seventy point zero kilogram person stands on scales in a lift, and the scales read seventy six point "
      "five kilograms. The scales push up with seven hundred and fifty newtons, but the weight is six hundred and eighty seven. The "
      "net force is sixty three point eight newtons up, so the acceleration is zero point nine one one upward. The lift is speeding "
      "up going up, or slowing down going down.",
      refs=['ex20q1', 'ar20q1'], covers=['N5', 'G2'], elements=[2, 4], exam=['X20-1'],
      problem='A 70.0 kg person stands on scales in a lift. The scales read 76.5 kg. What is the lift’s acceleration, and how might it be moving?'),
]),
Scene('we_rocket', P3, 'Worked example: a rocket', V.we_rocket, [
    S("Element two. A rocket of four hundred and twenty tonnes accelerates upward at three point zero zero metres per second squared "
      "at lift-off. That's four point two times ten to the five kilograms. The net force is thrust minus weight, so the thrust is m "
      "times a plus g: five point three eight times ten to the six newtons. The most common error was forgetting the weight.",
      refs=['ex24q6', 'ar24q6'], covers=['N5', 'N6', 'G2'], elements=[2], exam=['X24-6'],
      problem='A 420 t rocket accelerates upward at 3.00 m/s² at lift-off. What thrust do its engines provide?'),
    S("Later, the thrust is unchanged but the acceleration is twelve point zero. The mass is the thrust over a plus g, which is "
      "five point three eight times ten to the six, over twenty one point eight one: two point four seven times ten to the five "
      "kilograms. Don't subtract g: gravity still pulls down.",
      refs=['ex24q6', 'ar24q6'], covers=['N5', 'N6'], elements=[2], exam=['X24-6'],
      problem='Later, the thrust is the same but the acceleration is 12.0 m/s². What is the rocket’s mass?'),
    S("Check validity. The net force at lift-off is the mass times three: one point two six times ten to the six newtons. Thrust "
      "minus weight is five point three eight minus four point one two: also one point two six million. Lift-off needs thrust "
      "above weight, and here the ratio is one point three one. Draw the thrust arrow visibly longer.",
      refs=['ar24q6', 'ex24q6'], covers=['N5', 'N1'], elements=[2, 4], exam=['X24-6']),
]),
Scene('newton3', P3, 'Newton’s third law', V.newton3, [
    S("Newton's third law: when one object exerts a force on a second, the second exerts a force on the first that is equal in "
      "size, opposite in direction, and of the same type. The two forces act on different objects, so they never cancel on one "
      "object. A rocket pushes gas down, and the gas pushes the rocket up. A bullet pushes a plate, and the plate pushes it back.",
      refs=['content', 'ar23q4', 'ex23q4'], covers=['N8'], elements=[1], exam=['X23-4']),
    S("A common mistake is pairing weight with the normal force on a book. They're equal and opposite, but both act on the book, "
      "and they're different types. The pair of the book's weight is the book pulling the Earth up. The report gave a mark for "
      "naming the third law when finding the force on the plate. And a probe passing a planet gives it the opposite change in "
      "momentum.",
      refs=['ar23q4', 'ex23q4', 'ar19q4', 'ex19q4'], covers=['N8'], elements=[1, 4], exam=['X23-4', 'X19-4'],
      problem='A book rests on a table. Identify the Newton’s third law pair of the book’s weight, and say why the normal force is not it.'),
]),
# ------------------------------------------------------------------- part 4: momentum
Scene('impulse', P4, 'Momentum and impulse', V.impulse, [
    S("Part four. Momentum is mass times velocity: p equals m v, in the motion and momentum section of your information sheet. It's "
      "a vector, in kilogram metres per second. The same section gives Newton's second law as force equals change in momentum "
      "over time. So the change in momentum equals force times time, called the impulse, in newton seconds.",
      refs=['content', 'info'], covers=['P1', 'N6'], elements=[1]),
    S("On a force time graph, the area is the impulse, which is the change in momentum. On a momentum time graph, the gradient is "
      "the net force. Element three. A zero point two zero zero kilogram ball is kicked by a triangular force pulse peaking at "
      "three hundred newtons for zero point zero four zero seconds. The area is six point zero zero newton seconds, so, from rest, "
      "its speed is thirty point zero metres per second.",
      refs=['content', 'info'], covers=['N9', 'N6'], elements=[2, 3],
      problem='A 0.200 kg ball at rest is kicked with a triangular force pulse peaking at 300 N for 0.040 s. What is its speed afterwards?'),
    S("The same impulse can come from a large force for a short time, or a small force for a long time. That's why crumple zones, "
      "air bags and helmets work: they lengthen the stopping time, so the average force falls. When you predict, say it: the "
      "change in momentum is fixed, so more time means less force.",
      refs=['content', 'ar24q2'], covers=['N9', 'N5'], elements=[4],
      problem='Why does an air bag reduce the injury in a crash, in terms of momentum?'),
]),
Scene('dp_vector', P4, 'Change in momentum is a vector', V.dp_vector, [
    S("In two dimensions, the key skill is the change in momentum: final minus initial. Momentum is a vector, so that's a vector "
      "subtraction. The most common error in the reports, year after year, is adding the momenta head to tail, and that earns no "
      "marks. Write the vector statement first. Then draw both momenta from one point; the change joins the tip of the initial "
      "to the tip of the final.",
      refs=['ar20q3', 'ex20q3', 'ar23q4', 'ex23q4', 'ar21q1', 'ex21q1', 'ar19q4', 'ex19q4'], covers=['N10', 'P1', 'N6'], elements=[1, 2],
      exam=['X20-3', 'X23-4', 'X21-1', 'X19-4']),
    S("Then solve the triangle. At ninety degrees, use Pythagoras. Otherwise use the cosine rule, on your information sheet in the "
      "trigonometry identities section, with the angle inside the triangle. Use the sine rule or a tangent for direction. Always "
      "give a direction, relative to something clear, such as the initial momentum. Draw roughly to scale, since the report "
      "awarded marks for that.",
      refs=['ar19q4', 'ex19q4', 'ar20q3', 'ex20q3', 'info'], covers=['N10'], elements=[2], exam=['X19-4', 'X20-3']),
    S("A one dimensional case shows the sign problem. A ball hits a wall at ten metres per second and bounces straight back at ten. "
      "Taking the first direction as positive, the final velocity is minus ten, so the change is minus twenty. It's not zero, "
      "and not ten. A scalar difference earns only half a mark.",
      refs=['ar20q3', 'ex20q3'], covers=['P1', 'N10'], elements=[1, 2], exam=['X20-3']),
]),
Scene('we_bounce', P4, 'Worked example: a tennis return', V.we_bounce, [
    S("Element two. A zero point zero five eight zero kilogram tennis ball arrives at twenty five point zero metres per second, east. "
      "The racket returns it at thirty one point zero, twenty degrees above the horizontal, heading west. The momenta are one point "
      "four five, and one point eight zero kilogram metres per second. Drawn from one point, the angle between them is one hundred "
      "and sixty degrees.",
      refs=['ex20q3', 'ar20q3', 'ex21q1', 'ar21q1', 'ex25q2', 'ar25q2'], covers=['N10', 'P1'], elements=[2], exam=['X20-3', 'X21-1', 'X25-2'],
      problem='A 0.0580 kg ball moving east at 25.0 m/s is returned west at 31.0 m/s, 20.0° above the horizontal. What is its change in momentum?'),
    S("The cosine rule gives the root of one point four five squared, plus one point seven nine eight squared, minus two times "
      "those two times cosine one hundred and sixty. That's three point two zero kilogram metres per second. The cosine is "
      "negative, so the products add.",
      refs=['ar25q2', 'ar21q1', 'info'], covers=['N10', 'N6'], elements=[2], exam=['X25-2', 'X21-1']),
    S("The direction: tangent phi is zero point six one five over three point one four, so eleven point one degrees above west. "
      "From the initial momentum, that's one hundred and sixty nine degrees. For a five millisecond contact, the average force "
      "is six hundred and forty newtons, in the direction of the change in momentum. By the third law, the racket feels the "
      "same force the other way.",
      refs=['ar20q3', 'ex20q3', 'ar23q4', 'ex23q4'], covers=['N10', 'N8', 'N6'], elements=[2], exam=['X20-3', 'X23-4'],
      problem='The contact time is 5.00 ms. What is the average force on the ball, and in which direction?'),
]),
Scene('conserve', P4, 'Conservation of momentum', V.conserve, [
    S("The law of conservation of momentum: when no outside force acts, the total momentum before equals the total momentum after. "
      "It's a vector law, so in two dimensions each direction is conserved separately. In a collision, objects meet and bounce or "
      "stick. In an explosion, they start together and fly apart, so from rest their momenta cancel as vectors.",
      refs=['content', 'ex24q5', 'ar24q5', 'ex23q5', 'ar23q5'], covers=['P2', 'P3', 'P4'], elements=[1], exam=['X24-5', 'X23-5']),
    S("Momentum is conserved in every collision, but kinetic energy isn't. In an elastic collision, the total kinetic energy stays "
      "the same; in an inelastic one, some is lost as heat, sound or deformation. To decide, calculate the total kinetic energy "
      "before and after. A report says quoting momentum conservation was a common wrong answer to whether a collision is elastic.",
      refs=['ar22q2', 'ex22q2', 'ar18q2', 'ex18q2'], covers=['E6', 'P2'], elements=[1, 2], exam=['X22-2', 'X18-2']),
    S("Equal masses, one at rest, leave at ninety degrees. Why? The momentum triangle has sides p zero, p A and p B. Kinetic energy "
      "is p squared over two m, so if energy is also conserved, p zero squared equals p A squared plus p B squared: Pythagoras, "
      "a right angle. A marking note: the 2018 report credits momentum alone for the ninety degrees. Physically you need energy "
      "conservation as well, so state both.",
      refs=['ar18q2', 'ex18q2', 'ex22q2', 'ar22q2'], covers=['P3', 'E6'], elements=[1, 4], exam=['X18-2', 'X22-2']),
    S("You may be asked to show conservation from Newton's laws. During contact, the forces are equal and opposite, by the "
      "third law, for the same time. So the changes in momentum are equal and opposite: delta p one plus delta p two is zero, "
      "and the total doesn't change. The report warns that writing delta p one equals delta p two isn't enough.",
      refs=['ex21q3', 'ar21q3'], covers=['P2', 'N8', 'N6'], elements=[1], exam=['X21-3'],
      problem='Using Newton’s second and third laws, show that the total momentum is conserved when two objects collide.'),
]),
Scene('we_puck', P4, 'Worked example: two pucks', V.we_puck, [
    S("Element two. A zero point two zero zero kilogram puck at one point eight zero metres per second strikes an identical puck at "
      "rest. The first leaves at one point zero eight, and the pucks separate at right angles. The momentum triangle is right "
      "angled, with the original momentum as hypotenuse, so the second puck's speed is the root of one point eight squared "
      "minus one point zero eight squared: one point four four metres per second.",
      refs=['ex22q2', 'ar22q2', 'ex18q2', 'ar18q2'], covers=['P3', 'N10'], elements=[2], exam=['X22-2', 'X18-2'],
      problem='A 0.200 kg puck at 1.80 m/s strikes an identical puck at rest. The first puck leaves at 1.08 m/s and the pucks separate at 90°. What is the second puck’s speed?'),
    S("For the angles, the first puck's cosine is one point zero eight over one point eight, which is fifty three point one "
      "degrees from its original path. The second leaves at thirty six point nine on the other side. Make the diagram tidy: "
      "untidy ones led to wrong trigonometric ratios.",
      refs=['ar22q2', 'ar18q2'], covers=['P3', 'N10'], elements=[2], exam=['X22-2', 'X18-2'],
      problem='What angles do the two pucks leave at, from the first puck’s original direction?'),
    S("Is it elastic? Before, the kinetic energy is zero point three two four joules. After, a half times zero point two zero "
      "zero, times one point zero eight squared plus one point four four squared, is also zero point three two four. They're "
      "equal, so it's elastic. Show both calculations: a bare yes earns half marks.",
      refs=['ar22q2', 'ex22q2'], covers=['E6', 'E4', 'P3'], elements=[2, 4], exam=['X22-2'],
      problem='Is the puck collision elastic? Justify with kinetic energy calculations.'),
]),
Scene('we_skate', P4, 'Worked example: skaters and a launcher', V.we_skate, [
    S("Element two. A seventy kilogram skater moving north at four metres per second collides with a fifty five "
      "kilogram skater moving east at five, and they cling together. The momenta, two hundred and eighty and two "
      "hundred and seventy five, are at right angles, so the total is three hundred and ninety two kilogram metres per "
      "second. Over one hundred and twenty five kilograms, the velocity is three point one four metres per second, "
      "forty four point five degrees east of north. Energy isn't conserved here, but momentum is.",
      refs=['ex24q5', 'ar24q5', 'ar23q5', 'ex23q5'], covers=['P3', 'P4', 'N10', 'E6'], elements=[2, 4], exam=['X24-5', 'X23-5'],
      problem='A 70.0 kg skater moving north at 4.00 m/s collides with a 55.0 kg skater moving east at 5.00 m/s and they cling together. What is their final velocity?'),
    S("Explosions work the same way. A four point five zero kilogram launcher at rest fires a zero point zero six zero zero "
      "kilogram dart at ninety metres per second. The total momentum stays zero, so the launcher recoils the other way at one "
      "point two zero metres per second. Kinetic energy rises from nothing to two hundred and forty six joules, from stored "
      "chemical or elastic energy.",
      refs=['content'], covers=['P2', 'P4'], elements=[2, 4],
      problem='A 4.50 kg launcher at rest fires a 0.0600 kg dart at 90.0 m/s. What is the launcher’s recoil velocity?'),
]),
Scene('mass_flow', P4, 'Force from a moving stream', V.mass_flow, [
    S("The second law also covers moving mass. If a stream is pushed from rest to speed v, the force is mass per second times v. For "
      "a fluid, picture a cylinder: in one second, a column of length v passes through area A. Its mass is density times A times "
      "v. So the force is density times area times v squared.",
      refs=['content', 'ar25q5', 'ex25q5', 'ar21q4', 'ex21q4'], covers=['N7', 'N6'], elements=[1, 2], exam=['X25-5', 'X21-4']),
    S("This covers hoses, helicopters, jets and wind. The force on the fluid has an equal and opposite force on the machine, by the "
      "third law. A hovering helicopter isn't accelerating, so the force equals its weight, and markers reported many missing that. "
      "For energy, use the kinetic energy given to the air each second, a half times mass per second times v squared. Don't "
      "multiply force by air speed. For wind slowing from u to v, use the change.",
      refs=['ar25q5', 'ex25q5', 'ar20q2', 'ex20q2', 'ar21q4', 'ex21q4'], covers=['N7', 'N8', 'E4'], elements=[1, 2], exam=['X25-5', 'X20-2', 'X21-4']),
    S("Ion drives use the same law with tiny amounts. Expelling five point zero times ten to the minus six kilograms per second at "
      "thirty thousand metres per second gives only zero point one five newtons. On a five hundred kilogram probe, that's three "
      "point zero times ten to the minus four metres per second squared, but it never stops: over a year, about nine point five "
      "kilometres per second.",
      refs=['content', 'appendix'], covers=['N7'], elements=[2, 4],
      problem='An ion drive expels 5.0 × 10⁻⁶ kg/s at 3.0 × 10⁴ m/s on a 500 kg probe. What is the force, and the speed gained in a year?'),
]),
Scene('we_drone', P4, 'Worked example: a hovering drone', V.we_drone, [
    S("Element two. A drone pushes air down at nine point zero zero metres per second through rotors of area zero point two five zero "
      "square metres. The air density is one point two zero. In one second, the volume is area times speed: two point two five "
      "cubic metres. The mass is density times that: two point seven zero kilograms.",
      refs=['ex25q5', 'ar25q5', 'ex21q4', 'ar21q4'], covers=['N7', 'N6'], elements=[2], exam=['X25-5', 'X21-4'],
      problem='A drone pushes air down at 9.00 m/s through 0.250 m² of rotor area. The air density is 1.20 kg/m³. What mass of air is pushed down each second?'),
    S("The change in momentum each second is that mass times the speed: twenty four point three newtons, since the air starts "
      "from rest. By the third law, that's the upward force on the drone. If it hovers, that equals the weight, so the mass is "
      "twenty four point three over nine point eight one: two point four eight kilograms.",
      refs=['ex25q5', 'ar25q5', 'ex21q4', 'ar21q4'], covers=['N7', 'N8', 'N4'], elements=[2, 4], exam=['X25-5', 'X21-4'],
      problem='Given that the drone is hovering, what is its mass?'),
    S("The energy: each second the air gains a half times two point seven zero times nine squared: one hundred and nine watts. If the "
      "motors draw two hundred and eighty watts, the percentage is one hundred and nine over two hundred and eighty, times a hundred: "
      "thirty nine point one percent. Remember to multiply by a hundred.",
      refs=['ar25q5', 'ex25q5', 'ar21q4', 'ex21q4', 'ar20q2', 'ex20q2'], covers=['E4', 'E7', 'N7'], elements=[2, 4], exam=['X25-5', 'X21-4', 'X20-2'],
      problem='The drone’s motors draw 280 W. What percentage of that power is given to the air?'),
]),
# ------------------------------------------------------------------- part 5: circular motion
Scene('circ', P5, 'Circular motion', V.circ, [
    S("Part five. An object moving in a circle at constant speed is accelerating, because its velocity keeps changing direction. "
      "The velocity is along the tangent, with size the circumference over the period: v equals two pi r over T. That one isn't "
      "on the sheet. The change in velocity points to the centre: for a small angle, delta v is v times delta theta, and the "
      "angle swept each second is v over r, so the acceleration is v squared over r.",
      refs=['content'], covers=['C1', 'C2'], elements=[1], anim=4),
    S("The centripetal formulas are on your information sheet, in the motion, momentum and force section. The acceleration is v "
      "squared over r, which equals four pi squared r over T squared. The force is m v squared over r, which equals four pi "
      "squared m r over T squared. Centripetal means pointing to the centre. It isn't a new kind of force: it's the net force "
      "toward the centre, supplied by tension, gravity, friction or a component of another force.",
      refs=['content', 'info'], covers=['C2', 'C3', 'N6'], elements=[1, 2]),
    S("Tips. Given the period, use the four pi squared r over T squared form directly: the long way through v costs time and "
      "causes errors. The r is the radius, not the diameter or circumference. In a diagram, draw the real forces, such as tension "
      "and weight, and say their sum points to the centre. A dashed net force arrow is acceptable; a solid centripetal force arrow isn't.",
      refs=['ar20q5', 'ex20q5', 'ar25q3', 'ex25q3', 'ar24q1', 'ex24q1'], covers=['C2', 'C3'], elements=[1, 2], exam=['X20-5', 'X25-3', 'X24-1']),
]),
Scene('we_conical', P5, 'Worked example: a bob circling horizontally', V.we_conical, [
    S("Element two. A zero point two five zero kilogram bob hangs on a one point two zero metre string and circles horizontally, "
      "the string at thirty degrees to the vertical. Only weight and tension act. The bob doesn't move vertically, so the "
      "vertical part of the tension balances the weight: T cosine thirty equals m g, giving two point eight three newtons.",
      refs=['ex24q1', 'ar24q1', 'ex19q2', 'ar19q2'], covers=['C3', 'N2', 'N3'], elements=[2], exam=['X24-1', 'X19-2'],
      problem='A 0.250 kg bob on a 1.20 m string circles horizontally with the string at 30.0° to the vertical. What is the tension in the string?'),
    S("The horizontal part of the tension is the net force, pointing to the centre: one point four two newtons. The radius is the "
      "string length times sine thirty, zero point six zero zero metres. Then v squared is r g tan theta, so the speed is one "
      "point eight four metres per second. The net force is the centripetal force here, not another force added on.",
      refs=['ar24q1', 'ex24q1'], covers=['C2', 'C3', 'N5'], elements=[2], exam=['X24-1'],
      problem='What is the net force on the bob, and its speed?'),
    S("The period is two pi times zero point six over one point eight four four: two point zero five seconds. Check validity: the "
      "acceleration is g tan thirty, five point six six, and four pi squared r over T squared gives the same. The two routes agree.",
      refs=['ar24q1', 'ex24q1'], covers=['C1', 'C2'], elements=[2, 4], exam=['X24-1'],
      problem='What is the bob’s period of revolution?'),
]),
Scene('circ_apps', P5, 'Banking, leaning and tilting', V.circ_apps, [
    S("A tilted aircraft turns because of its tilt. The air pushes on the wings at right angles to them, so the lift has a "
      "vertical part, balancing the weight, and a horizontal part, which is the net force toward the centre. Element two: a six "
      "hundred kilogram glider banked at twenty five degrees. The lift is m g over cosine twenty five: six thousand five hundred "
      "newtons to three significant figures.",
      refs=['ex22q3', 'ar22q3'], covers=['C3', 'N2', 'N3'], elements=[2], exam=['X22-3'],
      problem='A 600 kg glider turns in a horizontal circle, banked at 25.0°. What is the lift force?'),
    S("The net force is m g tan twenty five: two thousand seven hundred and forty newtons, to the centre. At forty "
      "point zero metres per second, the radius is v squared over g tan theta: three hundred and fifty metres. In a "
      "similar exam question, four thousand four hundred and ten newtons was a common wrong answer: that's m g sine, "
      "not m g tan. Draw the force triangle.",
      refs=['ar22q3', 'ex22q3'], covers=['C2', 'C3', 'N5'], elements=[2], exam=['X22-3'],
      problem='At 40.0 m/s, what is the net force on the glider and the radius of its turn?'),
    S("The same method covers banked roads, leaning cyclists, a child swung by the arms, and a hanging charm in a turning or "
      "accelerating car, where tan theta equals a over g. For a prediction: at the same bank angle, doubling the speed makes the "
      "radius four times bigger, because of v squared.",
      refs=['ar19q2', 'ex19q2', 'ar24q1', 'ex24q1'], covers=['C3', 'C2'], elements=[1, 4], exam=['X19-2', 'X24-1'],
      problem='At the same bank angle, what happens to the radius of a turn if the speed doubles?'),
]),
Scene('spin', P5, 'Standing on a spinning planet', V.spin, [
    S("A person on the equator moves in a circle, so needs a centripetal acceleration of four pi squared R over T squared. On Earth "
      "that's zero point zero three three seven metres per second squared, since the equator moves at four hundred and sixty "
      "four metres per second. Only part of the gravitational pull is left to push on the ground, so the apparent weight is "
      "slightly less. On Mars, the effect is a little under half of one percent.",
      refs=['ex23q3', 'ar23q3', 'ex18q6', 'ar18q6', 'ex20q5', 'ar20q5'], covers=['C3', 'C2', 'G2'], elements=[2, 4], exam=['X23-3', 'X18-6', 'X20-5'],
      problem='Mars has equatorial radius 3.39 × 10⁶ m and rotates once in 24.6 h. What is the centripetal acceleration of a person on its equator?'),
    S("This also explains the Earth's shape. Equatorial material wants to move in a straight line, by Newton's first law, so the "
      "equator bulges. Two effects then reduce the push of the ground at the equator: the larger radius gives a smaller field "
      "strength, and the spin needs a net inward force. At the poles there's no circular motion. Reports say most students named a "
      "centripetal force, but didn't link it to how hard the ground pushes on the person.",
      refs=['ar23q3', 'ex23q3', 'ar20q5', 'ex20q5'], covers=['G6', 'C3', 'N4'], elements=[1, 4], exam=['X23-3', 'X20-5']),
    S("Take it to an extreme. On a small, fast spinning asteroid, the centripetal acceleration at the equator can approach the "
      "local g, so the ground hardly pushes and the surface is almost in orbit. That's the point of the Bennu question: the apparent "
      "acceleration is less than the field strength, not more. Students got it backward.",
      refs=['ar20q5', 'ex20q5', 'ar18q6', 'ex18q6'], covers=['C2', 'G12'], elements=[4], exam=['X20-5', 'X18-6'],
      problem='On a small fast-spinning asteroid, is the apparent acceleration due to gravity at the equator more or less than the field strength?'),
]),
# ------------------------------------------------------------------- part 6: work, energy and power
Scene('work', P6, 'Work and force-distance graphs', V.work, [
    S("Part six. Work is energy transferred by a force: W equals F s cosine theta, on your information sheet in the work, energy "
      "and power section. Theta is the angle between the force and the displacement. Only the part of the force along the "
      "displacement does work. A force at right angles does none, so gravity does no work on level motion, and a centripetal force "
      "does none on a circling object. The unit is the joule.",
      refs=['content', 'info', 'ar19q1', 'ex19q1'], covers=['E2'], elements=[1, 2], exam=['X19-1']),
    S("When the force changes, use a force distance graph: the work is the area under it. Count squares, or split it into triangles "
      "and rectangles, and read the scale carefully. The reports say many students didn't read the exact force from the graph, "
      "and others multiplied the biggest force by the distance, rather than finding the area.",
      refs=['ar23q2', 'ex23q2', 'ar18q1', 'ex18q1'], covers=['E1'], elements=[3], exam=['X23-2', 'X18-1']),
    S("Two energy forms use the same section of your information sheet. Gravitational potential energy is m g h, for a height "
      "change: on a slope, use the distance along it times sine theta. Kinetic energy is a half m v squared. And compare two "
      "launchers by the area under each graph, which is the stored energy, and by the force at full draw, which is how hard "
      "it is to hold.",
      refs=['content', 'info', 'ar18q1', 'ex18q1', 'ar18q4', 'ex18q4'], covers=['E3', 'E4', 'E1'], elements=[1, 3], exam=['X18-1', 'X18-4']),
]),
Scene('we_work', P6, 'Worked example: work from forces and graphs', V.we_work, [
    S("Element two. A sled is pulled twelve point zero metres along level snow by a rope pulling eighty point zero newtons at "
      "thirty five degrees above the horizontal. Only the horizontal component does work: eighty times twelve times cosine thirty "
      "five, seven hundred and eighty six joules. Always ask which angle lies between the force and the movement.",
      refs=['ex19q1', 'ar19q1', 'ar18q4'], covers=['E2'], elements=[2], exam=['X19-1'],
      problem='A sled is pulled 12.0 m along level snow by an 80.0 N rope at 35.0° above the horizontal. How much work does the rope do?'),
    S("Element three. A launcher's force distance graph runs straight from zero to sixty newtons at zero point one zero "
      "metres, to one hundred at zero point three zero, then ninety at zero point four zero. The area is three plus "
      "sixteen plus nine point five: twenty eight point five joules. Seventy percent goes to a zero point zero four "
      "five zero kilogram ball: nineteen point nine five joules, so twenty nine point eight metres per second.",
      refs=['ex23q2', 'ar23q2', 'ex18q1', 'ar18q1'], covers=['E1', 'E4', 'E5'], elements=[2, 3], exam=['X23-2', 'X18-1'],
      problem='A launcher’s force-distance graph has straight lines through (0, 0), (0.10 m, 60 N), (0.30 m, 100 N) and (0.40 m, 90 N). If 70% of the energy goes to a 0.0450 kg ball, what is its speed?'),
]),
Scene('energy', P6, 'Conservation of energy', V.energy, [
    S("Energy is never created or destroyed, only changed in form. Define a start and an end, and write the total "
      "energy at each. With no friction or drag, kinetic plus potential stays constant, so a ball dropped from h "
      "reaches the ground at the root of two g h. With friction, lost energy equals the work done against it. The "
      "report asked for this approach in the swinging egg question.",
      refs=['content', 'ar20q4', 'ex20q4'], covers=['E5', 'E3', 'E4'], elements=[1, 2], exam=['X20-4']),
    S("For collisions, use the kinetic energy test. Elastic: the total kinetic energy is unchanged. Inelastic: it falls. Calculate "
      "it before and after, compare, and state your conclusion with the numbers. The fraction lost is the difference over the "
      "original, times a hundred for a percentage.",
      refs=['ar22q2', 'ex22q2', 'ar18q2', 'ex18q2'], covers=['E6', 'E4'], elements=[1, 2], exam=['X22-2', 'X18-2']),
    S("Be careful when two ideas meet. A pellet embedding in a hanging block is a collision, so use momentum, since energy isn't "
      "conserved in it. Afterwards, the swing is a conservation of energy problem. Reports say many candidates used energy for "
      "the collision itself. Each stage has its own law, so label the stages.",
      refs=['ar23q5', 'ex23q5'], covers=['E5', 'P2'], elements=[1, 2], exam=['X23-5']),
]),
Scene('we_dart', P6, 'Worked example: a dart and a block', V.we_dart, [
    S("Element two. A zero point zero two five zero kilogram dart at forty point zero metres per second embeds in a zero point four "
      "seven five kilogram block hanging from strings. A collision: use momentum. The total mass is zero point five zero zero, so "
      "the speed just after is zero point zero two five times forty, over zero point five: two point zero zero metres per second.",
      refs=['ex23q5', 'ar23q5'], covers=['P2', 'N6'], elements=[2], exam=['X23-5'],
      problem='A 0.0250 kg dart at 40.0 m/s embeds in a hanging 0.475 kg block. What is the speed of the block and dart just after?'),
    S("Before, the kinetic energy is a half times zero point zero two five times forty squared: twenty point zero joules. After, "
      "it's a half times zero point five times two squared: one point zero zero joule. So nineteen joules, ninety five percent, "
      "was lost as heat, sound and deformation. Inelastic, with momentum still conserved.",
      refs=['ar23q5', 'ex23q5'], covers=['E6', 'E4'], elements=[2, 4], exam=['X23-5'],
      problem='How much kinetic energy is lost in the dart collision, as a percentage?'),
    S("For the swing, kinetic energy becomes potential energy: a half v squared equals g h, so h is two squared over two times nine "
      "point eight one: zero point two zero four metres. Check validity: using the dart's twenty joules would give a height twenty "
      "times too big. Only one joule is left, and one over m g gives the same zero point two zero four.",
      refs=['ar23q5', 'ex23q5'], covers=['E5', 'E3'], elements=[2, 4], exam=['X23-5'],
      problem='How high does the block swing?'),
]),
Scene('power', P6, 'Power and efficiency', V.power, [
    S("Power is the rate of transferring energy: P equals W over t, on your information sheet in the work, energy and power "
      "section, and it equals delta E over t. The unit is the watt, one joule per second. A good method is to work out the "
      "energy each second. For a steady force moving its point of application at constant speed, P equals F v, but don't use "
      "that for a stream of fluid being accelerated.",
      refs=['content', 'info', 'ar22q5', 'ex22q5', 'ar25q5', 'ex25q5'], covers=['E7', 'E2'], elements=[1, 2], exam=['X22-5', 'X25-5']),
    S("Efficiency is useful output over total input, times a hundred. A report notes students forgot the hundred. When "
      "an object climbs at constant speed, the kinetic energy doesn't change, so the engine supplies the potential "
      "energy gained per second plus the work against resistance per second. Both are needed. Resistance is a force, so "
      "use weight, not mass.",
      refs=['ar22q5', 'ex22q5', 'ar18q4', 'ex18q4', 'ar21q4'], covers=['E7', 'E3'], elements=[1, 2], exam=['X22-5', 'X18-4']),
]),
Scene('we_power', P6, 'Worked example: a car on a hill', V.we_power, [
    S("Element two. A one thousand two hundred kilogram car climbs an eight degree slope at a constant fifteen point zero metres per "
      "second, against a constant resistance of six hundred newtons. In one second it moves fifteen metres along the slope, "
      "gaining fifteen sine eight: two point zero nine metres of height. So the potential energy gained each second, m g h, is "
      "twenty four point six kilojoules: twenty four point six kilowatts.",
      refs=['ex22q5', 'ar22q5', 'ex18q4', 'ar18q4'], covers=['E3', 'E7'], elements=[2], exam=['X22-5', 'X18-4'],
      problem='A 1200 kg car climbs an 8.00° slope at a constant 15.0 m/s against a 600 N resistance. How much potential energy does it gain each second?'),
    S("Work against the resistance each second is six hundred times fifteen: nine point zero zero kilowatts. The kinetic energy "
      "isn't changing, so it adds nothing. The total is twenty four point six plus nine point zero: thirty three point six "
      "kilowatts, the useful power at the wheels.",
      refs=['ar22q5', 'ex22q5'], covers=['E7', 'E5'], elements=[2], exam=['X22-5'],
      problem='What is the total useful power the car needs at constant speed?'),
    S("If the engine produces forty five point zero kilowatts, the percentage used is thirty three point six over forty five, times a "
      "hundred: seventy four point six percent. Check validity: it's below a hundred, and the other eleven point four kilowatts is "
      "lost as heat and sound. An answer above a hundred shows an error, often a missed factor of a thousand.",
      refs=['ar22q5', 'ex22q5', 'ar18q4', 'ex18q4'], covers=['E7'], elements=[2, 4], exam=['X22-5', 'X18-4'],
      problem='If the engine produces 45.0 kW, what percentage of its power is used to move the car up the slope?'),
]),
# ------------------------------------------------------------------- part 7: gravity
Scene('grav_law', P7, 'Universal gravitation and field strength', V.grav_law, [
    S("Part seven. Newton's law of universal gravitation: two masses attract with a force F equals G M one M two over r squared. G is "
      "six point six seven times ten to the minus eleven newton metres squared per kilogram squared. Both are on your information "
      "sheet in the gravity and Kepler's law section. The distance r is between the centres. The two forces are equal and opposite. "
      "Doubling the distance makes the force a quarter.",
      refs=['content', 'info'], covers=['G1', 'N8'], elements=[1, 2]),
    S("Weight is the gravitational force on a body: F g equals m g. A mass creates a field around it, and field theory "
      "says the force on another mass comes from that field. Field strength is force per kilogram: g equals F g over m, "
      "in newtons per kilogram, the same as metres per second squared. Near one mass, g equals G M over r squared. All "
      "on the sheet. The source mass sets the field.",
      refs=['content', 'info'], covers=['G2', 'G3', 'G4', 'G6'], elements=[1]),
    S("Here's a show that question. A weather satellite orbits at seven point two zero times ten to the six metres, with a period "
      "of six point zero eight times ten to the three seconds. Its acceleration, four pi squared r over T squared, is seven "
      "point six nine. From the surface, nine point eight one times the radius ratio squared gives seven point six eight. They "
      "agree, so gravity follows an inverse square law.",
      refs=['ex25q3', 'ar25q3', 'ex21q5', 'ar21q5'], covers=['G1', 'G6', 'C2'], elements=[2, 3], exam=['X25-3', 'X21-5'],
      problem='A satellite orbits at r = 7.20 × 10⁶ m with period 6.08 × 10³ s. Earth’s radius is 6.37 × 10⁶ m. Show that gravity follows an inverse square law.'),
]),
Scene('we_g', P7, 'Worked example: field strength at altitude', V.we_g, [
    S("Element two. A satellite orbits five hundred and sixty kilometres above Earth's surface. Earth's radius is six point three "
      "seven times ten to the six metres, and g at the surface is nine point eight one. Use the radius from the centre: six point "
      "nine three times ten to the six metres. Since g goes as one over r squared, g is nine point eight one times the ratio "
      "squared: eight point two nine.",
      refs=['ex25q3', 'ar25q3', 'ex24q3', 'ar24q3'], covers=['G6', 'G4'], elements=[2], exam=['X25-3', 'X24-3'],
      problem='A satellite orbits 560 km above Earth’s surface (radius 6.37 × 10⁶ m, surface g 9.81 N/kg). What is g at its orbit?'),
    S("Check with G M over r squared: also eight point two nine newtons per kilogram. The ratio method avoids needing the mass, "
      "as the report notes. Common slips: using the altitude as r, mixing the Moon's radius with Earth's g, and, in the neutron "
      "star question, using the diameter instead of the radius. At that height, gravity is still about eighty five percent of "
      "its surface value.",
      refs=['ar25q3', 'ex25q3', 'ar24q3', 'ex24q3'], covers=['G6'], elements=[2, 4], exam=['X25-3', 'X24-3']),
]),
Scene('fields', P7, 'Gravitational fields', V.fields, [
    S("A gravitational field has a strength and a direction at every point: the way a mass would be pulled. Draw it with lines "
      "pointing toward the mass. Closer lines mean a stronger field. Around a single mass the lines are straight, evenly spaced "
      "and inward, getting further apart with distance. Near a planet's surface, they're parallel and evenly spaced.",
      refs=['content'], covers=['G3', 'G5', 'G8'], elements=[1], anim=2),
    S("For two masses, lines run into each, and more end on the bigger one. Lines never cross. Between the masses is a neutral "
      "point where the fields cancel, closer to the smaller mass, and the boundary between the two sets of lines curves around "
      "it. Far away, the pair looks like one mass. Reports credit lines in toward both, a denser pattern at the bigger mass, and "
      "the overall shape.",
      refs=['ar25q4', 'ex25q4', 'ar21q6', 'ex21q6'], covers=['G8', 'G5'], elements=[1, 3], exam=['X25-4', 'X21-6'],
      problem='Sketch the gravitational field around two masses, one larger than the other.'),
    S("At any point, the total field is the vector sum of each mass's field. Each is G M over r squared, pointing toward its own mass. "
      "Calculate each with its direction, then add as vectors: in a line, with signs; at an angle, head to tail. Add fields, "
      "not forces, and give the direction of your answer.",
      refs=['content', 'ar25q4', 'ex25q4', 'ar21q6', 'ex21q6'], covers=['G7', 'G6'], elements=[1, 2], exam=['X25-4', 'X21-6']),
]),
Scene('we_two', P7, 'Worked example: adding two fields', V.we_two, [
    S("Element two. Planets A and B have masses of nine point zero zero times ten to the twenty four, and one point two "
      "zero times ten to the twenty five kilograms. Point P is three point zero zero times ten to the eight metres from "
      "A, and four point zero zero times ten to the eight from B, with a right angle at P. The field of A is six point "
      "six seven times ten to the minus three newtons per kilogram, toward A. For B it's five point zero zero times ten "
      "to the minus three, toward B.",
      refs=['ex25q4', 'ar25q4', 'ex21q6', 'ar21q6'], covers=['G7', 'G6'], elements=[2], exam=['X25-4', 'X21-6'],
      problem='Planet A (9.00 × 10²⁴ kg) is 3.00 × 10⁸ m from point P and planet B (1.20 × 10²⁵ kg) is 4.00 × 10⁸ m from P, at a right angle. What is the field of each at P?'),
    S("The arrows are at right angles, so add them head to tail with Pythagoras: eight point three four times ten to the minus "
      "three newtons per kilogram. The direction: tangent of the angle is five over six point six seven, thirty six point nine "
      "degrees from the direction to A, turned toward B. Draw the triangle, and label which field is which.",
      refs=['ar25q4', 'ar21q6'], covers=['G7', 'N10'], elements=[2], exam=['X25-4', 'X21-6'],
      problem='What are the size and direction of the total gravitational field at P?'),
    S("Watch the angle. If two fields at a point are sixty degrees apart, as with an equilateral triangle of positions, the angle "
      "inside the head to tail triangle is one hundred and twenty. Reports say using sixty in the cosine rule was the most common "
      "error. And keep enough significant figures: where the fields almost cancel, early rounding can give zero.",
      refs=['ar25q4', 'ex25q4', 'ar21q6', 'ex21q6'], covers=['G7'], elements=[2, 4], exam=['X25-4', 'X21-6']),
]),
Scene('neutral', P7, 'Where the field is zero', V.neutral, [
    S("Element two. Planet A has nine point zero zero times ten to the twenty four kilograms, B has one point zero zero "
      "times ten to the twenty four, and they're six point zero times ten to the eight metres apart. Between them the "
      "fields cancel. Cancel G, then take the square root at once, avoiding a messy quadratic. The root masses are "
      "three to one, so r is three quarters of the separation: four point five times ten to the eight metres from A.",
      refs=['ex25q4', 'ar25q4'], covers=['G7', 'G6'], elements=[2], exam=['X25-4'],
      problem='Planet A (9.00 × 10²⁴ kg) and planet B (1.00 × 10²⁴ kg) are 6.0 × 10⁸ m apart. Where between them is the total field zero?'),
    S("Check validity. From A at four point five times ten to the eight, and from B at one point five times ten to the eight, each "
      "field is two point nine six times ten to the minus three newtons per kilogram, in opposite directions, so they cancel. And "
      "as predicted, the neutral point is much closer to the smaller mass, where the sketch's boundary curves.",
      refs=['ar25q4', 'ex25q4'], covers=['G7', 'G8'], elements=[2, 4], exam=['X25-4']),
]),
Scene('kepler', P7, 'Orbits and Kepler’s third law', V.kepler, [
    S("For a circular orbit, gravity provides the centripetal force: G M m over r squared equals four pi squared m r over T squared. "
      "The satellite's mass cancels, leaving T squared equals four pi squared r cubed over G M. That's Kepler's third law in "
      "Newtonian form, on your information sheet in the gravity and Kepler's law section. The r is the orbit radius from the "
      "centre of the central body, M is that body's mass, and T is in seconds.",
      refs=['content', 'info', 'ar24q3', 'ex24q3'], covers=['G9', 'G11', 'C2'], elements=[1, 2], exam=['X24-3']),
    S("The ratio form: for bodies orbiting the same central mass, T squared over r cubed is constant. So T one over T two, squared, "
      "equals r one over r two, cubed. This one isn't on the sheet, so learn it. You don't need G or M, so it's ideal when you're "
      "given one orbit and asked for another. Reports say the usual mistake is failing to square the periods or cube the radii.",
      refs=['content', 'ar20q5', 'ex20q5', 'ar22q4', 'ex22q4', 'ar23q6', 'ex23q6'], covers=['G10'], elements=[1, 2], exam=['X20-5', 'X22-4', 'X23-6']),
    S("A geosynchronous satellite has an orbital period equal to Earth's rotation, twenty four hours. If it orbits above the equator in "
      "the same direction, it stays above one point: geostationary. Kepler's law fixes its radius at four point two two times ten to "
      "the seven metres from Earth's centre: three point five nine times ten to the seven metres up, moving at three point zero seven "
      "kilometres per second.",
      refs=['content', 'appendix'], covers=['G11', 'K2'], elements=[1, 2, 4],
      problem='At what radius from the centre of Earth must a geosynchronous satellite orbit?'),
]),
Scene('we_orbit', P7, 'Worked example: moons of Mars', V.we_orbit, [
    S("Element two, with real moon data, which is reference data, not from TASC. Deimos orbits Mars at two point three "
      "four six times ten to the seven metres, with period one point two six two days. Phobos orbits at nine point "
      "three eight times ten to the six. Same body, so use the ratio form: one point two six two times the radius "
      "ratio to the power one and a half. That's zero point three one nine days, or seven point six six hours.",
      refs=['ex22q4', 'ar22q4', 'ex23q6', 'ar23q6', 'ex20q5', 'ar20q5'], covers=['G10', 'G11'], elements=[2], exam=['X22-4', 'X23-6', 'X20-5'],
      problem='Deimos orbits Mars at 2.346 × 10⁷ m with period 1.262 days. Phobos orbits at 9.38 × 10⁶ m. What is its period?'),
    S("Now the mass of Mars. Convert the period to seconds: one point zero nine times ten to the five. Then M is four pi squared r "
      "cubed over G T squared: six point four three times ten to the twenty three kilograms. Use the orbit radius, not the planet's "
      "radius, and each body's own period: not the asteroid's year for its probe's orbit.",
      refs=['ar24q3', 'ex24q3', 'ar22q4', 'ex22q4', 'ar20q5', 'ex20q5'], covers=['G9'], elements=[2], exam=['X24-3', 'X22-4', 'X20-5'],
      problem='Use the orbit of Deimos to find the mass of Mars.'),
    S("Check validity. That's about a tenth of Earth's mass, plausible for a much smaller planet. And putting the mass back in with "
      "the radius of Phobos gives zero point three one nine days again, matching the ratio answer. Two routes that agree are "
      "your best evidence of no error.",
      refs=['ar20q5', 'ex20q5'], covers=['G9', 'G10'], elements=[2, 4], exam=['X20-5']),
]),
Scene('grav_data', P7, 'Linearising gravity and orbit data', V.grav_data, [
    S("Element three. Here's invented data for four moons of one planet: radii of one, two, three and four times ten to the eight "
      "metres, and periods of seven point six nine, twenty one point eight, forty point zero and sixty one point six, in units of "
      "ten to the four seconds. T squared is proportional to r cubed, so plot T squared against r cubed: a straight line "
      "through the origin.",
      refs=['ex18q5', 'ar18q5'], covers=['G9', 'M4'], elements=[3], exam=['X18-5'],
      problem='Four moons have orbit radii 1.00, 2.00, 3.00 and 4.00 × 10⁸ m and periods 7.69, 21.8, 40.0 and 61.6 × 10⁴ s. What should be plotted to get a straight line?'),
    S("The gradient is four pi squared over G M. Take it from your line, using points far apart: a rise of about three point seven "
      "times ten to the eleven over a run of six point three times ten to the twenty five gives five point nine three times ten to "
      "the minus fifteen. So M is nine point nine eight times ten to the twenty five kilograms. The 2018 report gave full marks for "
      "the right mass even without the slope.",
      refs=['ar18q5', 'ex18q5'], covers=['G9'], elements=[2, 3], exam=['X18-5'],
      problem='Find the gradient of the T²–r³ graph and the mass of the planet.'),
    S("Force data works the same way. For masses of five point zero and twelve kilograms, the forces at four "
      "separations, zero point one zero to zero point two five metres, are four hundred, one hundred and seventy eight, "
      "one hundred, and sixty four nanonewtons. Plot force against one over r squared. The gradient, four point zero "
      "times ten to the minus nine, divided by sixty, gives G: six point six seven times ten to the minus eleven. Use "
      "the gradient, not one point.",
      refs=['ex19q3', 'ar19q3'], covers=['G1', 'M4'], elements=[3], exam=['X19-3'],
      problem='The force between masses of 5.0 kg and 12 kg is measured at four separations. How do you find G from a graph?'),
]),
Scene('weightless', P7, 'Weightlessness and free fall', V.weightless, [
    S("Weightlessness is a sensation. You feel weight because a surface pushes up on you. If only gravity acts, nothing pushes "
      "back, and you feel weightless, though gravity is still there. In a lift in free fall, the scales read zero: apparent weight "
      "is m times g minus a, zero when a equals g.",
      refs=['content', 'ar20q1', 'ex20q1'], covers=['G12', 'N5'], elements=[1], exam=['X20-1']),
    S("Astronauts in orbit feel weightless, yet gravity at their height is still about eighty five percent of its surface value. "
      "They're in free fall. Picture a cannon on a mountain: a faster shot lands further away. At high enough speed, the ground "
      "curves away as fast as the shot falls, and it never lands. That's an orbit.",
      refs=['content', 'appendix'], covers=['G12', 'G11', 'K2'], elements=[1, 4], anim=3,
      problem='Why do astronauts in orbit feel weightless, although gravity still acts on them?'),
]),
Scene('grav_contexts', P7, 'Gravity in unfamiliar contexts', V.grav_contexts, [
    S("Some element four contexts. A comet near a huge planet feels a stronger field on its near side than its far side, and the "
      "change isn't linear, because of r squared. So the near side accelerates more than the middle, and the middle more than the "
      "far side. The differences can pull the comet apart. In orbit, only the middle has the right speed, so it stretches.",
      refs=['ex22q6', 'ar22q6'], covers=['G6', 'G5'], elements=[1, 4], exam=['X22-6'],
      problem='Explain why a comet can break apart as it approaches a very massive planet.'),
    S("In a gravity assist, the planet's change in momentum equals the probe's, in the opposite direction, and its velocity change "
      "is negligible. Passing behind the planet speeds the probe up; passing ahead of it slows the probe down. A star orbiting an "
      "invisible object gives that object's mass, and a huge mass in a tiny region suggests a black hole. A planet very near its "
      "star is too hot for life.",
      refs=['ex19q4', 'ar19q4', 'ex19q5', 'ar19q5', 'ex23q6', 'ar23q6'], covers=['G9', 'G11', 'N8'], elements=[1, 4], exam=['X19-4', 'X19-5', 'X23-6'],
      problem='How can a planet be used to speed up or to slow down a space probe?'),
    S("The course names three contexts. Forensic ballistics predicts a projectile's path from gravity and air resistance. Artificial "
      "satellites are grouped by altitude, as low, medium or high orbit, and debris can hit working ones. And planetary motion: "
      "the ancient Earth centred model, the Sun centred models of Copernicus and Galileo, Kepler's three laws, and Newton showing "
      "that gravity explains them. Good topics for internal tasks.",
      refs=['appendix'], covers=['K1', 'K2', 'K3', 'G9'], elements=[4]),
]),
# ------------------------------------------------------------------- finish
Scene('exam_tips', P8, 'Tips for tests and the exam', V.exam_tips, [
    S("Finally, technique for tests and the exam, from what markers have reported over several years. One: for any change in "
      "momentum or vector sum, draw the vector diagram and give the direction. Two: convert before you substitute: kilometres per "
      "hour divide by three point six, kilometres to metres, days to seconds, tonnes to kilograms.",
      refs=['ar20q3', 'ar23q4', 'ar24q5', 'ar25q2', 'ar18q4', 'ar19q6', 'ar25q1']),
    S("Three: draw forces from the object, roughly to scale, with only real forces. Four: when you explain, name the law and the "
      "object, and use nouns, rather than the word it.", refs=['ar22q1', 'ar24q1', 'ar22q3', 'ar25q1']),
    S("Five: don't round in the middle, and write down the numbers you substitute, so errors can carry forward. Six: in "
      "show that questions, calculate your own value to three significant figures and use it. If you can't reach it, "
      "carry on with the value in the question.",
      refs=['ar25q5', 'ar22q5', 'ar23q2', 'ar24q2', 'ar23q5', 'ar24q6']),
    S("Thirteen: for the cosine rule on fields or momenta, use the angle inside the triangle. Fourteen: for a neutral point, cancel G "
      "and take the square root at once. Fifteen: classify a collision using kinetic energy, not momentum. Sixteen: read the mark "
      "allocation. A one mark step doesn't need a page of working, and a derive question needs each step shown.",
      refs=['ar25q4', 'ar22q2', 'ar24q4', 'ar21q6']),
]),
Scene('summary', P8, 'Summary', V.summary, [
    S("That's every part of Criterion 5. Motion is described by graphs and three equations. Projectiles split into independent "
      "parts. Forces and Newton's laws explain acceleration; momentum and impulse describe interactions, including in two "
      "dimensions. Circular motion needs a net force to the centre. Energy is conserved, and power is its rate. And gravity follows "
      "an inverse square law, giving fields, orbits and weightlessness. Practise explaining each idea in words as well as with "
      "numbers, and you'll be ready for your tests and for Section A. Good luck."),
]),
]

# --------------------------------------------------------------------------- numeric checks
_g, _G = 9.81, 6.67e-11
_rad, _deg = math.radians, math.degrees
_ME, _RE = 5.97e24, 6.37e6
# worked-example intermediate values, computed from the inputs
_vx = 22.0 * math.cos(_rad(35)); _vy = 22.0 * math.sin(_rad(35)); _tf = 2 * _vy / _g
_cx = 15.0 * math.cos(_rad(40)); _cy = 15.0 * math.sin(_rad(40))
_tc = (_cy + math.sqrt(_cy ** 2 + 2 * _g * 12.0)) / _g
_mgs = 8.50 * _g * math.sin(_rad(30)); _ff = 60.0 - _mgs
_aup = (_mgs + _ff) / 8.50; _adn = (_mgs - _ff) / 8.50; _sup = 2.40 ** 2 / (2 * _aup)
_thr = 4.20e5 * (3.00 + _g)
_pi, _pf = 0.0580 * 25.0, 0.0580 * 31.0
_dp = math.sqrt(_pi ** 2 + _pf ** 2 - 2 * _pi * _pf * math.cos(_rad(160)))
_dpa = _deg(math.atan2(_pf * math.sin(_rad(20)), _pf * math.cos(_rad(20)) + _pi))
_pt = math.hypot(70.0 * 4.00, 55.0 * 5.00)
_mdot = 1.20 * 0.250 * 9.00
_Pa = 0.5 * _mdot * 9.00 ** 2
_vcon = math.sqrt(1.20 * math.sin(_rad(30)) * _g * math.tan(_rad(30)))
_Tcon = 2 * math.pi * 1.20 * math.sin(_rad(30)) / _vcon
_acm = 4 * math.pi ** 2 * 3.39e6 / (24.6 * 3600) ** 2
_vd = 0.0250 * 40.0 / 0.500
_pe = 1200 * _g * 15.0 * math.sin(_rad(8)); _wr = 600 * 15.0
_gA = _G * 9.00e24 / 3.00e8 ** 2; _gB = _G * 1.20e25 / 4.00e8 ** 2
_rn = 6.0e8 * math.sqrt(9.0) / (math.sqrt(9.0) + 1.0)
_TD = 1.262 * 86400; _MM = 4 * math.pi ** 2 * 2.346e7 ** 3 / (_G * _TD ** 2)
_rg = (_G * _ME * 86400 ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
_Tk = [7.69e4, 21.8e4, 40.0e4, 61.6e4]; _rk = [1.00e8, 2.00e8, 3.00e8, 4.00e8]
_sl = (_Tk[3] ** 2 - _Tk[0] ** 2) / (_rk[3] ** 3 - _rk[0] ** 3)
_Gf = (400e-9 - 64e-9) / (100 - 16.0) / 60.0

CHECKS = [
    ('hiker distance', lambda: 3 + 4, 7, 1e-9),
    ('hiker speed', lambda: 7 / 2.0, 3.5, 1e-9),
    ('hiker displacement', lambda: math.hypot(3, 4), 5, 1e-9),
    ('hiker bearing', lambda: _deg(math.atan2(4, 3)), 53.13, 0.001),
    ('hiker velocity', lambda: 5 / 2.0, 2.5, 1e-9),
    ('cosine rule R', lambda: math.sqrt(25 + 64 - 2 * 5 * 8 * math.cos(_rad(120))), 11.36, 0.002),
    ('component east', lambda: 5 + 8 * math.cos(_rad(60)), 9.0, 1e-9),
    ('component north', lambda: 8 * math.sin(_rad(60)), 6.93, 0.001),
    ('van area 1', lambda: 0.5 * 8 * 20, 80, 1e-9),
    ('van area 2', lambda: 10 * 20, 200, 1e-9),
    ('van area 3', lambda: 0.5 * 5 * 20, 50, 1e-9),
    ('van displacement', lambda: 80 + 200 + 50, 330, 1e-9),
    ('van average velocity', lambda: 330 / 23.0, 14.3, 0.005),
    ('van a1', lambda: 20 / 8.0, 2.5, 1e-9),
    ('van a3', lambda: -20 / 5.0, -4.0, 1e-9),
    ('stone v squared', lambda: 12.0 ** 2 + 2 * _g * 30.0, 732.6, 1e-6),
    ('stone v', lambda: math.sqrt(732.6), 27.07, 0.001),
    ('stone t', lambda: (math.sqrt(732.6) + 12.0) / _g, 3.98, 0.001),
    ('stone t up', lambda: 12.0 / _g, 1.22, 0.003),
    ('stone h up', lambda: 12.0 ** 2 / (2 * _g), 7.34, 0.001),
    ('stone fall height', lambda: 30.0 + 12.0 ** 2 / (2 * _g), 37.3, 0.002),
    ('stone t down', lambda: (math.sqrt(732.6) + 12.0) / _g - 12.0 / _g, 2.76, 0.002),
    ('stone half g t2', lambda: 0.5 * _g * ((math.sqrt(732.6) + 12.0) / _g - 12.0 / _g) ** 2, 37.3, 0.002),
    ('kick speed', lambda: 79.2 / 3.6, 22.0, 1e-9),
    ('kick vx', lambda: _vx, 18.0, 0.002),
    ('kick vy', lambda: _vy, 12.6, 0.002),
    ('kick time', lambda: _tf, 2.57, 0.002),
    ('kick range', lambda: _vx * _tf, 46.4, 0.001),
    ('kick height', lambda: _vy ** 2 / (2 * _g), 8.12, 0.001),
    ('cliff vx', lambda: _cx, 11.5, 0.002),
    ('cliff vy', lambda: _cy, 9.64, 0.001),
    ('cliff t up', lambda: _cy / _g, 0.983, 0.001),
    ('cliff h up', lambda: _cy ** 2 / (2 * _g), 4.74, 0.001),
    ('cliff fall', lambda: 12.0 + _cy ** 2 / (2 * _g), 16.7, 0.003),
    ('cliff t down', lambda: math.sqrt(2 * (12.0 + _cy ** 2 / (2 * _g)) / _g), 1.85, 0.002),
    ('cliff t', lambda: _tc, 2.83, 0.001),
    ('cliff t sum', lambda: _cy / _g + math.sqrt(2 * (12.0 + _cy ** 2 / (2 * _g)) / _g), 2.83, 0.001),
    ('cliff range', lambda: _cx * _tc, 32.5, 0.001),
    ('cliff vy land', lambda: _cy - _g * _tc, -18.1, 0.002),
    ('cliff speed', lambda: math.hypot(_cx, _cy - _g * _tc), 21.5, 0.002),
    ('cliff angle', lambda: _deg(math.atan((_g * _tc - _cy) / _cx)), 57.6, 0.001),
    ('cliff energy speed', lambda: math.sqrt(15.0 ** 2 + 2 * _g * 12.0), 21.5, 0.002),
    ('derive u squared', lambda: 0.5 * _g * 90.0 / (math.sin(_rad(30)) * math.cos(_rad(30))), 1019.5, 0.001),
    ('derive u', lambda: math.sqrt(0.5 * _g * 90.0 / (math.sin(_rad(30)) * math.cos(_rad(30)))), 31.9, 0.002),
    ('half g', lambda: _g / 2, 4.905, 1e-9),
    ('mars range ratio', lambda: _g / 3.72, 2.64, 0.002),
    ('crate weight component', lambda: _mgs, 41.7, 0.002),
    ('crate friction', lambda: _ff, 18.3, 0.002),
    ('crate decel', lambda: _aup, 7.06, 0.001),
    ('crate net up', lambda: _mgs + _ff, 60.0, 1e-9),
    ('crate distance', lambda: _sup, 0.408, 0.001),
    ('crate a down', lambda: _adn, 2.75, 0.001),
    ('crate return speed', lambda: math.sqrt(2 * _adn * _sup), 1.50, 0.002),
    ('lift reading force', lambda: 76.5 * _g, 750.5, 0.001),
    ('lift weight', lambda: 70.0 * _g, 686.7, 0.001),
    ('lift net', lambda: 76.5 * _g - 70.0 * _g, 63.8, 0.001),
    ('lift a', lambda: (76.5 - 70.0) * _g / 70.0, 0.911, 0.001),
    ('rocket thrust', lambda: _thr, 5.38e6, 0.001),
    ('rocket later mass', lambda: _thr / (12.0 + _g), 2.47e5, 0.002),
    ('rocket net', lambda: 4.20e5 * 3.00, 1.26e6, 0.001),
    ('rocket weight', lambda: 4.20e5 * _g, 4.12e6, 0.001),
    ('rocket thrust minus weight', lambda: _thr - 4.20e5 * _g, 1.26e6, 0.001),
    ('rocket ratio', lambda: _thr / (4.20e5 * _g), 1.31, 0.004),
    ('kick pulse impulse', lambda: 0.5 * 300 * 0.040, 6.00, 1e-9),
    ('kick pulse speed', lambda: 0.5 * 300 * 0.040 / 0.200, 30.0, 1e-9),
    ('bounce p initial', lambda: _pi, 1.45, 1e-9),
    ('bounce p final', lambda: _pf, 1.798, 1e-9),
    ('bounce p final rounded', lambda: _pf, 1.80, 0.002),
    ('bounce dp', lambda: _dp, 3.20, 0.001),
    ('bounce dp unrounded', lambda: _dp, 3.1992, 1e-4),
    ('bounce dy', lambda: _pf * math.sin(_rad(20)), 0.615, 0.001),
    ('bounce direction', lambda: _dpa, 11.1, 0.002),
    ('bounce from initial', lambda: 180 - _dpa, 169, 0.002),
    ('bounce force', lambda: _dp / 5.00e-3, 640, 0.001),
    ('puck vB', lambda: math.sqrt(1.80 ** 2 - 1.08 ** 2), 1.44, 1e-9),
    ('puck angle A', lambda: _deg(math.acos(1.08 / 1.80)), 53.1, 0.001),
    ('puck angle B', lambda: 90 - _deg(math.acos(1.08 / 1.80)), 36.9, 0.001),
    ('puck KE before', lambda: 0.5 * 0.200 * 1.80 ** 2, 0.324, 1e-9),
    ('puck KE after', lambda: 0.5 * 0.200 * (1.08 ** 2 + 1.44 ** 2), 0.324, 1e-9),
    ('skater north p', lambda: 70.0 * 4.00, 280, 1e-9),
    ('skater east p', lambda: 55.0 * 5.00, 275, 1e-9),
    ('skater total p', lambda: _pt, 392, 0.002),
    ('skater total p unrounded', lambda: _pt, 392.46, 1e-4),
    ('skater v', lambda: _pt / 125.0, 3.14, 0.001),
    ('skater angle', lambda: _deg(math.atan2(275, 280)), 44.5, 0.001),
    ('skater KE before', lambda: 0.5 * 70.0 * 16.0 + 0.5 * 55.0 * 25.0, 1250, 0.003),
    ('skater KE after', lambda: 0.5 * 125.0 * (_pt / 125.0) ** 2, 616, 0.001),
    ('skater KE lost percent', lambda: 100 * (1 - 616.1 / 1247.5), 50.6, 0.001),
    ('launcher recoil', lambda: 0.0600 * 90.0 / 4.50, 1.20, 1e-9),
    ('launcher KE', lambda: 0.5 * 0.0600 * 90.0 ** 2 + 0.5 * 4.50 * 1.20 ** 2, 246, 0.002),
    ('ion force', lambda: 5.0e-6 * 3.0e4, 0.15, 1e-9),
    ('ion a', lambda: 0.15 / 500, 3.0e-4, 1e-9),
    ('ion year dv', lambda: 3.0e-4 * 365 * 24 * 3600, 9.5e3, 0.01),
    ('drone volume', lambda: 0.250 * 9.00, 2.25, 1e-9),
    ('drone mass flow', lambda: _mdot, 2.70, 1e-9),
    ('drone force', lambda: _mdot * 9.00, 24.3, 1e-9),
    ('drone mass', lambda: _mdot * 9.00 / _g, 2.48, 0.002),
    ('drone power', lambda: _Pa, 109, 0.004),
    ('drone efficiency', lambda: 100 * _Pa / 280.0, 39.1, 0.002),
    ('bob tension', lambda: 0.250 * _g / math.cos(_rad(30)), 2.83, 0.001),
    ('bob net force', lambda: 0.250 * _g * math.tan(_rad(30)), 1.42, 0.003),
    ('bob radius', lambda: 1.20 * math.sin(_rad(30)), 0.600, 1e-9),
    ('bob speed', lambda: _vcon, 1.84, 0.002),
    ('bob period', lambda: _Tcon, 2.05, 0.003),
    ('bob acceleration', lambda: _g * math.tan(_rad(30)), 5.66, 0.001),
    ('bob acceleration via T', lambda: 4 * math.pi ** 2 * 0.600 / _Tcon ** 2, 5.66, 0.001),
    ('glider lift', lambda: 600 * _g / math.cos(_rad(25)), 6.49e3, 0.001),
    ('glider net', lambda: 600 * _g * math.tan(_rad(25)), 2.74e3, 0.002),
    ('glider radius', lambda: 40.0 ** 2 / (_g * math.tan(_rad(25))), 350, 0.001),
    ('earth equator speed', lambda: 2 * math.pi * 6.378e6 / 86400, 464, 0.001),
    ('earth equator a', lambda: 4 * math.pi ** 2 * 6.378e6 / 86400 ** 2, 0.0337, 0.001),
    ('mars equator a', lambda: _acm, 0.0171, 0.003),
    ('mars equator percent', lambda: 100 * _acm / 3.72, 0.46, 0.005),
    ('sled work', lambda: 80.0 * 12.0 * math.cos(_rad(35)), 786, 0.001),
    ('launcher area 1', lambda: 0.5 * 0.10 * 60, 3.0, 1e-9),
    ('launcher area 2', lambda: 0.5 * (60 + 100) * 0.20, 16.0, 1e-9),
    ('launcher area 3', lambda: 0.5 * (100 + 90) * 0.10, 9.5, 1e-9),
    ('launcher work', lambda: 3.0 + 16.0 + 9.5, 28.5, 1e-9),
    ('launcher energy', lambda: 0.70 * 28.5, 19.95, 1e-9),
    ('launcher speed', lambda: math.sqrt(2 * 19.95 / 0.0450), 29.8, 0.001),
    ('dart v', lambda: _vd, 2.00, 1e-9),
    ('dart KE before', lambda: 0.5 * 0.0250 * 40.0 ** 2, 20.0, 1e-9),
    ('dart KE after', lambda: 0.5 * 0.500 * _vd ** 2, 1.00, 1e-9),
    ('dart KE lost', lambda: 20.0 - 1.00, 19.0, 1e-9),
    ('dart KE lost percent', lambda: 100 * 19.0 / 20.0, 95.0, 1e-9),
    ('dart height', lambda: _vd ** 2 / (2 * _g), 0.204, 0.001),
    ('dart height from one joule', lambda: 1.00 / (0.500 * _g), 0.204, 0.001),
    ('dart height from 20 J', lambda: 20.0 / (0.500 * _g) / (1.00 / (0.500 * _g)), 20, 1e-9),
    ('car height per s', lambda: 15.0 * math.sin(_rad(8)), 2.09, 0.002),
    ('car PE per s', lambda: _pe, 2.46e4, 0.002),
    ('car resistance work', lambda: _wr, 9.00e3, 1e-9),
    ('car total', lambda: _pe + _wr, 3.36e4, 0.001),
    ('car efficiency', lambda: 100 * (_pe + _wr) / 45.0e3, 74.6, 0.001),
    ('car lost', lambda: 45.0 - (_pe + _wr) / 1e3, 11.4, 0.005),
    ('satellite a_c', lambda: 4 * math.pi ** 2 * 7.20e6 / 6.08e3 ** 2, 7.69, 0.002),
    ('satellite inverse square', lambda: _g * (_RE / 7.20e6) ** 2, 7.68, 0.002),
    ('altitude r', lambda: _RE + 560e3, 6.93e6, 0.001),
    ('altitude g ratio', lambda: _g * (_RE / (_RE + 560e3)) ** 2, 8.29, 0.001),
    ('altitude g GM', lambda: _G * _ME / (_RE + 560e3) ** 2, 8.29, 0.001),
    ('altitude fraction', lambda: 100 * _g * (_RE / (_RE + 560e3)) ** 2 / _g, 85, 0.01),
    ('field A', lambda: _gA, 6.67e-3, 0.001),
    ('field B', lambda: _gB, 5.00e-3, 0.001),
    ('field total', lambda: math.hypot(_gA, _gB), 8.34e-3, 0.001),
    ('field angle', lambda: _deg(math.atan(_gB / _gA)), 36.9, 0.001),
    ('neutral r', lambda: _rn, 4.5e8, 1e-9),
    ('neutral r B', lambda: 6.0e8 - _rn, 1.5e8, 1e-9),
    ('neutral g from A', lambda: _G * 9.00e24 / _rn ** 2, 2.96e-3, 0.002),
    ('neutral g from B', lambda: _G * 1.00e24 / (6.0e8 - _rn) ** 2, 2.96e-3, 0.002),
    ('geo r', lambda: _rg, 4.22e7, 0.002),
    ('geo altitude', lambda: _rg - _RE, 3.59e7, 0.002),
    ('geo speed', lambda: 2 * math.pi * _rg / 86400, 3.07e3, 0.002),
    ('phobos T days', lambda: 1.262 * (9.38e6 / 2.346e7) ** 1.5, 0.319, 0.002),
    ('phobos T hours', lambda: 24 * 1.262 * (9.38e6 / 2.346e7) ** 1.5, 7.66, 0.002),
    ('deimos T seconds', lambda: _TD, 1.09e5, 0.002),
    ('mars mass', lambda: _MM, 6.43e23, 0.001),
    ('mars vs earth', lambda: _MM / _ME, 0.107, 0.01),
    ('phobos T from mass', lambda: 2 * math.pi * math.sqrt(9.38e6 ** 3 / (_G * _MM)) / 86400, 0.319, 0.002),
    ('kepler slope', lambda: _sl, 5.93e-15, 0.002),
    ('kepler rise', lambda: _Tk[3] ** 2 - _Tk[0] ** 2, 3.7e11, 0.02),
    ('kepler run', lambda: _rk[3] ** 3 - _rk[0] ** 3, 6.3e25, 1e-9),
    ('kepler mass', lambda: 4 * math.pi ** 2 / (_G * _sl), 9.98e25, 0.002),
    ('force gradient', lambda: (400e-9 - 64e-9) / (100 - 16.0), 4.0e-9, 1e-9),
    ('force G', lambda: _Gf, 6.67e-11, 0.002),
    # Unrounded values shown on screen above each rounded answer.
    ('shown: kick vx', lambda: _vx, 18.021, 1e-4),
    ('shown: kick vy', lambda: _vy, 12.619, 1e-4),
    ('shown: kick time', lambda: _tf, 2.5726, 1e-4),
    ('shown: kick range', lambda: _vx * _tf, 46.362, 1e-4),
    ('shown: kick height', lambda: _vy ** 2 / (2 * _g), 8.1158, 1e-4),
    ('shown: stone v', lambda: math.sqrt(732.6), 27.067, 1e-4),
    ('shown: stone t', lambda: (math.sqrt(732.6) + 12.0) / _g, 3.9823, 1e-4),
    ('shown: cliff t', lambda: _tc, 2.8301, 1e-4),
    ('shown: cliff range', lambda: _cx * _tc, 32.520, 1e-4),
    ('shown: cliff speed', lambda: math.hypot(_cx, _cy - _g * _tc), 21.458, 1e-4),
    ('shown: cliff angle', lambda: _deg(math.atan((_g * _tc - _cy) / _cx)), 57.622, 1e-4),
    ('shown: derive u', lambda: math.sqrt(0.5 * _g * 90.0 / (math.sin(_rad(30)) * math.cos(_rad(30)))), 31.929, 1e-4),
    ('shown: crate friction', lambda: _ff, 18.308, 1e-4),
    ('shown: crate decel', lambda: _aup, 7.0588, 1e-4),
    ('shown: crate distance', lambda: _sup, 0.40800, 1e-4),
    ('shown: crate a down', lambda: _adn, 2.7512, 1e-4),
    ('shown: crate return', lambda: math.sqrt(2 * _adn * _sup), 1.4983, 1e-4),
    ('shown: lift a', lambda: (76.5 - 70.0) * _g / 70.0, 0.91093, 1e-4),
    ('shown: rocket thrust', lambda: _thr, 5.3802e6, 1e-4),
    ('shown: rocket later mass', lambda: _thr / (12.0 + _g), 2.4669e5, 1e-4),
    ('shown: bounce dp', lambda: _dp, 3.1992, 1e-4),
    ('shown: bounce force', lambda: _dp / 5.00e-3, 639.85, 1e-4),
    ('shown: skater v', lambda: _pt / 125.0, 3.1397, 1e-4),
    ('shown: drone mass', lambda: _mdot * 9.00 / _g, 2.4771, 1e-4),
    ('shown: drone power', lambda: _Pa, 109.35, 1e-4),
    ('shown: drone efficiency', lambda: 100 * _Pa / 280.0, 39.054, 1e-4),
    ('shown: bob tension', lambda: 0.250 * _g / math.cos(_rad(30)), 2.8319, 1e-4),
    ('shown: bob speed', lambda: _vcon, 1.8434, 1e-4),
    ('shown: bob period', lambda: _Tcon, 2.0450, 1e-4),
    ('shown: glider lift', lambda: 600 * _g / math.cos(_rad(25)), 6494.5, 1e-4),
    ('shown: glider net', lambda: 600 * _g * math.tan(_rad(25)), 2744.7, 1e-4),
    ('shown: glider radius', lambda: 40.0 ** 2 / (_g * math.tan(_rad(25))), 349.77, 1e-4),
    ('shown: mars a', lambda: _acm, 0.017064, 1e-4),
    ('shown: sled work', lambda: 80.0 * 12.0 * math.cos(_rad(35)), 786.39, 1e-4),
    ('shown: launcher speed', lambda: math.sqrt(2 * 19.95 / 0.0450), 29.777, 1e-4),
    ('shown: dart height', lambda: _vd ** 2 / (2 * _g), 0.20387, 1e-4),
    ('shown: car PE', lambda: _pe, 24575.2, 1e-4),
    ('shown: car total', lambda: _pe + _wr, 33575.2, 1e-4),
    ('shown: car efficiency', lambda: 100 * (_pe + _wr) / 45.0e3, 74.611, 1e-4),
    ('shown: satellite a_c', lambda: 4 * math.pi ** 2 * 7.20e6 / 6.08e3 ** 2, 7.6892, 1e-4),
    ('shown: satellite inverse square', lambda: _g * (_RE / 7.20e6) ** 2, 7.6786, 1e-4),
    ('shown: altitude g', lambda: _g * (_RE / (_RE + 560e3)) ** 2, 8.2886, 1e-4),
    ('shown: field total', lambda: math.hypot(_gA, _gB), 8.3375e-3, 1e-4),
    ('shown: mars mass', lambda: _MM, 6.4279e23, 1e-4),
    ('shown: phobos T', lambda: 1.262 * (9.38e6 / 2.346e7) ** 1.5, 0.31906, 1e-4),
    ('shown: kepler mass', lambda: 4 * math.pi ** 2 / (_G * _sl), 9.982e25, 1e-3),
    ('shown: geo r', lambda: _rg, 4.2227e7, 1e-4),
]

# Report references that no slide cites are left out of the reference list.
_used = {r for sc in SCENES for st in sc.steps for r in st.refs} | {t[1] for t in EXAM_TOPICS.values()} \
    | {t[1] for t in SYLLABUS.values()} | {t[1] for t in ELEMENTS.values()} | {'info'}
REFS = {k: r for k, r in REFS.items() if k in _used}

VIDEO = Video(
    id='PHY415115_C5_newtonian_mechanics',
    course=COURSE, course_name='Physics', module=MODULE,
    module_name='Criterion 5: Identify and apply principles of Newtonian mechanics including gravitational fields',
    title='Criterion 5: Newtonian mechanics and gravitational fields, complete revision',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Motion in a Straight Line, Momentum, Force, Centripetal Force'),
    checks=CHECKS,
    thumbnail=V.thumbnail,
    allowed_overlaps=['identify and apply principles of newtonian mechanics including gravitational fields'],
    keywords=['displacement', 'velocity', 'acceleration', 'projectile', 'free body diagram', 'net force', 'Newton’s first law',
              'Newton’s second law', 'Newton’s third law', 'momentum', 'impulse', 'conservation of momentum', 'elastic', 'inelastic',
              'centripetal', 'work', 'kinetic energy', 'potential energy', 'conservation of energy', 'power', 'efficiency',
              'gravitational field', 'field strength', 'inverse square', 'Kepler', 'orbit', 'geostationary', 'weightlessness',
              'terminal velocity', 'vector'],
    description=('A complete revision explainer for TASC Physics (PHY415115) Criterion 5: Newtonian mechanics including '
                 'gravitational fields. For class tests and the end-of-year exam (Section A). Formulas from the TASC '
                 'information sheet are labelled on screen.'),
)
