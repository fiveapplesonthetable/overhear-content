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
    (0, None, "'No, we agreed specifically on today.' Lyova continues frankly as things stand, making his position completely clear."),
    (1, None, '\'Gulya, she is not going to eat you up.\' Lyova reaches for one key element with the guest: "syest" means "to eat", and it carries the main weight of what Lyova is saying.'),
    (2, None, "'Yes, see you soon.' Lyova lays out this point without fuss: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (3, None, "'I love you very much too.' Lyova weighs in pointedly on the spot, without trying to dress up how he really feels."),
    (4, None, '\'Alright, bye, I am waiting for you.\' Lyova colors one memorable detail right here: "poka" means "bye", and it carries the main weight of what Lyova is saying.'),
    (5, None, "'Oh, good morning!' The guest offers this update without fuss: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (6, None, "'You finally woke up, son.' The guest follows up evenly in this moment, keeping the focus on what actually matters here."),
    (7, None, '\'Even though you have a day off, you could have helped your mom.\' The guest features one concrete element in reply: "vykhodnoy" means "a day off", and it carries the main weight of what the guest is saying.'),
    (8, None, "'I have already washed all the floors.' The guest holds firm boldly with a shrug, watching Lyova's face to see how the news lands."),
    (9, None, "'Well and why did you do that, Mom?' Lyova prompts curiously to see how the guest will answer on the spot."),
    (10, None, '\'I would have done everything myself later.\' Lyova leans on one concrete word at once: "sdelal" means "did" (from "sdelat"), giving the line its exact edge.'),
    (11, None, '\'Yes, with you everything is later.\' The guest shares that remark with warmth: Russian says "u tebya" (literally "at you" or "by you") where English uses "you have" or "your", keeping the phrasing close and informal.'),
]
