# Authoring module for kukhnya-s05e05-scene-16.
ID = 'kukhnya-s05e05-scene-16'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 5
SCENE = 16
TITLE = "Бдительная гостья и сумка Елены  (The Vigilant Guest and Elena's Bag)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.05'
SOURCE_FILE = 'sources/kukhnya/s05/e05.ru.srt'
INTRO = "When Elena steps back into the dining room to pick up her purse, the guest whom Barinov warned earlier leaps into action, seizing Elena's bag and shouting for hotel security to arrest the supposed thief."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'The security guard thanks the guest for her vigilance while Elena glares daggers at Barinov as his latest lie blows up in his face. See you next time!'
CLOSING = ('barinov', 'До завтра!')
STORY = [
    ('guest', 'Стойте, отдайте сумку!', 'Stop, hand over the bag!', [(281, 'Стойте'), (282, 'Отдайте так сумку')], 'adapted'),
    ('elena', 'Что такое, это моя сумка!', 'What is going on, this is my bag!', [(281, 'Что такое'), (284, 'Это моя сумка')], 'adapted'),
    ('guest', 'Охрана, отдайте мою сумку!', 'Security, give back my bag!', [(283, 'охрана. Отдайте мою сумку')], 'adapted'),
    ('barinov', 'Так, что случилось?', 'Alright, what happened?', [(284, 'Так, что случилось')], 'adapted'),
    ('elena', 'Руки уберите от меня!', 'Take your hands off me!', [(286, 'Руки уберите меня')], 'adapted'),
    ('barinov', 'Тихо, тихо, что вообще происходит?', 'Quiet, quiet, what on earth is happening?', [(288, 'Тихо, тихо'), (289, 'Что вообще происходит')], 'adapted'),
    ('guest', 'Вы были совершенно правы.', 'You were completely right.', [(289, 'Вы были совершенно правы')], 'adapted'),
    ('guest', 'Она воровка!', 'She is a thief!', [(290, 'Она воровка')], 'adapted'),
    ('elena', 'Что?', 'What?', [(290, 'Что')], 'adapted'),
    ('barinov', 'Отпустите её, это недоразумение.', 'Let her go, this is a misunderstanding.', [(288, 'Тихо, тихо')], 'adapted'),
    ('guest', 'Спасибо за бдительность.', 'Thank you for your vigilance.', [(292, 'Спасибо за бдительность')], 'adapted'),
    ('elena', 'Витя, объясни мне, что это значит!', 'Vitya, explain to me what this means!', [(289, 'Что вообще происходит')], 'adapted'),
]
WALK = [
    (0, None, '\'Stop, hand over the bag!\' Mentioning the bag before Elena, the guest lands on "sumku" ("bag, purse", built on "sumka") to keep the statement grounded.'),
    (1, None, '\'What is going on, this is my bag!\' Mentioning her bag beside the guest, Elena links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (2, None, "'Security, give back my bag!' The guest pushes back pointedly on the spot, watching Elena's face to see how the news lands."),
    (3, None, '\'Alright, what happened?\' Barinov opens up frankly to Elena and lands on "sluchilos" ("happened", built on "sluchitsya") to keep the statement grounded.'),
    (4, None, "'Take your hands off me!' Touching on the hands in the exchange, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (5, None, "'Quiet, quiet, what on earth is happening?' Barinov challenges plainly while looking straight at the guest here."),
    (6, None, '\'You were completely right.\' The guest weighs in plainly at once and brings in "sovershenno" ("quite, completely") to make the meaning unmistakable.'),
    (7, None, '\'She is a thief!\' Discussing a thief to Elena, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (8, None, "'What?' Elena prompts calmly to see how Barinov will answer on the spot."),
    (9, None, '\'Let her go, this is a misunderstanding.\' Touching on a misunderstanding before Elena, Barinov lands on "nedorazumeniye" ("misunderstanding") as the key everyday word here.'),
    (10, None, '\'Thank you for your vigilance.\' The guest promptly sends this word of thanks for Barinov using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (11, None, "'Vitya, explain to me what this means!' Elena steps in firmly without holding back, bringing things back to earth after the buildup."),
]
