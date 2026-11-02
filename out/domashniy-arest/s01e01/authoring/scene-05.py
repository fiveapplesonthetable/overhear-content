# Authoring module for domashniy-arest-s01e01-scene-05.
ID = 'domashniy-arest-s01e01-scene-05'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = 'Экстренное совещание  (An Emergency Meeting)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'governor': 'Губернатор', 'vika': 'Вика'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Arkady has left the square, with his wife Vika beside him. Last time, he promised a lecturer to save an old monastery wall, then quietly told his deputy to get rid of her. Now his phone rings, and he greets the caller as Viktor Stepanovich, an important official, though the voice on the line doesn't sound much like a Viktor. Let's listen in Russian first."
OPENER = "Let's go through it. Arkady answers the phone in his most official voice."
TRANSITION = "Here's the whole conversation once more."
OUTRO = "So the busy mayor has a late meeting tonight, and it isn't with Viktor Stepanovich. Listen for 'I really can't today' when you watch. See you next time!"
CLOSING = ('vika', 'Пока, милый!')
STORY = [
    ('arkady', 'Виктор Степанович, приветствую вас.', 'Viktor Stepanovich, greetings.', [(183, 'Виктор Степанович, приветствую вас')], ''),
    ('governor', 'Привет, Аркадий Борисович. Что делаешь?', 'Hi, Arkady Borisovich. What are you doing?', [(184, 'Привет, Аркадий Борисович'), (185, 'Что делаешь')], ''),
    ('arkady', 'Работаю. Делаю жизнь людей лучше.', "Working. Making people's lives better.", [(188, 'Делаю жизнь людей лучше')], "'Тружусь на благо города' -> 'Работаю'"),
    ('governor', 'А мою жизнь лучше сделать не хочешь?', "And you don't want to make my life better?", [(189, 'А мою жизнь лучше сделать не хочешь')], ''),
    ('arkady', 'Виктор Степанович, сегодня никак не могу.', "Viktor Stepanovich, I really can't today.", [(190, 'Виктор Степанович'), (191, 'сегодня никак не могу')], "'к сожалению' dropped"),
    ('arkady', 'Работы очень много.', "There's a lot of work.", [(192, 'Работы очень много')], "'накопилось' dropped"),
    ('governor', 'Ну, приезжай вечером.', 'Well, come in the evening.', [(193, 'Ну, приезжай вечером')], ''),
    ('arkady', 'Но вечером я обещал быть с женой.', 'But I promised to be with my wife this evening.', [(198, 'вечером'), (198, 'обещал')], "'Я вечером супруге обещал время уделить' simplified"),
    ('governor', 'Ну, не хочешь, как хочешь.', "Well, if you don't want to, suit yourself.", [(199, 'Ну, не хочешь, как хочешь')], ''),
    ('vika', 'Я и сама хорошо проведу время.', "I'll have a good time on my own.", [(200, 'Я и сама'), (200, 'хорошо время проведу')], "'с собой' dropped, word order made standard"),
    ('arkady', 'Не надо кричать. Хорошо, я буду сегодня.', "There's no need to shout. All right, I'll be there tonight.", [(202, 'не надо кричать'), (203, 'Хорошо, я буду'), (204, 'Я буду сегодня')], 'cues 202-204 combined'),
    ('arkady', 'Всё, жму руку.', 'Right, cheers then.', [(205, 'Все, жму руку')], ''),
    ('vika', 'И что?', 'And?', [(206, 'И что')], ''),
    ('arkady', 'Совещание экстренное назначил.', "He's called an emergency meeting.", [(207, 'Совещание экстренное назначил')], ''),
    ('vika', 'Так тебя не ждать сегодня?', "So I shouldn't wait for you tonight?", [(209, 'Так тебя не ждать сегодня')], ''),
    ('arkady', 'Нет, милая, не жди.', "No, darling, don't wait.", [(210, 'Нет, милая, не жди')], ''),
    ('arkady', 'Поработать немного надо.', 'I need to do a bit of work.', [(211, 'Поработать немного надо')], ''),
]
WALK = [
    (0, None, ["'Viktor Stepanovich, greetings.' the translation for 'I greet you', ", ('arkady', 'приветствую вас'), ", sounds stiffly official — put on for Vika sitting right beside him. The caller is far less formal."]),
    (1, 'Привет, Аркадий Борисович.', ["'Hi, Arkady Borisovich.' Mixing the casual word for 'hi', ", ('governor', 'привет'), ", with formal 'Arkady Borisovich' already hints this is no ordinary boss. Then comes a simple question."]),
    (1, 'Что делаешь?', ["'What are you doing?' The action word ", ('governor', 'делаешь'), " literally translates to 'you are doing', so no extra word for 'you' is needed. Arkady answers like a politician."]),
    (2, None, ["'Working. Making people's lives better.' Again, the action words ", ('arkady', 'работаю'), " and ", ('arkady', 'делаю'), " translate to 'I am working' and 'I am making' without needing a separate word for 'I'. The caller has a better idea."]),
    (3, None, ["'And you don't want to make my life better?' Putting the words for 'my life', ", ('governor', 'мою жизнь'), ", right at the front contrasts her with 'people's lives', ending on ", ('governor', 'не хочешь?'), " which literally means 'don't you want?'. Arkady keeps up the act."]),
    (4, None, ["'Viktor Stepanovich, I really can't today.' Putting ", ('arkady', 'никак'), " before ", ('arkady', 'не могу'), " translates to 'in no way at all', turning 'I can't' into 'there's zero chance'. He adds a reason."]),
    (5, None, ["'There's a lot of work.' Literally, 'of work, very much' — after ", ('arkady', 'много'), ", meaning 'a lot', the term for 'work' shifts its sound to ", ('arkady', 'работы'), ". The caller doesn't give up."]),
    (6, None, ["'Well, come in the evening.' The action word ", ('governor', 'приезжай'), " specifically translates to 'come over by transport or car', unlike coming on foot. Arkady tries another excuse."]),
    (7, None, ["'But I promised to be with my wife this evening.' the term for 'promised', ", ('arkady', 'обещал'), ", shows a man is speaking, and ", ('arkady', 'с женой'), " translates to 'with my wife'. Now the caller sulks."]),
    (8, None, ["'Well, if you don't want to, suit yourself.' The phrase ", ('governor', 'не хочешь, как хочешь'), " — literally 'don't want to, as you want' — is a classic Russian shrug when someone turns you down. Then comes a little threat."]),
    (9, None, ["'I'll have a good time on my own.' Listen to which translates to 'on my own', ", ('vika', 'сама'), ": that little word belongs to a female speaker, giving away 'Viktor Stepanovich' at once!"]),
    (10, None, ["'There's no need to shout. All right, I'll be there tonight.' The phrase ", ('arkady', 'я буду'), " literally means 'I will be' and often stands in for 'I'll show up' or 'I'll be there'. Then he hangs up like a businessman."]),
    (11, None, ["'Right, cheers then.' The phrase ", ('arkady', 'жму руку'), " literally translates to 'I shake your hand', a brisk man-to-man sign-off used to fool Vika. She is curious."]),
    (12, None, ["'And?' Two tiny words, ", ('vika', 'и что?'), " — literally 'and what?' — ask 'so what did he want?'. Arkady has his cover story ready."]),
    (13, None, ["'He's called an emergency meeting.' the term for 'he scheduled', ", ('arkady', 'назначил'), ", shows a man did the scheduling to keep up the fiction that a man called it."]),
    (14, None, ["'So I shouldn't wait for you tonight?' Literally, 'so, not to wait for you today?' — ", ('vika', 'тебя не ждать?'), " translates to 'should I not wait for you?' using the simplest words."]),
    (15, None, ["'No, darling, don't wait.' the Russian for 'sweetheart' or 'darling', ", ('arkady', 'милая'), ", is a describing word for a woman, followed by ", ('arkady', 'не жди'), ", meaning 'don't wait'. He sighs as if it's a sacrifice."]),
    (16, None, ["'I need to do a bit of work.' Putting the translation for 'need to', ", ('arkady', 'надо'), ", right at the end of ", ('arkady', 'поработать немного надо'), " makes it sound weary and reluctant."]),
]
