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
INTRO = "Feeling guilty over Chef Barinov's damaged car mirror, Kostya tries to take the blame himself to protect Nastya. However, Nastya rushes forward to confess that she accidentally hit the mirror while riding her bicycle, leading to a surprisingly peaceful resolution. Let's listen to their confession in Russian."
OPENER = "Now let's examine how Kostya and Nastya confess their accident to Barinov line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Relieved of their guilt, Kostya and Nastya arrange their first intimate evening together. Next time you watch the episode, listen for the Russian expressions for 'to break' and 'mirror' — you will catch every word right away. See you next time!"
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
    (0, None, "'Chef, I broke your car mirror.' Kostya repeats his false confession. He insists he is the one who caused the damage."),
    (1, None, "'Chef, do not believe him at all!' Nastya urgently interrupts to tell the truth. She begs the Chef to ignore Kostya."),
    (2, None, "'I broke your side mirror myself!' She claims full responsibility. Nastya emphasizes that she did it herself."),
    (3, None, "'Did you both break my mirror together?' Chef Barinov is utterly confused. He wonders if they somehow did it together."),
    (4, None, "'I was riding a bicycle and grazed it.' Nastya explains exactly how it happened. She admits she clipped it while riding past."),
    (5, None, "'I was simply trying to protect Nastya, chef.' Kostya explains his noble motive. He admits he was just trying to shield Nastya."),
    (6, None, "'Chef, please forgive both of us!' Nastya pleads for mercy. She asks the Chef to pardon them both."),
    (7, None, "'I was fighting with the neighbor for two days!' Chef Barinov reveals his own exhaustion. He complains about his ongoing feud next door."),
    (8, None, "'Go back to work, you clumsy people!' He gruffly dismisses them without punishment. Barinov calls them clumsy but lets them go."),
    (9, None, "'Nastya, thank you, you acted very bravely.' Kostya praises her courage. He admires how bravely she faced the angry Chef."),
    (10, None, "'And you protected me so nicely, Kostya.' Nastya appreciates his chivalry with gratitude. She thanks him for trying to save her."),
    (11, None, "'Maybe you will come visit me tonight?' She shyly extends an invitation. Nastya asks if he still wants to come over."),
    (12, None, "'I will gladly come visit you tonight!' Kostya accepts the invitation with excitement. He happily agrees to the plan."),
]
