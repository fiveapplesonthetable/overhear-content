#!/usr/bin/env python3
"""Make every annotated line's `words[].t` equal the line's whitespace tokens (FEEDBACK.md item 9). Stdlib only.

  python3 tools/fix_tokens.py [out] [--dry-run]

For each non-narrator line whose `words` do not match the whitespace-split text of the segment (bare dashes skipped),
the words are re-aligned to the text by letters (ignoring spaces, apostrophes, hyphens and punctuation; the letters of
the tokens and of the words must be identical or the line is left alone and reported). Each group of overlapping
tokens/words is then rebuilt:

  * 1 word = 1 token (only punctuation differs, e.g. `boire` for `boire?`): `t` is set to the token.
  * several words = 1 token (`J'` + `ai` for `J'ai`): the entry comes from the same token annotated correctly
    elsewhere in the show (preferring the same lemma); if none, it is composed from the pieces: lemma/pos of the
    head piece (verb > noun > adj > adv > last), gloss and gram joined, IPA concatenated.
  * 1 word = several tokens (`un peu`, `tout de suite`, `Qu'est-ce que`): one entry per token, from the corpus as above;
    if the token is not found anywhere it inherits the unit's lemma, pos and gloss with no stress (filled in later).

Lexicon entries needed by new lemmas are copied from the same show's other scenes. Nothing in the text, `trans` or
segment order changes.
"""
import collections, json, re, sys
from pathlib import Path

HEAD_PRI = {"verb": 5, "noun": 4, "adj": 3, "adv": 2}
FIELDS = ("lemma", "pos", "stress", "gloss", "gram")


def letters(s): return re.sub(r"[\W_]", "", s.lower())
def key(t): return re.sub(r"^[^\w]+|[^\w]+$", "", t.lower())


def tokens_of(text): return [x for x in text.split() if re.search(r"\w", x)]


def load(f): return json.loads(Path(f).read_text(encoding="utf-8"))


def build_corpus(base):
    ent = collections.defaultdict(collections.Counter)       # (show, key) -> Counter of entry tuples
    lex = collections.defaultdict(collections.Counter)       # (show, lemma) -> Counter of json
    pairs = []
    for nf in sorted(base.rglob("scene-??.notes.json")):
        show = nf.parent.parent.name
        script = load(str(nf).replace(".notes.json", ".json"))
        notes = load(nf)
        pairs.append((nf, script, notes))
        for e in notes["lines"]:
            toks = tokens_of(script["segments"][e["seg"]]["t"])
            if [w["t"] for w in e["words"]] == toks:
                for w in e["words"]:
                    if w.get("stress") is not None or script["pair"] == "ru-en":
                        ent[(show, key(w["t"]))][tuple(w.get(f) for f in FIELDS)] += 1
        for k, L in notes["lexicon"].items(): lex[(show, k)][json.dumps(L, ensure_ascii=False)] += 1
    return ent, lex, pairs


def lookup(ent, show, tok, prefer_lemmas):
    c = ent.get((show, key(tok)))
    if not c: return None
    cands = [(n, t) for t, n in c.items() if t[0] in prefer_lemmas] or [(n, t) for t, n in c.items()]
    return dict(zip(FIELDS, max(cands)[1]))


def compose(pieces, tok):
    head = max(reversed(pieces), key=lambda p: HEAD_PRI.get(p["pos"], 1))
    st = [p.get("stress") for p in pieces]
    return {"t": tok, "lemma": head["lemma"], "pos": head["pos"],
            "stress": "".join(st) if all(st) else None,
            "gloss": " ".join(p["gloss"] for p in pieces),
            "gram": " + ".join(f"{p['t']}: {p['gram']}" for p in pieces)}


def groups(toks, words):
    """Pair up token and word runs that cover the same letters. -> [(toks, words)] or None."""
    tl, wl = [letters(t) for t in toks], [letters(w["t"]) for w in words]
    if "".join(tl) != "".join(wl): return None
    out, i, j = [], 0, 0
    while i < len(toks) or j < len(words):
        a, b, gt, gw = 0, 0, [], []
        while True:
            if a <= b and i < len(toks): a += len(tl[i]); gt.append(toks[i]); i += 1
            elif j < len(words): b += len(wl[j]); gw.append(words[j]); j += 1
            else: break
            if a == b and gt and gw: break
        out.append((gt, gw))
    return out


def add_missing(show, e, toks, ent, bad):
    """Letters of tokens and words differ (tokens dropped from the annotation, stray `-tu` pieces, half-split elisions):
    keep the runs that match, rebuild the others from the corpus (insert/replace) or drop the stray words (delete)."""
    import difflib
    ws = e["words"]
    sm = difflib.SequenceMatcher(None, [letters(t) for t in toks], [letters(w["t"]) for w in ws], autojunk=False)
    new = []
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        gt, gw = toks[a0:a1], ws[b0:b1]
        if op == "equal": new += [{**w, "t": t} for t, w in zip(gt, gw)]
        elif not gt: continue          # annotation words with no token (e.g. `-tu` after `vas-tu`): dropped
        else:
            r = rebuild(show, gt, gw, ent)
            if r is None: bad.append(("token not in corpus", gt, [w["t"] for w in gw])); return None
            new += r
    return new


def rebuild(show, gt, gw, ent):
    out = []
    prefer = {w["lemma"] for w in gw}
    for tok in gt:
        c = lookup(ent, show, tok, prefer)
        if c: out.append({"t": tok, **c})
        elif len(gt) == 1 and gw: out.append(compose(gw, tok))
        elif gw:
            u = gw[0]
            out.append({"t": tok, "lemma": u["lemma"], "pos": u["pos"], "stress": None, "gloss": u["gloss"], "gram": u["gram"]})
        elif tok[:1].isupper():                                    # a surname dropped from the annotation: a name, no stress needed
            nm = key(tok).capitalize()
            out.append({"t": tok, "lemma": nm, "pos": "name", "stress": None, "gloss": nm, "gram": "proper name"})
        else: return None
    return out


def fix_line(show, e, toks, ent, bad):
    g = groups(toks, e["words"])
    if g is None: return add_missing(show, e, toks, ent, bad)
    new = []
    for gt, gw in g:
        if len(gt) == 1 and len(gw) == 1: new.append({**gw[0], "t": gt[0]}); continue
        prefer = {w["lemma"] for w in gw}
        for tok in gt:
            c = lookup(ent, show, tok, prefer)
            if c: new.append({"t": tok, **c})
            elif len(gt) == 1: new.append(compose(gw, tok))
            else:
                u = gw[0]
                new.append({"t": tok, "lemma": u["lemma"], "pos": u["pos"], "stress": None, "gloss": u["gloss"], "gram": u["gram"]})
    return new


def main(argv):
    dry = "--dry-run" in argv
    args = [a for a in argv if not a.startswith("--")]
    base = Path(args[0] if args else "out")
    ent, lex, pairs = build_corpus(base)
    stats = collections.Counter()
    bad = []
    for nf, script, notes in pairs:
        show, hit = nf.parent.parent.name, False
        for e in notes["lines"]:
            seg = script["segments"][e["seg"]]
            if seg["v"] == "narrator": continue
            toks = tokens_of(seg["t"])
            if [w["t"] for w in e["words"]] == toks: continue
            nw = fix_line(show, e, toks, ent, bad)
            if nw is None: stats["lines left"] += 1; continue
            e["words"] = [{f: w.get(f) for f in ("t",) + FIELDS} for w in nw]
            stats["lines fixed"] += 1; hit = True
        for e in notes["lines"]:
            for w in e["words"]:
                if w["pos"] != "name" and w["lemma"].lower() not in notes["lexicon"]:
                    c = lex.get((show, w["lemma"].lower()))
                    if c: notes["lexicon"][w["lemma"].lower()] = json.loads(c.most_common(1)[0][0]); stats["lexicon entries copied"] += 1; hit = True
                    else: bad.append(("no lexicon entry", nf.name, w["lemma"]))
        if hit:
            stats["files changed"] += 1
            if not dry: nf.write_text(json.dumps(notes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(dict(stats))
    for b in bad[:40]: print("UNFIXED", b)
    print(len(bad), "unfixed")


if __name__ == "__main__":
    main(sys.argv[1:])
