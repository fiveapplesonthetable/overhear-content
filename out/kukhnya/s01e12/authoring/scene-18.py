# Authoring module for kukhnya-s01e12-scene-18.
ID = 'kukhnya-s01e12-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 18
TITLE = 'Полный зал  (A Packed House)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'angelina_h': 'Ангелина', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = "Over in the dining room, the restaurant's owner, Dmitry Nagiyev, is checking the bookings with the hostess, Angelina. He is in a very good mood. Here's the Russian."
OPENER = "Line by line, and enjoy the owner's good mood."
TRANSITION = 'Back to the top for the full scene.'
OUTRO = "It's a full house, and the owner thinks it is all his doing. Listen out for the phrase for no places left, it's what you'll hear when a place is booked out. Bye for now."
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('nagiyev', 'Ангелина, что у нас с резервами сегодня?', 'Angelina, how are our reservations today?', [(239, 'Ангелина, что у нас с резервами на сегодня?')], ''),
    ('angelina_h', 'Дмитрий Владимирович, все столики уже заняты.', 'Dmitry Vladimirovich, all tables are already booked.', [(240, 'Все столики забронированы.')], ''),
    ('nagiyev', 'Правда? Совсем не осталось мест?', 'Really? Are there no seats left at all?', [], ''),
    ('angelina_h', 'Да, свободных столиков больше нет.', 'Yes, there are no more free tables.', [], ''),
    ('angelina_h', 'Гости начнут приходить с минуты на минуту.', 'The guests will start arriving any minute.', [(240, 'Гость сейчас будет приезжать.')], ''),
    ('nagiyev', 'Ты смотри! Вышло так, как я говорил.', 'Look at that! It turned out just like I said.', [(241, 'Ты смотри, опять вышло так, как я сказал.')], ''),
    ('angelina_h', 'Наш ресторан сейчас очень популярен.', 'Our restaurant is very popular right now.', [], ''),
    ('nagiyev', 'Люди любят нас именно такими!', 'People love us just the way we are!', [(242, 'Нас любят такими, какими мы есть.')], ''),
    ('nagiyev', 'Иди готовь дополнительные столики.', 'Go prepare additional tables.', [(243, 'Иди готовь экстра столики.')], ''),
    ('angelina_h', 'Мы поставим ещё два стола у окна.', 'We will place two more tables by the window.', [], ''),
    ('nagiyev', 'Отлично, сегодня у нас полный зал!', 'Great, today we have a full house!', [(244, 'У нас сегодня биток.')], ''),
    ('angelina_h', 'Я сейчас всё быстро организую.', 'I will quickly organize everything right now.', [], ''),
    ('nagiyev', 'Прекрасно, вечер обещает быть удачным!', 'Wonderful, the evening promises to be successful!', [], ''),
]
WALK = [
    (0, None, ["'Angelina, how are our reservations today?' Let us examine the sentence: ", ('nagiyev', 'что'), ('nagiyev', 'у'), ('nagiyev', 'нас'), " means 'what do we have'."]),
    (1, None, ["'Dmitry Vladimirovich, all tables are already booked.' Let us look at this part: ", ('angelina_h', 'все'), ('angelina_h', 'столики'), " means 'all tables'."]),
    (2, None, ["'Really? Are there no seats left at all?' Let's analyze the sentence: ", ('nagiyev', 'совсем'), " means 'at all'."]),
    (3, None, ["'Yes, there are no more free tables.' We can analyze the phrase: ", ('angelina_h', 'свободных'), " means 'free'."]),
    (4, None, ["'The guests will start arriving any minute.' We can examine the phrase: ", ('angelina_h', 'с'), ('angelina_h', 'минуты'), ('angelina_h', 'на'), ('angelina_h', 'минуту'), " means 'any minute'."]),
    (5, None, ["'Look at that! It turned out just like I said.' Now let's break down the sentence: ", ('nagiyev', 'Вышло'), ('nagiyev', 'так'), " means 'it turned out so'."]),
    (6, None, ["'Our restaurant is very popular right now.' We can consider the dialogue: ", ('angelina_h', 'очень'), ('angelina_h', 'популярен'), " means 'very popular'."]),
    (7, None, ["'People love us just the way we are!' We will break down the words: ", ('nagiyev', 'именно'), ('nagiyev', 'такими'), " means 'exactly like this'."]),
    (8, None, ["'Go prepare additional tables.' We will consider the dialogue: ", ('nagiyev', 'дополнительные'), " means 'additional'."]),
    (9, None, ["'We will place two more tables by the window.' Let's examine the dialogue: ", ('angelina_h', 'у'), ('angelina_h', 'окна'), " means 'by the window'."]),
    (10, None, ["'Great, today we have a full house!' We can look at the speech: ", ('nagiyev', 'полный'), ('nagiyev', 'зал'), " means 'a full hall'."]),
    (11, None, ["'I will quickly organize everything right now.' We will analyze the dialogue: ", ('angelina_h', 'быстро'), " means 'quickly'."]),
    (12, None, ["'Wonderful, the evening promises to be successful!' Let's look at the phrase: ", ('nagiyev', 'обещает'), " means 'promises'."]),
]
