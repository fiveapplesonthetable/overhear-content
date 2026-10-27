# Authoring module for dix-pour-cent s02e04 scene 23 (cues 640-675).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-23.py --out out/dix-pour-cent/s02e04/scene-23.json

ID = "dix-pour-cent-s02e04-scene-23"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 23
TITLE = "Les conseils d'Arlette  (Arlette's Advice)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Arlette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 640-675. Gabriel speaks with senior agent Arlette about his growing jealousy over Sofia's collaboration "
    "with director Julien Doré. Arlette gives him wise advice about love and artistic freedom."
)

INTRO = (
    "In Gabriel's quiet office, senior agent Arlette Azemar checks in on her colleague as he wrestles with private doubts. "
    "Confessing his jealousy over Sofia's new artistic project with Julien Dore, Gabriel receives wise and reassuring advice from the veteran agent. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Tu vas bien, mon cher Gabriel?",
     "Are you doing well, my dear Gabriel?",
     [(640, "Ça va ?")], ""),
    ("gabriel", "C'est super pour le film de Sofia.",
     "It is great for Sofia's movie.",
     [(641, "C'est super pour Sofia.")], ""),
    ("lea", "Depuis leur rencontre, Sofia est rayonnante.",
     "Since their meeting, Sofia is radiant.",
     [(643, "mais depuis que vous êtes ensemble,"), (644, "Sofia est rayonnante.")], ""),
    ("gabriel", "Je crois que je suis jaloux!",
     "I think that I am jealous!",
     [(648, "Je crois que je suis jaloux !")], ""),
    ("gabriel", "Je ne suis plus si sûr.",
     "I am no longer so sure.",
     [(652, "Je suis pas si sûr de ce film.")], ""),
    ("gabriel", "Le scénario est un peu vulgaire.",
     "The script is a bit vulgar.",
     [(653, "C'est un peu vulgaire.")], ""),
    ("lea", "Tu connais très bien ce métier.",
     "You know this business very well.",
     [(666, "Mais c'est notre métier, ça.")], ""),
    ("lea", "On vend du désir au cinéma.",
     "We sell desire in cinema.",
     [(667, "On ne fait que vendre du désir.")], ""),
    ("gabriel", "Julien aime beaucoup les jolies femmes.",
     "Julien likes pretty women a lot.",
     [(664, "Il aime les femmes.")], ""),
    ("gabriel", "Je ne veux pas d'histoire.",
     "I do not want any trouble.",
     [(665, "Je ne veux pas qu'il aime la mienne.")], ""),
    ("lea", "Il faut du désir entre artistes.",
     "There must be desire between artists.",
     [(668, "Il faut du désir dans une collaboration")], ""),
    ("lea", "Laisse-la vivre sa propre vie.",
     "Let her live her own life.",
     [(672, "Laisse-la vivre sa vie.")], ""),
    ("lea", "Fais-lui confiance avant tout.",
     "Trust her above all.",
     [(674, "Avant tout, fais-lui confiance.")], ""),
    ("lea", "Elle t'aimera encore plus ainsi.",
     "She will love you even more that way.",
     [(675, "Elle t'aimera encore plus.")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'Are you doing well, my dear Gabriel?' Arlette gently checks in on her troubled colleague. "
     "The friendly address mon cher expresses fond regard."),
    (1, None,
     "'It is great for Sofia's movie.' Gabriel acknowledges the artistic breakthrough for his partner. "
     "The preposition pour links the positive sentiment to the film."),
    (2, None,
     "'Since their meeting, Sofia is radiant.' Arlette notices the actress's vibrant artistic energy. "
     "The adjective rayonnante describes someone beaming with happiness."),
    (3, None,
     "'I think that I am jealous!' Gabriel candidly confesses his private insecurity to the veteran agent. "
     "The phrase je crois que introduces an honest admission."),
    (4, None,
     "'I am no longer so sure.' He second-guesses the wisdom of setting up the collaboration. "
     "The negative locution ne ... plus si sur expresses rising doubt."),
    (5, None,
     "'The script is a bit vulgar.' He rationalizes his personal jealousy by criticizing the screenplay. "
     "The phrase un peu softens the evaluative adjective vulgaire."),
    (6, None,
     "'You know this business very well.' Arlette reminds him of the realities of the film industry. "
     "The adverb tres bien modifies the verb connais."),
    (7, None,
     "'We sell desire in cinema.' The senior agent explains that dramatic art thrives on emotional chemistry. "
     "The verb vend comes from the regular verb vendre."),
    (8, None,
     "'Julien likes pretty women a lot.' Gabriel voices his anxiety about the charismatic musician's reputation. "
     "The adverbial expression aime beaucoup describes strong attraction."),
    (9, None,
     "'I do not want any trouble.' The protective agent fears emotional heartbreak in his personal life. "
     "The partitive d'histoire colloquially means trouble or drama."),
    (10, None,
     "'There must be desire between artists.' Arlette insists that creative passion requires genuine mutual attraction. "
     "The impersonal verb il faut states a necessary condition."),
    (11, None,
     "'Let her live her own life.' She counsels Gabriel to avoid suffocating his talented girlfriend. "
     "The imperative laisse-la urges him to give her space."),
    (12, None,
     "'Trust her above all.' The veteran agent offers timeless wisdom on loving an artist. "
     "The idiom faire confiance a someone means to place trust in them."),
    (13, None,
     "'She will love you even more that way.' Arlette reassures him that respecting Sofia's independence strengthens love. "
     "The simple future aimera expresses confident reassurance."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Calmed by Arlette's experience and warmth, Gabriel learns to separate his professional role from his personal insecurities. "
    "Remember the essential French phrase for placing trust in someone: faire confiance."
)

CLOSING = ("lea", "Elle t'aimera encore plus ainsi.")
