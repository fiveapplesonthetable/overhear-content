ID = 'kukhnya-s03e01-scene-14'
SHOW = "kukhnya"
SEASON = 3
EPISODE = 1
SCENE = 14
TITLE = 'Обеденный перерыв  (Lunch Break)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'guest': 'anja', 'katya': 'angelina'}
LABELS = {'anya': 'Макс', 'guest': 'Гость', 'katya': 'Катя'}
SOURCE_NAME = "Кухня (Kukhnya) S3.01"
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'

INTRO = "After Fedya and Senya mock Max in the kitchen as a lowly waiter, Max decides to get revenge on Chef Barinov by recommending Katya's molecular menu to Nastya's hungry father."

STORY = [
    ('katya', 'Мы ещё посмотрим!', 'We will see about that yet!', [(255, 'Мы еще посмотрим')], 'adapted'),
    ('guest', 'Я проголодался.', 'I have gotten hungry.', [(256, 'я проголодался')], 'adapted'),
    ('guest', 'Господа, давайте сделаем обеденный перерыв.', "Gentlemen, let's take a lunch break.", [(257, 'Господа, давайте сделаем обеденный перерыв')], ''),
    ('guest', 'Потом подпишем.', 'We will sign afterward.', [(257, 'потом подпишем')], ''),
    ('guest', 'Максим, что тут у вас вкусного?', 'Maxim, what do you have that is delicious here?', [(258, 'Максим, будь любезен, что тут у вас')], 'adapted'),
    ('anya', 'Знаете, у нас появилось новое меню.', 'You know, we have a new menu.', [(259, 'знаете, у нас появилось новое меню')], ''),
    ('anya', 'Молекулярная кухня. Пожалуйста.', 'Molecular cuisine. Here you go.', [(260, 'Молекулярная кухня. Пожалуйста')], ''),
    ('guest', 'Химия?', 'Chemicals?', [(261, 'Химия')], 'adapted'),
    ('anya', 'Нет, всё натуральное.', 'No, everything is natural.', [(261, 'Нет, всё натуральное')], ''),
    ('guest', 'Как в вашей колбасе? Тогда неси.', 'Like in your sausage? Then bring it.', [(262, 'Как в вашей колбасе'), (263, 'Тогда неси')], 'adapted'),
    ('anya', 'Спагетти и утка, четыре порции!', 'Spaghetti and duck, four portions!', [(264, 'Спагетти'), (264, 'и утка')], 'adapted'),
    ('katya', 'Принято!', 'Order received!', [(265, 'Принято')], ''),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'We will see about that yet!' The meaning hinges on 'we' working together with 'we shall see' in spoken Russian."),
    (1, None, "'I have gotten hungry.' the guest anchors the line on 'I', while 'got hungry' completes the thought."),
    (2, None, "'Gentlemen, let's take a lunch break.' In Russian, the idea of 'gentlemen' flows naturally into 'break' without extra filler words."),
    (3, None, "'We will sign afterward.' Spoken Russian keeps this brisk, leaning on 'then' and finishing on 'will sign'."),
    (4, None, "'Maxim, what do you have that is delicious here?' Notice how Russian expresses 'what' and 'tasty' with crisp inflection rather than helper words. Max answers right away."),
    (5, None, "'You know, we have a new menu.' Max anchors the line on 'know', while 'menu' completes the thought."),
    (6, None, "'Molecular cuisine. Here you go.' Max brings out the contrast between 'molecular' and 'cuisine' in a few short words."),
    (7, None, "'Chemicals?' Notice how Russian expresses 'chemistry' and 'chemistry' with crisp inflection rather than helper words. Max answers right away."),
    (8, None, "'No, everything is natural.' The grammar packs 'no' and 'natural' into a tight, idiomatic kitchen exchange."),
    (9, None, "'Like in your sausage? Then bring it.' The meaning hinges on 'how' working together with 'bring' in spoken Russian."),
    (10, None, "'Spaghetti and duck, four portions!' In Russian, the idea of 'spaghetti' flows naturally into 'portions' without extra filler words. Katya answers right away."),
    (11, None, "'Order received!' Spoken Russian keeps this brisk, leaning on 'accepted' and finishing on 'accepted'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That brings Scene Fourteen to a close. Listen for Max assuring the sausage-factory boss that the molecular dishes are completely natural.'
CLOSING = ('katya', 'Заказ принят!')
