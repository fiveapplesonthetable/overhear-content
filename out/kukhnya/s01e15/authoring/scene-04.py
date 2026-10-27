ID = "kukhnya-s01e15-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 4
TITLE = "Мамины блинчики  (Mom's Pancakes)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lyova": "anja"}
LABELS = {"anya": "Баринов", "lyova": "Лёва"}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues 21-24. Lyova wakes Viktor Petrovich with pancakes."

INTRO = "Lyova tries to wake Viktor Petrovich up with freshly made pancakes and reminders about work. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("lyova", "Виктор Петрович, ну вставайте уже, ну!",
     "Viktor Petrovich, come on, get up already, come on!",
     [(21, "Виктор Петрович, ну вставайте уже, ну.")], "adapted"),
    ("anya", "Лёва, дай мне поспать ещё пять минут.",
     "Lyova, let me sleep for five more minutes.",
     [], "new"),
    ("lyova", "Во-первых, мама блинчиков для вас испекла.",
     "First, Mom baked pancakes for you.",
     [(22, "Во-первых, мама блинчиков испекла.")], "adapted"),
    ("anya", "Свежие блинчики это очень хороший повод.",
     "Fresh pancakes are a very good reason.",
     [], "new"),
    ("lyova", "Она приготовила сладкое варенье и чай.",
     "She prepared sweet jam and tea.",
     [], "new"),
    ("anya", "Твоя мама готовит просто потрясающие завтраки.",
     "Your mom makes simply amazing breakfasts.",
     [], "new"),
    ("lyova", "А во-вторых, вы действительно опоздаете.",
     "And second, you really will be late.",
     [(23, "А во-вторых")], "adapted"),
    ("anya", "Куда мне теперь так сильно спешить?",
     "Where do I have to rush so much now?",
     [], "new"),
    ("lyova", "Нас обоих уже ждут на нашей кухне.",
     "Both of us are already expected in our kitchen.",
     [], "new"),
    ("anya", "Какой же ты вредный человек, Лёва!",
     "What an annoying person you are, Lyova!",
     [(24, "Лёва")], "adapted"),
    ("lyova", "Я просто забочусь о нашей общей работе.",
     "I am simply caring about our shared work.",
     [], "new"),
    ("anya", "Ладно, встаю, неси скорее горячие блины!",
     "Alright, I am getting up, bring the hot pancakes soon!",
     [], "new"),
]

OPENER = "Let's break down this morning interaction."

WALK = [
    (0, None,
     "'Viktor Petrovich, come on, get up already, come on!' -- Lyova gently tries to wake his boss."),
    (1, None,
     "'Lyova, let me sleep for five more minutes.' -- The chef begs for a little more rest."),
    (2, None,
     "'First, Mom baked pancakes for you.' -- Lyova presents a delicious incentive from his mother."),
    (3, None,
     "'Fresh pancakes are a very good reason.' -- Viktor agrees that hot food sounds tempting."),
    (4, None,
     "'She prepared sweet jam and tea.' -- The sous-chef lists what is on the table."),
    (5, None,
     "'Your mom makes simply amazing breakfasts.' -- Viktor praises the culinary skills of his mother."),
    (6, None,
     "'And second, you really will be late.' -- Lyova mentions the urgent schedule at work."),
    (7, None,
     "'Where do I have to rush so much now?' -- Viktor grumbles about having to leave the warm bed."),
    (8, None,
     "'Both of us are already expected in our kitchen.' -- Lyova reminds him that the cooks are waiting."),
    (9, None,
     "'What an annoying person you are, Lyova!' -- The chef playfully scolds him for being so diligent."),
    (10, None,
     "'I am simply caring about our shared work.' -- Lyova justifies his insistence with professional duty."),
    (11, None,
     "'Alright, I am getting up, bring the hot pancakes soon!' -- Viktor finally agrees to get out of bed."),
]

TRANSITION = "Now let's listen to the scene again without interruption."
OUTRO = "Viktor Petrovich reluctantly gets out of bed, lured by the scent of fresh pancakes."
CLOSING = ("anya", "Ладно, встаю, неси скорее горячие блины!")
