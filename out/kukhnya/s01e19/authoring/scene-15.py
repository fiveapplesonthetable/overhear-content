# Authoring module for kukhnya-s01e19-scene-15.
ID = 'kukhnya-s01e19-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 15
TITLE = 'Спонсор и олигарх  (The Sponsor and the Oligarch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'director': 'Режиссёр', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Barinov is recording a cooking segment for television to advertise the restaurant's birthday party, but he keeps plugging the wrong thing and the director loses patience. Later he talks with Vika about who is coming. We'll hear it in Russian first."
OPENER = "Let's replay it step by step."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The party will be packed, and one very rich guest is on the list. Keep 'anshlag' in mind, since it's the Russian word for a full house at a theatre or a restaurant. See you next time!"
CLOSING = ('vika', 'До свидания!')
STORY = [
    ('barinov', 'Мы приготовили яйцо по-парижски.', 'We prepared a Parisian-style egg.', [(248, 'мы вместе с вами приготовили'), (248, 'яйцом по-парижски')], ''),
    ('barinov', 'Ждем вас в ресторане Клод Моне!', 'We wait for you at the Claude Monet restaurant!', [(250, 'вы можете попробовать в ресторане Клод Моне')], ''),
    ('director', 'Не снято! Вы не назвали спонсора!', "Don't cut! You didn't name the sponsor!", [(255, 'Не снято'), (256, 'вы ни разу не упомянули нашего спонсора')], ''),
    ('director', 'Вы уволены! Вон отсюда!', "You're fired! Get out of here!", [(258, 'Уволим'), (259, 'Вон отсюда')], ''),
    ('vika', 'Как дела, Виктор Петрович?', 'How are things, Viktor Petrovich?', [(263, 'как дела'), (264, 'Виктор Петрович')], ''),
    ('vika', 'Завтра будет аншлаг.', 'Tomorrow it will be packed.', [(265, 'Завтра будет аншлаг')], ''),
    ('vika', 'Даже Бьянка приедет.', 'Even Bianca will come.', [(265, 'Даже Бьянка приедет')], ''),
    ('barinov', 'Кто такая Бьянка?', 'Who is Bianca?', [(266, 'Кто')], ''),
    ('vika', 'Ее все знают.', 'Everyone knows her.', [(267, 'ее же все знают')], ''),
    ('barinov', 'У меня есть еще один козырь.', 'I have another ace up my sleeve.', [(272, 'У меня есть еще один козырной душ')], ''),
    ('barinov', 'Забронируй столик для Прохора Михайлова.', 'Book a table for Prokhor Mikhailov.', [(273, 'Забронируй столик')], ''),
    ('vika', 'Олигарх будет ужинать у нас?', 'The oligarch will dine with us?', [(274, 'Олигарх Прохора Михайлов будет ужинать у нас')], ''),
    ('barinov', 'Будет.', 'He will.', [(275, 'Будет')], ''),
    ('barinov', 'Его точно все знают.', 'Everyone definitely knows him.', [(275, 'его-то точно все знают')], ''),
]
WALK = [
    (0, None, "'We prepared a Parisian-style egg.' 'Parisian-style' is made with 'po' and a describing ending, 'po-parizhski'. 'We prepared' ends in 'li'."),
    (1, None, "'We're waiting for you at Claude Monet!' 'We wait' ends in 'yom', and 'for you' takes the 'a' form. 'At the restaurant' needs an 'e'."),
    (2, None, "'Cut! You didn't name the sponsor!' 'Not filmed' is a short neuter form, since a take is neuter. 'Sponsor' is borrowed."),
    (3, None, "'You're fired! Get out of here!' 'Fired' is a short plural form, with no 'are'. 'Von' is a one-word shove, 'out'."),
    (4, None, "'How are you, Viktor Petrovich?' 'How are matters' is the standard way to ask. Vika uses his name and patronymic."),
    (5, None, "'Tomorrow it'll be a full house.' 'Anshlag' is a borrowed German word used in theatres. 'It will be' is a single word."),
    (6, None, "'Even Bianca's coming.' 'Even' sits in front of the name. 'Will arrive' is a finished action, for arriving by vehicle."),
    (7, None, "'Who's Bianca?' The Russian is 'who such Bianca', and 'such' is feminine. It makes the question sound dismissive."),
    (8, None, "'Everyone knows her.' 'Her' goes first, and 'everyone knows' follows. That puts the stress on her."),
    (9, None, "'I've got another ace up my sleeve.' 'Trump card' is a card-game term. 'Another' is 'one more'."),
    (10, None, "'Book a table for the oligarch.' 'Book' is borrowed from French, and the 'irovat' ending makes it a Russian action word. 'Table' is a little table."),
    (11, None, "'Will the oligarch dine with us?' 'Oligarch' is a borrowed word. 'Dine' is built from the word for supper."),
    (12, None, "'He will.' Russians say yes by repeating the verb. Here the single word 'will be' is the answer."),
    (13, None, "'Everyone definitely knows him.' 'Him' comes first, as 'ego'. 'Definitely' is a handy one-word adverb."),
]
