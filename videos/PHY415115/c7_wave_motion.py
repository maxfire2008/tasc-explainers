"""PHY415115 Physics, Criterion 7: Identify and apply general principles of wave motion.

Worked example of a full video spec.  Build with:
    python -m explainer check   videos/PHY415115/c7_wave_motion.py
    python -m explainer preview videos/PHY415115/c7_wave_motion.py
    python -m explainer all     videos/PHY415115/c7_wave_motion.py

TODO for the agent before rendering (see CLAUDE.md, "Before you render"):
  * run `python -m explainer sources PHY415115`, then fill every PDF `page=` below from the cached files
  * confirm the info-sheet section name and that each sheet_eq formula is really on the sheet
  * add exam_topics for the 2021 and 2022 papers (only 2023-2025 were reviewed when this was written)
  * confirm element order against the standards table in the course document
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
# Source NAMES from sources/PHY415115/content.csv (list them with: python -m explainer sources PHY415115).
COURSE_DOC = 'phy415115-9.html'
INFO = 'PHY415115-Physics-Information-sheet.pdf'
SPEC = 'PHY415115-Physics-External-Assessment-Specifications.pdf'


def exam(y, q, page=None):
    return Ref(f'PHY415115-Physics-TASC-Exam-Paper-{y}.pdf', f'{y} exam, Section C, Question {q}', page)


def report(y, q, page=None):
    return Ref(f'PHY415115-Physics-Assessment-Report-{y}.pdf', f'{y} assessment report, Criterion 7, Question {q}', page)


REFS = {
    'standards': Ref(COURSE_DOC, 'Course document, Criterion 7 standards (element table)'),
    'content': Ref(COURSE_DOC, 'Course document, content: Unit 2 Waves (wave interactions, wave interference)'),
    'appendix': Ref(COURSE_DOC, 'Course document, Appendix 1: contexts (earthquakes & tsunamis; noise & acoustic design; wave theory of light)'),
    'info': Ref(INFO, 'Information sheet, Oscillations, Waves section', page=2),
    'spec': Ref(SPEC, 'External assessment specifications, Section C', page=None),
    'ex23q13': exam(2023, 13), 'ex23q14': exam(2023, 14), 'ex23q15': exam(2023, 15), 'ex23q16': exam(2023, 16),
    'ex23q17': exam(2023, 17), 'ex23q18': exam(2023, 18),
    'ex24q13': exam(2024, 13), 'ex24q14': exam(2024, 14), 'ex24q15': exam(2024, 15), 'ex24q16': exam(2024, 16),
    'ex24q17': exam(2024, 17), 'ex24q18': exam(2024, 18),
    'ex25q12': exam(2025, 12), 'ex25q13': exam(2025, 13), 'ex25q14': exam(2025, 14), 'ex25q15': exam(2025, 15),
    'ex25q16': exam(2025, 16), 'ex25q17': exam(2025, 17),
    'ar23q13': report(2023, 13), 'ar23q14': report(2023, 14), 'ar23q15': report(2023, 15), 'ar23q16': report(2023, 16),
    'ar23q17': report(2023, 17), 'ar23q18': report(2023, 18),
    'ar24q13': report(2024, 13), 'ar24q14': report(2024, 14), 'ar24q15': report(2024, 15), 'ar24q16': report(2024, 16),
    'ar24q17': report(2024, 17), 'ar24q18': report(2024, 18),
}

# --------------------------------------------------------------------------- coverage targets
# Every dot point of the course content for this criterion.  check fails if one is uncovered.
SYLLABUS = {
    'W1': ('Waves are periodic oscillations that transfer energy', 'content'),
    'W2': ('Transverse and longitudinal waves', 'content'),
    'W3': ('Simple harmonic motion underlies wave oscillation', 'content'),
    'W4': ('Sound is a mechanical, longitudinal wave', 'content'),
    'W5': ('Light is an electromagnetic wave: transverse, travels through a vacuum', 'content'),
    'W6': ('Relationships between wavelength, frequency, period, amplitude and wave speed', 'content'),
    'W7': ('Reflection and transmission at fixed and free boundaries in 1D, incl. phase change', 'content'),
    'W8': ('Reflection in two dimensions (rays, wavefronts)', 'content'),
    'W9': ("Refraction and Snell's law", 'content'),
    'W10': ('Relative and absolute refractive index', 'content'),
    'W11': ('Total internal reflection and critical angle', 'content'),
    'W12': ('Superposition, incl. 1D pulse diagrams', 'content'),
    'W13': ('Beats', 'content'),
    'W14': ('Resonance', 'content'),
    'W15': ('Standing waves in strings and pipes: nodes, antinodes, harmonics, overtones', 'content'),
    'W16': ('Wave speed on a stretched wire from tension and linear density', 'content'),
    'W17': ('Two-source interference: coherence, path difference, fringe width', 'content'),
    'W18': ('Diffraction (qualitative): greater for longer wavelengths', 'content'),
    'W19': ('Polarisation of transverse and electromagnetic waves', 'content'),
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
]

# --------------------------------------------------------------------------- scenes
S = Step
SCENES = [
Scene('intro', P0, 'Introduction: how Criterion 7 is assessed', V.intro, [
    S("Welcome. This video is a complete briefing on Criterion 7 of TASC Physics, PHY415115: identify and apply general "
      "principles of wave motion. Use it to revise for your class tests on waves and for the end of year exam. By the end, "
      "you should know every part of the waves content, which formulas are on your information sheet and where to find "
      "them, and the traps that examiners keep seeing in student answers.", refs=['standards'], anim=4),
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
    S("Light is different. It's an electromagnetic wave: oscillating electric and magnetic fields, at right angles to each "
      "other and to the direction of travel. So light behaves as a transverse wave, and it needs no medium. It crosses the "
      "vacuum of space at the speed of light, three point zero zero times ten to the eight metres per second. That value "
      "is on your information sheet, in the list of constants.", refs=['content'], covers=['W5'], elements=[1], anim=2),
]),
Scene('shm', P1, 'Simple harmonic motion', V.shm, [
    S("Underneath every wave is simple harmonic motion. Each particle in the medium oscillates like a mass on a spring. If "
      "you follow a point moving steadily around a circle, and watch only its height, you get exactly the same motion. "
      "Plotted against time, it traces out a sine curve.", refs=['content'], covers=['W3'], elements=[1], anim=4),
    S("We can write the displacement as y equals A sine omega t, where A is the amplitude, the maximum displacement from "
      "rest. Omega is the angular frequency. The relationship omega equals two pi f, which also equals two pi over T, is on "
      "your information sheet, in the oscillations and waves section.", refs=['content'], covers=['W3'], elements=[1], anim=4),
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
    S("And wave speed, v, links them all together: v equals f lambda, also on the information sheet. In one period, the "
      "wave moves forward exactly one wavelength. So the speed is wavelength divided by period, which is f lambda.",
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
      "eighteen metres apart.", covers=['W6'], elements=[3]),
    S("So the frequency is one over four, which is zero point two five hertz. And the wave speed is f lambda: zero point "
      "two five times eighteen, which is four point five metres per second. Notice that we needed both graphs: one for the "
      "period, and one for the wavelength.", covers=['W6'], elements=[2, 3]),
    S("You might also be asked for the velocity of the particle itself, at some moment. That's the gradient of the "
      "displacement time graph. Draw a tangent, pick two well separated points on it, and calculate rise over run. Here "
      "it's about zero point four four metres per second. Show the tangent and your points clearly, and include units.",
      covers=['W6'], elements=[3], exam=['X23-15'], refs=['ar23q15']),
]),
Scene('direction', P1, 'Which way is the wave travelling?', V.direction, [
    S("A common question: which way is the wave travelling? A snapshot on its own can't tell you, because a wave moving "
      "left and a wave moving right can look identical at one instant. You need to know how one point is moving next, for "
      "example from its displacement time graph.", covers=['W6'], elements=[3], exam=['X25-15'], refs=['ex25q15']),
    S("Here's a reliable trick. Imagine shifting the snapshot a tiny distance in one direction, say to the right. Then see "
      "where point P must go to sit on the shifted curve. For this snapshot, shifting right would make P move down.",
      covers=['W6'], elements=[3]),
    S("Now check P's displacement time graph. Just after time zero, P moves down. That matches the right shift, so the "
      "wave is travelling to the right. If P had moved up instead, the wave would be travelling to the left. Always say "
      "which graph features you used, because that's the analysis that element three rewards.",
      covers=['W6'], elements=[3, 4], exam=['X25-15']),
]),
Scene('pulses', P2, 'Pulses at fixed and free ends, and between strings', V.pulses, [
    S("Part two. What happens when a wave reaches a boundary? Start with a pulse on a string tied to a wall. This is a "
      "fixed end. When the pulse arrives, the string pulls up on the wall, and the wall pulls down on the string. So the "
      "reflected pulse comes back inverted. We call that a phase change of half a cycle, or one hundred and eighty "
      "degrees.", refs=['content'], covers=['W7'], elements=[1], exam=['X24-16'], anim=4),
    S("Now a free end. The end of the string is attached to a light ring that slides freely up and down a pole. The end "
      "overshoots, and the reflected pulse comes back the right way up. There's no phase change.",
      refs=['content'], covers=['W7'], elements=[1], anim=4),
    S("Most boundaries are in between. Here, a light string joins a heavier string. Part of the pulse is transmitted, and "
      "part is reflected. Because the heavy string behaves a bit like a fixed end, the reflected pulse is inverted. The "
      "transmitted pulse stays upright, but it travels more slowly, so it's squashed into a shorter length. Both pulses are "
      "smaller than the original, because the energy is shared between them.",
      refs=['content', 'ex24q16'], covers=['W7'], elements=[1, 4], exam=['X24-16'], anim=4),
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
      "information sheet formula next.", covers=['W16'], elements=[2]),
    S("v equals the square root of eighty over zero point zero zero eight, from the information sheet. That's the square "
      "root of ten thousand, which is one hundred metres per second.", covers=['W16'], elements=[2]),
    S("In a lab, the tension often comes from a hanging mass, as on a sonometer. The tension equals m g, the weight of the "
      "mass. Add more mass, the tension rises, the wave speed rises, and so does the pitch. Working backwards from a "
      "required frequency, you can find the mass needed. The string speed formula is still the one on your information "
      "sheet.", covers=['W16'], elements=[2, 4], exam=['X25-13'], refs=['ex25q13']),
]),
Scene('huygens', P2, "Wavefronts and Huygens' principle", V.huygens, [
    S("In two dimensions we draw wavefronts: lines joining points that are in phase, such as along each crest. Huygens' "
      "principle says that every point on a wavefront acts as a source of small circular wavelets. The new wavefront is "
      "the line that touches all of those wavelets. Rays show the direction of travel, at right angles to the wavefronts.",
      refs=['content'], covers=['W8'], elements=[1], exam=['X24-14']),
    S("So when a wave passes through a small gap, or spreads from a point source, the wavefronts become circles centred on "
      "the gap. In the same medium the speed doesn't change, so neither does the wavelength. Draw the circles evenly "
      "spaced, with the same spacing as the incoming waves. That's a mark examiners look for.",
      refs=['ar24q14'], covers=['W8', 'W18'], elements=[1], exam=['X24-14']),
]),
Scene('refraction', P2, "Reflection, refraction and Snell's law", V.refraction, [
    S("We measure every angle from the normal: the line perpendicular to the surface. The law of reflection says that the "
      "angle of incidence equals the angle of reflection. It's on your information sheet, in the oscillations and waves "
      "section, as theta i equals theta r.", refs=['content'], covers=['W8'], elements=[1]),
    S("Refraction is the change in direction when a wave crosses into a medium where it travels at a different speed. The "
      "frequency stays the same, so if the speed drops, the wavelength gets shorter. The part of each wavefront that "
      "crosses first slows down first, so the wavefront swings around. Slowing down bends the ray towards the normal. "
      "Speeding up bends it away.", refs=['content'], covers=['W9'], elements=[1], anim=2),
    S("For light, we describe a medium by its absolute refractive index, n. That's the speed of light in a vacuum, "
      "divided by the speed of light in the medium. Glass has n of about one point five, so light travels at about two "
      "thirds of its vacuum speed in glass. A higher n means slower light.", refs=['content'], covers=['W10'],
      elements=[1], anim=2),
    S("Snell's law connects the angles. On your information sheet, in the oscillations and waves section, it's written as "
      "n one sine theta i equals n two sine theta r. Equivalently, the ratio of the sines equals the ratio of the speeds, v "
      "one over v two, which equals n two over n one. That ratio, n two over n one, is the relative refractive index, going "
      "from medium one into medium two.", refs=['content'], covers=['W9', 'W10'], elements=[1], anim=2),
]),
Scene('tir', P2, 'Critical angle and total internal reflection', V.tir, [
    S("When light goes from a slower medium into a faster one, like glass into air, it bends away from the normal. As you "
      "increase the angle of incidence, the refracted ray swings closer and closer to the surface.", covers=['W11'],
      elements=[1], anim=6),
    S("At the critical angle, the refracted ray runs exactly along the surface, at ninety degrees to the normal. Put theta "
      "r equals ninety degrees into Snell's law, and you get: sine of the critical angle equals n two over n one. This one "
      "is not on the sheet, so learn it, or derive it from Snell's law.", covers=['W11'], elements=[1]),
    S("Beyond the critical angle, no light is refracted at all. All of it reflects back into the first medium. That's "
      "total internal reflection. It only happens going from a higher n to a lower n. It's how optical fibres keep light "
      "trapped over long distances.", covers=['W11'], elements=[1]),
    S("Tip: when you explain this, name it. It's not enough to say the angle is bigger than the critical angle. Say that "
      "the angle of incidence exceeds the critical angle, so total internal reflection occurs.", refs=['ar23q17'],
      covers=['W11'], elements=[1], exam=['X23-17']),
]),
Scene('we_refraction', P2, 'Worked example: glass to water', V.we_refraction, [
    S("Let's do a worked example for element two. Light travelling through glass, with n equals one point five two, meets "
      "a boundary with water, n equals one point three three, at an angle of incidence of fifty five degrees. Does it "
      "escape into the water?", covers=['W9', 'W11'], elements=[2]),
    S("First, find the critical angle. Sine theta c equals one point three three over one point five two, which is zero "
      "point eight seven five. So the critical angle is sixty one point zero degrees.", covers=['W11'], elements=[2]),
    S("Fifty five degrees is less than the critical angle, so the light does refract into the water. Snell's law, from the "
      "information sheet, gives sine theta r equals one point five two times sine fifty five degrees, all divided by one "
      "point three three. That's zero point nine three six, so theta r is about sixty nine point four degrees. It bends away "
      "from the normal, as it should, because it's speeding up.", covers=['W9'], elements=[2]),
    S("And if the angle of incidence were increased to sixty five degrees? That's above the critical angle, so there'd be "
      "total internal reflection. Notice how to check validity here, which is what an A rating needs. A refracted angle "
      "bigger than the incident angle makes sense when light speeds up. And if your calculator ever gives a sine bigger "
      "than one, that's Snell's law telling you there's total internal reflection.", covers=['W11'], elements=[2, 4],
      exam=['X24-15']),
]),
Scene('two_surfaces', P2, 'Refraction at two surfaces', V.two_surfaces, [
    S("Many questions send light through two surfaces, like a block or a prism. Here, light in air hits the top of a glass "
      "block, n equals one point five zero, at forty degrees. Snell's law gives a refracted angle of twenty five point four "
      "degrees inside the glass.", covers=['W9'], elements=[2], exam=['X24-15', 'X23-17'], refs=['ex24q15', 'ex23q17']),
    S("The ray now hits the side face. Because the side is at right angles to the top, the normals are at right angles "
      "too, so the new angle of incidence is ninety degrees minus twenty five point four, which is sixty four point six "
      "degrees. Missing this ninety minus theta step is a common way to lose a mark.", refs=['ar24q15'], covers=['W9'],
      elements=[2], exam=['X24-15']),
    S("The critical angle for glass to air is forty one point eight degrees. Sixty four point six is bigger, so there's "
      "total internal reflection at the side face. The method always works: draw the normal at every surface, use the "
      "angle sums in the triangle, then apply Snell's law or the critical angle again.", covers=['W11'], elements=[2],
      exam=['X23-17']),
]),
Scene('dispersion', P2, 'Dispersion in a prism', V.dispersion, [
    S("One more refraction idea: dispersion. In glass, the refractive index is slightly higher for blue light than for red "
      "light. So when white light enters a prism, blue bends more than red, and the colours spread out into a spectrum. "
      "Each colour also has its own critical angle, so in some situations one colour can escape while another is totally "
      "internally reflected. That's a nice element four prediction to look out for.", covers=['W9', 'W11'],
      elements=[1, 4], exam=['X25-12'], refs=['ex25q12']),
]),
Scene('seismic', P2, 'Seismic waves inside the Earth', V.seismic, [
    S("Refraction isn't just for light. Every wave refracts when its speed changes. Earthquakes send out P waves, which "
      "are longitudinal, and S waves, which are transverse. Inside the Earth's mantle, their speed generally increases "
      "with depth.", refs=['appendix'], covers=['W2', 'W9', 'A1'], elements=[1], exam=['X24-17'], ),
    S("Because the speed increases gradually, the wave refracts gradually too. It keeps bending away from the normal, away "
      "from the faster region, so the ray paths curve back up towards the surface.", refs=['ar24q17'],
      covers=['W9', 'A1'], elements=[1, 4], exam=['X24-17']),
    S("S waves can't pass through the Earth's liquid outer core. Why? A transverse wave needs a restoring force to pull "
      "each layer back when it's displaced sideways. A liquid can't resist that sideways shearing. Its layers just slide "
      "past each other. With no restoring force, there's no S wave. This leaves an S wave shadow on the far side of the "
      "Earth, and it's how we know the outer core is liquid.", refs=['ar24q17'], covers=['A1', 'W3'], elements=[1],
      exam=['X24-17']),
    S("Tip: for sound and seismic waves, reason using wave speed, not refractive index, and don't assume that denser means "
      "slower. Refractive index and optical density are ideas for light.", refs=['ar24q17'], covers=['A1'],
      elements=[1], exam=['X24-17']),
]),
Scene('quakes', P2, 'Monitoring earthquakes and tsunamis', V.quakes, [
    S("The course also asks you to apply waves to monitoring earthquakes and tsunamis. P waves are faster, so they reach a "
      "seismometer first, and the S waves arrive later. The further away the earthquake, the bigger that delay. Using "
      "three stations, seismologists can locate the epicentre.", refs=['appendix'], covers=['A1'], elements=[1, 3]),
    S("Here's an element two problem. P waves travel at eight point zero kilometres per second and S waves at four point "
      "five. The S waves arrive twenty seconds after the P waves. The S wave travel time minus the P wave travel time is "
      "twenty seconds, so the distance is twenty divided by one over four point five minus one over eight. That's about two "
      "hundred and six kilometres.", covers=['A1'], elements=[2]),
    S("Tsunamis are ocean waves with very long wavelengths. In deep ocean they travel fast with a small amplitude. Near the "
      "coast the water gets shallower, so they slow down. The frequency stays the same, so by v equals f lambda the "
      "wavelength shortens, the energy bunches up, and the amplitude grows. That's why a tsunami that's barely noticeable "
      "at sea can be devastating at the shore.", refs=['appendix'], covers=['A1', 'W6'], elements=[1, 4], anim=2),
]),
Scene('superposition', P3, 'Superposition and pulse diagrams', V.superposition, [
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
]),
Scene('beats', P3, 'Beats', V.beats, [
    S("Now let two sound waves with slightly different frequencies overlap. Sometimes they're in step, and add up. "
      "Sometimes they're out of step, and cancel. So the loudness rises and falls regularly. These are beats.",
      refs=['content'], covers=['W13'], elements=[1]),
    S("On a graph, you see a fast wave inside a slowly changing envelope. One beat is one full cycle of loudness, from one "
      "envelope maximum to the next. Be careful not to measure between the peaks of the fast wave.", refs=['ar24q18'],
      covers=['W13'], elements=[3], exam=['X24-18']),
    S("The beat frequency is the difference between the two frequencies. f beat equals f one minus f two, taking the "
      "positive value. This is not on the information sheet, so learn it. The pitch you actually hear is the average of the "
      "two.", covers=['W13'], elements=[1]),
    S("Example, for element three. A four hundred and forty hertz tuning fork is sounded together with a note of unknown "
      "frequency. To reduce reading error, measure across several beats. Here, four beats take one second, so the beat "
      "frequency is four hertz. If the time axis is in milliseconds, remember to convert to seconds.", refs=['ar24q18'],
      covers=['W13'], elements=[3], exam=['X24-18']),
    S("So the unknown frequency is either four hundred and forty four, or four hundred and thirty six hertz. One "
      "measurement can't tell you which. Here's how to decide. Stick a little blu tack on the unknown fork, which makes it "
      "vibrate more slowly. If the beats get faster, its frequency has moved further away from four forty, so it must have "
      "started below: four hundred and thirty six hertz. That's the kind of reasoned prediction element four rewards.",
      covers=['W13'], elements=[4], exam=['X24-18', 'X25-13', 'X23-13']),
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
      "interference at the nodes. And at certain frequencies, the system resonates. Answers that mention reflection, "
      "superposition and resonance score best.", refs=['ar24q13'], covers=['W15', 'W14'], elements=[1],
      exam=['X24-13'], anim=2),
]),
Scene('strings', P3, 'Strings: harmonics and overtones', V.strings, [
    S("On a string fixed at both ends, both ends must be nodes. The simplest pattern, called the fundamental or first "
      "harmonic, is a single loop. That's half a wavelength, so lambda equals two L. Not L. That's a very common mistake, "
      "and this relationship isn't on the information sheet.", refs=['ar23q13'], covers=['W15'], elements=[1],
      exam=['X23-13'], anim=2),
    S("The next patterns have two, three, and four loops. In general, the n th harmonic has a wavelength of two L over n, "
      "and a frequency of n times v over two L. So the harmonic frequencies are whole number multiples of the fundamental.",
      covers=['W15'], elements=[1], anim=2),
    S("Watch the words. The first harmonic is the fundamental. The first overtone is the next frequency above the "
      "fundamental, which on a string is the second harmonic. Harmonics and overtones are counted differently, so read the "
      "question carefully.", refs=['ar24q13'], covers=['W15'], elements=[1], exam=['X24-13'], anim=2),
]),
Scene('we_string', P3, 'Worked example: a guitar string', V.we_string, [
    S("Worked example, covering elements two and four. A guitar string is sixty five centimetres long, and its fundamental "
      "frequency is one hundred and ninety six hertz. Its linear mass density is one point two grams per metre. Find the "
      "wave speed, and the tension.", covers=['W15', 'W16'], elements=[2], exam=['X23-13', 'X25-13'],
      refs=['ex23q13', 'ex25q13']),
    S("The fundamental wavelength is two L, which is one point three zero metres. So, using v equals f lambda, v is one "
      "ninety six times one point three zero, which is about two hundred and fifty five metres per second.",
      covers=['W15'], elements=[2]),
    S("Rearranging the string speed formula gives T equals mu v squared. With mu equal to zero point zero zero one two "
      "kilograms per metre, the tension comes out at about seventy eight newtons.", covers=['W16'], elements=[2]),
    S("Now, a prediction. If the tension increases by four percent, how does the pitch change? Frequency is proportional "
      "to wave speed, which is proportional to the square root of tension. So the frequency rises by a factor of root one "
      "point zero four, which is about one point zero two. The new frequency is about two hundred hertz. Played alongside a "
      "one ninety six hertz tuning fork, you'd hear roughly four beats per second. Using a ratio like this is quicker, and "
      "avoids rounding errors.", covers=['W16', 'W13'], elements=[4], exam=['X23-13']),
]),
Scene('pipes', P3, 'Pipes: open, closed and end correction', V.pipes, [
    S("Air in pipes forms standing waves too. Here we draw the displacement of the air. At a closed end, the air can't "
      "move, so there's a displacement node. At an open end, the air moves most freely, so there's a displacement antinode.",
      refs=['content'], covers=['W15'], elements=[1]),
    S("In a pipe open at both ends, there are antinodes at both ends. The fundamental is half a wavelength, so lambda "
      "equals two L. Just like a string, all harmonics are possible.", covers=['W15'], elements=[1], exam=['X24-13']),
    S("In a pipe closed at one end, there's a node at the closed end, and an antinode at the open end. The fundamental is "
      "just a quarter of a wavelength, so lambda equals four L. And only odd harmonics are possible: the first, third, "
      "fifth, and so on. So the first overtone of a closed pipe is the third harmonic.", refs=['ar23q15'],
      covers=['W15'], elements=[1], exam=['X23-15', 'X24-13']),
    S("In reality, the antinode sits slightly outside each open end. This is the end correction: the pipe behaves as if "
      "it's a little longer than it really is. Apply it at every open end: once for a closed pipe, and twice for an open "
      "pipe. And when you sketch, put the antinodes just outside the opening, not inside the pipe.", refs=['ar24q13'],
      covers=['W15'], elements=[1], exam=['X24-13']),
    S("Example, for element two. A pipe twenty centimetres long is closed at one end. Ignoring end correction, lambda one "
      "is four L, which is zero point eight metres. The speed of sound in air, three hundred and forty four metres per "
      "second, is on your information sheet. So f one is three forty four over zero point eight, which is four hundred and "
      "thirty hertz. The first overtone is the third harmonic, at twelve hundred and ninety hertz. If we open up the closed "
      "end, the fundamental doubles, to eight hundred and sixty hertz.", covers=['W15'], elements=[2]),
    S("A real world prediction. Your ear canal is roughly a pipe about two and a half centimetres long, closed at the "
      "eardrum. Its fundamental is about three hundred and forty four over zero point one, or roughly three thousand four "
      "hundred hertz. Resonance boosts sounds near that frequency, which is why our ears are especially sensitive around "
      "three to four kilohertz. A shorter canal, like a child's, resonates at a higher frequency.",
      covers=['W15', 'W14'], elements=[4], exam=['X25-17'], refs=['ex25q17']),
]),
Scene('resonance', P3, 'Resonance', V.resonance, [
    S("Every object has natural frequencies at which it tends to oscillate. When a periodic driving force matches one of "
      "those natural frequencies, energy builds up and the amplitude grows very large. That's resonance. It's why a singer "
      "can make a wine glass ring, why a guitar body amplifies its strings, and why engineers worry about bridges and "
      "buildings in wind and earthquakes.", refs=['content'], covers=['W14'], elements=[1]),
    S("For strings and pipes, the natural frequencies are exactly the standing wave frequencies we just found. So "
      "resonance and standing waves go together: a standing wave builds up strongly when the driving frequency matches one "
      "of the harmonics.", covers=['W14', 'W15'], elements=[1]),
]),
Scene('noise', P3, 'Noise pollution and acoustic design', V.noise, [
    S("Waves also help us control noise, another context named in the course. Noise cancelling headphones use a "
      "microphone to sample the incoming noise, then play an inverted copy. The two superpose destructively, so the noise "
      "is largely cancelled. It works best for steady, low frequency sounds like engine hum.", refs=['appendix'],
      covers=['A2', 'W12'], elements=[1, 4]),
    S("Acoustic design uses every idea in this criterion. Soft, porous materials absorb sound and reduce reflections and "
      "echo. Heavy barriers reflect sound, but low frequencies, with long wavelengths, diffract over and around walls, "
      "which is why you still hear the bass of traffic. Engineers avoid resonance by mounting machines on soft supports, "
      "and they shape rooms so that reflections send sound where it's wanted.", refs=['appendix'],
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
      covers=['W17'], elements=[1], exam=['X23-16', 'X25-14'], anim=1),
    S("What decides loud or quiet is the path difference: how much further the wave from one source travels than the wave "
      "from the other. To find it, simply subtract one path length from the other. You don't need Pythagoras or "
      "trigonometry, unless you're asked for an angle.", refs=['ar24q14'], covers=['W17'], elements=[1],
      exam=['X24-14']),
    S("If the path difference is a whole number of wavelengths, n lambda, the waves arrive in phase. That's constructive "
      "interference, a maximum. If the path difference is a whole number minus a half, times lambda, the waves arrive "
      "completely out of phase. That's destructive interference, a minimum. Equal paths, at zero angle, always give a "
      "maximum for in-phase sources.", covers=['W17'], elements=[1], exam=['X23-16', 'X24-14']),
    S("Example, for element two. Two speakers are driven in phase at six hundred and eighty six hertz. The wavelength is "
      "three forty four over six eight six, which is about zero point five zero metres. You stand five metres from speaker "
      "A, and six point two five metres from speaker B. The path difference is one point two five metres, which is two and "
      "a half wavelengths. So you're at a quiet spot. Step to where the path difference is one point five metres, three "
      "whole wavelengths, and it's loud again.", covers=['W17'], elements=[2]),
]),
Scene('radar', P4, 'Two paths: radio waves and aircraft', V.radar, [
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
]),
Scene('youngs', P4, "Young's double slit and fringe width", V.youngs, [
    S("Young's double slit experiment shows light interfering. Light passes through two narrow slits, a distance d apart, "
      "onto a screen a distance x away. You see evenly spaced bright and dark fringes.", refs=['content', 'ex25q14'],
      covers=['W17'], elements=[1], exam=['X25-14']),
    S("The fringe width, W, equals lambda x over d. That's the form on your information sheet, in the oscillations and "
      "waves section, so use its letters: x is the distance to the screen, and d is the slit separation. A bigger "
      "wavelength, a more distant screen, or slits closer together all give wider fringes. This experiment was crucial "
      "evidence that light is a wave.", covers=['W17'], elements=[1]),
    S("Example, for element two. A green laser, with a wavelength of five hundred and thirty two nanometres, shines on two "
      "slits zero point two five millimetres apart, with a screen two metres away. Using the information sheet formula, W "
      "equals five hundred and thirty two times ten to the minus nine, times two, divided by zero point two five times ten "
      "to the minus three. That's about four point three millimetres. Switch to a red laser, with its longer wavelength, "
      "and the fringes spread further apart.", covers=['W17'], elements=[2], exam=['X25-14']),
    S("Where are the fringes? The central bright fringe has zero path difference. The n th bright fringe is n fringe "
      "widths from the centre, where the path difference is n wavelengths. The dark fringes sit halfway between, where the "
      "path difference is a whole number minus a half, times lambda.", covers=['W17'], elements=[1, 3],
      exam=['X25-14']),
    S("Is the answer valid? The formula relies on a small angle approximation. It only works when the distance to the "
      "screen is much bigger than the fringe width and the slit separation. Here, it's a few millimetres compared with two "
      "metres, so it's fine. If you're asked about the limitations of this formula, that's the answer, and vague "
      "references to other factors don't earn marks.", refs=['ar24q14'], covers=['W17'], elements=[2],
      exam=['X24-14']),
]),
Scene('diffraction', P4, 'Diffraction', V.diffraction, [
    S("Diffraction is the spreading of a wave as it passes through a gap, or around an obstacle. In this course, it's "
      "treated qualitatively. The spreading is most noticeable when the gap is similar in size to the wavelength. With a "
      "wide gap, the wave goes mostly straight through. With a narrow gap, it spreads out in curved wavefronts.",
      refs=['content'], covers=['W18'], elements=[1], anim=1),
    S("So longer wavelengths diffract more. That's why you can hear someone around a corner, but not see them. Sound "
      "wavelengths are around a metre, while light wavelengths are less than a millionth of a metre. It's also why long "
      "wave radio bends around hills when shorter wavelengths can't. Note that the wavelength doesn't change as the wave "
      "diffracts, so keep the spacing between wavefronts the same in your sketches.", refs=['content'],
      covers=['W18'], elements=[1, 4], exam=['X24-14'], anim=1),
]),
Scene('polarisation', P4, 'Polarisation', V.polarisation, [
    S("Polarisation is the strongest evidence that light is a transverse wave. In unpolarised light, the electric field "
      "oscillates in all directions perpendicular to the direction of travel. A polarising filter only lets through the "
      "component along its transmission axis. What comes out is plane polarised, oscillating in just one direction.",
      refs=['content'], covers=['W19'], elements=[1], exam=['X23-14']),
    S("Longitudinal waves can't be polarised, because they only oscillate along the direction of travel. There's no "
      "sideways direction to filter out. So polarisation tells transverse waves apart from longitudinal ones.",
      refs=['content'], covers=['W19', 'W2'], elements=[1]),
    S("If polarised light meets a second filter at an angle theta, resolve the amplitude like a vector. The component "
      "along the new axis is A cos theta, and that's what gets through. Use cosine, not sine, when theta is measured from "
      "the polarisation direction. And since intensity depends on amplitude squared, intensity falls by a factor of cos "
      "squared theta.", refs=['ar23q14'], covers=['W19'], elements=[1, 2], exam=['X23-14']),
    S("Two filters at ninety degrees to each other, called crossed filters, block everything, since cos ninety is zero. "
      "But put a third filter between them at forty five degrees, and some light gets through. The middle filter passes A "
      "cos forty five, about zero point seven one A, now polarised at forty five degrees. The last filter is forty five "
      "degrees from that, so it passes zero point seven one of that again. That's half the original amplitude, and a "
      "quarter of the intensity.", refs=['ar23q14'], covers=['W19'], elements=[2, 4], exam=['X23-14']),
    S("Light reflected off water or a road is partly polarised, mostly horizontally. Polarising sunglasses have vertical "
      "transmission axes, so they block much of that glare. Tilt your head ninety degrees, and the glare comes back.",
      covers=['W19'], elements=[4], exam=['X25-16'], refs=['ex25q16']),
    S("Light scattered by air molecules is polarised too. Sunlight scattered at ninety degrees is mostly plane polarised, "
      "so if you look at that part of the sky through a polarising filter and rotate it, the sky brightens and darkens. "
      "Reflection, scattering and filters all point the same way: light is a transverse wave.", covers=['W19', 'W5'],
      elements=[1, 4], exam=['X25-16']),
]),
Scene('light_history', P4, 'How we learned light is a wave', V.light_history, [
    S("The course also asks you to understand how the wave theory of light developed. Newton favoured a particle model, "
      "which explained reflection and straight line travel. Huygens proposed waves and wavelets, which explained "
      "refraction, but only if light travels more slowly in glass.", refs=['appendix'], covers=['A3'], elements=[1]),
    S("In eighteen oh one, Young's double slit experiment showed interference fringes, which particles couldn't explain. "
      "Then polarisation showed that light must be a transverse wave.", refs=['appendix'], covers=['A3', 'W17', 'W19'],
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
      "get part a wrong, keep going. Markers usually carry the error forward, and still give you method marks.",
      refs=['ar24q16', 'ar23q15']),
    S("That's every part of Criterion 7. Waves transfer energy. They're described by amplitude, wavelength, period, "
      "frequency and speed. They reflect, refract and superpose. They form beats and standing waves, they interfere and "
      "diffract, and if they're transverse, they can be polarised. Practise explaining each idea in words, as well as with "
      "numbers, and you'll be ready for your tests and for Section C. Good luck."),
]),
]

VIDEO = Video(
    id='PHY415115_C7_wave_motion',
    course=COURSE, course_name='Physics', module=MODULE,
    module_name='Criterion 7: Identify and apply general principles of wave motion',
    title='Criterion 7: wave motion, complete revision',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Oscillations, Waves'),
    checks=CHECKS,
    allowed_overlaps=['identify and apply general principles of wave motion'],
    keywords=['wavelength', 'frequency', 'amplitude', 'period', 'wave speed', 'transverse', 'longitudinal',
              'superposition', 'constructive', 'destructive', 'standing wave', 'node', 'antinode', 'harmonic',
              'overtone', 'fundamental', 'resonance', 'refraction', 'reflection', "Snell's law", 'critical angle',
              'total internal reflection', 'refractive index', 'path difference', 'coherent', 'diffraction',
              'polarisation', 'polarised', 'beats', 'beat frequency', 'end correction', 'restoring force',
              'linear mass density', 'tension', 'fringe width'],
    description=('A complete revision explainer for TASC Physics (PHY415115) Criterion 7: identify and apply general '
                 'principles of wave motion. For class tests and the end-of-year exam (Section C). Formulas from the '
                 'TASC information sheet are labelled on screen.'),
)
