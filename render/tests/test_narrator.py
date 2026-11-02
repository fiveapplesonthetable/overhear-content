"""Narrator method B: Russian-run detection (never guessed Cyrillic), strict transliteration, stress, parts, timing from part offsets,
clean splices, locks, and the build end to end on a synthetic scene.

Pure tests run with system python; the audio / build tests need numpy + soundfile + scipy + ffmpeg (tests/run_all.sh runs this file
again in the Qwen venv)."""
import ast
import json
import os
import random
import re
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path
from types import SimpleNamespace

import pytest

import config
import narrator
import narrator_ru as N
import narrator_work as W
from store import flock_ctx

HERE = Path(__file__).resolve().parents[1]


def vocab(*words):
    sc = N.Scope()
    for w in words:
        if isinstance(w, tuple):
            N.RuVocab.add(sc, w[0], w[1])
        else:
            N.RuVocab.add(sc, w)
    v = N.RuVocab()
    v.scopes = [sc]
    return v


V = vocab(("спасибо", "спаси́бо"), "за", ("кофе", "ко́фе"), "да", "ладно", "нет", "спаси", "бог", "спасаешь", "но", "ты", "вы")
EN = {"yes", "fine", "no", "the", "coffee", "girl", "for", "thanks", "someone"}

# the review's wrong-word examples: every one has the near-homophone in the vocabulary too
CONFUSABLE = ["готовить", "готовит", "есть", "ест", "спать", "спят", "чистый", "чисти", "сыр", "сир", "иметь", "имеет", "быть", "бить",
              "другу", "другую", "а", "я", "лучший", "настоящий", "свежий", "великий", "мелкий", "семья", "гостья", "гостя", "ем", "ему",
              "мой", "мои", "русский", "красные", "большие", "белье", "объяснить", "съесть", "счёт", "щи", "хорошо", "царь", "чай"]
VC = vocab(*CONFUSABLE)


# ---- strict transliteration ------------------------------------------------------------------------------------------
@pytest.mark.parametrize("lat,cyr", [("gotovit'", "готовить"), ("gotovit", "готовит"), ("yest'", "есть"), ("yest", "ест"),
                                      ("spat'", "спать"), ("spyat", "спят"), ("chistyy", "чистый"), ("chisti", "чисти"), ("syr", "сыр"),
                                      ("sir", "сир"), ("imet'", "иметь"), ("imeyet", "имеет"), ("byt'", "быть"), ("bit'", "бить"),
                                      ("drugu", "другу"), ("druguyu", "другую"), ("a", "а"), ("ya", "я"), ("luchshiy", "лучший"),
                                      ("nastoyashchiy", "настоящий"), ("svezhiy", "свежий"), ("velikiy", "великий"), ("melkiy", "мелкий"),
                                      ("sem'ya", "семья"), ("gost'ya", "гостья"), ("gostya", "гостя"), ("moy", "мой"), ("moi", "мои"),
                                      ("russkiy", "русский"), ("krasnyye", "красные"), ("bolshiye", "большие"), ("ob''yasnit'", "объяснить"),
                                      ("s''yest'", "съесть"), ("schyot", "счёт"), ("shchi", "щи"), ("khorosho", "хорошо"), ("tsar'", "царь")])
def test_the_review_examples_resolve_to_the_exact_word(lat, cyr):
    r = VC.resolve(lat)
    if r["tier"] == 3 and len(lat.replace("'", "")) < N.TIER3_MIN_LETTERS and lat not in N.TIER3_ALLOW:   # a short lone loose-key match keeps its sky English
        assert r["status"] == "none" and r["cands"] == [cyr] and r["rejected"] == [cyr], (lat, r)
        return
    assert r["status"] == "ok" and r["cyr"] == cyr, (lat, r)
    assert r["tier"] == 1 or lat in ("moy", "krasnyye", "bolshiye", "sem'ya"), (lat, r)


def test_a_is_never_ya_and_ya_never_a():
    assert VC.resolve("a")["cyr"] == "а" and VC.resolve("ya")["cyr"] == "я"
    assert VC.resolve("A")["cyr"] == "а"
    only_ya = vocab("я")
    assert only_ya.resolve("a")["status"] == "none"          # not even as a second choice
    only_a = vocab("а")
    assert only_a.resolve("ya")["status"] == "none"


def test_missing_soft_sign_is_not_silently_the_other_word():
    only = vocab("готовит", "ест")
    assert only.resolve("gotovit'")["status"] == "ok"         # only the loose key knows it, and it is the only candidate
    both = vocab("готовит", "готовить")
    assert both.resolve("gotovit")["cyr"] == "готовит" and both.resolve("gotovit'")["cyr"] == "готовить"


def test_ambiguity_is_unresolved_never_guessed_by_stress_or_length():
    v = vocab(("умеет", "уме́ет"), "уметь")
    r = v.resolve("umet")
    assert r["status"] == "ambiguous" and set(r["cands"]) == {"умеет", "уметь"}      # the old code took the stressed / shortest one
    # the sentence's own dialogue quote decides
    assert v.resolve("umet", {"уметь"})["cyr"] == "уметь"
    assert v.resolve("umet", {"умеет"})["cyr"] == "умеет"
    assert v.resolve("umet", {"что"})["status"] == "ambiguous"


def test_dialogue_quote_beats_a_homophone_of_the_show_vocabulary():
    v = vocab("сыр", "сир")
    assert v.resolve("sir")["cyr"] == "сир" and v.resolve("syr")["cyr"] == "сыр"      # strict
    only_syr = vocab("сыр")
    r = only_syr.resolve("sir")                                  # loose, unique, but only 3 letters: too likely a near-homophone, sky English stays
    assert r["status"] == "none" and r["rejected"] == ["сыр"]
    assert vocab("чистый").resolve("chistiy")["cyr"] == "чистый"      # the same kind of match on a longer word is taken
    assert v.resolve("sir", {"сыр"})["cyr"] == "сыр"             # the dialogue says сыр


def test_every_vocab_entry_resolves_back_to_itself():
    """Round trip: the transliteration of an entry must resolve to that entry (a homophone with the same strict key is ambiguous, never
    another word). First on the fixture, then on every form of the real Kukhnya notes when the content checkout is there."""
    for w in CONFUSABLE:
        r = VC.resolve(N.translit(w))
        assert r["status"] == "ok" and r["cyr"] == w, (w, N.translit(w), r)
    cd = Path(config.CONTENT_DIR)
    if not (cd / "out" / "kukhnya").exists():
        cd = Path(os.environ.get("OVERHEAR_CONTENT", "/nonexistent"))
    if not (cd / "out" / "kukhnya").exists():
        pytest.skip("no content checkout")
    sc = narrator.Vocabs(cd, "/nonexistent").show("kukhnya")
    v = N.RuVocab()
    v.scopes = [sc]
    clash = 0
    for w in sc.forms:
        r = v.resolve(N.translit(w))
        if r["status"] == "ok":
            assert r["cyr"].replace("ё", "е") == w.replace("ё", "е"), (w, r)      # never a DIFFERENT word
        else:
            assert r["status"] == "ambiguous" and w in r["cands"], (w, r)
            clash += 1
    assert clash < 0.001 * len(sc.forms) + 5        # genuine homographs only (мер / мэр, па-пам / папам)


def test_ending_variants_authors_write_loosely():
    v = vocab("верные", "вернее", "русский", "красный", "мой", "большие", "вышли")
    assert v.resolve("vernye")["cyr"] == "верные"             # not вернее
    assert v.resolve("russkii")["cyr"] == "русский" and v.resolve("krasny")["cyr"] == "красный"
    assert v.resolve("moi")["cyr"] == "мой" and v.resolve("bolshie")["cyr"] == "большие"
    assert v.resolve("Vyshli")["cyr"] == "вышли"


def test_hyphenated_and_cluster_spellings():
    v = vocab("что-нибудь", "по", "русски", "считаю")
    assert v.resolve("Chto-nibud'")["cyr"] == "что-нибудь"
    assert v.resolve("po-russki")["cyr"] == "по-русски"       # parts, when the whole is unknown
    assert v.resolve("schitayu")["cyr"] == "считаю"            # sch is сч, not щ


def test_translit_keys_match_across_schemes():
    for lat, cyr in [("spasibo", "спасибо"), ("spasayesh'", "спасаешь"), ("Bog", "Бог"), ("chai", "чай"),
                     ("zdravstvuyte", "здравствуйте"), ("khorosho", "хорошо"), ("moi", "мой"), ("tsar", "царь")]:
        r = vocab(cyr).resolve(lat)
        assert r["status"] == "ok" and r["cyr"] == cyr.lower(), lat


# ---- finding runs ----------------------------------------------------------------------------------------------------
def test_runs_come_from_known_words_only():
    t = "'Yes, thank you for your help.' \"Spasibo za\" is a frame you can reuse: \"spasibo\", then \"za\", \"for\", then whatever."
    runs, unres = N.find_runs(t, V, EN)
    assert [" ".join(r["cyr"]) for r in runs] == ["спасибо за", "спасибо", "за"]
    assert runs[0]["stressed"][0] == "спаси́бо"          # stress straight from the content
    assert unres == []
    runs, unres = N.find_runs('Say "blorp" now.', V, EN)    # a word the content does not know is never guessed
    assert runs == [] and [(u["inner"], u["kind"]) for u in unres] == [("blorp", "unknown")]


def test_english_glosses_are_not_russian():
    runs, _ = N.find_runs('The first is "no", and "yes, fine" is a gloss.', V, EN)    # "no" collides with но
    assert runs == []
    runs, _ = N.find_runs('The two "nyet" words do different jobs.', vocab("нет"), EN)
    assert [r["cyr"] for r in runs] == [["нет"]]


def test_single_word_a_no_on_are_russian_when_the_dialogue_says_so():
    v = vocab("а", "но", "он", "ты")
    en = {"a", "no", "on", "the", "but"}
    t = 'The line starts with "a" and "ty" follows.'
    runs, _ = N.find_runs(t, v, en)
    assert [r["cyr"] for r in runs] == [["ты"]]                       # "a" alone: an English article
    runs, _ = N.find_runs(t, v, en, ctx={"а", "ты"})
    assert [r["cyr"] for r in runs] == [["а"], ["ты"]]               # the quoted dialogue has а
    runs, _ = N.find_runs('Then "no" is a gloss.', v, en, ctx={"ты"})
    assert runs == []


def test_a_ty_is_checked_per_word_not_through_the_lossy_key():
    v = vocab("а", "ты", "я")
    runs, _ = N.find_runs('She says "A ty" back.', v, set())
    assert [r["cyr"] for r in runs] == [["а", "ты"]]                  # the old key made it "я ты"


def test_english_phrases_with_russian_looking_words_are_left_alone():
    v = vocab("то", "и", "он", "год", "ты")
    runs, unres = N.find_runs('It is "to shake", "I\'m glad" and "oh, come on".', v, {"shake", "glad", "oh", "come"})
    assert runs == [] and not [u for u in unres if u["kind"] in ("ambiguous", "partial")]


def frags(t, ctx=(), dialogue=(), en=frozenset({"the", "is", "a", "to", "and", "in", "an", "am", "re", "ever", "form"}), v=None):
    runs, unres = N.find_runs(t, v or vocab("ся"), en, ctx, dialogue)
    return [(r["inner"], r["cyr"][0], r["via"][0]) for r in runs if r["kind"] == "fragment"], unres


@pytest.mark.parametrize("text,inner,cyr", [
    ('ends in "-la" because Elena is a woman', "-la", "ла"),
    ('is "pere-", over, plus', "pere-", "пере"),
    ('is a plural in "-a", like', "-a", "а"),
    ('the "-eye" is the same one as in "faster"', "-eye", "ее"),
    ('starts with "ot-", away', "ot-", "от"),
    ('both begin with "ni-"', "ni-", "ни"),
    ('"-am" means "to" when it\'s a group', "-am", "ам"),
    ("end in -oye to match", "-oye", "ое"),
    ('ends in "-ite", the polite form', "-ite", "ите"),
    ("gets an -e after", "-e", "е"),
    ("add an -a.", "-a", "а"),
    ("It ends in \"-as'\" because", "-as'", "ась"),
    ("ends in -l because Max is a man.", "-l", "л"),
    ("and in -la for a woman, so you can tell", "-la", "ла"),
    ('the "-sya" family', "-sya", "ся"),
    ("taking -om, as parts of the day often do.", "-om", "ом"),
    ('with "po-" in front to make it', "po-", "по"),
    ('plus "-to", which turns it into "someone".', "-to", "то"),
    ('stretched out with "-yva-" in the middle', "-yva-", "ыва"),
    ("add \"-nibud'\" to \"what\"", "-nibud'", "нибудь"),
    ("The \"-ym\" ending", "-ym", "ым"),
])
def test_endings_and_prefixes_become_russian_runs(text, inner, cyr):
    got, unres = frags(text)
    assert [(i, c) for i, c, _ in got] == [(inner, cyr)] and got[0][2] == "fragment-table" and not [u for u in unres if u["kind"] == "fragment"]


def test_fragment_parts_keep_the_english_around_the_syllable():
    for t, want in [('ends in "-la" because Elena is a woman', [("en", "ends in"), ("ru", "ла"), ("en", "because Elena is a woman")]),
                    ('is "pere-", over, plus', [("en", "is"), ("ru", "пере"), ("en", "over, plus")]),
                    ("end in -oye to match", [("en", "end in"), ("ru", "ое"), ("en", "to match")]),
                    ("add an -a.", [("en", "add an"), ("ru", "а")])]:
        runs, _ = N.find_runs(t, vocab("ся"), {"is", "an"})
        assert [(p["kind"], p["text"]) for p in N.split_parts(t, runs)] == want


def test_fragments_beside_russian_words_and_each_other():
    t = 'both jobs end in "-ym" and "-om", the "as a" endings, and "spasibo" too.'
    runs, _ = N.find_runs(t, V, EN)
    assert [(r["kind"], r["cyr"]) for r in runs] == [("fragment", ["ым"]), ("fragment", ["ом"]), ("latin", ["спасибо"])]
    assert [p["text"] for p in N.split_parts(t, runs)] == ["both jobs end in", "ым", "and", "ом", "the \"as a\" endings, and", "спасибо", "too."]


def test_a_fragment_is_resolved_from_a_russian_word_of_the_line_first():
    v = vocab("работала")
    t = 'The verb "rabotala" ends in "-la" because Elena is a woman.'
    runs, _ = N.find_runs(t, v, {"the", "verb"})
    assert [(r["kind"], r["cyr"], r["via"]) for r in runs] == [("latin", ["работала"], runs[0]["via"]), ("fragment", ["ла"], ["fragment-context"])]
    got, _ = frags('It ends in -la here.', ctx={"она", "работала"})                  # the dialogue quote the sentence is about
    assert got == [("-la", "ла", "fragment-context")]
    got, _ = frags("It ends in -la here.", dialogue=["Она работала там."])           # the scene's dialogue
    assert got == [("-la", "ла", "fragment-context")]


def test_context_gives_the_table_form_when_a_word_carries_it_and_otherwise_the_letters_slice():
    got, _ = frags('The plural "-ye" fits.', ctx={"красивые"})
    assert got == [("-ye", "ые", "fragment-context")]                                # not the bare е the letters alone give
    got, _ = frags('The "-che" fits.', dialogue=["Это мельче."])
    assert got == [("-che", "че", "fragment-context")]
    got, _ = frags('The "-ly" fits.', dialogue=["Тихо лы."])
    assert got == []                                                                 # an English affix: only the table could resolve it
    got, _ = frags("The ending -y fits.", ctx={"красный"})                           # -y is ы or й: the context settles it
    assert got == [("-y", "й", "fragment-context")]


def test_ambiguous_endings_without_context_stay_english_and_are_listed():
    got, unres = frags('The ending "-y" and "-i" are loose.')
    assert got == [] and [u["inner"] for u in unres] == ["-y", "-i"] and {u["kind"] for u in unres} == {"fragment"}
    got, _ = frags("The ending -y fits.", ctx={"красный", "красны"})                  # the context disagrees: not guessed
    assert got == []


def test_english_hyphenated_words_and_affixes_are_never_fragments():
    for t in ['This is the "to"-form of it.', "Not a bare -ever here.", 'the prefix "re-" in English', 'the "-ness" and "-ity" glosses',
              "an X-ray and a well-known state-of-the-art re-entry", 'a "-form" noun', 'It ends "-ly" in English.', "a - b and c -- d"]:
        got, _ = frags(t, ctx={"ре", "ever"}, dialogue=["Реально, ever. Форма."])
        assert got == [], t
    got, unres = frags('the "-ness" and "-ity" glosses')
    assert unres == []                                                               # English affixes are not reported as leftovers either


def test_a_fragment_inside_a_longer_quote_is_a_gloss():
    got, _ = frags('The quote "ends in -la" and the "-la-la" song.')
    assert got == []


def test_ambiguous_and_partial_runs_are_reported_with_candidates():
    v = vocab("умеет", "уметь", "спаси", "за")
    runs, unres = N.find_runs('Say "umet" and "za" and "spasi blorp".', v, set())
    assert [r["cyr"] for r in runs] == [["за"]]
    kinds = {u["inner"]: u["kind"] for u in unres}
    assert kinds == {"umet": "ambiguous", "spasi blorp": "partial"}
    amb = next(u for u in unres if u["inner"] == "umet")
    assert amb["words"][0]["cands"] == ["умеет", "уметь"]


def test_spasi_bog_and_apostrophe():
    runs, _ = N.find_runs('It began as "spasi Bog", and "spasayesh\'" is saving.', V, EN)
    assert [" ".join(r["cyr"]) for r in runs] == ["спаси бог", "спасаешь"]


def test_parts_split_text_around_runs():
    t = '"Spasibo za kofe" thanks someone for the coffee.'
    runs, _ = N.find_runs(t, V, EN)
    parts = N.split_parts(t, runs)
    assert [(p["kind"], p["text"]) for p in parts] == [("ru", "спасибо за кофе"), ("en", "thanks someone for the coffee.")]
    t = "'Oh, come on.' \"Da ladno\" is, word for word, \"yes, fine\"."
    parts = N.split_parts(t, N.find_runs(t, V, EN)[0])
    assert [p["kind"] for p in parts] == ["en", "ru", "en"]
    assert parts[0]["text"] == "'Oh, come on.'" and parts[2]["text"].startswith("is, word for word")
    assert "yes, fine" in parts[2]["text"]            # English quotes inside an English part stay


def test_sentence_language_is_per_sentence():
    assert narrator.sentence_is_english("Max says \"spasibo\".")
    assert not narrator.sentence_is_english("Спасибо за кофе.")
    assert not narrator.sentence_is_english("Это не английский текст, a bit of English.")


# ---- stress ------------------------------------------------------------------------------------------------------------
def test_stress_is_automatic():
    # content form wins; monosyllables get nothing; RuAccent only for words with no stressed form
    seen = []

    def acc(sents):
        seen.extend(sents)
        return ["ла́дно" for _ in sents]
    assert N.stress_text(["спасибо", "за"], ["спаси́бо", None], acc) == "спаси́бо за"
    assert seen == []
    assert N.stress_text(["ладно"], [None], lambda s: ["ла́дно"]) == "ла́дно"
    assert N.stress_text(["ладно"], [None], None) == "ладно"         # no RuAccent: plain, never a guess


def test_homograph_stress_is_not_taken_from_another_sense():
    scene, ep = N.Scope(), N.Scope()
    N.RuVocab.add(scene, "замок", "за́мок")
    N.RuVocab.add(ep, "замок", "замо́к")
    v = N.RuVocab()
    v.scopes = [scene, ep]
    st, hom = v.stress_of("замок")
    assert hom and st == "за́мок"                  # the scene's own sense, flagged for review
    v.scopes = [ep, scene]                         # nobody is unanimous at the narrowest scope with two forms
    one = N.Scope()
    N.RuVocab.add(one, "замок", "за́мок")
    N.RuVocab.add(one, "замок", "замо́к")
    v.scopes = [one]
    assert v.stress_of("замок") == (None, True)
    w = vocab(("кофе", "ко́фе"))
    assert w.stress_of("кофе") == ("ко́фе", False)


def test_ruaccent_reads_the_dialogue_sentence_when_it_has_one():
    asked = []

    def acc(sents):
        asked.extend(sents)
        return ["Мы́ зна́ем замо́к." if "знаем" in sents[0] else "замок" for _ in sents]
    out = N.stress_text(["замок"], [None], acc, context="Мы знаем замок.")
    assert out == "замо́к" and asked == ["Мы знаем замок."]
    runs, _ = N.find_runs('Say "zamok" now.', vocab("замок"), set(), ctx={"замок"}, dialogue=["Мы знаем замок."])
    assert runs[0]["context"] == "Мы знаем замок."


def test_stress_setting_is_the_narrators_own():
    parts = [{"kind": "ru", "run": {"cyr": ["ладно"], "stressed": [None]}}]
    calls = []
    acc = lambda s: (calls.append(s), ["ла́дно"] * len(s))[1]
    narrator.stressed_for(parts, acc, "content")
    assert parts[0]["text"] == "ладно" and calls == []
    narrator.stressed_for(parts, acc, "none")
    assert parts[0]["text"] == "ладно" and calls == []
    narrator.stressed_for(parts, acc, "all")
    assert parts[0]["text"] == "ла́дно" and calls


# ---- timing ----------------------------------------------------------------------------------------------------------
def test_tokens_map_to_parts_and_times_follow_part_offsets():
    text = '"Spasibo za kofe" thanks someone for the coffee.'
    runs, _ = N.find_runs(text, V, EN)
    parts = N.split_parts(text, runs)
    toks = narrator.seg_tokens(text)
    sp = narrator.token_char_spans(text, toks)
    job = {"text": text, "parts": parts}
    offs = [(0.0, 1.2), (1.4, 3.0)]
    t = W.distribute(job, offs, sp)
    assert len(t) == len(toks) == 8
    assert t[0][0] == 0.0 and abs(t[2][1] - 1.2) < 1e-9          # the three Russian words fill the Russian part exactly
    assert abs(t[3][0] - 1.4) < 1e-9 and abs(t[-1][1] - 3.0) < 1e-9
    assert all(a <= b for a, b in t) and all(t[i][1] <= t[i + 1][0] + 1e-9 for i in range(len(t) - 1))
    assert t[0][1] - t[0][0] > t[1][1] - t[1][0]                 # спа-си-бо (3 vowels) longer than за (1)


def test_shift_moves_everything_after_the_replaced_sentence():
    spans = {"durationSec": 10.0, "segs": [
        {"seg": 0, "start": 0.0, "end": 2.0, "nextStart": 2.5, "sentences": [{"i": 0, "start": 0.0, "end": 2.0}]},
        {"seg": 1, "start": 2.5, "end": 5.0, "nextStart": 5.4, "sentences": [{"i": 0, "start": 2.5, "end": 3.5}, {"i": 1, "start": 3.8, "end": 5.0}]},
        {"seg": 2, "start": 5.4, "end": 7.0, "nextStart": 7.4, "sentences": [{"i": 0, "start": 5.4, "end": 7.0}]}]}
    timing = {"0": [{"s": 0.1, "e": 1.9}], "1": [{"s": 2.6, "e": 3.4}, {"s": 3.9, "e": 4.9}], "2": [{"s": 5.5, "e": 6.9}]}
    W.shift_doc(spans, timing, 3.5, 0.7)          # the first sentence of seg 1 grew by 0.7 s
    W.round_docs(spans, timing)
    s1 = spans["segs"][1]
    assert s1["start"] == 2.5 and s1["sentences"][0]["end"] == 4.2 and s1["sentences"][1]["start"] == 4.5
    assert s1["end"] == 5.7 and s1["nextStart"] == 6.1 and spans["segs"][2]["start"] == 6.1
    assert timing["0"][0]["e"] == 1.9 and timing["1"][1]["s"] == 4.6 and timing["2"][0]["e"] == 7.6
    assert spans["durationSec"] == 10.7


def test_token_guard_is_per_sentence():
    g = {"sentences": [{"i": 0, "text": "One two three."}, {"i": 1, "text": "Four five."}]}
    ok = [{"t": t} for t in "One two three. Four five.".split()]
    assert W.verify_tokens(g, ok, narrator) is None
    moved = [{"t": t} for t in "One two Four three. five.".split()]        # same total, a token crossed the boundary
    assert "line up" in W.verify_tokens(g, moved, narrator)
    assert "count" in W.verify_tokens(g, ok[:-1], narrator)


def test_whisper_verdicts():
    cfg = {"ruCer": 0.25, "enCer": 0.25}
    assert W.passes("ru", "спасибо за кофе", "Спасибо за кофе.", cfg)[0]
    assert not W.passes("ru", "спасибо", "Spasibo", cfg)[0]                      # wrong script = not Russian
    assert W.passes("en", "thanks someone for the coffee.", "Thanks, someone, for the coffee.", cfg)[0]
    assert not W.passes("en", "is a frame you can reuse", "is a frame", cfg)[0]
    assert W.passes("en", "God save, and", "God save and", cfg)[0]
    assert not W.passes("en", "God save, and", "Gods", cfg)[0]


def test_a_bare_syllable_is_judged_by_duration_not_by_a_skeleton():
    cfg = {"ruCer": 0.25, "enCer": 0.25}
    assert W.ru_key("а") == "" and W.ru_key("ое") == ""
    assert not W.passes("ru", "а", "Я", cfg)[0]                                          # a word of one vowel fails on its empty skeleton
    for ref, hyp in [("ла", ""), ("ла", "Ла."), ("ла", "Ля"), ("ла", "Ла-а."), ("а", "А."), ("а", "Я"), ("ое", "Ое"), ("пере", "Пере."),
                     ("ся", ""), ("ам", "Latin letters")]:
        assert W.passes("ru", ref, hyp, cfg, syllable=True)[0], (ref, hyp)               # nothing heard / a match on the key: the duration decides
    for ref, hyp in [("ла", "Да"), ("ое", "Ого"), ("ым", "Да")]:
        assert not W.passes("ru", ref, hyp, cfg, syllable=True)[0], (ref, hyp)           # Cyrillic with another syllable
    assert not W.passes("ru", "ла", "Да", cfg)[0] and not W.passes("ru", "спасибо", "Spasibo", cfg)[0]    # normal words are not loosened
    assert not W.duration_ok("ла", 0.05) and W.duration_ok("ла", 0.3)                    # the caller's test: not a click, not swallowed
    assert not W.plausible_part("ла", 0.05) and W.plausible_part("ла", 0.4) and not W.plausible_part("ла", 5.0)


def test_syllable_parts_are_flagged_and_get_their_own_id():
    s = {"narratorRu": {"version": 1, "temperatures": [0.5]}, "ttsEn": {"nfe": 32, "cfg": 2}, "lora": {"tag": "x"}}
    assert narrator.part_id("ru", "v", "ла", s, True) != narrator.part_id("ru", "v", "ла", s)
    assert narrator.part_id("ru", "v", "ла", s, False) == narrator.part_id("ru", "v", "ла", s)
    runs, _ = N.find_runs('ends in "-la" because', vocab("ся"), set())
    parts = N.split_parts('ends in "-la" because', runs)
    narrator.stressed_for(parts, lambda xs: pytest.fail("a bare syllable is never sent to RuAccent"), "all")
    assert [(p["kind"], p["text"], p.get("plain")) for p in parts if p["kind"] == "ru"] == [("ru", "ла", "ла")]


def test_ru_takes_never_share_a_seed_or_temperature_within_a_part():
    todo = [{"id": "a", "text": "xx", "takes": [0, 1]}, {"id": "b", "text": "y", "takes": [1]}, {"id": "c", "text": "zzz", "takes": [0]}]
    chunks = W.ru_chunks(todo, 2)
    assert all(len({k}) == 1 for k, _ in chunks)
    seen = {}
    for k, items in chunks:
        for it in items:
            seen.setdefault(it["id"], []).append(k)
    assert seen["a"] == [0, 1] and len(chunks) == 2
    assert sorted(it["id"] for k, c in chunks if k == 1 for it in c) == ["a", "b"]


def test_settings_do_not_touch_the_render_key():
    s = config.load_settings()
    s2 = json.loads(json.dumps(s))
    s2["narratorRu"]["rounds"] = 9
    assert config.tts_signature(s) == config.tts_signature(s2) and config.assembly_signature(s) == config.assembly_signature(s2)
    assert s["narratorRu"]["ruVoice"] == "ru-f1" and s["narratorRu"]["enVoice"] == "sky"
    assert s["narratorRu"]["gapMs"] == [150, 250]


def test_no_asserts_and_no_dead_code_in_the_build():
    tree = ast.parse((HERE / "narrator_work.py").read_text("utf-8"))
    assert not [n for n in ast.walk(tree) if isinstance(n, ast.Assert)]        # python -O would drop them
    assert "audio.__dict__" not in (HERE / "narrator_work.py").read_text("utf-8")
    with pytest.raises(SystemExit):
        narrator.parse_args(["--takes", "2"])             # settings own the take counts
    assert narrator.parse_args(["--retry-failed"]).retry_failed


# ---- splices (numpy) -----------------------------------------------------------------------------------------------
def _np():
    return pytest.importorskip("numpy")


def _burst(np, sr, f, dur, amp=0.2, seed=0):
    t = np.arange(int(dur * sr)) / sr
    env = np.minimum(1, np.minimum(t, dur - t) / 0.01)           # 10 ms ramps, like a trimmed sentence
    return (amp * env * np.sin(2 * np.pi * f * t)).astype("float32")


def test_quiet_point_and_splice_have_no_click_at_the_joins():
    np = _np()
    sr, F = 24000, 192
    rng = np.random.default_rng(1)
    gap = lambda s: (rng.standard_normal(int(s * sr)) * 1e-3).astype("float32")
    sig = np.concatenate([gap(0.3), _burst(np, sr, 220, 1.0), gap(0.3), _burst(np, sr, 330, 1.0), gap(0.3)])
    s0, e0 = int(1.6 * sr), int(2.6 * sr)               # the middle gap is [1.3, 1.6): the sentence to replace is [1.6, 2.6)
    y = np.concatenate([_burst(np, sr, 440, 0.8, 0.3), gap(0.02)])
    y = np.concatenate([gap(0.02), y])
    cl = W.quiet_point(sig, s0 - int(0.06 * sr), s0 + int(0.01 * sr), s0, F, after=True)
    cr = W.quiet_point(sig, e0 - int(0.01 * sr), min(len(sig), e0 + int(0.06 * sr)), e0, F, after=False)
    assert cl <= s0 + int(0.01 * sr) and cr >= e0 - int(0.01 * sr)
    for a, b in ((cl, cl + F), (cr - F, cr)):                   # both joins sit in near-silence
        assert float(np.sqrt((sig[a:b] ** 2).mean())) < 5e-3
    out = W.splice(sig, y, cl, cr, F)
    assert len(out) == len(sig) - (cr - cl) + len(y)
    assert np.array_equal(out[:cl], sig[:cl]) and np.array_equal(out[cl + len(y):], sig[cr:])
    quiet_step = float(np.abs(np.diff(sig[:int(0.2 * sr)])).max())
    for j in (cl, cl + len(y)):
        w = out[j - 48:j + 48]
        assert float(np.abs(np.diff(w)).max()) < max(4 * quiet_step, 0.02)      # no sample jump at the join
    # a hard cut INSIDE speech would have clicked: the same splice at a loud sample does jump, so the check above has teeth
    j = int(0.8 * sr)
    j += int(np.argmax(np.abs(sig[j:j + 200])))
    hard = np.concatenate([sig[:j + 1], y, sig[int(2.0 * sr):]])
    assert float(np.abs(np.diff(hard[j - 4:j + 6])).max()) > 0.1


def test_limiter_never_overshoots_and_has_no_steps():
    pytest.importorskip("scipy")
    np = _np()
    sr = 24000
    t = np.arange(sr) / sr
    x = (0.3 * np.sin(2 * np.pi * 200 * t)).astype("float32")
    x[12000:12010] *= 4.0                                          # a peak of 1.2
    y = W.limit_peaks(x, 0.88, sr)
    assert float(np.abs(y).max()) <= 0.88 + 1e-6
    assert np.array_equal(y[:6000], x[:6000])                      # far from the peak: untouched
    assert float(np.abs(np.diff(y / np.where(x == 0, 1, x))[1000:9000]).max()) < 1e-6
    g = np.abs(y[11000:13000]) / np.maximum(np.abs(x[11000:13000]), 1e-9)
    assert float(np.abs(np.diff(g[np.abs(x[11000:13000]) > 0.05])).max()) < 0.02      # the gain moves smoothly


def test_match_loudness_matches_after_the_limiter():
    pytest.importorskip("scipy")
    np = _np()
    import audio
    sr = 24000
    t = np.arange(2 * sr) / sr
    ref = (0.12 * np.sin(2 * np.pi * 300 * t)).astype("float32")
    rng = np.random.default_rng(3)
    y = (rng.standard_normal(2 * sr) * 0.05 * (1 + 4 * (rng.random(2 * sr) > 0.995))).astype("float32")      # peaky
    z = W.match_loudness(y, ref, sr)
    assert abs(audio.lufs(z, sr) - audio.lufs(ref, sr)) < 0.15
    assert float(np.abs(z).max()) <= W.LIMIT + 1e-6


def test_equal_power_crossfade_keeps_energy():
    np = _np()
    a = np.full(4000, 0.5, dtype="float32")
    b = np.full(4000, 0.5, dtype="float32")
    out = W.splice(a, b, 1000, 3000, 240)
    mid = out[1000:1240]
    # uncorrelated material of equal level keeps its power; for identical constants the sum of the two weights is >= 1 (up to sqrt 2)
    assert float(mid.min()) >= 0.49 and float(mid.max()) <= 0.5 * 1.4143
    assert np.array_equal(out[:1000], a[:1000])


def test_decoded_signal_is_enc_lag_late_so_cuts_are_made_there(tmp_path):
    np = _np()
    pytest.importorskip("scipy")
    import audio
    sr = 24000
    x = np.concatenate([np.zeros(sr // 2, dtype="float32"), _burst(np, sr, 300, 1.0), np.zeros(sr // 2, dtype="float32")])
    audio.encode_mp3(x, sr, tmp_path / "t.mp3", 96)
    d = W.decode_mp3(tmp_path / "t.mp3", sr)
    on_x = int(np.argmax(np.abs(x) > 0.02))
    on_d = int(np.argmax(np.abs(d) > 0.02))
    assert abs((on_d - on_x) - W.ENC_LAG) <= 12          # the stored file's spans are on x's timeline, the decoded signal on d's


# ---- the build, end to end on a synthetic scene ----------------------------------------------------------------------
SID = "kukhnya-s01e01-scene-01"
SR = 24000


def _need_audio():
    np = _np()
    pytest.importorskip("scipy")
    pytest.importorskip("soundfile")
    if subprocess.run(["ffmpeg", "-version"], capture_output=True).returncode != 0:
        pytest.skip("no ffmpeg")
    return np


class Scene:
    """A rendered scene on disk: dialogue, two adjacent narrator sentences with Russian, a narrator sentence without."""
    def __init__(self, tmp, np, tag="a"):
        import audio
        self.tmp, self.np = Path(tmp), np
        self.store = self.tmp / "store"
        self.content = self.tmp / "content"
        self.work = self.tmp / "work"
        nd = self.content / "out" / "kukhnya" / "s01e01"
        nd.mkdir(parents=True, exist_ok=True)
        notes = {"lines": [{"seg": 0, "trans": "Thanks for the coffee. Oh come on.", "words": [
            {"t": "Спасибо", "stress": "спаси́бо"}, {"t": "за"}, {"t": "кофе", "stress": "ко́фе"}, {"t": "Да"}, {"t": "ладно"}]}], "lexicon": {}}
        (nd / "scene-01.notes.json").write_text(json.dumps(notes, ensure_ascii=False), "utf-8")
        (nd / "scene-01.json").write_text(json.dumps({"id": SID, "pair": "ru-en", "segments": []}), "utf-8")
        rng = np.random.default_rng(7)
        gap = lambda s: (rng.standard_normal(int(s * SR)) * 1e-3).astype("float32")
        self.layout = [(0.3, 2.3, 220), (3.0, 4.6, 220), (4.9, 6.5, 220), (8.0, 9.5, 220), (10.0, 11.5, 220)]
        x = gap(0.3)
        t = 0.3
        for i, (a, b, f) in enumerate(self.layout):
            if a > t:
                x = np.concatenate([x, gap(a - t)])
            x = np.concatenate([x, _burst(np, SR, f + 10 * i, b - a, 0.2)])
            t = b
        x = np.concatenate([x, gap(0.5)])
        self.x = x
        d = self.store / SID
        d.mkdir(parents=True)
        audio.encode_mp3(x, SR, d / "audio.mp3", 96)
        tok = lambda s: [t for t in s.split() if re.search(r"\w", t)]
        T = [["Спасибо за кофе. Да ладно."], ['"Spasibo za" is a frame.', 'Say "da ladno" now.'], ["Ну хорошо."], ["It means thank you."]]
        sents = [
            (0, "max", "ru", [(0, 0.3, 2.3, T[0][0])]),
            (1, "narrator", "en", [(0, 3.0, 4.6, T[1][0]), (1, 4.9, 6.5, T[1][1])]),
            (2, "max", "ru", [(0, 8.0, 9.5, T[2][0])]),
            (3, "narrator", "en", [(0, 10.0, 11.5, T[3][0])])]
        segs, timing = [], {}
        for seg, v, lang, ss in sents:
            segs.append({"seg": seg, "v": v, "voice": v, "lang": lang, "start": ss[0][1], "end": ss[-1][2], "nextStart": ss[-1][2] + 0.4,
                         "sentences": [{"i": i, "start": a, "end": b, "text": txt, "engine": "f5-tts"} for i, a, b, txt in ss]})
            ws = []
            for i, a, b, txt in ss:
                tk = tok(txt)
                step = (b - a) / len(tk)
                ws += [{"t": w, "s": a + k * step, "e": a + (k + 1) * step - 0.01, "ok": True, "why": ""} for k, w in enumerate(tk)]
            timing[str(seg)] = ws
        spans = {"durationSec": len(x) / SR, "segs": segs}
        meta = {"sceneId": SID, "renderKey": "rk-" + tag, "contentHash": narrator.content_hash_of(self.content, SID), "durationSec": len(x) / SR, "audioSha256": "", "audioBytes": 0}
        from store import sha256_file
        meta["audioSha256"] = sha256_file(d / "audio.mp3")
        meta["audioBytes"] = (d / "audio.mp3").stat().st_size
        jb = lambda o: (json.dumps(o, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode()
        (d / "spans.json").write_bytes(jb(spans))
        (d / "timing.json").write_bytes(jb(timing))
        (d / "report.json").write_bytes(jb({"audio": {}}))
        (d / "meta.json").write_bytes(jb(meta))
        self.settings = config.load_settings()
        nr = self.settings["narratorRu"]
        nr["stress"] = "content"
        nr["publishLockWaitSec"] = 0.4
        self.settings_path = self.tmp / "settings.json"
        self.write_settings()

    def write_settings(self):
        self.settings_path.write_text(json.dumps(self.settings), "utf-8")

    def args(self, **kw):
        base = dict(content=str(self.content), retry_failed=False, store=str(self.store), work=str(self.work), settings=str(self.settings_path),
                    out="", plan=False)
        base.update(kw)
        return SimpleNamespace(**base)

    def plan(self, **kw):
        return narrator.build_plan(self.args(**kw), self.settings, [SID], self.store, self.work)

    def tones(self, plan, level=0.15):
        """Write a passing take for every part (a 440 Hz burst for Russian, 330 Hz for English) and the checks."""
        import soundfile as sf
        np = self.np
        (self.work / "takes").mkdir(parents=True, exist_ok=True)
        checks = {}
        for p in plan["parts"]:
            f = 440 if p["kind"] == "ru" else 330
            dur = 0.25 + 0.05 * len(p["plain"].split())
            w = np.concatenate([np.zeros(int(0.02 * SR), dtype="float32"), _burst(np, SR, f, dur, level), np.zeros(int(0.02 * SR), dtype="float32")])
            sf.write(str(self.work / "takes" / f"{p['id']}.t0.wav"), w, SR)
            checks[f"{p['id']}.t0"] = {"pass": True}
        (self.work / "checks.json").write_text(json.dumps(checks), "utf-8")

    def meta(self, base=None):
        return json.loads(((base or self.store / SID) / "meta.json").read_text("utf-8"))

    def build(self, plan, **kw):
        (self.work / "plan.json").write_text(json.dumps(plan, ensure_ascii=False), "utf-8")
        out = []
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            W.stage_build(self.args(**kw))
        return json.loads(buf.getvalue().strip().splitlines()[-1][3:])


@pytest.fixture
def scene(tmp_path, monkeypatch):
    np = _need_audio()
    monkeypatch.setattr(config, "PUBLISH_LOCK", tmp_path / "publish.lock")
    return Scene(tmp_path, np)


def test_plan_finds_both_adjacent_lines_and_skips_the_english_one(scene):
    plan = scene.plan()
    sc = plan["scenes"][0]
    assert [(j["seg"], j["i"]) for j in sc["jobs"]] == [(1, 0), (1, 1)]
    assert sc["jobs"][0]["parts"][0]["text"] == "спаси́бо за"       # the notes' stress, no RuAccent in "content" mode
    assert plan["skipped"] == [] and plan["unresolved"] == []


def test_build_end_to_end_timing_loudness_and_joins(scene):
    np = scene.np
    import audio
    plan = scene.plan()
    scene.tones(plan)
    before_sig = W.decode_mp3(scene.store / SID / "audio.mp3", SR)
    res = scene.build(plan)
    assert res["scenes"] == 1 and res["lines"] == 2 and res["failed"] == 0
    live = scene.store / SID
    meta = scene.meta()
    spans = json.loads((live / "spans.json").read_text())
    timing = json.loads((live / "timing.json").read_text())
    new_sig = W.decode_mp3(live / "audio.mp3", SR)
    # duration: spans, meta and the file agree
    dur = len(new_sig) / SR
    assert abs(spans["durationSec"] - dur) < 0.05 and abs(meta["durationSec"] - dur) < 0.05
    # monotonic spans, words inside their sentences' neighbourhood, every token kept
    starts = [q["start"] for g in spans["segs"] for q in g["sentences"]]
    ends = [q["end"] for g in spans["segs"] for q in g["sentences"]]
    assert starts == sorted(starts) and all(a < b for a, b in zip(starts, ends)) and all(e <= s2 + 1e-6 for e, s2 in zip(ends, starts[1:]))
    for k, ws in timing.items():
        assert all(w1["s"] <= w2["s"] + 1e-9 for w1, w2 in zip(ws, ws[1:]))
    assert len(timing["1"]) == len(scene_tokens(spans, 1))
    assert max(w["e"] for ws in timing.values() for w in ws) <= dur + 0.05
    # later regions shifted by exactly the length change; untouched dialogue is the same audio
    d_n = len(new_sig) - len(before_sig)
    assert abs(d_n / SR - (spans["durationSec"] - json.loads((scene.store / ".narrator-before" / SID / "spans.json").read_text())["durationSec"])) < 0.002
    a0, a1 = int(0.35 * SR), int(2.2 * SR)                            # seg 0, before everything that changed
    assert float(np.abs(new_sig[a0:a1] - before_sig[a0:a1]).max()) < 0.03       # one mp3 generation apart, never a different signal
    # the new Russian tones sit where the new timing says (ENC_LAG applied): the 440 Hz part starts at the first word
    first = timing["1"][0]
    seg_tone = new_sig[int((first["s"] - 0.1) * SR):int((first["e"] + 0.4) * SR)]
    assert float(np.sqrt((seg_tone ** 2).mean())) > 0.05
    # joins are in near-silence and click-free
    for line in meta["narratorRu"]["lines"]:
        for t in line["joins"]:
            j = int(round(t * SR)) + W.ENC_LAG
            assert float(np.sqrt((new_sig[j - 40:j + 40] ** 2).mean())) < 0.02
    # each replaced line is within 1.5 LU of what it replaced; untouched dialogue is not re-leveled (only one more mp3 generation)
    l0, l1 = audio.lufs(before_sig, SR), audio.lufs(new_sig, SR)
    lu = res["loudnessLU"][SID]
    assert abs(lu["scene"] - (l1 - l0)) < 0.02 and len(lu["lines"]) == 2 and all(abs(d) <= 1.5 for d in lu["lines"]), lu
    assert abs(lu["scene"]) < 0.2 and 0 <= lu["gainDb"] <= 1.0, lu           # the generation loss is given back, uniformly and within +-1 dB
    assert meta["narratorRu"]["version"] == "b1" and all(l["version"] == "b1" and l["sig"] for l in meta["narratorRu"]["lines"])
    assert meta["audioSha256"] == narrator.sha256_file(live / "audio.mp3")


def scene_tokens(spans, seg):
    g = next(g for g in spans["segs"] if g["seg"] == seg)
    return [t for q in g["sentences"] for t in narrator.seg_tokens(q["text"])]


def test_second_run_is_a_no_op_and_lines_are_never_doubled(scene):
    plan = scene.plan()
    scene.tones(plan)
    scene.build(plan)
    once = scene.meta()
    assert narrator_lines(once) == [(1, 0), (1, 1)]
    assert scene.plan()["scenes"] == []                      # same sigs, same version: nothing to do
    # a second run with the SAME plan (what an overlapping run would do) re-applies to the original, it does not stack on the splice
    sha1 = once["audioSha256"]
    scene.build(plan)
    twice = scene.meta()
    assert narrator_lines(twice) == [(1, 0), (1, 1)]
    assert abs(twice["durationSec"] - once["durationSec"]) < 1e-6 and twice["audioSha256"] == sha1
    # a duplicated job in one plan is spliced once
    plan2 = json.loads(json.dumps(plan))
    plan2["scenes"][0]["jobs"] = plan2["scenes"][0]["jobs"] * 2
    scene.build(plan2)
    assert narrator_lines(scene.meta()) == [(1, 0), (1, 1)]


def narrator_lines(meta):
    return [(l["seg"], l["i"]) for l in meta["narratorRu"]["lines"]]


def test_version_bump_redoes_done_lines_from_the_original(scene):
    plan = scene.plan()
    scene.tones(plan)
    scene.build(plan)
    before = scene.store / ".narrator-before" / SID
    sha_before = narrator.sha256_file(before / "audio.mp3")
    scene.settings["narratorRu"]["version"] = "b2"
    scene.write_settings()
    plan2 = scene.plan()
    assert [s["scene"] for s in plan2["scenes"]] == [SID]                     # the done-filter honours the version
    assert {l["version"] for l in scene.meta()["narratorRu"]["lines"]} == {"b1"}
    scene.tones(plan2)
    scene.build(plan2)
    m = scene.meta()
    assert {l["version"] for l in m["narratorRu"]["lines"]} == {"b2"} and narrator_lines(m) == [(1, 0), (1, 1)]
    assert narrator.sha256_file(before / "audio.mp3") == sha_before         # the original is still the original


def _set_hash(scene, md):
    m = json.loads(md.read_text("utf-8"))
    m["contentHash"] = narrator.content_hash_of(scene.content, SID)
    md.write_text(json.dumps(m), "utf-8")


def test_lines_that_no_longer_qualify_put_the_original_back(scene):
    scene.settings["narratorRu"]["lineLoudnessTolLU"] = 6.0
    scene.write_settings()
    plan = scene.plan()
    scene.tones(plan)
    scene.build(plan)
    original = scene.store / ".narrator-before" / SID
    # the content changed: "da ladno" is no longer known (neither in the notes nor in the rendered dialogue), so that line cannot be re-made
    nd = scene.content / "out" / "kukhnya" / "s01e01" / "scene-01.notes.json"
    notes = json.loads(nd.read_text("utf-8"))
    notes["lines"][0]["words"] = [w for w in notes["lines"][0]["words"] if w["t"] not in ("Да", "ладно")]
    nd.write_text(json.dumps(notes, ensure_ascii=False), "utf-8")
    rehash = lambda: [_set_hash(scene, md) for md in (original / "meta.json", scene.store / SID / "meta.json")]    # the render is taken to be from this content
    rehash()
    sps = [original / "spans.json", scene.store / SID / "spans.json"]          # the episode scope reads the rendered dialogue too
    for sp in sps:
        sp.write_text(sp.read_text("utf-8").replace("Да ладно", "Ну хорошо"), "utf-8")
    plan2 = scene.plan()
    assert plan2["scenes"][0]["jobs"][0]["i"] == 0 and len(plan2["scenes"][0]["jobs"]) == 1
    scene.tones(plan2)
    scene.build(plan2)
    assert narrator_lines(scene.meta()) == [(1, 0)]
    # and with nothing left at all the original returns byte for byte
    notes["lines"][0]["words"] = []
    nd.write_text(json.dumps(notes, ensure_ascii=False), "utf-8")
    rehash()
    for sp in sps:
        sp.write_text(sp.read_text("utf-8").replace("Спасибо за кофе", "Ну хорошо"), "utf-8")
    plan3 = scene.plan()
    assert plan3["scenes"][0]["jobs"] == [] and plan3["scenes"][0]["revert"]
    scene.build(plan3)
    assert (scene.store / SID / "audio.mp3").read_bytes() == (original / "audio.mp3").read_bytes()
    assert "narratorRu" not in scene.meta()


def test_before_copy_is_keyed_to_the_render_key(scene):
    plan = scene.plan()
    scene.tones(plan)
    scene.build(plan)
    before = scene.store / ".narrator-before" / SID
    assert scene.meta(before)["renderKey"] == "rk-a" and "narratorRu" not in scene.meta(before)
    # a normal re-render replaces the scene: new key, new audio, no narrator lines
    other = Scene(scene.tmp / "other", scene.np, tag="b")
    import store as S
    st = S.Store(scene.store)
    st.commit_scene(SID, {n: (other.store / SID / n) for n in ("audio.mp3", "spans.json", "timing.json", "report.json", "meta.json")})
    d, lm, note = narrator.original_dir(scene.store, SID)
    assert note == "live" and lm["renderKey"] == "rk-b"                      # the stale before-copy is not used
    plan2 = scene.plan()
    scene.tones(plan2)
    scene.build(plan2)
    assert scene.meta(before)["renderKey"] == "rk-b"                         # refreshed, not left holding the old render
    assert narrator.sha256_file(before / "audio.mp3") == narrator.sha256_file(other.store / SID / "audio.mp3")
    assert scene.meta()["renderKey"] == "rk-b" and narrator_lines(scene.meta())


def test_a_narrated_scene_without_a_valid_original_is_not_touched(scene):
    plan = scene.plan()
    scene.tones(plan)
    scene.build(plan)
    import shutil
    shutil.rmtree(scene.store / ".narrator-before")
    d, lm, note = narrator.original_dir(scene.store, SID)
    assert d is None and "no pristine original" in note
    sha = scene.meta()["audioSha256"]
    p = scene.plan()
    assert p["scenes"] == [] and p["errors"][0]["scene"] == SID
    assert scene.meta()["audioSha256"] == sha


def test_scene_changed_during_the_run_is_not_committed(scene, monkeypatch):
    import audio
    plan = scene.plan()
    scene.tones(plan)
    real = audio.encode_mp3

    def encode_then_rerender(sig, sr, out, kbps=96, *limits):
        real(sig, sr, out, kbps, *limits)
        m = json.loads((scene.store / SID / "meta.json").read_text())
        m["audioSha256"] = "someone-else"                                  # a render lands between the read and the commit
        (scene.store / SID / "meta.json").write_text(json.dumps(m))
    monkeypatch.setattr(audio, "encode_mp3", encode_then_rerender)
    res = scene.build(plan)
    assert res["scenes"] == 0 and res["failed"] >= 1
    assert "changed while the narrator was working" in res["failures"][0]["why"] and res["failures"][0]["sticky"] is False
    assert scene.meta()["audioSha256"] == "someone-else" and "narratorRu" not in scene.meta()
    assert not (scene.work / "failed.json").read_text().strip("{} \n")        # transient: not remembered as a failure


def test_publish_lock_is_taken_for_the_commit_and_waited_for(scene):
    from store import flock_ctx
    plan = scene.plan()
    scene.tones(plan)
    with flock_ctx(config.PUBLISH_LOCK):                  # the publisher is reading
        res = scene.build(plan)
        assert res["scenes"] == 0 and "publish.lock busy" in res["failures"][0]["why"]
        assert "narratorRu" not in scene.meta()
    res = scene.build(plan)                               # released: the same plan goes through
    assert res["scenes"] == 1
    # compatible with the publisher holding it through flock(1) (exclusive by default): wait, then commit
    scene.settings["narratorRu"]["publishLockWaitSec"] = 10
    scene.write_settings()
    scene.settings["narratorRu"]["version"] = "b1"
    holder = subprocess.Popen(["flock", str(config.PUBLISH_LOCK), "sleep", "1.5"])
    time.sleep(0.4)
    plan2 = json.loads(json.dumps(plan))
    t0 = time.time()
    res = scene.build(plan2)
    holder.wait()
    assert res["scenes"] == 1 and time.time() - t0 >= 0.8


def test_failed_lines_are_remembered_per_render_key_and_version(scene):
    scene.settings["narratorRu"]["lineLoudnessTolLU"] = 6.0
    scene.write_settings()
    plan = scene.plan()
    scene.tones(plan)
    checks = json.loads((scene.work / "checks.json").read_text())
    victim = plan["scenes"][0]["jobs"][1]["parts"][1]["id"]
    checks[f"{victim}.t0"] = {"pass": False}
    (scene.work / "checks.json").write_text(json.dumps(checks))
    res = scene.build(plan)
    assert res["lines"] == 1 and res["failed"] == 1 and res["failures"][0]["sticky"]
    assert (scene.store / "narrator-failures.jsonl").exists()
    assert narrator_lines(scene.meta()) == [(1, 0)]
    again = scene.plan()
    assert again["scenes"] == [] and again["knownFailed"] == 1 and again["parts"] == []     # the rest is current; no GPU time for the failed line
    assert [len(s["jobs"]) for s in scene.plan(retry_failed=True)["scenes"]] == [2]
    scene.settings["narratorRu"]["version"] = "b2"
    scene.write_settings()
    assert [len(s["jobs"]) for s in scene.plan()["scenes"]] == [2]           # a new version is a new chance


def test_dry_run_leaves_no_trace_in_the_store(scene, tmp_path):
    scene.settings["narratorRu"]["lineLoudnessTolLU"] = 6.0
    scene.write_settings()
    plan = scene.plan()
    scene.tones(plan)
    checks = json.loads((scene.work / "checks.json").read_text())
    victim = plan["scenes"][0]["jobs"][1]["parts"][1]["id"]
    checks[f"{victim}.t0"] = {"pass": False}
    (scene.work / "checks.json").write_text(json.dumps(checks))
    snap = {p.name: p.read_bytes() for p in (scene.store / SID).iterdir()}
    out = tmp_path / "dry"
    res = scene.build(plan, out=str(out))
    assert res["lines"] == 1 and res["failed"] == 1
    assert {p.name: p.read_bytes() for p in (scene.store / SID).iterdir()} == snap
    assert not (scene.store / ".narrator-before").exists() and not (scene.store / "narrator-failures.jsonl").exists()
    assert not (scene.work / "failed.json").exists()
    assert (out / f"{SID}.mp3").exists() and json.loads((out / f"{SID}.meta.json").read_text())["narratorRu"]["lines"]


def test_unresolved_run_keeps_the_whole_line_sky(scene):
    nd = scene.content / "out" / "kukhnya" / "s01e01" / "scene-01.notes.json"
    notes = json.loads(nd.read_text("utf-8"))
    notes["lines"][0]["words"] += [{"t": "ладно"}, {"t": "ладна"}]                  # "da ladno" is now unique anyway
    spans_p = scene.store / SID / "spans.json"
    spans = json.loads(spans_p.read_text("utf-8"))
    spans["segs"][1]["sentences"][1]["text"] = 'Say "umet" and "da ladno" now.'
    spans_p.write_text(json.dumps(spans, ensure_ascii=False))
    nd.write_text(json.dumps({"lines": notes["lines"] + [{"seg": 9, "words": [{"t": "умеет"}, {"t": "уметь"}]}], "lexicon": {}}, ensure_ascii=False), "utf-8")
    _set_hash(scene, scene.store / SID / "meta.json")
    plan = scene.plan()
    assert [(j["seg"], j["i"]) for j in plan["scenes"][0]["jobs"]] == [(1, 0)]       # (1, 1) has an ambiguous run: it keeps sky
    assert plan["skipped"][0]["i"] == 1 and plan["unresolved"][0]["kind"] == "ambiguous" and plan["unresolved"][0]["lineKeptSky"]
    assert plan["unresolved"][0]["candidates"][0]["cyr"] == ["умеет", "уметь"]


def test_stress_mode_all_asks_ruaccent_and_content_does_not(scene, monkeypatch):
    import ruaccent_fallback
    made = []

    class Fake:
        def __init__(self, *a, **k):
            made.append(1)

        def __call__(self, sents):
            return list(sents)
    monkeypatch.setattr(ruaccent_fallback, "RuAccent", Fake)
    scene.plan()
    assert made == []                                      # narratorRu.stress == "content"
    scene.settings["narratorRu"]["stress"] = "all"
    scene.settings["stress"]["ruaccentFallback"] = False    # the dialogue's own switch is irrelevant to the narrator
    scene.plan()
    assert made == [1]


# ---- locks -----------------------------------------------------------------------------------------------------------
def test_pipeline_and_work_locks_exclude_a_second_run(tmp_path):
    with narrator.pipeline_lock(tmp_path):
        with pytest.raises(narrator.Busy):
            with narrator.pipeline_lock(tmp_path):
                pass
        with narrator.work_lock(tmp_path / "w"):
            with pytest.raises(narrator.Busy):
                with narrator.work_lock(tmp_path / "w"):
                    pass
    with narrator.pipeline_lock(tmp_path):                 # released with the with-block
        pass


def test_a_second_narrator_run_on_the_same_work_dir_is_refused(scene):
    with narrator.work_lock(scene.work):
        with pytest.raises(narrator.Busy):
            narrator.run(scene.args(plan=False, all=False), scene.settings, [SID])


def test_narrator_only_takes_pipeline_lock_like_a_render_run(tmp_path):
    src = (HERE / "pipeline.py").read_text("utf-8")
    seg = src[src.index("if args.narrator_only:"):src.index("lock = open(store.root")]
    assert "narrator.pipeline_lock(store.root)" in seg and "return 75" in seg


def test_flock_ctx_times_out_and_is_exclusive(tmp_path):
    from store import flock_ctx, LockTimeout
    p = tmp_path / "l"
    with flock_ctx(p):
        with pytest.raises(LockTimeout):
            with flock_ctx(p, timeout=0.2):
                pass
        with flock_ctx(tmp_path / "other", timeout=0.2):          # another file is another lock
            pass
    with flock_ctx(p, timeout=0.2):
        pass


def test_commit_scene_never_leaves_a_moment_without_the_scene_dir(tmp_path):
    import store as S
    st = S.Store(tmp_path)
    st.commit_scene("s", {"a": b"0"})
    a, b = tmp_path / "x", tmp_path / "y"
    a.mkdir(); b.mkdir()
    if not S.exchange_dirs(a, b):
        pytest.skip("renameat2 RENAME_EXCHANGE not available here")
    missing = []
    stop = threading.Event()

    def watch():
        while not stop.is_set():
            if not (tmp_path / "s").is_dir():
                missing.append(1)
    th = threading.Thread(target=watch)
    th.start()
    for i in range(300):
        st.commit_scene("s", {"a": str(i).encode()})
    stop.set()
    th.join()
    assert not missing and (tmp_path / "s" / "a").read_bytes() == b"299"
    assert not [p for p in tmp_path.iterdir() if p.name.startswith(".s.")]


def test_pipeline_records_the_narrator_pass_in_state(tmp_path):
    import pipeline
    import store as S
    st = S.Store(tmp_path)
    pipeline.record_narrator_state(st, "RuntimeError: boom", {})
    assert st.state()["narrator"]["error"] == "RuntimeError: boom"
    pipeline.record_narrator_state(st, None, {"lines": 3, "scenes": 2, "failed": 1})
    n = st.state()["narrator"]
    assert n["error"] is None and (n["lines"], n["scenes"], n["failed"]) == (3, 2, 1)


@pytest.mark.parametrize("limits", [None, W.ENC_LIMITS])
def test_encoder_delay_constant_matches_audio_encode_mp3(tmp_path, limits):
    np = _np()
    import audio
    sig = pytest.importorskip("scipy.signal")
    x = (np.random.default_rng(0).standard_normal(24000 * 3) * 0.05).astype("float32")
    audio.encode_mp3(x, 24000, tmp_path / "t.mp3", 96, *([limits] if limits else []))
    d = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(tmp_path / "t.mp3"), "-f", "f32le", "-ac", "1", "-ar", "24000", "-"],
                                     capture_output=True).stdout, dtype=np.float32)
    n = min(len(x), len(d))
    lag = int(np.argmax(sig.correlate(x[:n], d[:n], "full", method="fft"))) - (n - 1)
    assert -lag == W.ENC_LAG


def test_compose_gaps_and_levels():
    np = _np()
    sr = 24000
    nr = config.load_settings()["narratorRu"]
    t = np.linspace(0, 1, sr // 2, endpoint=False)
    en = (0.05 * np.sin(2 * np.pi * 200 * t)).astype("float32")
    ru = (0.30 * np.sin(2 * np.pi * 300 * t)).astype("float32")
    job = {"parts": [{"kind": "en"}, {"kind": "ru"}, {"kind": "en"}]}
    y, offs = W.compose(job, [en, ru, en], nr, sr, random.Random(1))
    gaps = [offs[i + 1][0] - offs[i][1] for i in range(2)]
    assert all(0.149 <= g <= 0.251 for g in gaps)
    r = [W.act_rms(y[int(a * sr):int(b * sr)], sr) for a, b in offs]
    assert max(r) / min(r) < 1.15                      # Russian part brought to the English level
    assert len(y) / sr == pytest.approx(offs[-1][1], abs=1e-3)


# ---- second review: budgets, per-line loudness, scene-wide failures, atomic before-copy, real take through the limiter -----------------------
def test_match_loudness_refuses_a_take_that_needs_too_much_gain_or_limiting():
    pytest.importorskip("scipy")
    np = _need_audio()
    sr = 24000
    t = np.arange(2 * sr) / sr
    ref = (0.12 * np.sin(2 * np.pi * 300 * t)).astype("float32")
    rng = np.random.default_rng(5)
    quiet = (rng.standard_normal(2 * sr) * 0.0004).astype("float32")                  # about -60 dB: would need ~+40 dB
    with pytest.raises(W.LoudnessError, match="gain"):
        W.match_loudness(quiet, ref, sr)
    peaky = np.zeros(2 * sr, dtype="float32")                                           # a few huge clicks over a low floor: the limiter would eat them
    peaky += (rng.standard_normal(2 * sr) * 0.01).astype("float32")
    peaky[::2400] = 1.0
    peaky[1::2400] = -1.0
    loud_ref = (0.3 * np.sin(2 * np.pi * 300 * t)).astype("float32")
    with pytest.raises(W.LoudnessError):
        W.match_loudness(peaky, loud_ref, sr, max_limit_db=0.5)
    ok = W.match_loudness((ref * 0.5).astype("float32"), ref, sr)                       # +6 dB: within budget
    assert float(np.abs(ok).max()) <= W.LIMIT + 1e-6


def test_a_stored_take_goes_through_the_limiter_without_clipping_or_a_big_cut():
    """A real F5 take from the render store (read-only), scaled to a typical narrator level: the limiter touches it by only a few dB."""
    pytest.importorskip("scipy")
    np = _need_audio()
    import audio
    import soundfile as sf
    takes = sorted(Path(config.STORE, "cache", "tts").glob("*.flac"), key=lambda p: p.stat().st_size) if Path(config.STORE, "cache", "tts").is_dir() else []
    if not takes:
        pytest.skip("no stored takes here")
    for tk in takes[:40]:                                           # the smallest take with something in it
        y, sr = sf.read(str(tk), dtype="float32")
        y = y if y.ndim == 1 else y.mean(axis=1)
        lo = audio.lufs(y, sr)
        if len(y) > sr * 0.5 and np.isfinite(lo):
            break
    else:
        pytest.skip("no audible stored take here")
    y = (y * np.float32(10 ** ((-23 - lo) / 20))).astype("float32")                   # a take as the compose step hands it over
    ref = (y * np.float32(10 ** (3 / 20))).astype("float32")                           # a narrator line 3 dB louder, about -17 LUFS
    z = W.match_loudness(y, ref, sr)
    assert float(np.abs(z).max()) <= W.LIMIT + 1e-6
    assert abs(audio.lufs(z, sr) - audio.lufs(ref, sr)) < 0.15
    assert audio.lufs(y * np.float32(10 ** (3 / 20)), sr) - audio.lufs(z, sr) < 3.0     # the limiter took less than 3 dB off


def test_a_replaced_line_off_the_original_level_is_dropped_and_the_rest_of_the_scene_is_built(scene, monkeypatch):
    real, calls = W.match_loudness, []

    def second_too_quiet(*a, **k):
        z = real(*a, **k)
        calls.append(1)
        return z * (0.3 if len(calls) == 2 else 1.0)                 # the second line comes out about 10 dB under the line it replaces
    monkeypatch.setattr(W, "match_loudness", second_too_quiet)
    plan = scene.plan()
    scene.tones(plan, level=0.1)
    res = scene.build(plan)
    assert res["scenes"] == 1 and res["lines"] == 1 and res["failed"] == 1, res
    f = res["failures"][0]
    assert f["sticky"] and "LU" in f["why"] and (f["seg"], f["i"]) == (1, 1)
    assert narrator_lines(scene.meta()) == [(1, 0)]                  # the good line is narrated, the bad one keeps sky
    assert scene.plan()["knownFailed"] == 1


def test_a_scene_where_every_line_is_off_level_keeps_its_audio(scene):
    scene.settings["narratorRu"]["lineLoudnessTolLU"] = 0.0001
    scene.write_settings()
    plan = scene.plan()
    scene.tones(plan, level=0.1)
    snap = (scene.store / SID / "audio.mp3").read_bytes()
    res = scene.build(plan)
    assert res["scenes"] == 0 and res["failed"] == 2 and (scene.store / SID / "audio.mp3").read_bytes() == snap
    assert all(f["sticky"] for f in res["failures"])


def test_a_scene_wide_failure_is_remembered_only_the_second_time(scene, monkeypatch):
    def boom(*a, **k):
        raise W.SceneSkip("word times not monotonic", sticky=False, kind="monotonic")
    monkeypatch.setattr(W, "round_docs", boom)
    plan = scene.plan()
    scene.tones(plan)
    res = scene.build(plan)
    assert res["scenes"] == 0 and not res["failures"][0]["sticky"] and res["failed"] == 2
    assert scene.plan()["knownFailed"] == 0                          # the first time it may be transient: tried again
    res = scene.build(scene.plan())
    assert res["failures"][0]["sticky"] and "remembered" in res["failures"][0]["why"]
    assert scene.plan()["knownFailed"] == 2                          # the second time it is final for this render and version


def test_ensure_original_swaps_the_before_copy_atomically(scene, monkeypatch):
    plan = scene.plan()
    scene.tones(plan)
    st = narrator_store(scene.store)
    base, _ = W.ensure_original(st, SID, False)
    assert base == scene.store / ".narrator-before" / SID
    marker = base / "marker"
    marker.write_text("old")
    (scene.store / SID / "meta.json").write_text(json.dumps({**scene.meta(), "renderKey": "other"}))   # a newer render: the copy must be refreshed
    calls = []
    import store as S
    real = S.exchange_dirs
    monkeypatch.setattr(S, "exchange_dirs", lambda a, b: calls.append((a, b)) or real(a, b))
    base, _ = W.ensure_original(st, SID, False)
    assert len(calls) == 1 and not (base / "marker").exists() and (base / "audio.mp3").exists()
    assert json.loads((base / "meta.json").read_text())["renderKey"] == "other"
    assert not [p for p in (scene.store / ".narrator-before").iterdir() if p.name != SID]


def narrator_store(root):
    import store as S
    return S.Store(root)


def test_a_pristine_live_scene_is_the_original_even_when_a_before_copy_exists(scene):
    plan = scene.plan()
    scene.tones(plan)
    scene.build(plan)                                                # now a before-copy exists and the live scene is narrated
    d, lm, note = narrator.original_dir(scene.store, SID)
    assert note == "before" and d == scene.store / ".narrator-before" / SID
    shutil.rmtree(scene.store / SID)
    shutil.copytree(scene.store / ".narrator-before" / SID, scene.store / SID)   # the live scene is the pristine render again
    d, lm, note = narrator.original_dir(scene.store, SID)
    assert note == "live" and d == scene.store / SID


def test_publisher_waits_for_the_publish_lock_and_gives_up_with_75(tmp_path, monkeypatch):
    sys.path.insert(0, str(HERE.parents[1] / "publish"))
    try:
        L = pytest.importorskip("rulisten_pub.lock")   # the publisher lives in the private app repo
    finally:
        sys.path.pop(0)
    path = tmp_path / "publish.lock"
    holder = subprocess.Popen(["flock", str(path), "sleep", "1.2"])
    time.sleep(0.3)
    t0 = time.time()
    with L.publish_lock(path, timeout=10, log=lambda *a: None):
        assert time.time() - t0 >= 0.6
    holder.wait()
    with flock_ctx(path):
        with pytest.raises(L.LockTimeout):
            with L.publish_lock(path, timeout=0.3, log=lambda *a: None):
                pass


def test_content_checkout_that_differs_from_the_render_refuses_the_run(scene):
    nd = scene.content / "out" / "kukhnya" / "s01e01" / "scene-01.notes.json"
    notes = json.loads(nd.read_text("utf-8"))
    notes["lines"][0]["trans"] += " (edited)"
    nd.write_text(json.dumps(notes, ensure_ascii=False), "utf-8")
    with pytest.raises(narrator.ContentMismatch, match="contentHash"):
        scene.plan()


def test_batch_script_needs_an_explicit_content_checkout(tmp_path):
    env = {k: v for k, v in __import__("os").environ.items() if k != "OVERHEAR_CONTENT"}
    r = subprocess.run(["bash", str(HERE / "narrator_batch.sh"), "kukhnya-s01e01"], env=env, capture_output=True, text=True)
    assert r.returncode == 2 and "OVERHEAR_CONTENT" in r.stderr


def test_fragment_acceptance_judges_only_unquoted_english():
    import narrator_work as n
    cfg = {"enCer": 0.15, "ruCer": 0.15}
    assert n.is_fragment('is "pere-", over, plus') and n.is_fragment("Slowly now.") and not n.is_fragment("This is a long ordinary sentence with many words in it.")
    assert n.unquoted_words('is "pere-", over, plus') == ["is", "over", "plus"]
    assert n.unquoted_words('had "pri-".') == ["had"]
    assert n.passes("en", 'is "pere-", over, plus', "is pair a over plus", cfg)[0]
    assert not n.passes("en", 'is "pere-", over, plus', "is pair a plus over", cfg)[0]      # order matters
    assert not n.passes("en", 'is "serve", and', "is serve", cfg)[0]                          # a dropped English word fails
    assert n.passes("en", "Where is my favorite fish knife?", "Where is my favourite fish knife?", cfg)[0]   # old rule still accepts spelling variants
    assert n.duration_ok('is "serve", and', 1.2) and not n.duration_ok('is "serve", and', 0.4) and n.duration_ok("x", None)
    assert n.duration_ok("the stove.", 0.58)                   # F5's quantised lengths: a short correct take is not rejected


def test_fragment_gate_hears_quotes_names_and_numbers():
    import narrator_work as n
    cfg = {"enCer": 0.15, "ruCer": 0.15}
    # a skipped quoted gloss fails even when the unquoted words are all there
    assert not n.passes("en", 'is "I remember", and', "and", cfg)[0]
    assert n.passes("en", 'is "I remember", and', "as I remember, and", cfg)[0]
    assert not n.passes("en", 'the polite "you", for her boss', "The polite for her boss", cfg)[0]
    assert n.quotes_heard('is "povtor", and', ["puff", "tour", "and"])         # two words run together
    assert n.quotes_heard('had "-sya".', ["had"])                              # hyphen syllables are left to the duration test
    # names match by sound, ordinary words never do
    names = {"ainura"}
    assert n.word_like("ainura", "newer", names) and not n.word_like("ainura", "kanra", names)
    assert not n.word_like("smile", "small", set()) and not n.word_like("built", "flat", set())
    assert n.word_like("carrie", "carry", set())                               # homophone spelling
    assert not n.passes("en", "Pay attention, Vika.", "Pay tension, Vika.", cfg)[0]   # dropped syllable
    # numbers: Whisper writes digits
    assert n.spell_numbers("£20,000") .split() == ["twenty", "thousand", "pounds"]
    assert n.passes("en", "It costs twenty thousand pounds.", "It costs £20,000.", cfg)[0]
    # short Russian words on the consonant skeleton, only for Cyrillic transcripts
    assert n.passes("ru", "мог", "мок", cfg)[0] and not n.passes("ru", "мог", "mok", cfg)[0]


def test_f5_reads_english_without_quote_marks():
    assert narrator.f5_text('is "vile", and') == "is vile, and"
    assert narrator.f5_text("the polite \u201cyou\u201d, for her") == "the polite you, for her"
    assert narrator.f5_text("Vika's knife") == "Vika's knife"                  # apostrophes stay


def test_fragment_takes_slow_down_by_take_index_full_lines_do_not():
    sp = config.load_settings(None)["narratorRu"]["fragmentSpeeds"]
    assert sp[0] == 1.0 and sorted(sp, reverse=True) == sp
    assert [W.take_speed('is "loudly", and', k, sp) for k in range(len(sp))] == sp
    assert W.take_speed('is "loudly", and', len(sp), sp) == sp[0]
    assert W.take_speed("This is a long ordinary sentence of plain English words.", 3, sp) == 1.0


@pytest.mark.parametrize("ref,hyp", [('"for".', "Four."), ('"for".', "4."), ("takes -u.", "takes you.")])
def test_short_homophones_pass_the_fragment_gate(ref, hyp):
    assert W.passes("en", ref, hyp, config.load_settings(None)["narratorRu"])[0]


def test_a_swallowed_gloss_still_fails():
    assert not W.passes("en", 'is "loudly", and', "and", config.load_settings(None)["narratorRu"])[0]


@pytest.mark.parametrize("ref,hyp,ok", [
    ('is "or".', "is awe.", True),
    ('is "or".', "is all.", False),
    ('"our", is what makes the cook sound like one of the family.', "R is what makes the cook sound like one of the family.", True),
    ('"our", is what makes the cook sound like one of the family.', "is what makes the cook sound like one of the family.", False),
    ('is "asked", also with -la for Vika.', "is asked also with La Favica.", True),
    ('is "asked", also with -la for Vika.', "is asked also with La.", False),
    ("the stove for Vika", "the stove Favor", False),
])
def test_non_rhotic_or_and_a_word_run_into_a_name(ref, hyp, ok):
    assert W.passes("en", ref, hyp, config.load_settings(None)["narratorRu"])[0] is ok
