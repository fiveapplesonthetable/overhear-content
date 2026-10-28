# Authoring module for kukhnya-s03e12-scene-06.
ID = 'kukhnya-s03e12-scene-06'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 12
SCENE = 6
TITLE = 'Прапорщик Задов и деньги  (Ensign Zadov and Money)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.12'
SOURCE_FILE = 'sources/kukhnya/s03/e12.ru.srt'
INTRO = "Upstairs at Kirill Ilyich's door, Dmitry Nagiyev introduces himself and offers peace. Unfortunately, the retired officer recognizes Nagiyev from his comedic television role as Ensign Zadov and takes grave offense when Nagiyev offers him money. Listen to their exchange in Russian first."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Offering cash to a proud retired officer who already hates Nagiyev's television character turns out to be a painful mistake. See you next time!"
CLOSING = ('nagiyev', 'До свидания!')
STORY = [
    ('guest', 'Что тебе надо?', 'What do you want?', [(92, 'тебе надо')], 'adapted'),
    ('nagiyev', 'Здравствуйте, меня Дмитрий зовут.', 'Hello, my name is Dmitry.', [(92, 'Меня Дмитрий зовут')], 'adapted'),
    ('guest', 'Так, ты мне знаком.', 'Well, you look familiar to me.', [(93, 'Так, так')], 'adapted'),
    ('guest', 'Это ты, что ли, прапорщик?', 'Wait, are you that warrant officer?', [(94, 'Это ты, что ли, прапорщик')], 'adapted'),
    ('nagiyev', 'Молодец, узнал меня.', 'Well done, you recognized me.', [(96, 'Молодец')], 'adapted'),
    ('nagiyev', 'Я тебе мир предлагаю.', 'I am offering you peace.', [(97, 'Я тебе мир предлагаю')], 'adapted'),
    ('guest', 'Какой ещё тебе мир?', 'What kind of peace for you?', [(98, 'Какой тебе мир')], 'adapted'),
    ('guest', 'Ты всех русских прапорщиков опозорил!', 'You disgraced all Russian warrant officers!', [(99, 'Ты всех русских прапорщиков опозорил')], 'adapted'),
    ('guest', 'Ты всю русскую армию опозорил!', 'You disgraced the entire Russian army!', [(100, 'всю русскую армию')], 'adapted'),
    ('nagiyev', 'Я к тебе правда с миром пришёл.', 'I truly came to you in peace.', [(102, 'Я к тебе, правда, с миром пришел')], 'adapted'),
    ('nagiyev', 'Я просто тебе хотел денег предложить.', 'I just wanted to offer you some money.', [(103, 'Я просто тебе хотел денег предложить')], 'adapted'),
    ('guest', 'Денег мне решил предложить?', 'You decided to offer me money?', [(104, 'Денег'), (105, 'Денег')], 'adapted'),
]
WALK = [
    (0, None, "'What do you want?' The guest prompts straight out to see how Nagiyev will answer on the spot."),
    (1, None, '\'Hello, my name is Dmitry.\' Nagiyev leans on one telling word in reply: "zdravstvuyte" means "hello", and it carries the main weight of what Nagiyev is saying.'),
    (2, None, "'Well, you look familiar to me.' The guest sends the reply with ease: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (3, None, "'Wait, are you that warrant officer?' The guest questions evenly in front of Nagiyev without any preamble."),
    (4, None, '\'Well done, you recognized me.\' Nagiyev centers this direct element toward the guest: "molodets" means "well done, good boy", and it carries the main weight of what Nagiyev is saying.'),
    (5, None, "'I am offering you peace.' Nagiyev directs this update frankly here: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (6, None, "'What kind of peace for you?' The guest inquires frankly about what Nagiyev just brought up."),
    (7, None, '\'You disgraced all Russian warrant officers!\' The guest highlights this telling expression at once: "praporshchikov" means "warrant officers" (from "praporshchik"), giving the line its exact edge.'),
    (8, None, '\'You disgraced the entire Russian army!\' The guest sharpens one clear detail right here: "russkuyu" means "Russian" (from "russkiy"), giving the line its exact edge.'),
    (9, None, "'I truly came to you in peace.' Nagiyev jumps in plainly hearing the guest, testing the guest's reaction in the middle of the exchange."),
    (10, None, '\'I just wanted to offer you some money.\' Nagiyev sharpens one vivid detail for the guest: "predlozhit" means "to offer", and it carries the main weight of what Nagiyev is saying.'),
    (11, None, "'You decided to offer me money?' The guest states the comment for Nagiyev: Russian keeps the exact word order of a normal statement here, turning it into a question for Nagiyev purely through rising pitch at the end."),
]
