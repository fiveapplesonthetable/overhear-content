"""Audio for the forms in the lexicon's declension and conjugation tables (the cells of `forms` / `moreForms`).

One clip per SLOT of a table (pair, lemma, table, row label, column label, cell text), read by the same neutral voice as the example clips (settings.json `forms.voices`) with the same
Qwen3-TTS, loudness and mp3 format, but with the run3 stress LoRA and stress policy "all" (a form is a single word: its stress is the whole
point). Every clip is checked with Whisper; failures are retaken and finally dropped, so the app underlines only forms that play.

  <store>/forms/<id>.mp3 + <id>.json     a finished clip and its record (status "ok"), or a record alone (status "failed")
  <store>/forms/.work/<id>.{json,mp3}    a clip waiting for its Whisper check
  <store>/forms/.plan.json               the items that are current: id + ckey (written by pipeline.py; read by `stage.py forms` and the publisher)

`id` = form_id(pair, lemma, table title, row label, column label, cell). The publisher derives the same id from the entry and the table, and ships a clip
only when `.plan.json` still lists it with the same `ckey` (so stale audio never ships after a stress fix). A slot whose spelling occurs in another slot of
the lemma with a stress that is not certain to be the same gets no clip at all (plain text in the app).
Stress: the surface forms the notes already stress (`words[].stress` of the scenes, by lemma), the lemma's own stress, else RuAccent read
over the whole table column at once (a column is a better context than a lone word). Never marked by hand.
"""
import copy
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

import clips
import config
import form_overrides
import textprep
from plan import cache_key

KIND = "forms"
EMPTY = {"", "-", "–", "—"}


def form_id(pair: str, lemma: str, title: str, row: str, column: str, cell: str) -> str:
    """16 hex chars of sha256(pair NUL lemma NUL table title NUL row label NUL column label NUL cell text). One clip per SLOT of a table:
    the same spelling in two slots (вина, genitive singular and nominative plural) can be stressed differently. The publisher has the
    same function (publish/rulisten_pub/forms.py)."""
    return hashlib.sha256("\0".join((pair, lemma, title, row, column, cell)).encode("utf-8")).hexdigest()[:16]


def forms_settings(settings, lang="ru") -> dict:
    """Qwen settings for one form language. The Russian stress LoRA never voices French."""
    s = copy.deepcopy(settings)
    s["lora"]["enabled"] = bool(settings["forms"]["lora"] and lang == "ru")
    s["tts"]["batch"] = settings["forms"]["batch"]
    if lang != "ru":
        s["tts"]["batch"] = min(4, s["tts"]["batch"])
        s["forms"]["batch"] = s["tts"]["batch"]
    # Forms use QwenEngine even when scene dialogue and narration use F5.
    # Their cache keys must describe Qwen and its LoRA, rather than ttsRu/ttsEn.
    s.pop("ttsRu", None)
    s.pop("ttsEn", None)
    return s


def pieces(cell: str):
    """The forms inside one cell: "весь / всего" is two, read one after the other."""
    return [p.strip() for p in cell.split("/") if p.strip()]


def french_form_text(cell):
    """Read complete alternatives, not the typography of a conjugation table.

    Silent gender/number notation can be removed from a spoken form; unexplained
    parentheses or a bare elision need editorial review and are left unvoiced.
    """
    cell = re.sub(r"\s*/\s*", "/", cell.replace("’", "'").strip())
    # Feminine -e is silent after these vowel endings (allé(e), fini(e),
    # venu(e)); after a consonant it may change pronunciation, e.g. pris(e).
    cell = re.sub(r"(?<=[éiuû])\(e\)(?:\(s\))?", "", cell)
    if "(" in cell or ")" in cell:
        return None
    shared = re.fullmatch(r"((?:il|elle|ils|elles|on)(?:/(?:il|elle|ils|elles|on))+)\s+(.+)", cell)
    alternatives = [f"{subject} {shared[2]}" for subject in shared[1].split("/")] if shared else pieces(cell)
    if not alternatives or any(part.endswith("'") or not re.search(r"[aeiouyàâäéèêëîïôöùûüœæ]", part, re.I) for part in alternatives):
        return None
    return ", ".join(alternatives)


def spoken_form(lang, cell):
    """What the voice is asked to say for a non-Russian cell (None: needs review, no audio)."""
    return french_form_text(cell) if lang == "fr" else ", ".join(pieces(cell))


def slot_ids(scenes, settings):
    """All selected slots, including ones whose new uncertainty removes audio."""
    return {
        form_id(pair, lemma, sl.title, sl.row, sl.column, sl.cell)
        for (pair, lang, lemma), entry in base_entries(scenes).items()
        if lang in settings["forms"]["voices"]
        for sl in slots_of(entry)
    }


@dataclass
class Slot:
    title: str
    row: str            # the row's label (cells[0])
    column: str         # the column's heading
    cell: str
    table: int          # index among the entry's tables
    col: int            # column index in the table


def tables_of(entry):
    return [t for t in [entry.get("forms")] + list(entry.get("moreForms") or []) if t]


def slots_of(entry):
    """Every slot of the entry's tables with a form in it (not the label column, not the dashes), in table, column, row order."""
    out = []
    for ti, table in enumerate(tables_of(entry)):
        width = max((len(r["cells"]) for r in table["rows"]), default=0)
        for c in range(1, width):
            for r in table["rows"]:
                if c < len(r["cells"]) and r["cells"][c].strip() not in EMPTY and pieces(r["cells"][c]):
                    heads = table.get("columns") or []
                    out.append(Slot(table.get("title", ""), r["cells"][0], heads[c] if c < len(heads) else "", r["cells"][c], ti, c))
    return out


def stress_map(scenes):
    """{(lemma, bare form): {stressed forms}} from the notes' words. More than one stress means the notes themselves disagree."""
    out = {}
    for sc in scenes:
        for line in sc.notes.get("lines") or []:
            for w in line.get("words") or []:
                st, lem, t = w.get("stress"), w.get("lemma"), w.get("t")
                if st and lem and t and textprep.ACUTE in st:
                    out.setdefault((lem, textprep.bare(t)), set()).add(st)
    return out


def wants_mark(form: str) -> bool:
    return textprep.has_cyrillic(form) and textprep.vowel_count(form) >= 2 and "ё" not in form.lower()


def _marked(plain: str, stressed: str):
    """`plain` carrying the marks of `stressed` when that is the same word, else None."""
    offs = textprep.acute_offsets(plain, stressed)
    return textprep.apply_inserts(plain, offs) if offs else None


def _apply(p: str, m):
    return (_marked(p, m) if m else None) or p


def base_entries(scenes):
    """{(pair, lang, lemma): entry}: the entry the publisher shows for a lemma (lexicon_merge: most meanings, ties the earliest scene)."""
    base = {}
    for sc in scenes:
        for key, entry in (sc.notes.get("lexicon") or {}).items():
            k = (sc.pair, sc.lang, key)
            if k not in base or len(entry.get("meanings") or []) > len(base[k].get("meanings") or []):
                base[k] = entry
    return base


def _column_guesses(entry, slots, ruaccent):
    """{slot index: [RuAccent's marked piece, ...]} reading each table column as one list (a column is a better context than a lone word)."""
    out = {}
    if ruaccent is None:
        return out
    by_col = {}
    for i, sl in enumerate(slots):
        by_col.setdefault((sl.table, sl.col), []).append(i)
    for idxs in by_col.values():
        flat = [(i, p) for i in idxs for p in pieces(slots[i].cell)]
        marked = ruaccent([", ".join(p for _, p in flat)])[0].split(", ")
        if len(marked) != len(flat):
            continue
        for (i, _), m in zip(flat, marked):
            out.setdefault(i, []).append(m)
    return out


def entry_texts(entry, known, ruaccent, fdict=None, pos=None, use_overrides=True):
    """[(Slot, text for the model | None, why)] for every slot of the entry. Stress, in order: the dictionary's form for exactly this slot
    (`fdict`, Wiktionary: it tells вина́ from ви́на), the notes' stress of the form, the lemma's own stress, RuAccent over the table column.
    A slot gets None (no audio, `why` = the candidates) only when none of its forms has a slot-specific stress AND the readings of a spelling
    that occurs in several slots of the lemma disagree, or the notes stress it two ways. Never a guess."""
    lemma = entry["lemma"]
    slots = slots_of(entry)
    guesses = _column_guesses(entry, slots, ruaccent)
    lemma_st = entry.get("stress") or ""
    occ = {}                                    # spelling -> [(primary, column reading, resolved by the dictionary)] of every place it occurs
    marked = []                                 # per slot: [(spelling, primary, doubt, resolved)]
    for i, sl in enumerate(slots):
        ps = pieces(sl.cell)
        g = guesses.get(i, [None] * len(ps))
        row = []
        for p, gm in zip(ps, g):
            if not wants_mark(p):
                row.append((p, p, False, True))
                continue
            d = fdict.slot_stress(pos, lemma, sl.title, sl.row, sl.column, p) if fdict is not None else None
            if d:
                row.append((p, _apply(p, d), False, True))
                occ.setdefault(p, []).append((_apply(p, d), _apply(p, d), True))
                continue
            seen = known.get((lemma, textprep.bare(p)), set())
            m = next(iter(seen)) if len(seen) == 1 else None
            if m is None and textprep.bare(p) == textprep.bare(lemma) and textprep.ACUTE in lemma_st:
                m = lemma_st
            row.append((p, _apply(p, m or gm), len(seen) > 1, False))
            occ.setdefault(p, []).append((_apply(p, m or gm), _apply(p, gm), False))
        marked.append(row)
    certain, cands = {}, {}
    for p, places in occ.items():
        variants = {x for prim, col, res in places for x in ((prim,) if res else (prim, col))}
        if len(places) > 1 and ruaccent is not None and any(not res for _, _, res in places):
            variants.add(_apply(p, ruaccent([p])[0]))         # the form read alone must agree with every slot it is in
        certain[p] = len(places) == 1 or len(variants) == 1
        cands[p] = sorted(variants)
    out = []
    for sl, row in zip(slots, marked):
        bad = [p for p, _, d, res in row if not res and (d or not certain[p])]
        over = form_overrides.find(lemma, sl) if bad and use_overrides else None
        if over:
            out.append((sl, over[0], {"override": over[1]}))
        elif bad:
            out.append((sl, None, {"lemma": lemma, "title": sl.title, "row": sl.row, "column": sl.column, "cell": sl.cell,
                                   "candidates": {p: cands[p] for p in bad}}))
        else:
            out.append((sl, ", ".join(m for _, m, _, _ in row), None))
    return out


def warm_ruaccent(scenes, settings, ruaccent):
    """Everything that will need RuAccent (the Russian table columns, and the lone forms that occur in two slots), in ONE call
    (it starts a model per call)."""
    if ruaccent is None or not settings["stress"]["ruaccentFallback"]:
        return
    need = []
    for (pair, lang, lemma), entry in base_entries(scenes).items():
        if lang != "ru":
            continue
        slots = slots_of(entry)
        by_col, count = {}, {}
        for sl in slots:
            by_col.setdefault((sl.table, sl.col), []).append(sl)
            for p in pieces(sl.cell):
                count[p] = count.get(p, 0) + 1
        for col in by_col.values():
            need.append(", ".join(p for sl in col for p in pieces(sl.cell)))
        need += [p for p, n in count.items() if n > 1 and wants_mark(p)]
    if need:
        ruaccent(need)


def plan(scenes, settings, voices, ruaccent=None):
    """([clips.Item], stats): an item per slot of the lexicon tables the publisher will show (one entry per lemma, see base_entries), or nothing
    for a language without a voice. `settings` are the global ones; the forms ones (LoRA, batch, dictionary) are applied here.
    stats: slots; ambiguous (left without audio, stress not certain); ambiguous_without_dictionary and resolved_by_dictionary (how many of those
    the dictionary settled); review (one dict per slot left without audio: lemma, slot, candidates)."""
    known = stress_map(scenes)
    warm_ruaccent(scenes, settings, ruaccent)
    bases = base_entries(scenes)
    fdict = None
    path = settings["forms"].get("dictionary")
    if path and any(lang == "ru" for _, lang, _ in bases) and Path(path).is_file():
        import form_dict
        fdict = form_dict.FormDict(path, {form_dict.letters(lemma) for (pair, lang, lemma) in bases if lang == "ru"})
    items, seen, russian_ambiguous = [], set(), 0
    stats = {"slots": 0, "ambiguous": 0, "overridden": 0, "ambiguous_without_dictionary": 0, "resolved_by_dictionary": 0, "dictionary": fdict is not None, "review": []}
    for (pair, lang, lemma), entry in bases.items():
        voice = settings["forms"]["voices"].get(lang)
        if not voice:
            continue
        fs = forms_settings(settings, lang)
        form_cfg = {k: v for k, v in settings["forms"].items() if k not in ("gpu", "prio", "batch", "chunk", "dictionary")}
        form_cfg["voices"] = {lang: voice}
        form_cfg["lora"] = fs["lora"]["enabled"]
        # With the original Russian-only settings this is byte-for-byte the old
        # signature; adding a French voice does not invalidate Russian clips.
        asig = config.sha({"forms": form_cfg, "audio": settings["audio"], "version": "f2"})
        ref = voices.ref_version(voice)
        ra = ruaccent if (lang == "ru" and settings["stress"]["ruaccentFallback"]) else None
        if lang == "ru":
            rows = entry_texts(entry, known, ra, fdict, entry.get("pos"))
            stats["overridden"] += sum(1 for _, t, why in rows if t is not None and why)
            stats["ambiguous_without_dictionary"] += sum(1 for _, t, _ in entry_texts(entry, known, ra, None, entry.get("pos"), use_overrides=False) if t is None)
        else:
            rows = []
            for sl in slots_of(entry):
                spoken = spoken_form(lang, sl.cell)
                why = None if spoken else {"lemma": lemma, "title": sl.title, "row": sl.row, "column": sl.column,
                                           "cell": sl.cell, "reason": "written form notation needs review"}
                rows.append((sl, spoken, why))
        for sl, tts, why in rows:
            stats["slots"] += 1
            if tts is None:
                stats["ambiguous"] += 1
                russian_ambiguous += int(lang == "ru")
                stats["review"].append({**why, "pair": pair})
                continue
            fid = form_id(pair, entry["lemma"], sl.title, sl.row, sl.column, sl.cell)
            if fid in seen:
                continue
            seen.add(fid)
            st = textprep.Sentence(0, 0, "form", lang, tts if lang == "fr" else ", ".join(pieces(sl.cell)), tts, gap=0.0)
            st.voice = voice
            st.key = cache_key(fs, voice, ref, lang, tts)
            items.append(clips.Item(fid, pair, lang, sl.cell, voice, [st], config.sha({"sents": [st.key], "assembly": asig})))
    stats["resolved_by_dictionary"] = stats["ambiguous_without_dictionary"] - russian_ambiguous - stats["overridden"]
    return items, stats


def pending(items, store_root):
    cs = clips.ClipStore(store_root, KIND)
    return [it for it in items if not cs.is_done(it)]


# ---- the plan file: what pipeline.py hands to the GPU stage ----------------------------------------------------
def plan_path(store_root) -> Path:
    return Path(store_root) / KIND / ".plan.json"


def write_plan(items, store_root, replace_ids=None):
    clips.ClipStore(store_root, KIND)
    rows = [{"id": i.id, "pair": i.pair, "lang": i.lang, "text": i.text, "voice": i.voice, "ckey": i.ckey, "key": i.sents[0].key,
             "plain": i.sents[0].plain, "tts": i.sents[0].tts} for i in items]
    p = plan_path(store_root)
    if replace_ids is not None and p.exists():
        previous = json.loads(p.read_text("utf-8"))
        if not isinstance(previous, list):
            raise ValueError("existing form plan is not an array")
        rows = [r for r in previous if r["id"] not in replace_ids] + rows
    rows = list({r["id"]: r for r in rows}.values())
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(rows, ensure_ascii=False), "utf-8")
    tmp.replace(p)


def write_review(rows, store_root, scenes, settings):
    """Keep review items for lemmas outside this run's language/word scope."""
    scope = {(pair, lemma) for pair, lang, lemma in base_entries(scenes) if lang in settings["forms"]["voices"]}
    p = Path(store_root) / KIND / "review.jsonl"
    previous = [json.loads(line) for line in p.read_text("utf-8").splitlines() if line.strip()] if p.exists() else []
    kept = [r for r in previous if (r["pair"], r["lemma"]) not in scope]
    tmp = p.with_suffix(".tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in kept + rows), "utf-8")
    tmp.replace(p)


def read_plan(store_root, ids=None):
    want = set(ids) if ids is not None else None
    out = []
    for r in json.loads(plan_path(store_root).read_text("utf-8")):
        if want is not None and r["id"] not in want:
            continue
        st = textprep.Sentence(0, 0, "form", r["lang"], r["plain"], r["tts"], gap=0.0)
        st.voice, st.key = r["voice"], r["key"]
        out.append(clips.Item(r["id"], r["pair"], r["lang"], r["text"], r["voice"], [st], r["ckey"]))
    return out
