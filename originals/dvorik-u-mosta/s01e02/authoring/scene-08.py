# Authoring module for dvorik-u-mosta-s01e02-scene-08.
ID = 'dvorik-u-mosta-s01e02-scene-08'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Два гостя на один номер  (Two Names, One Room)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'yaroslav': 'Ярослав', 'kira': 'Кира', 'matvey': 'Матвей'}
INTRO = "On Wednesday evening, as dusk settles over St Petersburg, Yaroslav steps out of his office pale-faced, holding both the tablet and Matvey's paper ledger. Listen to the Russian first."
OPENER = "Now let's examine how the double-booking happened, line by line."
TRANSITION = "Let's hear the whole scene again from beginning to end."
OUTRO = "Two guests booked into Room 7, pouring rain outside, and only forty minutes before the eight o'clock arrival. Episode 2 is done — join us in Episode 3 to see if the attic can save the night."
CLOSING = ('yaroslav', 'До завтра!')
STORY = [
    ('yaroslav', 'Матвей... Кира... скажите мне, что шестой номер сегодня свободен.', 'Matvey... Kira... tell me that room six is free tonight.'),
    ('kira', 'Нет, Ярослав Ильич, час назад в шестой номер заселилась пара с юга.', 'No, Yaroslav Ilyich, an hour ago a couple from the south checked into room six.'),
    ('matvey', 'Все ключи с первого по седьмой заняты, а в восьмом номере свежая краска.', 'Every key from one to seven is taken, and room eight has wet paint.'),
    ('yaroslav', 'За что мне эта катастрофа?! Вчера я принял бронь на планшете без очков!', 'What did I do to deserve this disaster?! Yesterday I took a booking on the tablet without my glasses!'),
    ('kira', 'Подождите — давайте сверим экран планшета и бумажную книгу.', 'Wait — let us compare the tablet screen and the paper book.'),
    ('matvey', 'Дай угадаю. Вы пообещали гостю комнату, которой у нас нет?', 'Let me guess. Did you promise a guest a room we do not have?'),
    ('kira', 'Ярослав Ильич! Седьмой номер уже занят, и вы записали туда второго гостя!', 'Yaroslav Ilyich! Room seven is already occupied, and you wrote a second guest in there!'),
    ('yaroslav', 'И он приезжает вечерним поездом в восемь часов — через сорок минут!', "And he arrives on the eight o'clock evening train — in forty minutes!"),
    ('matvey', 'Говорил же я вам, что этот планшет — ловушка.', 'I told you that tablet is a trap.'),
    ('yaroslav', 'На улице идёт дождь, и все отели рядом полные! Что нам делать?', 'It is raining outside, and every hotel nearby is full! What are we to do?'),
    ('kira', 'Стойте — а что находится на третьем этаже над лестницей?', 'Hold on — what is up on the third floor above the stairs?'),
    ('matvey', 'Старая светлая мансарда... быстро за мной!', 'The old bright attic room... follow me, quickly!'),
]
WALK = [
    (0, None, ["'Matvey... Kira... tell me that room six is free tonight.' For an available hotel room or empty seat, Russian uses ", (None, 'свободен.'), " — 'free, unoccupied'."]),
    (1, None, ["'No, Yaroslav Ilyich, an hour ago a couple from the south checked into room six.' Notice ", (None, 'час назад'), " — simply 'an hour back' for 'an hour ago'."]),
    (2, None, ["'Every key from one to seven is taken, and room eight has wet paint.' Opposite of free is ", (None, 'заняты,'), " meaning 'taken' or 'occupied'."]),
    (3, None, ["'What did I do to deserve this disaster?! Yesterday I took a booking on the tablet without my glasses!' Dramatic ", (None, 'За что'), " asks 'what did I do to deserve this?' rather than a plain cause."]),
    (4, None, ["'Wait — let us compare the tablet screen and the paper book.' Checking two records side by side uses ", (None, 'сверим'), ' — built from the root for truth and trust.']),
    (5, None, ["'Let me guess. Did you promise a guest a room we do not have?' Casual ", (None, 'Дай угадаю.'), " literally says 'give that I guess' — 'let me guess'."]),
    (6, None, ["'Yaroslav Ilyich! Room seven is already occupied, and you wrote a second guest in there!' Here singular ", (None, 'уже занят,'), " matches masculine 'number' for room seven."]),
    (7, None, ["'And he arrives on the eight o'clock evening train — in forty minutes!' Future countdowns use 'through': ", (None, 'через сорок минут!'), " means 'in forty minutes'."]),
    (8, None, ["'I told you that tablet is a trap.' Putting the action first with ", (None, 'Говорил же я вам,'), " delivers a classic 'didn't I tell you so!'."]),
    (9, None, ["'It is raining outside, and every hotel nearby is full! What are we to do?' Rain 'walks' in Russian: ", (None, 'идёт дождь,'), " literally says 'rain is walking', while ", (None, 'Что нам делать?'), " asks 'what are we to do?'."]),
    (10, None, ["'Hold on — what is up on the third floor above the stairs?' Asking where a room sits uses ", (None, 'находится'), " — literally 'finds itself'."]),
    (11, None, ["'The old bright attic room... follow me, quickly!' No action word is needed in ", (None, 'быстро за мной!'), " — literally 'quickly behind me!' means 'follow me fast!'."]),
]
