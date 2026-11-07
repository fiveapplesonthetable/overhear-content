# Authoring module for dvorik-u-mosta-s02e01-scene-02.
ID = 'dvorik-u-mosta-s02e01-scene-02'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 1
SCENE = 2
TITLE = 'Убираем книги  (Move the Books)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'zoya': 'Зоя', 'matvey': 'Матвей'}
INTRO = "In the quiet back hallway behind the kitchen, Kira and Matvey stand before a tall wooden bookcase packed with old travel guides. Zoya hurries out of the café corner wiping flour from her hands. Let's listen in first."
OPENER = "Now let's take the bookcase apart, shelf by shelf."
TRANSITION = "Let's hear the whole conversation again from beginning to end."
OUTRO = "The heavy bookcase is aside and the hidden lock turns cleanly on the first try. Lift, pull, turn, open: those action words will keep coming back. See you next time."
CLOSING = ('zoya', 'Пока!')
STORY = [
    ('zoya', 'Это правда? За стеной моей кухни есть тайная комната?', 'Is it true? There is a secret room behind my kitchen wall?'),
    ('kira', 'Помоги мне положить эти зелёные книги на стул, Зоя.', 'Help me put these green books on the chair, Zoya.'),
    ('matvey', 'Сначала снимаем верхнюю полку, тогда шкаф станет лёгким.', 'First we clear the top shelf, then the bookcase will get light.'),
    ('zoya', 'Эти путеводители старше нас обеих, Кира!', 'These guidebooks are older than both of us, Kira!'),
    ('kira', 'Это последняя полка. Тянем на счёт три, Матвей?', 'This is the last shelf. Do we pull on the count of three, Matvey?'),
    ('matvey', 'Раз, два, три! Двигай левую сторону ко мне!', 'One, two, three! Move the left side towards me!'),
    ('zoya', 'Смотрите за шкафом! Белая краска и замочная скважина!', 'Look behind the bookcase! White paint and a keyhole!'),
    ('kira', 'Настоящая дверь, прямо здесь, в коридоре!', 'A real door, right here in the hallway!'),
    ('matvey', 'Давайте попробуем большой ключ из кедрового ящика.', "Let's try the big key from the cedar box."),
    ('zoya', 'Ну что, Матвей, он поворачивается?', 'Well, Matvey, does it turn?'),
    ('matvey', 'Один поворот направо... и замок открыт!', 'One turn to the right... and the lock is open!'),
    ('kira', 'Сначала подними ручку, как на входной двери!', 'Lift the handle first, just like on the front door!'),
]
WALK = [
    (0, None, ["'Is it true? There is a secret room behind my kitchen wall?' Zoya's first question, ", (None, 'Это правда?'), " is 'this is truth?', the everyday way to ask 'really?'."]),
    (1, None, ["'Help me put these green books on the chair, Zoya.' Between friends Kira uses the casual ", (None, 'Помоги мне'), ", 'help me', a request you can use with anyone you call by first name."]),
    (2, None, ["'First we clear the top shelf, then the bookcase will get light.' The word ", (None, 'лёгким'), " means 'light' as in not heavy, and it also means 'easy'."]),
    (3, None, ["'These guidebooks are older than both of us, Kira!' A guidebook is a 'way-leader': ", (None, 'путеводители'), " joins the old word for path with the word for leading."]),
    (4, None, ["'This is the last shelf. Do we pull on the count of three, Matvey?' Movers and friends say ", (None, 'на счёт три'), ", 'on the count of three', before any heavy lift."]),
    (5, None, ["'One, two, three! Move the left side towards me!' Notice how Russians count out loud: they say ", (None, 'Раз,'), " instead of the normal word for one when counting off."]),
    (6, None, ["'Look behind the bookcase! White paint and a keyhole!' A keyhole is a 'lock well': ", (None, 'замочная скважина!'), " pairs the word for lock with an old word for a narrow hole."]),
    (7, None, ["'A real door, right here in the hallway!' Kira adds ", (None, 'прямо'), " to 'here', and the place becomes 'right here', exactly this spot."]),
    (8, None, ["'Let's try the big key from the cedar box.' Matvey invites the group with ", (None, 'Давайте попробуем'), ", 'let's try', a polite way to suggest doing something together."]),
    (9, None, ["'Well, Matvey, does it turn?' The little opener ", (None, 'Ну что,'), " is 'well, so?', and it makes the question sound excited and impatient."]),
    (10, None, ["'One turn to the right... and the lock is open!' Directions are easy: ", (None, 'направо'), " is 'to the right', and its partner for left is very similar."]),
    (11, None, ["'Lift the handle first, just like on the front door!' The front door is the 'entrance door': ", (None, 'входной двери!'), " comes from the word for going in."]),
]
