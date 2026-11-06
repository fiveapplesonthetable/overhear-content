#!/usr/bin/env python3
"""Turn an authoring module into a scene script (scene-NN.json); optionally write a review sheet (--review FILE).

The structure is fixed (mirrors episodes 01-05): narrator intro, the whole story, a narrator
walk-through that replays key lines, the story again with shorter gaps, a send-off ending on one
short target-language line. The authoring module supplies the words; this script supplies the
gaps, checks the language rules, and checks every claimed source line against the subtitle file.

    python3 tools/compose.py out/kukhnya/s01e02/authoring/scene-01.py --out out/kukhnya/s01e02/scene-01.json
        [--review /tmp/scene-01.md]   a sheet of every line, its meaning and source cue, for your own read-through (never commit it)
        [--no-source-check]
    (see examples/*/authoring.py; SOURCE_FILE is relative to the repo root)

An authoring module defines:
    ID, TITLE, LEVEL, PAIR (the show.json pair, e.g. "ru-en"), LABELS, SOURCE_NAME, SOURCE_FILE,
    INTRO, STORY, OPENER, WALK, TRANSITION, OUTRO, CLOSING
  STORY    [(role, text, english, [(cue_no, "fragment of the subtitle line"), ...], note)]
  WALK     [(story_line_index, sentence_or_None, narrator_gloss)]  replay then explain
"""
import importlib.util, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHOW_FIELDS = ("SHOW", "SEASON", "EPISODE", "SCENE")   # optional module attributes copied into the JSON
sys.path.insert(0, str(ROOT / "render"))
from textprep import split_sentences           # the renderer's own split, so replays and spans agree (incl. 。！？؟)


def sentences(text):
    return [seg.strip() for _, _, seg in split_sentences(text.strip()) if seg.strip()]


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
    narrator = []
    for m in [mod.INTRO, mod.OPENER, mod.TRANSITION, mod.OUTRO]:
        if isinstance(m, str):
            narrator.append(m)
        elif m is not None:
            narrator.extend([p for p in m if isinstance(p, str)])
    for _, _, g in mod.WALK:
        if isinstance(g, str):
            narrator.append(g)
        else:
            narrator.extend([p for p in g if isinstance(p, str)])
    for t in narrator:
        if cyr.search(t): problems.append(f"narrator text contains Cyrillic: {t[:60]}")
        if mod.PAIR == "fr-en" and re.search(r"\b(le|la|les|est|vous|bonjour|merci)\b", t.lower()) and "bonjour" in t.lower():
            problems.append(f"narrator seems to quote French: {t[:60]}")


def build(mod, check_source=True, is_original=False):
    problems = []
    if is_original and getattr(mod, "SOURCE_FILE", None):
        problems.append("original scripts must not define SOURCE_FILE")
    check_language(mod, problems)
    story_sents = {s for _, text, *_ in mod.STORY for s in sentences(text)}
    segs = []

    def add(v, t, gap):
        segs.append({"v": v, "t": t, "gap": gap})

    def add_narrator_field(field, gap):
        if isinstance(field, str):
            add("narrator", field, gap)
        elif field is not None:
            for p_idx, part in enumerate(field):
                p_gap = gap if p_idx == len(field) - 1 else 0.25
                if isinstance(part, str):
                    add("narrator", part, p_gap)
                else:
                    add(part[0] or "narrator", part[1], p_gap)

    add_narrator_field(mod.INTRO, 0.8)
    for k, (role, text, *_r) in enumerate(mod.STORY):
        add(role, text, 0.9 if k == len(mod.STORY) - 1 else 0.55)
    add_narrator_field(mod.OPENER, 0.4)
    for k, (idx, only, gloss) in enumerate(mod.WALK):
        role, text = mod.STORY[idx][0], mod.STORY[idx][1]
        replay = only or text
        for s in sentences(replay):
            if s not in story_sents:
                problems.append(f"walk {k}: replay sentence not in the story: {s}")
        add(role, replay, 0.55)
        last = k == len(mod.WALK) - 1
        
        if isinstance(gloss, str):
            if last and isinstance(mod.TRANSITION, str):
                add("narrator", gloss + " " + mod.TRANSITION, 0.9)
            elif last and isinstance(mod.TRANSITION, list):
                add("narrator", gloss, 0.25)
                add_narrator_field(mod.TRANSITION, 0.9)
            else:
                add("narrator", gloss, 0.4)
        else:
            for p_idx, part in enumerate(gloss):
                p_last = last and (p_idx == len(gloss) - 1)
                gap = 0.9 if p_last else (0.4 if p_idx == len(gloss) - 1 else 0.25)
                if isinstance(part, str):
                    if p_last and isinstance(mod.TRANSITION, str):
                        add("narrator", part + " " + mod.TRANSITION, gap)
                    elif p_last and isinstance(mod.TRANSITION, list):
                        add("narrator", part, 0.25)
                        add_narrator_field(mod.TRANSITION, gap)
                    else:
                        add("narrator", part, gap)
                else:
                    p_role, p_text = part
                    p_role = p_role or role
                    if squash(p_text) not in squash(text):
                        problems.append(f"walk {k}: inline callout {p_text!r} not in story line: {text!r}")
                    add(p_role, p_text, gap)
    for k, (role, text, *_r) in enumerate(mod.STORY):
        add(role, text, 0.9 if k == len(mod.STORY) - 1 else 0.5)
    add_narrator_field(mod.OUTRO, 0.5)
    if mod.CLOSING is not None:
        add(mod.CLOSING[0], mod.CLOSING[1], 0.3)
    else:
        problems.append("CLOSING is required: every lesson ends with a short new target-language farewell")

    for r in {s["v"] for s in segs} - {"narrator"}:
        if r not in mod.LABELS:
            problems.append(f"role {r!r} missing from LABELS (and it must be a key of <show>/cast.json; no VOICES any more)")

    source_name = getattr(mod, "SOURCE_NAME", "Overhear Original")
    review = [f"# {mod.ID}: review sheet", "",
              f"Title: {mod.TITLE}", f"Level: {mod.LEVEL}", f"Pair: {mod.PAIR}",
              f"Source: {source_name}", getattr(mod, "SOURCE_NOTE", ""), "",
              "Each script line, its English meaning, and its source note.", "",
              "| # | Speaker | Script line | English meaning | Source subtitle line | Note |",
              "|---|---|---|---|---|---|"]
    sources = []
    cue_map = cues(mod.SOURCE_FILE) if (check_source and not is_original and getattr(mod, "SOURCE_FILE", None)) else {}
    for k, row in enumerate(mod.STORY):
        if len(row) == 3:
            role, text, en = row
            srcs, note = [], ""
        elif len(row) == 4 and isinstance(row[3], str):
            role, text, en, note = row
            srcs = []
        else:
            role, text, en, srcs, note = row[0], row[1], row[2], row[3], (row[4] if len(row) > 4 else "")
        shown = []
        for no, frag in srcs:
            if is_original:
                problems.append(f"story {k}: original scripts must not reference subtitle cues")
                continue
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
        kind = "original" if is_original else ("new" if not srcs else ("adapted" if note else "verbatim"))
        review.append(f"| {k + 1} | {label} | {text} | {en} | {'<br>'.join(shown) or ('original' if is_original else 'new')} | "
                      f"{(kind + ': ' + note) if note else kind} |")
    review += ["", "## Walk-through narration (English only, no target-language words quoted)", ""]
    for idx, _, g in mod.WALK:
        role = mod.STORY[idx][0]
        if isinstance(g, str):
            review.append(f"- {g}")
        else:
            parts = []
            for p in g:
                if isinstance(p, str):
                    parts.append(p)
                else:
                    parts.append(f"**[{p[0] or role}: {p[1]}]**")
            review.append(f"- {' '.join(parts)}")
    spec = {"id": mod.ID, "pair": mod.PAIR, "title": mod.TITLE, "level": mod.LEVEL,
            "labels": mod.LABELS, "segments": segs}
    if not is_original:
        spec["source"] = {"show": mod.SOURCE_NAME, "file": str(mod.SOURCE_FILE), "lines": sources}
    return spec, "\n".join(review) + "\n", problems


def label_of(mod, role):
    return {"narrator": "Narrator"}.get(role) or mod.LABELS.get(role, role)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    explicit_root = None
    out = None
    review_to = None
    args = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--root":
            explicit_root = argv[i + 1]; i += 2; continue
        if a.startswith("--root="):
            explicit_root = a.split("=", 1)[1]; i += 1; continue
        if a == "--out":
            out = Path(argv[i + 1]); i += 2; continue
        if a == "--review":
            review_to = Path(argv[i + 1]); i += 2; continue
        if not a.startswith("--"):
            args.append(a)
        i += 1
    src_path = Path(args[0])
    mod = load(src_path)
    out = out or src_path.with_suffix(".json")
    is_original = (explicit_root == "originals") or (explicit_root is None and (
        "originals" in src_path.resolve().parts or "originals" in out.resolve().parts or getattr(mod, "SOURCE_FILE", None) is None
    ))
    spec, review, problems = build(mod, check_source=("--no-source-check" not in argv and not is_original), is_original=is_original)
    for f in SHOW_FIELDS:
        if hasattr(mod, f): spec[f.lower()] = getattr(mod, f)
    if not is_original and "source" in spec:
        spec["source"]["file"] = str(mod.SOURCE_FILE)
    m = re.fullmatch(r"([a-z0-9-]+)-s(\d\d)e(\d\d)-scene-(\d\d)", mod.ID)      # show/season/episode/scene come from the id
    if m: spec.update(show=m[1], season=int(m[2]), episode=int(m[3]), scene=int(m[4]))
    spec = {"schemaVersion": 1, **spec}                                    # spec/schema/script.schema.json
    if problems:
        print("PROBLEMS:\n  " + "\n  ".join(problems))
        return 1
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if review_to: review_to.write_text(review, encoding="utf-8")
    print(f"{mod.ID}: {len(mod.STORY)} story lines, {len(spec['segments'])} segments -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
