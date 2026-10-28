# Authoring module for kukhnya-s06e03-scene-10.
ID = 'kukhnya-s06e03-scene-10'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 3
SCENE = 10
TITLE = 'Камера, мотор, дубль один!  (Camera, Rolling, Take One!)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.03'
SOURCE_FILE = 'sources/kukhnya/s06/e03.ru.srt'
INTRO = 'At halftime in the football match, the chefs head inside to cook lunch for the film crew, while Chef Barinov demands his hundred thousand rubles up front before stepping in front of the camera.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Holding a prop pistol and dressed as a movie villain, Barinov delivers his very first line on camera. See you next time!'
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('barinov', 'Так, все в ресторан, готовим обед!', 'Alright, everyone into the restaurant, we are cooking lunch!', [(162, 'Так, все в ресторан, готовим обед')], 'adapted'),
    ('denis', 'Это было несложно.', 'That was not hard.', [(164, 'Это было несложно')], 'exact'),
    ('denis', 'Мы договаривались до десяти, так что после обеда продолжим.', 'We agreed to play to ten, so we will continue after lunch.', [(165, 'мы договаривались до'), (165, 'так что после обеда продолжим')], 'adapted'),
    ('denis', 'Зачем продолжать свой позор?', 'Why prolong your disgrace?', [(166, 'свой позор?')], 'adapted'),
    ('nagiyev', 'Ну что, вы готовы?', 'Well, are you ready?', [(167, 'Ну что, готовы?')], 'adapted'),
    ('barinov', 'Подожди, а где деньги?', 'Wait, where is the money?', [(169, 'а где деньги?')], 'adapted'),
    ('nagiyev', 'Быстро учится, умный мальчик.', 'He learns fast, smart boy.', [(170, 'учиться, умный мальчик')], 'adapted'),
    ('nagiyev', 'Ничего еще не сняли, а уже деньги просит.', 'We have not filmed a thing yet, and he is already asking for money.', [(171, 'не сняли, а уже деньги')], 'adapted'),
    ('nagiyev', 'Пистолет, где его пистолет?', 'The pistol, where is his pistol?', [(173, 'Пистолет, где пистолет?')], 'adapted'),
    ('nagiyev', 'Готовы, давайте снимать!', "We are ready, let's film!", [(175, 'Готовы, давайте снимать')], 'exact'),
    ('nagiyev', 'Камера, мотор идет, поехали!', "Camera, rolling, let's go!", [(177, 'Камера, мотор'), (178, 'Мотор идет. Поехали')], 'adapted'),
    ('nagiyev', 'Сцена девять, дубль один, начали!', 'Scene nine, take one, action!', [(179, 'на девять дубль один'), (180, 'Начали!')], 'adapted'),
]
WALK = [
    (0, None, '\'Alright, everyone into the restaurant, we are cooking lunch!\' Emphasizing the restaurant in the exchange, Barinov chooses "restoran" ("restaurant") so Denis gets the point right away.'),
    (1, None, "'That was not hard.' Opening up earnestly at once, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (2, None, "'We agreed to play to ten, so we will continue after lunch.' Denis counters promptly toward Barinov, grounding the moment in plain reality."),
    (3, None, '\'Why prolong your disgrace?\' Addressing the disgrace in front of Nagiyev, Denis brings in "prodolzhat" ("to continue") to make the meaning unmistakable.'),
    (4, None, '\'Well, are you ready?\' Confirming how ready things are on the spot, Nagiyev links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (5, None, "'Wait, where is the money?' Barinov inquires straight out why things suddenly took this turn between them."),
    (6, None, '\'He learns fast, smart boy.\' Addressing the boy during the talk, Nagiyev centers the remark on "malchik" ("boy") without any extra fuss.'),
    (7, None, '\'We have not filmed a thing yet, and he is already asking for money.\' Talking about the money in front of Barinov, Nagiyev pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (8, None, "'The pistol, where is his pistol?' Nagiyev checks firmly why things suddenly took this turn between them."),
    (9, None, '\'We are ready, let\'s film!\' Pointing out how ready things are before Barinov, Nagiyev reaches for the Russian word "gotovy" ("ready", built from "gotovyy") right at the center of the line.'),
    (10, None, "'Camera, rolling, let's go!' Bringing up the camera in the exchange, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (11, None, "'Scene nine, take one, action!' Nagiyev speaks dryly around Barinov, keeping the focus on what actually matters here."),
]
