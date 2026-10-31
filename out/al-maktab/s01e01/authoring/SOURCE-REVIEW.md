# Al Maktab S01E01: bounded Arabic salary taster source review

## Exact scope and explicit omission

Three retained utterances, seven native written words, from 20.940–25.820 seconds of the [official MBC Shahid episode-one unexpected-call clip](https://www.youtube.com/watch?v=xqJ8wGtY_hg). The verified uploader is @MBCShahid. The official clip is 94.296 seconds; this lesson is a short taster, not a whole episode.

The original four-cue partial native source SRT remains **byte-for-byte unchanged**, SHA-256 `58680ec00172049b14057dad649f0b0c5ba88b3a2cff0d9f5bd3fe295a7ab5f5`. The original source coverage range 20.940–28.900 seconds is retained as provenance, not a claim that every cue is spoken in this taster. Cues 1–3 form a complete salary correction: Malik describes staff payment as a monthly allowance, and his female colleague calls it a salary.

Cue 4 (27.620–28.900), the responsibility statement, is deliberately omitted from the public story, all replays, teaching and recap. The source itself is corroborated, but generated speech failed the exact pronunciation gate: a finite retake was decoded with a final hamza by both independent engines (`براء` and `برأة`), rather than the intended outside expression. We do not rewrite source words, guess a pronunciation or waive the difference. `OMITTED-SOURCE.json` retains the exact cue, timestamps, source hash and reason. The earlier excluded unclear filler around 26.6–27.6 and disputed continuation after 28.9 remain excluded.

English teaching now covers only the self-correction, possessive ending, plural verb and noun/adjective order. All three retained native texts, translations, detailed word annotations and form tables are unchanged. No untested farewell or additional Arabic line is added.

## Acquisition and independent checks

The exact public clip was fetched through the existing download skill/put.io after direct local media delivery returned HTTP 403: transfer 108832920, file 1620360149. No DRM bypass, full-show acquisition, dual-subtitle backtranslation or original deletion occurred. The private original MP4 has 31,031,792 bytes and SHA-256 `3bdfb26329718748cf22bbb68b1e7ea42c97ae65594a4457a4a0a16bc9e21fda`. No source audio/video is committed or publicly served.

No native or automatic caption tracks were exposed, and no burned dialogue captions were visible in sampled source frames. The original container audio tag `eng` is unreliable. Three independent unprompted source decodes detect Arabic: cached small CPU (0.989448), large-v3 CPU (0.986554) and large-v3-turbo GPU (0.954590). The small model garbles several colloquial lines and is not treated as authoritative. Both stronger source decoders agree on every word retained in the taster and on the separately documented omitted source clause. Added punctuation and the division after the self-correction do not add speech. Other wording is omitted rather than guessed. These are model/text and visual source checks, not a human-listening certificate.

Private evidence directory: `/mnt/agent/pilot-source-discovery/arabic-research/`. Original decoding evidence: `original94s-large-auto-asr.json` and `/mnt/agent/narrator-runs/codex-seven-tasters/source-checks/ar-official-source-large-asr.json`. The detailed proof is `selected-source-proof.json`; its windows are source provenance, not public playback timings. Final generated audio requires its own word-level alignment and complete speech QA.

## Speaker identity and private references

Malik is visible speaking in the source meeting. During the salary response the camera pans from his reaction toward the woman in the charcoal abaya; the inspected private `colleague25.9.jpg` shows her. Her specific character name remains unverified, so the honest descriptive role `colleague` / زميلة is used. The other woman in pink is present but has no spoken lesson role.

Actual original references remain private: male 20.820–24.380 seconds and 27.620–28.900 seconds; female salary response 24.380–25.820 seconds. The female reference is genuinely very short. Do not add neighboring male speech or repeat-pad it to pretend it is a longer clean reference. The native backend owner must test whether conditioning and Saudi Arabic delivery are adequate. Cached generic Arabic support is not certification of Saudi pronunciation.

## Public audio and honest closing

Every public native line must be synthesized with a supported Arabic backend and pass independent production speech/quality checks. Original show clips and derived speech cuts stay private; no `sourceAudio` fields are present in the public candidate script. Arabic remains in logical order, and every native note word has a half-open Unicode codepoint span. Arabic pronunciation fields remain null under the native-script contract; no guessed stress or narrow actor-IPA claims are displayed. Generated native speech still requires independent pronunciation QA.

The script declares `format: taster`. Its final native reinforcement repeats the genuine salary correction after the English send-off; it is not mislabelled a newly spoken farewell. This follows the explicit taster contract and adds no invented Arabic speech.

## Learning metadata and limits

One focused Learn note explains the salary correction, allowance versus regular pay and noun/adjective order, using exact scene examples. All seven retained ordinary dictionary lemmas have individually sourced histories; all ten italic Learn word occurrences (five distinct surfaces) resolve to the retained dictionary and origins. The optional responsibility Learn note and its seven unused heads are removed. Forms for the retained words are unchanged. The detailed claim/source review is `ORIGIN-REVIEW.md`. A real serving candidate still requires production’s complete origin inventory.

## Illustration

`scene-01.webp` is 1024×1024 WebP, generated with the built-in image tool. The house-style contact sheet supplied style; inspected private source frames supplied clothing and setting. The final image was edited to match the chosen pre-call staff-pay discussion: exactly three cartoon adults, source-matching clothing, office blinds, grey chairs and lamp; Malik gestures with an empty hand. No phone, text, digits, logos or subtitles. It depicts roles rather than actor portraits.

Final prompt: preserve the three existing cartoon characters, clothing, colours, office blinds, chairs, lamp and table; remove the telephone and sound marks; Malik gestures earnestly with an open empty palm as he discusses staff pay. No new props, text or branding.
