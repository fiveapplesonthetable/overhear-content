# Authoring module for dix-pour-cent s04e04 scene 13 (cues 897-926).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s04e04/scene-13.json

ID = "dix-pour-cent-s04e04-scene-13"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 13
TITLE = "L'audition manquée  (The Missed Audition)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "sofia": "emilie"}
LABELS = {"lea": "Camille", "sofia": "Sofia"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 897-926. Returning to her office, Camille is furious to discover that Sofia "
    "skipped a crucial audition with director Paul Verhoeven on a friend's advice. The argument "
    "escalates when Camille realizes Sofia also borrowed and stretched out her brand-new designer shoes."
)

INTRO = (
    "Camille returns to her office to find Sofia lounging comfortably after her photoshoot. "
    "What begins as casual office gossip quickly turns into a heated argument when Camille asks about Sofia's major film audition. "
    "Let's listen to their confrontation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("sofia", "Camille, Gabriel et Sarah se disputent!",
     "Camille, Gabriel and Sarah are arguing!",
     [(901, "c'est la crise"), (903, "se sont disputés")], "Sofia gossips about Gabriel and Sarah"),
    ("lea", "Quoi? Ce n'est pas mon problème.",
     "What? That is not my problem.",
     [(902, "Quoi")], "Camille dismisses the gossip"),
    ("lea", "Tu as mis ça pour l'audition?",
     "Did you wear that for the audition?",
     [(904, "Tu as mis ça pour l'audition")], "Camille asks about Sofia's outfit"),
    ("sofia", "Non, je ne suis pas allée.",
     "No, I did not go.",
     [(905, "j'y suis pas allée")], "Sofia admits she skipped the audition"),
    ("lea", "Pardon? Tu as manqué le rendez-vous?",
     "Excuse me? You missed the appointment?",
     [(905, "Pardon"), (909, "l'audition")], "Camille is stunned"),
    ("sofia", "Il y a une projection bientôt.",
     "There is a screening soon.",
     [(908, "Il y a une projection")], "Sofia offers an excuse"),
    ("sofia", "C'est beaucoup mieux comme ça.",
     "It is much better like that.",
     [(908, "c'est mieux comme ça")], "Sofia claims her plan is better"),
    ("lea", "J'ai travaillé dur pour ce rôle!",
     "I worked hard for this role!",
     [(920, "Le temps que j'ai passé")], "Camille reminds her of the effort"),
    ("lea", "Attends, ce sont mes chaussures neuves?",
     "Wait, are those my new shoes?",
     [(911, "mes Louboutin"), (913, "elles sont à moi")], "Camille spots her shoes on Sofia's feet"),
    ("sofia", "Je les ai prises pour la photo.",
     "I took them for the photo.",
     [(914, "je les ai prises")], "Sofia admits borrowing them"),
    ("lea", "Tu ne veux pas travailler, Sofia!",
     "You do not want to work, Sofia!",
     [(921, "tu veux pas travailler")], "Camille accuses her of not caring"),
    ("lea", "Tu ne veux pas être actrice.",
     "You do not want to be an actress.",
     [(922, "Tu veux pas être actrice")], "Camille questions her ambition"),
    ("lea", "Maintenant, reprends tes affaires et sors!",
     "Now, take back your things and get out!",
     [(924, "reprends tes chaussures")], "Camille orders her to return the shoes"),
    ("sofia", "Voilà, je te rends tes chaussures!",
     "There, I give you back your shoes!",
     [(925, "rends-les"), (925, "Voilà")], "Sofia hands back the shoes"),
]

WALK = [
    (0, None,
     "'Camille, Gabriel and Sarah are arguing!' Sofia eagerly shares the latest hallway drama. "
     "The reciprocal verb 'se disputer' means to argue or quarrel."),
    (1, None,
     "'What? That is not my problem.' Camille brushes aside the gossip to focus on business. "
     "The negative 'ce n'est pas' means that is not."),
    (2, None,
     "'Did you wear that for the audition?' Camille points in disbelief at Sofia's extravagant golden dress. "
     "The past participle 'mis' comes from 'mettre', meaning to put on or wear."),
    (3, None,
     "'No, I did not go.' Sofia casually reveals that she skipped the meeting with the director. "
     "In the past tense with 'etre', the participle 'allee' agrees with a feminine speaker."),
    (4, None,
     "'Excuse me? You missed the appointment?' Camille can hardly believe what she is hearing. "
     "The verb 'manquer' means to miss an event or appointment."),
    (5, None,
     "'There is a screening soon.' Sofia claims she will meet the director casually at a movie screening instead. "
     "The feminine noun 'projection' refers to a film screening."),
    (6, None,
     "'It is much better like that.' Sofia defends her spontaneous strategy. "
     "The adverb 'mieux' is the comparative form meaning better."),
    (7, None,
     "'I worked hard for this role!' Camille reminds Sofia how much effort went into securing the casting call. "
     "Employed as an adverb, 'dur' means hard or intensely."),
    (8, None,
     "'Wait, are those my new shoes?' Camille suddenly notices her own designer heels on Sofia's feet. "
     "The feminine plural adjective 'neuves' means brand-new."),
    (9, None,
     "'I took them for the photo.' Sofia confesses that she borrowed the shoes from Camille's office without asking. "
     "The participle 'prises' agrees in gender and number with the preceding pronoun 'les'."),
    (10, None,
     "'You do not want to work, Sofia!' Camille loses her temper at her client's unprofessional attitude. "
     "The infinitive 'travailler' follows the negated verb 'vouloir'."),
    (11, None,
     "'You do not want to be an actress.' Camille accuses Sofia of preferring celebrity glamour over real acting. "
     "In French, professions after 'etre' omit the indefinite article."),
    (12, None,
     "'Now, take back your things and get out!' Camille demands her shoes back and orders Sofia to leave. "
     "The imperative 'sors' comes from the verb 'sortir'."),
    (13, None,
     "'There, I give you back your shoes!' Sofia angrily kicks off the heels and storms out of the room. "
     "The verb 'rendre' means to return or give back."),
]

OUTRO = (
    "Sofia marches out of the office barefoot, leaving Camille furious and exhausted. "
    "Looking down at her stretched-out designer shoes, Camille wonders how to salvage her client's career. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Tu as tout abîmé aujourd'hui!")
