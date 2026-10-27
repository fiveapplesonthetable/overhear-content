# Authoring module for dix-pour-cent s04e04 scene 15 (cues 950-1000).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s04e04/scene-15.json

ID = "dix-pour-cent-s04e04-scene-15"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 15
TITLE = "Un toast déplacé  (An Inappropriate Toast)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 950-1000. At Mathias's office party celebrating the acquisition of book rights, Mathias makes cynical "
    "jokes about handicapped animals and mocks the author Ulrika, prompting a disgusted Noémie to storm out in "
    "tears while Camille resolves to confront her father."
)

INTRO = (
    "At the agency, Mathias hosts a party to celebrate acquiring the book rights to a novel about disabled animals. "
    "Noemie is appalled when Mathias begins to mock the author and her cause in front of the whole room. "
    "Let's listen to their tense exchange in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Qu'est-ce qui se passe ici?",
     "What is going on here?",
     [(954, "Qu'est-ce qui se passe")], "Noémie asks what they are celebrating"),
    ("mathias", "On fête ça! Bois un verre!",
     "We are celebrating! Have a drink!",
     [(955, "On fête ça"), (956, "Tu veux boire quelque chose")], "Mathias celebrates happily"),
    ("lea", "Je peux te dire un mot?",
     "Can I have a word with you?",
     [(959, "je peux te dire un mot")], "Noémie pulls Mathias aside"),
    ("mathias", "Oui, bien sûr, ma chérie.",
     "Yes, of course, my darling.",
     [(963, "chérie")], "Mathias listens affectionately"),
    ("lea", "Tu n'as pas utilisé mes secrets?",
     "You did not use my secrets?",
     [(962, "Tu n'as pas utilisé ce que j'ai dit")], "Noémie asks about her confidential information"),
    ("mathias", "Non, écoute, je te le promets.",
     "No, listen, I promise you.",
     [(963, "Non, écoute"), (964, "Je te le promets")], "Mathias falsely reassures her"),
    ("lea", "Tu le jures devant tout le monde?",
     "Do you swear in front of everyone?",
     [(964, "Tu le jures")], "Noémie wants his word"),
    ("mathias", "Je voudrais porter un grand toast!",
     "I would like to propose a big toast!",
     [(968, "Je voudrais porter un toast")], "Mathias turns back to the room"),
    ("mathias", "À tous les animaux handicapés!",
     "To all the handicapped animals!",
     [(969, "À tous les animaux handicapés")], "Mathias raises his glass cynically"),
    ("mathias", "Sans eux, pas de droits!",
     "Without them, no rights!",
     [(970, "Sans eux, on n'aurait jamais obtenu ces droits")], "Mathias mocks the cause"),
    ("mathias", "J'ai enfin lu ce livre!",
     "I finally read this book!",
     [(971, "J'ai enfin lu le livre")], "Mathias comments on the manuscript"),
    ("mathias", "C'est dingue, c'est n'importe quoi!",
     "It is crazy, it makes no sense!",
     [(973, "C'est dingue"), (975, "C'est n'importe quoi")], "Mathias openly mocks the book"),
    ("lea", "Mathias, tu me dégoûtes vraiment!",
     "Mathias, you really disgust me!",
     [(978, "Dégoûtes")], "Noémie confronts him with disgust"),
    ("mathias", "Noémie, attends, reviens tout de suite!",
     "Noemie, wait, come back immediately!",
     [(976, "Noémie")], "Mathias calls out as she walks away"),
]

WALK = [
    (0, None,
     "'What is going on here?' Noemie arrives at the agency and wonders what the celebration is about. "
     "The question phrase 'qu'est-ce qui' asks what."),
    (1, None,
     "'We are celebrating! Have a drink!' Mathias pours champagne to mark their latest victory. "
     "The verb 'feter' means to celebrate."),
    (2, None,
     "'Can I have a word with you?' Noemie quietly pulls Mathias aside to ask a serious question. "
     "The expression 'dire un mot' means to have a brief word."),
    (3, None,
     "'Yes, of course, my darling.' Mathias answers her with his usual warm charm. "
     "The phrase 'bien sur' means of course."),
    (4, None,
     "'You did not use my secrets?' Noemie worries that Mathias exploited her private confessions. "
     "The negative construction 'ne ... pas' frames the past tense verb."),
    (5, None,
     "'No, listen, I promise you.' Mathias reassures his assistant with a straight face. "
     "The verb 'promettre' means to give one's word."),
    (6, None,
     "'Do you swear in front of everyone?' Noemie insists on an explicit commitment. "
     "The prepositional phrase 'devant tout le monde' means in front of everybody."),
    (7, None,
     "'I would like to propose a big toast!' Mathias turns to the crowd and raises his glass. "
     "The polite conditional 'je voudrais' expresses a desire."),
    (8, None,
     "'To all the handicapped animals!' Mathias dedicates the toast with blatant mockery. "
     "The adjective 'handicapes' modifies the plural noun 'animaux'."),
    (9, None,
     "'Without them, no rights!' Mathias jokes about how the cause brought them the adaptation deal. "
     "The preposition 'sans' denotes absence or lack."),
    (10, None,
     "'I finally read this book!' Mathias admits that he has only just skimmed the manuscript. "
     "The adverb 'enfin' means at last or finally."),
    (11, None,
     "'It is crazy, it makes no sense!' Mathias openly mocks the content of the novel. "
     "The idiom 'n'importe quoi' denotes complete nonsense."),
    (12, None,
     "'Mathias, you really disgust me!' Noemie is appalled by his utter cynicism and lack of respect. "
     "The verb 'degouter' expresses intense aversion."),
    (13, None,
     "'Noemie, wait, come back immediately!' Mathias calls after her in surprise as she storms out. "
     "The imperative 'attends' urges someone to stop and listen."),
]

OUTRO = (
    "Disgusted by Mathias's cruelty and broken promises, Noemie storms out of the party in tears. "
    "Meanwhile at ASK, Camille learns of her father's scheme and resolves to handle the situation herself. "
    "Now let's listen to the complete scene one last time."
)

CLOSING = ("lea", "C'est terminé!")
