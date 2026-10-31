# Agent instructions: TASC course explainer videos

You are building **narrated, animated revision videos (a rough goal of 15–45 min)**, one per course module/criterion, for Tasmanian
TASC courses. Each video is one Python *spec* file (plus a visuals file) rendered by the `explainer` engine in this repo.
The worked example is `videos/PHY415115/c7_wave_motion.py` + `c7_visuals.py`: read both before starting a new video.

Audience: students revising for **class tests and other internal assessment, and for the external exam**. Mention the
exam where relevant, but never present the video as being only for the exam.

---

## 1. Repo map

```
CLAUDE.md                 this file
explainer/                the engine (shared by every video). Change with care.
  style.py                ALL house style: colours, course/module accents, VOICE, timing, wording, thresholds
  layout.py               drawing helpers (header, bullets, card, sheet_eq, learn_eq, chip, wax, gax, arrows...)
  spec.py                 data model: Video, Scene, Step, Ref, InfoSheet
  builtin.py              AI-disclaimer scene (first, or after a `title` scene) and credits scene (last), added automatically
  sources.py              content.csv, download + cache, text extraction, verbatim-overlap checker
  tts.py                  narration synthesis (Kokoro), cached by text+voice hash
  subtitles.py            .srv3 (styled, YouTube) .srt .vtt .ass (burn-in)
  pipeline.py             check / preview / tts / docs / render
template/video_template.py   minimal runnable spec with every feature, heavily commented
videos/<COURSE>/          one folder per course: <module>_<slug>.py (spec) + <module>_visuals.py (draw functions)
sources/<COURSE>/         content.csv (URLs + licences, operator-supplied) and cache/ (downloads, git-ignored)
out/<video id>/           all outputs (video, docs, subtitles, previews, caches)
scripts/get_models.sh     downloads the Kokoro TTS model into models/kokoro/
pyproject.toml, uv.lock   Python dependencies (managed with uv: `uv add <package>`, then commit both files)
```

Commands (run from the repo root):

```
uv sync                                                        # creates .venv from pyproject.toml + uv.lock; also needs ffmpeg (with libass for --burn-subs) and the Inter font
bash scripts/get_models.sh
uv run python -m explainer sources PHY415115                          # download + list source NAMEs
uv run python -m explainer check   videos/PHY415115/c7_wave_motion.py   # must report 0 errors
uv run python -m explainer preview videos/PHY415115/c7_wave_motion.py   # frames + contact sheets in out/<id>/preview/
uv run python -m explainer tts     videos/PHY415115/c7_wave_motion.py
uv run python -m explainer render  videos/PHY415115/c7_wave_motion.py   # [--burn-subs] [--force]
uv run python -m explainer docs    videos/PHY415115/c7_wave_motion.py   # docs + subtitles only (needs tts)
uv run python -m explainer all     videos/PHY415115/c7_wave_motion.py   # check -> tts -> render
```

---

## 2. Inputs from the operator: `content.csv`

The operator supplies **`sources/<COURSE>/content.csv`** (or `sources/content.csv`). There's no header; the columns are
URL, licence and attribution:

```
https://www.tasc.tas.gov.au/students/courses/science/phy415115-9/,attribution,"Government of Tasmania, Tasmanian Assessment, Standards and Certification (TASC). Accessed 2026-10-31."
https://assets.tasc.tas.gov.au/uploads/2026/06/PHY415115-Physics-TASC-Exam-Paper-2024.pdf,copyrighted,
https://assets.tasc.tas.gov.au/uploads/2026/06/PHY415115-Physics-Assessment-Report-2024.pdf,quotes,
```

The engine downloads each URL once into `sources/<COURSE>/cache/` (with `index.json` recording URL, date, size and
sha256) and uses the cached copy from then on. `--refresh` re-downloads.

```
uv run python -m explainer sources PHY415115            # download/cache everything, list NAME / licence / size / URL
uv run python -m explainer sources PHY415115 --refresh  # re-download (e.g. a paper was updated)
```

* **Source NAME** = the last part of the URL path, URL-decoded; if it has no extension, `.html` is added
  (`.../phy415115-9/` → `phy415115-9.html`). Cite a source in a spec with `Ref(NAME, ...)`, or with the full URL.
  Always copy NAMEs from the `sources` listing.
* If a download fails (blocked network, login wall), the command prints the exact cache path. Ask the operator to put
  the file there; it is then used exactly as if downloaded. Never invent a source's content.
* PDFs are detected by content, so a URL without `.pdf` still parses correctly.
* `content.csv` holds only URLs and licences, so it can be committed; `cache/` is git-ignored.

| licence | what you may do |
|---|---|
| `attribution` | Adapt and quote freely. Must be credited (the attribution text is shown in credits and references). |
| `quotes` | Short verbatim quotes only (≤ `style.QUOTE_MAX_WORDS` words), and the step must cite that source. Paraphrase everything else. |
| `copyrighted` | **Reference only.** No verbatim text, no copied diagrams or data, no copied or lightly reworded questions. You may say *what topic* was examined and cite it. |

---

## 3. Workflow for a new video

1. **Download and read every source for the module.** Run `uv run python -m explainer sources <COURSE>`, then extract text:
   ```python
   from explainer.sources import extract_text, extract_pages
   pages = extract_pages('sources/PHY415115/cache/PHY415115-Physics-TASC-Exam-Paper-2024.pdf')  # pages[n-1] = page n
   ```
   Read: the course document (criterion standards table, all content dot points for the module, appendix/contexts,
   work requirements), the information sheet, the external assessment specifications, **every** exam paper's section
   for this criterion, and **every** assessment report's comments on it.

2. **Build the coverage targets in the spec** (the checker fails if any target is uncovered):
   * `SYLLABUS`: every content dot point for the module, *plus* every context/example the course names for it
     (e.g. appendix contexts). Split compound dot points so each is checkable.
   * `ELEMENTS`: every element of the criterion's standards table, **numbered by row position from the top
     (Element 1 = first row)** even if the document doesn't number them. Use these numbers in narration ("element
     three") and in `chip(fig, 'Element 3 · data')` tags on examples.
   * `EXAM_TOPICS`: one entry per question (or major part) in this criterion's section of **every** past paper
     supplied, described **in your own words**. Every topic must be taught somewhere. The checker warns if an exam
     file has no topics.

3. **Plan the running order and time budget.** Aim for 15–45 minutes total. This is a rough goal, not a hard limit:
   going over is fine when the content needs it, and coverage always wins over duration. Spend time in proportion to
   (a) how much of the syllabus it is, (b) how often and how heavily it is examined, (c) how often the assessment
   reports say students get it wrong. To stay close to the goal, give a **brief mention** (a sentence or two, no scene
   of its own) to anything that appeared in only one exam and isn't in the course content. Group scenes into 3–5 Parts; `Scene.topic` becomes the YouTube chapter title. Typical shape:
   overview (assessment, elements, standards) → Parts → tips for tests and the exam → summary. The engine adds the
   disclaimer and credits. `check` prints an estimated duration per part.

4. **Write original worked examples.** Base their *style and difficulty* on past questions, never their text:
   change the context, the numbers and the structure. Include at least one example per element, A-standard
   reasoning (validity checks, reasoned predictions in unfamiliar contexts) and the common errors from the reports.
   Put every number you say or show into `CHECKS` (`(label, lambda: computed, expected, rel_tol)`).

5. **Write the spec**: refs, coverage, scenes, steps. One step = one narration chunk = one build state of a slide,
   10–30 s each. Tag every step with `refs`, `covers`, `elements`, `exam` as appropriate.

6. **Write the visuals** (`<module>_visuals.py`) using only `explainer.layout` helpers and matplotlib on `wax`/`gax`
   axes. Copy patterns from `c7_visuals.py`.

7. `uv run python -m explainer check <spec>` until **0 errors**. Treat warnings as a to-do list. Missing PDF page numbers
   and unreferenced sources must be fixed, not ignored.

8. `uv run python -m explainer preview <spec>` and **look at every contact sheet** (`out/<id>/preview/_sheetNN.jpg`; open
   single frames at full size where text is dense). Fix overlaps, clipped text, text running off the slide, and labels
   colliding with the header or footer. Re-preview just the changed scenes with `--only scene_id ...`.

9. `tts`, then `render`. A full render of a 30–40 min video takes about 10–20 min on 2 CPUs; clips are cached, so
   re-renders only redo changed steps.

10. Review `out/<id>/`: watch a few minutes at several points, check `coverage.md` (no "NOT COVERED"),
    `references.md`, `timestamps.txt` and the subtitles. Deliver the mp4 with the docs.

---

## 4. Non-negotiable rules

**Copyright.** Obey section 2. `check` scans narration *and all on-screen text* against every source and fails on
any run of 8+ words from a `copyrighted` file, on over-long or uncited quotes from a `quotes` file, and warns on
uncited text from an `attribution` file. A clean check does not make close paraphrase of an exam question
acceptable: write genuinely new questions. Add to `allowed_overlaps` only for unavoidable generic phrases (e.g. the
criterion's own title from an attribution-licensed course document).

**AI disclosure.** The disclaimer scene and the "AI generated content" footer on every slide are added by the engine.
The disclaimer comes first, or second when the spec's first scene has the id `title` (a title card). Never remove or bypass them, and never draw a slide outside the pipeline.

**References.** Every slide that relies on a source cites it in `Step.refs`. The footer shows `Refs [n]`, and
`references.md`/`description.txt` list them with locator, page, **URL** and licence. Write `Ref.loc` so it reads
well on its own (e.g. `2024 exam, Section C, Question 16`). Cite:
* the course document for content and standards (locator = section name);
* the information sheet (cited automatically when `sheet_eq` is used);
* exam questions as `Section X, Question N` **with the PDF page**;
* assessment reports **with the page** where the comment appears.
Numbers are assigned by first appearance, so don't hard-code them.

**Information sheet.** Every formula shown is either
* `sheet_eq(...)`: it is on the information sheet. The slide gets a tag naming the sheet section, and the narration
  **on the slide where it first appears must say "information sheet" and name the section** (the checker enforces the
  phrase). Use the sheet's exact notation and letters (e.g. PHY415115 uses `w = λx/d` with x = slit-to-screen
  distance), and say what each letter means; or
* `learn_eq(...)`: it is *not* on the sheet, so tell students to learn or derive it; or
* plain `eq(...)`: only for things that aren't formulas to recall (e.g. `PD = r₂ − r₁`, a substitution line).
Verify each formula against the actual sheet before using `sheet_eq`, and set `Video.info_sheet.section` to the
sheet's real section heading. Constants on the sheet (e.g. speed of sound) also count: show them with `sheet_eq`.

**Coverage.** 100% of `SYLLABUS`, `ELEMENTS` and `EXAM_TOPICS`. To save time, shorten a topic; don't drop it. Course
content gets full teaching. A topic from a single exam that isn't in the course content still needs an `EXAM_TOPICS`
entry and a covering step, but a brief mention is enough.

**Accuracy.** Physics/maths must be right. Recompute every number in `CHECKS`. Check that directions, signs, phase
changes and diagrams match the narration (e.g. reflected pulses not bigger than the incident pulse; rays bending the
right way).

---

## 5. Writing narration for the voice

The narration is read by a TTS model, so write what should be *heard*:
* Numbers in words where precision matters: "zero point two five hertz", "three times ten to the eight metres per
  second", "sixty one point zero degrees". Units in full ("metres per second", "newtons").
* No symbols: write "lambda", "theta c", "mu", "equals", "over", "squared", "root", "percent", "minus". The checker
  warns about `λ θ μ = / ^ √ ≈ ° % < >` etc. in narration.
* Short sentences, one idea each, ~150–160 words per minute. A step is 25–80 words.
* Course codes and acronyms are fixed in `style.PRONUNCIATIONS` (e.g. `PHY415115`). Add new ones there, not in the
  narration, so subtitles stay readable.
* Subtitles are generated from the narration text. Keep it clean prose (no stage directions or markup).
* Say "element two" etc. when an example targets an element; "Tip:" for exam/test advice.

---

## 6. Visual style

* Use `explainer.layout` helpers only; never hard-code colours. Course accent `L.A1()`, module accent `L.A2()`
  (both set from `style.COURSE_ACCENTS` / `style.MODULE_ACCENTS`; add entries there for a new course/module).
  Semantic colours: `PINK` warnings/destructive/nodes, `GREEN` answers/constructive, `YELLOW` equations and highlights.
* Canvas 1920×1080. Keep content in x 0.04–0.96, y 0.07–0.82. The header (part label + title) sits above, and the footer
  (course, refs, AI notice) below. `chip()` defaults to the top-right corner.
* Minimum font size about 17 pt; body 22–28 pt; titles come from `header()`.
* Slides **build up** across steps (`s` = step index): add elements rather than replacing the whole layout, so the
  viewer keeps their place. The newest bullet is bright and older ones are dimmed (`bullets(..., dim=True)`).
* Animations: set `Step(anim=period_seconds)`. Frames for one period are drawn and looped, so everything periodic
  must complete a whole number of cycles as `ph` goes 0→1 (use `TAU * n * ph` with integer `n`). Keep periods short
  (1–6 s) because each frame costs ~0.1–0.3 s. Phase continues across consecutive animated steps of a scene.
* Every animated or dense slide: check it in preview.

---

## 7. Changing style or voice

* Voice: edit `style.VOICE` (`voice`, `speed`, `lang`). The list of good Kokoro voices is in the comment. Changing it
  re-synthesises all narration (cache key includes the voice).
* Look: edit `style.py` / `layout.py`. Both are part of every clip's cache key, so the next render redoes every clip.
* Editing a helper function inside a visuals file does **not** change the clip cache key of the scenes that call it.
  Use `render --force` after editing shared helpers.

---

## 8. Outputs (out/<video id>/)

| file | use |
|---|---|
| `<id>.mp4` | the video (1080p30, H.264/AAC) |
| `<id>_subtitled.mp4` | optional burnt-in styled subtitles (`--burn-subs`, needs ffmpeg with libass) |
| `<id>.srv3` | **styled YouTube subtitles** (colours, background, highlighted key terms). YouTube Studio → Subtitles → Upload file → *With timing* |
| `<id>.srt`, `<id>.vtt` | plain subtitles for other platforms |
| `timestamps.txt` | YouTube chapters (first is 0:00, each ≥ 10 s). Paste into the description |
| `description.txt` | ready-to-paste YouTube description: intro, AI notice, chapters, numbered references |
| `references.md` | full numbered reference list with attribution, licence, page and where each is shown |
| `coverage.md` | syllabus / element / exam-topic → timestamps (review for gaps) |
| `transcript.md` | timestamped narration for proofreading |

Highlighted subtitle terms come from `Video.keywords` (course accent), plus built-in patterns: "information sheet",
"Element N", exam/test words (module accent) and warnings (pink). Patterns are in `subtitles.BASE_PATTERNS`.

---

## 9. Lessons learned / gotchas

* Exam *questions* tend to probe things the syllabus lists in one line (e.g. direction of travel from graphs, end
  correction, 90° − θ geometry, tension from a hanging mass, scattering polarisation, radio reflection from metal).
  Map every past question to a teaching step; that's what `EXAM_TOPICS` is for.
* Assessment reports are the best source of "tips": quote sparingly (licence `quotes`) and cite page numbers.
* matplotlib mathtext: `\dfrac`, `\sqrt`, `^\circ`, `\Rightarrow`, `\mathrm{}` work; `\text{}` doesn't.
  Unicode sub/superscripts (`λ₁`, `m s⁻¹`) work in plain text.
* Long lines overflow silently. Wrap with `\n`, and always check the contact sheets.
* Labels near the top of the content area can collide with long titles. Keep diagrams below y ≈ 0.82.
* `preview` draws animated steps at phase 0.3, so check that mid-animation frames look right too.
* Kokoro sometimes mispronounces jargon. Fix it with `style.PRONUNCIATIONS`, then re-run `tts` (only changed steps
  regenerate).
* All clips must share encoder settings (they do via `style.VIDEO`) because they are joined with `-c copy`.
* A scene drawn through `extend()` (in a visuals file) hashes `extend`'s source, not the base function's, so use
  `render --force` after editing those draw functions.
* Keep the render command in the foreground or check on it; background jobs may be stopped when a session idles.

---

## 10. Definition of done

- [ ] All sources for the module read; `SYLLABUS`, `ELEMENTS` (numbered by table row), `EXAM_TOPICS` (every paper) complete
- [ ] `check`: 0 errors; no missing PDF page numbers; every source in `content.csv` referenced
- [ ] Every worked example is original, and every number is in `CHECKS`
- [ ] Information-sheet formulas use `sheet_eq` with the sheet's notation, and the narration names the sheet section
- [ ] Narration addresses tests *and* the exam; elements referred to by number
- [ ] Preview contact sheets reviewed; no overlaps or clipping
- [ ] Rendered; duration close to the 15–45 min goal (not a hard limit); `coverage.md` has no gaps; subtitles, timestamps, references and description generated
