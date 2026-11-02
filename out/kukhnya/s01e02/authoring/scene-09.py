# Authoring module for kukhnya-s01e02-scene-09.
ID = 'kukhnya-s01e02-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 9
TITLE = 'Хорошо или плохо?  (Good or Bad?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Senya, Fedya and Max are crowded behind the kitchen window, watching a guest taste their secretly cooked fricassee. She looks calm, and they can't tell what she thinks. Here's the conversation first."
OPENER = "Now let's go over the nervous watching."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Suspense is at its peak, with a guest who calls the waitress over. You've heard the words for good and its opposite, bad."
STORY = [
    ('senya', 'Смотрите, официант уже подал наше блюдо.', 'Look, the waiter has already served our dish.', [], ''),
    ('fedya', 'Она взяла вилку и пробует соус.', 'She picked up the fork and is tasting the sauce.', [], ''),
    ('max', 'Она улыбается или хмурится?', 'Is she smiling or frowning?', [], ''),
    ('senya', 'Она очень внимательно жуёт первый кусочек.', 'She is chewing the first piece very attentively.', [], ''),
    ('fedya', 'И почему-то совсем молчит.', 'And for some reason she is completely silent.', [], ''),
    ('max', 'А это хорошо или плохо?', 'Is that good or bad?', [(130, 'А это хорошо или плохо')], ''),
    ('senya', 'Я сам ничего пока не понимаю.', 'I do not understand anything yet myself.', [], ''),
    ('fedya', 'Главное, чтобы она не позвала директора.', 'The main thing is that she does not call the director.', [], ''),
    ('max', 'Смотрите, она сделала ещё один глоток.', 'Look, she took another sip.', [], ''),
    ('senya', 'Кажется, наше фрикасе ей понравилось!', 'It seems she liked our fricassee!', [], ''),
    ('fedya', 'Не радуйся раньше времени.', 'Do not celebrate too early.', [], ''),
    ('max', 'Ой, она зовёт официантку к столу!', 'Oh, she is calling the waitress to the table!', [], ''),
]
WALK = [
    (0, None, ['\'Look, the waiter has already served our dish.\' The word for "look", ', ('senya', 'Смотрите,'), ', is said to a group. The word for "served", ', ('senya', 'подал'), ', is a completed action word from the same family as the word for "serve".']),
    (1, None, ['\'She picked up the fork and is tasting the sauce.\' The ending on the word for "took", ', ('fedya', 'взяла'), ', shows it is a woman. The next action word, ', ('fedya', 'пробует'), ', translates to both "tastes" and "tries".']),
    (2, None, ['\'Is she smiling or frowning?\' The word for "smiles", ', ('max', 'улыбается'), ', is built from the naming word for a smile, and the word for "frowns" is ', ('max', 'хмурится?'), '. The little connecting word is ', ('max', 'или'), '.']),
    (3, None, ['\'She is chewing the first piece very attentively.\' The word for a piece, ', ('senya', 'кусочек.'), ', literally translates to a small piece. The describing word for attentively, ', ('senya', 'внимательно'), ', is built from the word for attention.']),
    (4, None, ['\'And for some reason she is completely silent.\' The word for "why" plus a short ending translates to "for some reason", ', ('fedya', 'почему-то'), '. Speakers add that short ending to question words when the answer is unknown.']),
    (5, None, ['\'Is that good or bad?\' The phrase ', ('max', 'хорошо или плохо?'), ' translates to "good or bad", two opposites joined by the word for "or". They are short and easy to remember.']),
    (6, None, ['\'I do not understand anything yet myself.\' The word for "nothing", ', ('senya', 'ничего'), ', is paired with a negative action word to make a double negative once more. The word for "yet" here, ', ('senya', 'пока'), ', is the same word as the casual "bye".']),
    (7, None, ['\'The main thing is that she does not call the director.\' The word for "the main thing", ', ('fedya', 'Главное,'), ', opens it, then the word for "so that", ', ('fedya', 'чтобы'), '. After that, the action word takes a completed form, ', ('fedya', 'не позвала'), ', even though it is about a hope.']),
    (8, None, ['\'Look, she took another sip.\' The word for a sip, ', ('max', 'глоток.'), ', translates to one swallow: the matching action word means to swallow. The phrase ', ('max', 'ещё один'), ' translates to "one more".']),
    (9, None, ['\'It seems she liked our fricassee!\' The language turns liking around: the fricassee does the pleasing, and the word for "to her", ', ('senya', 'ей'), ', is on the receiving end. So the action word, ', ('senya', 'понравилось!'), ', matches the dish, a neutral naming word, not her. The word ', ('senya', 'Кажется,'), ' up front softens it, literally meaning "it seems".']),
    (10, None, ['\'Do not celebrate too early.\' The phrase for "don\'t rejoice", ', ('fedya', 'Не радуйся'), ', is built from the describing word for glad. The phrase for "too early", ', ('fedya', 'раньше времени.'), ', literally translates to "earlier than time".']),
    (11, None, ['\'Oh, she is calling the waitress to the table!\' The word for a female waiter, ', ('max', 'официантку'), ', is built from the word for a male waiter with a female ending. The phrase for "to the table", ', ('max', 'к столу!'), ', adds a little sound to the word for table after the connecting word.']),
]
CLOSING = ("senya", "Счастливо!")
