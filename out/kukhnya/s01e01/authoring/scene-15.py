# Authoring module for kukhnya-s01e01-scene-15.
ID = 'kukhnya-s01e01-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 15
TITLE = 'Собеседование на кухне  (Interview in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "Max has been sent into a room by a couple of cooks who were pulling his leg, and it turns out to be the chef's office. Then the real head chef, Viktor Barinov, walks in and wants to know who this stranger is. Here's the confrontation in Russian first."
OPENER = "Let's go through their exchange."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Barinov is going to test him, and the test will be a hard one. You\'ve heard how a chef says "here, only I command", which is a good line to remember.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Здравствуйте, я пришёл сюда на важное собеседование.', 'Hello, I came here for an important interview.', [(123, 'Я на собеседовании')], ''),
    ('barinov', 'Ты кто такой и как сюда попал?', 'Who are you and how did you get in here?', [(141, 'Ты кто такой')], ''),
    ('max', 'Я принёс своё резюме для шеф-повара.', 'I brought my résumé for the head chef.', [(129, 'Вот мое резюме')], ''),
    ('barinov', 'Что ты вообще делаешь в моём кабинете?', 'What are you even doing in my office?', [(142, 'Ты что здесь делаешь')], ''),
    ('max', 'Другой повар сказал, что шеф уже здесь.', 'Another cook said that the chef is already here.', [(124, 'Вот шеф')], ''),
    ('barinov', 'Настоящий главный шеф-повар этого ресторана — я!', 'The real head chef of this restaurant is me!', [(135, 'Виктор Петрович идёт')], ''),
    ('max', 'Тот человек уже принял меня на работу.', 'That person already hired me for the job.', [(144, 'шеф меня уже взял')], ''),
    ('barinov', 'Кто посмел принять тебя без моего разрешения?', 'Who dared hire you without my permission?', [(145, 'Кто')], ''),
    ('max', 'Я мечтаю готовить вкусные блюда на кухне.', 'I dream of cooking delicious dishes in the kitchen.', [(130, 'Настоящему повару')], ''),
    ('barinov', 'Здесь командую только я и никто больше.', 'Only I command here and no one else.', [(143, 'Какое ещё нахрен собеседование')], ''),
    ('max', 'Пожалуйста, дайте мне один маленький шанс.', 'Please, give me one small chance.', [(132, 'твой потенциал')], ''),
    ('barinov', 'Ладно, сейчас проверим твои настоящие кулинарные навыки.', 'Fine, now we will test your real culinary skills.', [(132, 'увидел твой потенциал')], ''),
]
WALK = [
    (0, None, ['\'Hello, I came here for an important interview.\' ', ('max', 'Сюда'), ' is "to here", the same word that told Max not to come back. ', ('max', 'важное'), ' ends in ', ('max', '-ое'), ' because ', ('max', 'собеседование'), ' is neuter.']),
    (1, None, ['\'Who are you and how did you get in here?\' ', ('barinov', 'Ты кто такой'), ' is "you who such", a blunt way to say "who do you think you are?". The ', ('barinov', 'ты'), ' is rude from a stranger. ', ('barinov', 'попал'), ' means "ended up", as if by chance.']),
    (2, None, ['\'I brought my résumé for the head chef.\' ', ('max', 'Принёс'), ' is "brought", carried by a man; a woman would say ', ('max', 'принёс'), '. ', ('max', 'своё'), ' is "my own". ', ('max', 'резюме'), ' never changes.']),
    (3, None, ['\'What are you even doing in my office?\' ', ('barinov', 'вообще'), ' means "at all" or "even", and it adds irritation. ', ('barinov', 'в моём кабинете'), ' is "in my office", and both ', ('barinov', 'моём'), ' and ', ('barinov', 'кабинете'), ' take endings after ', ('barinov', 'в'), '.']),
    (4, None, ['\'Another cook said that the chef is already here.\' ', ('max', 'Другой'), ' is "another", which looks like ', ('max', 'друг'), ', friend, with an ending. ', ('max', 'сказал, что'), ' is "said that", and Russian always puts a comma before ', ('max', 'что'), '.']),
    (5, None, ['\'The real head chef of this restaurant is me!\' The dash stands for "is", and ', ('barinov', 'я'), ' comes last for punch. ', ('barinov', 'этого ресторана'), ' is "of this restaurant", with ', ('barinov', '-ого'), ' and ', ('barinov', '-а'), ' showing "of".']),
    (6, None, ['\'That person already hired me for the job.\' ', ('max', 'принял'), ' is "accepted", a second way to say "hired", after ', ('max', 'принял'), '. ', ('max', 'Тот человек'), ' is "that person".']),
    (7, None, ['\'Who dared hire you without my permission?\' ', ('barinov', 'Кто посмел'), ' is "who dared", a furious question in any kitchen. ', ('barinov', 'без'), ' is "without", as in water ', ('barinov', 'без'), ', and ', ('barinov', 'разрешения'), ', permission, becomes ', ('barinov', 'разрешения'), ' after it.']),
    (8, None, ['\'I dream of cooking delicious dishes in the kitchen.\' Max uses ', ('max', 'мечтаю'), ', "I dream", once more, and this time a plain verb follows it: ', ('max', 'мечтаю готовить'), ', "I dream to cook". ', ('max', 'вкусные блюда'), ' is plural, so the describing word ends in ', ('max', '-ые'), '.']),
    (9, None, ['\'Only I command here and no one else.\' ', ('barinov', 'командую'), ', "I command", sounds a lot like the English word. ', ('barinov', 'никто больше'), ' is "nobody more", which is how Russian says "no one else".']),
    (10, None, ['\'Please, give me one small chance.\' ', ('max', 'дайте'), ' is the polite "give", and ', ('max', 'мне'), ' is "to me". ', ('max', 'шанс'), ' is borrowed from French "chance", and ', ('max', 'один маленький'), ', "one small", makes the request sound humble.']),
    (11, None, ['\'Fine, now we will test your real culinary skills.\' ', ('barinov', 'ладно'), ' is "fine" or "okay", the same word as in ', ('barinov', 'Ладно'), '. ', ('barinov', 'твои'), ' is "your" in the friendly form, which tells Max the chef talks down to him.']),
]
