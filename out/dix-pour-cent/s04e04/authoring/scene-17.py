# Authoring module for dix-pour-cent s04e04 scene 17 (cues 1029-1033).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-17.py --out overhear-content/out/dix-pour-cent/s04e04/scene-17.json

ID = "dix-pour-cent-s04e04-scene-17"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 17
TITLE = "La trahison découverte  (The Betrayal Discovered)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1029-1033. Sitting at Mathias's computer while he is in the kitchen, Camille is stunned to read an open "
    "draft email revealing Mathias made false promises to author Ulrika to steal her away from ASK with plans "
    "to sideline her."
)

INTRO = (
    "Left alone at Mathias's desk, Camille looks for the paternity document on his computer. "
    "Instead, she spots an open draft email detailing Mathias's ruthless plot to deceive author Ulrika. "
    "Let's listen to this chilling discovery in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Voyons ce formulaire sur son ordinateur.",
     "Let us look for this form on his computer.",
     [(1022, "le formulaire")], "Camille looks at Mathias's computer screen"),
    ("lea", "Attends, qu'est-ce que c'est que ça?",
     "Wait, what is this?",
     [], "Camille notices an open message window"),
    ("lea", "C'est un brouillon d'e-mail ouvert.",
     "It is an open draft email.",
     [], "Camille spots the draft message"),
    ("lea", "J'ai fait des promesses à Ulrika...",
     "I made promises to Ulrika...",
     [(1029, "J'AI FAIT DES PROMESSES")], "Camille reads the first sentence aloud"),
    ("lea", "Pour qu'elle signe le contrat...",
     "So that she signs the contract...",
     [(1029, "POUR QU'ELLE SIGNE")], "Camille continues reading Mathias's email"),
    ("lea", "Mais je compte la décourager progressivement...",
     "But I plan to discourage her gradually...",
     [(1030, "DÉCOURAGER PROGRESSIVEMENT")], "Camille reads his cynical plan"),
    ("lea", "On peut la remplacer plus tard...",
     "We can replace her later on...",
     [(1031, "ON PEUT LA REMPLACER")], "Camille reads about sidelining the author"),
    ("lea", "Utiliser la note de frais...",
     "Use the expense account...",
     [(1032, "LA NOTE DE FRAIS")], "Camille reads about his financial scheme"),
    ("lea", "Pour une fondation animale...",
     "For an animal foundation...",
     [(1032, "POUR UNE FONDATION ANIMALE")], "Camille sees his fake donation plan"),
    ("lea", "Mon Dieu, c'est une trahison totale!",
     "My God, this is total betrayal!",
     [], "Camille is horrified by her father's dishonesty"),
    ("lea", "Il a menti à tout le monde.",
     "He lied to everyone.",
     [], "Camille realizes the depth of the deception"),
    ("mathias", "Camille? Tu as trouvé ce formulaire?",
     "Camille? Did you find that form?",
     [(1033, "Camille")], "Mathias walks back into the room"),
    ("mathias", "Voici deux verres pour fêter ça!",
     "Here are two glasses to celebrate this!",
     [(1026, "On trinque")], "Mathias brings glasses of champagne"),
    ("lea", "Oui, tout va très bien, papa.",
     "Yes, everything is fine, dad.",
     [], "Camille hides her shock and closes the window"),
]

WALK = [
    (0, None,
     "'Let us look for this form on his computer.' Camille prepares to search for the legal paperwork. "
     "The imperative form 'voyons' expresses let us see."),
    (1, None,
     "'Wait, what is this?' Camille is distracted by an unexpected open window on the screen. "
     "The conversational phrase 'qu'est-ce que c'est' asks what something is."),
    (2, None,
     "'It is an open draft email.' Camille notices an unsent message written by Mathias. "
     "The compound noun 'brouillon d'e-mail' denotes a draft message."),
    (3, None,
     "'I made promises to Ulrika...' Camille reads the beginning of her father's private strategy notes. "
     "The noun 'promesses' denotes commitments or vows."),
    (4, None,
     "'So that she signs the contract...' Camille discovers how Mathias persuaded the Swedish author. "
     "The conjunction 'pour que' introduces a subjunctive purpose clause."),
    (5, None,
     "'But I plan to discourage her gradually...' Camille discovers his plan to push the author aside. "
     "The verb phrase 'compter faire' expresses an intention to act."),
    (6, None,
     "'We can replace her later on...' Camille reads that Mathias intends to bring in a new writer. "
     "The verb 'remplacer' means to substitute or replace."),
    (7, None,
     "'Use the expense account...' Camille uncovers his plan to charge the company for personal schemes. "
     "The business term 'note de frais' denotes an expense report."),
    (8, None,
     "'For an animal foundation...' Camille reads how Mathias planned to feign charitable support. "
     "The noun 'fondation' designates an organization or charity."),
    (9, None,
     "'My God, this is total betrayal!' Camille realizes that her father betrayed both her and ASK. "
     "The feminine noun 'trahison' denotes treachery or disloyalty."),
    (10, None,
     "'He lied to everyone.' Camille sees clearly that Mathias manipulated everyone around him. "
     "The compound past tense 'a menti' comes from 'mentir'."),
    (11, None,
     "'Camille? Did you find that form?' Mathias returns from the kitchen holding two glasses. "
     "The past question 'tu as trouve' asks if someone found something."),
    (12, None,
     "'Here are two glasses to celebrate this!' Mathias approaches warmly to toast their reunion. "
     "The preposition 'voici' presents or introduces objects."),
    (13, None,
     "'Yes, everything is fine, dad.' Camille conceals her devastation behind a composed expression. "
     "The polite reassurance 'tout va bien' claims that all is well."),
]

OUTRO = (
    "Horrified by the evidence of her father's treachery, Camille quickly hides her discovery as Mathias returns. "
    "The revelation leaves her questioning everything about her relationship with him. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("mathias", "À notre nouvelle vie!")
