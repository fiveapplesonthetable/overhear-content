# Authoring module for kukhnya-s02e01-scene-02.
ID = 'kukhnya-s02e01-scene-02'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 2
TITLE = "Строгий приказ  (Strict Order)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "vika": "angelina", "anya": "alisa", "sasha": "anja"}
LABELS = {"vika": "Вика", "anya": "Макс", "sasha": "Саша"}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = 'In the dining room of Claude Monet, Max tries to tell waitress Sasha that their previous evening was a mistake. Art director Victoria arrives, immediately fires Sasha on the spot, and coldly puts Max in his place. Let us listen to their confrontation in Russian first.'
OPENER = "Now let us examine Victoria's dismissal of Sasha line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Heartbroken and furious, Victoria fires Sasha on the spot and refuses to let Max speak to her informally, leaving their relationship in ruins. Next time you watch the episode, listen for the Russian expressions for 'why' and 'in the morning' — you will catch every word right away. See you next time!"
CLOSING = ("vika", "Пока!")
STORY = [
    ('sasha', 'Привет, Макс, почему ты утром рано убежал?', 'Hi, Max, why did you run away early in the morning?', [(66, 'Ты так рано убежал с утра?')], ''),
    ('anya', 'Мне надо было быстро поехать домой утром.', 'I had to quickly go home in the morning.', [(67, 'Да, мне надо было забежать домой.')], ''),
    ('anya', 'Саша, вчера мы сделали очень большую ошибку.', 'Sasha, yesterday we made a very big mistake.', [(68, 'Переодеться. Слушай, Саша, мне кажется, мы вчера переборщили немного.')], ''),
    ('sasha', 'Не волнуйся, всё было просто очень хорошо.', 'Do not worry, everything was simply very good.', [(69, 'Да все нормально.')], ''),
    ('vika', 'Здравствуй, Саша, сегодня ты больше не работаешь.', 'Hello, Sasha, today you no longer work here.', [(72, 'Здрасте, Виктория Сергеевна. Здравствуй, до свидания.')], ''),
    ('vika', 'Ты уволена, собирай сразу все свои вещи.', 'You are fired, pack all your things immediately.', [(73, 'Ты уволена.'), (74, 'Можешь собрать вещи, завтра получишь расчет.')], ''),
    ('sasha', 'Простите, Виктория, за что вы меня уволили?', 'Excuse me, Victoria, what did you fire me for?', [(75, 'Простите, а за что?')], ''),
    ('vika', 'Завтра утром ты получишь все свои деньги.', 'Tomorrow morning you will receive all your money.', [(74, 'Можешь собрать вещи, завтра получишь расчет.')], ''),
    ('anya', 'Вика, подожди, так нельзя поступать с людьми!', 'Vika, wait, one cannot act like this with people!', [(77, 'Вик, подожди, так нельзя. Во-первых, Виктория Сергеевна.')], ''),
    ('vika', 'Для тебя я теперь только Виктория Сергеевна.', 'For you I am now only Victoria Sergeyevna.', [(77, 'Вик, подожди, так нельзя. Во-первых, Виктория Сергеевна.')], ''),
    ('vika', 'А теперь иди на кухню и работай!', 'And now go to the kitchen and work!', [(78, 'А во-вторых, Лавров. Иди работай.')], ''),
    ('anya', 'Пожалуйста, давай спокойно поговорим об этом вечером.', 'Please, let us calmly talk about this in the evening.', [], ''),
    ('vika', 'Надеюсь, я всё очень понятно тебе объяснила!', 'I hope I explained everything very clearly to you!', [(84, 'Лавров, надеюсь, я все понятно объяснила.')], ''),
]
WALK = [
    (0, None, "'Hi, Max, why did you run away early in the morning?' Sasha puts the word for 'hi' together with 'why' and 'this morning' in a crisp, natural spoken turn of phrase."),
    (1, None, "'I had to quickly go home in the morning.' Here Max anchors the line on the word meaning 'it is necessary' and builds the thought around 'was' and 'quickly'."),
    (2, None, "'Sasha, yesterday we made a very big mistake.' The phrasing opens with 'yesterday' before bringing in 'did' and 'very much' to make the point clear."),
    (3, None, "'Do not worry, everything was simply very good.' Sasha leads with the direct command form meaning 'worry', pairing it with 'was' and 'just'."),
    (4, None, "'Hello, Sasha, today you no longer work here.' Vika puts the word for 'hello' together with 'today' and 'more' in a crisp, natural spoken turn of phrase."),
    (5, None, "'You are fired, pack all your things immediately.' Vika leads with the direct command form meaning 'pack', pairing it with 'fired' and 'at once'."),
    (6, None, "'Excuse me, Victoria, what did you fire me for?' Sasha leads with the direct command form meaning 'excuse me', followed by 'fired'."),
    (7, None, "'Tomorrow morning you will receive all your money.' Vika expresses this naturally by combining the word for 'tomorrow' with 'this morning' and 'will receive'."),
    (8, None, "'Vika, wait, one cannot act like this with people!' Max leads with the direct command form meaning 'wait', pairing it with 'not allowed' and 'to treat'."),
    (9, None, "'For you I am now only Victoria Sergeyevna.' Russian omits the present-tense verb 'to be' here, linking 'now' directly with 'only' to make the point directly in conversation."),
    (10, None, "'And now go to the kitchen and work!' Vika leads with the direct command form meaning 'go', pairing it with 'now' and 'kitchen'."),
    (11, None, "'Please, let us calmly talk about this in the evening.' Max leads with the direct command form meaning 'let's', pairing it with 'calmly' and 'we'll have a talk'."),
    (12, None, "'I hope I explained everything very clearly to you!' Vika chooses the action verb meaning 'hope so' for the ongoing action, followed by 'very much' and 'clear'."),
]
