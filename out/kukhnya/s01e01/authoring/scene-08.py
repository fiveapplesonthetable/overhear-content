# Authoring module for kukhnya-s01e01-scene-08.
ID = 'kukhnya-s01e01-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'Режь мельче  (Chop It Finer)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "The chef moves on to Max's cutting board, and everything is wrong by about a millimetre. Barinov wants the onion finer, the meat beaten, and the table tidy. This is the Russian first."
OPENER = 'Now line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Notice how many of the chef's lines are about doing something better: finer, thinner, faster. You can hear the word endings changing to match."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Режь лук мельче, это же ресторан!', 'Chop the onion finer, this is a restaurant!', [(65, 'Режь мельче')], ''),
    ('max', 'Хорошо, шеф, я стараюсь резать тоньше.', 'Alright, Chef, I try to cut thinner.', [(65, 'Режь мельче')], ''),
    ('barinov', 'Теперь правильно отбивай свежее мясо.', 'Now tenderize the fresh meat properly.', [(65, 'Мясо отбивай')], ''),
    ('max', 'Я уже приготовил специальный деревянный молоток.', 'I already prepared a special wooden mallet.', [(65, 'Мясо отбивай')], ''),
    ('barinov', 'Мясо должно стать мягким и сочным.', 'The meat must become tender and juicy.', [(65, 'Мясо отбивай')], ''),
    ('max', 'Сколько времени нужно отбивать каждый кусок?', 'How much time does each piece need tenderizing?', [(65, 'Мясо отбивай')], ''),
    ('barinov', 'Не задавай глупых вопросов, работай быстрее!', 'Do not ask stupid questions, work faster!', [(65, 'Режь мельче')], ''),
    ('max', 'Я делаю всё точно по вашему заказу.', 'I do everything exactly according to your order.', [(65, 'Режь мельче')], ''),
    ('barinov', 'Следи за порядком на своём рабочем столе.', 'Keep watch over the order on your work table.', [(65, 'Режь мельче')], ''),
    ('max', 'У меня здесь всегда полная чистота.', 'I always have complete cleanliness here.', [(65, 'Режь мельче')], ''),
    ('barinov', 'Вот теперь кусочки нарезаны красиво и аккуратно.', 'Now the pieces are cut beautifully and neatly.', [(65, 'Режь мельче')], ''),
    ('max', 'Спасибо, шеф, я готовлю следующую партию!', 'Thank you, Chef, I am preparing the next batch!', [(65, 'Режь мельче')], ''),
]
WALK = [
    (0, None, ['\'Chop the onion finer, this is a restaurant!\' ', ('barinov', 'мельче,'), ' is "finer": small, with an ending for "more". ', ('barinov', 'это же ресторан!'), ' has a tiny word that means "after all", so this is a restaurant, after all.']),
    (1, None, ['\'Alright, Chef, I try to cut thinner.\' ', ('max', 'Хорошо,'), ' is "good", used as "alright". ', ('max', 'тоньше.'), ', thinner, is made like the word for finer: thin, plus an ending that means "more".']),
    (2, None, ['\'Now tenderize the fresh meat properly.\' ', ('barinov', 'отбивай'), ' has the verb to hit inside it, so tenderizing is beating the meat flat. Barinov uses the informal you to Max, which is why it\'s a short command. ', ('barinov', 'свежее мясо.'), ' is "fresh meat".']),
    (3, None, ['\'I already prepared a special wooden mallet.\' ', ('max', 'приготовил'), ' is "prepared", the finished partner of to cook or get ready. ', ('max', 'молоток.'), ', a mallet, is a small hammer, and ', ('max', 'деревянный'), ' has the word for wood inside it.']),
    (4, None, ['\'The meat must become tender and juicy.\' ', ('barinov', 'сочным.'), ', juicy, comes from juice. ', ('barinov', 'должно'), ' is "must", ending in -o because the word for meat is a neuter word. After ', ('barinov', 'стать'), ', "become", the describing words take special endings.']),
    (5, None, ['Here is the question, \'How much time does each piece need tenderizing?\' ', ('max', 'Сколько времени'), ' is "how much time", and the word for time changes its ending after how much. Max is asking a perfectly fair question.']),
    (6, None, ['\'Do not ask stupid questions, work faster!\' ', ('barinov', 'задавай'), ' used with a question is the Russian way to say "ask". ', ('barinov', 'быстрее!'), ', "faster", is quickly with an ending for "more".']),
    (7, None, ['\'I do everything exactly according to your order.\' After "according to", both words take the ending -u: ', ('max', 'вашему заказу.'), '. ', ('max', 'точно'), ', exactly, also works on its own as a firm "exactly!" or "for sure".']),
    (8, None, ['\'Keep watch over the order on your work table.\' ', ('barinov', 'своём'), ' means "your own", and Russian uses it whenever the owner is the one the sentence is about. ', ('barinov', 'рабочем столе.'), ' is "work table".']),
    (9, None, ['\'I always have complete cleanliness here.\' ', ('max', 'У меня'), ' is "at me" once more, with here and always in the middle. ', ('max', 'чистота.'), ', cleanliness, comes from clean.']),
    (10, None, ['\'Now the pieces are cut beautifully and neatly.\' ', ('barinov', 'кусочки'), ' are little pieces: a piece, made small. ', ('barinov', 'нарезаны'), ', "cut up", describes the result and never says who did the cutting.']),
    (11, None, ['\'Thank you, Chef, I am preparing the next batch!\' ', ('max', 'следующую'), ', "next", grows out of to follow. ', ('max', 'готовлю'), ' is "I am preparing", related to what Max said about preparing the mallet.']),
]
