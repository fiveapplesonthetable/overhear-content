# Authoring module for kukhnya-s06e04-scene-03.
ID = 'kukhnya-s06e04-scene-03'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 3
TITLE = "Утро у Лёвы дома  (Morning at Lyova's Home)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'On his day off, sous-chef Lyova reassures Gulya on the phone before she comes over to meet his mother Vera Ivanovna, who complains that she has already washed all the floors herself.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'When his mother sighs that she needs a female helper in the apartment, Lyova smiles and says one will arrive very soon. Until next time!'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('lyova', 'Нет, мы договаривались именно на сегодня.', 'No, we agreed specifically on today.', [(38, 'мы договаривались именно на сегодня')], 'adapted'),
    ('lyova', 'Гуля, да не съест она тебя.', 'Gulya, she is not going to eat you up.', [(39, 'да не съест она тебя')], 'adapted'),
    ('lyova', 'Да, до встречи.', 'Yes, see you soon.', [(40, 'Да. До встречи')], 'exact'),
    ('lyova', 'Я тоже тебя очень люблю.', 'I love you very much too.', [(41, 'Да, и я тебя')], 'adapted'),
    ('lyova', 'Все, пока, жду тебя.', 'Alright, bye, I am waiting for you.', [(43, 'Все, пока')], 'adapted'),
    ('guest', 'О, доброе утро!', 'Oh, good morning!', [(44, 'О, доброе утро')], 'exact'),
    ('guest', 'Проснулся наконец, сынок.', 'You finally woke up, son.', [(45, 'Проснулся наконец')], 'adapted'),
    ('guest', 'Хоть у тебя и выходной, мог бы маме помочь.', 'Even though you have a day off, you could have helped your mom.', [(46, 'Хоть у тебя и выходной мог бы маме помочь')], 'exact'),
    ('guest', 'Я уже все полы вымыла.', 'I have already washed all the floors.', [(47, 'Я уже все полы вымыла')], 'exact'),
    ('lyova', 'Ну и зачем, мама?', 'Well and why did you do that, Mom?', [(48, 'Ну и зачем, мам?')], 'adapted'),
    ('lyova', 'Я бы потом все сам сделал.', 'I would have done everything myself later.', [(49, 'Я бы потом все сам сделал')], 'exact'),
    ('guest', 'Да, у тебя все потом.', 'Yes, with you everything is later.', [(50, 'Да, у тебя все потом')], 'exact'),
]
WALK = [
    (0, None, "'No, we agreed specifically on today.' Lyova pushes back frankly without a pause, grounding the moment in plain reality."),
    (1, None, '\'Gulya, she is not going to eat you up.\' Lyova cuts in calmly before the guest and reaches for the Russian word "syest" ("to eat") right at the heart of the line.'),
    (2, None, "'Yes, see you soon.' Addressing the meeting to the guest, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (3, None, "'I love you very much too.' Lyova weighs in pointedly facing the guest, letting the remark speak for itself."),
    (4, None, '\'Alright, bye, I am waiting for you.\' Lyova lightly extends this casual farewell in one quick breath using "poka" ("bye") — the quick everyday word for "bye for now" between people on close terms.'),
    (5, None, '\'Oh, good morning!\' The guest smoothly directs this morning greeting to Lyova using "dobroye utro" ("good morning") — literally "kind morning", with the neuter ending matching "utro" ("morning").'),
    (6, None, "'You finally woke up, son.' The guest reacts evenly toward Lyova, before Lyova can change the subject."),
    (7, None, '\'Even though you have a day off, you could have helped your mom.\' Underscoring a day before Lyova, the guest centers the remark on "vykhodnoy" ("a day off") without any extra fuss.'),
    (8, None, '\'I have already washed all the floors.\' Underscoring the floors beside Lyova, the guest leans on "poly" ("floors") to give the whole sentence its punch.'),
    (9, None, "'Well and why did you do that, Mom?' Lyova prompts curiously to see how the guest will answer on the spot."),
    (10, None, "'I would have done everything myself later.' Lyova speaks wryly without any doubt, making his position completely clear."),
    (11, None, '\'Yes, with you everything is later.\' Opening up promptly before Lyova, the guest uses "u tebya" (literally "by you") where English says "you have" or "your".'),
]
