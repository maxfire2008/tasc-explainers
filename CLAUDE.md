# Agent instructions: TASC course explainer videos

You are preparing **narrated, animated revision videos (a rough goal of 15–45 min)**, one per course module/criterion,
for Tasmanian TASC courses in maths and the sciences. Each video is one Python *spec* file plus a visuals file, built by
the `explainer` engine in this repo. The model to follow is `videos/PHY415115/c7_wave_motion.py` + `c7_visuals.py`: read
both in full before starting a new video.

Audience: students revising for **class tests and other internal assessment, and for the external exam**. Mention the
exam where relevant, but never present the video as being only for the exam.

**Agents do everything except render the video.** That means sources, spec, visuals, `check`, `preview`, `tts`, `docs`,
review and commits. **Never run `render` or `all`.** The operator runs the render as the final step (section 12).

**Aim for consistency.** Following this file on the same module should give essentially the same video, and on a different
module or course a video with the same structure, feel and rigour. So follow the defaults in section 3 and the
blueprint in section 4 rather than inventing a new format. If a video for the module already exists, audit and amend it
against the sources; don't start again from scratch.

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
  pipeline.py             sources / check / preview / tts / docs / render
template/video_template.py   minimal runnable spec with every feature, heavily commented
videos/<COURSE>/          one folder per course: <module>_<slug>.py (spec) + <module>_visuals.py (draw functions)
sources/<COURSE>/         content.csv (URLs + licences, operator-supplied) and cache/ (downloads, git-ignored)
out/<video id>/           all outputs (video, docs, subtitles, previews, caches); git-ignored
scripts/get_models.sh     downloads the Kokoro TTS model into models/kokoro/
pyproject.toml, uv.lock   Python dependencies (managed with uv: `uv add <package>`, then commit both files)
```

Commands (run from the repo root). **Use uv for all Python.** Don't use `pip`, a bare `python`, or `requirements.txt`:

```
uv sync                                                                 # creates .venv from pyproject.toml + uv.lock
bash scripts/get_models.sh                                              # Kokoro TTS model into models/kokoro/ (~340 MB)
uv run python -m explainer sources PHY415115                            # download + list source NAMEs
uv run python -m explainer check   videos/PHY415115/c7_wave_motion.py   # must report 0 errors
uv run python -m explainer preview videos/PHY415115/c7_wave_motion.py   # frames + contact sheets in out/<id>/preview/
uv run python -m explainer tts     videos/PHY415115/c7_wave_motion.py   # narration audio (cached)
uv run python -m explainer docs    videos/PHY415115/c7_wave_motion.py   # all docs + subtitles (needs tts)
```

Operator only, because they make the video:

```
uv run python -m explainer render  videos/PHY415115/c7_wave_motion.py   # [--burn-subs] [--force]
uv run python -m explainer all     videos/PHY415115/c7_wave_motion.py   # check -> tts -> render
```

Setup notes:
* Install uv if it's missing: `curl -LsSf https://astral.sh/uv/install.sh | sh`. Add a dependency with `uv add <package>`
  and commit `pyproject.toml` and `uv.lock` together. For a one-off tool, use `uv run --with <package> ...`.
* Outside Python, the project needs the **Inter** font for previews to look right, and `ffmpeg` (with libass for
  `--burn-subs`) for rendering. If matplotlib prints `findfont: Font family 'Inter' not found`, you're previewing in a
  fallback font: install Inter (`extras/ttf` from https://github.com/rsms/inter/releases) into `~/.local/share/fonts`, and
  delete matplotlib's font cache (`~/.cache/matplotlib`) if the warning continues. Don't judge text fit in the fallback font.
* If you can't install something, say so and carry on as far as you can. Never commit `.venv/`, `models/`, `out/` or `cache/`.

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

**Work on a branch** and commit at each natural point: instructions or engine changes, corrections, content, layout fixes.
Stage named files rather than `git add -A`, so stray files stay out. Don't push unless asked.

**Identify the module first.** Courses name things differently. Specs use the criterion code (`C6`, file
`videos/<COURSE>/c6_<slug>.py`, id `<COURSE>_C6_<slug>`). If the operator's name ("Module 3", a unit, a topic) doesn't appear in
the course document, map it to the closest criterion from the course's own structure and exam sections, then state that
mapping in your report. Stop and ask only if it could reasonably mean more than one criterion. Add the course and module
colours to `style.COURSE_ACCENTS` and `style.MODULE_ACCENTS` if they're new.

1. **Download and read every source for the module.** Run `uv run python -m explainer sources <COURSE>`, then extract text
   into your scratch space, not the repo:
   ```python
   from explainer.sources import extract_text, extract_pages
   pages = extract_pages('sources/PHY415115/cache/PHY415115-Physics-TASC-Exam-Paper-2024.pdf')  # pages[n-1] = page n
   ```
   Read: the course document (criterion standards table, all content dot points for the module, appendix/contexts, work
   requirements), the information sheet, the external assessment specifications, **every** exam paper's section for this
   criterion, and **every** assessment report's comments on it. Read them in full; don't sample or rely on keyword searches.
   * **Look at the information sheet as an image** (`pdftoppm -png -r 100 <pdf> <prefix>` and open it). Text extraction
     scrambles formulas and misses anything in a diagram. PHY415115's string and pipe wavelengths appear only beside diagrams.
   * Use the course's real content section. The same document may also have a curriculum-alignment list ("Unit 2 – Waves")
     that isn't the syllabus for this criterion.
   * Formats change between years. Section names vary ("Part 3" or "Section C"), question numbers shift, some papers
     offer either/or questions, and some reports are comments while others are mostly model answers. Use each source's own
     labels. A page with little extracted text may be an image, so render it and look.

2. **Build the coverage targets in the spec** (the checker fails if any target is uncovered):
   * `SYLLABUS`: every content dot point for the module, *plus* every context/example the course names for it
     (e.g. appendix contexts). **Split compound dot points and sub-bullets so each named idea is its own entry.** One broad
     entry lets a video pass `check` while missing content. Follow the course's order and wording closely.
   * `ELEMENTS`: every element of the criterion's standards table, **numbered by row position from the top
     (Element 1 = first row)** even if the document doesn't number them. Use these numbers in narration ("element
     three") and in `chip(fig, 'Element 3 · data')` tags on examples.
   * `EXAM_TOPICS`: one entry per question in this criterion's section of **every** past paper supplied, including optional
     questions, described **in your own words** and naming each main idea tested. Every topic must be taught somewhere. The
     checker warns if an exam file has no topics. If a paper isn't split by criterion, assign its questions by topic.
   * Build the page tables once as you read, as `EXAM_PAGES` and `REPORT_PAGES` do in the C7 spec. Copy that pattern,
     including its filter that drops report references no slide cites.

3. **Sort every target into a teaching level, then plan the running order.**

   | level | what belongs here | how it's taught |
   |---|---|---|
   | **Full** | course content; anything examined in two or more papers; a skill the standards name (e.g. analysing data), even if examined once | explanation with a diagram, plus a worked example where it's numerical |
   | **Short** | a method or trap from one exam that extends course content | one step on an existing scene |
   | **Brief mention** | a context from only one exam that isn't in the course content | a sentence or two, grouped on one shared "unfamiliar contexts" slide; no scene of its own |

   Aim for 15–45 minutes total. This is a rough goal, not a hard limit: going over is fine when the content needs it, and
   coverage always wins over duration. If it runs long, use the brief-mention level and tighten wording; don't drop targets.
   Spend time in proportion to (a) how much of the syllabus it is, (b) how often and how heavily it is examined, (c) how
   often the assessment reports say students get it wrong. `check` prints an estimated duration per part. State the estimate
   in your report.

4. **Write original worked examples.** Base their *style and difficulty* on past questions, never their text:
   change the context, the numbers and the structure. Include at least one example per element, A-standard
   reasoning (validity checks, reasoned predictions in unfamiliar contexts) and the common errors from the reports.
   Put every number you say or show into `CHECKS` (`(label, lambda: computed, expected, rel_tol)`), computed from the inputs
   rather than typed in. Well-known real-world facts are fine as contexts, but pick your own numbers.

5. **Write the spec**: refs, coverage, scenes, steps. One step = one narration chunk = one build state of a slide,
   10–30 s each. Tag every step with `refs`, `covers`, `elements`, `exam` as appropriate. Only tag what the step really
   teaches: `coverage.md` trusts these tags.

6. **Write the visuals** (`<module>_visuals.py`) using only `explainer.layout` helpers and matplotlib on `wax`/`gax`
   axes. Copy patterns from `c7_visuals.py` (section 7).

7. `uv run python -m explainer check <spec>` until **0 errors**. Treat warnings as a to-do list. Aim for 0 warnings: missing PDF
   page numbers and unreferenced sources must be fixed, not ignored.

8. **Audit against the sources, because a clean `check` isn't enough.** It only tests the lists you wrote. Go back through the
   course dot points and each past question, phrase by phrase, and find where the narration or slide teaches each one. Check
   each report comment on a common error, and each "on the sheet" and "not on the sheet" claim against the sheet image, in
   both directions. Fix any gap, then re-run `check`.

9. `uv run python -m explainer preview <spec>` and **look at every contact sheet** (`out/<id>/preview/_sheetNN.jpg`; open
   single frames at full size where text is dense). Fix overlaps, clipped text, text running off the slide, and labels
   colliding with the header or footer. Check that diagrams show correct science, not just tidy layout. Re-preview just the
   changed scenes with `--only scene_id ...`, and look again. Partial previews overwrite the low-numbered sheets, so run one
   full preview at the end. Moving a label can push it off the slide with no error, so confirm it's still there.

10. `tts`, then `docs` (not `render`). `tts` is slow: a test took about 2.5 minutes per minute of narration on a many-core
    machine, so a long video can take hours. Run it in the background and check on it. It caches each step, so re-running
    it resumes and only redoes changed text. Listen to a sample for mispronounced terms and fix them in `style.PRONUNCIATIONS`. Review
    `transcript.md`, `coverage.md` (no "NOT COVERED"), `references.md`, `timestamps.txt`, `description.txt` and the subtitles.

11. **Commit and hand over** (section 12).

---

## 4. Video blueprint

Use this structure for every video, adapting the content rather than the shape. Keep scene order close to the course's
content order, so students can follow along with the course document.

| order | scene(s) | contents |
|---|---|---|
| 1 | `title` (one step) | Title card: criterion name and course. Narration welcomes the viewer, and says it's for class tests and the exam, and what they'll be able to do. |
| 2 | *(engine)* | AI disclaimer. The engine places it after a first scene with the id `title`. |
| 3 | `intro` | Four steps: how the criterion is assessed (internal and external, from the assessment specifications) → the elements, by number → what the C, B and A standards ask for → the roadmap. |
| 4 | 3–5 Parts | Topic scenes, grouped under `P1 = 'Part 1 · …'`. `Scene.topic` becomes the YouTube chapter title. |
| 5 | `exam_tips` | Numbered tips drawn from the assessment reports, building up across steps. Add a `more_tips` scene if there are more than eight. |
| 6 | `summary` | "Criterion N in one screen": the key ideas as chips, then a short close that mentions tests and the exam. |
| 7 | *(engine)* | Credits and references. |

Within a Part, teach each topic in this order:
1. **Concept**, with a diagram or animation that builds up.
2. **Formula**, with its sheet status (`sheet_eq` or `learn_eq`) and what each letter means.
3. **Worked example** in its own scene or steps: `chip()` with the element, a question `card()`, one line of working per
   step, the answer in `GREEN`, and a validity check where it suits.
4. **Trap or tip** from the reports, said plainly ("Tip: …"), cited with its page.
5. **Real-world or unfamiliar context** for element four, plus any contexts the course names.

**Across the whole video:** cover every element more than once; include data and graph reading as well as calculation; show
what "explain" needs beyond "describe"; and teach method for sketches (arrows, labels, smooth curves), because exams mark them.

**Adapting to other subjects:**
* *Sciences* (Physics, Chemistry, Biology, Physical Sciences): diagrams, processes, data tables, graphs, experiments. Physical
  Sciences covers both physics and chemistry content, so follow its criteria, not the Physics ones.
* *Maths:* the "diagram" is usually a graph or a line-by-line derivation built up across steps. Worked examples carry more of
  the time. Say each algebra step in words. Topics are often examined across a whole paper, so assign questions by topic.
* *Formula sheets:* treat any supplied formula or data sheet as the information sheet, and set `InfoSheet.section` to its real
  heading. If a course has no sheet, set `info_sheet=None`, use `eq()` for formulas, and tell students to learn them. The
  fixed tag wording is in `style.py`, so raise it with the operator if a course needs different wording.
* Keep the voice, slide style, chips, cards, tips and pacing the same in every subject. Only `style.MODULE_ACCENTS` and
  `style.COURSE_ACCENTS` vary. Don't change engine or house style for a single video.

---

## 5. Non-negotiable rules

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
* exam questions by the paper's own section label and question number **with the PDF page**;
* assessment reports **with the page** where the comment appears.
Numbers are assigned by first appearance, so don't hard-code them.

**Information sheet.** Every formula shown is either
* `sheet_eq(...)`: it is on the information sheet. The slide gets a tag naming the sheet section, and the narration
  **on the slide where it first appears must say "information sheet" and name the section** (the checker enforces the
  phrase). Use the sheet's exact notation and letters (e.g. PHY415115 uses `w = λx/d` with x = slit-to-screen
  distance), and say what each letter means; or
* `learn_eq(...)`: it is *not* on the sheet, so tell students to learn or derive it, in the narration too; or
* plain `eq(...)`: only for things that aren't formulas to recall (e.g. `PD = r₂ − r₁`, a substitution line).
A formula may appear on the sheet only beside a diagram, and it still counts (use `sheet_eq`). A rearranged or extended form
that isn't printed is `learn_eq`. Verify each formula against the actual sheet before using `sheet_eq`, and set `Video.info_sheet.section` to the
sheet's real section heading. Constants on the sheet (e.g. speed of sound) also count: show them with `sheet_eq`.

**Coverage.** 100% of `SYLLABUS`, `ELEMENTS` and `EXAM_TOPICS`. To save time, shorten a topic; don't drop it. Course
content gets full teaching. A topic from a single exam that isn't in the course content still needs an `EXAM_TOPICS`
entry and a covering step, but a brief mention is enough.

**Accuracy.** The science and maths must be right. Never state from memory what is or isn't on the sheet, what a question
asked or what a report said: check the source. Keep to the course's depth, so qualitative topics stay qualitative. Recompute every number in `CHECKS`. Check that directions, signs, phase
changes and diagrams match the narration (e.g. reflected pulses not bigger than the incident pulse; rays bending the
right way).

---

## 6. Writing narration for the voice

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

## 7. Visual style

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
* Reusable patterns in `c7_visuals.py` (copy them into a new visuals file; keep draw functions per scene):
  * `extend(base, n, *extras)` adds steps after a finished scene without rewriting its `if s == …` logic.
  * `title_card` and `overview` split one draw function between the `title` and `intro` scenes; `summary` does the same for tips.
  * `_panel` and `refraction_contexts` show the shared "unfamiliar contexts" slide of mini diagrams for brief mentions.
  * Tip grids (`exam_tips`, `more_tips`), question cards plus working (`we_refraction`), graph pairs (`linearise`), and
    build-up comparisons (`pipe_id`).
* `card()` needs height ≥ `0.04 + frac(size + 4) + lines × frac(size)`, or its text spills out of the bottom. Wrap any
  bullet that would pass x ≈ 0.96.
* Use `ax.set_aspect('equal')` for circles and true angles, because axes are rarely square.

---

## 8. Changing style or voice

* Voice: edit `style.VOICE` (`voice`, `speed`, `lang`). The list of good Kokoro voices is in the comment. Changing it
  re-synthesises all narration (cache key includes the voice).
* Look: edit `style.py` / `layout.py`. Both are part of every clip's cache key, so the next render redoes every clip.
* Editing a helper function inside a visuals file does **not** change the clip cache key of the scenes that call it.
  If a video has already been rendered, tell the operator to use `render --force` after you edit shared helpers.

---

## 9. Outputs (out/<video id>/)

`docs` produces everything below except the two mp4 files, which only the operator's `render` makes.

| file | use |
|---|---|
| `<id>.mp4` | the video (1080p30, H.264/AAC) |
| `<id>_subtitled.mp4` | optional burnt-in styled subtitles (`--burn-subs`, needs ffmpeg with libass) |
| `<id>.srv3` | **styled YouTube subtitles** (colours, background, highlighted key terms). YouTube Studio → Subtitles → Upload file → *With timing* |
| `<id>.srt`, `<id>.vtt` | plain subtitles for other platforms |
| `timestamps.txt` | YouTube chapters (first is 0:00, each ≥ 10 s). Paste into the description |
| `description.txt` | ready-to-paste YouTube description: intro, AI notice, chapters, numbered references |
| `references.md` | full numbered reference list with attribution, licence, page and where each is shown |
| `coverage.md` | syllabus / element / exam-topic → timestamps (review for gaps; it reflects step tags, not teaching quality) |
| `transcript.md` | timestamped narration for proofreading |

Highlighted subtitle terms come from `Video.keywords` (course accent), plus built-in patterns: "information sheet",
"Element N", exam/test words (module accent) and warnings (pink). Patterns are in `subtitles.BASE_PATTERNS`.

---

## 10. Lessons learned / gotchas

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
* A scene drawn through `extend()` hashes `extend`'s source, not the base function's. If that video was already rendered,
  tell the operator to use `render --force` after those draw functions change.
* The copyright checker reads on-screen text too, so a run of graph tick labels can falsely match a paper's numbers. Set
  fewer ticks (`ax.set_yticks(...)`). Common phrases can also match: reword them rather than adding to `allowed_overlaps`.
* The checker matches every source, including ones the step doesn't cite. If it reports an uncited match with a `quotes`
  source for your own wording, reword it.
* Reports also reveal scope: PHY415115's 2021 report says one derivation is beyond the course. Respect such notes: still
  list the question, but don't teach beyond the course.
* Keep the terms the course and papers use (e.g. "band width" as well as "fringe width"), so students recognise them.
* A spec file's `TODO` notes and placeholder comments must be gone when you finish.

---

## 11. Definition of done

- [ ] All sources for the module read in full, and the information sheet viewed as an image
- [ ] `SYLLABUS` split into checkable points, `ELEMENTS` numbered by table row, `EXAM_TOPICS` lists every question of every paper
- [ ] Every target taught at the right level (section 3), and the audit against the sources is done
- [ ] Follows the blueprint: title card, disclaimer, overview, Parts, tips, summary, credits
- [ ] `check`: 0 errors, and ideally 0 warnings; no missing PDF page numbers; every source in `content.csv` referenced
- [ ] Every worked example is original, and every number is in `CHECKS`
- [ ] Information-sheet formulas use `sheet_eq` with the sheet's notation, and the narration names the sheet section
- [ ] Narration addresses tests *and* the exam; elements referred to by number
- [ ] Full preview reviewed: no overlaps or clipping, and diagrams are correct
- [ ] `tts` and `docs` run; `coverage.md` has no gaps; transcript, subtitles, timestamps, references and description reviewed
- [ ] Duration close to the 15–45 min goal (not a hard limit)
- [ ] Committed on a branch. **Not rendered**: that's the operator's step

---

## 12. Handing over

Stop before rendering. In your final report, give:
* the video's spec path and id, and any module mapping you assumed;
* the `check` result and the duration, from the narration audio if `tts` ran, otherwise marked as an estimate;
* anything you couldn't do or verify (e.g. a source that wouldn't download, or `tts` not run because the model wasn't available);
* the command for the operator: `uv run python -m explainer render videos/<COURSE>/<spec>.py`, and whether it needs `--force`.

After rendering, the operator watches a few minutes at several points and publishes the mp4 with the docs. If they report
a problem, fix the spec and hand back the same way.
