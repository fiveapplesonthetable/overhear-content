# Authoring module for dix-pour-cent s03e02 scene 26 (cues 1150-1176).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e02/authoring/scene-26.py --out overhear-content/out/dix-pour-cent/s03e02/scene-26.json

ID = "dix-pour-cent-s03e02-scene-26"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 26
TITLE = "Si on se barrait ?  (What If We Left?)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1150-1176. Late at night at ASK, Andrea can no longer endure Hicham's crushing control. "
    "She pitches an audacious plan to Gabriel: leaving ASK together to launch their own independent agency."
)

INTRO = (
    "Back at the ASK offices late at night, Andrea reaches her breaking point under Hicham's oppressive management style. "
    "She corners Gabriel with an audacious, life-altering proposal. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "C'est Hicham, je n'en peux plus.", "It is Hicham, I cannot take it anymore.",
     [(1150, "C'est Hicham"), (1151, "J'en peux plus")], "Andrea shuts the door firmly behind Gabriel"),
    ("lea", "Moi, il m'étouffe complètement.", "He is completely suffocating me.",
     [(1153, "Moi, il m'étouffe")], ""),
    ("lea", "Et toi, il t'écrase.", "And you, he is crushing you.",
     [(1154, "Toi, il t'écrase")], ""),
    ("lea", "Ce n'est plus possible.", "This is no longer possible.",
     [(1155, "C'est plus possible")], ""),
    ("gabriel", "Je n'en peux plus non plus.", "I cannot take it anymore either.",
     [(1158, "J'en peux plus non plus")], "Gabriel sinks heavily into a chair"),
    ("lea", "Et si on se barrait?", "What if we took off?",
     [(1162, "Si on se barrait")], "Andrea looks intently into Gabriel's eyes"),
    ("gabriel", "Quoi? Mais où ça?", "What? But where to?",
     [(1163, "Quoi"), (1164, "Où ça")], ""),
    ("lea", "On prend tous nos talents.", "We take all our talent clients.",
     [(1165, "On prend tous nos talents")], ""),
    ("lea", "On monte notre propre agence!", "We set up our own agency!",
     [(1166, "On monte notre propre agence")], "Andrea gestures with intense passion"),
    ("gabriel", "Non, c'est vraiment impossible.", "No, that is really impossible.",
     [(1167, "Non, non, c'est impossible")], ""),
    ("gabriel", "C'est beaucoup trop risqué.", "It is much too risky.",
     [(1168, "C'est trop risqué, en fait")], ""),
    ("lea", "Évidemment que c'est risqué.", "Of course it is risky.",
     [(1169, "évidemment que c'est risqué")], ""),
    ("lea", "Mais on ne sera pas les premiers.", "But we will not be the first.",
     [(1170, "on sera pas les premiers")], ""),
    ("lea", "On serait nos propres patrons!", "We would be our own bosses!",
     [(1173, "on est nos propres patrons")], ""),
    ("lea", "On ne peut plus bosser avec lui.", "We can no longer work with him.",
     [(1176, "on peut plus bosser ensemble")], "Andrea leans across the desk with determination"),
]

OPENER = "Let's walk through this intense late-night agency conspiracy step by step."

WALK = [
    (0, None,
     "'It is Hicham, I cannot take it anymore.' Andrea vents her overwhelming frustration with their boss."),
    (1, None,
     "'He is completely suffocating me.' Andrea describes how Hicham micromanages and stifles her work."),
    (2, None,
     "'And you, he is crushing you.' Andrea points out the cruel pressure Hicham puts on Gabriel."),
    (3, None,
     "'This is no longer possible.' Andrea declares that the current agency dynamic has reached a dead end."),
    (4, None,
     "'I cannot take it anymore either.' Gabriel admits that he also feels broken by the hostile environment."),
    (5, None,
     "'What if we took off?' Andrea floats a bold and unexpected question of rebellion."),
    (6, None,
     "'What? But where to?' Gabriel is instantly taken aback by her sudden suggestion."),
    (7, None,
     "'We take all our talent clients.' Andrea envisions bringing their faithful stars along with them."),
    (8, None,
     "'We set up our own agency!' Andrea presents her grand vision of starting a new venture together."),
    (9, None,
     "'No, that is really impossible.' Gabriel recoils at the immense legal and financial obstacles."),
    (10, None,
     "'It is much too risky.' Gabriel worries about the terrifying dangers of an agency mutiny."),
    (11, None,
     "'Of course it is risky.' Andrea acknowledges the immense danger with resolute confidence."),
    (12, None,
     "'But we will not be the first.' Andrea reminds him that top talent agents split off all the time."),
    (13, None,
     "'We would be our own bosses!' Andrea sells the intoxicating freedom of complete independence."),
    (14, None,
     "'We can no longer work with him.' Andrea cements the absolute necessity of walking away from Hicham."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Driven to despair by Hicham's authoritarian behavior, Andrea reveals her revolutionary plan to quit ASK and build an agency of their own with Gabriel."
CLOSING = ("lea", "On monte notre propre agence!")
