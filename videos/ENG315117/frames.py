"""Freeze frames and short clips for the ENG315117 videos, cut from the films with ffmpeg.

The films are NOT in the repository.  Put the three files in ~/Downloads (or set ENG_FILM_DIR) and run

    uv run python videos/ENG315117/frames.py

Frames land in sources/ENG315117/cache/frames/ (git-ignored).  Everything here is used for study and criticism
(short stills and clips, each shown with commentary), as the operator authorised; see the handover notes.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'sources', 'ENG315117', 'cache', 'frames')
FILM_DIR = os.environ.get('ENG_FILM_DIR', os.path.expanduser('~/Downloads'))
FILMS = {
    'nx': 'North_by_Northwest_1959_1080p_HEVC.mkv',
    'rp': 'The_Talented_Mr_Ripley_1999_1080p_HEVC.mkv',
    'sh': 'The Shawshank Redemption (1994) - 1080p AVC.mkv',
}
# name -> (film, timestamp).  Each is a single freeze frame.
STILLS = {
    'nx_title': ('nx', '00:00:40'), 'nx_mistaken': ('nx', '00:10:57'), 'nx_drive': ('nx', '00:17:30'),
    'nx_dining': ('nx', '00:48:40'), 'nx_field': ('nx', '01:10:50'), 'nx_plane': ('nx', '01:12:30'),
    'nx_corn': ('nx', '01:13:40'), 'nx_match': ('nx', '02:05:30'), 'nx_climb': ('nx', '02:15:00'),
    'nx_tunnel': ('nx', '02:16:15'), 'nx_taxi': ('nx', '00:03:30'), 'nx_un': ('nx', '00:37:10'),
    'nx_auction': ('nx', '01:27:55'), 'nx_wives': ('nx', '02:11:45'),
    'rp_title': ('rp', '00:00:50'), 'rp_tom': ('rp', '00:09:30'), 'rp_chet': ('rp', '00:19:00'),
    'rp_dickie': ('rp', '00:30:00'), 'rp_beach': ('rp', '00:52:40'), 'rp_blood': ('rp', '00:57:40'),
    'rp_type': ('rp', '01:00:00'), 'rp_fake': ('rp', '02:11:15'), 'rp_cabin': ('rp', '02:12:40'),
    'rp_dark': ('rp', '02:13:20'), 'rp_herbert': ('rp', '00:17:05'), 'rp_sun': ('rp', '00:39:50'),
    'rp_basement': ('rp', '01:45:50'), 'rp_boat': ('rp', '00:55:50'),
    'sh_norton': ('sh', '00:13:20'), 'sh_cinema': ('sh', '00:42:08'), 'sh_sampler': ('sh', '00:51:30'),
    'sh_brooks': ('sh', '01:00:30'), 'sh_mozart': ('sh', '01:07:50'), 'sh_hope': ('sh', '01:12:40'),
    'sh_wall': ('sh', '01:46:00'), 'sh_poster': ('sh', '01:53:40'), 'sh_letter': ('sh', '02:15:40'),
    'sh_beach': ('sh', '02:17:50'), 'sh_ocean': ('sh', '02:18:20'), 'sh_trial': ('sh', '00:04:30'),
    'sh_rock': ('sh', '00:25:50'), 'sh_tunnel': ('sh', '01:59:20'), 'sh_music': ('sh', '01:11:40'),
}
# name -> (film, start timestamp, seconds).  Short clips are stored as numbered frames at CLIP_FPS and looped in the video.
CLIPS = {
    'nx_plane_clip': ('nx', '01:12:24', 2.4),
    'sh_beach_clip': ('sh', '02:17:46', 2.4),
}
CLIP_FPS = 10


def _ff(args):
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y'] + args, check=True)


def main(only=None):
    os.makedirs(OUT, exist_ok=True)
    for name, (f, t) in STILLS.items():
        dest = os.path.join(OUT, name + '.jpg')
        if only and name not in only or os.path.exists(dest):
            continue
        _ff(['-ss', t, '-i', os.path.join(FILM_DIR, FILMS[f]), '-frames:v', '1', '-vf', 'scale=1280:-1', '-q:v', '3', dest])
        print('still', name)
    for name, (f, t, secs) in CLIPS.items():
        if only and name not in only or os.path.exists(os.path.join(OUT, f'{name}_001.jpg')):
            continue
        _ff(['-ss', t, '-i', os.path.join(FILM_DIR, FILMS[f]), '-t', str(secs), '-vf', f'fps={CLIP_FPS},scale=960:-1', '-q:v', '4',
             os.path.join(OUT, f'{name}_%03d.jpg')])
        print('clip', name)


if __name__ == '__main__':
    main(sys.argv[1:] or None)
