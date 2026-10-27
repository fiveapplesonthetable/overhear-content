# Authoring module for dix-pour-cent s03e05 scene 10 (cues 351-383).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-10.py --out out/dix-pour-cent/s03e05/scene-10.json

ID = "dix-pour-cent-s03e05-scene-10"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 10
TITLE = "Réunion de crise  (Crisis Meeting)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 351-383. At ASK, Andrea convenes an urgent meeting where Mathias and Hicham "
               "clash over who should negotiate with the movie producers. Adapted for A1 French.")

INTRO = ("In the ASK conference room, Andrea calls a crisis meeting to address Beatrice's walkout. "
         "Both Mathias and Hicham argue over who is best equipped to negotiate with the demanding producers. "
         "Let's listen to their confrontation in French first.")

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
 ("lea", "Réunion de crise pour le film de Béatrice.",
  "Crisis meeting for Beatrice's film.",
  [(351, "Ok, réunion de crise sur le hyper guette")], "Convening meeting"),
 ("lea", "Je veux du concret et des solutions.",
  "I want concrete ideas and solutions.",
  [(352, "Je veux du précis, je veux du concret, je vous écoute")], "Demanding action"),
 ("mathias", "L'épreuve de force va être très rude.",
  "The power struggle will be very tough.",
  [(364, "On sait que l'épreuve de force va être difficile")], "Assessing standoff"),
 ("mathias", "Il faut envoyer notre meilleur négociateur.",
  "We must send our best negotiator.",
  [(365, "Donc il faut envoyer le meilleur d'entre nous au casse-pipe")], "Suggesting strategy"),
 ("mathias", "C'est pour cela que je dois y aller.",
  "That is why I must go.",
  [(366, "C'est pour ça que j'ai pensé qu'il fallait que ça soit moi")], "Offering himself"),
 ("hicham", "Pardon? Qui a décidé ce classement?",
  "Excuse me? Who decided this ranking?",
  [(367, "Pardon ?"), (369, "Mais il y a un classement officiel ?")], "Challenging hierarchy"),
 ("mathias", "J'ai vingt ans d'expérience juridique.",
  "I have twenty years of legal experience.",
  [(374, "Moi j'ai l'expérience, l'expertise juridique")], "Listing legal expertise"),
 ("mathias", "Et je sais parfaitement bien bluffer.",
  "And I know perfectly well how to bluff.",
  [(375, "Et je sais très bien bluffer")], "Claiming bluffing skill"),
 ("hicham", "Moi, j'ai bâti ma fortune rapidement.",
  "I built my fortune quickly.",
  [(376, "Et moi j'ai fait fortune en moins de 10 ans")], "Listing business success"),
 ("hicham", "Et je joue au poker tous les mardis.",
  "And I play poker every Tuesday.",
  [(378, "Et je joue au poker tous les mardis soir")], "Citing poker game"),
 ("hicham", "C'est moi qui vais gérer ce producteur.",
  "I am the one who will handle this producer.",
  [(379, "Donc je pense que c'est moi qui vais y aller")], "Declaring leadership"),
 ("lea", "Très bien, Hicham, vas-y alors.",
  "Very well, Hicham, go ahead then.",
  [(380, "Tu voudras")], "Accepting Hicham"),
 ("mathias", "Mais laisse-moi te briefer avant de partir.",
  "But let me brief you before leaving.",
  [(383, "Mais tu me laisseras te briefer un peu avant d'y aller")], "Offering briefing"),
 ("hicham", "D'accord pour un brief rapide de dix minutes.",
  "Agreed for a quick ten-minute briefing.",
  [(383, "Mais tu me laisseras te briefer un peu avant d'y aller")], "Agreeing to brief"),
]

WALK = [
 (0, None,
  "'Crisis meeting for Beatrice's film.' Andrea convenes the emergency meeting. "
  "The noun phrase 'reunion de crise' designates an urgent conference."),
 (1, None,
  "'I want concrete ideas and solutions.' Andrea demands practical action. "
  "The adjective 'concret' describes practical proposals."),
 (2, None,
  "'The power struggle will be very tough.' Mathias assesses the intense standoff. "
  "The compound noun 'epreuve de force' means showdown or trial of strength."),
 (3, None,
  "'We must send our best negotiator.' Mathias emphasizes the stakes. "
  "The superlative 'notre meilleur negociateur' designates the top advocate."),
 (4, None,
  "'That is why I must go.' Mathias volunteers himself as chief negotiator. "
  "The modal verb 'devoir' conveys duty."),
 (5, None,
  "'Excuse me? Who decided this ranking?' Hicham challenges Mathias's claim. "
  "The masculine noun 'classement' denotes a hierarchy or ranking."),
 (6, None,
  "'I have twenty years of legal experience.' Mathias lists his professional credentials. "
  "The adjective 'juridique' relates to law."),
 (7, None,
  "'And I know perfectly well how to bluff.' Mathias boasts of negotiation prowess. "
  "The verb 'bluffer' means to bluff in negotiations or poker."),
 (8, None,
  "'I built my fortune quickly.' Hicham asserts his business authority. "
  "The noun 'fortune' refers to wealth."),
 (9, None,
  "'And I play poker every Tuesday.' Hicham cites his weekly card game. "
  "The noun 'poker' refers to the card game."),
 (10, None,
  "'I am the one who will handle this producer.' Hicham claims the mission. "
  "The emphatic construction 'c'est moi qui' highlights the agent."),
 (11, None,
  "'Very well, Hicham, go ahead then.' Andrea yields to Hicham's determination. "
  "The imperative 'vas-y' grants permission."),
 (12, None,
  "'But let me brief you before leaving.' Mathias insists on providing tactical advice. "
  "The borrowed verb 'briefer' means to give instructions."),
 (13, None,
  "'Agreed for a quick ten-minute briefing.' Hicham accepts the preparation time. "
  "The adjective 'rapide' modifies the brief."),
]

OUTRO = ("Hicham prepares to face the furious production team with Mathias's strategic notes in hand. "
         "Whether his aggressive poker style will succeed in the film world is about to be tested. "
         "Now, let's review the scene once more.")

CLOSING = ("hicham", "C'est moi qui vais gérer ce producteur.")
