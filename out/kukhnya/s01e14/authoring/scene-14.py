# Authoring module for kukhnya-s01e14-scene-14.
ID = 'kukhnya-s01e14-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 14
TITLE = 'Секретный рецепт  (A Secret Recipe)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'Max returns to the kitchen in a panic. He needs to cook a classic French dish, but the boss is still unconscious. Elena walks in just in time. Hear it in Russian.'
OPENER = 'Here it is again, slower.'
TRANSITION = 'Now at normal speed.'
OUTRO = 'Max now has a French book he cannot read, and Barinov is finally awake. He uses a word for damn that also means devil. Until next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Шеф, пожалуйста, очнитесь!', 'Chef, please, wake up!', [(192, 'пожалуйста.')], ''),
    ('max', 'Что мне сейчас делать?', 'What should I do now?', [], ''),
    ('elena', 'Максимилиан, вы уже начали готовить?', 'Maximilian, have you already started cooking?', [(193, 'Максимилиан, вы начали?')], ''),
    ('max', 'Да, я почти всё подготовил.', 'Yes, I have almost prepared everything.', [], ''),
    ('elena', 'Это та самая кулинарная книга.', 'This is that very cookbook.', [(194, 'Вот эта книга.')], ''),
    ('elena', 'Здесь есть нужный старинный рецепт.', 'The needed old recipe is here.', [(194, 'Здесь есть старинный рецепт.')], ''),
    ('max', 'Большое спасибо за вашу помощь.', 'Thank you very much for your help.', [], ''),
    ('elena', 'Вы прекрасно говорите по-французски?', 'Do you speak French perfectly?', [(196, 'А вы по-французски-то понимаете?')], ''),
    ('max', 'Конечно, я отлично знаю язык.', 'Of course, I know the language excellently.', [(197, 'Обижаете. В совершенстве.')], ''),
    ('elena', 'Тогда прочитайте этот рецепт вслух.', 'Then read this recipe out loud.', [(198, 'Ну-ка прочитайте.')], ''),
    ('max', 'Сейчас мне нужно быстро работать.', 'Now I need to work quickly.', [(199, 'Работать надо.')], ''),
    ('barinov', 'Черт, моя голова ужасно болит!', 'Damn, my head hurts terribly!', [(201, 'О, черт, моя голова!')], ''),
    ('nagiyev', 'Наконец-то ты открыл свои глаза.', 'Finally you opened your eyes.', [(202, 'Наконец-то.')], ''),
]
WALK = [
    (0, None, ["'Chef, please, wake up!' To say wake up after fainting, use ", ('max', 'очнитесь'), '.']),
    (1, None, ["'What should I do now?' To say what to me to do, use ", ('max', 'Что'), ('max', 'мне'), ' and ', ('max', 'делать'), '.']),
    (2, None, ["'Maximilian, have you already started cooking?' To say 'started', use ", ('elena', 'начали'), '.']),
    (3, None, ["'Yes, I have almost prepared everything.' Almost is ", ('max', 'почти'), '. To say prepared, use ', ('max', 'подготовил'), '.']),
    (4, None, ["'This is that very cookbook.' That very is ", ('elena', 'та'), ('elena', 'самая'), '.']),
    (5, None, ["'The needed old recipe is here.' To say needed, use ", ('elena', 'нужный'), '. An old recipe is ', ('elena', 'старинный'), ('elena', 'рецепт'), '.']),
    (6, None, ["'Thank you very much for your help.' Help is ", ('max', 'помощь'), '.']),
    (7, None, ["'Do you speak French perfectly?' To say perfectly, use ", ('elena', 'прекрасно'), '. In French is ', ('elena', 'по'), '-', ('elena', 'французски'), '.']),
    (8, None, ["'Of course, I know the language excellently.' To say excellently, use ", ('max', 'отлично'), '.']),
    (9, None, ["'Then read this recipe out loud.' To say read out, use ", ('elena', 'прочитайте'), '. Out loud is ', ('elena', 'вслух'), '.']),
    (10, None, ["'Now I need to work quickly.' I need is ", ('max', 'мне'), ('max', 'нужно'), '.']),
    (11, None, ["'Damn, my head hurts terribly!' Damn is ", ('barinov', 'Черт'), '. My head is ', ('barinov', 'моя'), ('barinov', 'голова'), '.']),
    (12, None, ["'Finally you opened your eyes.' Finally is ", ('nagiyev', 'Наконец'), '-', ('nagiyev', 'то'), '. Eyes are ', ('nagiyev', 'глаза'), '.']),
]
