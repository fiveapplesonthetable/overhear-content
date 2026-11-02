# Authoring module for kukhnya-s01e04-scene-06.
ID = 'kukhnya-s01e04-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = "Гнев шефа  (The Chef's Wrath)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Barinov has found out that the rival restaurant is trying to recruit his cooks. After an angry phone call with Elena, he storms into the kitchen holding a résumé and demands to know whose it is. Here's the Russian first."
OPENER = "Now the chef's temper, line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = ['The chef is hunting for a traitor, and Max is nervous for a reason. Keep the term for traitor in mind, ', ('barinov', 'Предатель'), ', which is built from betray.']
CLOSING = ('max', 'До встречи!')
STORY = [
    ('barinov', 'Я съем свой поварской колпак!', "I will eat my chef's hat!", [(52, 'Я съем свой колпак')], ''),
    ('barinov', 'Никто из моих людей не пойдёт к вам!', 'None of my people will go to you!', [(52, 'кто-то из моих ходил к вам')], ''),
    ('elena', 'Тогда приятного вам аппетита, Виктор!', 'Then bon appétit to you, Viktor!', [(53, 'Тогда приятного аппетита')], ''),
    ('barinov', 'Ах вы, неблагодарные люди!', 'Oh you, ungrateful people!', [(54, 'неблагодарные')], ''),
    ('barinov', 'Чьё это резюме лежит на столе?', 'Whose résumé is lying on the table?', [(55, 'Чье это')], ''),
    ('barinov', 'Кто ходил на собеседование к конкурентам?', 'Who went for an interview to the competitors?', [], ''),
    ('max', 'Шеф, мы ничего об этом не знаем.', 'Chef, we know nothing about this.', [], ''),
    ('barinov', 'Почему вы все молчите?', 'Why are you all silent?', [(56, 'Молчите')], ''),
    ('barinov', 'Вы думаете, я ничего не узнаю?', "Do you think I won't find out anything?", [], ''),
    ('max', 'Мы верны нашему ресторану.', 'We are loyal to our restaurant.', [], ''),
    ('barinov', 'Ну что ж, я сам всё выясню!', 'Well then, I will find out everything myself!', [(57, 'Ничтуж')], ''),
    ('barinov', 'Предатель будет немедленно уволен!', 'The traitor will be immediately fired!', [], ''),
    ('max', 'Кажется, шеф в настоящей ярости.', 'It seems the chef is in a real fury.', [], ''),
    ('max', 'Надо быть очень осторожным сегодня.', 'Must be very careful today.', [], ''),
]
WALK = [
    (0, None, [
        "'I will eat my chef's hat!' ",
        ('barinov', 'свой'),
        " translates to one's own, and it replaces the phrase for my when the owner is performing the action. The Russian term for cook's, ",
        ('barinov', 'поварской'),
        ', is built from the action word for cook."'
    ]),
    (1, None, [
        "'None of my people will go to you!' ",
        ('barinov', 'Никто из моих людей не пойдёт'),
        ' literally translates to nobody of my people will not go, and both negatives are needed. The phrase ',
        ('barinov', 'к вам!'),
        ' translates to to you.'
    ]),
    (2, None, [
        "'Then bon appétit to you, Viktor!' Elena throws back the hat line with ",
        ('elena', 'приятного вам аппетита,'),
        ", with the Russian term for 'to you' tucked in the middle."
    ]),
    (3, None, [
        "'Oh you, ungrateful people!' ",
        ('barinov', 'Ах вы,'),
        ' opens a scolding. The Russian expression for ungrateful, ',
        ('barinov', 'неблагодарные'),
        " is built from the Russian expression for 'not' plus a word meaning 'grateful', as in ",
        ('barinov', 'неблагодарные'),
        ', people.',
        ', meaning grateful.'
    ]),
    (4, None, [
        "'Whose résumé is lying on the table?' The phrase for whose, ",
        ('barinov', 'Чьё'),
        ', matches the type of the term for résumé. ',
        ('barinov', 'лежит'),
        ', translates to lies, and is the action word for things lying flat on a table.'
    ]),
    (5, None, [
        "'Who went for an interview to the competitors?' The phrase for went, ",
        ('barinov', 'ходил'),
        ', translates to went and came back. The phrase ',
        ('barinov', 'к конкурентам?'),
        ' puts a different ending on the translation for competitors because of the little word ',
        ('barinov', 'к'),
        '.'
    ]),
    (6, None, [
        "'Chef, we know nothing about this.' The words for nothing and don't know literally translate to nothing we don't know, with both negatives. ",
        ('max', 'об этом'),
        ' uses the phrase for about, ',
        ('max', 'о'),
        ', which grows to ',
        ('max', 'об'),
        ' before a vowel sound.'
    ]),
    (7, None, [
        "'Why are you all silent?' ",
        ('barinov', 'молчите?'),
        ' translates to you are silent, for multiple people. ',
        ('barinov', 'вы все'),
        ' is literally you all.'
    ]),
    (8, None, [
        "'Do you think I won't find out anything?' ",
        ('barinov', 'узнаю?'),
        ", meaning I'll find out, is built from the action word to know. ",
        ('barinov', 'ничего не'),
        ' doubles the negative again.'
    ]),
    (9, None, [
        "'We are loyal to our restaurant.' The expression for faithful, ",
        ('max', 'верны'),
        ', is built from the Russian term for faith at its root. ',
        ('max', 'нашему ресторану.'),
        ' translates to to our restaurant, with matching endings.'
    ]),
    (10, None, [
        "'Well then, I will find out everything myself!' ",
        ('barinov', 'выясню!'),
        " contains the term for clear: literally I'll make it clear. ",
        ('barinov', 'Ну что ж,'),
        ' translates to well then, and ',
        ('barinov', 'сам'),
        ' is the phrase for myself.'
    ]),
    (11, None, [
        "'The traitor will be immediately fired!' The word for traitor, ",
        ('barinov', 'Предатель'),
        ', is built from the action word to betray. ',
        ('barinov', 'немедленно'),
        ' is built from ',
        ('barinov', 'не'),
        ' plus ',
        ('barinov', 'медленно'),
        ', slowly. ',
        ('barinov', 'будет'),
        ' and ',
        ('barinov', 'уволен!'),
        ' translate to will be fired.'
    ]),
    (12, None, [
        "'It seems the chef is in a real fury.' The phrase for it seems, ",
        ('max', 'Кажется,'),
        ', is built from the action word to show, plus an ending that makes it mean it shows itself. ',
        ('max', 'в настоящей ярости.'),
        ' translates to in real fury, with ending changes after ',
        ('max', 'в'),
        '.'
    ]),
    (13, None, [
        "'Must be very careful today.' The Russian expression for must is ",
        ('max', 'Надо'),
        ", which literally translates to it's needed. After ",
        ('max', 'быть'),
        ', be, the describing word for careful takes a special ending.'
    ]),
]
