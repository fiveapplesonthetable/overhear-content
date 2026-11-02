# Authoring module for kukhnya-s01e01-scene-10.
ID = 'kukhnya-s01e01-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 10
TITLE = 'Знакомое лицо в зале  (A Familiar Face in the Hall)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'This is the job interview. Max walks into the dining room of Claude Monet and asks a waitress for the owner. Then he looks across the room, and everything goes wrong, because he recognises the woman running the floor. Here it is in Russian first.'
OPENER = "Let's go through what Max and the waitress say."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max's first day has started with a surprise, and it won't be the last. You've also learned to say hello properly, and this word is a mouthful worth practising."
CLOSING = ('max', 'Пока')
STORY = [
    ('max', 'Здравствуйте! Я пришёл на встречу.', 'Hello! I arrived for an appointment.', [], ''),
    ('sasha', 'Добрый день! Вы к Дмитрию Владимировичу?', 'Good day! Are you here to see Dmitry Vladimirovich?', [], ''),
    ('max', 'Да, он приглашал меня на работу.', 'Yes, he invited me for a job.', [], ''),
    ('sasha', 'Хозяин пока занят на кухне.', 'The owner is busy in the kitchen for now.', [], ''),
    ('max', 'Понятно. А кто руководит залом?', 'Understood. And who is managing the dining room?', [], ''),
    ('sasha', 'Вон та строгая девушка у окна.', 'That strict young woman over by the window.', [], ''),
    ('max', 'Как зовут эту красивую девушку?', "What is this beautiful young woman's name?", [], ''),
    ('sasha', 'Это Виктория Сергеевна, наш арт-директор.', 'This is Viktoria Sergeyevna, our art director.', [], ''),
    ('max', 'О нет, какая неприятная ситуация!', 'Oh no, what an unpleasant situation!', [(72, 'Дерьмо')], ''),
    ('sasha', 'Что случилось? Вы так побледнели!', 'What happened? You turned so pale!', [], ''),
    ('max', 'Ничего страшного, голова кружится.', 'Nothing terrible, my head is spinning.', [], ''),
    ('sasha', 'Хотите сесть за свободный столик?', 'Would you like to sit at an available table?', [], ''),
    ('max', 'Нет, спасибо, я лучше постою.', "No, thank you, I'd rather stand.", [], ''),
]
WALK = [
    (0, None, ['\'Hello! I arrived for an appointment.\' ', ('max', 'Здравствуйте!'), ' is the formal hello, and the first v is silent, so it sounds a bit different. ', ('max', 'на встречу.'), ' is "for a meeting", the word you\'d use for any appointment.']),
    (1, None, ['\'Good day! Are you here to see Dmitry Vladimirovich?\' Russians address people formally by first name plus father\'s name. ', ('sasha', 'Владимировичу?'), ' means "son of Vladimir". After "to", the name takes the ending -u.']),
    (2, None, ['\'Yes, he invited me for a job.\' ', ('max', 'приглашал'), ' is "invited". ', ('max', 'на работу.'), ' is the everyday phrase for going to a job: the word for job turns its -a into -u after "na" when there\'s movement towards it.']),
    (3, None, ['\'The owner is busy in the kitchen for now.\' ', ('sasha', 'Хозяин'), ' is the owner, literally the master of the house. ', ('sasha', 'пока'), ' is "for now", exactly like the casual bye, which means "see you for now".']),
    (4, None, ['\'Understood. And who is managing the dining room?\' ', ('max', 'руководит'), ', "manages", is built from hand, and to lead. It\'s followed by the -om form, so the hall becomes ', ('max', 'залом?'), '.']),
    (5, None, ['\'That strict young woman over by the window.\' ', ('sasha', 'Вон'), ' is "over there", a further point than "here is". ', ('sasha', 'строгая'), ' and ', ('sasha', 'та'), ' both end like a woman\'s word, because young woman is feminine. ', ('sasha', 'у окна.'), ' is "at the window".']),
    (6, None, ['\'What is this beautiful young woman\'s name?\' ', ('max', 'Как зовут'), ' is literally "how do they call", with no "they" named. It\'s the normal way to ask what someone is called.']),
    (7, None, ['\'This is Viktoria Sergeyevna, our art director.\' ', ('sasha', 'Сергеевна,'), ' is "daughter of Sergey", the feminine version of a father\'s name. ', ('sasha', 'арт-директор.'), ' is "art director", borrowed whole.']),
    (8, None, ['\'Oh no, what an unpleasant situation!\' ', ('max', 'неприятная'), ' is a negative prefix plus pleasant: unpleasant. ', ('max', 'какая'), ' at the start turns the sentence into "what a...!".']),
    (9, None, ['\'What happened? You turned so pale!\' ', ('sasha', 'побледнели!'), ' has pale inside it, and it ends in -li, the plural, even though one person is being addressed. That\'s how the polite you works.']),
    (10, None, ['\'Nothing terrible, my head is spinning.\' ', ('max', 'Ничего страшного,'), ' is literally "nothing scary", the standard way to say "no big deal". ', ('max', 'голова кружится.'), ' has a circle in it: the head goes round.']),
    (11, None, ['\'Would you like to sit at an available table?\' ', ('sasha', 'Хотите'), ' is the formal "do you want". ', ('sasha', 'столик?'), ' is a little table, which is how a restaurant table is named. ', ('sasha', 'свободный'), ' is free, empty.']),
    (12, None, ['\'No, thank you, I\'d rather stand.\' ', ('max', 'лучше'), ', "better", is how Russians say "I\'d rather". It\'s the polite way to turn down a seat.']),
]
