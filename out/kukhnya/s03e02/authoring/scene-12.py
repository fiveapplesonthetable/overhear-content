# Authoring module for kukhnya-s03e02-scene-12.
ID = 'kukhnya-s03e02-scene-12'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 2
SCENE = 12
TITLE = 'Кто это сделал?  (Who Did This?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'katya': 'Катя', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.02'
SOURCE_FILE = 'sources/kukhnya/s03/e02.ru.srt'
INTRO = 'When Nagiyev refuses to take no for an answer, Barinov has to confess what the secret ingredient actually was, sending Nagiyev storming into the kitchen for answers.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That concludes Scene Twelve. Watch how quickly everyone in the kitchen points fingers once Nagiyev learns what was in the balsamic pearls. See you next time!'
CLOSING = ('katya', 'Пока!')
STORY = [
    ('nagiyev', 'Мне впервые блюдо понравилось!', 'For the first time I liked a dish!', [(170, 'Мне впервые блюдо понравилось')], ''),
    ('nagiyev', 'У тебя нет ингредиента? Почему не заказал? Облажался, да?', "You don't have the ingredient? Why didn't you order it? You messed up, huh?", [(171, 'У тебя нет ингредиента. Почему не заказал'), (172, 'Облажался, да')], 'adapted'),
    ('barinov', 'Дима, давай я тебе сделаю что-нибудь своё.', 'Dima, let me make you something of my own.', [(172, 'Дима, давай я тебе сделаю что-нибудь свое')], ''),
    ('nagiyev', 'Я просто хочу то блюдо, которое понравилось мне днём.', 'I just want that dish that I liked in the afternoon.', [(173, 'Я просто хочу то блюдо, которое понравилось мне днем')], ''),
    ('barinov', 'Хорошо, я принесу тебе это блюдо.', 'Fine, I will bring you that dish.', [(174, 'Хорошо, я принесу тебе это блюдо')], ''),
    ('barinov', 'Извините. Только назову тебе очень важный ингредиент.', 'Excuse me. Only I will name the very important ingredient for you.', [(175, 'Извините. Только назову тебе очень важный ингредиент')], ''),
    ('nagiyev', 'Это ты! Ты сделал, да?', 'It was you! You did it, right?', [(176, 'Это ты'), (177, 'Ты сделал, да')], 'adapted'),
    ('nagiyev', 'Кто в тарелку положил мне это?', 'Who put this on my plate?', [(178, 'в тарелку')], 'adapted'),
    ('katya', 'Это не для вас было сделано.', 'That was not made for you.', [(179, 'Это не для вас было сделано')], ''),
    ('nagiyev', 'Для кого?', 'For whom?', [(179, 'Для кого')], ''),
    ('katya', 'Для этих двоих. Они первые начали.', 'For these two. They started it first.', [(180, 'Для этих двоих. Они первые начали')], ''),
    ('barinov', 'Это Федя всё придумал, барана притащил.', 'Fedya came up with all of it, he brought the ram in.', [(181, 'Это Федя все придумал'), (181, 'притащил')], 'adapted'),
]
WALK = [
    (0, None, "'For the first time I liked a dish!' Nagiyev continues decisively toward Barinov, shifting the mood of the conversation in a single beat."),
    (1, None, '\'You don\'t have the ingredient? Why didn\'t you order it? You messed up, huh?\' Focusing on the ingredient on the spot, Nagiyev uses "ingrediyenta" ("ingredient", from "ingrediyent") to make the point stick.'),
    (2, None, '\'Dima, let me make you something of my own.\' Speaking calmly during the talk, Barinov starts with "davay" ("come on, let\'s") to invite Nagiyev right into the action.'),
    (3, None, "'I just want that dish that I liked in the afternoon.' Nagiyev speaks promptly toward Barinov, making his position completely clear."),
    (4, None, '\'Fine, I will bring you that dish.\' Discussing the dish beside Nagiyev, Barinov uses "blyudo" ("dish") to carry the main weight of the thought.'),
    (5, None, "'Excuse me. Only I will name the very important ingredient for you.' Barinov counters boldly without a pause, watching Nagiyev's face to see how the news lands."),
    (6, None, "'It was you! You did it, right?' Nagiyev checks curiously where this conversation is heading next."),
    (7, None, '\'Who put this on my plate?\' Pointing to his plate at once, Nagiyev centers the thought on "tarelku" ("plate, platter", from "tarelka") without wasting a word.'),
    (8, None, "'That was not made for you.' Katya speaks steadily beside Nagiyev, shifting the mood of the conversation in a single beat."),
    (9, None, "'For whom?' Nagiyev checks bluntly how Katya expects that to work in practice."),
    (10, None, '\'For these two. They started it first.\' Katya follows up promptly during the talk and leans on "pervyye" ("first", a form of "pervyy") to give the remark its edge.'),
    (11, None, '\'Fedya came up with all of it, he brought the ram in.\' Emphasizing the ram around Katya, Barinov brings in "pritashchil" ("dragged in", from "pritashchit") as the key Russian word here.'),
]
