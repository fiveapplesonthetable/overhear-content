# Authoring module for kukhnya-s03e20-scene-17.
ID = 'kukhnya-s03e20-scene-17'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 20
SCENE = 17
TITLE = 'Закрытие «Клод Моне»  (The Closing of Claude Monet)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.20'
SOURCE_FILE = 'sources/kukhnya/s03/e20.ru.srt'
INTRO = "Back at Claude Monet, Andrey Mikhailovich crashes the celebration with devastating news: because even top crisis manager Sergey quit, the chain's board has decided to close Claude Monet and turn it into a beer sports bar!"
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Chef Barinov's blackmail scheme backfired completely: getting Sergey fired convinced the board to shut down Claude Monet for good. Until next time!"
CLOSING = ('inspector', 'Хорошего дня!')
STORY = [
    ('inspector', 'С огромной радостью испорчу сейчас ваше весёлое празднование.', 'With immense pleasure I will now spoil your merry celebration.', [(290, 'С огромной радостью'), (290, 'ваше празднование')], 'adapted'),
    ('inspector', 'Совет учредителей нашей сети решил закрыть этот ресторан.', 'The board of founders of our chain has decided to close this restaurant.', [(291, 'Только что совет учредителей в нашей сети решил закрыть ресторан')], 'adapted'),
    ('inspector', 'И я лично решил сегодня сообщить вам об этом.', 'And I personally decided to inform you of this today.', [(292, 'и я лично решил сообщить вам об этом')], 'adapted'),
    ('barinov', 'Подождите, как это закрыть? Почему вы его закрываете?', 'Wait, what do you mean close it? Why are you closing it?', [(293, 'Как закрыть? Почему')], 'adapted'),
    ('inspector', 'Теперь на этом месте будет пивной спортбар.', 'Now there will be a beer sports bar in this spot.', [(295, 'Теперь здесь будет пивной спортбар')], 'adapted'),
    ('inspector', 'Потому что ваш французский ресторан совсем нерентабелен.', 'Because your French restaurant is completely unprofitable.', [(297, 'Потому что Клод Мане нерентабелен')], 'adapted'),
    ('inspector', 'И последней каплей для учредителей стал уход Сергея.', "And the last straw for the founders was Sergey's departure.", [(298, 'и последней каплей для учредителей стал уход Сергея')], 'adapted'),
    ('inspector', 'Если лучший управляющий не справился, то никто не сможет.', 'If the best manager could not cope, then nobody can.', [(299, 'Если лучший'), (299, 'управляющий не справился'), (300, 'то никто не сможет')], 'adapted'),
    ('barinov', 'Нет, так не пойдёт! Решай проблему, иначе расскажем жене!', 'No, that will not do! Solve the problem, or we will tell your wife!', [(301, 'Нет, нет, нет, так не пойдет. Давай решай эту проблему')], 'adapted'),
    ('inspector', 'Моя жена уже всё знает, вообще все знают.', 'My wife already knows everything, everyone knows.', [(302, 'Она знает'), (303, 'Все знают')], 'adapted'),
    ('inspector', 'А мне, честно говоря, теперь уже всё равно.', 'And honestly speaking, I do not care anymore.', [(304, 'А мне, честно говоря, все равно')], 'adapted'),
    ('max', 'Будьте здоровы, коллеги, прощайте навсегда!', 'Be well, colleagues, goodbye forever!', [(305, 'Будьте здоровы')], 'adapted'),
]
WALK = [
    (0, None, "'With immense pleasure I will now spoil your merry celebration.' The inspector jumps in openly beside Barinov, keeping the focus on what actually matters here."),
    (1, None, "'The board of founders of our chain has decided to close this restaurant.' The inspector chimes in lightly with a shrug, grounding the moment in plain reality."),
    (2, None, '\'And I personally decided to inform you of this today.\' The inspector reacts promptly during the talk and uses "soobshchit" ("inform, report") to carry the main weight of the thought.'),
    (3, None, '\'Wait, what do you mean close it? Why are you closing it?\' Answering evenly in the exchange, Barinov puts the question word "kak" right at the start so the inspector hears the focus immediately.'),
    (4, None, "'Now there will be a beer sports bar in this spot.' The inspector responds right away in this moment, bringing things back to earth after the buildup."),
    (5, None, '\'Because your French restaurant is completely unprofitable.\' Underscoring how unprofitable things are to Barinov, the inspector reaches for the Russian word "frantsuzskiy" ("French") right at the heart of the line.'),
    (6, None, '\'And the last straw for the founders was Sergey\'s departure.\' Pointing to the founders in the exchange, the inspector brings in "uchrediteley" ("of founders", from "uchreditel") as the key Russian word here.'),
    (7, None, "'If the best manager could not cope, then nobody can.' The inspector weighs in calmly with a smile, steering the talk right where he wants it."),
    (8, None, '\'No, that will not do! Solve the problem, or we will tell your wife!\' Emphasizing the problem at once, Barinov uses "problemu" ("problem", from "problema") to make the point stick.'),
    (9, None, '\'My wife already knows everything, everyone knows.\' Dwelling on his wife around Barinov, the inspector drops in "voobshche" ("in general, altogether") to sum up the whole situation at once.'),
    (10, None, "'And honestly speaking, I do not care anymore.' The inspector fires back steadily in this moment, keeping the focus on what actually matters here."),
    (11, None, '\'Be well, colleagues, goodbye forever!\' Bringing up the colleagues around the inspector, Max uses "proshchayte" ("farewell", from "proshchat") to make the point stick.'),
]
