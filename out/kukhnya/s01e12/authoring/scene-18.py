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
INTRO = 'In the dining room of Claude Monet, restaurant owner Dmitry Nagiyev checks the reservation book with hostess Angelina. Delighted to hear that all tables are booked solid, Nagiyev proudly declares that their restaurant needs no gimmicks to win over guests. Listen to their conversation in Russian first, then we will break down each line in English.'
OPENER = "Now let's go back through the exchange around A Packed House line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "In the Claude Monet dining room, owner Dmitry Nagiyev inspects the reservation book with hostess Angelina, celebrating that every single table is booked for the evening. Next time you watch the episode, listen for the Russian expressions for 'perfectly' and 'window' — you will catch every word right away. See you next time!"
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
    (0, None, "'Angelina, how are our reservations today?' Nagiyev asks Angelina about the table bookings for the evening."),
    (1, None, "'Dmitry Vladimirovich, all tables are already booked.' Angelina informs him that every single table is reserved."),
    (2, None, "'Yes, there are no more free tables.' Angelina confirms again that they are completely full."),
    (3, None, "'The guests will start arriving any minute.' Angelina says the customers will start showing up very soon."),
    (4, None, "'Look at that! It turned out just like I said.' Nagiyev brags that his predictions were completely right."),
    (5, None, "'People love us just the way we are!' Nagiyev is proud that people love the restaurant exactly as it is."),
    (6, None, "'Go prepare additional tables.' Nagiyev orders her to get extra tables ready for more guests."),
    (7, None, "'We will place two more tables by the window.' Angelina plans to set up two extra tables near the windows."),
    (8, None, "'Great, today we have a full house!' Nagiyev is thrilled that the restaurant will be packed tonight."),
    (9, None, "'Wonderful, the evening promises to be successful!' Nagiyev happily predicts that the night will be a big success."),
]
