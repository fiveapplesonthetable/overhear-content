# Authoring module for dix-pour-cent s04e04 scene 09 (cues 593-835).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-09.py --out overhear-content/out/dix-pour-cent/s04e04/scene-09.json

ID = "dix-pour-cent-s04e04-scene-09"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 9
TITLE = "Le refuge des loups  (The Wolves' Shelter)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "ulrika": "emilie"}
LABELS = {"lea": "Mathias", "ulrika": "Ulrika"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 616-641. In order to charm author Ulrika Desrosières and win her book's adaptation rights, "
    "Mathias visits her animal shelter. Posing as an animal lover, he finds himself invited into the pen to feed wolves."
)

INTRO = (
    "Aiming to secure the lucrative film rights to Ulrika Desrosieres's bestselling novel, Mathias Barneville travels to an animal sanctuary. "
    "He poses as an ardent philanthropist who deeply cares for retired circus performers. "
    "Ulrika welcomes the polished producer and invites him to participate in a surprisingly dangerous feeding routine. "
    "Let's listen to their meeting in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("ulrika", "Bienvenue dans notre refuge pour animaux âgés.",
     "Welcome to our shelter for elderly animals.",
     [(619, "Comme refuge pour eux")], "Ulrika introduces the sanctuary"),
    ("lea", "Votre travail ici est vraiment admirable, Ulrika.",
     "Your work here is truly admirable, Ulrika.",
     [(631, "Vous faites un travail formidable")], "Mathias begins his flattery"),
    ("ulrika", "Vous aimez vraiment les bêtes de cirque?",
     "Do you really like circus animals?",
     [(618, "cet endroit")], "Ulrika checks his motives"),
    ("lea", "J'ai toujours adoré protéger les animaux.",
     "I have always loved protecting animals.",
     [(630, "ce qu'il advenait des animaux")], "Mathias claims a passion for animals"),
    ("ulrika", "C'est rare pour un producteur parisien.",
     "That is rare for a Parisian producer.",
     [(623, "Je vous présente Mathias")], "Ulrika notes the contrast"),
    ("lea", "Je suis un homme de cœur d'abord.",
     "I am a man of heart first.",
     [(632, "C'est la moindre des choses")], "Mathias presents himself warmly"),
    ("ulrika", "Nous cherchons de nouveaux donateurs très généreux.",
     "We look for very generous new donors.",
     [(624, "Un nouveau donateur"), (625, "Et très généreux !")], "Ulrika mentions funding needs"),
    ("lea", "Je souhaite soutenir votre magnifique projet.",
     "I wish to support your magnificent project.",
     [(626, "Merci, on en a vraiment besoin !")], "Mathias pledges financial backing"),
    ("ulrika", "Venez m'aider avec notre travail quotidien.",
     "Come help me with our daily work.",
     [(633, "Vous voulez venir avec moi ?")], "Ulrika invites him to pitch in"),
    ("lea", "Avec plaisir, que devons-nous faire ensemble?",
     "With pleasure, what must we do together?",
     [(634, "Avec plaisir")], "Mathias gallantly agrees"),
    ("ulrika", "Nous allons nourrir les loups sauvages!",
     "We are going to feed wild wolves!",
     [(634, "Je vais nourrir les loups"), (635, "Les loups")], "Ulrika reveals the task"),
    ("lea", "Les loups? Dans cet enclos fermé?",
     "Wolves? Inside this enclosed pen?",
     [(635, "Les loups")], "Mathias feels sudden panic"),
    ("ulrika", "N'ayez pas peur, ils sont affamés!",
     "Do not be afraid, they are hungry!",
     [(638, "Vous n'avez pas peur ?")], "Ulrika laughs off the danger"),
    ("lea", "Très bien, avançons avec grand courage.",
     "Very well, let us advance with great courage.",
     [(639, "Non, non")], "Mathias puts on a brave face"),
]

WALK = [
    (0, None,
     "'Welcome to our shelter for elderly animals.' Ulrika shows the stylish Parisian producer around the grounds. "
     "The masculine noun 'refuge' means sanctuary or shelter."),
    (1, None,
     "'Your work here is truly admirable, Ulrika.' Mathias begins his flattery to gain the author's favor. "
     "The adjective 'admirable' means worthy of admiration."),
    (2, None,
     "'Do you really like circus animals?' Ulrika checks whether his interest in rescue beasts is genuine. "
     "The feminine noun 'betes' means animals or beasts."),
    (3, None,
     "'I have always loved protecting animals.' Mathias fabricates a lifelong commitment to animal welfare. "
     "The infinitive 'proteger' means to protect."),
    (4, None,
     "'That is rare for a Parisian producer.' Ulrika notes that film executives rarely spend time around farm animals. "
     "The adjective 'rare' describes unusual occurrences."),
    (5, None,
     "'I am a man of heart first.' Mathias lays on his charm with polished elegance. "
     "The phrase 'homme de coeur' describes a generous, caring person."),
    (6, None,
     "'We look for very generous new donors.' Ulrika highlights the severe operating expenses of the sanctuary. "
     "The adjective 'genereux' describes generous contributors."),
    (7, None,
     "'I wish to support your magnificent project.' Mathias promises generous financial assistance to win her book rights. "
     "The verb 'soutenir' means to support."),
    (8, None,
     "'Come help me with our daily work.' Ulrika invites him past the visitor gates into the pens. "
     "The adjective 'quotidien' means daily."),
    (9, None,
     "'With pleasure, what must we do together?' Mathias accepts eagerly before knowing the details of the job. "
     "The modal verb 'devons' expresses obligation."),
    (10, None,
     "'We are going to feed wild wolves!' Ulrika announces the terrifying chore with cheerful enthusiasm. "
     "The masculine noun 'loups' means wolves."),
    (11, None,
     "'Wolves? Inside this enclosed pen?' Mathias stammers as his suave composure quickly evaporates. "
     "The masculine noun 'enclos' refers to an animal pen."),
    (12, None,
     "'Do not be afraid, they are hungry!' Ulrika laughs and encourages the pale agent to enter. "
     "The adjective 'affames' describes starving beasts."),
    (13, None,
     "'Very well, let us advance with great courage.' Mathias forces a smile while stepping trembling toward the wolves. "
     "The noun 'courage' means bravery."),
]

OUTRO = (
    "Trapped by his own polite lies, Mathias steps cautiously into the pen beside the howling wolves. "
    "Determined to land the adaptation rights whatever the cost, the producer prepares to brave wild predators. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Les loups attendent leur repas avec faim!")
