ID = 'kukhnya-s03e02-scene-12'
SHOW = "kukhnya"
SEASON = 3
EPISODE = 2
SCENE = 12
TITLE = 'Кто это сделал?  (Who Did This?)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'chef': 'anja', 'katya': 'angelina'}
LABELS = {'anya': 'Нагиев', 'chef': 'Шеф', 'katya': 'Катя'}
SOURCE_NAME = "Кухня (Kukhnya) S3.02"
SOURCE_FILE = 'sources/kukhnya/s03/e02.ru.srt'

INTRO = 'When Nagiyev refuses to take no for an answer, Barinov has to confess what the secret ingredient actually was, sending Nagiyev storming into the kitchen for answers.'

STORY = [
    ('anya', 'Мне впервые блюдо понравилось!', 'For the first time I liked a dish!', [(170, 'Мне впервые блюдо понравилось')], ''),
    ('anya', 'У тебя нет ингредиента? Почему не заказал? Облажался, да?', "You don't have the ingredient? Why didn't you order it? You messed up, huh?", [(171, 'У тебя нет ингредиента. Почему не заказал'), (172, 'Облажался, да')], 'adapted'),
    ('chef', 'Дима, давай я тебе сделаю что-нибудь своё.', 'Dima, let me make you something of my own.', [(172, 'Дима, давай я тебе сделаю что-нибудь свое')], ''),
    ('anya', 'Я просто хочу то блюдо, которое понравилось мне днём.', 'I just want that dish that I liked in the afternoon.', [(173, 'Я просто хочу то блюдо, которое понравилось мне днем')], ''),
    ('chef', 'Хорошо, я принесу тебе это блюдо.', 'Fine, I will bring you that dish.', [(174, 'Хорошо, я принесу тебе это блюдо')], ''),
    ('chef', 'Извините. Только назову тебе очень важный ингредиент.', 'Excuse me. Only I will name the very important ingredient for you.', [(175, 'Извините. Только назову тебе очень важный ингредиент')], ''),
    ('anya', 'Это ты! Ты сделал, да?', 'It was you! You did it, right?', [(176, 'Это ты'), (177, 'Ты сделал, да')], 'adapted'),
    ('anya', 'Кто в тарелку положил мне это?', 'Who put this on my plate?', [(178, 'в тарелку')], 'adapted'),
    ('katya', 'Это не для вас было сделано.', 'That was not made for you.', [(179, 'Это не для вас было сделано')], ''),
    ('anya', 'Для кого?', 'For whom?', [(179, 'Для кого')], ''),
    ('katya', 'Для этих двоих. Они первые начали.', 'For these two. They started it first.', [(180, 'Для этих двоих. Они первые начали')], ''),
    ('chef', 'Это Федя всё придумал, барана притащил.', 'Fedya came up with all of it, he brought the ram in.', [(181, 'Это Федя все придумал'), (181, 'притащил')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'For the first time I liked a dish!' Notice how Russian expresses 'to me' and 'pleased' with crisp inflection rather than helper words."),
    (1, None, "'You don't have the ingredient? Why didn't you order it? You messed up, huh?' Here the Russian phrasing highlights 'at' before landing on 'yes'."),
    (2, None, "'Dima, let me make you something of my own.' The grammar packs 'Dima' and 'one's own' into a tight, idiomatic kitchen exchange."),
    (3, None, "'I just want that dish that I liked in the afternoon.' Notice how Russian expresses 'I' and 'in the afternoon' with crisp inflection rather than helper words. Chef Barinov answers right away."),
    (4, None, "'Fine, I will bring you that dish.' Here the Russian phrasing highlights 'well' before landing on 'dish'."),
    (5, None, "'Excuse me. Only I will name the very important ingredient for you.' The meaning hinges on 'excuse me' working together with 'ingredient' in spoken Russian."),
    (6, None, "'It was you! You did it, right?' In Russian, the idea of 'this' flows naturally into 'yes' without extra filler words."),
    (7, None, "'Who put this on my plate?' Here the Russian phrasing highlights 'who' before landing on 'this'."),
    (8, None, "'That was not made for you.' Notice how Russian expresses 'this' and 'made' with crisp inflection rather than helper words."),
    (9, None, "'For whom?' Spoken Russian keeps this brisk, leaning on 'for' and finishing on 'whom'. Katya answers right away."),
    (10, None, "'For these two. They started it first.' Katya anchors the line on 'for', while 'started' completes the thought."),
    (11, None, "'Fedya came up with all of it, he brought the ram in.' Here the Russian phrasing highlights 'this' before landing on 'dragged in'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That concludes Scene Twelve. Watch how quickly everyone in the kitchen points fingers once Nagiyev learns what was in the balsamic pearls.'
CLOSING = ('katya', 'Это было не для вас!')
