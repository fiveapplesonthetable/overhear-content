#!/usr/bin/env python3
"""Make every source.lines[].cue point inside its scene (FEEDBACK item 6). Python 3 stdlib only. Idempotent.

For each script whose source.lines cite a cue that starts outside [scene.start - 2 s, scene.end + 2 s]: the citation is
re-tied to a cue of the scene only if that cue really contains a run of >= 2 consecutive words of the story line (the
fragment is then that run, copied from the cue); otherwise the citation is dropped. No cue is invented and the story text
is never touched. The cue numbers, fragments and times are checked against the subtitle file named in source.file.

  python3 -I tools/fix_source_cues.py [out_dir]       # default: out
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def ts(s):
    m = re.match(r"(\d+):(\d\d):(\d\d)[,.](\d+)", s.strip())
    return int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3]) + int(m[4].ljust(3, "0")[:3]) / 1000


def squash(s): return re.sub(r"[\W_]+", " ", s.lower().replace("ё", "е")).strip()


_SRT = {}


def parse_srt(path):
    if path not in _SRT:
        out = _SRT[path] = {}
        for blk in re.split(r"\n\s*\n", path.read_text(encoding="utf-8").replace("\r", "").strip()):
            ln = blk.split("\n")
            m = re.match(r"(\S+) --> (\S+)", ln[1]) if len(ln) >= 3 else None
            if m and ln[0].strip().isdigit():
                out[int(ln[0])] = (ts(m[1]), ts(m[2]), " ".join(x.strip() for x in ln[2:]))
    return _SRT[path]


def story_lines(segs):
    first = next(i for i, s in enumerate(segs) if s["v"] != "narrator")
    j = first
    while j < len(segs) and segs[j]["v"] != "narrator": j += 1
    return [s["t"] for s in segs[first:j]]


def best_run(story, cue_text):
    """Longest run (>= 2 words) of consecutive words shared by the story line and the cue; the run as written in the cue."""
    sw = squash(story).split()
    cw = cue_text.split()
    cs = [squash(w) for w in cw]
    best = None
    for i in range(len(cw)):
        for j in range(len(sw)):
            n = 0
            while i + n < len(cw) and j + n < len(sw) and cs[i + n] and cs[i + n] == sw[j + n]: n += 1
            if n >= 2 and (best is None or n > best[0]): best = (n, " ".join(cw[i:i + n]).strip(",.!?;:—-… "))
    return best


def main(out):
    fixed = retied = dropped = 0
    for sp in sorted(Path(out).glob("*/*/scenes.json")):
        scenes = json.loads(sp.read_text(encoding="utf-8"))["scenes"]
        for k, s in enumerate(scenes, 1):
            p = sp.parent / f"scene-{k:02d}.json"
            if s.get("merge") is not None or not p.is_file(): continue
            d = json.loads(p.read_text(encoding="utf-8"))
            src = d.get("source")
            if not isinstance(src, dict): continue
            f = ROOT / src["file"]
            if not f.is_file(): continue
            cue = parse_srt(f)
            a, b = ts(s["start"]), ts(s["end"])
            inside = {n for n, c in cue.items() if a - 2 <= c[0] <= b + 2}
            story = story_lines(d["segments"])
            new, seen, changed = [], set(), False
            for ln in src["lines"]:
                if ln["cue"] not in cue or ln["cue"] in inside:
                    new.append(ln); continue
                changed = True
                best = None
                for n in sorted(inside):
                    r = best_run(story[ln["line"]], cue[n][2]) if ln["line"] < len(story) else None
                    if r and (best is None or r[0] > best[0]): best = (r[0], n, r[1])
                if best and squash(best[2]) in squash(cue[best[1]][2]):
                    key = (ln["line"], best[1], best[2])
                    if key not in seen:
                        seen.add(key); new.append({"line": ln["line"], "cue": best[1], "fragment": best[2]})
                    retied += 1
                else: dropped += 1
            if changed:
                new.sort(key=lambda x: (x["line"], x["cue"]))
                src["lines"] = new
                ind = 1 if p.read_text(encoding="utf-8").startswith('{\n "') else 2
                p.write_text(json.dumps(d, ensure_ascii=False, indent=ind) + "\n", encoding="utf-8")
                fixed += 1
    print(f"{fixed} scripts changed; {retied} citations re-tied inside the scene, {dropped} dropped")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "out")
