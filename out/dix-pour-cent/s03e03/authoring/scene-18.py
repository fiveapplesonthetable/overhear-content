# Authoring module for dix-pour-cent s03e03 scene 18 (cues 1085-1189).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-18.py --out out/dix-pour-cent/s03e03/scene-18.json

ID = "dix-pour-cent-s03e03-scene-18"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 18
TITLE = "L'échec de Julien Doré  (Julien Doré's Flop)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "julien": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Sofia", "julien": "Julien", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1085-1189. In a bar, Julien Doré discovers disastrous box office numbers for his film. "
    "Sofia reveals that Gabriel sabotaged France 2's financing. Julien is shocked, but then realizes "
    "that losing the mainstream money gave him full artistic freedom."
)

INTRO = (
    "At a Parisian bistro, director Julien Dore despairs over the terrible premiere numbers for his independent movie. "
    "When Sofia angrily exposes Gabriel's secret scheme that wrecked their network funding, an explosive argument turns into an unexpected moment of artistic gratitude. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("julien", "Les chiffres du film sont catastrophiques.",
     "The film's numbers are catastrophic.",
     [(1090, "avoir les chiffres de mon film")], "Julien reports the grim box office report"),
    ("julien", "Même ma famille n'est pas venue!",
     "Even my family did not come!",
     [(1103, "ma propre famille n'a pas été voir le film")], "Julien laments the lack of local support"),
    ("gabriel", "Ce film va devenir culte!",
     "This film will become a cult classic!",
     [(1115, "sont devenus cultes")], "Gabriel tries to maintain an optimistic outlook"),
    ("lea", "Nous avons manqué d'argent partout!",
     "We lacked money everywhere!",
     [(1125, "on s'en fout pas des millions")], "Sofia complains about the impoverished shoot"),
    ("lea", "Nous avions une peluche de blaireau.",
     "We had a stuffed badger toy.",
     [(1136, "On a pris une peluche")], "Sofia mocks the cheap production compromises"),
    ("julien", "C'est un véritable chef-d'œuvre artistique!",
     "It is a true artistic masterpiece!",
     [(1122, "l'heure absolue")], "Julien passionately defends his creative vision"),
    ("lea", "Gabriel a fait fuir la télévision.",
     "Gabriel scared away the television network.",
     [(1148, "la meuf de France 2")], "Sofia reveals Gabriel's hidden interference"),
    ("julien", "Gabriel, de quoi parle-t-elle exactement?",
     "Gabriel, what is she talking about exactly?",
     [(1147, "De quoi elle parle ?")], "Julien demands an immediate explanation"),
    ("gabriel", "J'ai inventé une histoire folle.",
     "I invented a crazy story.",
     [(1157, "J'ai raconté n'importe quoi")], "Gabriel confesses his sabotage scheme"),
    ("gabriel", "Je voulais garder Julien avec moi.",
     "I wanted to keep Julien with me.",
     [(1158, "pour pas que tu partais avec elle")], "Gabriel admits his possessive motive"),
    ("julien", "C'est totalement impardonnable, Gabriel!",
     "That is totally unforgivable, Gabriel!",
     [(1168, "C'est impardonnable")], "Julien explodes in initial indignation"),
    ("julien", "Mais c'est aussi un coup génial!",
     "But that is also a stroke of genius!",
     [(1172, "c'est génial aussi")], "Julien suddenly reconsiders the artistic outcome"),
    ("julien", "Grâce à toi, je suis libre!",
     "Thanks to you, I am free!",
     [(1180, "plus libre, quoi")], "Julien embraces the uncompromising result"),
    ("lea", "Vous êtes complètement fous tous les deux!",
     "You are both completely crazy!",
     [(1189, "N'importe quoi")], "Sofia throws up her hands in utter disbelief")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'The film's numbers are catastrophic.' Julien shares the disappointing ticket sales. "
     "The descriptive adjective conveys commercial failure."),
    (1, None,
     "'Even my family did not come!' Julien laments that his own kin stayed away. "
     "The negative compound past verb highlights his personal sting."),
    (2, None,
     "'This film will become a cult classic!' Gabriel attempts to cheer up his director. "
     "The near future verb predicts long-term artistic veneration."),
    (3, None,
     "'We lacked money everywhere!' Sofia vents about extreme budgetary constraints. "
     "The compound past verb of lacking recalls the shoestring production."),
    (4, None,
     "'We had a stuffed badger toy.' Sofia cites an absurd on-set cost cutting measure. "
     "The imperfect verb recalls a ridiculous prop replacement."),
    (5, None,
     "'It is a true artistic masterpiece!' Julien refuses to measure success in ticket sales. "
     "The emphatic noun phrase affirms his uncompromising pride."),
    (6, None,
     "'Gabriel scared away the television network.' Sofia reveals the truth behind lost funds. "
     "The causative verbal phrase attributes the financing failure to Gabriel."),
    (7, None,
     "'Gabriel, what is she talking about exactly?' Julien turns to his agent in shock. "
     "The interrogative inversion demands an immediate accounting of the facts."),
    (8, None,
     "'I invented a crazy story.' Gabriel confesses his wild fabrication to the broadcaster. "
     "The compound past verb admits intentional interference."),
    (9, None,
     "'I wanted to keep Julien with me.' Gabriel reveals his possessive fear of losing his star. "
     "The imperfect modal verb explains his selfish motivation."),
    (10, None,
     "'That is totally unforgivable, Gabriel!' Julien initially reacts with righteous anger. "
     "The predicate adjective condemns the agent's duplicity."),
    (11, None,
     "'But that is also a stroke of genius!' Julien experiences a sudden creative epiphany. "
     "The approving colloquial idiom reframes the disaster into artistic blessing."),
    (12, None,
     "'Thanks to you, I am free!' Julien embraces total creative autonomy. "
     "The causal prepositional phrase expresses unexpected liberation."),
    (13, None,
     "'You are both completely crazy!' Sofia marvels at their sudden mutual affection. "
     "The plural adjective captures her sheer bewilderment.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "Turning a catastrophic box office flop into an artistic victory, Julien Dore embraces Gabriel for inadvertently preserving his creative freedom. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("lea", "Vous êtes complètement fous tous les deux!")
