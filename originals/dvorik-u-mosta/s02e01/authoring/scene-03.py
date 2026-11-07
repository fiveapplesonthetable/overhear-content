# Authoring module for dvorik-u-mosta-s02e01-scene-03.
ID = 'dvorik-u-mosta-s02e01-scene-03'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 1
SCENE = 3
TITLE = 'Стекло и пыль  (Glass and Dust)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'zoya': 'Зоя', 'yaroslav': 'Ярослав'}
INTRO = "Kira pushes the narrow white door open, and morning light filters through dusty glass into a quiet, forgotten room. Zoya and Yaroslav step inside behind her in amazement. Listen to the whole scene first."
OPENER = "Let's step into Room 9 slowly and look around, line by line."
TRANSITION = "Now let's hear the whole scene again without stopping."
OUTRO = "Room 9 is a dry, sunlit glass tea room, and something tall is waiting under a white sheet in the corner. Let's find out what it is next time."
CLOSING = ('yaroslav', 'До свидания!')
STORY = [
    ('kira', 'Посмотрите на эти высокие стеклянные окна! Они выходят во двор!', 'Look at these tall glass windows! They look out onto the courtyard!'),
    ('zoya', 'Снаружи закрыты ставни, поэтому со двора никто их не видел.', 'The shutters are closed outside, so nobody saw them from the courtyard.'),
    ('yaroslav', 'Теперь я вспомнил! Дядя называл её зимней чайной комнатой.', 'Now I remember! My uncle called it the winter tea room.'),
    ('kira', 'Почему кто-то спрятал такую светлую комнату за шкафом?', 'Why did someone hide such a bright room behind a bookcase?'),
    ('yaroslav', 'Однажды весной стеклянная крыша протекла, а денег на ремонт не было.', 'One spring the glass roof leaked, and there was no money for repairs.'),
    ('zoya', 'Посмотрите на пол, Ярослав Ильич. Сухой камень, ни капли воды!', 'Look at the floor, Yaroslav Ilyich. Dry stone, not a drop of water!'),
    ('kira', 'Кто-то давно починил крышу во дворе и этот потолок тоже!', 'Someone fixed the courtyard roof long ago, and this ceiling too!'),
    ('zoya', 'Ярослав Ильич, сколько маленьких столиков здесь поместится?', 'Yaroslav Ilyich, how many little tables will fit in here?'),
    ('yaroslav', 'Подождите! Мы обещали городу открыть кафе для всех соседей!', 'Wait! We promised the city we would open a café for all the neighbours!'),
    ('kira', 'И вот комната, о которой писали в письме из города!', 'And here is the room the letter from the city was talking about!'),
    ('zoya', 'Тёплый хлеб, горячий чай, утреннее солнце и никакого ветра!', 'Warm bread, hot tea, morning sun and no wind at all!'),
    ('yaroslav', 'Стойте, а что это в углу под большой белой тканью?', 'Hold on, and what is that in the corner under the big white cloth?'),
]
WALK = [
    (0, None, ["'Look at these tall glass windows! They look out onto the courtyard!' Glass becomes a describing word with one ending: ", (None, 'стеклянные'), " means 'made of glass'."]),
    (1, None, ["'The shutters are closed outside, so nobody saw them from the courtyard.' Here ", (None, 'поэтому'), " is 'that is why', built from 'by this', and it links cause and result."]),
    (2, None, ["'Now I remember! My uncle called it the winter tea room.' Russian doesn't need 'my' for family: ", (None, 'Дядя'), " alone means 'my uncle' when Yaroslav is talking about his own."]),
    (3, None, ["'Why did someone hide such a bright room behind a bookcase?' The handy ", (None, 'кто-то'), " is 'someone': the word for 'who' plus a little tail that makes it unknown."]),
    (4, None, ["'One spring the glass roof leaked, and there was no money for repairs.' To say 'there was no money', Russian uses ", (None, 'денег'), " in the 'none of' form, followed by 'was not'."]),
    (5, None, ["'Look at the floor, Yaroslav Ilyich. Dry stone, not a drop of water!' The chunk ", (None, 'ни капли воды!'), " is 'not a drop of water', and you can swap in milk or coffee."]),
    (6, None, ["'Someone fixed the courtyard roof long ago, and this ceiling too!' Two different tops: the roof outside is a ", (None, 'крышу'), ", while the ceiling inside has its own word."]),
    (7, None, ["'Yaroslav Ilyich, how many little tables will fit in here?' Zoya shrinks the word for table: ", (None, 'столиков'), " means little café tables, cosy and small."]),
    (8, None, ["'Wait! We promised the city we would open a café for all the neighbours!' The borrowed word ", (None, 'кафе'), " never changes its ending, so it looks the same in every sentence."]),
    (9, None, ["'And here is the room the letter from the city was talking about!' Kira points with ", (None, 'И вот'), ", 'and here is', the phrase for presenting something you have just found."]),
    (10, None, ["'Warm bread, hot tea, morning sun and no wind at all!' Two kinds of heat: bread is ", (None, 'Тёплый'), " or warm, while tea is properly hot."]),
    (11, None, ["'Hold on, and what is that in the corner under the big white cloth?' A plain word for 'stop!', ", (None, 'Стойте,'), " is said to a group, and it also means 'hold on'."]),
]
