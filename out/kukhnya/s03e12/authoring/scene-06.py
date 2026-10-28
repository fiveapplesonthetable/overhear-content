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
    (0, None, "'What do you want?' The guest prompts straight out if there is more going on behind the scenes."),
    (1, None, '\'Hello, my name is Dmitry.\' Nagiyev casually sends this formal greeting toward the guest using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (2, None, "'Well, you look familiar to me.' Reacting naturally on the spot, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (3, None, "'Wait, are you that warrant officer?' The guest questions evenly what Nagiyev is actually getting at here."),
    (4, None, '\'Well done, you recognized me.\' Nagiyev answers calmly during the talk and reaches for the Russian word "molodets" ("well done, good boy") right at the heart of the line.'),
    (5, None, "'I am offering you peace.' Turning firmly in the exchange, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (6, None, "'What kind of peace for you?' The guest inquires frankly where this conversation is heading next."),
    (7, None, '\'You disgraced all Russian warrant officers!\' Bringing up the warrant officers in this beat, the guest uses "praporshchikov" ("warrant officers", from "praporshchik") to make the point stick.'),
    (8, None, "'You disgraced the entire Russian army!' The guest jumps in dryly with a nod, testing Nagiyev's reaction in the middle of the exchange."),
    (9, None, "'I truly came to you in peace.' Nagiyev replies plainly around the guest, so the guest knows he is not just making small talk."),
    (10, None, '\'I just wanted to offer you some money.\' Turning to the money around the guest, Nagiyev lands on "predlozhit" ("to offer") as the key everyday word here.'),
    (11, None, "'You decided to offer me money?' Dwelling on the money in the exchange, the guest keeps normal statement word order here, turning the line into a question for Nagiyev purely through rising pitch."),
]
