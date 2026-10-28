ID = "kukhnya-s04e06-scene-13"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 6
SCENE = 13
TITLE = "Беготня между ресторанами  (Running Between Restaurants)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lyova": "anja"}
LABELS = {"anya": "Шеф", "lyova": "Лёва"}
SOURCE_NAME = "Кухня (Kukhnya) S4.06"
SOURCE_FILE = "sources/kukhnya/s04/e06.ru.srt"
SOURCE_NOTE = "Cues 180-190. At Arcobaleno, Lyova photographs guests on his phone so Barinov can identify his friend Volodya, and meanwhile Denis struggles to bake the pastry at Claude Monet."

INTRO = "Over at Arcobaleno, Lyova tries to spot Barinov's friend in the dining room without knowing what he looks like. Barinov instructs Lyova to secretly photograph the guests on his phone, then dashes into the Arcobaleno kitchen in his chef's coat to prepare Volodya's meal."

STORY = [
    ("lyova", "Добрый вечер, вы сегодня ждёте главного шефа?", "Good evening, are you waiting for the head chef today?", [(180, "Добрый вечер.")], "adapted"),
    ("lyova", "Виктор Петрович, я не могу бегать к каждому столику!", "Viktor Petrovich, I cannot run to every table!", [(183, "Я не могу бегать к каждому столику.")], "adapted"),
    ("lyova", "Как я узнаю, кого именно вы ждёте?", "How will I find out whom exactly you are waiting for?", [(184, "Как я узнаю, кого вы ждете?")], "adapted"),
    ("anya", "Сфотографируй гостей на телефон и пришли мне.", "Photograph the guests on your phone and send it to me.", [(185, "Сфотографировали телефон и пришли мне.")], "adapted"),
    ("anya", "Лёва, ешь морковку, она для мозга полезна!", "Lyova, eat a carrot, it is good for the brain!", [(186, "Лёва, ешь морковку."), (187, "Для мозга полезно.")], "adapted"),
    ("anya", "А вот и твой друг, быстро встречай!", "And here is your friend, greet him quickly!", [], "new"),
    ("lyova", "Здравствуйте, Виктор Петрович, ваши гости уже в зале.", "Hello, Viktor Petrovich, your guests are already in the hall.", [(188, "Здравствуйте, Виктор Петрович. Привет.")], "adapted"),
    ("anya", "Отлично, сейчас я быстро приготовлю им горячее блюдо.", "Excellent, right now I will quickly cook them a hot dish.", [], "new"),
    ("anya", "А потом сразу побегу обратно к Лене.", "And then I will immediately run back to Lena.", [], "new"),
    ("lyova", "Смотрите только, чтобы Елена Павловна ничего не заметила!", "Just make sure that Elena Pavlovna does not notice anything!", [], "new"),
    ("anya", "А вот и я снова в зале!", "And here I am back in the dining room again!", [(189, "А вот и я.")], "adapted"),
    ("anya", "Надеюсь, наш десерт ещё не скоро принесут.", "I hope they will not bring our dessert anytime soon.", [], "new"),
]

OPENER = "Let's examine Barinov's frantic sprint between the two restaurants line by line."

WALK = [
    (0, None, "'Good evening, are you waiting for the head chef?' Lyova awkwardly checks a random table in the dining room."),
    (1, None, "'Viktor Petrovich, I cannot run to every table!' Multidirectional infinitive 'to run around' takes the dative phrase."),
    (2, None, "'How will I find out whom exactly you are waiting for?' Animate accusative 'whom' introduces the object question."),
    (3, None, "'Photograph the guests on your phone and send it to me.' Two singular perfective imperatives solve the identification problem."),
    (4, None, "'Lyova, eat a carrot, it is good for the brain!' Short neuter adjective 'useful' governs 'for' plus the genitive singular."),
    (5, None, "'And here is your friend, greet him quickly!' Barinov spots Volodya in the photo Lyova sends him."),
    (6, None, "'Hello, Viktor Petrovich, your guests are already in the hall.' Lyova welcomes Barinov at the back door of Arcobaleno."),
    (7, None, "'Excellent, right now I will quickly cook them a hot dish.' Substantivized neuter adjective 'hot' means a main course."),
    (8, None, "'And then I will immediately run back to Lena.' Perfective future 'will run' captures his frantic dash next door."),
    (9, None, "'Just make sure that Elena Pavlovna does not notice anything!' Lyova warns him that the ruse is risky."),
    (10, None, "'And here I am back in the dining room again!' Out of breath, Barinov slides back into his chair opposite Elena."),
    (11, None, "'I hope they will not bring our dessert anytime soon.' Meanwhile, Nagiyev is arriving at Claude Monet for his wine."),
]

TRANSITION = "Now let's hear the restaurant-hopping scene again from start to finish."
OUTRO = "While Barinov catches his breath at Elena's table, Dmitry Nagiyev arrives at Claude Monet demanding his five-thousand-dollar bottle of wine. See you in the next scene."
CLOSING = ("anya", "Сфотографируй гостей на телефон и пришли мне.")
CLOSING_TRANS = "Photograph the guests on your phone and send it to me."
