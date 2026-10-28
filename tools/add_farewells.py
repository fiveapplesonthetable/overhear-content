#!/usr/bin/env python3
"""Give every script a closing farewell (FEEDBACK item 5). Python 3 stdlib only. Idempotent.

A script whose last segment is not a short farewell (the app validator's rule: matches FAREWELL and <= 6 words) has that
last segment, a repeat of the final story line, replaced by a farewell from a fixed per-language list, spoken by the same
role (it is a speaking role of the scene). The notes file gets the entry for that segment index (trans, words) and the
lexicon entries the words need. The word/lexicon annotations are not written here: they are copied from scenes in the
repo that already end with that exact farewell (the most common version per language), so they are consistent
show-wide. Which farewell a scene gets is fixed by a hash of its id.

  python3 -I tools/add_farewells.py [out_dir]        # default: out
"""
import collections, json, re, sys, zlib
from pathlib import Path

FAREWELLS = {"ru": ["Пока!", "До свидания!", "До встречи!", "Хорошего дня!", "Всего хорошего!"],
             "fr": ["À bientôt!", "Au revoir!", "À demain!", "Bonne soirée!", "Bonne journée!"]}
SHOWS = {"kukhnya": "ru", "domashniy-arest": "ru", "dix-pour-cent": "fr"}
FAREWELL = {"ru": re.compile(r"Пока|До свидания|До встречи|До завтра|До скорого|До скорой|Увидимся|Всего (хорошего|доброго)|Счастливо|Хорошего дня|Спокойной ночи|Прощайте|Удачи", re.I),
            "fr": re.compile(r"À bientôt|Au revoir|À demain|À plus|À tout à l'heure|À la prochaine|Salut|Bonne (soirée|journée|nuit)|Bonsoir|Bon courage", re.I)}
J = lambda o: json.dumps(o, ensure_ascii=False, sort_keys=True)


def is_farewell(lang, t):
    return bool(FAREWELL[lang].search(t)) and len(t.split()) <= 6


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def dump(p, o, indent):
    p.write_text(json.dumps(o, ensure_ascii=False, indent=indent) + "\n", encoding="utf-8")


def indent_of(p):
    return 1 if p.read_text(encoding="utf-8").startswith('{\n "') else 2


def main(out):
    out = Path(out)
    scripts = sorted(out.glob("*/*/scene-[0-9][0-9].json"))
    # 1. library: (lang, farewell) -> most common (line entry, lexicon entries) among scenes that end with exactly it
    seen = collections.defaultdict(collections.Counter)
    orig = {}
    for p in scripts:
        lang = SHOWS[p.parts[-3]]
        d = load(p); last = d["segments"][-1]
        if last["t"] not in FAREWELLS[lang]: continue
        n = load(p.with_suffix(".notes.json"))
        e = next((l for l in n["lines"] if l["seg"] == len(d["segments"]) - 1), None)
        if not e: continue
        lemmas = {w["lemma"].lower() for w in e["words"] if w.get("pos") != "name"}
        if not all(l in n["lexicon"] for l in lemmas): continue
        v = {"entry": {"trans": e["trans"], "words": e["words"]}, "lex": {l: n["lexicon"][l] for l in sorted(lemmas)}}
        seen[(lang, last["t"])][J(v)] += 1
        orig[(lang, last["t"], J(v))] = v          # keep the original key order of the files
    lib = {k: orig[(*k, c.most_common(1)[0][0])] for k, c in seen.items()}
    changed = 0
    for p in scripts:
        lang = SHOWS[p.parts[-3]]
        ind = indent_of(p)
        d = load(p); segs = d["segments"]
        if is_farewell(lang, segs[-1]["t"]): continue
        fw = FAREWELLS[lang][zlib.crc32(d["id"].encode()) % len(FAREWELLS[lang])]
        if (lang, fw) not in lib: sys.exit(f"no annotation template for {lang} {fw!r}")
        t = lib[(lang, fw)]
        idx = len(segs) - 1
        segs[-1] = {"v": segs[-1]["v"], "t": fw, "gap": 0.3}
        npath = p.with_suffix(".notes.json")
        n = load(npath)
        entry = {"seg": idx, "trans": t["entry"]["trans"], "words": t["entry"]["words"]}
        n["lines"] = [l for l in n["lines"] if l["seg"] != idx] + [entry]
        n["lines"].sort(key=lambda l: l["seg"])
        for k, v in t["lex"].items(): n["lexicon"].setdefault(k, v)
        dump(p, d, ind); dump(npath, n, indent_of(npath)); changed += 1
    print(f"farewell added in {changed} scripts")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "out")
