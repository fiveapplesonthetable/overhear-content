# Authoring module for dix-pour-cent s04e03 scene 09 (cues 314-420).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-09.py --out overhear-content/out/dix-pour-cent/s04e03/scene-09.json

ID = "dix-pour-cent-s04e03-scene-09"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 9
TITLE = "Le trac du chef  (The Chef's Stage Fright)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jose": "theo"}
LABELS = {"lea": "Andréa", "jose": "José"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 323-403. On the movie set, José Garcia struggles with terrible stage fright while playing a restaurant chef. "
    "When Andréa visits him between takes, she relieves his anxiety by revealing that his co-star Laurence also stood him up twenty years ago."
)

INTRO = (
    "On a movie set where he plays a temperamental restaurant chef, Jose Garcia experiences severe stage fright. "
    "After botching a dozen takes in his chef apron, Jose confesses to his agent Andrea that he feels paralyzed around his co-star Laurence. "
    "Andrea listens to his worries before delivering an astonishing piece of news. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("jose", "Je rate toutes mes prises aujourd'hui.",
     "I mess up all my takes today.",
     [(348, "C'est la 12e prise qu'il rate")], "José laments his poor performance"),
    ("lea", "Calme-toi José, respire un grand coup.",
     "Calm down Jose, take a deep breath.",
     [(351, "-José"), (354, "OK ?")], "Andréa offers encouragement"),
    ("jose", "J'oublie mon texte à chaque fois!",
     "I forget my lines every time!",
     [(349, "il oublie son texte")], "José explains his struggle on set"),
    ("lea", "Tu dois juste crier sur ta brigade.",
     "You must just shout at your brigade.",
     [(352, "Tu dois leur crier dessus")], "Andréa advises him on the role"),
    ("jose", "Je n'y arrive pas avec Laurence.",
     "I cannot manage with Laurence.",
     [(379, "Il va bien ?")], "José confesses his discomfort"),
    ("lea", "Tu penses encore à cette histoire?",
     "Are you still thinking about that story?",
     [(382, "votre liaison il y a 20 ans")], "Andréa refers to their distant past"),
    ("jose", "Nous devions nous retrouver à l'hôtel.",
     "We were supposed to meet at the hotel.",
     [(387, "À l'hôtel, il y a 20 ans")], "José recalls their old rendezvous"),
    ("lea", "C'était il y a vingt ans!",
     "That was twenty years ago!",
     [(382, "il y a 20 ans")], "Andréa puts the past into perspective"),
    ("jose", "Je me sens toujours très coupable.",
     "I still feel very guilty.",
     [(386, "il se sent coupable")], "José admits his lingering regret"),
    ("lea", "J'ai parlé avec Laurence tout à l'heure.",
     "I spoke with Laurence just earlier.",
     [(378, "Je suis Andréa Martel")], "Andréa reveals she investigated"),
    ("jose", "Qu'est-ce qu'elle a dit sur moi?",
     "What did she say about me?",
     [(388, "de savoir que vous ne lui en voulez pas")], "José asks anxiously"),
    ("lea", "Elle n'est pas allée à l'hôtel!",
     "She did not go to the hotel!",
     [(394, "Moi non plus, je ne suis pas allée à l'hôtel")], "Andréa drops the bombshell"),
    ("jose", "Elle m'a posé un lapin aussi?",
     "She stood me up too?",
     [(397, "Vous vous êtes posé un lapin")], "José reacts with total surprise"),
    ("lea", "Oui, vous êtes quittes tous les deux!",
     "Yes, you are both even now!",
     [(398, "On peut dire ça comme ça")], "Andréa reassures her relieved client"),
]

WALK = [
    (0, None,
     "'I mess up all my takes today.' Jose despairs over his disastrous performance on set. "
     "The noun 'prises' means filming takes."),
    (1, None,
     "'Calm down Jose, take a deep breath.' Andrea urges her client to relax between camera setups. "
     "The reflexive verb 'se calmer' means to calm down."),
    (2, None,
     "'I forget my lines every time!' Jose struggles to memorize the fiery chef monologue. "
     "The noun 'texte' means script or actor lines."),
    (3, None,
     "'You must just shout at your brigade.' Andrea reminds him that the director wants genuine anger. "
     "The noun 'brigade' refers to a restaurant kitchen staff."),
    (4, None,
     "'I cannot manage with Laurence.' Jose reveals that acting opposite his former flame unnerves him. "
     "The adverbial pronoun 'y' refers to the task."),
    (5, None,
     "'Are you still thinking about that story?' Andrea asks about their ancient romantic liaison. "
     "The adverb 'encore' means still or yet."),
    (6, None,
     "'We were supposed to meet at the hotel.' Jose recalls their planned rendezvous that never occurred. "
     "The imperfect verb 'devions' expresses an unfulfilled expectation."),
    (7, None,
     "'That was twenty years ago!' Andrea puts the distant past into perspective. "
     "The phrase 'il y a' means ago when used with a time span."),
    (8, None,
     "'I still feel very guilty.' Jose admits that he never forgave himself for not showing up. "
     "The adjective 'coupable' means guilty."),
    (9, None,
     "'I spoke with Laurence just earlier.' Andrea reveals that she already questioned the actress in private. "
     "The idiom 'tout a l'heure' means just earlier."),
    (10, None,
     "'What did she say about me?' Jose eagerly asks about his co-star's reaction. "
     "The interrogative phrase 'qu'est-ce que' means what."),
    (11, None,
     "'She did not go to the hotel!' Andrea reveals that Laurence also skipped the secret date. "
     "The compound past 'est allee' uses the auxiliary etre."),
    (12, None,
     "'She stood me up too?' Jose is stunned to discover their mutual failure to meet. "
     "The idiom 'poser un lapin' means to stand someone up."),
    (13, None,
     "'Yes, you are both even now!' Andrea smiles and tells him that neither holds a grudge. "
     "The adjective 'quittes' means square or even."),
]

OUTRO = (
    "Relieved to learn that Laurence stood him up twenty years ago just as he did, Jose bursts into laughter. "
    "With his guilty conscience finally cleared, the actor returns to the set with renewed confidence to command his kitchen brigade. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("jose", "Je peux enfin jouer cette scène!")
