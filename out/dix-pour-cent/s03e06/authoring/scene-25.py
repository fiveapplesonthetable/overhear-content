# Authoring module for dix-pour-cent s03e06 scene 25 (cues 1291-1312).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-25.py --out out/dix-pour-cent/s03e06/scene-25.json

ID = "dix-pour-cent-s03e06-scene-25"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 25
TITLE = "Faire l'agent ailleurs  (An Agent Elsewhere)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1291-1312. In the hallway outside the gala, Camille catches up with Mathias as he prepares to leave ASK. "
    "Though she chooses to remain at the agency, Mathias warmly encourages her before Noemie runs out to join him."
)

INTRO = (
    "In the hallway outside the gala, Camille catches up with Mathias as he prepares to leave ASK. "
    "Though she chooses to remain at the agency, Mathias warmly encourages her before Noemie runs out to join him. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Je ne savais rien de ce plan secret.",
     "I knew nothing about this secret plan.",
     [(1291, "Je savais pas")], "Swore that she had no knowledge of the scheme"),
    ("lea", "Je n'étais pas au courant, je te promets!",
     "I was not in the loop, I promise you!",
     [(1292, "J'étais pas au courant, je te promets")], "Promised her father she was innocent"),
    ("mathias", "Ne t'inquiète pas ma fille, je sais.",
     "Do not worry my daughter, I know.",
     [(1293, "T'inquiète pas")], "Reassured Camille with paternal affection"),
    ("lea", "Où vas-tu partir maintenant, papa?",
     "Where are you going to go now, dad?",
     [(1294, "Tu vas où")], "Inquired about his future plans"),
    ("mathias", "Je vais faire l'agent ailleurs dans Paris.",
     "I will work as an agent elsewhere in Paris.",
     [(1297, "Faire l'agent ailleurs")], "Announced his intention to practice elsewhere"),
    ("mathias", "Veux-tu venir travailler avec moi là-bas?",
     "Do you want to come work with me over there?",
     [(1298, "Tu veux venir avec moi")], "Invited her to partner with him"),
    ("lea", "Je suis désolée, j'aimerais bien rester ici.",
     "I am sorry, I would like to stay here.",
     [(1300, "Je suis désolée"), (1301, "j'aimerais bien rester ici")], "Chose to stay loyal to her colleagues at ASK"),
    ("mathias", "C'est ton choix, ils vont te garder.",
     "It is your choice, they will keep you.",
     [(1303, "ils vont bien vouloir te garder")], "Accepted her decision with grace"),
    ("mathias", "Tu es douée et pleine de talent.",
     "You are gifted and full of talent.",
     [(1304, "T'es doué")], "Praised her talent and instincts"),
    ("mathias", "Tu es quelqu'un de bien, Camille.",
     "You are a good person, Camille.",
     [(1305, "T'es quelqu'un de bien, Camille")], "Gave her his deepest paternal blessing"),
    ("lea", "Merci pour tout ce que tu m'as appris.",
     "Thank you for everything you taught me.",
     [(1305, "Camille")], "Expressed heartfelt filial gratitude"),
    ("mathias", "Prends bien soin de toi et d'eux.",
     "Take good care of yourself and of them.",
     [(1305, "Camille")], "Wished her success and well-being"),
    ("lea", "Regarde papa, Noémie arrive en courant!",
     "Look dad, Noemie is arriving running!",
     [(1312, "c'est Mathias")], "Spotted Noemie rushing toward him"),
    ("lea", "Elle a finalement décidé de te suivre!",
     "She has ultimately decided to follow you!",
     [(1309, "tu vas le suivre"), (1312, "c'est Mathias")], "Announced Noemie's devotion")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'I knew nothing about this secret plan.' Camille rushes to reassure Mathias of her loyalty. "
     "The negative past sentence clarifies her total innocence."),
    (1, None,
     "'I was not in the loop, I promise you!' Camille emphasizes her sincerity. "
     "The idiomatic phrase with the verb expresses complete lack of prior knowledge."),
    (2, None,
     "'Do not worry my daughter, I know.' Mathias comforts her with gentle tenderness. "
     "The negative imperative soothes her immediate distress."),
    (3, None,
     "'Where are you going to go now, dad?' Camille asks about his next steps. "
     "The near-future question inquires about his uncertain destination."),
    (4, None,
     "'I will work as an agent elsewhere in Paris.' Mathias announces his fresh start. "
     "The verbal idiom describes continuing his profession independently."),
    (5, None,
     "'Do you want to come work with me over there?' Mathias makes a heartfelt offer. "
     "The inverted modal question invites her to build a new agency together."),
    (6, None,
     "'I am sorry, I would like to stay here.' Camille chooses her own independent path at ASK. "
     "The polite conditional phrase affirms her desire to remain."),
    (7, None,
     "'It is your choice, they will keep you.' Mathias respects her autonomy completely. "
     "The near-future verb reassures her about her secure position."),
    (8, None,
     "'You are gifted and full of talent.' Mathias praises her professional aptitude. "
     "The descriptive adjectives celebrate her proven skills as an agent."),
    (9, None,
     "'You are a good person, Camille.' Mathias pays her the highest personal compliment. "
     "The warm character evaluation serves as a fatherly blessing."),
    (10, None,
     "'Thank you for everything you taught me.' Camille honors his mentorship. "
     "The compound past verb acknowledges all the valuable guidance received."),
    (11, None,
     "'Take good care of yourself and of them.' Mathias bids a touching farewell. "
     "The caring imperative formula offers protective best wishes."),
    (12, None,
     "'Look dad, Noemie is arriving running!' Camille points down the hallway. "
     "The imperative verb draws attention to Noemie sprinting toward the exit."),
    (13, None,
     "'She has ultimately decided to follow you!' Camille smiles through her emotion. "
     "The compound past verb reveals that Mathias will not be alone after all.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "Outside the gala, Camille bids an affectionate farewell to her father as Noemie runs to join his side. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("mathias", "Prends bien soin de toi et d'eux.")
