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
    (0, None, '\'Viktor Petrovich, you should know too.\' Eva sharpens one memorable detail in reply: "dolzhny" means "must, should" (from "dolzhen"), giving the line its exact edge.'),
    (1, None, "'I am expecting a child right now.' Eva drops this line at once: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (2, None, "'I am pregnant by you.' Eva fires back wryly to be clear, before Barinov can change the subject."),
    (3, None, '\'What on earth are you saying, Eva?\' Barinov chooses one pointed piece in earnest: "govorish" means "you say" (from "govorit"), giving the line its exact edge.'),
    (4, None, '\'It is still very early.\' Eva offers that reply with ease: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (5, None, "'But soon everything will be noticeable.' Eva chimes in briskly beside Lyova, saying out loud what both of them already know."),
    (6, None, '\'Vitya, I really am pregnant.\' Eva highlights one concrete choice at once: "beremenna" means "pregnant" (from "beremennyy"), giving the line its exact edge.'),
    (7, None, '\'Viktor Petrovich, is everything all right with you?\' Lyova states that remark facing Eva: using "u vas" (literally "by you") is how Russian politely asks or talks about what someone has on their side.'),
    (8, None, "'Yes, Lyova, everything is fine.' Barinov opens up wryly to be clear, shifting the whole mood of the room in a single beat."),
    (9, None, '\'Well, I have a big problem.\' Lyova colors one key word in earnest: "bolshaya" means "large" (from "bolshoy"), giving the line its exact edge.'),
    (10, None, '\'Lyova, I am pregnant too.\' Eva drops the thought at once: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (11, None, "'We need to check everything urgently.' Barinov reacts lightly to settle things, making his position completely clear."),
]
