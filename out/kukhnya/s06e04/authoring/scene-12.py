# Authoring module for kukhnya-s06e04-scene-12.
ID = 'kukhnya-s06e04-scene-12'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 12
TITLE = "Пересоленный голубь и месть Дениса  (Oversalted Pigeon and Denis's Revenge)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = "Olivier tells Barinov that the pigeon is almost as good as his grandmother's in Provence—and then whispers to Katya how delicious it really is, while Katya tells her father that Olivier said it was oversalted!"
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Stung by the claim that his pigeon was oversalted and inferior to a French grandmother's, Barinov storms back to the kitchen. See you next time!"
CLOSING = ('katya', 'До встречи!')
STORY = [
    ('guest', 'Добрый день, я так понимаю, вы Виктор, папа Кати?', "Good afternoon, as I understand it, you are Viktor, Katya's dad?", [(192, 'Добрый день. Я так понимаю, вы Виктор, папа Кати?')], 'exact'),
    ('barinov', 'Друг моей дочери — мой друг.', 'A friend of my daughter is a friend of mine.', [(194, 'Друг моей дочери – мой друг')], 'exact'),
    ('barinov', 'Попробуйте блюдо, мне очень важно ваше мнение.', 'Try the dish, your opinion is very important to me.', [(195, 'Попробуйте'), (195, 'мне очень важно ваше мнение')], 'adapted'),
    ('guest', 'Как вкусно, практически так же хорошо, как и во Франции!', 'How delicious, practically as good as in France!', [(196, 'Как вкусно!'), (197, 'Практически так же хорошо, как и во Франции')], 'adapted'),
    ('guest', 'Для России это просто отлично.', 'For Russia this is simply excellent.', [(197, 'но для России это просто отлично')], 'adapted'),
    ('guest', 'Но чтобы готовить, как моя бабушка, надо родиться во Франции.', 'But to cook like my grandmother, one has to be born in France.', [(198, 'моя бабушка, но чтобы готовить, как она'), (199, 'надо родиться в')], 'adapted'),
    ('barinov', 'Приятного аппетита.', 'Enjoy your meal.', [(200, 'Приятного аппетита')], 'exact'),
    ('guest', 'Катя, это безумно вкусно!', 'Katya, this is insanely delicious!', [(201, 'Катя'), (202, 'Это безумно вкусно')], 'adapted'),
    ('barinov', 'Что он тебе сказал?', 'What did he say to you?', [(203, 'Что он сказал?')], 'adapted'),
    ('katya', 'Он сказал, что пересолено.', 'He said that it is oversalted.', [(204, 'Он сказал, что пересолено')], 'exact'),
    ('guest', 'Слушай, а Никита обычно здесь сидит?', 'Listen, does Nikita usually sit here?', [(205, 'Слушай, а Никита обычно здесь сидит?')], 'exact'),
    ('katya', 'Да, надо вернуть ему кое-что.', 'Yes, I need to pay him back for something.', [(206, 'Да'), (207, 'надо вернуть ему кое-что')], 'adapted'),
]
WALK = [
    (0, None, "'Good afternoon, as I understand it, you are Viktor, Katya's dad?' The guest checks briskly how Barinov expects that to work in practice."),
    (1, None, '\'A friend of my daughter is a friend of mine.\' Bringing up his daughter before the guest, Barinov reaches for the Russian word "docheri" ("of daughter", built from "doch") right at the center of the line.'),
    (2, None, "'Try the dish, your opinion is very important to me.' Barinov follows up quietly toward the guest, letting the remark speak for itself."),
    (3, None, "'How delicious, practically as good as in France!' The guest speaks up quietly around Barinov, before Barinov can change the subject."),
    (4, None, '\'For Russia this is simply excellent.\' The guest chimes in readily at once and centers the remark on "otlichno" ("perfect, great") without any extra fuss.'),
    (5, None, '\'But to cook like my grandmother, one has to be born in France.\' Discussing the old lady at once, the guest leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
    (6, None, "'Enjoy your meal.' Barinov replies decisively beside the guest, letting the remark speak for itself."),
    (7, None, '\'Katya, this is insanely delicious!\' The guest proceeds naturally around Katya and centers the remark on "bezumno" ("madly, crazily") without any extra fuss.'),
    (8, None, '\'What did he say to you?\' Reacting quietly in the exchange, Barinov puts the question word "chto" right at the start so Katya hears the focus immediately.'),
    (9, None, "'He said that it is oversalted.' Katya follows up candidly in this moment, refusing to let the moment slip past."),
    (10, None, '\'Listen, does Nikita usually sit here?\' The guest opens up vividly at once and reaches for the Russian word "slushay" ("listen", built from "slushat") right at the center of the line.'),
    (11, None, '\'Yes, I need to pay him back for something.\' Jumping in earnestly in the exchange, Katya leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
]
