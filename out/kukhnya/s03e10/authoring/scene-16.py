# Authoring module for kukhnya-s03e10-scene-16.
ID = 'kukhnya-s03e10-scene-16'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 10
SCENE = 16
TITLE = 'Знакомство за столиком  (Introductions at the Table)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.10'
SOURCE_FILE = 'sources/kukhnya/s03/e10.ru.srt'
INTRO = "Vika declines Nagiyev's keys for now, and Chef Barinov arrives at their table introducing Sveta as his date. When Sveta greets Nagiyev by name, he nervously claims she only recognizes him as an actor. Meanwhile, Lyova approaches Katya."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Hearing the words 'I know about France,' Katya assumes Lyova found out she was expelled from culinary school—until Lyova explains what Max actually told him! See you next time!"
CLOSING = ('lyova', 'Увидимся!')
STORY = [
    ('vika', 'Дима, я не могу их взять.', 'Dima, I cannot take them right now.', [(256, 'Дима, я не могу ее взять')], 'adapted'),
    ('vika', 'Извини, но пока я не могу.', 'Forgive me, but for now I cannot.', [(258, 'Пока не могу')], 'adapted'),
    ('barinov', 'Здравствуйте, друзья, знакомьтесь, это Света.', 'Hello, friends, meet Sveta.', [(259, 'Здравствуйте, знакомьтесь'), (260, 'Это Света')], 'adapted'),
    ('vika', 'Здравствуйте, очень приятно, я Виктория.', 'Hello, very nice to meet you, I am Victoria.', [(261, 'Здравствуйте, это Виктория')], 'adapted'),
    ('barinov', 'Я актёр, поэтому меня все узнают.', 'I am an actor, so everyone recognizes me.', [(263, 'я актер, поэтому меня все узнают')], 'adapted'),
    ('barinov', 'Давайте выпьем за наше знакомство!', 'Let us drink to our acquaintance!', [(264, 'давайте выпьем за знакомство')], 'adapted'),
    ('lyova', 'Привет, Катя, это цветы для тебя.', 'Hi, Katya, these flowers are for you.', [(265, 'Привет')], 'adapted'),
    ('vika', 'Спасибо, это очень мило, Лёва.', 'Thank you, that is very sweet, Lyova.', [(266, 'Спасибо, это очень мило')], 'adapted'),
    ('lyova', 'Не надо ничего говорить, я всё знаю.', 'There is no need to say anything, I know everything.', [(267, 'Не надо ничего говорить, я все знаю')], 'adapted'),
    ('vika', 'Подожди, что именно ты знаешь?', 'Wait, what exactly do you know?', [(268, 'Что ты знаешь?')], 'adapted'),
    ('lyova', 'Я знаю всю правду про Францию.', 'I know the whole truth about France.', [(268, 'Про Францию')], 'adapted'),
    ('vika', 'Какую ещё правду про Францию?', 'What truth about France?', [(269, 'Про Францию?')], 'adapted'),
]
WALK = [
    (0, None, '\'Dima, I cannot take them right now.\' Vika counters warmly in this beat and chooses "vzyat" ("to take") so Barinov gets the point right away.'),
    (1, None, '\'Forgive me, but for now I cannot.\' Vika replies readily around Barinov and reaches for the Russian word "izvini" ("sorry, excuse me", built from "izvinit") right at the center of the line.'),
    (2, None, '\'Hello, friends, meet Sveta.\' Barinov evenly gives this formal greeting for Vika using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (3, None, '\'Hello, very nice to meet you, I am Victoria.\' Vika naturally offers this formal greeting as they meet using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (4, None, '\'I am an actor, so everyone recognizes me.\' Focusing on an actor on the spot, Barinov chooses "aktyor" ("actor") so Vika gets the point right away.'),
    (5, None, "'Let us drink to our acquaintance!' Barinov pushes back decisively with a nod, keeping the focus on what actually matters here."),
    (6, None, '\'Hi, Katya, these flowers are for you.\' Focusing on the flowers on the spot, Lyova leans on "tsvety" ("the flowers", a form of "tsvetok") to give the remark its edge.'),
    (7, None, '\'Thank you, that is very sweet, Lyova.\' Vika directly shares this word of thanks in the exchange using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (8, None, "'There is no need to say anything, I know everything.' Lyova replies evenly on the spot, letting the remark speak for itself."),
    (9, None, '\'Wait, what exactly do you know?\' Vika weighs in openly before Lyova and centers the thought on "podozhdi" ("wait", from "podozhdat") without wasting a word.'),
    (10, None, '\'I know the whole truth about France.\' Talking about the whole truth with Vika, Lyova chooses "pravdu" ("truth", from the root "pravda") so Vika hears the exact meaning.'),
    (11, None, "'What truth about France?' Vika asks promptly where this conversation is heading next."),
]
