"""Paths, settings and the render signature (everything that changes the audio)."""
import hashlib
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIPELINE_VERSION = "overhear-render/1"

# Everything machine-specific lives under OVERHEAR_HOME (venvs, model caches, the render store); see render/setup/setup.sh and the repo README.
HOME = Path(os.environ.get("OVERHEAR_HOME", Path.home() / "overhear"))
CONTENT_DIR = Path(os.environ.get("OVERHEAR_CONTENT", HERE.parent))   # this repository
STORE = Path(os.environ.get("OVERHEAR_RENDER_STORE", HOME / "render-store"))
PUBLISH_LOCK = Path(os.environ.get("OVERHEAR_PUBLISH_LOCK", STORE / "publish.lock"))
GPURUN = os.environ.get("OVERHEAR_GPURUN", str(HERE / "gpurun"))
VENV_QWEN = os.environ.get("OVERHEAR_VENV_QWEN", str(HOME / "venv-qwen"))
VENV_F5 = os.environ.get("OVERHEAR_VENV_F5", str(HOME / "venv-f5"))
VENV_AR = os.environ.get("OVERHEAR_VENV_AR", str(HOME / "venv-asr"))
VENV_HI = os.environ.get("OVERHEAR_VENV_HI", str(HOME / "venv-f5"))
VENV_ASR = os.environ.get("OVERHEAR_VENV_ASR", str(HOME / "venv-asr"))
HF_TOKEN_FILE = Path(os.environ.get("OVERHEAR_HF_TOKEN_FILE", HOME / "hf-token.txt"))   # optional; never commit it
# Machine paths that settings.json names but that never change the audio's render key:
RUACCENT_PYTHON = os.environ.get("OVERHEAR_RUACCENT_PYTHON", f"{VENV_F5}/bin/python")
LORA_LOCAL = os.environ.get("OVERHEAR_LORA_LOCAL")            # unset = download the LoRA from Hugging Face
CHATTERBOX_LOCAL = os.environ.get("OVERHEAR_CHATTERBOX", str(HOME / "models" / "chatterbox"))  # ResembleAI/chatterbox snapshot (setup/download_models.py)
FORMS_DICTIONARY = os.environ.get("OVERHEAR_FORMS_DICTIONARY", str(HOME / "dict" / "kaikki.org-dictionary-Russian.jsonl"))
STRESS_CHECK_DIR = HERE.parent / "stress-check"

SETTINGS_FILE = Path(os.environ.get("OVERHEAR_RENDER_SETTINGS", HERE / "settings.json"))
VOICES_FILE = Path(os.environ.get("OVERHEAR_RENDER_VOICES", HERE / "voices.json"))


def load_settings(path=None):
    s = json.loads(Path(path or SETTINGS_FILE).read_text(encoding="utf-8"))
    s = {k: v for k, v in s.items() if not k.startswith("_")}
    if "stress" in s:
        s["stress"]["ruaccentPython"] = RUACCENT_PYTHON
    if "lora" in s:
        s["lora"]["local"] = LORA_LOCAL
    if "forms" in s and s["forms"].get("dictionary"):
        s["forms"]["dictionary"] = FORMS_DICTIONARY
    if "ttsAr" in s:
        s["ttsAr"]["modelLocal"] = CHATTERBOX_LOCAL
    if "ttsHi" in s and s["ttsHi"].get("engine") == "chatterbox":
        s["ttsHi"].setdefault("modelLocal", CHATTERBOX_LOCAL)
    return s


def stress_policy(s):
    p = s["stress"]["policy"]
    if p == "auto":
        return "all" if s["lora"]["enabled"] else "homographs"
    return p


def tts_signature(s, with_en=True, with_ar=True, with_hi=True, with_ru=True):
    """The part of the settings that changes what the model says (not how it is assembled)."""
    t = s["tts"]
    lora = s["lora"]
    return {
        "model": t["model"], "dtype": t["dtype"],
        "gen": [t["temperature"], t["top_k"], t["top_p"], t["repetition_penalty"]],
        "lora": (lora["tag"] if lora["enabled"] else None),
        "stress": stress_policy(s),
        "takeGates": "v2",
        **({"ru": _public(ru_engine(s))} if with_ru and ru_engine(s) else {}),
        **({"en": _public(en_engine(s))} if with_en and en_engine(s) else {}),
        **({"ar": _public(ar_engine(s))} if with_ar and ar_engine(s) else {}),
        **({"hi": _public(hi_engine(s))} if with_hi and hi_engine(s) else {}),
    }


def _public(block):
    """The block minus notes and machine paths (a path never changes the audio, so it never enters a render key)."""
    return {k: v for k, v in block.items() if not k.startswith("_") and k not in ("modelLocal", "venv")}


def ru_engine(s):
    """The target-language engine block (settings ttsRu) or None (Russian then uses tts{} like every other language)."""
    return s.get("ttsRu")


def en_engine(s):
    """The English/narrator engine block (settings ttsEn: F5-TTS v1 Base) or None (English then uses tts{} like French)."""
    return s.get("ttsEn")


def ar_engine(s):
    return s.get("ttsAr")


def hi_engine(s):
    return s.get("ttsHi")


def hi_venv(s):
    h = hi_engine(s) or {}
    v = h.get("venv")
    if v == "asr" or h.get("engine") == "chatterbox":
        return VENV_AR
    if v == "f5" or h.get("engine") in ("f5", "f5-hi"):
        return VENV_F5
    if v and Path(str(v)).exists():
        return str(v)
    if v:
        return str(HOME / str(v))
    return VENV_HI


def sentence_signature(s, lang):
    """What the sentence cache key depends on: ttsRu for Russian / ttsEn for English when configured, else the full tts
    signature. (voice, reference version and text are added by plan.cache_key.)"""
    ru, en, ar, hi = ru_engine(s), en_engine(s), ar_engine(s), hi_engine(s)
    if lang == "ru" and ru:
        # onflag sends the same first-take text as "homographs" did before marks existed; the text is in the cache key, so
        # the policy name is not: unchanged sentences keep their cached takes and marked ones (other text) miss it.
        return {"ru": {**_public(ru), **({"stress": "homographs"} if ru.get("stress") == "onflag" else {})}, "takeGates": "v3"}
    if lang == "en" and en:
        return {"en": _public(en), "takeGates": "v2"}
    if lang == "ar" and ar:
        return {"ar": _public(ar), "takeGates": "v4-ar-fullsent"}
    if lang == "hi" and hi:
        return {"hi": _public(hi), "takeGates": "v1-hi"}
    d = tts_signature(s, with_en=False, with_ar=False, with_hi=False, with_ru=False)
    d["takeGates"] = "v5-sky-pure" if lang == "en" else "v2"
    return d    # Other languages' sentence caches do not depend on Arabic/Hindi/narrator engines.


def engine_label(s, lang):
    if lang == "ar" and ar_engine(s):
        return "chatterbox-multilingual-v2"
    if lang == "hi" and hi_engine(s):
        return hi_engine(s).get("label", hi_engine(s).get("engine", "hindi-tts"))
    if lang == "en" and en_engine(s):
        return "f5-tts"
    return "qwen3-tts"


def assembly_signature(s):
    return {"audio": s["audio"], "align": s["align"], "renderVersion": s["renderVersion"],
            "turnMaxChars": int(s["audio"].get("turnMaxChars", 240)),
            "inlineCarrier": "v4-comma-name", "warmMaster": "v2-keep-plosives",
            **({"arTailCrop": "v2-ar-fullsent"} if ar_engine(s) else {})}


def sha(obj) -> str:
    if not isinstance(obj, (bytes, str)):
        obj = json.dumps(obj, sort_keys=True, ensure_ascii=False)
    if isinstance(obj, str):
        obj = obj.encode("utf-8")
    return hashlib.sha256(obj).hexdigest()
