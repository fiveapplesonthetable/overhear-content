# Authoring module for dix-pour-cent s04e05 scene 26 (cues 918-923).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-26.py --out out/dix-pour-cent/s04e05/scene-26.json

ID = "dix-pour-cent-s04e05-scene-26"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 26
TITLE = "Une nouvelle honnêteté  (A New Honesty)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 918-923. Walking in the fresh air after leaving the hospital, Mathias admits to Camille that speaking "
    "the honest truth feels completely bizarre to him, while Camille warmly reassures him that honesty is a great quality."
)

INTRO = (
    "Stepping out into the pleasant Parisian afternoon, Mathias and Camille walk side by side away from the hospital. "
    "Reflecting on his recent decision to speak openly without deceit, Mathias experiences the strange sensation of total honesty. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's look at Mathias reflecting on his new perspective step by step."

STORY = [
    ("lea", "Alors, comment tu te sens, Mathias?",
     "So, how do you feel, Mathias?",
     [(918, "Alors, comment tu te sens?")], "Camille asks how he feels in the open air"),
    ("mathias", "Je me sens enfin tout à fait honnête!",
     "I finally feel completely honest!",
     [(919, "Honnête!")], "Mathias shares his surprising state of mind"),
    ("lea", "C'est une belle sensation nouvelle.",
     "It is a wonderful new sensation.",
     [(920, "comme sensation")], "Camille validates his emotional breakthrough"),
    ("mathias", "C'est bizarre comme sensation pour moi.",
     "It feels weird as a sensation for me.",
     [(920, "c'est bizarre comme sensation")], "Admits that transparency is unfamiliar to him"),
    ("lea", "C'est parce que tu n'es pas habitué.",
     "It is because you are not used to it.",
     [(921, "t'y es pas habitué")], "Camille gently explains why it feels so strange"),
    ("mathias", "J'ai passé ma vie à mentir.",
     "I spent my life lying.",
     [(921, "habitué")], "Acknowledges his long history of manipulation"),
    ("lea", "Tu verras, être honnête est bien aussi.",
     "You will see, being honest is good too.",
     [(922, "c'est bien aussi")], "Camille highlights the peace of living truthfully"),
    ("mathias", "Oui, tu as totalement raison, Camille.",
     "Yes, you are totally right, Camille.",
     [(923, "Oui.")], "Mathias readily agrees with her wisdom"),
    ("lea", "Tu as fait le bon choix.",
     "You made the right choice.",
     [(923, "Oui.")], "Reassures him that he chose the proper path"),
    ("mathias", "Je veux être digne de toi.",
     "I want to be worthy of you.",
     [(923, "Oui.")], "Mathias expresses his commitment to change"),
    ("lea", "Nous recommençons sur de nouvelles bases.",
     "We are starting over on a new foundation.",
     [(923, "Oui.")], "Camille embraces their fresh beginning"),
    ("mathias", "C'est un vrai soulagement aujourd'hui.",
     "It is a true relief today.",
     [(923, "Oui.")], "Breathes deeply with a peaceful smile"),
    ("lea", "Je suis fière d'être ta fille.",
     "I am proud to be your daughter.",
     [(923, "Oui.")], "Camille speaks with deep filial pride"),
    ("mathias", "Et je suis fier de toi.",
     "And I am proud of you.",
     [(923, "Oui.")], "Mathias echoes her heartfelt affection"),
]

WALK = [
    (0, None,
     "'So, how do you feel, Mathias?' Camille checks in on his mindset as they stroll."),
    (1, None,
     "'I finally feel completely honest!' Mathias describes his unexpected psychological state."),
    (2, None,
     "'It is a wonderful new sensation.' Camille encourages him to appreciate the change."),
    (3, None,
     "'It feels weird as a sensation for me.' Mathias notes how unusual candor feels after years of scheming."),
    (4, None,
     "'It is because you are not used to it.' Camille points out that practice will make honesty feel natural."),
    (5, None,
     "'I spent my life lying.' Mathias looks back on his past professional duplicity."),
    (6, None,
     "'You will see, being honest is good too.' Camille promises that sincerity brings its own reward."),
    (7, None,
     "'Yes, you are totally right, Camille.' Mathias concedes her point with genuine humility."),
    (8, None,
     "'You made the right choice.' Camille reinforces his courageous decision."),
    (9, None,
     "'I want to be worthy of you.' Mathias articulates his aspiration to earn her lasting respect."),
    (10, None,
     "'We are starting over on a new foundation.' Camille looks forward to an honest bond."),
    (11, None,
     "'It is a true relief today.' Mathias feels unburdened by the weight of deception."),
    (12, None,
     "'I am proud to be your daughter.' Camille voices her sincere love and acceptance."),
    (13, None,
     "'And I am proud of you.' Mathias reciprocates with profound fatherly pride."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Walking through Paris together, Mathias discovers that truthfulness brings an unfamiliar yet liberating sense of peace, as Camille encourages him to embrace his new honesty."
CLOSING = ("mathias", "C'est un vrai soulagement aujourd'hui.")
