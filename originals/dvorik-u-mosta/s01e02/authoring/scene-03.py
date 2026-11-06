# Authoring module for dvorik-u-mosta-s01e02-scene-03.
ID = 'dvorik-u-mosta-s01e02-scene-03'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'Считаем сдачу  (Counting the Change)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'yaroslav': 'Ярослав', 'zoya': 'Зоя'}
INTRO = 'Nine minutes later, Kira bursts back through the courtyard gate carrying two heavy cloth bags of groceries for Zoya and Yaroslav. Listen to the scene in Russian first.'
OPENER = "Now let's go back through the grocery rescue line by line."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = 'An accidental packet of salted butter nearly caused a jam crisis, until Zoya turned it into the secret ingredient for the eggs. See you next time.'
CLOSING = ('zoya', 'Увидимся!')
STORY = [
    ('kira', 'Девять минут! Вот молоко, яйца и красные яблоки!', 'Nine minutes! Here are the milk, the eggs, and the red apples!'),
    ('zoya', 'Ты просто герой, Кира! Дай мне сначала молоко для кофемашины.', 'You are simply a hero, Kira! Give me the milk first for the coffee machine.'),
    ('yaroslav', 'Какая скорость! А продавец дал вам кассовый чек?', 'What speed! And did the shopkeeper give you a till receipt?'),
    ('kira', 'Вот он! Всё стоило три тысячи восемьсот, вот тысяча двести сдачи.', 'Right here! Everything cost three thousand eight hundred, here is twelve hundred in change.'),
    ('yaroslav', 'Тысяча, сто, двести. Точно до последнего рубля — спасибо!', 'One thousand, one hundred, two hundred. Exact to the last rouble — thank you!'),
    ('zoya', 'Секунду, Кира... какую пачку масла ты взяла?', 'Wait a second, Kira... which packet of butter did you grab?'),
    ('kira', 'В золотой обёртке с верхней полки. А что?', 'In the gold wrapper from the top shelf. Why?'),
    ('zoya', 'Это же морское солёное масло! Для сладких булочек нужно обычное масло!', 'That is salty sea butter! Sweet rolls need plain butter!'),
    ('kira', 'Ой, нет! На бегу все пачки казались одинаковыми!', 'Oh no! On the run all the packets looked identical!'),
    ('yaroslav', 'Разве можно подавать солёное масло к сладкому клубничному варенью?', 'Can we really serve salty butter with sweet strawberry jam?'),
    ('zoya', 'Стойте! С одной стороны, для варенья оно не годится, а с другой стороны, для омлета это мечта!', "Hold on! On the one hand, it won't work for jam, and on the other hand, for an omelette it is a dream!"),
    ('kira', 'Фух! Быстрая смекалка снова спасает завтрак.', 'Phew! Quick thinking saves breakfast again.'),
]
WALK = [
    (0, None, ["'Nine minutes! Here are the milk, the eggs, and the red apples!' After numbers from five upward, Russian counts minutes with the short plural ", (None, 'минут!'), ' dropping the ending completely.']),
    (1, None, ["'You are simply a hero, Kira! Give me the milk first for the coffee machine.' Adding ", (None, 'просто'), " means 'simply' or 'flat-out', giving Zoya's praise extra punch."]),
    (2, None, ["'What speed! And did the shopkeeper give you a till receipt?' A shop assistant or seller is ", (None, 'продавец'), ' — built directly from the action of selling.']),
    (3, None, ["'Right here! Everything cost three thousand eight hundred, here is twelve hundred in change.' Money handed back at the till is ", (None, 'сдачи.'), " literally 'what is given back'."]),
    (4, None, ["'One thousand, one hundred, two hundred. Exact to the last rouble — thank you!' Yaroslav counts roubles with delight: ", (None, 'до последнего рубля'), " means 'down to the very last rouble'."]),
    (5, None, ["'Wait a second, Kira... which packet of butter did you grab?' Just like saying 'one moment', ", (None, 'Секунду,'), ' asks someone to hold on for a single second.']),
    (6, None, ["'In the gold wrapper from the top shelf. Why?' Two tiny words at the end, ", (None, 'А что?'), " ask 'why, what's up?' when someone looks surprised."]),
    (7, None, ["'That is salty sea butter! Sweet rolls need plain butter!' Notice neuter ", (None, 'нужно обычное масло!'), " agreeing with 'butter', while ", (None, 'Это же'), " adds 'don't you see!'."]),
    (8, None, ["'Oh no! On the run all the packets looked identical!' Doing something while sprinting uses the vivid two-word phrase ", (None, 'На бегу'), " — 'on the run'."]),
    (9, None, ["'Can we really serve salty butter with sweet strawberry jam?' Opening a question with ", (None, 'Разве'), " expresses disbelief — 'can it really be that...?'."]),
    (10, None, ["'Hold on! On the one hand, it won't work for jam, and on the other hand, for an omelette it is a dream!' Listen to ", (None, 'С одной стороны,'), ' balanced by ', (None, 'а с другой стороны,'), ' — the classic pair for weighing two sides.']),
    (11, None, "'Phew! Quick thinking saves breakfast again.' Kira exhales with universal relief as the salted-butter mistake turns into breakfast gold."),
]
