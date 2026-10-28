# Authoring module for kukhnya-s05e11-scene-10.
ID = 'kukhnya-s05e11-scene-10'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 10
TITLE = "Заказ деда  (Grandpa's Order)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'
INTRO = 'The moment his grandmother steps out the door, Max stops Nastya at the bar to ask what his grandfather just ordered. Learning that the old man asked for roast meat and two hundred grams of strong alcohol, Max cancels the order and serves him steamed diet food instead.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings the bar interception to a close. Notice the comparison word meaning something stronger to drink as Nastya reads back the grandfather's order. See you next time!"
CLOSING = ('max', 'Увидимся!')
STORY = [
    ('max', 'Погоди!', 'Wait!', [(150, 'Погоди')], 'adapted'),
    ('max', 'А что мой дед заказал?', 'And what did my grandpa order?', [(151, 'А что мой дед заказал')], 'adapted'),
    ('nastya', 'Мяса жареного какого-нибудь.', 'Some kind of roast meat.', [(152, 'Мясо жареного какого-нибудь')], 'adapted'),
    ('nastya', 'Выпить что-нибудь покрепче, грамм двести.', 'Something stronger to drink, about two hundred grams.', [(153, 'Выпить что-нибудь покрепче, грамм двести')], 'adapted'),
    ('nastya', 'И компот.', 'And stewed fruit compote.', [(154, 'И компот')], 'adapted'),
    ('max', 'Ясно. Мясо не неси, только компот.', 'Got it. Do not bring the meat, only the compote.', [(155, 'Ясно'), (154, 'И компот')], 'adapted'),
    ('nastya', 'Хорошо, Макс.', 'Alright, Max.', [(155, 'Ясно')], 'adapted'),
    ('max', 'Вот твой обед, дед.', 'Here is your lunch, grandpa.', [(151, 'мой дед')], 'adapted'),
    ('guest', 'Вот это сервис!', 'Now that is service!', [(156, 'Вот это сервис')], 'adapted'),
    ('guest', 'А где же моё мясо?', 'And where is my meat?', [(152, 'Мясо')], 'adapted'),
    ('max', 'Тебе нельзя мясо, дед.', 'You are not allowed meat, grandpa.', [(151, 'дед')], 'adapted'),
    ('guest', 'Ну ладно, внучок.', 'Well alright, grandson.', [(156, 'Вот это сервис')], 'adapted'),
]
WALK = [
    (0, None, '\'Wait!\' Max pushes back openly before Nastya and lands on "pogodi" ("wait", built on "pogodit") to keep the statement grounded.'),
    (1, None, '\'And what did my grandpa order?\' Focusing on the grandfather before Nastya, Max puts the question word "chto" right at the start so Nastya hears the focus immediately.'),
    (2, None, "'Some kind of roast meat.' Nastya replies bluntly without a pause, shifting the mood of the conversation in a single beat."),
    (3, None, '\'Something stronger to drink, about two hundred grams.\' Mentioning the grams with Max, Nastya leans on "pokrepche" ("stronger", a form of "krepkiy") to give the remark its edge.'),
    (4, None, "'And stewed fruit compote.' Mentioning the compote during the talk, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (5, None, "'Got it. Do not bring the meat, only the compote.' Max proceeds sharply with a nod, without trying to dress up how he really feels."),
    (6, None, '\'Alright, Max.\' Nastya follows up earnestly in front of Max and brings in "khorosho" ("good, fine") to make the meaning unmistakable.'),
    (7, None, '\'Here is your lunch, grandpa.\' Focusing on the lunch around Nastya, Max links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (8, None, "'Now that is service!' The guest proceeds pointedly without a pause, making his position completely clear."),
    (9, None, '\'And where is my meat?\' Talking about his meat in the exchange, the guest puts the emphasis on "myaso" ("meat") in the middle of the talk.'),
    (10, None, '\'You are not allowed meat, grandpa.\' Returning to the meat right here, Max leans on "nelzya" ("it is not allowed, one must not"), which carries the whole predicate in Russian without needing "it is".'),
    (11, None, '\'Well alright, grandson.\' The guest smoothly chooses this word of agreement toward Max using "ladno" ("alright") — built from the old Russian root for harmony and order, used every day for "okay, fine".'),
]
