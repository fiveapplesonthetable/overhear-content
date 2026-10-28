# Authoring module for kukhnya-s05e11-scene-19.
ID = 'kukhnya-s05e11-scene-19'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 19
TITLE = "Обман деда раскрыт  (Grandpa's Trick Is Exposed)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'
INTRO = "At the bar, Vika gently pulls Max aside to break the sad news that his grandmother has only two months left to live. When Max blurts out 'Grandma too?!', the two of them realize that the sly grandfather told each of them a different lie just to drink and eat meat."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes the revelation at the bar. Listen for Vika's dry joke that now she knows who Max takes after as they head upstairs to confront his grandfather. Until next time!"
CLOSING = ('max', 'Всего хорошего!')
STORY = [
    ('vika', 'Макс, нам нужно поговорить.', 'Max, we need to talk.', [(300, 'Макс'), (301, 'нам нужно поговорить')], 'adapted'),
    ('max', 'Давай не сейчас.', 'Let us not do it right now.', [(302, 'Давай не сейчас')], 'adapted'),
    ('vika', 'Ты должен кое-что знать.', 'You must know something.', [(302, 'Ты должен кое-что знать')], 'adapted'),
    ('vika', 'Твоя бабушка серьёзно больна.', 'Your grandmother is seriously ill.', [(303, 'Твоя бабушка серьёзно больна')], 'adapted'),
    ('vika', 'Ей осталось пару месяцев.', 'She has a couple of months left.', [(304, 'Ей осталось пару месяцев')], 'adapted'),
    ('max', 'Бабушка тоже?', 'Grandma too?', [(305, 'Бабушка тоже')], 'adapted'),
    ('vika', 'Да, Максим Ильич сказал.', 'Yes, Maxim Ilyich said so.', [(305, 'Да'), (306, 'Максим Ильич сказал')], 'adapted'),
    ('vika', 'Подожди, что значит тоже?', "Wait, what does 'too' mean?", [(306, 'Что'), (307, 'значит тоже')], 'adapted'),
    ('max', 'Мне дед сказал, что это ему осталось два месяца!', 'Grandpa told me that he is the one with two months left!', [(304, 'осталось')], 'adapted'),
    ('vika', 'Он нас обоих обманул!', 'He fooled both of us!', [(308, 'понятно')], 'adapted'),
    ('vika', 'Теперь хотя бы понятно, в кого ты такой.', 'Now at least it is clear who you take after.', [(308, 'Теперь хотя бы понятно, в кого ты такой')], 'adapted'),
    ('max', 'Дед, нам надо серьёзно поговорить!', 'Grandpa, we need to have a serious talk!', [(309, 'Дед, нам надо серьезно поговорить')], 'adapted'),
]
WALK = [
    (0, None, '\'Max, we need to talk.\' Vika chimes in firmly to Max and leans on "pogovorit" ("to talk") to give the whole sentence its punch.'),
    (1, None, '\'Let us not do it right now.\' Leaning in evenly to Vika, Max starts with "davay" ("come on, let\'s") to invite Vika right into the action.'),
    (2, None, "'You must know something.' Vika follows up earnestly around Max, watching Max's face to see how the news lands."),
    (3, None, '\'Your grandmother is seriously ill.\' Underscoring the old lady in this beat, Vika chooses "babushka" ("old lady") so Max gets the point right away.'),
    (4, None, "'She has a couple of months left.' Returning to the months in front of Max, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (5, None, "'Grandma too?' Max wonders briskly whether Vika really thought this through."),
    (6, None, '\'Yes, Maxim Ilyich said so.\' Vika fires back smoothly in this beat and uses "ilich" ("Ilyich") to carry the main weight of the thought.'),
    (7, None, '\'Wait, what does \'too\' Speaking naturally with Max, Vika puts the question word "chto" right at the start so Max hears the focus immediately.'),
    (8, None, "'Grandpa told me that he is the one with two months left!' Bringing up the months with a smile, Max makes it clear to Vika that he means every word."),
    (9, None, '\'He fooled both of us!\' Vika chimes in naturally beside Max and centers the thought on "obmanul" ("cheated", from "obmanut") without wasting a word.'),
    (10, None, '\'Now at least it is clear who you take after.\' Speaking evenly to Max, Vika links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (11, None, "'Grandpa, we need to have a serious talk!' Max cuts in pointedly with Vika, watching Vika's face to see how the news lands."),
]
