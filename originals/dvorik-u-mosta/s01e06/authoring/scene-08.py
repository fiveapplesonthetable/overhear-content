# Authoring module for dvorik-u-mosta-s01e06-scene-08.
ID = 'dvorik-u-mosta-s01e06-scene-08'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = 'Девятый номер  (Room Nine)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'matvey': 'Матвей', 'kira': 'Кира', 'yaroslav': 'Ярослав'}
INTRO = 'Late Friday night after the courtyard empties, Kira and Yaroslav are closing the front desk when Matvey climbs up from the back cellar carrying extra café chairs — and a dusty wooden box. Listen first.'
OPENER = "Let's examine Matvey's cellar discovery in our Season 1 finale."
TRANSITION = 'Now listen to the final scene of Season 1 all the way through.'
OUTRO = "A ninth brass key, a dusty cedar box stamped 'Room 9', and a blueprint showing a hidden door on the ground floor! Season 1 of Bridge Courtyard Inn is complete — see you in Season 2!"
CLOSING = ('matvey', 'До встречи!')
STORY = [
    ('kira', 'Матвей, ты нашёл три складных стула за котельной?', 'Matvey, did you find the three folding chairs behind the boiler room?'),
    ('matvey', 'Стулья нашёл — а за старой кирпичной стенкой нашёл вот это.', 'Found the chairs — and behind an old brick partition wall I found this.'),
    ('yaroslav', 'Маленький кедровый ящик? За пятнадцать лет я ни разу не видел эту шкатулку!', 'A small cedar chest? In fifteen years I have never once seen this box!'),
    ('kira', 'Смахните пыль с латунной таблички сверху... стойте, прочитайте цифру!', 'Brush the dust off the brass plate on top... wait, read the number!'),
    ('yaroslav', 'Сейчас спущу очки со лба... Номер девять?!', 'Let me pull my glasses down from my forehead... Room nine?!'),
    ('kira', 'Матвей, посмотри на деревянную доску с ключами сзади: один, два, три, четыре, пять, шесть, семь, восемь!', 'Matvey, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!'),
    ('yaroslav', 'В нашем доме всегда было только восемь номеров! Где же девятый номер?!', 'Our house has only ever had eight rooms! Where on earth is room nine?!'),
    ('matvey', 'Послушайте, когда я наклоняю ящик — внутри скользит что-то железное.', 'Listen when I tilt the box — something metal slides inside.'),
    ('kira', 'Спереди крошечная замочная скважина, а снизу приклеен старый латунный ключ!', 'In front is a tiny keyhole, and taped underneath is an old brass key!'),
    ('yaroslav', 'Девятый латунный ключ?! Откроем сегодня ночью или подождём до утра?!', 'A ninth brass key?! Do we open it tonight or wait until morning?!'),
    ('matvey', 'Смотрите на сложенный чертёж у петли — на первом этаже нарисована тайная дверь!', 'Look at the folded blueprint by the hinge — a secret door is drawn on the ground floor!'),
    ('kira', 'Берите фонарик оба — моя вторая неделя начинается прямо сейчас!', 'Grab the flashlight, both of you — my second week starts right now!'),
]
WALK = [
    (0, None, ["'Matvey, did you find the three folding chairs behind the boiler room?' Chairs that fold flat are ", (None, 'складных стула'), " — 'folding chairs'."]),
    (1, None, ["'Found the chairs — and behind an old brick partition wall I found this.' Notice brick-built ", (None, 'за старой кирпичной стенкой'), " — 'behind an old brick wall'."]),
    (2, None, ["'A small cedar chest? In fifteen years I have never once seen this box!' Emphatic ", (None, 'ни разу не видел'), " says 'not even one single time have I seen'."]),
    (3, None, ["'Brush the dust off the brass plate on top... wait, read the number!' Wiping dust away with a quick sweep uses ", (None, 'Смахните пыль'), " — 'brush off the dust'."]),
    (4, None, ["'Let me pull my glasses down from my forehead... Room nine?!' Lowering glasses from one's forehead uses ", (None, 'со лба...'), " — 'down from the forehead'."]),
    (5, None, ["'Matvey, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!' Counting straight from ", (None, 'один, два, три,'), ' proves the board stops cold at eight.']),
    (6, None, ["'Our house has only ever had eight rooms! Where on earth is room nine?!' Adding the little intensifier makes ", (None, 'Где же'), " mean 'where on earth?!'."]),
    (7, None, ["'Listen when I tilt the box — something metal slides inside.' Leaning an object to one side is ", (None, 'наклоняю'), " — 'I tilt, tip'."]),
    (8, None, ["'In front is a tiny keyhole, and taped underneath is an old brass key!' Very tiny is ", (None, 'крошечная'), ' — built from the word for a tiny bread crumb.']),
    (9, None, ["'A ninth brass key?! Do we open it tonight or wait until morning?!' Ordinal ", (None, 'Девятый'), " turns 'nine' into 'the ninth'."]),
    (10, None, ["'Look at the folded blueprint by the hinge — a secret door is drawn on the ground floor!' Architectural plan or drawing is ", (None, 'чертёж'), ' — and ', (None, 'тайная дверь!'), " means 'a secret door!'."]),
    (11, None, ["'Grab the flashlight, both of you — my second week starts right now!' Taking hold of a hand torch is ", (None, 'Берите фонарик'), " — and Season 2's mystery is wide open!"]),
]
