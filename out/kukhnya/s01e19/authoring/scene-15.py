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
INTRO = "To advertise the restaurant's birthday, Chef Barinov is filming a cooking segment for TV. But there's a problem: he keeps promoting his restaurant instead of the sponsor's product. Later, he talks to Vika about the guest list."
OPENER = "Now let's go back through the exchange around The Sponsor and the Oligarch line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The Chef always has a backup plan. Let's see if the oligarch really shows up. Next time you watch the episode, listen for the Russian expressions for 'to prepare' and 'egg' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'До встречи!')
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
    (0, None, "'We prepared a Parisian-style egg.' Barinov announces to the camera that they prepared the special egg."),
    (1, None, "'We wait for you at the Claude Monet restaurant!' The chef enthusiastically invites everyone. We skip 'the' in Russian."),
    (2, None, "'Don't cut! You didn't name the sponsor!' The director yells that he forgot to name their sponsor."),
    (3, None, "'You're fired! Get out of here!' The director kicks him out of the studio. The word for 'are' is skipped."),
    (4, None, "'How are things, Viktor Petrovich?' Later, Vika greets the Chef at the restaurant."),
    (5, None, "'Tomorrow it will be packed.' The word for 'packed' comes from German and means a full house. We use 'it' in English, but Russian relies on the context."),
    (6, None, "'Even Bianca will come.' Vika excitedly mentions that even Bianca is coming to the party."),
    (7, None, "'Who is Bianca?' The Chef is not impressed. He adds a word to mean 'what kind of person'."),
    (8, None, "'Everyone knows her.' Vika defends her VIP guest. The object 'her' comes first in the sentence."),
    (9, None, "'I have another ace up my sleeve.' Barinov claims he has another trick up his sleeve."),
    (10, None, "'Book a table for Prokhor Mikhailov.' Barinov orders her to book a table for the wealthy oligarch."),
    (11, None, "'The oligarch will dine with us?' Vika is shocked. To dine means 'to have supper' in Russian."),
    (12, None, "'He will.' Barinov confirms the oligarch will definitely attend."),
    (13, None, "'Everyone definitely knows him.' He takes a jab at Bianca's fame. The word 'him' is placed at the front."),
]
