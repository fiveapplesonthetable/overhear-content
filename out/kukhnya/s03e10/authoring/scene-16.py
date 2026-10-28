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
    (0, None, "'Dima, I cannot take them right now.' Once she cannot take them right now, Vika can finally tell Barinov what she means."),
    (1, None, "'Forgive me, but for now I cannot.' Admitting that for now she cannot shows Vika being honest for a change."),
    (2, None, '\'Hello, friends, meet Sveta.\' With the work and date in play, Barinov keeps this short reply brisk and direct. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (3, None, "'Hello, very nice to meet you, I am Victoria.' Once very nice to meet Barinov she is Victoria, Vika can finally tell Barinov what she means."),
    (4, None, "'I am an actor, so everyone recognizes me.' Barinov explains that he is an actor so everyone recognizes him, keeping his voice calm and direct."),
    (5, None, '\'Let us drink to our acquaintance!\' Barinov declares that they should drink to their acquaintance as the tension in the room peaks. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (6, None, "'Hi, Katya, these flowers are for you.' Since these flowers are for Barinov, Lyova does not waste words on excuses."),
    (7, None, '\'Thank you, that is very sweet, Lyova.\' Mentioning that that is very sweet moves the talk in a new direction. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (8, None, "'There is no need to say anything, I know everything.' Noting that there is no need to say anything he knows everything keeps Lyova's side of the story simple and clear. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (9, None, "'Wait, what exactly do you know?' Questioning whether what exactly do Barinov knows is how Vika tests Barinov's story."),
    (10, None, "'I know the whole truth about France.' Lyova tells Barinov that he knows the whole truth about France without dressing it up."),
    (11, None, '\'What truth about France?\' With the moment and table hanging in the air, Vika puts Barinov on the spot. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
]
