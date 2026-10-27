# Authoring module for dix-pour-cent s03e05 scene 25 (cues 1026-1053).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-25.py --out out/dix-pour-cent/s03e05/scene-25.json

ID = "dix-pour-cent-s03e05-scene-25"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 25
TITLE = "Payer les Américains  (Paying the Americans)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1026-1053. At the bar table, Hicham reveals his decision to pay the American insurance claim using his own capital to save ASK. "
    "Deeply moved, Andrea realizes she must immediately cancel her secret legal registration for the rival agency."
)

INTRO = (
    "At the bar table, Hicham reveals his decision to pay the American insurance claim using his own capital to save ASK. "
    "Deeply moved, Andrea realizes she must immediately cancel her secret legal registration for the rival agency. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("hicham", "Connais-tu l'histoire légendaire de Miles Davis?",
     "Do you know the legendary story of Miles Davis?",
     [(1026, "C'est mythique"), (1027, "Miles Davis")], "Recalled a famous jazz cinema anecdote"),
    ("lea", "Il composait en direct devant l'écran.",
     "He composed live in front of the screen.",
     [(1028, "devant l'écran"), (1030, "improvisé dessus")], "Recalled his spontaneous scoring process"),
    ("hicham", "Je crois que je vais payer les Américains.",
     "I think that I will pay the Americans.",
     [(1032, "payer, les Américains")], "Announced his personal financial sacrifice"),
    ("lea", "Que viens-tu de dire à l'instant?",
     "What did you just say right now?",
     [(1033, "Qu'est-ce que tu dis")], "Reacted with total astonishment"),
    ("hicham", "J'ai longuement réfléchi à la situation.",
     "I thought at length about the situation.",
     [(1034, "J'ai réfléchi")], "Affirmed his deliberate strategic choice"),
    ("hicham", "Je sauverai ASK avec mes propres fonds.",
     "I will save ASK with my own funds.",
     [(1035, "je le ferai")], "Committed his personal money to rescue ASK"),
    ("lea", "C'est une somme absolument colossale, Hicham!",
     "That is an absolutely colossal sum, Hicham!",
     [(1036, "moins facile que ce que je croyais")], "Stressed the immense financial scale"),
    ("hicham", "Je me suis sincèrement attaché à cette boîte.",
     "I have grown sincerely attached to this firm.",
     [(1037, "attaché à cette boîte")], "Confessed his genuine emotional bond to ASK"),
    ("lea", "Je suis tellement heureuse d'entendre cela.",
     "I am so happy to hear that.",
     [(1039, "bien que tu le dises")], "Expressed profound relief and gratitude"),
    ("hicham", "Nous formons une vraie équipe soudée maintenant.",
     "We form a real tight team now.",
     [(1037, "cette boîte")], "Celebrated their renewed corporate solidarity"),
    ("lea", "Je dois passer un appel urgent immédiatement.",
     "I must make an urgent call immediately.",
     [(1040, "appelles Maître Hirsch")], "Realized she must stop the lawyers"),
    ("hicham", "Tu veux téléphoner à cette heure tardive?",
     "You want to telephone at this late hour?",
     [(1042, "Maintenant")], "Questioned the late night phone call"),
    ("lea", "Oui, pour stopper un dossier très important.",
     "Yes, to stop a very important file.",
     [(1041, "avancé sur le dossier")], "Hurried to halt the rival agency paperwork"),
    ("hicham", "Prends ton temps, je règle l'addition.",
     "Take your time, I am settling the bill.",
     [(1044, "Ok")], "Offered to pay the bar tab")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Do you know the legendary story of Miles Davis?' Hicham begins with an iconic music memory. "
     "The inverted question introduces an artistic reference."),
    (1, None,
     "'He composed live in front of the screen.' Andrea recalls his legendary soundtrack improvisation. "
     "The imperfect verb describes creative cinema history."),
    (2, None,
     "'I think that I will pay the Americans.' Hicham announces his momentous personal decision. "
     "The near-future verbal phrase delivers the financial breakthrough."),
    (3, None,
     "'What did you just say right now?' Andrea can barely believe what she is hearing. "
     "The recent past construction registers her utter shock."),
    (4, None,
     "'I thought at length about the situation.' Hicham emphasizes his careful reflection. "
     "The compound past verb with the adverb signals a mature choice."),
    (5, None,
     "'I will save ASK with my own funds.' Hicham commits his private fortune to the company. "
     "The simple future verb expresses resolute determination."),
    (6, None,
     "'That is an absolutely colossal sum, Hicham!' Andrea underscores the magnitude of the payout. "
     "The intensifying adverb magnifies the enormous cost."),
    (7, None,
     "'I have grown sincerely attached to this firm.' Hicham reveals his true feelings for ASK. "
     "The pronominal compound past verb confesses unexpected company loyalty."),
    (8, None,
     "'I am so happy to hear that.' Andrea responds with genuine warmth and admiration. "
     "The predicate adjective conveys heartfelt emotional reassurance."),
    (9, None,
     "'We form a real tight team now.' Hicham celebrates their newfound unity. "
     "The descriptive adjective cements their shared executive commitment."),
    (10, None,
     "'I must make an urgent call immediately.' Andrea suddenly remembers the secret legal filing. "
     "The modal verb of obligation conveys immediate procedural panic."),
    (11, None,
     "'You want to telephone at this late hour?' Hicham wonders about her abrupt departure. "
     "The temporal phrase questions calling business contacts after midnight."),
    (12, None,
     "'Yes, to stop a very important file.' Andrea rushes to halt the legal registration. "
     "The infinitive of purpose explains her urgent intervention."),
    (13, None,
     "'Take your time, I am settling the bill.' Hicham graciously handles the drinks. "
     "The courteous imperative gives her space to make the call.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "As Hicham pledges his own fortune to rescue the agency, Andrea rushes outside to call off her secret legal plans. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("lea", "Oui, pour stopper un dossier très important.")
