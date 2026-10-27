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

## s01e03 "Nathalie et Laura"
- 31 scenes in scenes.json, 22 scripted, 9 merged (4, 5, 8, 12, 21, 23, 27, 29, 31).
  - 4 (Gabriel vs Mathias, male-only) -> `prev` into 3; 5 (Mathias asks Dominique a favour for Camille) -> `next`
    into 6; 8 (Hervé and Hugo, male-only) -> `next` into 9; 12 ("Merci, Papa") -> `next` into 13;
    21 (Camille: "I want to be an agent") -> `prev` into 20; 23 (coffee machine) -> `prev` into 22;
    27 (ten out of ten, and no) -> `prev` into 26; 29 (Sofia's play, stage lines) -> `next` into 30;
    31 (StarMédia's offer to Mathias, male-only cliffhanger) -> `prev` into 30, told by the narrator in 30's outro.
- Voice constraint: only two female voices exist (lucie for `lea`, emilie); scenes with three women (e.g. 26:
  Nathalie, Laura, Solveig) give the third one's lines to the narrator.
- Validator gap warnings: silences between scenes, expected. Accented-name warnings: names only.
- Speaker readings / changes (details in each authoring file):
  - s01: writes out "M." as "monsieur" (cue 6), replaces Camille's swear word in cue 9 with "Oh non! Je suis désolée.", and assigns cue 15 ("Non, Gabriel, on ne peut pas toujours tout arranger!") to Andréa.
  - s02: simplifies cue 51 ("fais-la se tenir droite") to "Emmanuel, elle doit se tenir droite."; cue 48 ("Pour Gabriel, même une catastrophe, c'est juste un accroc!") is given to Laura.
  - s03: simplifies cue 59 to mock-formal "Laura Smet, Solveig Akerfelt vous veut pour son prochain film.", drops Gabriel's swear word in cue 77 ("Exclusif, hein?"), assigns cue 79 ("Non, la mère et la fille.") to Gabriel, and retells merged s04 (cues 87–99, male-only) in s03's outro.
  - s06: merged s05 (cues 100–106) is retold in the intro bridge; Noémie's crude lines (114, 121) and Hervé's insult (134) are dropped.
  - s07: the partners' opening chatter (142–150) is narrated in the intro; Arlette is narrated out to stay within three voices, with cue 154 given to Gabriel and cue 161 to Andréa.
  - s09: merged s08 (cues 166–182, Hervé and Hugo) is retold in the intro bridge; Sofia is narrated out of the story (2-female-voice limit), cues 186 and 188 are given to Camille, and cue 197 is given to Hervé.
  - s10: simplifies "soit sur un chalutier, soit sur une île" (cue 200) to "sur un bateau" and "enfermée ... sur un bateau de pêche 24h/24" (cue 208) to "avec elle sur un bateau, jour et nuit".
  - s11: omits the bodily-fluids joke in cue 223, simplifies "mon lieu de travail" (cue 225) to "mon agence", cleans up the breakup/sister lines in cues 245–247 to "Tu m'as quitté avec un SMS!", and simplifies cues 254–255 to "Je vais remplacer Brancillon."
  - s13: merged s12 (cues 259–263, "Merci, Papa") is retold in the intro bridge; omits "couché avec lui" in cue 267 and "Putain !" in cue 303, simplifies "tu espionnes pour Mathias" (cue 283) to "Tu travailles en secret pour Mathias?", and uses feminine "désolée" (cue 306) for Noémie.
  - s14: narrates Arlette's opening question about her dog (cue 313) in the opener, simplifies "décédé" (cue 318) to "mort" and "nous coller aux basques" (cue 332) to "rester ici", and shares the partners' worries at the end (cues 332–336) between Gabriel and Andréa (3-role limit).
  - s15: uses feminine "Tiens-toi droite." for cue 350, and narrates Gabriel's question in the parallel office cut so Mathias carries the male voice while Laura's refusal is kept.
  - s16: writes out the numbers in cues 379 ("Été deux mille onze.") and 384 ("treize ans"), omits the sexual joke in cue 404, replaces vulgar "chiante" in cue 405 with "capricieuse" (from cue 409), and folds Hervé's objection (cues 410–413) into Laura's own hesitation (3-role limit).
  - s17: narrates Hervé's long drinks list (cues 414–418) and keeps Solveig's replies; the two readings of the script are shortened and use different lines so no story line repeats.
  - s18: summarises the crossover at the lift (cues 446–455) in the intro; adapts Gabriel's request to Hervé (cues 467–468) in the 1st person for Laura ("Hervé, s'il te plaît! Je veux mon thé.") to stay within three voices; writes out "Mme" as "Madame" (cue 470); and retells Gabriel's voicemail at the end (cues 483–489) in the outro.
  - s19: drops the cocaine reference in cue 512, keeping "Et ne bois pas trop!".
  - s20: merged s21 (cues 545–555, Camille telling Mathias she won't call Besnehard because she wants to be an agent) is folded into lines 13–17 of s20's story.
  - s22: gives Mathias's and Arlette's lines in the meeting room (cues 557, 562, 565–566) to Andréa (3-role limit), drops swearing in cues 565 and 583, and summarises merged s23 (Zinedine Soualem and the coffee machine, cues 585–597) in s22's outro.
  - s24: keeps Gabriel on *vous* throughout with Solveig (dropping `t'a` / `te` in cues 601, 604), drops "Merde !" in cue 606, removes guillemets in cue 624, and gives Hervé's and Mathias's closing lines (cues 636, 639) to Gabriel (2-role limit).
  - s25: the dating-site handle "Impôts-du-cœur" (cue 656) is omitted; Colette's rejection is kept clean; Camille's knock at the door (cues 681–683) is narrated in the outro.
  - s26: Solveig's lines are told by the narrator (2-female-voice limit), leaving Nathalie (`lea`), Laura (`emilie`), and Gabriel (`theo`), with Mathias's lines given to Gabriel; merged s27 (cues 752–763, the agents' "dix sur dix" celebration and the double refusal) is retold in s26's outro.
  - s28: the "petit cul" joke (cues 785–788) is omitted.
  - s30: merged s29 (Sofia's stage monologue, cues 795–809) is retold in s30's intro, and merged s31 (François of StarMédia offering Mathias a partnership, cues 847–866, male-only cliffhanger) is retold in s30's outro; Gabriel's cues 828–829 are given to Hervé so François can use the second male voice (`marcel`).
- Final check s01e03: validator `OK: 0 errors, 112 warnings` = 84 accented-name warnings + 28 inter-scene gaps;
  qa.py `QA OK (22 scenes)`.
