# Authoring module for dix-pour-cent s02e03 scene 31 (cues 847-857).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-31.py --out out/dix-pour-cent/s02e03/scene-31.json

ID = "dix-pour-cent-s02e03-scene-31"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 31
TITLE = "Le lendemain matin chez ASK  (The Morning After at ASK)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "arlette": "Arlette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 847-857. Monday morning at ASK after a chaotic weekend. Andrea arrives energized, "
    "Arlette compliments her, and Gabriel shows up looking exhausted after his weekend in the drunk tank."
)

INTRO = (
    "It is Monday morning at the ASK agency after an eventful weekend. "
    "Andrea walks in feeling energized, while Gabriel arrives exhausted after two days in custody with Norman. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Bonjour, Arlette.", "Good morning, Arlette.",
     [(847, "Bonjour")], "Andrea arrives at the ASK office"),
    ("arlette", "Bonjour, Andréa. Tu as bien dormi?", "Good morning, Andrea. Did you sleep well?",
     [(847, "Bonjour")], ""),
    ("lea", "Arlette, cette herbe est terrible.", "Arlette, that weed is killer.",
     [(848, "Arlette, cette herbe est terrible")], ""),
    ("lea", "J'ai fait des rêves érotiques dingues tout le week-end.", "I had crazy erotic dreams all weekend.",
     [(849, "J'ai fait des rêves érotiques dingues tout le week-end")], ""),
    ("gabriel", "Pas moi.", "Not me.",
     [(850, "Pas moi")], "Gabriel walks in looking exhausted"),
    ("lea", "Pourquoi tu n'es pas venu à la fête?", "Why didn't you come to the party?",
     [(851, "Pourquoi tu n'es pas venu")], ""),
    ("gabriel", "J'avais des obligations personnelles.", "I had some personal obligations.",
     [(852, "J'avais des obligations personnelles")], ""),
    ("arlette", "Des obligations personnelles un dimanche soir?", "Personal obligations on a Sunday evening?",
     [(852, "obligations personnelles")], ""),
    ("gabriel", "Une affaire urgente avec un talent.", "An urgent matter with a talent.",
     [(852, "J'avais des obligations")], ""),
    ("arlette", "Salut tout le monde. Ça va, Marteau?", "Hello everyone. How are you, Marteau?",
     [(853, "Salut"), (854, "Salut tout le monde. Ça va, Marteau")], ""),
    ("lea", "Ça va très bien!", "I am doing very well!",
     [(854, "Ça va")], ""),
    ("arlette", "Et pour Aymeline Val aussi!", "And for Aymeline Val too!",
     [(855, "Aymeline Val aussi")], ""),
    ("arlette", "C'était pas dingue ce projet?", "Wasn't that project crazy?",
     [(855, "C'était pas dingue")], ""),
    ("lea", "C'était dingue!", "It was crazy!",
     [(856, "C'était dingue")], ""),
    ("gabriel", "Au moins, tout le monde est là ce matin.", "At least everyone is here this morning.",
     [(856, "C'était dingue")], ""),
]

OPENER = "Let's walk through the lively morning exchange at ASK step by step."

WALK = [
    (0, None,
     "'Good morning, Arlette.' Andrea greets her colleague as she enters the agency."),
    (1, None,
     "'Good morning, Andrea. Did you sleep well?' Arlette asks her with a friendly smile."),
    (2, None,
     "'Arlette, that weed is killer.' The word terrible here means potent or incredible."),
    (3, None,
     "'I had crazy erotic dreams all weekend.' The adjective dingue is an everyday word for crazy or wild."),
    (4, None,
     "'Not me.' Gabriel enters the office looking completely exhausted."),
    (5, None,
     "'Why didn't you come to the party?' Andrea asks in a negative past question."),
    (6, None,
     "'I had some personal obligations.' Gabriel uses the imperfect tense to offer a discreet excuse."),
    (7, None,
     "'Personal obligations on a Sunday evening?' Arlette raises an eyebrow playfully."),
    (8, None,
     "'An urgent matter with a talent.' Gabriel refers to his secret weekend ordeal with Norman."),
    (9, None,
     "'Hello everyone. How are you, Marteau?' Arlette affectionately uses Andrea's nickname."),
    (10, None,
     "'I am doing very well!' Andrea responds with confidence and energy."),
    (11, None,
     "'And for Aymeline Val too!' Arlette brings up the agency's new client."),
    (12, None,
     "'Wasn't that project crazy?' Arlette uses informal negative phrasing to seek agreement."),
    (13, None,
     "'It was crazy!' Andrea enthusiastically confirms the wild success of the weekend."),
    (14, None,
     "'At least everyone is here this morning.' Gabriel concludes with quiet relief after his night in jail."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "After an intense weekend for all the agents, the team reunites at ASK ready to tackle new challenges together."
CLOSING = ("lea", "C'était dingue!")
