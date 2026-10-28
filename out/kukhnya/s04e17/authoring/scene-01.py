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
    (0, None, '\'Viktor Petrovich, you should know too.\' Eva conveys a wry tack with Barinov, combining "tozhe" ("too") and "dolzhny" ("must, should") so the key meaning lands right away.'),
    (1, None, '\'I am expecting a child right now.\' Eva displays a thoughtful footing in the scene, putting "seychas" ("now") alongside "zhdu" ("I wait, expect") in a tight, everyday turn of phrase.'),
    (2, None, '\'I am pregnant by you.\' Eva conveys a serious footing during the exchange, building the phrase around "beremenna" ("pregnant") and "ya" ("I") for a crisp, natural delivery.'),
    (3, None, '\'What on earth are you saying, Eva?\' Barinov challenges calmly beside Lyova, leaning on "govorish" ("you say") before closing the thought with "chto" ("what").'),
    (4, None, '\'It is still very early.\' Eva takes a warm angle across the room, leaning on "srok" ("term") before closing the thought with "poka" ("bye").'),
    (5, None, '\'But soon everything will be noticeable.\' Eva maintains an earnest manner for Lyova, weaving "skoro" ("soon") together with "budet" ("will be") just the way native speakers do.'),
    (6, None, '\'Vitya, I really am pregnant.\' Eva projects a playful footing across the room, building the phrase around "pravda" ("honestly") and "beremenna" ("pregnant") for a crisp, natural delivery.'),
    (7, None, '\'Viktor Petrovich, is everything all right with you?\' Lyova inquires promptly with Eva now, placing "khorosho" ("good, fine") straight beside "viktor" ("Viktor") with no word for "to be" needed.'),
    (8, None, '\'Yes, Lyova, everything is fine.\' Barinov shares a candid attitude during the exchange, linking "poryadke" ("order") directly with "da" ("yes"), since Russian drops "is" and "are" in the present.'),
    (9, None, '\'Well, I have a big problem.\' Lyova sets a candid tone for Eva, leaning on "bolshaya" ("large") before closing the thought with "problema" ("problem").'),
    (10, None, '\'Lyova, I am pregnant too.\' Eva brings a sharp stance across the room, joining "tozhe" ("too") to "beremenna" ("pregnant") so every word pulls its weight.'),
    (11, None, '\'We need to check everything urgently.\' Barinov adopts a pointed note at once, putting "nuzhno" ("necessary") alongside "srochno" ("urgent, urgently") in a tight, everyday turn of phrase.'),
]
