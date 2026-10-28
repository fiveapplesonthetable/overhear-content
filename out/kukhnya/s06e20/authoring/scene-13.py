ID = 'kukhnya-s06e20-scene-13'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 20
SCENE = 13
TITLE = "Просьба инспектора и встреча в клинике  (The Inspector's Request and the Clinic Meeting)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'inspector': 'anja', 'nastya': 'angelina'}
LABELS = {'anya': 'Шеф', 'inspector': 'Инспектор', 'nastya': 'Настя'}
SOURCE_NAME = "Кухня (Kukhnya) S6.20"
SOURCE_FILE = 'sources/kukhnya/s06/e20.ru.srt'

INTRO = "Back in a wheelchair, Chef Barinov hears Patrick Malouda's special request: the inspector wants to watch Viktor cook in the kitchen so he can describe his courage in his report! Meanwhile, Nastya and her mother awkwardly run into each other at the DNA clinic."

STORY = [
    ('inspector', 'Значит, ваш сегодняшний ужин не отменяется.', 'So your dinner tonight is not canceled.', [(181, 'Значит, ваш ужин не отменяется')], 'adapted'),
    ('inspector', 'Виктор, у меня к вам просьба.', 'Viktor, I have a request for you.', [(182, 'Виктор, у меня просьба')], 'adapted'),
    ('inspector', 'Возможно, она покажется вам странной.', 'Perhaps it will seem strange to you.', [(183, 'Возможно, она покажется вам странной')], 'adapted'),
    ('inspector', 'Я хочу посмотреть, как вы готовите.', 'I want to watch how you cook.', [(183, 'я очень хочу посмотреть'), (184, 'как вы готовите')], 'adapted'),
    ('inspector', 'Хочу отразить это в своём отчёте.', 'I want to include this in my report.', [(184, 'чтобы отразить это в своем отчете')], 'adapted'),
    ('inspector', 'Скажите, можно мне это увидеть?', 'Tell me, may I see that?', [(185, 'Можно')], 'adapted'),
    ('anya', 'Да, конечно, приходите на кухню.', 'Yes, of course, come into the kitchen.', [(186, 'Конечно')], 'adapted'),
    ('nastya', 'Мама, а ты что тут делаешь?', 'Mom, what are you doing here?', [(188, 'А ты что тут делаешь')], 'adapted'),
    ('anya', 'Папа попросил забрать результаты анализа.', 'Dad asked me to pick up test results.', [(189, 'папа попросил забрать результаты его анализа')], 'adapted'),
    ('nastya', 'А у меня анализ папы Кости.', "And I have Kostya's dad's test.", [(190, 'тоже папа')], 'adapted'),
    ('nastya', 'Ладно, мне уже идти надо.', 'Alright, I need to get going now.', [(193, 'Ладно, мне идти надо')], 'adapted'),
    ('anya', 'Да, мне тоже пора домой.', 'Yes, it is time for me to go home too.', [(193, 'Да, мне тоже')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'So your dinner tonight is not canceled.' The negative particle sits right before the verb meaning 'is canceled' to negate the statement."),
    (1, None, "'Viktor, I have a request for you.' the inspector brings out the contrast between 'at' and 'me' in a few short words."),
    (2, None, "'Perhaps it will seem strange to you.' the inspector chooses the respectful plural 'you' alongside 'strange' to keep a polite distance."),
    (3, None, "'I want to watch how you cook.' the inspector anchors the line on 'I', while 'to cook' completes the thought."),
    (4, None, "'I want to include this in my report.' the inspector anchors the line on 'want', while 'report' completes the thought."),
    (5, None, "'Tell me, may I see that?' Notice how Russian expresses 'say' and 'to see' with crisp inflection rather than helper words. Chef Barinov answers right away."),
    (6, None, "'Yes, of course, come into the kitchen.' The meaning hinges on 'yes' working together with 'kitchen' in spoken Russian."),
    (7, None, "'Mom, what are you doing here?' Nastya brings out the contrast between 'mom' and 'and' in a few short words."),
    (8, None, "'Dad asked me to pick up test results.' The '-l' ending on the verb meaning 'asked' places the action in the masculine past tense. Nastya answers right away."),
    (9, None, "'And I have Kostya's dad's test.' Nastya brings out the contrast between 'and' and 'at' in a few short words."),
    (10, None, "'Alright, I need to get going now.' Here the Russian phrasing highlights 'all right' before landing on 'need'."),
    (11, None, "'Yes, it is time for me to go home too.' Chef Barinov brings out the contrast between 'yes' and 'to me' in a few short words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Before the DNA results even come back, tensions boil over at Kostya and Nastya's apartment. See you in the next scene."
CLOSING = ('nastya', 'Тогда увидимся вечером дома.')
