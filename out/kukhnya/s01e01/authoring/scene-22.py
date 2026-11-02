# Authoring module for kukhnya-s01e01-scene-22.
ID = 'kukhnya-s01e01-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 22
TITLE = "Визит конкурента  (The Rival's Visit)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'mark': 'Марк', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "A rival restaurant owner called Mark visits Claude Monet, and the owner, Nagiyev, welcomes him with a smile. The two men trade friendly insults about their head chefs, and then Nagiyev tells Vika to bring out the hot dishes. Here's the Russian first."
OPENER = "Let's look at how they trade insults."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Two owners, two chefs, and a lot of pride. You\'ve heard a nice phrase for the end of the scene: "I\'ll personally oversee it".'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('nagiyev', 'Рад приветствовать вас в лучшем ресторане!', 'Delighted to welcome you to the finest restaurant!', [(280, 'рад приветствовать вас в лучшем ресторане')], ''),
    ('mark', 'Мы открываем наш ресторан через две недели.', 'We are opening our restaurant in two weeks.', [(282, 'Мы открываемся через две недели')], ''),
    ('mark', 'Познакомься, это мой шеф-повар Елена.', 'Meet her, this is my chef Elena.', [(283, 'Вот познакомься'), (284, 'Мой шеф-повар Елена')], ''),
    ('mark', 'Она работала в самом лучшем ресторане.', 'She worked at the very best restaurant.', [(289, 'Она работала в самом лучшем ресторане')], ''),
    ('mark', 'А твой шеф ещё не заболел?', 'And has your chef not fallen sick yet?', [(294, 'А у твоего шефа-алкоголика печень еще не отвалилась?')], ''),
    ('nagiyev', 'Не волнуйся, мой шеф переживёт тебя.', 'Do not worry, my chef will outlive you.', [(295, 'Не волнуйся'), (296, 'переживет')], ''),
    ('nagiyev', 'Вика, скорее подавай гостям горячие блюда!', 'Vika, serve the hot dishes to the guests quickly!', [(298, 'Вика!'), (300, 'Подавай-ка, Вика, горячая')], ''),
    ('nagiyev', 'Наши гости очень сильно проголодались.', 'Our guests have gotten very hungry.', [(301, 'Гости наши проголодались')], ''),
    ('vika', 'Добрый день, сейчас всё принесут.', 'Good day, they will bring everything right now.', [(276, 'Добрый день'), (299, 'Да, Дмитрий Владимирович')], ''),
    ('mark', 'Только проследите, чтобы совсем не было перца.', 'Just make sure there is no pepper at all.', [(302, 'Да, только проследите, пожалуйста, чтобы совсем не было перца')], ''),
    ('vika', 'Хорошо, я немедленно предупрежу шеф-повара.', 'Very well, I will notify the head chef immediately.', [(303, 'Хорошо, сейчас же предупрежу шеф-повара')], ''),
    ('vika', 'На кухне уже готовят этот заказ.', 'In the kitchen they are already preparing this order.', [(304, 'основное блюдо для гостей можно уже подавать')], ''),
    ('nagiyev', 'У нас на кухне работают лучшие мастера.', 'In our kitchen the best masters work.', [], ''),
    ('vika', 'Я лично прослежу за этим блюдом.', 'I will personally oversee this dish.', [], ''),
]
WALK = [
    (0, None, ['\'Delighted to welcome you to the finest restaurant!\' ', ('nagiyev', 'Рад'), ' is "glad", used for "delighted". ', ('nagiyev', 'Приветствовать'), ', "to welcome", has ', ('nagiyev', 'привет'), ', hi, inside it.']),
    (1, None, ['\'We are opening our restaurant in two weeks.\' ', ('mark', 'Через две недели'), ' is "in two weeks", literally "through two weeks". ', ('mark', 'Две'), ' is the feminine "two", because ', ('mark', 'недели'), ' is feminine.']),
    (2, None, ['\'Meet her, this is my chef Elena.\' ', ('mark', 'Познакомься'), ' is "get acquainted", from ', ('mark', 'знаком'), ', familiar. Elena is a woman, but ', ('mark', 'повар'), ' stays masculine, so Mark says ', ('mark', 'мой шеф-повар'), ', not a feminine form.']),
    (3, None, ['\'She worked at the very best restaurant.\' ', ('mark', 'Работала'), ', "worked", ends in \"-\", ', ('mark', 'ла'), ', \" because Elena is a woman. ', ('mark', 'В самом лучшем ресторане'), ' is almost word for word what Max said about his interview restaurant, so you already know it.']),
    (4, None, ['\'And has your chef not fallen sick yet?\' ', ('mark', 'Заболел'), ' is "fell ill", from ', ('mark', 'болел'), ', to hurt or be ill. ', ('mark', 'Ещё не'), ' is "not yet". ', ('mark', 'Твой'), ' is the friendly "your".']),
    (5, None, ['\'Do not worry, my chef will outlive you.\' ', ('nagiyev', 'Переживёт'), ' is ', ('nagiyev', 'пере-'), ', over, plus ', ('nagiyev', 'живёт'), ', to live: outlive. ', ('nagiyev', 'Не волнуйся'), ' is the friendly "don\'t worry".']),
    (6, None, ['\'Vika, serve the hot dishes to the guests quickly!\' ', ('nagiyev', 'Скорее'), ' is "faster", the word from the coffee invitation. ', ('nagiyev', 'Подавай'), ' is "serve", and ', ('nagiyev', 'горячие блюда'), ' is plural, "hot dishes".']),
    (7, None, ['\'Our guests have gotten very hungry.\' ', ('nagiyev', 'Проголодались'), ' has ', ('nagiyev', 'голод'), ', hunger, inside it, and the whole word means "got hungry". The ', ('nagiyev', '-ли'), ' in it is the plural, for the guests, and ', ('nagiyev', '-сь'), ' is the "self" bit the verb always carries.']),
    (8, None, ['\'Good day, they will bring everything right now.\' ', ('vika', 'Принесут'), ' is "they will bring", with no subject. Russian uses an unnamed "they" for staff, like English "they\'ll bring it".']),
    (9, None, ['\'Just make sure there is no pepper at all.\' ', ('mark', 'Чтобы'), ' is "so that", introducing what he wants. ', ('mark', 'Не было перца'), ' is "there not be of pepper", with an "of" ending on ', ('mark', 'перца'), '.']),
    (10, None, ['\'Very well, I will notify the head chef immediately.\' ', ('vika', 'Немедленно'), ' is ', ('vika', 'не'), ' plus ', ('vika', 'медленно'), ', slowly: not slowly, so immediately. ', ('vika', 'Предупрежу'), ' is "I will warn", in one word.']),
    (11, None, ['\'In the kitchen they are already preparing this order.\' ', ('vika', 'Готовят'), ' is "they prepare", again with no named subject. ', ('vika', 'Заказ'), ' is "order", the word the chef used in "according to your order".']),
    (12, None, ['\'In our kitchen the best masters work.\' ', ('nagiyev', 'У нас на кухне'), ' is "at us on the kitchen", Russian for "in our kitchen". ', ('nagiyev', 'Мастера'), ' is a plural in \"-\", ', ('nagiyev', 'а'), ', \".']),
    (13, None, ['\'I will personally oversee this dish.\' ', ('vika', 'Прослежу'), ' is "I\'ll see to it", the same verb as ', ('vika', 'прослеж'), ' at the stove. After ', ('vika', 'за'), ', the phrase becomes ', ('vika', 'этим блюдом'), ': over this dish.']),
]
