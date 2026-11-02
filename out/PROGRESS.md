# Progress

The running log of this work. Update it in the same commit as the work it describes: what changed, what the checkers said,
what review found, and what you tried on the A100 (models, batch sizes, measured RTF and CER). Newest entries go at the
bottom of "Log".

## Starting point (2026-11-02)

Every RU and FR episode has seed content: scripts, notes, scenes.json, authoring modules and art.

| show | lang | seasons | episodes | art files | status |
|---|---|---|---|---|---|
| `kukhnya` | ru | S1-S6 | 120 | 2474 | seed; not release-ready |
| `domashniy-arest` | ru | S1 | 12 | 408 | seed; not release-ready |
| `dix-pour-cent` | fr | S1-S4 | 24 | 650 | seed; not release-ready |
| es, de, it, pt, ja, zh, ko, ar pilots | | | 0 | | no content, no voices (README "What to produce", spec/voices.md) |

No episode is rendered or packaged under the current contract. Earlier renders are not valid for release.

### Validator baseline

`python3 tools/validate.py --require-notes --all out` gave **FAIL: 676 errors, 4622 warnings**:

* **669 repeated narrator phrases** (`PHRASE_MAX` 50 per show): 628 in kukhnya, the rest in dix-pour-cent and
  domashniy-arest. They are template explanations ("Q right at the" x1847, "now let listen to" x425). Rewrite those
  explanations by hand (spec/quality.md §2); never with a generator.
* **Word-teaching share** (target 60%, an error under `--strict-teaching`): kukhnya 64%, domashniy-arest 37%,
  dix-pour-cent 27%. Shows can pass overall while individual scenes stay below 60%, so check each scene.
* **Lexicon conflicts:**
  * ru: `шеф-повар` has two stresses.
  * fr stress: blesser, expliquer, fêter, s'arrêter.
  * fr gender: bonheur, frais, mort, vert.
  * fr pos: frais, mort, même, soudain.
  * Fix: pick one shape per lemma for the whole show. Where two parts of speech are genuinely different words, split
    them into separate lemma keys.
* **Speaker naming:** `dix-pour-cent/s02e02/scene-21` segments 19, 25 and 41 say "Christophe", but the speaker key is
  `christophe` (Lambert) and the name is ambiguous with another cast entry. Check the source cue and fix the cast or
  the narration.

Kukhnya S2e04 to S6e20 were written from Whisper (`ru-only`) transcripts. Names and numbers may be misheard: check them against the show's cast and the surrounding cues, and drop a line you cannot confirm.

## Next

1. Kukhnya S1: fix to `--strict-teaching`, review, render, check, package. This is the first release.
2. Then dix-pour-cent S1 and domashniy-arest S1, then the rest of the README order.

## Log

| date | what | result |
|---|---|---|
| 2026-11-02 | Repo prepared as the A100 brief (README, spec/OUTPUT-CONTRACT.md, spec/quality.md, spec/voices.md) | content tests 100 passed; render tests 113 + 166 passed |
| 2026-11-02 | Fixed `render/gpurun` lock path (`os.path.join`), all 194 RU/FR lexicon conflicts across `out/`, and `dix-pour-cent/s02e02/scene-21` (`Christophe` -> `Lambert`) | `validate.py` 0 lexicon/cast errors; all tests passing |
| 2026-11-02 | A100-40GB throughput + English/foreign code-switching narrator bake-off (`Qwen3-TTS-12Hz-1.7B-Base` vs `F5-TTS v1` vs `Chatterbox`, `Systran/faster-whisper-large-v3` judge + ear-check) | `bench.sh` (50 mixed lines): b1 RTF 2.332 (CER 0.0052), b8 RTF 0.449, **b16 RTF 0.310 (CER 0.0038, 12.4 GiB)**. 30 pure-English narrator lines: **`Qwen3-TTS sky` b32 RTF 0.111 (9.0x real-time, 17.7 GiB), WER 0.0069, CER 0.0012, p90 0.0009** vs `F5-TTS sky` nfe16/32 WER 0.0148, CER 0.0054, p90 0.0208 (F5 clips short function words like `'is'`) vs `Chatterbox sky` RTF 0.899, WER 0.0120, CER 0.0033. Cross-lingual narration: `Qwen sky` inline handles Latin scripts (`fr`/`es`/`de`) cleanly; for Cyrillic/CJK, separate target-voice replay + Method B spliced `Qwen sky` (EN) + `Qwen+LoRA ru-f1` (RU, CER 0.000 on all 9 stressed test phrases incl. `за́мок`/`замо́к`) wins on ear-check & accuracy. Added `render/settings.ru-qwen-en.json` + multi-worker GPU lanes in `render/pipeline.py` (`OVERHEAR_SYNTH_WORKERS`, `OVERHEAR_ALIGN_WORKERS`, `OVERHEAR_FORM_WORKERS`, `PerthImplicitWatermarker` Python 3.12 fallback in `chatterbox_ar.py`). |
| 2026-11-02 | `kukhnya` `s01e01` (25 scenes): validated (`--require-notes --strict-teaching`), second-opinion text/homograph review (`scene-21` transliteration polish) | `validate.py --require-notes --strict-teaching out/kukhnya/s01e01` -> **OK: 0 errors** (99% word-teaching, 329/330) |
| 2026-11-02 | Right-sized A100-40GB VRAM reservations (`ttsMiB=7800`, `forms.ttsMiB=9000`) + `render/gpurun` small-step backfilling + `Path(args.settings).resolve()` in `render/pipeline.py` | 4–6 concurrent GPU workers active (`36.0 GiB / 40.96 GiB` VRAM, `100%` SM util, `273W`); `render/tests/` `281 passed, 2 skipped` |
| 2026-11-02 | `dix-pour-cent` `s01e01` (28 scenes): hand-polished explanations to `--strict-teaching`, applied second-opinion review fixes (6 trailing `TRANSITION` duplicates + `scene-34` `'word for'`), re-composed | `validate.py --require-notes --strict-teaching out/dix-pour-cent/s01e01` -> **OK: 0 errors** (79% word-teaching, 395/498) |
| 2026-11-02 | Live `/proc`+`nvidia-smi` VRAM accounting in `render/gpurun` + multi-scene persistent Qwen synthesis (`--scenes`) in `render/stage.py` & `render/pipeline.py` + fixed 3 gender mismatches in `render/casting/kukhnya.json` (`sasha`->`f`/`ru-f3`, `jindi`->`m`/`ru-m6`, `judge`->`f`/`angelina`). Source audit note: `sources/alrawabi-school/s01/e02..e04.ar.srt` contain *Atr Al-Sham* (*عطر الشام*) rather than *AlRawabi School*, so `alrawabi-school` ships `s01e01` only until upstream replaces `e02..e04`. | A100 VRAM pinned at `39.3–40.2 GiB / 40.96 GiB` (`96–98%` HBM, `99–100%` SM); 0 casting gender mismatches across `kukhnya`, `dix-pour-cent`, `domashniy-arest` |
| 2026-11-02 | Registered 48 synthetic pilot voices (3F + 3M x 8 languages: `ar`, `de`, `es`, `it`, `ja`, `ko`, `pt`, `zh`) in `render/refs/`, `render/voices.json`, `render/settings.*.json`, and `render/tests/test_language_profiles.py` (zero show audio; `Qwen3-TTS-12Hz-1.7B-VoiceDesign` for `de,es,it,ja,ko,pt,zh`, synthetic `VoiceDesign` timbre + `ChatterboxMultilingualTTS` for `ar`) | Whisper `large-v3` CER: **41/48 = `0.0000`**, **46/48 <= `0.0370`** (`es-m1` `0.0096`, `ar-m3` `0.0149`, `ko-m1` `0.0204`, `ar-f2` `0.0278`, `ja-m1` `0.0370`), plus 2 digit-vs-word transcripts with `0.0000` normalized phonetic CER (`es-f3` `0.0660` `"30"`/`"treinta"`, `de-m3` `0.0800` `"8"`/`"acht"`); ear-checked all 8 neutral `<lang>-f1` voices; `pytest render/tests/test_language_profiles.py render/tests/test_french_profile.py` -> **5 passed** |
