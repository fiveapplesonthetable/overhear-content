# Authoring module for dvorik-u-mosta-s01e02-scene-05.
ID = 'dvorik-u-mosta-s01e02-scene-05'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'Сок на галстуке  (Juice on the Tie)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'yaroslav': 'Ярослав', 'larisa': 'Лариса', 'kira': 'Кира'}
INTRO = 'Breakfast is in full swing in the sunlit café corner. Larisa Borisovna sits by the window while Yaroslav insists on serving drinks like a grand hotel host alongside Kira. Listen first.'
OPENER = "Now let's walk through breakfast at the window table."
TRANSITION = "Let's listen to the whole conversation again from start to finish."
OUTRO = "Larisa loved her breakfast, even if Yaroslav's tie drank most of the orange juice. Soon the front-desk telephone brings news about the mystery suitcase. See you next time."
CLOSING = ('larisa', 'Хорошего дня!')
STORY = [
    ('kira', 'Ещё раз доброе утро, Лариса Борисовна! Вы хотите кофе или чёрный чай?', 'Good morning again, Larisa Borisovna! Would you like coffee or black tea?'),
    ('larisa', 'Чёрный чай без сахара, пожалуйста, и один кусочек тёплого хлеба.', 'Black tea without sugar, please, and one slice of warm bread.'),
    ('yaroslav', 'Разрешите я налью вам свежий апельсиновый сок, Лариса Борисовна!', 'Allow me to pour you fresh orange juice, Larisa Borisovna!'),
    ('larisa', 'Ой, как любезно с вашей стороны. Только полстакана.', 'Oh, how kind of you. Just half a glass.'),
    ('yaroslav', 'В нашем доме сервис на пять звёзд — ой!', 'In our house, five-star service comes naturally — oops!'),
    ('kira', 'Осторожно, Ярослав Ильич, у кувшина широкое горлышко!', 'Careful, Yaroslav Ilyich, the pitcher has a wide spout!'),
    ('yaroslav', 'Какой ужас! На столе ни капли, слава богу... но весь сок у меня на галстуке!', 'How awful! Not a drop on the table, thank goodness... yet all the juice is on my tie!'),
    ('larisa', 'Не переживайте! Холодная вода с газом легко смывает апельсиновый сок.', 'Do not fret! Cold sparkling water washes orange juice right out.'),
    ('kira', 'Вот чистая салфетка и холодная вода, Ярослав Ильич.', 'Here is a clean napkin and cold water, Yaroslav Ilyich.'),
    ('yaroslav', 'Простите меня, я удалюсь в кабинет спасать галстук!', 'Forgive me, I shall retreat to my office to save my tie!'),
    ('larisa', 'Омлет сегодня просто восхитительный, Кира. Передайте Зое мою благодарность!', 'The omelette today is simply delicious, Kira. Pass my thanks on to Zoya!'),
    ('kira', 'Обязательно передам! Приятного аппетита.', 'I certainly will! Enjoy your meal.'),
]
WALK = [
    (0, None, ["'Good morning again, Larisa Borisovna! Would you like coffee or black tea?' Asking politely what a guest wants uses ", (None, 'Вы хотите'), ' followed directly by the drinks on offer.']),
    (1, None, ["'Black tea without sugar, please, and one slice of warm bread.' Ordering something plain without extras relies on ", (None, 'без сахара,'), " — 'without sugar'."]),
    (2, None, ["'Allow me to pour you fresh orange juice, Larisa Borisovna!' Notice ", (None, 'апельсиновый сок,'), ' turning the word for an orange into a describing word for juice.']),
    (3, None, ["'Oh, how kind of you. Just half a glass.' Joining 'half' onto 'glass' makes one tidy compound, ", (None, 'полстакана.'), " — 'half a glass'."]),
    (4, None, ["'In our house, five-star service comes naturally — oops!' Hotel ratings count stars just like English: ", (None, 'на пять звёзд'), " means 'at five stars'."]),
    (5, None, ["'Careful, Yaroslav Ilyich, the pitcher has a wide spout!' Warning someone in motion takes one quick word, ", (None, 'Осторожно,'), " — 'careful!'."]),
    (6, None, ["'How awful! Not a drop on the table, thank goodness... yet all the juice is on my tie!' Everyday relief slips out in ", (None, 'слава богу...'), " literally 'glory to God', used just like 'thank goodness'."]),
    (7, None, ["'Do not fret! Cold sparkling water washes orange juice right out.' Fizzy mineral water is simply ", (None, 'вода с газом'), " — 'water with gas'."]),
    (8, None, "'Here is a clean napkin and cold water, Yaroslav Ilyich.' Kira stays cool under pressure, handing over the rescue cloth before the stain can set."),
    (9, None, ["'Forgive me, I shall retreat to my office to save my tie!' Yaroslav picks lofty, theatrical ", (None, 'удалюсь'), " — 'I shall withdraw myself' — trying to keep his dignity intact."]),
    (10, None, ["'The omelette today is simply delicious, Kira. Pass my thanks on to Zoya!' Passing a message or greeting on to someone else uses ", (None, 'Передайте'), " — literally 'hand over'."]),
    (11, None, ["'I certainly will! Enjoy your meal.' Before anyone eats, Russians wish ", (None, 'Приятного аппетита.'), " — 'pleasant appetite', the twin of 'bon appétit'."]),
]
