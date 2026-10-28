# Authoring module for kukhnya-s01e12-scene-02.
ID = 'kukhnya-s01e12-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 2
TITLE = 'Фальшивая боль  (Fake Pain)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = "In the restaurant corridor, Max suddenly grabs his right side and groans in pain. When a concerned Victoria rushes over to help him, he miraculously recovers and reveals his true intentions. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine this tricky conversation in the corridor line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Furious at being tricked into worrying about his health, Victoria storms off, leaving Max standing alone with his cinema tickets. Next time you watch the episode, listen for the Russian expressions for 'ticket' and 'hurts' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Ай! Как мне больно в животе!', 'Ouch! How it hurts me in the stomach!', [(8, 'Блин, что это?'), (12, 'Ой, что это?')], ''),
    ('vika', 'Макс, что такое? Тебе очень больно?', 'Max, what is it? Does it hurt you a lot?', [(9, 'Что такое? Больно так?')], ''),
    ('max', 'Я не знаю, что это такое.', 'I do not know what this is.', [(10, 'Не знаю, что это.')], ''),
    ('vika', 'Ой, с правой стороны это очень плохо!', 'Oh, on the right side this is very bad!', [(11, 'Боже мой.')], ''),
    ('max', 'Боже мой, как мне сейчас больно.', 'My god, how much it hurts me now.', [], ''),
    ('vika', 'Давай я быстро вызову тебе врача.', 'Let me quickly call a doctor for you.', [], ''),
    ('max', 'Нет, серьёзно, не надо вызывать врачей.', 'No, seriously, do not call doctors.', [(10, 'Нет, всё нормально, всё нормально.')], ''),
    ('vika', 'Почему? Тебе же нужна срочная помощь.', 'Why? You need urgent help after all.', [], ''),
    ('max', 'Смотри, вот два билета в кино.', 'Look, here are two tickets to the cinema.', [(13, 'Билетики. Пойдем в кино, а?')], ''),
    ('vika', 'Ну ты и придурок, честное слово!', 'Well you are a jerk, honestly!', [(14, 'Дебил.')], ''),
    ('max', 'Пойдём в кино сегодня вечером, а?', 'Shall we go to the cinema tonight, eh?', [(13, 'Пойдем в кино, а?')], ''),
    ('vika', 'Ты настоящий идиот, я никуда не пойду!', 'You are a real idiot, I will not go anywhere!', [(14, 'Дебил.')], ''),
    ('max', 'Ладно, тогда я пойду в кино один.', 'Alright, then I will go to the cinema alone.', [], ''),
]
WALK = [
    (0, None, "'Ouch! How it hurts me in the stomach!' Max cries out because his stomach hurts a lot. Literally he says how it is painful to me in the stomach."),
    (1, None, "'Max, what is it? Does it hurt you a lot?' Vika asks Max what is wrong and if he is in a lot of pain."),
    (2, None, "'I do not know what this is.' Max says he does not know what is happening to him."),
    (3, None, "'Oh, on the right side this is very bad!' Vika worries because pain on the right side can be dangerous."),
    (4, None, "'My god, how much it hurts me now.' Max groans about how much pain he is feeling right now."),
    (5, None, "'Let me quickly call a doctor for you.' Vika offers to get a doctor for him right away."),
    (6, None, "'No, seriously, do not call doctors.' Max tells her not to call any doctors. He is pretending to be sick."),
    (7, None, "'Why? You need urgent help after all.' Vika asks why because she thinks he needs help right now."),
    (8, None, "'Look, here are two tickets to the cinema.' Max suddenly shows her two movie tickets. His pain was just a trick."),
    (9, None, "'Well you are a jerk, honestly!' Vika calls him a jerk for tricking her. She is really annoyed."),
    (10, None, "'Shall we go to the cinema tonight, eh?' Max invites her to the movies for tonight."),
    (11, None, "'You are a real idiot, I will not go anywhere!' Vika refuses to go anywhere with him because he acted like an idiot."),
    (12, None, "'Alright, then I will go to the cinema alone.' Max says he will just go to the movies by himself then."),
]
