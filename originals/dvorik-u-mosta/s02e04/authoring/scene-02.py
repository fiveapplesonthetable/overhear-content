# Authoring module for dvorik-u-mosta-s02e04-scene-02.
ID = 'dvorik-u-mosta-s02e04-scene-02'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 4
SCENE = 2
TITLE = 'Зелёные очки  (Green Glasses)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'yaroslav': 'Ярослав', 'kira': 'Кира', 'matvey': 'Матвей'}
INTRO = "Wearing his spotless white shirt, Yaroslav stops beside Kira and Matvey in the hallway and reaches eagerly for the small corner brush. Let's listen in first."
OPENER = "Let's watch Yaroslav's painting lesson again, line by line."
TRANSITION = "Let's hear the whole conversation again from beginning to end."
OUTRO = "White shirt spared, green glasses rescued in time, and Yaroslav retreats safely to dry ground at the front desk! See you next time."
CLOSING = ('kira', 'Пока!')
STORY = [
    ('yaroslav', 'Какой красивый зелёный! Дайте мне кисть, хозяин тоже должен помогать!', 'What a lovely green! Give me a brush, the owner has to help too!'),
    ('matvey', 'Шеф, на вас белоснежная рубашка и чёрные туфли.', 'Boss, you are wearing a snow-white shirt and black shoes.'),
    ('yaroslav', 'Только три дощечки внизу! У меня твёрдая рука, смотрите!', 'Just three little slats at the bottom! I have a steady hand, watch!'),
    ('kira', 'Осторожно, Ярослав Ильич, рукав в двух сантиметрах от краски!', 'Careful, Yaroslav Ilyich, your sleeve is two centimetres from the paint!'),
    ('yaroslav', 'Рубашка чистая! Ха! Подождите... у меня чешется нос.', 'The shirt is clean! Ha! Wait... my nose itches.'),
    ('kira', 'Ярослав Ильич, не поднимайте руку с кистью!', "Yaroslav Ilyich, don't lift the hand with the brush!"),
    ('yaroslav', 'Почему вы оба так смотрите на мой лоб?', 'Why are you both looking at my forehead like that?'),
    ('matvey', 'Потому что вы покрасили левое стекло своих очков в зелёный.', 'Because you just painted the left lens of your glasses green.'),
    ('yaroslav', 'Очки опять были на лбу?! Ой, всё вокруг как в лесу!', 'My glasses were on my forehead again?! Oh, everything around looks like a forest!'),
    ('kira', 'Не двигайтесь! Тёплая вода и мягкая тряпка, и всё отойдёт!', "Don't move! Warm water and a soft cloth, and it will all come off!"),
    ('yaroslav', 'Как новые! Спасибо, Кира. Пойду-ка я лучше к стойке.', "Good as new! Thank you, Kira. I think I'd better go to the front desk."),
    ('matvey', 'Мудрое решение, шеф. Мокрую краску оставьте нам.', 'A wise decision, boss. Leave the wet paint to us.'),
]
WALK = [
    (0, None, ["'What a lovely green! Give me a brush, the owner has to help too!' Duty sounds like ", (None, 'должен'), ", 'must' or 'has to', which changes its ending for a man or a woman."]),
    (1, None, ["'Boss, you are wearing a snow-white shirt and black shoes.' Clothes sit 'on' you: ", (None, 'на вас'), " is 'on you', the Russian way of saying what someone is wearing."]),
    (2, None, ["'Just three little slats at the bottom! I have a steady hand, watch!' A steady hand is a 'firm' one: ", (None, 'твёрдая рука,'), " and the word for firm also means hard."]),
    (3, None, ["'Careful, Yaroslav Ilyich, your sleeve is two centimetres from the paint!' Distance is measured 'in' a number: ", (None, 'в двух сантиметрах'), ", then 'from' the thing."]),
    (4, None, ["'The shirt is clean! Ha! Wait... my nose itches.' Body troubles happen 'at me': ", (None, 'у меня чешется нос.'), " and you can swap in a hand or an ear."]),
    (5, None, ["'Yaroslav Ilyich, don't lift the hand with the brush!' Kira's warning ", (None, 'не поднимайте'), " is the polite 'don't lift', a form for warnings to anyone you call by patronymic."]),
    (6, None, ["'Why are you both looking at my forehead like that?' The tiny word ", (None, 'так'), " means 'like that' or 'so', and here it carries all of his worry."]),
    (7, None, ["'Because you just painted the left lens of your glasses green.' Painting something a colour is 'into' that colour: ", (None, 'в зелёный.'), " Russian says 'paint it into green'."]),
    (8, None, ["'My glasses were on my forehead again?! Oh, everything around looks like a forest!' The word ", (None, 'опять'), " means 'again', usually with a sigh about something that keeps happening."]),
    (9, None, ["'Don't move! Warm water and a soft cloth, and it will all come off!' An everyday rag or cloth is ", (None, 'тряпка,'), " the thing for wiping tables and spills."]),
    (10, None, ["'Good as new! Thank you, Kira. I think I'd better go to the front desk.' The little tail in ", (None, 'Пойду-ка'), " makes 'I'll go' sound casual, like 'I think I'll just go'."]),
    (11, None, ["'A wise decision, boss. Leave the wet paint to us.' A wise choice is ", (None, 'Мудрое решение,'), ", and the word for decision comes from the verb for solving."]),
]
