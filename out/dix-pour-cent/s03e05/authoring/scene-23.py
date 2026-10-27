# Authoring module for dix-pour-cent s03e05 scene 23 (cues 989-1000).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-23.py --out out/dix-pour-cent/s03e05/scene-23.json

ID = "dix-pour-cent-s03e05-scene-23"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 23
TITLE = "La lettre d'Hicham  (Hicham's Letter)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 989-1000. Returning home after resolving the film crisis, Andréa finds Colette holding a letter from Hicham addressed to the family court judge. "
    "In the letter, Hicham officially waives his parental claim so that Colette can legitimately become Flora's recognized second parent."
)

INTRO = (
    "Returning home after resolving the film crisis, Andrea finds Colette holding a letter from Hicham addressed to the family court judge. "
    "In the letter, Hicham officially waives his parental claim so that Colette can legitimately become Flora's recognized second parent. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Tout s'est arrangé avec Béatrice Dalle!",
     "Everything worked out with Beatrice Dalle!",
     [(989, "bien passé avec Béatrice")], "Andrea announces the shoot's salvation"),
    ("colette", "C'est formidable, mais regarde cette lettre.",
     "That is wonderful, but look at this letter.",
     [(991, "lettre d'Hicham")], "Colette presents a surprising document"),
    ("lea", "Qu'est-ce qu'il se passe, Colette?",
     "What is going on, Colette?",
     [(990, "Qu'est-ce qu'il se passe")], "Andrea senses something serious"),
    ("colette", "C'est une lettre officielle d'Hicham.",
     "It is an official letter from Hicham.",
     [(991, "lettre d'Hicham")], "Colette reveals the author"),
    ("colette", "Elle est adressée au juge familial.",
     "It is addressed to the family judge.",
     [(991, "affaires familiales")], "Colette explains the legal recipient"),
    ("lea", "Que dit Hicham dans ce courrier?",
     "What does Hicham say in this letter?",
     [(992, "Hicham Janowski")], "Andrea asks for the contents"),
    ("colette", "Il rappelle qu'il est le père.",
     "He recalls that he is the father.",
     [(992, "père biologique")], "Colette quotes the biological fact"),
    ("colette", "Mais il admire notre beau couple.",
     "But he admires our beautiful couple.",
     [(995, "Andrea et Colette")], "Colette shares his praise"),
    ("colette", "Il veut protéger notre petite fille.",
     "He wants to protect our little daughter.",
     [(997, "Flora grandisse")], "Colette explains his protective motive"),
    ("lea", "Hicham a écrit tout cela?",
     "Hicham wrote all that?",
     [(994, "même si je suis")], "Andrea is stunned by his words"),
    ("colette", "Il renonce à reconnaître l'enfant.",
     "He renounces legal recognition of the child.",
     [(998, "renonce à reconnaître")], "Colette delivers the central legal concession"),
    ("colette", "Je deviens officiellement le deuxième parent!",
     "I officially become the second parent!",
     [(999, "deuxième parent")], "Colette celebrates her full parental status"),
    ("lea", "C'est un geste d'une générosité immense.",
     "It is a gesture of immense generosity.",
     [(1000, "respect entre les parents")], "Andrea is moved by his noble sacrifice"),
    ("colette", "Nous formons une vraie belle famille!",
     "We form a truly beautiful family!",
     [(997, "Flora grandisse")], "Colette rejoices in their united future")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Everything worked out with Beatrice Dalle!' Andrea shares the successful production rescue. "
     "The pronominal compound past verb announces positive resolution."),
    (1, None,
     "'That is wonderful, but look at this letter.' Colette redirects Andrea's focus. "
     "The imperative verb introduces a crucial piece of mail."),
    (2, None,
     "'What is going on, Colette?' Andrea senses an important family development. "
     "The interrogative phrase asks for immediate clarity."),
    (3, None,
     "'It is an official letter from Hicham.' Colette reveals who sent the document. "
     "The presentative construction identifies the surprising correspondence."),
    (4, None,
     "'It is addressed to the family judge.' Colette specifies the legal context. "
     "The passive participle construction indicates formal court communication."),
    (5, None,
     "'What does Hicham say in this letter?' Andrea eagerly inquires about the contents. "
     "The present verb asks for a summary of his written words."),
    (6, None,
     "'He recalls that he is the father.' Colette notes his initial statement of biological fact. "
     "The reporting verb introduces his personal opening acknowledgment."),
    (7, None,
     "'But he admires our beautiful couple.' Colette shares his respect for their partnership. "
     "The coordinating conjunction contrasts biology with their loving domestic unit."),
    (8, None,
     "'He wants to protect our little daughter.' Colette describes his deeper intent. "
     "The modal verb with an infinitive indicates selflessness for Flora's sake."),
    (9, None,
     "'Hicham wrote all that?' Andrea is amazed by his personal maturity. "
     "The compound past question expresses happy disbelief."),
    (10, None,
     "'He renounces legal recognition of the child.' Colette shares the life-changing waiver. "
     "The legal present verb confirms his voluntary surrender of formal paternity."),
    (11, None,
     "'I officially become the second parent!' Colette celebrates her secured legal standing. "
     "The present linking verb marks her recognized maternal status."),
    (12, None,
     "'It is a gesture of immense generosity.' Andrea is deeply touched by his gift. "
     "The evaluative noun phrase honors his gracious sacrifice."),
    (13, None,
     "'We form a truly beautiful family!' Colette looks forward to raising Flora together. "
     "The present verb celebrates full, recognized parental harmony.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "With a single generous legal letter, Hicham cements Andrea and Colette's family, bringing peace to their coparenting journey. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("colette", "Nous formons une vraie belle famille!")
