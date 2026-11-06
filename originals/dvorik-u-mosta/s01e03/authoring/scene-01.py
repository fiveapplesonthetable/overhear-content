# Authoring module for dvorik-u-mosta-s01e03-scene-01.
ID = 'dvorik-u-mosta-s01e03-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'Тридцать пять минут  (Thirty-Five Minutes)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'yaroslav': 'Ярослав', 'kira': 'Кира', 'matvey': 'Матвей'}
INTRO = 'Rain taps against the lobby windows of the Bridge Courtyard Inn in St Petersburg. With a second Room 7 guest arriving in thirty-five minutes, Yaroslav, Kira, and Matvey hurry toward the stairs. Listen first.'
OPENER = "Let's go back through their race against the clock line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Thirty-five minutes on the clock and four boxes in the way — let's climb up to the third-floor attic next time."
CLOSING = ('kira', 'До скорого!')
STORY = [
    ('yaroslav', 'Тридцать пять минут! Он напишет ужасный отзыв с одной звездой!', 'Thirty-five minutes! He will write a terrible review with one star!'),
    ('kira', 'Сделайте глубокий вдох, Ярослав Ильич. Пока никто ничего не написал.', 'Take a deep breath, Yaroslav Ilyich. Nobody has written anything yet.'),
    ('matvey', 'Вот маленький серебряный ключ от двери на третьем этаже.', 'Here is the small silver key to the door on the third floor.'),
    ('yaroslav', 'А в мансарде вообще есть нормальная кровать?', 'Does the attic even have a proper bed?'),
    ('matvey', 'Да, хорошая деревянная кровать, чистый стол и лучшее окно в доме.', 'Yes, a good wooden bed, a clean desk, and the best window in the house.'),
    ('kira', 'Тогда почему мы никогда не сдаём её гостям?', 'Then why do we never rent it to guests?'),
    ('matvey', 'Потому что лестница узкая, а Ярослав Ильич хранит там коробки с лампами.', 'Because the stairs are narrow, and Yaroslav Ilyich keeps lamp boxes there.'),
    ('yaroslav', 'Всего три маленькие коробки! Ну, может, четыре!', 'Only three small boxes! Well, maybe four!'),
    ('kira', 'Мы можем убрать четыре коробки за пять минут. Пойдёмте смотреть прямо сейчас!', 'We can move four boxes in five minutes. Let us go look right now!'),
    ('matvey', 'Вверх по лестнице, на площадке налево, последняя дверь наверху.', 'Up the stairs, left at the landing, the last door at the top.'),
    ('yaroslav', 'А я принесу чистые белые простыни из шкафа!', 'And I will bring clean white sheets from the cupboard!'),
    ('kira', 'Вперёд — кто быстрее на третий этаж!', 'Onward — race you to the third floor!'),
]
WALK = [
    (0, None, ["'Thirty-five minutes! He will write a terrible review with one star!' Online guest feedback is ", (None, 'отзыв'), " — built from 'calling back', how a guest answers after a stay."]),
    (1, None, ["'Take a deep breath, Yaroslav Ilyich. Nobody has written anything yet.' Notice three negative pieces working as a team in ", (None, 'никто ничего не написал.'), " — 'nobody nothing not wrote'."]),
    (2, None, ["'Here is the small silver key to the door on the third floor.' Keys in Russian belong 'from' a lock rather than 'to' it: ", (None, 'ключ от двери'), " literally says 'key from the door'."]),
    (3, None, ["'Does the attic even have a proper bed?' Slipping ", (None, 'вообще'), " into a worried question adds 'at all' or 'even'."]),
    (4, None, ["'Yes, a good wooden bed, a clean desk, and the best window in the house.' Watch the three describing endings change with each item: feminine ", (None, 'деревянная кровать,'), ' masculine desk, and neuter window.']),
    (5, None, ["'Then why do we never rent it to guests?' Renting out a room or flat uses ", (None, 'сдаём'), " — literally 'hand over' for a stay."]),
    (6, None, ["'Because the stairs are narrow, and Yaroslav Ilyich keeps lamp boxes there.' Keeping belongings stored long-term uses ", (None, 'хранит'), " — 'keeps safely'."]),
    (7, None, ["'Only three small boxes! Well, maybe four!' Opening with ", (None, 'Всего'), " means 'only, merely' when minimizing a count."]),
    (8, None, ["'We can move four boxes in five minutes. Let us go look right now!' Notice ", (None, 'Мы можем убрать'), " pairing 'we can' directly with 'clear away'."]),
    (9, None, ["'Up the stairs, left at the landing, the last door at the top.' Quick direction words need no action word at all: ", (None, 'налево,'), " points 'to the left'."]),
    (10, None, ["'And I will bring clean white sheets from the cupboard!' Carrying something here by hand uses ", (None, 'принесу'), " — 'I will bring'."]),
    (11, None, ["'Onward — race you to the third floor!' Instead of 'race you', Russian challenges a friend with ", (None, 'кто быстрее'), " — literally 'who is faster!'."]),
]
