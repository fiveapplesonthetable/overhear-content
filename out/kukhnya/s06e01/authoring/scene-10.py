# Authoring module for kukhnya-s06e01-scene-10.
ID = 'kukhnya-s06e01-scene-10'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 10
TITLE = 'Неожиданная гостья и пианист  (The Unexpected Guest and the Pianist)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'eleonora': 'Элеонора', 'katya': 'Катя', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = "After the oligarch introduces his wife Kristina—Nagiyev's own ex-wife—Katya confronts Eleonora for firing Denis, forcing Mikhail to improvise an excuse on the spot."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Katya insists it is merely a matter of principle, while Mikhail scrambles to bring Denis back before the ceremony. See you next time!'
CLOSING = ('katya', 'Пока!')
STORY = [
    ('eleonora', 'Давайте я вам покажу ваш номер.', 'Let me show you to your suite.', [(175, 'Давайте я вам покажу ваш номер')], 'exact'),
    ('mikhail', 'Выручай, мне срочно нужен пианист на вечер.', 'Help me out, I urgently need a pianist for the evening.', [(177, 'Выручай, мне срочно нужен пианист на вечер')], 'exact'),
    ('katya', 'Это так ты не вмешиваешься в мою личную жизнь?', 'Is this how you do not interfere in my personal life?', [(179, 'Это так ты не вмешиваешься в мою личную жизнь?')], 'exact'),
    ('eleonora', 'Успокойся, Катя.', 'Calm down, Katya.', [(180, 'Успокойся')], 'adapted'),
    ('katya', 'Ты сама взяла и уволила Дениса.', 'You went ahead and fired Denis yourself.', [(181, 'а сама взяла и уволила Дениса')], 'adapted'),
    ('eleonora', 'Может быть, он сам ушел?', 'Maybe he left on his own?', [(183, 'может быть, он сам ушел?')], 'adapted'),
    ('eleonora', 'Миша, а где пианист?', 'Misha, where is the pianist?', [(185, 'Миша, а где пианист?')], 'exact'),
    ('mikhail', 'Какой пианист?', 'Which pianist?', [(186, 'Какой пианист?')], 'exact'),
    ('eleonora', 'Пианист, которого Дима привел, найди его.', 'The pianist whom Dima brought, find him.', [(186, 'Пианист, которого Дима привел'), (187, 'Найди его')], 'adapted'),
    ('mikhail', 'Я его отправил переодеваться, ужасный пиджак.', 'I sent him to change clothes, an awful jacket.', [(189, 'Я его отправил переодеваться. Ужасный пиджак')], 'adapted'),
    ('eleonora', 'Ну видишь, будет твой Денис.', 'Well you see, your Denis will be here.', [(190, 'Ну, видишь, будет твой Денис')], 'adapted'),
    ('katya', 'Ты прекрасно знаешь, что мы расстались.', 'You know very well that we broke up.', [(192, 'Ты прекрасно знаешь, что мы расстались')], 'exact'),
]
WALK = [
    (0, None, '\'Let me show you to your suite.\' Emphasizing the number with Mikhail, Eleonora reaches for the Russian word "nomer" ("number") right at the heart of the line.'),
    (1, None, '\'Help me out, I urgently need a pianist for the evening.\' Mentioning a pianist in the exchange, Mikhail centers the remark on "pianist" ("pianist") without any extra fuss.'),
    (2, None, "'Is this how you do not interfere in my personal life?' Katya quizzes curiously to see how Eleonora will answer on the spot."),
    (3, None, '\'Calm down, Katya.\' Eleonora counters promptly on the spot and leans on "uspokoysya" ("calm down", a form of "uspokoitsya") to give the remark its edge.'),
    (4, None, "'You went ahead and fired Denis yourself.' Katya speaks pointedly facing Eleonora, without trying to dress up how she really feels."),
    (5, None, "'Maybe he left on his own?' Eleonora challenges bluntly if there is more going on behind the scenes."),
    (6, None, '\'Misha, where is the pianist?\' Highlighting the pianist to Mikhail, Eleonora puts the emphasis on "pianist" ("pianist") in the middle of the talk.'),
    (7, None, '\'Which pianist?\' Turning to the pianist in the exchange, Mikhail puts the question word "kakoy" right at the start so Eleonora hears the focus immediately.'),
    (8, None, "'The pianist whom Dima brought, find him.' Eleonora answers honestly with a shrug, to clear the air between them once and for all."),
    (9, None, '\'I sent him to change clothes, an awful jacket.\' Highlighting an awful jacket in the exchange, Mikhail brings in "pereodevatsya" ("to get changed") to make the meaning unmistakable.'),
    (10, None, "'Well you see, your Denis will be here.' Eleonora responds honestly without holding back, to clear the air between them once and for all."),
    (11, None, "'You know very well that we broke up.' Katya opens up calmly in their talk, keeping the focus on what actually matters here."),
]
