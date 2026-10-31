# TASC explainer videos

Generates narrated, animated revision videos (a rough goal of 15–45 min) for TASC course modules, with a consistent house style,
on-slide references, information-sheet callouts, YouTube chapters, styled subtitles and coverage checking.

Agents: read **CLAUDE.md** first. Agents prepare everything up to the thumbnail; the operator's render generates the narration, video and timed documents.

```bash
uv sync                                                   # also needs ffmpeg (+libass for burnt-in subs) and the Inter font
bash scripts/get_models.sh                                # Kokoro TTS model (~340 MB)
# list source URLs in sources/<COURSE>/content.csv (see sources/README.md), then:
uv run python -m explainer sources PHY415115                     # downloads + caches them
uv run python -m explainer check   videos/PHY415115/c7_wave_motion.py
uv run python -m explainer preview videos/PHY415115/c7_wave_motion.py
uv run python -m explainer thumbnail videos/PHY415115/c7_wave_motion.py
uv run python -m explainer render  videos/PHY415115/c7_wave_motion.py --burn-subs   # operator only
```

Outputs land in `out/<video id>/`: the mp4, `.srv3` styled YouTube subtitles, `.srt`/`.vtt`, `timestamps.txt`,
`description.txt`, `references.md`, `coverage.md`, `transcript.md`.

* House style, accents per course/module, voice: `explainer/style.py`
* New video: copy `template/video_template.py` (or the PHY415115 C7 example)
