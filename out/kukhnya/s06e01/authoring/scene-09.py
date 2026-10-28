# Authoring module for kukhnya-s06e01-scene-09.
ID = 'kukhnya-s06e01-scene-09'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 9
TITLE = "Золотой кирпич от олигарха  (The Oligarch's Golden Brick)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'eleonora': 'Элеонора', 'guest': 'Гость', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = 'Wealthy oligarch Danila Alyokhin arrives at the hotel lobby with a remarkably heavy wedding gift box for Eleonora and Nagiyev: a red brick containing a solid gold bar to fund their St. Petersburg hotel project.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Eleonora is thrilled by the investor's generosity, until Nagiyev turns around and sees who the oligarch's new wife actually is. Until next time!"
CLOSING = ('eleonora', 'Всего хорошего!')
STORY = [
    ('eleonora', 'Дима, олигарх приехал!', 'Dima, the oligarch has arrived!', [(151, 'Дима, Дима, Дима')], 'adapted'),
    ('eleonora', 'Как я рада вас видеть!', 'How glad I am to see you!', [(153, 'как рада вас видеть')], 'adapted'),
    ('guest', 'Мое поздравление молодоженам.', 'My congratulations to the newlyweds.', [(154, 'Мое поздравление молодоженам')], 'exact'),
    ('eleonora', 'Одно ваше присутствие — это уже подарок.', 'Your presence alone is already a gift.', [(155, 'Одно ваше присутствие, это уже подарок')], 'adapted'),
    ('nagiyev', 'Ух ты, тяжелый подарок.', 'Wow, it is a heavy gift.', [(156, 'Ух ты, тяжелый')], 'adapted'),
    ('nagiyev', 'Там золотой слиток?', 'Is there a gold ingot in there?', [(157, 'золотой слиток')], 'adapted'),
    ('guest', 'Можете взглянуть.', 'You may take a look.', [(158, 'Можете взглянуть')], 'exact'),
    ('nagiyev', 'Это просто кирпич.', 'It is just a brick.', [(159, 'Кирпич')], 'adapted'),
    ('guest', 'Это непростой кирпич, а внутри золотой слиток.', 'It is no ordinary brick, and inside is a gold ingot.', [(160, 'Это непростой кирпич'), (161, 'а внутри золотой слиток')], 'adapted'),
    ('guest', 'И я готов его финансировать.', 'And I am ready to finance it.', [(163, 'И я готов его финансировать')], 'exact'),
    ('eleonora', 'Боже мой, спасибо вам огромное!', 'Oh my goodness, thank you so much!', [(164, 'Боже мой, спасибо')], 'adapted'),
    ('guest', 'Я приехал с супругой, а вот она.', 'I arrived with my wife, and here she is.', [(170, 'Нет, с супругой'), (171, 'А вот, кстати, она')], 'adapted'),
]
WALK = [
    (0, None, "'Dima, the oligarch has arrived!' Eleonora weighs in plainly without holding back, saying out loud what both of them already know."),
    (1, None, '\'How glad I am to see you!\' Eleonora underscores this direct piece at once: "rada" means "glad", and it carries the main weight of what Eleonora is saying.'),
    (2, None, "'My congratulations to the newlyweds.' The guest hands over the comment right away: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (3, None, "'Your presence alone is already a gift.' Eleonora continues at once with a sigh, letting the remark speak for itself."),
    (4, None, '\'Wow, it is a heavy gift.\' Nagiyev chooses this sharp word at once: "tyazhelyy" means "heavy" (from "tyazhyolyy"), giving the line its exact edge.'),
    (5, None, '\'Is there a gold ingot in there?\' Nagiyev shapes this line without pause: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (6, None, "'You may take a look.' The guest steps in plainly to settle things, keeping the focus on what actually matters here."),
    (7, None, '\'It is just a brick.\' Nagiyev focuses on one clear term toward the guest: "kirpich" means "brick", and it carries the main weight of what Nagiyev is saying.'),
    (8, None, '\'It is no ordinary brick, and inside is a gold ingot.\' The guest drops that reply without pause: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (9, None, "'And I am ready to finance it.' The guest reacts plainly across the room, leaving no doubt about where he stands."),
    (10, None, '\'Oh my goodness, thank you so much!\' Eleonora highlights one colorful piece with the guest: "ogromnoye" means "huge, so very much" (from "ogromnyy"), giving the line its exact edge.'),
    (11, None, "'I arrived with my wife, and here she is.' The guest pushes back at once beside Nagiyev, leaving no doubt about where he stands."),
]
