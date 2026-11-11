"""Title card and thumbnail for Module 2 (adaptation: Rita Hayworth and Shawshank Redemption / The Shawshank Redemption)."""
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

from explainer import layout as L
from explainer.layout import wax, PINK
from explainer.spec import import_sibling

title_text = import_sibling(__file__, 'eng_common.py').title_text


def _book_to_film(fig, a=1.0):
    """Signature graphic: an open book on the left, a film strip on the right, and an arrow of transformation between them."""
    ax = wax(fig, [0.50, 0.08, 0.48, 0.84], (0, 10), (0, 8.5))
    ax.set_aspect('equal')
    # book
    ax.add_patch(FancyBboxPatch((0.4, 1.8), 3.0, 4.4, boxstyle='round,pad=0,rounding_size=0.15', fc=L.PANEL, ec=L.A2(), lw=5 * a))
    ax.add_patch(FancyBboxPatch((3.5, 1.8), 3.0 - 0.1, 4.4, boxstyle='round,pad=0,rounding_size=0.15', fc=L.PANEL, ec=L.A2(), lw=5 * a))
    for k in range(7):
        y = 5.5 - k * 0.55
        ax.plot([0.8, 3.0], [y, y], color=L.GRID, lw=4 * a)
        ax.plot([3.9, 6.0 - 0.1 - 0.1], [y, y], color=L.GRID, lw=4 * a)
    # film strip
    ax.add_patch(Rectangle((6.9, 0.8), 2.6, 6.4, fc=L.PANEL2, ec=L.A1(), lw=5 * a))
    for k in range(4):
        ax.add_patch(Rectangle((7.15, 1.1 + k * 1.55), 2.1, 1.25, fc=L.BG, ec=L.GRID, lw=2))
    for k in range(9):
        for x in (6.97, 9.33):
            ax.add_patch(Rectangle((x, 0.95 + k * 0.7), 0.1, 0.3, fc=L.GRID, ec='none'))
    L.arrow(ax, (6.3, 4.0), (6.85, 4.0), color=PINK, lw=6 * a, ms=34)
    return ax


def title_card(fig, s, ph):
    _book_to_film(fig)
    title_text(fig, 'MODULE 2 · ADAPTATION STUDY', 'From page to screen:\nhow meaning changes',
               'Rita Hayworth and Shawshank Redemption · The Shawshank Redemption\nRevision for class tests and the end of year exam',
               'ENG315117 English')


def thumbnail(fig):
    _book_to_film(fig, 1.4)
    fig.text(0.05, 0.84, 'MODULE 2', ha='left', va='center', color=L.A2(), fontsize=66, weight='bold')
    fig.text(0.05, 0.60, 'ADAPTATION', ha='left', va='center', color=L.FG, fontsize=100, weight='bold')
    fig.text(0.05, 0.38, 'English ENG315117', ha='left', va='center', color=L.A1(), fontsize=70, weight='bold')
