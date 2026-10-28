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
INTRO = "In the kitchen, Max and some of the cooks are having a quick rest after a long morning when two familiar faces walk in. Senya and Fedya are back, and they have something to say about the people who stayed. We'll hear it in Russian first."
OPENER = 'Here it is again, piece by piece.'
TRANSITION = 'Here is the whole conversation again.'
OUTRO = "The old pair are back, as cheeky as ever. The word the cooks throw at each other, 'invalidy', is Barinov's favourite insult, and it has become the kitchen's password. See you next time!"
CLOSING = ('max', 'До свидания!')
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
    (0, None, "'I'm very tired today.' 'Tired' is a short masculine form, since Max is a man. 'Today' sits at the end."),
    (1, None, "'We worked a lot this morning.' 'A lot' is a single small word. 'In the morning' has an 'om' ending."),
    (2, None, "'Let's rest a bit.' 'A bit' is literally 'not much'. 'Let's' is made from 'davayte' and a 'we' form."),
    (3, None, "'Hello, cooks!' The plural of 'cook' ends in a stressed 'a'. It's an odd plural, but a common one."),
    (4, None, "'Why are you standing around, cripples?' Literally, 'what did you get up for'. 'Cripples' is Barinov's pet insult, borrowed by the cooks."),
    (5, None, "'Can't you see?' It is only 'don't you see', with the polite plural. Fedya is mocking."),
    (6, None, "'The pros have arrived.' 'Professionals' is a borrowed word, in the plural. 'Arrived' has the plural ending 'li'."),
    (7, None, "'You aren't professionals.' The 'not' goes in front of the noun. There's no 'are'."),
    (8, None, "'You just talk a lot.' 'Just' and 'a lot' flank the verb. 'Talk' carries 'ite', the polite plural."),
    (9, None, "'We're telling the truth.' 'We tell' ends in 'im'. 'Truth' takes a 'u' ending."),
    (10, None, "'Go and work!' 'Go' is a polite plural command. The next word is the plain form 'to work'."),
    (11, None, "'Okay, we're going.' 'We go' finishes with 'yom'. The first word is a quick 'okay'."),
]
