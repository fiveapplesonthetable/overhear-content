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
    (0, None, '\'Nastya, look at me for one second.\' Kostya asks her to look at him, and Russian gives a length of time an "-u": "one second" becomes "odnu sekundu".'),
    (1, None, '\'What happened, Kostya?\' Nastya asks the standard question, "chto sluchilos\'".'),
    (2, None, '\'You have a really cool hairstyle today.\' "Prikol\'naya" is slang for "cool", from "prikol", a gag. "U tebya" is "at you", the "have" pattern.'),
    (3, None, '\'Really? Do you really like it?\' "Tebe nravitsya" is "to you it pleases". Nastya asks "pravda", truth, twice.'),
    (4, None, '\'Yes, it is so unusual and beautiful.\' "Neobychnaya" is "ne-" plus "obychnaya", usual. The "-aya" endings agree with "prichyoska".'),
    (5, None, '\'You have very sweet, soft curls.\' "Kudri" is "curls", always plural. "Myagkiye" is "soft", plural to match.'),
    (6, None, '\'Thank you, I took a long time doing this styling.\' "Dolgo delala" is "for a long time did", with "-la" for a woman. "Ukladka" is "styling", from "laying" the hair.'),
    (7, None, '\'They are curled like a little lamb\'s.\' "Ovechka" is a little sheep, and Kostya thinks it\'s sweet. "Zakrucheny" is "twisted", plural. "Kak u" is "like on".'),
    (8, None, '\'What did you just say like that?\' "Chto ty takoye skazal" is "what such did you say", a way of showing offense.'),
    (9, None, '\'I meant a fluffy little lamb.\' "Imel v vidu" is literally "had in view", and it means "I meant". "Pushistyy" comes from "pukh", down.'),
    (10, None, '\'You are a foolish sheep yourself, got it?\' "Sam ty" at the start is how Russians throw an insult back: "you yourself". "Ovtsa" is the ordinary sheep, and there\'s no "little" now.'),
    (11, None, '\'Sorry, I just wanted to make a compliment!\' "Izvini" is the friendly "sorry". Russians "make" a compliment, as the English "pay" one.'),
]
