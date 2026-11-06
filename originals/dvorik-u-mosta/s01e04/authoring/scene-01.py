# Authoring module for dvorik-u-mosta-s01e04-scene-01.
ID = 'dvorik-u-mosta-s01e04-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Без четверти семь  (Six Forty-Five)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'matvey': 'Матвей', 'kira': 'Кира'}
INTRO = 'It is six forty-five in the morning at the Bridge Courtyard Inn in St Petersburg. While the guests still sleep upstairs, Matvey sketches a street map on paper for Kira. Listen to the Russian scene first.'
OPENER = "Let's walk through Matvey's dawn directions one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Left at the gate, across the bridge, past the green pharmacy, and left into the square — Kira is off on her dawn mission. See you next time.'
CLOSING = ('kira', 'Удачи!')
STORY = [
    ('kira', 'Доброе утро, Матвей! Вода наверху правда уже совсем холодная?', 'Good morning, Matvey! Is the water upstairs really completely cold already?'),
    ('matvey', 'Холодная как в реке. Положи этот старый вентиль в карман пальто.', 'Cold as in a river. Put this old valve in your coat pocket.'),
    ('kira', 'Положила. А теперь скажи, как мне найти эту лавку.', 'Put it in. And now tell me how I find that shop.'),
    ('matvey', 'Выйди за ворота, поверни налево и иди прямо до каменного моста.', 'Step outside the gate, turn left, and walk straight to the stone bridge.'),
    ('kira', 'У ворот налево, прямо до моста. Мне переходить через реку?', 'Left at the gate, straight to the bridge. Should I cross the river?'),
    ('matvey', 'Да, перейди через мост и пройди мимо зелёной аптеки справа.', 'Yes, cross the bridge and walk past the green pharmacy on the right.'),
    ('kira', 'Мост, потом зелёная аптека справа. А дальше куда?', 'Bridge, then the green pharmacy on the right. And where next?'),
    ('matvey', 'Поверни налево на маленькую площадь. Ищи синюю деревянную дверь.', 'Turn left onto the small square. Look for a blue wooden door.'),
    ('kira', 'Снаружи есть большая вывеска?', 'Is there a big sign outside?'),
    ('matvey', 'Только золотой ключ над дверью. Покажи мастеру этот старый вентиль.', 'Only a golden key above the door. Show the craftsman this old valve.'),
    ('kira', 'Двадцать миллиметров, латунь, вентиль для котла — буду повторять всю дорогу!', 'Twenty millimetres, brass, boiler valve — I will repeat it the whole way!'),
    ('matvey', 'Беги быстро, Кира. Четвёртый номер встаёт в семь пятнадцать!', 'Run fast, Kira. Room four gets up at seven fifteen!'),
]
WALK = [
    (0, None, ["'Good morning, Matvey! Is the water upstairs really completely cold already?' Adding ", (None, 'совсем'), " before 'cold' means 'completely, thoroughly'."]),
    (1, None, ["'Cold as in a river. Put this old valve in your coat pocket.' Notice ", (None, 'как в реке.'), " — a crisp Petersburg comparison, 'as in the river'."]),
    (2, None, ["'Put it in. And now tell me how I find that shop.' One single past word, ", (None, 'Положила.'), " confirms 'I put it in', carrying Kira's feminine ending."]),
    (3, None, ["'Step outside the gate, turn left, and walk straight to the stone bridge.' Every street direction uses this trio: ", (None, 'поверни налево'), " for 'turn left' and ", (None, 'иди прямо'), " for 'walk straight'."]),
    (4, None, ["'Left at the gate, straight to the bridge. Should I cross the river?' Putting 'to me' with an action word in ", (None, 'Мне переходить'), " asks 'am I supposed to cross?'."]),
    (5, None, ["'Yes, cross the bridge and walk past the green pharmacy on the right.' Walking right past a landmark uses ", (None, 'пройди мимо'), " — 'pass by'."]),
    (6, None, ["'Bridge, then the green pharmacy on the right. And where next?' Three brisk words, ", (None, 'А дальше куда?'), " ask 'and further, where to?'."]),
    (7, None, ["'Turn left onto the small square. Look for a blue wooden door.' Open city squares take 'onto', so ", (None, 'на маленькую площадь.'), ' leads her out into the square.']),
    (8, None, ["'Is there a big sign outside?' A shop sign above a doorway is ", (None, 'вывеска?'), ' — built from the action of hanging something out to view.']),
    (9, None, ["'Only a golden key above the door. Show the craftsman this old valve.' Hanging directly overhead is ", (None, 'над дверью.'), " — 'above the door'."]),
    (10, None, ["'Twenty millimetres, brass, boiler valve — I will repeat it the whole way!' For 'all the way there', say ", (None, 'всю дорогу!'), " — literally 'the whole road'."]),
    (11, None, ["'Run fast, Kira. Room four gets up at seven fifteen!' Waking and getting out of bed is ", (None, 'встаёт'), " — 'gets up'."]),
]
