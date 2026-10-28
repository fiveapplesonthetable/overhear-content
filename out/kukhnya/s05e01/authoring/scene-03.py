ID = 'kukhnya-s05e01-scene-03'
SHOW = "kukhnya"
SEASON = 5
EPISODE = 1
SCENE = 3
TITLE = "Услуга «Шеф в номер»  (The 'Chef to the Room' Service)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'mikhail': 'anja', 'lev': 'angelina'}
LABELS = {'anya': 'Шеф', 'mikhail': 'Михаил', 'lev': 'Лёва'}
SOURCE_NAME = "Кухня (Kukhnya) S5.01"
SOURCE_FILE = 'sources/kukhnya/s05/e01.ru.srt'

INTRO = 'In the kitchen of Restaurant Victor, Chef Barinov discovers a promotional flyer announcing that hotel guests can summon the head chef directly to their rooms. Listen to his clash with manager Mikhail Dzhekovich.'

STORY = [
    ('lev', 'Я пытался его предупредить.', 'I tried to warn him.', [(36, 'я пытался его предупредить')], 'verbatim'),
    ('anya', 'Пошёл вон.', 'Get out.', [(38, 'Пошел')], 'adapted'),
    ('anya', 'Это что за ерунда?', 'What kind of nonsense is this?', [(39, 'Это что за ерунда?')], 'verbatim'),
    ('mikhail', 'В нашем отеле действует новая услуга.', 'A new service operates in our hotel.', [(40, 'В нашем отеле действует услуга')], 'adapted'),
    ('mikhail', 'Это услуга для наших гостей.', 'This is a service for our guests.', [(40, 'услуга')], 'adapted'),
    ('mikhail', 'Вы сможете посмотреть на работу шефа.', "You will be able to watch the chef's work.", [(41, 'Вы сможете понаблюдать за работой')], 'adapted'),
    ('mikhail', 'Это не прерывает ваш отдых.', 'This does not interrupt your rest.', [(42, 'не прерывая ваш отдых')], 'adapted'),
    ('mikhail', 'Я принимаю это после завтрака.', 'I accept that after breakfast.', [(43, 'я принимаю после завтрака')], 'adapted'),
    ('mikhail', 'А сейчас извини.', 'And right now excuse me.', [(44, 'А сейчас извини')], 'verbatim'),
    ('anya', 'Ты введи новую услугу.', 'You should introduce a new service.', [(45, 'ты введи новую услугу')], 'verbatim'),
    ('anya', 'Управляющий идёт прямо в номер.', 'The hotel manager goes straight to the room.', [(46, 'Управляющий в номер')], 'adapted'),
    ('anya', 'Не мешай нашему отдыху.', 'Do not disturb our rest.', [(47, 'вашего отдыха')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'I tried to warn him.' Notice the reflexive suffix on the verb meaning 'tried', turning the action back on the subject. Chef Barinov answers right away."),
    (1, None, "'Get out.' Chef Barinov anchors the line on 'went', while 'over there' completes the thought."),
    (2, None, "'What kind of nonsense is this?' The grammar packs 'this' and 'nonsense' into a tight, idiomatic kitchen exchange."),
    (3, None, "'A new service operates in our hotel.' Notice how Russian expresses 'our' and 'service' with crisp inflection rather than helper words."),
    (4, None, "'This is a service for our guests.' Here the Russian phrasing highlights 'this' before landing on 'guests'."),
    (5, None, "'You will be able to watch the chef's work.' The meaning hinges on 'you' working together with 'proper name' in spoken Russian."),
    (6, None, "'This does not interrupt your rest.' Mikhail chooses the respectful plural 'you' alongside 'rest' to keep a polite distance."),
    (7, None, "'I accept that after breakfast.' The grammar packs 'I' and 'breakfast' into a tight, idiomatic kitchen exchange."),
    (8, None, "'And right now excuse me.' The meaning hinges on 'and' working together with 'sorry' in spoken Russian."),
    (9, None, "'You should introduce a new service.' Spoken Russian keeps this brisk, leaning on 'you' and finishing on 'service'."),
    (10, None, "'The hotel manager goes straight to the room.' Spoken Russian keeps this brisk, leaning on 'hotel manager' and finishing on 'number'."),
    (11, None, "'Do not disturb our rest.' The grammar packs 'not' and 'to the rest' into a tight, idiomatic kitchen exchange."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings the argument over Mikhail's marketing stunt to a close. Notice how Barinov turns Mikhail's own slogan back on him. See you next time."
CLOSING = ('anya', 'Никто не будет командовать на моей кухне!')
