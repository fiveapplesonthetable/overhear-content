# Authoring module for dix-pour-cent s02e03 scene 16 (cues 405-422).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e03/authoring/scene-16.py --out overhear-content/out/dix-pour-cent/s02e03/scene-16.json

ID = "dix-pour-cent-s02e03-scene-16"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 16
TITLE = "Retrouvailles au Grand Colbert  (Reunion at Grand Colbert)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "annick": "emilie", "mathias": "theo"}
LABELS = {"lea": "Camille", "annick": "Annick", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 405-422. Mathias joins Annick and Camille at Le Grand Colbert restaurant. "
    "The former lovers share an awkward reunion over drinks."
)

INTRO = (
    "At Le Grand Colbert restaurant, Mathias finally arrives to meet Annick and their daughter Camille. "
    "Years of estrangement create palpable tension as the former couple exchange polite pleasantries and order drinks. "
    "Listen to the conversation in French first."
)

STORY = [
    ("annick", "J'ai besoin d'un verre. Garçon!",
     "I need a drink. Waiter!",
     [(405, "J'ai besoin d'un verre. Garçon")], ""),
    ("lea", "Regarde maman, il est là.",
     "Look Mom, he is here.",
     [(407, "Il est là")], ""),
    ("annick", "Il n'a pas changé.",
     "He has not changed.",
     [(408, "Il n'a pas changé")], ""),
    ("lea", "Toi non plus.",
     "Neither have you.",
     [(408, "Toi non plus")], ""),
    ("mathias", "Bonjour Annick. Bonjour Camille.",
     "Hello Annick. Hello Camille.",
     [(410, "Bonjour")], ""),
    ("annick", "Bonjour Mathias.",
     "Hello Mathias.",
     [(410, "Bonjour")], ""),
    ("lea", "Vous n'allez pas vous serrer la main?",
     "Are you not going to shake hands?",
     [(411, "Vous n'allez pas vous serrer la main")], ""),
    ("mathias", "Non, bien sûr que non.",
     "No, of course not.",
     [(412, "Non")], ""),
    ("annick", "Asseyez-vous, Mathias.",
     "Sit down, Mathias.",
     [(414, "Asseyez-vous")], ""),
    ("annick", "Un homme important doit être pressé.",
     "An important man must be in a hurry.",
     [(414, "Un homme important comme vous doit être pressé")], ""),
    ("mathias", "Oh, vous savez...",
     "Oh, you know...",
     [(415, "Oh, vous savez")], ""),
    ("mathias", "Juste un café, s'il vous plaît.",
     "Just a coffee, please.",
     [(416, "Juste un café, s'il vous plaît")], ""),
    ("annick", "Et un verre de rouge pour moi.",
     "And a glass of red wine for me.",
     [(417, "Et un verre de rouge pour moi")], ""),
    ("mathias", "Je m'en occupe.",
     "I will take care of it.",
     [(418, "Je m'en occupe")], ""),
    ("annick", "Vous vous occupez de tout, toujours.",
     "You take care of everything, always.",
     [(419, "Vous vous occupez de tout")], ""),
    ("mathias", "Mieux vaut tard que jamais.",
     "Better late than never.",
     [(422, "Mieux vaut tard que jamais")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'I need a drink. Waiter!' Annick signals the server to cope with her nerves. "
     "The traditional noun addresses brasserie waiters."),
    (1, None,
     "'Look Mom, he is here.' Camille spots her father entering the brasserie. "
     "The adverbial particle pinpoints physical presence in the room."),
    (2, None,
     "'He has not changed.' Annick observes Mathias with quiet surprise after eight years. "
     "The negative compound past tense notes his familiar appearance."),
    (3, None,
     "'Neither have you.' Camille offers an encouraging compliment to her mother. "
     "The adverbial phrase non plus expresses agreement in the negative."),
    (4, None,
     "'Hello Annick. Hello Camille.' Mathias greets them with formal reserve. "
     "The standard greeting introduces the awkward family reunion."),
    (5, None,
     "'Hello Mathias.' Annick responds cautiously, maintaining polite distance. "
     "The mutual formal tone highlights years of silence."),
    (6, None,
     "'Are you not going to shake hands?' Camille points out their stiff physical hesitation. "
     "The reciprocal construction se serrer la main questions their formality."),
    (7, None,
     "'No, of course not.' Mathias declines the cold corporate gesture between past lovers. "
     "The fixed emphatic expression reinforces obvious negation."),
    (8, None,
     "'Sit down, Mathias.' Annick invites him to join them at the table. "
     "The reflexive imperative asseyez-vous conveys formal courtesy."),
    (9, None,
     "'An important man must be in a hurry.' She uses gentle irony about his busy life. "
     "The adjective describes someone short on time."),
    (10, None,
     "'Oh, you know...' Mathias deflects the remark with understated modesty. "
     "The conversational filler avoids boastful agreement."),
    (11, None,
     "'Just a coffee, please.' Mathias orders a quick hot beverage from the waiter. "
     "The polite courtesy phrase completes the beverage request."),
    (12, None,
     "'And a glass of red wine for me.' Annick chooses wine to steady her emotions. "
     "The elliptical phrase un verre de rouge designates red wine colloquially."),
    (13, None,
     "'I will take care of it.' Mathias offers to cover the order. "
     "The pronominal verb s'occuper de expresses handling a responsibility."),
    (14, None,
     "'You take care of everything, always.' Annick evokes his habitual need for control. "
     "The pronoun tout functions as direct object of the action."),
    (15, None,
     "'Better late than never.' Mathias acknowledges their belated family reunion. "
     "The traditional French proverb reflects on timing and reconciliation.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Mathias and Annick attempt to bridge eight years of distance over coffee and wine, under the watchful gaze of their daughter Camille. "
    "Listen to the French conversation one more time."
)

CLOSING = ("annick", "C'est bon de vous voir.")
