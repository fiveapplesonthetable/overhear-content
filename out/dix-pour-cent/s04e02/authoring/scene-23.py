# Authoring module for dix-pour-cent s04e02 scene 23 (cues 1095-1102).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-23.py --out out/dix-pour-cent/s04e02/scene-23.json

ID = "dix-pour-cent-s04e02-scene-23"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 23
TITLE = "La fête à Saint-Ouen  (The Party in Saint-Ouen)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "sarah": "emilie"}
LABELS = {"lea": "Camille", "gabriel": "Gabriel", "sarah": "Sarah"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1095-1102. Sarah thanks Camille before leaving the ASK party. "
    "Gabriel catches up with Sarah and invites her to an exciting afterparty in Saint-Ouen, and they depart together."
)

INTRO = (
    "As the gathering at ASK begins to wind down, Sarah thanks Camille before Gabriel excitedly invites her to continue the evening at an afterparty in Saint-Ouen. Let's listen to the scene in French first."
)

STORY = [
    ("sarah", "Au revoir, Camille, merci pour tout.",
     "Goodbye, Camille, thank you for everything.",
     [(1095, "Au revoir, Camille")], "Sarah smiles and prepares to head out"),
    ("sarah", "La soirée était super sympa ici.",
     "The party was really nice here.",
     [(1095, "super sympa")], ""),
    ("lea", "Merci d'être venue ce soir, Sarah.",
     "Thank you for coming tonight, Sarah.",
     [(1095, "Au revoir, Camille")], "Camille sees her out warmly"),
    ("gabriel", "Te voilà enfin, tout va bien?",
     "There you are at last, is everything okay?",
     [(1096, "Te voilà, tout va bien")], "Gabriel hurries over to Sarah"),
    ("gabriel", "Il y a une fête à Saint-Ouen.",
     "There is a party in Saint-Ouen.",
     [(1097, "fête à Saint-Ouen")], "Suggests continuing the celebration elsewhere"),
    ("sarah", "Quelle est la grande urgence maintenant?",
     "What is the big rush now?",
     [(1098, "l'urgence")], ""),
    ("gabriel", "Cette fête va être incroyable.",
     "This party is going to be incredible.",
     [(1099, "va être de la bombe")], "Promises a memorable night"),
    ("gabriel", "Mes amis nous attendent là-bas.",
     "My friends are waiting for us there.",
     [(1099, "va être de la bombe")], ""),
    ("sarah", "As-tu prévu un bon transport?",
     "Did you arrange good transportation?",
     [(1100, "besoin d'un transport")], "Asks how they will travel"),
    ("gabriel", "Oui, un taxi attend dehors.",
     "Yes, a taxi is waiting outside.",
     [(1100, "besoin d'un transport")], "Assures her travel is covered"),
    ("sarah", "D'accord, partons tout de suite.",
     "All right, let's leave right away.",
     [(1101, "on y va")], "Accepts the invitation with enthusiasm"),
    ("gabriel", "Parfait, nous y allons ensemble.",
     "Perfect, we are going there together.",
     [(1101, "on y va")], ""),
    ("gabriel", "Allez, viens avec moi, Sarah!",
     "Come on, come with me, Sarah!",
     [(1102, "Allez, viens")], "Takes Sarah's arm as they leave"),
    ("lea", "Passez une très bonne nuit!",
     "Have a very good night!",
     [(1095, "Au revoir, Camille")], "Camille waves goodbye from the doorway"),
]

OPENER = "Let's examine Gabriel and Sarah's lively departure from the agency line by line."

WALK = [
    (0, None,
     "'Goodbye, Camille, thank you for everything.' Sarah thanks Camille warmly before leaving. A short, idiomatic conversational reply that keeps the exchange moving naturally."),
    (1, None,
     "'The party was really nice here.' Sarah compliments the pleasant evening at the agency. The descriptive adjective for 'great' agrees in gender and number with its noun."),
    (2, None,
     "'Thank you for coming tonight, Sarah.' Camille smiles and sees her guest out. The verb meaning 'having' pairs naturally with the noun for 'evening' in everyday conversation."),
    (3, None,
     "'There you are at last, is everything okay?' Gabriel catches up with Sarah by the door. Gabriel uses the casual singular 'you' with 'goes', showing close familiarity."),
    (4, None,
     "'There is a party in Saint-Ouen.' Gabriel suggests extending their night out in town. The key noun here means 'party', anchored by its matching French article."),
    (5, None,
     "'What is the big rush now?' Sarah playfully asks why they need to hurry. The adjective meaning 'big' takes its feminine form here to match the noun it describes."),
    (6, None,
     "'This party is going to be incredible.' Gabriel promises an unforgettable atmosphere. The descriptive adjective for 'incredible' agrees in gender and number with its noun."),
    (7, None,
     "'My friends are waiting for us there.' Gabriel explains that people are expecting them. The verb meaning 'are waiting for' pairs naturally with the noun for 'friends' in everyday conversation."),
    (8, None,
     "'Did you arrange good transportation?' Sarah asks how they will reach the venue. This conversational past tense combines a helper verb with the past participle for 'arranged'."),
    (9, None,
     "'Yes, a taxi is waiting outside.' Gabriel assures her that travel is taken care of. The verb meaning 'waits' pairs naturally with the noun for 'taxi' in everyday conversation."),
    (10, None,
     "'All right, let's leave right away.' Sarah agrees enthusiastically to the plan. Notice how the short vowel drops before a vowel sound around 'let's leave', making the phrase flow smoothly as one unit."),
    (11, None,
     "'Perfect, we are going there together.' Gabriel happily confirms their departure. The descriptive adjective for 'perfect' agrees in gender and number with its noun."),
    (12, None,
     "'Come on, come with me, Sarah!' Gabriel takes Sarah's hand as they head out. The clause hinges on the everyday verb meaning 'come on'."),
    (13, None,
     "'Have a very good night!' Camille waves as the pair leaves the building."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Eager to escape the agency atmosphere and keep the celebratory momentum going, Gabriel and Sarah say their goodbyes to Camille and leave together for Saint-Ouen. When you watch the episode, listen out for the expressions meaning 'party' and 'great'. You'll catch them now. See you next time."
CLOSING = ("gabriel", "Allez, viens avec moi, Sarah!")
