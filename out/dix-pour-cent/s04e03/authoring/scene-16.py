# Authoring module for dix-pour-cent s04e03 scene 16 (cues 784-798).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-16.py --out overhear-content/out/dix-pour-cent/s04e03/scene-16.json

ID = "dix-pour-cent-s04e03-scene-16"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 16
TITLE = "Le dîner écolo  (The Eco Dinner)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 784-798. In their apartment, Noémie prepares a roasted lamb dinner to impress "
    "Mathias's prospective film client, but Mathias casually mentions the guest's wife is a militant vegetarian."
)

INTRO = (
    "In their Parisian apartment kitchen, Noemie Leclerc prepares a roast lamb for an important dinner. "
    "Seeking reassurance from Mathias, her culinary confidence is shattered when he casually mentions their guest is a militant vegetarian. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Regarde, cet agneau est vraiment parfait.",
     "Look, this lamb is truly perfect.",
     [(784, "L'agneau est parfait")], "Noémie checks the roast"),
    ("lea", "Tu crois que sa femme va m'aimer?",
     "Do you think his wife will like me?",
     [(786, "sa femme va m'aimer")], "Noémie seeks reassurance"),
    ("mathias", "Elle va t'adorer, sans aucun doute.",
     "She will adore you, without any doubt.",
     [(786, "Sans aucun doute")], "Mathias reassures her"),
    ("lea", "Et Catherine, qu'aurait-elle préparé?",
     "And Catherine, what would she have prepared?",
     [(787, "Et Catherine"), (788, "servi de l'agneau")], "Noémie compares herself"),
    ("mathias", "Arrête de te comparer à Catherine.",
     "Stop comparing yourself to Catherine.",
     [(790, "Arrête de te comparer")], "Mathias cuts off the comparison"),
    ("mathias", "C'est toi que j'aime passionnément.",
     "It is you that I love passionately.",
     [(791, "C'est toi que j'aime")], "Mathias expresses his love"),
    ("mathias", "Tout va très bien se passer.",
     "Everything will go very well.",
     [(792, "Tout va bien se passer")], "Mathias encourages Noémie"),
    ("lea", "Quels sont ses centres d'intérêt?",
     "What are her areas of interest?",
     [(794, "centres d'intérêt")], "Noémie inquires about their guest"),
    ("mathias", "Elle est très écolo et engagée.",
     "She is very pro-environment and committed.",
     [(795, "Elle est très écolo")], "Mathias explains her passions"),
    ("lea", "C'est-à-dire? Donne-moi un exemple.",
     "That is to say? Give me an example.",
     [(795, "très écolo")], "Noémie asks for details"),
    ("mathias", "Elle défend les espèces menacées.",
     "She defends endangered species.",
     [(796, "espèces en voie d'extinction")], "Mathias mentions causes"),
    ("mathias", "Elle combat la cruauté des abattoirs.",
     "She fights slaughterhouse cruelty.",
     [(797, "cruauté dans les abattoirs")], "Mathias drops the bomb"),
    ("lea", "Tu me dis ça maintenant?",
     "You tell me that now?",
     [(798, "tu me dis ça maintenant")], "Noémie panics"),
    ("lea", "Mon beau rôti est foutu!",
     "My fine roast is ruined!",
     [(798, "tu me dis ça maintenant")], "Noémie despairs"),
]

WALK = [
    (0, None,
     "'Look, this lamb is truly perfect.' Noemie admires the roasted meat she cooked for the guests. "
     "The masculine noun 'agneau' designates lamb."),
    (1, None,
     "'Do you think his wife will like me?' Noemie reveals her nervous desire to make a great impression. "
     "The verb phrase 'va m'aimer' expresses near future."),
    (2, None,
     "'She will adore you, without any doubt.' Mathias offers warm and unconditional encouragement. "
     "The prepositional phrase 'sans aucun doute' means without doubt."),
    (3, None,
     "'And Catherine, what would she have prepared?' Noemie cannot help measuring herself against Mathias's ex-wife. "
     "The conditional verb 'aurait' expresses hypothesis."),
    (4, None,
     "'Stop comparing yourself to Catherine.' Mathias firmly urges Noemie to let go of old ghosts. "
     "The imperative 'arrete de' governs an infinitive verb."),
    (5, None,
     "'It is you that I love passionately.' Mathias reminds Noemie of his romantic devotion. "
     "The emphatic cleft sentence 'c'est toi que' highlights the object."),
    (6, None,
     "'Everything will go very well.' Mathias promises that the dinner will be a great success. "
     "The pronominal verb 'se passer' means to unfold or happen."),
    (7, None,
     "'What are her areas of interest?' Noemie prepares dinner conversation topics in advance. "
     "The plural noun phrase 'centres d'interet' means hobbies or interests."),
    (8, None,
     "'She is very pro-environment and committed.' Mathias shares background on the director's wife. "
     "The shortened colloquial adjective 'ecolo' means environmentalist."),
    (9, None,
     "'That is to say? Give me an example.' Noemie asks for specific details on the guest's causes. "
     "The transitional expression 'c'est-a-dire' requests clarification."),
    (10, None,
     "'She defends endangered species.' Mathias describes the guest's passionate activism. "
     "The feminine noun 'espece' designates a biological species."),
    (11, None,
     "'She fights slaughterhouse cruelty.' Mathias casually mentions that she campaigns against meat production. "
     "The noun 'abattoir' means slaughterhouse."),
    (12, None,
     "'You tell me that now?' Noemie is horrified that she cooked a meat feast for an animal activist. "
     "The adverb 'maintenant' marks present urgency."),
    (13, None,
     "'My fine roast is ruined!' Noemie realizes with despair that her main dish cannot be served. "
     "The colloquial adjective 'foutu' means ruined or wasted."),
]

OUTRO = (
    "Noemie discovers at the very last second that her roasted lamb will offend their vegetarian dinner guest. "
    "Scrambling to save the evening, she and Mathias must improvise an emergency meat-free menu. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("mathias", "On peut encore commander des légumes!")
