"""The render store: $OVERHEAR_HOME/render-store/

  <sceneId>/{audio.mp3, spans.json, timing.json, report.json, meta.json}     what the publisher ingests
  cache/tts/<key>.flac         one file per unique (model, lora, voice, refVersion, language, text)
  cache/el/<key>.mp3           ElevenLabs fallback sentences
  cache/ruaccent.json
  state.json                   failures / skips / last run (done-ness is read from meta.json, never stored twice)
  runs.jsonl                   one line per slice: scenes, audio seconds, wall seconds, rtf

Scene directories are written to a temp name and renamed, so a reader never sees half a render.
"""
import contextlib
import ctypes
import errno
import fcntl
import hashlib
import json
import os
import shutil
import time
from pathlib import Path

import config

_RENAME_EXCHANGE = 2


def exchange_dirs(a, b) -> bool:
    """Atomically swap two directories (renameat2 RENAME_EXCHANGE): both paths exist at every instant. False when the kernel/filesystem
    cannot (the caller falls back to two renames)."""
    try:
        libc = ctypes.CDLL(None, use_errno=True)
        fn = libc.renameat2
    except (OSError, AttributeError):
        return False
    r = fn(-100, os.fsencode(str(a)), -100, os.fsencode(str(b)), _RENAME_EXCHANGE)
    if r == 0:
        return True
    e = ctypes.get_errno()
    if e in (errno.EINVAL, errno.ENOSYS, errno.ENOTSUP, errno.EPERM):
        return False
    raise OSError(e, os.strerror(e), str(a))


class LockTimeout(Exception):
    pass


@contextlib.contextmanager
def flock_ctx(path, timeout=None, shared=False):
    """flock(2) on `path` (created if missing) held for the with-block. timeout None = wait for ever, 0 = try once. Raises LockTimeout.
    Plain flock(2), so it is compatible with `flock(1)` (exclusive by default) and `flock -s` in the publisher's wrapper."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    f = open(path, "a")
    mode = fcntl.LOCK_SH if shared else fcntl.LOCK_EX
    t0 = time.time()
    try:
        while True:
            try:
                fcntl.flock(f, mode | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if timeout is not None and time.time() - t0 >= timeout:
                    raise LockTimeout(f"{path} is held by another process")
                time.sleep(min(0.5, max(0.01, (timeout or 1) / 20)))
        yield f
    finally:
        f.close()          # closing the descriptor drops the lock


SCENE_FILES = ("audio.mp3", "spans.json", "timing.json", "report.json", "meta.json")


class Store:
    def __init__(self, root=None):
        self.root = Path(root or config.STORE)
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / "cache" / "tts").mkdir(parents=True, exist_ok=True)
        (self.root / "cache" / "el").mkdir(parents=True, exist_ok=True)

    def scene_dir(self, sid) -> Path:
        return self.root / sid

    def meta(self, sid):
        p = self.scene_dir(sid) / "meta.json"
        try:
            return json.loads(p.read_text("utf-8"))
        except Exception:
            return None

    def is_done(self, sid, render_key) -> bool:
        m = self.meta(sid)
        return bool(m) and m.get("renderKey") == render_key and all((self.scene_dir(sid) / f).exists() for f in SCENE_FILES)

    def tts_path(self, key) -> Path:
        return self.root / "cache" / "tts" / f"{key}.flac"

    def el_path(self, key) -> Path:
        return self.root / "cache" / "el" / f"{key}.mp3"

    def commit_scene(self, sid, files: dict):
        """files: {name: bytes|Path}. Atomic replace of the scene directory."""
        final = self.scene_dir(sid)
        tmp = self.root / f".{sid}.tmp.{os.getpid()}"
        shutil.rmtree(tmp, ignore_errors=True)
        tmp.mkdir(parents=True)
        for name, data in files.items():
            if isinstance(data, Path):
                shutil.copyfile(data, tmp / name)
            else:
                (tmp / name).write_bytes(data)
        if final.exists():
            if exchange_dirs(tmp, final):          # one atomic step: <sid> is never missing (the publisher's symlinks never dangle)
                shutil.rmtree(tmp, ignore_errors=True)       # tmp now holds the old scene
                return
            old = self.root / f".{sid}.old.{os.getpid()}"
            final.rename(old)
            tmp.rename(final)
            shutil.rmtree(old, ignore_errors=True)
        else:
            tmp.rename(final)

    # ---- state.json
    @property
    def state_path(self):
        return self.root / "state.json"

    def state(self):
        try:
            return json.loads(self.state_path.read_text("utf-8"))
        except Exception:
            return {"failed": {}, "skipped": {}, "contentCommit": None, "lastRun": None}

    def save_state(self, st):
        tmp = self.state_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(st, indent=1, sort_keys=True, ensure_ascii=False), "utf-8")
        tmp.replace(self.state_path)

    def log_run(self, rec):
        with open(self.root / "runs.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    def runs(self):
        p = self.root / "runs.jsonl"
        if not p.exists():
            return []
        out = []
        for line in p.read_text("utf-8").splitlines():
            try:
                out.append(json.loads(line))
            except Exception:
                pass
        return out


def sha256_file(p) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()
