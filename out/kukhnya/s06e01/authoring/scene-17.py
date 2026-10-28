# Authoring module for kukhnya-s06e01-scene-17.
ID = 'kukhnya-s06e01-scene-17'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 17
TITLE = "Тост с Михаилом и скандал Кристины  (A Toast with Mikhail and Kristina's Scene)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kristina': 'Кристина', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = "At the bar, brokenhearted Mikhail Dzhekovich pours Barinov a drink to toast Eleonora's wedding, before stumbling upon Kristina and Nagiyev arguing fiercely over money in a quiet room."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'When Mikhail accidentally catches Nagiyev kissing Kristina in the suite, he runs off to fetch Barinov as a witness. Until next time!'
CLOSING = ('mikhail', 'Пока!')
STORY = [
    ('mikhail', 'Витя, садись, выпьем.', "Vitya, sit down, let's drink.", [(302, 'Витя, садись'), (303, 'Выпьем')], 'adapted'),
    ('mikhail', 'Сегодня же такой счастливый день.', 'After all, today is such a happy day.', [(304, 'Сегодня же такой счастливый день')], 'exact'),
    ('mikhail', 'Уж я-то знаю.', 'I certainly know.', [(306, 'Уж я-то знаю')], 'exact'),
    ('mikhail', 'А это кто?', 'And who is that?', [(307, 'А это кто?')], 'exact'),
    ('barinov', 'Бывшая жена Нагиева.', "Nagiyev's ex-wife.", [(308, 'Бывшая жена Нагиева')], 'exact'),
    ('barinov', 'Миша, ты куда?', 'Misha, where are you going?', [(310, 'ты куда?')], 'adapted'),
    ('kristina', 'Где мои деньги?', 'Where is my money?', [(311, 'мои где?')], 'adapted'),
    ('mikhail', 'Нет никаких денег!', 'There is no money!', [(312, 'Нет никаких денег!')], 'exact'),
    ('mikhail', 'Вон какой денежный мешок.', 'Look what a moneybag you found.', [(314, 'денежный мешок')], 'adapted'),
    ('kristina', 'На себя посмотрите, прямо по любви, да?', 'Look at yourselves, right out of love, huh?', [(315, 'На себя посмотрите прям по любви, да?')], 'adapted'),
    ('mikhail', 'Да, по любви.', 'Yes, out of love.', [(316, 'Да, по любви')], 'exact'),
    ('kristina', 'Да, ты прав.', 'Yes, you are right.', [(318, 'Да. Ты прав')], 'exact'),
]
WALK = [
    (0, None, "'Vitya, sit down, let's drink.' Jumping in promptly right here, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (1, None, "'After all, today is such a happy day.' Mikhail pushes back briskly during the talk, to clear the air between them once and for all."),
    (2, None, "'I certainly know.' Reacting calmly at once, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (3, None, '\'And who is that?\' Answering openly before Barinov, Mikhail links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (4, None, "'Nagiyev's ex-wife.' Barinov speaks up pointedly around Mikhail, before Mikhail can change the subject."),
    (5, None, '\'Misha, where are you going?\' Jumping in dryly during the talk, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (6, None, '\'Where is my money?\' Dwelling on her money in the exchange, Kristina links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (7, None, "'There is no money!' Mikhail counters decisively facing Kristina, testing Kristina's reaction in the middle of the exchange."),
    (8, None, '\'Look what a moneybag you found.\' Turning to the sack on the spot, Mikhail lands on "denezhnyy" ("money, monetary") as the key everyday word here.'),
    (9, None, "'Look at yourselves, right out of love, huh?' Dwelling on the love in the exchange, Kristina keeps normal statement word order here, turning the line into a question for Mikhail purely through rising pitch."),
    (10, None, "'Yes, out of love.' Mikhail proceeds bluntly in this moment, making his position completely clear."),
    (11, None, '\'Yes, you are right.\' Pointing out how right Mikhail is during the talk, Kristina reaches for the Russian word "prav" ("right", built from "pravyy") right at the center of the line.'),
]
