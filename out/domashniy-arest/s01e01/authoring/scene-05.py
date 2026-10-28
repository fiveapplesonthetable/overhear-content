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
OUTRO = "So the busy mayor has a late meeting tonight, and it isn't with Viktor Stepanovich. Listen for 'I really can't today' when you watch, and. See you next time!"
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
    ('governor', 'Я и сама хорошо проведу время.', "I'll have a good time on my own.", [(200, 'Я и сама'), (200, 'хорошо время проведу')], "'с собой' dropped, word order made standard"),
    ('arkady', 'Не надо кричать. Хорошо, я буду сегодня.', "There's no need to shout. All right, I'll be there tonight.", [(202, 'не надо кричать'), (203, 'Хорошо, я буду'), (204, 'Я буду сегодня')], 'cues 202-204 combined'),
    ('arkady', 'Всё, жму руку.', 'Right, cheers then.', [(205, 'Все, жму руку')], ''),
    ('vika', 'И что?', 'And?', [(206, 'И что')], ''),
    ('arkady', 'Совещание экстренное назначил.', "He's called an emergency meeting.", [(207, 'Совещание экстренное назначил')], ''),
    ('vika', 'Так тебя не ждать сегодня?', "So I shouldn't wait for you tonight?", [(209, 'Так тебя не ждать сегодня')], ''),
    ('arkady', 'Нет, милая, не жди.', "No, darling, don't wait.", [(210, 'Нет, милая, не жди')], ''),
    ('arkady', 'Поработать немного надо.', 'I need to do a bit of work.', [(211, 'Поработать немного надо')], ''),
]
WALK = [
    (0, None, "'Viktor Stepanovich, greetings.' A very formal hello, the kind you use with someone important. Vika can hear every word. The caller is far less formal."),
    (1, 'Привет, Аркадий Борисович.', "'Hi, Arkady Borisovich.' A casual 'hi', but with his full name and his father's name. Then a simple question."),
    (1, 'Что делаешь?', "'What are you doing?' This is the casual 'you': the ending of the verb says it, so no pronoun is needed. Arkady answers like a politician."),
    (2, None, "'Working. Making people's lives better.' Again, no 'I': the verb endings already mean 'I work', 'I make'. The caller has a better idea."),
    (3, None, "'And you don't want to make my life better?' Quite a request from a government official. Arkady keeps up the act."),
    (4, None, "'Viktor Stepanovich, I really can't today.' The word in front of 'can't' means 'in no way', so it's a strong no. And he gives a reason."),
    (5, None, "'There's a lot of work.' Literally 'of work, very much'. After words for 'a lot', the noun takes the 'of' form. The caller doesn't give up."),
    (6, None, "'Well, come in the evening.' The verb means to come by car or transport, and it's a casual command. Arkady tries another excuse."),
    (7, None, "'But I promised to be with my wife this evening.' The word for 'promised' ends in a consonant because Arkady is a man. Now the caller sulks."),
    (8, None, "'Well, if you don't want to, suit yourself.' Word for word: 'you don't want, as you want'. A handy phrase when someone says no to you. And then a little threat."),
    (9, None, "'I'll have a good time on my own.' Listen to the word for 'myself' or 'on my own': it ends in 'a', which is the feminine form. So our Viktor Stepanovich is a woman, and Arkady gives in fast."),
    (10, None, "'There's no need to shout. All right, I'll be there tonight.' 'I will be' is the future of 'to be'. Then he hangs up like a businessman."),
    (11, None, "'Right, cheers then.' Word for word it says 'I shake your hand', a firm goodbye between men in business, which is funny when the caller is a woman. Vika is curious."),
    (12, None, "'And?' Two little words: 'and what?'. Arkady has his story ready."),
    (13, None, "'He's called an emergency meeting.' The verb is masculine past, so 'he', the official, called it. It's the official story for his wife. Vika gets the message."),
    (14, None, "'So I shouldn't wait for you tonight?' Literally, 'so, not to wait for you today?' Russians often ask with a bare verb like this. Arkady says it very sweetly."),
    (15, None, "'No, darling, don't wait.' The last word is a command, 'don't wait'. And he sighs, as if it's a sacrifice."),
    (16, None, "'I need to do a bit of work.' 'Need' comes at the end here, which makes it sound tired and casual."),
]
