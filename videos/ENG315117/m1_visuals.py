"""Title card and thumbnail for Module 1 (thriller).  The slides themselves are Slide(...) objects from eng_common."""
import numpy as np

from explainer import layout as L
from explainer.layout import wax, PINK, TAU
from explainer.spec import import_sibling

title_text = import_sibling(__file__, 'eng_common.py').title_text


def _target(fig, a=1.0):
    """Signature graphic: a crosshair over concentric rings, with a diagonal searchlight beam."""
    ax = wax(fig, [0.52, 0.06, 0.46, 0.86], (-1, 1), (-1.0, 1.0))
    ax.set_aspect('equal')
    t = np.linspace(0, TAU, 300)
    for r, col, lw in ((0.85, L.GRID, 4), (0.62, L.GRID, 4), (0.38, L.A2(), 6), (0.12, PINK, 8)):
        ax.plot(r * np.cos(t), r * np.sin(t), color=col, lw=lw * a, alpha=0.9)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ax.plot([dx * 0.05, dx * 0.98], [dy * 0.05, dy * 0.98], color=L.A2(), lw=5 * a)
    ax.fill([-1, -0.3, 0.2, -1], [-0.2, 0.9, 0.1, -0.2], color=L.A1(), alpha=0.10)
    return ax


def title_card(fig, s, ph):
    _target(fig)
    title_text(fig, 'MODULE 1 · GENRE STUDY', 'The thriller:\ncodes, conventions\nand themes',
               'North by Northwest · The Talented Mr Ripley · The Dry\nRevision for class tests and the end of year exam',
               'ENG315117 English')


def thumbnail(fig):
    _target(fig, 1.4)
    fig.text(0.05, 0.84, 'MODULE 1', ha='left', va='center', color=L.A2(), fontsize=66, weight='bold')
    fig.text(0.05, 0.60, 'THRILLER', ha='left', va='center', color=L.FG, fontsize=150, weight='bold')
    fig.text(0.05, 0.38, 'English ENG315117', ha='left', va='center', color=L.A1(), fontsize=70, weight='bold')
