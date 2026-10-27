# Authoring module for dix-pour-cent s03e04 scene 16 (cues 874-903).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-16.py --out out/dix-pour-cent/s03e04/scene-16.json

ID = "dix-pour-cent-s03e04-scene-16"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 16
TITLE = "Restons solidaires  (Let's Stick Together)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Isabelle Huppert", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 874-903. In the car after an all-night shoot, Isabelle Huppert thanks Mathias and Gabriel before heading to a fashion show. "
    "Mathias reveals to Gabriel that he knows about their secret agency plan and proposes that they unite against Hicham."
)

INTRO = (
    "After an exhausting night shoot, Isabelle Huppert thanks Mathias and Gabriel before heading to a fashion show. "
    "Mathias reveals he knows about their plan to launch a secret agency and proposes that they unite to oust Hicham instead. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Merci pour votre aide précieuse, les garçons.",
     "Thank you for your valuable help, boys.",
     [(874, "Merci, Mathias"), (890, "Encore merci, les garçons")], "Isabelle expresses her deep gratitude"),
    ("lea", "Cette folle nuit était un succès.",
     "This crazy night was a success.",
     [(875, "sans toi")], "Isabelle celebrates the completed shoot"),
    ("mathias", "Rentrez bien et reposez-vous, Isabelle.",
     "Get home safely and rest, Isabelle.",
     [(892, "Et repose-toi")], "Mathias advises rest after the marathon"),
    ("lea", "Je passe d'abord au défilé Chanel!",
     "I am stopping first at the Chanel show!",
     [(894, "défilé Chanel")], "Isabelle reveals her endless energy"),
    ("gabriel", "Cette femme ne dort donc jamais?",
     "Does this woman never sleep then?",
     [(897, "cette femme ne dort jamais")], "Gabriel marvels at her boundless stamina"),
    ("mathias", "Gabriel, je sais ce que vous préparez.",
     "Gabriel, I know what you are preparing.",
     [(878, "Je suis au courant, Gabriel")], "Mathias drops a bombshell"),
    ("gabriel", "De quoi parles-tu exactement, Mathias?",
     "What are you talking about exactly, Mathias?",
     [(876, "C'est pour ça que tu veux partir")], "Gabriel feigns innocence"),
    ("mathias", "Je connais votre agent immobilier.",
     "I know your real estate agent.",
     [(879, "Les gens immobiliers")], "Mathias cites his inside source"),
    ("mathias", "Vous cherchez de nouveaux bureaux.",
     "You are looking for new offices.",
     [(879, "vos bureaux")], "Mathias names their secret venture"),
    ("gabriel", "Nous ne pouvons plus travailler avec Hicham.",
     "We can no longer work with Hicham.",
     [(888, "l'intrus dans cette famille")], "Gabriel admits the unbearable tension"),
    ("mathias", "Mais nous devons rester tous solidaires!",
     "But we must all stick together!",
     [(882, "Faut qu'on reste solidaires")], "Mathias calls for internal unity"),
    ("mathias", "Nous sommes une vraie famille.",
     "We are a true family.",
     [(887, "On est une famille")], "Mathias appeals to their shared history"),
    ("mathias", "Si Hicham partait, vous resteriez?",
     "If Hicham left, would you stay?",
     [(889, "S'il partait, vous resteriez")], "Mathias proposes an alliance to oust Hicham"),
    ("gabriel", "C'est une proposition très intéressante, Mathias.",
     "That is a very interesting proposal, Mathias.",
     [(883, "Un peu comme cette nuit")], "Gabriel shows cautious openness")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Thank you for your valuable help, boys.' Isabelle shows heartfelt appreciation for her agents. "
     "The polite formula acknowledges their overnight assistance."),
    (1, None,
     "'This crazy night was a success.' Isabelle celebrates the triumphant filming. "
     "The demonstrative adjective highlights the unique, hectic shoot."),
    (2, None,
     "'Get home safely and rest, Isabelle.' Mathias recommends overdue sleep. "
     "The coordinated imperative verbs express courteous concern."),
    (3, None,
     "'I am stopping first at the Chanel show!' Isabelle reveals her immediate fashion appointment. "
     "The present motion verb demonstrates her tireless schedule."),
    (4, None,
     "'Does this woman never sleep then?' Gabriel is stunned by her stamina. "
     "The negative rhetorical question expresses sheer awe."),
    (5, None,
     "'Gabriel, I know what you are preparing.' Mathias signals that their secrets are out. "
     "The relative clause introduces knowledge of their hidden plans."),
    (6, None,
     "'What are you talking about exactly, Mathias?' Gabriel questions the accusation. "
     "The interrogative inversion attempts to stall for time."),
    (7, None,
     "'I know your real estate agent.' Mathias reveals his source of information. "
     "The direct verb confirms insider knowledge of their office hunt."),
    (8, None,
     "'You are looking for new offices.' Mathias exposes their plan to leave ASK. "
     "The present verb describes their secret commercial search."),
    (9, None,
     "'We can no longer work with Hicham.' Gabriel justifies their desire to leave. "
     "The negative modal construction highlights irreconcilable friction."),
    (10, None,
     "'But we must all stick together!' Mathias urges agency cohesion. "
     "The obligation modal with an adjective pleads for unity."),
    (11, None,
     "'We are a true family.' Mathias stresses their deep personal bond. "
     "The linking verb with an adjective appeals to emotional loyalty."),
    (12, None,
     "'If Hicham left, would you stay?' Mathias proposes a mutual coup. "
     "The conditional hypothesis tests Gabriel's willingness to remain."),
    (13, None,
     "'That is a very interesting proposal, Mathias.' Gabriel considers the tactical offer. "
     "The evaluative adjective signals unexpected alignment between rivals.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "Following an exhausting night of cinema acrobatics, Mathias and Gabriel discover an unexpected shared goal. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("gabriel", "C'est une proposition très intéressante, Mathias.")
