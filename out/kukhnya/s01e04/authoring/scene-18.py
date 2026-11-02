# Authoring module for kukhnya-s01e04-scene-18.
ID = 'kukhnya-s01e04-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 18
TITLE = 'Шеф против шефа  (Chef Against Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Chef Barinov marches into the rival restaurant to find Elena Sokolova, determined to find out which of his cooks came to her for a job. Elena has no intention of telling him. Here's the Russian first."
OPENER = "Let's go through the standoff."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = ['Barinov leaves without a name, but he\'s determined to find the traitor himself. Take away ', ('elena', 'всего вам доброго!'), ', the Russian way to say "all the best".']
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'У меня к вам совсем простой вопрос.', 'I have a very simple question for you.', [(251, 'простой вопрос')], ''),
    ('elena', 'Как у шеф-повара к шеф-повару?', 'From one head chef to another?', [(252, 'Как у шеф-повара к шеф-повару')], ''),
    ('barinov', 'Кто из моих поваров приходил к вам?', 'Which of my cooks came to see you?', [(253, 'Кто из моих людей')], ''),
    ('elena', 'Я не сдаю своих людей, Виктор.', 'I do not rat out my people, Viktor.', [(257, 'Не сдаю своих людей')], ''),
    ('barinov', 'Это мой повар, а не ваш!', 'He is my cook, not yours!', [(258, 'Это мой человек')], ''),
    ('elena', 'Он хочет работать на хорошей кухне.', 'He wants to work in a good kitchen.', [], ''),
    ('barinov', 'У меня лучшая кухня в этом городе!', 'I have the best kitchen in this city!', [], ''),
    ('elena', 'Тогда почему ваши люди ищут работу?', 'Then why are your people looking for work?', [], ''),
    ('barinov', 'Я обязательно узнаю его имя сам!', 'I will definitely find out his name myself!', [], ''),
    ('elena', 'Мне уже пора идти на кухню.', 'It is time for me to go to the kitchen.', [(261, 'Надо идти работать')], ''),
    ('elena', 'Вы сами выход отсюда найдёте?', 'Will you find the way out yourself?', [(262, 'Выход найдете')], ''),
    ('barinov', 'Найду, дорогу я отлично помню.', 'I will, I remember the way very well.', [(263, 'Найду')], ''),
    ('elena', 'Вот и отлично, всего вам доброго!', 'Wonderful then, all the best to you!', [(263, 'Ну и хорошо')], ''),
]
WALK = [
    (0, None, [
        '\'I have a very simple question for you.\' Literally, "at me to you a quite simple question", with no action word "have" at all. Barinov says ',
        ('barinov', 'к вам'),
        ', the polite form, keeping his rival at a distance.'
    ]),
    (1, None, [
        "'From one head chef to another?' ",
        ('elena', 'Как у шеф-повара к шеф-повару?'),
        ' translates to "as at a head chef to a head chef", ending in -a for "at" and -u for "to".'
    ]),
    (2, None, [
        "'Which of my cooks came to see you?' ",
        ('barinov', 'Кто из моих поваров'),
        ' translates to "who of my cooks". The Russian term for "came", ',
        ('barinov', 'приходил'),
        ', describes a trip there and back, which makes it a visit.'
    ]),
    (3, None, [
        '\'I do not rat out my people, Viktor.\' The Russian expression for "rat out" translates to hand over, to the police or to an examiner. ',
        ('elena', 'своих людей,'),
        ' translates to "my own people".'
    ]),
    (4, None, [
        "'He is my cook, not yours!' ",
        ('barinov', 'а не ваш!'),
        ' translates to "and not yours". The little ',
        ('barinov', 'а'),
        ' sets one claim against the other.'
    ]),
    (5, None, [
        '\'He wants to work in a good kitchen.\' Russians work literally on the kitchen. The describing word for "good" takes a matching ending.'
    ]),
    (6, None, [
        '\'I have the best kitchen in this city!\' The phrase for "best" has a feminine ending to match the kitchen. ',
        ('barinov', 'в этом городе!'),
        ' translates to "in this city".'
    ]),
    (7, None, [
        "'Then why are your people looking for work?' Elena throws back the very words Barinov used about newspapers, ",
        ('elena', 'ищут работу?'),
        ', they look for work. ',
        ('elena', 'ваши'),
        ' marks the polite "your" for multiple people, to match the word for "people".'
    ]),
    (8, None, [
        "'I will definitely find out his name myself!' ",
        ('barinov', 'обязательно'),
        ' translates to "definitely". The term for "his" never changes, and ',
        ('barinov', 'узнаю'),
        ' translates to "I\'ll find out".'
    ]),
    (9, None, [
        '\'It is time for me to go to the kitchen.\' The phrase for "it is time for me" literally translates to "to me already it\'s time". The term for kitchen takes a "to" ending for heading there.'
    ]),
    (10, None, [
        '\'Will you find the way out yourself?\' The Russian term for "exit", ',
        ('elena', 'выход'),
        ', is built from "out" plus "a going". ',
        ('elena', 'сами'),
        ' is the polite form for "yourself".'
    ]),
    (11, None, [
        "'I will, I remember the way very well.' Russian answers by repeating the action word, ",
        ('barinov', 'Найду,'),
        ', I\'ll find. The expression for "road" gets an action-receiving ending.'
    ]),
    (12, None, [
        "'Wonderful then, all the best to you!' ",
        ('elena', 'всего вам доброго!'),
        ' translates to "of all good to you", a wish in the "of" form. It is a polite goodbye.'
    ]),
]
