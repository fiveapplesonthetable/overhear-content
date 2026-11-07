# Authoring module for dvorik-u-mosta-s02e01-scene-04.
ID = 'dvorik-u-mosta-s02e01-scene-04'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 1
SCENE = 4
TITLE = 'Под белой тканью  (Under the White Sheet)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'larisa': 'Лариса', 'matvey': 'Матвей'}
INTRO = "Hearing excited voices down the hall, Room 4 guest Larisa walks over with her morning teacup just as Kira and Matvey reach the tall shape under the white cloth. Listen first."
OPENER = "Now let's lift that white sheet together, one line at a time."
TRANSITION = "Let's listen to the whole conversation again from start to finish."
OUTRO = "Beneath the dust sheet stands a warm walnut piano with every key working except one silent note in the middle. See you in the next scene."
CLOSING = ('larisa', 'Всего доброго!')
STORY = [
    ('larisa', 'Доброе утро! Почему все стоят внутри стены?', 'Good morning! Why is everyone standing inside the wall?'),
    ('kira', 'Идите сюда, Лариса Борисовна! Мы нашли девятый номер!', 'Come here, Larisa Borisovna! We found room nine!'),
    ('larisa', 'Боже мой, какие окна! Можно войти?', 'My goodness, what windows! May I come in?'),
    ('matvey', 'Осторожно, тут пыльный порог. Помогите мне сложить эту ткань.', 'Careful, the threshold is dusty here. Help me fold this cloth.'),
    ('kira', 'Раз, два... ой! Смотрите, какое тёмное блестящее дерево!', 'One, two... oh! Look at this dark, shiny wood!'),
    ('larisa', 'Пианино! Настоящее старое пианино из ореха!', 'A piano! A real old walnut piano!'),
    ('matvey', 'Осторожно с крышкой. Её не открывали много лет.', 'Careful with the lid. Nobody has opened it for many years.'),
    ('larisa', 'Посмотрите на клавиши, Кира. Они чистые и целые.', 'Look at the keys, Kira. They are clean and whole.'),
    ('kira', 'Сыграйте что-нибудь, Лариса Борисовна! Для всего дома!', 'Play something, Larisa Borisovna! For the whole house!'),
    ('larisa', 'Слушайте... низко, тепло... Подождите, эта клавиша в середине молчит!', 'Listen... low, warm... Wait, this key in the middle is silent!'),
    ('matvey', 'Все клавиши поют, а одна в середине молчит?', 'All the keys sing, but one in the middle is silent?'),
    ('larisa', 'Один хороший ремонт, Матвей, и пианино вспомнит все песни.', 'One good repair, Matvey, and the piano will remember every song.'),
]
WALK = [
    (0, None, ["'Good morning! Why is everyone standing inside the wall?' One small word covers 'everyone': ", (None, 'все'), " takes a plural verb, so it is really 'all are standing'."]),
    (1, None, ["'Come here, Larisa Borisovna! We found room nine!' Kira invites an older guest with the polite ", (None, 'Идите сюда,'), " 'come here', plus her first name and her father's name."]),
    (2, None, ["'My goodness, what windows! May I come in?' Asking permission takes one word in Russian: ", (None, 'Можно войти?'), " is 'possible to come in?', and you can swap in any action."]),
    (3, None, ["'Careful, the threshold is dusty here. Help me fold this cloth.' Dust becomes a describing word: ", (None, 'пыльный'), " is 'dusty', made from the plain word for dust with one extra ending."]),
    (4, None, ["'One, two... oh! Look at this dark, shiny wood!' To admire something, Kira uses ", (None, 'какое'), ", 'what a', and the ending matches the word for wood."]),
    (5, None, ["'A piano! A real old walnut piano!' The word ", (None, 'Пианино!'), " came from Italian and never changes, whatever the sentence does."]),
    (6, None, ["'Careful with the lid. Nobody has opened it for many years.' Matvey needs no 'nobody' here: ", (None, 'не открывали'), " is 'they did not open', with no 'they' said at all."]),
    (7, None, ["'Look at the keys, Kira. They are clean and whole.' Piano keys have their own name: ", (None, 'клавиши.'), " A door key is a different word, the one Matvey carries on his ring."]),
    (8, None, ["'Play something, Larisa Borisovna! For the whole house!' The vague ", (None, 'что-нибудь,'), " means 'anything at all', so Kira isn't asking for one particular song."]),
    (9, None, ["'Listen... low, warm... Wait, this key in the middle is silent!' Russian has one verb for 'be silent': ", (None, 'молчит!'), " so the key 'keeps quiet' like a stubborn person."]),
    (10, None, ["'All the keys sing, but one in the middle is silent?' Matvey turns the keys into singers with ", (None, 'поют,'), " from the same verb you use for people singing songs."]),
    (11, None, ["'One good repair, Matvey, and the piano will remember every song.' The word ", (None, 'ремонт,'), " is any repair, from fixing a piano to redoing a whole flat."]),
]
