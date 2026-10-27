# Authoring module for dix-pour-cent s04e05 scene 19 (cues 744-773).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e05/authoring/scene-19.py --out overhear-content/out/dix-pour-cent/s04e05/scene-19.json

ID = "dix-pour-cent-s04e05-scene-19"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 19
TITLE = "Le couple improbable  (The Improbable Couple)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "guillaume": "theo"}
LABELS = {"lea": "Sigourney", "guillaume": "Guillaume"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 744-773. Paparazzi spot Sigourney Weaver with Gaspard Ulliel near the Eiffel Tower, while director "
    "Guillaume explains to Gabriel that he reversed the film's roles before learning the distributor has pulled out."
)

INTRO = (
    "After seeing Sigourney Weaver with young actor Gaspard Ulliel, director Guillaume decides to switch the roles in his movie. "
    "However, when Sigourney joins him at a cafe, they learn that the distributor has abruptly pulled out. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("guillaume", "Qu'est-ce qu'elle fait là-bas?",
     "What is she doing over there?",
     [(744, "Qu'est-ce qu'elle fait")], "Guillaume watches Sigourney on the bridge"),
    ("guillaume", "Elle s'achète une tour Eiffel?",
     "Is she buying herself an Eiffel Tower?",
     [(745, "Elle s'achète une miniature de la tour Eiffel")], "Guillaume notices her souvenir"),
    ("guillaume", "J'ai changé d'avis pour le film.",
     "I changed my mind about the movie.",
     [(752, "J'ai changé d'avis")], "Guillaume announces his new vision"),
    ("guillaume", "Sigourney va jouer avec Gaspard Ulliel!",
     "Sigourney will act with Gaspard Ulliel!",
     [(751, "Sigourney Weaver et Gaspard Ulliel")], "Guillaume explains the new pairing"),
    ("guillaume", "Le sujet, c'est l'amour, non?",
     "The subject is love, is it not?",
     [(756, "Le sujet, c'est l'amour, non")], "Guillaume defends his artistic choice"),
    ("lea", "Bonjour Guillaume! Comment allez-vous?",
     "Hello Guillaume! How are you doing?",
     [(759, "Bonjour"), (760, "Comment allez-vous")], "Sigourney joins them at the café"),
    ("guillaume", "Bonjour Sigourney! Pas trop fatiguée?",
     "Hello Sigourney! Not too tired?",
     [(760, "Sigourney. Comment allez-vous ? Pas trop fatiguée")], "Guillaume greets his star warmly"),
    ("lea", "Fatiguée? Pourquoi? Pas du tout!",
     "Tired? Why? Not at all!",
     [(761, "Fatiguée ? Pourquoi"), (767, "Pas du tout")], "Sigourney replies with energy"),
    ("lea", "Un espresso très serré, s'il vous plaît.",
     "A very strong espresso, please.",
     [(762, "Un espresso s'il vous plaît. Très serré")], "Sigourney orders her coffee"),
    ("guillaume", "J'ai une mauvaise nouvelle, je suis désolé.",
     "I have bad news, I am sorry.",
     [(770, "Je suis désolé")], "Guillaume receives a phone call"),
    ("guillaume", "Le distributeur s'est retiré du projet.",
     "The distributor pulled out of the project.",
     [(771, "Le distributeur s'est retiré")], "Guillaume shares the setback"),
    ("lea", "Quoi? Il refuse d'inverser les rôles?",
     "What? He refuses to switch the roles?",
     [], "Sigourney is indignant"),
    ("lea", "Laissez-moi aller me changer!",
     "Let me go change my clothes!",
     [(772, "Laissez-moi aller me changer")], "Sigourney takes charge of the situation"),
    ("guillaume", "Sigourney, vraiment? Qu'allez-vous faire?",
     "Sigourney, really? What are you going to do?",
     [(773, "Sigourney. Vraiment")], "Guillaume looks at her in amazement"),
]

WALK = [
    (0, None,
     "'What is she doing over there?' Guillaume spots Sigourney standing on the footbridge. "
     "The adverb 'la-bas' points to a location over there."),
    (1, None,
     "'Is she buying herself an Eiffel Tower?' Guillaume is amused to see her shopping for trinkets. "
     "The reflexive verb 's'acheter' means to buy for oneself."),
    (2, None,
     "'I changed my mind about the movie.' Guillaume tells Gabriel that he is revising the script. "
     "The idiom 'changer d'avis' means to change one's mind."),
    (3, None,
     "'Sigourney will act with Gaspard Ulliel!' Guillaume pairs the American icon with the young French star. "
     "The near future 'va jouer' expresses an upcoming plan."),
    (4, None,
     "'The subject is love, is it not?' Guillaume argues that romance transcends age differences. "
     "The tag question 'non' seeks agreement at the end of a clause."),
    (5, None,
     "'Hello Guillaume! How are you doing?' Sigourney arrives at the cafe table in high spirits. "
     "The polite inquiry 'comment allez-vous' asks how someone is."),
    (6, None,
     "'Hello Sigourney! Not too tired?' Guillaume checks on his leading lady after her outing. "
     "The feminine adjective 'fatiguee' means tired."),
    (7, None,
     "'Tired? Why? Not at all!' Sigourney brushes off any suggestion of fatigue. "
     "The emphatic phrase 'pas du tout' means not at all."),
    (8, None,
     "'A very strong espresso, please.' Sigourney orders a concentrated coffee from the waiter. "
     "In cafe culture, 'serre' describes a short, strong espresso."),
    (9, None,
     "'I have bad news, I am sorry.' Guillaume hangs up his phone with a worried look. "
     "The noun phrase 'une mauvaise nouvelle' means bad news."),
    (10, None,
     "'The distributor pulled out of the project.' Guillaume explains that their financier backed out. "
     "The reflexive verb 'se retirer' means to withdraw."),
    (11, None,
     "'What? He refuses to switch the roles?' Sigourney realizes the distributor doubts an older leading woman. "
     "The verb 'inverser' means to reverse or switch."),
    (12, None,
     "'Let me go change my clothes!' Sigourney decides to confront the distributor in person. "
     "The reflexive infinitive 'me changer' means to change clothes."),
    (13, None,
     "'Sigourney, really? What are you going to do?' Guillaume is astonished by her bold determination. "
     "The inverted question 'qu'allez-vous faire' asks what are you going to do."),
]

OUTRO = (
    "Refusing to let the film fall apart, Sigourney Weaver prepares to confront the distributor directly. "
    "With Guillaume in tow, she sets out to prove that her romantic lead is completely believable. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Suivez-moi!")
