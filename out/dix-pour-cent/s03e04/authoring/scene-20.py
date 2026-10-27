# Authoring module for dix-pour-cent s03e04 scene 20 (cues 935-1116).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-20.py --out out/dix-pour-cent/s03e04/scene-20.json

ID = "dix-pour-cent-s03e04-scene-20"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 20
TITLE = "La déclaration de naissance  (The Birth Declaration)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 935-1116. At the maternity clinic, Hicham brings a teddy bear for the newborn baby. "
    "When the civil registrar arrives to complete the birth certificate, Andrea declares the child fatherless, sparking an intense clash with Hicham."
)

INTRO = (
    "At the maternity clinic, Hicham brings a teddy bear for the newborn baby. "
    "When the civil registrar arrives to complete the birth certificate, Andrea declares the child fatherless, sparking an intense clash with Hicham. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Merci pour le petit ours en peluche.",
     "Thank you for the little teddy bear.",
     [(935, "Merci pour le petit ours")], "Thanked him for the plush gift"),
    ("hicham", "C'est un cadeau pour notre fille.",
     "It is a gift for our daughter.",
     [(935, "petit ours")], "Presented the gift with paternal pride"),
    ("lea", "L'officier d'état civil vient d'arriver.",
     "The civil registrar has just arrived.",
     [(938, "l'officier d'état civil")], "Announced the registrar arrival"),
    ("hicham", "Il vient pour la déclaration de naissance?",
     "Is he coming for the birth declaration?",
     [(939, "déclaration de naissance")], "Asked about the official formality"),
    ("lea", "Oui, nous devons donner nos noms officiels.",
     "Yes, we must give our official names.",
     [(944, "Nom de la mère")], "Confirmed the administrative process"),
    ("hicham", "Mon nom de famille est Janowski.",
     "My family name is Janowski.",
     [(949, "Janowski")], "Stated his surname proudly"),
    ("lea", "Non Hicham, j'indique sans père.",
     "No Hicham, I am indicating without father.",
     [(950, "Sans père")], "Refused to name a legal father"),
    ("hicham", "Comment oses-tu dire une chose pareille?",
     "How dare you say such a thing?",
     [(950, "Sans père")], "Reacted with fierce outrage"),
    ("lea", "J'en ai longuement discuté avec Colette.",
     "I discussed it at great length with Colette.",
     [(955, "On en a très longuement discuté avec Colette")], "Cited prior agreement with her partner"),
    ("hicham", "Mais je suis le père biologique!",
     "But I am the biological father!",
     [(949, "Janowski")], "Asserted his biological paternity"),
    ("lea", "Colette et moi formons sa famille.",
     "Colette and I form her family.",
     [(955, "avec Colette")], "Defined their established family unit"),
    ("hicham", "Je refuse d'être rayé de sa vie.",
     "I refuse to be erased from her life.",
     [(950, "Sans père")], "Vowed to remain part of her future"),
    ("lea", "Tu garderas toujours une place importante.",
     "You will always keep an important place.",
     [(965, "Et tu seras important pour elle")], "Reassured him of his enduring bond"),
    ("hicham", "J'ai besoin de temps pour digérer cela.",
     "I need time to process that.",
     [(965, "important pour elle")], "Expressed lingering emotional shock")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Thank you for the little teddy bear.' Andrea expresses genuine appreciation for the gift. "
     "The courteous formula opens the conversation warmly."),
    (1, None,
     "'It is a gift for our daughter.' Hicham proudly refers to the new baby. "
     "The possessive adjective establishes his emotional investment."),
    (2, None,
     "'The civil registrar has just arrived.' Andrea introduces the municipal official into the room. "
     "The compound past verb signals the start of the legal procedure."),
    (3, None,
     "'Is he coming for the birth declaration?' Hicham inquires about the administrative paperwork. "
     "The prepositional phrase names the mandatory registration process."),
    (4, None,
     "'Yes, we must give our official names.' Andrea confirms the statutory procedure. "
     "The modal verb of obligation highlights the legal requirement."),
    (5, None,
     "'My family name is Janowski.' Hicham announces his identity to the registrar. "
     "The noun phrase declares his paternal surname."),
    (6, None,
     "'No Hicham, I am indicating without father.' Andrea delivers a stunning unilateral decision. "
     "The prepositional phrase legally excludes him from the certificate."),
    (7, None,
     "'How dare you say such a thing?' Hicham is deeply wounded by her statement. "
     "The interrogative idiom expresses profound disbelief and hurt."),
    (8, None,
     "'I discussed it at great length with Colette.' Andrea stands firmly by their joint decision. "
     "The adverbial structure emphasizes careful premeditation."),
    (9, None,
     "'But I am the biological father!' Hicham insists on his fundamental parental reality. "
     "The emphatic noun phrase defends his biological identity."),
    (10, None,
     "'Colette and I form her family.' Andrea asserts her domestic reality with Colette. "
     "The transitive verb defines the two mothers as the primary household."),
    (11, None,
     "'I refuse to be erased from her life.' Hicham protests against being sidelined as a parent. "
     "The passive infinitive rejects bureaucratic erasure."),
    (12, None,
     "'You will always keep an important place.' Andrea reassures him of his personal significance. "
     "The future tense verb promises ongoing presence without legal custody."),
    (13, None,
     "'I need time to process that.' Hicham struggles to accept the painful boundary. "
     "The verbal idiom with the verb expresses necessary emotional time.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "In the hospital room, Andrea and Hicham confront the delicate boundaries between biological fatherhood and family law. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("lea", "Tu garderas toujours une place importante.")
