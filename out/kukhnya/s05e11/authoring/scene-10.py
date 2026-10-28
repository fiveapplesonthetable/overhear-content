ID = 'kukhnya-s05e11-scene-10'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 10
TITLE = "Заказ деда  (Grandpa's Order)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "anya": "alisa", "nastya": "angelina", "guest": "anja"}
LABELS = {"anya": "Макс", "nastya": "Настя", "guest": "Гость"}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'

INTRO = 'The moment his grandmother steps out the door, Max stops Nastya at the bar to ask what his grandfather just ordered. Learning that the old man asked for roast meat and two hundred grams of strong alcohol, Max cancels the order and serves him steamed diet food instead.'

STORY = [
    ('anya', 'Погоди!', 'Wait!', [(150, 'Погоди')], 'adapted'),
    ('anya', 'А что мой дед заказал?', 'And what did my grandpa order?', [(151, 'А что мой дед заказал')], 'adapted'),
    ('nastya', 'Мяса жареного какого-нибудь.', 'Some kind of roast meat.', [(152, 'Мясо жареного какого-нибудь')], 'adapted'),
    ('nastya', 'Выпить что-нибудь покрепче, грамм двести.', 'Something stronger to drink, about two hundred grams.', [(153, 'Выпить что-нибудь покрепче, грамм двести')], 'adapted'),
    ('nastya', 'И компот.', 'And stewed fruit compote.', [(154, 'И компот')], 'adapted'),
    ('anya', 'Ясно. Мясо не неси, только компот.', 'Got it. Do not bring the meat, only the compote.', [(155, 'Ясно'), (154, 'И компот')], 'adapted'),
    ('nastya', 'Хорошо, Макс.', 'Alright, Max.', [(155, 'Ясно')], 'adapted'),
    ('anya', 'Вот твой обед, дед.', 'Here is your lunch, grandpa.', [(151, 'мой дед')], 'adapted'),
    ('guest', 'Вот это сервис!', 'Now that is service!', [(156, 'Вот это сервис')], 'adapted'),
    ('guest', 'А где же моё мясо?', 'And where is my meat?', [(152, 'Мясо')], 'adapted'),
    ('anya', 'Тебе нельзя мясо, дед.', 'You are not allowed meat, grandpa.', [(151, 'дед')], 'adapted'),
    ('guest', 'Ну ладно, внучок.', 'Well alright, grandson.', [(156, 'Вот это сервис')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Wait!' Here the Russian phrasing highlights 'to wait a little' before landing on 'to wait a little'."),
    (1, None, "'And what did my grandpa order?' The meaning hinges on 'and' working together with 'ordered' in spoken Russian."),
    (2, None, "'Some kind of roast meat.' Nastya brings out the contrast between 'meat' and 'roasted' in a few short words."),
    (3, None, "'Something stronger to drink, about two hundred grams.' Nastya anchors the line on 'to drink', while 'two hundred' completes the thought."),
    (4, None, "'And stewed fruit compote.' Nastya centers this short reply on 'stewed fruit drink, compote', letting a few direct words carry the whole meaning."),
    (5, None, "'Got it. Do not bring the meat, only the compote.' Spoken Russian keeps this brisk, leaning on 'clear' and finishing on 'stewed fruit drink'. Nastya answers right away."),
    (6, None, "'Alright, Max.' In Russian, the idea of 'well' flows naturally into 'Max' without extra filler words."),
    (7, None, "'Here is your lunch, grandpa.' The grammar packs 'here' and 'grandfather' into a tight, idiomatic kitchen exchange."),
    (8, None, "'Now that is service!' Notice how Russian expresses 'here' and 'service' with crisp inflection rather than helper words."),
    (9, None, "'And where is my meat?' Here the Russian phrasing highlights 'and' before landing on 'meat'."),
    (10, None, "'You are not allowed meat, grandpa.' The meaning hinges on 'to you' working together with 'grandfather' in spoken Russian."),
    (11, None, "'Well alright, grandson.' the guest anchors the line on 'come on', while 'grandson' completes the thought."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings the bar interception to a close. Notice the comparative adjective meaning something stronger to drink as Nastya reads back the grandfather's order. See you next time!"
CLOSING = ("anya", "Увидимся!")
