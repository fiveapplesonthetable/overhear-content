# Authoring module for kukhnya-s01e04-scene-20.
ID = 'kukhnya-s01e04-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 20
TITLE = 'Синий супчик  (The Blue Soup)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'louis': 'Луи', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = 'Max brings his special soup to the kitchen crew, and it is a startling bright blue. The cooks are suspicious, Louis the pastry chef recognises his missing food dye, and the soup turns out to taste surprisingly good. Here is the Russian first.'
OPENER = "Let's look at the blue soup."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'The cooks have to admit the blue soup tastes good. You\'ve heard a very useful phrase for "as if".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('senya', 'Что это за странное блюдо?', 'What kind of strange dish is this?', [(269, 'Что за фигня')], ''),
    ('max', 'Это мой новый вкусный суп!', 'This is my new delicious soup!', [], ''),
    ('senya', 'Почему он такого синего цвета?', 'Why is it such a blue color?', [], ''),
    ('max', 'Это оригинальный авторский рецепт.', "This is an original creator's recipe.", [], ''),
    ('senya', 'Спасибо, я сегодня на диете.', 'Thanks, I am on a diet today.', [(270, 'Спасибо, я сегодня на диете')], ''),
    ('max', 'Подожди, это действительно очень вкусно!', 'Wait, this is really very delicious!', [(271, 'Подожди, это вкусно')], ''),
    ('louis', 'Пардон, это же мой краситель!', 'Pardon, that is my food coloring!', [(275, 'Пардон, это же мой краситель')], ''),
    ('louis', 'Я так долго его искал!', 'I looked for it for so long!', [(276, 'я искал, я потерял')], ''),
    ('max', 'Подождите, вы куда все уходите?', 'Wait, where are you all going?', [(277, 'Подождите, вы куда')], ''),
    ('senya', 'Мы не хотим есть химию.', 'We do not want to eat chemicals.', [], ''),
    ('max', 'Но это же реально вкусно!', 'But this is actually delicious!', [(277, 'Это же реально вкусно')], ''),
    ('senya', 'Какой интересный красивый супчик.', 'What an interesting pretty little soup.', [(273, 'Какой красивый супчик')], ''),
    ('senya', 'Как будто прямо море ешь.', 'Like you are eating the sea directly.', [(278, 'как будто море ешь')], ''),
    ('max', 'Я же говорил, что вкусно!', 'I told you it was delicious!', [(278, 'Правда, вкусно')], ''),
]
WALK = [
    (0, None, [
        "'What kind of strange dish is this?' ",
        ('senya', 'Что это за'),
        " translates to 'what kind of'. ",
        ('senya', 'странное'),
        ', strange, describes the Russian term for dish, ',
        ('senya', 'блюдо?'),
        '.'
    ]),
    (1, None, [
        "'This is my new delicious soup!' Built from ",
        ('max', 'мой новый вкусный'),
        " meaning 'my new delicious', where every describing word matches the Russian term for soup, ",
        ('max', 'суп!'),
        '.'
    ]),
    (2, None, [
        "'Why is it such a blue color?' Russian literally gives color as an 'of' phrase: ",
        ('senya', 'такого синего цвета?'),
        ", meaning 'of such a blue color'. The Russian expression for color here is ",
        ('senya', 'цвета?'),
        '.'
    ]),
    (3, None, [
        "'This is an original creator's recipe.' The Russian term for author's is ",
        ('max', 'авторский'),
        ", which describes a chef's own unique cooking. ",
        ('max', 'оригинальный'),
        " translates to 'original'."
    ]),
    (4, None, [
        "'Thanks, I am on a diet today.' The phrase for thanks, ",
        ('senya', 'Спасибо,'),
        ', is used here as a polite no. ',
        ('senya', 'на диете.'),
        " literally translates to 'on a diet'."
    ]),
    (5, None, [
        "'Wait, this is really very delicious!' ",
        ('max', 'Подожди,'),
        ' is the translation for wait. ',
        ('max', 'действительно'),
        " translates to 'really', and ",
        ('max', 'вкусно!'),
        " is 'tasty'."
    ]),
    (6, None, [
        "'Pardon, that is my food coloring!' The Russian expression for dye, ",
        ('louis', 'краситель!'),
        ', is built from the action word for paint, and ',
        ('louis', 'это же'),
        " translates to 'why, that's'."
    ]),
    (7, None, [
        "'I looked for it for so long!' ",
        ('louis', 'искал!'),
        " translates to 'looked for', and ",
        ('louis', 'так долго'),
        " is the phrase for 'so long'."
    ]),
    (8, None, [
        "'Wait, where are you all going?' The translation for 'where to' is ",
        ('max', 'куда'),
        '. ',
        ('max', 'вы'),
        ' and ',
        ('max', 'все'),
        " together translate to 'you all', and ",
        ('max', 'уходите?'),
        " means 'you are leaving'."
    ]),
    (9, None, [
        "'We do not want to eat chemicals.' The expression for chemistry, ",
        ('senya', 'химию.'),
        ', is used here to mean artificial additives.'
    ]),
    (10, None, [
        "'But this is actually delicious!' ",
        ('max', 'реально'),
        " is the slang word for 'really'. ",
        ('max', 'это же'),
        " literally adds the feeling of 'after all'."
    ]),
    (11, None, [
        "'What an interesting pretty little soup.' The translation for little soup, ",
        ('senya', 'супчик.'),
        ', is built from soup with an affectionate ending, making it a cozy little dish. ',
        ('senya', 'Какой'),
        " literally translates to 'what a'."
    ]),
    (12, None, [
        "'Like you are eating the sea directly.' The term for 'as if' is ",
        ('senya', 'Как будто'),
        '. ',
        ('senya', 'ешь.'),
        " translates to 'you eat', meaning 'one eats' in general."
    ]),
    (13, None, [
        "'I told you it was delicious!' ",
        ('max', 'Я же говорил,'),
        " translates to 'I did say', built from ",
        ('max', 'же'),
        " meaning 'after all'."
    ]),
]
