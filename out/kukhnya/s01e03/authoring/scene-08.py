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
INTRO = 'Outside the dining hall, Max attempts an awkward conversation with art director Victoria about keeping their private encounter secret. Irritated by his clumsy assumptions, Victoria uses him to ward off her persistent ex-husband Vadim by introducing Max as her new boyfriend. Listen to the dialogue in Russian first.'
OPENER = "Let's review this awkward hallway confrontation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Trapped in a spontaneous romance of convenience, Max and Victoria must now play the part in front of Vadim. See you next time!'
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
    (0, None, "'Vika, we need to talk calmly.' Max awkwardly tries to initiate a conversation about keeping their secret."),
    (1, None, "'My personal life is none of your business.' Vika sharply tells him to stay out of her private affairs."),
    (2, None, "'Let us not tell anyone anything.' Max clumsily initiates a conversation about keeping their secret."),
    (3, None, "'Are you afraid that I will tell colleagues?' Victoria is offended because she misunderstands his caution."),
    (4, None, "'Me? No, I do not care at all.' Max denies caring about what their coworkers might think."),
    (5, None, "'There is nothing serious between us anyway.' Attempting to minimize their relationship is a clumsy way to de-escalate the situation."),
    (6, None, "'Oh, so that is how you speak now!' Victoria misinterprets his words and takes offense."),
    (7, None, "'Vika, wait! Who is this young man?' Vadim interrupts the argument, demanding to know the identity of the young cook."),
    (8, None, "'Vadim, did you want to know the truth?' Challenging the older man directly requires an offer of full honesty."),
    (9, None, "'Yes, I want to know everything.' Stubborn insistence on hearing the unfiltered facts pushes the confrontation forward."),
    (10, None, "'Here, meet my boyfriend.' Sarcastic introductions finally reveal the new romantic partner."),
    (11, None, "'This is my Max, we are together now!' Vika proudly declares their relationship status just to spite the older man."),
    (12, None, "'Very nice to meet you, esteemed Vadim.' Max tries to salvage the disastrous situation with excessive, terrified politeness."),
]
