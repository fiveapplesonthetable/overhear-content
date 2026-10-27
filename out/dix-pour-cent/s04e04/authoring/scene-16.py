# Authoring module for dix-pour-cent s04e04 scene 16 (cues 1001-1028).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-16.py --out overhear-content/out/dix-pour-cent/s04e04/scene-16.json

ID = "dix-pour-cent-s04e04-scene-16"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 16
TITLE = "La reconnaissance de paternité  (The Paternity Recognition)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1001-1028. Camille visits Mathias at his apartment to discuss her lost adaptation contract and announces "
    "that she has decided to accept official paternity recognition. Deeply touched, Mathias offers to download "
    "the legal forms from his computer while pouring drinks."
)

INTRO = (
    "Camille arrives at Mathias's apartment to discuss her lost book contract and share an unexpected decision. "
    "She tells Mathias that she is finally ready to accept official paternity recognition. "
    "Let's listen to their emotional conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("mathias", "Bonjour Camille! Comment tu vas?",
     "Hello Camille! How are you doing?",
     [(1003, "Comment tu vas")], "Mathias welcomes his daughter warmly"),
    ("lea", "Ça va. Noémie n'est pas là?",
     "I am fine. Is Noemie not here?",
     [(1005, "Noémie n'est pas là")], "Camille checks if Noémie is present"),
    ("mathias", "Non. Qu'est-ce qui se passe?",
     "No. What is going on?",
     [(1004, "Qu'est-ce qui se passe")], "Mathias senses her tension"),
    ("lea", "J'ai des problèmes au travail.",
     "I am having problems at work.",
     [(1007, "J'ai des problèmes au travail")], "Camille mentions her professional difficulties"),
    ("lea", "J'ai perdu mon premier grand contrat.",
     "I lost my first big contract.",
     [(1010, "mon premier grand contrat")], "Camille refers to the book adaptation deal"),
    ("mathias", "Ne t'inquiète pas, d'autres contrats viendront.",
     "Do not worry, other contracts will come.",
     [(1011, "D'autres contrats viendront")], "Mathias offers paternal encouragement"),
    ("lea", "Mais je voulais te parler d'autre chose.",
     "But I wanted to talk to you about something else.",
     [(1012, "je voulais te parler")], "Camille shifts the subject"),
    ("lea", "J'ai réfléchi à la reconnaissance de paternité.",
     "I thought about the paternity recognition.",
     [(1013, "reconnaissance de paternité")], "Camille brings up official recognition"),
    ("mathias", "Vraiment? Qu'est-ce qui t'a fait changer d'avis?",
     "Really? What made you change your mind?",
     [(1016, "changer d'avis")], "Mathias is surprised and moved"),
    ("lea", "Je veux le faire, on se ressemble.",
     "I want to do it, we resemble each other.",
     [(1020, "Je veux le faire"), (1020, "on se ressemble")], "Camille appeals to their resemblance"),
    ("mathias", "On peut aller à la mairie demain!",
     "We can go to town hall tomorrow!",
     [(1021, "aller à la mairie")], "Mathias enthusiastically proposes a visit to town hall"),
    ("lea", "On peut télécharger le formulaire maintenant?",
     "Can we download the form now?",
     [(1022, "télécharger le formulaire")], "Camille suggests getting the document immediately"),
    ("mathias", "Tu as raison, assieds-toi à mon bureau!",
     "You are right, sit down at my desk!",
     [(1022, "Tu as raison"), (1024, "assieds-toi")], "Mathias points to his computer desk"),
    ("mathias", "On trinque? Je vais chercher à boire!",
     "Shall we drink to it? I will get something to drink!",
     [(1026, "On trinque")], "Mathias heads to the kitchen"),
]

WALK = [
    (0, None,
     "'Hello Camille! How are you doing?' Mathias welcomes his daughter into his apartment. "
     "The greeting question 'comment tu vas' asks how someone is."),
    (1, None,
     "'I am fine. Is Noemie not here?' Camille checks whether Mathias is currently alone. "
     "The adverb 'ici' or 'la' denotes location."),
    (2, None,
     "'No. What is going on?' Mathias wonders what brings Camille to his home so unexpectedly. "
     "The interrogative phrase 'qu'est-ce qui se passe' asks what is happening."),
    (3, None,
     "'I am having problems at work.' Camille mentions that things have gone wrong at the agency. "
     "The plural noun phrase 'des problemes' denotes difficulties."),
    (4, None,
     "'I lost my first big contract.' Camille explains the loss of her promising book adaptation. "
     "The ordinal adjective 'premier' means first."),
    (5, None,
     "'Do not worry, other contracts will come.' Mathias tries to comfort her with professional optimism. "
     "The future tense 'viendront' comes from the verb 'venir'."),
    (6, None,
     "'But I wanted to talk to you about something else.' Camille steers the conversation toward a personal matter. "
     "The imperfect verb form 'voulais' expresses past intention."),
    (7, None,
     "'I thought about the paternity recognition.' Camille announces her willingness to make their bond official. "
     "The compound noun 'reconnaissance de paternite' denotes legal recognition."),
    (8, None,
     "'Really? What made you change your mind?' Mathias is pleasantly surprised by her change of heart. "
     "The idiom 'changer d'avis' means to alter one's opinion."),
    (9, None,
     "'I want to do it, we resemble each other.' Camille notes their shared traits and personality. "
     "The reflexive verb 'se ressembler' means to look like or resemble."),
    (10, None,
     "'We can go to town hall tomorrow!' Mathias eagerly suggests making the declaration immediately. "
     "The modal phrase 'on peut' expresses ability or possibility."),
    (11, None,
     "'Can we download the form now?' Camille suggests preparing the paperwork right away. "
     "The verb 'telecharger' means to download files."),
    (12, None,
     "'You are right, sit down at my desk!' Mathias invites her to use his personal computer. "
     "The imperative 'assieds-toi' invites someone to take a seat."),
    (13, None,
     "'Shall we drink to it? I will get something to drink!' Mathias heads to the kitchen to celebrate the moment. "
     "The informal verb 'trinquer' means to clink glasses in celebration."),
]

OUTRO = (
    "Deeply touched by Camille's decision, Mathias leads her to his computer and goes to fetch drinks. "
    "As she sits down at his desk, Camille is left alone in front of his open screen. "
    "Now let's listen to the complete discussion once more."
)

CLOSING = ("lea", "Merci, papa.")
