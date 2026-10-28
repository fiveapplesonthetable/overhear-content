# Authoring module for kukhnya-s01e15-scene-17.
ID = 'kukhnya-s01e15-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 17
TITLE = 'Желание переехать  (Desire to Move In)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "Max has made up his mind, and he arrives at Vika's flat. He wants to move in with her, and he has trouble saying why. Hear it in Russian first."
OPENER = 'Slowly, once more.'
TRANSITION = 'Now the scene in one go.'
OUTRO = "Max has finally said what he wants. Vika's answer comes next."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Привет, Макс.', 'Hi, Max.', [(335, 'Привет.')], ''),
    ('max', 'Привет.', 'Hi.', [(335, 'Привет.')], ''),
    ('max', 'Я хочу переехать к тебе.', 'I want to move to your place.', [(336, 'Я хочу переехать к тебе.')], ''),
    ('vika', 'Тебе негде жить?', 'Do you have nowhere to live?', [(337, 'Что, негде жить?')], ''),
    ('max', 'Нет, у меня миллион вариантов.', 'No, I have a million options.', [(337, 'Да нет, просто...'), (338, 'Да миллион вариантов.')], ''),
    ('max', 'Костя зовёт меня назад.', 'Kostya is calling me back.', [(338, 'Просто Костя назад зовет,')], ''),
    ('max', 'Лёва тоже приглашает жить.', 'Leva is also inviting me to live.', [(338, 'Лёва тоже приглашает,')], ''),
    ('max', 'Но я готов жить с тобой.', 'But I am ready to live with you.', [(339, 'Но я готов жить с тобой.')], ''),
    ('vika', 'Что ты хочешь сказать?', 'What do you want to say?', [], ''),
    ('max', 'Я хочу жить с тобой.', 'I want to live with you.', [(340, 'В смысле, хочу.')], ''),
    ('max', 'Я не хочу быть без тебя.', 'I do not want to be without you.', [(341, 'В смысле, не хочу без тебя.')], ''),
    ('vika', 'Это очень приятно слышать.', 'That is very pleasant to hear.', [], ''),
    ('max', 'Правда?', 'Really?', [], ''),
    ('vika', 'Да, я тебе верю.', 'Yes, I believe you.', [], ''),
]
WALK = [
    (0, None, "'Hi, Max.' 'Privet' is the casual hello, and it's what Russians say to friends. She adds his name."),
    (1, None, "'Hi.' Max answers with the same word. Russians usually return 'privet' with 'privet'."),
    (2, None, "'I want to move to your place.' 'K tebe', literally 'to you', is how Russian says 'to your place'. 'Pereekhat' is 'to move house'."),
    (3, None, "'Do you have nowhere to live?' 'Negde' is 'gde', where, with 'ne' in front: 'there is nowhere'. Add 'zhit' and you have 'nowhere to live', with no 'you' or 'have' needed."),
    (4, None, "'No, I have a million options.' 'Million' stays the same, and the thing counted takes 'of' in the plural, 'variantov'. 'U menya' is 'at me'."),
    (5, None, "'Kostya is calling me back.' 'Zovyot' is 'calls', in the sense of calling someone to come. 'Nazad' is 'back', and 'menya' is 'me'."),
    (6, None, "'Lyova is also inviting me to live.' 'Priglashaet' is 'invites', followed by 'to live' in its basic shape. 'Tozhe' is 'also'."),
    (7, None, "'But I am ready to live with you.' 'Gotov' is 'ready' with no ending, the man's form; Vika would say 'gotova'. 'Zhit s toboy', to live with you, follows directly."),
    (8, None, "'What do you want to say?' She asks him directly. It's the Russian for 'what are you getting at?'."),
    (9, None, "'I want to live with you.' 'Khochu zhit s toboy': 'want', 'to live', 'with you'. In the show Max only manages 'v smysle, khochu', 'I mean, I want to'."),
    (10, None, "'I do not want to be without you.' 'Bez tebya' is 'without you', and 'bez' takes the 'a' form of 'you'. 'Byt' is 'to be'."),
    (11, None, "'That is very pleasant to hear.' 'Priyatno' is 'pleasant', and Russian needs no 'is' here. 'Slyshat' is 'to hear'."),
    (12, None, "'Really?' One word, 'pravda', the same as 'truth'. Max can hardly believe it."),
    (13, None, "'Yes, I believe you.' 'Tebe veryu' is 'to you I believe'. In Russian you believe 'to' somebody, so 'you' goes in the 'to' form."),
]
