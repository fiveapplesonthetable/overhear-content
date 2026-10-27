# Authoring module for dix-pour-cent s04e03 scene 24 (cues 1028-1043).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-24.py --out out/dix-pour-cent/s04e03/scene-24.json

ID = "dix-pour-cent-s04e03-scene-24"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 24
TITLE = "Renvoyée de la crèche  (Expelled from the Creche)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1028-1043. After allowing actor Jose Garcia to supervise children at the daycare, Andrea is kicked out by the furious director "
    "and arrives at ASK with baby Flora in her arms."
)

INTRO = (
    "After allowing actor Jose Garcia to supervise children at the daycare, Andrea is kicked out by the furious director and arrives at ASK with baby Flora in her arms. Let's listen to the scene in French first."
)

STORY = [
    ("lea", "On peut trouver une bonne solution!",
     "We can find a good solution!",
     [(1028, "On peut trouver une solution")], "Andrea tries to negotiate with the director"),
    ("lea", "José Garcia n'est pas un inconnu.",
     "Jose Garcia is not a stranger.",
     [(1033, "José Garcia n'est pas vraiment un inconnu")], ""),
    ("lea", "Capucine s'occupe très bien des enfants.",
     "Capucine takes very good care of the children.",
     [(1034, "Capucine s'en est très bien sortie avec les enfants")], "Defends her assistant's babysitting"),
    ("lea", "La directrice refuse de m'écouter aujourd'hui.",
     "The director refuses to listen to me today.",
     [(1032, "Je ne le tolérerai pas")], ""),
    ("lea", "Elle nous a chassées de là!",
     "She kicked us out of there!",
     [(1032, "Je ne le tolérerai pas")], "Andrea vents her outrage"),
    ("gabriel", "Bonjour Andréa, que fais-tu avec Flora?",
     "Hello Andrea, what are you doing with Flora?",
     [(1041, "Bonjour, Andréa")], "Gabriel greets her in the hallway"),
    ("gabriel", "Tu inscris le bébé aux castings?",
     "Are you signing the baby up for auditions?",
     [(1042, "Tu inscris le gamin à des castings")], "Teases her playfully about the baby"),
    ("lea", "Non, la directrice est trop méchante.",
     "No, the director is too mean.",
     [(1038, "Madame Sale-garce")], ""),
    ("lea", "On nous a mises à la porte!",
     "They threw us out the door!",
     [(1043, "On nous a mis à la porte de la crèche")], "Explains the disaster at the crèche"),
    ("gabriel", "À la porte de la crèche?",
     "Out the door of the daycare?",
     [(1043, "On nous a mis à la porte de la crèche")], "Gabriel looks shocked"),
    ("lea", "Oui, je n'ai plus de garde.",
     "Yes, I no longer have childcare.",
     [(1043, "On nous a mis à la porte de la crèche")], ""),
    ("gabriel", "C'est une catastrophe pour ton travail.",
     "That is a disaster for your work.",
     [(1043, "On nous a mis à la porte de la crèche")], "Recognizes the administrative trouble"),
    ("lea", "Je dois garder Flora à l'agence.",
     "I must keep Flora at the agency.",
     [(1043, "On nous a mis à la porte de la crèche")], "Andrea sighs under the strain"),
    ("gabriel", "Nous allons t'aider avec le bébé.",
     "We are going to help you with the baby.",
     [(1043, "On nous a mis à la porte de la crèche")], "Gabriel offers full team support"),
]

OPENER = "Let's examine how Andrea deals with her daycare dilemma step by step."

WALK = [
    (0, None,
     "'We can find a good solution!' Andrea tries in vain to negotiate with the daycare staff."),
    (1, None,
     "'Jose Garcia is not a stranger.' Andrea defends having the famous actor supervise the children."),
    (2, None,
     "'Capucine takes very good care of the children.' Andrea praises the young assistant's help."),
    (3, None,
     "'The director refuses to listen to me today.' Andrea laments the administrator's rigid stance."),
    (4, None,
     "'She kicked us out of there!' Andrea describes being expelled from the establishment."),
    (5, None,
     "'Hello Andrea, what are you doing with Flora?' Gabriel greets Andrea at the agency."),
    (6, None,
     "'Are you signing the baby up for auditions?' Gabriel teases her playfully about the baby."),
    (7, None,
     "'No, the director is too mean.' Andrea vents her frustration with the strict nursery head."),
    (8, None,
     "'They threw us out the door!' Andrea reveals the shocking news of their expulsion."),
    (9, None,
     "'Out the door of the daycare?' Gabriel expresses disbelief at the sudden ban."),
    (10, None,
     "'Yes, I no longer have childcare.' Andrea admits she has no alternative care arranged."),
    (11, None,
     "'That is a disaster for your work.' Gabriel recognizes the administrative nightmare."),
    (12, None,
     "'I must keep Flora at the agency.' Andrea resolves to balance work and infant care."),
    (13, None,
     "'We are going to help you with the baby.' Gabriel promises support from colleagues."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Cast out of the local daycare following the babysitting incident with Jose Garcia, Andrea brings baby Flora to ASK and explains her parenting predicament to Gabriel."
CLOSING = ("lea", "On nous a mises à la porte!")
