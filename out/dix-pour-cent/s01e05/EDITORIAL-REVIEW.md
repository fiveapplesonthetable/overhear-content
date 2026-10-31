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
