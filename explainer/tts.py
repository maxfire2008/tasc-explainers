"""Narration synthesis.  The engine and voice come from style.VOICE.
Audio is cached by a hash of (voice settings + prepared text), so editing one step or
changing the voice only regenerates what changed."""
import hashlib
import json
import os
import re

from . import style as S

_engine = None


def prepare(text):
    """Apply style.PRONUNCIATIONS and tidy whitespace."""
    for pat, rep in S.PRONUNCIATIONS:
        text = re.sub(pat, rep, text)
    return re.sub(r'\s+', ' ', text).strip()


def key(text):
    blob = json.dumps(S.VOICE, sort_keys=True) + '\n' + prepare(text)
    return hashlib.sha1(blob.encode()).hexdigest()[:16]


def _kokoro(root):
    global _engine
    if _engine is None:
        from kokoro_onnx import Kokoro
        m = os.path.join(root, S.VOICE['model']); v = os.path.join(root, S.VOICE['voices'])
        if not (os.path.exists(m) and os.path.exists(v)):
            raise SystemExit('Kokoro model files missing: run  bash scripts/get_models.sh')
        _engine = Kokoro(m, v)
    return _engine


def synth(text, out_dir, root):
    """Return path to a wav for `text`, synthesising it if not cached."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, key(text) + '.wav')
    if os.path.exists(path):
        return path
    import soundfile as sf
    eng = S.VOICE['engine']
    if eng == 'kokoro':
        samples, sr = _kokoro(root).create(prepare(text), voice=S.VOICE['voice'], speed=S.VOICE['speed'],
                                           lang=S.VOICE['lang'])
    else:
        # To add an engine: produce (float32 mono samples, sample_rate) here and keep the cache logic.
        raise NotImplementedError(f'TTS engine {eng!r} not implemented in explainer/tts.py')
    tmp = path + '.tmp.wav'
    sf.write(tmp, samples, sr)
    os.replace(tmp, path)
    return path
