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
OUTRO = "Eva's sudden revelation leaves Viktor Petrovich, Lyova, and Denis completely bewildered in the kitchen. Listen for the word meaning pregnant and the expression meaning soon when you watch. Until next time!"
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
    (0, None, '\'Viktor Petrovich, you should know too.\' Eva counters briskly in front of Barinov and puts the weight on "dolzhny" ("must, should", from "dolzhen") as the exchange unfolds.'),
    (1, None, "'I am expecting a child right now.' Talking about a child on the spot, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (2, None, "'I am pregnant by you.' Eva proceeds wryly beside Barinov, so Barinov knows she is not just making small talk."),
    (3, None, '\'What on earth are you saying, Eva?\' Barinov answers boldly beside Eva and lands on "govorish" ("you say", built on "govorit") to keep the statement grounded.'),
    (4, None, '\'It is still very early.\' Showing how small things are to Barinov, Eva links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (5, None, "'But soon everything will be noticeable.' Eva pushes back briskly facing Barinov, testing Barinov's reaction in the middle of the exchange."),
    (6, None, '\'Vitya, I really am pregnant.\' Explaining how pregnant things are right here, Eva brings in "beremenna" ("pregnant", from "beremennyy") as the key Russian word here.'),
    (7, None, '\'Viktor Petrovich, is everything all right with you?\' Stepping in smoothly in front of Barinov, Lyova links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (8, None, "'Yes, Lyova, everything is fine.' Barinov continues wryly beside Lyova, keeping the focus on what actually matters here."),
    (9, None, '\'Well, I have a big problem.\' Focusing on a big problem before Barinov, Lyova centers the thought on "bolshaya" ("large", from "bolshoy") without wasting a word.'),
    (10, None, '\'Lyova, I am pregnant too.\' Insisting on how pregnant she is on the spot, Eva links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (11, None, "'We need to check everything urgently.' Barinov counters at once toward Eva, leaving no doubt about where he stands."),
]
