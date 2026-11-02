# Authoring module for kukhnya-s01e05-scene-03.
ID = 'kukhnya-s01e05-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = 'Операция «Треска»  (Operation Cod)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Over in the Claude Monet kitchen, Chef Barinov has a problem that has nothing to do with love: somebody thawed a pile of cod, and it all has to be sold today. He gathers the staff and pulls in Sasha, one of the waitresses, to help. Listen to it in Russian first.'
OPENER = 'Now slowly. Barinov gives orders, and orders are short, which suits us.'
TRANSITION = 'Once more from the top, at full speed.'
OUTRO = 'Some of this works in any job: the word for \'understood\', and asking \'what do we do now\'. As for the cod, Barinov means that fine.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Внимание, повара! Начнём наше собрание.', 'Attention, cooks! Let us begin our meeting.', [(38, 'начнем собрание')], ""),
    ('sasha', 'Шеф, что сегодня стряслось на кухне?', 'Chef, what happened in the kitchen today?', [], ""),
    ('barinov', 'Кто-то вчера разморозил пять килограммов трески.', 'Someone thawed five kilograms of cod yesterday.', [(39, 'разморозил пять килограммов трески')], ""),
    ('sasha', 'И что нам теперь делать?', 'And what are we to do now?', [], ""),
    ('barinov', 'Мы обязаны продать всю рыбу сегодня!', 'We must sell all the fish today!', [(40, 'мы должны ее сегодня продать')], ""),
    ('sasha', 'Гости заказывают только мясо и пасту.', 'Guests only order meat and pasta.', [], ""),
    ('barinov', 'Саша, подойди ко мне немедленно.', 'Sasha, come to me immediately.', [(42, 'Саша! Зайди сюда')], ""),
    ('sasha', 'Я слушаю вас внимательно, шеф.', 'I am listening to you carefully, chef.', [(43, 'Да, шеф')], ""),
    ('barinov', 'Передай официантам: сегодня активно предлагаем треску.', 'Tell the waiters: today we actively offer cod.', [(43, 'что сегодня продаем треску')], ""),
    ('sasha', 'Может быть, сделаем специальную скидку?', 'Maybe we will give a special discount?', [], ""),
    ('barinov', 'Да, скидка двадцать процентов на рыбу.', 'Yes, twenty percent discount on fish.', [(44, 'скидка 20%')], ""),
    ('sasha', 'Понятно, шеф, мы всё организуем.', 'Understood, chef, we will organize everything.', [(45, 'Понятно')], ""),
    ('barinov', 'Если рыба останется, я вас оштрафую!', 'If fish remains, I will fine you!', [], ""),
]
WALK = [
    (0, None, [
        "'Attention, cooks! Let us begin our meeting.' works just like 'attention!' in English. ",
        ('barinov', 'Внимание,'),
        " The word for 'cook' makes its plural with a stressed -a, ",
        ('barinov', 'повара!'),
        ", as a handful of common words do."
    ]),
    (1, None, [
        "'Chef, what happened in the kitchen today?' is a dramatic 'happened', for something ",
        ('sasha', 'стряслось'),
        " bad that has suddenly landed on you. Kitchens take the preposition for 'on', not 'in': ",
        ('sasha', 'на'),
        ('sasha', 'кухне?'),
        ", 'in the kitchen'."
    ]),
    (2, None, [
        "'Someone thawed five kilograms of cod yesterday.' is the pronoun for 'who' plus ",
        ('barinov', 'Кто-то'),
        " -to, making 'someone'. ",
        ('barinov', 'разморозил'),
        " has the noun for 'frost' inside, with the prefix undoing it, and after the number 'five' comes ",
        ('barinov', 'килограммов'),
        ('barinov', 'трески.'),
        ", 'of kilograms of cod'."
    ]),
    (3, None, [
        "'And what are we to do now?' Literally 'and what to-us now to do?'. There's no 'should' and no 'are', just ",
        ('sasha', 'нам'),
        ", 'to us', and the bare verb ",
        ('sasha', 'делать?')
    ]),
    (4, None, [
        "'We must sell all the fish today!' is a strong 'must', close to ",
        ('barinov', 'обязаны'),
        " 'we are obliged'. The noun for 'fish' becomes ",
        ('barinov', 'всю'),
        ('barinov', 'рыбу'),
        " because it's what gets sold."
    ]),
    (5, None, [
        "'Guests only order meat and pasta.' Pasta becomes ",
        ('sasha', 'пасту.'),
        " as the thing ordered, while ",
        ('sasha', 'мясо'),
        ", 'meat', stays as it is: words ending in -o don't change here."
    ]),
    (6, None, [
        "'Sasha, come to me immediately.' is a command to one person, ",
        ('barinov', 'подойди'),
        " 'come over'. Before ",
        ('barinov', 'мне'),
        ", the little preposition for 'to' gets an extra vowel, forming ",
        ('barinov', 'ко'),
        ('barinov', 'мне'),
        "."
    ]),
    (7, None, [
        "'I am listening to you carefully, chef.' Sasha uses ",
        ('sasha', 'вас'),
        ", the polite 'you', with her boss. ",
        ('sasha', 'внимательно,'),
        " meaning 'carefully', is built on the noun for 'attention' that opened the scene."
    ]),
    (8, None, [
        "'Tell the waiters: today we actively offer cod.' is 'pass on', for handing a ",
        ('barinov', 'Передай'),
        " ss on', for handing a message along. ",
        ('barinov', 'официантам:'),
        " ends in -am, meaning 'to the waiters'."
    ]),
    (9, None, [
        "'Maybe we will give a special discount?' is literally 'may be'. Sasha phrases ",
        ('sasha', 'Может'),
        ('sasha', 'быть,'),
        ' her idea as a question, the safe way to suggest something to a boss.'
    ]),
    (10, None, [
        "'Yes, twenty percent discount on fish.' , 'twenty', means 'two' glued to ",
        ('barinov', 'двадцать'),
        " a shortened 'ten'. After it, the noun for 'percent' takes the form ",
        ('barinov', 'процентов'),
        ", as it does after five, six and so on."
    ]),
    (11, None, [
        "'Understood, chef, we will organize everything.' 'understood', is the word to use ",
        ('sasha', 'Понятно,'),
        ' with any boss. ',
        ('sasha', 'организуем.'),
        " looks like English, with the ending representing 'we'."
    ]),
    (12, None, [
        "'If fish remains, I will fine you!' , 'if', opens the ",
        ('barinov', 'Если'),
        ' threat. ',
        ('barinov', 'оштрафую!'),
        " hides the root word for 'a fine', and ",
        ('barinov', 'вас'),
        " here means the whole staff."
    ]),
]
