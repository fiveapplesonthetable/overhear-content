# Authoring module for dix-pour-cent s03e04 scene 15 (cues 840-873).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e04/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s03e04/scene-15.json

ID = "dix-pour-cent-s03e04-scene-15"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 15
TITLE = "Tournage interrompu  (Shoot Suspended)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "marcel", "cedric": "theo"}
LABELS = {"lea": "Isabelle", "gabriel": "Gabriel", "cedric": "Cédric"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 840-873. On the French set, director Cédric Kahn searches frantically for missing star Isabelle Huppert. "
    "After Gabriel stalls him, Isabelle arrives with an alibi and reveals how she successfully derailed the American shoot."
)

INTRO = (
    "On the French film set, director Cedric Kahn frantically searches for his missing lead actress Isabelle Huppert. "
    "After Gabriel stalls the frustrated director, Isabelle reappears with an ingenious excuse, having successfully shut down the rival American production. "
    "Listen to the scene in French first."
)

STORY = [
    ("cedric", "Isabelle n'est pas dans sa loge?",
     "Is Isabelle not in her dressing room?",
     [(843, "Elle n'est pas là")], ""),
    ("gabriel", "Je sais, on attend son retour.",
     "I know, we are waiting for her return.",
     [(844, "Je sais"), (845, "On attend")], ""),
    ("cedric", "C'est sa dernière scène ce soir!",
     "It is her last scene tonight!",
     [(847, "C'est sa dernière scène")], ""),
    ("cedric", "Isabelle, où étais-tu passée?",
     "Isabelle, where had you gone?",
     [(854, "T'étais où")], ""),
    ("lea", "J'étais à la pharmacie de garde.",
     "I was at the late-night pharmacy.",
     [(857, "pharmacie de garde")], ""),
    ("lea", "Je voulais être discrète pour vous.",
     "I wanted to be discreet for you.",
     [(858, "Je voulais rester discrète")], ""),
    ("cedric", "On t'attend sur le décor maintenant.",
     "We are waiting for you on set now.",
     [(863, "on t'attend sur le décor")], ""),
    ("lea", "D'accord, j'arrive tout de suite.",
     "Alright, I am coming right away.",
     [(864, "À tout de suite")], ""),
    ("gabriel", "Comment as-tu fait pour partir?",
     "How did you manage to get away?",
     [(865, "comment t'as fait")], ""),
    ("lea", "Tout a dégénéré avec Ben Stiller.",
     "Everything fell apart with Ben Stiller.",
     [(866, "dégénéré entre le metteur en scène et Ben Stiller")], ""),
    ("lea", "Ils ont commencé à se disputer.",
     "They started arguing with each other.",
     [(867, "venue aux mains")], ""),
    ("lea", "Le tournage américain est interrompu.",
     "The American shoot is suspended.",
     [(869, "tournage interrompu")], ""),
    ("lea", "C'est vraiment génial, non?",
     "That is truly genius, isn't it?",
     [(870, "C'est cool, non")], ""),
    ("gabriel", "Tu es incroyable, Isabelle!",
     "You are incredible, Isabelle!",
     [(870, "C'est cool")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Is Isabelle not in her dressing room?' Cedric worries about his missing lead actress. "
     "The negative question shows rising panic."),
    (1, None,
     "'I know, we are waiting for her return.' Gabriel stalls the director diplomatically. "
     "The acknowledgment buys precious time."),
    (2, None,
     "'It is her last scene tonight!' The director stresses the tight deadline. "
     "The exclamation emphasizes schedule constraints."),
    (3, None,
     "'Isabelle, where had you gone?' Cedric demands an explanation for her absence. "
     "The direct question seeks accountability."),
    (4, None,
     "'I was at the late-night pharmacy.' Isabelle offers a clever medical alibi. "
     "The locational phrase accounts for her delay."),
    (5, None,
     "'I wanted to be discreet for you.' She feigns embarrassment over health issues. "
     "The polite explanation disarms suspicion."),
    (6, None,
     "'We are waiting for you on set now.' Cedric accepts the excuse and heads to set. "
     "The imperative urgency requests immediate presence."),
    (7, None,
     "'Alright, I am coming right away.' Isabelle promises prompt arrival on set. "
     "The responsive phrase confirms readiness."),
    (8, None,
     "'How did you manage to get away?' Gabriel marvels at her miraculous escape. "
     "The curious question asks for the secret trick."),
    (9, None,
     "'Everything fell apart with Ben Stiller.' Isabelle explains the collapse of the American shoot. "
     "The dramatic verb describes total chaos."),
    (10, None,
     "'They started arguing with each other.' She details how she provoked creative conflict. "
     "The past tense narrative recounts the confrontation."),
    (11, None,
     "'The American shoot is suspended.' Isabelle delivers the triumphant news. "
     "The passive construction marks her artistic victory."),
    (12, None,
     "'That is truly genius, isn't it?' She boasts of her cunning sabotage. "
     "The rhetorical question seeks admiration."),
    (13, None,
     "'You are incredible, Isabelle!' Gabriel expresses utter astonishment and relief. "
     "The admiring exclamation praises her audacity.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "With lightning-fast improvisation and daring cunning, Isabelle Huppert pulls off the impossible double booking. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "Allons tourner cette fameuse scène.")
