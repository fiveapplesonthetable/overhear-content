"""RuAccent stress for sentences the notes do not fully cover. Runs in the separate RuAccent venv (a subprocess)
and caches results on disk, so the pipeline process never imports ruaccent."""
import json
import subprocess
import sys
from pathlib import Path

import config

_HERE = Path(__file__).resolve().parent


class RuAccent:
    def __init__(self, python, cache_file):
        self.python, self.cache_file = python, Path(cache_file)
        self.cache = json.loads(self.cache_file.read_text("utf-8")) if self.cache_file.exists() else {}

    def __call__(self, sentences):
        todo = [s for s in dict.fromkeys(sentences) if s not in self.cache]
        if todo:
            r = subprocess.run([self.python, "-I", str(_HERE / "ruaccent_cli.py")], input=json.dumps(todo, ensure_ascii=False),
                               capture_output=True, text=True, cwd="/tmp")
            if r.returncode != 0:
                sys.stderr.write("ruaccent failed: " + r.stderr[-400:] + "\n")
                return list(sentences)
            for s, m in zip(todo, json.loads(r.stdout)):
                self.cache[s] = m
            self.cache_file.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.cache_file.with_suffix(".tmp")
            tmp.write_text(json.dumps(self.cache, ensure_ascii=False), "utf-8")
            tmp.replace(self.cache_file)
        return [self.cache[s] for s in sentences]
