# Authoring module for dix-pour-cent s02e02 scene 19 (cues 677-692).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-19.py --out out/dix-pour-cent/s02e02/scene-19.json

ID = "dix-pour-cent-s02e02-scene-19"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 19
TITLE = "Le choix de Mathias  (The Choice of Mathias)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 677-692. Sofia realizes that keeping Gabriel as her agent complicates their romance. "
    "Together they discuss alternative agents at ASK, and Sofia decides to ask Mathias to represent her."
)

INTRO = (
    "Back at the ASK offices, Sofia and Gabriel have a candid, mature discussion about their future. "
    "Realizing that mixing love and professional representation causes unnecessary tension, Sofia looks "
    "for a new agent within ASK. Listen to their conversation in French first."
)

STORY = [
    ("lea", "Je crois que vous avez raison.",
     "I think you are right.",
     [(677, "Je crois que vous avez raison")], ""),
    ("lea", "Mélanger travail et vie sentimentale, c'est difficile.",
     "Mixing work and personal life is difficult.",
     [(678, "Mélanger travail et vie sentimentale, c'est")], ""),
    ("gabriel", "Alors vous me lâchez ou vous trouvez un nouvel agent?",
     "So are you dropping me or finding a new agent?",
     [(679, "Alors vous me lâchez ou vous trouvez un nouvel agent")], ""),
    ("lea", "Si je change d'agent, vous pouvez quand même me conseiller?",
     "If I change agents, can you still advise me?",
     [(680, "Si je change d'agent, vous pouvez quand même me conseiller")], ""),
    ("lea", "Ou m'aider discrètement?",
     "Or help me discreetly?",
     [(681, "ou m'aider discrètement")], ""),
    ("gabriel", "Bien sûr. Vous avez quelqu'un en tête? Andréa?",
     "Of course. Do you have someone in mind? Andréa?",
     [(682, "Bien sûr"), (683, "Vous avez quelqu'un en tête ? Andréa")], ""),
    ("lea", "Je ne sais pas, elle fait un peu peur.",
     "I don't know, she's a bit scary.",
     [(684, "Je ne sais pas, elle fait un peu peur")], ""),
    ("lea", "En plus c'est votre amie, c'est délicat.",
     "Besides she is your friend, it's delicate.",
     [(685, "En plus c'est votre amie, c'est délicat")], ""),
    ("gabriel", "Arlette n'est peut-être pas le bon choix pour une jeune actrice.",
     "Arlette might not be the right choice for a young actress.",
     [(686, "Arlette n'est peut-être pas le bon choix pour une jeune actrice")], ""),
    ("lea", "Même si on l'aime bien!",
     "Even if we like her!",
     [(687, "Même si on l'aime bien")], ""),
    ("lea", "Je pensais à Mathias. Parce que c'est un bon agent.",
     "I was thinking of Mathias. Because he's a good agent.",
     [(688, "Je pensais à Mathias. Parce que c'est un bon agent")], ""),
    ("lea", "Avec lui, personne ne peut dire que je bénéficie d'un traitement de faveur.",
     "With him, nobody can say I get preferential treatment.",
     [(689, "Avec lui, personne ne peut dire que je bénéficie d'un traitement de faveur")], ""),
    ("gabriel", "Je suis sûr que vous avez raison. C'est un bon choix.",
     "I'm sure you are right. It's a good choice.",
     [(690, "Je suis sûr que vous avez raison. C'est un bon choix")], ""),
    ("lea", "Oui, je crois. À tout à l'heure!",
     "Yes, I think so. See you shortly!",
     [(691, "Oui, je crois"), (692, "À tout à l'heure")], ""),
]

OPENER = "Let's examine how Sofia and Gabriel navigate this professional transition line by line."

WALK = [
    (0, None,
     "'I think you are right.' Sofia acknowledges the wisdom of separating romance from management. "
     "The phrase avoir raison means to be right."),
    (1, None,
     "'Mixing work and personal life is difficult.' She names the central conflict. "
     "The infinitive mélanger acts as the grammatical subject."),
    (2, None,
     "'So are you dropping me or finding a new agent?' Gabriel asks for clarity. "
     "The colloquial verb lâcher means to drop or let go of someone."),
    (3, None,
     "'If I change agents, can you still advise me?' Sofia seeks reassurance that Gabriel will remain close. "
     "The phrase changer de takes an indefinite complement."),
    (4, None,
     "'Or help me discreetly?' She wants his behind-the-scenes guidance. "
     "The adverb ends in the classic -ment suffix."),
    (5, None,
     "'Of course. Do you have someone in mind? Andréa?' Gabriel suggests their dynamic colleague. "
     "The idiom avoir quelqu'un en tête means to have someone in mind."),
    (6, None,
     "'I don't know, she's a bit scary.' Sofia hesitates given Andréa's fierce intensity. "
     "The expression faire peur means to be scary or intimidating."),
    (7, None,
     "'Besides she is your friend, it's delicate.' She points out the awkward overlapping friendships. "
     "The phrase en plus means moreover or besides."),
    (8, None,
     "'Arlette might not be the right choice for a young actress.' Gabriel considers generational differences. "
     "The negative structure n'est pas le bon choix expresses careful advice."),
    (9, None,
     "'Even if we like her!' Sofia adds warmly to avoid sounding dismissive. "
     "The conjunction même si introduces a concessive clause."),
    (10, None,
     "'I was thinking of Mathias. Because he's a good agent.' Sofia reveals her top candidate. "
     "The imperfect je pensais indicates thoughtful consideration."),
    (11, None,
     "'With him, nobody can say I get preferential treatment.' Mathias's strict professionalism protects her reputation. "
     "The phrase traitement de faveur means special or favored treatment."),
    (12, None,
     "'I'm sure you are right. It's a good choice.' Gabriel gracefully accepts her decision. "
     "The adjective phrase être sûr que takes the indicative."),
    (13, None,
     "'Yes, I think so. See you shortly!' Sofia wraps up their meeting with optimism. "
     "The farewell phrase à tout à l'heure means see you soon."),
]

TRANSITION = "Now let's listen to the entire conversation once more from start to finish."

OUTRO = (
    "Sofia has chosen Mathias as her new agent, creating a clear professional boundary while keeping Gabriel's love. "
    "Remember the key expression for having someone in mind: avoir quelqu'un en tête."
)

CLOSING = ("gabriel", "Je suis sûr que vous avez raison. C'est un bon choix.")
