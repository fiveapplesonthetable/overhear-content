# Authoring module for kukhnya-s04e06-scene-13.
ID = 'kukhnya-s04e06-scene-13'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 6
SCENE = 13
TITLE = 'Беготня между ресторанами  (Running Between Restaurants)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.06'
SOURCE_FILE = 'sources/kukhnya/s04/e06.ru.srt'
INTRO = "Over at Arcobaleno, Lyova tries to spot Barinov's friend in the dining room without knowing what he looks like. Barinov instructs Lyova to secretly photograph the guests on his phone, then dashes into the Arcobaleno kitchen in his chef's coat to prepare Volodya's meal."
OPENER = "Let's examine Barinov's frantic sprint between the two restaurants line by line."
TRANSITION = "Now let's hear the restaurant-hopping scene again from start to finish."
OUTRO = "While Barinov catches his breath at Elena's table, Dmitry Nagiyev arrives at Claude Monet demanding his five-thousand-dollar bottle of wine. Until next time!"
CLOSING = ('barinov', 'Увидимся!')
STORY = [
    ('lyova', 'Добрый вечер, вы сегодня ждёте главного шефа?', 'Good evening, are you waiting for the head chef today?', [(180, 'Добрый вечер.')], 'adapted'),
    ('lyova', 'Виктор Петрович, я не могу бегать к каждому столику!', 'Viktor Petrovich, I cannot run to every table!', [(183, 'Я не могу бегать к каждому столику.')], 'adapted'),
    ('lyova', 'Как я узнаю, кого именно вы ждёте?', 'How will I find out whom exactly you are waiting for?', [(184, 'Как я узнаю, кого вы ждете?')], 'adapted'),
    ('barinov', 'Сфотографируй гостей на телефон и пришли мне.', 'Photograph the guests on your phone and send it to me.', [(185, 'Сфотографировали телефон и пришли мне.')], 'adapted'),
    ('barinov', 'Лёва, ешь морковку, она для мозга полезна!', 'Lyova, eat a carrot, it is good for the brain!', [(186, 'Лёва, ешь морковку.'), (187, 'Для мозга полезно.')], 'adapted'),
    ('barinov', 'А вот и твой друг, быстро встречай!', 'And here is your friend, greet him quickly!', [], 'new'),
    ('lyova', 'Здравствуйте, Виктор Петрович, ваши гости уже в зале.', 'Hello, Viktor Petrovich, your guests are already in the hall.', [(188, 'Здравствуйте, Виктор Петрович. Привет.')], 'adapted'),
    ('barinov', 'Отлично, сейчас я быстро приготовлю им горячее блюдо.', 'Excellent, right now I will quickly cook them a hot dish.', [], 'new'),
    ('barinov', 'А потом сразу побегу обратно к Лене.', 'And then I will immediately run back to Lena.', [], 'new'),
    ('lyova', 'Смотрите только, чтобы Елена Павловна ничего не заметила!', 'Just make sure that Elena Pavlovna does not notice anything!', [], 'new'),
    ('barinov', 'А вот и я снова в зале!', 'And here I am back in the dining room again!', [(189, 'А вот и я.')], 'adapted'),
    ('barinov', 'Надеюсь, наш десерт ещё не скоро принесут.', 'I hope they will not bring our dessert anytime soon.', [], 'new'),
]
WALK = [
    (0, None, '\'Good evening, are you waiting for the head chef?\' Noting how good things are to Barinov, Lyova reaches for the Russian word "glavnogo" ("main", built from "glavnyy") right at the center of the line.'),
    (1, None, '\'Viktor Petrovich, I cannot run to every table!\' Bringing up the small table before Barinov, Lyova lands on "stoliku" ("small table", built on "stolik") to keep the statement grounded.'),
    (2, None, "'How will I find out whom exactly you are waiting for?' Lyova checks bluntly about what Barinov just brought up."),
    (3, None, '\'Photograph the guests on your phone and send it to me.\' Emphasizing the photograph right here, Barinov uses "sfotografiruy" ("photograph") to carry the main weight of the thought.'),
    (4, None, '\'Lyova, eat a carrot, it is good for the brain!\' Addressing a carrot during the talk, Barinov chooses "morkovku" ("carrot", from the root "morkovka") so Lyova hears the exact meaning.'),
    (5, None, "'And here is your friend, greet him quickly!' Barinov steps in quietly with a nod, watching Lyova's face to see how the news lands."),
    (6, None, '\'Hello, Viktor Petrovich, your guests are already in the hall.\' Turning to the visitors on the spot, Lyova centers the remark on "zdravstvuyte" ("hello") without any extra fuss.'),
    (7, None, '\'Excellent, right now I will quickly cook them a hot dish.\' Bringing up a hot dish during the talk, Barinov leans on "otlichno" ("great, excellent"), which carries the whole predicate in Russian without needing "it is".'),
    (8, None, "'And then I will immediately run back to Lena.' Barinov counters lightly around Lyova, letting the remark speak for itself."),
    (9, None, '\'Just make sure that Elena Pavlovna does not notice anything!\' Lyova steps in naturally before Barinov and leans on "zametila" ("to notice, spot", a form of "zametit") to give the remark its edge.'),
    (10, None, '\'And here I am back in the dining room again!\' Checking on the hall with Lyova, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (11, None, "'I hope they will not bring our dessert anytime soon.' Barinov answers lightly with a shrug, shifting the mood of the conversation in a single beat."),
]
