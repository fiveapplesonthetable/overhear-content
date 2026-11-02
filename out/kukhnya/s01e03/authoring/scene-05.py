# Authoring module for kukhnya-s01e03-scene-05.
ID = 'kukhnya-s01e03-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 5
TITLE = 'Паника на кухне  (Panic in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "Max rushes into the kitchen in a panic. A prosecutor, Vika's ex-husband, is after him, and he tells the chef. Barinov has little sympathy, and starts speaking about Max as though he were already dead. This is the Russian first."
OPENER = "Now let's go over the chef's joke."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'The chef sends Max back to work, which is the best advice a cynic can give. You\'ve learned the phrase for "you don\'t joke with a prosecutor".'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Шеф, у меня большие проблемы.', 'Chef, I have big problems.', [], ''),
    ('barinov', 'Что опять стряслось, огузок?', 'What happened again, Oguzok?', [], ''),
    ('max', 'Меня ищет грозный прокурор.', 'A terrible prosecutor is looking for me.', [], ''),
    ('barinov', 'И за что же он тебя ищет?', 'And why is he looking for you?', [], ''),
    ('max', 'Он знает про меня и Вику.', 'He knows about me and Vika.', [], ''),
    ('barinov', 'Ты спал с чужой женщиной?', "You slept with someone else's woman?", [(162, 'спал с чужой')], ''),
    ('max', 'Я не знал, что она замужем.', 'I did not know that she is married.', [], ''),
    ('barinov', 'Это был самый талантливый повар.', 'He was the most talented cook.', [(161, 'Это был самый талантливый')], ''),
    ('barinov', 'Которого я когда-либо знал.', 'Whom I ever knew.', [(161, 'которого я знал')], ''),
    ('max', 'Шеф, вы меня уже хороните?', 'Chef, are you already burying me?', [], ''),
    ('barinov', 'С прокурором шутки плохи.', "You don't mess with a prosecutor.", [], ''),
    ('barinov', 'Он тебя быстро за решётку отправит.', 'He will quickly send you behind bars.', [], ''),
    ('max', 'Что же мне теперь делать?', 'What should I do now?', [], ''),
    ('barinov', 'Иди работай и не болтай.', 'Go work and do not chat.', [], ''),
]
WALK = [
    (0, None, [
        "'Chef, I have big problems.' Let us review ",
        ('max', 'у меня'),
        ", literally 'at me', translates to 'I have'. ",
        ('max', 'большие проблемы.'),
        ' puts the shape for more than one on both words.'
    ]),
    (1, None, [
        "'What happened again, Oguzok?' Take note of ",
        ('barinov', 'стряслось,'),
        " translates to a casual 'happened', kept for unpleasant surprises. The word for 'again' is ",
        ('barinov', 'опять'),
        ', and the chef uses his nickname for Max.'
    ]),
    (2, None, [
        "'A terrible prosecutor is looking for me.' Observe how ",
        ('max', 'Меня ищет'),
        " puts 'me' first, then the action word 'looks for'. ",
        ('max', 'грозный'),
        " is the word for the tsar's title that English translates to 'the Terrible', and it means fearsome."
    ]),
    (3, None, [
        "'And why is he looking for you?' Observe how ",
        ('barinov', 'за что'),
        " literally means 'for what', the 'why' you ask about a punishment. ",
        ('barinov', 'же'),
        ' sharpens the question.'
    ]),
    (4, None, [
        "'He knows about me and Vika.' What happens here, ",
        ('max', 'про'),
        " is the spoken word for 'about'. After it, the name Vika changes its ending to ",
        ('max', 'Вику.'),
        " and 'I' changes to ",
        ('max', 'меня'),
        '.'
    ]),
    (5, None, [
        "'You slept with someone else's woman?' ",
        ('barinov', 'спал с'),
        " translates to 'slept with', and after the word for 'with', the next words change their endings: ",
        ('barinov', 'чужой женщиной?'),
        ' The word ',
        ('barinov', 'чужой'),
        " translates to 'someone else's'."
    ]),
    (6, None, [
        "'I did not know that she is married.' The word for a married woman is ",
        ('max', 'замужем.'),
        " It is literally built from words meaning 'behind a husband'."
    ]),
    (7, None, [
        "'He was the most talented cook.' We can hear ",
        ('barinov', 'Это был'),
        " translates to 'this was', and the chef talks about Max as a memory. ",
        ('barinov', 'самый талантливый'),
        " is the phrase for 'the most talented'."
    ]),
    (8, None, [
        "'Whom I ever knew.' Let us check ",
        ('barinov', 'Которого'),
        " is the word for 'whom', in a special shape for the target of an action. The word ",
        ('barinov', 'когда-либо'),
        " translates to 'ever', and is built from the word for 'when'."
    ]),
    (9, None, [
        "'Chef, are you already burying me?' Max says ",
        ('max', 'вы'),
        " as a respectful 'you' to the chef. ",
        ('max', 'хороните?'),
        " translates to 'you bury', and ",
        ('max', 'уже'),
        " is the word for 'already'."
    ]),
    (10, None, [
        "'You don't mess with a prosecutor.' ",
        ('barinov', 'С прокурором шутки плохи.'),
        " literally translates to 'with a prosecutor jokes are bad'. It's a fixed phrase, and the word for 'prosecutor' can be swapped for anyone dangerous."
    ]),
    (11, None, [
        "'He will quickly send you behind bars.' Focusing here, ",
        ('barinov', 'за решётку'),
        " literally translates to 'behind the grille', which means prison. ",
        ('barinov', 'отправит.'),
        " is the action word for 'will send'."
    ]),
    (12, None, [
        "'What should I do now?' Observe how ",
        ('max', 'Что же мне теперь делать?'),
        " literally translates to 'what to me to do?', the pattern for asking advice. The word for 'now' is ",
        ('max', 'теперь'),
        ', and ',
        ('max', 'же'),
        ' adds a sense of despair.'
    ]),
    (13, None, [
        "'Go work and do not chat.' In this sentence, ",
        ('barinov', 'Иди работай'),
        " puts two commands side by side, 'go' and 'work'. ",
        ('barinov', 'не болтай.'),
        " translates to 'do not chatter'."
    ]),
]
