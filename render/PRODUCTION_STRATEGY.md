# Overhear V3 Production Audio & Authoring Strategy

This document records the proven end-to-end content, voice, TTS, splicing, mastering, and 40 GB A100 multi-daemon architecture used to produce human-grade bilingual lessons across all 10 language pairs (`ru`, `fr`, `pt`, `ar`, `it`, `es`, `de`, `ja`, `zh`, `ko` -> `en`).

---

## 1. Why Early TTS Pipelines Sounded Robotic/Stitched — and the 5 Root-Cause Fixes

### Root Cause A: Fragmented Narrator Sentences Around Inline Foreign Callouts
- **Problem:** Under `spec/recipe.md`, `narrator` text never contains target-language or transliterated words; `WALK` splits an explanation into alternating segments (`narrator` -> `character "Зато"` -> `narrator`). Synthesizing each split English fragment (`", then "`, `" with an "`, `"."`) as an isolated TTS call caused:
  1. **Multiple narrator voices:** Zero-shot cloning (`Qwen3-TTS-1.7B-Base`) loses speaker lock on 1–3 word fragments without sentence context.
  2. **End-of-sentence bangs/gasps:** Unterminated fragments ending in `"with an "` or `"and "` caused autoregressive TTS to pause `0.4s` waiting to continue and emit a truncated syllable/pop at `max_new_tokens`.
  3. **Detached commas & big `300+ ms` gaps:** Leading commas (`', "for", then...'`) were stripped by the TTS tokenizer, while `0.25s` segment gaps + `20ms` trim margins created unnatural `~350 ms` dead silences around every word.
- **V3 Fix — Continuous Carrier-Sentence Inline Splicing (`render/render_scene.py: CarrierChain`):**
  - `Renderer.prepare()` detects every inline `WALK` chain (`gap == 0.25`) and builds **one complete, grammatically punctuated English carrier sentence** per explanation (inserting `"phrase"` / `"phrase,"` at target callout slots and moving detached commas onto the placeholder).
  - `Qwen3-TTS-12Hz-1.7B-Base` (`sky`, cloned from `render/refs/sky.flac` at low-entropy `temperature=0.60, top_k=30, top_p=0.88, repetition_penalty=1.08` with 2 candidates and `WavLM >= 0.78`) synthesizes the **entire carrier sentence in a single continuous take**, locking 100% identical relaxed British female voice, RP accent, room presence, and natural comma/falling intonation across the whole explanation.
  - `Renderer.finish()` runs `MMS_FA` (`aligner.char_times`) once on the leveled carrier waveform, cuts at true `5 ms` acoustic energy valleys around each placeholder (`12 ms` raised-cosine fades), maps exact character timings back to each script segment, and drops the character's native-voiced word inline with **punctuation-aware conversational micro-gaps (`60 ms` lead-in, `70 ms` inline continuation, `130 ms` comma breath, `220 ms` sentence boundary)**.
  - Result: 100% contract-compliant per-segment `spans.json` and `timing.json` (`check_render.py` = `0 errors`), zero foreign words in narrator JSON, single unbroken narrator voice, and natural inline bilingual cadence.

### Root Cause B: Short-Clip (`< 400 ms`) ITU-R BS.1770 LUFS `+15 dB` Gain Explosion ("Echo Bang")
- **Problem:** BS.1770 (`audio.py: lufs`) uses a `400 ms` integration window. Zero-padding `80–200 ms` 1-word callouts (`"у"`, `"за"`, `"Что?"`) to `400 ms` filled 50–80% of the window with zeros, under-measuring loudness by `8–12 dB` and causing `prepare_sentence()` to apply up to **`+15 dB` (`5.6x`) gain** — turning tiny room tails or codec release clicks into loud echo bangs.
- **V3 Fix (`render/audio.py`):**
  - Short clips (`< 400 ms`) are periodically tiled (`np.resize(x, blk)`) when measuring active speech LUFS so short words have zero silence-padding bias.
  - Positive segment gain is capped at `+5.0 dB` for `< 0.45s` clips (`+7.5 dB` otherwise), and all fades use smooth raised-cosine (`0.5 * (1 - cos)`) tapers.

### Root Cause C: Self-Masking Transient Detector & Slow-Speed F5-TTS Duration Babble
- **Problem:**
  1. `gates.py: check_transient` previously defined `last_speech` using `rms >= silence_thresh`, which included the bang itself, and ignored any bang followed by `> 80 ms` of codec silence.
  2. `ESpeech` (`F5-TTS` non-autoregressive flow-matching DiT) has fixed output frame count `gen_frames / speed`; setting `speed = 0.45–0.5` or `min_gen_frames = 0.95s` on a 1-syllable word (`"Что?"`) forced the DiT to hallucinate `2+` seconds of reference-bleed babble to fill the mel window.
- **V3 Fix (`render/gates.py`, `render/espeech.py`, `render/audio.py`):**
  - `espeech.py` uses `rt.rstrip() + " "` (preventing reference prompt bleed across `n_ref`), `min_gen_frames = 0.42s`, and `speeds = [1.0, 0.92, 0.85]`.
  - Both `gates.py: check_transient` and `audio.py: trim` detect contiguous active-speech islands relative to **median** speech RMS (`med_rms`): detached `< 220 ms` post-silence EOS pops (`>= 75 ms` gap) are sliced off cleanly before the gap; single-sentence clips with `>= 220 ms` post-silence secondary babble (`>= 180 ms` gap) or edge bursts (`> 3.1x med_rms` broadband or `> 1.9x med_rms` `< 150 Hz` thump) are rejected and retaken (`attempt < 3` in `turbo_daemon.py`).

### Root Cause D: Thin / Flat Neural Codec Timbre
- **Problem:** Raw `24 kHz` neural codec outputs (`Mimi` in Qwen3-TTS, `Vocos` in F5/ESpeech) have slightly recessed `130–220 Hz` chest fundamentals.
- **V3 Fix — Studio Broadcast Warmth Mastering (`render/audio.py: _podcast_warm_eq`):**
  - Applied uniformly in `master()` prior to `-16.0 LUFS` program normalization and `96 kHz` oversampled `-2 dBTP` true-peak limiting:
    1. `55 Hz` 2nd-order Butterworth high-pass (eliminates subsonic thumps),
    2. `+2.0 dB` peaking biquad at `155 Hz` (`Q = 0.75`) for warm human chest fullness,
    3. `+1.2 dB` high-shelf at `5.2 kHz` (`Q = 0.707`) for crisp consonant presence.

### Root Cause E: Whole-Turn Multi-Sentence Prosody & Introductory English Commas
- **V3 Fix (`render/textprep.py`):**
  - Consecutive dialogue/narrator sentences within a turn up to `turnMaxChars = 240` (`90` for `ru` ESpeech) are synthesized as a single continuous waveform (`group_turn_chunks`), deriving sub-sentence `(start, end)` spans in `spans.json` from `MMS_FA` word timestamps.
  - `polish_english_commas()` restores missing introductory commas (`"A little later,"`, `"In the present tense,"`, `"Meanwhile,"`, `"In Russian,"`, etc.) for natural prosodic breath pauses.

---

## 2. Proven Open-Weight Permissive (`Apache-2.0` / `MIT`) Model Stack

| Role / Language | Engine & Checkpoint | License | Key Settings |
|---|---|---|---|
| **English Narrator (`all 10 pairs`)** | `Qwen/Qwen3-TTS-12Hz-1.7B-Base` (`sky` British female) | `Apache-2.0` | Cloned from `render/refs/sky.flac` (`relaxed British, natural & melodic`) on full `CarrierChain` sentences at `temp=0.60, top_k=30, top_p=0.88`, `2` takes, `WavLM >= 0.78` |
| **Target (`fr, pt, es, de, it, ja, zh, ko`)** | `Qwen/Qwen3-TTS-12Hz-1.7B-Base` | `Apache-2.0` | Single-ref zero-shot cloning from Pilot Voices V2 (`f: 178–221 Hz`, `m: 95–177 Hz`); `WavLM >= 0.67` |
| **Target (`ru`)** | `ESpeech/ESpeech-TTS-1_RL-V2` + `RUAccent` | Permissive | Homograph stress from `.notes.json` + `RUAccent` fallback; `speeds: [1.0, 0.92, 0.85]` |
| **Target (`ar`)** | `ResembleAI/chatterbox` (`ChatterboxMultilingualTTS`) | `MIT` | Warm V2 `ar` voice pool; `torch.backends.cudnn.enabled = False` isolation |
| **Take Gates (`all`)** | `faster-whisper large-v3-turbo` + `microsoft/wavlm-base-plus-sv` + `librosa.yin` | `MIT` | Best-of-N (`N=3..4`), `CER <= 0.18`, verbatim-repeat check, island/transient gate, F0 `18–45 Hz` tie-breaker |
| **Forced Alignment (`all`)** | `torchaudio.pipelines.MMS_FA` (`uroman` wordspans on `ja,zh,ko,ar`) | Permissive | Resident on CUDA; `empty_cache()` after each scene |

*(Never use non-commercial models such as `fish-speech-1.5` or `higgs-audio`, and never use original show audio.)*

---

## 3. Decoupled `/dev/shm` Persistent 40 GB A100 Topology (`render/turbo_daemon.py`)

To sustain **`95–100%` SM utilization and `35–39 GiB / 40.96 GiB` VRAM** with zero model reloads and zero `ctranslate2` (cuDNN 9) vs `PyTorch` (cuDNN 8/CUDA 12) library collisions:

1. **Process Isolation by Virtualenv:**
   - `venv-qwen` (`en-worker` x2 on `/dev/shm/overhear-turbo/jobs_en` + `qwen-worker` x2 on `jobs_qwen` + `orchestrator` running `MMS_FA`)
   - `venv-f5` (`ru-worker` x1–2 on `jobs_ru`, auto-releasing VRAM when idle so Round-1 Qwen/Chatterbox can use the slot)
   - `venv-asr` (`ar-worker` on `jobs_ar` + `gate-worker` x2 scoring candidate `.npz` bundles in `cands/` with 4-thread CPU F0/transient pools)
2. **Atomic Lock-Free Queueing in RAM (`/dev/shm/overhear-turbo`):**
   - Jobs are named `{prio:04d}_{episode}_{key}.json` and claimed atomically via `os.rename` to `.claim.{pid}`, with periodic dead-PID reclamation (`tick % 20 == 0`).
3. **Continuous Verification & Release Loop:**
   - Every completed episode writes `done_{episode}.json` only after `tools/check_render.py --episode {episode}` exits `0`, followed by ear-check on `Gemini 3.1 Pro`, logging in `out/PROGRESS.md`, pushing to `origin/main`, and publishing via `python3 -I tools/package_render.py ~/overhear/render-store --episode {episode} --release` (`--clobber`).
