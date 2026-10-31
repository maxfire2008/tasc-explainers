"""TEMPLATE video spec.  Copy to videos/<COURSE>/<module>_<slug>.py (and usually split the draw
functions into a sibling <module>_visuals.py, as in videos/PHY415115/), then fill it in.

This file runs as-is so you can see the moving parts:
    uv run python -m explainer check   template/video_template.py --allow-missing-sources
    uv run python -m explainer preview template/video_template.py
    uv run python -m explainer tts     template/video_template.py
    uv run python -m explainer render  template/video_template.py

Rules that the checker enforces (see CLAUDE.md for the reasons):
  * every syllabus dot point, every element and every past-exam topic is covered by some Step
  * every Ref points at a source in content.csv (by NAME or URL); PDF refs need page numbers
  * no verbatim text from 'copyrighted' sources; quotes from 'quotes' sources are short and cited
  * a slide that shows an information-sheet formula (sheet_eq) says "information sheet" in its narration
  * every number in a worked example is recomputed in CHECKS
The framework adds the AI disclaimer (first, or after a first scene with id 'title') and credits (last) scenes, the footer
("AI generated content", course label, reference numbers) and all output documents.
"""
import math

import numpy as np

from explainer import layout as L, style
from explainer.layout import header, T, bullets, card, sheet_eq, learn_eq, chip, wax, arrow, label, GRID, PINK, GREEN, TAU
from explainer.spec import Video, Scene, Step, Ref, InfoSheet

COURSE, MODULE = 'TEMPLATE', 'C0'           # course code = folder in sources/; module = criterion code
L.use(style.theme(COURSE, MODULE))          # gives L.A1() (course accent) and L.A2() (module accent)

P1 = 'Part 1 · Describing waves'            # part label shown above slide titles; groups chapters


# --------------------------------------------------------------------------- draw functions
# draw(fig, s, ph): s = build step (0..n-1), ph = animation phase 0..1 (seamless loop).
def wave_speed(fig, s, ph):
    header(fig, 'Wave speed')                              # part label comes from the Scene
    ax = wax(fig, [0.05, 0.40, 0.55, 0.38], (0, 10), (-1.6, 1.6))
    x = np.linspace(0, 10, 600)
    ax.axhline(0, color=GRID, lw=1.2, ls='--')
    ax.plot(x, np.sin(TAU * (x / 4 - ph)), color=L.A1(), lw=4)   # 1 cycle per loop -> seamless
    arrow(ax, (6, 1.4), (9, 1.4), color=L.A2())
    label(ax, 5.8, 1.4, 'direction of travel', size=20, color=L.A2(), ha='right')
    bullets(fig, ['One wavelength passes per period', 'So speed = wavelength ÷ period'][:s + 1], s + 1, 0.64, 0.76)
    if s >= 1:
        sheet_eq(fig, 0.07, 0.25, r'$v = f\lambda$', size=48, color=GREEN)    # ON the information sheet


def example(fig, s, ph):
    header(fig, 'Worked example')
    chip(fig, 'Element 2 · problems')                     # tag which element is practised
    card(fig, 0.05, 0.58, 0.45, 0.20, 'Question', 'f = 50 Hz, λ = 0.40 m.\nFind the wave speed.')
    if s >= 1:
        T(fig, 0.55, 0.74, r'$v = f\lambda = 50\times0.40 = 20\ \mathrm{m\ s^{-1}}$', size=32, color=GREEN)
        learn_eq(fig, 0.55, 0.50, r'$f = \dfrac{v}{\lambda}$', size=36)      # NOT on the sheet (rearranged)


# --------------------------------------------------------------------------- spec
REFS = {
    # key: Ref(source NAME from content.csv or its URL, locator, page for PDFs)
    # NAME = last part of the URL path (+ '.html' if it has no extension); list with: uv run python -m explainer sources <COURSE>
    'content': Ref('course-doc.html', 'Course document, content: Waves'),
    'standards': Ref('course-doc.html', 'Course document, criterion standards table'),
    'info': Ref('Information-sheet.pdf', 'Information sheet, Waves section', page=2),
    'ex24q1': Ref('Exam-Paper-2024.pdf', '2024 exam, Section C, Question 1', page=12),
    'ar24q1': Ref('Assessment-Report-2024.pdf', '2024 assessment report, Question 1', page=5),
}
SYLLABUS = {'T1': ('Relationship between wave speed, frequency and wavelength', 'content')}
ELEMENTS = {1: ('Describes and explains principles', 'standards'), 2: ('Solves numerical problems', 'standards')}
EXAM_TOPICS = {'X24-1': ('Wave speed from frequency and wavelength (in our own words)', 'ex24q1')}
CHECKS = [('example v', lambda: 50 * 0.40, 20, 1e-9)]

SCENES = [
    Scene('wave_speed', P1, 'Wave speed', wave_speed, [
        Step("In one period, a wave moves forward exactly one wavelength.",
             refs=['content'], covers=['T1'], elements=[1], anim=2),
        Step("So the wave speed is the wavelength divided by the period, which is f lambda. "
             "This formula is on your information sheet, in the waves section.",
             refs=['content'], covers=['T1'], elements=[1], anim=2),
    ]),
    Scene('example', P1, 'Worked example', example, [
        Step("Here's a question for element two. A wave has a frequency of fifty hertz and a wavelength of zero point four "
             "metres. What is its speed?", covers=['T1'], elements=[2], exam=['X24-1'], refs=['ex24q1']),
        Step("v equals f lambda, so fifty times zero point four, which is twenty metres per second. Rearranged as f equals v "
             "over lambda, it isn't on the sheet in that form, so practise rearranging.", covers=['T1'], elements=[2],
             refs=['ar24q1']),
    ]),
]

VIDEO = Video(
    id='TEMPLATE_C0_example', course=COURSE, course_name='Template Course', module=MODULE,
    module_name='Criterion 0: Example module', title='Template video',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=InfoSheet(ref='info', section='Waves'), checks=CHECKS,
    keywords=['wavelength', 'frequency', 'wave speed'],
    description='Template description: one or two sentences for YouTube.',
)
