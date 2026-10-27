# Authoring module for dix-pour-cent s04e06 scene 18 (cues 828-848).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e06/authoring/scene-18.py --out overhear-content/out/dix-pour-cent/s04e06/scene-18.json

ID = "dix-pour-cent-s04e06-scene-18"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 18
TITLE = "L'adieu lucide  (A Clear-Eyed Farewell)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 828-848. Sitting on a park bench while Flora rests, Andrea and Colette have a candid, mature talk. "
    "Andrea admits her mistakes and realizes she cannot change who she is, leading them to agree to separate while co-parenting Flora."
)

INTRO = (
    "On a quiet bench in a Parisian park, Andrea Martel and Colette Brancillon watch over baby Flora. "
    "With genuine honesty, Andrea reflects on their painful separation and confronts her own nature as an ambitious agent. "
    "Together, they make a mature decision about their future and their daughter. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("colette", "Qu'est-ce qu'elle a tout à coup?",
     "What is wrong with her suddenly?",
     [(828, "Qu'est-ce qu'elle a ?")], "Colette checks on Flora's crying"),
    ("lea", "Ce sont des pleurs de soulagement.",
     "These are tears of relief.",
     [(829, "C'est des pleurs de décompression, je crois...")], "Andrea explains the emotional release"),
    ("colette", "Ne t'inquiète pas, ça va aller.",
     "Do not worry, it will be fine.",
     [(831, "Ne t'inquiète pas.")], "Colette offers gentle comfort"),
    ("lea", "J'étais très en colère contre toi.",
     "I was very angry with you.",
     [(835, "J'étais très en colère contre toi.")], "Andrea confesses her initial resentment"),
    ("colette", "Je comprends ta colère de départ.",
     "I understand your initial anger.",
     [(836, "Mais je comprends pourquoi tu es partie.")], "Colette validates Andrea's feelings"),
    ("lea", "Tu n'avais pas d'autre choix.",
     "You had no other choice.",
     [(837, "Tu n'avais pas le choix.")], "Andrea acknowledges the inevitability of the split"),
    ("lea", "Cela m'a forcé à réfléchir.",
     "That forced me to reflect.",
     [(838, "C'était la seule façon de me forcer à regarder la vérité en face.")], "Andrea shares her realization"),
    ("colette", "À réfléchir à notre avenir commun?",
     "To reflect on our shared future?",
     [(839, "Et à réfléchir à ce que je veux vraiment dans la vie.")], "Colette probes Andrea's thoughts"),
    ("lea", "Je ne peux pas changer qui je suis.",
     "I cannot change who I am.",
     [(844, "Je ne peux jamais être quelqu'un d'autre.")], "Andrea admits her core identity"),
    ("lea", "Je t'aime, mais soyons honnêtes.",
     "I love you, but let us be honest.",
     [(845, "Je t'aime Colette, mais je ne veux pas...")], "Andrea speaks with profound sincerity"),
    ("lea", "Il vaut mieux qu'on s'arrête là.",
     "It is better that we stop there.",
     [(847, "Il vaut mieux qu'on s'arrête là.")], "Andrea delivers the heartbreaking conclusion"),
    ("colette", "C'est sans doute la meilleure décision.",
     "It is undoubtedly the best decision.",
     [(847, "Il vaut mieux qu'on s'arrête là.")], "Colette nods in bittersweet agreement"),
    ("lea", "On va s'occuper de Flora ensemble.",
     "We will take care of Flora together.",
     [(848, "Et puis on verra ensemble comment s'occuper de Flora.")], "Andrea confirms their joint parenting role"),
    ("colette", "Oui, nous serons toujours une famille.",
     "Yes, we will always be a family.",
     [(848, "Et puis on verra ensemble comment s'occuper de Flora.")], "Colette reaffirms their eternal family bond"),
]

WALK = [
    (0, None,
     "'What is wrong with her suddenly?' Colette wonders why baby Flora is crying softly. "
     "The idiom 'tout a coup' means suddenly or all of a sudden."),
    (1, None,
     "'These are tears of relief.' Andrea understands that the baby feels the tension releasing. "
     "The plural noun 'pleurs' designates weeping or crying."),
    (2, None,
     "'Do not worry, it will be fine.' Colette offers calm reassurance. "
     "The imperative 'ne t'inquiete pas' means do not worry."),
    (3, None,
     "'I was very angry with you.' Andrea admits her initial resentment after the breakup. "
     "The phrase 'en colere contre' expresses anger toward someone."),
    (4, None,
     "'I understand your initial anger.' Colette acknowledges the pain she caused. "
     "The noun 'depart' in this context means beginning or onset."),
    (5, None,
     "'You had no other choice.' Andrea recognizes that leaving was necessary. "
     "The masculine noun 'choix' means choice."),
    (6, None,
     "'That forced me to reflect.' Andrea explains how the shock made her look at herself. "
     "The verb 'forcer' means to compel or force."),
    (7, None,
     "'To reflect on our shared future?' Colette asks gently about Andrea's thoughts. "
     "The adjective 'commun' describes something shared together."),
    (8, None,
     "'I cannot change who I am.' Andrea accepts her nature as a dedicated agent. "
     "The verb 'changer' signifies changing or altering."),
    (9, None,
     "'I love you, but let us be honest.' Andrea speaks from a place of deep sincerity. "
     "The imperative 'soyons' comes from 'etre' in the first-person plural."),
    (10, None,
     "'It is better that we stop there.' Andrea makes the painful decision to end their relationship. "
     "The impersonal idiom 'il vaut mieux' means it is better."),
    (11, None,
     "'It is undoubtedly the best decision.' Colette nods in quiet agreement. "
     "The adverbial expression 'sans doute' means undoubtedly or without doubt."),
    (12, None,
     "'We will take care of Flora together.' Andrea confirms their lifelong parental commitment. "
     "The pronominal verb 's'occuper de' means to take care of."),
    (13, None,
     "'Yes, we will always be a family.' Colette confirms that their bond as co-parents remains unbroken. "
     "The adverb 'toujours' means always."),
]

OUTRO = (
    "With heavy hearts but clear minds, Andrea and Colette release their romantic past. "
    "Unburdened by false promises, they choose mutual respect and unified devotion to Flora. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("colette", "Nous resterons toujours unies pour Flora!")
