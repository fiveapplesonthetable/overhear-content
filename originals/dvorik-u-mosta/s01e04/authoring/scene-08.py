# Authoring module for dvorik-u-mosta-s01e04-scene-08.
ID = 'dvorik-u-mosta-s01e04-scene-08'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = 'Мальчик на ступеньке  (The Boy on the Stairs)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'larisa': 'Лариса', 'kira': 'Кира', 'roman': 'Роман'}
INTRO = 'Stepping out into the sunlit courtyard, Larisa Borisovna tells Kira more about the two brothers from Lipovy Lane, unaware that Roman has just walked down the stairs behind them. Listen first.'
OPENER = "Now let's savour that courtyard reunion line by line."
TRANSITION = "Let's hear the whole scene again from beginning to end."
OUTRO = 'Little Roman from the third stair is standing right in front of his childhood piano teacher — and he is the mystery suitcase owner. Episode 4 is complete; see you in Episode 5.'
CLOSING = ('roman', 'До встречи!')
STORY = [
    ('kira', 'Расскажите ещё про тех двух мальчиков с Липового переулка, Лариса Борисовна!', 'Tell me more about those two boys from Lipovy Lane, Larisa Borisovna!'),
    ('larisa', 'Старший брат был смелым и шумным, вечно спешил на музыкальных гаммах.', 'The older brother was bold and noisy, forever rushing on his musical scales.'),
    ('kira', 'А младший брат с деревянным поездом?', 'And the younger brother with the wooden train?'),
    ('larisa', 'Тихий как мышка! Он сидел на третьей ступеньке и слушал каждую ноту.', 'Quiet as a little mouse! He sat on the third step and listened to every single note.'),
    ('kira', 'Слушал, как звучит комната... подождите секунду!', 'Listened to how the room sounds... wait a second!'),
    ('larisa', 'После урока он всегда спрашивал, почему в дождь пианино звучит теплее.', 'After the lesson he always asked why the piano sounds warmer in the rain.'),
    ('roman', 'Потому что мокрые деревянные ставни смягчают эхо от каменной мостовой...', 'Because wet wooden shutters soften the echo off the stone pavement...'),
    ('kira', 'Роман! Вы стояли прямо за нами?!', 'Roman! Were you standing right behind us?!'),
    ('larisa', 'Боже мой... посмотрите на эти глаза! Маленький Рома с третьей ступеньки?!', 'Good heavens... look at those eyes! Little Roma from the third step?!'),
    ('roman', 'Лариса Борисовна?! Учительница музыки моего брата по пятницам?!', "Larisa Borisovna?! My brother's Friday music teacher?!"),
    ('kira', 'Стойте — значит, в понедельник вечером на крыльце... второй синий чемодан...', 'Hold on — then on Monday night on the porch... the second blue suitcase...'),
    ('roman', 'Да, Кира. Тот синий чемодан — мой, и я расскажу вам всю правду.', 'Yes, Kira. That blue suitcase is mine, and I will tell you the whole truth.'),
]
WALK = [
    (0, None, ["'Tell me more about those two boys from Lipovy Lane, Larisa Borisovna!' Asking for more of a story uses ", (None, 'Расскажите ещё'), " — 'tell more!'."]),
    (1, None, ["'The older brother was bold and noisy, forever rushing on his musical scales.' Notice ", (None, 'Старший брат'), " for 'older brother', paired right below with 'younger brother'."]),
    (2, None, ["'And the younger brother with the wooden train?' Here comes the matching half of the family pair: ", (None, 'младший брат'), " — 'younger brother'."]),
    (3, None, ["'Quiet as a little mouse! He sat on the third step and listened to every single note.' Affectionate ", (None, 'как мышка!'), " calls him 'like a little mouse', gentle rather than timid."]),
    (4, None, ["'Listened to how the room sounds... wait a second!' Kira connects the boy on the stairs to the grown acoustic architect through ", (None, 'как звучит комната...'), " — 'how the room sounds'."]),
    (5, None, ["'After the lesson he always asked why the piano sounds warmer in the rain.' Warmer in tone is ", (None, 'теплее.'), " — 'warmer', serving both temperature and musical sound."]),
    (6, None, ["'Because wet wooden shutters soften the echo off the stone pavement...' Built from 'soft', ", (None, 'смягчают'), " means 'soften', spoken from memory twenty-five years later."]),
    (7, None, ["'Roman! Were you standing right behind us?!' Right behind someone's back is ", (None, 'прямо за нами?!'), " — 'right behind us'."]),
    (8, None, ["'Good heavens... look at those eyes! Little Roma from the third step?!' Russian family nicknames shorten Roman into warm ", (None, 'Рома'), ' — the childhood name his teacher remembers.']),
    (9, None, ["'Larisa Borisovna?! My brother's Friday music teacher?!' Notice feminine ", (None, 'Учительница'), ' naming a female teacher specifically.']),
    (10, None, "'Hold on — then on Monday night on the porch... the second blue suitcase...' Every clue from the entire week snaps into focus at once."),
    (11, None, ["'Yes, Kira. That blue suitcase is mine, and I will tell you the whole truth.' Promising no more secrets uses ", (None, 'всю правду.'), " — 'the whole truth'."]),
]
