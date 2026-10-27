ID = "kukhnya-s01e17-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 12
TITLE = "Хитрость и слайсер  (A Trick and a Slicer)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja", "nagiyev": "angelina"}
LABELS = {"anya": "Макс", "senya": "Сеня", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 145-220. Max loudly fakes a phone call so Sasha will spread the rumor that tomorrow is his birthday, "
    "while in the dining room Senya presents his new seasonal veal dish to Nagiyev and convinces him to buy a slicer."
)

INTRO = (
    "In the kitchen, Max pretends to talk on the phone within Sasha's earshot so she will tell everyone that tomorrow is his birthday. "
    "Meanwhile, in the dining room, Senya serves his winning veal dish to restaurant owner Dmitry Nagiyev and asks for a new kitchen machine. "
    "Let's listen to the scene in Russian first."
)

STORY = [
    ("anya", "Нет, завтра я не буду праздновать.",
     "No, tomorrow I will not celebrate.",
     [(148, "Завтра ничего не планирую праздновать")], "adapted"),
    ("anya", "Я никому не скажу про праздник.",
     "I will not tell anyone about the holiday.",
     [(149, "говорить никому не буду")], "adapted"),
    ("anya", "Ладно, не волнуйся за меня, пока.",
     "All right, do not worry about me, bye.",
     [(150, "Ладно, не волнуйся за меня, пока")], "adapted"),
    ("anya", "Думаю, Саше хватит десяти минут.",
     "I think ten minutes will be enough for Sasha.",
     [(153, "Саше хватит 10 минут")], "adapted"),
    ("senya", "Дмитрий, пожалуйста, попробуйте наше новое блюдо.",
     "Dmitry, please try our new dish.",
     [(187, "Пожалуйста, пробуйте")], "adapted"),
    ("nagiyev", "Ты кто такой? Это что такое?",
     "Who are you? What is this?",
     [(188, "Ты кто такой? Это что такое?")], "verbatim"),
    ("senya", "Это новое сезонное блюдо от шефа.",
     "This is the new seasonal dish from the Chef.",
     [(189, "Это новое сезонное блюдо")], "adapted"),
    ("senya", "Это я придумал, а шеф выбрал.",
     "I invented it, and the Chef chose it.",
     [(191, "Это я придумал")], "adapted"),
    ("nagiyev", "Очень неплохо, мне нравится, спасибо.",
     "Not bad at all, I like it, thank you.",
     [(197, "Очень неплохо. Спасибо")], "adapted"),
    ("senya", "Нам на кухню очень нужна машина.",
     "We really need a machine for the kitchen.",
     [(198, "нам на кухню нужен")], "adapted"),
    ("nagiyev", "Что это ещё за новая машина?",
     "What kind of new machine is that?",
     [], "new"),
    ("senya", "Она режет ветчину очень тонкими кусками.",
     "It cuts ham in very thin pieces.",
     [(200, "ветчины очень тонкими")], "adapted"),
    ("nagiyev", "Ладно, Вика, купи ему эту машину.",
     "All right, Vika, buy him this machine.",
     [(201, "купи ему")], "adapted"),
]

OPENER = (
    "That was the scene in the kitchen and dining room. "
    "Now let's walk through it line by line."
)

WALK = [
    (0, "Max speaks loudly into his phone near Sasha.",
     "'No, tomorrow I will not celebrate' — завтра means tomorrow, and я не буду праздновать means I will not celebrate."),
    (1, None,
     "'I will not tell anyone about the holiday' — никому means to no one, не скажу means I will not say, and про праздник means about the holiday."),
    (2, None,
     "'All right, do not worry about me, bye' — не волнуйся means do not worry, за меня means about me, and пока means bye."),
    (3, "Max hangs up and smiles.",
     "'I think ten minutes will be enough for Sasha' — хватит takes the dative Саше and genitive десяти минут to say ten minutes will be enough for Sasha."),
    (4, "In the dining room, Senya approaches Nagiyev's table.",
     "'Dmitry, please try our new dish' — пожалуйста means please, and попробуйте is the polite imperative for try."),
    (5, None,
     "'Who are you? What is this?' — ты кто такой asks who are you, and это что такое asks what is this."),
    (6, None,
     "'This is the new seasonal dish from the Chef' — новое сезонное блюдо means new seasonal dish, and от шефа means from the Chef."),
    (7, None,
     "'I invented it, and the Chef chose it' — придумал means invented or thought up, and выбрал means chose."),
    (8, "Nagiyev tastes the veal roll.",
     "'Not bad at all, I like it, thank you' — очень неплохо means very not bad or quite good, and мне нравится means I like it."),
    (9, None,
     "'We really need a machine for the kitchen' — нам нужна машина means we need a machine, and на кухню means for the kitchen."),
    (10, None,
     "'What kind of new machine is that?' — что за asks what kind of, and новая машина means new machine."),
    (11, None,
     "'It cuts ham in very thin pieces' — она режет means it cuts, ветчину is ham in the accusative, and тонкими кусками means in thin pieces."),
    (12, "Nagiyev turns to Victoria.",
     "'All right, Vika, buy him this machine' — купи is the imperative for buy, ему means for him, and эту машину means this machine."),
]

TRANSITION = (
    "Now listen to the full scene again."
)

OUTRO = (
    "Max's birthday rumor is officially underway, and Senya has charmed Nagiyev into buying new equipment. "
    "Here is one last line from the scene."
)

CLOSING = ("nagiyev", "Очень неплохо, мне нравится, спасибо.")
