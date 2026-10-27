# Authoring module for dix-pour-cent s02e02 scene 27 (cues 896-921).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-27.py --out out/dix-pour-cent/s02e02/scene-27.json

ID = "dix-pour-cent-s02e02-scene-27"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 27
TITLE = "La fin de la lune de miel  (The End of the Honeymoon)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "mathias": "marcel"}
LABELS = {"lea": "Andréa", "hicham": "Hicham", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 896-921. After Mathias fails to pick up her calls, Andréa enters Hicham's office "
    "to explain why they failed to sign Fabrice Luchini. Furious at her failure and defiant attitude, "
    "majority owner Hicham fires her on the spot and orders her to leave ASK immediately. "
    "Adapted for A1 French."
)

INTRO = (
    "At the agency, Andrea tries unsuccessfully to reach Mathias Barneville before meeting with Hicham. "
    "When she tries to apologize for the disastrous evening with Fabrice Luchini, Hicham's patience runs out. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("mathias", "Vous êtes sur la messagerie de Mathias.",
     "You have reached Mathias's voicemail.",
     [(896, "Bonjour, vous êtes sur la messagerie de Mathias Barneville.")], "Shortened message"),
    ("mathias", "Laissez un message après le bip.",
     "Leave a message after the beep.",
     [(897, "Laissez un message et je vous rappellerai.")], "Adapted voicemail prompt"),
    ("lea", "Mathias ne répond toujours pas.",
     "Mathias is still not answering.",
     [(898, "tu as vu Mathias ?")], "Adapted line"),
    ("lea", "Bonjour, Hicham. Je suis désolée.",
     "Hello, Hicham. I am sorry.",
     [(902, "Bonjour."), (903, "Désolée pour hier soir.")], "Adapted greeting"),
    ("lea", "Hier soir, la situation était difficile.",
     "Last night, the situation was difficult.",
     [(904, "Ça s'est tendu, j'avais peur."), (905, "C'était horrible.")], "Adapted description"),
    ("hicham", "La lune de miel est terminée.",
     "The honeymoon is over.",
     [(907, "la lune de miel est terminée, Marteau.")], "Dropped nickname Marteau"),
    ("hicham", "Prends tes affaires et va-t'en.",
     "Take your things and go away.",
     [(908, "Prends tes affaires et va-t'en.")], ""),
    ("lea", "Arrête, Hicham, sois raisonnable.",
     "Stop it, Hicham, be reasonable.",
     [(909, "Arrête, Hicham.")], "Added sois raisonnable"),
    ("hicham", "Il y a des limites ici.",
     "There are limits here.",
     [(910, "Il y a des limites.")], "Added ici"),
    ("hicham", "Nous ne sommes pas des animaux.",
     "We are not animals.",
     [(910, "On n'est pas des animaux.")], "Formalized subject to nous"),
    ("lea", "Qu'est-ce que tu veux de plus?",
     "What more do you want?",
     [(914, "Qu'est-ce que tu veux de plus ?")], ""),
    ("hicham", "Rentre chez toi maintenant.",
     "Go home now.",
     [(915, "Rentre chez toi.")], "Added maintenant"),
    ("lea", "Tu ne peux pas me virer!",
     "You cannot fire me!",
     [(916, "Tu ne peux pas me virer.")], ""),
    ("hicham", "Et pourquoi pas?",
     "And why not?",
     [(916, "Pourquoi pas ?")], "Added Et"),
    ("lea", "Je suis associée de l'agence.",
     "I am a partner in the agency.",
     [(917, "Je suis associé, il faut un accord.")], "Adapted with de l'agence"),
    ("hicham", "Je suis l'actionnaire majoritaire.",
     "I am the majority shareholder.",
     [(918, "Je suis actionnaire majoritaire.")], "Added article"),
    ("hicham", "Laisse ton ordinateur et tes dossiers.",
     "Leave your computer and your files.",
     [(920, "Laisse tout ce qui appartient"), (921, "ordinateur, clients... tout.")], "Adapted computer and files"),
]

OPENER = "Let's examine how Hicham is coldly dismissing Andrea with no hesitation."

WALK = [
    (0, None,
     "'You have reached Mathias's voicemail.' A standard French greeting on an answering machine."),
    (1, None,
     "'Leave a message after the beep.' An imperative instruction using the preposition apres."),
    (2, None,
     "'Mathias is still not answering.' The adverb toujours meaning still in a negative sentence."),
    (3, None,
     "'Hello, Hicham. I am sorry.' A polite opening apology addressed to her boss."),
    (4, None,
     "'Last night, the situation was difficult.' The compound temporal phrase hier soir."),
    (5, None,
     "'The honeymoon is over.' A metaphor announcing the end of good relations."),
    (6, None,
     "'Take your things and go away.' Two imperatives ordering immediate departure."),
    (7, None,
     "'Stop it, Hicham, be reasonable.' An imperative followed by the subjunctive form of etre."),
    (8, None,
     "'There are limits here.' The presentative phrase il y a with a plural noun."),
    (9, None,
     "'We are not animals.' A formal first-person plural negative statement."),
    (10, None,
     "'What more do you want?' An idiomatic question with de plus meaning further."),
    (11, None,
     "'Go home now.' An imperative using rentrer meaning to go home."),
    (12, None,
     "'You cannot fire me!' The colloquial verb virer meaning to dismiss or fire."),
    (13, None,
     "'And why not?' An interrogative phrase challenging her objection."),
    (14, None,
     "'I am a partner in the agency.' The feminine noun associee referring to her partnership status."),
    (15, None,
     "'I am the majority shareholder.' The adjective majoritaire modifying the owner noun."),
    (16, None,
     "'Leave your computer and your files.' An imperative followed by possessive determiners."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Hicham has ruthlessly fired Andrea, asserting his complete authority as majority owner. "
    "Andrea faces exile from the agency she helped build."
)

CLOSING = ("lea", "Ce n'est pas fini, Hicham.")
