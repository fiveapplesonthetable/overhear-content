# Authoring module for dvorik-u-mosta-s02e05-scene-01.
ID = 'dvorik-u-mosta-s02e05-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 5
SCENE = 1
TITLE = 'Это просто соседка  (Only the Neighbour Next Door)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'matvey': 'Матвей', 'yaroslav': 'Ярослав'}
INTRO = "At ten o'clock on Tuesday night at the Bridge Courtyard Inn, Kira, Matvey, and Yaroslav hurry to the front door expecting an early city inspector, and find their next-door neighbour smiling on the step instead. Listen first."
OPENER = "Let's open that late-night envelope again, one line at a time."
TRANSITION = "Now let's hear the whole late-night scene again from start to finish."
OUTRO = "Sugar and salt are clearly labelled in red, the checklist is clear, and Wednesday's six o'clock kitchen shift is waiting. See you next time."
CLOSING = ('kira', 'Спокойной ночи!')
STORY = [
    ('yaroslav', 'Фух! Моё сердце чуть не прыгнуло выше нашего дерева!', 'Phew! My heart nearly jumped higher than our tree!'),
    ('kira', 'Это была просто соседка из книжного магазина с нашей почтой!', 'It was just the neighbour from the bookshop with our mail!'),
    ('matvey', 'Прочитай городской конверт с печатью, Кира.', 'Read the city envelope with the stamp, Kira.'),
    ('kira', '«Отдел охраны памятников. Проверка кафе: в среду, ровно в три».', "'Heritage office. Café inspection: on Wednesday, at three sharp.'"),
    ('yaroslav', 'Слава богу, не сегодня! Прочитайте список внутри, Кира!', 'Thank goodness, not tonight! Read the list inside, Kira!'),
    ('kira', 'Первое: понятная вывеска и открытый вход во двор для соседей.', 'One: a clear sign and an open way into the courtyard for neighbours.'),
    ('matvey', 'Ворота смазаны, деревянная вывеска покрашена. Готово.', 'Gate oiled, wooden sign painted. Done.'),
    ('kira', 'Второе: светлые безопасные места внутри, горячий чай и еда.', 'Two: bright, safe seats inside, hot tea and food.'),
    ('yaroslav', 'Двенадцать стульев, чистые окна, новый провод... и две загадочные белые банки!', 'Twelve chairs, clean windows, new wire... and two mysterious white jars!'),
    ('matvey', 'Подпиши эти банки прямо сейчас, Кира, пока никто не лёг спать.', 'Label those jars right now, Kira, before anyone goes to bed.'),
    ('kira', 'Левая банка... сладко! Правая... солоно, как море! Две красные надписи!', 'Left jar... sweet! Right one... salty as the sea! Two red labels!'),
    ('yaroslav', 'Всё, мы спасены! Все спать, в шесть утра на кухню!', "That's it, we're saved! Everyone to bed, kitchen at six in the morning!"),
]
WALK = [
    (0, None, ["'Phew! My heart nearly jumped higher than our tree!' The little chunk ", (None, 'чуть не'), " means 'almost', and it is used for things that luckily did not happen.", ]),
    (1, None, ["'It was just the neighbour from the bookshop with our mail!' The neighbour is a woman, so Kira says ", (None, 'соседка'), "; a man next door would be the shorter word without the final sound."]),
    (2, None, ["'Read the city envelope with the stamp, Kira.' Matvey describes the envelope as ", (None, 'с печатью,'), " 'with a stamp', and an official stamp is exactly what every Russian document wants."]),
    (3, None, ["'Heritage office. Café inspection: on Wednesday, at three sharp.' For 'sharp' Russian puts one small word in front of the time: ", (None, 'ровно в три'), ", literally 'evenly at three'."]),
    (4, None, ["'Thank goodness, not tonight! Read the list inside, Kira!' Yaroslav's relief, ", (None, 'Слава богу,'), " is literally 'glory to God', and people say it all day without thinking of church."]),
    (5, None, ["'One: a clear sign and an open way into the courtyard for neighbours.' Lists in Russian often count with ", (None, 'Первое:'), ", 'the first', instead of a plain number."]),
    (6, None, ["'Gate oiled, wooden sign painted. Done.' To tick off a job, just say ", (None, 'Готово.'), " It means 'ready' or 'done', and it works for soup, homework and gates."]),
    (7, None, ["'Two: bright, safe seats inside, hot tea and food.' Kira reads ", (None, 'места внутри,'), " and the first word, 'places', is also how Russians ask about free seats on a train."]),
    (8, None, ["'Twelve chairs, clean windows, new wire... and two mysterious white jars!' Yaroslav's ", (None, 'загадочные'), " comes from the word for a riddle, so the jars are literally 'riddle-like'."]),
    (9, None, ["'Label those jars right now, Kira, before anyone goes to bed.' Going to bed is ", (None, 'лёг спать.'), ", literally 'lay down to sleep', a pair you can reuse every night."]),
    (10, None, ["'Left jar... sweet! Right one... salty as the sea! Two red labels!' Kira tastes and reports the feeling, not the thing: ", (None, 'солоно,'), " is 'it is salty', the way you would say 'it is cold'."]),
    (11, None, ["'That's it, we're saved! Everyone to bed, kitchen at six in the morning!' Russian can drop the verb in an order like ", (None, 'Все спать,'), " which simply means 'everyone, sleep'."]),
]
