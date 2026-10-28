# Authoring module for kukhnya-s01e19-scene-04.
ID = 'kukhnya-s01e19-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 4
TITLE = 'Экскурсия для Игоря  (Tour for Igor)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nagiyev': 'Нагиев', 'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Nagiyev is showing his friend Igor around Claude Monet, boasting about everything. He calls the staff by the wrong names and proudly introduces his art director. We'll hear it in Russian first."
OPENER = "Let's go through it one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Nagiyev has no idea who half his staff are, but he makes the tour sound grand. 'Voobshche-to' is a handy phrase for 'actually' when you're correcting someone. See you next time!"
CLOSING = ('vika', 'До свидания!')
STORY = [
    ('nagiyev', 'Вот, Игорь.', 'Here you go, Igor.', [(44, 'Вот, Игорек, это и есть оазис французской кухни.')], ''),
    ('nagiyev', 'Это оазис французской кухни.', 'This is an oasis of French cuisine.', [(44, 'Вот, Игорек, это и есть оазис французской кухни.')], ''),
    ('nagiyev', 'Анклав качества.', 'A bastion of quality.', [(45, 'Анклав качества.')], ''),
    ('nagiyev', 'Сколько сил вложено сюда.', 'So much effort went into this place.', [(46, 'Ой, сколько сил вложено сюда, сколько любви, энергии.')], ''),
    ('nagiyev', 'Официант, как родной ребенок.', 'A waiter is like my own child.', [(48, 'Официант, как родной ребенок.')], ''),
    ('nagiyev', 'О, привет, Виляш.', 'Oh, hi, Vilyash.', [(49, 'О, привет, Виляш.')], ''),
    ('nastya', 'Я Настя, вообще-то.', 'I am Nastya, actually.', [(50, 'Я Настя, вообще-то.')], ''),
    ('nagiyev', 'Новенькая, наверное.', 'She must be new.', [(52, 'Новенькая, наверное.')], ''),
    ('nagiyev', 'Ну, пойдем дальше.', "Well, let's keep going.", [(53, 'Ну, пойдем дальше.')], ''),
    ('nagiyev', 'Сделай нам два кофе.', 'Make us two coffees.', [(54, 'Здрасте, здрасте. Сделай-ка нам два кофе.')], ''),
    ('nagiyev', 'Это Виктория Сергеевна.', 'This is Viktoria Sergeyevna.', [(55, 'Это Виктория Сергеевна, так сказать, арт-лицо,')], ''),
    ('nagiyev', 'Арт-директор нашего ресторана.', 'The art director of our restaurant.', [(56, 'арт-директор нашего ресторана.')], ''),
    ('vika', 'Добрый день.', 'Good afternoon.', [(59, 'Добрый день. Здравствуйте, Игорь.')], ''),
]
WALK = [
    (0, None, "'Here you go, Igor.' The small word 'vot' points at the dining room. Igor's name needs no change here."),
    (1, None, "'This is an oasis of French cuisine.' 'Of French cuisine' has an 'oy' ending on 'French' and an 'i' on 'cuisine'. 'Oasis' is a borrowed word."),
    (2, None, "'A bastion of quality.' 'Enclave' is borrowed too. 'Of quality' needs an 'a' ending."),
    (3, None, "'So much effort has gone into this place.' 'How much' is used here as an exclamation. 'Effort' is literally 'strengths'."),
    (4, None, "'A waiter is like my own child.' 'Own' here means 'by blood', which makes the staff almost family. 'Child' is an irregular word."),
    (5, None, "'Oh, hi, Vilyash.' He greets the wrong person with the casual hello. The name he uses is wrong, which is the joke."),
    (6, None, "'I'm Nastya, actually.' 'Actually' has the little 'to' added, which sharpens the correction. There's no 'am'."),
    (7, None, "'She must be new.' 'New girl' is made by adding a small ending to 'new'. 'Probably' is one word."),
    (8, None, "'Well, let's keep going.' 'We'll go' works as 'let's go'. 'Further' is another handy small word."),
    (9, None, "'Make us two coffees.' Coffee is masculine and never changes, so 'two' takes its masculine form. 'Make' is the casual command."),
    (10, None, "'This is Viktoria Sergeyevna.' He gives her first name and patronymic, the formal way. There's no 'is'."),
    (11, None, "'The art director of our restaurant.' 'Art director' is a hyphenated compound. 'Of our restaurant' takes an 'ogo' and an 'a'."),
    (12, None, "'Good afternoon.' The greeting means 'kind day'. Vika keeps it short and formal."),
]
