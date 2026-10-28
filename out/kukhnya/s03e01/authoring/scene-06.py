# Authoring module for kukhnya-s03e01-scene-06.
ID = 'kukhnya-s03e01-scene-06'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 6
TITLE = 'Звонок из Лондона  (A Call from London)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = 'After Barinov rejects yet another candidate for not having a moustache, Nagiyev boasts that he can hire a molecular chef with a single phone call, while Vika receives an unexpected job offer.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings this scene to an end. Listen for Barinov's rule about moustaches and Vika politely turning down the London restaurant offer. See you next time!"
CLOSING = ('vika', 'До свидания!')
STORY = [
    ('barinov', 'Не родиться женщиной.', 'Not to be born a woman.', [(89, 'Не родиться женщиной')], ''),
    ('barinov', 'А почему вы без усов?', 'And why do you have no moustache?', [(90, 'А почему вы без усов')], ''),
    ('barinov', 'Я беру только поваров с усами.', 'I only hire cooks with moustaches.', [(91, 'Я беру в команду только поваров с усами')], 'adapted'),
    ('nagiyev', 'Я за один звонок найду вам повара.', 'I will find you a cook with one phone call.', [(95, 'за один телефонный звонок'), (96, 'найду вам повара')], 'adapted'),
    ('nagiyev', 'Телефон мой где?', 'Where is my phone?', [(97, 'Телефон мой где')], ''),
    ('vika', 'Да, добрый день. А с кем я говорю?', 'Yes, good afternoon. Who am I speaking with?', [(100, 'добрый день'), (101, 'А с кем я говорю')], 'adapted'),
    ('vika', 'Чем я могу вам помочь?', 'How can I help you?', [(105, 'Чем я могу вам помочь')], ''),
    ('vika', 'Спасибо, конечно.', 'Thank you, of course.', [(107, 'Спасибо, конечно')], ''),
    ('vika', 'Но я не собираюсь менять работу.', 'But I am not planning to change jobs.', [(108, 'Но я вообще не собираюсь менять')], 'adapted'),
    ('vika', 'Я подумаю позже.', 'I will think about it later.', [(109, 'подумать'), (109, 'позже')], 'adapted'),
    ('vika', 'Хорошо. Отлично.', 'All right. Excellent.', [(110, 'Хорошо. Отлично')], ''),
    ('vika', 'До свидания.', 'Goodbye.', [(111, 'До свидания')], ''),
]
WALK = [
    (0, None, "'Not to be born a woman.' Over the conversation and the phone, Barinov answers Nagiyev without a second thought."),
    (1, None, "'And why do you have no moustache?' By asking why Nagiyev has no moustache, Barinov presses Nagiyev for a straight answer."),
    (2, None, "'I only hire cooks with moustaches.' Adding that he only hires cooks with moustaches fills in the missing piece for Nagiyev."),
    (3, None, '\'I will find you a cook with one phone call.\' Saying that he will find Barinov a cook with one phone call is how Nagiyev sets the tone with Barinov. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (4, None, "'Where is my phone?' Here asking where his phone is shows Nagiyev looking for the real truth."),
    (5, None, '\'Yes, good afternoon. Who am I speaking with?\' Around the call and conversation, Vika wants to know where Barinov really stands. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, '\'How can I help you?\' Asking how she helps Barinov can cuts straight through the tension between Vika and Barinov. Even in the middle of the drama, she keeps the polite plural "you" that workplace Russian expects.'),
    (7, None, "'Thank you, of course.' With the work and job in play, Vika keeps this short reply brisk and direct."),
    (8, None, "'But I am not planning to change jobs.' Noting that she is not planning to change jobs keeps Vika's side of the story simple and clear."),
    (9, None, "'I will think about it later.' Vika mentions that she will think about it later so Barinov sees what is at stake."),
    (10, None, "'All right. Excellent.' Around the work and job, Vika sets a calm, everyday tone with Barinov."),
    (11, None, "'Goodbye.' Between the point and the call, Vika gives Barinov a quick, grounded response."),
]
