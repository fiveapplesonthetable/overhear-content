# Authoring module for dix-pour-cent s03e06 scene 21 (cues 1007-1101).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-21.py --out out/dix-pour-cent/s03e06/scene-21.json

ID = "dix-pour-cent-s03e06-scene-21"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 21
TITLE = "Le double artistique  (The Artistic Double)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1007-1101. At the ASK anniversary party, Andrea and Gabriel coordinate their defense "
    "against suspicious American producers by explaining that Cedric Kahn hired an artistic double to create a ghost."
)

INTRO = (
    "At the ASK anniversary party, Andrea and Gabriel face furious questions about Isabelle Huppert's secret schedule. "
    "To defuse the accusations, Andrea and Gabriel explain that director Cedric Kahn hired an artistic double to create a poetic ghost. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("gabriel", "Les producteurs américains posent des questions.",
     "The American producers are asking questions.",
     [(1018, "de quoi vous nous accusiez")], "Gabriel reports mounting pressure"),
    ("lea", "Ils pensent qu'Isabelle a triché?",
     "Do they think that Isabelle cheated?",
     [(1020, "Isabelle Huppert ne pouvait pas tourner")], "Andrea assesses the suspicion"),
    ("gabriel", "Ils ont vu le tournage nocturne.",
     "They saw the night shoot.",
     [(1031, "tournage de Marie de Médicis")], "Gabriel explains what aroused suspicion"),
    ("lea", "Isabelle était au mariage de son fils!",
     "Isabelle was at her son's wedding!",
     [(1022, "mariage de son fils")], "Andrea states their official alibi"),
    ("gabriel", "Il s'agit d'un énorme malentendu.",
     "This is a huge misunderstanding.",
     [(1028, "énorme malentendu")], "Gabriel echoes the agency defense"),
    ("lea", "Cédric Kahn a utilisé un double.",
     "Cedric Kahn used a double.",
     [(1073, "vrai double de son actrice")], "Andrea reveals the creative strategy"),
    ("gabriel", "Une doublure pour créer un fantôme.",
     "A stand-in to create a ghost.",
     [(1072, "créer un fantôme")], "Gabriel details the artistic concept"),
    ("lea", "C'est une idée poétique et surréaliste!",
     "It is a poetic, surrealist idea!",
     [(1075, "poétique"), (1076, "surréaliste")], "Andrea frames the deception as art"),
    ("gabriel", "En France, nous avons des idées.",
     "In France, we have ideas.",
     [(1070, "on a des idées")], "Gabriel invokes French cultural pride"),
    ("lea", "Les Américains veulent voir les images.",
     "The Americans want to see footage.",
     [(1079, "images de tout ça")], "Andrea announces the immediate challenge"),
    ("gabriel", "Le premier montage est dans le bureau.",
     "The first cut is in the office.",
     [(1083, "D'ici")], "Gabriel confirms footage availability"),
    ("lea", "Allons leur montrer ce beau film.",
     "Let us go show them this fine film.",
     [(1101, "Allez, on accouche")], "Andrea prepares for the screening"),
    ("gabriel", "Espérons que le résultat soit convaincant.",
     "Let us hope the result is convincing.",
     [(1085, "petit peu délicat")], "Gabriel expresses quiet concern"),
    ("lea", "Notre agence sauvera ce projet important.",
     "Our agency will save this important project.",
     [(1096, "très important")], "Andrea rallies agency confidence")
]

WALK = [
    (0, None,
     "'The American producers are asking questions.' Gabriel warns of incoming scrutiny. "
     "The verbal locution 'poser des questions' means to ask questions."),
    (1, None,
     "'Do they think that Isabelle cheated?' Andrea inquires about the gravity of the doubts. "
     "The verb 'tricher' means to cheat or play unfairly."),
    (2, None,
     "'They saw the night shoot.' Gabriel explains that the concurrent production was witnessed. "
     "The adjective 'nocturne' describes nighttime activity."),
    (3, None,
     "'Isabelle was at her son's wedding!' Andrea points to the confirmed family event. "
     "The noun 'mariage' denotes a wedding celebration."),
    (4, None,
     "'This is a huge misunderstanding.' Gabriel emphasizes that everything is innocent. "
     "The idiom 'il s'agit de' means it is a matter of."),
    (5, None,
     "'Cedric Kahn used a double.' Andrea presents their primary narrative defense. "
     "The noun 'double' refers to a body double or stand-in."),
    (6, None,
     "'A stand-in to create a ghost.' Gabriel explains the directorial motive. "
     "The noun 'doublure' refers specifically to a stand-in performer."),
    (7, None,
     "'It is a poetic, surrealist idea!' Andrea sells the artistic rationale with passion. "
     "The coordinated adjectives celebrate avant-garde cinema."),
    (8, None,
     "'In France, we have ideas.' Gabriel quotes a famous French aphorism. "
     "The plural noun 'idees' conveys ingenuity and creative resourcefulness."),
    (9, None,
     "'The Americans want to see footage.' Andrea states the demands of the foreign partners. "
     "The modal verb 'veulent' expresses their firm insistence."),
    (10, None,
     "'The first cut is in the office.' Gabriel points toward the projection room. "
     "The noun 'montage' designates film editing or an edit cut."),
    (11, None,
     "'Let us go show them this fine film.' Andrea leads the delegation forward boldly. "
     "The imperative 'allons' expresses collective resolution."),
    (12, None,
     "'Let us hope the result is convincing.' Gabriel tempers enthusiasm with realism. "
     "The subjunctive 'soit' follows the verb of hoping or wishing."),
    (13, None,
     "'Our agency will save this important project.' Andrea rallies her fellow agent. "
     "The future verb 'sauvera' promises a successful rescue.")
]

OUTRO = (
    "Armed with an artistic explanation, Andrea and Gabriel head toward the screening room to convince the American producers. "
    "With ASK's reputation on the line, every scene of the rough cut will count. "
    "Now let's listen to the dialogue one last time in French."
)

CLOSING = ("lea", "Notre agence sauvera ce projet important.")
