# Authoring module for dix-pour-cent s02e03 scene 18 (cues 446-463).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-18.py --out out/dix-pour-cent/s02e03/scene-18.json

ID = "dix-pour-cent-s02e03-scene-18"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 18
TITLE = "Une rencontre embarrassante  (An Awkward Encounter)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "catherine": "emilie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "catherine": "Catherine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 446-463. Catherine arrives at the restaurant alongside a mortified Noémie, confronting Mathias, Camille, and Annick. "
    "Mathias hurriedly dismisses Noémie back to the agency, while Catherine coolly sits down and orders a coffee amid thick tension."
)

INTRO = (
    "At Le Grand Colbert restaurant, Mathias is having lunch with Camille and her mother Annick when Catherine arrives unexpectedly. "
    "A mortified Noémie stands beside her as Mathias tries to control the deeply uncomfortable situation. "
    "Listen to the scene in French first."
)

STORY = [
    ("catherine", "Annick, je présume?",
     "Annick, I presume?",
     [(452, "Annick, je présume")], ""),
    ("catherine", "Je suis Catherine Barneville.",
     "I am Catherine Barneville.",
     [(453, "Catherine Barneville")], ""),
    ("mathias", "Catherine? Qu'est-ce que tu fais là?",
     "Catherine? What are you doing here?",
     [(450, "je ne savais pas que Mathias serait là")], ""),
    ("catherine", "Je viens déjeuner avec vous tous.",
     "I came to have lunch with you all.",
     [(446, "Je viens avec toi")], ""),
    ("mathias", "Noémie, retournez au bureau, s'il vous plaît.",
     "Noémie, please return to the office.",
     [(457, "Retournez au bureau, s'il vous plaît")], ""),
    ("lea", "Très bien, je vous laisse.",
     "Very well, I will leave you.",
     [(457, "D'accord")], ""),
    ("mathias", "Ce déjeuner n'était pas prévu ainsi.",
     "This lunch was not planned this way.",
     [(451, "Je n'avais pas prévu de le voir")], ""),
    ("catherine", "Ce n'est rien, je m'assieds avec vous.",
     "It's nothing, I'll sit with you.",
     [(459, "Ne t'inquiète pas, c'est pas ta faute")], ""),
    ("mathias", "Tu veux commander à manger?",
     "Do you want to order something to eat?",
     [(460, "Vous êtes trois ? Quatre ? Pour déjeuner ?")], ""),
    ("catherine", "Non, juste un café, s'il vous plaît.",
     "No, just a coffee, please.",
     [(461, "Non... non"), (462, "Un café, s'il vous plaît")], ""),
    ("mathias", "Pourquoi tu es venue ici exactement?",
     "Why did you come here exactly?",
     [(455, "C'est à propos de Christophe Lambert")], ""),
    ("catherine", "Je voulais faire la connaissance d'Annick.",
     "I wanted to meet Annick.",
     [(453, "Enchantée. Annick Valentini")], ""),
    ("mathias", "Tu cherches à me provoquer?",
     "Are you trying to provoke me?",
     [(456, "Pardon ? Euh... non")], ""),
    ("catherine", "Pas du tout, nous sommes civilisés.",
     "Not at all, we are civilized.",
     [(458, "C'est moi qui ai proposé ce déjeuner")], ""),
    ("mathias", "Alors soyons calmes devant tout le monde.",
     "Then let's be calm in front of everyone.",
     [(459, "Ne t'inquiète pas")], ""),
    ("catherine", "Parfait. Buvons notre café.",
     "Perfect. Let's drink our coffee.",
     [(463, "Un café, voilà")], "")
]

OPENER = "Let's examine how Catherine unexpectedly joins Mathias for a family lunch."

WALK = [
    (0, None,
     "'Annick, I presume?' Catherine approaches the table with sharp confidence. "
     "The verb présumer means to presume or assume."),
    (1, None,
     "'I am Catherine Barneville.' She introduces herself formally to Mathias's former mistress. "
     "The subject pronoun je combines with the irregular present of être."),
    (2, None,
     "'Catherine? What are you doing here?' Mathias chokes on his surprise. "
     "The question phrase qu'est-ce que asks what."),
    (3, None,
     "'I came to have lunch with you all.' Catherine smiles icily. "
     "The verb venir expresses coming to a location."),
    (4, None,
     "'Noémie, please return to the office.' Mathias quickly orders his assistant away. "
     "The imperative retournez uses polite vous."),
    (5, None,
     "'Very well, I will leave you.' Noémie gladly seizes the chance to flee. "
     "The verb phrase laisser indicates leaving someone."),
    (6, None,
     "'This lunch was not planned this way.' Mathias tries to defend the arrangement. "
     "The past participle prévu comes from prévoir."),
    (7, None,
     "'It's nothing, I'll sit with you.' Catherine pulls out a chair deliberately. "
     "The reflexive verb s'asseoir means to sit down."),
    (8, None,
     "'Do you want to order something to eat?' Mathias asks nervously. "
     "The verb commander means to order in a restaurant."),
    (9, None,
     "'No, just a coffee, please.' Catherine declines food politely. "
     "The adverb juste restricts the noun café."),
    (10, None,
     "'Why did you come here exactly?' Mathias demands quietly. "
     "The compound past es venue agrees with feminine singular Catherine."),
    (11, None,
     "'I wanted to meet Annick.' Catherine explains her bold curiosity. "
     "The idiom faire la connaissance de means to make someone's acquaintance."),
    (12, None,
     "'Are you trying to provoke me?' Mathias suspects her hostile motives. "
     "The verbal locution chercher à means to seek or try to."),
    (13, None,
     "'Not at all, we are civilized.' Catherine feigns polite innocence. "
     "The adjective civilisé describes polite behavior."),
    (14, None,
     "'Then let's be calm in front of everyone.' Mathias pleads for discretion. "
     "The imperative soyons is the subjunctive imperative form of être."),
    (15, None,
     "'Perfect. Let's drink our coffee.' Catherine takes control of the table. "
     "The imperative buvons comes from boire.")
]

TRANSITION = "Now let's listen to the icy encounter at Le Grand Colbert once more."

OUTRO = (
    "With ice in the air, Catherine takes her seat opposite Annick, leaving Mathias trapped between his past and present. "
    "Listen to the scene once more in French."
)

CLOSING = ("catherine", "Parfait. Buvons notre café.")
