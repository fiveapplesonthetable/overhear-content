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
    (0, None, '\'What is the occasion?\' Asking what the occasion is is how Elena puts Barinov on the spot. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, '\'I have very important news.\' Adding that he has very important news fills in the missing piece for Elena. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (2, None, "'They offered me a new job.' Between the shift and the pride, Barinov gives Elena a quick, grounded response."),
    (3, None, '\'I did not tell you, I wanted to make a surprise.\' Noting that she did not tell Barinov she wanted to make a surprise keeps Elena\'s side of the story simple and clear. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (4, None, '\'In two days I have a meeting with readers.\' Even though in two days she has a meeting with readers, Elena keeps a steady face in front of Barinov. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (5, None, "'Sorry, a new job?' Turning from the menu to the work, Elena asks Barinov directly."),
    (6, None, "'Yes, but I decided to turn it down.' Saying that he decided to turn it down is how Barinov sets the tone with Elena."),
    (7, None, "'I am going to fight for the star.' Because he is going to fight for the star, Barinov treats the matter as settled."),
    (8, None, "'Right now I am going to introduce a new auteur menu.' Admitting that right now he is going to introduce a new auteur menu shows Barinov being honest for a change."),
    (9, None, '\'That is wonderful, you will be the first chef in Russia.\' Saying that that is wonderful Barinov will be the first in Russia is how Elena sets the tone with Barinov. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (10, None, '\'And you wrote a culinary book.\' Since Elena wrote a culinary book, Barinov does not waste words on excuses. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (11, None, "'I am very tired today.' Since he is very tired today, Barinov does not waste words on excuses."),
]
