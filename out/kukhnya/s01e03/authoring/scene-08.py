# Authoring module for kukhnya-s01e03-scene-08.
ID = 'kukhnya-s01e03-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = 'Знакомься, это Макс  (Meet Max)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vadim': 'Вадим', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'Max catches Vika outside the dining room and awkwardly tries to agree that they will keep their night together a secret. Vika is not impressed by how he says it, and then her ex-husband Vadim turns up asking questions, so she decides to use Max. Here is the Russian first.'
OPENER = "Let's follow them step by step."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So Max is now a boyfriend, whether he likes it or not. Take away his phrase for "I don\'t care", and notice it has a second life as "anyway".'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Вика, нам нужно спокойно поговорить.', 'Vika, we need to talk calmly.', [], ''),
    ('vika', 'Моя личная жизнь тебя не касается.', 'My personal life is none of your business.', [(199, 'Моя личная жизнь тебя не касается')], ''),
    ('max', 'Давай не будем никому ничего рассказывать.', 'Let us not tell anyone anything.', [(202, 'не надо им об этом рассказывать')], ''),
    ('vika', 'Ты боишься, что я расскажу коллегам?', 'Are you afraid that I will tell colleagues?', [(204, 'Ты боишься, что я расскажу')], ''),
    ('max', 'Я? Нет, мне вообще всё равно.', 'Me? No, I do not care at all.', [(205, 'Я? Да прям')], ''),
    ('max', 'Между нами всё равно ничего серьёзного нет.', 'There is nothing serious between us anyway.', [(207, 'у нас'), (208, 'а так')], ''),
    ('vika', 'Ах вот как ты заговорил!', 'Oh, so that is how you speak now!', [], ''),
    ('vadim', 'Вика, постой! Кто этот молодой человек?', 'Vika, wait! Who is this young man?', [(210, 'ты хотел знать')], ''),
    ('vika', 'Вадим, ты хотел знать правду?', 'Vadim, did you want to know the truth?', [(210, 'Вадим, ты хотел знать')], ''),
    ('vadim', 'Да, я хочу знать всё.', 'Yes, I want to know everything.', [], ''),
    ('vika', 'Вот, познакомься с моим парнем.', 'Here, meet my boyfriend.', [(211, 'Вот, познакомься')], ''),
    ('vika', 'Это мой Макс, мы теперь вместе!', 'This is my Max, we are together now!', [(212, 'Это мой Максик')], ''),
    ('max', 'Очень приятно познакомиться, уважаемый Вадим.', 'Very nice to meet you, esteemed Vadim.', [], ''),
]
WALK = [
    (0, None, [
        "'Vika, we need to talk calmly.' In Russian, ",
        ('max', 'нам нужно'),
        ' translates to "to us necessary". ',
        ('max', 'спокойно'),
        ' literally means "calmly".'
    ]),
    (1, None, [
        '\'My personal life is none of your business.\' The phrase for "personal life" is ',
        ('vika', 'Моя личная жизнь'),
        ' And ',
        ('vika', 'тебя не касается.'),
        ' literally translates to "does not touch you", a handy way to say "none of your business".'
    ]),
    (2, None, [
        '\'Let us not tell anyone anything.\' The phrase for "let\'s not" is ',
        ('max', 'Давай не будем'),
        ' Then come ',
        ('max', 'никому'),
        ' to nobody, and ',
        ('max', 'ничего'),
        ' nothing, stacking the no-words.'
    ]),
    (3, None, [
        '\'Are you afraid that I will tell colleagues?\' The word for "afraid" is ',
        ('vika', 'боишься,'),
        ' which ends with a sound showing something happening to yourself. ',
        ('vika', 'коллегам?'),
        ' translates to "to colleagues", with a sound at the end for the "to" direction.'
    ]),
    (4, None, [
        "'Me? No, I do not care at all.' The classic shrug here is ",
        ('max', 'мне вообще всё равно.'),
        ' which literally translates to "to me all is equal". He slips ',
        ('max', 'вообще'),
        ' into the middle to push it to "I couldn\'t care less".'
    ]),
    (5, None, [
        '\'There is nothing serious between us anyway.\' Here the phrase for "anyway" is ',
        ('max', 'всё равно'),
        ('max', 'Между нами'),
        ' translates to "between us", and ',
        ('max', 'ничего серьёзного нет.'),
        ' literally means "nothing serious there isn\'t".'
    ]),
    (6, None, [
        '\'Oh, so that is how you speak now!\' The word for "started speaking" is ',
        ('vika', 'заговорил!'),
        ' built from an action word for speaking plus a start sound. ',
        ('vika', 'Ах вот как'),
        ' translates to "ah, so that\'s how".'
    ]),
    (7, None, [
        '\'Vika, wait! Who is this young man?\' The word for "wait" is ',
        ('vadim', 'постой!'),
        ' which literally means "stand a moment". ',
        ('vadim', 'молодой человек?'),
        ' translates to "young man", the standard way to refer to a young stranger.'
    ]),
    (8, None, [
        "'Vadim, did you want to know the truth?' Vika says ",
        ('vika', 'ты'),
        ' to her ex-husband to show they are close. ',
        ('vika', 'хотел'),
        ' translates to "wanted", with an ending showing it is about a man, and ',
        ('vika', 'правду?'),
        ' is the word for "truth".'
    ]),
    (9, None, [
        "'Yes, I want to know everything.' Short and handy: ",
        ('vadim', 'хочу'),
        ' plus ',
        ('vadim', 'знать'),
        ' the word for "to know", then ',
        ('vadim', 'всё.'),
        ' everything. Careful with the final sound, as changing it gives the word for "everyone".'
    ]),
    (10, None, [
        '\'Here, meet my boyfriend.\' The action word for "meet" is ',
        ('vika', 'познакомься'),
        ' with an ending showing it happens to yourself. Then comes ',
        ('vika', 'с моим парнем.'),
        ' translating to "with my boyfriend", where the ends of the words change to match the "with" direction.'
    ]),
    (11, None, [
        "'This is my Max, we are together now!' Two little parts with no action word at all: ",
        ('vika', 'Это мой Макс,'),
        ' this my Max, and ',
        ('vika', 'мы теперь вместе!'),
        ' we now together. Do not mix up the word for "we" with the word for "my".'
    ]),
    (12, None, [
        "'Very nice to meet you, esteemed Vadim.' Check out how ",
        ('max', 'Очень приятно познакомиться,'),
        ' literally means "very pleasant to get acquainted". ',
        ('max', 'уважаемый'),
        ' translates to "esteemed" or "respected", and it sounds stiff here.'
    ]),
]
