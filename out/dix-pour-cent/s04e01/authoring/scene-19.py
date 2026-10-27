# Authoring module for dix-pour-cent s04e01 scene 19 (cues 898-906).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-19.py --out out/dix-pour-cent/s04e01/scene-19.json

ID = "dix-pour-cent-s04e01-scene-19"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 19
TITLE = "La robe de Noémie  (Noémie's Dress)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 898-906. Arriving at the Césars, Noémie worries about her flashy dress while Mathias tries to comfort her, "
    "but the mood turns bitter when an acquaintance dismissively calls Noémie his little assistant."
)

INTRO = (
    "Arriving at the Cesars ceremony, Noemie feels anxious about her striking outfit. "
    "While Mathias tries to reassure her, an acquaintance greets them and patronizingly refers to Noemie as his little assistant, leaving her hurt. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("mathias", "Alors, trouvons nos places, par ici.",
     "So, let us find our seats, over here.",
     [(898, "Par là, c'est ça")], "Mathias leads the way inside"),
    ("lea", "Attends, Mathias, ma robe est catastrophique!",
     "Wait, Mathias, my dress is a disaster!",
     [(899, "ma robe est catastrophique")], "Noemie panics over her look"),
    ("mathias", "Mais non, ta robe est magnifique.",
     "Not at all, your dress is stunning.",
     [(900, "ta robe est magnifique")], "Mathias compliments her sincerely"),
    ("lea", "C'est trop tape-à-l'œil!",
     "It is too flashy!",
     [(901, "trop tape-à-l'œil")], "Noemie worries about being judged"),
    ("mathias", "Tu es élégante et très lumineuse.",
     "You are elegant and very radiant.",
     [(900, "crois-moi")], "Mathias attempts to bolster her confidence"),
    ("lea", "Une amie arrive vers nous, regarde.",
     "A friend is coming toward us, look.",
     [(901, "Bonjour")], "Noemie spots an industry acquaintance"),
    ("mathias", "Bonjour Mathilde, comment vas-tu ce soir?",
     "Hello Mathilde, how are you tonight?",
     [(902, "Bonjour, Mathilde")], "Mathias exchanges greetings"),
    ("lea", "Elle m'a appelée ta petite assistante!",
     "She called me your little assistant!",
     [(903, "ta petite assistante")], "Noemie feels deeply slighted"),
    ("mathias", "Je n'ai pas pu la corriger.",
     "I was not able to correct her.",
     [(904, "pas pu la corriger")], "Mathias makes an awkward excuse"),
    ("lea", "Tu aurais dû défendre mon statut.",
     "You should have defended my status.",
     [(904, "la corriger")], "Noemie calls out his passivity"),
    ("mathias", "Je suis désolé pour ce mot.",
     "I am sorry for that word.",
     [(904, "Désolée")], "Mathias apologizes awkwardly"),
    ("lea", "Ce milieu reste cruel avec moi.",
     "This circle remains cruel to me.",
     [(904, "Désolée")], "Noemie vents her frustration"),
    ("mathias", "Nos deux sièges sont juste ici.",
     "Our two seats are right here.",
     [(906, "Ces deux places là")], "Mathias redirects focus to seating"),
    ("lea", "Asseyons-nous pour regarder la cérémonie.",
     "Let us sit down to watch the ceremony.",
     [(905, "c'est par ici")], "Noemie takes her seat quietly")
]

WALK = [
    (0, None,
     "'So, let us find our seats, over here.' Mathias navigates the busy foyer. "
     "The imperative 'trouvons' suggests moving to locate their reserved spots."),
    (1, None,
     "'Wait, Mathias, my dress is a disaster!' Noemie is struck by sudden insecurity. "
     "The adjective 'catastrophique' expresses acute dramatic distress."),
    (2, None,
     "'Not at all, your dress is stunning.' Mathias counters her worry with praise. "
     "The phrase 'mais non' softly contradicts a negative claim."),
    (3, None,
     "'It is too flashy!' Noemie fears looking conspicuous among celebrities. "
     "The idiomatic adjective 'tape-a-l'oeil' means flashy or gaudy."),
    (4, None,
     "'You are elegant and very radiant.' Mathias praises her graceful appearance. "
     "The adjective 'lumineuse' denotes glowing, bright beauty."),
    (5, None,
     "'A friend is coming toward us, look.' Noemie notes an approaching guest. "
     "The preposition 'vers' indicates movement toward a person."),
    (6, None,
     "'Hello Mathilde, how are you tonight?' Mathias welcomes an old associate. "
     "The greeting 'comment vas-tu' asks about someone's well-being."),
    (7, None,
     "'She called me your little assistant!' Noemie expresses righteous resentment. "
     "The compound past verb 'a appelee' recounts the condescending remark."),
    (8, None,
     "'I was not able to correct her.' Mathias defends his hesitation in the moment. "
     "The verb 'corriger' means to set the record straight."),
    (9, None,
     "'You should have defended my status.' Noemie demands proper professional recognition. "
     "The conditional 'aurais du' indicates an unfulfilled obligation."),
    (10, None,
     "'I am sorry for that word.' Mathias recognizes her genuine hurt. "
     "The adjective 'desole' expresses regret and empathy."),
    (11, None,
     "'This circle remains cruel to me.' Noemie laments the snobbish film elite. "
     "The noun 'milieu' refers to a social or professional environment."),
    (12, None,
     "'Our two seats are right here.' Mathias finds their numbered row. "
     "The noun 'sieges' refers to theater seats."),
    (13, None,
     "'Let us sit down to watch the ceremony.' Noemie prepares for the evening program. "
     "The reflexive imperative 'asseyons-nous' invites both of them to sit.")
]

OUTRO = (
    "Swallowing her hurt pride, Noemie takes her seat beside Mathias in the glamorous hall. "
    "Though surrounded by Parisian cinema royalty, the sting of being belittled lingers beneath the surface. "
    "Now let's listen to the scene one last time in French."
)

CLOSING = ("lea", "Asseyons-nous pour regarder la cérémonie.")
