"""Narrator lines that contain Russian words: find the Russian runs and their Cyrillic, split the line into English / Russian parts.

Pure Python (no numpy/torch) so the planner and the unit tests run anywhere. The Cyrillic is never guessed: a quoted Latin run counts
as Russian only when EVERY word of it resolves to a Russian word the content already has (the scene's dialogue, notes words and
lexicon; then the episode's; then the show's) by a STRICT transliteration match (я=ya, ь=', ый=yy, ий=iy ...). A loose key is used
only when nothing matches strictly. Several candidates are narrowed by the Russian words of the sentence's own dialogue quote; if
that does not decide, the run is unresolved and the line keeps its old (sky) audio. Stress forms come from the same data and RuAccent
for words with none; see stress_text().
"""
import re
import unicodedata

ACUTE = "́"
CYR = re.compile(r"[А-Яа-яЁё́]+(?:-[А-Яа-яЁё́]+)*")
LAT_WORD = re.compile(r"[A-Za-z]+(?:['\-]+[A-Za-z]+)*'*")
QUOTED = re.compile(r"[\"“”«»]([^\"“”«»]+)[\"“”«»]")

_C2L = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
        "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh",
        "щ": "shch", "ы": "y", "э": "e", "ю": "yu", "я": "ya"}
_VOW = "аеёиоуыэюя"


def strip_marks(s):
    return unicodedata.normalize("NFC", unicodedata.normalize("NFD", s).replace(ACUTE, ""))


def cyr_strict(word):
    """The one strict transliteration of a Cyrillic word: я=ya (never a), ь=', ъ='', ы=y, и=i, ый=yy, ий=iy, е=ye after a vowel / ь / ъ / at the start and e elsewhere, ё=yo, х=kh, щ=shch. Not lossy for the
    pairs that matter (я/а, ь present/absent, ы/и, ий/ы, ё/е apart from the rare е/э)."""
    w = strip_marks(word).lower().replace("-", "")
    out = []
    for i, c in enumerate(w):
        prev = w[i - 1] if i else ""
        nxt = w[i + 1] if i + 1 < len(w) else ""
        if c == "е":
            out.append("ye" if (not prev or prev in _VOW or prev in "ьъ") else "e")
        elif c == "ё":
            out.append("yo")
        elif c == "ь":
            out.append("'")
        elif c == "ъ":
            out.append("''")
        else:
            out.append(_C2L.get(c, ""))
    return "".join(out)


def lat_strict(word):
    """A quoted Latin word brought to cyr_strict's alphabet. Only spellings of the SAME letter are folded (j for y, c/x/w/q). Nothing
    is dropped or merged: a missing soft sign, a plain a for ya, ii for ий all stay different. The
    endings authors write loosely are lat_variants()."""
    w = word.lower().replace("’", "'").replace("ʼ", "'").replace("`", "'").replace("-", "")
    w = re.sub(r"[^a-z']", "", w).lstrip("'")
    w = w.replace("j", "y").replace("x", "ks").replace("w", "v").replace("q", "k")
    w = re.sub(r"c(?![h])", lambda m: "ts" if w[m.end():m.end() + 1] in ("e", "i", "y") else "k", w)
    return w


def lat_variants(word):
    """[lat_strict(word)] + other readings of the endings and clusters authors write loosely, each itself a STRICT form of some word:
    -ii / -yi / -ai.. for -ий / -ый / -ай.., consonant+ye for -ые, -ie for -ие, final consonant+y for -ый / -ий, sch for щ. Used only
    when the first form matches nothing (candidates tier 2, together with soft())."""
    w = lat_strict(word)
    out = []
    if w.endswith("ii"):
        out.append(w[:-1] + "y")                            # -ий
    if w.endswith("yi"):
        out.append(w[:-1] + "y")                            # -ый
    if re.search(r"[aeou]i$", w):
        out.append(w[:-1] + "y")                            # -ой, -ай, -ей, -уй
    if re.search(r"[^aeiouy']ye$", w):
        out.append(w[:-2] + "yye")                          # -ые
    if w.endswith("ie") and len(w) > 3:
        out.append(w[:-2] + "iye")                          # -ие
    if re.search(r"[^aeiouy']y$", w):
        out += [w + "y", w[:-1] + "iy"]                     # -ый, -ий
    if "sch" in w:
        out.append(w.replace("sch", "shch"))                # sch is mostly сч (schyot); щ only when nothing else matches
    return [w] + [x for i, x in enumerate(out) if x not in out[:i] and x != w]


_TOK = re.compile(r"shch|zh|kh|ts|ch|sh|ya|yu|yo|ye|.")


def soft(strict):
    """A strict form with the soft / hard sign marks that sit before a vowel letter dropped (sem'ya = semya, ob''yasni = obyasni): the
    iotated vowel already says it. Used for tier 2 only, on both sides."""
    return re.sub(r"'(?=[aeiouy])", "", strict.replace("''", ""))


TIER3_MIN_LETTERS = 5      # a lone loose-key candidate is taken only for a word this long; shorter ones are too likely a near-homophone ("sir" -> сыр)
TIER3_ALLOW = frozenset({"nyet", "tsar"})      # short words that only the loose key finds (no soft sign before the end, ye/ie), checked by hand


def loose(strict):
    """Second-chance key of a strict form (used only when no strict match exists): ye/yo->e, kh->h, shch->sh, y~i (ы~и, й~и), no
    apostrophes, no doubled letters. ya/yu stay, so a never matches я."""
    out = []
    for t in _TOK.findall(strict):
        if t == "shch":
            t = "sh"
        elif t in ("ye", "yo"):
            t = "e"
        elif t == "kh":
            t = "h"
        elif t == "'":
            continue
        elif t == "y":
            t = "i"
        out.append(t)
    return re.sub(r"(.)\1+", r"\1", "".join(out))


def translit(cyr):
    """What a content author would write for a Cyrillic word (the strict form)."""
    return cyr_strict(cyr)


class Scope:
    """Russian word forms of one scope: forms {lowercase cyrillic: {stressed variants}} and the strict / loose transliteration indexes."""

    def __init__(self):
        self.forms = {}
        self.i1 = {}
        self.i1s = {}
        self.i2 = {}

    def put(self, low, stressed=None):
        if low not in self.forms:
            self.forms[low] = set()
            s = cyr_strict(low)
            self.i1.setdefault(s, set()).add(low)
            self.i1s.setdefault(soft(s), set()).add(low)
            self.i2.setdefault(loose(s), set()).add(low)
        if stressed:
            self.forms[low].add(stressed)


def _yo_dedupe(cands):
    """е/ё spelling variants of one word are one candidate: the ё form wins (it is the more specific one)."""
    best = {}
    for c in sorted(cands):
        k = c.replace("ё", "е")
        if k not in best or "ё" in c:
            best[k] = c
    return sorted(best.values())


class RuVocab:
    """Scopes are consulted narrow to wide. resolve() NEVER picks between forms by stress or length: a strict transliteration match
    first (any scope, narrowest first), the loose key only when there is none; several candidates are narrowed by the Russian words of
    the sentence's own dialogue quote, and still several = ambiguous (the caller leaves that line alone)."""

    def __init__(self):
        self.scopes = []

    def new_scope(self):
        d = Scope()
        self.scopes.append(d)
        return d

    @staticmethod
    def add(scope, surface, stress=None):
        toks = CYR.findall(surface)
        stoks = CYR.findall(stress) if stress else []
        for j, tok in enumerate(toks):
            low = strip_marks(tok).lower()
            st = None
            if ACUTE in tok:
                st = unicodedata.normalize("NFC", tok.lower())
            elif len(stoks) == len(toks) and ACUTE in stoks[j] and strip_marks(stoks[j]).lower() == low:
                st = unicodedata.normalize("NFC", stoks[j].lower())
            scope.put(low, st)

    def candidates(self, latin_word):
        """-> (tier, [cyrillic]); tier 1 exact strict, 2 the same without soft/hard-sign marks before vowels and with the loosely written endings read strictly, 3 loose key, 0 none. The first
        scope with a match decides within a tier."""
        keys = lat_variants(latin_word)
        for sc in self.scopes:                               # tier 1: the exact strict form
            c = sc.i1.get(keys[0])
            if c:
                return 1, _yo_dedupe(c)
        for sc in self.scopes:                               # tier 2: a strict form of a looser-written ending
            c = set()
            for key in keys:
                c |= sc.i1s.get(soft(key), set())
            if c:
                return 2, _yo_dedupe(c)
        for sc in self.scopes:                               # tier 3: the loose key
            c = sc.i2.get(loose(keys[0]))
            if c:
                return 3, _yo_dedupe(c)
        return 0, []

    def stress_of(self, cyr):
        """-> (stressed or None, homograph). One stressed form across all scopes: that one. Several different ones (a homograph, or the
        same spelling in another sense): only a form the narrowest scope that has any is unanimous about, else None (and the caller
        gives RuAccent the sentence)."""
        allv = set()
        per_scope = []
        for sc in self.scopes:
            v = sc.forms.get(cyr)
            if v:
                allv |= v
                per_scope.append(v)
        if not allv:
            return None, False
        if len(allv) == 1:
            return next(iter(allv)), False
        if self.scopes and len(per_scope[0]) == 1 and self.scopes[0].forms.get(cyr) == per_scope[0]:
            return next(iter(per_scope[0])), True
        return None, True

    def resolve(self, latin_word, ctx=frozenset()):
        """_resolve, and for a hyphenated word that is unknown as a whole: its parts, all of which must resolve (po-russki)."""
        r = self._resolve(latin_word, ctx)
        parts = [p for p in latin_word.split("-") if p]
        if r["status"] == "none" and len(parts) > 1:
            rs = [self._resolve(p, ctx) for p in parts]
            if any(x["status"] == "ambiguous" for x in rs):
                return {**r, "status": "ambiguous", "cands": [c for x in rs for c in x["cands"]]}
            if all(x["status"] == "ok" for x in rs):
                return {**r, "status": "ok", "cyr": "-".join(x["cyr"] for x in rs), "stressed": None,
                        "homograph": any(x["homograph"] for x in rs), "via": rs[0]["via"]}
        return r

    def _resolve(self, latin_word, ctx=frozenset()):
        """-> {"status": ok|ambiguous|none, "cyr", "stressed", "homograph", "cands", "tier", "via"}"""
        tier, cands = self.candidates(latin_word)
        res = {"status": "none", "cands": cands, "tier": tier, "cyr": None, "stressed": None, "homograph": False, "via": None}
        pick, via = None, None
        v1 = lat_variants(latin_word)
        s2 = loose(v1[0])
        in_ctx_strict = _yo_dedupe([c for c in ctx if cyr_strict(c) in v1])
        in_ctx_loose = _yo_dedupe([c for c in ctx if loose(cyr_strict(c)) == s2])
        if len(in_ctx_strict) == 1:
            pick, via = in_ctx_strict[0], "dialogue-strict"
        elif not in_ctx_strict and len(in_ctx_loose) == 1:
            pick, via = in_ctx_loose[0], "dialogue-loose"
        elif len(cands) == 1 and (tier in (1, 2) or len(latin_word.replace("'", "")) >= TIER3_MIN_LETTERS or latin_word.lower() in TIER3_ALLOW):
            pick, via = cands[0], "tier%d" % tier
        elif len(cands) == 1:                    # a short word on its loose key alone is no evidence ("sir" -> сыр): it keeps its sky English
            res["rejected"] = cands
        elif len(cands) > 1:
            res.update(status="ambiguous")
            res["cands"] = cands + [c for c in in_ctx_loose if c not in cands]
            return res
        elif in_ctx_loose:
            res.update(status="ambiguous", cands=in_ctx_loose)
            return res
        if pick is None:
            return res
        st, hom = self.stress_of(pick)
        res.update(status="ok", cyr=pick, stressed=st, homograph=hom, via=via)
        return res


def vocab_from_notes(scope, notes, lines_texts=()):
    """Add a scene's notes (words[].t/stress, lexicon lemma/stress/forms/examples) and plain Russian texts to a scope."""
    for l in (notes or {}).get("lines", []):
        if isinstance(l, dict):
            for w in l.get("words") or []:
                RuVocab.add(scope, w.get("t", ""), w.get("stress"))
            RuVocab.add(scope, l.get("text", "") or "")
    for key, e in ((notes or {}).get("lexicon") or {}).items():
        RuVocab.add(scope, key, e.get("stress") if isinstance(e, dict) else None)
        if isinstance(e, dict):
            RuVocab.add(scope, e.get("lemma", ""), e.get("stress"))
            for r in (e.get("forms") or {}).get("rows", []):
                for c in r.get("cells", []):
                    RuVocab.add(scope, c)
            for ex in e.get("examples") or []:
                RuVocab.add(scope, ex.get("text", ""))
            for rel in e.get("related") or []:
                RuVocab.add(scope, rel.get("word", ""))
    for t in lines_texts:
        RuVocab.add(scope, t)


def english_vocab(notes, texts):
    """Words that are English in this scene (translations, glosses, narrator prose outside double quotes): a quoted run made only
    of these is an English gloss (\"no\", \"yes, fine\"), never a transliteration."""
    ws = set()
    for l in (notes or {}).get("lines", []):
        if isinstance(l, dict):
            ws.update(w.lower() for w in re.findall(r"[A-Za-z]+", l.get("trans", "") or ""))
            for w in l.get("words") or []:
                ws.update(x.lower() for x in re.findall(r"[A-Za-z]+", w.get("gloss", "") or ""))
    for key, e in ((notes or {}).get("lexicon") or {}).items():
        if isinstance(e, dict):
            ws.update(x.lower() for x in re.findall(r"[A-Za-z]+", e.get("gloss", "") or ""))
            for m in e.get("meanings") or []:
                ws.update(x.lower() for x in re.findall(r"[A-Za-z]+", m.get("en", "") or ""))
    for t in texts:
        ws.update(x.lower() for x in re.findall(r"[A-Za-z]+", QUOTED.sub(" ", t)))
    return ws


_RU_SPELLING = re.compile(r"'|zh|kh|shch|yy|iy|ya|yu|yo")


def _is_english_piece(w, en_words):
    parts = [p for p in w.lower().split("'") if p]
    return bool(parts) and all(p in en_words for p in parts)


def _window(tokens, words):
    n = len(words)
    for i in range(len(tokens) - n + 1):
        if tokens[i:i + n] == words:
            return i
    return -1


# Morphological fragments the narrator quotes in Latin letters ("-la", "pere-"). Only unambiguous ones are listed: -y (ы or й) and -i
# (и or ь+и) are left out, they resolve from context or stay English. Keys are lat_strict forms.
SUFFIXES = {"sya": "ся", "as'": "ась", "la": "ла", "li": "ли", "lo": "ло", "l": "л", "am": "ам", "ami": "ами", "akh": "ах", "ah": "ах",
            "om": "ом", "omu": "ому", "oy": "ой", "aya": "ая", "oye": "ое", "oe": "ое", "ye": "ые", "eye": "ее", "ite": "ите", "te": "те",
            "ym": "ым", "im": "им", "u": "у", "yu": "ю", "ya": "я", "a": "а", "o": "о", "e": "е", "ov": "ов", "ev": "ев", "ost": "ость",
            "nik": "ник", "to": "то", "che": "че", "she": "ше", "nibud'": "нибудь", "ogo": "ого", "ego": "его", "em": "ем", "emu": "ему",
            "uyu": "ую", "yy": "ый", "iy": "ий", "ey": "ей", "ay": "ай", "ee": "ее", "ie": "ие", "iye": "ие", "yye": "ые", "ymi": "ыми",
            "imi": "ими", "ka": "ка", "ik": "ик", "et": "ет", "ut": "ут", "yom": "ём"}
PREFIXES = {"pere": "пере", "ot": "от", "ni": "ни", "po": "по", "pri": "при", "za": "за", "vy": "вы", "raz": "раз", "pro": "про",
            "do": "до", "na": "на", "pod": "под", "u": "у", "s": "с", "v": "в", "ne": "не", "so": "со"}
INFIXES = {"yva": "ыва"}
# English affixes the narrator quotes the same way ("re-", "-ness"): never read as Russian unless the table lists them
EN_AFFIXES = frozenset({"re", "un", "pre", "dis", "non", "anti", "ly", "ness", "ity", "ing", "ed", "er", "est", "ful", "less", "able", "ish",
                        "form", "ever", "self", "ment", "tion"})
_FRAG_QUOTED = re.compile(r"^(-?)([a-z]{1,8}'?)(-?)$")
_FRAG_BARE = re.compile(r"(?<![\w\"'“”«»-])(-[A-Za-z]{1,8}'?-?|[A-Za-z]{1,8}-)(?![\w-])")


def _fragment(s):
    """'-la' -> ('suffix', 'la'), 'pere-' -> ('prefix', 'pere'), '-yva-' -> ('infix', 'yva'); None for anything else."""
    m = _FRAG_QUOTED.match(s.strip().lower())
    if not m or not (m[1] or m[3]):
        return None
    return ("infix" if m[1] and m[3] else "suffix" if m[1] else "prefix"), m[2]


def _fragment_slices(kind, lat, words):
    """The Cyrillic ending / start of each word whose strict transliteration ends / starts with the fragment at a letter boundary
    (cyr_strict(word[:i]) is a prefix of cyr_strict(word), so the rest of the transliteration says where the fragment begins)."""
    out = []
    for w in words:
        w = strip_marks(w).lower().replace("-", "")
        full = cyr_strict(w)
        if kind == "suffix":
            hit = next((w[i:] for i in range(len(w) - 1, -1, -1) if full[len(cyr_strict(w[:i])):] == lat), None)
        else:
            hit = next((w[:i] for i in range(1, len(w) + 1) if cyr_strict(w[:i]) == lat), None)
        if hit:
            out.append(hit)
    return out


def resolve_fragment(kind, lat, tiers, en_words):
    """-> (cyrillic syllable, via) or None. `tiers` = lists of Cyrillic words, nearest first (the sentence's own runs, the dialogue quote it
    is about, the scene's dialogue). (a) The first tier with a word that ends / starts with the fragment decides: the table's form when
    such a word carries it (-ye is -ые in "красивые", not the -е the letters alone give), else the one slice they agree on.
    (b) The table of common endings and prefixes. A fragment that is an English word or affix is only ever resolved by the table."""
    known = {"suffix": SUFFIXES, "prefix": PREFIXES, "infix": INFIXES}[kind].get(lat)
    if known is None and (kind == "infix" or lat in en_words or lat in EN_AFFIXES):
        return None
    for words in tiers:
        slices = _fragment_slices(kind, lat, words)
        if known and slices and any((strip_marks(w).lower().endswith if kind == "suffix" else strip_marks(w).lower().startswith)(known) for w in words):
            return known, "fragment-context"
        if len(set(slices)) == 1:
            return slices[0], "fragment-context"
        if slices:
            break           # the nearest words disagree: not guessed, the table (if it has the fragment) decides
    return (known, "fragment-table") if known else None


def find_runs(text, vocab, en_words, ctx=(), dialogue=()):
    """-> (runs, unresolved).
    run = {a, b (outer span incl. quotes), inner, words[latin], cyr[plain], stressed[or None], homograph[bool], via[str], context}.
    unresolved = [{inner, kind, words: [{lat, cands}]}] with kind ambiguous | partial (a part of the quote resolves: the caller must
    leave the whole line alone) | unknown (nothing matches: not claimed as Russian, the line is not blocked).
    ctx: Russian words (lowercase) of the dialogue quote this sentence is about. dialogue: Russian sentences, only used to hand RuAccent
    the sentence a run's words occur in. Literal Cyrillic in the text is a run of its own."""
    ctx = frozenset(strip_marks(c).lower() for c in ctx)
    runs, unresolved, frags = [], [], []
    dtoks = [[strip_marks(t).lower() for t in CYR.findall(d)] for d in dialogue]
    for m in QUOTED.finditer(text):
        inner = m.group(1)
        words = LAT_WORD.findall(inner)
        if not words:
            continue
        if inner.strip().startswith("-") or inner.strip().endswith("-"):
            frags.append((m.start(), [(m.end(), inner)]))     # a morphological fragment ("-sya", "pere-"), not a word: resolved below
            continue
        eng = [_is_english_piece(w, en_words) for w in words]
        res = [vocab.resolve(w, ctx) for w in words]
        if all(eng):
            # an English gloss ("no", "yes, fine"), unless every word is a Russian word of this sentence's own dialogue quote or is
            # spelled the way only a transliteration is (a trailing apostrophe as in spat', zh, kh, shch, yy, iy, ya, yu, yo)
            if not all(r["status"] == "ok" and (r["via"].startswith("dialogue") or _RU_SPELLING.search(w.lower())) for w, r in zip(words, res)):
                continue
        elif any(e and r["status"] == "none" for e, r in zip(eng, res)):
            continue          # an English phrase some words of which look Russian ("to shake", "I'm glad"): a gloss, not a run
        ok = [r["status"] == "ok" for r in res]
        if all(ok):
            cyr = [r["cyr"] for r in res]
            context = None
            for d, dt in zip(dialogue, dtoks):
                if _window([c.replace("ё", "е") for c in dt], [c.replace("ё", "е") for c in cyr]) >= 0:
                    context = d
                    break
            runs.append({"a": m.start(), "b": m.end(), "inner": inner, "words": words, "cyr": cyr,
                         "stressed": [r["stressed"] for r in res], "homograph": [r["homograph"] for r in res],
                         "via": [r["via"] for r in res], "context": context, "kind": "latin"})
            continue
        kind = "ambiguous" if any(r["status"] == "ambiguous" for r in res) else ("partial" if any(ok) else "unknown")
        unresolved.append({"inner": inner, "kind": kind, "words": [{"lat": w, "cands": r["cands"]} for w, r in zip(words, res)]})
    for m in re.finditer(r"[А-Яа-яЁё\u0301]+(?:[ ,]+[А-Яа-яЁё\u0301]+)*", text):
        if any(r["a"] <= m.start() < r["b"] for r in runs):
            continue
        ws = CYR.findall(strip_marks(m.group()))
        runs.append({"a": m.start(), "b": m.end(), "inner": m.group(), "words": ws, "cyr": [w.lower() for w in ws],
                     "stressed": [None] * len(ws), "homograph": [False] * len(ws), "via": ["literal"] * len(ws), "context": None,
                     "kind": "cyrillic"})
    quoted = [(m.start(), m.end()) for m in QUOTED.finditer(text)]
    for m in _FRAG_BARE.finditer(text):          # bare fragments ("ends in -la"); one inside a quote is part of an English gloss ("X-ray")
        if not any(a <= m.start() < b for a, b in quoted) and not any(r["a"] <= m.start() < r["b"] for r in runs):
            g = m.group(1)
            frags.append((m.start(), [(m.end(), g)] + ([(m.end() - 1, g[:-1])] if g.endswith("'") else [])))   # -ish' (ишь), else a closing quote
    tiers = [[w for r in runs for w in r["cyr"]], sorted(ctx), [t for dt in dtoks for t in dt]]
    for a, forms in sorted(frags):
        for b, inner in forms:
            f = _fragment(inner)
            got = resolve_fragment(f[0], f[1], tiers, en_words) if f else None
            if got:
                runs.append({"a": a, "b": b, "inner": inner, "words": [inner.strip().strip("-")], "cyr": [got[0]], "stressed": [None],
                             "homograph": [False], "via": [got[1]], "context": None, "kind": "fragment"})
                break
        else:
            f = _fragment(forms[-1][1])
            if f and f[1] not in EN_AFFIXES and f[1] not in en_words:
                unresolved.append({"inner": forms[-1][1], "kind": "fragment", "words": [{"lat": forms[-1][1], "cands": []}]})
    runs.sort(key=lambda r: r["a"])
    return runs, unresolved


def split_parts(text, runs):
    """Parts in order: {"kind": "en"|"ru", "a", "b" (char span of the part's tokens in `text`), "text" (to synthesise), "run"}."""
    parts, pos = [], 0

    def en(a, b):
        raw = text[a:b]
        t = raw.strip().strip("\"“”«»").strip()
        t = re.sub(r"^[,;:\s]+", "", t)
        if re.search(r"[A-Za-z0-9]", t):
            parts.append({"kind": "en", "a": a, "b": b, "text": t})

    for r in runs:
        en(pos, r["a"])
        parts.append({"kind": "ru", "a": r["a"], "b": r["b"], "run": r, "text": " ".join(r["cyr"])})
        pos = r["b"]
    en(pos, len(text))
    return parts


def vowels(w):
    return max(1, len(re.findall(r"[аеёиоуыэюяaeiouy]", w.lower())))


def stress_text(words_cyr, stressed, ruaccent=None, context=None):
    """Stress marks for a Russian run, automatic: (1) the stressed form the content has (notes / lexicon), (2) RuAccent for the
    rest of the multi-syllable words, (3) nothing for monosyllables. With `context` (the dialogue sentence the run occurs in) RuAccent
    reads the whole sentence and the run's words are cut out of its answer; otherwise it reads the run alone. Returns the text with U+0301."""
    out = []
    todo = [i for i, (w, s) in enumerate(zip(words_cyr, stressed)) if not s and vowels(w) > 1 and "ё" not in w]
    marked = {}
    if todo and ruaccent is not None:
        try:
            if context:
                ctoks = CYR.findall(strip_marks(context))
                plain = [t.lower() for t in ctoks]
                at = _window([p.replace("ё", "е") for p in plain], [w.replace("ё", "е") for w in words_cyr])
                res = CYR.findall(ruaccent([context])[0])
                if at >= 0 and len(res) == len(ctoks):
                    cand = res[at:at + len(words_cyr)]
                    marked = {i: cand[i].lower() for i in todo if ACUTE in cand[i] and strip_marks(cand[i]).lower() == words_cyr[i]}
            if not marked:
                res = ruaccent([" ".join(words_cyr)])[0].split()
                if len(res) == len(words_cyr):
                    marked = {i: res[i] for i in todo if ACUTE in res[i] and strip_marks(res[i]).lower() == words_cyr[i]}
        except Exception:
            marked = {}
    for i, (w, s) in enumerate(zip(words_cyr, stressed)):
        out.append(s or marked.get(i) or w)
    return " ".join(out)


def token_parts(text, parts, tokens_with_spans):
    """For each token (start, end) in the sentence text -> index of the part it belongs to (nearest part when in between)."""
    res = []
    for (a, b) in tokens_with_spans:
        mid = (a + b) / 2
        best, bd = 0, 1e9
        for i, p in enumerate(parts):
            d = 0 if p["a"] <= mid < p["b"] else min(abs(mid - p["a"]), abs(mid - p["b"]))
            if d < bd:
                best, bd = i, d
        res.append(best)
    return res
