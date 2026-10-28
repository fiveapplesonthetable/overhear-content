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
OUTRO = 'So Max is now a boyfriend, whether he likes it or not. Take away "mne vsyo ravno", "I don\'t care", and notice it has a second life as "anyway".'
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
    (0, None, '\'Vika, we need to talk calmly.\' The pattern is "to us necessary", and "calmly" grows out of "calm", a relative of "good night".'),
    (1, None, '\'My personal life is none of your business.\' Vika says "does not touch you", which is the Russian idea of "none of your business". "Personal" is borrowed enough to follow.'),
    (2, None, '\'Let us not tell anyone anything.\' A stack of negatives once more: "let\'s not", "to nobody" and "nothing". The first word is the friendly "let\'s".'),
    (3, None, '\'Are you afraid that I will tell colleagues?\' "Are you afraid" has a "-sya" at the end, a little "self". "Colleagues" ends in "-am", the "to" ending.'),
    (4, None, '\'Me? No, I do not care at all.\' "Mne vsyo ravno" is literally "to me everything is equal", and it\'s how Russians say "I don\'t care". It\'s worth learning whole.'),
    (5, None, '\'There is nothing serious between us anyway.\' The same "vsyo ravno" turns up with the meaning "anyway" or "all the same". "Between us" and "nothing serious isn\'t" are the other two chunks.'),
    (6, None, '\'Oh, so that is how you speak now!\' "Started speaking" has a prefix meaning "begin", so it\'s "you\'ve started talking like that". Vika is hurt.'),
    (7, None, '\'Vika, wait! Who is this young man?\' "Wait" has "stand" inside it, so it means "stand a moment". "Young man" is the usual polite way to point at a young man.'),
    (8, None, '\'Vadim, did you want to know the truth?\' She speaks to him with the friendly "you". "Wanted" has a man\'s "-l" ending, and "truth" doubles as "really?".'),
    (9, None, '\'Yes, I want to know everything.\' Short and demanding, with "I want" and "everything" as the only pieces. Vadim doesn\'t waste words.'),
    (10, None, '\'Here, meet my boyfriend.\' The same word means "guy" and "boyfriend", so context does the work. "Meet" is a command with "self" on the end, and "with my boyfriend" takes the "with" endings.'),
    (11, None, '\'This is my Max, we are together now!\' "My Max" is how Russians show affection or ownership. "We together" is all you need to say you\'re a couple.'),
    (12, None, '\'Very nice to meet you, esteemed Vadim.\' This is the formal "pleased to meet you", with "pleasant" at the heart of it. "Esteemed" is "respect" stretched into a describing word, so it sounds stiff, and Max is making fun.'),
]
