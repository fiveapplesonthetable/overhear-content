# Authoring module for dix-pour-cent s02e06 scene 30 (cues 858-882).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-30.py --out out/dix-pour-cent/s02e06/scene-30.json

ID = "dix-pour-cent-s02e06-scene-30"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 30
TITLE = "Je t'aime, Andréa  (I Love You, Andréa)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "colette": "Colette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 858-882. Colette calls Andrea from Paris to apologize, confess her love, and offer to support her. "
    "Moments later, a devastated Gabriel finds Andrea and confesses that Sofia has left him forever."
)

INTRO = (
    "Outside the crowded Cannes party, Andrea receives an unexpected phone call from Colette. "
    "Just as their heartfelt conversation concludes, Gabriel stumbles over in tears with heartbreaking news. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Allô, Colette?", "Hello, Colette?",
     [(858, "Allô")], "Andrea steps away from the party to answer her phone"),
    ("colette", "Je suis désolée pour hier soir.", "I am sorry about last night.",
     [(859, "Je suis désolé pour hier soir")], ""),
    ("colette", "J'ai vraiment dépassé les bornes.", "I really crossed the line.",
     [(859, "j'ai dépassé les bornes")], ""),
    ("lea", "Non, ce n'est rien.", "No, it is nothing.",
     [(860, "Non")], ""),
    ("colette", "Ce n'est pas facile pour toi.", "It is not easy for you.",
     [(861, "Je sais que c'est pas facile pour toi en ce moment")], ""),
    ("colette", "Tu vis quelque chose d'incroyable.", "You are living through something incredible.",
     [(866, "Tu vis quelque chose"), (867, "d'incroyable")], ""),
    ("colette", "Je voulais te dire que je suis là.", "I wanted to tell you that I am here.",
     [(874, "Je voulais juste te dire que je suis là")], ""),
    ("colette", "Je veux le vivre avec toi.", "I want to experience it with you.",
     [(875, "Et je crois que je veux le vivre avec toi")], ""),
    ("colette", "Parce que je t'aime, Andréa.", "Because I love you, Andrea.",
     [(877, "Parce que je t'aime, Andréa")], ""),
    ("lea", "Moi aussi je t'aime, Colette.", "I love you too, Colette.",
     [(878, "Moi aussi je t'aime")], ""),
    ("gabriel", "Sofia est partie!", "Sofia is gone!",
     [(879, "Elle est partie")], "Gabriel stumbles over in deep despair"),
    ("gabriel", "Elle m'a définitivement quitté.", "She definitely left me.",
     [(880, "Elle m'a quitté")], ""),
    ("gabriel", "Elle avait totalement raison.", "She was completely right.",
     [(881, "Elle avait raison")], ""),
    ("gabriel", "Je suis vraiment une ordure!", "I really am a piece of trash!",
     [(882, "Je suis une ordure")], ""),
    ("lea", "Gabriel, calme-toi un peu.", "Gabriel, calm down a little.",
     [(882, "Je suis une ordure")], ""),
]

OPENER = "Let's walk through these two emotional phone and party moments step by step."

WALK = [
    (0, None,
     "'Hello, Colette?' Andrea answers her ringing phone away from the loud music."),
    (1, None,
     "'I am sorry about last night.' Colette opens with a sincere and tender apology."),
    (2, None,
     "'I really crossed the line.' Colette regrets putting unfair pressure on Andrea."),
    (3, None,
     "'No, it is nothing.' Andrea gently reassures her partner."),
    (4, None,
     "'It is not easy for you.' Colette shows deep empathy for Andrea's inner turmoil."),
    (5, None,
     "'You are living through something incredible.' Colette recognizes the magnitude of the pregnancy."),
    (6, None,
     "'I wanted to tell you that I am here.' Colette promises steadfast emotional support."),
    (7, None,
     "'I want to experience it with you.' Colette decides to embrace the journey together."),
    (8, None,
     "'Because I love you, Andrea.' Colette makes a vulnerable and heartfelt declaration of love."),
    (9, None,
     "'I love you too, Colette.' Andrea warmly reciprocates her feelings without hesitation."),
    (10, None,
     "'Sofia is gone!' Gabriel approaches in complete disarray, delivering his painful news."),
    (11, None,
     "'She definitely left me.' Gabriel faces the bitter finality of his breakup."),
    (12, None,
     "'She was completely right.' Gabriel acknowledges that his deceit drove Sofia away."),
    (13, None,
     "'I really am a piece of trash!' Gabriel wallows in intense self-reproach."),
    (14, None,
     "'Gabriel, calm down a little.' Andrea immediately switches from lover to loyal friend."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "After receiving an unexpected and heartfelt confession of love from Colette, Andrea turns to comfort a devastated Gabriel after Sofia leaves him."
CLOSING = ("lea", "Moi aussi je t'aime, Colette.")
