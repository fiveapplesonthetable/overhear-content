# Authoring module for kukhnya-s01e13-scene-13.
ID = 'kukhnya-s01e13-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 13
TITLE = 'Признание перед шефом  (Confession Before the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Kostya has told the boss he broke the mirror, but Nastya won't let him take the blame. Both of them are standing in front of Barinov. Here is what they say, in Russian first."
OPENER = 'Now the confession again, with time to look at each line.'
TRANSITION = 'Now the confession from the beginning.'
OUTRO = "Barinov lets them off, and Kostya says yes to the invitation. Two new expressions worth keeping are 'both' and 'on a visit'. Talk soon."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Шеф, это я сломал зеркало машины.', 'Chef, I broke your car mirror.', [(175, 'Шеф, это я сломал ваше зеркало.')], ''),
    ('nastya', 'Шеф, совсем не верьте ему!', 'Chef, do not believe him at all!', [(176, 'Нет, не верьте ему.')], ''),
    ('nastya', 'Это я сама сломала зеркало!', 'I broke your side mirror myself!', [(177, 'Это я сломала ваше зеркало.')], ''),
    ('barinov', 'Вы оба сломали моё зеркало?', 'Did you both break my mirror together?', [], ''),
    ('nastya', 'Я ехала на велосипеде и задела.', 'I was riding a bicycle and grazed it.', [(181, 'Я ехала на велосипеде, и случайно ваше зеркало сломала.')], ''),
    ('kostya', 'Я просто хотел защитить Настю, шеф.', 'I was simply trying to protect Nastya, chef.', [(178, 'А он просто хочет меня прикрыть.')], ''),
    ('nastya', 'Шеф, простите нас обоих, пожалуйста!', 'Chef, please forgive both of us!', [(182, 'Шеф, простите меня, пожалуйста.')], ''),
    ('barinov', 'Я два дня ругался с соседкой!', 'I was fighting with the neighbor for two days!', [(184, 'А я с ней уже дня два воины.')], ''),
    ('barinov', 'Идите работать, вы оба настоящие инвалиды!', 'Go back to work, you clumsy people!', [(183, 'Вот вы инвалиды.')], ''),
    ('kostya', 'Настя, спасибо, ты поступила очень смело.', 'Nastya, thank you, you acted very bravely.', [(174, 'настя')], ''),
    ('nastya', 'И ты меня красиво защитил, Костя.', 'And you protected me so nicely, Kostya.', [(178, 'меня')], ''),
    ('nastya', 'Может, ты сегодня придёшь в гости?', 'Maybe you will come visit me tonight?', [], ''),
    ('kostya', 'С огромным удовольствием приду к тебе!', 'I will gladly come visit you tonight!', [], ''),
]
WALK = [
    (0, None, ["'Chef, I broke your car mirror.' Let us break down the words: ", ('kostya', 'зеркало'), ('kostya', 'машины'), " is 'the car mirror', and the term for car takes a different ending when it means 'of the car'. Kostya's verb ", ('kostya', 'сломал'), " ends in a man's past form."]),
    (1, None, ["'Chef, do not believe him at all!' In Russian you believe 'to' a person, so 'him' changes shape to ", ('nastya', 'ему'), '. Notice ', ('nastya', 'совсем'), ', meaning at all, makes the order stronger.']),
    (2, None, ["'I broke your side mirror myself!' Let us look at the words: ", ('nastya', 'сама'), " is 'myself', in a woman's form. Nastya adds it so that nobody can doubt it was her."]),
    (3, None, ["'Did you both break my mirror together?' Let us inspect the dialogue: ", ('barinov', 'оба'), " is 'both', and with it the plural ", ('barinov', 'Вы'), " clearly means 'you two'. The verb ", ('barinov', 'сломали'), ' has the plural ending.']),
    (4, None, ["'I was riding a bicycle and grazed it.' The verb ", ('nastya', 'ехала'), " means 'was riding', with a woman's ending. We hear ", ('nastya', 'на'), ('nastya', 'велосипеде'), " is 'on a bicycle', and ", ('nastya', 'задела'), " is 'brushed against'."]),
    (5, None, ["'I was simply trying to protect Nastya, chef.' The verb ", ('kostya', 'защитить'), " is 'to protect'. The name ", ('kostya', 'Настю'), ' changes its ending because she is the one protected.']),
    (6, None, ["'Chef, please forgive both of us!' The expression ", ('nastya', 'нас'), ('nastya', 'обоих'), " is 'we both' in the form for the people being forgiven. The verb ", ('nastya', 'простите'), " echoes the term Russians use for 'excuse me'."]),
    (7, None, ["'I was fighting with the neighbor for two days!' After 'two', the term for day becomes ", ('barinov', 'дня'), '. A woman neighbor is ', ('barinov', 'соседкой'), ', and ', ('barinov', 'с'), ('barinov', 'соседкой'), " is 'with the neighbor'."]),
    (8, None, ["'Go back to work, you clumsy people!' The term ", ('barinov', 'инвалиды'), " literally means 'disabled people', and here it is a rude way of calling them hopeless. The expression ", ('barinov', 'Идите'), ('barinov', 'работать'), ' is the plural order plus the plain verb.']),
    (9, None, ["'Nastya, thank you, you acted very bravely.' The term ", ('kostya', 'смело'), " is 'bravely', and ", ('kostya', 'поступила'), " means 'acted' or 'behaved'. The ending shows it is a woman who acted."]),
    (10, None, ["'And you protected me so nicely, Kostya.' Now let's inspect the phrase: ", ('nastya', 'красиво'), " is 'beautifully', meaning he did it well. The verb ", ('nastya', 'защитил'), " is the man's past form for 'protected'."]),
    (11, None, ["'Maybe you will come visit me tonight?' The expression ", ('nastya', 'в'), ('nastya', 'гости'), " is 'as guests', which means 'on a visit'. Nastya adds ", ('nastya', 'сегодня'), ", today, to mean 'tonight'."]),
    (12, None, ["'I will gladly come visit you tonight!' Now we can focus on the phrase: ", ('kostya', 'С'), ('kostya', 'огромным'), ('kostya', 'удовольствием'), " is 'with huge pleasure'. The verb ", ('kostya', 'приду'), " answers her 'you will come'."]),
]
