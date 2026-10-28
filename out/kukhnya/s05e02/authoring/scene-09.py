# Authoring module for kukhnya-s05e02-scene-09.
ID = 'kukhnya-s05e02-scene-09'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 9
TITLE = 'Соус демиглас и тридцать восемь часов  (Demi-Glace Sauce and Thirty-Eight Hours)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = 'After Nastya storms off, Kostya angrily tells Denis to go confess to Katya, while in the kitchen Chef Barinov tends to a French demi-glace sauce that has been simmering for thirty-eight hours. Listen to the scene.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that highlights Chef Barinov's devotion to classic French sauces. Notice the everyday expression 'schitayetsya' meaning 'is considered'. Until next time!"
CLOSING = ('barinov', 'До завтра!')
STORY = [
    ('kostya', 'Ну, чего ты так уставился?', 'Well, what are you staring at like that?', [(92, 'Ну, что уставился?')], 'adapted'),
    ('kostya', 'Иди и расскажи обо всём Кате.', 'Go and tell Katya about everything.', [(93, 'Иди и расскажи обо всем')], 'adapted'),
    ('barinov', 'Во Франции этот соус считается одним из основных.', 'In France this sauce is considered one of the foundational ones.', [(94, 'Во Франции'), (94, 'считается одним из основных')], 'adapted'),
    ('barinov', 'Это один из главных соусов.', 'It is one of the main sauces.', [(94, 'основных соусов')], 'adapted'),
    ('barinov', 'Для приготовления нужны талант и терпение.', 'Preparation requires talent and patience.', [(95, 'Для его приготовления нужны'), (95, 'талант, но еще и терпение')], 'adapted'),
    ('barinov', 'Ведь он готовится очень долго.', 'After all, it cooks for a very long time.', [(96, 'Ведь он готовится')], 'adapted'),
    ('barinov', 'Осталось его процедить и немного выпарить.', 'All that remains is to strain it and reduce it a bit.', [(97, 'осталось его процедить и еще немножко выпарить')], 'adapted'),
    ('senya', 'Тут новый заказ шефу в номер.', "Here is a new 'Chef to the Room' order.", [(98, 'Заказ шеф номер')], 'adapted'),
    ('barinov', 'Нельзя бросать приготовление нашего соуса.', 'One must not abandon the preparation of our sauce.', [(99, 'не бросать его приготовление')], 'adapted'),
    ('barinov', 'Сеня, возьми этот заказ.', 'Senya, take this order.', [(100, 'возьми заказ')], 'adapted'),
    ('senya', 'Это слишком большая ответственность, я не потяну.', 'That is too big a responsibility, I cannot handle it.', [(101, 'Это слишком большая ответственность, я не потяну')], 'verbatim'),
    ('senya', 'Пусть лучше Лёва туда сходит.', 'Better let Lyova go up there.', [(102, 'пусть'), (102, 'сходит')], 'adapted'),
]
WALK = [
    (0, None, "'Well, what are you staring at like that?' Kostya questions straight out before Barinov can change the subject."),
    (1, None, "'Go and tell Katya about everything.' Kostya pushes back right away without holding back, refusing to let the moment slip past."),
    (2, None, '\'In France this sauce is considered one of the foundational ones.\' Discussing the sauce at once, the "-sya" ending on "schitayetsya" ("to be considered") marks an action that unfolds mutually or turns back on the speaker.'),
    (3, None, "'It is one of the main sauces.' Barinov continues sharply in this moment, so Kostya knows he is not just making small talk."),
    (4, None, '\'Preparation requires talent and patience.\' Addressing the preparation around Kostya, Barinov reaches for the Russian word "prigotovleniya" ("for preparation", built from "prigotovleniye") right at the center of the line.'),
    (5, None, '\'After all, it cooks for a very long time.\' Holding firm firmly beside Senya, the "-sya" ending on "gotovitsya" ("is preparing") marks an action that unfolds mutually or turns back on the speaker.'),
    (6, None, "'All that remains is to strain it and reduce it a bit.' Barinov chimes in frankly in their talk, leaving no doubt about where he stands."),
    (7, None, '\'Here is a new \'Chef to the Room\' Discussing the order at once, Senya reaches for the Russian word "novyy" ("new") right at the heart of the line.'),
    (8, None, '\'One must not abandon the preparation of our sauce.\' Addressing the preparation in front of Senya, Barinov leans on "nelzya" ("it is not allowed, one must not"), which carries the whole predicate in Russian without needing "it is".'),
    (9, None, "'Senya, take this order.' Barinov speaks up honestly beside Senya, refusing to let the moment slip past."),
    (10, None, '\'That is too big a responsibility, I cannot handle it.\' Bringing up a responsibility at once, Senya leans on "otvetstvennost" ("responsibility") to give the whole sentence its punch.'),
    (11, None, '\'Better let Lyova go up there.\' Senya speaks frankly at once and uses "luchshe" ("better") to carry the main weight of the thought.'),
]
