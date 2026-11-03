# Overhear V5 Production Audio, Simplification & QA Runbook

This document records the complete, reproducible content, voice-design, TTS, acoustic QA, mastering, and 40 GB A100 multi-daemon architecture used to produce studio-grade bilingual episodes across all 10 language pairs (`pt`, `ru`, `fr`, `ar`, `es`, `de`, `ko`, `it`, `ja`, `zh` -> `en`).

---

## 1. Simplified Scene Architecture (Zero AI-Slop Narration)

Every scene follows a clean 6-part structure (`tools/simplify_walk.py`, validated by `tools/validate.py`):
1. **English Scene Introduction (`SCENE_INTRO`, `seg 0`):** Brief English setup spoken by British female narrator **`sky`** (`render/refs/sky.flac` — mandatory narrator across all 10 languages).
2. **Cold Open (`STORY`):** Full target-language dialogue played naturally at conversational pacing (`gap = 0.55s`).
3. **Line-by-Line Opener (`WALK_INTRO`):** Canonical golden `sky` transition (`"Now let's go through it line by line with the English translation."`, `WavLM = 0.9564`).
4. **Pure Translation Line-by-Line (`WALK`):** Each turn plays `[Target-language line (gap=0.55s)]` -> `[English translation ONLY (gap=0.45s)]`, with zero filler grammar/vocabulary AI-slop commentary and zero fragmented/orphaned inline callouts.
5. **Pre-Replay Transition (`REPLAY_INTRO`):** Canonical golden `sky` transition (`"Now let's listen to the whole conversation one last time."`, `WavLM = 0.9676`, `gap = 0.75s`) right before switching back into the final full reading.
6. **Natural-Speed Replay & Send-Off (`REPLAY` + `OUTRO` + `CLOSING`):** Full scene replay at natural cadence (`gap = 0.50s`), brief English sign-off, and a short target-language farewell.

To convert any newly authored episode to this clean format while automatically remapping `scene-*.notes.json` and `learn/**/*.json` segment indices:
```bash
python3 -I tools/simplify_walk.py out/<show>/<sXXeYY>
python3 -I tools/validate.py --require-notes out/<show>/<sXXeYY>
```

---

## 2. Acoustic Debugging Guide (What the Frequencies & Metrics Mean)

All automated gates (`render/gates.py`, `render/audio.py`, `render/render_scene.py`) and the standalone CLI inspector (`tools/diagnose_audio.py`) measure five physical audio properties:

1. **Fundamental Frequency / Pitch (`F0` in `Hz`, measured via `librosa.yin`):**
   - How many times per second the speaker's vocal cords vibrate — what the human ear perceives as **voice pitch**.
   - **Grounded adult male:** `95–155 Hz`.
   - **Calm, grounded adult female (`sky` narrator & dramatic actresses):** `165–205 Hz` (with pitch standard deviation `std` `18–35 Hz`).
   - **Cartoon / "Duolingo-perky" voice defect:** Median `F0 > 215 Hz` or 90th-percentile `p90 > 250 Hz` with wide sing-song swings (`std > 45 Hz`). We enforce `F0 in [165, 226] Hz` on `sky` in `render/gates.py` and design grounded female voices (`162–198 Hz`) via the two-stage recipe in `tools/design_voices.py`.
2. **Sliding-Window Speaker Embedding Similarity (`WavLM-base-plus-sv`, `0.0–1.0`):**
   - Measures vocal-tract timbre identity on every overlapping `1.8s` window (`0.9s` stride) across the entire clip against `render/refs/sky.flac`.
   - Whole-clip averages can hide a 1.5-second character-roleplay voice flip (`0.93` average while the first `1.8s` dropped to `0.72`). Requiring **every `1.8s` window `>= 0.85`** + stripping quotes/exclamations in `render/textprep.py: sanitize_english_narrator_tts()` eliminates narrator voice switching completely.
3. **Zero-Crossing Rate (`ZCR`) & Reference Prompt Tail Trim (Pre-Line `"shh"` Prevention):**
   - `ZCR` measures how often the waveform crosses `0.0` per sample: voiced vowels are smooth (`ZCR ~ 0.02–0.07` = `250–800 Hz`), whereas `"shh"` / breath hiss is rapid high-frequency turbulence (`ZCR > 0.15` = `1.8–4.5 kHz`).
   - `render/tts.py:_prompt` trims `sky.flac` cleanly at `7.88s` + `160 ms` pure `0.0` digital silence so zero-shot `Qwen3-TTS` never completes a cut-off reference breath at token `0`.
4. **First & Last Word Completion Guard (`edge_ok` in `render/gates.py`) & Plosive Tail Protection (`render/audio.py`):**
   - On a 50-character line (`"É isso que você quer pra sua vida? Perder o foco?"`), dropping `"oco"` (`"Perder o f..."`) is only `0.06` overall CER (`<= 0.18`), which previously slipped past whole-sentence CER! `gates.py` now checks exact/near-exact edit distance on **both the first word and the final word** (`edge_ok`) across all alphabetic languages (`en, pt, es, fr, it, de, ru`).
   - `render/audio.py:_strip_detached_tail_pop` only strips a single `< 55 ms`, `< 25%` peak-RMS EOS click after `>= 320 ms` silence — never multi-syllable words containing voiceless plosive closures (`/k/` in `"foco"`, `/p/` in `"equipe"`).
5. **Studio Broadcast Warmth EQ (`155 Hz` & `5.2 kHz`) + `-16 LUFS` Loudness (`render/audio.py`):**
   - `55 Hz` high-pass (removes subsonic thumps), `+2.0 dB @ 155 Hz` (warm chest resonance), `+1.2 dB @ 5.2 kHz` (crisp consonant clarity), normalized to `-16.0 LUFS` (`ITU-R BS.1770-4`, with `< 400 ms` tiling so short callouts never get `+15 dB` silence-padding gain) and `-2 dBTP` true-peak limiting.
   - For Arabic (`ChatterboxMultilingualTTS`), `render_scene.py` (`arTailCrop: v1`) crops post-sentence EOS hum/sigh tails at the `MMS_FA` acoustic valley `45–125 ms` after the final aligned Arabic word.

Run diagnostics anytime via:
```bash
~/overhear/venv-asr/bin/python tools/diagnose_audio.py refs --lang it
~/overhear/venv-asr/bin/python tools/diagnose_audio.py scene ~/overhear/render-store/porta-dos-fundos-s01e01-scene-03
```

---

## 3. Reproducible 40 GB A100 Multi-Worker Execution (`tools/launch_round_robin.py` & `render/turbo_daemon.py`)

1. **Initialize the strict round-robin episode queue and launch the persistent worker pool:**
   ```bash
   export OVERHEAR_HOME="$HOME/overhear" PATH="/usr/bin:$HOME/.local/bin:$PATH"
   cd ~/overhear-content
   python3 -I tools/launch_round_robin.py --reset-done
   python3 -B -I render/turbo_daemon.py master --qwen-workers 1 --en-workers 1 --ru-workers 2 --gate-workers 1 --batch-seqs 16
   ```
   *(When `jobs_qwen` and `jobs_ar` are empty, a 2nd `en-worker --id 2 --batch-seqs 16` can run concurrently alongside `master`, keeping total VRAM `~24–34 GiB / 40.96 GiB` with zero `gate-1` `ctranslate2` OOMs.)*

2. **Verify and `--clobber` publish each completed episode (`/dev/shm/overhear-turbo/done_<ep>.json`) in strict round-robin order:**
   ```bash
   python3 -I tools/check_render.py ~/overhear/render-store --episode <ep>
   python3 -I tools/package_render.py ~/overhear/render-store --episode <ep> --release
   ```
