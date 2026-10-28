# Authoring module for kukhnya-s04e17-scene-01.
ID = 'kukhnya-s04e17-scene-01'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 17
SCENE = 1
TITLE = 'Новость о беременности  (Pregnancy News)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eva': 'Ева', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.17'
SOURCE_FILE = 'sources/kukhnya/s04/e17.ru.srt'
INTRO = "Waitress Eva pulls Chef Viktor Barinov, sous-chef Lyova, and young cook Denis aside one by one at Claude Monet. With a calm, serious expression, she tells each man in secret that she is expecting a baby. Let's listen to their stunned reactions in Russian."
OPENER = "Now let's break down Eva's unexpected announcement and the chefs' reactions line by line."
TRANSITION = "Let's hear the entire conversation from start to finish without interruption."
OUTRO = "Eva's sudden revelation leaves Viktor Petrovich, Lyova, and Denis completely bewildered in the kitchen. Listen for the adjective meaning pregnant and the adverb meaning soon when you watch. Until next time!"
CLOSING = ('eva', 'Всего хорошего!')
STORY = [
    ('eva', 'Виктор Петрович, вы тоже должны знать.', 'Viktor Petrovich, you should know too.', [(1, 'Виктор Петрович, думаю, вы тоже должны знать')], 'adapted'),
    ('eva', 'Я сейчас жду ребёнка.', 'I am expecting a child right now.', [], 'new'),
    ('eva', 'Я беременна от тебя.', 'I am pregnant by you.', [(5, 'я беременна от тебя')], 'adapted'),
    ('barinov', 'Что ты такое говоришь, Ева?', 'What on earth are you saying, Eva?', [], 'new'),
    ('eva', 'Срок пока ещё очень небольшой.', 'It is still very early.', [(3, 'Срок пока небольшой')], 'adapted'),
    ('eva', 'Но скоро всё будет заметно.', 'But soon everything will be noticeable.', [(3, 'но скоро будет заметно')], 'adapted'),
    ('eva', 'Витя, я правда беременна.', 'Vitya, I really am pregnant.', [(4, 'Витя, я беременна')], 'adapted'),
    ('lyova', 'Виктор Петрович, у вас всё хорошо?', 'Viktor Petrovich, is everything all right with you?', [(7, 'Виктор Петрович, у вас все в порядке')], 'adapted'),
    ('barinov', 'Да, Лёва, всё в порядке.', 'Yes, Lyova, everything is fine.', [(7, 'в порядке'), (8, 'Да')], 'adapted'),
    ('lyova', 'А у меня большая проблема.', 'Well, I have a big problem.', [], 'new'),
    ('eva', 'Лёва, я тоже беременна.', 'Lyova, I am pregnant too.', [(10, 'Я беременна')], 'adapted'),
    ('barinov', 'Нам нужно срочно всё проверить.', 'We need to check everything urgently.', [], 'new'),
]
WALK = [
    (0, None, "'Viktor Petrovich, you should know too.' Eva mentions that Barinov should know so Barinov sees what is at stake."),
    (1, None, "'I am expecting a child right now.' Eva explains that she is expecting a child right now, keeping her voice calm and direct."),
    (2, None, '\'I am pregnant by you.\' Explaining that she is pregnant by Barinov lays the cards on the table for Barinov. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (3, None, "'What on earth are you saying, Eva?' Over the conversation and the news, Barinov presses Eva for a straight answer."),
    (4, None, "'It is still very early.' Realizing that it is still very early changes how Eva handles the situation."),
    (5, None, "'But soon everything will be noticeable.' Noting that soon everything will be noticeable keeps Eva's side of the story simple and clear."),
    (6, None, "'Vitya, I really am pregnant.' With the moment and news in play, Eva keeps this short reply brisk and direct."),
    (7, None, '\'Viktor Petrovich, is everything all right with you?\' Here asking whether everything all right with Barinov shows Lyova looking for the real truth. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (8, None, "'Yes, Lyova, everything is fine.' Saying that everything is fine is how Barinov sets the tone with Eva."),
    (9, None, "'Well, I have a big problem.' Having a big problem is how Lyova lays out the situation for Barinov."),
    (10, None, "'Lyova, I am pregnant too.' Realizing that she is pregnant changes how Eva handles the situation."),
    (11, None, "'We need to check everything urgently.' Here needing to check everything urgently sets up the next turn in their exchange. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
]
