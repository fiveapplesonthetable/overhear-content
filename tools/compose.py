#!/usr/bin/env python3
"""Turn an authoring module into a scene script (scene-NN.json) and its review sheet (scene-NN.REVIEW.md).

The structure is fixed (mirrors episodes 01-05): narrator intro, the whole story, a narrator
walk-through that replays key lines, the story again with shorter gaps, a send-off ending on one
short target-language line. The authoring module supplies the words; this script supplies the
gaps, checks the language rules, and checks every claimed source line against the subtitle file.

    python3 tools/compose.py draft.py --out out/kukhnya/s01e02/scene-01.json [--no-source-check]
    (see examples/*/authoring.py; SOURCE_FILE is relative to the repo root)

An authoring module defines:
    ID, TITLE, LEVEL, PAIR ("ru-en" | "fr-en"), LABELS, SOURCE_NAME, SOURCE_FILE,
    INTRO, STORY, OPENER, WALK, TRANSITION, OUTRO, CLOSING
  STORY    [(role, text, english, [(cue_no, "fragment of the subtitle line"), ...], note)]
  WALK     [(story_line_index, sentence_or_None, narrator_gloss)]  replay then explain
"""
import importlib.util, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHOW_FIELDS = ("SHOW", "SEASON", "EPISODE", "SCENE")   # optional module attributes copied into the JSON
SENT = re.compile(r'(?<=[.!?…])[\s]+')     # same split as render.py


def sentences(text):
    return [p.strip() for p in SENT.split(text.strip()) if p.strip()]


def load(path):
    path = Path(path)
    spec = importlib.util.spec_from_file_location("authoring_draft", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cues(path):
    t = (ROOT / path).read_text(encoding="utf-8").replace("\r", "")
    out = {}
    for blk in re.split(r"\n\s*\n", t.strip()):
        lines = blk.split("\n")
        if len(lines) < 3:
            continue
        m = re.match(r"(\d\d:\d\d:\d\d),\d+ -->", lines[1])
        if m:
            out[int(lines[0])] = (m.group(1), " ".join(l.strip() for l in lines[2:]))
    return out


def squash(s):
    return re.sub(r"[\W_]+", " ", s.lower().replace("ё", "е")).strip()


def check_language(mod, problems):
    cyr = re.compile(r"[\u0400-\u04ff]")
    for i, (role, text, *_rest) in enumerate(mod.STORY):
        if mod.PAIR == "ru-en":
            if re.search(r"[A-Za-z]", text): problems.append(f"story {i}: Latin letters in Russian text: {text}")
            if "\u0301" in text: problems.append(f"story {i}: stress mark in text")
        else:
            if cyr.search(text): problems.append(f"story {i}: Cyrillic in French text")
            if re.search(r"\s[?!:;]", text): problems.append(f"story {i}: space before ?!:; (write 'là ?' as 'là?'): {text}")
            if "\u2019" in text: problems.append(f"story {i}: typographic apostrophe, use '")
            if "«" in text or "»" in text: problems.append(f"story {i}: guillemets in spoken line")
    narrator = [mod.INTRO, mod.OPENER, mod.TRANSITION, mod.OUTRO] + [g for _, _, g in mod.WALK]
    for t in narrator:
        if cyr.search(t): problems.append(f"narrator text contains Cyrillic: {t[:60]}")
        if mod.PAIR == "fr-en" and re.search(r"\b(le|la|les|est|vous|bonjour|merci)\b", t.lower()) and "bonjour" in t.lower():
            problems.append(f"narrator seems to quote French: {t[:60]}")


def build(mod, check_source=True):
    problems = []
    check_language(mod, problems)
    story_sents = {s for _, text, *_ in mod.STORY for s in sentences(text)}
    segs = []

    def add(v, t, gap):
        segs.append({"v": v, "t": t, "gap": gap})

    add("narrator", mod.INTRO, 0.8)
    for k, (role, text, *_r) in enumerate(mod.STORY):
        add(role, text, 0.9 if k == len(mod.STORY) - 1 else 0.55)
    add("narrator", mod.OPENER, 0.4)
    for k, (idx, only, gloss) in enumerate(mod.WALK):
        role, text = mod.STORY[idx][0], mod.STORY[idx][1]
        replay = only or text
        for s in sentences(replay):
            if s not in story_sents:
                problems.append(f"walk {k}: replay sentence not in the story: {s}")
        add(role, replay, 0.55)
        last = k == len(mod.WALK) - 1
        add("narrator", gloss + (" " + mod.TRANSITION if last else ""), 0.9 if last else 0.4)
    for k, (role, text, *_r) in enumerate(mod.STORY):
        add(role, text, 0.9 if k == len(mod.STORY) - 1 else 0.5)
    add("narrator", mod.OUTRO, 0.5)
    if mod.CLOSING is not None:
        add(mod.CLOSING[0], mod.CLOSING[1], 0.3)
    elif getattr(mod, "FORMAT", None) != "taster":
        problems.append("Only an explicit taster may end with the English outro without a native closing")

    for r in {s["v"] for s in segs} - {"narrator"}:
        if r not in mod.LABELS:
            problems.append(f"role {r!r} missing from LABELS (and it must be a key of out/<show>/cast.json; no VOICES any more)")

    review = [f"# {mod.ID}: review sheet", "",
              f"Title: {mod.TITLE}", f"Level: {mod.LEVEL}", f"Pair: {mod.PAIR}",
              f"Source: {mod.SOURCE_NAME}", getattr(mod, "SOURCE_NOTE", ""), "",
              "Each script line, its English meaning, and the subtitle line(s) it was taken from "
              "(cue number and time in the sidecar). `new` = written for the story, no subtitle behind it; "
              "`adapted` = a source line changed as noted.", "",
              "| # | Speaker | Script line | English meaning | Source subtitle line | Note |",
              "|---|---|---|---|---|---|"]
    sources = []
    cue_map = cues(mod.SOURCE_FILE) if check_source else {}
    for k, (role, text, en, srcs, note) in enumerate(mod.STORY):
        shown = []
        for no, frag in srcs:
            if check_source:
                if no not in cue_map:
                    problems.append(f"story {k}: no cue {no} in {mod.SOURCE_FILE}")
                    continue
                ts, full = cue_map[no]
                if squash(frag) not in squash(full):
                    problems.append(f"story {k}: fragment {frag!r} not in cue {no}: {full[:80]!r}")
                shown.append(f"#{no} {ts}: {frag}")
            else:
                shown.append(f"#{no}: {frag}")
            sources.append({"line": k, "cue": no, "fragment": frag})
        label = label_of(mod, role)
        kind = "new" if not srcs else ("adapted" if note else "verbatim")
        review.append(f"| {k + 1} | {label} | {text} | {en} | {'<br>'.join(shown) or 'new'} | "
                      f"{(kind + ': ' + note) if note else kind} |")
    review += ["", "## Walk-through narration (English only, no target-language words quoted)", ""]
    review += [f"- {g}" for _, _, g in mod.WALK]
    spec = {"id": mod.ID, "pair": mod.PAIR, "title": mod.TITLE, "level": mod.LEVEL,
            "labels": mod.LABELS, "segments": segs,
            "source": {"show": mod.SOURCE_NAME, "file": str(mod.SOURCE_FILE), "lines": sources}}
    if getattr(mod, "FORMAT", None) is not None: spec["format"] = mod.FORMAT
    return spec, "\n".join(review) + "\n", problems


def label_of(mod, role):
    return {"narrator": "Narrator"}.get(role) or mod.LABELS.get(role, role)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else None
    if out and str(out) in args: args.remove(str(out))
    mod = load(args[0])
    out = out or Path(args[0]).with_suffix(".json")
    spec, review, problems = build(mod, "--no-source-check" not in sys.argv)
    for f in SHOW_FIELDS:
        if hasattr(mod, f): spec[f.lower()] = getattr(mod, f)
    spec["source"]["file"] = str(mod.SOURCE_FILE)
    m = re.fullmatch(r"([a-z-]+)-s(\d\d)e(\d\d)-scene-(\d\d)", mod.ID)      # show/season/episode/scene come from the id
    if m: spec.update(show=m[1], season=int(m[2]), episode=int(m[3]), scene=int(m[4]))
    spec = {"schemaVersion": 1, **spec}                                    # spec/schema/script.schema.json
    if problems:
        print("PROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(1)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    out.with_suffix(".REVIEW.md").write_text(review, encoding="utf-8")
    print(f"{mod.ID}: {len(mod.STORY)} story lines, {len(spec['segments'])} segments -> {out}")
