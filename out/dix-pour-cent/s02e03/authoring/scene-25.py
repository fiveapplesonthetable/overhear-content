# Authoring module for dix-pour-cent s02e03 scene 25 (cues 642-661).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-25.py --out out/dix-pour-cent/s02e03/scene-25.json

ID = "dix-pour-cent-s02e03-scene-25"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 25
TITLE = "Partie de laser game  (Laser Tag Battle)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "norman": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Andréa", "norman": "Norman", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 642-661. At the laser game arena, the ASK agency team celebrates Elvis's birthday. "
    "While Andréa and Hicham playfully shoot each other, Gabriel congratulates YouTuber Norman Thavaud "
    "on landing a dramatic film role. Adapted for A1 French."
)

INTRO = (
    "At a lively laser game arena, the ASK team gathers to celebrate Elvis's birthday party. "
    "Between rounds of laser tag, Gabriel takes Norman aside to discuss his new movie role. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Viens jouer au laser game!",
     "Come and play laser games!",
     [(642, "Viens jouer au laser game.")], ""),
    ("norman", "Se déguiser et se faire tirer dessus, ce n'est pas mon truc.",
     "Dressing up and being shot at is not my thing.",
     [(643, "Me déguiser en GI et me faire tirer dessus, c'est pas mon truc.")], "Formalized negation"),
    ("lea", "Tu vas voir l'ambiance de l'agence.",
     "You will see the agency's atmosphere.",
     [(644, "Elle va voir ce qu'est ASK.")], "Adapted line"),
    ("lea", "Où sont les gilets?",
     "Where are the vests?",
     [(646, "Où sont les gilets pare-balles ?")], "Shortened to les gilets"),
    ("lea", "Janowski, à toi de jouer!",
     "Janowski, your turn to play!",
     [(647, "Hé, Janowski !"), (649, "À toi !")], ""),
    ("gabriel", "Salut, Norman. Félicitations pour ton film.",
     "Hi, Norman. Congratulations on your movie.",
     [(654, "Salut, Norman."), (655, "Félicitations pour le film d'Audiard.")], "Shortened title"),
    ("norman", "Merci, Gabriel.",
     "Thanks, Gabriel.",
     [(654, "Salut."), (655, "Merci.")], ""),
    ("gabriel", "Je ne t'imaginais pas dans ce rôle.",
     "I did not imagine you in that role.",
     [(656, "Je ne t'imaginais pas dans un rôle comme ça.")], "Shortened sentence"),
    ("norman", "Un rôle comme quoi?",
     "A role like what?",
     [(657, "Un rôle comme quoi ?")], ""),
    ("gabriel", "Un vrai rôle dans un film dramatique.",
     "A real role in a dramatic film.",
     [(658, "Je veux dire, jouer un vrai rôle, dans un film.")], "Added dramatique"),
    ("gabriel", "Où tu dois vraiment jouer la comédie.",
     "Where you must really act.",
     [(659, "Où tu dois vraiment jouer la comédie.")], ""),
    ("norman", "Oui, c'est un grand changement pour moi.",
     "Yes, it is a big change for me.",
     [(660, "Ouais.")], "Expanded Norman response"),
    ("norman", "De toute façon, c'est très cool.",
     "Anyway, it is very cool.",
     [(661, "De toute façon, c'est cool.")], "Added très"),
    ("gabriel", "Tu as beaucoup de talent, Norman.",
     "You have a lot of talent, Norman.",
     [], "Gabriel encouragement"),
    ("norman", "J'espère que le public va aimer.",
     "I hope the public will like it.",
     [], "Norman hope"),
]

OPENER = "Let's examine how Gabriel is discussing Norman's new acting project with him."

WALK = [
    (0, None,
     "'Come and play laser games!' An imperative urging participation in the game."),
    (1, None,
     "'Dressing up and being shot at is not my thing.' The idiom ce n'est pas mon truc meaning not my cup of tea."),
    (2, None,
     "'You will see the agency's atmosphere.' The near future tense expressing immediate experience."),
    (3, None,
     "'Where are the vests?' An interrogative question looking for game equipment."),
    (4, None,
     "'Janowski, your turn to play!' The phrase a toi followed by de and an infinitive."),
    (5, None,
     "'Hi, Norman. Congratulations on your movie.' Gabriel offers congratulations on a new film."),
    (6, None,
     "'Thanks, Gabriel.' A standard polite acknowledgment."),
    (7, None,
     "'I did not imagine you in that role.' An imperfect tense expressing past expectations."),
    (8, None,
     "'A role like what?' An interrogative question challenging the speaker's assumption."),
    (9, None,
     "'A real role in a dramatic film.' The adjective vrai modifying role."),
    (10, None,
     "'Where you must really act.' The modal verb devoir expressing artistic requirement."),
    (11, None,
     "'Yes, it is a big change for me.' Norman reflects on his career transition."),
    (12, None,
     "'Anyway, it is very cool.' The adverbial phrase de toute facon."),
    (13, None,
     "'You have a lot of talent, Norman.' Gabriel offers sincere professional praise."),
    (14, None,
     "'I hope the public will like it.' The verb esperer followed by a dependent clause."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Gabriel encourages Norman as he transitions from web comedy to serious cinema. "
    "Meanwhile, the party around them continues in full swing."
)

CLOSING = ("norman", "On retourne au jeu!")
