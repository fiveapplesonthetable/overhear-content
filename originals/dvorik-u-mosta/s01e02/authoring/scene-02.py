# Authoring module for dvorik-u-mosta-s01e02-scene-02.
ID = 'dvorik-u-mosta-s01e02-scene-02'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = 'В холодильнике нет молока  (No Milk in the Fridge)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'zoya': 'Зоя', 'kira': 'Кира', 'yaroslav': 'Ярослав'}
INTRO = 'Back in the café kitchen, Zoya opens the fridge and gasps just as Kira and owner Yaroslav walk in. Eight guests are waking up upstairs, and breakfast starts in twenty minutes. Listen first.'
OPENER = "Now let's break down the kitchen emergency line by line."
TRANSITION = "Let's hear the whole conversation again from beginning to end."
OUTRO = "Armed with a shopping list and cash from the till, Kira sprints toward the morning market. Let's see what she comes back with next time."
CLOSING = ('kira', 'Удачи!')
STORY = [
    ('zoya', 'Ой, беда! Ярослав Ильич, Кира, у нас на кухне авария!', 'Oh, trouble! Yaroslav Ilyich, Kira, we have a kitchen emergency!'),
    ('yaroslav', 'Пожалуйста, не говорите слово авария до утреннего кофе!', 'Please do not say the word emergency before morning coffee!'),
    ('zoya', 'У машины с фермы сломалось колесо. Посмотрите в холодильник!', 'The farm van broke a wheel. Look inside the fridge!'),
    ('kira', 'Капля молока, два яйца, а масла в холодильнике совсем не было!', 'A drop of milk, two eggs, and there was no butter in the fridge at all!'),
    ('yaroslav', 'В половине восьмого вниз спустятся восемь голодных гостей!', 'At half past seven eight hungry guests will come down the stairs!'),
    ('zoya', 'По крайней мере, мой хлеб уже в духовке.', 'My bread is already in the oven, at least.'),
    ('kira', 'Дайте мне сумку и наличные деньги! Магазин на углу открывается в семь.', 'Give me a bag and cash! The corner shop opens at seven.'),
    ('yaroslav', 'Вы успеете сбегать туда и обратно за десять минут?', 'Can you make it there and back in ten minutes?'),
    ('kira', 'Смотрите! Говорите точно, какие продукты нам нужны.', 'Watch me! Tell me exact details on which groceries we need.'),
    ('zoya', 'Нам нужны три бутылки молока, двадцать яиц, масло, сыр и красные яблоки!', 'We need three bottles of milk, twenty eggs, butter, cheese, and red apples!'),
    ('yaroslav', 'Вот пять тысяч из кассы. И мне обязательно нужен чек!', 'Here is five thousand from the cash box. And I definitely need a receipt!'),
    ('kira', 'Ждите меня — я уже бегу за дверь!', 'Wait for me — I am already running out the door!'),
]
WALK = [
    (0, None, ["'Oh, trouble! Yaroslav Ilyich, Kira, we have a kitchen emergency!' Notice ", (None, 'у нас на кухне'), " stacking 'by us' with 'in the kitchen' to set the scene fast."]),
    (1, None, ["'Please do not say the word emergency before morning coffee!' Yaroslav begs for calm before his caffeine: ", (None, 'до утреннего кофе!'), " means 'before morning coffee'."]),
    (2, None, ["'The farm van broke a wheel. Look inside the fridge!' A refrigerator has a transparent name, ", (None, 'холодильник!'), " — literally 'the cold-maker', built from the word for cold."]),
    (3, None, ["'A drop of milk, two eggs, and there was no butter in the fridge at all!' Absence in the past uses ", (None, 'не было!'), ' which never changes for gender or plural items.']),
    (4, None, ["'At half past seven eight hungry guests will come down the stairs!' Telling the half-hour looks forward to the next hour, so ", (None, 'В половине восьмого'), " literally says 'in half of the eighth'."]),
    (5, None, ["'At least the bread dough is already in the oven.' In the kitchen Zoya prepares ", (None, 'хлеб'), ' for dough, sitting warm inside the oven.']),
    (6, None, ["'Give me a bag and cash! The corner shop opens at seven.' Physical bills and coins are ", (None, 'наличные деньги!'), " — 'on-hand money', as opposed to a bank card."]),
    (7, None, ["'Can you make it there and back in ten minutes?' One brisk action word, ", (None, 'успеете'), " captures 'manage to do it in time before the deadline'."]),
    (8, None, "'Watch me! Tell me exact details on which groceries we need.' Kira doesn't hesitate for a second, turning Yaroslav's panic into a practical shopping list."),
    (9, None, ["'We need three bottles of milk, twenty eggs, butter, cheese, and red apples!' Because groceries are plural, 'needed' takes its plural shape ", (None, 'Нам нужны'), " — 'to us are needed'."]),
    (10, None, ["'Here is five thousand from the cash box. And I definitely need a receipt!' Compare that with singular masculine 'receipt': now Yaroslav says ", (None, 'нужен чек!'), ' matching the single slip of paper.']),
    (11, None, ["'Wait for me — I am already running out the door!' Right now in motion on one urgent errand, Kira uses ", (None, 'уже бегу'), " — 'I am already running'."]),
]
