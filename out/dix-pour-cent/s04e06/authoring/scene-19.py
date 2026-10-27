# Authoring module for dix-pour-cent s04e06 scene 19 (cue 849).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e06/authoring/scene-19.py --out overhear-content/out/dix-pour-cent/s04e06/scene-19.json

ID = "dix-pour-cent-s04e06-scene-19"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 19
TITLE = "Le baiser d'adieu  (The Goodbye Kiss)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 849. After Andrea and Colette mutually agree to part ways, Colette looks at Andrea with deep affection. "
    "Surprised that Andrea was finally so completely honest, Colette leans in for a tender, bittersweet goodbye kiss."
)

INTRO = (
    "On the park bench, a gentle silence settles between Andrea Martel and Colette Brancillon after their painful agreement. "
    "Moved by Andrea's unprecedented honesty, Colette shares a tender final kiss that seals their parting with love and respect. "
    "Let's listen to their words in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Tu ne dis rien, Colette?",
     "You say nothing, Colette?",
     [(849, "Tu ne m'as pas répondu...")], "Andrea breaks the quiet pause"),
    ("colette", "J'écoute ce que tu me dis.",
     "I am listening to what you tell me.",
     [(849, "Tu ne m'as pas répondu...")], "Colette reflects on their words"),
    ("lea", "Tu ne m'as pas vraiment répondu.",
     "You did not really answer me.",
     [(849, "Tu ne m'as pas répondu...")], "Andrea notices Colette's deep silence"),
    ("colette", "Regarde-moi dans les yeux, Andréa.",
     "Look at me in the eyes, Andrea.",
     [(849, "Tu ne m'as pas répondu...")], "Colette turns with gentle affection"),
    ("lea", "Je te regarde avec tout mon cœur.",
     "I look at you with all my heart.",
     [(849, "Tu ne m'as pas répondu...")], "Andrea meets her gaze openly"),
    ("colette", "Tu n'as jamais été aussi sincère.",
     "You have never been so sincere.",
     [(849, "Tu ne m'as pas répondu...")], "Colette praises Andrea's courage"),
    ("lea", "Je veux seulement être juste aujourd'hui.",
     "I only want to be fair today.",
     [(849, "Tu ne m'as pas répondu...")], "Andrea expresses her true intention"),
    ("colette", "Laisse-moi t'embrasser une dernière fois.",
     "Let me kiss you one last time.",
     [(849, "Tu ne m'as pas répondu...")], "Colette leans forward softly"),
    ("lea", "C'est un baiser d'adieu?",
     "Is this a goodbye kiss?",
     [(849, "Tu ne m'as pas répondu...")], "Andrea whispers with mixed feelings"),
    ("colette", "C'est un baiser de respect mutuel.",
     "It is a kiss of mutual respect.",
     [(849, "Tu ne m'as pas répondu...")], "Colette defines the gesture's meaning"),
    ("lea", "Je n'oublierai jamais nos moments partagés.",
     "I will never forget our shared moments.",
     [(849, "Tu ne m'as pas répondu...")], "Andrea honors their romance"),
    ("colette", "Moi non plus, chère Andréa.",
     "Me neither, dear Andrea.",
     [(849, "Tu ne m'as pas répondu...")], "Colette reciprocates the sentiment"),
    ("lea", "Merci pour ta tendresse et ton écoute.",
     "Thank you for your tenderness and listening.",
     [(849, "Tu ne m'as pas répondu...")], "Andrea offers gratitude before parting"),
]

WALK = [
    (0, None,
     "'You say nothing, Colette?' Andrea wonders about the long silence between them. "
     "The negative pronoun 'rien' means nothing."),
    (1, None,
     "'I am listening to what you tell me.' Colette reflects on Andrea's thoughtful words. "
     "The verb 'ecoute' comes from 'ecouter', to listen."),
    (2, None,
     "'You did not really answer me.' Andrea notices that Colette has remained quiet. "
     "The compound past 'as repondu' comes from 'repondre'."),
    (3, None,
     "'Look at me in the eyes, Andrea.' Colette turns toward her with warm affection. "
     "The imperative 'regarde-moi' combines the verb with an object pronoun."),
    (4, None,
     "'I look at you with all my heart.' Andrea returns her steady, open gaze. "
     "The noun 'cœur' designates the heart."),
    (5, None,
     "'You have never been so sincere.' Colette appreciates Andrea's absolute emotional truth. "
     "The adjective 'sincere' means honest or candid."),
    (6, None,
     "'I only want to be fair today.' Andrea explains her desire for clear honesty. "
     "The restrictive adverb 'seulement' means only."),
    (7, None,
     "'Let me kiss you one last time.' Colette leans in softly toward Andrea. "
     "The verb 'embrasser' means to kiss."),
    (8, None,
     "'Is this a goodbye kiss?' Andrea whispers softly as their lips touch. "
     "The compound noun 'baiser d'adieu' signifies a parting kiss."),
    (9, None,
     "'It is a kiss of mutual respect.' Colette honors everything they shared together. "
     "The adjective 'mutuel' describes reciprocal feelings."),
    (10, None,
     "'I will never forget our shared moments.' Andrea acknowledges the deep impact of their love. "
     "The future form 'oublierai' comes from 'oublier'."),
    (11, None,
     "'Me neither, dear Andrea.' Colette smiles with peaceful finality. "
     "The phrase 'moi non plus' means me neither."),
    (12, None,
     "'Thank you for your tenderness and listening.' Andrea expresses her heartfelt gratitude. "
     "The noun 'tendresse' translates to tenderness or affection."),
]

OUTRO = (
    "With a gentle kiss and words of gratitude, Andrea and Colette conclude their love story without bitterness. "
    "Ready to build separate lives while raising Flora together, they embrace a brighter future. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("colette", "Prends grand soin de notre fille!")
