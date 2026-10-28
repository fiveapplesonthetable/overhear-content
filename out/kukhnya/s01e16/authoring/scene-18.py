# Authoring module for kukhnya-s01e16-scene-18.
ID = 'kukhnya-s01e16-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 18
TITLE = 'Метод дедукции  (Method of Deduction)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'The inspector is still working his way around the dining room. He stops at the table where Fedya sits dressed as a guest, and when Fedya insists he is just a customer, the inspector lists three small habits that give him away.'
OPENER = "Now the inspector's case against Fedya, line by line."
TRANSITION = 'And the whole conversation again, without stopping.'
OUTRO = "Fedya has to admit he is a cook. Keep 'nelzya' from this scene: it's the word on every sign that tells you what you're not allowed to do. See you next time!"
CLOSING = ('inspector', 'До свидания!')
STORY = [
    ('inspector', 'А вот вы-то мне и нужны.', "And you're just the one I need.", [(260, 'А вот вас-то мне кажется и нужно, уважаемый.')], ''),
    ('inspector', 'Можно взглянуть на ваши документы?', 'May I take a look at your papers?', [(261, 'Я могу взглянуть на ваши документы?')], ''),
    ('fedya', 'Я просто гость.', "I'm just a guest.", [], ''),
    ('inspector', 'Вы же повар в этом ресторане.', "But you're the cook in this restaurant.", [(261, 'Вы же повар в этом ресторане, правильно?')], ''),
    ('fedya', 'С чего вы взяли?', 'What makes you think that?', [], ''),
    ('inspector', 'Только повар так смотрит на блюдо.', 'Only a cook looks at a dish like that.', [(262, 'Потому что только повар может так придирчиво рассматривать'), (263, 'блюдо.')], ''),
    ('inspector', 'Потому что готовил его кто-то другой.', 'Because someone else cooked it.', [(264, 'потому что готовил-то его кто-то другой, а не вы.')], ''),
    ('inspector', 'Вы всё время трогаете голову.', 'You keep touching your head.', [(265, 'Вы все время трогаете голову')], ''),
    ('inspector', 'Вы привыкли к колпаку.', "You're used to the chef's hat.", [(265, 'потому что привыкли быть в колпаке.')], ''),
    ('inspector', 'И вы не пьёте своё вино.', "And you aren't drinking your wine.", [(266, 'Вы не прикоснулись вообще к замечательному шардоне,')], ''),
    ('inspector', 'Потому что на работе пить нельзя.', "Because you're not allowed to drink at work.", [(267, 'потому что на работе пить запрещено.')], ''),
    ('fedya', 'Да, вы правы.', "Yes, you're right.", [], ''),
    ('inspector', 'Вуаля.', 'Voilà.', [(269, 'Вуаля.')], ''),
]
WALK = [
    (0, None, "'And you're just the one I need.' 'Vy-to mne i nuzhny' is literally 'you, then, to me are needed': Russian says what you need is 'needed to you'. The little '-to' and 'i' add the sense of 'you're the very one'."),
    (1, None, "'May I take a look at your papers?' 'Mozhno', 'it is possible', is the everyday way to ask permission. 'Vzglyanut na' means 'to take a glance at', a quicker, more polite word than plain 'look'."),
    (2, None, "'I'm just a guest.' 'Gost' means 'guest', and in a restaurant it's also the word for a customer. 'Prosto', 'simply', does the job of English 'just'."),
    (3, None, "'But you're the cook in this restaurant.' 'Zhe' after 'vy' is a small word of insistence, like 'but you are, aren't you'. 'Povar' means 'cook', from the old verb 'varit', 'to boil'."),
    (4, None, "'What makes you think that?' 'S chego vy vzyali?' is literally 'from what did you take it?', the usual way to challenge a guess. It sounds a little defensive, which is the point."),
    (5, None, "'Only a cook looks at a dish like that.' 'Tak', 'so' or 'like that', points to the way he looks. 'Bliudo' means 'dish', both the plate of food and the course on a menu."),
    (6, None, "'Because someone else cooked it.' 'Kto-to drugoy' means 'someone else': 'kto-to' is 'someone', and 'drugoy' is 'other'. 'Ego', 'it', points back to the dish, which is neuter."),
    (7, None, "'You keep touching your head.' 'Vsyo vremya', literally 'all the time', is how Russian says 'keep doing' something. Russian needs no 'your' before 'head'."),
    (8, None, "'You're used to the chef's hat.' 'Privyknut k' means 'to get used to', and 'kolpak' is the tall white cook's hat. 'K kolpaku' adds '-u' to the hat after 'k'."),
    (9, None, "'And you aren't drinking your wine.' 'Svoyo' means 'your own', and Russian uses it whenever the owner is the person doing the action. 'Vino' is 'wine', a word that never changes its ending."),
    (10, None, "'Because you're not allowed to drink at work.' 'Nelzya' means 'it is not allowed', and it is followed by the plain 'pit', 'to drink'. Russian says 'na rabote', literally 'on work', for 'at work'."),
    (11, None, "'Yes, you're right.' 'Vy pravy' is literally 'you are right', with no word for 'are'. A man would say 'ty prav' to a friend; 'pravy' is the polite form for 'vy'."),
    (12, None, "'Voila.' The inspector borrows the French word, like a conjurer finishing a trick. Russians write it in their own letters and say it much as the French do."),
]
