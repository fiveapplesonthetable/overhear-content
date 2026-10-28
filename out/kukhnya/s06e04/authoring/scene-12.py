ID = 'kukhnya-s06e04-scene-12'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 4
SCENE = 12
TITLE = "Пересоленный голубь и месть Дениса  (Oversalted Pigeon and Denis's Revenge)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'guest': 'anja', 'katya': 'angelina'}
LABELS = {'anya': 'Шеф', 'guest': 'Гость', 'katya': 'Катя'}
SOURCE_NAME = "Кухня (Kukhnya) S6.04"
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'

INTRO = "Olivier tells Barinov that the pigeon is almost as good as his grandmother's in Provence—and then whispers to Katya how delicious it really is, while Katya tells her father that Olivier said it was oversalted!"

STORY = [
    ('guest', 'Добрый день, я так понимаю, вы Виктор, папа Кати?', "Good afternoon, as I understand it, you are Viktor, Katya's dad?", [(192, 'Добрый день. Я так понимаю, вы Виктор, папа Кати?')], 'exact'),
    ('anya', 'Друг моей дочери — мой друг.', 'A friend of my daughter is a friend of mine.', [(194, 'Друг моей дочери – мой друг')], 'exact'),
    ('anya', 'Попробуйте блюдо, мне очень важно ваше мнение.', 'Try the dish, your opinion is very important to me.', [(195, 'Попробуйте'), (195, 'мне очень важно ваше мнение')], 'adapted'),
    ('guest', 'Как вкусно, практически так же хорошо, как и во Франции!', 'How delicious, practically as good as in France!', [(196, 'Как вкусно!'), (197, 'Практически так же хорошо, как и во Франции')], 'adapted'),
    ('guest', 'Для России это просто отлично.', 'For Russia this is simply excellent.', [(197, 'но для России это просто отлично')], 'adapted'),
    ('guest', 'Но чтобы готовить, как моя бабушка, надо родиться во Франции.', 'But to cook like my grandmother, one has to be born in France.', [(198, 'моя бабушка, но чтобы готовить, как она'), (199, 'надо родиться в')], 'adapted'),
    ('anya', 'Приятного аппетита.', 'Enjoy your meal.', [(200, 'Приятного аппетита')], 'exact'),
    ('guest', 'Катя, это безумно вкусно!', 'Katya, this is insanely delicious!', [(201, 'Катя'), (202, 'Это безумно вкусно')], 'adapted'),
    ('anya', 'Что он тебе сказал?', 'What did he say to you?', [(203, 'Что он сказал?')], 'adapted'),
    ('katya', 'Он сказал, что пересолено.', 'He said that it is oversalted.', [(204, 'Он сказал, что пересолено')], 'exact'),
    ('guest', 'Слушай, а Никита обычно здесь сидит?', 'Listen, does Nikita usually sit here?', [(205, 'Слушай, а Никита обычно здесь сидит?')], 'exact'),
    ('katya', 'Да, надо вернуть ему кое-что.', 'Yes, I need to pay him back for something.', [(206, 'Да'), (207, 'надо вернуть ему кое-что')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Good afternoon, as I understand it, you are Viktor, Katya's dad?' Notice how Russian expresses 'good' and 'Katya's' with crisp inflection rather than helper words. Chef Barinov answers right away."),
    (1, None, "'A friend of my daughter is a friend of mine.' Chef Barinov anchors the line on 'friend', while 'of daughter' completes the thought."),
    (2, None, "'Try the dish, your opinion is very important to me.' The grammar packs 'try' and 'opinion' into a tight, idiomatic kitchen exchange."),
    (3, None, "'How delicious, practically as good as in France!' The meaning hinges on 'how' working together with 'France' in spoken Russian."),
    (4, None, "'For Russia this is simply excellent.' In Russian, the idea of 'for' flows naturally into 'perfectly' without extra filler words."),
    (5, None, "'But to cook like my grandmother, one has to be born in France.' The meaning hinges on 'but' working together with 'France' in spoken Russian."),
    (6, None, "'Enjoy your meal.' Notice how Russian expresses 'pleasant' and 'appetite' with crisp inflection rather than helper words. the guest answers right away."),
    (7, None, "'Katya, this is insanely delicious!' Here the Russian phrasing highlights 'Katya' before landing on 'deliciously'."),
    (8, None, "'What did he say to you?' Chef Barinov raises the pitch on 'said' to turn the phrase into a direct spoken question."),
    (9, None, "'He said that it is oversalted.' Spoken Russian keeps this brisk, leaning on 'he' and finishing on 'oversalted'. the guest answers right away."),
    (10, None, "'Listen, does Nikita usually sit here?' the guest anchors the line on 'listen', while 'is sitting' completes the thought."),
    (11, None, "'Yes, I need to pay him back for something.' The meaning hinges on 'yes' working together with 'something' in spoken Russian."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Stung by the claim that his pigeon was oversalted and inferior to a French grandmother's, Barinov storms back to the kitchen. See you in the next scene."
CLOSING = ('katya', 'Он сказал, что пересолено!')
