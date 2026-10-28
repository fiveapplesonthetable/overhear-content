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
    (0, None, "'Good afternoon, as I understand it, you are Viktor, Katya's dad?' The guest checks briskly what Barinov is actually getting at here."),
    (1, None, '\'A friend of my daughter is a friend of mine.\' Barinov stresses one concrete choice toward Katya: "docheri" means "of daughter" (from "doch"), giving the line its exact edge.'),
    (2, None, '\'Try the dish, your opinion is very important to me.\' Barinov emphasizes this sharp touch with the guest: "poprobuyte" means "try, taste" (from "poprobovat"), giving the line its exact edge.'),
    (3, None, "'How delicious, practically as good as in France!' The guest proceeds quietly as things stand, so Katya knows he is not just making small talk."),
    (4, None, '\'For Russia this is simply excellent.\' The guest features one telling piece with Barinov: "otlichno" means "perfect, great", and it carries the main weight of what the guest is saying.'),
    (5, None, '\'But to cook like my grandmother, one has to be born in France.\' The guest lays out that answer to Katya: the single Russian word "nado" ("it is necessary, one needs to") sets up the whole statement without needing a separate word for "it is".'),
    (6, None, "'Enjoy your meal.' Barinov speaks up decisively toward the guest, bringing things back to earth after the buildup."),
    (7, None, '\'Katya, this is insanely delicious!\' The guest picks one direct detail in reply: "bezumno" means "madly, crazily", and it carries the main weight of what the guest is saying.'),
    (8, None, '\'What did he say to you?\' Barinov sends this answer with ease: putting the question word "chto" right at the front of the line lets the guest hear the point of the question on the very first beat.'),
    (9, None, "'He said that it is oversalted.' Katya cuts in candidly before the guest, keeping the focus on what actually matters here."),
    (10, None, '\'Listen, does Nikita usually sit here?\' The guest reaches for one loaded word toward Barinov: "slushay" means "listen" (from "slushat"), giving the line its exact edge.'),
    (11, None, '\'Yes, I need to pay him back for something.\' Katya shares that line briskly now: the single Russian word "nado" ("it is necessary, one needs to") sets up the whole statement without needing a separate word for "it is".'),
]
