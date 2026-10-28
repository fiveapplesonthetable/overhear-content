# Authoring module for domashniy-arest-s01e04-scene-09.
ID = 'domashniy-arest-s01e04-scene-09'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 9
TITLE = 'Вафельный рожок  (The Waffle-Cone Costume)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fan': 'Девушка', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "Last time, Arkady saw that the video of Samson throwing him out the window had four million views and told a stunned Pasha that Samson would be the next mayor of Sineozersk. Meanwhile, out on the street, Samson has no idea he is famous: he is standing miserably inside a giant waffle-cone costume while Nina lectures him. Let's listen in Russian first."
OPENER = "Let's go back through the scene. Outside the children's cafe, Samson glares out from inside a giant foam waffle cone."
TRANSITION = "Let's hear the whole street scene again from start to finish."
OUTRO = 'So poor Samson goes from feeling like a street clown to being mobbed by fans for selfies — and once he learns that Yulia uploaded the video, he hurries straight home in a rage. See you next time!'
CLOSING = ('nina', 'Пока!')
STORY = [
    ('samson', 'Я что, клоун, что ли?', 'What am I, a clown or something?', [(258, 'Я что, клоун, что ли')], ''),
    ('nina', 'Не клоун, а вафельный рожок!', 'Not a clown, a waffle cone!', [(259, 'Не клоун, а вафельный рожок')], ''),
    ('samson', 'Не буду я вафлей! Я сейчас другую работу найду.', "I won't be a waffle! I'll find another job right now.", [(260, 'Не буду я'), (260, 'Я сейчас другую работу найду')], "cue 260 slip 'вафлями' -> 'вафлей'"),
    ('nina', 'Другую работу найдёшь — с этой уйдёшь.', "When you find another job, you'll leave this one.", [(261, 'Другую найдешь, с этой')], "cue 261 'уволишься' simplified to A1 'уйдёшь'"),
    ('samson', 'Нина, ты не понимаешь, что это унизительно?', "Nina, don't you understand that this is humiliating?", [(262, 'ты не понимаешь, что это'), (262, 'унизительно')], "cue 262 slip 'Инна' -> 'Нина'"),
    ('nina', 'Унизительно? А быть безработным — это не унизительно?', "Humiliating? And being unemployed — isn't that humiliating?", [(263, 'Унизительно? А быть безработным, это не унизительно')], ''),
    ('fan', 'Здравствуйте! Извините, а вы случайно не Самсон?', 'Hello! Excuse me, are you by any chance Samson?', [(264, 'Здравствуйте. Извините'), (264, 'а вы случайно не')], "cue 264 slip 'Солсон' -> 'Самсон'"),
    ('samson', 'Что? Да, я Иван Самсонов.', "What? Yes, I'm Ivan Samsonov.", [(265, 'Иван')], "cue 265 'Чего? Иван Васильевич, я...' made clear"),
    ('fan', 'Это он, ребята, Самсон! Ребята, идите сюда!', "It's him, guys, Samson! Guys, come over here!", [(267, 'Это он, ребята'), (268, 'Ребята, идите сюда')], "cue 267 slip 'Солсон' -> 'Самсон'"),
    ('fan', 'Давайте быстрее! А можно с вами фотографию, пожалуйста?', 'Hurry up! May I take a photo with you, please?', [(269, 'Давайте быстрее'), (271, 'А можно с вами фотографию, пожалуйста')], ''),
    ('samson', 'Что происходит? Я не пойму.', "What is going on? I don't understand.", [(274, 'Что происходит? Я не пойму')], ''),
    ('nina', 'Ты ещё не понял? Ты теперь знаменитый!', "Haven't you understood yet? You're famous now!", [(276, 'ты еще не понял')], "'Ты теперь знаменитый!' added to explain the crowd"),
    ('nina', 'Алло, Юля, я перезвоню!', "Hello, Yulia, I'll call you back!", [(277, 'я перезвоню')], "cue 277 'Юль' -> 'Юля'"),
]
WALK = [
    (0, None, "'What am I, a clown or something?' The two particles at the end add a tone of annoyed disbelief: 'or something?'. Nina corrects him matter-of-factly."),
    (1, None, "'Not a clown, a waffle cone!' Literally 'a waffle little horn', which is what Russian calls an ice-cream cone. Samson tries to pull the costume off."),
    (2, None, "'I won't be a waffle! I'll find another job right now.' Notice the 'with/as' ending on 'waffle' after the future 'I will not be'. Nina blocks his way."),
    (3, None, "'When you find another job, you'll leave this one.' Two single-action form futures side by side, without 'when': 'you will find another, you will leave from this one'."),
    (4, None, "'Nina, don't you understand that this is humiliating?' Meanwhile, Nina fires the word right back at him."),
    (5, None, "'Humiliating? And being unemployed — isn't that humiliating?' Again, after 'to be', the adjective 'unemployed' takes the 'with/as' ending. Just then, a young woman on the pavement stops and stares at Samson's face."),
    (6, None, "'Hello! Excuse me, are you by any chance Samson?' The adverb in the middle literally means 'by chance' or 'accidentally'. Samson blinks in surprise."),
    (7, None, "'What? Yes, I'm Ivan Samsonov.' The young woman turns and waves to her friends down the street."),
    (8, None, "'It's him, guys, Samson! Guys, come over here!' Suddenly a whole group of young people comes running with their phones out."),
    (9, None, "'Hurry up! May I take a photo with you, please?' Literally 'is it possible with you a photograph, please?'. Samson stands frozen inside his giant waffle cone as everyone poses with him."),
    (10, None, "'What is going on? I don't understand.' He has not seen the internet yet today."),
    (11, None, "'Haven't you understood yet? You're famous now!' At that moment Nina's phone rings: it is their daughter Yulia."),
    (12, None, "'Hello, Yulia, I'll call you back!' The prefix on the verb means doing something again or back: 'call back'."),
]
