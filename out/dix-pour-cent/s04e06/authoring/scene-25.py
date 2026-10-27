# Authoring module for dix-pour-cent s04e06 scene 25 (cue 1040).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e06/authoring/scene-25.py --out out/dix-pour-cent/s04e06/scene-25.json

ID = "dix-pour-cent-s04e06-scene-25"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 25
TITLE = "Éteindre les lumières  (Turning Off the Lights)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 1040. In the quiet offices of ASK after the party, Gabriel and Andrea prepare to leave. "
    "Looking around the darkened agency, Andrea asks Gabriel to turn off the lights one last time."
)

INTRO = (
    "In the empty offices of ASK after the farewell gathering, Andrea and Gabriel linger alone in the quiet hallways. "
    "Looking around at the dark desks and deserted corridors, they share a poignant moment before Gabriel turns off the agency lights forever. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's look at Andrea and Gabriel in the quiet ASK office step by step."

STORY = [
    ("lea", "Tout le monde est parti maintenant.", "Everyone has left now.",
     [(1038, "parti")], ""),
    ("gabriel", "Oui, le bureau est enfin vide.", "Yes, the office is finally empty.",
     [(1038, "partir")], ""),
    ("lea", "Regarde toutes ces chaises vides.", "Look at all these empty chairs.",
     [(1038, "partir")], ""),
    ("gabriel", "C'est étrange sans tout ce bruit.", "It is strange without all this noise.",
     [(1038, "partir")], ""),
    ("lea", "Nous avons vécu des moments formidables.", "We experienced wonderful moments.",
     [(1038, "partir")], ""),
    ("gabriel", "Dix ans de travail ensemble.", "Ten years of work together.",
     [(1038, "partir")], ""),
    ("lea", "Je n'oublierai jamais cette aventure.", "I will never forget this adventure.",
     [(1038, "partir")], ""),
    ("gabriel", "Moi non plus, chère Andréa.", "Me neither, dear Andrea.",
     [(1038, "partir")], ""),
    ("lea", "Tu es prêt à partir maintenant?", "Are you ready to leave now?",
     [(1038, "Prêt à partir")], ""),
    ("gabriel", "Oui, prenons nos manteaux.", "Yes, let us take our coats.",
     [(1039, "Allez")], ""),
    ("lea", "Attends! Les lumières!", "Wait! The lights!",
     [(1040, "Attends ! Les lumières")], ""),
    ("gabriel", "Ah oui, j'allais oublier.", "Oh yes, I was going to forget.",
     [(1040, "lumières")], ""),
    ("lea", "Éteins le grand couloir.", "Turn off the big hallway.",
     [(1040, "lumières")], ""),
    ("gabriel", "Voilà, tout est sombre maintenant.", "There, everything is dark now.",
     [(1040, "lumières")], ""),
]

WALK = [
    (0, None,
     "'Everyone is left now.' Andrea observes the quiet agency after the party."),
    (1, None,
     "'Yes, the office is finally empty.' Gabriel agrees with a gentle nod."),
    (2, None,
     "'Look at all these empty chairs.' Andrea looks at the deserted space."),
    (3, None,
     "'It is strange without all this noise.' Gabriel feels that the silence is strange."),
    (4, None,
     "'We experienced wonderful moments.' Andrea recalls the wonderful years that they shared."),
    (5, None,
     "'Ten years of work together.' Gabriel reflects on the long years of shared work."),
    (6, None,
     "'I will never forget this adventure.' Andrea says that this adventure was unforgettable."),
    (7, None,
     "'Me neither, dear Andrea.' Gabriel reassures her that he feels the same way."),
    (8, None,
     "'Are you ready to leave now?' Andrea asks if he is ready to go."),
    (9, None,
     "'Yes, let us take our coats.' Gabriel gathers his coat to prepare for the cold."),
    (10, None,
     "'Wait! The lights!' Andrea reminds him to turn off the lights."),
    (11, None,
     "'Oh yes, I was going to forget.' Gabriel smiles and moves to the wall switch."),
    (12, None,
     "'Turn off the big hallway.' Andrea points to the switch in the long corridor."),
    (13, None,
     "'There, everything is dark now.' Gabriel turns off the lamps and it is now dark."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Standing in the quiet darkness of ASK, Andrea and Gabriel share a final nostalgic moment together before turning off the office lights and walking away."
CLOSING = ("gabriel", "Voilà, tout est sombre maintenant.")
