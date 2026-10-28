#!/usr/bin/env python3
"""One-shot migration of out/ to the v1 schemas (spec/schema/*.schema.json). Python 3 stdlib only.

  python3 tools/migrate_v1.py [out] [--dry-run]

Applies to the source files, deterministically and idempotently, the same legacy-variant rewrites that the app's
`validate.py --lenient` makes in memory (so a second run changes nothing):

  scenes.json   schemaVersion added; source_file/total_cues/source and per scene cue_start/cue_end/id/time_range/
                status/merged_into dropped; bilingual "<target>  (<English>)" titles -> the English part;
                keys in schema order.
  scene-NN.json schemaVersion added; show/season/episode/scene derived from the id; level -> canonical; segment
                text trimmed.
  *.notes.json  schemaVersion + id added; show/season/episode/scene dropped; line.text dropped; word `grammar` ->
                `gram` (`gram` wins when both exist); word `note` folded into an empty `gram`; missing `stress` -> null;
                lexicon: aspect/animacy spellings canonicalised (perf/perfective -> pf, imperf/imperfective/ipf ->
                impf, animate/inanimate/inanim -> anim/inan, `animate: bool` -> animacy), `gender: null` omitted,
                gender `pl` -> number `pl`, "plural only" -> `pl`, junk genders repaired or omitted, `ipa` -> `stress`
                (when stress is empty), IPA found in `pos` moved out (see below), `moreForms`/`forms` added,
                one-column tables -> null / dropped, unknown fields dropped.

IPA in `pos`: about 50 French entries have their fields shifted by one (`pos` holds the IPA, `stress` holds the part of
speech). They are rotated back: stress <- IPA, pos <- the old stress value. Russian entries whose `pos` holds the word
itself (затем, близко, хреново) get `adv`.

It does NOT touch the text of any line, the tokens of a `words` list, summaries or locations (those are separate steps).
"""
import json, re, sys
from pathlib import Path

POS = {"noun", "verb", "adj", "adv", "pron", "prep", "conj", "part", "num", "interj", "det", "phrase", "name"}
ASPECT = {"perf": "pf", "perfective": "pf", "pf": "pf", "imperf": "impf", "imperfective": "impf", "ipf": "impf", "impf": "impf"}
ANIMACY = {"animate": "anim", "inanimate": "inan", "inanim": "inan", "anim": "anim", "inan": "inan"}
LEVEL = {"ru-en": "A1 — Duolingo Section 2", "fr-en": "A1 — débutant"}
GENDER_FIX = {"mo": "m", "pwɛ̃": "m", "pisin": "f"}          # mot, poing, piscine: spelling/IPA typed into gender; the real value
GENDER_OMIT = {"m/f", "mf", "fan"}                              # common-gender nouns (fan, gosse, orthophoniste): no single value
POS_FIX = {"aj": "interj", "lao": "adv", "ajœʁ": "adv"}         # IPA-in-pos entries whose real pos was lost with the shift
SCENES_KEYS = ("scene", "start", "end", "title", "summary", "characters", "location", "merge")
WORD_KEYS = ("t", "lemma", "pos", "stress", "gloss", "gram")
LEX_KEYS = {"lemma", "stress", "pos", "gloss", "aspect", "pair", "gender", "plural", "animacy", "governs", "register",
            "meanings", "forms", "moreForms", "examples", "related", "number"}
COUNT = {}


def n(name, k=1): COUNT[name] = COUNT.get(name, 0) + k


def table_cols(t): return len(t["columns"]) if isinstance(t, dict) and isinstance(t.get("columns"), list) else 99


def migrate_scenes(d):
    if "schemaVersion" not in d: n("scenes: schemaVersion added")
    out = {"schemaVersion": 1}
    for k in ("show", "season", "episode", "title"): out[k] = d[k]
    for k in d:
        if k not in out and k != "scenes": n(f"scenes: dropped {k}")
    out["scenes"] = []
    for s in d["scenes"]:
        for k in s:
            if k not in SCENES_KEYS: n(f"scenes[]: dropped {k}")
        t = s["title"]
        m = re.fullmatch(r"(.+?)\s{2,}\((.+)\)", t.strip())
        if m: t = m[2].strip(); n("scenes[]: bilingual title -> English part")
        out["scenes"].append({**{k: s[k] for k in SCENES_KEYS if k in s}, "title": t})
    return out


def migrate_script(d):
    if "schemaVersion" not in d: n("script: schemaVersion added")
    out = {"schemaVersion": 1, **{k: v for k, v in d.items() if k != "schemaVersion"}}
    m = re.fullmatch(r"([a-z-]+)-s(\d\d)e(\d\d)-scene-(\d\d)", out["id"])
    for k, v in (("show", m[1]), ("season", int(m[2])), ("episode", int(m[3])), ("scene", int(m[4]))):
        if k not in out: out[k] = v; n(f"script: {k} derived from id")
    lvl = LEVEL.get(out["pair"])
    if lvl and out["level"] != lvl and out["level"] in ("A1", "beginner", "Beginner", "a1"): out["level"] = lvl; n("script: level -> canonical")
    for s in out["segments"]:
        if s["t"] != s["t"].strip(): s["t"] = s["t"].strip(); n("script: segment text trimmed")
    return out


def migrate_lex(key, L):
    # 1. fields shifted by one: pos holds IPA/word, stress holds the part of speech
    if L.get("pos") not in POS:
        if L.get("stress") in POS:                                   # French: pos=IPA, stress=pos
            ipa, L["pos"], L["stress"] = L["pos"], L["stress"], L["pos"]
            n("lexicon: IPA moved out of pos")
        elif L["pos"] in POS_FIX:
            L["pos"] = POS_FIX[L["pos"]]
        else:                                                        # Russian: pos holds the lemma itself
            L["pos"] = "adv"; n("lexicon: pos holding the word -> adv")
    if L.get("pos") in ("aj", "lao", "ajœʁ"): L["pos"] = POS_FIX[L["pos"]]
    if L.get("pos") not in POS: raise ValueError(f"cannot repair pos of {key}: {L.get('pos')!r}")
    # 2. gender / number
    if "gender" in L:
        g = L["gender"]
        if g is None: del L["gender"]; n("lexicon: gender null omitted")
        elif g not in ("m", "f", "n"):
            if g == "pl": L.setdefault("number", "pl"); del L["gender"]; n("lexicon: gender pl -> number pl")
            elif g in GENDER_FIX: L["gender"] = GENDER_FIX[g]; n("lexicon: junk gender repaired")
            elif g in GENDER_OMIT: del L["gender"]; n("lexicon: common-gender omitted")
            else: raise ValueError(f"unknown gender {g!r} on {key}")
    if "number" in L and L["number"] != "pl":
        if "plural" in str(L["number"]): L["number"] = "pl"; n("lexicon: number 'plural only' -> pl")
        else: del L["number"]; n("lexicon: invalid number dropped")
    # 3. aspect / animacy
    if "aspect" in L:
        a = ASPECT.get(str(L["aspect"]).lower())
        if a is None: del L["aspect"]; n("lexicon: unknown aspect dropped")
        elif a != L["aspect"]: L["aspect"] = a; n("lexicon: aspect spelling")
    if "animacy" in L:
        a = ANIMACY.get(str(L["animacy"]).lower())
        if a is None: del L["animacy"]
        elif a != L["animacy"]: L["animacy"] = a; n("lexicon: animacy spelling")
    if "animate" in L:
        v = L.pop("animate"); n("lexicon: animate -> animacy")
        if isinstance(v, bool): L.setdefault("animacy", "anim" if v else "inan")
    if "ipa" in L:
        v = L.pop("ipa"); n("lexicon: ipa -> stress")
        if v and not L.get("stress"): L["stress"] = v
    # 4. tables
    if "moreForms" not in L: L["moreForms"] = []; n("lexicon: moreForms added")
    if "forms" not in L: L["forms"] = None; n("lexicon: forms added as null")
    if table_cols(L["forms"]) < 2 and L["forms"] is not None: L["forms"] = None; n("lexicon: one-column forms -> null")
    if any(table_cols(t) < 2 for t in L["moreForms"]): L["moreForms"] = [t for t in L["moreForms"] if table_cols(t) >= 2]; n("lexicon: one-column moreForms dropped")
    for k in [k for k in L if k not in LEX_KEYS]: del L[k]; n(f"lexicon: dropped {k}")
    return L


def migrate_notes(d, sid):
    if "schemaVersion" not in d: n("notes: schemaVersion added")
    if "id" not in d: n("notes: id added")
    for k in ("show", "season", "episode", "scene"):
        if k in d: n(f"notes: dropped {k}")
    out = {"schemaVersion": 1, "id": sid, "lines": [], "lexicon": {}}
    for e in d["lines"]:
        if "text" in e: n("notes line: dropped text")
        words = []
        for w in e["words"]:
            w = dict(w)
            if "grammar" in w:
                g = w.pop("grammar"); n("word: grammar -> gram")
                if not w.get("gram"): w["gram"] = g
            if "note" in w:
                nt = w.pop("note"); n("word: note folded/dropped")
                if not w.get("gram") and nt: w["gram"] = nt
            if "stress" not in w: w["stress"] = None; n("word: stress key added as null")
            for k in [k for k in w if k not in WORD_KEYS]: del w[k]; n(f"word: dropped {k}")
            words.append({k: w[k] for k in WORD_KEYS if k in w})
        out["lines"].append({"seg": e["seg"], "trans": e["trans"], "words": words})
    for k, L in d["lexicon"].items(): out["lexicon"][k] = migrate_lex(k, L)
    return out


def dump(d, like):
    ind = 2 if re.match(r'\{\n  "', like) else 1
    return json.dumps(d, ensure_ascii=False, indent=ind) + "\n"


def main(argv):
    dry = "--dry-run" in argv
    args = [a for a in argv if not a.startswith("--")]
    base = Path(args[0] if args else "out")
    changed = 0
    for f in sorted(base.rglob("*.json")):
        if f.name == "scenes.json": kind = "scenes"
        elif re.fullmatch(r"scene-\d\d\.notes\.json", f.name): kind = "notes"
        elif re.fullmatch(r"scene-\d\d\.json", f.name): kind = "script"
        else: continue
        text = f.read_text(encoding="utf-8")
        d = json.loads(text)
        if kind == "scenes": new = migrate_scenes(d)
        elif kind == "script": new = migrate_script(d)
        else:
            m = re.fullmatch(r"scene-(\d\d)\.notes\.json", f.name)
            new = migrate_notes(d, f"{f.parent.parent.name}-{f.parent.name}-scene-{m[1]}")
        out = dump(new, text)
        if out != text:
            changed += 1
            if not dry: f.write_text(out, encoding="utf-8")
    print(f"{'would change' if dry else 'changed'} {changed} files")
    for k, v in sorted(COUNT.items(), key=lambda kv: -kv[1]): print(f"  {v:7d}  {k}")


if __name__ == "__main__":
    main(sys.argv[1:])
