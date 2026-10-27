# Authoring module for dix-pour-cent s03e06 scene 14 (cues 623-626).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s03e06/scene-14.json

ID = "dix-pour-cent-s03e06-scene-14"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 14
TITLE = "Le royaume des morts  (The Realm of the Dead)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "directeur": "theo"}
LABELS = {"lea": "Gabriel", "directeur": "Le réalisateur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 623-626. On the set, the stand-in delivers her solemn line "
               "while the director complains about rustling leaves.")

INTRO = ("The cameras roll as the stand-in delivers her solemn line on the forest film set. "
         "However, unexpected noises on the floor disrupt the delicate atmosphere during the take. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Silence, elle commence sa réplique.",
  "Quiet, she begins her line.",
  [(623, "Je reviens du royaume")], "Calling attention"),
 ("directeur", "Je reviens du royaume des morts.",
  "I return from the realm of the dead.",
  [(623, "Je reviens du royaume des morts")], "Delivering line"),
 ("lea", "Pour vous dire adieu enfin.",
  "To bid you farewell at last.",
  [(623, "pour vous dire adieu")], "Finishing sentence"),
 ("directeur", "Oh là! Coupez tout de suite!",
  "Oh my! Cut right away!",
  [(624, "Oh là")], "Stopping take"),
 ("lea", "Quel est le problème cette fois?",
  "What is the problem this time?",
  [(625, "Oh là")], "Inquiring problem"),
 ("directeur", "J'entends un bruit très gênant.",
  "I hear a very annoying noise.",
  [(626, "Moi, j'entends beaucoup les feuilles")], "Complaining about noise"),
 ("lea", "C'est seulement le vent nocturne.",
  "It is only the night wind.",
  [(626, "Moi, j'entends beaucoup les feuilles")], "Offering explanation"),
 ("directeur", "Les feuilles qui tombent par terre!",
  "The leaves falling on the floor!",
  [(626, "les feuilles qui tombent par terre")], "Specifying noise"),
 ("lea", "Le bruit donne un ton dramatique.",
  "The noise gives a dramatic tone.",
  [(626, "quand même")], "Reframing sound"),
 ("directeur", "Ce craquement gâche toute l'émotion.",
  "This crunching ruins all the emotion.",
  [(626, "quand même")], "Rejecting explanation"),
 ("lea", "L'ingénieur du son peut nettoyer ça.",
  "The sound engineer can clean that.",
  [(626, "quand même")], "Proposing fix"),
 ("directeur", "Tu as toujours une solution, Gabriel.",
  "You always have a solution, Gabriel.",
  [(626, "quand même")], "Yielding to agent"),
 ("lea", "Gardons cette magnifique prise maintenant.",
  "Let's keep this wonderful take now.",
  [(623, "Je reviens du royaume")], "Wrapping take"),
 ("directeur", "D'accord, c'est bon pour moi!",
  "Agreed, it is good for me!",
  [(623, "Je reviens du royaume")], "Concluding take"),
]

WALK = [
 (0, None,
  "'Quiet, she begins her line.' Gabriel urges everyone on set to listen. "
  "The verb 'commencer' takes a direct object here."),
 (1, None,
  "'I return from the realm of the dead.' The director recites the theatrical script line. "
  "The noun 'royaume' evokes a mythical realm."),
 (2, None,
  "'To bid you farewell at last.' Gabriel completes the tragic farewell sentence. "
  "The phrase 'dire adieu' expresses a definitive parting."),
 (3, None,
  "'Oh my! Cut right away!' The director suddenly halts the recording. "
  "The imperative 'coupez' orders the camera operators to stop."),
 (4, None,
  "'What is the problem this time?' Gabriel asks what caused the interruption. "
  "The interrogative adjective 'quel' agrees with the masculine noun probleme."),
 (5, None,
  "'I hear a very annoying noise.' The director points out an acoustic defect. "
  "The adjective 'genant' describes an unwelcome disturbance."),
 (6, None,
  "'It is only the night wind.' Gabriel downplays the extraneous sound. "
  "The adjective 'nocturne' relates to the night."),
 (7, None,
  "'The leaves falling on the floor!' The director identifies the rustling debris. "
  "The relative clause 'qui tombent' describes the action of the leaves."),
 (8, None,
  "'The noise gives a dramatic tone.' Gabriel highlights the poetic mood. "
  "The adjective 'dramatique' conveys heightened theatrical intensity."),
 (9, None,
  "'This crunching ruins all the emotion.' The director remains unconvinced by the sound. "
  "The verb 'gacher' means to spoil or ruin something."),
 (10, None,
  "'The sound engineer can clean that.' Gabriel suggests fixing the audio in postproduction. "
  "The modal verb 'peut' indicates technical capability."),
 (11, None,
  "'You always have a solution, Gabriel.' The director admires Gabriel's endless resourcefulness. "
  "The adverb 'toujours' expresses constant persistence."),
 (12, None,
  "'Let's keep this wonderful take now.' Gabriel presses to save the take and move on. "
  "The imperative 'gardons' calls for retaining the shot."),
 (13, None,
  "'Agreed, it is good for me!' The director finally gives his approval. "
  "The phrase 'c'est bon' signals complete satisfaction."),
]

OUTRO = ("Gabriel successfully saves the tricky scene despite the director's complaints about ambient noise. "
         "With the forest scene safely recorded, Gabriel can now breathe a sigh of relief. "
         "Now, let's review the scene one last time.")

CLOSING = ("directeur", "D'accord, c'est bon pour moi!")
