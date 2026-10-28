# Authoring module for kukhnya-s05e12-scene-20.
ID = 'kukhnya-s05e12-scene-20'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 12
SCENE = 20
TITLE = 'Выходи за меня  (Marry Me)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.12'
SOURCE_FILE = 'sources/kukhnya/s05/e12.ru.srt'
INTRO = "Chasing Elena's taxi in a white horse-drawn carriage, Chef Barinov holds out the ring and asks her to marry him for real. Although Max and Vika's divorce is finalized the next day, Max believes a miracle is still possible—while Kostya role-plays as Masseur Konstantin for Nastya."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings Episode Twelve of Season Five to an unforgettable conclusion. Listen for Viktor's marriage proposal—marry me—and Max's hope that a miracle will still happen. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Отпусти меня!', 'Let me go!', [(299, 'Отпусти меня')], 'adapted'),
    ('max', 'Говорят, что мысли материальны.', 'They say that thoughts are material.', [(300, 'Говорят, что мысли материальны')], 'adapted'),
    ('max', 'Если признаться себе в том, чего по-настоящему хочешь.', 'If you admit to yourself what you truly want.', [(301, 'Если признаться себе в том, чего по-настоящему хочешь')], 'adapted'),
    ('max', 'Возможно, чудо произойдёт.', 'Perhaps a miracle will happen.', [(302, 'Возможно, чудо произойдет')], 'adapted'),
    ('barinov', 'Выходи за меня!', 'Marry me!', [(303, 'Выходи за меня')], 'adapted'),
    ('max', 'Теперь ваш брак официально расторгнут.', 'Now your marriage is officially dissolved.', [(304, 'Теперь ваш брак официально')], 'adapted'),
    ('max', 'Но я не сдаюсь.', 'But I am not giving up.', [(302, 'чудо произойдет')], 'adapted'),
    ('max', 'Здравствуйте, можно заказать массаж?', 'Hello, can I order a massage?', [(305, 'Здравствуйте. Можно заказать массаж')], 'adapted'),
    ('max', 'Плюс интимные услуги?', 'Plus intimate services?', [(305, 'плюс интимные услуги')], 'adapted'),
    ('kostya', 'Ну конечно можно!', 'Well of course you can!', [(306, 'Ну, конечно, можно')], 'adapted'),
    ('max', 'Массажист Константин уже выезжает!', 'Masseur Konstantin is already on his way!', [(307, 'Массажист Константин уже выезжает')], 'adapted'),
    ('max', 'Жду вас с нетерпением!', 'I am waiting for you impatiently!', [(306, 'конечно, можно')], 'adapted'),
]
WALK = [
    (0, None, "'Let me go!' Pushing back calmly right here, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (1, None, "'They say that thoughts are material.' Touching on the thoughts with a sigh, Max lets Barinov see exactly where things stand."),
    (2, None, '\'If you admit to yourself what you truly want.\' Max follows up readily to Barinov and leans on "po-nastoyashchemu" ("truly") to give the whole sentence its punch.'),
    (3, None, "'Perhaps a miracle will happen.' Dwelling on a miracle in the exchange, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (4, None, "'Marry me!' Barinov proceeds plainly in their talk, before Max can change the subject."),
    (5, None, '\'Now your marriage is officially dissolved.\' Underscoring the marriage on the spot, Max leans on "ofitsialno" ("official, officially") to give the whole sentence its punch.'),
    (6, None, '\'But I am not giving up.\' Opening up boldly beside Barinov, the "-sya" ending on "sdayus" ("to give up") marks an action that unfolds mutually or turns back on the speaker.'),
    (7, None, '\'Hello, can I order a massage?\' Max readily offers this formal greeting with Kostya using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (8, None, '\'Plus intimate services?\' Pointing to the services around Kostya, Max leans on "intimnyye" ("intimate", a form of "intimnyy") to give the remark its edge.'),
    (9, None, '\'Well of course you can!\' Kostya politely delivers this confirmation in front of Max using "konechno" ("of course") — spoken with a soft "shn" sound in everyday Moscow Russian to mean "of course, certainly".'),
    (10, None, "'Masseur Konstantin is already on his way!' Discussing the massage therapist without a pause, Max puts the real issue right on the table for Kostya."),
    (11, None, '\'I am waiting for you impatiently!\' Max answers directly in front of Kostya and lands on "neterpeniyem" ("to forward", built on "neterpenit") to keep the statement grounded.'),
]
