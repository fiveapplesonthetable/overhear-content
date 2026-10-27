# Authoring module for dix-pour-cent s02e03 scene 14 (cues 353-383).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e03/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s02e03/scene-14.json

ID = "dix-pour-cent-s02e03-scene-14"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 14
TITLE = "La fête d'anniversaire  (Laser Game Party)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "mathias": "marcel"}
LABELS = {"lea": "Camille", "hicham": "Hicham", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 353-383. Hicham tasks Camille with organizing a birthday laser tag party for his son Elvis. "
    "Mathias warns Camille not to demean herself by acting as a babysitter."
)

INTRO = (
    "Hicham introduces his ten-year-old son Elvis at the agency and looks for entertainment during their week together in Paris. "
    "When the boy asks for a laser tag party, Hicham quickly delegates all the party logistics to Camille. "
    "Listen to the conversation in French first."
)

STORY = [
    ("hicham", "Bonjour tout le monde!",
     "Hello everyone!",
     [(354, "Bonjour tout le monde")], ""),
    ("lea", "Bonjour Hicham.",
     "Hello Hicham.",
     [(355, "Bonjour")], ""),
    ("hicham", "Voici mon fils, Elvis.",
     "This is my son, Elvis.",
     [(357, "Voici mon fils, Elvis")], ""),
    ("hicham", "Il a dix ans ce week-end.",
     "He is ten this weekend.",
     [(358, "Il a dix ans ce week-end")], ""),
    ("hicham", "On fait une fête à Paris.",
     "We are having a party in Paris.",
     [(358, "on fait une fête")], ""),
    ("hicham", "Elvis aime bien le laser game.",
     "Elvis likes laser tag.",
     [(370, "J'aime bien le laser game")], "adapted from Elvis's preference"),
    ("hicham", "Tu peux arranger ça, Camille?",
     "Can you arrange that, Camille?",
     [(373, "Tu peux arranger ça"), (377, "Camille")], ""),
    ("lea", "Okay, laisse-moi faire.",
     "Okay, leave it to me.",
     [(374, "Okay, laisse-moi faire")], ""),
    ("hicham", "Deux allers-retours pour ses amis.",
     "Two round-trip tickets for his friends.",
     [(378, "Deux allers-retours pour Ferdinand et Elliot")], "shortened friend list"),
    ("hicham", "Merci, Camille.",
     "Thanks, Camille.",
     [(379, "Merci, Camille")], ""),
    ("mathias", "T'es fou, Camille?",
     "Are you crazy, Camille?",
     [(380, "T'es fou")], "colloquial masculine agreement used in source cue"),
    ("lea", "Pourquoi tu dis ça?",
     "Why do you say that?",
     [(380, "Pourquoi")], ""),
    ("mathias", "Tu joues les baby-sitters pour lui.",
     "You are playing the babysitter for him.",
     [(381, "si tu joues les baby-sitters")], ""),
    ("mathias", "Il ne te respectera pas.",
     "He will not respect you.",
     [(381, "Il ne te respectera pas")], ""),
    ("lea", "Je veux être agent junior.",
     "I want to be a junior agent.",
     [(382, "Je veux être agent junior")], ""),
    ("lea", "Donc je fais attention, Mathias.",
     "So I am being careful, Mathias.",
     [(383, "donc je fais attention")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Hello everyone!' Hicham greets the open office with typical swagger. "
     "The fixed expression tout le monde means everyone."),
    (1, None,
     "'Hello Hicham.' Camille replies politely to her new boss. "
     "The standard polite greeting opens their exchange."),
    (2, None,
     "'This is my son, Elvis.' Hicham introduces his visiting young boy. "
     "The presentation word voici introduces people directly into view."),
    (3, None,
     "'He is ten this weekend.' The upcoming milestone prompts a celebration. "
     "French expresses age using the verb avoir with the number of years."),
    (4, None,
     "'We are having a party in Paris.' Hicham plans festivities during their week together. "
     "The colloquial pronoun on acts as the subject for making a party."),
    (5, None,
     "'Elvis likes laser tag.' Hicham shares his son's chosen entertainment activity. "
     "The adverbial combination aimer bien indicates moderate liking."),
    (6, None,
     "'Can you arrange that, Camille?' Hicham immediately delegates the party logistics. "
     "The modal verb pouvoir expresses request in question form."),
    (7, None,
     "'Okay, leave it to me.' Camille readily takes charge of the task. "
     "The imperative phrase laisse-moi faire offers full handling."),
    (8, None,
     "'Two round-trip tickets for his friends.' Hicham orders transportation arrangements. "
     "The compound noun aller-retour designates return train or plane tickets."),
    (9, None,
     "'Thanks, Camille.' Hicham expresses brisk satisfaction with her help. "
     "The polite expression merci closes his set of requests."),
    (10, None,
     "'Are you crazy, Camille?' Mathias pulls his secret daughter aside in disbelief. "
     "The informal contraction t'es replaces tu es in everyday speech."),
    (11, None,
     "'Why do you say that?' Camille questions his sharp objection. "
     "The interrogative adverb pourquoi seeks clarification of his concern."),
    (12, None,
     "'You are playing the babysitter for him.' Mathias warns her against subservient duties. "
     "The idiom jouer les designates acting out an unhelpful role."),
    (13, None,
     "'He will not respect you.' Mathias cautions that flunky tasks undermine authority. "
     "The future tense of respecter warns of negative consequences."),
    (14, None,
     "'I want to be a junior agent.' Camille reaffirms her clear professional ambition. "
     "The verb expresses determination followed by an infinitive."),
    (15, None,
     "'So I am being careful, Mathias.' Camille insists she knows how to manage the boundary. "
     "The idiom faire attention signifies being vigilant and prudent.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Mathias worries that Camille is lowering herself to an errand runner, but Camille remains determined to earn her promotion. "
    "Listen to the French scene once more."
)

CLOSING = ("lea", "C'est sous contrôle, Mathias.")
