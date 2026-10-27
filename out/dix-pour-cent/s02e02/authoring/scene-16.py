# Authoring module for dix-pour-cent s02e02 scene 16 (cues 540-574).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-16.py --out out/dix-pour-cent/s02e02/scene-16.json

ID = "dix-pour-cent-s02e02-scene-16"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 16
TITLE = "L'appel nocturne de Fabrice  (Fabrice's Late-Night Call)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "fabrice": "marcel", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "fabrice": "Fabrice", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 540-574. In the middle of the night, an agitated Fabrice Luchini calls Andréa Martel to ask for an urgent face-to-face meeting. "
    "He fumes about Bréhier losing him the James Bond role. As soon as she hangs up, Andréa calls Gabriel to announce that their elaborate ruse worked."
)

INTRO = (
    "In the middle of the night, Andrea's private evening is abruptly interrupted when her mobile phone rings. "
    "On the line is an agitated and sleepless Fabrice Luchini, desperate to talk after discovering that his agent lost him the James Bond role. "
    "After agreeing to meet him immediately, Andrea rings Gabriel in triumph to celebrate the success of their cunning trap. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

OPENER = "Let's walk through the conversation step by step."

STORY = [
    ("lea", "Allô? Fabrice?", "Hello? Fabrice?",
     [(549, "Allô"), (550, "Ça va, Fabrice")], ""),
    ("fabrice", "Andréa, je ne dors pas.", "Andrea, I cannot sleep.",
     [(551, "Non"), (566, "C'est un grand insomniaque")], ""),
    ("lea", "Qu'est-ce qui ne va pas?", "What is wrong?",
     [(550, "Ça va, Fabrice")], ""),
    ("fabrice", "J'ai rencontré Debbie MacWilliams ce soir.", "I met Debbie MacWilliams tonight.",
     [(567, "Il a vu Debbie")], ""),
    ("fabrice", "Bréhier a totalement raté le rôle.", "Bréhier completely ruined the role.",
     [(512, "lui a posé problème")], ""),
    ("lea", "Le rôle dans James Bond?", "The role in James Bond?",
     [(521, "dans Bond")], ""),
    ("fabrice", "Oui! Je dois te voir maintenant.", "Yes! I must see you now.",
     [(553, "Maintenant"), (554, "d'accord")], ""),
    ("lea", "D'accord, j'arrive tout de suite.", "All right, I am coming right away.",
     [(555, "J'arrive. À tout de suite")], ""),
    ("lea", "Gabriel, tu es réveillé?", "Gabriel, are you awake?",
     [(562, "T'es réveillée")], ""),
    ("gabriel", "Allô Andréa? Qu'est-ce qui se passe?", "Hello Andrea? What is going on?",
     [(565, "il veut quoi")], ""),
    ("lea", "Fabrice vient de m'appeler!", "Fabrice just called me!",
     [(562, "Devine qui vient d'appeler"), (563, "Luchini")], ""),
    ("gabriel", "C'est vrai? Le plan a marché!", "Is that true? The plan worked!",
     [(564, "Putain")], ""),
    ("gabriel", "Sois très douce avec lui.", "Be very gentle with him.",
     [(568, "sois pas agressif"), (569, "Tout en douceur")], ""),
    ("lea", "Ne t'inquiète pas, je gère.", "Do not worry, I am handling it.",
     [(571, "T'inquiète pas")], ""),
    ("gabriel", "Tu es la meilleure, bonne chance!", "You are the best, good luck!",
     [(572, "T'es le meilleur")], ""),
]

WALK = [
    (0, None, "'Hello? Fabrice?' Andrea answers her phone surprised by the late hour."),
    (1, None, "'Andrea, I cannot sleep.' Fabrice explains that his insomnia and racing thoughts kept him awake."),
    (2, None, "'What is wrong?' Andrea asks what is troubling him so deeply."),
    (3, None, "'I met Debbie MacWilliams tonight.' Fabrice reveals his evening encounter with the purported British casting director."),
    (4, None, "'Bréhier completely ruined the role.' Fabrice blames his long-time agent for squandering the opportunity."),
    (5, None, "'The role in James Bond?' Andrea pretends to hear the news for the first time."),
    (6, None, "'Yes! I must see you now.' Fabrice insists on meeting in person without waiting until morning."),
    (7, None, "'All right, I am coming right away.' Andrea quickly agrees to come over immediately."),
    (8, None, "'Gabriel, are you awake?' Andrea calls Gabriel to wake him and share the urgent news."),
    (9, None, "'Hello Andrea? What is going on?' Gabriel answers groggily, wondering why she is calling at night."),
    (10, None, "'Fabrice just called me!' Andrea triumphantly announces that Luchini took the bait."),
    (11, None, "'Is that true? The plan worked!' Gabriel is thrilled that their elaborate bluff paid off."),
    (12, None, "'Be very gentle with him.' Gabriel counsels her to approach the wounded star with care and tact."),
    (13, None, "'Do not worry, I am handling it.' Andrea reassures him that she has the situation completely under control."),
    (14, None, "'You are the best, good luck!' Gabriel cheers her on before she sets off into the night."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "With Fabrice completely hooked by their deception, Andrea rushes out to comfort the star and seal the deal. "
    "Listen to the scene once more to solidify your French conversational skills."
)

CLOSING = ("gabriel", "Tu es la meilleure, bonne chance!")
