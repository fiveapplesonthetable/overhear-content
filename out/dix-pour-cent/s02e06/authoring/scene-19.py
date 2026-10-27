# Authoring module for dix-pour-cent s02e06 scene 19 (cues 512-532).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-19.py --out out/dix-pour-cent/s02e06/scene-19.json

ID = "dix-pour-cent-s02e06-scene-19"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 19
TITLE = "Balade sur la Croisette  (Strolling Around)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Arlette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 512-532. Arlette and Gabriel stroll down the Boulevard de la Croisette in Cannes. "
    "Arlette playfully explains the various festival sections to Gabriel, who gets a text message from Sofia "
    "announcing her arrival in Cannes."
)

INTRO = (
    "Strolling along the sunny Croisette during the Cannes Film Festival, Arlette guides Gabriel through the maze of festival sections. "
    "A surprise text message from Sofia brings a burst of romance to Gabriel's festival schedule. "
    "Listen to the scene in French first."
)

STORY = [
    ("gabriel", "Ce film turc est en compétition officielle?",
     "Is that Turkish film in the official competition?",
     [(512, "Ce film turc est en compétition officielle ?")], ""),
    ("lea", "Non, il passe à la Quinzaine des réalisateurs.",
     "No, it is screening at the Directors' Fortnight.",
     [(513, "Non, c'est à la Quinzaine des cinéastes.")], ""),
    ("gabriel", "C'est la sélection pour les premiers films?",
     "Is that the selection for first films?",
     [(514, "C'est pour les premiers films ?")], ""),
    ("lea", "Non, ça c'est la Semaine de la Critique.",
     "No, that is the Critics' Week.",
     [(514, "Non, ça c'est la Semaine de la Critique.")], ""),
    ("gabriel", "Je n'y comprends vraiment rien du tout.",
     "I really do not understand anything at all.",
     [(515, "Je n'y comprends rien.")], ""),
    ("lea", "Il y a aussi une section appelée ACID.",
     "There is also a section called ACID.",
     [(515, "Il y a aussi l'ACID."), (517, "Une compétition s'appelle l'ACID ?")], ""),
    ("gabriel", "C'est un nom assez surprenant pour un festival!",
     "That is quite a surprising name for a festival!",
     [(518, "Ridicule !")], ""),
    ("gabriel", "Attends, je viens de recevoir un message.",
     "Wait, I just received a message.",
     [(519, "Je viens à Cannes. On peut se voir ? Il faut qu'on parle.")], ""),
    ("lea", "Un problème urgent avec un de tes acteurs?",
     "An urgent problem with one of your actors?",
     [(520, "Un problème ? Une mauvaise nouvelle ?")], ""),
    ("gabriel", "Non, c'est Sofia qui vient d'arriver à Cannes.",
     "No, it is Sofia who has just arrived in Cannes.",
     [(519, "Je viens à Cannes."), (521, "Non, c'est juste un acteur qui reporte un rendez-vous.")], ""),
    ("lea", "C'est merveilleux! Tu devrais aller la retrouver.",
     "That is wonderful! You should go meet her.",
     [(522, "Allons-y.")], ""),
    ("gabriel", "J'ai un peu peur de mélanger travail et amour.",
     "I am a little afraid of mixing work and love.",
     [(532, "Pas trop stressée ?")], ""),
    ("lea", "Profite de la vie, Gabriel, nous sommes à Cannes!",
     "Enjoy life, Gabriel, we are in Cannes!",
     [(525, "C'est Cannes !")], ""),
    ("lea", "Regarde le soleil et la foule sur la Croisette.",
     "Look at the sun and the crowd on the Croisette.",
     [(524, "On va se balader, sentir l'ambiance sur la Croisette")], ""),
    ("gabriel", "Tu as raison, l'ambiance ici est magique.",
     "You are right, the atmosphere here is magical.",
     [(524, "sentir l'ambiance sur la Croisette")], ""),
    ("lea", "Alors va rejoindre Sofia et sois heureux!",
     "Then go join Sofia and be happy!",
     [(522, "Allons-y."), (525, "C'est Cannes !")], "")
]

OPENER = "Let's examine how Arlette and Gabriel enjoy the vibrant festival atmosphere."

WALK = [
    (0, None,
     "'Is that Turkish film in the official competition?' Gabriel checks the festival program. "
     "The feminine noun compétition refers to film competition."),
    (1, None,
     "'No, it is screening at the Directors' Fortnight.' Arlette knows the festival categories well. "
     "The noun phrase Quinzaine des réalisateurs designates a parallel section."),
    (2, None,
     "'Is that the selection for first films?' Gabriel asks for clarification. "
     "The feminine noun sélection designates the chosen films."),
    (3, None,
     "'No, that is the Critics' Week.' Arlette explains the distinctions patiently. "
     "The proper noun Semaine de la Critique designates another section."),
    (4, None,
     "'I really do not understand anything at all.' Gabriel admits his total confusion. "
     "The negative phrase rien du tout means nothing at all."),
    (5, None,
     "'There is also a section called ACID.' Arlette mentions the independent cinema showcase. "
     "The acronym ACID stands for an association of independent cinema."),
    (6, None,
     "'That is quite a surprising name for a festival!' Gabriel smiles at the acronym. "
     "The adjective surprenant means surprising or unexpected."),
    (7, None,
     "'Wait, I just received a message.' Gabriel checks his buzzing phone. "
     "The construction viens de recevoir expresses recent receipt."),
    (8, None,
     "'An urgent problem with one of your actors?' Arlette notices his sudden focus. "
     "The adjective urgent describes pressing matters."),
    (9, None,
     "'No, it is Sofia who has just arrived in Cannes.' Gabriel admits the source of the message. "
     "The construction vient d'arriver indicates immediate arrival."),
    (10, None,
     "'That is wonderful! You should go meet her.' Arlette encourages his romance. "
     "The adjective merveilleux expresses great delight."),
    (11, None,
     "'I am a little afraid of mixing work and love.' Gabriel expresses his customary anxiety. "
     "The infinitive mélanger means to mix or blend."),
    (12, None,
     "'Enjoy life, Gabriel, we are in Cannes!' Arlette urges him to embrace joy. "
     "The imperative profite de advises taking advantage of good times."),
    (13, None,
     "'Look at the sun and the crowd on the Croisette.' Arlette gestures toward the bustling boulevard. "
     "The feminine noun foule refers to a large crowd."),
    (14, None,
     "'You are right, the atmosphere here is magical.' Gabriel begins to relax and enjoy the moment. "
     "The adjective magique describes an enchanting setting."),
    (15, None,
     "'Then go join Sofia and be happy!' Arlette sends him off with heartfelt warmth. "
     "The imperative sois comes from the verb être.")
]

TRANSITION = "Now let's listen to the cheerful stroll once more at normal pace."

OUTRO = (
    "Under the Mediterranean sun, Arlette reminds Gabriel to savor love and cinema at the Cannes Film Festival. "
    "Listen to the charming conversation once more in French."
)

CLOSING = ("lea", "Alors va rejoindre Sofia et sois heureux!")
