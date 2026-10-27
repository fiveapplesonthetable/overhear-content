# Authoring module for dix-pour-cent s04e04 scene 21 (cues 1150-1205).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-21.py --out out/dix-pour-cent/s04e04/scene-21.json

ID = "dix-pour-cent-s04e04-scene-21"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 21
TITLE = "Confidences au bar  (Confidences at the Bar)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie"}
LABELS = {"lea": "Andréa", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1150-1205. Unwinding over drinks at a Parisian bar, Andréa and rival agent Élise form an unexpected bond. "
    "After Élise delays Andréa's nanny so they can stay out, the two agents share hilarious confidential horror stories "
    "about their most demanding celebrity clients."
)

INTRO = (
    "In a relaxed Parisian lounge bar, Andréa and rival agent Elise unwind over cocktails after a grueling week of work. "
    "Letting their professional guard down, the two women trade hilarious confidential anecdotes about their most eccentric clients. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Ma nounou Patsy est vraiment fabuleuse.",
     "My nanny Patsy is really fabulous.",
     [(1150, "Patsy est fabuleuse !")], "Praised her devoted babysitter"),
    ("elise", "Buvons un autre verre toutes les deux.",
     "Let us drink another glass, both of us.",
     [(1156, "On en prend un autre ?")], "Suggested another round of drinks"),
    ("lea", "Je dois rentrer avant minuit ce soir.",
     "I must go home before midnight tonight.",
     [(1157, "j'ai dit à Patsy que je rentrais")], "Mentioned her strict curfew"),
    ("elise", "J'ai prévenu ta nounou par téléphone.",
     "I notified your nanny by phone.",
     [(1159, "Oui, bonjour Patsy, c'est Élise")], "Took matters into her own hands"),
    ("lea", "Tu n'as vraiment peur de rien!",
     "You are truly afraid of nothing!",
     [(1161, "Mais…")], "Marveled at her colleague's audacity"),
    ("elise", "J'éteins mon portable pour la soirée.",
     "I am turning off my phone for the evening.",
     [(1172, "Et j'éteins mon téléphone")], "Cut off work intrusions"),
    ("lea", "Nos acteurs nous épuisent toute la journée.",
     "Our actors exhaust us all day long.",
     [(1178, "On s'occupe d'eux toute la journée")], "Vented about demanding movie stars"),
    ("elise", "Quel est ton client le plus difficile?",
     "Who is your most difficult client?",
     [(1174, "c'est qui le talent le plus pénible ?")], "Prompted an insider trade secret"),
    ("lea", "François Berléand est un hypocondriaque total!",
     "François Berléand is a total hypochondriac!",
     [(1180, "Berléand"), (1181, "C'est un hypocondriaque total")], "Revealed a star's extreme obsession"),
    ("elise", "Raconte-moi un peu ses habitudes bizarres.",
     "Tell me a little about his strange habits.",
     [(1175, "Dis-moi tout !")], "Eagerly requested juicy details"),
    ("lea", "Il panique dès qu'un acteur éternue.",
     "He panics as soon as an actor sneezes.",
     [(1185, "Tu éternues, t'es dehors")], "Shared his germaphobic reaction"),
    ("elise", "C'est tellement drôle et absurde!",
     "It is so funny and absurd!",
     [(1188, "C'est trop fort !")], "Laughed heartily at the anecdote"),
    ("lea", "Nous faisons un métier de fous.",
     "We do a crazy profession.",
     [(1170, "Ça fait partie du boulot")], "Reflected on the madness of talent agency life"),
    ("elise", "Trinquons à notre belle amitié secrète!",
     "Let us toast to our lovely secret friendship!",
     [(1155, "À sainte Patsy !")], "Celebrated their newfound camaraderie"),
]

WALK = [
    (0, None,
     "'My nanny Patsy is really fabulous.' Andréa shows photos of baby Flora on her phone. "
     "The adjective fabuleuse praises her extraordinary child care."),
    (1, None,
     "'Let us drink another glass, both of us.' Elise beckons the waiter for another cocktail. "
     "The imperative verb buvons encourages festive bonding."),
    (2, None,
     "'I must go home before midnight tonight.' Andréa remembers her domestic duties. "
     "The temporal phrase avant minuit ce soir sets a boundary."),
    (3, None,
     "'I notified your nanny by phone.' Elise smiles cheekily after making the call. "
     "The compound past verb ai prévenu signals a bold fait accompli."),
    (4, None,
     "'You are truly afraid of nothing!' Andréa shakes her head with impressed amusement. "
     "The idiomatic phrase n'as peur de rien honors her fearless boldness."),
    (5, None,
     "'I am turning off my phone for the evening.' Elise powers down her screen. "
     "The present verb éteins shows deliberate detachment from work."),
    (6, None,
     "'Our actors exhaust us all day long.' Andréa sighs over the endless celebrity demands. "
     "The present verb épuisent describes heavy emotional fatigue."),
    (7, None,
     "'Who is your most difficult client?' Elise leans across the table with curiosity. "
     "The superlative phrase le plus difficile invites candid honesty."),
    (8, None,
     "'François Berléand is a total hypochondriac!' Andréa spills the hilarious truth. "
     "The descriptive noun phrase un hypocondriaque total evokes comic eccentricity."),
    (9, None,
     "'Tell me a little about his strange habits.' Elise listens with rapt amusement. "
     "The imperative phrase raconte-moi encourages the storytelling."),
    (10, None,
     "'He panics as soon as an actor sneezes.' Andréa details his extreme germ phobia. "
     "The temporal conjunction dès que introduces his instant panic."),
    (11, None,
     "'It is so funny and absurd!' Elise bursts out laughing at the table. "
     "The paired adjectives drôle et absurde capture the bizarre reality of stardom."),
    (12, None,
     "'We do a crazy profession.' Andréa raises her glass with affectionate exasperation. "
     "The colloquial expression un métier de fous summarizes agency life."),
    (13, None,
     "'Let us toast to our lovely secret friendship!' Elise clinks glasses warmly. "
     "The imperative trinquons seals their unexpected sisterhood."),
]

OUTRO = "Andréa and Elise raise their glasses in laughter, united in friendship against the daily chaos of show business."
CLOSING = ("elise", "Trinquons à notre belle amitié secrète!")
