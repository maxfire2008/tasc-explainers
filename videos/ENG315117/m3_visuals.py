"""Title card, thumbnail and the river-flat diagram for Module 3 (close text study: The Secret River, the play)."""
import numpy as np
from matplotlib.patches import Rectangle, Circle, Polygon

from explainer import layout as L
from explainer.layout import wax, label, arrow, GRID, PINK, GREEN, YELLOW, TAU
from explainer.spec import import_sibling

title_text = import_sibling(__file__, 'eng_common.py').title_text


def _river_art(fig, a=1.0):
    """Signature graphic: a river between two banks, a low sun, and a row of fence posts that start to look like bars."""
    ax = wax(fig, [0.45, 0.06, 0.53, 0.86], (0, 10), (0, 10))
    y = np.linspace(0, 10, 200)
    xc = 5 + 1.4 * np.sin(y * 0.75)
    ax.fill_betweenx(y, xc - 0.9, xc + 0.9, color=L.A1(), alpha=0.35)
    ax.plot(xc - 0.9, y, color=L.A1(), lw=5 * a)
    ax.plot(xc + 0.9, y, color=L.A1(), lw=5 * a)
    t = np.linspace(0, TAU, 100)
    ax.fill(8.2 + 0.9 * np.cos(t), 7.8 + 0.9 * np.sin(t), color=L.A2(), alpha=0.9)
    for k in range(7):
        x = 0.5 + k * 0.62
        ax.add_patch(Rectangle((x, 1.2), 0.2, 3.2, fc=L.PANEL2, ec=L.FG, lw=2.5 * a))
    ax.plot([0.4, 4.7], [3.8, 3.8], color=L.FG, lw=3 * a)
    return ax


def title_card(fig, s, ph):
    _river_art(fig)
    title_text(fig, 'MODULE 3 · CLOSE TEXT STUDY', 'The Secret River:\nperspectives on place\nand belonging',
               'Andrew Bovell’s play, adapted from the novel by Kate Grenville\nRevision for class tests and the end of year exam',
               'ENG315117 English')


def thumbnail(fig):
    _river_art(fig, 1.4)
    fig.text(0.05, 0.84, 'MODULE 3', ha='left', va='center', color=L.A2(), fontsize=66, weight='bold')
    fig.text(0.05, 0.60, 'PERSPECTIVES', ha='left', va='center', color=L.FG, fontsize=100, weight='bold')
    fig.text(0.05, 0.38, 'English ENG315117', ha='left', va='center', color=L.A1(), fontsize=70, weight='bold')


def river_flat(fig, s, ph):
    """Build-up diagram: one river flat, two claims."""
    L.header(fig, 'One river flat, two claims')
    L.chip(fig, 'Element 3 · construction of perspective')
    ax = wax(fig, [0.04, 0.09, 0.92, 0.72], (0, 16), (0, 8))
    ax.set_aspect('equal')
    y = np.linspace(0, 8, 200)
    xc = 8 + 0.6 * np.sin(y * 0.9)
    ax.fill_betweenx(y, xc - 0.7, xc + 0.7, color=L.A1(), alpha=0.35)
    ax.plot(xc - 0.7, y, color=L.A1(), lw=3)
    ax.plot(xc + 0.7, y, color=L.A1(), lw=3)
    label(ax, 8.1, 0.45, 'the river (Dhirrumbim)', size=20, color=L.A1(), bbox=dict(fc=L.BG, ec='none', pad=2))
    if s >= 1:                                  # Thornhill's claim
        ax.add_patch(Rectangle((1.2, 2.2), 4.4, 3.8, fc='none', ec=YELLOW, lw=3, ls='--'))
        ax.add_patch(Rectangle((2.0, 4.8), 1.0, 0.8, fc=L.PANEL2, ec=L.FG, lw=2.5))
        ax.add_patch(Polygon([(1.9, 5.6), (2.5, 6.1), (3.1, 5.6)], fc=L.PANEL2, ec=L.FG, lw=2.5))
        for k in range(4):
            ax.plot([3.6 + k * 0.45] * 2, [2.7, 4.2], color=L.GREEN, lw=3)
        label(ax, 3.4, 6.55, 'Thornhill: 100 acres, a dug square', size=24, color=YELLOW)
        label(ax, 3.4, 1.65, '“This is my place now.”', size=26, color=YELLOW, style='italic')
    if s >= 2:                                  # Dharug place
        ax.add_patch(Circle((12.6, 5.0), 0.45, fc=L.PINK, ec='none', alpha=0.85))
        for dx in (-1.0, 1.0):
            ax.add_patch(Polygon([(12.6 + dx - 0.45, 4.3), (12.6 + dx, 5.3), (12.6 + dx + 0.45, 4.3)], fc=L.PANEL2, ec=L.FG, lw=2.5))
        label(ax, 12.6, 6.55, 'Dharug camp and country', size=24, color=L.A2())
        label(ax, 12.6, 1.65, '“This is our place. Our country.”', size=26, color=L.A2(), style='italic')
    if s >= 3:                                  # yams in Thornhill's dug square
        for k in range(5):
            ax.plot([4.2 + k * 0.28], [3.2], marker='*', ms=18, color=L.A2(), ls='')
    if s == 3:
        label(ax, 8.2, 7.45, 'the yams he digs up are Dharug food', size=24, color=L.A2(), bbox=dict(fc=L.BG, ec='none', pad=2))
        arrow(ax, (7.2, 7.2), (4.9, 3.5), color=L.A2(), lw=3)
    if s >= 4:                                  # the fence at the end
        ax.plot([6.15, 6.15], [1.8, 6.2], color=PINK, lw=6)
        for yy in np.linspace(1.9, 6.1, 9):
            ax.plot([5.9, 6.4], [yy, yy], color=PINK, lw=3)
        label(ax, 8.2, 7.45, 'The fence looks like bars. Which side is Thornhill on?', size=24, color=PINK, bbox=dict(fc=L.BG, ec='none', pad=2))
