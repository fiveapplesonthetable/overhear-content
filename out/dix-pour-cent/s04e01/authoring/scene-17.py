# Authoring module for dix-pour-cent s04e01 scene 17 (cues 882-896).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e01/authoring/scene-17.py --out overhear-content/out/dix-pour-cent/s04e01/scene-17.json

ID = "dix-pour-cent-s04e01-scene-17"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 17
TITLE = "Sur le tapis rouge  (On the Red Carpet)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mimie": "emilie", "elise": "theo"}
LABELS = {"lea": "Andréa", "mimie": "Mimie", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 882-896. On the César red carpet, Andréa encounters Mimie Mathy escorted by rival StarMédia "
    "agent Élise Formain, discovering that Mimie was poached with lavish promises of limousines and VIP access."
)

INTRO = (
    "At the prestigious Cesar Awards red carpet, Andrea arrives only to face an unpleasant surprise. "
    "Her former talent Mimie Mathy appears alongside Elise Formain, the aggressive boss of rival agency StarMedia. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Bonsoir, Mimie! Quelle surprise de te voir!",
     "Good evening, Mimie! What a surprise to see you!",
     [(883, "Quelle surprise")], ""),
    ("mimie", "Bonsoir, Andréa, je suis très heureuse.",
     "Good evening, Andrea, I am very happy.",
     [(883, "Oh, Andréa")], ""),
    ("elise", "Inutile de me présenter, chère Andréa.",
     "No need to introduce me, dear Andrea.",
     [(884, "Inutile de présenter Élise Formain")], ""),
    ("lea", "Élise Formain, de l'agence StarMédia!",
     "Elise Formain, from the StarMedia agency!",
     [(884, "Élise Formain, de StarMédia")], ""),
    ("lea", "Est-ce ta nouvelle agente, Mimie?",
     "Is she your new agent, Mimie?",
     [(886, "c'est ta nouvelle agente, alors")], ""),
    ("mimie", "Tout à fait, cela change d'ASK!",
     "Absolutely, this makes a change from ASK!",
     [(887, "Tout à fait ! Ça change d'ASK")], ""),
    ("mimie", "J'ai eu une magnifique limousine blanche.",
     "I had a magnificent white limousine.",
     [(888, "En vingt-quatre heures, une limousine")], ""),
    ("mimie", "Et une invitation d'honneur aux Césars!",
     "And an honorary invitation to the Cesars!",
     [(889, "une invitation aux Césars")], ""),
    ("mimie", "Élise croit vraiment en mon talent.",
     "Elise truly believes in my talent.",
     [(890, "qu'on croit en moi")], ""),
    ("lea", "Je suis heureuse pour ton succès.",
     "I am happy for your success.",
     [(885, "Comment allez-vous")], ""),
    ("elise", "StarMédia sait prendre soin des artistes.",
     "StarMedia knows how to take care of artists.",
     [(887, "Ça change d'ASK")], ""),
    ("mimie", "On m'appelle pour les photos officielles!",
     "They are calling me for the official photos!",
     [(891, "Mimie ! Par ici"), (892, "C'est mon tour")], ""),
    ("elise", "Allons sur le tapis rouge prestigieux.",
     "Let us go onto the prestigious red carpet.",
     [(888, "le tapis rouge"), (894, "le photocall")], ""),
    ("lea", "La guerre des agences a commencé.",
     "The agency war has begun.",
     [(897, "Je vous laisse")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Good evening, Mimie! What a surprise to see you!' Andrea greets her former client warmly at the gala. "
     "The exclamation expresses surprise."),
    (1, None,
     "'Good evening, Andrea, I am very happy.' Mimie radiates pride and excitement. "
     "The positive adjective conveys her joy."),
    (2, None,
     "'No need to introduce me, dear Andrea.' Elise steps forward with cold confidence. "
     "The courteous phrase hides sharp rivalry."),
    (3, None,
     "'Elise Formain, from the StarMedia agency!' Andrea immediately identifies the predator circling her agency. "
     "The exclamation acknowledges her foe."),
    (4, None,
     "'Is she your new agent, Mimie?' Andrea asks the painful question directly. "
     "The interrogative sentence seeks confirmation of betrayal."),
    (5, None,
     "'Absolutely, this makes a change from ASK!' Mimie does not hesitate to contrast the treatment. "
     "The adverb emphasizes her satisfaction."),
    (6, None,
     "'I had a magnificent white limousine.' She lists the luxury perks provided by her new representation. "
     "The descriptive noun phrase impresses."),
    (7, None,
     "'And an honorary invitation to the Cesars!' Mimie highlights the VIP access she was promised. "
     "The prepositional phrase underlines the prestige."),
    (8, None,
     "'Elise truly believes in my talent.' The actress appreciates the personal attention. "
     "The present tense confirms her newfound confidence."),
    (9, None,
     "'I am happy for your success.' Andrea hides her sting behind professional courtesy. "
     "The polite reply maintains her dignity."),
    (10, None,
     "'StarMedia knows how to take care of artists.' Elise boasts about her superior management style. "
     "The confident assertion taunts her rival."),
    (11, None,
     "'They are calling me for the official photos!' Mimie is summoned to the flashbulbs. "
     "The present tense announces her time in the spotlight."),
    (12, None,
     "'Let us go onto the prestigious red carpet.' Elise leads her new star toward the photographers. "
     "The imperative verb claims victory."),
    (13, None,
     "'The agency war has begun.' Andrea realizes the fierce battle ahead for ASK's survival. "
     "The declarative sentence foretells conflict.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Confronted by the poaching triumph of StarMedia on the red carpet, Andrea prepares for an all-out agency war. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "StarMédia est une rivale redoutable.")
