# Authoring module for kukhnya-s01e13-scene-05.
ID = 'kukhnya-s01e13-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 5
TITLE = "Опоздание Макса  (Max's Tardiness)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Max arrives late to the kitchen, claiming he just overslept. The Chef immediately punishes him with warehouse duty and asks Victoria for her opinion. Let's listen closely to the conversation in Russian first, and then walk through each line together."
OPENER = "Let's join the kitchen staff as Max finally arrives to work."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Sent to the stockroom for the day, Max learns that arriving late has immediate consequences. Next time you watch the episode, listen for the Russian expressions for 'to excuse' and 'just' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Привет всем.', 'Hi to everyone.', [(64, 'Привет всем.')], ''),
    ('max', 'Шеф, извините, я просто проспал.', 'Boss, excuse me, I simply overslept.', [(66, 'Шеф, извините.'), (71, 'Я просто проспал.')], ''),
    ('max', 'Больше такое не повторится.', 'Such a thing will not happen again.', [(72, 'больше такое не повторится.')], ''),
    ('barinov', 'Сегодня ты работаешь на складе.', 'Today you are working in the stockroom.', [(61, 'сегодня')], ''),
    ('barinov', 'Ещё раз проспишь — я тебя уволю.', 'Oversleep one more time — I will fire you.', [(59, 'еще')], ''),
    ('max', 'Но шеф, я отличный повар.', 'But boss, I am an excellent cook.', [], ''),
    ('barinov', 'Повар должен приходить на работу вовремя.', 'A cook must arrive at work on time.', [], ''),
    ('max', 'Я обещаю больше никогда не опаздывать.', 'I promise to never be late again.', [], ''),
    ('barinov', 'Я сказал своё слово.', 'I have said my word.', [], ''),
    ('barinov', 'Виктория Сергеевна, почему вы так молчите?', 'Victoria Sergeyevna, why are you so silent?', [], ''),
    ('vika', 'Надо раньше ложиться спать, чтобы не проспать.', 'It is necessary to go to bed earlier to not oversleep.', [(61, 'надо')], ''),
    ('barinov', 'Вот видите, она со мной согласна.', 'Here you see, she agrees with me.', [], ''),
]
WALK = [
    (0, None, "'Hi to everyone.' Max enters the busy kitchen looking slightly guilty."),
    (1, None, "'Boss, excuse me, I simply overslept.' He quickly offers an excuse for his lateness."),
    (2, None, "'Such a thing will not happen again.' Max tries to sound very responsible and serious."),
    (3, None, "'Today you are working in the stockroom.' The Chef does not hesitate to discipline him."),
    (4, None, "'Oversleep one more time — I will fire you.' Chef Barinov puts the word for 'more' together with 'time' and 'oversleep' in a crisp, natural spoken turn of phrase."),
    (5, None, "'But boss, I am an excellent cook.' Russian omits the present-tense verb 'to be' here, linking 'excellent' directly with 'chef', combining 'excellent' with 'chef'."),
    (6, None, "'A cook must arrive at work on time.' The Chef reminds him about basic professional discipline."),
    (7, None, "'I promise to never be late again.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (8, None, "'I have said my word.' The stubborn Chef refuses to change his strict decision."),
    (9, None, "'Victoria Sergeyevna, why are you so silent?' Here Chef Barinov anchors the line on the word meaning 'why' and builds the thought around 'are you silent'."),
    (10, None, "'It is necessary to go to bed earlier to not oversleep.' The phrasing opens with 'it is necessary' before bringing in 'earlier' and 'go to bed' to make the point clear."),
    (11, None, "'Here you see, she agrees with me.' The Chef feels completely justified in his harsh punishment."),
]
