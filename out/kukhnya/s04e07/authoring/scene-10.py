# Authoring module for kukhnya-s04e07-scene-10.
ID = 'kukhnya-s04e07-scene-10'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 7
SCENE = 10
TITLE = "Победа Баринова  (Barinov's Victory)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.07'
SOURCE_FILE = 'sources/kukhnya/s04/e07.ru.srt'
INTRO = 'In the dining room, Gavril Ilyich tastes the first course prepared by German Land. After a single bite, the guest frowns, asks whether Viktor Barinov really cooked this dish, and threatens to celebrate the banquet elsewhere—handing Barinov a triumphant victory in the bet!'
OPENER = "Let's examine how Barinov wins the culinary bet line by line."
TRANSITION = "Now let's listen to the tasting and bet-victory scene again."
OUTRO = 'Having proven his culinary mastery over German, Barinov pauses to collect the first installment of his payment from Dmitry Nagiyev. See you next time!'
CLOSING = ('guest', 'До свидания!')
STORY = [
    ('nagiyev', 'Приятного вам аппетита, уважаемый Гавриил Ильич!', 'Enjoy your meal, respected Gavriil Ilyich!', [(162, 'Пятного аппетита.')], 'adapted'),
    ('guest', 'Благодарю вас, сейчас с удовольствием попробую.', 'I thank you, I will taste it with pleasure right now.', [(162, 'Благодарю.')], 'adapted'),
    ('guest', 'Скажите, это блюдо точно готовил Баринов?', 'Tell me, did Barinov definitely cook this dish?', [(163, 'Это точно баринов готовил?')], 'adapted'),
    ('guest', 'Знаете, мы лучше отпразднуем в другом месте.', 'You know, we would rather celebrate in another place.', [(164, 'мы, наверное, все-таки в другом месте отпраздновали.')], 'adapted'),
    ('nagiyev', 'Умоляю вас, это просто маленькое недоразумение!', 'I beg you, this is just a small misunderstanding!', [(165, 'Умоляю. Это какое-то, видимо, недоразумение.')], 'adapted'),
    ('nagiyev', 'Сейчас мы всё очень быстро исправим!', 'Right now we will fix everything very quickly!', [(166, 'Сейчас мы его решим.')], 'adapted'),
    ('nagiyev', 'Вам подадут блюдо лично от Виктора Баринова.', 'They will serve you a dish personally from Viktor Barinov.', [(168, 'подадут блюдо прямо от баринова')], 'adapted'),
    ('nagiyev', 'Я сам лично за этим строго прослежу!', 'I will personally oversee this strictly myself!', [(168, 'я лично за этим прослежу')], 'adapted'),
    ('barinov', 'Ну что, господин всезнайка, режь помидоры с яйцом!', 'Well then, Mister Know-It-All, chop the tomatoes and egg!', [(169, 'мистер'), (170, 'я знаю все секреты помидоры с яйцом')], 'adapted'),
    ('barinov', 'Судя по всему, наш спор выиграл я!', 'Judging by everything, I am the one who won our bet!', [(172, 'сбор выиграл'), (173, 'я выиграл и выиграл')], 'adapted'),
    ('barinov', 'Так что быстро надевай фартук и работай!', 'So put on an apron quickly and get to work!', [(175, 'сейчас работа')], 'adapted'),
    ('nagiyev', 'Витя, иди скорее на кухню спасать банкет!', 'Vitya, go to the kitchen quickly to save the banquet!', [], 'new'),
]
WALK = [
    (0, None, '\'Enjoy your meal, respected Gavriil Ilyich!\' Discussing the appetite around the guest, Nagiyev leans on "uvazhayemyy" ("respected, esteemed") to give the whole sentence its punch.'),
    (1, None, "'I thank you, I will taste it with pleasure right now.' The guest chimes in boldly with a sigh, bringing things back to earth after the buildup."),
    (2, None, "'Tell me, did Barinov definitely cook this dish?' The guest checks evenly what Nagiyev is actually getting at here."),
    (3, None, '\'You know, we would rather celebrate in another place.\' Pointing to the place in the exchange, the guest uses "otprazdnuyem" ("to celebrate", from "otprazdnovat") to make the point stick.'),
    (4, None, '\'I beg you, this is just a small misunderstanding!\' Checking on a small misunderstanding around the guest, Nagiyev uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (5, None, "'Right now we will fix everything very quickly!' Nagiyev counters frankly with a shrug, keeping the focus on what actually matters here."),
    (6, None, '\'They will serve you a dish personally from Viktor Barinov.\' Touching on a dish in front of Barinov, Nagiyev uses "blyudo" ("dish") to carry the main weight of the thought.'),
    (7, None, '\'I will personally oversee this strictly myself!\' Nagiyev chimes in dryly on the spot and lands on "proslezhu" ("to see to it", built on "prosledit") to keep the statement grounded.'),
    (8, None, "'Well then, Mister Know-It-All, chop the tomatoes and egg!' Barinov cuts in candidly around Nagiyev, to clear the air between them once and for all."),
    (9, None, '\'Judging by everything, I am the one who won our bet!\' Pointing to the judging at once, Barinov chooses "sudya" ("judging") so Nagiyev gets the point right away.'),
    (10, None, '\'So put on an apron quickly and get to work!\' Emphasizing an apron to Nagiyev, Barinov leans on "fartuk" ("apron") to give the whole sentence its punch.'),
    (11, None, "'Vitya, go to the kitchen quickly to save the banquet!' Nagiyev pushes back frankly facing Barinov, without trying to dress up how he really feels."),
]
