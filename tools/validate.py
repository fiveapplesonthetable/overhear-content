#!/usr/bin/env python3
"""Validator for Overhear content. Python 3 stdlib only.

  python3 tools/validate.py out/kukhnya/s01e01            # one episode dir
  python3 tools/validate.py out                           # every episode dir under out/
  python3 tools/validate.py --script FILE.json            # one scene script (examples/*/scene.json)
  options: --require-notes  every target-language line must be annotated (final check)
           --strict         warnings count as errors
Exit 0 = clean, 1 = errors. Warnings (e.g. subtitle gaps) are printed but pass unless --strict.
Checks: spec/*.md describes each rule.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHOWS = {"kukhnya": "ru", "domashniy-arest": "ru", "dix-pour-cent": "fr"}
VOICES = {"ru": {"narrator": "sky", "anya": "alisa", "_other": {"anja", "angelina"}},
          "fr": {"narrator": "sky", "lea": "lucie", "_other": {"emilie", "theo", "marcel"}}}
PAIR = {"ru": "ru-en", "fr": "fr-en"}
CYR = re.compile(r"[Ѐ-ӿ]")
LAT = re.compile(r"[A-Za-z]")
ACUTE = "́"
POS = {"noun", "verb", "adj", "adv", "pron", "prep", "conj", "part", "num", "interj", "det", "phrase", "name"}
MERGE = {None, "prev", "next"}
GAP_WARN = 120.0          # seconds of uncovered subtitle time worth a warning
ENG = set("the a an is are was to of and in it you i that this we he she they for on with as at be have not do".split())


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, where, msg): self.errors.append(f"{where}: {msg}")
    def warn(self, where, msg): self.warnings.append(f"{where}: {msg}")


# ---------------------------------------------------------------- subtitles
def ts(s):
    m = re.match(r"(\d+):(\d\d):(\d\d)[,.](\d+)", s.strip())
    if not m: raise ValueError(s)
    return int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3]) + int(m[4].ljust(3, "0")[:3]) / 1000


def parse_srt(path):
    """-> {cue_no: (start_s, end_s, text)}"""
    out = {}
    t = Path(path).read_text(encoding="utf-8").replace("\r", "")
    for blk in re.split(r"\n\s*\n", t.strip()):
        ln = blk.split("\n")
        if len(ln) >= 3:
            m = re.match(r"(\S+) --> (\S+)", ln[1])
            if m and ln[0].strip().isdigit():
                out[int(ln[0])] = (ts(m[1]), ts(m[2]), " ".join(x.strip() for x in ln[2:]))
    return out


def squash(s): return re.sub(r"[\W_]+", " ", s.lower().replace("ё", "е")).strip()
def fmt(sec): return f"{int(sec // 3600):02d}:{int(sec % 3600 // 60):02d}:{sec % 60:06.3f}".replace(".", ",")


# ---------------------------------------------------------------- script
def target_ok(lang, text, where, rep):
    if lang == "ru":
        if not CYR.search(text): rep.err(where, f"Russian line has no Cyrillic: {text[:50]!r}")
        if LAT.search(text): rep.err(where, f"Latin letters in Russian line: {text[:50]!r}")
    else:
        if CYR.search(text): rep.err(where, f"Cyrillic in French line: {text[:50]!r}")
        if re.search(r"\s[?!:;]", text): rep.err(where, f"space before ?!:; (write 'là?'): {text[:50]!r}")
        if "’" in text: rep.err(where, "typographic apostrophe, use '")
        if "«" in text or "»" in text: rep.err(where, "guillemets in a spoken line")


def check_script(path, lang, rep, expect_id=None):
    w = str(path)
    try: d = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e: return rep.err(w, f"not valid JSON: {e}")
    for k in ("id", "pair", "title", "level", "voices", "labels", "segments", "source"):
        if k not in d: rep.err(w, f"missing field {k!r}")
    if "segments" not in d or "voices" not in d: return None
    if expect_id and d.get("id") != expect_id: rep.err(w, f"id should be {expect_id!r}, is {d.get('id')!r}")
    if d.get("pair") != PAIR[lang]: rep.err(w, f"pair should be {PAIR[lang]!r}")
    v, segs = d["voices"], d["segments"]
    want = VOICES[lang]
    if v.get("narrator") != want["narrator"]: rep.err(w, "voices.narrator must be 'sky'")
    roles = [r for r in v if r != "narrator"]
    prot = [r for r in want if r not in ("narrator", "_other")][0]
    if prot not in v: rep.err(w, f"voices must include the protagonist role {prot!r}")
    for r in roles:
        if r == prot and v[r] != want[prot]: rep.err(w, f"role {prot!r} must use voice {want[prot]!r}")
        if r != prot and v[r] not in want["_other"]: rep.err(w, f"voice {v[r]!r} for role {r!r} must be one of {sorted(want['_other'])}")
    if len(set(v.values())) != len(v): rep.err(w, "each role needs its own voice")
    if len(roles) > 3: rep.err(w, "at most three speaking roles besides the narrator")
    for r in roles:
        if r not in d.get("labels", {}) and r != prot: rep.err(w, f"labels missing display name for role {r!r}")
    if not isinstance(segs, list) or len(segs) < 20: return rep.err(w, "segments missing or too short (a scene has ~60-80)")
    for i, s in enumerate(segs):
        sw = f"{w} segment {i}"
        if not isinstance(s, dict) or not {"v", "t", "gap"} <= set(s): rep.err(sw, "needs v, t, gap"); continue
        if s["v"] not in v: rep.err(sw, f"role {s['v']!r} not in voices")
        if not isinstance(s["t"], str) or not s["t"].strip(): rep.err(sw, "empty text"); continue
        if not isinstance(s["gap"], (int, float)) or not 0 <= s["gap"] <= 3: rep.err(sw, "gap must be 0..3 seconds")
        if ACUTE in s["t"]: rep.err(sw, "stress mark in text (stress belongs only in stress fields)")
        if s["v"] == "narrator":
            if CYR.search(s["t"]): rep.err(sw, f"narrator must be English only: {s['t'][:50]!r}")
            elif len(s["t"].split()) > 6 and not (ENG & set(re.findall(r"[a-z]+", s["t"].lower()))):
                rep.err(sw, f"narrator line does not look English: {s['t'][:50]!r}")
            if lang == "fr" and re.search(r"[àâçéèêëîïôûùœ]", s["t"].lower()) and not re.search(r"Léa|Hervé|Élodie", s["t"]):
                rep.warn(sw, f"narrator line has French letters (quoting French?): {s['t'][:50]!r}")
        else:
            target_ok(lang, s["t"], sw, rep)
    if segs[0]["v"] != "narrator": rep.err(w, "first segment must be the narrator intro")
    if segs[-1]["v"] == "narrator": rep.err(w, "last segment must be one short target-language line")
    # 5-part shape: intro, story, walk-through, story again, outro + closing line
    first = next((i for i, s in enumerate(segs) if s["v"] != "narrator"), None)
    if first is not None:
        j = first
        while j < len(segs) and segs[j]["v"] != "narrator": j += 1
        story = [s["t"] for s in segs[first:j]]
        if j - first < 8: rep.warn(w, f"story has only {j - first} lines (aim for 12-18)")
        k = len(segs) - 1
        while k > 0 and segs[k]["v"] != "narrator": k -= 1       # closing line sits after the outro
        tail = [s["t"] for s in segs[:k] if s["v"] != "narrator"][-len(story):]
        if tail != story: rep.warn(w, "the whole story is not repeated unchanged before the outro (part 4)")
        if sum(1 for s in segs[j:k] if s["v"] == "narrator") < 3: rep.warn(w, "walk-through (part 3) looks missing")
    src = d.get("source", {})
    sf = ROOT / src.get("file", "")
    if not src.get("file") or not sf.is_file(): rep.err(w, f"source.file missing or not found: {src.get('file')}")
    elif not src.get("lines"): rep.warn(w, "source.lines empty: no story line is tied to a subtitle cue")
    else:
        cue = parse_srt(sf)
        for ln in src["lines"]:
            c = cue.get(ln.get("cue"))
            if c is None: rep.err(w, f"source cue {ln.get('cue')} not in {src['file']}")
            elif squash(ln.get("fragment", "")) not in squash(c[2]):
                rep.err(w, f"fragment {ln.get('fragment')!r} not in cue {ln['cue']}: {c[2][:60]!r}")
    return d


# ---------------------------------------------------------------- notes
def table_ok(t, where, rep):
    if not isinstance(t, dict) or not {"title", "columns", "rows"} <= set(t): return rep.err(where, "table needs title, columns, rows")
    for r in t["rows"]:
        if not isinstance(r, dict) or len(r.get("cells", [])) != len(t["columns"]):
            rep.err(where, f"row {r!r:.60} does not have {len(t['columns'])} cells")


def no_acute_outside_stress(o, where, rep, key=""):
    if isinstance(o, str):
        if ACUTE in o and key != "stress": rep.err(where, f"U+0301 outside a stress field (key {key!r})")
    elif isinstance(o, dict):
        for k, v in o.items(): no_acute_outside_stress(v, where, rep, k)
    elif isinstance(o, list):
        for v in o: no_acute_outside_stress(v, where, rep, key)


def check_stress(lang, word, st, where, rep):
    if st is None: return
    if lang == "ru":
        if st.replace(ACUTE, "") != word: rep.err(where, f"stress {st!r} must be the word {word!r} plus U+0301")
    else:
        if re.search(r"[\s/\[\]]", st) or re.search(r"[A-Z]", st) or ACUTE in st: rep.err(where, f"fr stress must be bare IPA: {st!r}")
        if re.search(r"[éèêàùçôîï]", st): rep.err(where, f"fr stress holds spelling letters, not IPA: {st!r}")


def check_notes(path, script, lang, require, rep):
    w = str(path)
    try: n = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e: return rep.err(w, f"not valid JSON: {e}")
    no_acute_outside_stress(n, w, rep)
    segs, lex = script["segments"], n.get("lexicon", {})
    if not isinstance(n.get("lines"), list): return rep.err(w, "needs 'lines' list")
    done = set()
    for e in n["lines"]:
        i = e.get("seg")
        if not isinstance(i, int) or not 0 <= i < len(segs): rep.err(w, f"bad seg index {i!r}"); continue
        done.add(i); lw = f"{w} seg {i}"
        text = segs[i]["t"]
        if not str(e.get("trans", "")).strip() and segs[i]["v"] != "narrator": rep.err(lw, "missing trans (English translation)")
        pos = 0
        for wd in e.get("words", []):
            t = wd.get("t", "")
            at = text.find(t, pos)
            if not t or at < 0: rep.err(lw, f"word {t!r} not found in order in the line"); continue
            pos = at + len(t)
            for f in ("lemma", "pos", "gloss"):
                if wd.get(f) in (None, ""): rep.err(lw, f"word {t!r} missing {f}")
            if wd.get("pos") and wd["pos"] not in POS: rep.err(lw, f"word {t!r}: pos {wd['pos']!r} not in {sorted(POS)}")
            if wd.get("lemma") and wd["lemma"].lower() not in lex and wd.get("pos") != "name":
                rep.err(lw, f"lemma {wd['lemma']!r} has no entry in lexicon")
            if lang == "ru" and wd.get("stress") and len(re.findall("[аеёиоуыэюя]", wd["stress"].lower())) > 1 and ACUTE not in wd["stress"] and "ё" not in wd["stress"]:
                rep.err(lw, f"stress {wd['stress']!r} lacks the U+0301 mark")
    for lemma, L in lex.items():
        lw = f"{w} lexicon[{lemma}]"
        for f in ("lemma", "pos", "gloss", "meanings"):
            if not L.get(f): rep.err(lw, f"missing {f}")
        if L.get("lemma") != lemma: rep.err(lw, "key must equal lemma")
        check_stress(lang, lemma, L.get("stress"), lw, rep)
        for t in [L.get("forms")] * bool(L.get("forms")) + list(L.get("moreForms") or []): table_ok(t, lw, rep)
        if L.get("pos") in ("noun", "adj", "verb") and not L.get("forms") and lang == "ru":
            rep.err(lw, "ru noun/adj/verb needs a forms table")
        for m in L.get("meanings", []):
            if not m.get("en"): rep.err(lw, "meaning needs 'en'")
    if require:
        for i, s in enumerate(segs):
            if s["v"] != "narrator" and i not in done: rep.err(w, f"target line {i} not annotated: {s['t'][:40]!r}")


# ---------------------------------------------------------------- episode
def check_scenes(epdir, show, rep):
    w = str(epdir / "scenes.json")
    lang = SHOWS[show]
    m = re.fullmatch(r"s(\d\d)e(\d\d)", epdir.name)
    if not m: return rep.err(str(epdir), "episode dir must be named sNNeNN")
    sn, en = m[1], m[2]
    try: sc = json.loads((epdir / "scenes.json").read_text(encoding="utf-8"))
    except Exception as e: return rep.err(w, f"missing or invalid scenes.json: {e}")
    if sc.get("show") != show or sc.get("season") != int(sn) or sc.get("episode") != int(en):
        rep.err(w, "show/season/episode do not match the folder")
    scenes = sc.get("scenes")
    if not scenes: return rep.err(w, "no scenes")
    srt = ROOT / "sources" / show / f"s{sn}" / f"e{en}.{lang}.dual.srt"
    cue = parse_srt(srt) if srt.is_file() else {}
    if not cue: rep.err(w, f"source subtitles missing: {srt.relative_to(ROOT)}")
    prev_end = None
    for k, s in enumerate(scenes, 1):
        sw = f"{w} scene {k}"
        for f in ("scene", "start", "end", "title", "summary", "characters", "location", "merge"):
            if f not in s: rep.err(sw, f"missing {f}")
        if s.get("scene") != k: rep.err(sw, f"scene numbers must run 1..N without gaps (found {s.get('scene')})")
        if s.get("merge") not in MERGE: rep.err(sw, "merge must be null, 'prev' or 'next'")
        if s.get("merge") == "prev" and k == 1 or s.get("merge") == "next" and k == len(scenes):
            rep.err(sw, "merge target does not exist")
        try: a, b = ts(s["start"]), ts(s["end"])
        except Exception: rep.err(sw, "start/end must be HH:MM:SS,mmm"); continue
        if b <= a: rep.err(sw, "end must be after start")
        if prev_end is not None and a < prev_end - 0.001: rep.err(sw, "overlaps the previous scene")
        prev_end = b
        s["_t"] = (a, b)
        if s.get("merge") is None:
            n = f"{k:02d}"
            sp = epdir / f"scene-{n}.json"
            if not sp.is_file(): rep.err(sw, f"missing scene-{n}.json")
            else:
                d = check_script(sp, lang, rep, expect_id=f"{show}-s{sn}e{en}-scene-{n}")
                if d is not None:
                    notes = epdir / f"scene-{n}.notes.json"
                    if notes.is_file(): check_notes(notes, d, lang, REQ[0], rep)
                    elif REQ[0]: rep.err(sw, f"missing scene-{n}.notes.json")
            if not any((epdir / f"scene-{n}.{x}").is_file() for x in ("webp", "png")):
                rep.err(sw, f"missing art scene-{n}.webp (or .png)")
    # coverage: every cue must sit inside some scene; report long uncovered stretches
    if cue:
        spans = [s["_t"] for s in scenes if "_t" in s]
        miss = [(n, c) for n, c in sorted(cue.items()) if not any(a - 0.5 <= c[0] <= b + 0.5 for a, b in spans)]
        if miss:
            rep.err(w, f"{len(miss)} subtitle cues fall outside every scene (first: cue {miss[0][0]} at {fmt(miss[0][1][0])}); scenes must cover the whole episode")
        last = max(c[1] for c in cue.values())
        if spans and spans[-1][1] < last - 1: rep.err(w, f"last scene ends {fmt(spans[-1][1])}, episode subtitles run to {fmt(last)}")
        for (a1, b1), (a2, b2) in zip(spans, spans[1:]):
            if a2 - b1 > 1: rep.warn(w, f"gap of {a2 - b1:.0f}s between scenes at {fmt(b1)}-{fmt(a2)}")
        for s in scenes:
            if "_t" in s:
                inside = sorted(c for c in cue.values() if s["_t"][0] - .5 <= c[0] <= s["_t"][1] + .5)
                for c1, c2 in zip(inside, inside[1:]):
                    if c2[0] - c1[1] > GAP_WARN: rep.warn(w, f"scene {s['scene']}: {c2[0] - c1[1]:.0f}s without subtitles at {fmt(c1[1])} (one scene?)")
    if not (epdir.parent / "characters.md").is_file(): rep.warn(str(epdir), "no characters.md next to the season folders")


REQ = [False]


def main(argv):
    REQ[0] = "--require-notes" in argv
    strict = "--strict" in argv
    args = [a for a in argv if not a.startswith("--")]
    rep = Report()
    if "--script" in argv:
        p = Path(args[0]).resolve()
        lang = "fr" if re.search(r"dix|fr-", str(p)) else "ru"
        check_script(p, lang, rep)
    else:
        base = Path(args[0] if args else "out").resolve()
        eps = [base] if re.fullmatch(r"s\d\de\d\d", base.name) else sorted(p.parent for p in base.rglob("scenes.json"))
        if not eps: rep.err(str(base), "no episode folders (with scenes.json) found")
        for ep in eps:
            show = ep.parent.name
            if show not in SHOWS: rep.err(str(ep), f"show folder must be one of {sorted(SHOWS)}"); continue
            check_scenes(ep, show, rep)
    for x in rep.warnings: print("WARN ", x)
    for x in rep.errors: print("ERROR", x)
    bad = rep.errors or (strict and rep.warnings)
    print(f"{'FAIL' if bad else 'OK'}: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
