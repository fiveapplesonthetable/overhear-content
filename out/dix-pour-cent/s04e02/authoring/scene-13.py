# Authoring module for dix-pour-cent s04e02 scene 13 (cues 789-808).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e02/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s04e02/scene-13.json

ID = "dix-pour-cent-s04e02-scene-13"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 13
TITLE = "L'avenir de l'agence  (The Future of the Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Gabriel", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 789-808. Outside the community center, Gabriel confronts producer Mathias "
               "about losing Dany Boon to a rival agency.")

INTRO = ("Outside the community hall, Gabriel intercepts Mathias to question his aggressive maneuvers behind the scenes. "
         "Facing the threat of losing top talent to rival agencies, Gabriel fights to keep ASK afloat. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Hé toi, attends une seconde, Mathias!",
  "Hey you, wait a second, Mathias!",
  [(789, "Hé, toi")], "Calling out"),
 ("mathias", "Ce n'est pas fini pour Auteuil.",
  "It is not over for Auteuil.",
  [(790, "ce n'est pas fini")], "Discussing role"),
 ("lea", "Écoute, la situation devient trop compliquée.",
  "Listen, the situation is becoming too complicated.",
  [(791, "c'est compliqué")], "Pointing out tension"),
 ("mathias", "Je te tiens au courant demain.",
  "I keep you posted tomorrow.",
  [(793, "Je te tiens au courant")], "Dismissing concern"),
 ("lea", "Tu vas céder au chantage maintenant?",
  "Are you going to give in to blackmail now?",
  [(795, "au chantage")], "Accusing producer"),
 ("mathias", "Je suis producteur de cinéma maintenant.",
  "I am a cinema producer now.",
  [(797, "Je suis producteur")], "Asserting new role"),
 ("lea", "Tu dois protéger nos acteurs préférés.",
  "You must protect our favorite actors.",
  [(798, "le meilleur acteur")], "Appealing to past"),
 ("mathias", "Je choisis le meilleur acteur possible.",
  "I choose the best actor possible.",
  [(798, "le meilleur acteur")], "Prioritizing film"),
 ("lea", "Si Dany quitte ASK, nous coulons!",
  "If Dany leaves ASK, we sink!",
  [(799, "quitte ASK")], "Warning catastrophe"),
 ("mathias", "L'agence va commencer à couler vite.",
  "The agency will start sinking fast.",
  [(800, "commencer à couler")], "Acknowledging risk"),
 ("lea", "J'appelle Franck pour tout arranger.",
  "I call Franck to arrange everything.",
  [(803, "J'appelle Franck")], "Taking action"),
 ("mathias", "Il filtre tous mes appels récents.",
  "He filters all my recent calls.",
  [(805, "filtre mes appels")], "Doubting success"),
 ("lea", "Allô Franck? Oui, c'est Gabriel ici.",
  "Hello Franck? Yes, it is Gabriel here.",
  [(806, "c'est Gabriel")], "Reaching actor"),
 ("mathias", "Bonne chance pour convaincre notre ami!",
  "Good luck convincing our friend!",
  [(803, "J'appelle Franck")], "Wishing luck"),
]

WALK = [
 (0, None,
  "'Hey you, wait a second, Mathias!' Gabriel catches up with the former agent. "
  "The imperative 'attends' requests a brief moment."),
 (1, None,
  "'It is not over for Auteuil.' Mathias insists the casting choice is still open. "
  "The adjective 'fini' indicates completion."),
 (2, None,
  "'Listen, the situation is becoming too complicated.' Gabriel stresses the mounting confusion. "
  "The verb 'devenir' means to become."),
 (3, None,
  "'I keep you posted tomorrow.' Mathias promises to share updates later. "
  "The idiom 'tenir au courant' means to keep someone informed."),
 (4, None,
  "'Are you going to give in to blackmail now?' Gabriel questions Mathias's ethics. "
  "The verb 'ceder' expresses yielding or surrendering."),
 (5, None,
  "'I am a cinema producer now.' Mathias underlines his independence from ASK. "
  "The noun 'producteur' denotes a film producer."),
 (6, None,
  "'You must protect our favorite actors.' Gabriel appeals to their shared history. "
  "The adjective 'prefere' expresses preference."),
 (7, None,
  "'I choose the best actor possible.' Mathias prioritizes artistic criteria. "
  "The superlative 'le meilleur' means the best."),
 (8, None,
  "'If Dany leaves ASK, we sink!' Gabriel warns of financial ruin. "
  "The verb 'couler' figuratively means to sink or go bankrupt."),
 (9, None,
  "'The agency will start sinking fast.' Mathias acknowledges the impending danger. "
  "The verb phrase 'commencer a' marks the start of an event."),
 (10, None,
  "'I call Franck to arrange everything.' Gabriel intervenes directly with the talent. "
  "The verb 'arranger' means to resolve or sort out."),
 (11, None,
  "'He filters all my recent calls.' Mathias warns that Franck is avoiding him. "
  "The verb 'filtrer' means to screen or filter."),
 (12, None,
  "'Hello Franck? Yes, it is Gabriel here.' Gabriel manages to reach Franck on the phone. "
  "The phrase 'c'est Gabriel ici' is common in phone introductions."),
 (13, None,
  "'Good luck convincing our friend!' Mathias offers parting encouragement. "
  "The prepositional phrase 'bonne chance pour' wishes success."),
]

OUTRO = ("Gabriel takes initiative to prevent top client Dany Boon from departing ASK. "
         "Reaching out to Franck Dubosc directly, Gabriel tries to salvage the agency from collapse. "
         "Now, let's review the scene one last time.")

CLOSING = ("mathias", "Bonne chance pour convaincre notre ami!")
