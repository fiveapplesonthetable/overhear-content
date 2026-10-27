# Authoring module for dix-pour-cent s04e02 scene 18 (cues 984-1016).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-18.py --out out/dix-pour-cent/s04e02/scene-18.json

ID = "dix-pour-cent-s04e02-scene-18"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 18
TITLE = "Le frère jumeau d'Ozon  (Ozon's Twin Brother)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "franck": "theo"}
LABELS = {"lea": "Sophia", "franck": "Franck"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 984-1016. At the party, Franck Dubosc teases Sophia with an absurd prank, convincing her "
    "that director François Ozon alternates shoot days with a fictional twin brother Gilles. Sophia laughs off the joke."
)

INTRO = (
    "At the lively apartment party, Franck Dubosc shares a private laugh with young actress Sophia. "
    "Mischievously deadpanning, Franck invents a wild story about director Francois Ozon sharing directing duties with a secret twin brother. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("franck", "Camille t'a parlé du prochain film?",
     "Did Camille tell you about the next film?",
     [(984, "Camille t'a dit")], "Franck brings up the upcoming role"),
    ("lea", "Oui, le projet avec Fabrice Luchini!",
     "Yes, the project with Fabrice Luchini!",
     [(984, "film avec Luchini")], "Sophia confirms the exciting cast"),
    ("franck", "C'est bien François Ozon qui réalise?",
     "It is Francois Ozon directing, right?",
     [(987, "François Ozon qui réalise")], "Franck sets up his playful joke"),
    ("lea", "Oui, enfin, un jour sur deux.",
     "Yes, well, every other day.",
     [(989, "un jour sur deux")], "Sophia repeats the bizarre detail"),
    ("franck", "François Ozon a un frère jumeau.",
     "Francois Ozon has a twin brother.",
     [(992, "frère jumeau")], "Franck spins his absurd yarn"),
    ("lea", "Vraiment? Je ne savais pas cela!",
     "Really? I did not know that!",
     [(997, "Je savais pas")], "Sophia falls for the tall tale"),
    ("franck", "Son frère Gilles tourne le lendemain.",
     "His brother Gilles shoots the next day.",
     [(995, "lendemain c'est Gilles")], "Franck adds comical specifics"),
    ("lea", "Lequel des deux ai-je rencontré?",
     "Which of the two did I meet?",
     [(999, "lequel que j'ai rencontré")], "Sophia tries to trace her memories"),
    ("franck", "Tu as dû voir son frère!",
     "You must have seen his brother!",
     [(1003, "t'as dû voir Gilles")], "Franck doubles down on the tease"),
    ("lea", "Attends, tu me fais marcher, là?",
     "Wait, you are pulling my leg?",
     [(1007, "Tu me fais marcher")], "Sophia catches on to the prank"),
    ("franck", "Oui, j'adore inventer des bêtises.",
     "Yes, I love making up nonsense.",
     [(1007, "Ouais")], "Franck gleefully confesses"),
    ("lea", "Quel clown, j'y ai presque cru!",
     "What a clown, I almost believed it!",
     [(1009, "Quel clown")], "Sophia laughs at her gullibility"),
    ("franck", "Ta grande sincérité est très touchante.",
     "Your great sincerity is very moving.",
     [(1012, "C'est touchant")], "Franck praises her candid warmth"),
    ("lea", "Allez, viens danser avec nous maintenant!",
     "Come on, come dance with us now!",
     [(1015, "Viens danser")], "Sophia pulls him to the dance floor")
]

WALK = [
    (0, None,
     "'Did Camille tell you about the next film?' Franck asks about the upcoming casting. "
     "The compound past verb 'a parle' introduces the conversation topic."),
    (1, None,
     "'Yes, the project with Fabrice Luchini!' Sophia confirms the exciting co-star. "
     "The preposition 'avec' indicates working alongside an actor."),
    (2, None,
     "'It is Francois Ozon directing, right?' Franck asks about the director. "
     "The verb 'realise' refers to cinematic directing."),
    (3, None,
     "'Yes, well, every other day.' Sophia repeats an odd scheduling remark. "
     "The temporal phrase 'un jour sur deux' means every second day."),
    (4, None,
     "'Francois Ozon has a twin brother.' Franck launches into his elaborate prank. "
     "The adjective 'jumeau' denotes a twin sibling."),
    (5, None,
     "'Really? I did not know that!' Sophia reacts with innocent surprise. "
     "The negative imperfect 'ne savais pas' notes former unawareness."),
    (6, None,
     "'His brother Gilles shoots the next day.' Franck elaborates on the alternating schedule. "
     "The temporal noun 'lendemain' designates the following day."),
    (7, None,
     "'Which of the two did I meet?' Sophia tries to figure out which person she saw. "
     "The interrogative pronoun 'lequel' asks to distinguish between options."),
    (8, None,
     "'You must have seen his brother!' Franck teasingly convinces her. "
     "The modal structure 'as du voir' expresses high probability."),
    (9, None,
     "'Wait, you are pulling my leg?' Sophia realizes she is being pranked. "
     "The colorful idiom 'faire marcher' means to pull someone's leg or tease."),
    (10, None,
     "'Yes, I love making up nonsense.' Franck proudly admits his playful habit. "
     "The colloquial noun 'betises' refers to harmless silliness or jokes."),
    (11, None,
     "'What a clown, I almost believed it!' Sophia laughs at her own credulity. "
     "The noun 'clown' affectionately labels someone playful and humorous."),
    (12, None,
     "'Your great sincerity is very moving.' Franck warmly compliments Sophia's candid honesty. "
     "The feminine noun 'sincerite' commends genuine, open nature."),
    (13, None,
     "'Come on, come dance with us now!' Sophia dismisses the teasing and invites Franck to dance. "
     "The imperative 'viens danser' urges immediate celebration.")
]

OUTRO = (
    "With laughter and playful banter, Franck Dubosc brings warmth and joy to the gathering. "
    "Recognizing Sophia's refreshing sincerity, he joins her on the dance floor in high spirits. "
    "Now let's listen to the scene one last time in French."
)

CLOSING = ("lea", "Allez, viens danser avec nous maintenant!")
