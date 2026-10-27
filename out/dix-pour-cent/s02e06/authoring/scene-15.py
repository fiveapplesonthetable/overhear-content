# Authoring module for dix-pour-cent s02e06 scene 15 (cues 374-406).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e06/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s02e06/scene-15.json

ID = "dix-pour-cent-s02e06-scene-15"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 15
TITLE = "Cet enfant est le mien  (That Child is Mine)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 374-406. At a hotel bar in Cannes, Hicham confronts Andrea about her pregnancy, "
    "claiming fatherhood while Andrea fiercely insists that her body and decision belong to her alone."
)

INTRO = (
    "At a Cannes hotel bar, agency boss Hicham confronts Andrea after discovering that she is pregnant following their intimate night together. "
    "Claiming biological fatherhood, Hicham insists on having a say in the pregnancy, while Andrea fiercely defends her exclusive bodily autonomy. "
    "Listen to the scene in French first."
)

STORY = [
    ("hicham", "Salut, Andréa! Tu viens d'arriver?",
     "Hi, Andrea! Did you just arrive?",
     [(375, "Salut"), (376, "Tu viens d'arriver")], ""),
    ("lea", "Oui, je viens d'arriver au bar.",
     "Yes, I just arrived at the bar.",
     [(377, "Oui, à l'instant même")], ""),
    ("hicham", "Rien ne vaut ces belles fraises.",
     "Nothing beats these lovely strawberries.",
     [(383, "Rien ne vaut les fraises")], ""),
    ("lea", "Je prendrai une coupe de champagne.",
     "I will have a glass of champagne.",
     [(387, "une coupe de champagne")], ""),
    ("hicham", "Tu allais me le dire quand?",
     "When were you going to tell me?",
     [(389, "Tu allais me le dire quand")], ""),
    ("hicham", "Je parle de ton bébé.",
     "I am talking about your baby.",
     [(390, "Pour le bébé")], ""),
    ("hicham", "Inutile de mentir, je sais tout!",
     "No use lying, I know everything!",
     [(392, "Inutile de mentir. Je sais")], ""),
    ("lea", "Ça ne te regarde pas du tout.",
     "That is none of your business at all.",
     [(394, "Ça ne te regarde pas")], ""),
    ("hicham", "Ça me regarde tout à fait!",
     "It concerns me completely!",
     [(396, "ça me regarde tout à fait")], ""),
    ("hicham", "Je suis le père de cet enfant.",
     "I am the father of that child.",
     [(399, "le père de cet enfant")], ""),
    ("lea", "Quel enfant? Il n'y a personne!",
     "What child? There is nobody!",
     [(400, "Quel enfant ? Il n'y a pas d'enfant")], ""),
    ("lea", "Il y a juste moi et mon corps.",
     "There is just me and my body.",
     [(401, "Il y a juste moi et mon corps")], ""),
    ("lea", "C'est moi qui décide, d'accord?",
     "I am the one who decides, okay?",
     [(402, "c'est moi qui décide")], ""),
    ("hicham", "Tu ne décides pas toute seule.",
     "You do not decide all alone.",
     [(403, "Tu ne décides rien tout seul")], ""),
    ("hicham", "Cet enfant est aussi le mien!",
     "That child is mine as well!",
     [(404, "Cet enfant est le mien")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Hi, Andrea! Did you just arrive?' Hicham approaches her at the Cannes hotel bar. "
     "The recent past construction inquires about her arrival."),
    (1, None,
     "'Yes, I just arrived at the bar.' Andrea responds casually while ordering a drink. "
     "The directional prepositional phrase locates their encounter."),
    (2, None,
     "'Nothing beats these lovely strawberries.' Hicham attempts friendly small talk with complimentary fruit. "
     "The indefinite negative pronoun emphasizes supreme quality."),
    (3, None,
     "'I will have a glass of champagne.' Andrea orders alcohol to signal independence and defiance. "
     "The simple future verb expresses a decisive request."),
    (4, None,
     "'When were you going to tell me?' Hicham abruptly drops the pleasantries to confront her. "
     "The interrogative adverb challenges her secrecy."),
    (5, None,
     "'I am talking about your baby.' He directly addresses her secret pregnancy. "
     "The prepositional verb introduces the sensitive topic."),
    (6, None,
     "'No use lying, I know everything!' Hicham asserts complete knowledge of her condition. "
     "The predicate adjective dismisses any denial."),
    (7, None,
     "'That is none of your business at all.' Andrea fiercely defends her personal privacy. "
     "The negative pronoun phrase rejects his inquiry."),
    (8, None,
     "'It concerns me completely!' Hicham insists on his personal stake in the matter. "
     "The adverbial phrase emphasizes total relevance."),
    (9, None,
     "'I am the father of that child.' He claims his biological paternity without hesitation. "
     "The definitive noun phrase asserts parental status."),
    (10, None,
     "'What child? There is nobody!' Andrea denies the existence of a child at this early stage. "
     "The exclamatory question pushes back against his presumption."),
    (11, None,
     "'There is just me and my body.' She firmly asserts bodily autonomy over her pregnancy. "
     "The restrictive adverb underscores exclusive self-ownership."),
    (12, None,
     "'I am the one who decides, okay?' Andrea makes it clear that the choice belongs solely to her. "
     "The cleft sentence emphasizes personal sovereignty."),
    (13, None,
     "'You do not decide all alone.' Hicham refuses to be excluded from parental decisions. "
     "The negative verb phrase challenges her unilateral stance."),
    (14, None,
     "'That child is mine as well!' He claims an equal right to the unborn child. "
     "The possessive pronoun asserts shared ownership.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Fiercely asserting her bodily autonomy, Andrea rejects Hicham's demands to participate in decisions about her pregnancy. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "C'est ma vie et mon choix.")
