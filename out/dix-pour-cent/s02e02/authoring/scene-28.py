# Authoring module for dix-pour-cent s02e02 scene 28 (cues 922-942).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-28.py --out out/dix-pour-cent/s02e02/scene-28.json

ID = "dix-pour-cent-s02e02-scene-28"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 28
TITLE = "La nouvelle agente de Fabrice  (Fabrice's New Agent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "fabrice": "theo", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "fabrice": "Fabrice", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 922-942. At her desk, Andréa receives an unexpected phone call from star actor Fabrice Luchini. "
    "Amused by her bold bluff with the fake James Bond casting and grateful for her encouragement, "
    "Fabrice decides to sign with her as his new agent, saving her position at ASK under Hicham's watchful eye."
)

INTRO = (
    "Sitting at her agency desk after a chaotic bluff involving a fake James Bond casting call, Andrea receives an unexpected phone call from star actor Fabrice Luchini. "
    "Amused by her daring tactics and grateful for her romantic encouragement, the eccentric actor announces that he wants her as his new agent, right as agency boss Hicham looks on in approval. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Allô?", "Hello?",
     [(922, "Allô")], "Andréa answers her mobile phone"),
    ("fabrice", "Bonjour, Andréa. C'est Fabrice Luchini.", "Hello, Andréa. This is Fabrice Luchini.",
     [(922, "Bonjour, Andréa"), (923, "C'est Fabrice Luchini")], ""),
    ("lea", "Bonjour, Fabrice. Vous allez bien?", "Hello, Fabrice. Are you well?",
     [(923, "Bonjour, Fabrice"), (924, "Vous allez bien")], ""),
    ("fabrice", "Très bien. Je voulais juste vous dire...", "Very well. I just wanted to tell you...",
     [(924, "Très bien"), (925, "Je voulais juste vous dire")], ""),
    ("fabrice", "J'ai rendez-vous avec elle ce soir.", "I have a date with her tonight.",
     [(926, "j'ai rendez-vous avec elle ce soir")], "mentioning the woman from the night before"),
    ("lea", "C'est formidable, je suis vraiment contente pour vous.", "That's wonderful, I am really happy for you.",
     [(928, "C'est formidable, je suis vraiment contente pour vous")], ""),
    ("fabrice", "Grâce à vous! Vous m'avez revigoré.", "Thanks to you! You have revitalized me.",
     [(929, "Grâce à vous"), (931, "Vous m'avez revigoré")], ""),
    ("fabrice", "Je trouve ça drôle. Vous êtes une joueuse, et c'est rare.", "I find it funny. You are a gambler, and that is rare.",
     [(932, "je trouve ça drôle"), (933, "Vous êtes une joueuse, et c'est rare")], ""),
    ("lea", "Merci.", "Thank you.",
     [(934, "Merci")], ""),
    ("fabrice", "Ce serait un plaisir de les découvrir avec vous.", "It would be a pleasure to discover them with you.",
     [(937, "ce serait un plaisir de les découvrir avec vous")], ""),
    ("lea", "Merci pour votre appel, Fabrice.", "Thank you for your call, Fabrice.",
     [(938, "Merci pour votre appel, Fabrice")], ""),
    ("fabrice", "Prenez soin de vous... Ma Nouvelle Agente.", "Take care of yourself... My New Agent.",
     [(939, "Prenez soin de vous"), (939, "Ma Nouvelle Agente")], ""),
    ("lea", "À bientôt, Fabrice.", "See you soon, Fabrice.",
     [(940, "À bientôt")], "adapted greeting"),
    ("fabrice", "À bientôt.", "Talk to you soon.",
     [(940, "À bientôt")], ""),
    ("hicham", "Bravo, Martel.", "Well done, Martel.",
     [(941, "Bravo, Martel")], "Hicham smiles from the doorway"),
    ("hicham", "Je savais que vous en étiez capable.", "I knew you were capable of it.",
     [(942, "Je savais que vous en étiez capable")], ""),
]

OPENER = "Let's walk through the phone call of Fabrice Luchini step by step."

WALK = [
    (0, None,
     "'Hello?' Andrea answers her mobile phone at the agency."),
    (1, None,
     "'Hello, Andrea. This is Fabrice Luchini.' Fabrice identifies himself warmly."),
    (2, None,
     "'Hello, Fabrice. Are you well?' Andrea uses the polite question form."),
    (3, None,
     "'Very well. I just wanted to tell you...' The imperfect 'voulais' softens the request."),
    (4, None,
     "'I have a date with her tonight.' The fixed idiom 'avoir rendez-vous' means to have an appointment."),
    (5, None,
     "'That's wonderful, I am really happy for you.' The feminine adjective 'contente' agrees with Andrea."),
    (6, None,
     "'Thanks to you! You have revitalized me.' The preposition 'grace a' introduces a positive cause."),
    (7, None,
     "'I find it funny. You are a gambler, and that is rare.' The noun 'joueuse' praises Andrea's boldness."),
    (8, None,
     "'Thank you.' Andrea accepts his flattering compliment."),
    (9, None,
     "'It would be a pleasure to discover them with you.' The conditional 'serait' expresses polite desire."),
    (10, None,
     "'Thank you for your call, Fabrice.' Andrea thanks him for reaching out directly."),
    (11, None,
     "'Take care of yourself... My New Agent.' The imperative 'prenez soin de vous' is a caring farewell."),
    (12, None,
     "'See you soon, Fabrice.' Andrea says goodbye to her prestigious new client."),
    (13, None,
     "'Talk to you soon.' Fabrice returns the farewell before hanging up."),
    (14, None,
     "'Well done, Martel.' Hicham steps in to congratulate his daring agent."),
    (15, None,
     "'I knew you were capable of it.' The imperfect verbs 'savais' and 'etiez' reflect past confidence."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "By winning over Fabrice Luchini with her boldness, Andrea saves her position at ASK and earns the hard-won respect of new majority shareholder Hicham Janowski."
CLOSING = ("hicham", "Je savais que vous en étiez capable.")
