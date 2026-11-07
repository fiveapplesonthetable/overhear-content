# Authoring module for dvorik-u-mosta-s02e06-scene-01.
ID = 'dvorik-u-mosta-s02e06-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 6
SCENE = 1
TITLE = 'Сорок жёлтых лимонов  (Forty Yellow Lemons)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'zoya': 'Зоя', 'kira': 'Кира', 'gleb': 'Глеб'}
INTRO = 'Friday morning dawns bright and clear at the Bridge Courtyard Inn, and today is opening day for the Room 9 garden café! In the kitchen, Zoya stands happily at her counter without pillows while Kira and Gleb roll up their sleeves over bowls of yellow lemons. Listen first.'
OPENER = "Now let's squeeze this busy kitchen morning one line at a time."
TRANSITION = "Now listen to the whole lemon-squeezing morning again from start to finish."
OUTRO = 'Zoya is back on her feet, the sugar jar is checked twice, and forty lemons are turning into golden tarts for tonight. See you next time.'
CLOSING = ('zoya', 'Увидимся!')
STORY = [
    ('kira', 'Зоя! Смотри, ты стоишь у плиты на двух ногах!', 'Zoya! Look, you are standing at the stove on both feet!'),
    ('zoya', 'Два дня на подушках — и чудо: сегодня совсем не болит!', 'Two days on pillows, and a miracle: today it does not hurt at all!'),
    ('gleb', 'И очень вовремя, шеф: мы принесли с рынка сорок свежих лимонов.', 'And just in time, Chef: we brought forty fresh lemons from the market.'),
    ('zoya', 'Сорок лимонов — это четыре больших противня миндального пирога к шести!', 'Forty lemons means four big trays of almond tart by six!'),
    ('kira', 'Зоя, как ты думаешь, сколько соседей сегодня придёт?', 'Zoya, how many neighbours do you think will come today?'),
    ('zoya', 'На Липовом переулке новости летят быстро, когда есть музыка и тёплый хлеб!', 'On Lipovy Lane news flies fast when there is music and warm bread!'),
    ('gleb', 'Я уже порезал десять лимонов, а Кира взбивает яйца с сахаром.', 'I have already sliced ten lemons, and Kira is beating the eggs with sugar.'),
    ('zoya', 'Кира, ты сначала проверила большую красную надпись на банке с сахаром?', 'Kira, did you check the big red label on the sugar jar first?'),
    ('kira', 'Проверила два раза и попробовала щепотку! Сладко, как летом!', 'I checked twice and tasted a pinch! Sweet as summer!'),
    ('gleb', 'А горячий чай на двадцать четыре чашки сразу, Зоя?', 'And what about hot tea for twenty-four cups at once, Zoya?'),
    ('zoya', 'Два больших чайника чёрного чая, два с мятой из дворика и горячее молоко.', 'Two big pots of black tea, two with mint from the courtyard, and hot milk.'),
    ('kira', 'Первый противень — в духовку! Шесть часов, мы идём!', 'The first tray goes into the oven! Six o\'clock, here we come!'),
]
WALK = [
    (0, None, ["'Zoya! Look, you are standing at the stove on both feet!' Russians stand 'by' a stove, not 'at' it: ", (None, 'у плиты'), " uses the little word for 'next to'."]),
    (1, None, ["'Two days on pillows, and a miracle: today it does not hurt at all!' There is no 'it' and no 'my ankle' in ", (None, 'совсем не болит!'), " The verb alone says that something hurts."]),
    (2, None, ["'And just in time, Chef: we brought forty fresh lemons from the market.' Gleb borrows Matvey's nickname for the boss: ", (None, 'шеф:'), " works for any head cook too."]),
    (3, None, ["'Forty lemons means four big trays of almond tart by six!' A deadline hour takes 'towards' in Russian, so ", (None, 'к шести!'), " means 'by six', ready in time."]),
    (4, None, ["'Zoya, how many neighbours do you think will come today?' Kira slips in ", (None, 'как ты думаешь,'), " literally 'how do you think', where English says 'what'."]),
    (5, None, ["'On Lipovy Lane news flies fast when there is music and warm bread!' In Russian news does not travel, it flies: ", (None, 'новости летят'), " is 'news is flying'."]),
    (6, None, ["'I have already sliced ten lemons, and Kira is beating the eggs with sugar.' Recipes mix things 'with' each other: ", (None, 'яйца с сахаром.'), " is 'eggs with sugar'."]),
    (7, None, ["'Kira, did you check the big red label on the sugar jar first?' A jar 'with' sugar is how Russians name it: ", (None, 'банке с сахаром?'), " means 'the sugar jar'."]),
    (8, None, ["'I checked twice and tasted a pinch! Sweet as summer!' A tiny amount of salt or sugar is ", (None, 'щепотку!'), " the bit you pick up between two fingers."]),
    (9, None, ["'And what about hot tea for twenty-four cups at once, Zoya?' Handy little ", (None, 'сразу,'), " means 'at once', all together in one go."]),
    (10, None, ["'Two big pots of black tea, two with mint from the courtyard, and hot milk.' Zoya says ", (None, 'чайника'), ", from the everyday word for a teapot or a kettle; Russian uses one word for both."]),
    (11, None, ["'The first tray goes into the oven! Six o'clock, here we come!' Kira skips the verb completely: ", (None, 'в духовку!'), " 'into the oven!' is enough when the action is obvious."]),
]
