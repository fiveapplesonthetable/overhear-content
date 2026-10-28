# Authoring module for kukhnya-s03e01-scene-17.
ID = 'kukhnya-s03e01-scene-17'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 17
TITLE = 'Неожиданная новость  (Unexpected News)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = "While Nastya's father is in the restroom, he overhears his partners scheming to cheat him with a duplicate contract, and when Nastya runs out to warn him, Kostya blurts out their biggest secret."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes Scene Seventeen. Listen for Kostya stepping forward to tell Nastya's stunned father that he is about to become a grandfather. Until next time!"
CLOSING = ('kostya', 'Хорошего дня!')
STORY = [
    ('guest', 'У нас есть дубликаты. Сейчас подпишем.', 'We have duplicate copies. We will sign now.', [(297, 'У нас есть дубликаты. Сейчас подпишем')], ''),
    ('guest', 'Хорошо, я вас за столиком жду.', 'Good, I am waiting for you at the table.', [(298, 'Хорошо, я вас за столиком жду')], ''),
    ('guest', 'Зачем шампанское попросил?', 'Why did you ask for champagne?', [(299, 'Зачем шампанское попросил')], ''),
    ('guest', 'Не мог подождать, пока подпишем?', "Couldn't you wait until we signed?", [(300, 'Не мог подождать, пока подпишем')], ''),
    ('guest', 'А если он заметит?', 'And what if he notices?', [(302, 'А если он заметит')], ''),
    ('guest', 'Ничего он не заметит. Мне он доверяет.', "He won't notice anything. He trusts me.", [(304, 'Ничего он не заметит'), (304, 'он доверяет')], 'adapted'),
    ('guest', 'Сейчас всё подпишем, и бизнес наш.', 'We will sign everything now, and the business is ours.', [(305, 'Сейчас все подпишем. И бизнес наш')], ''),
    ('guest', 'Давайте уже второй экземпляр.', 'Give me the second copy already.', [(306, 'Давайте уже второй экземпляр')], ''),
    ('nastya', 'Папа, они хотят тебя обмануть!', 'Dad, they want to cheat you!', [(308, 'тебя обмануть')], 'adapted'),
    ('guest', 'Ты что, беременна?', 'What, are you pregnant?', [(310, 'Ты что, беременна')], ''),
    ('kostya', 'Да, она беременна, вы станете дедушкой!', 'Yes, she is pregnant, you will become a grandfather!', [(311, 'Да. Она беременна, вы станете дедушкой')], ''),
    ('kostya', 'Мы скоро поженимся. Честное слово.', 'We are getting married soon. Word of honor.', [(313, 'скоро поженимся'), (314, 'Честное слово')], 'adapted'),
]
WALK = [
    (0, None, '\'We have duplicate copies. We will sign now.\' Mentioning the duplicate around Nastya, the guest reaches for "u nas" ("by us, at our place") to talk about what they share.'),
    (1, None, "'Good, I am waiting for you at the table.' The guest pushes back pointedly hearing Nastya, bringing things back to earth after the buildup."),
    (2, None, '\'Why did you ask for champagne?\' Bringing up the champagne around Nastya, the guest reaches for the Russian word "shampanskoye" ("champagne") right at the heart of the line.'),
    (3, None, "'Couldn't you wait until we signed?' Holding firm smoothly beside Nastya, the guest keeps normal statement word order here, turning the line into a question for Nastya purely through rising pitch."),
    (4, None, "'And what if he notices?' The guest inquires wryly whether Nastya really thought this through."),
    (5, None, '\'He won\'t notice anything. He trusts me.\' The guest steps in naturally to Nastya and puts the weight on "doveryayet" ("trusts", from "doveryat") as the exchange unfolds.'),
    (6, None, '\'We will sign everything now, and the business is ours.\' Turning to the business on the spot, the guest centers the thought on "podpishem" ("will sign", from "podpisat") without wasting a word.'),
    (7, None, "'Give me the second copy already.' The guest replies warmly on the spot, refusing to let the moment slip past."),
    (8, None, '\'Dad, they want to cheat you!\' Highlighting the dad around the guest, Nastya puts the emphasis on "papa" ("Dad") in the middle of the talk.'),
    (9, None, '\'What, are you pregnant?\' Explaining how pregnant things are around Kostya, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (10, None, "'Yes, she is pregnant, you will become a grandfather!' Kostya pushes back sharply toward the guest, letting the remark speak for itself."),
    (11, None, '\'We are getting married soon. Word of honor.\' Stressing how honest things are at once, Kostya brings in "chestnoye" ("honest", from "chestnyy") as the key Russian word here.'),
]
