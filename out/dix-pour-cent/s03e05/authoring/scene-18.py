# Authoring module for dix-pour-cent s03e05 scene 18 (cues 773-782).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-18.py --out overhear-content/out/dix-pour-cent/s03e05/scene-18.json

ID = "dix-pour-cent-s03e05-scene-18"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 18
TITLE = "Plus de corset  (No More Brace)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 773-782. In his office, Noémie playfully demonstrates her recovery to Mathias, "
    "showing that her medical neck brace is off and teasing him about their mutual affection."
)

INTRO = (
    "In Mathias's office at ASK, Noemie reveals a wonderful personal surprise. "
    "Free at last from her medical neck brace, she shows off her restored mobility and shares a playful, affectionate exchange with Mathias. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Vous n'avez rien remarqué d'important?",
     "Did you not notice anything important?",
     [(773, "n'avez même pas remarqué")], ""),
    ("mathias", "Non, qu'est-ce qui a changé?",
     "No, what has changed?",
     [(774, "Quoi")], ""),
    ("lea", "Vous ne voyez vraiment rien là?",
     "Do you truly see nothing there?",
     [(775, "Vous voyez rien là")], ""),
    ("mathias", "Je ne vois rien de particulier.",
     "I see nothing in particular.",
     [(774, "Quoi")], ""),
    ("lea", "Je n'ai plus mon corset!",
     "I do not have my neck brace anymore!",
     [(776, "J'ai plus le corset")], ""),
    ("lea", "Ça y est, c'est enfin fini!",
     "That is it, it is finally over!",
     [(777, "Ça y est c'est fini")], ""),
    ("mathias", "C'est une excellente nouvelle, Noémie.",
     "That is excellent news, Noemie.",
     [(777, "c'est fini")], ""),
    ("lea", "Regardez, je peux bouger librement maintenant.",
     "Look, I can move freely now.",
     [(778, "Regardez je peux même danser")], ""),
    ("lea", "Je peux même danser pour vous!",
     "I can even dance for you!",
     [(778, "danser la danse du ventre")], ""),
    ("mathias", "Moi, j'aimais bien votre corset.",
     "As for me, I actually liked your brace.",
     [(779, "Moi j'aimais bien votre corset")], ""),
    ("lea", "Ah bon, vous trouviez cela bien?",
     "Oh really, did you think that was nice?",
     [(780, "Ah oui")], ""),
    ("mathias", "Oui, cela vous allait très bien.",
     "Yes, it suited you very well.",
     [(781, "Oui")], ""),
    ("lea", "Je pourrais le remettre pour vous.",
     "I could put it back on for you.",
     [(782, "Tu pourrais le remettre")], ""),
    ("lea", "Si cela peut vous faire plaisir!",
     "If that can bring you pleasure!",
     [(782, "si ça vous excite")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Did you not notice anything important?' Noemie teases Mathias about his lack of observation. "
     "The negative question draws attention to her appearance."),
    (1, None,
     "'No, what has changed?' Mathias wonders what he managed to miss. "
     "The confused response seeks clarification."),
    (2, None,
     "'Do you truly see nothing there?' She points to her neck and posture. "
     "The playful question prompts a closer look."),
    (3, None,
     "'I see nothing in particular.' Mathias looks around without spotting the change. "
     "The honest admission confesses his blindness."),
    (4, None,
     "'I do not have my neck brace anymore!' Noemie joyfully reveals she has taken off her medical brace. "
     "The cheerful announcement marks recovery."),
    (5, None,
     "'That is it, it is finally over!' She celebrates the end of her convalescence. "
     "The relieved exclamation expresses pure joy."),
    (6, None,
     "'That is excellent news, Noemie.' Mathias smiles with relief at her physical recovery. "
     "The warm adjective congratulates his assistant."),
    (7, None,
     "'Look, I can move freely now.' She demonstrates her restored mobility. "
     "The imperative verb invites him to observe her movement."),
    (8, None,
     "'I can even dance for you!' Noemie playfully offers a joyful demonstration. "
     "The modal verb highlights her newfound freedom."),
    (9, None,
     "'As for me, I actually liked your brace.' Mathias admits his fondness for her former look. "
     "The personal confession reveals tender affection."),
    (10, None,
     "'Oh really, did you think that was nice?' She reacts with playful surprise to his compliment. "
     "The teasing question continues their banter."),
    (11, None,
     "'Yes, it suited you very well.' Mathias confirms his genuine appreciation. "
     "The affirmative statement compliments her charm."),
    (12, None,
     "'I could put it back on for you.' Noemie flirts with a humorous promise. "
     "The conditional verb offers a playful compromise."),
    (13, None,
     "'If that can bring you pleasure!' She finishes her tease with a bright smile. "
     "The lighthearted remark deepens their romantic connection.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "A moment of lighthearted relief brings Noemie and Mathias closer together amidst hectic agency life. "
    "Listen to the conversation once more in French."
)

CLOSING = ("mathias", "Vous êtes toujours pleine de surprises.")
