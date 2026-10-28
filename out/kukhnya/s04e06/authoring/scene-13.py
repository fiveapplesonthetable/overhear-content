ID = 'kukhnya-s04e06-scene-13'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 6
SCENE = 13
TITLE = "Беготня между ресторанами  (Running Between Restaurants)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "chef": "anja", "lyova": "angelina"}
LABELS = {"chef": "Шеф", "lyova": "Лёва"}
SOURCE_NAME = 'Кухня (Kukhnya) S4.06'
SOURCE_FILE = 'sources/kukhnya/s04/e06.ru.srt'

INTRO = "Over at Arcobaleno, Lyova tries to spot Barinov's friend in the dining room without knowing what he looks like. Barinov instructs Lyova to secretly photograph the guests on his phone, then dashes into the Arcobaleno kitchen in his chef's coat to prepare Volodya's meal."

STORY = [
    ('lyova', 'Добрый вечер, вы сегодня ждёте главного шефа?', 'Good evening, are you waiting for the head chef today?', [(180, 'Добрый вечер.')], 'adapted'),
    ('lyova', 'Виктор Петрович, я не могу бегать к каждому столику!', 'Viktor Petrovich, I cannot run to every table!', [(183, 'Я не могу бегать к каждому столику.')], 'adapted'),
    ('lyova', 'Как я узнаю, кого именно вы ждёте?', 'How will I find out whom exactly you are waiting for?', [(184, 'Как я узнаю, кого вы ждете?')], 'adapted'),
    ('chef', 'Сфотографируй гостей на телефон и пришли мне.', 'Photograph the guests on your phone and send it to me.', [(185, 'Сфотографировали телефон и пришли мне.')], 'adapted'),
    ('chef', 'Лёва, ешь морковку, она для мозга полезна!', 'Lyova, eat a carrot, it is good for the brain!', [(186, 'Лёва, ешь морковку.'), (187, 'Для мозга полезно.')], 'adapted'),
    ('chef', 'А вот и твой друг, быстро встречай!', 'And here is your friend, greet him quickly!', [], 'new'),
    ('lyova', 'Здравствуйте, Виктор Петрович, ваши гости уже в зале.', 'Hello, Viktor Petrovich, your guests are already in the hall.', [(188, 'Здравствуйте, Виктор Петрович. Привет.')], 'adapted'),
    ('chef', 'Отлично, сейчас я быстро приготовлю им горячее блюдо.', 'Excellent, right now I will quickly cook them a hot dish.', [], 'new'),
    ('chef', 'А потом сразу побегу обратно к Лене.', 'And then I will immediately run back to Lena.', [], 'new'),
    ('lyova', 'Смотрите только, чтобы Елена Павловна ничего не заметила!', 'Just make sure that Elena Pavlovna does not notice anything!', [], 'new'),
    ('chef', 'А вот и я снова в зале!', 'And here I am back in the dining room again!', [(189, 'А вот и я.')], 'adapted'),
    ('chef', 'Надеюсь, наш десерт ещё не скоро принесут.', 'I hope they will not bring our dessert anytime soon.', [], 'new'),
]

OPENER = "Let's examine Barinov's frantic sprint between the two restaurants line by line."

WALK = [
    (0, None, "'Good evening, are you waiting for the head chef?' Lyova awkwardly checks a random table in the dining room."),
    (1, None, "'Viktor Petrovich, I cannot run to every table!' Here Lyova anchors the thought on 'can, am able to' and finishes on 'small table, café table', keeping the spoken rhythm brisk and natural."),
    (2, None, "'How will I find out whom exactly you are waiting for?' In everyday Russian, 'how / as' flows straight into 'to wait, to expect' without extra linking words."),
    (3, None, "'Photograph the guests on your phone and send it to me.' Chef Barinov pairs 'photograph' with 'came' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (4, None, "'Lyova, eat a carrot, it is good for the brain!' Notice how Russian puts 'eat' and 'brain' together in a short, direct phrase where word endings show how the ideas connect."),
    (5, None, "'And here is your friend, greet him quickly!' Barinov spots Volodya in the photo Lyova sends him."),
    (6, None, "'Hello, Viktor Petrovich, your guests are already in the hall.' Lyova welcomes Barinov at the back door of Arcobaleno."),
    (7, None, "'Excellent, right now I will quickly cook them a hot dish.' Chef Barinov pairs 'perfectly' with 'dish' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (8, None, "'And then I will immediately run back to Lena.' Notice how Russian puts 'later, afterwards' and 'Lena' together in a short, direct phrase where word endings show how the ideas connect."),
    (9, None, "'Just make sure that Elena Pavlovna does not notice anything!' Lyova warns him that the ruse is risky."),
    (10, None, "'And here I am back in the dining room again!' Out of breath, Barinov slides back into his chair opposite Elena."),
    (11, None, "'I hope they will not bring our dessert anytime soon.' Meanwhile, Nagiyev is arriving at Claude Monet for his wine."),
]

TRANSITION = "Now let's hear the restaurant-hopping scene again from start to finish."
OUTRO = "While Barinov catches his breath at Elena's table, Dmitry Nagiyev arrives at Claude Monet demanding his five-thousand-dollar bottle of wine. Until next time!"
CLOSING = ("chef", "Увидимся!")
