# Authoring module for dix-pour-cent s02e02 scene 20 (cues 693-709).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-20.py --out out/dix-pour-cent/s02e02/scene-20.json

ID = "dix-pour-cent-s02e02-scene-20"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 20
TITLE = "Une nuit platonique  (A Platonic Night)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "arlette": "Arlette", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 693-709. Andréa bursts into ASK after spending the entire night talking with Fabrice Luchini. "
    "She announces that Luchini has fired Bréhier and invited her to the theatre, thrilling Arlette and impressing Mathias."
)

INTRO = (
    "Early in the morning at ASK, Andréa arrives looking radiant after an all-night conversation with Fabrice Luchini. "
    "She shares the thrilling breakthrough with Arlette and Mathias: Luchini has broken with rival agent François Bréhier. "
    "Listen to the scene in French first."
)

STORY = [
    ("arlette", "On a passé une folle nuit?",
     "Did we have a wild night?",
     [(693, "On a passé une folle nuit")], ""),
    ("lea", "Exactement! Devinez avec qui.",
     "Exactly! Guess with whom.",
     [(694, "Exactement"), (695, "Devinez avec qui")], ""),
    ("mathias", "Avec qui?",
     "With whom?",
     [(695, "Avec qui")], ""),
    ("lea", "Fabrice Luchini.",
     "None other than Fabrice Luchini.",
     [(696, "Fabrice Luchini")], ""),
    ("mathias", "Non. Il ne fallait pas aller jusque-là.",
     "No. You shouldn't have gone that far.",
     [(696, "Non"), (697, "Il ne fallait pas aller jusque-là")], ""),
    ("lea", "Non... c'était fou et platonique.",
     "No... it was wild and platonic.",
     [(698, "Non... c'était fou et platonique")], ""),
    ("lea", "Il a quitté Bréhier.",
     "He left Bréhier.",
     [(699, "Il a quitté Bréhier")], ""),
    ("arlette", "C'est une excellente nouvelle! J'adore!",
     "That is excellent news! I love it!",
     [(700, "c'est une excellente nouvelle ! J'adore")], "Cleaned 'putain'"),
    ("mathias", "Calme-toi, Arlette.",
     "Calm down, Arlette.",
     [(701, "Calme-toi, Arlette")], ""),
    ("arlette", "Quel rabat-joie!",
     "What a killjoy!",
     [(701, "Quel rabat-joie")], ""),
    ("lea", "On a parlé toute la nuit, j'adore ce type.",
     "We talked all night, I adore this guy.",
     [(702, "On a parlé toute la nuit, j'adore ce type")], ""),
    ("lea", "Je ne veux pas me vanter mais je crois qu'il m'aime bien aussi.",
     "I don't want to brag but I think he likes me too.",
     [(703, "Je ne veux pas me vanter mais je crois qu'il m'aime bien aussi")], ""),
    ("mathias", "Je ne comprends pas. Il a dit oui?",
     "I don't understand. Did he say yes?",
     [(704, "Je ne comprends pas. Il a dit oui")], ""),
    ("lea", "Pas encore, mais il m'a invitée au théâtre ce soir.",
     "Not yet, but he invited me to the theatre tonight.",
     [(705, "Pas encore, mais il m'a invitée au théâtre ce soir")], ""),
    ("lea", "On ne fête pas ça trop vite, mais ça s'annonce bien!",
     "Let's not celebrate too quickly, but it looks promising!",
     [(706, "On ne fête pas ça trop vite, mais ça s'annonce bien")], ""),
    ("lea", "Tu vois, Mathias? Il fallait juste oser.",
     "You see, Mathias? We just had to dare.",
     [(707, "Tu vois, Mathias ? Il fallait juste oser")], ""),
]

OPENER = "Let's explore Andréa's triumphant morning debrief line by line."

WALK = [
    (0, None,
     "'Did we have a wild night?' Arlette teases Andréa's disheveled and glowing appearance. "
     "The phrase passer une nuit means to spend the night."),
    (1, None,
     "'Exactly! Guess with whom.' Andréa hypes up the mystery. "
     "The imperative form devinez commands them to guess."),
    (2, None,
     "'With whom?' Mathias asks with dry skepticism. "
     "The interrogative prepositional phrase uses qui."),
    (3, None,
     "'None other than Fabrice Luchini.' Andréa drops the superstar name triumphantly. "
     "She pauses for dramatic effect."),
    (4, None,
     "'No. You shouldn't have gone that far.' Mathias immediately suspects a scandal. "
     "The impersonal imperfect il fallait describes what was required."),
    (5, None,
     "'No... it was wild and platonic.' Andréa sets the record straight. "
     "The adjectives fou and platonique qualify the experience."),
    (6, None,
     "'He left Bréhier.' She delivers the crucial agency intelligence. "
     "The passé composé uses the auxiliary to have."),
    (7, None,
     "'That is excellent news! I love it!' Arlette rejoices at their rival's loss. "
     "The verb adorer expresses delight."),
    (8, None,
     "'Calm down, Arlette.' Mathias tries to maintain composure. "
     "The reflexive imperative calme-toi uses the informal pronoun."),
    (9, None,
     "'What a killjoy!' Arlette mocks Mathias's perpetual pessimism. "
     "The exclamatory word quel introduces the compound noun rabat-joie."),
    (10, None,
     "'We talked all night, I adore this guy.' Andréa describes their deep mutual connection. "
     "The phrase toute la nuit indicates uninterrupted duration."),
    (11, None,
     "'I don't want to brag but I think he likes me too.' She notes their instant chemistry. "
     "The reflexive verb se vanter means to brag or boast."),
    (12, None,
     "'I don't understand. Did he say yes?' Mathias demands practical confirmation. "
     "The verb to say is in the conversational past tense."),
    (13, None,
     "'Not yet, but he invited me to the theatre tonight.' Andréa reveals her follow-up date. "
     "Because Andréa is female, the past participle invitée takes an extra e."),
    (14, None,
     "'Let's not celebrate too quickly, but it looks promising!' She cautions prudence while staying optimistic. "
     "The pronominal idiom s'annoncer bien means to look promising."),
    (15, None,
     "'You see, Mathias? We just had to dare.' She proudly claims credit for taking the risk. "
     "The verb oser means to dare."),
]

TRANSITION = "Now let's listen to the whole debriefing once more from start to finish."

OUTRO = (
    "Andréa has pulled off a diplomatic masterstroke, opening the door for Luchini to join ASK. "
    "Remember the key verb for taking a bold chance: oser."
)

CLOSING = ("lea", "Tu vois, Mathias? Il fallait juste oser.")
