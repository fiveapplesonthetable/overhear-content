# Authoring module for dix-pour-cent s02e02 scene 26 (cues 858-895).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-26.py --out out/dix-pour-cent/s02e02/scene-26.json

ID = "dix-pour-cent-s02e02-scene-26"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 26
TITLE = "Cartes de visite et confidences  (Business Cards and Confidences)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Camille", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 858-895. At ASK, Hervé shows Camille the business cards he designed for his future "
    "promotion to junior agent. He then reveals he knows her big secret: that her father is "
    "famous actor Christophe Lambert, but he mistakenly believes she simply has a secret crush on him. "
    "Adapted for A1 French."
)

INTRO = (
    "At the agency reception, Hervé proudly shows Camille the new business cards he designed. "
    "He then drops a surprising revelation, claiming he has figured out the identity of Camille's father. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("herve", "Ta mère arrive quand?",
     "When does your mother arrive?",
     [(858, "Ta mère arrive quand ?")], ""),
    ("lea", "Elle arrive la semaine prochaine.",
     "She arrives next week.",
     [(859, "La semaine prochaine.")], "Added elle arrive"),
    ("herve", "Attends, regarde mes cartes de visite.",
     "Wait, look at my business cards.",
     [(867, "Attends, je ne t'ai pas montré."), (868, "créer des cartes de visite")], "Shortened sentence"),
    ("herve", "J'ai passé la nuit à les faire.",
     "I spent the night making them.",
     [(868, "J'ai passé toute la nuit")], "Added à les faire"),
    ("herve", "C'est pour quand je serai agent junior!",
     "It is for when I am a junior agent!",
     [(869, "pour quand Hicham me fait agent junior.")], "Adapted with future tense"),
    ("lea", "Génial! Cette couleur est plus claire.",
     "Awesome! This colour is lighter.",
     [(870, "Génial !"), (873, "Celle-ci est plus claire")], ""),
    ("herve", "Tu as raison, c'est beaucoup mieux.",
     "You are right, it is much better.",
     [(874, "T'as raison."), (873, "mieux.")], ""),
    ("lea", "Je pourrai être ton assistante.",
     "I will be able to be your assistant.",
     [(878, "je pourrai être ton assistante.")], ""),
    ("herve", "Merci, Camille. Tu es une vraie amie.",
     "Thank you, Camille. You are a true friend.",
     [(879, "Merci, Camille, c'est rare d'avoir de vrais amis")], "Adapted line"),
    ("herve", "Au fait, je sais qui est ton père.",
     "By the way, I know who your father is.",
     [(881, "Au fait..."), (882, "Je sais qui est ton père.")], ""),
    ("lea", "Ah bon? Comment tu sais ça?",
     "Really? How do you know that?",
     [(883, "Ah bon ?"), (884, "Comment ?")], "Added tu sais ça"),
    ("herve", "C'est évident, voyons!",
     "It is obvious, come on!",
     [(885, "C'est évident.")], "Added voyons"),
    ("lea", "Tu n'es pas en colère?",
     "You are not angry?",
     [(887, "Tu n'es pas... en colère.")], ""),
    ("herve", "Tout le monde a droit à ses secrets.",
     "Everyone has a right to their secrets.",
     [(888, "Tout le monde a droit à ses petits secrets.")], ""),
    ("herve", "Je voulais te le dire.",
     "I wanted to tell you.",
     [(891, "Je voulais te le dire")], ""),
    ("herve", "J'adore Christophe Lambert depuis mon enfance!",
     "I have loved Christophe Lambert since my childhood!",
     [(892, "depuis mes huit ans !")], "Clarified Christophe Lambert"),
    ("lea", "Tu es incroyable, Hervé!",
     "You are incredible, Hervé!",
     [], "Camille relieved reaction"),
]

OPENER = "Let's examine how Hervé shares his cards and his funny mistake with Camille."

WALK = [
    (0, None,
     "'When does your mother arrive?' A familiar question putting the interrogative adverb quand at the end."),
    (1, None,
     "'She arrives next week.' The present tense used with near-future temporal adverbs."),
    (2, None,
     "'Wait, look at my business cards.' Two imperative verbs in succession."),
    (3, None,
     "'I spent the night making them.' The verb passer with an object pronoun before the infinitive."),
    (4, None,
     "'It is for when I am a junior agent!' The future tense of etre in a temporal clause."),
    (5, None,
     "'Awesome! This colour is lighter.' An enthusiastic exclamation followed by a comparative adjective."),
    (6, None,
     "'You are right, it is much better.' The idiom avoir raison followed by a comparative adverb."),
    (7, None,
     "'I will be able to be your assistant.' The future tense of the modal verb pouvoir."),
    (8, None,
     "'Thank you, Camille. You are a true friend.' A sincere compliment using the adjective vrai."),
    (9, None,
     "'By the way, I know who your father is.' The introductory idiom au fait followed by an indirect question."),
    (10, None,
     "'Really? How do you know that?' A double question expressing surprise."),
    (11, None,
     "'It is obvious, come on!' The interjection voyons urging common sense."),
    (12, None,
     "'You are not angry?' A negative question inquiring about emotional reaction."),
    (13, None,
     "'Everyone has a right to their secrets.' The legal and social idiom avoir droit a."),
    (14, None,
     "'I wanted to tell you.' The imperfect tense expressing a past desire."),
    (15, None,
     "'I have loved Christophe Lambert since my childhood!' The preposition depuis expressing duration starting in the past."),
    (16, None,
     "'You are incredible, Hervé!' Camille laughs with relief at his hilarious mistake."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Hervé proudly displays his agency ambition and shares his wild theory about Camille's father. "
    "Camille is secretly relieved that her true parentage remains safe."
)

CLOSING = ("herve", "À plus tard, Camille!")
