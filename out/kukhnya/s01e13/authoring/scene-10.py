# Authoring module for kukhnya-s01e13-scene-10.
ID = 'kukhnya-s01e13-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 10
TITLE = 'Звонок из Милана  (A Call from Milan)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'angelina_h': 'Ангелина', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Max decides to fix his mistake by making a fake phone call. He calls the restaurant hostess Angelina, pretending to be from the Milan trade show. Let's listen to his brilliant plan in Russian."
OPENER = "Now let's go back through the exchange around A Call from Milan line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max's crazy plan actually worked, and Vika is heading back to the restaurant. Let's see what happens next. Next time you watch the episode, listen for the Russian expressions for 'signora' and 'kind' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Бонжорно, синьоры.', 'Buongiorno, signori.', [], ''),
    ('angelina_h', 'Добрый день, ресторан Клод Моне.', 'Good afternoon, Claude Monet restaurant.', [], ''),
    ('max', 'Меня зовут Александр.', 'My name is Alexander.', [(130, 'Меня зовут Александр')], ''),
    ('max', 'Выставка отменяется.', 'The exhibition is cancelled.', [(132, 'выставка отменится')], ''),
    ('max', 'Передайте это Виктории.', 'Pass this on to Victoria.', [(133, 'Передайте')], ''),
    ('angelina_h', 'Хорошо, я передам.', 'All right, I will pass it on.', [], ''),
    ('max', 'Граци, синьора, чао-чао.', 'Grazie, signora, ciao-ciao.', [(134, 'Граци, сеньора'), (135, 'Чао-чао.')], ''),
    ('angelina_h', 'Да, алло. Виктория Сергеевна, здравствуйте.', 'Yes, hello. Victoria Sergeyevna, hello.', [(138, 'Да, алло. Виктория Сергеевна, здравствуйте')], ''),
    ('angelina_h', 'Звонил представитель выставки из Милана.', 'A representative of the exhibition from Milan called.', [(139, 'Звонил представитель выставки из Милана')], ''),
    ('angelina_h', 'Он сказал, что она отменяется.', 'He said that it is cancelled.', [(139, 'сказал, что она отменяется.')], ''),
    ('vika', 'А, правда? Я уже в Домодедово.', 'Oh, really? I am already in Domodedovo.', [(140, 'А, правда? А я уже в Домодедово')], ''),
    ('vika', 'Я чуть не улетела.', 'I almost flew away.', [(140, 'чуть не улетела.')], ''),
    ('vika', 'Спасибо, что предупредили.', 'Thank you for warning me.', [(141, 'Спасибо, что предупредили.')], ''),
]
WALK = [
    (0, None, "'Buongiorno, signori.' Russian omits the present-tense verb 'to be' here, linking 'buongiorno' directly with 'signora' to make the point directly in conversation."),
    (1, None, "'Good afternoon, Claude Monet restaurant.' Russian omits the present-tense verb 'to be' here, linking 'good' directly with 'day', combining 'good' with 'day' and 'restaurant'."),
    (2, None, "'My name is Alexander.' Max delivers a punchy conversational reaction built around the Russian word meaning 'call'."),
    (3, None, "'The exhibition is cancelled.' Max expresses this naturally by combining the word for 'exhibition' with 'is canceled'."),
    (4, None, "'Pass this on to Victoria.' Max leads with the direct command form meaning 'to pass on' to make the point directly in conversation."),
    (5, None, "'All right, I will pass it on.' Here Angelina anchors the line on the word meaning 'good' and builds the thought around 'will pass on'."),
    (6, None, "'Grazie, signora, ciao-ciao.' Russian omits the present-tense verb 'to be' here, linking 'grazie' directly with 'signora', followed by 'ciao-ciao'."),
    (7, None, "'Yes, hello. Victoria Sergeyevna, hello.' Russian omits the present-tense verb 'to be' here, linking 'hello?' directly with 'hello', combining 'hello?' with 'hello'."),
    (8, None, "'A representative of the exhibition from Milan called.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (9, None, "'He said that it is cancelled.' Angelina uses the action verb meaning 'said' to focus on the single completed result, pairing it with 'is canceled'."),
    (10, None, "'Oh, really? I am already in Domodedovo.' Russian omits the present-tense verb 'to be' here, linking 'honestly' directly with 'already', combining 'honestly' with 'already'."),
    (11, None, "'I almost flew away.' Vika expresses this naturally by combining the word for 'nearly' with 'to fly away'."),
    (12, None, "'Thank you for warning me.' Vika puts the word for 'thank you' together with 'warned' in a crisp, natural spoken turn of phrase."),
]
