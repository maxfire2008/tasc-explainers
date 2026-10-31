"""Drawing helpers shared by every video.  Scene draw functions should only use these
(plus plain matplotlib on axes from wax/gax) so that every video looks the same.

Coordinates passed to helpers are *figure fractions* (0..1, origin bottom-left) unless
the helper takes an axes.  The layout canvas is 1920x1080.  Keep content inside
x 0.04..0.96 and y 0.07..0.82 (header above, footer below).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.text import Text

from . import style as S

plt.rcParams.update({'font.family': S.FONT_FAMILY, 'mathtext.fontset': S.MATH_FONTSET,
                     'axes.unicode_minus': True})

BG, PANEL, PANEL2, FG, SOFT, MUT, GRID = S.BG, S.PANEL, S.PANEL2, S.FG, S.SOFT, S.MUT, S.GRID
PINK, GREEN, YELLOW = S.PINK, S.GREEN, S.YELLOW
CM_WAVE = LinearSegmentedColormap.from_list('wave', S.WAVE_CMAP)
TAU = 2 * np.pi

# Theme + per-frame context.  The pipeline sets these; specs call use() at import so
# frames can also be drawn interactively.
TH = S.theme('DEFAULT', 'DEFAULT')
ctx = dict(part='', sheet_used=False, sheet_section='', course_label='', scale=1)


def use(theme):
    global TH
    TH = theme


def A1():
    """Course accent colour."""
    return TH.accent


def A2():
    """Module accent colour."""
    return TH.accent2


# ----------------------------------------------------------------------------- basics
def new_fig():
    fig = plt.figure(figsize=(S.VIDEO['width'] / 100, S.VIDEO['height'] / 100), dpi=100 * ctx['scale'])
    fig.patch.set_facecolor(BG)
    return fig


def frac(size):
    """Height of one text line of `size` pt, as a figure fraction."""
    return size * 100 / 72 / S.VIDEO['height'] * 1.38


def header(fig, title, part=None):
    """Part label + slide title.  part defaults to the scene's part (set by the pipeline)."""
    part = (part if part is not None else ctx['part']).upper()
    if part:
        fig.text(0.05, 0.935, part.replace('·', ' · '), color=A1(), fontsize=19, weight='bold', va='center')
    fig.text(0.05, 0.873, title, color=FG, fontsize=44, weight='bold', va='center')


def footer(fig, ref_numbers=()):
    """Drawn automatically by the pipeline on EVERY slide.  Do not call from scenes."""
    fig.text(0.05, 0.032, ctx['course_label'], color=MUT, fontsize=14, va='center')
    fig.text(0.95, 0.032, S.FOOTER_AI, color=SOFT, fontsize=14, va='center', ha='right', style='italic')
    if ref_numbers:
        fig.text(0.80, 0.032, 'Refs ' + ', '.join(f'[{n}]' for n in ref_numbers), color=A1(), fontsize=14,
                 va='center', ha='right')


def ai_badge(fig):
    """Large robot icon + AI notice for thumbnails.  Drawn by the pipeline; do not call from scenes."""
    x, y, w, h = 0.425, 0.025, 0.55, 0.125
    box(fig, x, y, w, h, fc=PANEL, ec=PINK, lw=5)
    ax = wax(fig, [x + 0.012, y + 0.012, h * 9 / 16 * 1.25, h - 0.024], (-6, 6), (-4, 5))
    ax.set_aspect('equal')
    ax.add_patch(FancyBboxPatch((-3.6, -3.6), 7.2, 5.8, boxstyle='round,pad=0,rounding_size=1.2', fc=PINK, ec='none'))
    ax.plot([0, 0], [2.2, 3.6], color=PINK, lw=6)
    ax.add_patch(Circle((0, 4), 0.8, fc=PINK, ec='none'))
    for sx in (-1, 1):
        ax.add_patch(FancyBboxPatch((sx * 4.5 - 0.6, -1.8), 1.2, 2.2, boxstyle='round,pad=0,rounding_size=0.4', fc=PINK, ec='none'))
        ax.add_patch(Circle((sx * 1.6, 0), 0.95, fc=BG, ec='none', zorder=5))
    ax.add_patch(FancyBboxPatch((-1.9, -2.6), 3.8, 0.8, boxstyle='round,pad=0,rounding_size=0.3', fc=BG, ec='none', zorder=5))
    fig.text(x + h * 9 / 16 * 1.25 + 0.03, y + h / 2, S.FOOTER_AI, color=FG, fontsize=54, weight='bold', va='center')


def T(fig, x, y, s, size=28, color=FG, **kw):
    """Plain text, anchored top-left by default.  Mathtext ($...$) allowed."""
    kw.setdefault('va', 'top')
    return fig.text(x, y, s, fontsize=size, color=color, linespacing=1.3, **kw)


def bullets(fig, items, n, x, y, size=27, gap=0.022, mark='•', mcol=None, dim=True):
    """First n items as bullets.  The newest is bright, older ones dimmed (dim=True).
    Use '\n' inside an item to wrap.  Returns the y below the last bullet."""
    mcol = mcol or A1()
    for i, s in enumerate(items[:n]):
        col = FG if (i == n - 1 or not dim) else SOFT
        fig.text(x, y, mark, color=mcol, fontsize=size, va='top')
        fig.text(x + 0.022, y, s, color=col, fontsize=size, va='top', linespacing=1.3)
        y -= frac(size) * (s.count('\n') + 1) + gap
    return y


def box(fig, x, y, w, h, fc=PANEL, ec=None, lw=2, r=0.012):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={r}', transform=fig.transFigure,
                       fc=fc, ec=ec if ec else fc, lw=lw, zorder=0)
    fig.add_artist(p)
    return p


def card(fig, x, y, w, h, title, body, tcol=None, size=24):
    """Rounded card with a coloured title.  Examples use tcol=A2(), warnings PINK, tips YELLOW."""
    box(fig, x, y, w, h)
    T(fig, x + 0.018, y + h - 0.025, title, size=size + 4, color=tcol or A2(), weight='bold')
    T(fig, x + 0.018, y + h - 0.025 - frac(size + 4) - 0.012, body, size=size, color=SOFT)


def eq(fig, x, y, s, size=40, color=YELLOW, ha='left', va='center', bg=True):
    """An equation in a box.  Use sheet_eq / learn_eq instead whenever the formula's
    status on the information sheet is known."""
    kw = dict(boxstyle='round,pad=0.45', fc=PANEL, ec=GRID, lw=1.5) if bg else None
    return fig.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, bbox=kw)


def sheet_eq(fig, x, y, s, size=40, color=YELLOW):
    """Formula that IS on the information sheet: boxed, with a tag naming the sheet section.
    The pipeline then auto-cites the info-sheet reference on this slide, and the checker
    requires the step's narration to mention 'information sheet'."""
    ctx['sheet_used'] = True
    t = fig.text(x, y, s, fontsize=size, color=color, ha='left', va='center',
                 bbox=dict(boxstyle='round,pad=0.45', fc=PANEL, ec=A1(), lw=2.5))
    fig.text(x, _below(fig, t, size), '▣ ' + S.INFO_SHEET_TAG.format(section=ctx['sheet_section']),
             fontsize=15, color=A1(), ha='left', va='top', weight='bold')
    return t


def _below(fig, t, size):
    """Figure y just below a boxed text (box pad 0.45 em)."""
    bb = t.get_window_extent(fig.canvas.get_renderer())
    return (bb.y0 - 0.45 * size * fig.dpi / 72) / fig.bbox.height - 0.012


def learn_eq(fig, x, y, s, size=40, color=YELLOW):
    """Formula students must remember or derive (NOT on the information sheet)."""
    t = fig.text(x, y, s, fontsize=size, color=color, ha='left', va='center',
                 bbox=dict(boxstyle='round,pad=0.45', fc=PANEL, ec=PINK, lw=2.5, ls='--'))
    fig.text(x, _below(fig, t, size), S.NOT_ON_SHEET_TAG, fontsize=15, color=PINK, ha='left', va='top',
             weight='bold')
    return t


def chip(fig, s, color=None, size=17, x=0.95, y=0.935, ha='right'):
    """Small rounded label, top-right by default (level with the part label),
    e.g. chip(fig, 'Element 2 · problems') on worked examples."""
    fig.text(x, y, s, fontsize=size, color=BG, ha=ha, va='center', weight='bold',
             bbox=dict(boxstyle='round,pad=0.35', fc=color or A2(), ec='none'))


# ----------------------------------------------------------------------------- axes
def wax(fig, rect, xlim, ylim):
    """Invisible axes for diagrams.  rect = [x, y, w, h] in figure fractions."""
    ax = fig.add_axes(rect)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axis('off'); ax.patch.set_alpha(0)
    return ax


def gax(fig, rect, xlim, ylim, xlabel, ylabel, ticks=True):
    """Visible graph axes in house style."""
    ax = fig.add_axes(rect)
    ax.set_facecolor(PANEL)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    for k in ['top', 'right']: ax.spines[k].set_visible(False)
    for k in ['left', 'bottom']: ax.spines[k].set_color(MUT)
    ax.tick_params(colors=SOFT, labelsize=16)
    ax.set_xlabel(xlabel, color=SOFT, fontsize=18)
    ax.set_ylabel(ylabel, color=SOFT, fontsize=18)
    ax.axhline(0, color=GRID, lw=1.2, zorder=0)
    if not ticks:
        ax.set_xticks([]); ax.set_yticks([])
    return ax


def darrow(ax, p0, p1, color=FG, lw=2.5, style='<|-|>', ms=22):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, color=color, lw=lw))


def arrow(ax, p0, p1, color=FG, lw=3, ms=26, **kw):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle='-|>', mutation_scale=ms, color=color, lw=lw, **kw))


def label(ax, x, y, s, size=22, color=FG, **kw):
    kw.setdefault('ha', 'center'); kw.setdefault('va', 'center')
    ax.text(x, y, s, fontsize=size, color=color, **kw)


# ----------------------------------------------------------------------------- frame capture
def to_rgb(fig):
    fig.canvas.draw()
    return np.asarray(fig.canvas.buffer_rgba())[:, :, :3].copy()


def texts(fig):
    """All visible strings on the slide (used by the copyright checker)."""
    out = []
    for t in fig.findobj(Text):
        s = t.get_text()
        if s and t.get_visible():
            out.append(s)
    return out
