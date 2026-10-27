# Authoring module for dix-pour-cent s03e04 scene 24 (cues 1289-1301).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-24.py --out out/dix-pour-cent/s03e04/scene-24.json

ID = "dix-pour-cent-s03e04-scene-24"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 24
TITLE = "La percée du Yi-king  (The I Ching's Breakthrough)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 1289-1301. In Mathias's office, Noemie reads an inspiring passage from the I Ching, "
               "urging Mathias to seize the moment and break through to take control of ASK.")

INTRO = ("Inside Mathias's office at ASK, Noemie consults the ancient Chinese text of the I Ching for guidance. "
         "She reads aloud hexagram forty-three, symbolizing the Breakthrough, urging Mathias to act decisively. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Mathias, c'est absolument génial.",
  "Mathias, this is absolutely brilliant.",
  [(1289, "Mathias, c'est génial.")], "Expressing excitement"),
 ("lea", "C'est le signe de la percée.",
  "It is the sign of the breakthrough.",
  [(1290, "C'est la percée.")], "Identifying hexagram"),
 ("mathias", "Une percée après tant de tensions?",
  "A breakthrough after so much tension?",
  [(1291, "Une percée."), (1292, "tension accumulée.")], "Reflecting on struggle"),
 ("lea", "Comme un fleuve brisant ses digues.",
  "Like a river breaking its dikes.",
  [(1293, "d'un fleuve")], "Poetic river image"),
 ("lea", "Comme un grand nuage qui crève.",
  "Like a great cloud bursting.",
  [(1294, "Comme un nuage qui crève.")], "Poetic storm image"),
 ("lea", "Les hommes vulgaires vont disparaître.",
  "Vulgar men are going to disappear.",
  [(1295, "les hommes vulgaires")], "Predicting victory"),
 ("mathias", "Que dit le texte sur l'action?",
  "What does the text say about action?",
  [(1296, "Une action résolue")], "Asking about action"),
 ("lea", "Une action résolue amène le changement.",
  "Resolute action brings about change.",
  [(1296, "Une action résolue")], "Citing core teaching"),
 ("mathias", "C'est vraiment très frappant, Noémie.",
  "It is truly very striking, Noemie.",
  [(1297, "c'est fou, Mathias.")], "Acknowledging relevance"),
 ("lea", "Ça veut dire que c'est maintenant.",
  "It means that now is the time.",
  [(1298, "Ça veut dire que c'est maintenant.")], "Urging immediate move"),
 ("mathias", "Nous devons passer à l'attaque.",
  "We must go on the offensive.",
  [(1299, "Allez-y, Mathias.")], "Resolving to attack"),
 ("lea", "Allez-y franchement, Mathias!",
  "Go for it boldly, Mathias!",
  [(1299, "Allez-y, Mathias.")], "Encouraging boldness"),
 ("lea", "Percez sans hésiter!",
  "Break through without hesitation!",
  [(1300, "Percez.")], "Calling to break through"),
 ("mathias", "Oui, nous allons percer ensemble.",
  "Yes, we are going to break through together.",
  [(1301, "Percez.")], "Uniting in ambition"),
]

WALK = [
 (0, None,
  "'Mathias, this is absolutely brilliant.' Noemie reads the ancient Chinese divination result with excitement. "
  "The adverb 'absolument' emphasizes her conviction."),
 (1, None,
  "'It is the sign of the breakthrough.' Noemie identifies hexagram 43 of the I Ching. "
  "The noun 'percee' signifies a major breakthrough."),
 (2, None,
  "'A breakthrough after so much tension?' Mathias listens attentively to the reading. "
  "The noun 'tension' denotes the protracted strain at ASK."),
 (3, None,
  "'Like a river breaking its dikes.' Noemie quotes the poetic imagery of natural release. "
  "The noun 'fleuve' refers to a large river flowing to the sea."),
 (4, None,
  "'Like a great cloud bursting.' Noemie describes the dramatic release of pent-up energy. "
  "The verb 'crever' here figuratively means to burst with rain."),
 (5, None,
  "'Vulgar men are going to disappear.' Noemie interprets the hexagram's forecast about overcoming adversaries like Hicham. "
  "The adjective 'vulgaires' denotes coarse or inferior persons."),
 (6, None,
  "'What does the text say about action?' Mathias asks for the tactical counsel of the reading. "
  "The interrogative pronoun 'que' opens the inverted question."),
 (7, None,
  "'Resolute action brings about change.' Noemie recites the core principle of the hexagram. "
  "The feminine adjective 'resolue' describes decisive and purposeful conduct."),
 (8, None,
  "'It is truly very striking, Noemie.' Mathias is struck by how accurately the ancient text fits their struggle. "
  "The adjective 'frappant' means vivid or remarkable."),
 (9, None,
  "'It means that now is the time.' Noemie urges that hesitation must end immediately. "
  "The verbal expression 'veut dire' means signifies or indicates."),
 (10, None,
  "'We must go on the offensive.' Mathias resolves to initiate their decisive takeover maneuver. "
  "The idiom 'passer a l'attaque' means to take the initiative."),
 (11, None,
  "'Go for it boldly, Mathias!' Noemie encourages him to trust his strength. "
  "The imperative 'allez-y' urges someone forward with vigor."),
 (12, None,
  "'Break through without hesitation!' Noemie repeats the inspirational command of the hexagram. "
  "The imperative 'percez' calls for breaking through obstacles."),
 (13, None,
  "'Yes, we are going to break through together.' Mathias confirms their shared commitment to victory. "
  "The near-future construction 'allons percer' signals imminent resolution."),
]

OUTRO = ("The ancient wisdom of the I Ching strengthens Mathias's resolve to move against Hicham without delay. "
         "With Noemie by his side, he is ready to take back control of the agency. "
         "Now, let's review the scene one last time.")

CLOSING = ("mathias", "Oui, nous allons percer ensemble.")
