# Authoring module for dix-pour-cent s03e05 scene 13 (cues 408-448).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s03e05/scene-13.json

ID = "dix-pour-cent-s03e05-scene-13"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 13
TITLE = "La répétition intime  (The Intimate Rehearsal)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "valentin": "theo"}
LABELS = {"lea": "Camille", "valentin": "Valentin"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 408-448. At the ASK agency, Camille coaches her boyfriend and new client Valentin through an audition scene. "
    "When Camille critiques his overly aggressive delivery and explains subtle camera acting, Valentin takes offense "
    "and threatens to walk out before Camille apologizes. Adapted for A1 French."
)

INTRO = (
    "In the quiet of the agency office, Camille Valentini rehearses an audition scene with Valentin. "
    "When Valentin launches into an intense, shouting performance, Camille stops him to explain the nuance of film acting. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
    ("valentin", "Tu dois partir immédiatement là-bas!",
     "You must leave over there immediately!",
     [(408, "Faut que tu ailles là-bas")], "Shouting dramatic line"),
    ("valentin", "C'est une très grande chance pour toi.",
     "It is a very big opportunity for you.",
     [(410, "C'est une grande chance")], "Insisting on career chance"),
    ("valentin", "Ne gâche pas cette opportunité unique!",
     "Do not waste this unique opportunity!",
     [(411, "Ne la gâche pas")], "Urging not to waste"),
    ("valentin", "Pourquoi tu ne veux pas venir avec moi?",
     "Why do you not want to come with me?",
     [(415, "Pourquoi tu veux pas venir avec moi ?")], "Asking why partner refuses"),
    ("lea", "Pourquoi est-ce que tu cries comme ça?",
     "Why are you shouting like that?",
     [(416, "Pourquoi tu cries comme ça ?")], "Critiquing loud delivery"),
    ("lea", "C'est une scène d'amour très intime.",
     "It is a very intimate love scene.",
     [(418, "C'est une scène intime")], "Reminding of scene intimacy"),
    ("lea", "Tu n'as pas besoin de hurler.",
     "You do not need to yell.",
     [(420, "T'as pas besoin de hurler comme ça")], "Advising against shouting"),
    ("valentin", "Mais mon personnage est vraiment en colère!",
     "But my character is really angry!",
     [(422, "Parce qu'il est en colère ?")], "Defending aggressive choice"),
    ("lea", "Il faut une progression dans la scène.",
     "There must be a progression in the scene.",
     [(425, "y'a une progression dans la scène")], "Explaining dramatic arc"),
    ("lea", "La caméra devine tes pensées secrètes.",
     "The camera guesses your secret thoughts.",
     [(428, "Ça finit ta pensée la caméra")], "Highlighting camera sensitivity"),
    ("lea", "Garde le visage calme comme un masque.",
     "Keep your face calm like a mask.",
     [(429, "t'exprimes rien"), (430, "Comme un masque")], "Teaching understated acting"),
    ("valentin", "Tu sais quoi, laisse tomber, j'arrête!",
     "You know what, forget it, I stop!",
     [(435, "laisse tomber"), (437, "Vaut mieux qu'on arrête")], "Getting frustrated and quitting"),
    ("lea", "Attends, reste, je suis désolée Valentin.",
     "Wait, stay, I am sorry Valentin.",
     [(439, "reste"), (444, "Pardon si je t'ai fait douter")], "Pleading with actor to stay"),
    ("lea", "Pardon, c'est entièrement de ma faute.",
     "Sorry, it is entirely my fault.",
     [(445, "Pardon c'est ma faute")], "Assuming responsibility"),
]

WALK = [
    (0, None,
     "'You must leave over there immediately!' Valentin recites his dramatic audition dialogue loudly. "
     "The modal expression 'tu dois' expresses strong obligation."),
    (1, None,
     "'It is a very big opportunity for you.' The character emphasizes what is at stake. "
     "The feminine noun 'chance' means opportunity or lucky break."),
    (2, None,
     "'Do not waste this unique opportunity!' Valentin urges his fictional partner not to squander her future. "
     "The verb 'gacher' means to waste or spoil."),
    (3, None,
     "'Why do you not want to come with me?' Valentin pushes with intense emotion. "
     "The preposition 'avec' introduces accompaniment."),
    (4, None,
     "'Why are you shouting like that?' Camille halts the rehearsal to question his volume. "
     "The verb 'crier' means to shout or cry out."),
    (5, None,
     "'It is a very intimate love scene.' Camille reminds him of the tender context. "
     "The adjective 'intime' describes close, private moments."),
    (6, None,
     "'You do not need to yell.' Camille explains that projection is unnecessary for film. "
     "The verb 'hurler' means to scream or yell loudly."),
    (7, None,
     "'But my character is really angry!' Valentin justifies his intense vocal delivery. "
     "The idiom 'etre en colere' expresses the state of anger."),
    (8, None,
     "'There must be a progression in the scene.' Camille teaches pacing and gradual buildup. "
     "The noun 'progression' signifies a step-by-step development."),
    (9, None,
     "'The camera guesses your secret thoughts.' Camille notes how the camera magnifies subtle thought. "
     "The noun 'camera' denotes the movie camera."),
    (10, None,
     "'Keep your face calm like a mask.' Camille urges a restrained, interior performance. "
     "The masculine noun 'masque' refers to a protective or disguising mask."),
    (11, None,
     "'You know what, forget it, I stop!' Valentin feels hurt and threatens to walk away. "
     "The colloquial idiom 'laisser tomber' means to drop it or give up."),
    (12, None,
     "'Wait, stay, I am sorry Valentin.' Camille rushes to comfort her vulnerable boyfriend. "
     "The adjective 'desolee' conveys heartfelt apology."),
    (13, None,
     "'Sorry, it is entirely my fault.' Camille softens the critique to rebuild his confidence. "
     "The noun 'faute' means mistake, error, or fault."),
]

OUTRO = (
    "Coaching an actor who is also a boyfriend proves delicate for Camille. "
    "Balancing honest professional direction with personal feelings requires patience and tact. "
    "Now let's listen to the scene once more."
)

CLOSING = ("lea", "Pardon, c'est entièrement de ma faute.")
