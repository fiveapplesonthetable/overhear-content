# Voices

Every voice in a public render is cloned from a reference clip in `render/refs/<key>.flac`. The pool lives in
`render/voices.json`; who speaks with which voice lives in `render/casting/<show>.json`.

## What a reference may be

* **Synthetic:** designed with `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` from a text description (this is how `ru-m1`..`ru-m7`
  and `ru-f1`..`ru-f3` were made), or from another TTS model whose license allows publishing its output.
* **Licensed speech:** a CC0 corpus clip (e.g. Mozilla Common Voice, CC0), with its corpus id recorded.
* **Never** a cut of the show's own audio, or any recording of a real actor or person who has not licensed it. That rule has no
  exceptions, including "private conditioning only". `render/tests/test_language_profiles.py` checks the pool for it.

## The pool today

ru: `alisa anja angelina ru-f1 ru-f2 ru-f3` (f), `ru-m1`..`ru-m7` (m). fr: `lucie emilie` (f), `theo marcel` (m). en
narrator: `sky`. The pilot languages (es, de, it, pt, ja, zh, ko, ar) have **no voices yet**. Make them before their first render.

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
