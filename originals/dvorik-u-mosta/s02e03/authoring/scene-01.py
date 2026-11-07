# Authoring module for dvorik-u-mosta-s02e03-scene-01.
ID = 'dvorik-u-mosta-s02e03-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 3
SCENE = 1
TITLE = 'Осталось три дня  (Three Days Left)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'zoya': 'Зоя', 'yaroslav': 'Ярослав'}
INTRO = 'On Sunday morning at the Bridge Courtyard Inn, Yaroslav paces beside the breakfast counter with three pages of worried notes while Kira and Zoya pour coffee and plan the week. Listen to the scene first.'
OPENER = "Let's go back through the morning planning session line by line."
TRANSITION = "Now let's listen to the whole café-corner plan again from start to finish."
OUTRO = "Three days, three clear steps, and Yaroslav's aunt's green guest book is finally on the table. See you in the next scene."
CLOSING = ('kira', 'До встречи!')
STORY = [
    ('yaroslav', 'Воскресенье, понедельник, вторник... а в среду в три часа приходит инспектор!', 'Sunday, Monday, Tuesday... and on Wednesday at three the inspector comes!'),
    ('zoya', 'Сядьте и выпейте горячий кофе, пока не пролили, Ярослав Ильич.', 'Sit down and drink your hot coffee before you spill it, Yaroslav Ilyich.'),
    ('kira', 'Посмотрите на нашу доску: три дня, три простых дела.', 'Look at our board: three days, three simple jobs.'),
    ('yaroslav', 'Всего три дела?! Вчера девятый номер был полон пыли и молчащих клавиш!', 'Only three jobs?! Yesterday room nine was full of dust and silent keys!'),
    ('kira', 'Воскресенье: помыть все окна и прочитать гостевую книгу вашей тёти.', "Sunday: wash all the windows and read your aunt's guest book."),
    ('zoya', 'Понедельник: покрасить ставни в тёплый зелёный и поставить двенадцать стульев.', 'Monday: paint the shutters warm green and set out twelve chairs.'),
    ('kira', 'Вторник: починить молчащую клавишу и испечь лимонные пироги на среду!', 'Tuesday: fix the silent key and bake lemon tarts for Wednesday!'),
    ('yaroslav', 'Когда гора делится на три маленьких холма, я снова могу дышать!', 'When a mountain splits into three little hills, I can breathe again!'),
    ('zoya', 'Ярослав Ильич, где старая зелёная книга с чердака?', 'Yaroslav Ilyich, where is the old green book from the attic?'),
    ('yaroslav', 'Вот она, под мышкой! Подождите... а где моя чашка кофе?', 'Here it is, under my arm! Wait... where is my cup of coffee?'),
    ('kira', 'В вашей левой руке, Ярослав Ильич.', 'In your left hand, Yaroslav Ilyich.'),
    ('zoya', 'Отдохните десять минут, шеф! Книгу прочитают Кира и Лариса Борисовна.', 'Rest for ten minutes, boss! Kira and Larisa Borisovna will read the book.'),
]
WALK = [
    (0, None, ["'Sunday, Monday, Tuesday... and on Wednesday at three the inspector comes!' Days of the week are lowercase in Russian, and a day takes the little word 'in': ", (None, 'в среду'), " is 'on Wednesday'."]),
    (1, None, ["'Sit down and drink your hot coffee before you spill it, Yaroslav Ilyich.' Russian sneaks a 'not' into this kind of warning: ", (None, 'пока не пролили,'), " is literally 'while you have not spilled it'."]),
    (2, None, ["'Look at our board: three days, three simple jobs.' Kira says ", (None, 'три простых дела.'), " Its last word covers a job, a task, even a matter or affair, so you will hear it everywhere."]),
    (3, None, ["'Only three jobs?! Yesterday room nine was full of dust and silent keys!' Yaroslav's ", (None, 'Всего'), " means 'only' here, though it literally comes from 'of everything', as in 'that's all there is'."]),
    (4, None, ["'Sunday: wash all the windows and read your aunt's guest book.' In Russian the owner comes after the thing: ", (None, 'книгу вашей тёти.'), " is 'the book of your aunt'."]),
    (5, None, ["'Monday: paint the shutters warm green and set out twelve chairs.' Russians paint something 'into' a colour: ", (None, 'в тёплый зелёный'), " is 'into warm green'."]),
    (6, None, ["'Tuesday: fix the silent key and bake lemon tarts for Wednesday!' For a deadline or a target day Russian uses 'on', so ", (None, 'на среду!'), " means 'for Wednesday', ready by then."]),
    (7, None, ["'When a mountain splits into three little hills, I can breathe again!' Keep ", (None, 'снова'), " handy: it means 'again', and you can drop it into almost any sentence."]),
    (8, None, ["'Yaroslav Ilyich, where is the old green book from the attic?' Zoya wants the book that came ", (None, 'с чердака?'), " 'from the attic', down off the very top of the house."]),
    (9, None, ["'Here it is, under my arm! Wait... where is my cup of coffee?' Russians carry things ", (None, 'под мышкой!'), " which is literally 'under the armpit', the everyday way to say 'under my arm'."]),
    (10, None, ["'In your left hand, Yaroslav Ilyich.' Kira says ", (None, 'левой руке,'), " and that second word means both 'hand' and 'arm', so the context decides."]),
    (11, None, ["'Rest for ten minutes, boss! Kira and Larisa Borisovna will read the book.' Zoya puts the object first, ", (None, 'Книгу прочитают'), ", to say 'the book, they will read it', which keeps the focus on the book."]),
]
