# Authoring module for dix-pour-cent s03e03 scene 25 (cues 1369-1392).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e03/authoring/scene-25.py --out overhear-content/out/dix-pour-cent/s03e03/scene-25.json

ID = "dix-pour-cent-s03e03-scene-25"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 25
TITLE = "Une nouvelle vie à l'agence  (A New Life at the Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "andrea": "emilie"}
LABELS = {"lea": "Camille", "mathias": "Mathias", "andrea": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1369-1392. Mathias gently places the newborn baby on Andrea's chest. "
    "After Andrea is settled, Mathias stays behind in the dark office late at night, humbly cleaning the floor. Camille joins him to help."
)

INTRO = (
    "Immediately following the dramatic birth at ASK, Andrea rests with her newborn while Mathias quietly cleans the office floor in the dead of night. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("mathias", "Prenez-le doucement dans vos bras.", "Take him gently in your arms.",
     [(1369, "Agnez-le")], "Mathias gently wraps the newborn in a clean cloth"),
    ("mathias", "Il sort tout seul maintenant.", "He is coming out on his own now.",
     [(1370, "il va sortir tout seul")], ""),
    ("mathias", "Directement sur le ventre d'Andréa!", "Directly onto Andrea's stomach!",
     [(1372, "Directement sur le ventre de la mer")], "Mathias gently places the baby on Andrea"),
    ("andrea", "Merci infiniment pour votre aide précieuse.", "Thank you so much for your precious help.",
     [(1377, "Merci"), (1378, "merci de m'avoir accompagnée")], "Andrea weeps with relief and joy"),
    ("andrea", "Je suis complètement épuisée maintenant.", "I am completely exhausted now.",
     [(1379, "Je suis épuisée")], ""),
    ("andrea", "Je vais m'écrouler de fatigue.", "I am going to collapse from tiredness.",
     [(1380, "Je vais m'écrouler, je crois")], ""),
    ("mathias", "C'est Andréa qui est vraiment exceptionnelle.", "It is Andrea who is truly exceptional.",
     [(1384, "c'est Andrea qui est exceptionnelle")], "Mathias smiles warmly at Andrea"),
    ("mathias", "C'est elle qui a tout fait.", "She is the one who did everything.",
     [(1385, "C'est elle qui a tout fait")], ""),
    ("andrea", "Bonne nuit à tous, merci.", "Good night to everyone, thank you.",
     [(1386, "bonne nuit, Mathias")], "Andrea closes her eyes peacefully"),
    ("lea", "Mathias, qu'est-ce que tu fais?", "Mathias, what are you doing?",
     [(1387, "Qu'est-ce que tu fais")], "Camille returns to find Mathias kneeling with a mop"),
    ("mathias", "Tu vois bien, je nettoie.", "You can see, I am cleaning.",
     [(1388, "tu vois, je nettoie")], "Mathias wipes the floor in the dimly lit office"),
    ("lea", "Ce n'est pas à toi de faire ça.", "That is not for you to do.",
     [(1389, "ce n'est pas à toi de faire ça")], ""),
    ("mathias", "Si, Camille, c'est à moi.", "Yes, Camille, it is for me.",
     [(1390, "Si, c'est à moi")], "Mathias looks up with tenderness"),
    ("mathias", "C'est vraiment à moi.", "It is truly for me.",
     [(1391, "C'est à moi")], ""),
    ("lea", "Alors, laisse-moi t'aider maintenant.", "Then let me help you now.",
     [(1388, "je nettoie")], "Camille takes a cloth and kneels by her father"),
]

OPENER = "Let's walk through this touching resolution in the aftermath of the birth step by step."

WALK = [
    (0, None,
     "'Take him gently in your arms.' Mathias carefully receives the newborn baby."),
    (1, None,
     "'He is coming out on his own now.' Mathias announces that the delivery is completing smoothly."),
    (2, None,
     "'Directly onto Andrea's stomach!' Mathias places the baby right onto Andrea's chest."),
    (3, None,
     "'Thank you so much for your precious help.' Andrea expresses deep gratitude through tears."),
    (4, None,
     "'I am completely exhausted now.' Andrea lies back after the monumental physical ordeal."),
    (5, None,
     "'I am going to collapse from tiredness.' Andrea admits she has nothing left to give."),
    (6, None,
     "'It is Andrea who is truly exceptional.' Mathias generously directs all praise to the mother."),
    (7, None,
     "'She is the one who did everything.' Mathias honors Andrea's incredible fortitude."),
    (8, None,
     "'Good night to everyone, thank you.' Andrea whispers her farewell before falling asleep."),
    (9, None,
     "'Mathias, what are you doing?' Camille finds her father working quietly in the dark office."),
    (10, None,
     "'You can see, I am cleaning.' Mathias explains his solitary chore with quiet dignity."),
    (11, None,
     "'That is not for you to do.' Camille objects to the senior partner doing janitorial work."),
    (12, None,
     "'Yes, Camille, it is for me.' Mathias softly insists on taking responsibility for this place."),
    (13, None,
     "'It is truly for me.' Mathias acknowledges the deep personal bond to this miraculous moment."),
    (14, None,
     "'Then let me help you now.' Camille joins her father to share the tender task."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "After Andrea welcomes her newborn daughter, Mathias quietly cleans the office floor in the dead of night, joined by his daughter Camille in a poignant moment of unity."
CLOSING = ("mathias", "Si, Camille, c'est à moi.")
