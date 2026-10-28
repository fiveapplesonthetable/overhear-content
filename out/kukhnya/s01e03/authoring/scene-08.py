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
    (0, None, '\'Vika, we need to talk calmly.\' "Nam nuzhno" is "to us necessary". "Spokoyno", calmly, is from "spokoynyy", calm, the word in "spokoynoy nochi", good night.'),
    (1, None, '\'My personal life is none of your business.\' "Tebya ne kasayetsya" is "does not touch you", the Russian "none of your business". "Lichnaya zhizn\'" is "personal life".'),
    (2, None, '\'Let us not tell anyone anything.\' "Davay ne budem" is "let\'s not". Then come "nikomu", to nobody, and "nichego", nothing, stacking the negatives.'),
    (3, None, '\'Are you afraid that I will tell colleagues?\' "Boish\'sya", you\'re afraid, ends in -sya. "Kollegam" is "to colleagues", with the -am plural for "to".'),
    (4, None, '\'Me? No, I do not care at all.\' "Mne vsyo ravno" is "to me all is equal", the Russian for "I don\'t care". "Voobshche" adds "at all".'),
    (5, None, '\'There is nothing serious between us anyway.\' Here "vsyo ravno" means "anyway". "Mezhdu nami" is "between us", and "nichego ser\'yoznogo net" is "nothing serious there isn\'t".'),
    (6, None, '\'Oh, so that is how you speak now!\' "Zagovoril" is "govoril", spoke, with "za-", which here means "started". "Ah vot kak" is "ah, so that\'s how".'),
    (7, None, '\'Vika, wait! Who is this young man?\' "Postoy" is "stand a moment", from "stoyat\'", to stand. "Molodoy chelovek", young man, is the standard way to refer to a young stranger.'),
    (8, None, '\'Vadim, did you want to know the truth?\' Vika says "ty" to her ex-husband. "Khotel", wanted, ends in -l for a man, and "pravda" is "truth".'),
    (9, None, '\'Yes, I want to know everything.\' "Khochu znat\'" is "I want to know", and "vsyo" is "everything".'),
    (10, None, '\'Here, meet my boyfriend.\' "Paren\'" means both "guy" and "boyfriend". "Poznakom\'sya", meet, ends in -sya, and "s moim parnem", with my boyfriend, ends in -im and -em after "s".'),
    (11, None, '\'This is my Max, we are together now!\' "Moy Maks" is "my Max". "My teper\' vmeste" is "we now together", with no verb at all.'),
    (12, None, '\'Very nice to meet you, esteemed Vadim.\' "Ochen\' priyatno poznakomit\'sya" is "very pleasant to get acquainted". "Uvazhayemyy", esteemed, means "respected", and it sounds stiff here.'),
]
