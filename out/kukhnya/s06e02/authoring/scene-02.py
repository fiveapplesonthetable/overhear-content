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
    (0, None, '\'What is the occasion?\' Elena states this update toward Barinov: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (1, None, "'I have very important news.' Barinov speaks right away toward Elena, leaving no doubt about where he stands."),
    (2, None, '\'They offered me a new job.\' Barinov stresses this direct term toward Elena: "predlozhili" means "offered" (from "predlozhit"), giving the line its exact edge.'),
    (3, None, '\'I did not tell you, I wanted to make a surprise.\' Elena favors this direct piece with Barinov: "syurpriz" means "surprise", and it carries the main weight of what Elena is saying.'),
    (4, None, "'In two days I have a meeting with readers.' Elena cuts in calmly around Barinov, without trying to dress up how she really feels."),
    (5, None, '\'Sorry, a new job?\' Elena anchors one vivid detail in earnest: "novaya" means "new" (from "novyy"), giving the line its exact edge.'),
    (6, None, '\'Yes, but I decided to turn it down.\' Barinov puts the reaction before Elena: the "-sya" ending on "otkazatsya" ("to refuse, decline") turns the action inward or makes it happen between people naturally.'),
    (7, None, "'I am going to fight for the star.' Barinov counters calmly during the talk, saying out loud what both of them already know."),
    (8, None, '\'Right now I am going to introduce a new auteur menu.\' Barinov spotlights one key term with Elena: "avtorskoye" means "auteur, signature" (from "avtorskiy"), giving the line its exact edge.'),
    (9, None, '\'That is wonderful, you will be the first chef in Russia.\' Elena favors one key term right here: "zamechatelno" means "wonderful", and it carries the main weight of what Elena is saying.'),
    (10, None, "'And you wrote a culinary book.' Barinov follows up openly without holding back, to clear the air between them once and for all."),
    (11, None, '\'I am very tired today.\' Barinov grounds one vivid piece in reply: "segodnya" means "today", and it carries the main weight of what Barinov is saying.'),
]
