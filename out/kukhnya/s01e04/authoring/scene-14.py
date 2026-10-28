# Authoring module for kukhnya-s01e04-scene-14.
ID = 'kukhnya-s01e04-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 14
TITLE = 'Кудрявая причёска  (The Curly Hairstyle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Kostya has been working up the courage to pay Nastya a compliment about her new curls, and he gets it terribly wrong. He compares her hair to a little sheep, and she does not take it well. Here's the Russian first."
OPENER = "Let's see how the compliment falls apart."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Kostya\'s compliment was meant kindly, but a sheep is a sheep. Notice "sam ty", the Russian way to throw an insult back.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Настя, посмотри на меня одну секунду.', 'Nastya, look at me for one second.', [(173, 'Настя')], ''),
    ('nastya', 'Что случилось, Костя?', 'What happened, Kostya?', [(173, 'Что')], ''),
    ('kostya', 'У тебя сегодня очень прикольная причёска.', 'You have a really cool hairstyle today.', [(174, 'У тебя прическа сегодня очень прикольная')], ''),
    ('nastya', 'Правда? Тебе правда нравится?', 'Really? Do you really like it?', [(174, 'прическа')], ''),
    ('kostya', 'Да, она такая необычная и красивая.', 'Yes, it is so unusual and beautiful.', [(175, 'Очень прикольная')], ''),
    ('kostya', 'У тебя очень милые мягкие кудри.', 'You have very sweet, soft curls.', [(175, 'такая вся')], ''),
    ('nastya', 'Спасибо, я долго делала эту укладку.', 'Thank you, I took a long time doing this styling.', [(175, 'прикольная')], ''),
    ('kostya', 'Они закручены, как у маленькой овечки.', "They are curled like a little lamb's.", [(177, 'Как у овечки')], ''),
    ('nastya', 'Что ты сейчас такое сказал?', 'What did you just say like that?', [(178, 'Сам ты')], ''),
    ('kostya', 'Я имел в виду пушистую овечку.', 'I meant a fluffy little lamb.', [(177, 'Как у овечки')], ''),
    ('nastya', 'Сам ты глупая овца, понял?', 'You are a foolish sheep yourself, got it?', [(178, 'Сам ты овца')], ''),
    ('kostya', 'Извини, я просто хотел сделать комплимент!', 'Sorry, I just wanted to make a compliment!', [(178, 'овца')], ''),
]
WALK = [
    (0, None, '\'Nastya, look at me for one second.\' "Posmotri na menya" is "look at me". A length of time takes -u: "odnu sekundu".'),
    (1, None, '\'What happened, Kostya?\' "Chto sluchilos\'?" is "what has happened?". "Sluchilos\'" shares a root with "sluchay", an event.'),
    (2, None, '\'You have a really cool hairstyle today.\' "Prikol\'naya" is slang for "cool", from "prikol", a gag. "U tebya" is the "have" pattern.'),
    (3, None, '\'Really? Do you really like it?\' "Pravda", truth, is used here for "really?", twice. "Tebe nravitsya" is "to you it\'s pleasing".'),
    (4, None, '\'Yes, it is so unusual and beautiful.\' "Neobychnaya" is "ne-" plus "obychnaya", usual. The -aya endings match "prichyoska".'),
    (5, None, '\'You have very sweet, soft curls.\' "Kudri", curls, is a plural word. "Milyye myagkiye" both carry plural -ye.'),
    (6, None, '\'Thank you, I took a long time doing this styling.\' "Dolgo delala" is "long did", with -la for a woman. "Ukladka", styling, is from "ukladyvat\'", to lay in place.'),
    (7, None, '\'They are curled like a little lamb\'s.\' "Zakrucheny", twisted, is plural. "Kak u ovechki" is "as at a little sheep", and "ovechka" is a pet form of "ovtsa".'),
    (8, None, '\'What did you just say like that?\' "Chto ty takoye skazal?" is "what such did you say?", a question that signals offence.'),
    (9, None, '\'I meant a fluffy little lamb.\' "Imel v vidu" is "had in view", Russian for "meant". "Pushistyy", fluffy, comes from "pukh", down.'),
    (10, None, '\'You are a foolish sheep yourself, got it?\' "Sam ty" throws an insult back: "you yourself are". "Ovtsa" is the plain sheep, without the pet ending.'),
    (11, None, '\'Sorry, I just wanted to make a compliment!\' "Izvini" is the familiar "sorry". Russians "make" a compliment, "sdelat\' kompliment", where English pays one.'),
]
