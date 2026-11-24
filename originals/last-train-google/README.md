# The Last Train: Google TTS pilot

One original ru-en lesson for the public Originals catalogue. Written for this
Google TTS trial; no TV adaptation or source recording is used. It follows the
standard five-part lesson and annotation contracts.

Google model: `gemini-3.8-flash-tts`, via the Google Agent Platform REST endpoint.
Anna: Kore. Boris: Charon. English narrator: Sulafat, directed as a warm female
British English audiobook narrator. The exact directions are in `google-voices.json`.
The narrator's British accent is requested explicitly; automatic transcription
checks content, not accent or subjective voice quality.

Authentication uses the existing gcloud identity in project `cyclevpn`. No API key
is needed. The Vertex AI API (`aiplatform.googleapis.com`) was enabled for this trial.
Requests incur the project's Google TTS usage charges. No credentials belong in git.

From the content checkout, with STORE pointing at a separate pilot render directory:

```sh
python3 tools/validate.py --require-notes --strict-teaching originals/last-train-google/s01e01
python3 tools/google_tts_scene.py synth \
  --script originals/last-train-google/s01e01/scene-01.json \
  --casting originals/last-train-google/google-voices.json --store "$STORE"
# Run finish and qa in the renderer's torch/torchaudio/faster-whisper environment.
python3 tools/google_tts_scene.py finish \
  --script originals/last-train-google/s01e01/scene-01.json \
  --casting originals/last-train-google/google-voices.json --store "$STORE"
python3 tools/google_tts_scene.py qa \
  --script originals/last-train-google/s01e01/scene-01.json \
  --casting originals/last-train-google/google-voices.json --store "$STORE"
python3 tools/check_render.py "$STORE" --episode last-train-google-s01e01
python3 tools/package_render.py "$STORE" --episode last-train-google-s01e01
```

Commit the script, notes, casting and renderer before `finish`, so provenance records
the correct source commit. `synth` caches each complete request; changes to voice,
style, model or words produce a new take. Repeat passages reuse identical audio.
`finish` uses MMS forced alignment and the existing loudness/MP3 pipeline; it refuses
missing or zero-length word alignments. `qa` transcribes distinct segments of the
finished MP3 without reference prompts and flags character error rates above 10%.
Review any flagged differences and listen before promoting the voice beyond this trial.

The normal publisher uploads audio and content objects before catalogue documents,
with `meta/app` last. Use the public receiver's actual systemd environment, not the
publisher's stale default paths, and verify the remote catalogue after upload.
The complete example and form tables are included. Existing verified dictionary audio
is reused where its identity matches; missing clips are generated with the standard
Qwen dictionary voice, including the Russian stress adapter for forms. Google TTS
is used only for the scene speech. The lesson retains the normal five-part structure.
