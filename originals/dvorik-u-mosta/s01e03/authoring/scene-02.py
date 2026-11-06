# Authoring module for dvorik-u-mosta-s01e03-scene-02.
ID = 'dvorik-u-mosta-s01e03-scene-02'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'Уютная мансарда  (The Sunny Attic)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'matvey': 'Матвей', 'kira': 'Кира', 'zoya': 'Зоя'}
INTRO = 'Up under the wooden eaves on the third floor, Matvey unlocks the attic room for Kira while Zoya climbs up carrying fresh towels. Listen to the Russian scene first.'
OPENER = "Now let's walk through their attic inspection line by line."
TRANSITION = "Let's hear the whole scene again from start to finish."
OUTRO = 'With wooden beams and rain on the roof, the attic only needs a lamp, two pillows, and a rug. See you next time as they race the clock.'
CLOSING = ('zoya', 'Пока!')
STORY = [
    ('kira', 'Ой, посмотрите на эту комнату! Большие деревянные балки и окно во двор!', 'Oh, look at this room! Big wooden beams and a window onto the courtyard!'),
    ('zoya', 'Послушайте дождь по крыше — здесь наверху так уютно!', 'Listen to the rain on the roof — it is so cosy up here!'),
    ('matvey', 'Сухо, тепло и тихо. А теперь скажите, чего тут не хватает.', 'Dry, warm, and quiet. Now tell me what is missing here.'),
    ('kira', 'Так: есть кровать, стол и стул, но нам нужна настольная лампа.', 'Okay: there is a bed, a table, and a chair, yet we need a desk lamp.'),
    ('zoya', 'И нет зеркала на стене, а пол кажется пустым без коврика.', 'And there is no mirror on the wall, while the floor looks bare without a rug.'),
    ('matvey', 'В моей мастерской внизу стоит латунная лампа для чтения.', 'Downstairs in my workshop stands a brass reading lamp.'),
    ('zoya', 'А у меня в кладовке есть две мягкие подушки и синий коврик!', 'And in the store room I have two soft pillows and a blue rug!'),
    ('kira', 'А маленькая ванная рядом? Там работает свет?', 'What about the small bathroom next door? Does the light work in there?'),
    ('matvey', 'Новая лампочка с прошлой недели, чистое мыло и много горячей воды.', 'A new lightbulb since last week, clean soap, and plenty of hot water.'),
    ('zoya', 'Дайте нам пятнадцать минут, и эта мансарда будет лучше седьмого номера!', 'Give us fifteen minutes, and this attic will be better than room seven!'),
    ('kira', 'Бери картонные коробки, Матвей — несём их вниз по лестнице!', "Grab the cardboard boxes, Matvey — let's carry them down the stairs!"),
    ('matvey', 'Осторожно на повороте, не задень стену!', 'Careful on the turn, do not graze the wall!'),
]
WALK = [
    (0, None, ["'Oh, look at this room! Big wooden beams and a window onto the courtyard!' Overhead ceiling timbers are ", (None, 'деревянные балки'), ' — giving the top floor its warm character.']),
    (1, None, ["'Listen to the rain on the roof — it is so cosy up here!' Few Russian words are warmer than ", (None, 'уютно!'), ' describing a snug, inviting space on a rainy evening.']),
    (2, None, ["'Dry, warm, and quiet. Now tell me what is missing here.' Asking what a room lacks uses ", (None, 'не хватает.'), " — literally 'does not suffice'."]),
    (3, None, ["'Okay: there is a bed, a table, and a chair, yet we need a desk lamp.' Built from 'on the table', ", (None, 'настольная лампа.'), ' names a table or bedside lamp.']),
    (4, None, ["'And there is no mirror on the wall, while the floor looks bare without a rug.' Absence flips 'mirror' into ", (None, 'нет зеркала'), " — 'there is no mirror'."]),
    (5, None, ["'Downstairs in my workshop stands a brass reading lamp.' Lamps, plates, and upright items 'stand' in Russian: ", (None, 'стоит'), " sounds much more natural than plain 'is'."]),
    (6, None, ["'And in the store room I have two soft pillows and a blue rug!' Turning 'carpet' into affectionate ", (None, 'коврик!'), ' gives you a small bedside rug.']),
    (7, None, "'What about the small bathroom next door? Does the light work in there?' Kira checks the practical details guests always test first."),
    (8, None, ["'A new lightbulb since last week, clean soap, and plenty of hot water.' Compare 'lamp' with little ", (None, 'лампочка'), ' — adding the small ending turns a whole lamp into a lightbulb!']),
    (9, None, ["'Give us fifteen minutes, and this attic will be better than room seven!' Comparing two rooms needs no word for 'than': ", (None, 'лучше седьмого номера!'), " says 'better of the seventh room'."]),
    (10, None, ["'Grab the cardboard boxes, Matvey — let's carry them down the stairs!' Casual ", (None, 'Бери'), " tells Matvey 'grab, take', matching their brisk teamwork."]),
    (11, None, ["'Careful on the turn, do not graze the wall!' Staircase corners call for ", (None, 'на повороте,'), " — 'on the turn, at the bend'."]),
]
