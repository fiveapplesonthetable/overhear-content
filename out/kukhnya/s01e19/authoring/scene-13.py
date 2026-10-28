# Authoring module for kukhnya-s01e19-scene-13.
ID = 'kukhnya-s01e19-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 13
TITLE = 'Инвалиды  (The Cripples)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = 'In the kitchen, Max and the other cooks are taking a breather when Senya and Fedya, the two fired cooks, march back in. First the scene in Russian; listen for the swagger.'
OPENER = "Line by line now, starting with Max's break."
TRANSITION = 'Hear the return of the pros once more.'
OUTRO = 'Senya and Fedya are back and already bossing everyone around, and you kept up with them. See you next time!'
CLOSING = ('senya', 'Пока, повара!')
STORY = [
    ('max', 'Я очень устал сегодня.', 'I am very tired today.', [], ''),
    ('max', 'Мы много работали утром.', 'We worked a lot in the morning.', [], ''),
    ('max', 'Давайте немного отдохнем.', "Let's rest a bit.", [], ''),
    ('senya', 'Привет, повара!', 'Hello, cooks!', [], ''),
    ('fedya', 'Что встали, инвалиды?', 'What are you standing around for, cripples?', [(233, 'Что встали, инвалиды')], ''),
    ('fedya', 'Не видите?', "Can't you see?", [(234, 'Не видите')], ''),
    ('senya', 'Профессионалы пришли.', 'The pros are here.', [(235, 'Профессионалы пришли')], ''),
    ('max', 'Вы не профессионалы.', 'You are not professionals.', [], ''),
    ('max', 'Вы просто много говорите.', 'You just talk a lot.', [], ''),
    ('fedya', 'Мы говорим правду.', 'We are telling the truth.', [], ''),
    ('senya', 'Идите работать!', 'Go to work!', [], ''),
    ('max', 'Хорошо, мы идем.', 'Okay, we are going.', [], ''),
]
WALK = [
    (0, None, "'I am very tired today.' \"Ya ustal\", 'I'm tired', is said with the past form, literally 'I got tired'. A woman says \"ya ustala\"."),
    (1, None, "'We worked a lot in the morning.' \"Utrom\", 'in the morning', is \"utro\" with -om added, just as \"vecher\" gives \"vecherom\". \"Mnogo\" means 'a lot'."),
    (2, None, "'Let's rest a bit.' \"Davayte\" plus 'we' turns into 'let's' for a group. \"Otdokhnyom\" means 'we'll rest'."),
    (3, None, "'Hello, cooks!' \"Povar\", 'cook', becomes \"povara\", with the stress on the end. That ending for more than one comes with just a few words, like \"doma\", 'houses'."),
    (4, None, "'What are you standing around for, cripples?' \"Chto vstali\" is 'why have you stopped?', with \"chto\" meaning 'why'. \"Invalidy\", 'cripples', is a nasty insult here."),
    (5, None, "'Can't you see?' \"Vidite\", 'you see', ends in -te because Fedya speaks to the whole group. To one friend it's \"vidish'\"."),
    (6, None, "'The pros are here.' \"Prishli\", 'came', ends in -li because there are two of them. \"Professionaly\" is the word Senya uses for himself and Fedya."),
    (7, None, "'You are not professionals.' \"Vy ne professionaly\" is just 'you not professionals'. Russian needs no 'are'."),
    (8, None, "'You just talk a lot.' \"Prosto\" covers both 'just' and 'simply'. \"Govorite\", 'you talk', is aimed at both of them."),
    (9, None, "'We are telling the truth.' \"Govorit' pravdu\" is 'to tell the truth': \"pravda\" becomes \"pravdu\". A lone \"Pravda\" can mean 'really?'."),
    (10, None, "'Go to work!' \"Idite rabotat'\", 'go work', has no 'to' between the two verbs. \"Idi\" spat', 'go to sleep', works the same way."),
    (11, None, "'Okay, we are going.' \"Idyom\" is 'we go' or 'we're going', on foot. \"Khorosho\", 'good', is the plain 'okay'."),
]
