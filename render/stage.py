"""One GPU step of one scene, run by pipeline.py inside `gpurun <MiB> ...` (one reservation per step, per scene).

  stage.py missing --scene ID                        no GPU: sentences still to synthesise per engine {ru, en, other}
  stage.py synth  --scene ID                         Qwen3-TTS: synthesise the scene's missing sentences that have no engine block of their own (French)   (reserve ~4800 MiB)
  stage.py synth-ru --scene ID                       ESpeech (settings ttsRu, venv-f5): the scene's missing Russian sentences (~3500)
  stage.py synth-en --scene ID                       F5-TTS v1 Base (settings ttsEn, venv-f5): the scene's missing English/narrator sentences (~2400)
  stage.py retake --scene ID --keys k1,k2            other seeds for flagged sentences, per language: ESpeech (ru) / F5 (en) when configured, else Qwen
  stage.py clips  --scenes ID,ID --attempt N         Qwen3-TTS: example clips of those scenes (attempt 0 = first takes, N = retakes) (~6300)
  stage.py forms  --ids-file F --attempt N           Qwen3-TTS: table-form clips of the ids in F, from <store>/forms/.plan.json (attempt 0 / retakes) (~5400)
  stage.py finish --scene ID [--no-retake] [--times JSON]   MMS_FA alignment + stress check + assemble + write (~1500 MiB)

Prints exactly one result line:  OK {...} | RESULT {...} | NEED_RETAKE {"keys": [...]} | FAIL {"error": ...}
"""
import argparse
import json
import os
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

import config  # noqa: E402
import content  # noqa: E402


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, file=sys.stderr, flush=True)


def _make_ru_engine(settings, voices, log, retake=False):
    ru = config.ru_engine(settings)
    if ru and ru.get("engine") in ("qwen", "qwen-lora"):
        from tts import QwenEngine
        s_ru = json.loads(json.dumps(settings))
        use_lora = bool(ru.get("lora", ru.get("engine") == "qwen-lora"))
        if retake and ru.get("stress") == "onflag" and settings.get("lora", {}).get("hf"):
            use_lora = True
        s_ru["lora"]["enabled"] = use_lora
        if ru.get("loraTag"):
            s_ru["lora"]["tag"] = ru["loraTag"]
        if "temperature" in ru:
            s_ru["tts"]["temperature"] = float(ru["temperature"])
        if "repetition_penalty" in ru:
            s_ru["tts"]["repetition_penalty"] = float(ru["repetition_penalty"])
        return QwenEngine(s_ru, voices, log=log)
    from espeech import EspeechEngine
    return EspeechEngine(settings, voices, log=log)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["missing", "synth", "synth-ru", "synth-en", "synth-ar", "synth-hi", "retake", "finish", "clips", "forms"])
    ap.add_argument("--scene", default="")
    ap.add_argument("--scenes", default="")
    ap.add_argument("--attempt", type=int, default=0)
    ap.add_argument("--ids-file", default="")
    ap.add_argument("--keys", default="")
    ap.add_argument("--no-retake", action="store_true")
    ap.add_argument("--times", default="{}")
    ap.add_argument("--content", default=str(config.CONTENT_DIR))
    ap.add_argument("--root", choices=["out", "originals", "all"], default=None)
    ap.add_argument("--store", default=str(config.STORE))
    ap.add_argument("--settings", default=None)
    a = ap.parse_args()
    if a.root:
        os.environ["OVERHEAR_CONTENT_ROOT"] = a.root
    try:
        settings = config.load_settings(a.settings)
        if os.environ.get("OVERHEAR_TTS_BATCH"):
            b = int(os.environ["OVERHEAR_TTS_BATCH"])
            settings["tts"]["batch"] = settings["tts"]["batchEn"] = b
            if "clips" in settings:
                settings["clips"]["batch"] = b
        from voices import Voices
        from store import Store
        from ruaccent_fallback import RuAccent
        from render_scene import Renderer
        voices, store = Voices(), Store(a.store)
        if a.stage == "forms":
            import forms
            import clips
            from tts import QwenEngine
            ids = json.loads(Path(a.ids_file).read_text("utf-8"))
            items = forms.read_plan(store.root, ids)
            if a.attempt:
                items = clips.retakes_among(items, clips.ClipStore(store.root, forms.KIND), a.attempt)
            else:
                items = forms.pending(items, store.root)
            t0 = time.time()
            out = []
            if items:
                for lang in sorted({it.lang for it in items}):
                    fs = forms.forms_settings(settings, lang)
                    if os.environ.get("OVERHEAR_FORMS_BATCH"):
                        fs["tts"]["batch"] = fs["forms"]["batch"] = int(os.environ["OVERHEAR_FORMS_BATCH"])
                    if lang == "ar" and config.ar_engine(fs):
                        from chatterbox_ar import ChatterboxArEngine
                        eng = ChatterboxArEngine(fs, voices, log=log)
                    elif lang == "hi" and config.hi_engine(fs):
                        from hindi_tts import HindiEngine
                        eng = HindiEngine(fs, voices, log=log)
                    else:
                        eng = QwenEngine(fs, voices, log=log)
                    out.extend(clips.render_items([it for it in items if it.lang == lang], eng, store, fs, a.attempt, log=log, kind=forms.KIND))
                    eng.free()
            print("OK " + json.dumps({"stage": "forms", "ids": out, "wall": round(time.time() - t0, 2)}), flush=True)
            return
        ruacc = RuAccent(settings["stress"]["ruaccentPython"], store.root / "cache" / "ruaccent.json") if settings["stress"]["ruaccentFallback"] else None
        if a.stage == "clips":
            import clips
            from tts import QwenEngine
            scenes = []
            for sid in [x for x in a.scenes.split(",") if x]:
                s1 = content.load_scene(content.scene_path(a.content, sid))
                if isinstance(s1, content.Scene):
                    scenes.append(s1)
            if a.attempt == 0:
                items = list(clips.pending_for(scenes, settings, voices, store.root, ruacc).values())
            else:
                items = clips.items_for_retake(scenes, settings, voices, store.root, a.attempt, ruacc)
            t0 = time.time()
            ids = []
            if items:
                settings["tts"]["batch"] = settings["clips"]["batch"]
                for lang in sorted({it.lang for it in items}):
                    if lang == "ar" and config.ar_engine(settings):
                        from chatterbox_ar import ChatterboxArEngine
                        eng = ChatterboxArEngine(settings, voices, log=log)
                    elif lang == "hi" and config.hi_engine(settings):
                        from hindi_tts import HindiEngine
                        eng = HindiEngine(settings, voices, log=log)
                    else:
                        eng = QwenEngine(settings, voices, log=log)
                    ids.extend(clips.render_items([it for it in items if it.lang == lang], eng, store, settings, a.attempt, log=log))
                    eng.free()
            print("OK " + json.dumps({"stage": "clips", "ids": ids, "wall": round(time.time() - t0, 2)}), flush=True)
            return
        if a.stage in ("synth", "synth-ru", "synth-en", "synth-ar", "synth-hi") and a.scenes:
            ru, en, ar, hi = config.ru_engine(settings), config.en_engine(settings), config.ar_engine(settings), config.hi_engine(settings)

            def engine_for_multi(lang):
                if lang == "ar" and ar:
                    from chatterbox_ar import ChatterboxArEngine
                    return ChatterboxArEngine(settings, voices, log=log)
                if lang == "hi" and hi:
                    from hindi_tts import HindiEngine
                    return HindiEngine(settings, voices, log=log)
                if lang == "ru" and ru:
                    return _make_ru_engine(settings, voices, log, retake=(a.stage == "retake"))
                if lang == "en" and en:
                    from f5en import F5EnEngine
                    return F5EnEngine(settings, voices, log=log)
                from tts import QwenEngine
                return QwenEngine(settings, voices, log=log)

            def label_multi(lang):
                return lang if (lang == "ru" and ru) or (lang == "en" and en) or (lang == "ar" and ar) or (lang == "hi" and hi) else None

            r = Renderer(settings, voices, store, ruacc, log=log)
            target_lang = {"synth-ru": "ru", "synth-en": "en", "synth-ar": "ar", "synth-hi": "hi"}.get(a.stage)
            merged = {}
            for sid in [x for x in a.scenes.split(",") if x]:
                s1 = content.load_scene(content.scene_path(a.content, sid))
                if not isinstance(s1, content.Scene):
                    continue
                c1 = r.prepare(s1)
                for k, it in c1.uniq.items():
                    if target_lang:
                        if it["lang"] == target_lang:
                            merged[k] = it
                    elif not label_multi(it["lang"]):
                        merged[k] = it
            items = list(merged.values())
            t0 = time.time()
            if not items or all(store.tts_path(it["key"]).exists() for it in items):
                print("OK " + json.dumps({"stage": a.stage, "n": 0, "audio_s": 0.0, "cached": len(items), "wall": 0.0}), flush=True)
                return
            eng = engine_for_multi(target_lang or "fr")
            st = eng.synth_many(items, store)
            st["wall"] = round(time.time() - t0, 2)
            print("OK " + json.dumps({"stage": a.stage, **st}), flush=True)
            return
        sc = content.load_scene(content.scene_path(a.content, a.scene))
        if not isinstance(sc, content.Scene):
            raise RuntimeError("skip: " + sc.reason)
        r = Renderer(settings, voices, store, ruacc, log=log)
        ctx = r.prepare(sc)
        t0 = time.time()
        ru, en, ar, hi = config.ru_engine(settings), config.en_engine(settings), config.ar_engine(settings), config.hi_engine(settings)
        if a.stage == "synth-ru" and not ru:
            raise RuntimeError("synth-ru needs settings ttsRu")
        if a.stage == "synth-en" and not en:
            raise RuntimeError("synth-en needs settings ttsEn")
        if a.stage == "synth-ar" and not ar:
            raise RuntimeError("synth-ar needs settings ttsAr and a complete local multilingual V2 snapshot")
        if a.stage == "synth-hi" and not hi:
            raise RuntimeError("synth-hi needs settings ttsHi")
        if a.stage == "missing":     # no GPU: how many sentences each engine still has to make (lets the pipeline skip a reservation)
            miss = {"ru": 0, "en": 0, "ar": 0, "hi": 0, "other": 0}
            for it in ctx.uniq.values():
                if not store.tts_path(it["key"]).exists():
                    miss[it["lang"] if (it["lang"] == "ru" and ru) or (it["lang"] == "en" and en) or (it["lang"] == "ar" and ar) or (it["lang"] == "hi" and hi) else "other"] += 1
            print("OK " + json.dumps({"stage": "missing", **miss}), flush=True)
            return
        if a.stage in ("synth", "synth-ru", "synth-en", "synth-ar", "synth-hi", "retake"):
            def engine_for(lang):
                if lang == "ar" and ar:
                    from chatterbox_ar import ChatterboxArEngine
                    return ChatterboxArEngine(settings, voices, log=log)
                if lang == "hi" and hi:
                    from hindi_tts import HindiEngine
                    return HindiEngine(settings, voices, log=log)
                if lang == "ru" and ru:
                    return _make_ru_engine(settings, voices, log, retake=(a.stage == "retake"))
                if lang == "en" and en:
                    from f5en import F5EnEngine
                    return F5EnEngine(settings, voices, log=log)
                from tts import QwenEngine
                return QwenEngine(settings, voices, log=log)

            def label(lang):      # "ru" / "en" / "ar" / "hi" when they have their own engine, else the Qwen share
                return lang if (lang == "ru" and ru) or (lang == "en" and en) or (lang == "ar" and ar) or (lang == "hi" and hi) else None

            if a.stage == "retake":
                by = {}
                for k in [k for k in a.keys.split(",") if k]:
                    by.setdefault(ctx.uniq[k]["lang"], []).append(k)
                st = {"retaken": 0, "takes": 0}
                for lang, ks in by.items():
                    eng = engine_for(lang)
                    r1 = r.retake(ctx, eng, ks)
                    eng.free()
                    st = {k: st[k] + r1[k] for k in st}
            else:
                lang = {"synth-ru": "ru", "synth-en": "en", "synth-ar": "ar", "synth-hi": "hi"}.get(a.stage)
                if lang:
                    items = [it for it in ctx.uniq.values() if it["lang"] == lang]
                else:      # Qwen: everything that has no engine block of its own
                    items = [it for it in ctx.uniq.values() if not label(it["lang"])]
                if all(store.tts_path(it["key"]).exists() for it in items):
                    print("OK " + json.dumps({"stage": a.stage, "n": 0, "audio_s": 0.0, "cached": len(items), "wall": 0.0}), flush=True)
                    return
                eng = engine_for(lang or "fr")
                st = eng.synth_many(items, store)
            st["wall"] = round(time.time() - t0, 2)
            print("OK " + json.dumps({"stage": a.stage, **st}), flush=True)
        else:
            from align import Aligner
            commit = content.git_commit(a.content)
            kind, res = r.finish(ctx, Aligner("cuda"), commit, allow_retake=not a.no_retake, times=json.loads(a.times))
            if kind == "retake":
                print("NEED_RETAKE " + json.dumps({"sceneId": a.scene, "keys": res}), flush=True)
            else:
                print("RESULT " + json.dumps(res, ensure_ascii=False), flush=True)
    except Exception as e:
        traceback.print_exc()
        print("FAIL " + json.dumps({"sceneId": a.scene, "error": f"{type(e).__name__}: {str(e)[:300]}"}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
