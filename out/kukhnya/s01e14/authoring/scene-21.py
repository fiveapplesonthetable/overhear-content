# Authoring module for kukhnya-s01e14-scene-21.
ID = 'kukhnya-s01e14-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 21
TITLE = 'Дегустатор  (The Taster)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'Jacques has had too much to drink and is now singing in the dining room. Nagiyev decides to judge the dish himself. Listen in Russian first.'
OPENER = 'Once more, from the singing to the tasting.'
TRANSITION = 'Now the whole scene in one go.'
OUTRO = 'Jacques is out of action, and the owner is about to taste the dish. Does it deserve the fuss? Speak soon.'
CLOSING = ('nagiyev', 'До встречи!')
STORY = [
    ('nagiyev', 'Гости громко исполняют Марсельезу.', 'The guests are loudly singing La Marseillaise.', [(302, 'Исполняют Марсельезу')], ''),
    ('vika', 'Кажется, наш французский гость устал.', 'It seems our French guest is tired.', [], ''),
    ('nagiyev', 'Давайте дружно извиним Жака.', 'Let us all forgive Jacques.', [(303, 'Давайте извиним Жак')], ''),
    ('nagiyev', 'Он, видимо, сегодня сильно накушался.', 'He apparently had too much today.', [(303, 'он, видимо'), (303, 'сильно накушался')], ''),
    ('nagiyev', 'Даже без нашего главного блюда.', 'Even without our main dish.', [(303, 'и без нашего блюда')], ''),
    ('vika', 'Он уже не может оценивать еду.', 'He can no longer judge the food.', [], ''),
    ('nagiyev', 'Поэтому он сейчас просто поёт.', 'That is why he is just singing right now.', [], ''),
    ('nagiyev', 'Ну что ж, дорогие друзья.', 'Well then, dear friends.', [(304, 'Ну что ж')], ''),
    ('nagiyev', 'Тогда главным дегустатором буду я.', 'Then I will be the main taster.', [(304, 'тогда дегустатором буду я')], ''),
    ('nagiyev', 'Я сам попробую это блюдо.', 'I will taste this dish myself.', [], ''),
    ('vika', 'Надеюсь, блюдо вам очень понравится.', 'I hope you will really like the dish.', [], ''),
    ('nagiyev', 'Посмотрим, что приготовил наш повар.', 'Let us see what our chef cooked.', [], ''),
]
WALK = [
    (0, None, ["'The guests are loudly singing La Marseillaise.' The anthem is what is being sung, so we hear ", ('nagiyev', 'Марсельезу'), '. And ', ('nagiyev', 'исполняют'), ' is a formal verb for singing or playing.']),
    (1, None, ["'It seems our French guest is tired.' Russians use the past tense ", ('vika', 'устал'), ' to say someone is tired. ', ('vika', 'Кажется'), ', meaning it seems, opens the sentence with a comma.']),
    (2, None, ["'Let us all forgive Jacques.' Now we can focus on this part: ", ('nagiyev', 'дружно'), ' means all together. Jacques becomes ', ('nagiyev', 'Жака'), ' because he is the one being forgiven.']),
    (3, None, ["'He apparently had too much today.' We can consider this part: ", ('nagiyev', 'видимо'), ' means apparently. ', ('nagiyev', 'накушался'), " means to eat one's fill, and here it is a polite joke for too much to drink."]),
    (4, None, ["'Even without our main dish.' After without, the dish takes its of form, so the main dish becomes ", ('nagiyev', 'главного'), ('nagiyev', 'блюда'), '.']),
    (5, None, ["'He can no longer judge the food.' Now we can focus on the phrase: ", ('vika', 'уже'), ('vika', 'не'), ' is the Russian for no longer. ', ('vika', 'оценивать'), ' is to judge or rate.']),
    (6, None, ["'That is why he is just singing right now.' We will consider this part: ", ('nagiyev', 'Поэтому'), ' means that is why. ', ('nagiyev', 'поёт'), ' means sings.']),
    (7, None, ["'Well then, dear friends.' Now let's break down this line: ", ('nagiyev', 'Ну'), ('nagiyev', 'что'), ('nagiyev', 'ж'), ' is a drawn-out well then, a favourite of people who are about to make a speech.']),
    (8, None, ["'Then I will be the main taster.' After I will be, the job takes the as ending, giving us ", ('nagiyev', 'главным'), ('nagiyev', 'дегустатором'), '. The I comes last for drama, as ', ('nagiyev', 'я'), '.']),
    (9, None, ["'I will taste this dish myself.' Now let's focus on the sentence: ", ('nagiyev', 'сам'), ' is myself. ', ('nagiyev', 'попробую'), ' is I will try, and for food it also means I will taste.']),
    (10, None, ["'I hope you will really like the dish.' We can look at the speech: ", ('vika', 'Надеюсь'), ' means I hope. ', ('vika', 'понравится'), ' means it will be pleasing.']),
    (11, None, ["'Let us see what our chef cooked.' Let us look at this line: ", ('nagiyev', 'Посмотрим'), ' means we will look, and Russians use it as let us see. ', ('nagiyev', 'повар'), ' supplies an everyday word for a cook.']),
]
