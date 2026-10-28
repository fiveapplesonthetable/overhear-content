# Authoring module for kukhnya-s01e16-scene-18.
ID = 'kukhnya-s01e16-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 18
TITLE = 'Метод дедукции  (Method of Deduction)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "The inspector is still working his way around the dining room. He stops at the table of Louis, who says he is just a customer, and then lists three small habits that prove otherwise. We'll hear it in Russian first."
OPENER = "Now let's go back through it slowly."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Louis admits he is a cook, and the inspector gets his way. Keep 'nelzya' in mind from this scene, since it's the word on every sign that tells you what you can't do. See you next time!"
CLOSING = ('inspector', 'До свидания!')
STORY = [
    ('inspector', 'Можно посмотреть на ваши документы?', 'May I look at your documents?', [(261, 'ваши документы?')], ''),
    ('louis', 'Я просто обычный гость ресторана.', 'I am just an ordinary guest of the restaurant.', [], ''),
    ('inspector', 'Нет, вы работаете здесь поваром.', 'No, you work here as a chef.', [(261, 'Вы же повар в этом ресторане')], ''),
    ('louis', 'Почему вы вдруг так решили?', 'Why did you suddenly decide so?', [], ''),
    ('inspector', 'Вы очень внимательно смотрите на блюдо.', 'You are looking at the dish very carefully.', [(262, 'только повар может так придирчиво рассматривать')], ''),
    ('inspector', 'Вам эта еда совсем не нравится.', 'You do not like this food at all.', [(263, 'ему оно не понравится')], ''),
    ('inspector', 'Потому что готовил её другой повар.', 'Because another chef cooked it.', [(264, 'готовил-то его кто-то другой')], ''),
    ('louis', 'Я просто люблю хорошую кухню.', 'I simply love good cuisine.', [], ''),
    ('inspector', 'Ещё вы постоянно трогаете свою голову.', 'Also you are constantly touching your head.', [(265, 'Вы все время трогаете голову')], ''),
    ('inspector', 'На работе вы всегда носите шапку.', 'At work you always wear a cap.', [], ''),
    ('inspector', 'И вы совсем не пьёте вино.', 'And you are not drinking the wine at all.', [(266, 'Вы не прикоснулись вообще')], ''),
    ('inspector', 'Потому что на работе нельзя пить.', 'Because at work one must not drink.', [(267, 'потому что на работе пить')], ''),
    ('louis', 'Да, вы сказали чистую правду.', 'Yes, you told the pure truth.', [], ''),
]
WALK = [
    (0, None, "'May I look at your documents?' It opens with the ask-permission word, followed by 'look at'. 'Your' is plural to match 'documents', and the plural ending is a simple 'y'."),
    (1, None, "'I am just an ordinary guest of the restaurant.' There is no word for 'of'. The restaurant simply takes an 'a' ending and goes after 'guest'."),
    (2, None, "'No, you work here as a chef.' There's no word for 'as' either. The chef takes an 'om' ending, and that does the job."),
    (3, None, "'Why did you suddenly decide that?' 'Suddenly' is a good little word to keep, and it sits right after the 'why'. 'Decided' has the 'li' ending since the inspector is addressed as 'you', politely."),
    (4, None, "'You are looking at the dish very carefully.' 'Carefully' is a describing word with an 'o' ending, like many of the 'how' words. 'Look at' takes the little word for 'on'."),
    (5, None, "'You don't like this food at all.' Again it's 'to you not pleasing', so 'you' takes the 'am' ending. 'At all' is the pair 'altogether not'."),
    (6, None, "'Because another chef cooked it.' Russian says 'her' for the food, because the word for food is feminine. The first two words are 'because'."),
    (7, None, "'I simply love good cuisine.' The word for cuisine is the same as for 'kitchen', which is the title of the show. 'Good' ends in 'uyu' because it's what is loved."),
    (8, None, "'Also you constantly touch your head.' 'Your own' is a special little word, which always points back to the person doing the action. 'Constantly' is built from a word meaning 'constant'."),
    (9, None, "'At work you always wear a cap.' Russians say 'on work' for 'at work', and the work takes an 'e'. The word for 'wear' is the one for something you carry on yourself regularly."),
    (10, None, "'And you aren't drinking the wine at all.' 'Not at all' appears again, now in front of 'drink'. The wine itself stays in its basic form, because it isn't being drunk."),
    (11, None, "'Because you can't drink at work.' This 'can't' is the 'not allowed' word, and you'll see it on signs. It's followed by the plain 'to drink', with no 'you' at all."),
    (12, None, "'Yes, you told the pure truth.' Literally 'clean truth', so truth is something that can be clean. The ending on 'told' is the polite plural."),
]
