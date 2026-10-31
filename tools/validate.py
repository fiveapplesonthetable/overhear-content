#!/usr/bin/env python3
"""Validator for Overhear content. Python 3 stdlib only.

  python3 tools/validate.py out/kukhnya/s01e01            # one episode dir
  python3 tools/validate.py out                           # every episode dir under out/
  python3 tools/validate.py --script FILE.json            # one scene script (examples/*/scene.json)
  options: --require-notes  every target-language line must be annotated (final check)
           --strict         warnings count as errors
           --strict-teaching  a scene with < 60% (or < 4) teaching explanations is an error, not a warning
           --metadata-only  validate Learn notes, dictionary and word histories only
           --all            list every error (default: the first 150 and a tally by kind)
Exit 0 = clean, 1 = errors. Warnings (e.g. subtitle gaps) are printed but pass unless --strict.
Checks: spec/*.md describes each rule; FEEDBACK.md "P-1" describes the cast, narrator-name and explanation rules.
"""
import hashlib, json, re, sys, unicodedata
from pathlib import Path

SCHEMA_DIR = Path(__file__).resolve().parents[1] / "spec" / "schema"
SCHEMA_FILES = {"scenes": "scenes.schema.json", "script": "script.schema.json", "notes": "notes.schema.json", "cast": "cast.schema.json", "learn": "learn-article.schema.json", "origins": "word-origins.schema.json", "dictionary": "dictionary.schema.json"}
LENIENT_VERSION = [False]   # --script mode: examples/ predate the schema (and cannot be edited), so schema errors only warn
LEX_SEEN = {}               # lang -> field -> lemma -> {value: scene file}; judged by check_lexicon (one lemma, one entry shape)
LEX_FIELDS = ("pos", "gender", "aspect", "pair", "stress")
ART_SEEN = {}               # md5 of a scene's art -> scenes using it; judged by check_art (one picture per scene)
TEMPLATE_SEEN = {}          # show -> explanation skeleton -> [(where, scene id)]; judged by check_templates (whole show)
PLACEHOLDER_SUMMARY = ("The characters discuss their situation", "ENG ")
FAREWELL = {"ru": re.compile(r"Пока|До свидания|До встречи|До завтра|До скорого|До скорой|Увидимся|Всего (хорошего|доброго)|Счастливо|Хорошего дня|Спокойной ночи|Прощайте|Удачи", re.I),
            "fr": re.compile(r"À bientôt|Au revoir|À demain|À plus|À tout à l'heure|À la prochaine|Salut|Bonne (soirée|journée|nuit)|Bonsoir|Bon courage", re.I),
            "es": re.compile(r"\b(?:Adiós|Hasta (?:luego|pronto|mañana|la próxima)|Nos vemos|Chao|Chau|Buenas (?:noches|tardes))\b", re.I)}
FAREWELL.update({
    "de": re.compile(r"Tschüss|Auf Wiedersehen|Bis (bald|morgen|später)|Schönen Tag", re.I),
    "it": re.compile(r"Arrivederci|A presto|A domani|Ciao|Buona (giornata|serata)", re.I),
    "ja": re.compile(r"さようなら|またね|また明日|また会いましょう|じゃあね"),
    "zh": re.compile(r"再见|明天见|回头见|下次见"),
    "ko": re.compile(r"안녕히 (가세요|계세요)|안녕|또 (봐요|만나요)|다음에 (봐요|만나요)"),
    "ar": re.compile(r"مع السلامة|إلى اللقاء|الى اللقاء|نشوفك|أشوفك|اشوفك"),
})

SCHEMA_ERR_CAP = 8          # per file; the rest is summarised ("and N more")

ROOT = Path(__file__).resolve().parents[1]
SHOWS = {"kukhnya": "ru", "domashniy-arest": "ru", "dix-pour-cent": "fr", "paquita-salas": "es", "die-discounter": "de", "boris": "it", "the-producers": "ko", "the-naked-director": "ja", "behind-the-scenes": "zh", "al-maktab": "ar"}
PAIR = {lang: f"{lang}-en" for lang in ("ru", "fr", "es", "de", "it", "ko", "ja", "zh", "ar")}
CYR = re.compile(r"[Ѐ-ӿ]")
LAT = re.compile(r"[A-Za-z]")
ACUTE = "́"
POS = {"noun", "verb", "adj", "adv", "pron", "prep", "conj", "part", "num", "interj", "det", "phrase", "name"}
MERGE = {None, "prev", "next"}
GAP_WARN = 120.0          # seconds of uncovered subtitle time worth a warning
ENG = set("the a an is are was to of and in it you i that this we he she they for on with as at be have not do".split())


# ---------------------------------------------------------------- JSON Schema (small draft 2020-12 subset)
# Supports exactly what spec/schema/*.json uses: $ref (#/$defs/x), anyOf, enum, const, type (name or list), properties,
# required, additionalProperties (false or schema), propertyNames.pattern, minProperties, items, minItems, maxItems,
# minLength, minimum, maximum, pattern. Other keywords (title, description, $id, $schema, $defs) are annotations.
_TYPES = {"string": str, "boolean": bool, "null": type(None), "object": dict, "array": list}
_SCHEMAS = {}


def load_schema(kind):
    if kind not in _SCHEMAS: _SCHEMAS[kind] = json.loads((SCHEMA_DIR / SCHEMA_FILES[kind]).read_text(encoding="utf-8"))
    return _SCHEMAS[kind]


def _is_type(v, t):
    if t == "integer": return isinstance(v, int) and not isinstance(v, bool)
    if t == "number": return isinstance(v, (int, float)) and not isinstance(v, bool)
    return isinstance(v, _TYPES[t])


def schema_errors(v, sch, root, path="$"):
    """-> list of 'path: message' for the ways v does not match sch."""
    if "$ref" in sch:
        node = root
        for part in sch["$ref"].lstrip("#/").split("/"): node = node[part]
        return schema_errors(v, node, root, path)
    out = []
    if "anyOf" in sch and not any(not schema_errors(v, b, root, path) for b in sch["anyOf"]):
        return [f"{path}: matches none of the allowed shapes"]
    if "const" in sch and v != sch["const"]: out.append(f"{path}: must be {sch['const']!r}, is {v!r}")
    if "enum" in sch and v not in sch["enum"]: out.append(f"{path}: {v!r} not one of {sch['enum']}")
    if "type" in sch:
        ts = sch["type"] if isinstance(sch["type"], list) else [sch["type"]]
        if not any(_is_type(v, t) for t in ts): return out + [f"{path}: must be {'/'.join(ts)}, is {type(v).__name__}"]
    if isinstance(v, str):
        if len(v) < sch.get("minLength", 0): out.append(f"{path}: empty or too short")
        if "pattern" in sch and not re.search(sch["pattern"], v): out.append(f"{path}: {v[:60]!r} does not match {sch['pattern']}")
    if _is_type(v, "number"):
        if "minimum" in sch and v < sch["minimum"]: out.append(f"{path}: {v} below {sch['minimum']}")
        if "maximum" in sch and v > sch["maximum"]: out.append(f"{path}: {v} above {sch['maximum']}")
    if isinstance(v, list):
        if len(v) < sch.get("minItems", 0): out.append(f"{path}: needs at least {sch['minItems']} items, has {len(v)}")
        if len(v) > sch.get("maxItems", 1 << 30): out.append(f"{path}: at most {sch['maxItems']} items, has {len(v)}")
        if "items" in sch:
            for i, x in enumerate(v): out += schema_errors(x, sch["items"], root, f"{path}[{i}]")
    if isinstance(v, dict):
        if len(v) < sch.get("minProperties", 0): out.append(f"{path}: needs at least {sch['minProperties']} keys")
        for k in sch.get("required", []):
            if k not in v: out.append(f"{path}: missing required field {k!r}")
        props, extra = sch.get("properties", {}), sch.get("additionalProperties", True)
        for k, x in v.items():
            if "propertyNames" in sch and not re.search(sch["propertyNames"]["pattern"], k): out.append(f"{path}: key {k!r} has a bad form")
            if k in props: out += schema_errors(x, props[k], root, f"{path}.{k}")
            elif extra is False: out.append(f"{path}: unknown field {k!r} (not in the schema)")
            elif isinstance(extra, dict): out += schema_errors(x, extra, root, f"{path}.{k}")
    return out


def check_schema(d, kind, where, rep):
    """Validate parsed JSON d against spec/schema; errors (capped per file) go to rep. Returns True if clean."""
    sch = load_schema(kind)
    errs = schema_errors(d, sch, sch)
    if LENIENT_VERSION[0]:      # --script mode (examples/): legacy files, schema differences are warnings only
        for e in errs[:SCHEMA_ERR_CAP]: rep.warn(where, f"schema (legacy example): {e}")
        return not errs
    for e in errs[:SCHEMA_ERR_CAP]: rep.err(where, f"schema: {e}")
    if len(errs) > SCHEMA_ERR_CAP: rep.err(where, f"schema: ... and {len(errs) - SCHEMA_ERR_CAP} more schema errors in this file")
    return not errs


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, where, msg): self.errors.append(f"{where}: {msg}")
    def warn(self, where, msg): self.warnings.append(f"{where}: {msg}")


def check_learn(root, rep):
    """learn/<pair>/<id>.json: schema, id = file name, pair = folder, related notes exist, every example is a target-language line of a
    scene under out/ (sceneId <show>-sNNeNN-scene-NN, seg = index into that scene's script segments). Section ids are checked by the publisher
    against the app's config/ui."""
    root = Path(root)
    lang = {pair: target for target, pair in PAIR.items()}
    for pdir in sorted(p for p in (root / "learn").glob("*") if p.is_dir()):
        notes = {}
        for f in sorted(pdir.glob("*.json")):
            try: d = json.loads(f.read_text(encoding="utf-8"))
            except ValueError as e: rep.err(str(f), f"not JSON ({e})"); continue
            if check_schema(d, "learn", str(f), rep): notes[f.stem] = (f, d)
        for name, (f, d) in notes.items():
            if d["id"] != name: rep.err(str(f), f"id {d['id']!r} must equal the file name")
            if d["pair"] != pdir.name: rep.err(str(f), f"pair {d['pair']!r} must equal the folder {pdir.name!r}")
            for r in d["related"]:
                if r == name or r not in notes: rep.err(str(f), f"related {r!r} is not another note of {pdir.name}")
            for ex in d["examples"]:
                m = re.fullmatch(r"([a-z-]+)-(s\d\d)(e\d\d)-scene-(\d\d)", ex["sceneId"])
                sp = root / "out" / m[1] / (m[2] + m[3]) / f"scene-{m[4]}.json" if m else None
                if not sp or not sp.exists(): rep.err(str(f), f"example scene {ex['sceneId']} does not exist"); continue
                segs = json.loads(sp.read_text(encoding="utf-8"))["segments"]
                if ex["seg"] >= len(segs): rep.err(str(f), f"example {ex['sceneId']}#{ex['seg']}: scene has {len(segs)} segments")
                elif segs[ex["seg"]]["v"] == "narrator": rep.err(str(f), f"example {ex['sceneId']}#{ex['seg']} is a narrator line")
                elif SHOWS.get(m[1]) != lang.get(pdir.name): rep.err(str(f), f"example {ex['sceneId']} is not a {pdir.name} show")


def check_metadata(root, rep):
    """Learning notes and independent dictionary/history metadata, without validating unrelated scenes."""
    root = Path(root)
    check_learn(root, rep)
    for folder, kind in (("word-origins", "origins"), ("dictionary", "dictionary")):
        for path in sorted((root / folder).glob("*.json")):
            try:
                doc = json.loads(path.read_text(encoding="utf-8"))
            except ValueError as error:
                rep.err(str(path), f"not JSON ({error})")
                continue
            if not check_schema(doc, kind, str(path), rep):
                continue
            if doc["pair"] != path.stem:
                rep.err(str(path), "pair must equal the file name")
            if kind == "dictionary":
                for key, entry in doc["entries"].items():
                    if key != entry["lemma"].lower():
                        rep.err(str(path), f"dictionary key {key!r} does not match its lemma")


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
        name = {"fr": "French", "es": "Spanish", "de": "German", "it": "Italian", "ja": "Japanese", "zh": "Chinese", "ko": "Korean", "ar": "Arabic"}.get(lang, lang)
        if CYR.search(text): rep.err(where, f"Cyrillic in {name} line: {text[:50]!r}")
        if lang in ("fr", "es") and re.search(r"\s[?!:;]", text): rep.err(where, f"space before ?!:; (write 'là?'): {text[:50]!r}")
        if lang in ("fr", "es", "de", "it") and "’" in text: rep.err(where, "typographic apostrophe, use '")
        if lang in ("fr", "es") and ("«" in text or "»" in text): rep.err(where, "guillemets in a spoken line")

        native = {"ja": r"[\u3040-\u30ff\u3400-\u9fff]", "zh": r"[\u3400-\u9fff]", "ko": r"[\uac00-\ud7a3\u1100-\u11ff]", "ar": r"[\u0620-\u064a\u066e-\u06d3]"}.get(lang)
        if native and not any(re.search(native, ch) and unicodedata.category(ch).startswith("L") and ch not in "ـー" for ch in text):
            rep.err(where, f"{name} line has no native-script letters: {text[:50]!r}")


def check_script(path, lang, rep, expect_id=None, cast=None):
    """cast = {role key: cast.json entry} of the show, or None (--script mode: no cast checks)."""
    w = str(path)
    try: d = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e: return rep.err(w, f"not valid JSON: {e}")
    check_schema(d, "script", w, rep)
    for k in ("id", "pair", "title", "level", "labels", "segments", "source"):
        if k not in d: rep.err(w, f"missing field {k!r}")
    if "segments" not in d: return None
    if expect_id and d.get("id") != expect_id: rep.err(w, f"id should be {expect_id!r}, is {d.get('id')!r}")
    if d.get("pair") != PAIR[lang]: rep.err(w, f"pair should be {PAIR[lang]!r}")
    segs = d["segments"]
    if not isinstance(segs, list) or not all(isinstance(s, dict) and isinstance(s.get("v"), str) for s in segs):
        return rep.err(w, "segments must be a list of {v, t, gap}")
    roles = sorted({s["v"] for s in segs if s["v"] != "narrator"})
    labels = d.get("labels") if isinstance(d.get("labels"), dict) else {}
    check_cast_use(w, roles, labels, cast, rep)
    if len(roles) > 3: rep.err(w, "at most three speaking roles besides the narrator")
    for r in roles:
        if r not in labels and not (cast is None and r in SLOT_KEYS):       # (--script mode: examples/ predate cast.json and labels)
            rep.err(w, f"labels missing display name for role {r!r}")
    if len(segs) < 20: return rep.err(w, "segments missing or too short (a scene has ~60-80)")
    for i, s in enumerate(segs):
        sw = f"{w} segment {i}"
        if not isinstance(s, dict) or not {"v", "t", "gap"} <= set(s): rep.err(sw, "needs v, t, gap"); continue
        if not isinstance(s["t"], str) or not s["t"].strip(): rep.err(sw, "empty text"); continue
        if not isinstance(s["gap"], (int, float)) or not 0 <= s["gap"] <= 3: rep.err(sw, "gap must be 0..3 seconds")
        if ACUTE in s["t"]: rep.err(sw, "stress mark in text (stress belongs only in stress fields)")
        if s["v"] == "narrator":
            if any(x in s["t"] for x in PLACEHOLDER_SUMMARY): rep.err(sw, f"placeholder text leaked into the narration: {s['t'][:60]!r}")
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
        if not FAREWELL[lang].search(segs[-1]["t"]) or len(segs[-1]["t"].split()) > 6:
            rep.err(w, f"last segment must be a short farewell (Пока! / До свидания! / À bientôt!), not a story line: {segs[-1]['t'][:50]!r}")
        if sum(1 for s in segs[j:k] if s["v"] == "narrator") < 3: rep.warn(w, "walk-through (part 3) looks missing")
    check_narration(w, d, cast, rep, getattr(cast, "other", frozenset()))
    check_explanations(w, d, d.get("show") or str(d.get("id", "")).split("-s")[0], cast, rep)
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


# ---------------------------------------------------------------- cast, narrator names, explanations (FEEDBACK.md P-1)
SLOT_KEYS = {"anya", "lea", "lead", "hero", "heroine", "protagonist", "viewpoint", "main", "extra", "narrator"}
_CAST = {}


class Cast(dict):
    """{role key: cast entry}; .other = non-character proper nouns the narration may use (cast.json other_names)."""
    other = frozenset()
_WORDS = []


def cast_names(entry):
    """Single-word name tokens a cast entry allows in English narration ('Viktor Barinov' allows Viktor and Barinov)."""
    return {t for form in entry["en"] for t in re.findall(r"[^\W\d_][\w'’-]*", form)}


def load_cast(showdir, rep):
    """-> {key: entry} from <show>/cast.json, or None when missing/invalid (the error is reported once per file)."""
    f = Path(showdir) / "cast.json"
    if f in _CAST: return _CAST[f]
    out = None
    if not f.is_file():
        rep.err(str(f), "missing cast.json (one entry per character: key, ru, en, gender); see FEEDBACK.md P-1")
    else:
        try: c = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e: c = None; rep.err(str(f), f"not valid JSON: {e}")
        if c is not None:
            sch = load_schema("cast")
            errs = schema_errors(c, sch, sch)
            for e in errs[:SCHEMA_ERR_CAP]: rep.err(str(f), f"schema: {e}")
            if not errs:
                out, seen_ru, seen_en = Cast(), {}, {}
                out.other = frozenset(t for n in c.get("other_names", []) for t in WORD.findall(n))
                if c["show"] != Path(showdir).name: rep.err(str(f), f"show {c['show']!r} does not match the folder")
                for e in c["cast"]:
                    k = e["key"]
                    if k in out: rep.err(str(f), f"key `{k}` listed twice"); continue
                    if k in SLOT_KEYS: rep.err(str(f), f"key `{k}` is a viewpoint/protagonist slot, not a character: use the character's own name (max, barinov, ...)")
                    out[k] = e
                    if e["ru"] in seen_ru: rep.err(str(f), f"`{k}` and `{seen_ru[e['ru']]}` have the same display name {e['ru']!r}: one character = one key")
                    seen_ru.setdefault(e["ru"], k)
                    for t in {t for t in cast_names(e) if t[:1].isupper()} - {"Chef"}:        # the bare title "Chef" is shared by design
                        if t in seen_en and seen_en[t] != k: rep.err(str(f), f"English name {t!r} belongs to both `{seen_en[t]}` and `{k}`")
                        seen_en.setdefault(t, k)
    _CAST[f] = out
    return out


def check_cast_use(w, roles, labels, cast, rep):
    """Every role key is a cast.json key and its label is the cast.json `ru` name."""
    if cast is None: return
    for r in roles:
        if r not in cast:
            rep.err(w, f"role key `{r}` is not in cast.json" + (" (viewpoint slot keys are not allowed; use the character's own name)" if r in SLOT_KEYS else ""))
        elif labels.get(r) is not None and labels[r] != cast[r]["ru"]:
            rep.err(w, f"label for `{r}` is {labels[r]!r}, cast.json says {cast[r]['ru']!r}")
    for r in labels:
        if r not in cast: rep.err(w, f"labels has key `{r}` which is not in cast.json")


def common_words():
    if not _WORDS:
        f = Path(__file__).with_name("narration_words.txt")
        _WORDS.append(set(f.read_text(encoding="utf-8").split()) if f.is_file() else set())
    return _WORDS[0]


GLOSS = re.compile(r"^'(.+?)'(?=\s|$)\s*(.*)$", re.S)
TRANSITION_TAIL = re.compile(r"\s*Now let's listen to the whole.*$|\s*Now let's hear.*$", re.S)
WORD = re.compile(r"[^\W\d_][\w'’-]*", re.U)
NOT_NAMES = {"Japanese", "Italian", "Georgian", "Chinese", "American", "British", "Korean", "Alright", "Season", "Episode", "I", "I'm", "I'll", "I've", "I'd", "Russian", "Russians", "French", "English", "Moscow", "Russia", "France", "Paris", "Claude", "Monet",
             "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Cyrillic", "Mr", "Mrs", "Dr", "OK", "Okay", "Kukhnya"}


def split_gloss(seg_text):
    """'<gloss>' explanation -> (gloss, explanation without a trailing 'Now let's listen...'), or None."""
    m = GLOSS.match(seg_text.strip())
    return (m[1], TRANSITION_TAIL.sub("", m[2]).strip()) if m else None


def explanations(segs):
    """[(segment index, gloss, explanation)]: the narrator segments that follow a spoken line and start with its quoted gloss."""
    out = []
    for i in range(1, len(segs)):
        if segs[i]["v"] == "narrator" and segs[i - 1]["v"] != "narrator" and isinstance(segs[i].get("t"), str):
            g = split_gloss(segs[i]["t"])
            if g: out.append((i, g[0], g[1]))
    return out


def unquote(text):
    """Replace quoted spans ('...' and "...") by Q."""
    return re.sub(r'(?:(?<=\s)|^)\'.*?\'(?=[\s.,;:!?]|$)|"[^"]*"|\u201c[^\u201d]*\u201d', "Q", text)


def strip_possessive(tok): return re.sub(r"['’]s?$", "", tok)


def narration_names(text, known, extra=frozenset()):      # extra: allowed non-character proper nouns (cast.json other_names, show title)
    """Capitalised name-like tokens in narrator text outside quoted glosses: [(token, is_cast_name)].
    A capitalised word counts as a name if it is a cast name, or its lowercase form is not an ordinary English word
    (tools/narration_words.txt, built from the corpus) and it is not in NOT_NAMES / extra."""
    out, initial = [], True
    for m in re.finditer(r"[^\W\d_][\w'’-]*|[.!?:]", unquote(text)):
        if m[0] in ".!?:": initial = True; continue
        t, was_initial, initial = strip_possessive(m[0]), initial, False
        if not t[:1].isupper() or len(t) < 2 or t.isupper() or t in NOT_NAMES or t in extra: continue
        if t in known: out.append((t, True))
        elif t.lower() in common_words(): continue
        elif was_initial and len(t) >= 7 and re.search(r"(ed|ing|ly|ive|ous|ful|ial|ean|ent|ant|ble|ists?|ness|less|ic|al)$", t): continue      # "Huddled", "Yearning": ordinary words that open a sentence
        else: out.append((t, False))
    return out


GRAMMAR_END = (r"nouns?|verbs?|adjectives?|adverbs?|pronouns?|prepositions?|conjunctions?|particles?|participles?|infinitives?|imperatives?|"
               r"tenses?|aspects?|cases?|nominative|genitive|dative|accusative|instrumental|prepositional|locative|vocative|superlative|comparative|"
               r"perfective|imperfective|reflexive|subjunctive|conditional|gerund|clauses?|constructions?|phrases?|forms?|moods?|voice|"
               r"negation|declension|conjugation|predicate|modal|diminutive|possessive|interrogative|exclamation|expression")
GRAMMAR_ENDING = re.compile(rf"\b(?:with|using|via)\b(?:\s+[\w'’-]+){{0,8}}?\s+(?:{GRAMMAR_END})\s*[.!?…]*\s*$", re.I)
GRAMMAR_TERM = re.compile(r"\b(?:nouns?|verbs?|adjectives?|adverbs?|pronouns?|prepositions?|conjunctions?|particles?|participles?|infinitives?|"
                          r"imperatives?|tenses?|aspects?|nominative|genitive|dative|accusative|instrumental|prepositional case|locative|vocative|"
                          r"superlative|comparative|perfective|imperfective|reflexive|subjunctive|conditional|gerund|declension|conjugation|"
                          r"conjugated|declined|grammatical|grammar)\b", re.I)
GRAMMAR_DENSITY_MAX = 0.30      # share of a scene's explanations that may use a grammar term (FEEDBACK.md says about one in five)
GRAMMAR_DENSITY_MIN_N = 4       # scenes with fewer explanations are not judged
SKEL_WORDS = 6                  # words of the normalised explanation that make the skeleton
SKEL_MIN_WORDS = 6              # explanations shorter than this cannot be matched to a template
# TEMPLATE_MAX: a skeleton (first 6 words, quotes -> Q, names -> N, lower-cased) may appear at most this many times in
# one show; every line beyond that is a fill-in-the-blank template. Tuning, measured on Kukhnya on 2026-10-28 (30,298
# explanations of >= 6 words, 4,119 distinct skeletons): 4,014 skeletons occur fewer than 5 times (that is what hand-written
# openings look like: even "He means that ..." / "This is the ..." / "It sounds ..." stay in single digits); 37 skeletons occur
# 100-2,100 times each (the generated templates, ~20,000 lines); 25 sit in between at 16-40 uses (553 lines, all of them
# template variants such as "N uses the informal everyday Q"). The three hand-written gold scenes (s01e02 scene-01..03)
# have 39 explanations and 39 different skeletons. 15 is the first value above the natural cluster that still catches the
# in-between variants; below it (e.g. 5) a show with 1,000+ lines would trip on honest repeats like "He means that ...".
TEMPLATE_MAX = 15


def skeleton(expl, names=frozenset()):
    """Normalised opening of an explanation: Q for quoted spans, N for names, lower-case, first SKEL_WORDS words."""
    text = unquote(expl)
    toks, prev_end = [], True
    for m in re.finditer(r"Q(?![\w'’])|[^\W\d_][\w'’-]*|[.!?…]", text):
        t = m[0]
        if t in ".!?…": prev_end = True; continue
        base = strip_possessive(t)
        if t == "Q": toks.append("Q")
        elif base[:1].isupper() and (not prev_end or base in names or base.lower() not in common_words()): toks.append("N")
        else: toks.append(base.lower())
        prev_end = False
    out = []
    for t in toks:
        if t == "N" and out and out[-1] == "N": continue       # "Chef Barinov" is one N
        out.append(t)
    return " ".join(out[:SKEL_WORDS]), len(out)


def check_narration(w, d, cast, rep, other=frozenset()):
    """Narrator names must match the people who speak; the speaker's grammar must match the cast gender."""
    segs, roles = d["segments"], {s["v"] for s in d["segments"] if s["v"] != "narrator"}
    if cast is None: return
    known = set().union(*(cast_names(e) for e in cast.values())) if cast else set()
    show_words = set(re.findall(r"[A-Za-z]+", str(d.get("show", "")).replace("-", " ").title())) | other
    for i, s in enumerate(segs):
        if s["v"] != "narrator" or not isinstance(s.get("t"), str): continue
        sw = f"{w} segment {i}"
        for tok, is_cast in narration_names(s["t"], known, show_words):
            if not is_cast: rep.err(sw, f"narration names {tok!r}, who is not a character in cast.json (nor an ordinary word); fix the name or add the character")
        prev = segs[i - 1] if i else None
        if prev and prev["v"] != "narrator" and prev["v"] in cast:
            g = split_gloss(s["t"])
            if g:
                first = WORD.search(g[1])
                tok = strip_possessive(first[0]) if first else None
                if tok and tok in known and tok not in cast_names(cast[prev["v"]]):
                    who = [k for k, e in cast.items() if tok in cast_names(e)]
                    rep.err(sw, f"narration says {tok!r} did this but the line was spoken by `{prev['v']}` ({cast[prev['v']]['en'][0]}); {tok!r} is `{who[0]}`")
    # grammar follows gender (heuristic, warning only): a masculine speaker's "я ... -ла" past tense
    for i, s in enumerate(segs):
        e = cast.get(s["v"])
        if e and e["gender"] == "m" and isinstance(s.get("t"), str):
            m = re.search(r"\b[Яя]\s+(?:[^\s.!?…]+\s+){0,2}?(\w+ла)\b(?![-\w])", s["t"])
            if m and m[1].lower() not in FEM_NOUNS: rep.warn(f"{w} segment {i}", f"`{s['v']}` is male but says {m[1]!r} (feminine past tense?): {s['t'][:50]!r}")


FEM_NOUNS = {"школа", "скала", "игла", "стрела", "мгла", "метла", "пила", "мула", "гора", "дыра"}   # "-ла" words that are not past-tense verbs


def check_explanations(w, d, show, cast, rep):
    """P-1 problem 2: no grammar-label endings, no reused templates, little grammar jargon. Fills TEMPLATE_SEEN."""
    segs = d["segments"]
    names = set().union(*(cast_names(e) for e in cast.values())) if cast else set()
    ex = explanations(segs)
    gram = 0
    for i, gloss, expl in ex:
        if GRAMMAR_ENDING.search(unquote(expl)):
            rep.err(f"{w} segment {i}", f"explanation ends with a grammar label ('with/using ... <grammar term>'): ...{expl[-60:]!r}")
        if GRAMMAR_TERM.search(unquote(expl)): gram += 1
        sk, n = skeleton(expl, names)
        if n >= SKEL_MIN_WORDS: TEMPLATE_SEEN.setdefault(show, {}).setdefault(sk, []).append((f"{w} segment {i}", d.get("id")))
    check_teaching(w, ex, show, rep)
    count_phrases(d, show, cast)
    if len(ex) >= GRAMMAR_DENSITY_MIN_N and gram / len(ex) > GRAMMAR_DENSITY_MAX:
        rep.err(w, f"{gram} of {len(ex)} explanations ({100 * gram // len(ex)}%) use grammar terms; at most {int(GRAMMAR_DENSITY_MAX * 100)}% (aim for one in five)")


def check_templates(rep):
    """A skeleton used more than TEMPLATE_MAX times in one show is a fill-in-the-blank template: error on every line using it."""
    for show, sk in sorted(TEMPLATE_SEEN.items()):
        for k, uses in sorted(sk.items()):
            if len(uses) > TEMPLATE_MAX:
                for where, _ in uses:
                    rep.err(where, f"explanation is a reused template ({len(uses)} uses in {show}, max {TEMPLATE_MAX}): skeleton {k!r}")


# ---------------------------------------------------------------- teaching share (FEEDBACK.md P-2)
# An explanation "teaches" when, beyond retelling the plot, it points at the target language: names a word/form/chunk,
# says what it is built from or literally means, compares it with English, or says how to reuse it. Heuristic (regex +
# quoted foreign words), tuned on the hand-written gold scenes (out/kukhnya/s01e02 scene-01..03, examples/) which must
# score high, against plot-only drafts (out/kukhnya/s01e07 scene-05) which must score low.
TEACH = re.compile(
    r"\b(?:the|this|that|its|a|another|one|little|tiny|small|short|same|single|polite|formal|informal|common|everyday|key|plain|simple)\s+(?:(?:russian|french|english)\s+)?(?:words?|chunks?|phrases?|expressions?|idioms?|sentences?|endings?|forms?|verbs?|nouns?|particles?|prefix|suffix|roots?|stems?|diminutives?|slang|nicknames?|surnames?|first names?|contractions?|abbreviations?)\b\s*(?:for|means?|is|are|comes|sounds|works|here|there|in|can|stands|carries|adds|does|changes|literally|from|of)\b"
    r"|\bliterally\b|\bbuilt (?:from|on|out of)\b|\bcomes from\b|\bshort for\b|\bstands for\b|\bderived\b|\bcloser to\b|\bword[- ]for[- ]word\b"
    r"|\b(?:russian|french|russians)\s+(?:happily|simply|often|always|never|usually|typically|also|just|really|does|doesn't|says?|uses?|has|have|keeps?|drops?|adds?|puts?|marks?|likes?|loves?|speakers?|word|words|phrase|phrases|sentences?|grammar|verbs?|nouns?|endings?|can|would|reaches|prefers|treats|splits|doubles|needs?|requires?|lets?|makes?|gives?|turns?|builds?|stresses|rolls)\b"
    r"|\b(?:in|to) (?:russian|french)\b|\bwhere english\b|\bunlike english\b|\bthan english\b|\bin english\b|\benglish (?:says?|uses?|speakers?|has|would|needs?|adds?|drops?|doesn't|lacks?|calls?|prefers?|puts?)\b"
    r"|\b(?:past|present|future) tense\b|\b(?:perfective|imperfective|plural|singular|feminine|masculine|neuter|genitive|dative|accusative|instrumental|nominative|diminutive)\b|\bpronounc|\btransliterat|\bsounds like\b|\bspelled\b|\bstress(?:ed)?\b|\bcognate\b"
    r"|\bswap in\b|\bhandy (?:sentence|phrase|word|way|chunk)\b|\breusable\b|\bre-?use\b|\byou(?:'d| would| can| could)\s+(?:say|shout|use|hear|reach)\b|\bwhat you(?:'d| would) (?:say|shout|use)\b"
    r"|\bmeans? [\"“']|\bcan mean\b|\bboth mean\b|\bdoubles? the\b|\bsurname\b|\bnickname\b|\b(?:tiny|little|small) word\b|\bthe (?:polite|formal|informal) version\b"
    r"|\brather than\b|\bin the (?:russian|french|negative)\b|\b(?:casual|formal|polite|informal) [\"“']?you\b|[\"“']you[\"”']"
    r"|\b(?:one|two|three|first|last|next|same|opposite|extra|special) (?:words?|endings?|forms?)\b|\b(?:command|negative|question|polite|short|plural|casual) forms?\b|\b(?:endings?|nouns?|verbs?|adjectives?|adverbs?)\b"
    r"|\byou(?:'ll| will) (?:hear|see|say|use|notice)\b|\buseful (?:sentences?|phrases?|words?|chunks?)\b|\bin the language\b|\bjoined by\b|\brepeats? the words\b|\b(?:expression|idiom)s?\b|\b(?:polite|formal|informal|casual)(?:,| and) (?:formal |polite |informal |casual )?version\b|\b(?:a|an) (?:\w+ ){0,2}words?\b"
    r"|[\"”]\s+(?:is|are|twice|says it all|lands|sounds|stands)\b|\bthe (?:prize|key|big|small|tiny|little) word\b", re.I)
CYR_OR_ACCENT = re.compile(r"[Ѐ-ӿ]|[à-ÿ]")
TEACH_MIN_SHARE = 0.60          # FEEDBACK.md P-2: at least 60% of a scene's explanations must teach...
TEACH_MIN_N = 4                 # ...in scenes with at least this many explanations (and at least this many must teach)
TEACH_SEEN = {}                 # show -> [teaching, total] over all scenes; summarised by show_summary
STRICT_TEACH = [False]          # --strict-teaching: a scene below the bar is an error instead of a warning


def teaches(expl):
    """True if the explanation says something about the target language (not just plot). See TEACH."""
    if TEACH.search(expl) or CYR_OR_ACCENT.search(expl): return True
    # a quoted transliterated/foreign word, e.g. Kostya's little word "zato": one quoted token that is not ordinary English
    for q in re.findall(r"\"([^\"]+)\"|“([^”]+)”", expl):
        q = "".join(q).strip(" .,!?")
        if q and q.isalpha() and q.lower() not in common_words() and q.lower() not in ENG: return True
    return False


def check_teaching(w, ex, show, rep):
    """Per scene: share of explanations that teach. Warn below 60% (or fewer than 4 teaching lines); error with --strict-teaching."""
    n = len(ex)
    t = sum(1 for _, _, e in ex if teaches(e))
    tot = TEACH_SEEN.setdefault(show, [0, 0])
    tot[0] += t; tot[1] += n
    if n < TEACH_MIN_N: return
    if t < TEACH_MIN_N or t / n < TEACH_MIN_SHARE:
        (rep.err if STRICT_TEACH[0] else rep.warn)(w, f"only {t} of {n} explanations ({100 * t // n}%) teach something about the target language (need at least {int(TEACH_MIN_SHARE * 100)}% and {TEACH_MIN_N}); add the word, what it is built from, or how it differs from English")


# ---------------------------------------------------------------- show-wide repeated phrases (FEEDBACK.md P-2)
PHRASE_N = 4                    # a repeated phrase is 4 or more words...
PHRASE_MAX = 50                 # ...used more than this many times in the explanations (narrator text after each quoted gloss) of one show
PHRASE_SEEN = {}                # show -> {phrase: count}; judged by check_phrases


def narrator_phrases(text, names=frozenset()):
    """Distinct 4-word shingles of explanation text, within a sentence, with quoted spans -> Q and names -> N (the same
    normalisation as skeleton(), so 'Max chooses "x"' and 'Kostya chooses "y"' are the same phrase)."""
    toks, prev_end = [], True
    for m in re.finditer(r"Q(?![\w'’])|[^\W\d_][\w'’-]*|[.!?…]", unquote(text)):
        t = m[0]
        if t in ".!?…": toks.append("."); prev_end = True; continue
        base = strip_possessive(t)
        if t == "Q": toks.append("Q")
        elif base[:1].isupper() and (not prev_end or base in names or base.lower() not in common_words()): toks.append("N")
        else: toks.append(base.lower())
        prev_end = False
    out, run = set(), []
    for t in toks + ["."]:
        if t != ".": run.append(t); continue
        run = [x for i, x in enumerate(run) if not (x == "N" and i and run[i - 1] == "N")]
        for i in range(len(run) - PHRASE_N + 1):
            g = run[i:i + PHRASE_N]
            if g.count("N") + g.count("Q") <= 1: out.add(" ".join(g))      # skip phrases that are mostly placeholders
        run = []
    return out


def count_phrases(d, show, cast):
    names = set().union(*(cast_names(e) for e in cast.values())) if cast else set()
    seen = PHRASE_SEEN.setdefault(show, {})
    for _, _, expl in explanations(d["segments"]):      # the part-3 explanations only: the mandated scaffolding (transitions, closing line) repeats by design
        for ph in narrator_phrases(expl, names): seen[ph] = seen.get(ph, 0) + 1


def check_phrases(rep):
    """A 4+ word phrase in narrator text used more than PHRASE_MAX times in one show is an error (one error per phrase)."""
    for show, seen in sorted(PHRASE_SEEN.items()):
        for ph, n in sorted(seen.items(), key=lambda kv: -kv[1]):
            if n > PHRASE_MAX: rep.err(show, f"narrator phrase repeated {n} times in the show (max {PHRASE_MAX}): {ph!r}")


def show_summary():
    """One line per show: teaching share and the most repeated narrator phrases."""
    lines = []
    for show in sorted(set(TEACH_SEEN) | set(PHRASE_SEEN)):
        t, n = TEACH_SEEN.get(show, [0, 0])
        top = sorted(PHRASE_SEEN.get(show, {}).items(), key=lambda kv: -kv[1])[:3]
        lines.append(f"SHOW {show}: word-teaching: {100 * t // n if n else 0}% ({t}/{n} explanations); top repeated phrases: "
                     + (", ".join(f"{ph!r} x{c}" for ph, c in top) or "none"))
    return lines


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
        if re.search(r"[\s/\[\]]", st) or re.search(r"[A-Z]", st) or ACUTE in st: rep.err(where, f"{lang} stress must be bare IPA: {st!r}")
        if re.search(r"[éèêàùçôîï]" if lang == "fr" else r"[áéíóúñü]", st):
            rep.err(where, f"{lang} stress holds spelling letters, not IPA: {st!r}")


def check_notes(path, script, lang, require, rep):
    w = str(path)
    try: n = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e: return rep.err(w, f"not valid JSON: {e}")
    check_schema(n, "notes", w, rep)
    if n.get("id") not in (None, script.get("id")): rep.err(w, f"id {n.get('id')!r} must equal the script id {script.get('id')!r}")
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
        toks = [x for x in text.split() if re.search(r"\w", x)]       # bare dashes ("—") need no entry
        if segs[i]["v"] != "narrator" and [wd.get("t") for wd in e.get("words", [])] != toks:
            rep.err(lw, f"words must be the line's whitespace-separated tokens, one entry each, none merged or split ({len(toks)} in text, {len(e.get('words', []))} annotated): {text[:40]!r}")
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
            if wd.get("pos") != "name" and not wd.get("stress") and (
                    lang in ("fr", "es") or (len(re.findall("[аеёиоуыэюя]", t.lower())) > 1 and "ё" not in t.lower())):
                rep.err(lw, f"word {t!r} needs a stress value ({'IPA' if lang in ('fr', 'es') else 'U+0301 mark; null only for one-vowel words or ё'})")
            if lang == "es": check_stress(lang, t, wd.get("stress"), lw, rep)
            if lang == "ru" and wd.get("stress") and len(re.findall("[аеёиоуыэюя]", wd["stress"].lower())) > 1 and ACUTE not in wd["stress"] and "ё" not in wd["stress"]:
                rep.err(lw, f"stress {wd['stress']!r} lacks the U+0301 mark")
    for lemma, L in lex.items():
        lw = f"{w} lexicon[{lemma}]"
        for f in ("lemma", "pos", "gloss", "meanings"):
            if not L.get(f): rep.err(lw, f"missing {f}")
        if L.get("lemma") != lemma: rep.err(lw, "key must equal lemma")
        check_stress(lang, lemma, L.get("stress"), lw, rep)
        if lemma != lemma.lower() and L.get("pos") != "name": rep.err(lw, "lexicon key/lemma must be lowercase")
        if lang == "ru" and L.get("stress") and len(re.findall("[аеёиоуыэюя]", lemma)) > 1 and "ё" not in lemma and ACUTE not in L["stress"]:
            rep.err(lw, f"stress {L['stress']!r} lacks the U+0301 mark")
        for f in LEX_FIELDS:
            LEX_SEEN.setdefault(lang, {}).setdefault(f, {}).setdefault(lemma, {}).setdefault(json.dumps(L.get(f), ensure_ascii=False), w)
        for t in [L.get("forms")] * bool(L.get("forms")) + list(L.get("moreForms") or []): table_ok(t, lw, rep)
        if L.get("pos") in ("noun", "adj", "verb") and not L.get("forms") and lang in ("ru", "es"):
            rep.err(lw, f"{lang} noun/adj/verb needs a forms table")
        for m in L.get("meanings", []):
            if not m.get("en"): rep.err(lw, "meaning needs 'en'")
    if require:
        for i, s in enumerate(segs):
            if s["v"] != "narrator" and i not in done: rep.err(w, f"target line {i} not annotated: {s['t'][:40]!r}")


# ---------------------------------------------------------------- art and characters
def webp_size(path):
    """(width, height) of a lossy/lossless/extended WebP, or None if the file is not a readable WebP."""
    b = Path(path).read_bytes()[:40]
    if len(b) < 30 or b[:4] != b"RIFF" or b[8:12] != b"WEBP": return None
    k = b[12:16]
    if k == b"VP8 ": return (int.from_bytes(b[26:28], "little") & 0x3FFF, int.from_bytes(b[28:30], "little") & 0x3FFF)
    if k == b"VP8L":
        bits = int.from_bytes(b[21:25], "little")
        return ((bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1)
    if k == b"VP8X": return (int.from_bytes(b[24:27], "little") + 1, int.from_bytes(b[27:30], "little") + 1)
    return None


def check_art(rep):
    """Every scene gets its own picture: byte-identical art in two scenes is an error."""
    dup = [v for v in ART_SEEN.values() if len(v) > 1]
    if dup: rep.errors.insert(0, f"art: {len(dup)} pictures are used by more than one scene ({sum(map(len, dup))} scenes); e.g. {' = '.join(dup[0])}")


def check_lexicon(rep):
    """The same lemma must carry the same pos/gender/aspect/pair/stress in every scene's lexicon."""
    for lang, fields in sorted(LEX_SEEN.items()):
        for f, lemmas in fields.items():
            bad = {k: v for k, v in lemmas.items() if len(v) > 1}
            if bad:
                ex = "; ".join(f"{k}: {' vs '.join(vals)}" for k, vals in sorted(bad.items())[:4])
                rep.errors.insert(0, f"lexicon ({lang}): {len(bad)} lemmas have conflicting {f} across scenes; e.g. {ex}")


def source_coverage(sc, cue, source_file, where, rep):
    """Return the declared source scope; missing coverage retains whole-episode policy."""
    coverage = sc.get("coverage")
    if coverage is None:
        return cue, None
    if not isinstance(coverage, dict) or coverage.get("type") != "excerpt":
        rep.err(where, "coverage must declare an explicit excerpt")
        return cue, None
    try:
        for edge in (coverage["start"], coverage["end"]):
            if not isinstance(edge, str) or not re.fullmatch(r"\d{2}:[0-5]\d:[0-5]\d,\d{3}", edge): raise ValueError()
        start, end = ts(coverage["start"]), ts(coverage["end"])
        if not 0 <= start < end: raise ValueError()
    except (KeyError, TypeError, ValueError):
        rep.err(where, "excerpt start/end must be valid increasing nonnegative timestamps")
        return cue, None
    if not source_file.is_file() or hashlib.sha256(source_file.read_bytes()).hexdigest() != coverage.get("sourceSha256"):
        rep.err(where, "excerpt sourceSha256 must match the complete retained source subtitle bytes")
    # Any overlapping cue belongs to the scope; cutting a cue at either edge is rejected.
    selected = {n: c for n, c in cue.items() if c[0] < end and c[1] > start}
    if not selected:
        rep.err(where, "excerpt contains no source subtitle cues")
    if any(c[0] < start - .001 or c[1] > end + .001 for c in selected.values()):
        rep.err(where, "excerpt bounds cut through a source subtitle cue")
    for scene in sc.get("scenes", []):
        try:
            a, b = ts(scene["start"]), ts(scene["end"])
            if a < start - .001 or b > end + .001:
                rep.err(where, "scene extends outside the declared excerpt")
        except (KeyError, TypeError, ValueError): pass  # ordinary scene checks report this
    return selected, (start, end)


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
    check_schema(sc, "scenes", w, rep)
    scenes = sc.get("scenes")
    if not scenes: return rep.err(w, "no scenes")
    srt = ROOT / "sources" / show / f"s{sn}" / f"e{en}.{lang}.dual.srt"
    if not srt.is_file(): srt = srt.with_name(f"e{en}.{lang}.srt")      # Russian-only Whisper transcript (no English)
    cue = parse_srt(srt) if srt.is_file() else {}
    if not cue: rep.err(w, f"source subtitles missing: {srt.relative_to(ROOT)}")
    scoped_cue, excerpt_bounds = source_coverage(sc, cue, srt, w, rep)
    cast = load_cast(epdir.parent, rep)
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
        if str(s.get("summary", "")).startswith(PLACEHOLDER_SUMMARY): rep.err(sw, f"placeholder summary, write what happens: {s['summary'][:50]!r}")
        if s.get("merge") is None:
            n = f"{k:02d}"
            sp = epdir / f"scene-{n}.json"
            if not sp.is_file(): rep.err(sw, f"missing scene-{n}.json")
            else:
                d = check_script(sp, lang, rep, expect_id=f"{show}-s{sn}e{en}-scene-{n}", cast=cast)
                if d is not None:
                    # A transition explicitly folded into this lesson contributes its
                    # own source range (spec/scenes-format.md), without changing the
                    # underlying, non-overlapping scene boundaries.
                    source_scenes = [s]
                    left, right = k - 2, k
                    while left >= 0 and scenes[left].get("merge") == "next":
                        source_scenes.append(scenes[left]); left -= 1
                    while right < len(scenes) and scenes[right].get("merge") == "prev":
                        source_scenes.append(scenes[right]); right += 1
                    source_ranges = []
                    for source_scene in source_scenes:
                        try: source_ranges.append((ts(source_scene["start"]), ts(source_scene["end"])))
                        except (KeyError, TypeError, ValueError): pass  # reported by the scene checks
                    out = [ln.get("cue") for ln in d["source"].get("lines", []) if ln.get("cue") in cue and not any(start - 2 <= cue[ln["cue"]][0] <= end + 2 for start, end in source_ranges)]
                    if out: rep.err(sw, f"{len(out)} source cues lie outside this lesson's scene and merged source ranges (first: cue {out[0]}); tie lines only to cues of the scene or its merged transitions")
                    if excerpt_bounds:
                        if (ROOT / d["source"].get("file", "")).resolve() != srt.resolve():
                            rep.err(sw, "excerpt script source.file must match its hashed coverage subtitle file")
                        outside_scope = [ln.get("cue") for ln in d["source"].get("lines", []) if ln.get("cue") not in scoped_cue]
                        if outside_scope: rep.err(sw, f"source cues lie outside the declared excerpt: {outside_scope[:5]}")
                    notes = epdir / f"scene-{n}.notes.json"
                    if notes.is_file(): check_notes(notes, d, lang, REQ[0], rep)
                    elif REQ[0]: rep.err(sw, f"missing scene-{n}.notes.json")
            if not any((epdir / f"scene-{n}.{x}").is_file() for x in ("webp", "png")):
                rep.err(sw, f"missing art scene-{n}.webp (or .png)")
            elif (epdir / f"scene-{n}.webp").is_file():
                size = webp_size(epdir / f"scene-{n}.webp")
                if size != (1024, 1024): rep.err(sw, f"scene-{n}.webp must be a 1024x1024 webp, is {size}")
                ART_SEEN.setdefault(hashlib.md5((epdir / f"scene-{n}.webp").read_bytes()).hexdigest(), []).append(f"{show}/{epdir.name}/scene-{n}")
    # Every cue in the declared scope must be covered. Default is still the whole episode.
    if scoped_cue:
        spans = [s["_t"] for s in scenes if "_t" in s]
        miss = [(n, c) for n, c in sorted(scoped_cue.items()) if not any(a - 0.5 <= c[0] <= b + 0.5 for a, b in spans)]
        if miss:
            rep.err(w, f"{len(miss)} subtitle cues fall outside every scene (first: cue {miss[0][0]} at {fmt(miss[0][1][0])}); scenes must cover the {'declared excerpt' if excerpt_bounds else 'whole episode'}")
        last = max(c[1] for c in scoped_cue.values())
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
LIST_CAP = 150          # errors listed in full; beyond that a tally by kind


def main(argv):
    REQ[0] = "--require-notes" in argv
    TEMPLATE_SEEN.clear(); TEACH_SEEN.clear(); PHRASE_SEEN.clear(); STRICT_TEACH[0] = "--strict-teaching" in argv; LEX_SEEN.clear(); ART_SEEN.clear()
    strict = "--strict" in argv
    show_all = "--all" in argv
    LENIENT_VERSION[0] = "--script" in argv
    args = [a for a in argv if not a.startswith("--")]
    rep = Report()
    if "--metadata-only" in argv:
        root = Path(args[0] if args else ".").resolve()
        check_metadata(root.parent if root.name == "out" else root, rep)
        for error in rep.errors: print("ERROR", error)
        print(f"{'FAIL' if rep.errors else 'OK'}: {len(rep.errors)} errors")
        return 1 if rep.errors else 0
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
    check_templates(rep)
    check_phrases(rep)
    check_lexicon(rep)
    check_art(rep)
    if "--script" not in argv and base.name == "out": check_metadata(base.parent, rep)
    for x in rep.warnings[:LIST_CAP]: print("WARN ", x)
    if len(rep.warnings) > LIST_CAP: print(f"... {len(rep.warnings) - LIST_CAP} more warnings")
    for x in rep.errors[:None if show_all else LIST_CAP]: print("ERROR", x)
    if len(rep.errors) > LIST_CAP and not show_all:
        tally = {}
        for x in rep.errors:
            k = re.sub(r"\d+", "N", x.split(": ", 1)[-1])[:60]
            tally[k] = tally.get(k, 0) + 1
        print(f"... {len(rep.errors) - LIST_CAP} more errors; by kind:")
        for k, n in sorted(tally.items(), key=lambda kv: -kv[1])[:20]: print(f"  {n:6d}  {k}")
    for x in show_summary(): print(x)
    bad = rep.errors or (strict and rep.warnings)
    print(f"{'FAIL' if bad else 'OK'}: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
