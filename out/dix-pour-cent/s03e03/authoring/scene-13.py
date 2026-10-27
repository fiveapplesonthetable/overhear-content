# Authoring module for dix-pour-cent s03e03 scene 13 (cues 538-591).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e03/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s03e03/scene-13.json

ID = "dix-pour-cent-s03e03-scene-13"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 13
TITLE = "L'agent double  (The Double Agent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "annick": "emilie"}
LABELS = {"lea": "Camille", "herve": "Hervé", "annick": "Annick"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 538-591. In Camille's apartment, Camille and Hervé set up twin phones and a shared inbox "
    "to operate jointly as 'Camille Valentini', until Camille's mother Annick calls on speakerphone."
)

INTRO = (
    "At home, Camille and Herve prepare an ambitious undercover scheme to manage talent together. "
    "By sharing two phones and a joint calendar under the single name of Camille Valentini, they plan to conquer Paris. "
    "Listen to the scene in French first."
)

STORY = [
    ("herve", "Est-ce que tu es prêt?",
     "Are you ready?",
     [(541, "t'es prêt")], ""),
    ("lea", "Voici les téléphones de Camille Valentini.",
     "Here are the phones for Camille Valentini.",
     [(546, "téléphones de la")], ""),
    ("lea", "Un pour toi, un pour moi.",
     "One for you, one for me.",
     [(549, "Un pour toi, un pour moi")], ""),
    ("herve", "Mais c'est vraiment génial!",
     "But that is truly genius!",
     [(550, "c'est génial")], ""),
    ("lea", "J'ai créé une adresse commune.",
     "I created a shared address.",
     [(553, "j'ai créé une adresse")], ""),
    ("lea", "On va être partout à la fois.",
     "We are going to be everywhere at once.",
     [(562, "On va être partout à la fois")], ""),
    ("lea", "Attends, c'est ma mère.",
     "Wait, it is my mother.",
     [(567, "C'est ma mère")], ""),
    ("lea", "Surtout, tu ne lui dis rien.",
     "Above all, you do not tell her anything.",
     [(573, "tu lui dis rien")], ""),
    ("annick", "Camille, qu'est-ce qui se passe?",
     "Camille, what is going on?",
     [(575, "qu'est-ce qui se passe")], ""),
    ("herve", "On va être Camille tous les deux.",
     "We are going to be Camille together.",
     [(576, "tous les deux")], ""),
    ("annick", "Vous êtes complètement dérangées!",
     "You are completely out of your minds!",
     [(577, "vous êtes complètement dérangées")], ""),
    ("lea", "Tu dis toujours que je travaille trop.",
     "You always say that I work too much.",
     [(582, "que je travaille trop")], ""),
    ("annick", "Tu lui fais confiance, à lui?",
     "Do you trust him?",
     [(586, "Tu lui fais confiance, à lui")], ""),
    ("lea", "Maman, il t'entend là!",
     "Mom, he can hear you right now!",
     [(589, "Maman, il t'entend")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Are you ready?' Herve checks if his partner is prepared for the plan. "
     "The interrogative phrase asks about readiness."),
    (1, None,
     "'Here are the phones for Camille Valentini.' Camille presents the new mobile devices. "
     "The demonstrative adverb introduces the phones."),
    (2, None,
     "'One for you, one for me.' She divides the matching handsets fairly. "
     "The numbers establish an equal partnership."),
    (3, None,
     "'But that is truly genius!' Herve expresses his genuine admiration for the setup. "
     "The exclamative statement praises the scheme."),
    (4, None,
     "'I created a shared address.' Camille explains their new shared inbox. "
     "The compound past verb describes setting up the email."),
    (5, None,
     "'We are going to be everywhere at once.' She shares their ambitious vision for the agency. "
     "The near future verb promises complete coverage."),
    (6, None,
     "'Wait, it is my mother.' Camille notices an incoming phone call. "
     "The present demonstrative identifies the caller."),
    (7, None,
     "'Above all, you do not tell her anything.' She warns Herve to keep quiet about the identity trick. "
     "The negative imperative requests strict secrecy."),
    (8, None,
     "'Camille, what is going on?' Annick senses something unusual right away. "
     "The familiar interrogative asks for an explanation."),
    (9, None,
     "'We are going to be Camille together.' Herve proudly reveals their shared professional persona. "
     "The near future phrase explains the partnership."),
    (10, None,
     "'You are completely out of your minds!' Annick reacts with disbelief at the dangerous idea. "
     "The descriptive adjective marks total astonishment."),
    (11, None,
     "'You always say that I work too much.' Camille defends their secret workload sharing. "
     "The frequency adverb emphasizes her mother's past complaints."),
    (12, None,
     "'Do you trust him?' Annick questions whether Herve is genuinely dependable. "
     "The direct question expresses maternal suspicion."),
    (13, None,
     "'Mom, he can hear you right now!' Camille reminds her mother that speakerphone is on. "
     "The present verb signals Herve is listening.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "United under one identity, Camille and Herve take on double the workload with double the energy. "
    "Listen to the conversation once more in French."
)

CLOSING = ("herve", "Je serai toujours là pour vous.")
