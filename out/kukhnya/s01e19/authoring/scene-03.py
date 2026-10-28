# Authoring module for kukhnya-s01e19-scene-03.
ID = 'kukhnya-s01e19-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 3
TITLE = 'Снова допрос  (Interrogation again)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "The morning after, Max is surprised to find Kostya at home when he should be at work. Kostya has bad news, and Max has some of his own. We'll hear it in Russian first."
OPENER = "Now let's look at what was said."
TRANSITION = 'Now the whole conversation once more, from start to finish.'
OUTRO = "Both friends are in the same boat: no jobs, and troubles with women. Remember 'menya uvolili', literally 'me they fired', which is the standard way to say you've lost your job. See you next time!"
CLOSING = ('kostya', 'До свидания!')
STORY = [
    ('max', 'Что ты здесь делаешь?', 'What are you doing here?', [(29, 'Что ты здесь делаешь? Что не на работе?')], ''),
    ('max', 'Что не на работе?', "Why aren't you at work?", [(29, 'Что ты здесь делаешь? Что не на работе?')], ''),
    ('kostya', 'Опять допрос.', 'Another interrogation.', [(31, 'Опять допрос. Вы что, сговорились что ли?')], ''),
    ('kostya', 'Вы сговорились что ли?', 'Did you plan this or something?', [(31, 'Опять допрос. Вы что, сговорились что ли?')], ''),
    ('max', 'Я сегодня во вторую смену.', 'I am on the second shift today.', [(32, 'Я сегодня в вторую смену.')], ''),
    ('kostya', 'Отлично. Я с тобой поеду.', 'Great. I will go with you.', [(33, 'Отлично. Я с тобой поеду.')], ''),
    ('max', 'Может ты забыл,', 'Maybe you forgot,', [(34, 'Костян, может ты забыл, но у тебя вроде это.')], ''),
    ('kostya', 'Да, я помню.', 'Yeah, I remember.', [(35, 'Да, да, я помню, меня уволили. Мне надо забрать кое-что.')], ''),
    ('kostya', 'Меня уволили.', 'I got fired.', [(35, 'Да, да, я помню, меня уволили. Мне надо забрать кое-что.')], ''),
    ('max', 'А что ты не у Вики остался?', "Why didn't you stay at Vika's?", [(36, 'А что ты у Викини остался? Она меня не пустила.')], ''),
    ('max', 'Она меня не пустила.', "She wouldn't let me in.", [(36, 'А что ты у Викини остался? Она меня не пустила.')], ''),
    ('kostya', 'Она все усложнять начала.', 'She started making everything complicated.', [(39, 'Она все усложнять начала.')], ''),
]
WALK = [
    (0, None, "'What are you doing here?' 'Doing' finishes with 'esh' for the casual 'you'. 'Here' is the casual word."),
    (1, None, "'Why aren't you at work?' 'What' is used for 'why' in casual talk. 'At work' uses 'on' and an 'e' ending."),
    (2, None, "'Another interrogation.' 'Again' is just one word, and 'interrogation' is the same as in the last scene. Kostya has heard this one before."),
    (3, None, "'Did you two plan this, or what?' 'Plotted together' carries 's', for 'with each other'. 'Or something' is made with a small tag 'li' on 'what'."),
    (4, None, "'I'm on the second shift today.' 'On the second shift' is 'in the second shift', with the object form. 'Second' comes from 'two'."),
    (5, None, "'Great, I'll come with you.' 'I'll go' is a future form for going by vehicle. 'With you' is the irregular 'toboy'."),
    (6, None, "'Maybe you forgot.' 'Maybe' is a short word. 'Forgot' ends in the masculine 'l'."),
    (7, None, "'Yes, I remember.' 'I remember' is one word, with no 'I' needed. It's a flat reply."),
    (8, None, "'I got fired.' Russian says 'me they fired', putting 'me' first. 'They fired' has no 'they', only an ending."),
    (9, None, "'Why didn't you stay at Vika's?' 'At Vika's' is 'at Vika', with the name taking an 'i' ending. 'Stayed' ends in 'sya'."),
    (10, None, "'She didn't let me in.' The 'a' on 'let in' says it's a woman. 'Me' takes the 'a' form."),
    (11, None, "'She started making everything complicated.' 'Complicate' is built from 'complex', with a prefix. 'Started' finishes with 'a', for a woman."),
]
