"""House style for every explainer video.

Everything that should look or sound the same across videos lives here:
colours, fonts, the per-course and per-module accent colours, the narration
voice, video encoding, timing, disclaimer/credit wording and the copyright
thresholds used by the checker.  Change it here, never inside a video spec.
"""
import hashlib
from dataclasses import dataclass

# --------------------------------------------------------------------------- canvas
VIDEO = dict(width=1920, height=1080, fps=30, crf=20, preset='veryfast', gop=120,
             audio_bitrate='160k')

# --------------------------------------------------------------------------- base palette (dark theme)
BG = '#0e1726'        # slide background
PANEL = '#17243b'     # cards / boxes
PANEL2 = '#1d2d49'    # alternate rows / highlighted cards
FG = '#eef2f8'        # main text
SOFT = '#b3c0d4'      # secondary text
MUT = '#7b8ca8'       # muted text, axes
GRID = '#2b3c5a'      # rest lines, grid, box edges

# Semantic colours: SAME meaning in every video. Course/module accents must not reuse these.
PINK = '#f15bb5'      # warnings, "careful!", destructive, nodes
GREEN = '#9bde7e'     # results / final answers, constructive
YELLOW = '#ffd166'    # equations, amplitudes, highlights
WAVE_CMAP = ['#06101f', '#123a63', '#3a8fc4', '#bff0ff']   # ripple-tank style fields

FONT_FAMILY = ['Inter', 'DejaVu Sans']
MATH_FONTSET = 'dejavusans'

# --------------------------------------------------------------------------- course & module accents
# accent  = course colour (part labels, bullets, primary curves)
# accent2 = module colour (second curve, arrows, card titles, "example" cards)
COURSE_ACCENTS = {
    'PHY415115': '#4cc9f0',   # Physics: cyan
    'CHM415115': '#a78bfa',   # Chemistry: violet
    'MTS415118': '#5eead4',   # Maths Specialised: teal
    'MTM415118': '#60a5fa',   # Maths Methods: blue
    'BIO415115': '#c4b5fd',   # Biology: lavender
}
_COURSE_FALLBACK = ['#4cc9f0', '#a78bfa', '#5eead4', '#60a5fa', '#c4b5fd', '#7dd3fc']

MODULE_ACCENTS = {
    # (course, module) -> colour.  Module = criterion / unit code used in the spec.
    ('PHY415115', 'C5'): '#fb7185',   # Newtonian mechanics: rose
    ('PHY415115', 'C6'): '#c084fc',   # Electricity & magnetism: purple
    ('PHY415115', 'C7'): '#f9a03f',   # Wave motion: orange
    ('PHY415115', 'C8'): '#f472b6',   # Light, atomic & nuclear: magenta
}
_MODULE_FALLBACK = ['#f9a03f', '#fb7185', '#c084fc', '#f472b6', '#fdba74', '#e879f9']


@dataclass(frozen=True)
class Theme:
    course: str
    module: str
    accent: str
    accent2: str


def _pick(key, options):
    return options[int(hashlib.md5(key.encode()).hexdigest(), 16) % len(options)]


def theme(course, module):
    """Theme for a course/module. Unknown codes get a stable fallback colour."""
    a1 = COURSE_ACCENTS.get(course) or _pick(course, _COURSE_FALLBACK)
    a2 = MODULE_ACCENTS.get((course, module)) or _pick(course + module, _MODULE_FALLBACK)
    return Theme(course, module, a1, a2)


# --------------------------------------------------------------------------- narration voice
# engine 'kokoro' = kokoro-onnx (offline, CPU).  Model files: run scripts/get_models.sh
# Good Kokoro voices: af_heart (US F, best quality), af_bella, am_michael, am_fenrir (US M),
#                     bf_emma, bf_isabella (UK F), bm_george, bm_fable (UK M).
# There is no Australian voice in Kokoro; lang must match the voice ('en-us' or 'en-gb').
# Changing anything here invalidates the TTS cache, so all narration is regenerated.
VOICE = dict(engine='kokoro', voice='af_heart', speed=1.0, lang='en-us',
             model='models/kokoro/kokoro-v1.0.onnx', voices='models/kokoro/voices-v1.0.bin')

# Applied to narration text before synthesis (regex, replacement).  Keep narration itself
# readable; put pronunciation hacks here.
PRONUNCIATIONS = [
    (r'\bPHY415115\b', 'P H Y four one five, one one five'),
    (r'\bTASC\b', 'task'),
    (r'\bTIR\b', 'total internal reflection'),
]

# --------------------------------------------------------------------------- thumbnail (YouTube: 16:9, under 2 MB)
THUMBNAIL = dict(width=1280, height=720, max_bytes=2 * 1024 * 1024)

# --------------------------------------------------------------------------- timing (seconds)
LEAD_FIRST = 0.7     # silence before the first step of a scene
LEAD = 0.3           # silence before other steps
TAIL = 0.6           # hold after narration ends
TAIL_LAST = 2.5      # hold on the very last step of the video
MIN_CHAPTER = 10.0   # YouTube's minimum chapter length

# --------------------------------------------------------------------------- fixed wording
FOOTER_AI = 'AI generated content'
DISCLAIMER_TITLE = 'AI-generated content'
DISCLAIMER_BODY = ('The narration, visuals and example questions in this video were produced with\n'
                   'by artificial intelligence with some human oversight. They may contain errors.\n'
                   'Always check with your teacher, the course document and the information sheet.')
DISCLAIMER_NARRATION = ('Before we start: this video was made with the by artificial intelligence with some human oversight, '
                        'including the narration, the visuals and the worked examples. It may contain errors, '
                        'so always check with your teacher, your course document and your information sheet.')
COPYRIGHT_HOLDER = 'Tasmanian Assessment, Standards and Certification (TASC)'
ATTRIBUTION_LICENCE = 'Creative Commons Attribution 4.0 International (CC BY 4.0) licence'
CREDITS_NARRATION = ('Course content in this video is adapted from material published by {holder}, '
                     'used under a  Creative Commons Attribution 4.0 International licence. Past exams and assessment reports are '
                     'referenced but not reproduced, and every example question is original. '
                     'The full reference list is in the description.')
INFO_SHEET_TAG = 'Information sheet · {section}'
NOT_ON_SHEET_TAG = 'Not on the information sheet: learn it'

# YouTube timestamps line format.  Available: {time} {part} {part_short} {topic}
TIMESTAMP_FORMAT = '{time} {part_short}: {topic}'

# --------------------------------------------------------------------------- copyright checker
NGRAM = 8                 # shortest verbatim run (words) the checker looks for
QUOTE_MAX_WORDS = 20      # longest verbatim run allowed from a 'quotes' source
# 'copyrighted' sources: any run >= NGRAM words is an error.
# 'attribution' sources: runs are allowed, but the step must cite that source.
