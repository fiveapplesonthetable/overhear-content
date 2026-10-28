# Authoring module for kukhnya-s05e02-scene-01.
ID = 'kukhnya-s05e02-scene-01'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 1
TITLE = 'Ресторан при бутик-отеле «Элеон»  (A Restaurant Inside Boutique Hotel Eleon)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = 'At the start of Episode 2, Denis introduces Boutique Hotel Eleon and explains the three big differences between a standalone restaurant and Restaurant Victor inside a hotel. Listen to the Russian narration first.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that introduces the new rhythm of life at Boutique Hotel Eleon. Notice the impersonal verb 'prikhoditsya' used with the dative plural for 'the cooks have to'. Until next time!"
CLOSING = ('denis', 'До встречи!')
STORY = [
    ('denis', 'Перед вами наш новый отель.', 'Before you is our new hotel.', [(1, 'Перед вами')], 'adapted'),
    ('denis', 'Здесь находится наш ресторан.', 'Our restaurant is located right here.', [(2, 'Здесь находится ресторан')], 'adapted'),
    ('denis', 'Мы теперь работаем в этом отеле.', 'We now work in this hotel.', [(2, 'в котором мы работаем')], 'adapted'),
    ('denis', 'Чем отличается ресторан при отеле?', 'How does a hotel restaurant differ?', [(3, 'чем отличается обычный ресторан от ресторана при отеле?')], 'adapted'),
    ('denis', 'В отеле всегда есть завтраки.', 'In a hotel there are always breakfasts.', [(4, 'в отеле есть завтраки')], 'adapted'),
    ('denis', 'Поварам приходится рано вставать.', 'The cooks have to get up early.', [(5, 'поварам приходится вставать')], 'adapted'),
    ('barinov', 'Мы встаём каждое утро рано.', 'We get up early every morning.', [(5, 'утра')], 'adapted'),
    ('denis', 'Гости ресторана — это не только посетители.', 'Restaurant guests are not just casual visitors.', [(6, 'гости ресторана – это не только'), (6, 'посетители')], 'adapted'),
    ('denis', 'Это ещё и постояльцы отеля.', 'They are also hotel residents.', [(7, 'но и постояльцы отеля')], 'adapted'),
    ('denis', 'Мы должны кормить всех гостей.', 'We must feed all the guests.', [(9, 'мы должны кормить')], 'adapted'),
    ('denis', 'Кто-то не хочет вставать с кровати.', 'Someone does not want to get out of bed.', [(10, 'с кровати')], 'adapted'),
    ('barinov', 'Им лень спуститься в ресторан!', 'They are too lazy to come down to the restaurant!', [(10, 'спуститься в ресторан')], 'adapted'),
]
WALK = [
    (0, None, "'Before you is our new hotel.' Denis reminds Barinov that before Barinov is their new hotel before the moment passes."),
    (1, None, "'Our restaurant is located right here.' Because their restaurant is located right here, Denis treats the matter as settled."),
    (2, None, "'We now work in this hotel.' With the restaurant and hotel in play, Denis keeps this short reply brisk and direct."),
    (3, None, "'How does a hotel restaurant differ?' Wondering how a hotel restaurant differ is how Denis puts Barinov on the spot."),
    (4, None, "'In a hotel there are always breakfasts.' Claiming that in a hotel there are always breakfasts sounds confident, even if Barinov has doubts."),
    (5, None, "'The cooks have to get up early.' Pointing out that the cooks have to get up early gives Barinov a sobering reality check."),
    (6, None, "'We get up early every morning.' Getting up early every morning moves the conversation forward without extra drama."),
    (7, None, '\'Restaurant guests are not just casual visitors.\' Realizing that restaurant guests are not just casual visitors changes how Denis handles the situation. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (8, None, '\'They are also hotel residents.\' Noting that they are also hotel residents keeps Denis\'s side of the story simple and clear. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (9, None, "'We must feed all the guests.' Even though they must feed all the guests, Denis keeps a steady face in front of Barinov."),
    (10, None, "'Someone does not want to get out of bed.' Admitting that someone does not want to get out of bed shows Denis being honest for a change."),
    (11, None, "'They are too lazy to come down to the restaurant!' Because they are too lazy to come down to the restaurant, Barinov does not bother softening the blow for Denis. Russian puts the key word right up front so his emotion lands on the first beat."),
]
