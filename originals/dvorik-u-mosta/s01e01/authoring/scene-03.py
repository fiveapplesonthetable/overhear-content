# Authoring module for dvorik-u-mosta-s01e01-scene-03.
ID = 'dvorik-u-mosta-s01e01-scene-03'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Где мои очки?  (Where Are My Glasses?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'yaroslav': 'Ярослав', 'kira': 'Кира', 'matvey': 'Матвей'}
INTRO = 'Before the first guest arrives, anxious owner Yaroslav hurries in from the courtyard patting his coat pockets. Kira and Matvey watch as he searches everywhere for his reading glasses. Listen to the Russian first.'
OPENER = "Now let's unpack the scene line by line."
TRANSITION = "Let's listen to the whole conversation once more from start to finish."
OUTRO = 'Yaroslav found his glasses on his own forehead just as the taxi pulled up outside. Relax and let the rhythm of the words sink in; see you next time.'
CLOSING = ('yaroslav', 'До свидания!')
STORY = [
    ('yaroslav', 'Доброе утро всем! Добро пожаловать, Кира. Всё готово?', 'Good morning, everyone! Welcome, Kira. Is everything ready?'),
    ('kira', 'Доброе утро, Ярослав Ильич! Да, стойка чистая, и ключи готовы.', 'Good morning, Yaroslav Ilyich! Yes, the desk is clean, and the keys are ready.'),
    ('yaroslav', 'Гостья из четвёртого номера живёт у нас всю неделю. Всё должно быть идеально!', 'The guest in room four is staying with us all week. Everything must be perfect!'),
    ('matvey', 'Успокойтесь, Ярослав Ильич. Комната чистая, а полотенца свежие.', 'Calm down, Yaroslav Ilyich. The room is clean, and the towels are fresh.'),
    ('yaroslav', 'Мне нужно прочитать книгу бронирований, но я не могу найти очки!', 'I need to read the reservation book, but I cannot find my glasses!'),
    ('kira', 'Может, они в кармане пальто?', 'Maybe they are in your coat pocket?'),
    ('yaroslav', 'Нет, тут только ручка и три старых чека!', 'No, only a pen and three old receipts are here!'),
    ('matvey', 'Посмотрите в зеркало за стойкой, шеф.', 'Look in the mirror behind the desk, boss.'),
    ('yaroslav', 'Зачем мне смотреть в... ой! Очки опять на голове!', 'Why should I look in the... oh! My glasses are on my head again!'),
    ('kira', 'Прямо у вас на лбу, целые и невредимые.', 'Right there on your forehead, safe and sound.'),
    ('yaroslav', 'Никому не говорите! А теперь широко улыбайтесь, когда позвонят.', 'Do not tell anyone! And now smile brightly when the bell rings.'),
    ('matvey', 'Вот как раз такси подъехало к воротам.', 'Right on cue, a taxi just pulled up to the gate.'),
]
WALK = [
    (0, None, ["'Good morning, everyone! Welcome, Kira. Is everything ready?' The warm greeting ", (None, 'Добро пожаловать,'), ' welcomes guests and new staff alike.']),
    (1, None, "'Good morning, Yaroslav Ilyich! Yes, the desk is clean, and the keys are ready.' Kira addresses the owner by first name plus father's name — the classic Russian mark of polite respect at work."),
    (2, None, ["'The guest in room four is staying with us all week. Everything must be perfect!' Russian has a dedicated feminine word for a female guest, ", (None, 'Гостья'), ' — telling everyone a woman is arriving.']),
    (3, None, ["'Calm down, Yaroslav Ilyich. The room is clean, and the towels are fresh.' Notice the gentle contrast word ", (None, 'а'), ' linking two parallel facts: the room on one side, the towels on the other.']),
    (4, None, ["'I need to read the reservation book, but I cannot find my glasses!' Pairing ", (None, 'не могу найти'), " puts 'cannot' right before 'to find', just like English."]),
    (5, None, ["'Maybe they are in your coat pocket?' At the start of a suggestion, ", (None, 'Может,'), " is short for 'it may be' and works as an everyday 'maybe'."]),
    (6, None, ["'No, only a pen and three old receipts are here!' Notice ", (None, 'ручка'), ' — the very same word meant door handle in scene one and means writing pen here, because both are held by hand.']),
    (7, None, ["'Look in the mirror behind the desk, boss.' Matvey points behind the counter with ", (None, 'за стойкой,'), ' meaning right behind the front desk.']),
    (8, None, ["'Why should I look in the... oh! My glasses are on my head again!' Listen to ", (None, 'Зачем'), " asking 'for what purpose?', while ", (None, 'опять'), ' admits this happens again and again.']),
    (9, None, ["'Right there on your forehead, safe and sound.' Russian says ", (None, 'у вас на лбу,'), " — literally 'by you on the forehead' instead of 'on your forehead'."]),
    (10, None, ["'Do not tell anyone! And now smile brightly when the bell rings.' Where English says 'smile brightly', Russian idiomatic speech says ", (None, 'широко улыбайтесь,'), " — literally 'smile widely'."]),
    (11, None, ["'Right on cue, a taxi just pulled up to the gate.' The approaching prefix on ", (None, 'подъехало'), ' shows the car pulled right up to the entrance rather than driving inside.']),
]
