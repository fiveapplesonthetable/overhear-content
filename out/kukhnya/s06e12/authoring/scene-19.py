# Authoring module for kukhnya-s06e12-scene-19.
ID = 'kukhnya-s06e12-scene-19'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 12
SCENE = 19
TITLE = "Кольцо на чужой руке и признание Михаила  (A Ring on Another Hand and Mikhail's Confession)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.12'
SOURCE_FILE = 'sources/kukhnya/s06/e12.ru.srt'
INTRO = "At the anniversary table, Kostya awkwardly presents Nastya with her new ring while it is still stuck on Sveta's hand. Upstairs in room 205, Barinov confronts Mikhail, who—having eaten the spiked pasta himself—confesses that he hates Barinov for siding with Nagiyev."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Shocked by Mikhail's confession under the truth serum, Barinov learns just how many of his recent disasters Mikhail secretly caused. Until next time!"
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('kostya', 'Настенька, от души поздравляю тебя с нашей годовщиной.', 'Nastenka, from the bottom of my heart I congratulate you on our anniversary.', [(308, 'Настенька, поздравляю тебя с нашей годовщиной')], 'adapted'),
    ('kostya', 'Пусть эта красота на руке вечно гармонирует с тобой.', 'May this beauty on the hand forever harmonize with you.', [(309, 'И пусть эта красота на руке вечно гармонирует')], 'adapted'),
    ('mikhail', 'Спасибо, конечно, но мне ещё не дарили кольцо на другой женщине.', 'Thank you, of course, but nobody has ever given me a ring on another woman before.', [(310, 'Спасибо, конечно'), (311, 'Мне еще никто не дарил кольцо на другой женщине')], 'adapted'),
    ('kostya', 'Прости, Настя, просто Света подумала, что Денис ей кольцо купил.', 'Forgive me, Nastya, Sveta just thought that Denis bought the ring for her.', [(312, 'Прости меня, пожалуйста, Настя'), (313, 'Она подумала, что Дэн ей кольцо купил')], 'adapted'),
    ('kostya', 'Не волнуйся, мы сейчас пойдём и быстро его снимем.', 'Do not worry, we will go right now and quickly take it off.', [(315, 'Мы сейчас снимем')], 'adapted'),
    ('barinov', 'Миша, можешь объяснить, как сыворотка правды попала в общий котёл?', 'Misha, can you explain how the truth serum got into the common pot?', [(316, 'объяснить, как сыворотка правды попала в общий котел')], 'adapted'),
    ('mikhail', 'Я вылил твою сыворотку в котёл, а вместо неё воды налил.', 'I poured your serum into the pot, and poured water in its place.', [(317, 'Я ее вылил, а вместо нее воды налил')], 'adapted'),
    ('barinov', 'Миша, но зачем ты вообще это сегодня сделал?', 'Misha, why on earth did you do that today?', [(318, 'Миша, зачем ты это сделал')], 'adapted'),
    ('mikhail', 'Потому что я очень хотел, чтобы ты сегодня проигрался.', 'Because I really wanted you to lose your money today.', [(319, 'Хотел, чтобы ты проигрался')], 'adapted'),
    ('mikhail', 'Я тебя ненавижу, потому что ты меня тогда предал.', 'I hate you, because you betrayed me back then.', [(320, 'Я тебя ненавижу'), (322, 'Ты меня предал')], 'adapted'),
    ('mikhail', 'Я считал тебя другом, а ты поддержал этого Нагиева.', 'I considered you a friend, and you supported that Nagiyev.', [(322, 'Я тебя считал другом, а ты поддержал не меня')], 'adapted'),
    ('barinov', 'Миша, но ведь я тогда просто пожалел Элеонору.', 'Misha, but back then I simply felt sorry for Eleonora.', [(323, 'Миша, я тогда просто пожалел Элеонору')], 'adapted'),
    ('mikhail', 'Это очень благородно, но с тех пор я перестал жалеть тебя!', 'That is very noble, but since then I stopped feeling sorry for you!', [(324, 'Благородно, но с тех пор я перестал жалеть тебя')], 'adapted'),
]
WALK = [
    (0, None, '\'Nastenka, from the bottom of my heart I congratulate you on our anniversary.\' Mentioning his anniversary in this beat, Kostya lands on "godovshchinoy" ("anniversary", built on "godovshchina") to keep the statement grounded.'),
    (1, None, '\'May this beauty on the hand forever harmonize with you.\' Discussing the beauty in this beat, Kostya chooses "garmoniruyet" ("harmonizes", from the root "garmonirovat") so Mikhail hears the exact meaning.'),
    (2, None, "'Thank you, of course, but nobody has ever given me a ring on another woman before.' Mikhail responds calmly with a smile, grounding the moment in plain reality."),
    (3, None, '\'Forgive me, Nastya, Sveta just thought that Denis bought the ring for her.\' Underscoring the ring to Mikhail, Kostya brings in "koltso" ("ring") to make the meaning unmistakable.'),
    (4, None, '\'Do not worry, we will go right now and quickly take it off.\' Turning firmly to Barinov, the "-sya" ending on "volnuysya" ("worry") marks an action that unfolds mutually or turns back on the speaker.'),
    (5, None, "'Misha, can you explain how the truth serum got into the common pot?' Barinov asks firmly why things suddenly took this turn between them."),
    (6, None, '\'I poured your serum into the pot, and poured water in its place.\' Talking about the serum with Barinov, Mikhail reaches for the Russian word "syvorotku" ("serum", built from "syvorotka") right at the center of the line.'),
    (7, None, '\'Misha, why on earth did you do that today?\' Weighing in calmly with Mikhail, Barinov drops in "voobshche" ("in general, altogether") to sum up the whole situation at once.'),
    (8, None, "'Because I really wanted you to lose your money today.' Mikhail chimes in at once watching Barinov, steering the talk right where he wants it."),
    (9, None, '\'I hate you, because you betrayed me back then.\' Mikhail responds smoothly right here and reaches for the Russian word "nenavizhu" ("hate", built from "nenavidet") right at the center of the line.'),
    (10, None, "'I considered you a friend, and you supported that Nagiyev.' Mikhail counters sharply watching Barinov, shifting the mood of the conversation in a single beat."),
    (11, None, "'Misha, but back then I simply felt sorry for Eleonora.' Barinov continues frankly with a smile, steering the talk right where he wants it."),
    (12, None, '\'That is very noble, but since then I stopped feeling sorry for you!\' Mikhail continues evenly with Barinov and lands on "blagorodno" ("nobly") as the key everyday word here.'),
]
