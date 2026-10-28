# Authoring module for kukhnya-s01e20-scene-19.
ID = 'kukhnya-s01e20-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 19
TITLE = 'Продажа ресторана  (Selling the Restaurant)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "At the owner's table, Barinov is about to learn that Dima has sold the restaurant to Eleonora Andreyevna. The lines are longer here; here it is in Russian."
OPENER = "Let's look at the pieces."
TRANSITION = 'Now the table talk once more.'
OUTRO = "Barinov has just found out the restaurant was sold behind his back. Russian borrows biznes from English, and prosto biznes means 'just business'. See you next time!"
CLOSING = ('nagiyev', 'Удачи!')
STORY = [
    ('eleonora', 'Красивое кольцо.', 'Beautiful ring.', [(302, 'Красивое кольцо')], ''),
    ('nagiyev', 'Макс отдал.', 'Max gave it away.', [(303, 'Макс отдал')], ''),
    ('barinov', 'Макс?', 'Max?', [(304, 'Макс')], ''),
    ('nagiyev', 'Элеонора Андреевна, прошу.', 'Eleonora Andreyevna, please, have a seat.', [(305, 'Андреевна'), (306, 'Прошу')], ''),
    ('barinov', 'Кушай, кушай, хозяин платит.', 'Eat up, eat up, the owner is paying.', [(307, 'хозяин платит')], ''),
    ('nagiyev', 'О, смотри, кто пришёл. Здравствуйте.', "Oh, look who's here. Hello.", [(308, 'О, смотри, кто'), (309, 'Здравствуйте')], ''),
    ('eleonora', 'Не помешаю?', 'Am I interrupting?', [(310, 'Не помешаю')], ''),
    ('eleonora', 'Виктор Петрович, я в курсе того, что произошло.', 'Viktor Petrovich, I know what happened.', [(311, 'Виктор Петрович, я в курсе того, что произошло')], ''),
    ('eleonora', 'Я вам очень сочувствую.', 'I really feel for you.', [(312, 'Я вам очень сочувствую')], ''),
    ('eleonora', 'Вы настоящий профессионал.', "You're a real professional.", [(313, 'вы настоящий профессионал')], ''),
    ('barinov', 'Вы вообще о чём?', 'What are you even talking about?', [(315, 'Вы вообще о чем')], ''),
    ('nagiyev', 'У нас с вами был сложный период.', 'You and I went through a rough patch.', [(316, 'У нас с вами был сложный период')], ''),
    ('nagiyev', 'Но благодаря вам у нас всё получилось.', 'But thanks to you, it all worked out.', [(318, 'Но благодаря вам у нас все получилось')], ''),
    ('nagiyev', 'Спасибо вам за вас.', 'Thank you for being you.', [(319, 'Спасибо вам за вас')], ''),
    ('barinov', 'Ты что, продал ресторан?', 'Did you sell the restaurant?', [(320, 'Ты что, продал ресторан')], ''),
    ('barinov', 'Дима, как ты мог? Мы же всё исправили.', 'Dima, how could you? We fixed everything.', [(323, 'Дима, как ты мог'), (324, 'Мы же все исправили')], ''),
    ('nagiyev', 'Не ори. Вить, это бизнес. Просто бизнес.', "Don't yell. Vitya, it's business. Just business.", [(325, 'Не ори'), (326, 'Вить, это бизнес'), (327, 'Просто бизнес')], ''),
    ('nagiyev', 'Поверь мне, лучше продать на подъёме.', "Trust me, it's better to sell on the way up.", [(328, 'Поверь мне, лучше продать'), (329, 'на подъеме')], ''),
]
WALK = [
    (0, None, "'Beautiful ring.' Russian needs no verb here, and krasivoe ends in -oe because koltso, 'ring', is neuter."),
    (1, None, "'Max gave it away.' The word otdal means 'gave away': ot-, 'off, away', in front of dal, 'gave'."),
    (2, None, "'Max?' In Russian a one-word question works on the voice alone, with the pitch rising on the word."),
    (3, None, "'Eleonora Andreyevna, please, have a seat.' Russian proshu literally means 'I ask', and a host uses it to invite you to sit or go first."),
    (4, None, "'Eat up, eat up, the owner is paying.' The word khozyain means 'owner' or 'host', the one whose place it is."),
    (5, None, "'Oh, look who's here. Hello.' Russian says smotri, kto prishyol, literally 'look who has come', and zdravstvuyte is the polite hello."),
    (6, None, "'Am I interrupting?' Russian asks ne pomeshayu, literally 'won't I get in the way?', when joining a table."),
    (7, None, "'Viktor Petrovich, I know what happened.' The phrase v kurse literally means 'in the course', and Russian uses it for 'in the know'."),
    (8, None, "'I really feel for you.' The word sochuvstvuyu literally means 'I feel together with', and it takes vam, 'to you'."),
    (9, None, "'You're a real professional.' Russian uses nastoyashchiy, 'real, genuine', where English might say 'true'."),
    (10, None, "'What are you even talking about?' Russian leaves out the verb: vy voobshche o chyom, literally 'you at all about what?'."),
    (11, None, "'You and I went through a rough patch.' Russian says u nas s vami, literally 'at us with you', for 'you and I had'."),
    (12, None, "'But thanks to you, it all worked out.' Russian says vsyo poluchilos, literally 'everything came out', for 'it worked out'."),
    (13, None, "'Thank you for being you.' Russian says spasibo vam za vas, literally 'thank you for you', a set phrase for toasts."),
    (14, None, "'Did you sell the restaurant?' Russian starts with ty chto, literally 'you what', to show shock, and prodal ends in -l for a man."),
    (15, None, "'Dima, how could you? We fixed everything.' The little word zhe adds 'but we did!', and kak ty mog means 'how could you'."),
    (16, None, "'Don't yell. It's business. Just business.' Russian borrows biznes from English, and ne ori, 'don't yell', is a blunt thing to say."),
    (17, None, "'Trust me, it's better to sell on the way up.' The phrase na podyome literally means 'on the rise', and luchshe means 'better'."),
]
