# Authoring module for kukhnya-s01e06-scene-04.
ID = 'kukhnya-s01e06-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 4
TITLE = 'Баранина и трюфели  (Mutton and Truffles)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'timur': 'Тимур'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Out at the back of Claude Monet, Chef Barinov meets Timur, who sells him meat and anything else he can lay his hands on. They haggle over a lamb, and then Timur brings out something much more expensive. It's in Russian first."
OPENER = "Let's take it line by line. Bargaining is a good place to pick up prices and numbers."
TRANSITION = 'Now the whole deal again, start to finish.'
OUTRO = 'You can now ask "pochyom", how much, and name a price in hundreds. Timur\'s trick of going from six hundred to seven hundred is one every market in the world knows. See you next time.'
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('barinov', 'Скажи честно, этот баран умер от старости?', 'Tell me honestly, did this sheep die of old age?', [(7, 'Скажи честно, Тимур, ведь этот баран умер от старости')], ''),
    ('timur', 'Зачем обижаешь? Это молодой и вкусный ягнёнок!', 'Why insult me? This is a young and tasty lamb!', [(8, 'зачем обижаешь'), (9, 'молодой и вкусный ягненок')], ''),
    ('barinov', 'У меня на кухне уже хватает баранов.', 'I already have enough sheep in the kitchen.', [(12, 'у меня такие бараны')], ''),
    ('timur', 'Подожди, посмотри вот это отличное мясо!', 'Wait, look at this excellent meat!', [(13, 'подожди. Вот, посмотри вот этого'), (14, 'на этом мясе')], ''),
    ('timur', 'Клянусь, это самое лучшее свежее мясо!', 'I swear, this is the best fresh meat!', [(14, 'Клянусь'), (14, 'на этом мясе')], ''),
    ('barinov', 'Да, этот ягнёнок действительно хороший.', 'Yes, this lamb is really good.', [(15, 'Да, это хороший')], ''),
    ('barinov', 'Хорошо, я беру это мясо.', 'Fine, I will take this meat.', [(17, 'Хорошо, беру')], ''),
    ('timur', 'Шеф, дорогой, а трюфели тебе надо?', 'Chef, my dear, do you need truffles?', [(18, 'Шеф, брат, трюфеля надо')], ''),
    ('barinov', 'Ты опять предлагаешь мне контрабанду?', 'Are you offering me contraband again?', [(20, 'ты опять'), (21, 'Контрабанду мне предлагаешь')], ''),
    ('barinov', 'Конечно надо! Почём ты их продаёшь?', 'Of course I do! How much are you selling them for?', [(21, 'Конечно, надо'), (22, 'Почем')], ''),
    ('timur', 'Тебе по-братски всего шестьсот евро за килограмм.', 'For you as a friend, only six hundred euros per kilogram.', [(22, 'Тебе по-братски всего'), (22, '600 евро за килограмм')], ''),
    ('barinov', 'Отлично, я беру эти трюфели!', 'Great, I will take these truffles!', [(23, 'беру, давай')], ''),
    ('timur', 'Тогда цена выросла до семисот евро!', 'Then the price has risen to seven hundred euros!', [(23, 'Тогда 700')], ''),
    ('barinov', 'Тимур, не наглей и отдавай товар!', "Timur, don't get cheeky and hand over the goods!", [(24, 'Тимур, не наглей')], ''),
]
WALK = [
    (0, None, '\'Tell me honestly, did this sheep die of old age?\' "Baran" is a ram, and calling a person "baran" is calling them a blockhead. "Ot starosti", of old age, is literally \'from oldness\', with "starost" built on "staryy", old.'),
    (1, None, '\'Why insult me? This is a young and tasty lamb!\' "Zachem" is \'what for?\', a bit sharper than the plain "pochemu". "Yagnyonok", lamb, has the -yonok ending Russian uses for baby animals, as in "kotyonok", kitten.'),
    (2, None, '\'I already have enough sheep in the kitchen.\' Here the sheep are Barinov\'s cooks. "Khvataet", there\'s enough, makes what follows change, so barany becomes "baranov".'),
    (3, None, '\'Wait, look at this excellent meat!\' "Podozhdi", wait, is how you\'d stop someone who\'s about to walk off. "Vot eto" works like \'this one right here\', with a pointing finger.'),
    (4, None, '\'I swear, this is the best fresh meat!\' "Klyanus", I swear, is a single verb, and you\'ll hear it from every market seller. "Samoe luchshee" piles \'most\' on top of \'best\', the way people do when they\'re selling.'),
    (5, None, '\'Yes, this lamb is really good.\' "Deystvitelno", really or indeed, is the serious word for it; "pravda", truly, is the chattier one.'),
    (6, None, '\'Fine, I will take this meat.\' "Beru", I take, comes from "brat", to take, though it barely looks like it, so learn it as it is. "Khorosho", good, is also the everyday \'fine, OK\'.'),
    (7, None, '\'Chef, my dear, do you need truffles?\' "Dorogoy" means \'dear\' and \'expensive\' at once, which suits a man selling truffles. "Tebe nado" is \'to you is needed\', the usual way to ask \'do you need\'.'),
    (8, None, '\'Are you offering me contraband again?\' "Opyat", again, is often a complaint, as it is here. "Kontrabanda" turns into "kontrabandu" as the thing on offer.'),
    (9, None, '\'Of course I do! How much are you selling them for?\' Barinov answers with Timur\'s own word, "nado", needed. "Pochyom", how much each, is the market way of asking a price.'),
    (10, None, '\'For you as a friend, only six hundred euros per kilogram.\' "Po-bratski", \'brotherly\', is from "brat", brother, built like "po-russki", in Russian. "Za kilogramm" is \'per kilo\', the "za" you\'ll see on every price tag.'),
    (11, None, '\'Great, I will take these truffles!\' "Eti", these, is the plural of "etot", this, from the lamb line. Barinov says yes at once, which is a mistake at a market.'),
    (12, None, '\'Then the price has risen to seven hundred euros!\' "Vyrosla", it has grown, has -a for "tsena", price, a feminine word. "Do", up to, changes the number too: "semsot" becomes "do semisot".'),
    (13, None, '\'Timur, don\'t get cheeky and hand over the goods!\' "Ne nagley", don\'t be cheeky, comes from "naglyy", cheeky or brazen. "Otdavay" is \'give over\', from ot-, away, and "davat", to give.'),
]
