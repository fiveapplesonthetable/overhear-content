# Authoring module for dix-pour-cent s03e05 scene 03 (cues 46-58).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-03.py --out out/dix-pour-cent/s03e05/scene-03.json

ID = "dix-pour-cent-s03e05-scene-03"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 3
TITLE = "Les trente ans d'ASK  (Thirty Years of ASK)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel"}
LABELS = {"lea": "Mathias", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 46-58. Mathias shows Hicham where ASK was founded thirty years ago, planning the agency anniversary party. Adapted for A1 French.")

INTRO = ("At the ASK office, senior agent Mathias Barneville walks executive director Hicham Janowski through party plans. "
         "Insisting on celebrating the agency's thirtieth anniversary right at the firm, Mathias shares the founding history of the company. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Voici mon projet pour la fête d'ASK.",
  "Here is my project for the ASK party.",
  [(46, "les gens arrivent")], "Presented party vision"),
 ("hicham", "Comment prévois-tu d'accueillir les invités?",
  "How do you plan to welcome the guests?",
  [(48, "petite coupe")], "Inquired about guest reception"),
 ("lea", "Une coupe de champagne de bienvenue.",
  "A welcome glass of champagne.",
  [(48, "petite coupe")], "Proposed welcome drinks"),
 ("hicham", "Et ensuite, où vont les gens?",
  "And next, where do people go?",
  [(49, "sur la terrasse avec vue sur tout Paris")], "Asked about party layout"),
 ("lea", "Tout le monde monte sur la terrasse.",
  "Everyone goes up to the terrace.",
  [(49, "sur la terrasse avec vue sur tout Paris")], "Described rooftop setting"),
 ("hicham", "Pourquoi ne pas louer un grand lieu?",
  "Why not rent a large venue?",
  [(51, "les 30 ans de l'agence dans un grand lieu")], "Suggested external venue"),
 ("lea", "Je veux fêter nos trente ans ici.",
  "I want to celebrate our thirty years here.",
  [(51, "les 30 ans de l'agence dans un grand lieu")], "Defended in-house celebration"),
 ("hicham", "Je suis prêt à payer le prix.",
  "I am ready to pay the price.",
  [(52, "je suis prêt à mettre les moyens qu'il faut")], "Offered full budget support"),
 ("lea", "Regarde, c'est ici qu'on a commencé.",
  "Look, this is where we started.",
  [(54, "C'est ici qu'on a commencé avec Samuel")], "Showed agency origin spot"),
 ("hicham", "Vous aviez commencé dans cette pièce?",
  "You had started in this room?",
  [(55, "On louait un petit studio")], "Asked about original space"),
 ("lea", "Samuel et moi partagions ce petit studio.",
  "Samuel and I shared this small studio.",
  [(55, "On louait un petit studio")], "Recalled early partnership"),
 ("hicham", "C'est une belle histoire pour l'agence.",
  "That is a lovely story for the agency.",
  [(54, "C'est ici qu'on a commencé avec Samuel")], "Acknowledged heritage"),
 ("lea", "Cette fête aura une valeur sentimentale unique.",
  "This party will have a unique sentimental value.",
  [(50, "je vais pas me battre avec toi là-dessus")], "Emphasized emotional legacy"),
 ("hicham", "D'accord Mathias, organisons tout sur place.",
  "Agreed Mathias, let us organize everything on site.",
  [(50, "je vais pas me battre avec toi là-dessus")], "Conceded to nostalgic venue"),
]

OPENER = "Let's observe as Mathias and Hicham plan the agency's anniversary celebration."

WALK = [
 (0, None,
  "'Here is my project for the ASK party.' A direct presentation introducing the event layout."),
 (1, None,
  "'How do you plan to welcome the guests?' A focused question checking guest reception logistics."),
 (2, None,
  "'A welcome glass of champagne.' A traditional hospitable touch offering sparkling wine on arrival."),
 (3, None,
  "'And next, where do people go?' A sequential logistical query asking about party flow."),
 (4, None,
  "'Everyone goes up to the terrace.' A clear spatial direction leading guests to scenic rooftops."),
 (5, None,
  "'Why not rent a large venue?' A practical commercial suggestion proposing an outside event space."),
 (6, None,
  "'I want to celebrate our thirty years here.' An emotional declaration defending the agency's historic home."),
 (7, None,
  "'I am ready to pay the price.' A generous executive commitment offering financial resources."),
 (8, None,
  "'Look, this is where we started.' A nostalgic gesture pointing to the agency's humble origins."),
 (9, None,
  "'You had started in this room?' A surprised inquiry discovering historical company roots."),
 (10, None,
  "'Samuel and I shared this small studio.' A personal reminiscence honoring the co-founder."),
 (11, None,
  "'That is a lovely story for the agency.' A sympathetic acknowledgment appreciating company tradition."),
 (12, None,
  "'This party will have a unique sentimental value.' An eloquent defense prioritizing heart over luxury."),
 (13, None,
  "'Agreed Mathias, let us organize everything on site.' A gracious concession embracing the historical venue."),
]

TRANSITION = "Now let's listen to Mathias and Hicham again at full speed."

OUTRO = ("Hicham agrees to host the milestone celebration inside the agency, touched by the company's humble beginnings. "
         "Mathias smiles, proud to celebrate thirty years of dedication alongside the memory of his late partner Samuel.")

CLOSING = ("lea", "Ce sera une soirée inoubliable pour nous tous.")
