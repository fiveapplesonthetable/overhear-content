# Authoring module for dix-pour-cent s04e06 scene 22 (cues 912-956).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e06/authoring/scene-22.py --out overhear-content/out/dix-pour-cent/s04e06/scene-22.json

ID = "dix-pour-cent-s04e06-scene-22"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 22
TITLE = "Le départ d'Andréa  (Andréa's Departure)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jean": "theo"}
LABELS = {"lea": "Andréa", "jean": "Jean Reno"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 912-956. Jean Reno sets up champagne in the conference room to thank the ASK team for their support. "
    "Andrea joins him and reveals she is stepping away from the agency, sharing heartfelt advice with the movie star."
)

INTRO = (
    "In the conference room of ASK, movie star Jean Reno brings champagne to express his gratitude to the agency staff. "
    "Meeting him alone, Andrea Martel confides that she is resigning from agent life to start a new chapter. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("jean", "C'est pour vous remercier tous!",
     "It is to thank you all!",
     [(917, "C'est pour vous tous."), (918, "Pour vous remercier de m'avoir poussé à continuer.")], "Jean presents gifts of appreciation"),
    ("lea", "Merci Jean, c'est très gentil.",
     "Thank you Jean, that is very kind.",
     [(923, "Merci Jean, c'est très gentil de ta part.")], "Andrea thanks him warmly"),
    ("lea", "J'ai quelque chose à te dire.",
     "I have something to tell you.",
     [(924, "parce que j'ai quelque chose à te dire.")], "Andrea turns the tone serious"),
    ("jean", "Tu as l'air grave, Andréa.",
     "You look serious, Andrea.",
     [(924, "Je suis content que tu sois là")], "Jean observes her solemn expression"),
    ("lea", "Je pars de l'agence.",
     "I am leaving the agency.",
     [(925, "Je pars.")], "Andrea announces her departure"),
    ("jean", "Tu quittes ce métier?",
     "Are you quitting this job?",
     [(927, "Tu pars ?")], "Jean is surprised by the decision"),
    ("lea", "Oui, je m'en vais définitivement.",
     "Yes, I am leaving definitively.",
     [(928, "Je pars."), (929, "et c'est moi qui m'en vais.")], "Andrea confirms stepping down"),
    ("jean", "C'est une vie de chien.",
     "It is a dog's life.",
     [(931, "Le métier d'agent, c'est vraiment une vie de chien.")], "Jean recognizes the brutal stress"),
    ("lea", "Mais toi, tu dois continuer.",
     "But you, you must go on.",
     [(932, "Je pars, mais toi tu dois continuer.")], "Andrea encourages him to act"),
    ("jean", "Seulement si le film se fait!",
     "Only if the movie happens!",
     [(933, "Si le Beauvois se fait.")], "Jean sets a strict condition"),
    ("lea", "Élise Formain est une femme redoutable.",
     "Elise Formain is a formidable woman.",
     [(935, "Tu connais Élise Formain ?")], "Andrea gives cautionary advice"),
    ("jean", "Ne t'inquiète pas pour moi.",
     "Do not worry about me.",
     [(935, "Tu connais Élise Formain ?")], "Jean smiles with veteran confidence"),
    ("lea", "Prends bien soin de ton talent.",
     "Take good care of your talent.",
     [(932, "tu dois continuer.")], "Andrea bids a caring farewell"),
    ("jean", "Bonne chance pour ta nouvelle vie!",
     "Good luck for your new life!",
     [(918, "Pour vous remercier")], "Jean raises a celebratory toast"),
]

WALK = [
    (0, None,
     "'It is to thank you all!' Jean Reno presents champagne and treats to the team. "
     "The verb 'remercier' means to thank."),
    (1, None,
     "'Thank you Jean, that is very kind.' Andrea appreciates the generous thought. "
     "The adjective 'gentil' describes kind behavior."),
    (2, None,
     "'I have something to tell you.' Andrea shifts the mood with a serious announcement. "
     "The pronoun 'quelque chose' means something."),
    (3, None,
     "'You look serious, Andrea.' Jean notices her solemn expression. "
     "The idiom 'avoir l'air' translates to look or seem."),
    (4, None,
     "'I am leaving the agency.' Andrea delivers her shocking decision. "
     "The verb form 'pars' comes from 'partir', to leave."),
    (5, None,
     "'Are you quitting this job?' Jean asks in genuine astonishment. "
     "The verb 'quitter' means to quit or leave behind."),
    (6, None,
     "'Yes, I am leaving definitively.' Andrea confirms that her agent career is over. "
     "The adverb 'definitivement' signifies permanently or definitively."),
    (7, None,
     "'It is a dog's life.' Jean remarks on the exhausting demands of talent representation. "
     "The expression 'vie de chien' denotes a miserable, harsh life."),
    (8, None,
     "'But you, you must go on.' Andrea urges him to stay dedicated to cinema. "
     "The modal verb 'devoir' conveys duty or obligation."),
    (9, None,
     "'Only if the movie happens!' Jean conditions his continuation on good cinema. "
     "The pronominal construction 'se faire' means to happen or come to fruition."),
    (10, None,
     "'Elise Formain is a formidable woman.' Andrea warns him about rival management. "
     "The adjective 'redoutable' describes someone fearsome or formidable."),
    (11, None,
     "'Do not worry about me.' Jean reassures her with his veteran wisdom. "
     "The imperative 'ne t'inquiete pas' means do not worry."),
    (12, None,
     "'Take good care of your talent.' Andrea gives her final parting wish as an agent. "
     "The masculine noun 'talent' refers to natural ability or flair."),
    (13, None,
     "'Good luck for your new life!' Jean raises a glass to her brave next chapter. "
     "The phrase 'bonne chance' means good luck."),
]

OUTRO = (
    "As Jean Reno and Andrea clink glasses in the agency boardroom, an era quietly draws to a close. "
    "Having guided her artists through triumphs and crises, Andrea steps bravely into the future on her own terms. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("jean", "Merci pour tout ce que tu as fait!")
