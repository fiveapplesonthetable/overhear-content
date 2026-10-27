# Authoring module for dix-pour-cent s02e03 scene 30 (cues 801-846).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-30.py --out out/dix-pour-cent/s02e03/scene-30.json

ID = "dix-pour-cent-s02e03-scene-30"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 30
TITLE = "Libérés de cellule  (Released from the Cell)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "officer": "marcel"}
LABELS = {"lea": "Norman", "gabriel": "Gabriel", "officer": "Le policier"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 801-846. Sitting in the cell, Norman confides his deep feelings of inadequacy to Gabriel, "
    "who reveals he never actually called Audiard to cancel. The police officer, moved by their conversation "
    "and remembering his own abandoned youth dreams, decides to release them without charges."
)

INTRO = (
    "Sharing a cold detention cell into the early morning hours, Gabriel helps Norman confront his deepest insecurities about working with legendary director Jacques Audiard. "
    "Moved by their honesty, the sympathetic police officer makes an unexpected decision that gives Norman a second chance at his film career. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Il voulait que je sois dur.", "He wanted me to be tough.",
     [(802, "Il voulait que je sois dur")], "Norman explains Audiard's demands"),
    ("lea", "Je ne peux pas, je n'ai pas assez vécu.", "I cannot do it, I have not lived enough.",
     [(804, "Je ne peux pas, je n'ai pas assez vécu")], ""),
    ("lea", "Il m'a dit de chercher en moi.", "He told me to search within myself.",
     [(806, "Il m'a dit de chercher en moi")], ""),
    ("lea", "J'ai cherché mais il n'y avait rien.", "I searched but there was nothing.",
     [(807, "J'ai cherché mais il n'y avait rien")], ""),
    ("gabriel", "Tu as inventé tout un genre sur Internet.", "You invented a whole genre on the Internet.",
     [(809, "inventé tout un genre sur Internet")], ""),
    ("gabriel", "Tu as ta propre folie, ta propre violence.", "You have your own madness, your own violence.",
     [(813, "Tu as ta propre folie, ta propre violence")], ""),
    ("gabriel", "Audiard veut ce qu'il y a sous la surface.", "Audiard wants what lies beneath the surface.",
     [(816, "Audiard veut ce qu'il y a sous la surface")], ""),
    ("lea", "De toute façon, c'est trop tard maintenant.", "In any case, it is too late now.",
     [(817, "De toute façon, c'est trop tard maintenant")], ""),
    ("gabriel", "Non, ce n'est pas trop tard.", "No, it is not too late.",
     [(818, "Non, ce n'est pas trop tard")], ""),
    ("gabriel", "Je ne l'ai pas appelé.", "I did not call him.",
     [(820, "Je ne l'ai pas appelé")], "revealing his trick"),
    ("lea", "Tu m'as sauvé la mise!", "You saved my skin!",
     [(822, "Tu m'as sauvé la mise")], ""),
    ("officer", "Monsieur Sarda, suivez-moi, s'il vous plaît.", "Mr. Sarda, follow me, please.",
     [(826, "Monsieur Sarda"), (827, "Suivez-moi, s'il vous plaît")], "the officer unlocks the cell"),
    ("officer", "Vous êtes libre de partir.", "You are free to leave.",
     [(828, "Vous êtes libre de partir")], ""),
    ("officer", "Je vous ai entendus parler cette nuit.", "I heard you talking last night.",
     [(831, "Je vous ai entendus parler cette nuit")], ""),
    ("officer", "Tout le monde a peur. Il doit faire ce film.", "Everyone has fear. He must make this movie.",
     [(833, "tout le monde a peur"), (840, "Il doit faire ce film")], ""),
    ("gabriel", "Merci beaucoup!", "Thank you very much!",
     [(841, "Merci beaucoup")], ""),
    ("lea", "Je conduis? Non.", "Should I drive? No.",
     [(846, "Je conduis ? Non")], "leaving the police station"),
]

OPENER = "Let's walk through the overnight conversation and release step by step."

WALK = [
    (0, None,
     "'He wanted me to be tough.' Norman describes the director's demanding vision."),
    (1, None,
     "'I cannot do it, I have not lived enough.' Norman admits his feeling of inadequacy."),
    (2, None,
     "'He told me to search within myself.' The verb 'chercher' takes the preposition 'en'."),
    (3, None,
     "'I searched but there was nothing.' Norman describes his internal emptiness."),
    (4, None,
     "'You invented a whole genre on the Internet.' Gabriel reminds Norman of his creative achievements."),
    (5, None,
     "'You have your own madness, your own violence.' Gabriel affirms Norman's unique energy."),
    (6, None,
     "'Audiard wants what lies beneath the surface.' The phrase 'sous la surface' evokes deeper emotion."),
    (7, None,
     "'In any case, it is too late now.' This common conversational idiom means anyway."),
    (8, None,
     "'No, it is not too late.' Gabriel prepares his surprising revelation."),
    (9, None,
     "'I did not call him.' The compound past negation 'ne... pas' frames the verb 'appeler'."),
    (10, None,
     "'You saved my skin!' The idiom 'sauver la mise' means to save the day."),
    (11, None,
     "'Mr. Sarda, follow me, please.' The imperative 'suivez-moi' commands him politely."),
    (12, None,
     "'You are free to leave.' The adjective 'libre' means free."),
    (13, None,
     "'I heard you talking last night.' The past participle 'entendus' agrees with 'vous'."),
    (14, None,
     "'Everyone has fear. He must make this movie.' The officer shows deep empathy for the young actor."),
    (15, None,
     "'Thank you very much!' Gabriel expresses immense gratitude."),
    (16, None,
     "'Should I drive? No.' Norman jokes about his missing driver's license."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Thanks to Gabriel's clever bluff and a compassionate police officer, Norman regains his confidence and heads toward his big-screen debut."
CLOSING = ("lea", "Je conduis? Non.")
