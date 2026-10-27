# Authoring module for dix-pour-cent s03e03 scene 12 (cues 479-537).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e03/authoring/scene-12.py --out overhear-content/out/dix-pour-cent/s03e03/scene-12.json

ID = "dix-pour-cent-s03e03-scene-12"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 12
TITLE = "La future star du cinéma  (The Future Cinema Star)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "marcel"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 479-537. Back at the agency, Mathias furiously corners Camille about the audition scandal, "
    "only for Camille to reveal that Samy was a massive hit and got invited back for a callback."
)

INTRO = (
    "Back at the ASK offices, Mathias angrily confronts Camille for bypassing agency procedure and sending an unvetted client to auditions. "
    "Camille proudly fires back, announcing that Samy amazed the producers and landed a crucial callback. "
    "Listen to the scene in French first."
)

STORY = [
    ("mathias", "Qu'est-ce qui s'est passé aux essais?",
     "What happened at the screen tests?",
     [(530, "aux essais")], ""),
    ("mathias", "Pourquoi tu n'as pas répondu au téléphone?",
     "Why did you not answer the telephone?",
     [(531, "répondu au téléphone")], ""),
    ("lea", "J'ai eu un petit imprévu.",
     "I had a small unexpected issue.",
     [(532, "petit cafouillage")], ""),
    ("mathias", "Un petit imprévu? Tu te moques de moi?",
     "A small unexpected issue? Are you mocking me?",
     [(533, "Un petit cafouillage")], ""),
    ("mathias", "On a l'air de quoi maintenant?",
     "What do we look like right now?",
     [(534, "l'air de quoi")], ""),
    ("lea", "On a l'air d'une agence formidable!",
     "We look like a wonderful agency!",
     [(535, "on a l'air de ceux")], ""),
    ("lea", "On vient de recruter une future bombe!",
     "We just recruited a future sensation!",
     [(535, "la future petite bombe")], ""),
    ("lea", "La future grande star du cinéma français!",
     "The future great star of French cinema!",
     [(535, "du cinéma français")], ""),
    ("mathias", "Samy a vraiment réussi ses essais?",
     "Did Samy really succeed at his auditions?",
     [(536, "Samy a cartonné")], ""),
    ("lea", "Samy a totalement cartonné aujourd'hui!",
     "Samy totally rocked the audition today!",
     [(536, "Samy a cartonné")], ""),
    ("lea", "Les producteurs le veulent absolument pour demain.",
     "The producers absolutely want him for tomorrow.",
     [(536, "call-back demain")], ""),
    ("lea", "Ils veulent le voir en call-back.",
     "They want to see him for a callback.",
     [(536, "call-back demain")], ""),
    ("lea", "Et maintenant, c'est moi son agent!",
     "And now, I am his talent agent!",
     [(537, "c'est moi son agent")], ""),
    ("mathias", "Tu as pris un risque énorme, Camille.",
     "You took an enormous risk, Camille.",
     [(534, "l'air de quoi"), (537, "son agent")], ""),
    ("lea", "Mais ce risque a parfaitement payé!",
     "But that risk paid off perfectly!",
     [(536, "cartonné"), (537, "son agent")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'What happened at the screen tests?' Mathias interrogates Camille with sharp suspicion. "
     "The interrogative phrase investigates the unexpected turn of events."),
    (1, None,
     "'Why did you not answer the telephone?' He demands an explanation for her unreachable status. "
     "The negative past question criticizes lack of communication."),
    (2, None,
     "'I had a small unexpected issue.' Camille defends herself with a modest excuse. "
     "The noun phrase downplays the chaotic situation."),
    (3, None,
     "'A small unexpected issue? Are you mocking me?' Mathias expresses incredulity at her casual tone. "
     "The pronominal question challenges her seriousness."),
    (4, None,
     "'What do we look like right now?' He worries about the professional image of ASK. "
     "The idiomatic phrase evokes acute professional embarrassment."),
    (5, None,
     "'We look like a wonderful agency!' Camille turns the narrative around with upbeat energy. "
     "The positive predicate noun reframes the outcome."),
    (6, None,
     "'We just recruited a future sensation!' She reveals the exciting discovery. "
     "The near past construction announces a sensational signing."),
    (7, None,
     "'The future great star of French cinema!' Camille makes a bold artistic prediction. "
     "The expansive noun phrase asserts supreme confidence."),
    (8, None,
     "'Did Samy really succeed at his auditions?' Mathias begins to reconsider his anger. "
     "The past tense question seeks concrete confirmation."),
    (9, None,
     "'Samy totally rocked the audition today!' Camille describes his triumphant performance. "
     "The colloquial French verb denotes overwhelming success."),
    (10, None,
     "'The producers absolutely want him for tomorrow.' She reports urgent production enthusiasm. "
     "The adverbial intensifier confirms strong director interest."),
    (11, None,
     "'They want to see him for a callback.' Camille cites the formal invitation. "
     "The industry loanword denotes the secondary selection stage."),
    (12, None,
     "'And now, I am his talent agent!' She proudly establishes her own managerial status. "
     "The present copular statement marks a career milestone."),
    (13, None,
     "'You took an enormous risk, Camille.' Mathias acknowledges her bold gamble with caution. "
     "The past active verb highlights perilous agency initiative."),
    (14, None,
     "'But that risk paid off perfectly!' Camille celebrates a decisive professional victory. "
     "The celebratory statement closes the debate with triumph.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Turning a chaotic casting situation into a major victory, Camille proves her sharp eye for talent to a stunned Mathias. "
    "Listen to the conversation once more in French."
)

CLOSING = ("mathias", "On verra bien ce que donne le rappel.")
