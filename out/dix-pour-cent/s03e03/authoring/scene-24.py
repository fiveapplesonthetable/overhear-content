# Authoring module for dix-pour-cent s03e03 scene 24 (cues 1324-1368).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e03/authoring/scene-24.py --out overhear-content/out/dix-pour-cent/s03e03/scene-24.json

ID = "dix-pour-cent-s03e03-scene-24"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 24
TITLE = "L'accouchement à l'agence  (Delivery at the Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "arlette": "Arlette", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1324-1368. An emergency birth takes place inside Andrea's office. "
    "With a midwife guiding them over speakerphone, Arlette and Mathias step up to deliver the baby together."
)

INTRO = (
    "In Andrea's office, an emergency birth unfolds as Arlette calls a midwife on speakerphone and guides a stunned Mathias through delivering the baby. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("arlette", "Qu'est-ce qu'elle dit, la sage-femme?", "What is the midwife saying?",
     [(1324, "Elle dit quoi, la sage-femme")], "Arlette holds the phone on speaker in the middle of the room"),
    ("arlette", "On est dans des bureaux ici!", "We are in office spaces here!",
     [(1325, "on est dans des bureaux")], ""),
    ("arlette", "Oui, c'est la maman qui crie.", "Yes, it is the mother screaming.",
     [(1328, "c'est la mère qui crie")], "Andrea groans in pain from the sofa"),
    ("arlette", "Elle est en train d'accoucher!", "She is giving birth right now!",
     [(1329, "elle va accoucher")], ""),
    ("arlette", "Le SAMU ne va pas tarder.", "The ambulance will not be long.",
     [(1331, "Le SAMU va pas tarder")], ""),
    ("arlette", "Le bébé arrive, elle va pousser.", "The baby is coming, she will push.",
     [(1333, "Elle est en train de pousser"), (1334, "Le bébé va sortir")], ""),
    ("arlette", "Mathias, entrez vite dans la pièce!", "Mathias, come into the room quickly!",
     [(1335, "Il faut quelqu'un")], "Mathias hurries in, looking flustered"),
    ("arlette", "Donnez vos lacets pour le cordon!", "Give your shoelaces for the cord!",
     [(1350, "j'ai besoin de vos lacets pour clamper le cordon")], ""),
    ("mathias", "Pardon? Mais comment on fait?", "Excuse me? But how do we do it?",
     [(1351, "Pardon")], "Mathias bends down in shock"),
    ("arlette", "Ne discutez pas, faites vite!", "Do not argue, be quick!",
     [(1352, "On discute pas"), (1353, "Fais ce que je dis")], ""),
    ("mathias", "D'accord, je vous écoute attentivement.", "Agreed, I am listening to you closely.",
     [(1344, "Je vous écoute")], "Mathias kneels before Andrea"),
    ("mathias", "Ça y est, je vois la tête!", "Here it is, I see the head!",
     [(1364, "C'est la tête")], "Mathias prepares his hands"),
    ("mathias", "Le bébé va sortir les épaules.", "The baby is going to bring out the shoulders.",
     [(1365, "le bébé va sortir les épaules")], ""),
    ("lea", "Ah! Aidez-moi, je pousse!", "Ah! Help me, I am pushing!",
     [(1333, "de pousser")], "Andrea grips Arlette's hand tightly"),
    ("arlette", "Mathias, vous êtes comme un chef!", "Mathias, you are doing like a champion!",
     [(1367, "Vous vous débrouillez comme un chef")], "Arlette smiles encouragingly"),
]

OPENER = "Let's walk through this intense emergency delivery in the ASK office step by step."

WALK = [
    (0, None,
     "'What is the midwife saying?' Arlette listens intently to the emergency instructions."),
    (1, None,
     "'We are in office spaces here!' Arlette clarifies that they have no hospital facilities."),
    (2, None,
     "'Yes, it is the mother screaming.' Arlette confirms the intense labor cries to the operator."),
    (3, None,
     "'She is giving birth right now!' Arlette realizes there is no time to wait for the ambulance."),
    (4, None,
     "'The ambulance will not be long.' Arlette tries to reassure everyone despite the rush."),
    (5, None,
     "'The baby is coming, she will push.' Arlette relays the urgent physical progression."),
    (6, None,
     "'Mathias, come into the room quickly!' Arlette summons Mathias to assist with the birth."),
    (7, None,
     "'Give your shoelaces for the cord!' Arlette demands an improvised clamp for the umbilical cord."),
    (8, None,
     "'Excuse me? But how do we do it?' Mathias is bewildered by the sudden medical role."),
    (9, None,
     "'Do not argue, be quick!' Arlette brooks no hesitation in the emergency."),
    (10, None,
     "'Agreed, I am listening to you closely.' Mathias focuses and prepares to catch the newborn."),
    (11, None,
     "'Here it is, I see the head!' Mathias announces the miraculous sight of the baby crowning."),
    (12, None,
     "'The baby is going to bring out the shoulders.' Mathias follows the midwife's step-by-step guidance."),
    (13, None,
     "'Ah! Help me, I am pushing!' Andrea cries out as she exerts all her remaining strength."),
    (14, None,
     "'Mathias, you are doing like a champion!' Arlette commends Mathias for his heroic delivery."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Coached over speakerphone by a midwife, Mathias and Arlette successfully deliver Andrea's baby right inside the ASK agency office."
CLOSING = ("arlette", "Mathias, vous êtes comme un chef!")
