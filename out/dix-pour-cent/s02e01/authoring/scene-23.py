# Authoring module for dix-pour-cent s02e01 scene 23 (cues 681-726).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-23.py --out out/dix-pour-cent/s02e01/scene-23.json

ID = "dix-pour-cent-s02e01-scene-23"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 23
TITLE = "Réveil chez Gabriel  (Waking Up at Gabriel's)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Virginie", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 681-726. The morning after crashing at Gabriel's apartment, Virginie wakes up in a playful mood. "
    "Hearing Gabriel worry about ASK's financial collapse, she teases him by offering to train him for an acting career."
)

INTRO = (
    "The morning after her arrival at Gabriel's apartment, Virginie wakes up feeling energized and playful. "
    "As Gabriel frets over the agency's uncertain future, Virginie teases him by offering private acting and singing lessons. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("gabriel", "Ah, la dormeuse est enfin réveillée!",
     "Ah, the sleepyhead is finally awake!",
     [(681, "Ah, la dormeuse est réveillée !")], ""),
    ("lea", "Bonjour Gabriel. Tu as du café?",
     "Good morning Gabriel. Do you have coffee?",
     [(682, "Bonjour"), (730, "Je peux avoir un café ?")], ""),
    ("gabriel", "Oui, prends une tasse dans la cuisine.",
     "Yes, take a cup in the kitchen.",
     [(694, "Mange quelque chose")], ""),
    ("lea", "Si ton agence ferme, que vas-tu faire?",
     "If your agency closes, what will you do?",
     [(696, "Si ton agence coule vraiment")], ""),
    ("gabriel", "Je ne sais pas. Mon travail est ma sécurité.",
     "I do not know. My job is my security.",
     [(703, "Ce travail, c'est ma sécurité")], ""),
    ("lea", "Tu pourrais devenir un grand acteur.",
     "You could become a great actor.",
     [(707, "prendre des cours et tout ça")], ""),
    ("gabriel", "Tu es complètement folle, Virginie!",
     "You are completely crazy, Virginie!",
     [(701, "Tu es folle")], ""),
    ("lea", "Mais non! Je peux te donner des cours.",
     "Not at all! I can give you lessons.",
     [(711, "Je pourrais te donner des cours")], ""),
    ("lea", "De la danse, du chant, de la comédie!",
     "Dance, singing, comedy!",
     [(712, "Danse"), (713, "chant, comédie")], ""),
    ("lea", "Le ciel est plus pur que mon cœur!",
     "The sky is purer than my heart!",
     [(714, "« Le ciel est plus pur que le fond de mon cœur ! »")], "Racine reference quoted without guillemets"),
    ("gabriel", "Tu veux juste te moquer de moi.",
     "You just want to make fun of me.",
     [(716, "Tu veux juste m'enfermer, c'est ça ?")], ""),
    ("lea", "Tu seras magnifique sur scène.",
     "You will be magnificent on stage.",
     [(718, "je te présenterai au monde"), (722, "Elle est magnifique !")], ""),
    ("lea", "Allez, on se met au travail tout de suite.",
     "Come on, let's get to work right away.",
     [(725, "Bon, on se met au travail")], ""),
    ("gabriel", "D'accord, je veux bien essayer.",
     "All right, I am willing to try.",
     [(726, "D'accord")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'Ah, the sleepyhead is finally awake!' Gabriel greets Virginie as she wakes up. "
     "The feminine noun la dormeuse refers to a sleeping woman."),
    (1, None,
     "'Good morning Gabriel. Do you have coffee?' She immediately looks for her morning dose of coffee. "
     "The partitive article du introduces the beverage."),
    (2, None,
     "'Yes, take a cup in the kitchen.' Gabriel invites her to make herself comfortable. "
     "The imperative prends gives a warm and informal invitation."),
    (3, None,
     "'If your agency closes, what will you do?' She asks about his plans if the agency goes bankrupt. "
     "The conjunction si introduces a conditional clause."),
    (4, None,
     "'I do not know. My job is my security.' Gabriel worries about losing his steady career. "
     "The possessive adjective ma agrees with the feminine noun."),
    (5, None,
     "'You could become a great actor.' Virginie teasingly proposes a dramatic career shift. "
     "The conditional pourrais makes a playful suggestion."),
    (6, None,
     "'You are completely crazy, Virginie!' Gabriel laughs at her absurd idea. "
     "The feminine adjective folle matches the female subject."),
    (7, None,
     "'Not at all! I can give you lessons.' She eagerly offers to act as his private mentor. "
     "The phrase mais non strongly contradicts his objection."),
    (8, None,
     "'Dance, singing, comedy!' She lists the classic disciplines of stage performance. "
     "The preposition de is repeated before each separate discipline."),
    (9, None,
     "'The sky is purer than my heart!' She recites a dramatic classical verse to demonstrate. "
     "The comparative adjective plus pur expresses a poetic comparison."),
    (10, None,
     "'You just want to make fun of me.' Gabriel suspects she is only trying to tease him. "
     "The reflexive verb se moquer de means to mock or poke fun."),
    (11, None,
     "'You will be magnificent on stage.' She assures him that audiences will be dazzled. "
     "The future tense form seras indicates future confidence."),
    (12, None,
     "'Come on, let's get to work right away.' She enthusiastically pushes him to begin his training. "
     "The expression se mettre au travail means to start working."),
    (13, None,
     "'All right, I am willing to try.' Gabriel gives in playfully to her theatrical coaching. "
     "The phrase je veux bien indicates willing consent."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Virginie brightens Gabriel's morning with playful banter about his theatrical talents. "
    "Remember the versatile French expression for starting a task: se mettre au travail."
)

CLOSING = ("gabriel", "D'accord, je veux bien essayer.")
