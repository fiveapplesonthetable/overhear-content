# Authoring module for dix-pour-cent s02e03 scene 15 (cues 384-404).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e03/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s02e03/scene-15.json

ID = "dix-pour-cent-s02e03-scene-15"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 15
TITLE = "Rendez-vous au Grand Colbert  (Lunch Plans)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "annick": "emilie"}
LABELS = {"lea": "Camille", "annick": "Annick"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 384-404. Camille meets her mother Annick at Le Grand Colbert restaurant. "
    "Annick nervously touches up her hair while awaiting Mathias's arrival."
)

INTRO = (
    "At the agency, Noemie asked to join Camille for lunch, but Camille declined so she could spend time with her mother Annick. "
    "Now seated together at Le Grand Colbert restaurant, Annick frets over her appearance as they wait for Mathias. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "J'ai un déjeuner avec ma mère au Grand Colbert.",
     "I am having lunch with my mother at the Grand Colbert.",
     [(386, "avec ma mère. Au Grand Colbert")], ""),
    ("lea", "On a besoin d'un moment seules toutes les deux.",
     "We need time alone together.",
     [(389, "on a besoin d'un moment seules toutes les deux")], ""),
    ("lea", "Ça fait une éternité que je ne l'ai pas vue.",
     "It has been ages since I saw her.",
     [(390, "Ça fait une éternité que je ne l'ai pas vue")], ""),
    ("annick", "Il arrive à quelle heure?",
     "What time is he coming?",
     [(393, "Il arrive à quelle heure")], ""),
    ("annick", "Il a peut-être oublié.",
     "Maybe he forgot.",
     [(394, "Il a peut-être oublié")], ""),
    ("annick", "Ou il ne veut pas me voir.",
     "Or he does not want to see me.",
     [(394, "ou ne veut pas me voir")], ""),
    ("lea", "Il a dit qu'il viendrait pour le café.",
     "He said he would come for coffee.",
     [(395, "il a dit qu'il viendrait pour le café")], ""),
    ("lea", "D'accord, maman?",
     "Okay, Mom?",
     [(396, "D'accord")], ""),
    ("annick", "Je n'ai pas fait mes racines.",
     "I have not done my roots.",
     [(397, "Je n'ai pas fait mes racines")], ""),
    ("lea", "Tu n'as pas un seul cheveu blanc.",
     "You do not have a single white hair.",
     [(399, "Tu n'as pas un seul cheveu blanc")], ""),
    ("annick", "C'est pas un rendez-vous galant.",
     "This is not a romantic date.",
     [(400, "C'est pas un rendez-vous galant")], ""),
    ("annick", "Ça fait huit ans!",
     "It has been eight years!",
     [(402, "Ça fait huit ans")], ""),
    ("lea", "C'est un super produit.",
     "This is a great product.",
     [(403, "C'est un super produit")], ""),
    ("lea", "Voilà, tu es très bien.",
     "There, you look very nice.",
     [(404, "Voilà")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'I am having lunch with my mother at the Grand Colbert.' Camille shares her special lunch plans. "
     "The prepositional contraction au precedes the restaurant name."),
    (1, None,
     "'We need time alone together.' Mother and daughter cherish their rare reunion. "
     "The verbal idiom avoir besoin de indicates genuine emotional necessity."),
    (2, None,
     "'It has been ages since I saw her.' The idiom signifies a very long absence. "
     "The fixed temporal expression emphasizes years of separation."),
    (3, None,
     "'What time is he coming?' Annick checks the exact hour of Mathias's expected arrival. "
     "The interrogative phrase asks for specific clock time."),
    (4, None,
     "'Maybe he forgot.' Annick voices self-doubt about whether Mathias will show up. "
     "The modal adverb introduces hesitant uncertainty."),
    (5, None,
     "'Or he does not want to see me.' She worries about old wounds and unresolved tension. "
     "The conjunction ou coordinates alternative fears."),
    (6, None,
     "'He said he would come for coffee.' Camille reassures her mother about the agreed plan. "
     "The conditional viendrait expresses future action relative to the past statement."),
    (7, None,
     "'Okay, Mom?' Camille uses a gentle prompt to calm her mother's rising anxiety. "
     "The tag d'accord seeks mutual emotional reassurance."),
    (8, None,
     "'I have not done my roots.' Annick fusses over her hair color before seeing him. "
     "The plural noun racines refers to untreated hair roots."),
    (9, None,
     "'You do not have a single white hair.' Camille inspects her mother with reassuring eyes. "
     "The adjective seul reinforces total absence of gray."),
    (10, None,
     "'This is not a romantic date.' Annick pretends indifference despite her visible nervousness. "
     "The adjective galant modifies rendez-vous to describe a date."),
    (11, None,
     "'It has been eight years!' She emphasizes the long passage of time since they last met. "
     "The temporal construction specifies elapsed years."),
    (12, None,
     "'This is a great product.' Camille fixes her mother's hair with a cosmetic spray. "
     "The prefix super intensifies product quality in everyday speech."),
    (13, None,
     "'There, you look very nice.' Camille offers heartfelt encouragement before Mathias arrives. "
     "The enthusiastic interjection marks the successful completion of hair styling.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Annick tries to mask her deep emotions behind small worries about hair and makeup, while Camille patiently stands by her side. "
    "Listen to the conversation once more in French."
)

CLOSING = ("annick", "Espérons qu'il arrive vite.")
