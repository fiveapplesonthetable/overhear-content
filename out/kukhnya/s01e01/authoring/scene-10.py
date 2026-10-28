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
OUTRO = 'Max\'s first day has started with a surprise, and it won\'t be the last. You\'ve also learned to say hello properly, and "zdravstvuyte" is a mouthful worth practising.'
CLOSING = ('max', 'Пока!')
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
    (0, None, '\'Hello! I arrived for an appointment.\' "Zdravstvuyte" is the formal hello, and the first "v" is silent, so it sounds like "zdrastvuyte". "Na vstrechu" is "for a meeting", the word you\'d use for any appointment.'),
    (1, None, '\'Good day! Are you here to see Dmitry Vladimirovich?\' Russians address people formally by first name plus father\'s name. "Vladimirovich" means "son of Vladimir". After "k", "to", the name takes the ending "-u": "Dmitriyu Vladimirovichu".'),
    (2, None, '\'Yes, he invited me for a job.\' "Priglashal" is "invited". "Na rabotu" is the everyday phrase for going to a job: "rabota" turns its -a into -u after "na" when there\'s movement towards it.'),
    (3, None, '\'The owner is busy in the kitchen for now.\' "Khozyain" is the owner, literally the master of the house. "Poka" is "for now", exactly like the casual "poka", "bye", which means "see you for now".'),
    (4, None, '\'Understood. And who is managing the dining room?\' "Rukovodit", "manages", is built from "ruka", hand, and "vodit\'", to lead. It\'s followed by the "-om" form, so "zal", the hall, becomes "zalom".'),
    (5, None, '\'That strict young woman over by the window.\' "Von" is "over there", a further point than "vot", "here is". "Strogaya" and "ta" both end like a woman\'s word, because "devushka" is feminine. "U okna" is "at the window".'),
    (6, None, '\'What is this beautiful young woman\'s name?\' "Kak zovut" is literally "how do they call", with no "they" named. It\'s the normal way to ask what someone is called.'),
    (7, None, '\'This is Viktoria Sergeyevna, our art director.\' "Sergeyevna" is "daughter of Sergey", the feminine version of a father\'s name. "Art-direktor" is "art director", borrowed whole.'),
    (8, None, '\'Oh no, what an unpleasant situation!\' "Nepriyatnaya" is "ne" plus "priyatnaya", pleasant: unpleasant. "Kakaya" at the start turns the sentence into "what a...!".'),
    (9, None, '\'What happened? You turned so pale!\' "Pobledneli" has "blednyy", pale, inside it, and it ends in "-li", the plural, even though one person is being addressed. That\'s how the polite "vy" works.'),
    (10, None, '\'Nothing terrible, my head is spinning.\' "Nichego strashnogo" is literally "nothing scary", the standard way to say "no big deal". "Golova kruzhitsya" has "krug", a circle, in it: the head goes round.'),
    (11, None, '\'Would you like to sit at an available table?\' "Khotite" is the formal "do you want". "Stolik" is a little "stol", a table, which is how a restaurant table is named. "Svobodnyy" is free, empty.'),
    (12, None, '\'No, thank you, I\'d rather stand.\' "Luchshe", "better", is how Russians say "I\'d rather": "ya luchshe postoyu", "I\'d better stand". It\'s the polite way to turn down a seat.'),
]
