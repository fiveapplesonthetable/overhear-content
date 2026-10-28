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
    (0, None, '\'Delighted to welcome you to the finest restaurant!\' "Rad" is "glad", used for "delighted". "Privetstvovat\'", "to welcome", has "privet", hi, inside it.'),
    (1, None, '\'We are opening our restaurant in two weeks.\' "Cherez dve nedeli" is "in two weeks", literally "through two weeks". "Dve" is the feminine "two", because "nedelya" is feminine.'),
    (2, None, '\'Meet her, this is my chef Elena.\' "Poznakomsya" is "get acquainted", from "znakomyy", familiar. Elena is a woman, but "povar" stays masculine, so Mark says "moy shef-povar", not a feminine form.'),
    (3, None, '\'She worked at the very best restaurant.\' "Rabotala" is "worked", with -la for a woman. "V samom luchshem restorane" is "in the very best restaurant".'),
    (4, None, '\'And has your chef not fallen sick yet?\' "Zabolel" is "fell ill", from "bolet\'", to hurt or be ill. "Yeshchyo ne" is "not yet". "Tvoy" is the friendly "your".'),
    (5, None, '\'Do not worry, my chef will outlive you.\' "Perezhivyot" is "pere-", over, plus "zhit\'", to live: outlive. "Ne volnuysya" is the friendly "don\'t worry".'),
    (6, None, '\'Vika, serve the hot dishes to the guests quickly!\' "Skoreye" is "faster", the word from the coffee invitation. "Podavay" is "serve", and "goryachiye blyuda" is plural, "hot dishes".'),
    (7, None, '\'Our guests have gotten very hungry.\' "Progolodalis\'" has "golod", hunger, inside it, and "pro-" for "thoroughly". The "-lis\'" shows the plural.'),
    (8, None, '\'Good day, they will bring everything right now.\' "Prinesut" is "they will bring", with no subject. Russian uses an unnamed "they" for staff, like English "they\'ll bring it".'),
    (9, None, '\'Just make sure there is no pepper at all.\' "Chtoby" is "so that", introducing what he wants. "Ne bylo pertsa" is "there not be of pepper", with an "of" ending on "perets".'),
    (10, None, '\'Very well, I will notify the head chef immediately.\' "Nemedlenno" is "ne" plus "medlenno", slowly: not slowly, so immediately. "Preduprezhu" is "I will warn", in one word.'),
    (11, None, '\'In the kitchen they are already preparing this order.\' "Gotovyat" is "they prepare", again with no named subject. "Zakaz" is "order", the word the chef used in "according to your order".'),
    (12, None, '\'In our kitchen the best masters work.\' "U nas na kukhne" is "at us on the kitchen", Russian for "in our kitchen". "Mastera" is a plural in "-a", like "povara", cooks.'),
    (13, None, '\'I will personally oversee this dish.\' "Proslezhu" is "I will watch through", the family of "prosledi" from the kitchen. "Za etim blyudom" is "over this dish", the ending that "za" calls for.'),
]
