#!/usr/bin/env python3
"""Interactive batch renderer for every video spec in videos/.

    uv run python scripts/render_queue.py [--workers 4] [--force] [--burn-subs] [--all]

1. Pick videos in an interactive menu: type a number in a row's ORDER cell to select it and set
   its place in the queue, press x/tab to make it EXCLUSIVE (runs alone) or parallel, enter to
   start. Without a TTY a prompt like "5 2x 1" is used instead.
2. Videos render in that order, WORKERS at a time (default 4); an exclusive video waits for the
   running ones to finish, runs alone, and nothing starts until it is done.
3. A video that crashes goes to a retry queue. When the main queue is empty the retry queue
   runs ONE at a time; a video that crashes again goes to the back of that queue. Retries
   repeat until you press Ctrl-C.
4. After every render finishes, a status report is printed. Every line of render output is
   printed with a "[<video id>]" prefix.

Operator tool: this runs `render`, so it is not for the development machine.
"""
import argparse
import os
import re
import signal
import subprocess
import sys
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ID_RE = re.compile(r"""\bid\s*=\s*['"]([A-Za-z0-9_\-]+)['"]""")

print_lock = threading.Lock()
procs = {}            # video id -> Popen, for clean shutdown
procs_lock = threading.Lock()
stopping = threading.Event()


def say(msg=''):
    with print_lock:
        print(msg, flush=True)


# ---------------------------------------------------------------- discovery
def discover():
    """[(video id, spec path)] for every spec under videos/ (files that build a Video)."""
    found = []
    for p in sorted((ROOT / 'videos').glob('*/*.py')):
        text = p.read_text(encoding='utf-8')
        if not re.search(r'\bVideo\(', text):
            continue
        # the id is the first `id='...'` after `Video(`
        m = ID_RE.search(text[re.search(r'\bVideo\(', text).start():])
        if m:
            found.append((m.group(1), p.relative_to(ROOT)))
    return found


# ---------------------------------------------------------------- menu
def finish(items, order, excl):
    """Selected rows sorted by their order cell (ties keep listing order) -> [(vid, spec, exclusive)]."""
    rows = [(int(order[i]), i) for i in range(len(items)) if order[i]]
    return [(items[i][0], items[i][1], excl[i]) for _, i in sorted(rows)]


def menu_curses(items):
    import curses

    def run(scr):
        curses.curs_set(0)
        n = len(items)
        order = [''] * n          # the typed order cell; blank = not selected
        excl = [False] * n
        cur = top = 0
        fresh = False             # True right after moving onto a row: first digit replaces the cell
        while True:
            h, w = scr.getmaxyx()
            rows = max(1, h - 5)
            cur = max(0, min(cur, n - 1))
            top = min(max(top, cur - rows + 1), cur)
            scr.erase()
            scr.addnstr(0, 0, 'Select videos to render', w - 1, curses.A_BOLD)
            scr.addnstr(1, 0, 'up/down move | type digits in the ORDER cell (backspace clears) | space select/deselect',
                        w - 1)
            scr.addnstr(2, 0, 'x or tab: toggle EXCLUSIVE (runs alone) / parallel | a all | n none | enter start | q quit',
                        w - 1)
            scr.addnstr(3, 0, ' ORDER  MODE       VIDEO', w - 1, curses.A_UNDERLINE)
            for i in range(top, min(n, top + rows)):
                mode = ('exclusive' if excl[i] else 'parallel ') if order[i] else '          '
                line = f' [{order[i]:>3}]  {mode} {items[i][0]}  ({items[i][1]})'
                scr.addnstr(4 + i - top, 0, line, w - 1, curses.A_REVERSE if i == cur else 0)
            scr.addnstr(h - 1, 0, f'{sum(1 for o in order if o)} selected', w - 1)
            scr.refresh()
            k = scr.getch()
            if k in (curses.KEY_UP, ord('k')):
                cur -= 1; fresh = True
            elif k in (curses.KEY_DOWN, ord('j')):
                cur += 1; fresh = True
            elif k == curses.KEY_PPAGE:
                cur -= rows; fresh = True
            elif k == curses.KEY_NPAGE:
                cur += rows; fresh = True
            elif 48 <= k <= 57:
                order[cur] = (order[cur] if not fresh else '') + chr(k)
                order[cur] = order[cur][-3:]
                fresh = False
            elif k in (curses.KEY_BACKSPACE, 127, 8):
                order[cur] = order[cur][:-1]
            elif k == ord(' '):
                order[cur] = '' if order[cur] else str(1 + max([int(o) for o in order if o] + [0]))
                fresh = True
            elif k in (ord('x'), 9):
                excl[cur] = not excl[cur]
                if not order[cur]:
                    order[cur] = str(1 + max([int(o) for o in order if o] + [0]))
            elif k == ord('a'):
                order = [str(i + 1) for i in range(n)]
            elif k == ord('n'):
                order = [''] * n
            elif k in (10, 13, curses.KEY_ENTER):
                if any(order):
                    return finish(items, order, excl)
            elif k in (ord('q'), 27):
                return None

    return curses.wrapper(run)


def menu_text(items):
    for i, (vid, spec) in enumerate(items, 1):
        print(f'{i:3}. {vid}  ({spec})')
    print('Type the numbers in the order to render. Add x to make one exclusive (runs alone),')
    print('e.g. "5 2x 1" = 5, then 2 on its own, then 1. "all" = everything in listed order.')
    ans = input('> ').strip().lower()
    if not ans:
        return None
    if ans == 'all':
        return [(v, s, False) for v, s in items]
    out = []
    for part in re.split(r'[,\s]+', ans):
        m = re.fullmatch(r'(\d+)(x?)', part)
        if m and 1 <= int(m.group(1)) <= len(items):
            v, sp = items[int(m.group(1)) - 1]
            out.append((v, sp, bool(m.group(2))))
    return out


def choose(items, select_all):
    if select_all:
        return [(v, s, False) for v, s in items]
    if sys.stdin.isatty() and sys.stdout.isatty():
        try:
            return menu_curses(items)
        except Exception as e:  # curses unavailable or terminal too odd
            print(f'(curses menu failed: {e}; using text menu)')
    return menu_text(items)


# ---------------------------------------------------------------- running
class State:
    def __init__(self, vid, spec, exclusive=False):
        self.vid, self.spec, self.exclusive = vid, spec, exclusive
        self.status = 'queued'     # queued / rendering / succeeded / crashed / retry-queued
        self.crashes = 0
        self.runs = 0
        self.last_rc = None
        self.last_secs = None


def run_render(st, extra):
    """Run one render attempt, streaming prefixed output. Returns the exit code."""
    cmd = ['uv', 'run', 'python', '-m', 'explainer', 'render', str(st.spec)] + extra
    env = dict(os.environ, PYTHONUNBUFFERED='1')
    prefix = f'[{st.vid}] '
    say(f'{prefix}--- attempt {st.runs}: {" ".join(cmd)}')
    t0 = time.time()
    try:
        p = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             stdin=subprocess.DEVNULL, start_new_session=True)
    except OSError as e:
        say(f'{prefix}could not start: {e}')
        return 127
    with procs_lock:
        procs[st.vid] = p
    buf = b''
    while True:
        chunk = os.read(p.stdout.fileno(), 4096)
        if not chunk:
            break
        buf += chunk
        # split on \n and \r so progress bars show as separate lines
        parts = re.split(rb'[\r\n]+', buf)
        buf = parts.pop()
        for line in parts:
            if line.strip():
                say(prefix + line.decode('utf-8', 'replace').rstrip())
    if buf.strip():
        say(prefix + buf.decode('utf-8', 'replace').rstrip())
    rc = p.wait()
    with procs_lock:
        procs.pop(st.vid, None)
    st.last_secs = time.time() - t0
    return rc


def attempt(st, extra):
    st.runs += 1
    st.status = 'rendering'
    rc = run_render(st, extra)
    st.last_rc = rc
    if stopping.is_set():
        st.status = 'interrupted'
    elif rc == 0:
        st.status = 'succeeded'
    else:
        st.crashes += 1
        st.status = 'crashed'
        say(f'[{st.vid}] CRASHED (exit code {rc}, crash #{st.crashes})')
    return st


def report(states, title):
    with print_lock:
        w = max(len(s.vid) for s in states)
        print(f'\n===== STATUS REPORT: {title}  ({time.strftime("%H:%M:%S")}) =====')
        for s in states:
            if s.status == 'succeeded':
                note = f'succeeded' + (f' (after {s.crashes} crash{"es" if s.crashes != 1 else ""})' if s.crashes else '')
            elif s.status in ('crashed', 'retry-queued'):
                note = f'crashed x{s.crashes}, waiting in retry queue'
            elif s.status == 'rendering':
                note = 'rendering now' + (f' (crashed x{s.crashes} before)' if s.crashes else '')
            elif s.status == 'interrupted':
                note = 'interrupted'
            else:
                note = 'queued'
            t = f'  last run {s.last_secs / 60:.1f} min' if s.last_secs else ''
            print(f'  {s.vid:<{w}}  {note}{t}')
        n = lambda k: sum(s.status == k for s in states)
        print(f'  -- {n("succeeded")} succeeded, {n("rendering")} rendering, '
              f'{n("queued")} queued, {n("crashed") + n("retry-queued")} in retry queue\n', flush=True)


def kill_all():
    with procs_lock:
        for p in list(procs.values()):
            try:
                os.killpg(p.pid, signal.SIGTERM)
            except (ProcessLookupError, PermissionError):
                pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workers', type=int, default=4, help='parallel renders in the main pass (default 4)')
    ap.add_argument('--force', action='store_true', help='pass --force to render')
    ap.add_argument('--burn-subs', action='store_true', help='pass --burn-subs to render')
    ap.add_argument('--all', action='store_true', help='skip the menu and render every video')
    a = ap.parse_args()
    extra = (['--force'] if a.force else []) + (['--burn-subs'] if a.burn_subs else [])

    items = discover()
    if not items:
        sys.exit('no video specs found under videos/')
    chosen = choose(items, a.all)
    if not chosen:
        sys.exit('nothing selected')

    states = [State(v, s, x) for v, s, x in chosen]
    main_q = deque(states)
    retry_q = deque()
    say(f'Rendering {len(states)} video(s), {a.workers} at a time. Ctrl-C to stop.')

    try:
        # ---- pass 1: parallel
        with ThreadPoolExecutor(max_workers=a.workers) as ex:
            running = {}
            # strict order: the head of the queue is never overtaken. An exclusive video waits for
            # everything running to finish and runs alone; nothing starts while it runs.
            while main_q or running:
                while main_q and len(running) < a.workers:
                    head = main_q[0]
                    if head.exclusive and running:
                        break
                    if any(r.exclusive for r in running.values()):
                        break
                    st = main_q.popleft()
                    running[ex.submit(attempt, st, extra)] = st
                done, _ = wait(running, return_when=FIRST_COMPLETED)
                for f in done:
                    st = running.pop(f)
                    f.result()
                    if st.status == 'crashed':
                        st.status = 'retry-queued'
                        retry_q.append(st)
                    report(states, f'{st.vid} finished ({st.status})')

        # ---- pass 2: one at a time, repeat until stopped
        if retry_q:
            say(f'Main pass done. {len(retry_q)} crashed video(s) will now be retried one at a time, '
                f'repeating until you press Ctrl-C.')
        while retry_q:
            st = retry_q.popleft()
            attempt(st, extra)
            if st.status == 'crashed':
                st.status = 'retry-queued'
                retry_q.append(st)
            report(states, f'{st.vid} finished ({st.status})')
        say('All selected videos rendered.')
    except KeyboardInterrupt:
        stopping.set()
        say('\nStopping: terminating running renders...')
        kill_all()
        time.sleep(1)
        report(states, 'stopped by user')
        sys.exit(130)


if __name__ == '__main__':
    main()
