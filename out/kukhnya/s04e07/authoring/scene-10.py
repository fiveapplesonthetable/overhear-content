ID = 'kukhnya-s04e07-scene-10'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 7
SCENE = 10
TITLE = "Победа Баринова  (Barinov's Victory)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "guest": "anja", "nagiyev": "angelina"}
LABELS = {"guest": "Гость", "nagiyev": "Нагиев"}
SOURCE_NAME = 'Кухня (Kukhnya) S4.07'
SOURCE_FILE = 'sources/kukhnya/s04/e07.ru.srt'

INTRO = 'In the dining room, Gavril Ilyich tastes the first course prepared by German Land. After a single bite, the guest frowns, asks whether Viktor Barinov really cooked this dish, and threatens to celebrate the banquet elsewhere—handing Barinov a triumphant victory in the bet!'

STORY = [
    ('nagiyev', 'Приятного вам аппетита, уважаемый Гавриил Ильич!', 'Enjoy your meal, respected Gavriil Ilyich!', [(162, 'Пятного аппетита.')], 'adapted'),
    ('guest', 'Благодарю вас, сейчас с удовольствием попробую.', 'I thank you, I will taste it with pleasure right now.', [(162, 'Благодарю.')], 'adapted'),
    ('guest', 'Скажите, это блюдо точно готовил Баринов?', 'Tell me, did Barinov definitely cook this dish?', [(163, 'Это точно баринов готовил?')], 'adapted'),
    ('guest', 'Знаете, мы лучше отпразднуем в другом месте.', 'You know, we would rather celebrate in another place.', [(164, 'мы, наверное, все-таки в другом месте отпраздновали.')], 'adapted'),
    ('nagiyev', 'Умоляю вас, это просто маленькое недоразумение!', 'I beg you, this is just a small misunderstanding!', [(165, 'Умоляю. Это какое-то, видимо, недоразумение.')], 'adapted'),
    ('nagiyev', 'Сейчас мы всё очень быстро исправим!', 'Right now we will fix everything very quickly!', [(166, 'Сейчас мы его решим.')], 'adapted'),
    ('nagiyev', 'Вам подадут блюдо лично от Виктора Баринова.', 'They will serve you a dish personally from Viktor Barinov.', [(168, 'подадут блюдо прямо от баринова')], 'adapted'),
    ('nagiyev', 'Я сам лично за этим строго прослежу!', 'I will personally oversee this strictly myself!', [(168, 'я лично за этим прослежу')], 'adapted'),
    ('guest', 'Ну что, господин всезнайка, режь помидоры с яйцом!', 'Well then, Mister Know-It-All, chop the tomatoes and egg!', [(169, 'мистер'), (170, 'я знаю все секреты помидоры с яйцом')], 'adapted'),
    ('guest', 'Судя по всему, наш спор выиграл я!', 'Judging by everything, I am the one who won our bet!', [(172, 'сбор выиграл'), (173, 'я выиграл и выиграл')], 'adapted'),
    ('guest', 'Так что быстро надевай фартук и работай!', 'So put on an apron quickly and get to work!', [(175, 'сейчас работа')], 'adapted'),
    ('nagiyev', 'Витя, иди скорее на кухню спасать банкет!', 'Vitya, go to the kitchen quickly to save the banquet!', [], 'new'),
]

OPENER = "Let's examine how Barinov wins the culinary bet line by line."

WALK = [
    (0, None, "'Enjoy your meal, respected Gavriil Ilyich!' Here Nagiyev anchors the thought on 'pleasant' and finishes on 'ilyich', keeping the spoken rhythm brisk and natural."),
    (1, None, "'I thank you, I will taste it with pleasure right now.' Formal first-person verb 'I thank' elevates the register."),
    (2, None, "'Tell me, did Barinov definitely cook this dish?' One spoonful is enough for the connoisseur to spot the difference."),
    (3, None, "'You know, we would rather celebrate in another place.' Notice how Russian puts 'know' and 'place' together in a short, direct phrase where word endings show how the ideas connect."),
    (4, None, "'I beg you, this is just a small misunderstanding!' Nagiyev scrambles to keep the lucrative banquet from walking out."),
    (5, None, "'Right now we will fix everything very quickly!' In everyday Russian, 'right now' flows straight into 'will fix' without extra linking words."),
    (6, None, "'They will serve you a dish personally from Viktor Barinov.' Impersonal third-person plural future represents the restaurant service."),
    (7, None, "'I will personally oversee this strictly myself!' Notice how Russian puts 'personally' and 'to see to it, to keep an eye on' together in a short, direct phrase where word endings show how the ideas connect."),
    (8, None, "'Well then, Mister Know-It-All, chop the tomatoes and egg!' Back in the kitchen, Barinov puts German on basic prep duty."),
    (9, None, "'Judging by everything, I am the one who won our bet!' In everyday Russian, 'judging' flows straight into 'won' without extra linking words."),
    (10, None, "'So put on an apron quickly and get to work!' Singular imperatives assert Barinov's total victory."),
    (11, None, "'Vitya, go to the kitchen quickly to save the banquet!' Before cooking, however, Barinov insists on collecting his first kick from Nagiyev."),
]

TRANSITION = "Now let's listen to the tasting and bet-victory scene again."
OUTRO = 'Having proven his culinary mastery over German, Barinov pauses to collect the first installment of his payment from Dmitry Nagiyev. See you next time!'
CLOSING = ("guest", "До свидания!")
