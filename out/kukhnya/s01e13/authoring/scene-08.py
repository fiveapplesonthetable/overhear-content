# Authoring module for kukhnya-s01e13-scene-08.
ID = 'kukhnya-s01e13-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 8
TITLE = "Признание Насти  (Nastya's Confession)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Nastya has realised she is the one who broke Barinov's mirror, and now two people are fighting over it. She takes Kostya aside to tell him, but Kostya is thinking about something else. Listen to their talk in Russian first."
OPENER = 'Again, a bit more slowly this time.'
TRANSITION = 'Now their talk, straight through.'
OUTRO = "Kostya's timing is terrible, and Nastya lets him know. His name on its own, said sharply, is a whole telling-off. Until next time."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Костя, мне надо тебе кое-что сказать.', 'Kostya, I need to tell you something.', [(103, 'надо тебе кое-что сказать')], ''),
    ('nastya', 'Я поступила неправильно.', 'I acted wrongly.', [(104, 'Я поступила неправильно')], ''),
    ('kostya', 'Настя, ты передумала насчет вечера?', 'Nastya, did you change your mind about tonight?', [(105, 'Настя, ты передумала насчет вечера')], ''),
    ('nastya', 'Я не об этом.', "That's not what I'm talking about.", [(106, 'Я не об этом')], ''),
    ('nastya', 'Это я разбила зеркало Виктору Петровичу.', "It was me who broke Viktor Petrovich's mirror.", [(107, 'я разбила зеркало Виктору Петровичу')], ''),
    ('nastya', 'И теперь они из-за меня ссорятся.', 'And now they are fighting because of me.', [(108, 'Они из-за меня ссорятся')], ''),
    ('kostya', 'Ничего себе!', 'Wow!', [(109, 'Ничего себе')], ''),
    ('kostya', 'И что теперь делать?', 'And what do we do now?', [], ''),
    ('kostya', 'Стало быть, насчет вечера всё в силе?', 'So, is everything still on for tonight?', [(110, 'Стало быть, насчет вечера')], ''),
    ('nastya', 'Костя!', 'Kostya!', [(111, 'Костя')], ''),
    ('nastya', 'Как ты можешь?', 'How could you?', [], ''),
    ('nastya', 'Ты только об одном и думаешь!', 'You only think about one thing!', [(111, 'только об одном и думаешь')], ''),
]
WALK = [
    (0, None, ["'Kostya, I need to tell you something.' The extra bit on the front of ", ('nastya', 'кое'), '-', ('nastya', 'что'), " means 'a certain', so it comes out 'a certain something'. ", ('nastya', 'мне'), ('nastya', 'надо'), " is 'to me it's necessary', I need to, and ", ('nastya', 'тебе'), " is 'to you', the person being told."]),
    (1, None, ["'I acted wrongly.' Nastya's ending on ", ('nastya', 'поступила'), ' tells you a woman speaks. ', ('nastya', 'неправильно'), " is simply the word for 'correctly', with a negative in front."]),
    (2, None, ["'Nastya, did you change your mind about tonight?' We can inspect the dialogue: ", ('kostya', 'передумала'), " is 'changed your mind', built from the word for 'to think', and a bit meaning 'over again'. ", ('kostya', 'насчет'), " means 'regarding' and is common in speech."]),
    (3, None, ["'That's not what I'm talking about.' Russian says 'I not about this', with no action word. It is a good phrase for steering a conversation back."]),
    (4, None, ["'It was me who broke Viktor Petrovich's mirror.' Now let's examine this part: ", ('nastya', 'Это'), ('nastya', 'я'), " starts it, 'it's me who'. ", ('nastya', 'разбила'), " is 'smashed' in a woman's form. Russians say 'broke the mirror to him', so ", ('nastya', 'Виктору'), ('nastya', 'Петровичу'), ' takes a special ending.']),
    (5, None, ["'And now they are fighting because of me.' Now let's break down the dialogue: ", ('nastya', 'из'), '-', ('nastya', 'за'), ('nastya', 'меня'), " is 'because of me', and ", ('nastya', 'ссорятся'), " means 'they quarrel with each other'."]),
    (6, None, ["'Wow!' We can inspect the dialogue: ", ('kostya', 'Ничего'), ('kostya', 'себе'), " is 'nothing to oneself', and nobody can say why it means 'wow', but it does. It's a good one to say when you are surprised."]),
    (7, None, ["'And what do we do now?' Russian says 'what to do', with no 'we' and no 'should'. The basic form of the action carries all of it."]),
    (8, None, ["'So, is everything still on for tonight?' Now let's inspect the sentence: ", ('kostya', 'Стало'), ('kostya', 'быть'), " means 'so', or 'it has become to be'. ", ('kostya', 'в'), ('kostya', 'силе'), " is 'in force', so 'still on'. Kostya is thinking only about the date."]),
    (9, None, ["'Kostya!' It is just his name, said as a telling-off. She uses his plain name here, not the pet name from the bar."]),
    (10, None, ["'How could you?' We can inspect the speech: ", ('nastya', 'можешь'), " is 'you can', so 'how can you'. In Russian it works as a reproach when someone has done something unthinkable."]),
    (11, None, ["'You only think about one thing!' We can focus on the phrase: ", ('nastya', 'об'), ('nastya', 'одном'), " uses a special word for 'about' before a vowel, which makes the wording easier to say. A small ", ('nastya', 'и'), " in the sentence gives 'only' extra bite."]),
]
