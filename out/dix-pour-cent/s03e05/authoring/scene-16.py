# Authoring module for dix-pour-cent s03e05 scene 16 (cues 729-737).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-16.py --out overhear-content/out/dix-pour-cent/s03e05/scene-16.json

ID = "dix-pour-cent-s03e05-scene-16"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 16
TITLE = "Les préparatifs de la fête  (Party Preparations)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "valentin": "theo"}
LABELS = {"lea": "Noémie", "valentin": "Valentin"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 729-745. At the ASK reception desk, Valentin stops by to find Camille while Noémie juggles frantic logistics "
    "and deliveries for the agency's 30th anniversary celebration amidst the mounting agency crises. Adapted for A1 French."
)

INTRO = (
    "At the agency front desk, Valentin drops by hoping to catch Camille before running off to an audition. "
    "Meanwhile, Noemie manages phone calls and delivery logistics for ASK's grand thirtieth anniversary celebration. "
    "Let's listen to their exchanges in French first."
)

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
    ("valentin", "Bonjour Noémie, je cherche ma chère Camille.",
     "Hello Noemie, I am looking for my dear Camille.",
     [(730, "je vais chercher Camille")], "Looking for Camille"),
    ("lea", "Camille termine un rendez-vous dans son bureau.",
     "Camille is finishing a meeting in her office.",
     [(731, "elle est bientôt finie")], "Informing of meeting"),
    ("valentin", "D'accord, mais je dois vite partir maintenant.",
     "Alright, but I must quickly leave now.",
     [(733, "je dois filer")], "Hurrying off"),
    ("valentin", "Dis-lui que je l'embrasse très fort!",
     "Tell her that I send her big kisses!",
     [(734, "Gros bisous courage")], "Sending affection"),
    ("lea", "Oui, bon courage pour ta journée, Valentin!",
     "Yes, good luck for your day, Valentin!",
     [(734, "courage")], "Wishing luck"),
    ("lea", "Agence ASK, bonjour, j'écoute votre demande.",
     "ASK agency, hello, I am listening to your request.",
     [(738, "bonjour")], "Answering office phone"),
    ("lea", "C'est pour la fête des trente ans?",
     "Is this for the thirty-year anniversary party?",
     [(740, "la fête des 30 ans")], "Confirming event call"),
    ("lea", "Nous organisons une magnifique fête ce soir.",
     "We are organizing a magnificent party tonight.",
     [(740, "la fête")], "Describing reception"),
    ("lea", "Il n'y a pas de parking privé.",
     "There is no private parking.",
     [(741, "y'a pas de parking")], "Explaining parking limits"),
    ("lea", "Mais des places de livraison sont libres.",
     "But delivery spots are free.",
     [(741, "des places pour les livraisons")], "Noting delivery bays"),
    ("lea", "Elles se trouvent juste en bas.",
     "They are located right downstairs.",
     [(742, "Juste en bas dans la rue")], "Giving street location"),
    ("lea", "Vous pouvez déposer le matériel dans la rue.",
     "You can drop off the equipment in the street.",
     [(742, "dans la rue")], "Instructing equipment delivery"),
    ("lea", "Je vous en prie, à tout à l'heure!",
     "You are welcome, see you shortly!",
     [(743, "De rien"), (744, "Au revoir")], "Closing phone call"),
]

WALK = [
    (0, None,
     "'Hello Noemie, I am looking for my dear Camille.' Valentin stops by the reception desk. "
     "The verb 'chercher' means to look for or seek."),
    (1, None,
     "'Camille is finishing a meeting in her office.' Noemie explains that Camille is still occupied. "
     "The verb 'terminer' means to end or finish."),
    (2, None,
     "'Alright, but I must quickly leave now.' Valentin is pressed for time and cannot wait. "
     "The verb 'partir' means to leave or depart."),
    (3, None,
     "'Tell her that I send her big kisses!' Valentin leaves an affectionate message. "
     "The verb 'embrasser' means to kiss or hug."),
    (4, None,
     "'Yes, good luck for your day, Valentin!' Noemie sends warm encouragement. "
     "The noun 'courage' idiomatically wishes someone strength."),
    (5, None,
     "'ASK agency, hello, I am listening to your request.' Noemie picks up an incoming phone call. "
     "The noun 'demande' refers to a request or inquiry."),
    (6, None,
     "'Is this for the thirty-year anniversary party?' Noemie handles event logistics. "
     "The cardinal numeral 'trente' means thirty."),
    (7, None,
     "'We are organizing a magnificent party tonight.' Noemie describes the major milestone celebration. "
     "The feminine noun 'fete' denotes a formal party or celebration."),
    (8, None,
     "'There is no private parking.' Noemie warns about Parisian parking constraints. "
     "The masculine noun 'parking' denotes a car park."),
    (9, None,
     "'But delivery spots are free.' Noemie points out designated loading zones. "
     "The noun 'livraison' means delivery."),
    (10, None,
     "'They are located right downstairs.' Noemie directs the driver to the street below. "
     "The reflexive verb 'se trouver' indicates location."),
    (11, None,
     "'You can drop off the equipment in the street.' Noemie guides the delivery team. "
     "The verb 'deposer' means to drop off or unload."),
    (12, None,
     "'You are welcome, see you shortly!' Noemie concludes the logistical call politely. "
     "The temporal phrase 'a tout a l'heure' means see you soon."),
]

OUTRO = (
    "Noemie keeps the agency functioning smoothly behind the scenes while party preparations swing into gear. "
    "Even as backstage drama threatens to boil over, the grand anniversary celebration must go on. "
    "Now let's listen to the scene once more."
)

CLOSING = ("lea", "Je vous en prie, à tout à l'heure!")
