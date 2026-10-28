ID = 'kukhnya-s05e10-scene-05'
SHOW = "kukhnya"
SEASON = 5
EPISODE = 10
SCENE = 5
TITLE = 'Проверка номеров  (Inspecting the Rooms)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'inspector': 'anja'}
LABELS = {'anya': 'Михаил', 'inspector': 'Инспектор'}
SOURCE_NAME = "Кухня (Kukhnya) S5.10"
SOURCE_FILE = 'sources/kukhnya/s05/e10.ru.srt'

INTRO = 'Upstairs in the hotel corridor, the strict commission chairwoman measures the hallway and inspects a guest room, criticizing the lighting and wrinkled bedding. Mikhail cheerfully brushes off every flaw as a trifle and leads them to a suite that turns out to be occupied.'

STORY = [
    ('anya', 'Что-то не так?', 'Is something wrong?', [(81, 'Что-то не так')], 'adapted'),
    ('inspector', 'Коридор у вас должен быть на пять сантиметров шире.', 'Your corridor must be five centimeters wider.', [(82, 'Коридор у вас должен быть на пять сантиметров шире')], 'adapted'),
    ('anya', 'Всё исправлено!', 'Everything is fixed!', [(84, 'Все исправлено')], 'adapted'),
    ('inspector', 'Постель помята.', 'The bed is rumpled.', [(85, 'Постель помят')], 'adapted'),
    ('inspector', 'Уборка номеров — три балла.', 'Room housekeeping is three points.', [(86, 'Уборка номеров – три балла')], 'adapted'),
    ('anya', 'Это такие пустяки!', 'Those are such trifles!', [(87, 'Это такие пустяки')], 'adapted'),
    ('anya', 'У нас всё отлично, на пять звёзд.', 'Everything with us is excellent, worthy of five stars.', [(88, 'У нас все отлично'), (89, 'На пять звезд')], 'adapted'),
    ('anya', 'Мы не знали, что этот люкс занят.', 'We did not know that this suite was occupied.', [(90, 'Мы не знали, что этот люк занят')], 'adapted'),
    ('anya', 'Пройдёмте в другой.', 'Let us proceed to another one.', [(91, 'Пройдемте в другой')], 'adapted'),
    ('inspector', 'А вы что, не в курсе?', 'Are you not aware?', [(91, 'А вы что, не в курсе')], 'adapted'),
    ('inspector', 'Какие номера у вас свободны, какие заняты?', 'Which rooms of yours are vacant and which are occupied?', [(91, 'какие номера у вас свободны'), (92, 'какие заняты')], 'adapted'),
    ('anya', 'Сейчас всё проверим!', 'We will check everything right now!', [(84, 'Все исправлено')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Is something wrong?' The meaning hinges on 'something' working together with 'so' in spoken Russian."),
    (1, None, "'Your corridor must be five centimeters wider.' the inspector chooses the respectful plural 'you' alongside 'wider' to keep a polite distance. Mikhail answers right away."),
    (2, None, "'Everything is fixed!' Mikhail brings out the contrast between 'everything' and 'fixed' in a few short words."),
    (3, None, "'The bed is rumpled.' the inspector brings out the contrast between 'bedding' and 'rumpled' in a few short words."),
    (4, None, "'Room housekeeping is three points.' the inspector anchors the line on 'cleaning', while 'points' completes the thought. Mikhail answers right away."),
    (5, None, "'Those are such trifles!' The grammar packs 'this' and 'trifles' into a tight, idiomatic kitchen exchange."),
    (6, None, "'Everything with us is excellent, worthy of five stars.' The grammar packs 'at' and 'stars' into a tight, idiomatic kitchen exchange."),
    (7, None, "'We did not know that this suite was occupied.' The plural past ending '-li' on the verb for 'to know' covers a group or the polite 'you'."),
    (8, None, "'Let us proceed to another one.' Spoken Russian keeps this brisk, leaning on 'let's go' and finishing on 'another'."),
    (9, None, "'Are you not aware?' the inspector chooses the respectful plural 'you' alongside 'course' to keep a polite distance."),
    (10, None, "'Which rooms of yours are vacant and which are occupied?' In Russian, the idea of 'what' flows naturally into 'occupied' without extra filler words. Mikhail answers right away."),
    (11, None, "'We will check everything right now!' Mikhail brings out the contrast between 'now' and 'everything' in a few short words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes the corridor inspection scene. Notice the short passive participles for fixed, rumpled, vacant, and occupied as the inspector grades the hotel. See you in the next scene.'
CLOSING = ('anya', 'У нас всё отлично!')
