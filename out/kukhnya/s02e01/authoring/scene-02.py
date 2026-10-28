# Authoring module for kukhnya-s02e01-scene-02.
ID = 'kukhnya-s02e01-scene-02'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 2
TITLE = 'Строгий приказ  (Strict Order)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = 'In the dining room of Claude Monet, Max tries to tell waitress Sasha that their previous evening was a mistake. Art director Victoria arrives, immediately fires Sasha on the spot, and coldly puts Max in his place. Let us listen to their confrontation in Russian first.'
OPENER = "Now let us examine Victoria's dismissal of Sasha line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Heartbroken and furious, Victoria fires Sasha on the spot and refuses to let Max speak to her informally, leaving their relationship in ruins. Next time you watch the episode, listen for the Russian expressions for 'why' and 'in the morning' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('sasha', 'Привет, Макс, почему ты утром рано убежал?', 'Hi, Max, why did you run away early in the morning?', [(66, 'Ты так рано убежал с утра?')], ''),
    ('max', 'Мне надо было быстро поехать домой утром.', 'I had to quickly go home in the morning.', [(67, 'Да, мне надо было забежать домой.')], ''),
    ('max', 'Саша, вчера мы сделали очень большую ошибку.', 'Sasha, yesterday we made a very big mistake.', [(68, 'Переодеться. Слушай, Саша, мне кажется, мы вчера переборщили немного.')], ''),
    ('sasha', 'Не волнуйся, всё было просто очень хорошо.', 'Do not worry, everything was simply very good.', [(69, 'Да все нормально.')], ''),
    ('vika', 'Здравствуй, Саша, сегодня ты больше не работаешь.', 'Hello, Sasha, today you no longer work here.', [(72, 'Здрасте, Виктория Сергеевна. Здравствуй, до свидания.')], ''),
    ('vika', 'Ты уволена, собирай сразу все свои вещи.', 'You are fired, pack all your things immediately.', [(73, 'Ты уволена.'), (74, 'Можешь собрать вещи, завтра получишь расчет.')], ''),
    ('sasha', 'Простите, Виктория, за что вы меня уволили?', 'Excuse me, Victoria, what did you fire me for?', [(75, 'Простите, а за что?')], ''),
    ('vika', 'Завтра утром ты получишь все свои деньги.', 'Tomorrow morning you will receive all your money.', [(74, 'Можешь собрать вещи, завтра получишь расчет.')], ''),
    ('max', 'Вика, подожди, так нельзя поступать с людьми!', 'Vika, wait, one cannot act like this with people!', [(77, 'Вик, подожди, так нельзя. Во-первых, Виктория Сергеевна.')], ''),
    ('vika', 'Для тебя я теперь только Виктория Сергеевна.', 'For you I am now only Victoria Sergeyevna.', [(77, 'Вик, подожди, так нельзя. Во-первых, Виктория Сергеевна.')], ''),
    ('vika', 'А теперь иди на кухню и работай!', 'And now go to the kitchen and work!', [(78, 'А во-вторых, Лавров. Иди работай.')], ''),
    ('max', 'Пожалуйста, давай спокойно поговорим об этом вечером.', 'Please, let us calmly talk about this in the evening.', [], ''),
    ('vika', 'Надеюсь, я всё очень понятно тебе объяснила!', 'I hope I explained everything very clearly to you!', [(84, 'Лавров, надеюсь, я все понятно объяснила.')], ''),
]
WALK = [
    (0, None, "'Hi, Max, why did you run away early in the morning?' Sasha greets Max warmly and asks why he slipped out so early that morning."),
    (1, None, "'I had to quickly go home in the morning.' Max makes up a quick excuse about needing to rush home."),
    (2, None, "'Sasha, yesterday we made a very big mistake.' He tries to tell Sasha gently that last night was a huge mistake."),
    (3, None, "'Do not worry, everything was simply very good.' Sasha brushes off his worry and says she thought everything was great."),
    (4, None, "'Hello, Sasha, today you no longer work here.' Vika walks up and coldly announces that Sasha no longer works at the restaurant."),
    (5, None, "'You are fired, pack all your things immediately.' Furious after catching them together, Vika fires Sasha on the spot and tells her to pack."),
    (6, None, "'Excuse me, Victoria, what did you fire me for?' Stunned, Sasha politely asks Victoria why she is being let go."),
    (7, None, "'Tomorrow morning you will receive all your money.' Vika refuses to explain and simply says Sasha will get her final pay tomorrow morning."),
    (8, None, "'Vika, wait, one cannot act like this with people!' Max steps in and protests that Vika cannot treat people that way."),
    (9, None, "'For you I am now only Victoria Sergeyevna.' Vika icily demands that Max address her only by her formal full name from now on."),
    (10, None, "'And now go to the kitchen and work!' She orders him to march straight back to the kitchen and do his job."),
    (11, None, "'Please, let us calmly talk about this in the evening.' Max begs her to talk things over calmly after the shift ends."),
    (12, None, "'I hope I explained everything very clearly to you!' Vika cuts him off sharply, warning him that she has made herself crystal clear."),
]
