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
    (0, None, "'Dima, the oligarch has arrived!' Eleonora fires back plainly across the room, letting the remark speak for itself."),
    (1, None, '\'How glad I am to see you!\' Explaining how glad she is before the guest, Eleonora puts the emphasis on "rada" ("glad") in the middle of the talk.'),
    (2, None, "'My congratulations to the newlyweds.' Touching on the newlyweds before Eleonora, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (3, None, "'Your presence alone is already a gift.' Bringing up the presence with a shrug, Eleonora keeps the guest's attention locked on what matters."),
    (4, None, '\'Wow, it is a heavy gift.\' Insisting on how heavy things are in the exchange, Nagiyev brings in "tyazhelyy" ("heavy", from "tyazhyolyy") as the key Russian word here.'),
    (5, None, '\'Is there a gold ingot in there?\' Stressing how golden things are beside the guest, Nagiyev links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (6, None, "'You may take a look.' The guest speaks up plainly in their talk, so Nagiyev knows he is not just making small talk."),
    (7, None, '\'It is just a brick.\' Underscoring a brick beside the guest, Nagiyev puts the emphasis on "kirpich" ("brick") in the middle of the talk.'),
    (8, None, '\'It is no ordinary brick, and inside is a gold ingot.\' Underscoring how golden things are beside Nagiyev, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (9, None, "'And I am ready to finance it.' The guest answers plainly in this moment, making his position completely clear."),
    (10, None, '\'Oh my goodness, thank you so much!\' Mentioning the good with the guest, Eleonora puts the weight on "ogromnoye" ("huge, so very much", from "ogromnyy") as the exchange unfolds.'),
    (11, None, '\'I arrived with my wife, and here she is.\' Focusing on his wife right here, the guest puts the weight on "suprugoy" ("wife, spouse", from "supruga") as the exchange unfolds.'),
]
