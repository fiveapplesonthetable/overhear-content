#!/usr/bin/env python3
"""Fill missing `stress` values on annotated words (FEEDBACK.md items 7 and 9). Driver is stdlib only.

  python3 tools/fill_stress.py [out] [--dry-run]

A word needs a value when it is not a name and (the show is French, or the Russian word has 2+ vowels and no ё).
  French   1. the IPA the same token (case-folded, punctuation stripped) has elsewhere in the show, if all agree on one;
           2. else espeak-ng (fr-fr) through `phonemizer`, run in the local-tts kokoro venv; length marks and stress
              marks are removed so the value is bare IPA like the rest of the corpus.
  Russian  RuAccent (CPU) on the whole segment, in the f5 venv; the marked word replaces the null.
Only null/empty values are written; nothing else in the file changes. Paths of the helper venvs can be overridden with
OVERHEAR_PHON_PY / OVERHEAR_RUACCENT_PY.
"""
import collections, json, os, re, subprocess, sys
from pathlib import Path

PHON_PY = os.environ.get("OVERHEAR_PHON_PY", "/mnt/agent/local-tts/venv-kokoro/bin/python")
ACC_PY = os.environ.get("OVERHEAR_RUACCENT_PY", "/mnt/agent/local-tts/venv-f5/bin/python")
ACC_CLI = "/mnt/agent/ru-listen/pipeline/render/ruaccent_cli.py"
ACUTE = "́"
PHON_SRC = """
import json, sys, espeakng_loader
from phonemizer.backend.espeak.wrapper import EspeakWrapper
EspeakWrapper.set_library(espeakng_loader.get_library_path()); EspeakWrapper.set_data_path(espeakng_loader.get_data_path())
from phonemizer import phonemize
w = json.load(sys.stdin)
json.dump(phonemize(w, language="fr-fr", backend="espeak", strip=True), sys.stdout, ensure_ascii=False)
"""


def key(t): return re.sub(r"^[^\w]+|[^\w]+$", "", t.lower())
def bare(t): return re.sub(r"^[^\w]+|[^\w]+$", "", t)
def tokens_of(text): return [x for x in text.split() if re.search(r"\w", x)]
def vowels(s): return len(re.findall("[аеёиоуыэюя]", s.lower()))


def needs(lang, w):
    if w["pos"] == "name" or w.get("stress"): return False
    return lang == "fr" or (vowels(w["t"]) > 1 and "ё" not in w["t"].lower())


def run(cmd, payload):
    r = subprocess.run(cmd, input=json.dumps(payload, ensure_ascii=False), capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def main(argv):
    dry = "--dry-run" in argv
    args = [a for a in argv if not a.startswith("--")]
    base = Path(args[0] if args else "out")
    files = []
    known = collections.defaultdict(lambda: collections.defaultdict(set))       # show -> key -> {ipa}
    todo_fr, todo_ru = set(), []
    for nf in sorted(base.rglob("scene-??.notes.json")):
        show = nf.parent.parent.name
        lang = "fr" if show == "dix-pour-cent" else "ru"
        script = json.loads(Path(str(nf).replace(".notes.json", ".json")).read_text(encoding="utf-8"))
        notes = json.loads(nf.read_text(encoding="utf-8"))
        files.append((nf, show, lang, script, notes))
        for e in notes["lines"]:
            if script["segments"][e["seg"]]["v"] == "narrator": continue
            for w in e["words"]:
                if w.get("stress") and (lang == "fr" or ACUTE in w["stress"]): known[show][key(w["t"])].add(w["stress"] if lang == "fr" else w["stress"].lower())
                elif needs(lang, w):
                    if lang == "fr": todo_fr.add(key(w["t"]))
                    else: todo_ru.append(script["segments"][e["seg"]]["t"])
    # lexicon entries with stress null (the schema wants a string): collected here, filled below
    lex_known = collections.defaultdict(lambda: collections.defaultdict(set))   # show -> lemma -> {stress}
    lex_todo = {"fr": set(), "ru": set()}
    for nf, show, lang, script, notes in files:
        for k, L in notes["lexicon"].items():
            if L.get("stress"): lex_known[show][k].add(L["stress"])
            elif lang == "ru" and vowels(k) > 1 and "ё" not in k: lex_todo["ru"].add(k)
            elif lang == "fr": lex_todo["fr"].add(k)
    # French: corpus first, espeak for the rest
    fr_map = {k: next(iter(v)) for s in known.values() for k, v in s.items() if len(v) == 1}
    need_phon = sorted(k for k in todo_fr if not any(k in known[s] and len(known[s][k]) == 1 for s in known))
    phon = {}
    if need_phon:
        out = run([PHON_PY, "-c", PHON_SRC], need_phon)
        phon = {k: re.sub(r"[ːˈˌ]", "", v).replace(" ", "") for k, v in zip(need_phon, out)}
    lex_fr = sorted(k for k in lex_todo["fr"] if not any(len(lex_known[sh].get(k, ())) == 1 for sh in lex_known))
    if lex_fr:
        out = run([PHON_PY, "-c", PHON_SRC], lex_fr)
        phon.update({"lex:" + k: re.sub(r"[ːˈˌ]", "", v).replace(" ", "") for k, v in zip(lex_fr, out)})
    lex_ru = sorted(lex_todo["ru"])
    ru_lex = dict(zip(lex_ru, run([ACC_PY, ACC_CLI], lex_ru))) if lex_ru else {}
    ru_text = sorted(set(todo_ru))
    acc = dict(zip(ru_text, run([ACC_PY, ACC_CLI], ru_text))) if ru_text else {}
    stats = collections.Counter()
    for nf, show, lang, script, notes in files:
        hit = False
        for e in notes["lines"]:
            seg = script["segments"][e["seg"]]["t"]
            if script["segments"][e["seg"]]["v"] == "narrator": continue
            marked = acc.get(seg, "").split() if lang == "ru" else []
            toks = tokens_of(seg)
            for w in e["words"]:
                if not needs(lang, w): continue
                if lang == "fr":
                    k = key(w["t"])
                    if len(known[show].get(k, ())) == 1: v, src = next(iter(known[show][k])), "corpus"
                    else: v, src = phon.get(k), "espeak"
                else:
                    v, src = None, "ruaccent"
                    mt = [m for m in marked if m.replace(ACUTE, "").strip(".,!?:;—-«»…\"") == bare(w["t"]).strip("-")] if marked else []
                    cand = [bare(m) for m in marked if bare(m.replace(ACUTE, "")) == bare(w["t"])]
                    if cand and ACUTE in cand[0]: v = cand[0]
                    elif len(known[show].get(key(w["t"]), ())) == 1:          # RuAccent left it bare: same form elsewhere in the show
                        v, src = next(iter(known[show][key(w["t"])])), "corpus"
                        if bare(w["t"])[:1].isupper(): v = v[:1].upper() + v[1:]
                if v: w["stress"] = v; hit = True; stats[f"{lang} filled from {src}"] += 1
                else: stats[f"{lang} left"] += 1; print("LEFT", nf.name, w["t"])
        for k, L in notes["lexicon"].items():
            if L.get("stress"): continue
            if lang == "ru" and (vowels(k) <= 1 or "ё" in k): v, src = k, "lexicon lemma"            # one vowel or ё: no mark needed
            elif len(lex_known[show].get(k, ())) == 1: v, src = next(iter(lex_known[show][k])), "lexicon corpus"
            elif lang == "ru": v, src = (ru_lex.get(k) if ACUTE in ru_lex.get(k, "") else None), "lexicon ruaccent"
            else: v, src = phon.get("lex:" + k), "lexicon espeak"
            if v: L["stress"] = v; hit = True; stats[f"{lang} {src}"] += 1
            else: stats[f"{lang} lexicon left"] += 1; print("LEFT lexicon", nf.name, k)
        if hit and not dry: nf.write_text(json.dumps(notes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(dict(stats))


if __name__ == "__main__":
    main(sys.argv[1:])
