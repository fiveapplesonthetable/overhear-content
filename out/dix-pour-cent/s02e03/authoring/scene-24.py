# Authoring module for dix-pour-cent s02e03 scene 24 (cues 621-641).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-24.py --out out/dix-pour-cent/s02e03/scene-24.json

ID = "dix-pour-cent-s02e03-scene-24"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 24
TITLE = "Julien veut partir  (Julien Wants to Leave)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "julien": "marcel"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel", "julien": "Julien"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 621-641. Gabriel finds Julien Doré wanting to leave the laser game lounge after arguing with Charlotte Le Bon. "
    "Gabriel encourages Sofia to talk to Julien and pitch herself for his new film project."
)

INTRO = (
    "In the lounge of the laser game center, Gabriel spots musician and filmmaker Julien Dore looking anxious to leave. "
    "After Julien admits to a creative dispute, Gabriel pushes actress Sofia Leprince to seize the moment and introduce herself. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("gabriel", "Salut Julien! Tu vas bien?",
     "Hi Julien! Are you doing well?",
     [(622, "-Salut, Julien.")], ""),
    ("julien", "Tu peux me trouver un taxi?",
     "Can you find me a taxi?",
     [(623, "Tu peux me trouver un taxi ?")], ""),
    ("gabriel", "Il y a un problème?",
     "Is there a problem?",
     [(624, "Un problème ?")], ""),
    ("julien", "Je me suis disputé avec Charlotte.",
     "I argued with Charlotte.",
     [(625, "Charlotte et moi on s'est disputés à propos du film.")], ""),
    ("julien", "Elle ne comprend pas la fin.",
     "She does not understand the ending.",
     [(626, "Elle ne comprend pas.")], ""),
    ("julien", "Je dois rentrer à Paris.",
     "I must go back to Paris.",
     [(627, "Je dois rentrer à Paris.")], ""),
    ("gabriel", "Sofia veut faire des essais.",
     "Sofia wants to do screen tests.",
     [(629, "Dis-moi si tu veux organiser des essais voix avec Sofia.")], ""),
    ("julien", "On verra ça plus tard.",
     "We will see about that later.",
     [(638, "Ça va se faire")], ""),
    ("lea", "Tu es trop lourd, Gabriel!",
     "You are too pushy, Gabriel!",
     [(631, "-T'es lourd, c'est pénible.")], ""),
    ("lea", "Il n'est pas intéressé.",
     "He is not interested.",
     [(634, "Il n'est visiblement pas intéressé par moi.")], ""),
    ("gabriel", "Arrête de t'inquiéter comme ça.",
     "Stop worrying like that.",
     [(635, "Allez, arrête de t'inquiéter !")], ""),
    ("gabriel", "Julien est toujours très stressé.",
     "Julien is always very stressed.",
     [(636, "Julien est toujours stressé")], ""),
    ("gabriel", "Tu dois tenter le coup.",
     "You must give it a shot.",
     [(638, "tu dois tenter le coup.")], ""),
    ("lea", "D'accord, je vais lui parler.",
     "All right, I will talk to him.",
     [(640, "Ah, c'est super que tu sois venu.")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'Hi Julien! Are you doing well?' Gabriel greets the visiting artist in the party lounge. "
     "The informal greeting salut is used among friends and colleagues."),
    (1, None,
     "'Can you find me a taxi?' Julien urgently asks for a ride away from the venue. "
     "The verb trouver means to find or locate."),
    (2, None,
     "'Is there a problem?' The agent senses that something went wrong with the project. "
     "The phrase il y a introduces the existence of something."),
    (3, None,
     "'I argued with Charlotte.' The musician explains the artistic disagreement with his partner. "
     "The reflexive verb se disputer indicates a verbal argument."),
    (4, None,
     "'She does not understand the ending.' Julien feels misunderstood regarding the climax of his film. "
     "The negation ne ... pas surrounds the conjugated verb comprend."),
    (5, None,
     "'I must go back to Paris.' Frustrated by the dispute, he decides to cut his visit short. "
     "The modal verb dois expresses necessity or obligation."),
    (6, None,
     "'Sofia wants to do screen tests.' Gabriel seizes the opportunity to pitch his actress client. "
     "The noun essais refers to auditions or screen tests."),
    (7, None,
     "'We will see about that later.' Julien deflects the business pitch while in a hurry. "
     "The simple future verra comes from the irregular verb voir."),
    (8, None,
     "'You are too pushy, Gabriel!' Sofia reproaches her agent for bringing up work at an awkward moment. "
     "The adjective lourd idiomatically means pushy, clumsy, or annoying."),
    (9, None,
     "'He is not interested.' She feels discouraged and doubts the singer has any interest in her. "
     "The adjective interesse describes someone who is interested."),
    (10, None,
     "'Stop worrying like that.' Gabriel urges her not to let insecurity hold her back. "
     "The imperative arrete tells someone to stop an action."),
    (11, None,
     "'Julien is always very stressed.' The agent explains that creative people often experience intense anxiety. "
     "The adverb toujours indicates habitual behavior."),
    (12, None,
     "'You must give it a shot.' Gabriel encourages his client to take advantage of the opportunity. "
     "The idiomatic phrase tenter le coup means to give it a shot or take a chance."),
    (13, None,
     "'All right, I will talk to him.' Sofia finally agrees to approach the artist directly. "
     "The near future vais parler indicates an immediate intention."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Despite her initial hesitation, Sofia gathers her courage to approach Julien Dore. "
    "Remember the colloquial French idiom for taking a chance: tenter le coup."
)

CLOSING = ("lea", "D'accord, je vais lui parler.")
