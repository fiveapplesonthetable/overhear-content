# Authoring module for kukhnya-s03e04-scene-03.
ID = 'kukhnya-s03e04-scene-03'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 4
SCENE = 3
TITLE = 'Праздник в зале  (Celebration in the Dining Room)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.04'
SOURCE_FILE = 'sources/kukhnya/s03/e04.ru.srt'
INTRO = 'Out in the dining room, Dmitry Nagiyev dances in brimming with joy, handing out cash bonuses to the staff and ordering champagne for every guest in the restaurant.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes Scene Three. Listen for Nagiyev's boundless generosity as he calls for good champagne for the entire room. Until next time!"
CLOSING = ('nagiyev', 'Хорошего дня!')
STORY = [
    ('nagiyev', 'Ребята! Здравствуйте! Ты моя хорошая.', 'Guys! Hello! You are my good girl.', [(28, 'Ребята'), (29, 'Ты моя хорошая')], 'adapted'),
    ('nagiyev', 'Да, мне очень нравится, как ты работаешь.', 'Yes, I really like how you work.', [(31, 'Да, мне очень, очень нравится, как ты работаешь')], 'adapted'),
    ('nagiyev', 'Молодец! А кому премия, Виктория Сергеевна?', 'Well done! And who gets a bonus, Viktoria Sergeyevna?', [(32, 'Молодец. А кому премия, Виктория Сергеевна')], ''),
    ('nagiyev', 'Кому премия?', 'Who gets a bonus?', [(33, 'Кому премия')], ''),
    ('nagiyev', 'Народу много в зале?', 'Are there many people in the dining room?', [(36, 'Народу много в зале')], ''),
    ('vika', 'Человек пятнадцать.', 'About fifteen people.', [(37, 'Человек')], 'adapted'),
    ('nagiyev', 'Господа, всем шампанского хорошего!', 'Ladies and gentlemen, good champagne for everyone!', [(38, 'Господа, всем шампанского хорошего')], ''),
    ('vika', 'Спасибо!', 'Thank you!', [(39, 'Спасибо')], ''),
    ('vika', 'Дмитрий Владимирович, а позвольте узнать повод?', 'Dmitry Vladimirovich, may I ask the occasion?', [(40, 'Дмитрий Владимирович, а позвольте узнать повод')], ''),
    ('nagiyev', 'Ну, позволю!', 'Well, I will allow it!', [(41, 'позволю')], 'adapted'),
    ('nagiyev', 'Всем шампанского за мой счёт!', 'Champagne for everyone on my tab!', [(38, 'всем шампанского')], 'adapted'),
    ('vika', 'Отличная новость!', 'Wonderful news!', [(32, 'Молодец')], 'adapted'),
]
WALK = [
    (0, None, "'Guys! Hello! You are my good girl.' Nagiyev opens up openly beside Vika, making his position completely clear."),
    (1, None, '\'Yes, I really like how you work.\' Nagiyev answers boldly with Vika and chooses "rabotayesh" ("are working", from the root "rabotat") so Vika hears the exact meaning.'),
    (2, None, '\'Well done! And who gets a bonus, Viktoria Sergeyevna?\' Discussing a bonus during the talk, the "-sya" ending on "molodets" ("well done, good boy") marks an action that unfolds mutually or turns back on the speaker.'),
    (3, None, "'Who gets a bonus?' Nagiyev checks candidly if there is more going on behind the scenes."),
    (4, None, '\'Are there many people in the dining room?\' Addressing the people right here, Nagiyev leans on "narodu" ("the people", a form of "narod") to give the remark its edge.'),
    (5, None, "'About fifteen people.' Holding firm candidly at once, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (6, None, "'Ladies and gentlemen, good champagne for everyone!' Nagiyev opens up promptly without holding back, bringing things back to earth after the buildup."),
    (7, None, '\'Thank you!\' Vika warmly shares this word of thanks right on cue using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (8, None, "'Dmitry Vladimirovich, may I ask the occasion?' Bringing up the reason in front of Nagiyev, Vika keeps normal statement word order here, turning the line into a question for Nagiyev purely through rising pitch."),
    (9, None, "'Well, I will allow it!' Nagiyev fires back evenly hearing Vika, to clear the air between them once and for all."),
    (10, None, '\'Champagne for everyone on my tab!\' Turning to the champagne in front of Vika, Nagiyev puts the weight on "shampanskogo" ("of champagne", from "shampanskoye") as the exchange unfolds.'),
    (11, None, "'Wonderful news!' Mentioning the news to Nagiyev, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
]
