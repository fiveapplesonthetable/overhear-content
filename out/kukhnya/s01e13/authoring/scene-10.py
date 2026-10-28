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
    (0, None, "'Buongiorno, signori.' Max puts on a fake accent. He greets the staff in Italian to sound convincing."),
    (1, None, "'Good afternoon, Claude Monet restaurant.' Angelina answers professionally. She states the restaurant's name clearly."),
    (2, None, "'My name is Alexander.' Max introduces his fabricated persona. He gives himself a generic name."),
    (3, None, "'The exhibition is cancelled.' He delivers the fake bad news. Max claims the entire event has been called off."),
    (4, None, "'Pass this on to Victoria.' He makes sure the message reaches his target. Max specifically asks her to tell Vika."),
    (5, None, "'All right, I will pass it on.' Angelina accepts the message without suspicion. She promises to relay the information."),
    (6, None, "'Grazie, signora, ciao-ciao.' Max signs off in character. He throws in a few more Italian words for good measure."),
    (7, None, "'Yes, hello. Victoria Sergeyevna, hello.' Angelina calls Vika to deliver the news. She starts with a polite greeting."),
    (8, None, "'A representative of the exhibition from Milan called.' She passes on the fabricated story. Angelina reports that the organizers called."),
    (9, None, "'He said that it is cancelled.' She relays the crucial detail. Angelina tells Vika the trip is off."),
    (10, None, "'Oh, really? I am already in Domodedovo.' Vika is shocked by the sudden change. She mentions she is already at the airport."),
    (11, None, "'I almost flew away.' Vika realizes how close she came to leaving. She notes that she nearly boarded the plane."),
    (12, None, "'Thank you for warning me.' She expresses gratitude for the timely update. Vika genuinely appreciates the heads-up."),
]
