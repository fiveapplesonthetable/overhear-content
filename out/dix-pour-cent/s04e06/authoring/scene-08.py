# Authoring module for dix-pour-cent s04e06 scene 08 (cues 357-391).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e06/authoring/scene-08.py --out out/dix-pour-cent/s04e06/scene-08.json

ID = "dix-pour-cent-s04e06-scene-08"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 8
TITLE = "Un deuil à l'agence  (A Mourning at the Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 357-391. At ASK, Andrea and Mathias argue bitterly over defecting clients and lost projects, "
    "until Arlette arrives in tears with her dying dog Jean."
)

INTRO = (
    "At the ASK offices, tensions explode between Andrea and Mathias over lost film projects and departing clients. "
    "But their bitter quarrel comes to a sudden halt when Arlette rushes in with devastating news. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's look at Andrea and Mathias arguing before tragedy strikes step by step."

STORY = [
    ("lea", "François Ozon est parti chez StarMédia.",
     "Francois Ozon left for StarMedia.",
     [(358, "Ozon")], "Andrea brings up the loss of a major filmmaker"),
    ("mathias", "Ce beau projet peut sauver l'agence.",
     "This fine project can save the agency.",
     [(372, "sauver ASK")], "Mathias defends his alternative production plan"),
    ("lea", "Tu as tout démoli ici avant.",
     "You demolished everything here before.",
     [(373, "démolir")], "Andrea blames him for destabilizing the agency"),
    ("mathias", "C'est vous qui m'avez viré!",
     "You are the ones who fired me!",
     [(374, "m'avez viré")], "Mathias reminds her of his forced departure"),
    ("lea", "Le départ des talents, c'est toi.",
     "The departure of talent is on you.",
     [(376, "responsabilité")], "Andrea holds him accountable for the client exodus"),
    ("mathias", "Je voulais devenir un producteur indépendant.",
     "I wanted to become an independent producer.",
     [(377, "producteur")], "Mathias explains his career transition"),
    ("lea", "Mais tu n'es plus producteur aujourd'hui!",
     "But you are no longer a producer today!",
     [(378, "Tu n'es plus producteur")], "Andrea mocks his failed producer ventures"),
    ("lea", "Tu es devenu un simple manipulateur.",
     "You have become a mere manipulator.",
     [(380, "manipulateur")], "Andrea calls out his deceptive maneuvers"),
    ("mathias", "Ça te soulage de crier ainsi?",
     "Does it comfort you to shout like this?",
     [(382, "soulage")], "Mathias deflects her fury with a sarcastic question"),
    ("mathias", "Tu as laissé entrer Élise Formain.",
     "You let Elise Formain enter.",
     [(383, "Élise entrer")], "Mathias points out Andrea's own error in hiring Elise"),
    ("lea", "Regarde, voilà Arlette qui arrive affolée.",
     "Look, here comes Arlette in a panic.",
     [(385, "Arlette")], "Andrea spots Arlette rushing in with her dog"),
    ("mathias", "Qu'est-ce qui se passe avec Jean?",
     "What is going on with Jean?",
     [(388, "se passe")], "Mathias asks what has happened to Arlette's dog"),
    ("mathias", "Le pauvre petit chien est glacé.",
     "The poor little dog is ice cold.",
     [(389, "glacé")], "Mathias touches the dog and realizes something is wrong"),
    ("mathias", "Je suis désolé, il est parti.",
     "I am sorry, he has passed away.",
     [(390, "Il est parti")], "Mathias breaks the sad news that the dog has died"),
]

WALK = [
    (0, None,
     "'Francois Ozon left for StarMedia.' Andrea laments that another prestigious director has defected."),
    (1, None,
     "'This fine project can save the agency.' Mathias argues that his proposed film package could rescue ASK."),
    (2, None,
     "'You demolished everything here before.' Andrea accuses Mathias of sabotaging the agency from within."),
    (3, None,
     "'You are the ones who fired me!' Mathias fires back that the partners ousted him first."),
    (4, None,
     "'The departure of talent is on you.' Andrea pins the blame for recent client losses squarely on Mathias."),
    (5, None,
     "'I wanted to become an independent producer.' Mathias explains that he left agent work to pursue film production."),
    (6, None,
     "'But you are no longer a producer today!' Andrea reminds him that his independent production company collapsed."),
    (7, None,
     "'You have become a mere manipulator.' Andrea attacks his credibility and motives."),
    (8, None,
     "'Does it comfort you to shout like this?' Mathias asks if venting her rage makes her feel any better."),
    (9, None,
     "'You let Elise Formain enter.' Mathias reminds her that she was the one who hired the corporate saboteur."),
    (10, None,
     "'Look, here comes Arlette in a panic.' Andrea notices Arlette entering the room in great distress."),
    (11, None,
     "'What is going on with Jean?' Mathias asks about the state of her beloved pet dog."),
    (12, None,
     "'The poor little dog is ice cold.' Mathias examines the motionless dog and senses the worst."),
    (13, None,
     "'I am sorry, he has passed away.' Mathias gently informs Arlette that her dog has died."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "An angry confrontation between Andrea and Mathias over ASK's downfall is silenced by tragedy when Arlette arrives with her beloved dog Jean, who has passed away."
CLOSING = ("mathias", "Je suis désolé, il est parti.")
