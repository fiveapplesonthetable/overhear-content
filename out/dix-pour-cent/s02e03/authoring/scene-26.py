# Authoring module for dix-pour-cent s02e03 scene 26 (cues 662-682).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-26.py --out out/dix-pour-cent/s02e03/scene-26.json

ID = "dix-pour-cent-s02e03-scene-26"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 26
TITLE = "Virée interdite  (Joyride)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "norman": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Elvis", "norman": "Norman", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 662-682. In the parking lot outside the laser game arena, young Elvis persuades Norman "
    "to take Hicham's luxury sports car for a spin by challenging his courage. "
    "Adapted for A1 French."
)

INTRO = (
    "In the dark parking lot outside the arena, young Elvis corners Norman near Hicham's luxury sports car. "
    "Daring him and calling him a coward, Elvis pushes Norman into making a reckless decision. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Hé, tu es encore debout?",
     "Hey, are you still awake?",
     [(662, "Hé !"), (663, "T'es encore debout ?")], ""),
    ("norman", "Je ne dors pas. Il ne faut pas jouer ici.",
     "I am not sleeping. You must not play here.",
     [(664, "Je dors pas"), (665, "Faut pas jouer avec les voitures.")], "Combined lines"),
    ("lea", "On peut faire un tour de voiture?",
     "Can we go for a spin in the car?",
     [(666, "On peut faire un tour ?")], "Added de voiture"),
    ("norman", "Pas de tour, ce n'est pas ta voiture.",
     "No spin, it is not your car.",
     [(667, "Pas de tour, c'est pas un jouet, c'est pas ta voiture.")], "Formalized negation"),
    ("lea", "C'est celle de mon père, il est d'accord!",
     "It is my father's, he agrees!",
     [(668, "C'est celle de mon père, il est d'accord.")], ""),
    ("norman", "Ah non, pas du tout, va au lit.",
     "Oh no, not at all, go to bed.",
     [(669, "Ah non, pas du tout. On déconne pas, allez au lit.")], "Simplified line"),
    ("lea", "S'il te plaît, Norman!",
     "Please, Norman!",
     [(670, "S'il te plaît, Norman !")], ""),
    ("lea", "Tu as peur de conduire?",
     "Are you afraid of driving?",
     [(671, "T'as peur ? Je parie que t'as peur de conduire.")], "Shortened question"),
    ("lea", "Tu as peur, poule mouillée!",
     "You are scared, wimp!",
     [(673, "T'as peur, poule mouillée !")], ""),
    ("norman", "D'accord, monte, on y va!",
     "All right, get in, let us go!",
     [(674, "On y va !")], "Added d'accord, monte"),
    ("gabriel", "Qu'est-ce qu'ils font là-bas?",
     "What are they doing over there?",
     [(675, "Tu t'énerves, là ?")], "Adapted dialogue"),
    ("gabriel", "Norman prend la voiture d'Hicham!",
     "Norman is taking Hicham's car!",
     [(678, "C'est dirigé contre moi.")], "Adapted line"),
    ("norman", "Attache ta ceinture, Elvis!",
     "Fasten your seat belt, Elvis!",
     [], "Norman driving warning"),
    ("lea", "C'est parti, roule vite!",
     "Here we go, drive fast!",
     [], "Elvis excited response"),
    ("gabriel", "C'est une très mauvaise idée.",
     "That is a very bad idea.",
     [(680, "Il ne respecte rien.")], "Adapted reaction"),
]

OPENER = "Let's examine how Elvis is convincing Norman to take the sports car for a drive."

WALK = [
    (0, None,
     "'Hey, are you still awake?' A familiar question checking if someone is up late."),
    (1, None,
     "'I am not sleeping. You must not play here.' The impersonal verb falloir in the negative."),
    (2, None,
     "'Can we go for a spin in the car?' The idiom faire un tour meaning to go for a drive."),
    (3, None,
     "'No spin, it is not your car.' A firm refusal followed by a negative possessive clause."),
    (4, None,
     "'It is my father's, he agrees!' The demonstrative pronoun celle referring to the car."),
    (5, None,
     "'Oh no, not at all, go to bed.' The emphatic negative phrase pas du tout."),
    (6, None,
     "'Please, Norman!' A polite begging formula."),
    (7, None,
     "'Are you afraid of driving?' The idiom avoir peur de followed by an infinitive."),
    (8, None,
     "'You are scared, wimp!' An informal playful insult challenging courage."),
    (9, None,
     "'All right, get in, let us go!' An imperative followed by the idiom on y va."),
    (10, None,
     "'What are they doing over there?' The interrogative phrase qu'est-ce que with a spatial adverb."),
    (11, None,
     "'Norman is taking Hicham's car!' The present tense of prendre describing the unauthorized departure."),
    (12, None,
     "'Fasten your seat belt, Elvis!' An imperative addressed to a passenger."),
    (13, None,
     "'Here we go, drive fast!' An excited exclamation launching the drive."),
    (14, None,
     "'That is a very bad idea.' An evaluative statement predicting trouble."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Norman gives in to Elvis's teasing and drives off into the night in Hicham's car. "
    "A disastrous joyride is about to unfold."
)

CLOSING = ("norman", "Attention au virage!")
