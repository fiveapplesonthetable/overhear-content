# Authoring module for kukhnya-s01e04-scene-10.
ID = 'kukhnya-s01e04-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 10
TITLE = 'Детектор лжи  (The Lie Detector)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'expert': 'Эксперт', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = 'The chef is determined to find the traitor, so he has hired a lie-detector expert and set up a machine in his office. Fedya, the fish cook, is the first to be questioned. Here is the Russian first.'
OPENER = "Let's go through the questioning."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Fedya passes the test and is sent to fetch Senya. The key takeaway is the phrase for a lie detector, which literally means detector of a lie.'
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('barinov', 'Заходи, Федя. Садись на стул.', 'Come in, Fedya. Sit down on the chair.', [(114, 'Заходи')], ''),
    ('fedya', 'Шеф, а что это такое?', 'Chef, what is this thing?', [(116, 'Шеф, это чего')], ''),
    ('barinov', 'Это настоящий детектор лжи, Федя.', 'This is a real lie detector, Fedya.', [(117, 'Это детектор лжи, Федя')], ''),
    ('barinov', 'Я должен поймать крысу на кухне.', 'I must catch the rat in the kitchen.', [(118, 'поймать крысу')], ''),
    ('expert', 'Отвечайте только «да» или «нет».', "Answer only 'yes' or 'no'.", [(120, 'Отвечайте только')], ''),
    ('fedya', 'Хорошо, это мне вполне понятно.', 'Fine, that is completely clear to me.', [(121, 'Понятно')], ''),
    ('expert', 'Скажите, сегодня действительно среда?', 'Tell me, is today really Wednesday?', [(123, 'Скажите, сегодня среда')], ''),
    ('fedya', 'Да, сегодня среда.', 'Yes, today is Wednesday.', [(124, 'Да')], ''),
    ('expert', 'Ваше настоящее имя Фёдор?', 'Is your real name Fyodor?', [(129, 'Ваше имя Фёдор')], ''),
    ('fedya', 'Да.', 'Yes.', [(130, 'Да')], ''),
    ('barinov', 'Ты ходил в соседний ресторан?', 'Did you go to the neighboring restaurant?', [(135, 'соседний ресторан')], ''),
    ('fedya', 'Нет, я никуда не ходил.', 'No, I did not go anywhere.', [(137, 'Нет')], ''),
    ('barinov', 'Свободен. Позови сюда Сеню.', 'You are free to go. Call Senya in here.', [(138, 'Свободен'), (139, 'позови там Сеню')], ''),
]
WALK = [
    (0, None, [
        '"Come in, Fedya. Sit down on the chair." The term for come in is ',
        ('barinov', 'Заходи,'),
        ', built from the starting part for going inside. The action word for seat yourself is ',
        ('barinov', 'Садись'),
        ', built from an ending that means doing it to yourself.'
    ]),
    (1, None, [
        '"Chef, what is this thing?" The phrase ',
        ('fedya', 'что это такое?'),
        ' literally translates to "what is this such?", a handy way to ask what something is.'
    ]),
    (2, None, [
        '"This is a real lie detector, Fedya." The phrase for a lie drops a sound to become ',
        ('barinov', 'лжи,'),
        ', meaning "of a lie". The whole phrase translates to "detector of a lie".'
    ]),
    (3, None, [
        '"I must catch the rat in the kitchen." The Russian expression for rat, ',
        ('barinov', 'крысу'),
        ', is also slang for a traitor. The action word ',
        ('barinov', 'поймать'),
        ' translates to "to catch", and ',
        ('barinov', 'должен'),
        ' is the describing word for "must" when a man is speaking.'
    ]),
    (4, None, [
        '"Answer only yes or no." The action word ',
        ('expert', 'Отвечайте'),
        ' is an instruction built from a polite ending. The Russian term for only is ',
        ('expert', 'только'),
        ', and the little word for or is ',
        ('expert', 'или'),
        '.'
    ]),
    (5, None, [
        '"Fine, that is completely clear to me." The translation for completely, ',
        ('fedya', 'вполне'),
        ', literally translates to "in full". The word for clear, ',
        ('fedya', 'понятно.'),
        ', needs no word for "I" when you say it is clear to you.'
    ]),
    (6, None, [
        '"Tell me, is today really Wednesday?" The Russian term for Wednesday, ',
        ('expert', 'среда?'),
        ', is built from the phrase for middle, since it falls mid-week. The phrase for really is ',
        ('expert', 'действительно'),
        '.'
    ]),
    (7, None, [
        '"Yes, today is Wednesday." Fedya repeats the day of the week, ',
        ('fedya', 'сегодня среда.'),
        ' with no action word, because the language leaves out the Russian expression for "is".'
    ]),
    (8, None, [
        '"Is your real name Fyodor?" The full name behind Fedya is ',
        ('expert', 'Фёдор?'),
        '. The describing word for real, ',
        ('expert', 'настоящее'),
        ', takes a matching ending for the Russian term for name, ',
        ('expert', 'имя'),
        '.'
    ]),
    (9, None, ['"Yes." Just ', ('fedya', 'Да.'), ', which is exactly what the expert asked for.']),
    (10, None, [
        '"Did you go to the neighboring restaurant?" The action word ',
        ('barinov', 'ходил'),
        ' literally translates to "went and came back". The describing word for neighboring, ',
        ('barinov', 'соседний'),
        ', is built from the Russian term for neighbor.'
    ]),
    (11, None, [
        '"No, I did not go anywhere." The phrase ',
        ('fedya', 'никуда не ходил.'),
        ' literally translates to "nowhere not went", which doubles the negative.'
    ]),
    (12, None, [
        '"You are free to go. Call Senya in here." The Russian expression for free is ',
        ('barinov', 'Свободен.'),
        ', used here as a short word for a man. The action word for call is ',
        ('barinov', 'Позови'),
        ', and Senya turns into ',
        ('barinov', 'Сеню.'),
        ' as the target of the action.'
    ]),
]
