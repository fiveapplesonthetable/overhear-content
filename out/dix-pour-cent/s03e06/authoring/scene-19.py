# Authoring module for dix-pour-cent s03e06 scene 19 (cues 978-980).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-19.py --out overhear-content/out/dix-pour-cent/s03e06/scene-19.json

ID = "dix-pour-cent-s03e06-scene-19"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 19
TITLE = "Avertissement secret  (A Secret Warning)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 978-980. In the noisy corridor during the anniversary party, Andréa pulls Mathias aside "
    "with alarming news that his key client Guillaume Canet plans to leave the agency."
)

INTRO = (
    "Amid the noisy buzz of ASK's anniversary celebration, Mathias learns alarming news about his star client Guillaume Canet. "
    "Andrea urgently pulls him aside into a quiet room to discuss the impending crisis without alerting the party. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Tais-toi, ne parle pas ici!",
     "Be quiet, do not speak here!",
     [(978, "Tais-toi pas ici")], ""),
    ("mathias", "Pourquoi me tires-tu le bras ainsi?",
     "Why are you pulling my arm like that?",
     [(971, "tu me râches le bras à moitié")], ""),
    ("lea", "Il y a un très gros problème.",
     "There is a very big problem.",
     [(979, "Il y a grand amendeur")], ""),
    ("mathias", "Qu'est-ce qui se passe encore?",
     "What is going on now?",
     [(973, "Quoi")], ""),
    ("lea", "Guillaume Canet ne viendra pas ce soir.",
     "Guillaume Canet will not come tonight.",
     [(969, "Guillaume Canet ne viendra pas ce soir")], ""),
    ("mathias", "Je sais, il tourne en Ukraine.",
     "I know, he is filming in Ukraine.",
     [(970, "il tourne en Ukraine")], ""),
    ("lea", "Non, il veut quitter notre agence!",
     "No, he wants to leave our agency!",
     [(972, "Il veut quitter l'agence")], ""),
    ("mathias", "Mais d'où tiens-tu cette folie?",
     "Where do you get this madness?",
     [(974, "d'où tu tiens ça")], ""),
    ("lea", "J'ai d'excellentes sources bien informées.",
     "I have excellent, well-informed sources.",
     [(975, "J'ai mes sources")], ""),
    ("mathias", "Guillaume est mon client le plus fidèle.",
     "Guillaume is my most loyal client.",
     [(976, "Guillaume est mon client")], ""),
    ("lea", "Une agence rivale lui fait les yeux doux.",
     "A rival agency is courting him.",
     [(972, "quitter l'agence")], ""),
    ("mathias", "C'est un véritable coup de poignard!",
     "That is a real stab in the back!",
     [(977, "S'il voulait quitter")], ""),
    ("lea", "Viens, il faut qu'on parle discrètement.",
     "Come, we must speak discreetly.",
     [(979, "il faut qu'on parle"), (980, "Viens")], ""),
    ("mathias", "Allons tout de suite dans mon bureau.",
     "Let us go to my office right away.",
     [(980, "Viens")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Be quiet, do not speak here!' Andrea hushes Mathias in the middle of the party. "
     "The imperative verb warns him to maintain secrecy."),
    (1, None,
     "'Why are you pulling my arm like that?' Mathias wonders why she is acting so frantically. "
     "The interrogative sentence reflects annoyance."),
    (2, None,
     "'There is a very big problem.' Andrea delivers a grave warning about agency stability. "
     "The short sentence signals impending danger."),
    (3, None,
     "'What is going on now?' Mathias asks what latest catastrophe has hit ASK. "
     "The informal phrase conveys mounting exhaustion."),
    (4, None,
     "'Guillaume Canet will not come tonight.' She reveals the unexpected absence of their star client. "
     "The future negation raises an alarm."),
    (5, None,
     "'I know, he is filming in Ukraine.' Mathias tries to brush aside her worry with an alibi. "
     "The present tense provides a harmless excuse."),
    (6, None,
     "'No, he wants to leave our agency!' Andrea drops the bombshell regarding his client's departure. "
     "The exclamation reveals devastating news."),
    (7, None,
     "'Where do you get this madness?' Mathias refuses to believe the shocking rumor. "
     "The interrogative phrase questions her intelligence."),
    (8, None,
     "'I have excellent, well-informed sources.' She insists her insider information is solid. "
     "The noun phrase defends her credibility."),
    (9, None,
     "'Guillaume is my most loyal client.' Mathias proudly defends his special bond with the actor. "
     "The superlative adjective expresses trust."),
    (10, None,
     "'A rival agency is courting him.' Andrea warns that competitors are circling their top talent. "
     "The idiom describes aggressive poaching."),
    (11, None,
     "'That is a real stab in the back!' Mathias reacts with outrage at the prospect of betrayal. "
     "The dramatic metaphor highlights the stakes."),
    (12, None,
     "'Come, we must speak discreetly.' Andrea pulls him away from listening ears. "
     "The imperative verb initiates a confidential retreat."),
    (13, None,
     "'Let us go to my office right away.' Mathias agrees to plan their defense in private. "
     "The adverbial phrase emphasizes urgency.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Threatened with the loss of their top star, Andrea and Mathias unite to protect ASK from outside predators. "
    "Listen to the conversation once more in French."
)

CLOSING = ("mathias", "Nous devons sauver ce contrat capital.")
