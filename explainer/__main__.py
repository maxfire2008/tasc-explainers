"""CLI:  python -m explainer <command> <spec.py> [options]

commands
  sources  download/cache every URL in content.csv and list source NAMES  (--refresh to re-download)
  check    validate coverage, references, copyright overlap, info-sheet mentions, numeric checks
  preview  draw one frame per step + contact sheets into out/<id>/preview/   (--only scene_id ...)
  tts      synthesise narration (cached)
  docs     timestamps, references, coverage, transcript, description, subtitles (needs tts)
  render   full video + all docs + subtitles  (--force re-renders cached clips, --burn-subs)
  all      check (must pass) -> tts -> render
"""
import argparse
import sys

from . import pipeline as P
from .spec import load


def main():
    ap = argparse.ArgumentParser(prog='python -m explainer')
    ap.add_argument('command', choices=['sources', 'check', 'preview', 'tts', 'docs', 'render', 'all'])
    ap.add_argument('spec', help='spec file (or, for `sources`, a spec file or a course code)')
    ap.add_argument('--refresh', action='store_true', help='sources: re-download even if cached')
    ap.add_argument('--only', nargs='*', help='preview: only these scene ids')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--burn-subs', action='store_true')
    ap.add_argument('--allow-missing-sources', action='store_true',
                    help='development only: missing source files become warnings')
    ap.add_argument('--no-copyright-scan', action='store_true')
    a = ap.parse_args()
    if a.command == 'sources':
        course = a.spec if not a.spec.endswith('.py') else load(a.spec).course
        P.list_sources(course, a.refresh)
        return
    v = load(a.spec)
    if a.command == 'check':
        errs, _ = P.check(v, a.allow_missing_sources, not a.no_copyright_scan)
        sys.exit(1 if errs else 0)
    if a.command == 'preview':
        P.preview(v, a.only)
    elif a.command == 'tts':
        P.make_tts(v)
    elif a.command == 'docs':
        P.docs_only(v)
    elif a.command == 'render':
        P.render(v, a.force, a.burn_subs)
    elif a.command == 'all':
        errs, _ = P.check(v, a.allow_missing_sources, not a.no_copyright_scan)
        if errs:
            sys.exit('check failed: fix the errors above before rendering')
        P.make_tts(v)
        P.render(v, a.force, a.burn_subs)


if __name__ == '__main__':
    main()
