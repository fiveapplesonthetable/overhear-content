# Authoring module for kukhnya-s05e10-scene-16.
ID = 'kukhnya-s05e10-scene-16'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 10
SCENE = 16
TITLE = "Вердикт комиссии и транс Макса  (The Commission's Verdict and Max's Trance)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.10'
SOURCE_FILE = 'sources/kukhnya/s05/e10.ru.srt'
INTRO = "At the commission's dinner table, the chairwoman declares that Hotel Eleon deserves only three stars because the service is a nightmare. To win a vote in their favor, Chef Barinov sits behind the unconscious Pavel Vladimirovich and puppets his head while the hypnotist puts Max into a trance."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That brings the dining-room scene to a close. Notice how the chairwoman announces her three-star verdict while Kostya realizes the woman is putting Max into a trance. See you next time!'
CLOSING = ('inspector', 'До завтра!')
STORY = [
    ('inspector', 'Мой вердикт — три звезды.', 'My verdict is three stars.', [(231, 'Мой вердикт – три звезды')], 'adapted'),
    ('inspector', 'Сервис, персонал — это кошмар какой-то!', 'The service, the staff, it is some kind of nightmare!', [(232, 'Сервис, персонал – это кошмар какой-то')], 'adapted'),
    ('max', 'Кому ещё вина?', 'More wine for anyone?', [(233, 'Кому еще вина')], 'adapted'),
    ('inspector', 'Вкусно. Павел Владимирович, а вы что думаете?', 'Delicious. Pavel Vladimirovich, and what do you think?', [(234, 'Вкусно. Павел Владимирович, а вы что думаете')], 'adapted'),
    ('barinov', 'Понятно. Я, конечно, согласен с вами.', 'Understood. I, of course, agree with you.', [(235, 'Понятно. Я, конечно, согласен с вами')], 'adapted'),
    ('barinov', 'Но с другой стороны, в целом отель неплохой.', 'But on the other hand, overall the hotel is not bad.', [(236, 'Но с другой стороны, в целом отель неплохой')], 'adapted'),
    ('barinov', 'Персонал старается.', 'The staff tries hard.', [(237, 'Персонал старается')], 'adapted'),
    ('max', 'Я сейчас.', 'I will be right back.', [(238, 'Я сейчас')], 'adapted'),
    ('barinov', 'Всё понравилось?', 'Did you like everything?', [(239, 'Все понравилось')], 'adapted'),
    ('inspector', 'Очень.', 'Very much.', [(240, 'Очень')], 'adapted'),
    ('max', 'Что-то он долго. Она его в транс вводит!', 'He is taking a long time. She is putting him into a trance!', [(241, 'Что-то он долго. Она его в транс вводит')], 'adapted'),
    ('barinov', 'Ничего, Макс с детства не поддаётся гипнозу.', 'It is nothing, Max has not succumbed to hypnosis since childhood.', [(242, 'Ничего. Макс с детства не поддается гипнозу')], 'adapted'),
]
WALK = [
    (0, None, '\'My verdict is three stars.\' Mentioning his verdict at once, the inspector chooses "verdikt" ("verdict") so Max gets the point right away.'),
    (1, None, '\'The service, the staff, it is some kind of nightmare!\' Checking on the staff at once, the inspector links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (2, None, "'More wine for anyone?' Max prompts eagerly before the inspector can change the subject."),
    (3, None, '\'Delicious. Pavel Vladimirovich, and what do you think?\' The inspector proceeds sharply in the exchange and brings in "vkusno" ("it\'s tasty") to make the meaning unmistakable.'),
    (4, None, '\'Understood. I, of course, agree with you.\' Barinov responds candidly beside the inspector and centers the thought on "soglasen" ("agreed", from "soglasnyy") without wasting a word.'),
    (5, None, "'But on the other hand, overall the hotel is not bad.' Barinov answers sharply during the talk, before the inspector can change the subject."),
    (6, None, '\'The staff tries hard.\' Highlighting the staff right here, Barinov centers the remark on "personal" ("staff") without any extra fuss.'),
    (7, None, "'I will be right back.' Reacting candidly before Barinov, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (8, None, "'Did you like everything?' Barinov presses curiously to see how the inspector will answer on the spot."),
    (9, None, '\'Very much.\' The inspector replies quietly with Barinov and chooses "ochen" ("very much") so Barinov gets the point right away.'),
    (10, None, '\'He is taking a long time. She is putting him into a trance!\' Focusing on a trance right here, Max leans on "trans" ("trance") to give the whole sentence its punch.'),
    (11, None, "'It is nothing, Max has not succumbed to hypnosis since childhood.' Barinov chimes in wryly across the room, leaving no doubt about where he stands."),
]
