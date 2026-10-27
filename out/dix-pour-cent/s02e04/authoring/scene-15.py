# Authoring module for dix-pour-cent s02e04 scene 15 (cues 395-425).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e04/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s02e04/scene-15.json

ID = "dix-pour-cent-s02e04-scene-15"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 15
TITLE = "La manifestation  (Anti-Hartman Protest)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "sacha": "theo", "andrea": "emilie"}
LABELS = {"lea": "Camille", "sacha": "Sacha", "andrea": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 395-425. Outside the radio studio, angry protesters gather. "
    "Camille alerts Andréa and quickly puts Sacha into a taxi to prevent a hostile encounter with Mathias and Isabelle."
)

INTRO = (
    "Outside the radio building, an angry crowd of conservative demonstrators gathers to protest against Sacha Hartman's movie. "
    "Learning that Mathias and Isabelle are on their way, Camille coordinates with Andrea to hurry the director into a waiting cab. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Non, Camille. Vous faites erreur.",
     "No, Camille. You are mistaken.",
     [(397, "Non, Camille")], ""),
    ("lea", "Mathias vient ici avec Isabelle Adjani.",
     "Mathias is coming here with Isabelle Adjani.",
     [(400, "avec Isabelle Adjani au studio radio")], ""),
    ("lea", "Je dois trouver un moyen d'éloigner Hartman.",
     "I must find a way to get Hartman away.",
     [(402, "Je dois trouver un moyen"), (403, "d'éloigner Hartman")], ""),
    ("sacha", "Donne-moi les clés de la voiture.",
     "Give me the car keys.",
     [(405, "donne-moi les clés")], ""),
    ("lea", "Tu es sûre de vouloir conduire?",
     "Are you sure you want to drive?",
     [(406, "Tu es sûre")], ""),
    ("sacha", "Regarde dehors! C'est quoi ça?",
     "Look outside! What is that?",
     [(409, "C'est quoi ça")], ""),
    ("lea", "C'est une manifestation anti-Hartman.",
     "It is an anti-Hartman demonstration.",
     [(411, "Une manifestation anti-Hartman")], ""),
    ("sacha", "Ils ne sont pas très accueillants.",
     "They are not very welcoming.",
     [(413, "Pas très accueillants")], ""),
    ("lea", "Ils cherchent la bagarre.",
     "They are looking for a fight.",
     [(414, "ils cherchent la bagarre")], ""),
    ("andrea", "Camille? Des militants sont devant le studio.",
     "Camille? Activists are in front of the studio.",
     [(417, "sont devant le studio")], ""),
    ("andrea", "Si Sacha les voit, ça va dégénérer.",
     "If Sacha sees them, things will escalate.",
     [(420, "ça va dégénérer")], ""),
    ("andrea", "Bon, sors par derrière avec lui.",
     "Right, sneak out the back with him.",
     [(421, "sors par derrière")], ""),
    ("lea", "Je t'envoie un taxi tout de suite.",
     "I am sending you a taxi right now.",
     [(422, "Je t'envoie un taxi")], ""),
    ("sacha", "Merci beaucoup, Camille!",
     "Thank you very much, Camille!",
     [(422, "Merci, Camille")], ""),
    ("sacha", "Je monte dans ce taxi.",
     "I am getting into this taxi.",
     [(422, "Je t'envoie un taxi")], "adapted cab boarding")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'No, Camille. You are mistaken.' Camille corrects Mathias on the surprise phone call. "
     "The verbal idiom faire erreur polite defers identity confusion."),
    (1, None,
     "'Mathias is coming here with Isabelle Adjani.' She realizes an ambush is underway. "
     "The present tense of venir expresses immediate imminent arrival."),
    (2, None,
     "'I must find a way to get Hartman away.' Camille plans rapid evasive action. "
     "The semi-auxiliary devoir governs an infinitive phrase of necessity."),
    (3, None,
     "'Give me the car keys.' Sacha impatiently asks for their vehicle. "
     "The imperative combines the verb donner with attached object pronoun."),
    (4, None,
     "'Are you sure you want to drive?' Camille hesitates to hand over vehicle control. "
     "The adjective follows the second-person singular copula."),
    (5, None,
     "'Look outside! What is that?' Sacha spots commotion on the street below. "
     "The colloquial interrogative c'est quoi questions visual phenomena."),
    (6, None,
     "'It is an anti-Hartman demonstration.' Camille identifies the hostile crowd. "
     "The compound prefix attaches directly to the director name."),
    (7, None,
     "'They are not very welcoming.' Sacha dryly observes the vocal protesters. "
     "The negative frame modifies the plural descriptive adjective."),
    (8, None,
     "'They are looking for a fight.' Camille warns of imminent danger outside. "
     "The verbal phrase signifies seeking physical confrontation."),
    (9, None,
     "'Camille? Activists are in front of the studio.' Andrea calls with alarming updates. "
     "The spatial preposition locates the demonstrators relative to the entrance."),
    (10, None,
     "'If Sacha sees them, things will escalate.' Andrea fears an explosive public scene. "
     "The conditional clause predicts uncontrolled escalation."),
    (11, None,
     "'Right, sneak out the back with him.' Andrea gives clear tactical escape directions. "
     "The imperative of sortir specifies an emergency rear exit."),
    (12, None,
     "'I am sending you a taxi right now.' Camille arranges a swift getaway car. "
     "The temporal phrase emphasizes rapid transport coordination."),
    (13, None,
     "'Thank you very much, Camille!' Sacha expresses heartfelt relief at her quick thinking. "
     "The polite expression conveys heartfelt gratitude."),
    (14, None,
     "'I am getting into this taxi.' The director safely steps into the vehicle. "
     "The prepositional verb signifies boarding the vehicle.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Thanks to Camille's quick reflexes and Andrea's warning, Sacha slips safely into a taxi before Mathias and Isabelle arrive. "
    "Listen to the French scene once more."
)

CLOSING = ("lea", "Mission accomplie, Andréa.")
