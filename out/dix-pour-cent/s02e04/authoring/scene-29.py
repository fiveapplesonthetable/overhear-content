# Authoring module for dix-pour-cent s02e04 scene 29 (cues 898-947).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-29.py --out out/dix-pour-cent/s02e04/scene-29.json

ID = "dix-pour-cent-s02e04-scene-29"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 29
TITLE = "Le secret de Mathias  (Mathias's Secret)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 898-947. Confronted by Andrea and Hicham about sabotaging the Sacha Hartman meeting, "
    "Camille is about to be fired. Mathias steps forward, admits orchestrating the sabotage, "
    "and stuns everyone by revealing that Camille is his daughter."
)

INTRO = (
    "In the aftermath of the collapsed meeting, the agency partners corner Camille, demanding answers. "
    "As Hicham threatens to fire her on the spot, Mathias steps in and reveals a life-altering truth. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Camille, donne-moi une explication.", "Camille, give me an explanation.",
     [(898, "Camille"), (900, "Donne-moi une explication")], "Andrea demands an explanation from Camille"),
    ("hicham", "On vient de perdre Sacha Hartman et Isabelle Adjani.", "We have just lost Sacha Hartman and Isabelle Adjani.",
     [(904, "On vient de perdre Sacha Hartman et Isabelle Adjani")], ""),
    ("hicham", "Le vrai problème, c'est Camille.", "The real problem is Camille.",
     [(910, "Le vrai problème"), (911, "c'est Camille")], ""),
    ("lea", "Elle a jeté le scénario à la poubelle.", "She threw the screenplay in the trash.",
     [(916, "elle a jeté"), (917, "le scénario de Sacha à la poubelle")], ""),
    ("hicham", "C'est peut-être une taupe.", "Maybe she is a mole.",
     [(920, "C'est peut-être une taupe")], ""),
    ("hicham", "Au moindre doute, elle dégage.", "At the slightest doubt, she is out.",
     [(923, "Au moindre doute, elle dégage")], ""),
    ("mathias", "C'est moi qui lui ai demandé de mentir.", "I am the one who asked her to lie.",
     [(924, "C'est moi qui lui ai demandé de mentir")], "Mathias steps forward to intervene"),
    ("mathias", "C'est moi qui ai jeté ce script.", "I am the one who threw out this script.",
     [(925, "C'est moi qui ai jeté ce script")], ""),
    ("mathias", "Camille est ma fille.", "Camille is my daughter.",
     [(927, "Camille"), (928, "est ma fille")], ""),
    ("lea", "Pardon? Votre fille?", "Pardon? Your daughter?",
     [(929, "Pardon"), (930, "Votre fille")], ""),
    ("hicham", "Quand comptiez-vous nous le dire?", "When were you planning to tell us?",
     [(932, "Quand comptiez-vous nous le dire")], ""),
    ("mathias", "Le moment venu. Aujourd'hui, apparemment.", "When the time came. Today, apparently.",
     [(933, "Le moment venu"), (934, "Aujourd'hui, apparemment")], ""),
    ("lea", "Elle est là depuis neuf mois!", "She has been here for nine months!",
     [(935, "Elle est là depuis neuf mois")], ""),
    ("lea", "Vous vous êtes bien foutus de nous!", "You really made fools of us!",
     [(940, "Vous vous êtes bien foutus de nous")], ""),
    ("mathias", "J'assume l'entière responsabilité.", "I take full responsibility.",
     [(944, "J'assume l'entière responsabilité")], ""),
    ("mathias", "Si quelqu'un doit partir, c'est moi.", "If someone has to leave, it is me.",
     [(945, "Si quelqu'un doit partir, c'est moi")], ""),
    ("hicham", "Je suis tout à fait d'accord.", "I completely agree.",
     [(946, "Je suis tout à fait d'accord")], ""),
]

OPENER = "Let's walk through the shocking revelation of Mathias step by step."

WALK = [
    (0, None,
     "'Camille, give me an explanation.' Andrea demands answers after the disastrous meeting."),
    (1, None,
     "'We have just lost Sacha Hartman and Isabelle Adjani.' Hicham highlights the catastrophic loss."),
    (2, None,
     "'The real problem is Camille.' Hicham directs everyone's anger toward the young assistant."),
    (3, None,
     "'She threw the screenplay in the trash.' Andrea explains Camille's shocking behavior."),
    (4, None,
     "'Maybe she is a mole.' Hicham suspects corporate espionage from a rival agency."),
    (5, None,
     "'At the slightest doubt, she is out.' Hicham threatens immediate dismissal."),
    (6, None,
     "'I am the one who asked her to lie.' Mathias steps forward and confesses his instructions."),
    (7, None,
     "'I am the one who threw out this script.' Mathias takes personal ownership of the old grudge."),
    (8, None,
     "'Camille is my daughter.' Mathias delivers the stunning revelation that shocks the entire agency."),
    (9, None,
     "'Pardon? Your daughter?' Andrea reacts with utter disbelief and shock."),
    (10, None,
     "'When were you planning to tell us?' Hicham questions the senior agent's secrecy."),
    (11, None,
     "'When the time came. Today, apparently.' Mathias answers with bitter resignation."),
    (12, None,
     "'She has been here for nine months!' Andrea is appalled by how long the secret was kept."),
    (13, None,
     "'You really made fools of us!' Andrea expresses anger over being deceived by her colleague."),
    (14, None,
     "'I take full responsibility.' Mathias refuses to deflect blame onto his daughter."),
    (15, None,
     "'If someone has to leave, it is me.' Mathias offers his own resignation to save Camille."),
    (16, None,
     "'I completely agree.' Hicham coldly accepts the senior partner's departure."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "With Mathias finally admitting that Camille is his secret daughter, the entire balance of power at ASK is turned upside down."
CLOSING = ("hicham", "Je suis tout à fait d'accord.")
