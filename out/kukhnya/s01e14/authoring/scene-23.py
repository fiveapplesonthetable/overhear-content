# Authoring module for kukhnya-s01e14-scene-23.
ID = 'kukhnya-s01e14-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 23
TITLE = 'Максим молодец  (Maxim Did Great)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'At the bar, Kostya and Nastya have watched the whole drama, and now they gossip about Max and Vika. Hear it in Russian.'
OPENER = 'Their chat again, one line at a time.'
TRANSITION = 'Now the chat from the beginning.'
OUTRO = 'Vika has a plan for saying sorry, and Kostya approves. You can guess what she is pouring. Catch you in the next one.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('kostya', 'Максим молодец.', 'Maxim did great.', [(309, 'Максим молодец')], ''),
    ('kostya', 'Он помог Вике.', 'He helped Vika.', [(309, 'он помог Вике')], ''),
    ('kostya', 'Он спас вечер.', 'He saved the evening.', [], ''),
    ('nastya', 'Да, она наговорила ему гадости.', 'Yeah, she said awful things to him.', [(310, 'Да, она наговорила ему'), (310, 'гадости')], ''),
    ('nastya', 'Всякие гадости.', 'All sorts of awful things.', [(310, 'всякие гадости')], ''),
    ('nastya', 'И ей очень стыдно.', 'And she feels terrible.', [(310, 'очень стыдно')], ''),
    ('kostya', 'И как же она это исправит?', "So how's she going to make it right?", [(311, 'И как же она это исправит')], ''),
    ('kostya', 'Что она будет делать?', 'What will she do?', [], ''),
    ('nastya', 'А, водка.', 'Ah, vodka.', [(312, 'А, водка')], ''),
    ('nastya', 'Она нальёт ему водки.', 'She will pour him vodka.', [], ''),
    ('kostya', 'Это хороший план.', "That's a good plan.", [], ''),
    ('nastya', 'Она знает, что делать.', 'She knows what to do.', [], ''),
]
WALK = [
    (0, None, ["'Maxim did great.' Kostya uses the full name, ", ('kostya', 'Максим'), '. ', ('kostya', 'молодец'), ' comes from the term for young, but it is the everyday well done, and it works for a woman too.']),
    (1, None, ["'He helped Vika.' Helped takes the to form of the person, so Vika becomes ", ('kostya', 'Вике'), '.']),
    (2, None, ["'He saved the evening.' Let's break down the sentence: ", ('kostya', 'спас'), ' is saved. The same root sits in the term for thank you, which grew out of goodness save you.']),
    (3, None, ["'Yeah, she said awful things to him.' Now let's examine the speech: ", ('nastya', 'наговорила'), ' is the verb to talk with a prefix added, so it means she said a whole heap. ', ('nastya', 'ему'), ' is to him, meaning Max.']),
    (4, None, ["'All sorts of awful things.' Nastya just carries on the sentence. ", ('nastya', 'Всякие'), ' means all sorts of. It is usually things you would rather not have said.']),
    (5, None, ["'And she feels terrible.' Let us inspect this part: ", ('nastya', 'ей'), ' is to her, and ', ('nastya', 'стыдно'), ' is ashamed, which is something that happens to a person.']),
    (6, None, ["'So how's she going to make it right?' Let us focus on the dialogue: ", ('kostya', 'исправит'), ' is to put right, from the root for correctly. ', ('kostya', 'же'), ' adds the so of a curious question.']),
    (7, None, ["'What will she do?' We can analyze the dialogue: ", ('kostya', 'будет'), ('kostya', 'делать'), ' means will be doing, which is the future. Kostya asks about the process, not the result.']),
    (8, None, ["'Ah, vodka.' Let's focus on the words: ", ('nastya', 'водка'), ' is water plus a small-and-dear ending, so literally little water.']),
    (9, None, ["'She will pour him vodka.' Vodka becomes ", ('nastya', 'водки'), ', meaning some vodka, which is the of form for an amount of something. ', ('nastya', 'нальёт'), ' means she will pour.']),
    (10, None, ["'That's a good plan.' Plan is masculine, so good has the masculine ending, giving us ", ('kostya', 'хороший'), ('kostya', 'план'), '.']),
    (11, None, ["'She knows what to do.' Now we can focus on the speech: ", ('nastya', 'что'), ('nastya', 'делать'), ' is what to do: the question word, then the basic form of the verb, with no to needed.']),
]
