# Authoring module for dix-pour-cent s02e03 scene 19 (cues 464-495).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-19.py --out out/dix-pour-cent/s02e03/scene-19.json

ID = "dix-pour-cent-s02e03-scene-19"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 19
TITLE = "Dispute autour de l'appartement  (Arguing Over the Apartment)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Catherine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 464-495. Stepping outside the dining room, Catherine and Mathias engage in a vicious confrontation. "
    "Mathias accuses Catherine of using Annick to spite him, while Catherine furiously exposes Mathias's secret betrayal "
    "and his attempt to sell their shared apartment behind her back."
)

INTRO = (
    "Stepping away from the lunch table, Mathias confronts Catherine about her sudden friendship with Annick. "
    "Their bitter divorce erupts into a furious argument over money, trust, and the family apartment. "
    "Listen to the scene in French first."
)

STORY = [
    ("mathias", "Pourquoi tu voulais le numéro d'Annick?",
     "Why did you want Annick's number?",
     [(474, "C'est quoi cette complicité avec Annick ? Pourquoi tu voulais son numéro")], ""),
    ("lea", "C'est interdit que des femmes se parlent?",
     "Is it forbidden for women to talk to each other?",
     [(475, "C'est mauvais que des femmes se parlent")], ""),
    ("mathias", "Tu fais ça juste pour m'embêter!",
     "You're doing this just to annoy me!",
     [(476, "C'est juste pour m'embêter")], ""),
    ("mathias", "Pauvre Camille, prise entre deux feux.",
     "Poor Camille, caught between two fires.",
     [(477, "Pauvre Camille, prise entre deux feux")], ""),
    ("mathias", "Cette situation devient totalement malsaine.",
     "This situation is becoming completely toxic.",
     [(477, "C'est malsain")], ""),
    ("lea", "Tu oses me parler de ce qui est malsain?",
     "You dare talk to me about what is toxic?",
     [(478, "Tu me parles de ce qui est malsain")], ""),
    ("lea", "Vendre notre appartement dans mon dos?",
     "Selling our apartment behind my back?",
     [(479, "Vendre notre appartement dans mon dos, c'est pas malsain")], ""),
    ("mathias", "C'est mon appartement personnel!",
     "It is my personal apartment!",
     [(480, "C'est mon appartement")], ""),
    ("lea", "J'ai financé les rénovations il y a cinq ans.",
     "I financed the renovations five years ago.",
     [(481, "J'ai financé les travaux il y a cinq ans")], ""),
    ("mathias", "Si c'est une simple question d'argent...",
     "If it's a simple question of money...",
     [(482, "Si c'est une question d'argent")], ""),
    ("lea", "Tu caches ton ancienne maîtresse à l'agence!",
     "You are hiding your former mistress at the agency!",
     [(484, "Où vous cachez votre ancienne maîtresse et votre fille")], ""),
    ("mathias", "Je voulais simplement protéger notre famille.",
     "I simply wanted to protect our family.",
     [(485, "j'étais inquiète")], ""),
    ("lea", "Hippolyte m'a dit que tu t'effondrais.",
     "Hippolyte told me you were collapsing.",
     [(485, "Hippolyte m'a dit que vous vous étiez effondré")], ""),
    ("mathias", "Je vais très bien, comme tu le vois.",
     "I am doing very well, as you see.",
     [(486, "Mais je vois que vous allez bien")], ""),
    ("lea", "On ne peut vraiment plus se parler.",
     "We really can't talk to each other anymore.",
     [(488, "Parce que comme vous le voyez, on ne peut plus se parler")], ""),
    ("mathias", "Alors réglons tout avec nos avocats.",
     "Then let's settle everything with our lawyers.",
     [(487, "Pourquoi ne m'avez-vous pas appelée")], "")
]

OPENER = "Let's examine how Catherine and Mathias bitterly clash over their divorce."

WALK = [
    (0, None,
     "'Why did you want Annick's number?' Mathias demands angrily. "
     "The interrogative adverb pourquoi asks for reasons."),
    (1, None,
     "'Is it forbidden for women to talk to each other?' Catherine deflects coolly. "
     "The adjective interdit means prohibited or forbidden."),
    (2, None,
     "'You're doing this just to annoy me!' Mathias sees right through her game. "
     "The verb embêter means to annoy or bother someone."),
    (3, None,
     "'Poor Camille, caught between two fires.' Mathias worries about his daughter. "
     "The idiom pris entre deux feux means caught in the crossfire."),
    (4, None,
     "'This situation is becoming completely toxic.' Mathias criticizes Catherine's maneuver. "
     "The adjective malsain means unhealthy or toxic."),
    (5, None,
     "'You dare talk to me about what is toxic?' Catherine turns on him fiercely. "
     "The verb oser means to dare."),
    (6, None,
     "'Selling our apartment behind my back?' She reveals his hidden scheme. "
     "The idiom dans le dos de quelqu'un means behind someone's back."),
    (7, None,
     "'It is my personal apartment!' Mathias shouts defensively. "
     "The possessive adjective mon indicates sole ownership."),
    (8, None,
     "'I financed the renovations five years ago.' Catherine counters with facts. "
     "The temporal expression il y a expresses ago."),
    (9, None,
     "'If it's a simple question of money...' Mathias attempts to reduce the dispute. "
     "The noun phrase une question d'argent means a financial matter."),
    (10, None,
     "'You are hiding your former mistress at the agency!' Catherine denounces his lies. "
     "The adjective ancienne placed before the noun means former."),
    (11, None,
     "'I simply wanted to protect our family.' Mathias insists on his good intentions. "
     "The verb protéger means to protect."),
    (12, None,
     "'Hippolyte told me you were collapsing.' Catherine mentions their son's worry. "
     "The reflexive verb s'effondrer means to break down or collapse."),
    (13, None,
     "'I am doing very well, as you see.' Mathias refuses to show vulnerability. "
     "The expression aller bien means to be doing well."),
    (14, None,
     "'We really can't talk to each other anymore.' Catherine recognizes the end of dialogue. "
     "The negative structure ne ... plus means no longer."),
    (15, None,
     "'Then let's settle everything with our lawyers.' Mathias surrenders to legal warfare. "
     "The imperative réglons comes from régler.")
]

TRANSITION = "Now let's listen to their explosive argument once more from start to finish."

OUTRO = (
    "With all bridges burned and bitter secrets exposed, Catherine and Mathias leave only the lawyers to resolve their shattered marriage. "
    "Listen to the scene once more in French."
)

CLOSING = ("mathias", "Alors réglons tout avec nos avocats.")
