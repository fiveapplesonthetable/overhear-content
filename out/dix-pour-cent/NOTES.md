# dix-pour-cent: notes and decisions

## Show-wide
- Episode titles: S1 episodes are named after the guest star; s01e01 = "Cécile" (Cécile de France).
- Protagonist key `lea` (voice lucie) = the viewpoint character of each scene, so it maps to different show characters
  in different scenes (mostly Camille, also Andréa, Cécile, Sofia, Miranda, Arlette). Its `LABELS["lea"]` gives the
  real name. `tools/compose.py` hardcodes the display label "Léa" for `lea` in REVIEW.md only; the scene JSON labels
  are authoritative.
- The reference learner "Léa" (blonde bob) from `art/style/` is not used as a show character.
- House-style looks reused: Arlette = silver bun + round glasses + raspberry jumper (art/style/fr-01-agence.webp);
  Hervé = deep skin, black beard, navy suit, mustard tie (art/style/fr-03-rendez-vous.webp).
- Swearing (very frequent in the source: merde, putain...) and sexual/drug references are never put in story lines;
  the plot is retold in clean A1 French and the narrator mentions things neutrally where needed.
- Scenes with only male speakers can't carry the protagonist voice (lucie, female) truthfully, so a short male-only
  stretch is merged into a neighbour and told by the narrator in the next scene's bridge (s01e01 scenes 9, 10, 22).

## s01e01 "Cécile"
- 35 scenes in scenes.json, 28 scripted, 7 merged (7, 9, 10, 15, 18, 22, 25).
  - 7 (Andréa offers Sofia the job, Sofia refuses: she is an actress) -> folded into 8 (Andréa hires Camille).
  - 9 (Gabriel and Samuel: "don't lie, just don't tell her the truth"; Samuel leaves for Rio) -> folded into 8 as
    `prev`; male-only, retold in the bridge of scene 11.
  - 10 (Gabriel rejects Cécile's call by mistake) -> `next` into 11; speakers around him are not identifiable from
    the subtitles alone, so the narrator retells it.
  - 15 (Noémie: "Mathias is very, very married") -> `prev` into 14.
  - 18 (Andréa: find Canet's fee, "Improvise") -> `next` into 19.
  - 22 (Gabriel and Hervé at a bar) -> `prev` into 21; male-only.
  - 25 (Gabriel: "she said yes to him") -> `next` into 26.
- Validator "gap between scenes" warnings: these are silences with no subtitles (titles, music, action) between the
  last cue of one scene and the first cue of the next; scene `end` is the end of its last cue as the spec requires,
  so the gaps are expected. The opening "TITRE PRINCIPAL" card (cue 70) is inside scene 1, the
  "ASK - AGENCE SAMUEL KERR" card (cue 104) inside scene 3.
- Speaker attribution from subtitles alone is uncertain in a few places (e.g. who invites whom to lunch in scene 12);
  stories stay with what is certain.
- Narrator lines contain accented proper names (Cécile, Andréa, Noémie, Clémentine, Koltès, Azémar, StarMédia, Côte
  d'Azur). The validator warns "narrator line has French letters" for these because it only whitelists a few names;
  no French words are quoted in narration, so these warnings are expected.
- Notes tokenisation (show convention): one `words[]` entry per whitespace token, punctuation attached; elided forms
  stay one token ("J'ai", "C'est", "l'agence", "n'est") with the lemma of the host word and the elision explained in
  `gram` ("je + ai: ..."); "Qu'est-ce" -> lemma "qu'est-ce que"; hyphenated imperatives ("Passe-moi") one token.
- Scene boundary fix: cue 772 (Cécile: "I'll give you an answer soon") moved from scene 29 to the start of scene 30.
- Speaker attribution is not given by the subtitles; helpers' readings (all noted in the authoring files):
  - s01: the Tarantino message (cue 63) is shown as Gabriel reading it under his breath; journalist = third role.
  - s02: Gabriel has no voice (one male voice); Mathias says his phone lines and his question to Gabriel.
  - s04: coffee order (125-127) given to Camille / Noémie / Mathias.
  - s05: Andréa takes cues 177, 186, 194, 198, 205; Samuel 185, 188/190, 193, 195, 211; Mathias's attack narrated.
  - s12: Gabriel escapes to lunch with Sofia (consistent with s16) and fakes an urgent call (cue 419).
  - s16: wine lines 473-475 and "Merci" 481 to Gabriel; Cécile gets the last line (cue 485) as she arrives.
  - s19: Mathias's phone request (581) is relayed by Noémie; the colleague Gabriel grabs is left unnamed.
  - s23: "la ministre" (cue 635 says "le ministre", but Mathias then calls her a young woman); Miranda's closing
    "Je vais parler à Quentin" is new glue showing she gives in.
  - s26: Andréa's "Camille? Mais pourquoi?" is new.
  - s27: Andréa's insults (blonde, paysanne, péquenaude) left out; "trompée" (feminine) for cue 711.
  - s28: cue 740 to Mathias (tu), Miranda's "lipofilling" merged into Mathias's line.
  - s35: "Mais on a gardé une grande actrice" (probably Gabriel) is given to Andréa (3-role limit).
- Register: the cues have Gabriel and Cécile on *vous* in the opening call and *tu* later; Noémie/Camille mixed;
  scripts follow the cues (see characters.md).
- Clean retelling: swearing dropped everywhere; Andréa's "another Clémentine I slept with" -> "Il y a une autre
  Clémentine?"; cocaine (cue 160) omitted; Magali's threat and Arlette's crude dog joke narrated or omitted.
- Art: all generated with the image-generator from characters.md. Known small slips accepted: s28 Mathias wears a
  thin tie, s29 Arlette's glasses are clear and the dog lacks its eye patch, a few faint outlines in s14/16/17.
  - s30: Mathias's two *vous* (cues 787, 795) normalised to *tu*, as everywhere else between them.
  - s31: cue 805 is a written note; Camille reads it aloud. s32: Arlette kept on *vous* throughout (cues switch to
    *tu* at 842); the Tinder/body jokes omitted; 846 "embobiner" -> "Il manipule tout le monde."
- Final check: validator `OK: 0 errors, 231 warnings` = 201 accented-name warnings + 30 inter-scene subtitle gaps,
  both explained above; qa.py `QA OK (28 scenes)`.

## s01e02 "Line et Françoise"
- 31 scenes in scenes.json, 23 scripted, 8 merged (7, 10, 13, 15, 18, 20, 23, 25).
  - 7 (shawl in the bin, photocopies) -> `next` into 8; 10 (funeral guest lists) -> `next` into 11;
    13 (Line's doubts on the phone, emergency-meeting text) -> `prev` into 12, retold in 14's bridge;
    15 (Andréa's sleepless night: bank site, then a dating-site chat; on-screen text only) -> `next` into 16;
    18 (Camille asks Sofia a favour) -> `prev` into 17; 20 ("I did a Mathias") -> `next` into 21;
    23 (Sofia's goodnight) -> `next` into 24; 25 (scooter ride to the funeral) -> `next` into 26.
- The Line Renaud lunch is split in two by the photocopier scene (6 and 9), as in the episode.
- On-screen texts (BANQUE EN LIGNE, chat messages, WHITE ZOMBIE poster, the meeting text message) are not dialogue.
- Validator gap warnings: silences between scenes (credits/music/action), expected.
- Text rule learned: compose/validate split sentences on "…", so an ellipsis inside a line splits it into two
  sentences; use commas inside lines ("Euh, oui, outjet!") and keep "…" only at the end of a line.
- Speaker readings / changes (details in each authoring file):
  - s01: Françoise says "Vous n'avez pas de famille... J'ai une vie" (40-42); "Désolée" (48) is Andréa.
  - s02: Hervé is the one "six days" without; Camille's three months retold as "Je suis seule depuis trois mois".
  - s03: Andréa and Mathias on *vous* as in the cues; "Mathias, stop that" gloss for the bare "Camille!".
  - s04: sexual talk (188-195) out of the story; the donor line simplified ("Entre un donneur anonyme et un ami...").
  - s06: the Rio "orgy" rumour -> "les rumeurs de Rio".
  - s12: lines 368/375/379 left out (register unclear). s13 summary corrected: Gabriel has the doubts, Line doesn't.
  - s14: Andréa has no money (430-431), Mathias offers support (403-404).
  - s17: Hervé tells the Line/Samuel/Françoise story; merged 18 mentioned in the outro.
  - s21: Andréa's lie is retold without naming her listener (cue 592 unclear).
  - s28: Catherine has no voice; two of her lines go to Hippolyte; Camille: "Ton père, c'est Mathias?" (new).
  - s29: kept clean (nothing happened, she fell asleep).
  - s30: it is Gabriel who promises to take Andréa to Holland (taking back 628-629); "Salaud!" -> "Tu es bête!".
  - s31: "Tu es un lâche!" (masculine, said to Mathias); insults dropped; Noémie lights Camille's cigarette.
  - s22: Hélène's "people jump on dead bodies" (658) retold as "Tout le monde veut la place de Samuel".
  - s24: Hippolyte and Camille on *vous* here, as in the cues (they were on *tu* in s08).
  - s26: the agents' squabble reduced to Mathias's summary; eulogies condensed; the sung lyric (749) not used.
- Final check s01e02: validator `OK: 0 errors, 175 warnings` = 149 accented-name warnings + 26 inter-scene gaps;
  qa.py `QA OK (23 scenes)`.
