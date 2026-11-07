# Authoring module for dvorik-u-mosta-s02e01-scene-07.
ID = 'dvorik-u-mosta-s02e01-scene-07'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 1
SCENE = 7
TITLE = 'Считаем деньги  (Count the Coins)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'yaroslav': 'Ярослав', 'kira': 'Кира', 'zoya': 'Зоя'}
INTRO = "At the front desk, Yaroslav is adding numbers on a notepad with a worried frown when Kira and Zoya show him the thirty-year-old courtyard postcard. Listen first."
OPENER = "Now let's count the costs with them, line by line."
TRANSITION = "Now let's hear the whole conversation again from start to finish."
OUTRO = "With a practical budget and full guest rooms upstairs, Yaroslav gives the green light for Friday at six. One last scene for Episode 1, so let's listen."
CLOSING = ('yaroslav', 'До завтра!')
STORY = [
    ('yaroslav', 'Фото чудесное, правда. Но новая мебель для кафе стоит целое состояние!', 'The photo is wonderful, truly. But new café furniture costs a fortune!'),
    ('kira', 'А кто говорит о дорогой новой мебели, Ярослав Ильич?', 'And who is talking about expensive new furniture, Yaroslav Ilyich?'),
    ('zoya', 'В подвале уже есть четыре деревянных стола, а наверху белые скатерти.', 'There are already four wooden tables in the cellar, and white tablecloths upstairs.'),
    ('yaroslav', 'А стулья, чашки, зелёная краска для ставен, лампы?', 'And chairs, cups, green paint for the shutters, lamps?'),
    ('kira', 'Вот мой список: две банки краски, двенадцать чашек и лимоны с рынка.', 'Here is my list: two cans of paint, twelve cups and lemons from the market.'),
    ('zoya', 'А Роман и Глеб помогут принести столы бесплатно!', 'And Roman and Gleb will help bring the tables for free!'),
    ('yaroslav', 'Подождите, я проверю ещё раз... Только столько на всю комнату?', 'Wait, let me check again... Only this much for the whole room?'),
    ('kira', 'На этой неделе все номера заняты. Мы можем заплатить сегодня наличными.', 'This week all the rooms are taken. We can pay in cash today.'),
    ('yaroslav', 'И город хочет увидеть наше кафе открытым до конца месяца!', 'And the city wants to see our café open before the end of the month!'),
    ('zoya', 'Скажите «да», Ярослав Ильич, пока вы снова не потеряли очки!', "Say 'yes', Yaroslav Ilyich, before you lose your glasses again!"),
    ('yaroslav', 'Хорошо, да! Девятый номер открывается в следующую пятницу в шесть!', 'All right, yes! Room nine opens next Friday at six!'),
    ('kira', 'Отлично! Пойдёмте проверим лампу в зимнем саду!', "Great! Let's go and check the lamp in the winter garden!"),
]
WALK = [
    (0, None, ["'The photo is wonderful, truly. But new café furniture costs a fortune!' Russian prices things like 'a whole fortune': ", (None, 'целое состояние!'), " is the same big exaggeration as in English."]),
    (1, None, ["'And who is talking about expensive new furniture, Yaroslav Ilyich?' One word does two jobs: ", (None, 'дорогой'), " is 'expensive' here, and 'dear' when you greet a loved one."]),
    (2, None, ["'There are already four wooden tables in the cellar, and white tablecloths upstairs.' Zoya means one cloth for every table, so she uses the plural ", (None, 'скатерти.'), " Linen for the tables is already in the house."]),
    (3, None, ["'And chairs, cups, green paint for the shutters, lamps?' Yaroslav lists his worries with ", (None, 'А стулья,'), ", 'and what about chairs?', where the little word for 'and' raises a new point."]),
    (4, None, ["'Here is my list: two cans of paint, twelve cups and lemons from the market.' After 'twelve', cups switch to the 'many of' form: ", (None, 'двенадцать чашек'), "."]),
    (5, None, ["'And Roman and Gleb will help bring the tables for free!' Something free of charge is ", (None, 'бесплатно!'), ", made from 'without' plus 'payment'."]),
    (6, None, ["'Wait, let me check again... Only this much for the whole room?' Yaroslav double-checks with ", (None, 'ещё раз...'), " 'one more time', a chunk you can add to any request."]),
    (7, None, ["'This week all the rooms are taken. We can pay in cash today.' Paying 'with cash' is one word: ", (None, 'наличными.'), " means 'with the money on hand'."]),
    (8, None, ["'And the city wants to see our café open before the end of the month!' The chunk ", (None, 'до конца месяца!'), " is 'until the end of the month', a classic deadline phrase."]),
    (9, None, ["'Say yes, Yaroslav Ilyich, before you lose your glasses again!' Zoya teases him with ", (None, 'пока вы снова не потеряли'), ", where 'while... not' means 'before'."]),
    (10, None, ["'All right, yes! Room nine opens next Friday at six!' Time is easy: ", (None, 'в шесть!'), " is 'at six', just 'in' plus the number."]),
    (11, None, ["'Great! Let's go and check the lamp in the winter garden!' Kira suggests going together with the polite ", (None, 'Пойдёмте'), ", 'let's go', which includes her boss."]),
]
