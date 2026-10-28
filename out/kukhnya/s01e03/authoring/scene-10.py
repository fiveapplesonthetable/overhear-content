# Authoring module for kukhnya-s01e03-scene-10.
ID = 'kukhnya-s01e03-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 10
TITLE = 'История про гуся  (The Story of the Goose)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "Having secretly replaced the missing live goose with a dressed market carcass, Max returns to face head chef Viktor Barinov. Barinov immediately questions why Max's apron is spotless without a single drop of blood, forcing Max to tell a shocking lie. Let's listen to their confrontation in Russian first."
OPENER = "Let's replay a few lines to examine key phrases and vocabulary."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Lyova prepares the bird for roasting while Barinov begins preparing the special compliment. Next time you watch the episode, listen for the Russian expressions for 'fast' and 'important' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Огузок! Где мой свежий гусь?', 'Guzak! Where is my fresh goose?', [(235, 'Где гусь')], ''),
    ('max', 'Я только что прикончил его!', 'I have just finished it off!', [(236, 'Я его только что прикончил')], ''),
    ('barinov', 'Почему ты такой подозрительно чистый?', 'Why are you so suspiciously clean?', [(237, 'А что ты такой чистенький')], ''),
    ('barinov', 'На тебе нет ни капли крови!', 'There is not a drop of blood on you!', [(237, 'ни капельки крови на тебя не попало')], ''),
    ('max', 'Я его совсем не резал.', 'I did not cut it at all.', [(238, 'Я его не зарезал')], ''),
    ('barinov', 'И как ты его убил?', 'And how did you kill it?', [], ''),
    ('max', 'Шеф, я его просто задушил!', 'Chef, I simply strangled it!', [(239, 'Я его задушил')], ''),
    ('barinov', 'Какой кошмар! Настоящий Отелло на кухне!', 'What a nightmare! A real Othello in the kitchen!', [(240, 'Какой ужас'), (240, 'Ладно, Отелло')], ''),
    ('barinov', 'Тащи свою птицу су-шефу на стол!', "Drag your bird to the sous-chef's table!", [(240, 'тащи свою дездемону с ушефу')], ''),
    ('barinov', 'Лёва, начинай быстро готовить гуся!', 'Lyova, start preparing the goose quickly!', [(241, 'Лёва, начинай готовить гуся')], ''),
    ('lyova', 'Понял, шеф, я включаю духовку.', 'Understood, Chef, I am turning on the oven.', [(242, 'Понял, шеф')], ''),
    ('barinov', 'А я займусь важным комплиментом.', 'And I will take care of an important compliment.', [(243, 'А я займусь комплиментом от шефа')], ''),
    ('max', 'Я спас птицу и свою работу.', 'I saved the bird and my job.', [], ''),
]
WALK = [
    (0, None, "'I have just finished it off!' Max announces he completed the task."),
    (1, None, "'There is not a drop of blood on you!' Barinov points out the lack of mess."),
    (2, None, "'Chef, I simply strangled it!' Max explains his clean method of killing."),
    (3, None, "'Lyova, start preparing the goose quickly!' Barinov orders the cook to begin working on the bird."),
]
