# Authoring module for dix-pour-cent s02e01 scene 27 (cues 790-850).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-27.py --out out/dix-pour-cent/s02e01/scene-27.json

ID = "dix-pour-cent-s02e01-scene-27"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 27
TITLE = "Règlement de comptes en direct  (Live Settling of Scores)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "ramzy": "theo", "michel": "marcel"}
LABELS = {"lea": "Virginie", "ramzy": "Ramzy", "michel": "Michel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 790-850. On the red couch of Vivement Dimanche, Michel Drucker hosts Virginie Efira and Ramzy Bedia. "
    "Their real-life couple tensions and secret contract disputes spill over on live television before turning into "
    "a passionate on-air reconciliation."
)

INTRO = (
    "On the bright studio set of Vivement Dimanche, host Michel Drucker welcomes celebrity couple Ramzy Bedia and Virginie Efira to the famous red sofa. "
    "While promoting their new romantic comedy, the couple trade barbed remarks and settle their secret financial dispute live on air. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("michel", "Virginie Efira!", "Introducing Virginie Efira!",
     [(791, "Virginie Efira")], "Michel introduces Virginie on set"),
    ("lea", "Michel, bonjour. Bonjour, mon amour.", "Michel, hello. Hello, my love.",
     [(793, "Michel, bonjour. Bonjour, mon amour")], ""),
    ("ramzy", "C'est super que tu sois là.", "It's great that you're here.",
     [(795, "c'est super que tu sois là")], ""),
    ("lea", "Les surprises, c'est important.", "Surprises are important.",
     [(797, "les surprises, c'est important")], ""),
    ("ramzy", "Il y a pire que l'ennui dans une relation.", "There are worse things than boredom in a relationship.",
     [(800, "il y a pire que l'ennui dans une relation")], ""),
    ("lea", "Certaines surprises sont indésirables.", "Some surprises are unwelcome.",
     [(804, "Certaines surprises sont indésirables")], ""),
    ("ramzy", "Comme là, maintenant.", "Like right now.",
     [(808, "Comme là, maintenant")], ""),
    ("michel", "Regardons un extrait du film.", "Let's watch a clip of the film.",
     [(809, "Regardons un extrait du film")], ""),
    ("ramzy", "Qu'est-ce que tu fais là? C'est tellement gênant.", "What are you doing here? It's so awkward.",
     [(812, "Qu'est-ce que tu fais là"), (812, "C'est tellement gênant")], "whispering during the clip"),
    ("lea", "T'es tellement horrible.", "You are so horrible.",
     [(814, "T'es tellement horrible")], ""),
    ("ramzy", "Je suis horrible?", "I am horrible?",
     [(815, "Je suis horrible")], ""),
    ("lea", "Complètement!", "Totally!",
     [(815, "Complètement")], ""),
    ("michel", "On est en direct...", "We are live on air...",
     [(822, "On est en direct")], "warning them as cameras return"),
    ("ramzy", "Tu peux garder l'argent.", "You can keep the money.",
     [(824, "Tu peux garder l'argent")], ""),
    ("lea", "Parce que je t'aime.", "Because I love you.",
     [(831, "Parce que je t'aime")], ""),
    ("michel", "Quel couple volcanique!", "What a volcanic couple!",
     [(832, "Quel couple volcanique")], ""),
    ("lea", "Oui, ça en vaut la peine.", "Yes, it's worth it.",
     [(844, "Oui, ça en vaut la peine")], ""),
]

OPENER = "Let's walk through the live television exchange step by step."

WALK = [
    (0, None,
     "'Introducing Virginie Efira!' Michel Drucker introduces his special guest to the television audience."),
    (1, None,
     "'Michel, hello. Hello, my love.' Virginie greets both the host and her partner."),
    (2, None,
     "'It's great that you're here.' The subjunctive 'sois' follows the phrase 'c'est super que'."),
    (3, None,
     "'Surprises are important.' The plural noun 'surprises' takes the feminine plural form."),
    (4, None,
     "'There are worse things than boredom in a relationship.' The comparative 'pire que' means 'worse than'."),
    (5, None,
     "'Some surprises are unwelcome.' The feminine adjective 'indesirables' agrees with 'surprises'."),
    (6, None,
     "'Like right now.' The adverbial phrase 'comme la, maintenant' points to the present moment."),
    (7, None,
     "'Let's watch a clip of the film.' The imperative 'regardons' invites the audience to watch together."),
    (8, None,
     "'What are you doing here? It's so awkward.' Ramzy whispers furiously while the clip rolls."),
    (9, None,
     "'You are so horrible.' The informal contraction 't'es' stands for 'tu es'."),
    (10, None,
     "'I am horrible?' Ramzy questions Virginie's blunt accusation."),
    (11, None,
     "'Totally!' The adverb 'completement' adds emphatic confirmation."),
    (12, None,
     "'We are live on air...' Michel urgently warns the arguing couple as the cameras return."),
    (13, None,
     "'You can keep the money.' The modal verb 'peux' is followed by the infinitive 'garder'."),
    (14, None,
     "'Because I love you.' The conjunction 'parce que' introduces the real reason for her passion."),
    (15, None,
     "'What a volcanic couple!' The exclamative adjective 'quel' agrees with the masculine noun 'couple'."),
    (16, None,
     "'Yes, it's worth it.' The idiom 'en valoir la peine' means to be worth the trouble."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Virginie and Ramzy turned their real marital crisis into compelling television, leaving Michel Drucker delighted by their passion."
CLOSING = ("lea", "Oui, ça en vaut la peine.")
