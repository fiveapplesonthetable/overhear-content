ID = "domashniy-arest-s01e10-scene-07"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 7
TITLE = "Наблюдательное оборудование  (Surveillance Equipment)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "tolya": "anja"}
LABELS = {"anya": "Соколов", "tolya": "Анатолий"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 211-217. Sokolov asks what equipment he gets for the stakeout and is told to use his own eyes. "
    "When he spots his colleagues preparing to drink alcohol, they joke that his eyes are functioning perfectly."
)

INTRO = (
    "In this short scene, agent Sokolov prepares for his surveillance assignment outside Anikeyev's former home. "
    "When he asks his partner Anatoly for professional surveillance equipment, he is told that his own two eyes are more than enough. "
    "Noticing a bottle on the table, Sokolov realizes what his colleagues plan to do in his absence. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Я прямо сейчас должен идти?",
     "Must I go right now?",
     [(211, "Прямо на работе")], ""),
    ("tolya", "Да, Соколов, именно сейчас.",
     "Yes, Sokolov, right now.",
     [], "Anatoly confirms the immediate order"),
    ("anya", "А что у меня из оборудования?",
     "And what equipment do I have?",
     [(213, "А что у меня из наблюдательного оборудования")], ""),
    ("tolya", "Твои собственные глаза!",
     "Your own eyes!",
     [(214, "Глаза")], ""),
    ("anya", "И это всё моё оборудование?",
     "And is that all my equipment?",
     [], "Sokolov expresses skepticism"),
    ("tolya", "Этого тебе вполне достаточно.",
     "That is quite enough for you.",
     [], "Anatoly dismisses complaints"),
    ("anya", "А что это у вас на столе?",
     "And what is that on your table?",
     [(215, "А вы что тут")], ""),
    ("anya", "Вы что, пить алкоголь собрались?",
     "Are you planning to drink alcohol?",
     [(215, "пить собрались")], ""),
    ("tolya", "Ну вот, твои глаза отлично работают!",
     "Well look, your eyes work excellently!",
     [(216, "наблюдательное оборудование функционирует")], ""),
    ("tolya", "Наблюдательное оборудование в полном порядке.",
     "The surveillance equipment is in full working order.",
     [(216, "Ну вот, наблюдательное оборудование функционирует")], ""),
    ("anya", "Вы будете отдыхать, а я мёрзнуть?",
     "You will relax while I freeze?",
     [], "Sokolov resents the unfair assignment"),
    ("tolya", "Приказ начальника надо выполнять.",
     "The chief's order must be carried out.",
     [], "Anatoly appeals to authority"),
    ("tolya", "Иди и действуй, Соколов!",
     "Go and take action, Sokolov!",
     [(217, "Действуй, Соколов")], ""),
    ("anya", "Понял, уже иду наблюдать.",
     "Understood, I am already going to observe.",
     [], "Sokolov resigns to his task"),
]

OPENER = (
    "Now let's examine Sokolov's comedic briefing line by line. "
    "Sokolov discovers what equipment he gets for surveillance."
)

WALK = [
    (0, None,
     "'Must I go right now?' Sokolov clarifies the timing with a modal adjective."),
    (1, None,
     "'Yes, Sokolov, right now.' Anatoly confirms the urgency with an emphatic adverb."),
    (2, None,
     "'And what equipment do I have?' Sokolov asks about surveillance gear."),
    (3, None,
     "'Your own eyes!' Anatoly answers bluntly with a plural noun."),
    (4, None,
     "'And is that all my equipment?' Sokolov questions the lack of technology."),
    (5, None,
     "'That is quite enough for you.' Anatoly uses a predicative adverb for sufficiency."),
    (6, None,
     "'And what is that on your table?' Sokolov notices a suspicious bottle."),
    (7, None,
     "'Are you planning to drink alcohol?' Sokolov asks about their party plans."),
    (8, None,
     "'Well look, your eyes work excellently!' Anatoly jokes at the sharpness of his vision."),
    (9, None,
     "'The surveillance equipment is in full working order.' Anatoly mocks him with official bureaucratic jargon."),
    (10, None,
     "'You will relax while I freeze?' Sokolov resents the unfair division of labor."),
    (11, None,
     "'The chief's order must be carried out.' Anatoly cites authority using an infinitive construction."),
    (12, None,
     "'Go and take action, Sokolov!' Anatoly sends him off with two imperative verbs."),
    (13, None,
     "'Understood, I am already going to observe.' Sokolov departs reluctantly for the cold stakeout."),
]

TRANSITION = "Now let's listen to Anatoly and Sokolov's conversation once more without pauses."
OUTRO = (
    "Equipped only with his own eyes, Sokolov heads out to the cold stakeout. "
    "In the next scene, pressure mounts on the kindergarten director."
)
CLOSING = ("tolya", "Иди и действуй, Соколов!")
