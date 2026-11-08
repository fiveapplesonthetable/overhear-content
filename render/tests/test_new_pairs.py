"""Tests for spec/NEW-PAIRS.md:
1. Both ru-en and en-es validate (tools/validate.py --require-notes) and render end-to-end through Renderer + check_render.
2. hi-en validates with 100% Devanagari spans, vowel-length romanized readings, and Hindi word tables, and maps cleanly through native_text uroman targets.
3. Existing -en render keys, sentence cache keys, TTS signatures, and assembly signatures remain unchanged.
"""
import json
import shutil
import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "render"))

import check_render as cr  # noqa: E402
import config  # noqa: E402
import content  # noqa: E402
import native_text  # noqa: E402
import plan  # noqa: E402
from render_scene import Renderer  # noqa: E402
from store import Store  # noqa: E402
import validate as v  # noqa: E402


EX_ART = ROOT / "examples" / "kukhnya-s01e02-knife" / "art.webp"


class DummyVoices:
    def __init__(self, refs, casting_by_show, wav_dir: Path):
        self.refs = refs
        self._casting = casting_by_show
        self._wav_dir = wav_dir

    def lang_of(self, key):
        return self.refs[key]["lang"]

    def ref_path(self, key):
        return self._wav_dir / f"{key}.wav"

    def ref_version(self, key):
        return "12345678"

    def voices_version(self):
        return 1

    def resolve(self, scene):
        doc = self._casting[scene.show]
        out = {"narrator": doc["narrator"]}
        for r, info in doc["characters"].items():
            out[r] = info["voice"]
        return out


class FakeAligner:
    """Deterministic monotonic character/word aligner so Renderer.finish runs full assembly + check_render offline."""
    def char_times(self, wav, sr, text, lang):
        dur = max(0.2, len(wav) / sr)
        n = max(1, len(text))
        res = []
        for i, ch in enumerate(text):
            if ch.isalnum():
                a = dur * (i / n) * 0.85
                b = min(dur, a + max(0.02, dur * 0.6 / n))
                res.append((a, b))
            else:
                res.append(None)
        x16 = np.zeros(max(320, int(dur * 16000)), dtype=np.float32)
        return res, x16

    def word_times(self, wav, sr, text, lang, words):
        p = native_text.targets(text, lang, words)
        dur = max(0.2, len(wav) / sr)
        n = max(1, len(p.letters))
        frame_sec = 0.02
        spans = []
        for idx in range(n):
            s_f = int((dur * 0.8 * idx / n) / frame_sec)
            e_f = max(s_f + 1, int((dur * 0.8 * (idx + 0.8) / n) / frame_sec))
            spans.append(SimpleNamespace(start=s_f, end=e_f, score=0.95))
        x16 = np.zeros(max(320, int(dur * 16000)), dtype=np.float32)
        return native_text.aggregate(p, spans, frame_sec, dur), x16


def _write_show_tree(base: Path, show: str, pair: str, show_title: dict, cast_list: list, script: dict, notes: dict):
    show_dir = base / "originals" / show
    ep_dir = show_dir / "s01e01"
    (show_dir / "art").mkdir(parents=True)
    ep_dir.mkdir(parents=True)
    shutil.copy(EX_ART, show_dir / "art" / "cover.webp")
    shutil.copy(EX_ART, ep_dir / "scene-01.webp")
    (show_dir / "bible.md").write_text(f"# {show}\n\nOriginal Season 1.\n", "utf-8")
    (show_dir / "characters.md").write_text("# Characters\n\n- Cast\n", "utf-8")
    (show_dir / "show.json").write_text(json.dumps({
        "schemaVersion": 1,
        "slug": show,
        "pair": pair,
        "title": show_title,
        "summary": show_title,
        "type": "series",
        "categories": ["everyday-life"],
        "seasons": [{"n": 1, "title": show_title}],
        "cover": "art/cover.webp",
    }, ensure_ascii=False), "utf-8")
    (show_dir / "cast.json").write_text(json.dumps({
        "schemaVersion": 1,
        "show": show,
        "cast": cast_list,
    }, ensure_ascii=False), "utf-8")
    (ep_dir / "scenes.json").write_text(json.dumps({
        "schemaVersion": 1,
        "show": show,
        "season": 1,
        "episode": 1,
        "title": "Episode 1",
        "scenes": [{
            "scene": 1,
            "title": "Morning Desk",
            "summary": "Two characters check the morning room key at the front desk.",
            "characters": [c["key"] for c in cast_list],
            "location": "front desk",
        }],
    }, ensure_ascii=False), "utf-8")
    (ep_dir / "scene-01.json").write_text(json.dumps(script, ensure_ascii=False), "utf-8")
    (ep_dir / "scene-01.notes.json").write_text(json.dumps(notes, ensure_ascii=False), "utf-8")
    return ep_dir


def _synth_sine(path: Path, sr=24000, sec=0.8, hz=220.0):
    t = np.linspace(0, sec, int(sr * sec), endpoint=False, dtype=np.float32)
    w = 0.12 * np.sin(2 * np.pi * hz * t)
    sf.write(str(path), w, sr, format="FLAC", subtype="PCM_16")


def test_both_ru_en_and_en_es_validate_and_render(tmp_path):
    # 1. Build valid ru-en original scene
    ru_segs = [{"v": "narrator", "t": "Dasha greets Pavel at the desk.", "gap": 0.6}]
    ru_story = [
        ("dasha", "Привет, Павел!"),
        ("pavel", "Доброе утро!"),
        ("dasha", "Где ключ?"),
        ("pavel", "Ключ здесь."),
    ] * 2
    for role, line in ru_story:
        ru_segs.append({"v": role, "t": line, "gap": 0.5})
    ru_segs.append({"v": "narrator", "t": "Let us walk through two key lines.", "gap": 0.4})
    ru_segs.append({"v": "dasha", "t": "Привет, Павел!", "gap": 0.5})
    ru_segs.append({"v": "narrator", "t": "'Hi, Pavel!' Dasha uses the everyday Russian greeting.", "gap": 0.4})
    ru_segs.append({"v": "dasha", "t": "Где ключ?", "gap": 0.5})
    ru_segs.append({"v": "narrator", "t": "'Where is the key?' Notice Russian needs no word for 'is' in the present tense.", "gap": 0.8})
    for role, line in ru_story:
        ru_segs.append({"v": role, "t": line, "gap": 0.45})
    ru_segs.append({"v": "narrator", "t": "See you in the next lesson.", "gap": 0.5})
    ru_segs.append({"v": "dasha", "t": "Пока!", "gap": 0.3})

    ru_script = {
        "schemaVersion": 1,
        "id": "test-ru-inn-s01e01-scene-01",
        "pair": "ru-en",
        "show": "test-ru-inn",
        "season": 1, "episode": 1, "scene": 1,
        "title": "Ключ  (The Key)",
        "level": "A1 — beginner",
        "labels": {"dasha": "Даша", "pavel": "Павел"},
        "segments": ru_segs,
    }
    ru_lines = []
    for idx, g in enumerate(ru_segs):
        if g["v"] == "narrator":
            continue
        t = g["t"]
        if t == "Привет, Павел!":
            wds = [
                {"t": "Привет,", "lemma": "привет", "pos": "interj", "stress": "приве\u0301т,", "gloss": "hi", "gram": "interj"},
                {"t": "Павел!", "lemma": "павел", "pos": "name", "stress": None, "gloss": "Pavel", "gram": "proper noun"},
            ]
            tr = "Hi, Pavel!"
        elif t == "Доброе утро!":
            wds = [
                {"t": "Доброе", "lemma": "добрый", "pos": "adj", "stress": "до\u0301брое", "gloss": "good", "gram": "nom n sg"},
                {"t": "утро!", "lemma": "утро", "pos": "noun", "stress": "у\u0301тро!", "gloss": "morning", "gram": "nom n sg"},
            ]
            tr = "Good morning!"
        elif t == "Где ключ?":
            wds = [
                {"t": "Где", "lemma": "где", "pos": "adv", "stress": None, "gloss": "where", "gram": "interrogative adv"},
                {"t": "ключ?", "lemma": "ключ", "pos": "noun", "stress": None, "gloss": "key", "gram": "nom m sg"},
            ]
            tr = "Where is the key?"
        elif t == "Ключ здесь.":
            wds = [
                {"t": "Ключ", "lemma": "ключ", "pos": "noun", "stress": None, "gloss": "key", "gram": "nom m sg"},
                {"t": "здесь.", "lemma": "здесь", "pos": "adv", "stress": None, "gloss": "here", "gram": "adv"},
            ]
            tr = "The key is here."
        else:
            wds = [{"t": "Пока!", "lemma": "пока", "pos": "interj", "stress": "пока\u0301!", "gloss": "bye", "gram": "interj"}]
            tr = "Bye!"
        ru_lines.append({"seg": idx, "trans": tr, "words": wds})

    ru_notes = {
        "schemaVersion": 1,
        "id": "test-ru-inn-s01e01-scene-01",
        "lines": ru_lines,
        "lexicon": {
            "привет": {"lemma": "привет", "stress": "приве\u0301т", "pos": "interj", "gloss": "hi",
                       "meanings": [{"en": "hi", "note": ""}], "forms": None, "moreForms": [],
                       "examples": [{"text": "Привет!", "trans": "Hi!"}, {"text": "Привет, друг!", "trans": "Hi, friend!"}], "related": []},
            "добрый": {"lemma": "добрый", "stress": "до\u0301брый", "pos": "adj", "gloss": "kind, good",
                       "meanings": [{"en": "good, kind", "note": ""}],
                       "forms": {"title": "Declension", "columns": ["", "m", "f", "n", "pl"], "rows": [{"cells": ["nominative", "добрый", "добрая", "доброе", "добрые"]}]},
                       "moreForms": [], "examples": [{"text": "Добрый день!", "trans": "Good afternoon!"}, {"text": "Доброе утро!", "trans": "Good morning!"}], "related": []},
            "утро": {"lemma": "утро", "stress": "у\u0301тро", "pos": "noun", "gender": "n", "gloss": "morning",
                     "meanings": [{"en": "morning", "note": ""}],
                     "forms": {"title": "Declension", "columns": ["", "sg", "pl"], "rows": [{"cells": ["nominative", "утро", "утра"]}]},
                     "moreForms": [], "examples": [{"text": "Доброе утро!", "trans": "Good morning!"}, {"text": "Утро тихое.", "trans": "The morning is quiet."}], "related": []},
            "где": {"lemma": "где", "stress": "где", "pos": "adv", "gloss": "where",
                    "meanings": [{"en": "where", "note": ""}], "forms": None, "moreForms": [],
                    "examples": [{"text": "Где ключ?", "trans": "Where is the key?"}, {"text": "Где чай?", "trans": "Where is the tea?"}], "related": []},
            "ключ": {"lemma": "ключ", "stress": "ключ", "pos": "noun", "gender": "m", "gloss": "key",
                     "meanings": [{"en": "key", "note": ""}],
                     "forms": {"title": "Declension", "columns": ["", "sg", "pl"], "rows": [{"cells": ["nominative", "ключ", "ключи"]}]},
                     "moreForms": [], "examples": [{"text": "Где ключ?", "trans": "Where is the key?"}, {"text": "Ключ здесь.", "trans": "The key is here."}], "related": []},
            "здесь": {"lemma": "здесь", "stress": "здесь", "pos": "adv", "gloss": "here",
                      "meanings": [{"en": "here", "note": ""}], "forms": None, "moreForms": [],
                      "examples": [{"text": "Ключ здесь.", "trans": "The key is here."}, {"text": "Я здесь.", "trans": "I am here."}], "related": []},
            "пока": {"lemma": "пока", "stress": "пока\u0301", "pos": "interj", "gloss": "bye",
                     "meanings": [{"en": "bye", "note": ""}], "forms": None, "moreForms": [],
                     "examples": [{"text": "Пока!", "trans": "Bye!"}, {"text": "Пока, Павел!", "trans": "Bye, Pavel!"}], "related": []},
        },
    }

    # 2. Build valid en-es original scene (English target dialogue + Spanish narrator & learning notes)
    en_segs = [{"v": "narrator", "t": "Claire saluda a Owen en la recepción de la posada.", "gap": 0.6}]
    en_story = [
        ("claire", "Good morning, Owen!"),
        ("owen", "Hi, Claire!"),
        ("claire", "Where is the key?"),
        ("owen", "The key is here."),
    ] * 2
    for role, line in en_story:
        en_segs.append({"v": role, "t": line, "gap": 0.5})
    en_segs.append({"v": "narrator", "t": "Repasemos las frases clave con calma.", "gap": 0.4})
    en_segs.append({"v": "claire", "t": "Where is the key?", "gap": 0.5})
    en_segs.append({"v": "narrator", "t": "'¿Dónde está la llave?' En inglés, el verbo va antes del sujeto en las preguntas.", "gap": 0.4})
    en_segs.append({"v": "owen", "t": "The key is here.", "gap": 0.5})
    en_segs.append({"v": "narrator", "t": "'La llave está aquí.' Escuchemos toda la escena de nuevo.", "gap": 0.8})
    for role, line in en_story:
        en_segs.append({"v": role, "t": line, "gap": 0.45})
    en_segs.append({"v": "narrator", "t": "Nos vemos en el próximo episodio.", "gap": 0.5})
    en_segs.append({"v": "claire", "t": "See you soon!", "gap": 0.3})

    en_script = {
        "schemaVersion": 1,
        "id": "test-en-es-inn-s01e01-scene-01",
        "pair": "en-es",
        "show": "test-en-es-inn",
        "season": 1, "episode": 1, "scene": 1,
        "title": "The Key  (La llave)",
        "level": "A1 — principiante",
        "labels": {"claire": "Claire", "owen": "Owen"},
        "segments": en_segs,
    }
    en_lines = []
    for idx, g in enumerate(en_segs):
        if g["v"] == "narrator":
            continue
        t = g["t"]
        if t == "Good morning, Owen!":
            wds = [
                {"t": "Good", "lemma": "good", "pos": "adj", "stress": "ɡʊd", "gloss": "buenos", "gram": "adj"},
                {"t": "morning,", "lemma": "morning", "pos": "noun", "stress": "ˈmɔɹnɪŋ", "gloss": "días / mañana", "gram": "sg noun"},
                {"t": "Owen!", "lemma": "owen", "pos": "name", "stress": None, "gloss": "Owen", "gram": "nombre propio"},
            ]
            tr = "¡Buenos días, Owen!"
        elif t == "Hi, Claire!":
            wds = [
                {"t": "Hi,", "lemma": "hi", "pos": "interj", "stress": "haɪ", "gloss": "hola", "gram": "interj"},
                {"t": "Claire!", "lemma": "claire", "pos": "name", "stress": None, "gloss": "Claire", "gram": "nombre propio"},
            ]
            tr = "¡Hola, Claire!"
        elif t == "Where is the key?":
            wds = [
                {"t": "Where", "lemma": "where", "pos": "adv", "stress": "wɛɹ", "gloss": "dónde", "gram": "adv interrogativo"},
                {"t": "is", "lemma": "be", "pos": "verb", "stress": "ɪz", "gloss": "está", "gram": "3ª sg presente"},
                {"t": "the", "lemma": "the", "pos": "det", "stress": "ðə", "gloss": "la", "gram": "artículo definido"},
                {"t": "key?", "lemma": "key", "pos": "noun", "stress": "kiː", "gloss": "llave", "gram": "sustantivo sg"},
            ]
            tr = "¿Dónde está la llave?"
        elif t == "The key is here.":
            wds = [
                {"t": "The", "lemma": "the", "pos": "det", "stress": "ðə", "gloss": "la", "gram": "artículo definido"},
                {"t": "key", "lemma": "key", "pos": "noun", "stress": "kiː", "gloss": "llave", "gram": "sustantivo sg"},
                {"t": "is", "lemma": "be", "pos": "verb", "stress": "ɪz", "gloss": "está", "gram": "3ª sg presente"},
                {"t": "here.", "lemma": "here", "pos": "adv", "stress": "hɪɹ", "gloss": "aquí", "gram": "adv"},
            ]
            tr = "La llave está aquí."
        else:
            wds = [
                {"t": "See", "lemma": "see", "pos": "verb", "stress": "siː", "gloss": "vemos", "gram": "forma base"},
                {"t": "you", "lemma": "you", "pos": "pron", "stress": "juː", "gloss": "te", "gram": "pronombre"},
                {"t": "soon!", "lemma": "soon", "pos": "adv", "stress": "suːn", "gloss": "pronto", "gram": "adv"},
            ]
            tr = "¡Hasta pronto!"
        en_lines.append({"seg": idx, "trans": tr, "words": wds})

    en_notes = {
        "schemaVersion": 1,
        "id": "test-en-es-inn-s01e01-scene-01",
        "lines": en_lines,
        "lexicon": {
            "good": {"lemma": "good", "stress": "ɡʊd", "pos": "adj", "gloss": "bueno",
                     "meanings": [{"en": "bueno", "note": "Comparativo irregular: better, best."}],
                     "forms": {"title": "Forms", "columns": ["", "form"], "rows": [
                         {"cells": ["positive", "good"]}, {"cells": ["comparative", "better"]}, {"cells": ["superlative", "best"]}
                     ]},
                     "moreForms": [], "examples": [{"text": "Good morning!", "trans": "¡Buenos días!"}, {"text": "That coffee is good.", "trans": "Ese café es bueno."}], "related": []},
            "morning": {"lemma": "morning", "stress": "ˈmɔɹnɪŋ", "pos": "noun", "gloss": "mañana",
                        "meanings": [{"en": "mañana (parte del día)", "note": ""}], "forms": None, "moreForms": [],
                        "examples": [{"text": "Good morning!", "trans": "¡Buenos días!"}, {"text": "Every morning is quiet.", "trans": "Cada mañana es tranquila."}], "related": []},
            "hi": {"lemma": "hi", "stress": "haɪ", "pos": "interj", "gloss": "hola",
                   "meanings": [{"en": "hola", "note": ""}], "forms": None, "moreForms": [],
                   "examples": [{"text": "Hi, Claire!", "trans": "¡Hola, Claire!"}, {"text": "Hi there!", "trans": "¡Hola!"}], "related": []},
            "where": {"lemma": "where", "stress": "wɛɹ", "pos": "adv", "gloss": "dónde",
                      "meanings": [{"en": "dónde", "note": ""}], "forms": None, "moreForms": [],
                      "examples": [{"text": "Where is the key?", "trans": "¿Dónde está la llave?"}, {"text": "Where are you?", "trans": "¿Dónde estás?"}], "related": []},
            "be": {"lemma": "be", "stress": "biː", "pos": "verb", "gloss": "ser o estar",
                   "meanings": [{"en": "ser, estar", "note": ""}],
                   "forms": {"title": "Forms", "columns": ["", "form"], "rows": [
                       {"cells": ["base", "be"]}, {"cells": ["3rd sg", "is"]}, {"cells": ["past", "was / were"]},
                       {"cells": ["past participle", "been"]}, {"cells": ["-ing", "being"]}
                   ]},
                   "moreForms": [], "examples": [{"text": "The key is here.", "trans": "La llave está aquí."}, {"text": "I am ready.", "trans": "Estoy listo."}], "related": []},
            "the": {"lemma": "the", "stress": "ðə", "pos": "det", "gloss": "el, la, los, las",
                    "meanings": [{"en": "el, la, los, las", "note": ""}], "forms": None, "moreForms": [],
                    "examples": [{"text": "The key is here.", "trans": "La llave está aquí."}, {"text": "Open the door.", "trans": "Abre la puerta."}], "related": []},
            "key": {"lemma": "key", "stress": "kiː", "pos": "noun", "gloss": "llave",
                    "meanings": [{"en": "llave", "note": ""}], "forms": None, "moreForms": [],
                    "examples": [{"text": "Where is the key?", "trans": "¿Dónde está la llave?"}, {"text": "Here is your key.", "trans": "Aquí está tu llave."}], "related": []},
            "here": {"lemma": "here", "stress": "hɪɹ", "pos": "adv", "gloss": "aquí",
                     "meanings": [{"en": "aquí", "note": ""}], "forms": None, "moreForms": [],
                     "examples": [{"text": "The key is here.", "trans": "La llave está aquí."}, {"text": "Come here.", "trans": "Ven aquí."}], "related": []},
            "see": {"lemma": "see", "stress": "siː", "pos": "verb", "gloss": "ver",
                    "meanings": [{"en": "ver", "note": ""}],
                    "forms": {"title": "Forms", "columns": ["", "form"], "rows": [
                        {"cells": ["base", "see"]}, {"cells": ["3rd sg", "sees"]}, {"cells": ["past", "saw"]},
                        {"cells": ["past participle", "seen"]}, {"cells": ["-ing", "seeing"]}
                    ]},
                    "moreForms": [], "examples": [{"text": "See you soon!", "trans": "¡Hasta pronto!"}, {"text": "I see the sign.", "trans": "Veo el cartel."}], "related": []},
            "you": {"lemma": "you", "stress": "juː", "pos": "pron", "gloss": "tú, usted, ustedes",
                    "meanings": [{"en": "tú, usted, ustedes", "note": ""}], "forms": None, "moreForms": [],
                    "examples": [{"text": "See you soon!", "trans": "¡Hasta pronto!"}, {"text": "Are you ready?", "trans": "¿Estás listo?"}], "related": []},
            "soon": {"lemma": "soon", "stress": "suːn", "pos": "adv", "gloss": "pronto",
                     "meanings": [{"en": "pronto", "note": ""}], "forms": None, "moreForms": [],
                     "examples": [{"text": "See you soon!", "trans": "¡Hasta pronto!"}, {"text": "Breakfast is ready soon.", "trans": "El desayuno estará listo pronto."}], "related": []},
        },
    }

    ru_ep = _write_show_tree(
        tmp_path / "ru_repo", "test-ru-inn", "ru-en",
        {"ru": "Дворик", "en": "Little Inn"},
        [{"key": "dasha", "ru": "Даша", "en": ["Dasha"], "gender": "f"},
         {"key": "pavel", "ru": "Павел", "en": ["Pavel"], "gender": "m"}],
        ru_script, ru_notes,
    )
    en_ep = _write_show_tree(
        tmp_path / "en_repo", "test-en-es-inn", "en-es",
        {"en": "Courtyard Inn", "es": "La Posada del Patio"},
        [{"key": "claire", "ru": "Claire", "en": ["Claire"], "gender": "f"},
         {"key": "owen", "ru": "Owen", "en": ["Owen"], "gender": "m"}],
        en_script, en_notes,
    )

    assert v.main(["--require-notes", "--root", "originals", str(ru_ep)]) == 0
    assert v.main(["--require-notes", "--root", "originals", str(en_ep)]) == 0

    # 3. Render both ru-en and en-es through Renderer.prepare + Renderer.finish and verify check_render passes
    wav_dir = tmp_path / "voices"
    wav_dir.mkdir()
    refs = {
        "sky": {"lang": "en", "gender": "f", "text": "Hello."},
        "ru-f1": {"lang": "ru", "gender": "f", "text": "Привет."},
        "ru-m1": {"lang": "ru", "gender": "m", "text": "Привет."},
        "es-narr": {"lang": "es", "gender": "f", "text": "Hola."},
        "en-f1": {"lang": "en", "gender": "f", "text": "Good morning."},
        "en-m1": {"lang": "en", "gender": "m", "text": "Good morning."},
    }
    for vk in refs:
        _synth_sine(wav_dir / f"{vk}.wav")
    casting_map = {
        "test-ru-inn": {"narrator": "sky", "characters": {"dasha": {"voice": "ru-f1"}, "pavel": {"voice": "ru-m1"}}},
        "test-en-es-inn": {"narrator": "es-narr", "characters": {"claire": {"voice": "en-f1"}, "owen": {"voice": "en-m1"}}},
    }
    voices = DummyVoices(refs, casting_map, wav_dir)
    settings = config.load_settings()
    settings["audio"]["interSentenceGap"]["ru"] = 0.4
    settings["audio"]["interSentenceGap"]["es"] = 0.4
    settings["audio"]["interSentenceGap"]["en"] = 0.3

    for repo_dir, ep_dir, ep_id, sid, expected_narr_lang in [
        (tmp_path / "ru_repo", ru_ep, "test-ru-inn-s01e01", "test-ru-inn-s01e01-scene-01", "en"),
        (tmp_path / "en_repo", en_ep, "test-en-es-inn-s01e01", "test-en-es-inn-s01e01-scene-01", "es"),
    ]:
        store = Store(repo_dir / "store")
        sc = content.load_scene(ep_dir / "scene-01.json")
        assert isinstance(sc, content.Scene)
        assert sc.native_lang == expected_narr_lang
        renderer = Renderer(settings, voices, store, log=lambda *_: None)
        ctx = renderer.prepare(sc)
        for key, item in ctx.uniq.items():
            _synth_sine(store.tts_path(key), sec=max(0.6, len(item["text_plain"]) * 0.045))
        kind, res = renderer.finish(ctx, FakeAligner(), content_commit="abc1234", allow_retake=False)
        assert kind == "done" and res["sceneId"] == sid
        rep = cr.Report()
        cr.check_scene(store.root, sid, ep_dir / "scene-01.json", ep_dir / "scene-01.notes.json", rep)
        assert rep.errors == [], f"{sid} check_render errors: {rep.errors}"
        spans_doc = json.loads((store.root / sid / "spans.json").read_text("utf-8"))
        assert spans_doc["segs"][0]["lang"] == expected_narr_lang


def test_hindi_validation_and_native_uroman_alignment(tmp_path):
    hi_line = "नमस्ते, कमरा खाली है?"
    # Spans for: नमस्ते (0..6), कमरा (8..12), खाली (13..17), है (18..20)
    words = [
        {"t": "नमस्ते", "span": [0, 6], "reading": "namastē", "lemma": "नमस्ते", "pos": "interj", "stress": None, "gloss": "hello", "gram": "greeting"},
        {"t": "कमरा", "span": [8, 12], "reading": "kamarā", "lemma": "कमरा", "pos": "noun", "stress": None, "gloss": "room", "gram": "m sg direct"},
        {"t": "खाली", "span": [13, 17], "reading": "khālī", "lemma": "खाली", "pos": "adj", "stress": None, "gloss": "free, vacant", "gram": "invariant adj"},
        {"t": "है", "span": [18, 20], "reading": "hai", "lemma": "होना", "pos": "verb", "stress": None, "gloss": "is", "gram": "3rd sg present"},
    ]
    parsed = native_text.words_for_segment(hi_line, words, "hi")
    targs = native_text.targets(hi_line, "hi", parsed)
    assert "".join(targs.letters) == "namastekamarakhalihai"

    # Validate a complete hi-en scene
    hi_segs = [{"v": "narrator", "t": "Meera welcomes Aarav at the courtyard haveli.", "gap": 0.6}]
    for _ in range(8):
        hi_segs.append({"v": "meera", "t": hi_line, "gap": 0.5})
    hi_segs.append({"v": "narrator", "t": "Let us listen closely to that greeting.", "gap": 0.4})
    hi_segs.append({"v": "meera", "t": hi_line, "gap": 0.5})
    hi_segs.append({"v": "narrator", "t": "'Hello, is the room vacant?' Notice Hindi puts the verb at the end of the sentence.", "gap": 0.8})
    for _ in range(8):
        hi_segs.append({"v": "meera", "t": hi_line, "gap": 0.45})
    hi_segs.append({"v": "narrator", "t": "Until next time.", "gap": 0.5})
    hi_segs.append({"v": "meera", "t": "फिर मिलेंगे!", "gap": 0.3})

    closing_words = [
        {"t": "फिर", "span": [0, 3], "reading": "phir", "lemma": "फिर", "pos": "adv", "stress": None, "gloss": "again", "gram": "adv"},
        {"t": "मिलेंगे", "span": [4, 11], "reading": "milēṅgē", "lemma": "मिलना", "pos": "verb", "stress": None, "gloss": "will meet", "gram": "1st pl future m"},
    ]
    hi_notes = {
        "schemaVersion": 1,
        "id": "test-hi-haveli-s01e01-scene-01",
        "lines": [
            {"seg": idx, "trans": "See you again!" if g["t"] == "फिर मिलेंगे!" else "Hello, is the room free?",
             "words": closing_words if g["t"] == "फिर मिलेंगे!" else words}
            for idx, g in enumerate(hi_segs) if g["v"] != "narrator"
        ],
        "lexicon": {
            "नमस्ते": {"lemma": "नमस्ते", "stress": None, "pos": "interj", "gloss": "hello",
                       "meanings": [{"en": "hello, greetings", "note": ""}], "forms": None, "moreForms": [],
                       "examples": [{"text": "नमस्ते!", "trans": "Hello!"}, {"text": "नमस्ते जी।", "trans": "Hello."}], "related": []},
            "कमरा": {"lemma": "कमरा", "stress": None, "pos": "noun", "gender": "m", "gloss": "room",
                     "meanings": [{"en": "room", "note": ""}],
                     "forms": {"title": "Declension", "columns": ["", "sg", "pl"], "rows": [
                         {"cells": ["direct", "कमरा", "कमरे"]}, {"cells": ["oblique", "कमरे", "कमरों"]}
                     ]},
                     "moreForms": [], "examples": [{"text": "कमरा बड़ा है।", "trans": "The room is big."}, {"text": "कमरे में मेज़ है।", "trans": "There is a table in the room."}], "related": []},
            "खाली": {"lemma": "खाली", "stress": None, "pos": "adj", "gloss": "empty, vacant",
                     "meanings": [{"en": "empty, vacant", "note": "Uninflecting adjective."}], "forms": None, "moreForms": [],
                     "examples": [{"text": "कमरा खाली है।", "trans": "The room is vacant."}, {"text": "कुर्सी खाली है।", "trans": "The chair is free."}], "related": []},
            "होना": {"lemma": "होना", "stress": None, "pos": "verb", "gloss": "to be",
                     "meanings": [{"en": "to be", "note": ""}],
                     "forms": {"title": "Present", "columns": ["", "sg", "pl"], "rows": [
                         {"cells": ["1st", "हूँ", "हैं"]}, {"cells": ["2nd", "है / हो", "हो / हैं"]}, {"cells": ["3rd", "है", "हैं"]}
                     ]},
                     "moreForms": [], "examples": [{"text": "कमरा यहाँ है।", "trans": "The room is here."}, {"text": "मैं तैयार हूँ।", "trans": "I am ready."}], "related": []},
            "फिर": {"lemma": "फिर", "stress": None, "pos": "adv", "gloss": "again, then",
                    "meanings": [{"en": "again, then", "note": ""}], "forms": None, "moreForms": [],
                    "examples": [{"text": "फिर मिलेंगे!", "trans": "See you again!"}, {"text": "फिर क्या हुआ?", "trans": "Then what happened?"}], "related": []},
            "मिलना": {"lemma": "मिलना", "stress": None, "pos": "verb", "gloss": "to meet",
                      "meanings": [{"en": "to meet", "note": ""}],
                      "forms": {"title": "Present habitual", "columns": ["", "m", "f"], "rows": [
                          {"cells": ["1st sg", "मिलता हूँ", "मिलती हूँ"]}, {"cells": ["2nd pol", "मिलते हैं", "मिलती हैं"]}
                      ]},
                      "moreForms": [], "examples": [{"text": "फिर मिलेंगे!", "trans": "See you again!"}, {"text": "कल मिलते हैं।", "trans": "Let's meet tomorrow."}], "related": []},
        },
    }
    hi_script = {
        "schemaVersion": 1,
        "id": "test-hi-haveli-s01e01-scene-01",
        "pair": "hi-en",
        "show": "test-hi-haveli",
        "season": 1, "episode": 1, "scene": 1,
        "title": "कमरा  (The Room)",
        "level": "A1 — beginner",
        "labels": {"meera": "मीरा"},
        "segments": hi_segs,
    }
    hi_ep = _write_show_tree(
        tmp_path / "hi_repo", "test-hi-haveli", "hi-en",
        {"hi": "आँगन हवेली", "en": "Courtyard Haveli"},
        [{"key": "meera", "ru": "मीरा", "en": ["Meera"], "gender": "f"},
         {"key": "aarav", "ru": "आरव", "en": ["Aarav"], "gender": "m"}],
        hi_script, hi_notes,
    )
    assert v.main(["--require-notes", "--root", "originals", str(hi_ep)]) == 0
