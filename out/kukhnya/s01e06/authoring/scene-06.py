# Authoring module for kukhnya-s01e06-scene-06.
ID = 'kukhnya-s01e06-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = 'Проверка на кухне  (Kitchen Inspection)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Max has just learned that the shaving story was a prank, and now there's a real inspection on the way. In the kitchen at Claude Monet, Vika, who runs the dining room, warns Chef Barinov that the sanitary inspector is coming, and Barinov has his own idea of how to deal with it. It's in Russian first."
OPENER = "Let's go back through it. Vika is exasperated, and Barinov is relaxed in a way that should worry you."
TRANSITION = 'Now the full scene once more.'
OUTRO = 'Hold on to "esli by", if only. Put "by" after "esli" and again after "my", and the two together make \'would\'. See you next time.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Они всех новичков так обманывают?', 'Do they trick all newcomers like that?', [(53, 'Они всех новичков так разводят')], ''),
    ('max', 'Мне надо скорее надеть поварской колпак.', "I must quickly put on my chef's hat.", [(54, 'И колпак не забудь надеть')], ''),
    ('vika', 'Шеф, сегодня пятнадцатое число, ты помнишь?', 'Chef, today is the fifteenth, do you remember?', [(60, 'Сегодня пятнадцатое число'), (61, 'Ты помнишь')], ''),
    ('vika', 'Скоро придёт санитарная инспекция ресторана.', "Soon the restaurant's sanitary inspection will arrive.", [(61, 'Придет СЭС')], ''),
    ('vika', 'А у тебя на кухне опять бардак!', 'And in your kitchen there is a mess again!', [(61, 'а у тебя тут опять бардак')], ''),
    ('barinov', 'Где ты видишь беспорядок, дорогая?', 'Where do you see a mess, my dear?', [(62, 'Где бардак'), (66, 'Дорогуша')], ''),
    ('barinov', 'Посмотри сама, какая здесь чистая полка!', 'Look for yourself what a clean shelf this is!', [(63, 'Посмотри, какая чистая полка')], ''),
    ('barinov', 'Маленькие деньги решают любые большие проблемы.', 'A little money solves any big problems.', [(64, 'Маленькие деньги решают большие проблемы')], ''),
    ('vika', 'Если бы был порядок, мы бы не платили!', "If there were order, we wouldn't pay!", [(65, 'Если бы у тебя на кухне был порядок, мы бы не платили')], ''),
    ('barinov', 'На кухне ресторана всегда много работы.', 'There is always a lot of work in a restaurant kitchen.', [(67, 'тут никто не готовил')], ''),
    ('barinov', 'Инспекторы ищут нарушения только ради денег.', 'Inspectors look for violations only for money.', [(68, 'нарушения ищут'), (69, 'чтобы за них платили')], ''),
    ('vika', 'Надо срочно навести идеальную чистоту.', 'We must urgently establish perfect cleanliness.', [(72, 'убирать')], ''),
    ('max', 'Кажется, сегодня у нас большие проблемы.', 'It seems today we have big problems.', [], ''),
    ('max', 'Я пойду мыть полы на кухне.', 'I will go wash the floors in the kitchen.', [], ''),
]
WALK = [
    (0, None, '\'Do they trick all newcomers like that?\' "Novichok", newcomer, is built on "novyy", new. "Obmanyvayut", they deceive, is the general word for cheating or fooling someone.'),
    (1, None, '\'I must quickly put on my chef\'s hat.\' "Nadet" is putting clothes on yourself; dressing someone else is "odet". "Kolpak" is the tall cook\'s hat, and "povarskoy", cook\'s, comes from "povar".'),
    (2, None, '\'Chef, today is the fifteenth, do you remember?\' "Pomnish", you remember, is the "ty" form, and Vika says "ty" to the chef as an equal. "Ty pomnish" at the end of a sentence is a nudge: \'you haven\'t forgotten, have you?\''),
    (3, None, '\'Soon the restaurant\'s sanitary inspection will arrive.\' "Pridyot", will come, is from the same family as "prikhodit", comes. "Restoran" becomes "restorana" for \'of the restaurant\'.'),
    (4, None, '\'And in your kitchen there is a mess again!\' "U tebya na kukhne", \'at you in the kitchen\', is how Russian says \'in your kitchen\'. "Bardak" is a colloquial, slightly rough word for a mess.'),
    (5, None, '\'Where do you see a mess, my dear?\' Barinov swaps her "bardak" for the proper word, "besporyadok", which is "bez", without, plus "poryadok", order. "Dorogaya" is \'my dear\' for a woman, said with an edge.'),
    (6, None, '\'Look for yourself what a clean shelf this is!\' "Sama", yourself, ends in -a because he\'s talking to a woman. "Kakaya", which, turns into \'what a\' when you exclaim it.'),
    (7, None, '\'A little money solves any big problems.\' "Dengi", money, is always plural in Russian, so \'solve\' is plural too: "reshayut". It\'s Barinov\'s whole philosophy in one sentence.'),
    (8, None, '\'If there were order, we wouldn\'t pay!\' The little word "by" turns up twice, once after "esli", if, and once after "my", we. Together they make \'if there were... we would\'.'),
    (9, None, '\'There is always a lot of work in a restaurant kitchen.\' After "mnogo", a lot, the noun changes: "rabota" becomes "mnogo raboty". "Na kukhne restorana" stacks it up: \'in the kitchen of the restaurant\'.'),
    (10, None, '\'Inspectors look for violations only for money.\' "Ishchut", they look for, comes from "iskat", with sk turning into shch. After "radi", for the sake of, "dengi" becomes "deneg".'),
    (11, None, '\'We must urgently establish perfect cleanliness.\' "Navesti chistotu" is the set phrase for cleaning a place up properly. "Chistota", cleanliness, is from "chistyy", clean, which you heard on the shelf.'),
    (12, None, '\'It seems today we have big problems.\' "Kazhetsya", it seems, is a handy way to start any cautious remark. "U nas", \'at us\', is the \'we have\' you\'ve heard all scene.'),
    (13, None, '\'I will go wash the floors in the kitchen.\' "Poydu myt" is \'I\'ll go and wash\', with the second verb left in its plain form. Russians wash "poly", floors, in the plural, even in one room.'),
]
