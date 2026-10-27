# Authoring module for dix-pour-cent s03e02 scene 24 (cues 1057-1090).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e02/authoring/scene-24.py --out overhear-content/out/dix-pour-cent/s03e02/scene-24.json

ID = "dix-pour-cent-s03e02-scene-24"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 24
TITLE = "Les aveux de Gabriel et Monika  (Gabriel and Monica's Confessions)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Monika", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1057-1090. Late in the evening, Gabriel visits Monica Bellucci in her apartment to apologize for his deceit. "
    "To his relief, Monica stops him from beating himself up and admits that she too felt deeply lonely and vulnerable."
)

INTRO = (
    "Late in the evening, a guilt-ridden Gabriel pays a visit to superstar client Monica Bellucci. "
    "Expecting harsh anger, he is surprised to find that Monica shares his vulnerability and loneliness. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("gabriel", "Monika? C'est Gabriel.", "Monica? It is Gabriel.",
     [(1060, "Monika ?"), (1061, "C'est Gabriel")], "Gabriel enters nervously, holding his hat"),
    ("gabriel", "Je suis en dessous de tout.", "I am completely worthless.",
     [(1062, "je suis en dessous de tout")], ""),
    ("gabriel", "Une vraie espèce de raclure.", "A real kind of scumbag.",
     [(1064, "Une espèce de raclure")], ""),
    ("gabriel", "Un vrai détritus, voilà.", "A true piece of trash.",
     [(1066, "Un détritus, voilà")], ""),
    ("lea", "N'en fais pas trop, quand même.", "Do not overdo it, all the same.",
     [(1067, "n'en fais pas trop, quand même")], "Monica gestures for him to sit down"),
    ("gabriel", "Non, mais c'est vrai, quoi!", "No, but it is true, really!",
     [(1068, "Non, mais c'est vrai, quoi")], ""),
    ("lea", "Arrête de te flageller tout le temps.", "Stop beating yourself up all the time.",
     [(1070, "arrête de te flageller")], ""),
    ("lea", "À moi de parler maintenant.", "My turn to speak now.",
     [(1072, "À moi, maintenant")], "Monica sits opposite him on the sofa"),
    ("lea", "Moi aussi, j'ai honte.", "I am ashamed as well.",
     [(1076, "Moi aussi, j'ai honte")], ""),
    ("lea", "C'est moi qui vais mal.", "I am the one doing badly.",
     [(1078, "C'est moi qui suis pas bien")], ""),
    ("lea", "Mettre en péril une relation de confiance?", "Jeopardizing a relationship of trust?",
     [(1080, "Mettre en péril une relation de confiance")], ""),
    ("lea", "Je ne peux pas rester seule?", "Can I not stay alone?",
     [(1082, "je peux pas rester seule un petit peu")], ""),
    ("gabriel", "Mais c'est normal, c'est humain.", "But that is normal, it is human.",
     [(1084, "C'est normal, quoi"), (1085, "C'est humain")], "Gabriel speaks gently to comfort her"),
    ("lea", "C'est très pénible d'être seule.", "It is very painful being alone.",
     [(1086, "C'est pénible, aussi, d'être seule")], ""),
    ("lea", "Ça fait combien de temps, toi?", "How long has it been for you?",
     [(1090, "Ça fait combien de temps, toi")], "Monica looks at Gabriel with genuine curiosity"),
]

OPENER = "Let's walk through these sincere confessions between Gabriel and Monica step by step."

WALK = [
    (0, None,
     "'Monica? It is Gabriel.' Gabriel timidly identifies himself as he arrives at her home."),
    (1, None,
     "'I am completely worthless.' Gabriel wallows in profound guilt over his deceitful behavior."),
    (2, None,
     "'A real kind of scumbag.' Gabriel continues to berate himself with harsh insults."),
    (3, None,
     "'A true piece of trash.' Gabriel concludes his excessive self-criticism in despair."),
    (4, None,
     "'Do not overdo it, all the same.' Monica gently interrupts his extreme self-flagellation."),
    (5, None,
     "'No, but it is true, really!' Gabriel insists that he thoroughly deserves her condemnation."),
    (6, None,
     "'Stop beating yourself up all the time.' Monica urges her agent to cease his self-pity."),
    (7, None,
     "'My turn to speak now.' Monica takes charge of the conversation to share her own burden."),
    (8, None,
     "'I am ashamed as well.' Monica candidly admits that she also feels regret about her actions."),
    (9, None,
     "'I am the one doing badly.' Monica confesses her inner emotional crisis to her friend."),
    (10, None,
     "'Jeopardizing a relationship of trust?' Monica reflects on how close she came to ruining everything."),
    (11, None,
     "'Can I not stay alone?' Monica explains her deep dread of returning to an empty home."),
    (12, None,
     "'But that is normal, it is human.' Gabriel comforts his client with heartfelt understanding."),
    (13, None,
     "'It is very painful being alone.' Monica acknowledges the heavy weight of single life."),
    (14, None,
     "'How long has it been for you?' Monica asks Gabriel about his own experience with bachelorhood."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "After rushing to apologize to Monica Bellucci, Gabriel is relieved to discover that the famous star understands his pain and struggles with loneliness too."
CLOSING = ("lea", "C'est très pénible d'être seule.")
