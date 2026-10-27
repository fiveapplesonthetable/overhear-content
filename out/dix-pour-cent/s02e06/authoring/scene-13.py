# Authoring module for dix-pour-cent s02e06 scene 13 (cues 287-326).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e06/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s02e06/scene-13.json

ID = "dix-pour-cent-s02e06-scene-13"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 13
TITLE = "Déjeuner sur le bateau  (Lunch on the Boat)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "juliette": "emilie", "gillieres": "theo"}
LABELS = {"lea": "Andréa", "juliette": "Juliette", "gillieres": "Gillières"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 287-326. In Cannes, Andrea shields Juliette Binoche from media magnate Jean-Denis Gillières "
    "by scheduling a lunch on his yacht for Monday, knowing Juliette will have already departed."
)

INTRO = (
    "At the Cannes luxury hotel, powerful media mogul Jean-Denis Gillieres corners Andrea, insisting on meeting with Juliette Binoche. "
    "Learning that Juliette despises his advances, Andrea cleverly arranges a business lunch on his private yacht for a day when Juliette will have already left town. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Juliette, je suis avec Jean-Denis Gillières.",
     "Juliette, I am with Jean-Denis Gillieres.",
     [(288, "je suis avec Jean-Denis Gillières")], ""),
    ("lea", "Il veut te voir tout de suite.",
     "He wants to see you right away.",
     [(289, "Il veut te voir")], ""),
    ("juliette", "Non, je t'en supplie, pas lui!",
     "No, I beg you, not him!",
     [(290, "je t'en supplie, pas lui")], ""),
    ("juliette", "Je ne veux pas le voir.",
     "I do not want to see him.",
     [(293, "Je ne veux pas le voir")], ""),
    ("juliette", "Il est tellement pénible!",
     "He is so tiresome!",
     [(295, "Il est pénible")], ""),
    ("juliette", "Il ne comprend pas le mot non.",
     "He does not understand the word no.",
     [(300, "comprendre le mot « non »")], ""),
    ("lea", "D'accord, je m'en occupe.",
     "Understood, I am taking care of it.",
     [(301, "Je m'en occupe")], ""),
    ("lea", "Juliette est vraiment désolée, monsieur.",
     "Juliette is truly sorry, sir.",
     [(302, "elle est vraiment désolée")], ""),
    ("lea", "Elle répète son discours important.",
     "She is rehearsing her important speech.",
     [(304, "elle répète son discours")], ""),
    ("gillieres", "J'adore les femmes intelligentes!",
     "I adore intelligent women!",
     [(308, "J'adore les femmes intelligentes")], ""),
    ("lea", "Elle prépare son premier film.",
     "She is preparing her first film.",
     [(310, "son premier long métrage")], ""),
    ("gillieres", "Déjeunons sur mon bateau, lundi.",
     "Let us have lunch on my boat on Monday.",
     [(313, "déjeuner sur mon bateau, lundi")], ""),
    ("gillieres", "Ce sera calme et très agréable.",
     "It will be calm and very pleasant.",
     [(314, "Ce sera calme et agréable")], ""),
    ("gillieres", "Je peux aider pour le financement.",
     "I can help with the financing.",
     [(316, "aider pour le financement")], ""),
    ("lea", "Lundi, c'est parfait pour nous!",
     "Monday is perfect for us!",
     [(322, "Lundi, c'est parfait")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Juliette, I am with Jean-Denis Gillieres.' Andrea calls her client from the hotel lobby. "
     "The prepositional phrase identifies the powerful media mogul beside her."),
    (1, None,
     "'He wants to see you right away.' Andrea asks if the businessman can come up. "
     "The adverbial locution indicates urgency."),
    (2, None,
     "'No, I beg you, not him!' Juliette pleads with her agent to keep him away. "
     "The emphatic negative interjection conveys intense dread."),
    (3, None,
     "'I do not want to see him.' She firmly refuses any meeting with him. "
     "The negative verb construction expresses clear refusal."),
    (4, None,
     "'He is so tiresome!' Juliette explains how intrusive his unwanted attention has been. "
     "The intensifying adverb heightens her exasperation."),
    (5, None,
     "'He does not understand the word no.' Juliette points out his persistent boundary crossing. "
     "The direct object noun quotes her explicit refusal."),
    (6, None,
     "'Understood, I am taking care of it.' Andrea steps in to shield her celebrity client. "
     "The pronominal verb guarantees discreet management of the problem."),
    (7, None,
     "'Juliette is truly sorry, sir.' Andrea returns to Gillieres with a diplomatic excuse. "
     "The adverb modifies her apologetic statement."),
    (8, None,
     "'She is rehearsing her important speech.' Andrea invents an urgent professional excuse for Juliette's absence. "
     "The transitive verb explains her schedule conflict."),
    (9, None,
     "'I adore intelligent women!' Gillieres expresses admiring condescension toward the actress. "
     "The plural noun phrase reflects his vanity."),
    (10, None,
     "'She is preparing her first film.' Andrea mentions Juliette's directing aspirations to steer the conversation. "
     "The ordinal adjective specifies her directorial debut."),
    (11, None,
     "'Let us have lunch on my boat on Monday.' Gillieres proposes an exclusive meeting on his yacht. "
     "The imperative verb extends an invitation."),
    (12, None,
     "'It will be calm and very pleasant.' The wealthy mogul promises a secluded setting. "
     "The future copula introduces coordinating predicate adjectives."),
    (13, None,
     "'I can help with the financing.' Gillieres dangles financial backing for her movie project. "
     "The modal verb introduces investment assistance."),
    (14, None,
     "'Monday is perfect for us!' Andrea eagerly agrees, knowing Juliette leaves Cannes on Sunday. "
     "The evaluative adjective seals the clever scheduling maneuver.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "By agreeing to a yacht lunch after Juliette's departure, Andrea protects her star client while politely humoring the wealthy mogul. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "C'est noté dans l'agenda, monsieur.")
