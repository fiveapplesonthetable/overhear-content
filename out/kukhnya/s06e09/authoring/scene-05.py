# Authoring module for kukhnya-s06e09-scene-05.
ID = 'kukhnya-s06e09-scene-05'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 9
SCENE = 5
TITLE = 'Знакомство с Ларисой  (Meeting Larisa)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.09'
SOURCE_FILE = 'sources/kukhnya/s06/e09.ru.srt'
INTRO = 'In the restaurant dining room, Lyova greets his mother expecting to meet an older family friend, only to be introduced to Larisa—a young, charming nurse from the local clinic whom his mother praises enthusiastically.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Lyova feels awkward as his mother plays matchmaker at the table, and meanwhile Denis and Katya arrive at the hospital for his X-ray. Until next time!'
CLOSING = ('guest', 'До встречи!')
STORY = [
    ('lyova', 'Мама, привет, ну и где подруга?', 'Mom, hello, so where is your friend?', [(66, 'Привет'), (67, 'Ну и где подруга')], 'adapted'),
    ('guest', 'Ну вот она идёт к нам.', 'Well, here she is coming toward us.', [(68, 'Ну вот она')], 'adapted'),
    ('lyova', 'Здравствуйте, мне очень приятно с вами познакомиться.', 'Hello, I am very pleased to meet you.', [(69, 'Здравствуйте'), (70, 'Познакомься')], 'adapted'),
    ('guest', 'Познакомься, сынок, это моя подруга Лариса.', 'Meet her, son, this is my friend Larisa.', [(70, 'Познакомься, это Лариса')], 'adapted'),
    ('lyova', 'Я просто совсем не ожидал увидеть.', 'I just did not expect to see at all.', [(72, 'он просто не ожидал увидеть'), (74, 'не ожидал')], 'adapted'),
    ('guest', 'Не нервничай, она очень милая девушка.', 'Do not be nervous, she is a very nice girl.', [(72, 'Не нервничай')], 'adapted'),
    ('lyova', 'Мне кажется, вы сейчас немного преувеличиваете.', 'It seems to me you are exaggerating a little right now.', [(73, 'А вы преувеличиваете')], 'adapted'),
    ('guest', 'Да нет, я говорю чистую правду.', 'No, I am telling the pure truth.', [(74, 'Да')], 'adapted'),
    ('lyova', 'Мама, я лучше рядом с тобой сяду.', 'Mom, I would rather sit next to you.', [(76, 'Мам, я к тебе сяду')], 'adapted'),
    ('guest', 'Лариса самая заботливая медсестра в поликлинике.', 'Larisa is the most caring nurse at the clinic.', [(78, 'Лариса самая заботливая и самая общительная медсестра в нашей поликлинике')], 'adapted'),
    ('lyova', 'Мама, хватит меня так громко хвалить.', 'Mom, stop praising me so loudly.', [(79, 'про Лёва ты всё знаешь')], 'adapted'),
    ('guest', 'Ну про Лёву ты уже всё знаешь.', 'Well, you already know everything about Lyova.', [(79, 'Ну, про Лёва ты всё знаешь')], 'adapted'),
    ('lyova', 'Давайте лучше посмотрим наше сегодняшнее меню.', 'Let us better look at our menu for today.', [(80, 'Умный')], 'adapted'),
]
WALK = [
    (0, None, '\'Mom, hello, so where is your friend?\' Asking whether Mom hello so where is the guest\'s friend puts the guest right on the defensive. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'Well, here she is coming toward us.' Once here she is coming toward them, the guest can finally tell Lyova what he means."),
    (2, None, "'Hello, I am very pleased to meet you.' Being very pleased to meet the guest moves the conversation forward without extra drama."),
    (3, None, '\'Meet her, son, this is my friend Larisa.\' Here meeting her son this is his friend Larisa sets up the next turn in their exchange. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (4, None, "'I just did not expect to see at all.' Since he just did not expect to see at all, Lyova does not waste words on excuses."),
    (5, None, "'Do not be nervous, she is a very nice girl.' Mentioning that do not be nervous she is a very nice girl moves the talk in a new direction."),
    (6, None, '\'It seems to me you are exaggerating a little right now.\' Claiming that it seems to him the guest is exaggerating a little right now sounds confident, even if the guest has doubts. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (7, None, "'No, I am telling the pure truth.' Since he is telling the pure truth, the guest does not waste words on excuses."),
    (8, None, "'Mom, I would rather sit next to you.' Explaining that Mom he would rather sit next to the guest lays the cards on the table for the guest."),
    (9, None, "'Larisa is the most caring nurse at the clinic.' The guest mentions that Larisa is the most caring nurse at the clinic so Lyova sees what is at stake."),
    (10, None, "'Mom, stop praising me so loudly.' With the family and friend in play, Lyova keeps this short reply brisk and direct."),
    (11, None, "'Well, you already know everything about Lyova.' Around the family and friend, the guest sets a calm, everyday tone with Lyova."),
    (12, None, '\'Let us better look at our menu for today.\' Pointing out that they should better look at their menu for today gives the guest a sobering reality check. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
]
