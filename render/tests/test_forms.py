import json
from types import SimpleNamespace
import pytest

import clips
import config
import forms
from voices import Voices

TABLE = {"title": "Declension", "columns": ["", "sg", "pl"],
         "rows": [{"cells": ["nominative", "вино", "вина"]}, {"cells": ["genitive", "вина", "вин"]}, {"cells": ["accusative", "вино / вина", "-"]}]}


def scene(table=TABLE, lemma="вино", lang="ru", pair="ru-en", stress="вино́", words=(), meanings=1, pos="noun"):
    entry = {"lemma": lemma, "pos": pos, "stress": stress, "meanings": [{}] * meanings, "forms": table, "moreForms": []}
    return SimpleNamespace(lang=lang, pair=pair, notes={"lexicon": {lemma: entry}, "lines": [{"words": list(words)}]})


def settings(with_french=False):
    """The real settings, except that the (large, untracked) dictionary dump is not read."""
    s = config.load_settings()
    s["forms"]["dictionary"] = None
    if not with_french:
        s["forms"]["voices"].pop("fr", None)
    return s


def test_french_or_empty_scene_selection_preserves_published_russian_form_plan(tmp_path, monkeypatch):
    import pipeline
    folder = tmp_path / "forms"
    folder.mkdir()
    plan = folder / ".plan.json"
    review = folder / "review.jsonl"
    before = b'[{"id":"published-russian-form","ckey":"checked"}]'
    plan.write_bytes(before)
    review.write_bytes(b'previous review\n')

    def unexpected(*args, **kwargs):
        raise AssertionError("No form planning or synthesis is needed for these scenes")

    monkeypatch.setattr(forms, "plan", unexpected)
    monkeypatch.setattr(pipeline, "run_stage", unexpected)
    for selected in [[], [scene(lang="fr", pair="fr-en")]]:
        result = pipeline.run_forms(SimpleNamespace(store=tmp_path), settings(), None,
                                    SimpleNamespace(root=tmp_path), selected, log=lambda _: None)
        assert result["pending"] == result["passed"] == result["failed"] == 0
        assert plan.read_bytes() == before
        assert review.read_bytes() == b'previous review\n'


class FakeAccent:
    """RuAccent stand-in: puts a mark on the first vowel of every word of every string; remembers what it was asked."""
    def __init__(self, table=None):
        self.asked, self.table = [], table or {}

    def __call__(self, strings):
        self.asked += list(strings)
        out = []
        for s in strings:
            if s in self.table:
                out.append(self.table[s])
                continue
            out.append(" ".join(next(("".join(w[:i + 1] + "́" + w[i + 1:]) for i, c in enumerate(w) if c in "аеиоуыэюя"), w) for w in s.split(" ")))
        return out


def texts(items):
    return {i.id: i.sents[0].tts for i in items}


def test_form_id_pinned_and_shared_with_the_publisher():
    assert forms.form_id("ru-en", "резать", "Present", "я", "sg", "режу") == "a66c90062ae484e3"
    base = ("ru-en", "вино", "Declension", "genitive", "sg", "вина")
    assert forms.form_id(*base) != forms.form_id("ru-en", "вино", "Declension", "nominative", "pl", "вина")      # the slot is part of the identity
    assert forms.form_id(*base) != forms.form_id("ru-en", "другое", *base[2:])


def test_slots_skip_the_label_column_and_dashes():
    assert [(s.row, s.column, s.cell) for s in forms.slots_of(scene().notes["lexicon"]["вино"])] == [
        ("nominative", "sg", "вино"), ("genitive", "sg", "вина"), ("accusative", "sg", "вино / вина"), ("nominative", "pl", "вина"), ("genitive", "pl", "вин")]
    assert forms.pieces("вино / вина") == ["вино", "вина"]


def test_the_same_spelling_stressed_differently_in_two_slots_gets_no_audio():
    s, v = settings(), Voices()
    # вино: genitive singular вина́, nominative plural ви́на; RuAccent reads the sg column and the pl column differently
    ra = FakeAccent({"вино, вина, вино, вина": "вино́, вина́, вино́, вина́", "вина, вин": "ви́на, вин", "вино": "вино́", "вина": "вина́"})
    items, stats = forms.plan([scene()], s, v, ra)
    got = {i.text: i.sents[0].tts for i in items}
    assert "вина" not in got and "вино / вина" not in got and stats["ambiguous"] == 3     # every slot that holds the spelling вина: none plays
    assert got["вин"] == "вин" and got["вино"] == "вино́"          # вино: nominative singular only (the accusative cell holds вина too: no audio)
    assert len([i for i in items if i.text == "вино"]) == 1


def test_рука_genitive_singular_and_nominative_plural_are_not_guessed():
    s, v = settings(), Voices()
    table = {"title": "Declension", "columns": ["", "sg", "pl"], "rows": [
        {"cells": ["nominative", "рука", "руки"]}, {"cells": ["genitive", "руки", "рук"]}]}
    ra = FakeAccent({"рука, руки": "рука́, руки́", "руки, рук": "ру́ки, рук"})
    items, stats = forms.plan([scene(table, "рука", stress="рука́")], s, v, ra)
    assert {i.text for i in items} == {"рука", "рук"} and (stats["slots"], stats["ambiguous"]) == (4, 2)


def test_the_same_spelling_with_the_same_stress_everywhere_keeps_every_slot():
    s, v = settings(), Voices()
    table = {"title": "Declension", "columns": ["", "m"], "rows": [{"cells": ["nominative", "новый"]}, {"cells": ["accusative", "новый"]}]}
    items, stats = forms.plan([scene(table, "новый", stress="но́вый")], s, v, FakeAccent())
    assert [i.text for i in items] == ["новый", "новый"] and len({i.id for i in items}) == 2 and stats["ambiguous"] == 0
    assert len({i.sents[0].key for i in items}) == 1                 # one synthesis serves both slots


def test_a_form_the_notes_stress_two_ways_for_the_lemma_gets_no_audio():
    s, v = settings(), Voices()
    words = [{"t": "вина", "lemma": "вино", "stress": "вина́"}, {"t": "вина", "lemma": "вино", "stress": "ви́на"}]
    items, stats = forms.plan([scene(words=words)], s, v, FakeAccent())
    assert "вина" not in {i.text for i in items}


def test_stress_comes_from_the_notes_then_the_lemma_then_ruaccent_over_the_column():
    s, v = settings(), Voices()
    ra = FakeAccent()
    table = {"title": "T", "columns": ["", "a"], "rows": [{"cells": ["x", "вино"]}, {"cells": ["y", "стола"]}, {"cells": ["z", "вин"]}, {"cells": ["w", "дома / окна"]}]}
    words = [{"t": "стола,", "lemma": "вино", "stress": "стола́"}]
    items, _ = forms.plan([scene(table, words=words)], s, v, ra)
    got = {i.text: i.sents[0].tts for i in items}
    assert got["стола"] == "стола́"                                  # the notes' own stress for that surface form of that lemma
    assert got["вино"] == "вино́"                                    # the lemma's stress
    assert got["вин"] == "вин"                                       # one vowel: no mark
    assert got["дома / окна"] == "до́ма, о́кна"                      # RuAccent over the column
    assert any("вино, стола, вин, дома, окна" in a for a in ra.asked)


def test_one_entry_per_lemma_the_one_the_publisher_shows():
    s, v = settings(), Voices()
    other = {"title": "Declension", "columns": ["", "sg"], "rows": [{"cells": ["nominative", "вино"]}, {"cells": ["genitive", "вины"]}]}
    items, _ = forms.plan([scene(), scene(other, meanings=1)], s, v, FakeAccent())          # tie: the earliest scene's table
    assert "вины" not in {i.text for i in items}
    items, _ = forms.plan([scene(), scene(other, meanings=2)], s, v, FakeAccent())          # more meanings wins
    assert {i.text for i in items} == {"вино", "вины"}


def test_a_language_without_a_voice_has_no_forms_and_a_mark_never_changes_the_letters():
    s, v = settings(), Voices()
    assert forms.plan([scene(lang="fr", pair="fr-en")], s, v)[0] == []
    bad = lambda strings: ["xyz" for _ in strings]                   # RuAccent returning something else is ignored
    got, _ = forms.plan([scene(stress="")], s, v, bad)
    assert all(i.sents[0].tts.replace("́", "") == ", ".join(forms.pieces(i.text)) for i in got)


def french_scene(cells=("je suis", "il / elle est", "ils/elles sont"), lemma="être"):
    table = {"title": "Present", "columns": ["", "form"],
             "rows": [{"cells": [str(i), cell]} for i, cell in enumerate(cells)]}
    return scene(table, lemma, lang="fr", pair="fr-en", stress="", pos="verb")


def test_french_forms_use_lucie_base_qwen_without_russian_lora():
    s = settings(with_french=True)
    fs = forms.forms_settings(s, "fr")
    assert not fs["lora"]["enabled"] and fs["tts"]["batch"] <= 4
    assert s["forms"]["lora"] and forms.forms_settings(s, "ru")["lora"]["enabled"]
    items, stats = forms.plan([french_scene()], s, Voices())
    assert stats["ambiguous"] == 0
    assert {i.voice for i in items} == {"lucie"}
    assert [i.sents[0].tts for i in items] == ["je suis", "il est, elle est", "ils sont, elles sont"]
    assert all(i.sents[0].plain == i.sents[0].tts for i in items)


@pytest.mark.parametrize(("written", "spoken"), [
    ("il/elle est allé(e)", "il est allé, elle est allé"),
    ("ils / elles sont venu(e)(s)", "ils sont venu, elles sont venu"),
    ("le/la/l'", None), ("qu’", None), ("pris(e)", None),
    ("petit(e)", None), ("nous (optionnel)", None),
])
def test_french_notation_is_expanded_only_when_pronunciation_is_known(written, spoken):
    assert forms.french_form_text(written) == spoken


def test_adding_french_preserves_the_original_russian_audio_cache_keys():
    s, v = settings(), Voices()
    old, _ = forms.plan([scene()], s, v, FakeAccent())
    new, _ = forms.plan([scene(), french_scene()], settings(with_french=True), v, FakeAccent())
    ru = [i for i in new if i.lang == "ru"]
    assert [(i.id, i.ckey, i.sents[0].key) for i in ru] == [(i.id, i.ckey, i.sents[0].key) for i in old]
    # Pin against the original pre-French assembly signature too.
    old_asig = config.sha({"forms": {k: val for k, val in s["forms"].items()
                                   if k not in ("gpu", "prio", "batch", "chunk", "dictionary")},
                           "audio": s["audio"], "version": "f2"})
    assert all(i.ckey == config.sha({"sents": [i.sents[0].key], "assembly": old_asig}) for i in ru)


def test_french_plan_merge_keeps_russian_audio_and_unselected_lemmas(tmp_path):
    s, v = settings(with_french=True), Voices()
    russian = forms.plan([scene()], s, v, FakeAccent())[0]
    other = forms.plan([french_scene(("j'ai",), "avoir")], s, v)[0]
    selected = french_scene(("je suis", "pris(e)"))
    items, stats = forms.plan([selected], s, v)
    forms.write_plan(russian + other, tmp_path)
    path = forms.plan_path(tmp_path)
    old_rows = json.loads(path.read_text())
    refused_id = forms.form_id("fr-en", "être", "Present", "1", "form", "pris(e)")
    path.write_text(json.dumps(old_rows + [{"id": refused_id, "ckey": "old unsafe audio"}]))
    cs = clips.ClipStore(tmp_path, forms.KIND)
    for item in russian:
        (cs.dir / f"{item.id}.mp3").write_bytes(b"checked audio")
        (cs.dir / f"{item.id}.json").write_text(json.dumps({"ckey": item.ckey, "status": "ok"}))
    forms.write_plan(items, tmp_path, replace_ids=forms.slot_ids([selected], s))
    after = json.loads(path.read_text())
    assert after[:len(old_rows)] == old_rows
    assert refused_id not in {row["id"] for row in after}
    assert {row["id"] for row in after} == {i.id for i in russian + other + items}
    assert not forms.pending(russian, tmp_path)
    assert stats["ambiguous"] == 1
    assert stats["resolved_by_dictionary"] == 0


def test_scoped_plan_update_fails_closed_on_invalid_existing_data(tmp_path):
    folder = tmp_path / "forms"
    folder.mkdir()
    path = folder / ".plan.json"
    path.write_text('{"wrong":"shape"}')
    with pytest.raises(ValueError, match="not an array"):
        forms.write_plan([], tmp_path, replace_ids=set())
    assert path.read_text() == '{"wrong":"shape"}'


def test_french_review_update_preserves_russian_and_other_lemma_review(tmp_path):
    folder = tmp_path / "forms"
    folder.mkdir()
    path = folder / "review.jsonl"
    kept = [{"pair": "ru-en", "lemma": "вино", "cell": "вина"},
            {"pair": "fr-en", "lemma": "avoir", "cell": "other"}]
    path.write_text("".join(json.dumps(row) + "\n" for row in kept + [{"pair": "fr-en", "lemma": "être", "cell": "stale"}]))
    replacement = {"pair": "fr-en", "lemma": "être", "cell": "pris(e)"}
    forms.write_review([replacement], tmp_path, [french_scene()], settings(with_french=True))
    assert [json.loads(line) for line in path.read_text().splitlines()] == kept + [replacement]


def test_french_asr_compares_spoken_forms_and_never_expands_russian_numbers(monkeypatch):
    import clip_asr
    record = {"lang": "fr", "text": "il/elle est", "tts": "il est, elle est"}
    def unexpected(*args):
        raise AssertionError("Russian number expansion cannot process French")
    monkeypatch.setattr(clip_asr.numwords, "expand", unexpected)
    assert clip_asr.comparison_texts(record, "forms", "il est, elle est") == (record["tts"], "il est, elle est")
    assert clip_asr.comparison_texts(record, "forms", "4") == (record["tts"], "4")
    assert clip_asr.comparison_texts(record, "clips", "il est") == (record["text"], "il est")


def test_french_asr_keeps_strict_cer_even_when_russian_folding_is_requested():
    pytest.importorskip("jiwer")
    import clip_asr
    record = {"lang": "fr", "text": "il/elle est", "tts": "il est, elle est"}
    assert clip_asr.comparison_cer(record, "forms", "Il est, elle est.", True) == 0
    assert clip_asr.comparison_cer(record, "forms", "Il est.", True) > 0.15
    assert clip_asr.comparison_cer({"lang": "fr", "text": "quatre", "tts": "quatre"}, "forms", "4", True) > 0.15
    assert clip_asr.comparison_cer({"lang": "fr", "text": "parlé", "tts": "parlé"}, "forms", "parle", True) > 0.15
    assert clip_asr.comparison_cer({"lang": "fr", "text": "parlé", "tts": "parlé"}, "forms", "parle\u0301.", True) == 0


def test_keys_follow_voice_text_lora_and_assembly():
    s, v = settings(), Voices()
    a = forms.plan([scene()], s, v, FakeAccent())[0][0]
    s2 = json.loads(json.dumps(s))
    s2["forms"]["programLufs"] = -18.0
    b = forms.plan([scene()], s2, v, FakeAccent())[0][0]
    assert b.ckey != a.ckey and b.sents[0].key == a.sents[0].key          # loudness: re-assemble, no new synthesis
    s3 = json.loads(json.dumps(s))
    s3["forms"]["batch"], s3["forms"]["chunk"] = 1, 7
    assert forms.plan([scene()], s3, v, FakeAccent())[0][0].ckey == a.ckey   # batch and chunk are not part of the audio
    s4 = json.loads(json.dumps(s))
    s4["forms"]["lora"] = False
    assert forms.plan([scene()], s4, v, FakeAccent())[0][0].sents[0].key != a.sents[0].key
    ex = clips.plan_scene(SimpleNamespace(lang="ru", pair="ru-en", notes={"lexicon": {"w": {"examples": [{"text": "вино", "trans": "x"}]}}}), s, v)[0]
    assert ex.sents[0].key != a.sents[0].key                              # never shares audio with the plain-model example clips


def test_plan_file_roundtrip_commit_fail_and_retake_selection(tmp_path):
    s, v = settings(), Voices()
    items = forms.plan([scene()], s, v, FakeAccent())[0]
    forms.write_plan(items, tmp_path)
    back = forms.read_plan(tmp_path)
    assert [(i.id, i.ckey, i.sents[0].key, i.sents[0].tts) for i in back] == [(i.id, i.ckey, i.sents[0].key, i.sents[0].tts) for i in items]
    assert [i.id for i in forms.read_plan(tmp_path, [items[1].id])] == [items[1].id]
    cs = clips.ClipStore(tmp_path, forms.KIND)
    for i in back[:2]:
        (cs.work / f"{i.id}.mp3").write_bytes(b"mp3")
        cs.write_work(i.id, {"id": i.id, "pair": i.pair, "text": i.text, "lang": i.lang, "voice": i.voice, "ckey": i.ckey, "tries": 0, "durationSec": 0.7})
    clips.commit(tmp_path, back[0].id, 0.0, "вино", None, forms.KIND)
    clips.fail_final(tmp_path, back[1].id, 0.9, "что-то", forms.KIND)
    assert cs.record(back[0].id)["status"] == "ok" and (cs.dir / f"{back[0].id}.mp3").exists()
    assert cs.record(back[1].id)["status"] == "failed" and not (cs.dir / f"{back[1].id}.mp3").exists()
    assert [i.id for i in forms.pending(back, tmp_path)] == [i.id for i in back[2:]]       # only the missing ones are rendered
    assert not (tmp_path / "clips" / f"{back[0].id}.json").exists()                         # forms never write into the example clips
    cs.write_work(back[2].id, {"ckey": back[2].ckey, "tries": 0, "failedCheck": True})
    assert [i.id for i in clips.retakes_among(back, cs, 1)] == [back[2].id]


def test_the_whisper_check_folds_unstressed_vowels_only():
    import clip_asr
    f = clip_asr.folded_cer
    assert f("гостя́", "Гастя") == 0 and f("вино́", "Вино.") == 0 and f("весь, всего́", "Весь, всего.") == 0
    assert f("го́стя", "Гастя") > 0.15 and f("вино́", "вина") > 0.15 and f("вина́", "вино") > 0.15    # a wrong ending on a stressed vowel still fails
    assert f("дне", "дни") > 0.15 and f("ви́на", "вино") > 0.15                                         # a lone vowel is stressed; so is a marked one
    assert f("вино", "вина") > 0.15                                                                      # no mark: no stress known: no folding


class FakeDict:
    """form_dict.FormDict stand-in: {(lemma, title, row, column, letters): stressed form}."""
    def __init__(self, table):
        self.table = table

    def slot_stress(self, pos, lemma, title, row, column, piece):
        return self.table.get((lemma, title, row, column, piece))


def with_dict(table):
    return FakeDict(table)


def planned(scene_, fd, ra=None):
    """{slot id: text for the model} with the dictionary."""
    import textprep as tp
    known = forms.stress_map([scene_])
    entry = next(iter(scene_.notes["lexicon"].values()))
    return {(sl.row, sl.column, sl.cell): t for sl, t, _ in forms.entry_texts(entry, known, ra or FakeAccent(), fd, "noun")}


def test_the_dictionary_gives_every_slot_its_own_stress_even_for_one_spelling():
    fd = with_dict({("вино", "Declension", "genitive", "sg", "вина"): "вина́", ("вино", "Declension", "nominative", "pl", "вина"): "ви́на",
                    ("вино", "Declension", "accusative", "sg", "вина"): "вина́", ("вино", "Declension", "accusative", "sg", "вино"): "вино́",
                    ("вино", "Declension", "nominative", "sg", "вино"): "вино́"})
    got = planned(scene(), fd)
    assert got[("genitive", "sg", "вина")] == "вина́" and got[("nominative", "pl", "вина")] == "ви́на"       # one spelling, two stresses
    assert got[("accusative", "sg", "вино / вина")] == "вино́, вина́"                                          # the piece of a two-form cell too


def test_рука_окно_each_slot_gets_its_dictionary_stress():
    d = {("рука", "Declension", "genitive", "sg", "руки"): "руки́", ("рука", "Declension", "nominative", "pl", "руки"): "ру́ки",
         ("рука", "Declension", "nominative", "sg", "рука"): "рука́", ("рука", "Declension", "genitive", "pl", "рук"): "рук"}
    table = {"title": "Declension", "columns": ["", "sg", "pl"], "rows": [{"cells": ["nominative", "рука", "руки"]}, {"cells": ["genitive", "руки", "рук"]}]}
    got = planned(scene(table, "рука", stress="рука́"), with_dict(d))
    assert got[("genitive", "sg", "руки")] == "руки́" and got[("nominative", "pl", "руки")] == "ру́ки" and got[("genitive", "pl", "рук")] == "рук"
    d = {("окно", "Declension", "genitive", "sg", "окна"): "окна́", ("окно", "Declension", "nominative", "pl", "окна"): "о́кна"}
    table = {"title": "Declension", "columns": ["", "sg", "pl"], "rows": [{"cells": ["genitive", "окна", "-"]}, {"cells": ["nominative", "-", "окна"]}]}
    got = planned(scene(table, "окно", stress="окно́"), with_dict(d))
    assert got[("genitive", "sg", "окна")] == "окна́" and got[("nominative", "pl", "окна")] == "о́кна"


def test_a_verb_with_moving_stress_жить():
    d = {("жить", "Past", "past", "m", "жил"): "жи́л", ("жить", "Past", "past", "f", "жила"): "жила́", ("жить", "Past", "past", "pl", "жили"): "жи́ли",
         ("жить", "Present", "1st", "sg", "живу"): "живу́"}
    past = {"title": "Past", "columns": ["", "m", "f", "n", "pl"], "rows": [{"cells": ["past", "жил", "жила", "жило", "жили"]}]}
    present = {"title": "Present", "columns": ["", "sg", "pl"], "rows": [{"cells": ["1st", "живу", "живём"]}]}
    sc = scene(past, "жить", stress="жи́ть", pos="verb")
    sc.notes["lexicon"]["жить"]["moreForms"] = [present]
    got = planned(sc, with_dict(d))
    assert got[("past", "m", "жил")] == "жил"    # one vowel: no mark and got[("past", "f", "жила")] == "жила́" and got[("past", "pl", "жили")] == "жи́ли"
    assert got[("1st", "sg", "живу")] == "живу́"


def test_no_dictionary_stress_and_disagreeing_readings_leave_the_slot_silent_with_its_candidates():
    ra = FakeAccent({"вино, вина, вино, вина": "вино́, вина́, вино́, вина́", "вина, вин": "ви́на, вин", "вино": "вино́", "вина": "вина́"})
    entry = scene().notes["lexicon"]["вино"]
    rows = forms.entry_texts(entry, {}, ra, FakeDict({}), "noun")
    silent = [(sl.row, sl.column, why["candidates"]) for sl, t, why in rows if t is None]
    assert ("genitive", "sg", {"вина": ["ви́на", "вина́"]}) in silent and len(silent) == 3
    # the dictionary settles two of the three slots of the spelling; the third has no slot-specific stress and now contradicts them
    fd = FakeDict({("вино", "Declension", "genitive", "sg", "вина"): "вина́", ("вино", "Declension", "nominative", "pl", "вина"): "ви́на"})
    rest = [(sl.row, sl.column) for sl, t, _ in forms.entry_texts(entry, {}, ra, fd, "noun") if t is None]
    assert rest == [("accusative", "sg")]


def test_the_plan_counts_what_the_dictionary_resolved(tmp_path):
    import json as _json
    dump = tmp_path / "ru.jsonl"
    forms_ = [{"form": "вино́", "tags": ["nominative", "singular"]}, {"form": "вина́", "tags": ["genitive", "singular"]}, {"form": "ви́на", "tags": ["nominative", "plural"]},
              {"form": "ви́н", "tags": ["genitive", "plural"]}, {"form": "вино́", "tags": ["accusative", "singular"]}, {"form": "вина́", "tags": ["dated", "genitive", "singular"]}]
    dump.write_text(_json.dumps({"word": "вино", "lang_code": "ru", "pos": "noun", "forms": forms_}, ensure_ascii=False) + "\nnot json\n", "utf-8")
    s, v = settings(), Voices()
    ra = FakeAccent({"вино, вина, вино, вина": "вино́, вина́, вино́, вина́", "вина, вин": "ви́на, вин", "вино": "вино́", "вина": "вина́"})
    items, without = forms.plan([scene()], s, v, ra)
    s["forms"]["dictionary"] = str(dump)
    items2, stats = forms.plan([scene()], s, v, ra)
    assert without["dictionary"] is False and stats["dictionary"] is True
    assert stats["ambiguous_without_dictionary"] == without["ambiguous"] == 3 and stats["ambiguous"] <= 1
    assert stats["resolved_by_dictionary"] == 3 - stats["ambiguous"] and len(stats["review"]) == stats["ambiguous"]
    got = {(i.text, i.sents[0].tts) for i in items2}
    assert ("вина", "вина́") in got and ("вина", "ви́на") in got


def test_the_reviewed_overrides_are_well_formed_and_fill_only_silent_slots():
    import form_overrides
    import form_dict
    table = form_overrides.table()                       # raises when a text is not the cell's letters
    assert table and all(form_dict.letters(text) == form_dict.letters(cell) for (lemma, cell), es in table.items() for _, text, _ in es)
    assert all(text.count("́") >= 1 for es in table.values() for _, text, _ in es)           # every override marks a stress
    ra = FakeAccent({"вино, вина, вино, вина": "вино́, вина́, вино́, вина́", "вина, вин": "ви́на, вин", "вино": "вино́", "вина": "вина́"})
    entry = scene().notes["lexicon"]["вино"]
    # an override for a spelling of this lemma fills exactly the slots that were silent
    form_overrides.table.cache_clear()
    import json as _json
    orig = form_overrides.PATH
    try:
        import tempfile, pathlib
        p = pathlib.Path(tempfile.mkdtemp()) / "o.json"
        p.write_text(_json.dumps({"entries": [{"lemma": "вино", "cell": "вина", "text": "вина́", "slots": [["Declension", "genitive", "sg"]], "why": "test"}]}, ensure_ascii=False), "utf-8")
        form_overrides.PATH = p
        form_overrides.table.cache_clear()
        rows = forms.entry_texts(entry, {}, ra, FakeDict({}), "noun")
        got = {(sl.row, sl.column): (t, why) for sl, t, why in rows}
        assert got[("genitive", "sg")] == ("вина́", {"override": "test"})
        assert got[("nominative", "pl")][0] is None                     # the other slot of the spelling is still silent
        assert forms.entry_texts(entry, {}, ra, FakeDict({}), "noun", use_overrides=False)[1][1] is None
        p.write_text(_json.dumps({"entries": [{"lemma": "вино", "cell": "вина", "text": "вода́", "slots": "all", "why": "x"}]}), "utf-8")
        form_overrides.table.cache_clear()
        try:
            form_overrides.table()
            assert False, "a text with other letters must be refused"
        except ValueError:
            pass
    finally:
        form_overrides.PATH = orig
        form_overrides.table.cache_clear()


def test_the_audit_lists_cells_that_are_not_the_dictionarys_form_for_the_slot():
    import sys
    sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[1] / "tools"))
    import audit_forms

    class D:
        def slot_letters(self, pos, lemma, title, row, column):
            return {"вино": {"вино"}, "вина": {"вина"}}.get(
                {("nominative", "sg"): "вино", ("genitive", "sg"): "вина"}.get((row, column), ""))

    table = {"title": "Declension", "columns": ["", "sg"], "rows": [{"cells": ["nominative", "вино"]}, {"cells": ["genitive", "винаго"]},
                                                                    {"cells": ["accusative", "вино"]}]}
    sc = scene(table)
    sc.id = "s1"
    bad, counts = audit_forms.audit([sc], D())
    assert [(r["row"], r["piece"]) for r in bad] == [("genitive", "винаго")] and counts["match"] == 1 and counts["unknown"] == 1


def test_an_unstressed_adjective_ending_gets_one_more_retake():
    import clip_asr
    f = clip_asr.unstressed_adjective_ending
    assert f("ва́жной") and f("ми́лое") and f("о́бщая") and f("ва́жные, ва́жных") is False and f("ва́жные")
    assert not f("важно́й") and not f("большо́й") and not f("до́ма") and not f("вино")        # a stressed ending, or not an adjective ending
    assert json.loads(open(__import__("pathlib").Path(__file__).resolve().parents[1] / "settings.json").read())["forms"]["extraRetakes"] == 1
