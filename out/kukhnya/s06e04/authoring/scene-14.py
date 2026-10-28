# Authoring module for kukhnya-s06e04-scene-14.
ID = 'kukhnya-s06e04-scene-14'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 14
TITLE = 'Разоблачение за столиком  (Unmasking at the Table)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = "Barinov sits down at Olivier's table and tells him to drop the act because he knows he is the Michelin inspector—while Louis pulls Katya aside to show her the photo of the real inspector."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Realizing that the real Michelin inspector is actually sitting across the dining room right now, Katya tries to stop her father before he does something crazy. See you next time!'
CLOSING = ('louis', 'Увидимся!')
STORY = [
    ('guest', 'Извините, я только на минутку.', 'Excuse me, I will just be a minute.', [(222, 'Извините, я на минутку')], 'adapted'),
    ('guest', 'По-моему, голубь немного сухой, но я не эксперт.', 'In my opinion, the pigeon is a bit dry, though I am no expert.', [(223, 'По-моему, голубь немного'), (224, 'не эксперт')], 'adapted'),
    ('barinov', 'Оливье, давайте прекратим эту комедию.', "Olivier, let's stop this charade.", [(225, 'Оливье, давайте прекратим эту комедию')], 'exact'),
    ('barinov', 'Вы же инспектор!', 'After all, you are the inspector!', [(226, 'Вы инспектор')], 'adapted'),
    ('barinov', 'И от вас зависит, получим мы звезду или нет.', 'And it depends on you whether we get a star or not.', [(227, 'И от вас зависит, получим мы звезду или нет')], 'exact'),
    ('barinov', 'У нас есть большое желание быть лучшими.', 'We have a great desire to be the best.', [(228, 'желание быть лучшими')], 'adapted'),
    ('barinov', 'И вы видите, как сильно я хочу, чтобы мой ресторан стал лучше.', 'And you see how badly I want my restaurant to become better.', [(229, 'И вы видите, как сильно я хочу'), (230, 'чтобы мой ресторан стал лучше')], 'adapted'),
    ('barinov', 'Костя, принеси еще бутылку вина для инспектора!', 'Kostya, bring another bottle of wine for the inspector!', [(231, 'Костя, принеси еще бутылку вина для инспектора')], 'exact'),
    ('louis', 'Катя, я хочу тебе кое-что показать.', 'Katya, I want to show you something.', [(232, 'я хочу тебе кое-что показать')], 'adapted'),
    ('louis', 'Кто это на фото?', 'Who is this in the photo?', [(233, 'Кто это?')], 'adapted'),
    ('louis', 'Это настоящий инспектор, мне отец фото прислал.', 'That is the real inspector, my father sent me the photo.', [(233, 'Это настоящий инспектор'), (234, 'Мне отец'), (234, 'прислал')], 'adapted'),
    ('guest', 'Спасибо за вино, Виктор.', 'Thank you for the wine, Viktor.', [(231, 'бутылку вина')], 'adapted'),
]
WALK = [
    (0, None, "'Excuse me, I will just be a minute.' Saying that he will just be a minute is how the guest sets the tone with Barinov."),
    (1, None, "'In my opinion, the pigeon is a bit dry, though I am no expert.' Since in his opinion the pigeon is a bit dry though he is no expert, the guest does not waste words on excuses."),
    (2, None, "'Olivier, let's stop this charade.' Mentioning that Olivier let them stop this charade moves the talk in a new direction."),
    (3, None, '\'After all, you are the inspector!\' Saying that after all the guest is the inspector is how Barinov takes charge of the moment. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (4, None, '\'And it depends on you whether we get a star or not.\' Over the table and the moment, Barinov answers the guest without a second thought. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (5, None, "'We have a great desire to be the best.' Explaining that they have a great desire to be the best lays the cards on the table for the guest."),
    (6, None, '\'And you see how badly I want my restaurant to become better.\' Barinov mentions that how badly he wants his restaurant to become better so the guest sees what is at stake. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (7, None, "'Kostya, bring another bottle of wine for the inspector!' Saying that the guest should bring another bottle of wine for the inspector is how Barinov takes charge of the moment. Russian puts the key word right up front so his emotion lands on the first beat."),
    (8, None, "'Katya, I want to show you something.' Once he wants to show Barinov something, Louis can finally tell Barinov what he means."),
    (9, None, '\'Who is this in the photo?\' Asking who this in the photo is cuts straight through the tension between Louis and Barinov. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (10, None, '\'That is the real inspector, my father sent me the photo.\' Realizing that that is the real inspector his father sent him the photo changes how Louis handles the situation. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (11, None, "'Thank you for the wine, Viktor.' Turning from the inspector to the moment, the guest keeps the exchange moving."),
]
