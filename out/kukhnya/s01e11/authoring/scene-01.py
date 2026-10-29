# Authoring module for kukhnya-s01e11-scene-01.
ID = 'kukhnya-s01e11-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 1
TITLE = 'Кто главный в ресторане  (Who Runs the Restaurant)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "Welcome to Kukhnya, a Russian comedy set in the kitchen of Claude Monet, a smart French restaurant in Moscow. Barinov is the loud head chef, Max the newest cook, and Kostya the bartender who is Max's best friend. In this episode a secret restaurant critic is expected, and nobody knows who he is. It starts quietly, at the bar, where Max and Kostya ask who really runs the place. You'll hear it in Russian first, and you don't need to catch every word."
OPENER = 'First line first.'
TRANSITION = 'Time to hear it all again.'
OUTRO = 'Max and Kostya agree that the guest comes first. That idea will be tested very soon, once the word about the critic gets out. Catch you next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, кто самый главный в нашем ресторане?', 'Kostya, who is the most important in our restaurant?', [(1, 'кто главный в ресторане?')], ''),
    ('kostya', 'Может быть, наш строгий шеф-повар?', 'Maybe our strict head chef?', [(3, 'Шеф?')], ''),
    ('max', 'Или богатый хозяин ресторана Дмитрий?', 'Or the rich restaurant owner Dmitry?', [(4, 'ресторана?')], ''),
    ('kostya', 'А может, наш строгий директор Виктория?', 'Or maybe our strict director Viktoria?', [(2, 'Директор?')], ''),
    ('max', 'Нет, самые главные здесь — это гости.', 'No, the most important here are the guests.', [(5, 'Главный в ресторане — это гости.')], ''),
    ('kostya', 'Это правда, наши гости бывают разные.', 'That is true, our guests can be very different.', [(7, 'гости бывают разные.')], ''),
    ('max', 'Одни гости бывают слишком жадными.', 'Some guests can be too stingy.', [(8, 'Бывают очень жадные.')], ''),
    ('kostya', 'Другие гости бывают очень весёлыми.', 'Other guests can be very cheerful.', [(13, 'Бывают очень')], ''),
    ('max', 'И они часто обнимают тебя?', 'And do they often hug you?', [], ''),
    ('kostya', 'Да, постоянно говорят разные добрые слова.', 'Yes, they constantly say various kind words.', [(17, 'Хороший ты парень, Костя.')], ''),
    ('max', 'Они платят деньги за этот обед.', 'They pay money for this lunch.', [], ''),
    ('kostya', 'Поэтому мы всегда улыбаемся каждому гостю.', 'Therefore we always smile at every guest.', [], ''),
    ('max', 'Гость всегда остаётся самым главным.', 'The guest always remains the most important.', [], ''),
]
WALK = [
    (0, None, '\'Kostya, who is the most important in our restaurant?\' Russian says "kto samy glavny", "who most main", with no "is" at all. "Glavny", "main", grows out of "golova", "head", so the main person is the one at the head.'),
    (1, None, '\'Maybe our strict head chef?\' "Mozhet byt", word for word "can be", is the Russian "maybe". And the job title is "shef-povar", two words joined by a hyphen, "chef-cook". Kostya names Barinov first.'),
    (2, None, '\'Or the rich restaurant owner Dmitry?\' There\'s no "of" here: "khozyain restorana" is "owner restaurant-of", and the -a on "restorana" does that job. "Bogaty" is "rich".'),
    (3, None, '\'Or maybe our strict director Viktoria?\' "A mozhet" is a shorter "or maybe", with "byt" dropped. Kostya uses Vika\'s full name, Viktoria, the way you\'d name a boss. He is running down the staff list.'),
    (4, None, '\'No, the most important here are the guests.\' Where English says "are", Russian often puts a pause and "eto", "this": "samye glavnye zdes, eto gosti". "Samye glavnye" ends in -ye to match the plural "gosti".'),
    (5, None, '\'That is true, our guests can be very different.\' Agreeing, Kostya says "eto pravda", word for word "this truth", with no "is" in it. The verb "byvayut" means "they tend to be, now and then", so guests come in all kinds.'),
    (6, None, '\'Some guests can be too stingy.\' Russian lines up "odni" and "drugie", "ones" and "others", just like English "some ... others". "Zhadny", "stingy", is literally "greedy". "Slishkom" is "too".'),
    (7, None, '\'Other guests can be very cheerful.\' "Drugie", "others", answers the "odni" of the last line. "Vesyolymi", "cheerful", has an -ymi ending, the one that comes after "byvayut".'),
    (8, None, '\'And do they often hug you?\' "Obnimayut" is "they hug", from "obnimat", to put your arms around someone. "Chasto" is "often". Max is teasing his friend.'),
    (9, None, '\'Yes, they constantly say various kind words.\' "Postoyanno", "constantly", is from the same family as "postoyannye gosti", "regular guests", the constant ones. "Dobrye slova" is "kind words".'),
    (10, None, '\'They pay money for this lunch.\' Before the thing you buy, "za" means "in exchange for": you pay "za obed", for the lunch. "Platyat" is the "they" form of "platit", "to pay". Max states the plain commercial truth.'),
    (11, None, '\'Therefore we always smile at every guest.\' "Ulybaemsya", "we smile", ends in -sya, a habit some Russian verbs have. "Kazhdomu gostyu" is "to every guest": you smile "to" someone in Russian.'),
    (12, None, '\'The guest always remains the most important.\' "Ostayotsya", "remains", has the -sya ending again. After it, "samy glavny" becomes "samym glavnym". A tidy last line.'),
]
