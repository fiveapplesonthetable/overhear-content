# Authoring module for dix-pour-cent s02e05 scene 13 (cues 361-377).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e05/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s02e05/scene-13.json

ID = "dix-pour-cent-s02e05-scene-13"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 13
TITLE = "Le test de grossesse  (Pregnancy Test)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie"}
LABELS = {"lea": "Andréa", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 361-377. In the ASK agency restroom, Andréa and Camille discover a positive pregnancy test "
    "and playfully guess which woman in the office it belongs to."
)

INTRO = (
    "In the agency restroom, Andrea and Camille discover a positive pregnancy test left behind in the trash. "
    "Intrigued and amused, they speculate about which colleague or visiting client could be expecting a baby. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Regarde ça! C'est drôle.",
     "Look at that! It is funny.",
     [(361, "C'est drôle")], ""),
    ("camille", "De qui tu crois que c'est?",
     "Whose do you think it is?",
     [(362, "De qui tu crois que c'est")], ""),
    ("lea", "Tu penses à Sofia?",
     "Do you think of Sofia?",
     [(364, "Sofia")], ""),
    ("camille", "Non, pas Sofia. Et moi alors?",
     "No, not Sofia. What about me?",
     [(365, "Camille")], ""),
    ("lea", "Non, pas toi, Camille.",
     "No, not you, Camille.",
     [(365, "Camille")], ""),
    ("lea", "Peut-être Noémie?",
     "Maybe Noemie?",
     [(366, "Noémie")], ""),
    ("camille", "Ou une actrice de passage?",
     "Or a visiting actress?",
     [(367, "Une actrice")], ""),
    ("lea", "Non, tu imagines une actrice ici?",
     "No, can you imagine an actress here?",
     [(367, "Non"), (368, "Tu imagines")], ""),
    ("lea", "Une actrice qui fait son test ici?",
     "An actress taking her test here?",
     [(369, "Une actrice qui vient"), (369, "sur son test de grossesse ici")], "adapted from line"),
    ("camille", "En tout cas, solidarité féminine!",
     "In any case, female solidarity!",
     [(370, "solidarité féminine")], ""),
    ("lea", "Vous savez ce qu'on dit?",
     "Do you know what they say?",
     [(371, "Vous savez ce qu'on dit")], ""),
    ("camille", "Non, pas du tout.",
     "No, not at all.",
     [(373, "Je savais pas qu'on disait ça")], ""),
    ("lea", "Pas un mot à personne!",
     "Not a word to anyone!",
     [(372, "Pas un mot")], ""),
    ("camille", "Je ne dis rien, promis.",
     "I say nothing, promise.",
     [(372, "Pas un mot")], "adapted agreement"),
    ("lea", "C'est notre petit secret.",
     "It is our little secret.",
     [(372, "Pas un mot")], "adapted closure")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Look at that! It is funny.' Andrea points out the unexpected object with amusement. "
     "The demonstrative pronoun introduces an amusing visual surprise."),
    (1, None,
     "'Whose do you think it is?' Camille wonders who took the test. "
     "The interrogative phrase asks for the owner of the test."),
    (2, None,
     "'Do you think of Sofia?' Andrea suggests their colleague as a candidate. "
     "The prepositional verb specifies the person under consideration."),
    (3, None,
     "'No, not Sofia. What about me?' Camille playfully floats herself as a possibility. "
     "The disjunctive pronoun puts forward her own name."),
    (4, None,
     "'No, not you, Camille.' Andrea immediately dismisses that option. "
     "The direct address rules out the young assistant."),
    (5, None,
     "'Maybe Noemie?' Andrea suggests Mathias's devoted assistant next. "
     "The modal adverb introduces a tentative possibility."),
    (6, None,
     "'Or a visiting actress?' Camille considers external celebrity clients. "
     "The prepositional phrase specifies temporary presence."),
    (7, None,
     "'No, can you imagine an actress here?' Andrea finds that idea far-fetched. "
     "The verb imagines questions the plausibility of the scenario."),
    (8, None,
     "'An actress taking her test here?' She pictures a star using the office toilet. "
     "The relative clause describes an improbable bathroom action."),
    (9, None,
     "'In any case, female solidarity!' Camille invokes discretion among women. "
     "The noun phrase appeals to mutual loyalty."),
    (10, None,
     "'Do you know what they say?' Andrea recalls a humorous proverb. "
     "The fixed expression introduces a folk saying."),
    (11, None,
     "'No, not at all.' Camille has never heard the expression before. "
     "The emphatic negative adverb conveys total unfamiliarity."),
    (12, None,
     "'Not a word to anyone!' Andrea demands complete confidentiality. "
     "The elliptical command enforces strict office silence."),
    (13, None,
     "'I say nothing, promise.' Camille vows to keep quiet. "
     "The negative present verb guarantees discretion."),
    (14, None,
     "'It is our little secret.' Andrea seals the shared discovery. "
     "The possessive determiner establishes a shared bond.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Amused by their restroom discovery, Andrea and Camille agree to keep the positive test strictly between themselves. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "Motus et bouche cousue!")
