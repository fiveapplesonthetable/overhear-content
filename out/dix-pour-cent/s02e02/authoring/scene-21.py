# Authoring module for dix-pour-cent s02e02 scene 21 (cues 710-758).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-21.py --out out/dix-pour-cent/s02e02/scene-21.json

ID = "dix-pour-cent-s02e02-scene-21"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 21
TITLE = "Visite surprise de Christophe Lambert  (Surprise Visit from Christophe Lambert)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "christophe": "theo", "mathias": "marcel"}
LABELS = {"lea": "Noémie", "christophe": "Christophe", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 710-758. Actor Christophe Lambert arrives at the ASK agency. "
    "Noémie is completely starstruck and asks for a selfie, before Mathias takes him into an office to discuss a new film role."
)

INTRO = (
    "Celebrated actor Christophe Lambert pays an unexpected visit to the ASK agency. "
    "Receptionist and assistant Noemie Leclerc is starstruck and eagerly asks for a commemorative photograph before Mathias whisks him into an office. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Oh mon Dieu, c'est Christophe Lambert!",
     "Oh my goodness, it is Christophe Lambert!",
     [(718, "Oh mon Dieu")], ""),
    ("christophe", "Bonjour Noémie! Comment tu vas?",
     "Hello Noemie! How are you doing?",
     [(714, "Noémie ! Comment tu vas ?")], ""),
    ("lea", "Je vais très bien, merci beaucoup.",
     "I am doing very well, thank you very much.",
     [(721, "-Tu es très émotive. -Oui")], ""),
    ("lea", "Je peux prendre une photo avec vous?",
     "Can I take a photo with you?",
     [(722, "Je peux prendre une photo ?")], ""),
    ("christophe", "Oui, pas de problème avec plaisir!",
     "Yes, no problem with pleasure!",
     [(723, "Oui !"), (725, "Pas de problème")], ""),
    ("lea", "Je suis une très grande fan.",
     "I am a very big fan.",
     [(726, "je suis fan de vous")], ""),
    ("christophe", "Moi aussi, je suis très sympa.",
     "Me too, I am very friendly.",
     [(727, "Moi aussi je suis timide, mais je suis sympa")], ""),
    ("lea", "Mettez-vous plus près. Grand sourire!",
     "Get closer. Big smile!",
     [(728, "Plus près"), (729, "Voilà. Grand sourire")], ""),
    ("mathias", "Salut Christophe! Viens par ici.",
     "Hi Christophe! Come this way.",
     [(731, "-Salut, Christophe"), (734, "-Par ici")], ""),
    ("christophe", "Mathias! C'est un plaisir de te voir.",
     "Mathias! It is a pleasure to see you.",
     [(731, "-Mathias !"), (732, "-Comment tu vas ? -Bien")], ""),
    ("mathias", "Le réalisateur te veut pour ce rôle.",
     "The director wants you for this role.",
     [(736, "Il te veut pour le rôle")], ""),
    ("mathias", "Lis le scénario ce soir.",
     "Read the script tonight.",
     [(741, "Lis le scénario")], ""),
    ("christophe", "D'accord, je vais le lire rapidement.",
     "All right, I will read it quickly.",
     [(743, "Ouais, bien sûr")], ""),
    ("christophe", "À tout à l'heure Mathias. Au revoir!",
     "See you later Mathias. Goodbye!",
     [(752, "À tout à l'heure, Mathias !"), (754, "Au revoir")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'Oh my goodness, it is Christophe Lambert!' Noemie is astonished to see the famous film star walk into the lobby. "
     "The phrase oh mon Dieu expresses sudden shock or delight."),
    (1, None,
     "'Hello Noemie! How are you doing?' Christophe warmly greets her by name with relaxed charm. "
     "The question comment tu vas is an informal greeting used among acquaintances."),
    (2, None,
     "'I am doing very well, thank you very much.' She responds politely while trying to hide her excitement. "
     "The adverb phrase tres bien indicates feeling great."),
    (3, None,
     "'Can I take a photo with you?' She gathers her courage to ask for a souvenir snapshot. "
     "The modal verb peux asks for polite permission."),
    (4, None,
     "'Yes, no problem with pleasure!' Christophe is gracious and happy to grant her request. "
     "The expression pas de probleme reassures someone completely."),
    (5, None,
     "'I am a very big fan.' She confesses her longstanding admiration for his filmography. "
     "The adjective grande emphasizes her deep enthusiasm."),
    (6, None,
     "'Me too, I am very friendly.' He jokes playfully to put the nervous assistant at ease. "
     "The adverb phrase moi aussi adds a friendly humorous touch."),
    (7, None,
     "'Get closer. Big smile!' She prepares the smartphone camera for the picture. "
     "The imperative mettez-vous instructs him where to stand."),
    (8, None,
     "'Hi Christophe! Come this way.' Mathias steps out of his office to welcome his high-profile client. "
     "The imperative viens invites someone to follow."),
    (9, None,
     "'Mathias! It is a pleasure to see you.' The actor greets his agent with genuine warmth. "
     "The phrase c'est un plaisir expresses polite enthusiasm."),
    (10, None,
     "'The director wants you for this role.' Mathias pitches an exciting new film offer right away. "
     "The direct object pronoun te comes before the conjugated verb."),
    (11, None,
     "'Read the script tonight.' The agent encourages him to evaluate the material without delay. "
     "The imperative form lis gives a direct instruction."),
    (12, None,
     "'All right, I will read it quickly.' Christophe agrees to look through the project immediately. "
     "The near future structure vais lire expresses immediate intention."),
    (13, None,
     "'See you later Mathias. Goodbye!' He wraps up the visit on an upbeat note before leaving. "
     "The phrase a tout a l'heure means see you shortly."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Christophe Lambert charms the ASK office before heading off to read his new movie script. "
    "Remember the classic phrase for asking permission: je peux followed by an infinitive."
)

CLOSING = ("christophe", "À tout à l'heure Mathias. Au revoir!")
