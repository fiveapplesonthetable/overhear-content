# Authoring module for dix-pour-cent s03e05 scene 20 (cues 793-828).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-20.py --out overhear-content/out/dix-pour-cent/s03e05/scene-20.json

ID = "dix-pour-cent-s03e05-scene-20"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 20
TITLE = "Visite nocturne  (Late Night Visit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "carlotta": "emilie"}
LABELS = {"lea": "Andréa", "hicham": "Hicham", "carlotta": "Carlotta"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 793-828. After a painful phone argument with his ex-wife Carlotta regarding their son Elvis, "
    "a vulnerable Hicham visits Andréa late at night to see and hold his newborn daughter."
)

INTRO = (
    "After an upsetting phone argument with his ex-wife about their son, "
    "Hicham visits Andrea's apartment late at night. "
    "Seeking comfort, he asks to hold his newborn baby daughter. "
    "Listen to the scene in French first."
)

STORY = [
    ("hicham", "Je voulais juste parler à Elvis.",
     "I just wanted to speak to Elvis.",
     [(794, "envie de parler à Elvis")], ""),
    ("carlotta", "Pour ce week-end, il ne viendra pas.",
     "For this weekend, he will not come.",
     [(797, "pour ce week-end il viendra pas")], ""),
    ("hicham", "Comment ça, il ne viendra pas?",
     "What do you mean, he will not come?",
     [(798, "Comment ça il viendra pas")], ""),
    ("carlotta", "Il a un match samedi, c'est important.",
     "He has a game on Saturday, it is important.",
     [(799, "match samedi c'est important")], ""),
    ("hicham", "C'est mon week-end avec lui, Carlotta!",
     "It is my weekend with him, Carlotta!",
     [(800, "C'est mon week-end Carlotta")], ""),
    ("carlotta", "Il ne veut pas venir à Paris.",
     "He does not want to come to Paris.",
     [(809, "il aime pas venir te voir à Paris")], ""),
    ("hicham", "Moi, je fais tout pour lui!",
     "As for me, I do everything for him!",
     [(816, "je fais tout pour lui")], ""),
    ("hicham", "Bonsoir, Andréa. Je peux entrer un instant?",
     "Good evening, Andrea. May I come in for a moment?",
     [(824, "Je peux entrer")], ""),
    ("lea", "Il est trop tard pour parler boulot.",
     "It is too late to talk work.",
     [(825, "il est trop tard pour parler boulot")], ""),
    ("hicham", "Je ne suis pas là pour travailler.",
     "I am not here to work.",
     [(826, "pas là pour parler boulot")], ""),
    ("hicham", "S'il te plaît. Je peux voir la petite?",
     "Please. May I see the little one?",
     [(827, "je peux voir un peu la petite")], ""),
    ("lea", "Elle dort tranquillement dans son berceau.",
     "She is sleeping peacefully in her crib.",
     [(827, "la petite")], ""),
    ("hicham", "Est-ce que je peux la prendre?",
     "May I hold her?",
     [(828, "peux la garder un peu")], ""),
    ("lea", "Oui, tiens-la doucement contre toi.",
     "Yes, hold her gently against you.",
     [(828, "comme ça")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'I just wanted to speak to Elvis.' Hicham explains why he called his ex-wife. "
     "The imperfect tense expresses his simple intention."),
    (1, None,
     "'For this weekend, he will not come.' Carlotta refuses to send their son over. "
     "The future tense delivers bad news."),
    (2, None,
     "'What do you mean, he will not come?' Hicham reacts with angry disbelief. "
     "The interrogative phrase challenges her statement."),
    (3, None,
     "'He has a game on Saturday, it is important.' Carlotta prioritizes the soccer match. "
     "The adjective justifies the change of plans."),
    (4, None,
     "'It is my weekend with him, Carlotta!' Hicham insists on his parental custody rights. "
     "The exclamation marks his strong frustration."),
    (5, None,
     "'He does not want to come to Paris.' Carlotta delivers a harsh emotional blow. "
     "The negative verb claims the boy made the decision."),
    (6, None,
     "'As for me, I do everything for him!' Hicham defends his dedication as a loving father. "
     "The stressed pronoun asserts his devotion."),
    (7, None,
     "'Good evening, Andrea. May I come in for a moment?' Feeling lonely, he visits his colleague late at night. "
     "The polite question asks for shelter."),
    (8, None,
     "'It is too late to talk work.' Andrea greets him with weary caution. "
     "The impersonal expression sets professional boundaries."),
    (9, None,
     "'I am not here to work.' Hicham denies any professional motive. "
     "The negative sentence reveals personal vulnerability."),
    (10, None,
     "'Please. May I see the little one?' He asks softly to see his newborn daughter. "
     "The polite request expresses paternal tenderness."),
    (11, None,
     "'She is sleeping peacefully in her crib.' Andrea points toward the infant. "
     "The present tense describes the quiet nursery."),
    (12, None,
     "'May I hold her?' Hicham asks for permission to hold the baby girl. "
     "The polite question seeks physical comfort."),
    (13, None,
     "'Yes, hold her gently against you.' Andrea softens and hands him the child. "
     "The imperative verb guides his cautious embrace.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Holding his daughter in his arms brings quiet comfort to Hicham after a difficult evening. "
    "Listen to the conversation once more in French."
)

CLOSING = ("hicham", "Elle est vraiment magnifique, Andréa.")
