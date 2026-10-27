# Authoring module for dix-pour-cent s03e06 scene 22 (cues 1102-1218).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-22.py --out out/dix-pour-cent/s03e06/scene-22.json

ID = "dix-pour-cent-s03e06-scene-22"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 22
TITLE = "Une infirmière de province  (A Provincial Nurse)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "corinne": "emilie"}
LABELS = {"lea": "Andréa", "corinne": "Corinne"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1102-1218. In the screening room, Corinne explains her role as a nurse and shares a heartfelt "
    "hospital memory that moves the producers to tears. Claude Lelouch offers her a role, and Andrea proudly thanks her."
)

INTRO = (
    "In the screening room, Andrea and the producers review the film footage featuring Corinne. "
    "Corinne explains her role as a nurse and shares a deeply poignant hospital memory, moving the entire room and making Andrea proud. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Le premier montage du film est prêt.",
     "The first cut of the film is ready.",
     [(1104, "C'est un premier montage")], "Andrea introduces the screening"),
    ("corinne", "Je joue le rôle d'une infirmière.",
     "I play the role of a nurse.",
     [(1162, "le rôle de l'infirmière")], "Corinne clarifies her character"),
    ("lea", "Vous avez soigné un vieux patient?",
     "You cared for an elderly patient?",
     [(1163, "soins à ce petit monsieur")], "Andrea prompts her for details"),
    ("corinne", "Oui, le vieux monsieur Cardette.",
     "Yes, elderly Mr. Cardette.",
     [(1158, "monsieur Cardette")], "Corinne recalls his name"),
    ("corinne", "Il avait presque quatre-vingt-dix ans.",
     "He was nearly ninety years old.",
     [(1166, "avoir 90 ans")], "Corinne describes the frail patient"),
    ("corinne", "Il voulait seulement un peu parler.",
     "He only wanted to talk a little.",
     [(1170, "pour lui parler")], "Corinne recalls his loneliness"),
    ("corinne", "Mais je manquais cruellement de temps.",
     "But I was desperately short on time.",
     [(1173, "J'ai pas le temps")], "Corinne confesses hospital pressure"),
    ("corinne", "Quand je suis revenue, il était mort.",
     "When I returned, he had died.",
     [(1181, "il était mort")], "Corinne shares the heartbreaking end"),
    ("lea", "Votre émotion a bouleversé la salle!",
     "Your emotion moved the entire room!",
     [(1186, "très grande actrice")], "Andrea marvels at the audience reaction"),
    ("corinne", "Claude Lelouch m'a proposé un film.",
     "Claude Lelouch offered me a film.",
     [(1198, "à vous proposer")], "Corinne shares the unexpected offer"),
    ("lea", "C'est un honneur immense pour vous!",
     "It is an immense honor for you!",
     [(1203, "such an honor")], "Andrea celebrates the director's offer"),
    ("corinne", "Merci pour cette soirée totalement incroyable.",
     "Thank you for this totally incredible evening.",
     [(1206, "cette soirée")], "Corinne expresses heartfelt gratitude"),
    ("lea", "Merci pour tout ce courage, Corinne.",
     "Thank you for all this courage, Corinne.",
     [(1216, "Merci de ce que vous avez fait")], "Andrea recognizes her bravery"),
    ("lea", "J'étais très fière d'être votre agent!",
     "I was very proud to be your agent!",
     [(1217, "très fière")], "Andrea offers sincere professional praise")
]

WALK = [
    (0, None,
     "'The first cut of the film is ready.' Andrea presents the work-in-progress cut. "
     "The adjective 'pret' indicates readiness."),
    (1, None,
     "'I play the role of a nurse.' Corinne describes her on-screen character. "
     "The verbal phrase 'jouer le role' means to play the part."),
    (2, None,
     "'You cared for an elderly patient?' Andrea asks about the touching hospital scene. "
     "The verb 'soigner' means to care for or treat medically."),
    (3, None,
     "'Yes, elderly Mr. Cardette.' Corinne remembers the specific patient fondly. "
     "The courtesy title 'monsieur' precedes the family name."),
    (4, None,
     "'He was nearly ninety years old.' Corinne mentions the patient's great age. "
     "The compound numeral 'quatre-vingt-dix' designates ninety."),
    (5, None,
     "'He only wanted to talk a little.' Corinne evokes the patient's simple wish for company. "
     "The restrictive adverb 'seulement' emphasizes his humble request."),
    (6, None,
     "'But I was desperately short on time.' Corinne describes the relentless pace of nursing. "
     "The verb 'manquer de' expresses lacking or being short of something."),
    (7, None,
     "'When I returned, he had died.' Corinne recounts the heartbreaking hospital truth. "
     "The past tense 'etait mort' describes the tragic discovery."),
    (8, None,
     "'Your emotion moved the entire room!' Andrea highlights how profoundly everyone reacted. "
     "The verb 'bouleverser' means to move deeply or overwhelm emotionally."),
    (9, None,
     "'Claude Lelouch offered me a film.' Corinne shares the thrilling news of a role offer. "
     "The compound past verb 'a propose' denotes a formal proposal."),
    (10, None,
     "'It is an immense honor for you!' Andrea celebrates the prestigious recognition. "
     "The noun 'honneur' denotes deep respect and prestige."),
    (11, None,
     "'Thank you for this totally incredible evening.' Corinne expresses her warmth and gratitude. "
     "The adjective 'incroyable' highlights the surreal, wondrous night."),
    (12, None,
     "'Thank you for all this courage, Corinne.' Andrea honors her composure under pressure. "
     "The noun 'courage' commends her bravery before the producers."),
    (13, None,
     "'I was very proud to be your agent!' Andrea closes with sincere professional pride. "
     "The adjective 'fiere' indicates deep admiration and pride.")
]

OUTRO = (
    "Corinne's raw emotional honesty saves the day for ASK, turning a potential disaster into a triumphant celebration. "
    "For one unforgettable evening, a humble provincial nurse became the brightest star in Paris. "
    "Now let's listen to the scene one last time in French."
)

CLOSING = ("lea", "J'étais très fière d'être votre agent!")
