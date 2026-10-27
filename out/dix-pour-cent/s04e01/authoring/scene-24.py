# Authoring module for dix-pour-cent s04e01 scene 24 (cues 994-1004).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-24.py --out out/dix-pour-cent/s04e01/scene-24.json

ID = "dix-pour-cent-s04e01-scene-24"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 24
TITLE = "L'offensive d'Andréa  (Andréa's Offensive)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "herve": "marcel"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 994-1004. At the Cesar ceremony, Herve reveals breaking news that Mathias is becoming a producer at Mediawan. "
    "Andrea and Gabriel immediately resolve to fight to keep their talents, calling an emergency agency meeting."
)

INTRO = (
    "At the Cesar ceremony, Herve reveals breaking news that Mathias is becoming an independent producer at Mediawan. "
    "Andrea and Gabriel immediately resolve to fight to keep their talents. Let's listen to the scene in French first."
)

STORY = [
    ("herve", "Noémie ne vous a rien dit?",
     "Didn't Noemie tell you anything?",
     [(994, "Noémie ne vous a rien dit")], "Herve rushes over to Gabriel and Andrea"),
    ("herve", "Elle garde le secret professionnel.",
     "She keeps professional confidentiality.",
     [(995, "secret professionnel")], ""),
    ("herve", "Avez-vous vu tous les tweets?",
     "Did you see all the tweets?",
     [(996, "vu tous les tweets")], "Herve pulls out his mobile phone"),
    ("herve", "Mathias devient producteur chez Mediawan!",
     "Mathias is becoming a producer at Mediawan!",
     [(997, "devient producteur pour Mediawan")], "Announces the huge breaking news"),
    ("gabriel", "C'est une nouvelle tout à fait incroyable.",
     "That is completely incredible news.",
     [(998, "excellente nouvelle")], "Gabriel looks utterly stunned"),
    ("gabriel", "Je refuse de négocier avec lui.",
     "I refuse to negotiate with him.",
     [(999, "envie de négocier avec lui")], ""),
    ("lea", "Préfères-tu qu'il parte avec ses talents?",
     "Would you prefer he left with his talents?",
     [(1000, "qu'il parte avec tous ses clients")], "Andrea steps forward determinedly"),
    ("lea", "Notre mission est claire maintenant.",
     "Our mission is clear now.",
     [(1001, "Notre mission est maintenant claire")], ""),
    ("lea", "Nous devons convaincre tous les artistes.",
     "We must convince all the artists.",
     [(1001, "convaincre de rester avec nous")], ""),
    ("gabriel", "Regarde, les rivaux forment un groupe.",
     "Look, our rivals are forming a group.",
     [(1002, "Un conclave StarMédia")], "Gabriel points toward competing agents"),
    ("gabriel", "Devons-nous nous inquiéter ce soir?",
     "Should we be worried tonight?",
     [(1003, "On devrait s'inquiéter")], ""),
    ("lea", "Non, nous passons à l'offensive.",
     "No, we go on the offensive.",
     [(1003, "passer à l'offensive")], "Andrea rejects any sign of weakness"),
    ("lea", "Demain matin, réunion à huit heures.",
     "Tomorrow morning, meeting at eight o'clock.",
     [(1004, "réunion à l'agence")], "Sets a firm agency meeting time"),
    ("lea", "C'est une occasion parfaite pour nous.",
     "It is a perfect opportunity for us.",
     [(1004, "C'est bien")], "Andrea smiles with fierce confidence"),
]

OPENER = "Let's examine how Andrea and Gabriel react to the surprise industry announcement line by line."

WALK = [
    (0, None,
     "'Didn't Noemie tell you anything?' Herve asks Gabriel and Andrea if they heard the news."),
    (1, None,
     "'She keeps professional confidentiality.' Herve notes that Noemie kept the secret faithfully."),
    (2, None,
     "'Did you see all the tweets?' Herve points to the flood of announcements on social media."),
    (3, None,
     "'Mathias is becoming a producer at Mediawan!' Herve confirms the massive career move."),
    (4, None,
     "'That is completely incredible news.' Gabriel reacts with shock to the revelation."),
    (5, None,
     "'I refuse to negotiate with him.' Gabriel dreads dealing with Mathias as an outside producer."),
    (6, None,
     "'Would you prefer he left with his talents?' Andrea asks if losing clients is better."),
    (7, None,
     "'Our mission is clear now.' Andrea outlines the primary objective for the firm."),
    (8, None,
     "'We must convince all the artists.' Andrea insists on keeping their talent roster intact."),
    (9, None,
     "'Look, our rivals are forming a group.' Gabriel spots competing agents gathering together."),
    (10, None,
     "'Should we be worried tonight?' Gabriel asks whether ASK is facing imminent peril."),
    (11, None,
     "'No, we go on the offensive.' Andrea chooses to fight back rather than retreat."),
    (12, None,
     "'Tomorrow morning, meeting at eight o'clock.' Andrea schedules an urgent strategy session."),
    (13, None,
     "'It is a perfect opportunity for us.' Andrea finds confidence in the upcoming battle."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Faced with Mathias Barneville's sudden departure to become a film producer, Andrea rallies Gabriel to take the offensive and calls an emergency agency meeting for eight o'clock tomorrow morning."
CLOSING = ("lea", "Non, nous passons à l'offensive.")
