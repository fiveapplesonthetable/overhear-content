# Authoring module for kukhnya-s06e02-scene-02.
ID = 'kukhnya-s06e02-scene-02'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 2
TITLE = "Книга Елены и решение бороться  (Elena's Book and the Decision to Fight)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = "At home, Barinov prepares to tell Elena that he is leaving the restaurant—until Elena reveals her surprise: she has just published her own cookbook, sparking Barinov's competitive pride."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Refusing to be outshone by Elena's new cookbook, Barinov stays up all night creating an ambitious Michelin-worthy menu. See you next time!"
CLOSING = ('elena', 'Всего хорошего!')
STORY = [
    ('elena', 'Что за повод?', 'What is the occasion?', [(14, 'Что за повод?')], 'exact'),
    ('barinov', 'У меня очень важная новость.', 'I have very important news.', [(15, 'У меня очень важная новость')], 'exact'),
    ('barinov', 'Мне предложили новую работу.', 'They offered me a new job.', [(17, 'Мне предложили новую работу')], 'exact'),
    ('elena', 'Я тебе не говорила, хотела сделать сюрприз.', 'I did not tell you, I wanted to make a surprise.', [(18, 'Я тебе не говорила'), (19, 'Хотела сделать сюрприз')], 'adapted'),
    ('elena', 'У меня через два дня встреча с читателями.', 'In two days I have a meeting with readers.', [(21, 'У меня через два дня встреча с читателями')], 'exact'),
    ('elena', 'Прости, новая работа?', 'Sorry, a new job?', [(22, 'Прости, новая работа?')], 'exact'),
    ('barinov', 'Да, но я решил отказаться.', 'Yes, but I decided to turn it down.', [(23, 'Да'), (24, 'Но я решил отказаться')], 'adapted'),
    ('barinov', 'Я буду бороться за звезду.', 'I am going to fight for the star.', [(25, 'Я буду бороться за')], 'adapted'),
    ('barinov', 'Сейчас собираюсь вводить новое авторское меню.', 'Right now I am going to introduce a new auteur menu.', [(26, 'собираюсь вводить новое авторское меню')], 'adapted'),
    ('elena', 'Это замечательно, ты будешь первым поваром России.', 'That is wonderful, you will be the first chef in Russia.', [(27, 'Это замечательно'), (28, 'Ты будешь первым поваром России')], 'adapted'),
    ('barinov', 'А ты написала кулинарную книжку.', 'And you wrote a culinary book.', [(29, 'кулинарную книжку')], 'adapted'),
    ('barinov', 'Я очень устал сегодня.', 'I am very tired today.', [(31, 'Устал')], 'adapted'),
]
WALK = [
    (0, None, '\'What is the occasion?\' Bringing up the reason on the spot, Elena links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (1, None, "'I have very important news.' Barinov jumps in right away with a smile, before Elena can change the subject."),
    (2, None, '\'They offered me a new job.\' Mentioning a new job during the talk, Barinov reaches for the Russian word "predlozhili" ("offered", built from "predlozhit") right at the center of the line.'),
    (3, None, "'I did not tell you, I wanted to make a surprise.' Elena counters decisively on the spot, bringing things back to earth after the buildup."),
    (4, None, "'In two days I have a meeting with readers.' Mentioning the readers around Barinov, Elena lets Barinov see exactly where things stand."),
    (5, None, '\'Sorry, a new job?\' Elena warmly extends this personal apology as they meet using "prosti" ("forgive me") — the close, informal way to say "forgive me" or "I\'m sorry" to someone dear.'),
    (6, None, '\'Yes, but I decided to turn it down.\' Pressing on candidly in front of Elena, the "-sya" ending on "otkazatsya" ("to refuse, decline") marks an action that unfolds mutually or turns back on the speaker.'),
    (7, None, "'I am going to fight for the star.' Barinov counters calmly beside Elena, so Elena knows he is not just making small talk."),
    (8, None, '\'Right now I am going to introduce a new auteur menu.\' Describing how auteur he is during the talk, Barinov reaches for the Russian word "avtorskoye" ("auteur, signature", built from "avtorskiy") right at the center of the line.'),
    (9, None, "'That is wonderful, you will be the first chef in Russia.' Elena steps in dryly hearing Barinov, leaving no doubt about where she stands."),
    (10, None, "'And you wrote a culinary book.' Barinov chimes in openly without a pause, testing Elena's reaction in the middle of the exchange."),
    (11, None, '\'I am very tired today.\' Barinov steps in boldly on the spot and brings in "segodnya" ("today") to make the meaning unmistakable.'),
]
