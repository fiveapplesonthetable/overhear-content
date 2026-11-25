# Voices

The local cloning pipeline uses reference clips in `render/refs/<key>.flac`. Its pool lives in
`render/voices.json`; casting lives in `render/casting/<show>.json`. An authorised provider trial can instead use
that provider's named synthetic voices, with exact model, voice and directions recorded in the show. This changes
speech generation only: the same lesson, annotations, real word timing, render and publication contracts apply.

## Standing narrator style

The narrator is always female, warm, relaxed, clear and conversational. English is always British English, matching
the established Southern British narrator's character. For narration in another language choose a comparable native
female voice. Dialogue characters retain their own casting. Avoid shrill delivery, exaggerated brightness or a robotic
classroom cadence. Keep voice identity stable between segments and specify the accent explicitly when using a provider.
Automatic transcription checks wording; it does not certify accent or subjective voice quality.

## What a reference may be

* **Synthetic:** designed with `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` from a text description (this is how `ru-m1`..`ru-m7`
  and `ru-f1`..`ru-f3` were made), or from another TTS model whose license allows publishing its output.
* **Licensed speech:** a CC0 corpus clip (e.g. Mozilla Common Voice, CC0), with its corpus id recorded.
* **Never** a cut of the show's own audio, or any recording of a real actor or person who has not licensed it. That rule has no
  exceptions, including "private conditioning only". `render/tests/test_language_profiles.py` checks the pool for it.

## The pool today

ru: `alisa anja angelina ru-f1 ru-f2 ru-f3` (f), `ru-m1`..`ru-m7` (m). fr: `lucie emilie` (f), `theo marcel` (m). en
narrator reference: `sky` / `en-f1`. This list is historical, not an inventory: inspect current `render/voices.json`,
language settings and casting before creating or selecting voices. Later languages already have populated profiles.

## Owner listening feedback (2026-11-02)

On the earlier pilot renders: the **Arabic voices were very bad**, and one **Portuguese voice was far too high-pitched and
unpleasant**. Do not reuse those voices. For ar and pt, design more candidates than usual, reject anything shrill, thin or
robotic, and have Gemini listen with that complaint in mind. Prefer natural mid or low pitch over bright voices in every language.

## Making voices for a new language

1. For each pilot show, list the speaking characters by gender from `out/<show>/cast.json`. Plan at least 3 voices per gender,
   with distinct ages and timbres, and one calm neutral female reader for example and form clips.
2. Write a VoiceDesign description per voice (age, pitch, timbre, pace, accent, mood) and a 7-12 s reference sentence in the
   target language: natural, everyday, covering varied sounds. Use native script for ja/zh/ko/ar.
3. Generate several takes per voice on the A100. Keep the best: Whisper CER of the take against its text <= 0.05, no
   artefacts, the right language and accent. Have Gemini listen to the shortlist as well.
4. Save it as `render/refs/<lang>-<f|m><n>.flac` (24 kHz mono) and add a `voices.json` `refs` entry:

       "es-f1": {"file": "refs/es-f1.flac", "lang": "es", "gender": "f", "text": "<exact transcript>",
                 "desc": "VoiceDesign: <the description>", "seconds": 8.4,
                 "source": [{"model": "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign", "seed": 7, "note": "synthetic, no show audio"}]}

   Add `"designedFor": "<role key>"` if you designed it for one character. Casting then prefers it for that role.
5. Set the language profile's (`render/settings.<lang>-*.json`) `clips.voices` and `forms.voices` to the neutral reader, so
   example and form clips render too.
6. Arabic renders with Chatterbox multilingual (`settings.ar-chatterbox-en.json`, `ttsAr`). Its reference can be a CC0
   Common Voice clip or a synthetic one; record which.

Casting (`render/casting/<show>.json`) is built automatically from `cast.json` the first time a show renders, and is
append-only after that. To re-cast a character, edit its `voice` there; the scenes that use it re-render by themselves. Commit
the refs, `voices.json` and the casting files.

Record each new voice and its CER in `out/PROGRESS.md`.
