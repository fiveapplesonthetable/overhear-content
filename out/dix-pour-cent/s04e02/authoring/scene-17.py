# Authoring module for dix-pour-cent s04e02 scene 17 (cues 844-880).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-17.py --out out/dix-pour-cent/s04e02/scene-17.json

ID = "dix-pour-cent-s04e02-scene-17"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 17
TITLE = "La zone de confort  (The Comfort Zone)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "franck": "theo"}
LABELS = {"lea": "Dylan", "franck": "Franck"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 844-880. In a quiet corner at the party, young César winner Dylan confesses his imposter syndrome "
    "and fear of taking on different roles. Veteran comic Franck Dubosc shares his own bizarre beginnings to inspire Dylan."
)

INTRO = (
    "In a quiet corner at the apartment gathering, young actor Dylan opens up to veteran entertainer Franck Dubosc. "
    "Paralyzed by self-doubt and imposter syndrome after his early success, Dylan listens as Franck shares the strange, unpredictable path of his own career. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Je dois travailler ma diction.",
     "I have to work on my diction.",
     [(844, "travailler ma diction")], "Dylan laments his spoken delivery"),
    ("franck", "Pardon? Tout le monde te comprend.",
     "Excuse me? Everyone understands you.",
     [(845, "Pardon")], "Franck dismisses the worry"),
    ("lea", "Je ne suis pas vraiment acteur.",
     "I am not really an actor.",
     [(848, "pas vraiment acteur")], "Dylan expresses imposter syndrome"),
    ("franck", "Tu as gagné un beau César!",
     "You won a fine Cesar!",
     [(850, "valu ton César")], "Franck reminds him of his official prize"),
    ("lea", "J'ai seulement eu de la chance.",
     "I only got lucky.",
     [(849, "eu de la chance")], "Dylan downplays his talent"),
    ("franck", "Tu as des milliers de propositions.",
     "You have thousands of offers.",
     [(851, "milliers de propositions")], "Franck cites his high industry demand"),
    ("lea", "Je flippe pour mon avenir.",
     "I am terrified for my future.",
     [(853, "je flippe")], "Dylan admits his deep anxiety"),
    ("franck", "Tu restes dans ta zone confortable.",
     "You stay in your comfort zone.",
     [(861, "zone de confort")], "Franck diagnoses the psychological block"),
    ("lea", "Comment as-tu commencé ce métier?",
     "How did you start this profession?",
     [(864, "comment j'ai commencé")], "Dylan asks about Franck's beginnings"),
    ("franck", "J'étais assistant pour un magicien!",
     "I was assistant to a magician!",
     [(869, "assistant d'un magicien")], "Franck shares his humble bizarre start"),
    ("lea", "Et tu as toujours peur?",
     "And are you still afraid?",
     [(873, "encore la trouille")], "Dylan checks if stage fright ever fades"),
    ("franck", "J'ai encore la trouille parfois.",
     "I still get terrified sometimes.",
     [(873, "encore la trouille")], "Franck admits lasting vulnerability"),
    ("franck", "Il ne faut jamais hésiter d'essayer.",
     "You must never hesitate to try.",
     [(874, "peur d'essayer")], "Franck gives vital artistic advice"),
    ("lea", "Merci Franck, ce conseil me rassure.",
     "Thank you Franck, this advice reassures me.",
     [(878, "très important")], "Dylan feels genuinely comforted")
]

WALK = [
    (0, None,
     "'I have to work on my diction.' Dylan worries about his vocal articulation. "
     "The modal verb 'dois' conveys an obligation to improve."),
    (1, None,
     "'Excuse me? Everyone understands you.' Franck brushes aside Dylan's self-criticism. "
     "The present verb 'comprend' reassures clarity of speech."),
    (2, None,
     "'I am not really an actor.' Dylan feels fraudulent despite his accolades. "
     "The negative structure 'ne... pas' minimizes personal identity."),
    (3, None,
     "'You won a fine Cesar!' Franck points to Dylan's prestigious award. "
     "The past tense 'as gagne' highlights earned recognition."),
    (4, None,
     "'I only got lucky.' Dylan attributes his success to sheer coincidence. "
     "The verbal idiom 'avoir de la chance' means to be fortunate."),
    (5, None,
     "'You have thousands of offers.' Franck reminds him of numerous script invitations. "
     "The noun 'propositions' refers to professional film offers."),
    (6, None,
     "'I am terrified for my future.' Dylan confesses his dread of taking risks. "
     "The colloquial verb 'flipper' means to freak out or panic."),
    (7, None,
     "'You stay in your comfort zone.' Franck analyzes Dylan's protective instincts. "
     "The noun phrase 'zone confortable' indicates safe familiarity."),
    (8, None,
     "'How did you start this profession?' Dylan seeks guidance from Franck's journey. "
     "The compound past 'as commence' asks about early professional steps."),
    (9, None,
     "'I was assistant to a magician!' Franck recounts his colorful early career. "
     "The noun 'magicien' evokes theatrical illusion work."),
    (10, None,
     "'And are you still afraid?' Dylan wonders if experience banishes anxiety. "
     "The adverb 'toujours' inquires about continuous feelings of fear."),
    (11, None,
     "'I still get terrified sometimes.' Franck normalizes fear as part of acting. "
     "The colloquial idiom 'avoir la trouille' means to be scared stiff."),
    (12, None,
     "'You must never hesitate to try.' Franck urges creative fearlessness. "
     "The impersonal expression 'il ne faut jamais' sets a universal rule."),
    (13, None,
     "'Thank you Franck, this advice reassures me.' Dylan gains fresh courage. "
     "The verb 'rassure' denotes restoring emotional confidence.")
]

OUTRO = (
    "Franck Dubosc's candid humility helps Dylan see that vulnerability and fear are part of every actor's path. "
    "Reassured by Franck's words, Dylan finds the confidence to embrace new challenges. "
    "Now let's listen to the scene one last time in French."
)

CLOSING = ("lea", "Merci Franck, ce conseil me rassure.")
