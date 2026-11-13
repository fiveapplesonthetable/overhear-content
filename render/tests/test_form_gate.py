import json

import pytest

import clips
import form_gate as fg

# (language, text sent to the voice, what Whisper wrote): the same sounds written differently. All of these failed the spelling CER.
SAME_SOUND = [
    ("hi", "लाएगा", "लाइगा"), ("hi", "दरवाज़ा", "दर्वाजा"), ("hi", "रहूँगा", "रहुंगा"), ("hi", "गुस्से", "गुसे"), ("hi", "रातें", "राते"),
    ("ar", "فاضية", "فاضيه"), ("ar", "كنست", "كناست"), ("ar", "أصايل", "أصائل"), ("ar", "بيكبس", "بيك بس"), ("ar", "طار", "تار"),
    ("ko", "칸이", "카니"), ("ko", "안이", "아니"), ("ko", "빛바래요", "빗바래요."), ("ko", "대체예요", "대체에요."), ("ko", "큰길이", "큰 길이"), ("ko", "쌓습니다", "쌌습니다."),
    ("fr", "ils comparent, elles comparent", "Il compare, elle compare."),
    ("fr", "carrée", "Carré."), ("fr", "nue", "nu"), ("fr", "la tante", "L'attente."), ("fr", "tu leveras", "Tu le verras."),
]
JAPANESE_SAME_SOUND = [("越しじゃない", "腰じゃない"), ("はまって", "ハマって"), ("三年前です", "3年前です"), ("銅です", "どうです。"), ("会って", "あって"), ("駄目です", "ダメです。")]

# A different word (a different sound, a missing suffix, a hallucination): none of these may pass.
DIFFERENT_WORD = [
    ("hi", "हटाओगे", "अटाओगे"), ("hi", "देखेगी", "नेखेगी"), ("hi", "घर", "काट  काट  काट"), ("hi", "सीधी", "इधे"), ("hi", "पुल", "गुल"),
    ("ar", "قلقوا", "غلقوا"), ("ar", "حفرتوا", "حفرت"), ("ar", "راح", "راحة"), ("ar", "غطسنا", "لطسنة"), ("ar", "تخت", "تَخْتَ وَلَا يَا إِشَيْئًا بَنِي"),
    ("ko", "창고를", "참고를"), ("ko", "맞혀요", "맞춰요"), ("ko", "추상이", "추상위"), ("ko", "풉니다", "다음 영상에서 만나요."), ("ko", "강이", "강의"), ("ko", "일을", "알을"),
    ("fr", "pull", "Poules."), ("fr", "brillons", "Brillant."), ("fr", "mes", "Mais."), ("fr", "lents", "L'an."), ("fr", "quatre", "4"),
]
JAPANESE_DIFFERENT_WORD = [("方だった", "型だった"), ("石畳です", "石田までです"), ("連れます", "ぬれます。"), ("越しじゃない", "星じゃない"), ("上らない", "終わらない")]


def passes(lang, text, heard, strict=1.0):
    return fg.gated_cer(lang, text, heard, strict) <= 0.15


@pytest.mark.parametrize("lang,text,heard", SAME_SOUND)
def test_same_sound_written_differently_passes(lang, text, heard):
    assert passes(lang, text, heard)


@pytest.mark.parametrize("lang,text,heard", DIFFERENT_WORD)
def test_a_different_word_still_fails(lang, text, heard):
    assert not passes(lang, text, heard)


@pytest.mark.parametrize("text,heard", JAPANESE_SAME_SOUND)
def test_japanese_compares_readings(text, heard):
    pytest.importorskip("pykakasi")
    assert passes("ja", text, heard)


@pytest.mark.parametrize("text,heard", JAPANESE_DIFFERENT_WORD)
def test_japanese_different_reading_fails(text, heard):
    pytest.importorskip("pykakasi")
    assert not passes("ja", text, heard)


def test_the_gate_is_never_stricter_than_the_spelling_cer():
    assert fg.gated_cer("hi", "लाएगा", "बिलकुल अलग", 0.05) == 0.05
    assert fg.gated_cer("de", "Haus", "Maus", 0.25) == 0.25               # other languages are left to the spelling CER


def test_a_short_word_tolerates_one_confusable_sound_but_not_one_different_sound():
    assert passes("ar", "طار", "تار")                                  # emphatic/plain: half a point in three letters
    assert not passes("ar", "طار", "نار")
    assert not passes("fr", "ou", "a")


def test_nothing_heard_fails():
    for lang in ("hi", "ar", "ko", "fr"):
        assert fg.sound_cer(lang, "x" if lang == "fr" else "ا", "...") == 1.0


def test_comparison_cer_uses_the_gate_for_forms_only():
    pytest.importorskip("jiwer")
    pytest.importorskip("numpy")
    import clip_asr
    rec = {"lang": "hi", "text": "लाएगा", "tts": "लाएगा"}
    assert clip_asr.comparison_cer(rec, "forms", "लाइगा") <= 0.15
    assert clip_asr.comparison_cer(rec, "clips", "लाइगा") > 0.15


def item(lang):
    return clips.Item("abc", f"{lang}-en", lang, "t", "v", [], "key1")


def write(store, **rec):
    (store.dir / "abc.json").write_text(json.dumps({"id": "abc", "ckey": "key1", **rec}))


def test_failure_of_an_older_gate_is_stale_but_a_pass_is_not(tmp_path):
    store = clips.ClipStore(tmp_path, "forms")
    write(store, status="failed")                                     # failed before there was a gate version
    assert not store.is_done(item("hi"))
    write(store, status="failed", gate="fg0")
    assert not store.is_done(item("hi"))
    write(store, status="failed", gate=fg.GATE_VERSION)
    assert store.is_done(item("hi"))
    (store.dir / "abc.mp3").write_bytes(b"x")
    write(store, status="ok")
    assert store.is_done(item("hi"))
    write(store, status="ok", ckey="other")
    assert not store.is_done(item("hi"))


def test_languages_without_the_gate_keep_their_failures(tmp_path):
    store = clips.ClipStore(tmp_path, "forms")
    write(store, status="failed")
    assert store.is_done(item("ru"))
    clip_store = clips.ClipStore(tmp_path, "clips")
    (clip_store.dir / "abc.json").write_text(json.dumps({"id": "abc", "ckey": "key1", "status": "failed"}))
    assert clip_store.is_done(item("hi"))


def test_fail_final_records_the_gate_version(tmp_path):
    store = clips.ClipStore(tmp_path, "forms")
    store.write_work("abc", {"id": "abc", "pair": "hi-en", "text": "t", "lang": "hi", "voice": "v", "ckey": "key1", "tries": 2})
    clips.fail_final(tmp_path, "abc", 0.5, "x", "forms")
    assert store.record("abc")["gate"] == fg.GATE_VERSION
    assert store.is_done(item("hi"))
