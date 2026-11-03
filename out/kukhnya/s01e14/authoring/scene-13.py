# Authoring module for kukhnya-s01e14-scene-13.
ID = 'kukhnya-s01e14-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 13
TITLE = 'Где шеф?  (Where is the Chef?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'diana': 'Диана', 'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'The guests are asking for the chef, but Barinov has passed out. Diana tracks Max down and asks him to cook for her, and Nagiyev hurries in to steer her back to the dining room. Listen in Russian first.'
OPENER = 'Now in slow motion.'
TRANSITION = 'Now the whole scene again.'
OUTRO = "Max heads off to Diana's table with no idea what he is about to cook. Notice how Diana uses the polite form of 'you' with him all the way through. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('diana', 'Витя, просыпайтесь!', 'Vitya, wake up!', [(179, 'Витя! Просыпайтесь!')], ''),
    ('nagiyev', 'Он не проснется.', 'He will not wake up.', [(180, 'Не проснется')], ''),
    ('nagiyev', 'Бесполезно его будить.', 'It is useless to wake him.', [(180, 'Бесполезно.')], ''),
    ('diana', 'Максимилиан, вот вы где.', 'Maximilian, there you are.', [(182, 'Максимилиан, вот вы где.')], ''),
    ('max', 'Да, я здесь.', 'Yes, I am here.', [], ''),
    ('diana', 'Вы прячетесь от нас.', 'You are hiding from us.', [(183, 'а вы вот где прячетесь.')], ''),
    ('max', 'Я ни от кого не прячусь.', 'I am not hiding from anyone.', [], ''),
    ('diana', 'Приготовьте нам маленький шедевр.', 'Prepare a little masterpiece for us.', [(184, 'приготовили маленький шедевр')], ''),
    ('diana', 'Мы хотим старинную французскую кухню.', 'We want classic French cuisine.', [(184, 'Мы хотим'), (184, 'из старинной французской кухни.')], ''),
    ('max', 'Шеф-повару нужно отдыхать.', 'A chef needs to rest.', [(185, 'шеф-повару тоже нужно отдыхать')], ''),
    ('nagiyev', 'У нас производственное совещание.', 'We have a production meeting.', [(189, 'У нас маленькое производственное совещание.')], ''),
    ('diana', 'Максимилиан, я вас жду.', 'Maximilian, I am waiting for you.', [(190, 'Максимилиан, я вас жду.')], ''),
    ('max', 'Я сейчас к вам приду.', 'I will come to you now.', [(191, 'я сразу к вам.')], ''),
]
WALK = [
    (0, None, ["'Vitya, wake up!' Vitya is Barinov's first name. To say wake up politely, use ", ('diana', 'просыпайтесь'), '.']),
    (1, None, ["'He will not wake up.' To say he will not wake up, use ", ('nagiyev', 'не'), ('nagiyev', 'проснется'), '.']),
    (2, None, ["'It is useless to wake him.' To say it is useless, use ", ('nagiyev', 'Бесполезно'), '. Waking someone else up is ', ('nagiyev', 'будить'), '.']),
    (3, None, ["'Maximilian, there you are.' To say 'so there you are', use ", ('diana', 'вот'), ('diana', 'вы'), ('diana', 'где'), '.']),
    (4, None, ["'Yes, I am here.' To say 'I am here', use ", ('max', 'я'), ('max', 'здесь'), '.']),
    (5, None, ["'You are hiding from us.' To say you are hiding, use ", ('diana', 'прячетесь'), '. From us is ', ('diana', 'от'), ('diana', 'нас'), '.']),
    (6, None, ["'I am not hiding from anyone.' To say from nobody, use ", ('max', 'ни'), ('max', 'от'), ('max', 'кого'), '.']),
    (7, None, ["'Prepare a little masterpiece for us.' To tell someone to prepare something politely, use ", ('diana', 'Приготовьте'), '. To us is ', ('diana', 'нам'), '.']),
    (8, None, ["'We want classic French cuisine.' The term for kitchen and cuisine is ", ('diana', 'кухню'), '.']),
    (9, None, ["'A chef needs to rest.' To say to the chef it is needed, use ", ('max', 'Шеф'), '-', ('max', 'повару'), ('max', 'нужно'), '.']),
    (10, None, ["'We have a production meeting.' To say 'we have', use ", ('nagiyev', 'У'), ('nagiyev', 'нас'), '. A meeting is ', ('nagiyev', 'совещание'), '.']),
    (11, None, ["'Maximilian, I am waiting for you.' To say 'I am waiting for you', use ", ('diana', 'я'), ('diana', 'вас'), ('diana', 'жду'), '.']),
    (12, None, ["'I will come to you now.' To say 'to you', use ", ('max', 'к'), ('max', 'вам'), '. I will come is ', ('max', 'приду'), '.']),
]
