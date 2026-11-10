"""Data model for a video spec.  A spec is a Python file that defines VIDEO = Video(...).
See template/video_template.py for a fully commented example."""
from dataclasses import dataclass, field
from typing import Callable, Optional
import importlib.util
import os
import sys


@dataclass
class Ref:
    """A citable source location.  `file` = the source NAME from content.csv (see
    `python -m explainer sources <spec>`) or the source's full URL."""
    file: str
    loc: str = ''                 # human locator: 'Section C, Q16(b)', 'Criterion 7 standards table'
    page: Optional[object] = None  # PDF page number(s) of the locator, e.g. 7 or '7-8'.  Required for PDFs.
    note: str = ''                # optional extra note shown in references.md


@dataclass
class Step:
    """One narration chunk = one on-screen build state of a scene."""
    text: str                                       # narration, written to be SPOKEN (see CLAUDE.md)
    refs: list = field(default_factory=list)        # keys of Video.refs cited on this slide
    covers: list = field(default_factory=list)      # keys of Video.syllabus explained here
    elements: list = field(default_factory=list)    # element numbers (int) exercised here
    exam: list = field(default_factory=list)        # keys of Video.exam_topics addressed here
    anim: Optional[float] = None                    # loop period in seconds -> animated step; None = still
    min_dur: float = 0.0                            # minimum on-screen time (s)
    problem: str = ''                               # the question whose explanation starts at this step (for problems.txt)


@dataclass
class Scene:
    id: str
    part: str            # 'Part 2 · Boundaries'  -> header label + grouping
    topic: str           # YouTube chapter title, e.g. 'Total internal reflection'
    draw: Callable       # draw(fig, step_index, phase)  phase in [0,1) for animated steps
    steps: list


@dataclass
class InfoSheet:
    ref: str             # key in Video.refs pointing at the information sheet
    section: str         # section heading on the sheet, e.g. 'Oscillations, Waves'


@dataclass
class Video:
    id: str                       # output folder name, e.g. 'PHY415115_C7_wave_motion'
    course: str                   # course code, e.g. 'PHY415115' (also the sources/ subfolder)
    course_name: str              # 'Physics'
    module: str                   # module/criterion code, e.g. 'C7'
    module_name: str              # 'Criterion 7: Identify and apply general principles of wave motion'
    title: str                    # title-card text
    refs: dict                    # key -> Ref
    syllabus: dict                # key -> (dot point text, ref key)       100% must be covered
    elements: dict                # number -> (element text, ref key)      all must be exercised
    exam_topics: dict             # key -> (what was examined, ref key)    all must be covered
    scenes: list
    info_sheet: Optional[InfoSheet] = None
    checks: list = field(default_factory=list)         # (label, fn() -> value, expected, rel_tol)
    allowed_overlaps: list = field(default_factory=list)  # phrases the copyright checker ignores
    description: str = ''         # YouTube description intro (timestamps + refs are appended)
    keywords: list = field(default_factory=list)  # key terms highlighted in styled subtitles
    thumbnail: Optional[Callable] = None  # draw(fig): YouTube thumbnail, based on the title card
    render_scale: Optional[int] = None    # overrides style.VIDEO['render_scale'] for this video (1 -> 1920x1080)

    @property
    def course_label(self):
        return f'{self.course} {self.course_name}  ·  {self.module_name.split(":")[0]}'

    def all_steps(self):
        for sc in self.scenes:
            for i, st in enumerate(sc.steps):
                yield sc, i, st


def import_sibling(spec_file, filename):
    """Import a helper module (e.g. the visuals file) that sits next to a spec file,
    under a unique module name so different courses can reuse file names."""
    path = os.path.join(os.path.dirname(os.path.abspath(spec_file)), filename)
    name = 'sib_' + os.path.abspath(path).replace(os.sep, '_').replace('.', '_')
    if name in sys.modules:
        return sys.modules[name]
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    sys.modules[name] = m
    s.loader.exec_module(m)
    return m


def load(path):
    """Import a spec file and return its VIDEO with built-in disclaimer/credits added."""
    path = os.path.abspath(path)
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root not in sys.path:
        sys.path.insert(0, root)
    name = 'spec_' + os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    v = mod.VIDEO
    from . import builtin
    builtin.wrap(v)
    return v
