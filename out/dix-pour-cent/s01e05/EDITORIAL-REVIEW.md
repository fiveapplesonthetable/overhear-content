# S01E05 editorial review

Reviewed batches are ready for central audio rendering and listening checks; this file does not certify rendered audio or public publication.

## Batch 1: scenes 01–04

Checked the French dialogue and speakers against source cues 1–88. Corrected the episode introduction to Julie Gayet and JoeyStarr, the eighteenth-century film, and the actual film-set dispute. Split Julie's “Moi aussi!” from JoeyStarr's following insult. Removed invented hallway, taxi, dropped-toast and eavesdropping details from the explanations.

Rewrote every walkthrough explanation for these four scenes. Each one now teaches contextual meaning, a useful word, a French construction or a spoken-language feature. The teacher speaks English; all French replay lines remain separate native-role segments. Restored complete English translations, including contractions, across all repeated story and replay lines.

Reviewed word annotations in context, including articles versus object pronouns, impersonal “il y a”, “en” with material and lateness, affirmative “si”, “plus” in a farewell, and “attention” as a kind gesture. Corrected adjective forms, relevant gender forms, examples and the mixed noun/verb uses of “dîner”. Removed unsupported generated historical/regularity claims. Inspected the four existing illustrations and found them consistent with the revised scenes.

Validation: `python3 -I tools/validate.py out/dix-pour-cent/s01e05 --require-notes` reports 0 errors. Remaining episode-wide teaching warnings concern scenes outside this reviewed batch; source timeline-gap warnings describe the original episode's cuts. No shared dictionary, cast or learn files changed.

The other scenes are not approved by this review yet.

## Batch 2: scenes 05–08

Checked against source cues 89–157 and read the entire remaining episode source through cue 739 for continuity. Restored “Non, Julie!” to Andrea instead of the previous invented reply by Julie. Kept learner simplifications explicit in scene 06. Rewrote every English explanation, completed all contraction-bearing translations, and removed unsupported actions/locations from the connective narration.

Corrected ordinary “he”, “has”, “the”, “all”, “door”, “girl”, “in costumes” and “pass for” annotations that previously pointed to unrelated multiword entries or senses. Reviewed all noncanonical lexicon forms, examples and pronunciation entries for these scenes, and checked the four illustrations. No shared metadata changed. Validation: 0 errors, 95 warnings across the episode; scenes 01–08 have no explanation warnings.

## Batch 3: scenes 09–12

Checked dialogue, speakers and plot against source cues 158–251. Split the writer's “Jonathan” from Arlette's correction “Ryan”, preserving the actual exchange. Removed the agent-planning question wrongly assigned to Julie from scene 11; the remaining 13-line lesson starts with Gabriel's promise. Documented dialogue compression in the three-role scene 10. All English explanations rewritten and repeated translations completed.

Corrected death as a noun, affirmative comparative “plus”, plural/impersonal expressions, object pronouns, note versus word, dear versus expensive, a fresh start versus departure, surprised as an adjective, share versus apart, and the separate components of “quelque chose”. Reviewed noncanonical forms/examples and the illustrations. Scene 12 artwork requires replacement for Arlette/dog continuity; scene 05 is also held for JoeyStarr art correction. Those two scripts/notes are ready for rendering, but this review does not approve those illustrations for publication. Scenes 09–12 validator: no explanation warnings; episode-wide validation: 0 errors, 86 warnings.

## Art continuity correction: scenes 05 and 12

Used the built-in imagegen tool in edit mode after inspecting target images and established references. Scene 05 now uses scene 01's JoeyStarr and Samir identities/costumes; scene 12 now uses scene 09's Arlette and small tan dog. Viewed both generated outputs and both final 1024×1024 WebP files. These two illustrations are now approved; the earlier publication holds for their artwork are cleared. Scripts/notes stayed frozen.

Prompt 05: Keep scene 05's composition, actress, courtyard and film equipment; replace the right-hand actor with scene 01's Black, close-cropped, clean-shaven servant in a cream shirt, brown breeches, white stockings and buckled shoes; replace the director with scene 01's dark-haired, bearded director in a navy sweater and tan trousers. Preserve the warm flat-color style and add no text or people.

Prompt 12: Keep scene 12's composition, Mathias, office and pink armchair; replace the left-hand woman with scene 09's light-skinned Arlette, swept-up brown hair, round optical glasses, olive outfit and silk scarf; preserve her scissors gesture. Match scene 09's tan French bulldog on the chair. Preserve the warm flat-color style and add no text or people.

## Batch 4: scenes 13–15 and 17

Checked against source cues 237–336, including the intervening scenes merged into scene 17. Removed the invented horse fall; Julie's injury followed the greenhouse ladder escape. Rebuilt scene 17's 16-step walkthrough in story order, removed the duplicate wrong-index tailbone explanation attached to a thank-you, and restored complete English for the surprise, entrance, insistence and departure lines. All explanations now teach a useful contextual feature.

Corrected river as a common noun, woods rather than drink, running rather than current, schedule components, impersonal objects, reflexive forms, and positive comparisons. Added proper noun/verb forms and examples. Four illustrations inspected; no generation needed for this batch. One notes-only follow-up to frozen scene 09 adds the positive comparative sense of “plus”; its already-correct token gloss and script are unchanged. Validation before that additive meaning: 0 errors, 74 episode warnings; one warning in scene 13 merely flags the accent in the proper place name Corrèze.

## Primary-video check: scene 01

Inspected private CPU-extracted source frames and burned bilingual subtitles for the opening set dispute. Corrected the remaining inherited speaker error: Julie, replying to JoeyStarr, says “Je travaille, d'accord?” Revised its English explanation accordingly. The other opening speaker assignments, including the split “Moi aussi!” / “Allez à vos dîners mondains!”, match the visible exchange. Scene 01 is reapproved for rendering after this correction. No private video frames or signed URLs are committed.

## Primary-video correction pass: scenes 02–15 and 17

CPU-extracted private source frames, burned bilingual subtitles and denser one-frame-per-second sequences supersede the earlier subtitle-only speaker assumptions. No source frames, audio, tokens or signed URLs are committed.

- 02: Andrea brings breakfast and says “Voilà. De rien!”; corrected from Colette.
- 03: Sofia's autograph exchange is with Hervé, not Camille. Removed that detour and its greeting, keeping 12 lines focused on Camille, Sofia's overheard film news and Mathias.
- 04: Female set assistant is now `assistante_plateau`, coordinated with central cast/voice ownership.
- 05: Documented brief crew-report folding into the director for three lesson voices.
- 06: Gabriel advises Julie. Corrected Andrea's incorrectly assigned lines and all narrative references.
- 07: Andrea listens to JoeyStarr and describes her attraction to Colette. Corrected the agent, female agreement and invented Gabriel/Anna narrative.
- 08: Removed the last reassurance, which actually belongs to Arlette and Marie-Sophie at the agency, not Andrea and Julie on set.
- 09: Arlette makes the comparison with her first husband; corrected from Marie-Sophie.
- 10: Dense frames confirm Camille's mother/fan lines and Noémie's surprised reply. Only Hervé's opening question is deliberately folded into Camille's role, explicitly recorded in the review sheet; the visiting actor's request remains explicitly recast as Noémie's reply.
- 11: Replaced the invented locked-greenhouse escape. JoeyStarr fakes the borrowed-phone call, Julie asks for her phone back, then the agents hear alarm outside. All French lines now follow that source sequence; three roles and 12 lines.
- 12: Removed the unsupported dog/armchair story. The brief “his armchair” speaker still needs an independent primary check; this scene remains held pending that check.
- 13: Noémie pitches the notice idea to Mathias while Camille listens from the doorway. Corrected the fabricated Camille/Hervé exchange, the narrator and feminine agreement.
- 14: Gabriel counsels Julie. Brief crew scheduling information and Andrea's reassurance are explicitly folded into the director/Gabriel for three lesson roles.
- 15: Andrea gives all encouragement, including the costume comment; no separate costumière or Gabriel speaks these lines.
- 17: Checked the surprise, bath, injury aftermath and departure against source frames; roles and revised walkthrough order agree.

Scripts/notes 02–11, 13–15 and 17 are reapproved for rendering after these changes. Artwork 06, 07, 08, 11, 12, 13, 14 and 15 is held for necessary role/scene corrections. Scene 12 remains held for its short speaker check as well. Episode validator: 0 errors; proper-name accent warnings and later unreviewed lessons remain.

## Art correction after primary-video role audit

Used the built-in imagegen edit tool for exactly the eight necessary affected illustrations, with inspected established character references. Final 1024×1024 WebP files were viewed together after conversion.

- 06 and 14: Gabriel advises Julie.
- 07 and 15: Andrea talks with/encourages JoeyStarr.
- 08: removed the invented background Andrea/Julie tea scene.
- 11: replaced the invented greenhouse/ladder image with JoeyStarr's borrowed-phone excuse at the restaurant table, watched by Julie.
- 12: removed the unsupported dog on the armchair.
- 13: Noémie presents the proposed notice to Mathias; removed the invented Hervé/Camille staging.

These eight illustrations are approved for their corrected lesson scripts. Full prompts and built-in-tool provenance are recorded in `ART-REVIEW.json`. The independent source-audio/register check continues and is a separate publication gate.

## Original French audio and register correction

Unprompted cached local CPU ASR of the private original French audio completed seven bounded diagnostic clips: opening, office/armchair, agent conversations, morning/office arrival, borrowed-phone meeting, encouragement, and hotel visit. The remaining source queue was handed to central GPU QA; this worktree runs no GPU process.

The working dual subtitles' French track is backtranslated. All reviewed scene sheets now explicitly identify the dialogue as learner adaptation and label source-linked lines as adapted, with no “verbatim French” claim. Lesson 01's spoken introduction also identifies it as an adaptation. Original-audio evidence was used to repair register, rather than preserving the synthetic subtitles' forms:

- 01: familiar TU, “Tu es”, “Va”, “tes”, “Articule”, “s'il te plaît” and “Appelle”; revised teaching and word forms.
- 06: Joey addresses Andrea with TU, “Tu as entendu”.
- 08: Gabriel/Sofia retain professional VOUS, including “content pour vous”.
- 10: Mathias continues VOUS with Noémie, including the reminder.
- 12: Mathias addresses Arlette with VOUS; Arlette replies with TU. The audio names Jean Gabin's armchair. The ending is “couic”, a sound signalling the character's abrupt end, rather than a film-set “Coupez”. Revised title, native lines, explanations and notes accordingly.
- 13: Mathias uses VOUS with Noémie in his question and instructions.

The word “couic” and its /kwik/ pronunciation were cross-checked against [Le Robert](https://dictionnaire.lerobert.com/definition/couic) and [Larousse's French–English entry](https://www.larousse.fr/dictionnaires/francais-anglais/couic/19621); the scene-specific implication of being finished off comes from the source context. No generated etymology is supplied.

Validation: 0 errors, 78 episode-wide warnings. Later scenes 18–30 remain unapproved and are not included in this provenance/register approval. Scene 12's short armchair speaker is still flagged for independent central confirmation despite the clearer actual wording.

## Batch 5: scenes 18–21, original-audio approval

Inspected source-video frames and independent unprompted original-French GPU ASR for the dinner/birthday, proposed buyout, father/son warning, hotel reception and doorway exchanges. Corrected Andrea's opening dinner reply, Mathias's production proposal and Catherine's response, and removed unsupported birthday-boyfriend/cake and breakfast-tray narration. Rebuilt every English walkthrough and complete translation in story order. All four lessons explicitly identify the French as learner adaptation. Reviewed contextual word lemmas, object pronouns, affirmative si, news versus new, ready versus lending, reflexive warning forms, future forms, noun genders, adjective agreements, IPA and examples. Removed residual invented suffix histories and stock adverb-placement claims from the first twenty reviewed lessons.

Additional original-audio/visual follow-ups to earlier lessons: Sofia addresses Joey with VOUS in 04 while he uses TU; removed 05's unsupported plural command; 11's two brief Andrea calls are explicitly folded into Gabriel, rather than falsely assigned to Joey. Names alone at a distance are not treated as authoritative ASR evidence. Scene12's short armchair speaker remains for independent central confirmation.

Separate art commit corrects 18 (Gabriel/Andrea dinner), 19 (Mathias identity) and 21 (Gabriel/Andrea doorway without a tray). Built-in image edits used inspected references, final square1024 WebPs inspected, full prompts in ART-REVIEW.json. These three images are approved. Scenes18–21 are approved for central rendering/listening after integration. No private source media or credentials committed.

## Batch6: scenes22–25

Reviewed complete source-video sheets and independent unprompted original-French ASR for the car argument, petition, roadside help, cancelled scene, barn shoot and calmer return drive. Female set assistant corrected in23 using the existing centrally coordinated cast entry. Camille's petition opinion restored as a statement rather than an invented question; Mathias's replies are explained in narration while native dialogue retains three roles. Rewrote every walkthrough with contextual vocabulary/construction teaching, complete English meanings and adaptation provenance. Corrected positive plus, ordinary articles/subjects, word-level impersonal components, tax terminology, feminine referring pronouns, polite versus plural vous, commands, object pronouns, pain, so much, relationship expressions and adjective forms. Unsupported generated histories and false sound-based related words removed. Detailed entries include actual adjective/noun contrasts and reflexive/impersonal forms.

Separate artwork19faf4005 corrects22/23/25 identities and female assistant; all inspected final square1024 outputs approved. Existing24 illustration matches the revised learner sequence. Scenes22–25 are approved for central rendering/listening. Validation:0 errors; remaining teaching warnings belong to later unreviewed scenes, and these four have only proper-name accent warnings. No private source media committed.

## Final batch: scenes27–30

Complete source-video sheets and independent unprompted original-French ASR reviewed. Corrected meeting speakers and swapped the draft's reversed Julie/Didier callbacks in27. Hervé's fake Spielberg voicemail and Andrea's repeated name were falsely assigned to Gabriel/Julie in28; the voicemail is now explained in the introduction and native dialogue starts with Gabriel's actual callback. Brief Andrea-agent instructions are explicitly folded into Gabriel to keep three voices. Corrected Julie's fear of being judged irresponsible. In29 Noémie's petition referral is omitted rather than assigned to Mathias; restored professional VOUS throughout the Gabriel/Sofia exchange before Sofia's explicit request to change to TU. In30 restored actual family TU and removed Hippolyte's warning question falsely assigned to Camille; his request is explicitly recast as Catherine's for three speaking roles.

Every explanation rewritten with contextual word/construction teaching, complete English translations preserved, and word annotations reviewed against each occurrence. Corrected noun/verb distinctions in birthday celebration and injuries, news/new, preferred/favourite, custody/keep, singular/plural polite forms, direct/indirect objects, impersonal components, completed/reflexive forms and compound components. Added reviewed forms/examples for fêter and blesser, reflexive forms and actual adjective/noun contrasts. Removed inherited false historical claims and unrelated sound-alike suggestions. Casser's incorrect generic être-helper claim is corrected in the notes wherever used.

Artwork29/30 was corrected separately in19faf4005 and approved after inspection; existing27/28 art matches the learner story. A short11 acknowledgement explanation was refined during strict-teaching audit; its native dialogue stayed fixed. Authoring03 now uses the same English spelling Andrea already present in narration/notes.

Full episode validation with --require-notes --strict-teaching:0 errors; every playable lesson meets the teaching threshold. Private source media never committed. This editorial review is separate from central audio render/listening QA and public publication. Two short speaker details remain held for independent central confirmation:12 Jean Gabin armchair line (currently Mathias), and30 final confession line (currently Mathias; recipient not specified in the lesson). All other27–29 editorial material is approved for central rendering/listening;30 remains on the stated short-speaker hold.
