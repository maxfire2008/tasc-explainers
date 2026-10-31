"""Scenes the framework adds to EVERY video: the AI disclaimer (first) and credits (last).
Specs must not define these themselves."""
from . import layout as L
from . import style as S
from .spec import Scene, Step

DISCLAIMER_ID = '_disclaimer'
CREDITS_ID = '_credits'


def _disclaimer(fig, s, ph):
    L.box(fig, 0.15, 0.30, 0.70, 0.40, fc=L.PANEL, ec=L.PINK, lw=3)
    fig.text(0.5, 0.635, '⚠  ' + S.DISCLAIMER_TITLE, ha='center', va='center', color=L.PINK, fontsize=44,
             weight='bold')
    fig.text(0.5, 0.47, S.DISCLAIMER_BODY, ha='center', va='center', color=L.FG, fontsize=24, linespacing=1.5)


def _make_credits(video):
    def draw(fig, s, ph):
        fig.text(0.5, 0.84, 'Credits', ha='center', color=L.FG, fontsize=48, weight='bold')
        y = 0.75
        lines = getattr(video, 'credit_lines', None) or [('(credits are filled in by the pipeline)', L.SOFT, 22)]
        for t, c, sz in lines:
            fig.text(0.5, y, t, ha='center', va='top', color=c, fontsize=sz)
            y -= L.frac(sz) * (t.count('\n') + 1) + 0.016
    return draw


def wrap(video):
    ids = [sc.id for sc in video.scenes]
    if DISCLAIMER_ID not in ids:
        video.scenes.insert(0, Scene(DISCLAIMER_ID, '', 'AI disclaimer', _disclaimer,
                                     [Step(S.DISCLAIMER_NARRATION, min_dur=S.MIN_CHAPTER)]))
    if CREDITS_ID not in ids:
        video.scenes.append(Scene(CREDITS_ID, '', 'Credits and references', _make_credits(video),
                                  [Step(S.CREDITS_NARRATION.format(holder=S.COPYRIGHT_HOLDER), min_dur=S.MIN_CHAPTER)]))
