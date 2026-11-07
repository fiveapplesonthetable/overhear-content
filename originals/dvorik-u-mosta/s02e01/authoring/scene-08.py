# Authoring module for dvorik-u-mosta-s02e01-scene-08.
ID = 'dvorik-u-mosta-s02e01-scene-08'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 1
SCENE = 8
TITLE = 'Не трогайте выключатель  (Don\'t Touch That Switch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'matvey': 'Матвей', 'yaroslav': 'Ярослав', 'kira': 'Кира'}
INTRO = "Back at the threshold of Room 9, Matvey opens his leather tool bag to inspect the old brass wall switch, but an excited Yaroslav reaches past him beside Kira. Listen first."
OPENER = "Let's replay that loud pop one line at a time."
TRANSITION = "Now listen to the whole scene again from start to finish."
OUTRO = "One impatient click from Yaroslav pops the ground-floor fuse and proves Room 9 needs fresh wiring before Friday! Episode 1 of Season 2 is complete. See you in Episode 2."
CLOSING = ('matvey', 'Удачи!')
STORY = [
    ('matvey', 'Минуту, шеф. Не трогайте пока этот латунный выключатель.', "One minute, boss. Don't touch that brass switch yet."),
    ('yaroslav', 'Зачем ждать? Я помню эту стеклянную лампу. Смотрите, как она светит!', 'Why wait? I remember this glass lamp. Watch how it shines!'),
    ('kira', 'Ярослав Ильич, подождите! У Матвея в руке отвёртка!', 'Yaroslav Ilyich, wait! Matvey has a screwdriver in his hand!'),
    ('yaroslav', 'Только один щелчок... Ой! Ой-ой-ой.', 'Just one click... Oh! Oh dear.'),
    ('kira', 'Что это был за хлопок в коридоре?', 'What was that bang in the hallway?'),
    ('matvey', 'Это старый провод. Он выбил пробки на первом этаже.', 'That was the old wire. It blew the fuses on the ground floor.'),
    ('yaroslav', 'В холле погасла лампа! Я сломал и духовку на кухне?', 'The lamp in the lobby went out! Did I break the oven in the kitchen too?'),
    ('kira', 'Ой, я слышу, как Зоя зовёт нас из тёмной кухни!', 'Oh, I can hear Zoya calling us from the dark kitchen!'),
    ('matvey', 'Проводу тридцать лет, шеф. Никогда не включайте свет, пока я не посмотрю.', 'The wire is thirty years old, boss. Never turn on the light until I have looked.'),
    ('yaroslav', 'Ты можешь починить это до обеда, Матвей? Скажи, что у тебя есть пробки!', 'Can you fix it before lunch, Matvey? Tell me you have fuses!'),
    ('matvey', 'Кухню я включу за две минуты. А девятому номеру нужен новый медный провод.', 'I will get the kitchen back on in two minutes. But room nine needs new copper wire.'),
    ('kira', 'Держите фонарик, Ярослав Ильич. До пятницы осталось шесть дней!', 'Hold the torch, Yaroslav Ilyich. Six days are left until Friday!'),
]
WALK = [
    (0, None, ["'One minute, boss. Don't touch that brass switch yet.' The little word ", (None, 'пока'), " here means 'for now' or 'yet', not 'bye', which is the same word in a different job."]),
    (1, None, ["'Why wait? I remember this glass lamp. Watch how it shines!' To ask 'what for?', Yaroslav says ", (None, 'Зачем'), ", a question about purpose rather than cause."]),
    (2, None, ["'Yaroslav Ilyich, wait! Matvey has a screwdriver in his hand!' A screwdriver is a 'turner-out': ", (None, 'отвёртка!'), " comes from the verb for turning or unscrewing."]),
    (3, None, ["'Just one click... Oh! Oh dear.' Russians stretch the little cry ", (None, 'Ой-ой-ой.'), " into three, and it means 'oh dear, that went wrong'."]),
    (4, None, ["'What was that bang in the hallway?' Kira asks with ", (None, 'Что это был за'), ", 'what kind of... was that', a question you can finish with any noise or thing."]),
    (5, None, ["'That was the old wire. It blew the fuses on the ground floor.' In Russian homes fuses are called 'plugs': ", (None, 'выбил пробки'), " is literally 'knocked out the plugs'."]),
    (6, None, ["'The lamp in the lobby went out! Did I break the oven in the kitchen too?' A light that goes out uses the same verb as a candle: ", (None, 'погасла'), ", 'went out'."]),
    (7, None, ["'Oh, I can hear Zoya calling us from the dark kitchen!' The word ", (None, 'зовёт'), " means 'calls', both calling someone over and calling someone a name."]),
    (8, None, ["'The wire is thirty years old, boss. Never turn on the light until I have looked.' Age goes to the person or thing: ", (None, 'Проводу тридцать лет,'), " is literally 'to the wire, thirty years'."]),
    (9, None, ["'Can you fix it before lunch, Matvey? Tell me you have fuses!' Yaroslav uses the casual 'you' with his handyman: ", (None, 'Ты можешь'), ", 'can you', and then the casual 'tell me'."]),
    (10, None, ["'I will get the kitchen back on in two minutes. But room nine needs new copper wire.' Need works backwards: ", (None, 'девятому номеру нужен'), " is 'to room nine is needed'."]),
    (11, None, ["'Hold the torch, Yaroslav Ilyich. Six days are left until Friday!' The countdown chunk ", (None, 'До пятницы осталось'), " is 'until Friday there remain', and you can swap in any deadline."]),
]
