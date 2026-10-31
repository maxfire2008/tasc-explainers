# Sources

One folder per course code, e.g. `sources/PHY415115/`, containing **`content.csv`**: one row per source,
`url,licence,attribution`, no header:

    https://www.tasc.tas.gov.au/students/courses/science/phy415115-9/,attribution,"Government of Tasmania, Tasmanian Assessment, Standards and Certification (TASC). Accessed 2026-10-31."
    https://assets.tasc.tas.gov.au/uploads/2026/06/PHY415115-Physics-TASC-Exam-Paper-2024.pdf,copyrighted,
    https://assets.tasc.tas.gov.au/uploads/2026/06/PHY415115-Physics-Assessment-Report-2024.pdf,quotes,

licence: `attribution` | `quotes` | `copyrighted` (see CLAUDE.md section 2).

`uv run python -m explainer sources PHY415115` downloads every URL into `sources/PHY415115/cache/` (git-ignored) and lists
the source NAMEs specs use in `Ref(...)`.  If a download is blocked, place the file at the printed cache path.

`content.example.csv` is the full list for the PHY415115 example; copy it to `sources/PHY415115/content.csv`.
