# Authoring module for kukhnya-s01e11-scene-18.
ID = 'kukhnya-s01e11-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 18
TITLE = 'Неожиданное признание  (An Unexpected Confession)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "The woman who ran to the restroom has a husband, and he is waiting to pay the bill. He wants to apologise to Vika for the trouble. Listen first, and I'll explain afterwards."
OPENER = "Let's unpack it."
TRANSITION = 'Back to the full version.'
OUTRO = 'The lady is not the critic, and the mystery is not solved. Vika has another suspect. Take care until then.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Здравствуйте, вам понравился наш ресторан сегодня?', 'Hello, did you like our restaurant today?', [], ''),
    ('guest', 'Вы уж извините нас, ради бога.', 'Please forgive us, for the love of heaven.', [(221, 'Вы уж извините нас, ради бога')], ''),
    ('vika', 'Что-то случилось с вашей женой?', 'Did something happen with your wife?', [], ''),
    ('guest', 'Моя жена мне всё подробно рассказала.', 'My wife told me everything in detail.', [(220, 'Мне моя жена все рассказала')], ''),
    ('vika', 'Она отравилась каким-то нашим блюдом?', 'Did she get poisoned by some dish of ours?', [(210, 'после вашего блюда отравилась')], ''),
    ('guest', 'Нет, она вовсе не отравилась едой.', 'No, she was not poisoned by food at all.', [], ''),
    ('vika', 'Почему же ей стало так плохо?', 'Why then did she feel so ill?', [], ''),
    ('guest', 'Она беременна, уже на третьем месяце.', 'She is pregnant, already in the third month.', [(222, 'Она на третьем месяце беременности')], ''),
    ('vika', 'Так у неё просто сильный токсикоз?', 'So she just has bad morning sickness?', [(223, 'токсикоз')], ''),
    ('guest', 'Да, от запахов еды её тошнит.', 'Yes, the smells of food make her nauseous.', [], ''),
    ('vika', 'Мы очень переживали за её здоровье.', 'We were very worried about her health.', [], ''),
    ('guest', 'Спасибо вам за понимание и заботу.', 'Thank you for your understanding and care.', [], ''),
    ('vika', 'Значит, эта женщина точно не критик.', 'So this woman is definitely not the critic.', [(226, 'мы точно знаем, что критик не она')], ''),
]
WALK = [
    (0, None, ["'Hello, did you like our restaurant today?' Now we can examine the sentence: ", ('vika', 'вам'), ('vika', 'понравился'), ' means to you pleased, which is did you like, and the verb ends to agree with ', ('vika', 'ресторан'), ', which is masculine. Vika opens politely.']),
    (1, None, ["'Please forgive us, for the love of heaven.' We will look at this part: ", ('guest', 'уж'), ' softens the request, like please do. ', ('guest', 'ради'), ('guest', 'бога'), " is for heaven's sake, which uses the term Nastya used for pleasure."]),
    (2, None, ["'Did something happen with your wife?' We will analyze this line: ", ('vika', 'Что'), '-', ('vika', 'то'), ' is what, with a suffix that makes it something. ', ('vika', 'с'), ('vika', 'вашей'), ('vika', 'женой'), ' is with your wife, with endings that follow with.']),
    (3, None, ["'My wife told me everything in detail.' Let's focus on the speech: ", ('guest', 'подробно'), ' is in detail, which is the expression Max used about explaining everything. ', ('guest', 'рассказала'), ' is told, with a feminine ending for the wife.']),
    (4, None, ["'Did she get poisoned by some dish of ours?' Now let's break down this line: ", ('vika', 'каким'), '-', ('vika', 'то'), ' means some. ', ('vika', 'отравилась'), ' means got poisoned, with a feminine ending. ', ('vika', 'блюдом'), ' is by a dish.']),
    (5, None, ["'No, she was not poisoned by food at all.' We will break down this part: ", ('guest', 'вовсе'), ('guest', 'не'), " is not at all, which is Barinov's phrase. ", ('guest', 'едой'), ' is by food, which is food in its by means of form.']),
    (6, None, ["'Why then did she feel so ill?' We can break down the dialogue: ", ('vika', 'Почему'), ('vika', 'же'), ' is why then. ', ('vika', 'ей'), ('vika', 'стало'), ('vika', 'так'), ('vika', 'плохо'), ' is to her became so bad, which is the pattern for feeling ill.']),
    (7, None, ["'She is pregnant, already in the third month.' Russians are ", ('guest', 'на'), ('guest', 'третьем'), ('guest', 'месяце'), ', on the third month. ', ('guest', 'беременна'), ' is pregnant, as a short form with a feminine ending.']),
    (8, None, ["'So she just has bad morning sickness?' Let's analyze the words: ", ('vika', 'токсикоз'), ' is toxicosis, which is the medical word Russians use for morning sickness. ', ('vika', 'у'), ('vika', 'неё'), ' is at her, the pattern for she has. ', ('vika', 'Так'), ' is so.']),
    (9, None, ["'Yes, the smells of food make her nauseous.' Now we can examine the words: ", ('guest', 'от'), ('guest', 'запахов'), ('guest', 'еды'), ' is from the smells of food. ', ('guest', 'её'), ('guest', 'тошнит'), ' means her nauseates, and it has no subject.']),
    (10, None, ["'We were very worried about her health.' Let us focus on this part: ", ('vika', 'переживали'), ' means worried, and is plural, because Vika speaks for the restaurant. ', ('vika', 'здоровье'), ' is health, which is the word Senya used.']),
    (11, None, ["'Thank you for your understanding and care.' Let's inspect the sentence: ", ('guest', 'за'), ' is for. ', ('guest', 'заботу'), ' is care, which is what Vika said children need. ', ('guest', 'понимание'), ' is understanding.']),
    (12, None, ["'So this woman is definitely not the critic.' Let's focus on the speech: ", ('vika', 'Значит'), ' means so. ', ('vika', 'точно'), ('vika', 'не'), ' is definitely not. Vika crosses a suspect off her list.']),
]
