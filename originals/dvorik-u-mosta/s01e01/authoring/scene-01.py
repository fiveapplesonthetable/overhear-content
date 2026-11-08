# Authoring module for dvorik-u-mosta-s01e01-scene-01.
ID = 'dvorik-u-mosta-s01e01-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Подними ручку  (Lift the Handle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'matvey': 'Матвей'}
INTRO = 'Kira arrives early for her very first morning at the Bridge Courtyard Inn in St Petersburg. Behind the front desk, veteran handyman Matvey is already pouring strong tea. Listen to the conversation in Russian first without worrying about catching every word.'
OPENER = "Now let's go back through the conversation slowly, one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kira is inside, the eight brass keys are on the board, and her first morning has begun. Don't worry if a few words went past quickly; they come back all week. See you next time."
CLOSING = ('kira', 'До встречи!')
STORY = [
    ('kira', 'Доброе утро! Извините, дверь закрыта?', 'Good morning! Excuse me, is the door locked?'),
    ('matvey', 'Доброе утро. Нет, сначала подними ручку, а потом толкай.', 'Good morning. No, lift the handle first, then push.'),
    ('kira', 'Ой, открылась! Спасибо. Я Кира, новый администратор.', 'Oh, it opened! Thank you. I am Kira, the new receptionist.'),
    ('matvey', 'Я Матвей. Ты пришла на десять минут раньше.', 'I am Matvey. You arrived ten minutes early.'),
    ('kira', 'В первый день я всегда хожу быстро. А где компьютер?', 'On my first day I always walk fast. Where is the computer?'),
    ('matvey', 'В ящике. Здесь мы пишем в большой бумажной книге карандашом.', 'In the drawer. Here we write in a big paper book with a pencil.'),
    ('kira', 'В бумажной книге? Правда?', 'In a paper book? Really?'),
    ('matvey', 'Бумага работает, даже когда отключают электричество.', 'Paper still works when the power goes out.'),
    ('kira', 'Логично! А это ключи?', 'Fair enough! And these are the keys?'),
    ('matvey', 'Да, восемь комнат и восемь латунных ключей. Гость в четвёртый номер приезжает сегодня.', "Yes, eight rooms and eight brass keys. Room four's guest arrives today."),
    ('kira', 'Отлично. Расскажите мне всё, что нужно знать.', 'Great. Tell me everything I need to know.'),
    ('matvey', 'Правило номер один: сначала выпей горячий чай, а потом отвечай на звонок.', 'Rule number one: drink hot tea first, then answer the bell.'),
]
WALK = [
    (0, None, ["'Good morning! Excuse me, is the door locked?' Notice ", (None, 'закрыта?'), ' — it means closed or locked, with a feminine ending to match the word for door.']),
    (1, None, ["'Good morning. No, lift the handle first, then push.' Matvey speaks to his new colleague with casual commands. The time word ", (None, 'сначала'), " literally builds from 'from the beginning' and means 'first'."]),
    (2, None, ["'Oh, it opened! Thank you. I am Kira, the new receptionist.' Russian drops 'am' in the present, so ", (None, 'Я Кира'), " is literally just 'I Kira'."]),
    (3, None, ["'I am Matvey. You arrived ten minutes early.' Listen to ", (None, 'пришла'), ' — its feminine ending marks a past action by a woman, because Kira is the one who walked in.']),
    (4, None, ["'On my first day I always walk fast. Where is the computer?' For a habit she repeats every time, Russian picks the multidirectional walking word ", (None, 'хожу'), ' rather than a one-way trip.']),
    (5, None, ["'In the drawer. Here we write in a big paper book with a pencil.' No extra word for 'with' is needed: ", (None, 'карандашом'), " changes its tail to mean 'by pencil'."]),
    (6, None, ["'In a paper book? Really?' One brisk word, ", (None, 'Правда?'), " literally means 'truth?' and works whenever English says 'really?'."]),
    (7, None, ["'Paper still works when the power goes out.' The phrase 'power goes out' translates to ", (None, 'отключают электричество'), " — literally 'they disconnect the electricity'."]),
    (8, None, ["'Fair enough! And these are the keys?' Starting a question with ", (None, 'А это'), " smoothly shifts attention to the next thing on the wall: 'and this?'."]),
    (9, None, ["'Yes, eight rooms and eight brass keys. Room four's guest arrives today.' Hotels in Russia call guest rooms by the word for number, so the guest arrives ", (None, 'в четвёртый номер'), " — 'into the fourth number'."]),
    (10, None, ["'Great. Tell me everything I need to know.' Even while Matvey uses casual speech, Kira stays respectful with ", (None, 'Расскажите'), " — the polite command form for 'tell'."]),
    (11, None, ["'Rule number one: drink hot tea first, then answer the bell.' Warm hospitality starts behind the counter: ", (None, 'горячий чай'), " pairs 'hot' with tea, distinct from merely warm bread."]),
]
