# Authoring module for dix-pour-cent s03e02 scene 25 (cues 1091-1149).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e02/authoring/scene-25.py --out overhear-content/out/dix-pour-cent/s03e02/scene-25.json

ID = "dix-pour-cent-s03e02-scene-25"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 25
TITLE = "Le remède du célibat  (The Remedy for Being Single)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Monika", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1091-1149. In her Parisian kitchen, Monica Bellucci discusses the difficulties of being single with Gabriel. "
    "Gabriel shares his secret to surviving solitude—friendship—before Monica offers him an herbal tea and gives a playful tutorial on her electric kettle."
)

INTRO = (
    "Sitting comfortably in her stylish Parisian kitchen, Monica Bellucci opens up about her personal struggles with dating and solitude. "
    "Together, she and Gabriel share an intimate laugh over tea. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Ça fait trois semaines pour moi.", "It has been three weeks for me.",
     [(1091, "Trois semaines")], "Monica sighs as she leans back against the counter"),
    ("gabriel", "Mais trois semaines, ce n'est rien!", "But three weeks is nothing!",
     [(1092, "trois semaines, c'est rien")], ""),
    ("lea", "Je suis super nulle en célibat.", "I am super terrible at being single.",
     [(1096, "Je suis super nulle")], ""),
    ("lea", "Je déteste vraiment ça.", "I really hate that.",
     [(1098, "Je déteste ça")], ""),
    ("lea", "Et toi, ça fait combien de temps?", "And you, how long has it been?",
     [(1103, "Et toi, ça fait longtemps")], "Monica looks at Gabriel curiously"),
    ("gabriel", "Ça fait déjà six mois.", "It has already been six months.",
     [(1104, "Six mois")], ""),
    ("gabriel", "Mais j'ai appris un grand truc.", "But I learned a great secret.",
     [(1108, "Mais j'ai appris un truc")], ""),
    ("lea", "Et c'est quoi, ton secret?", "And what is it, your secret?",
     [(1110, "Et c'est quoi")], ""),
    ("gabriel", "C'est l'amitié, tout simplement.", "It is friendship, quite simply.",
     [(1111, "L'amitié")], "Gabriel smiles warmly at his star client"),
    ("lea", "Tu veux bien une infusion?", "Would you like an herbal tea?",
     [(1113, "une infusion"), (1114, "je veux bien une infusion")], "Monica walks over to the modern kettle"),
    ("gabriel", "Oui, je veux bien une infusion.", "Yes, I would love an herbal tea.",
     [(1114, "je veux bien une infusion")], ""),
    ("lea", "J'ouvre le couvercle de la bouilloire.", "I open the lid of the kettle.",
     [(1119, "J'ouvre le couvercle")], "Monica demonstrates with theatrical flair"),
    ("lea", "Je mets de l'eau dedans.", "I put some water inside.",
     [(1120, "Je mets de l'eau")], ""),
    ("lea", "Et j'allume le bouton.", "And I turn on the switch.",
     [(1126, "Je mets en route")], ""),
    ("gabriel", "Capito, c'est très clair!", "Understood, that is very clear!",
     [(1131, "Capito")], "Gabriel laughs in appreciation"),
]

OPENER = "Let's walk through this warm and playful kitchen conversation step by step."

WALK = [
    (0, None,
     "'It has been three weeks for me.' Monica admits how recent her new period of solitude is. Notice how 'makes' leads directly into the noun meaning 'weeks'."),
    (1, None,
     "'But three weeks is nothing!' Gabriel tries to put her brief time alone into perspective. The key noun here means 'weeks', anchored by its matching French article."),
    (2, None,
     "'I am super terrible at being single.' Monica frankly confesses her complete inability to live solo. The key noun here means 'bachelorhood', anchored by its matching French article."),
    (3, None,
     "'I really hate that.' Monica expresses her intense aversion to coming home to an empty house. The clause hinges on the everyday verb meaning 'loathe'."),
    (4, None,
     "'And you, how long has it been?' Monica turns the question back to her trusted agent. The verb meaning 'makes' pairs naturally with the noun for 'duration' in everyday conversation."),
    (5, None,
     "'It has already been six months.' Gabriel reveals that he has been on his own for half a year. The verb meaning 'makes' pairs naturally with the noun for 'calendar months' in everyday conversation."),
    (6, None,
     "'But I learned a great secret.' Gabriel hints at a powerful truth he discovered through his trials. Notice how 'have' leads directly into the noun meaning 'trick'."),
    (7, None,
     "'And what is it, your secret?' Monica eagerly invites him to reveal his personal discovery. In everyday spoken French, rising intonation on 'recipe' at the end is enough to turn the sentence into a question."),
    (8, None,
     "'It is friendship, quite simply.' Gabriel shares his heartfelt recipe for enduring solitude. The key noun here means 'comradeship', anchored by its matching French article."),
    (9, None,
     "'Would you like an herbal tea?' Monica warmly offers hospitality to her loyal confidant. The verb meaning 'wish' pairs naturally with the noun for 'herbal tisane' in everyday conversation."),
    (10, None,
     "'Yes, I would love an herbal tea.' Gabriel gladly accepts a warm drink in her modern kitchen. Notice how 'would like' leads directly into the noun meaning 'herbal tisane'."),
    (11, None,
     "'I open the lid of the kettle.' Monica begins a playful step-by-step tutorial on making tea. The verb meaning 'uncover' pairs naturally with the noun for 'cap' in everyday conversation."),
    (12, None,
     "'I put some water inside.' Monica carefully pours fresh water into the electric appliance. Notice how 'pour' leads directly into the noun meaning 'liquid'."),
    (13, None,
     "'And I turn on the switch.' Monica clicks the machine into action with a satisfied smile. The verb meaning 'switch on' pairs naturally with the noun for 'switch' in everyday conversation."),
    (14, None,
     "'Understood, that is very clear!' Gabriel playfully praises her clear kitchen demonstration."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Bonding over the challenges of being single, Monica and Gabriel discover the healing power of genuine friendship while sharing tea in her kitchen. When you watch the episode, listen out for the expressions meaning 'makes' and 'weeks'. You'll catch them now. See you next time."
CLOSING = ("gabriel", "C'est l'amitié, tout simplement.")
