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
    (0, None, '\'Wait!\' Max shows an honest rhythm in the room, leaning on "pogodi" ("wait") as a compact, one-word response that needs no extra words.'),
    (1, None, '\'And what did my grandpa order?\' Max checks quietly in this moment, joining "ded" ("grandfather") to "zakazal" ("ordered") so every word pulls its weight.'),
    (2, None, '\'Some kind of roast meat.\' Nastya keeps a grounded position straight away, using "myasa" (from "myaso", "meat") alongside "zharenogo" ("roasted, fried") to shape the meaning.'),
    (3, None, '\'Something stronger to drink, about two hundred grams.\' Nastya favors a resolute style right away, combining "vypit" ("to drink") and "pokrepche" ("stronger") so the key meaning lands right away.'),
    (4, None, '\'And stewed fruit compote.\' Nastya presents a playful position without hesitation, putting all the weight on "kompot" ("compote") so the reply lands immediately.'),
    (5, None, '\'Got it. Do not bring the meat, only the compote.\' Max keeps a natural posture with Nastya, putting "yasno" ("clear, got it") alongside "myaso" ("meat") in a tight, everyday turn of phrase.'),
    (6, None, '\'Alright, Max.\' Nastya conveys an honest bearing as they talk, anchoring the Russian line on "khorosho" ("good, fine") and "maks" ("Max") without extra filler.'),
    (7, None, '\'Here is your lunch, grandpa.\' Max maintains a clear posture at this moment, leaning on "obed" ("lunch") before closing the thought with "ded" ("grandfather").'),
    (8, None, '\'Now that is service!\' The guest holds a lively manner in this beat, linking "servis" ("service"), "vot" ("there, here"), and "eto" ("this") in one brisk exchange.'),
    (9, None, '\'And where is my meat?\' The guest asks briskly at this point, linking "gde" ("where"), "myaso" ("meat"), and "zhe" ("but, after all") in one brisk exchange.'),
    (10, None, '\'You are not allowed meat, grandpa.\' Max shares a direct style in the conversation, putting "nelzya" ("not allowed") alongside "myaso" ("meat") in a tight, everyday turn of phrase.'),
    (11, None, '\'Well alright, grandson.\' The guest takes a grounded posture straight away, leaning on "vnuchok" ("grandson") before closing the thought with "nu" ("oh, come on").'),
]
