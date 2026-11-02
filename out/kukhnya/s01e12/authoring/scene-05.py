# Authoring module for kukhnya-s01e12-scene-05.
ID = 'kukhnya-s01e12-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 5
TITLE = 'Опасные конкуренты  (Dangerous Competitors)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = "Back in the dining room, Vika has found a leaflet for an Italian restaurant opening next door, and she shows it to Chef Barinov. She wants to change the menu, and he does not. Listen to the argument in Russian, then we'll unpack it."
OPENER = 'Now in pieces, and keep an eye on who is afraid of whom.'
TRANSITION = 'Once more, the full argument, uninterrupted.'
OUTRO = "Barinov stomps off, and Vika is left with a leaflet and a problem. Count how often he says 'my' about the kitchen when you hear it again."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('vika', 'Витя, посмотри на этот рекламный буклет!', 'Vitya, look at this advertising flyer!', [(41, 'Полюбуйся.')], ''),
    ('barinov', 'Что это за странное слово Аркобалено?', 'What kind of strange word is Arcobaleno?', [(42, 'ресторана Аркобалена.')], ''),
    ('barinov', 'Это вообще что, редкая болезнь почек?', 'What is that anyway, a rare kidney disease?', [(45, 'Это вообще что, болезнь почек?')], ''),
    ('vika', 'Аркобалено значит радуга по-итальянски, Витя.', 'Arcobaleno means rainbow in Italian, Vitya.', [(46, 'Аркабалена – это радуга по-итальянски.')], ''),
    ('barinov', 'Я не пойду в их кафе!', 'I will not go to their cafe!', [(43, 'я к ним не приду.')], ''),
    ('vika', 'Через неделю они открываются рядом с нами.', 'In a week they are opening right next to us.', [(48, 'У нас под боком через неделю открываются конкуренты.')], ''),
    ('barinov', 'Ой, боюсь, кафе Радуга нас разорит!', 'Oh, I am scared, cafe Rainbow will bankrupt us!', [(49, 'Боюсь, боюсь. Кафе «Радуга» разорит нас.')], ''),
    ('vika', 'Витя, нам пора привлечь новых гостей.', 'Vitya, it is time for us to attract new guests.', [(54, 'Нам нужно привлечь людей чем-то новым.')], ''),
    ('vika', 'Нам нужно срочно поменять наше меню.', 'We need to urgently change our menu.', [(55, 'Меню поменять.')], ''),
    ('barinov', 'Мы лучшие, и нас любят за это!', 'We are the best, and people love us for that!', [(55, 'Мы такие, какие есть, и за это нас любят.')], ''),
    ('vika', 'Ресторану нужны свежие и смелые идеи.', 'The restaurant needs fresh and bold ideas.', [], ''),
    ('barinov', 'Меняй всё в зале, на своей территории!', 'Change everything in the dining room, on your turf!', [(56, 'меняй на своей территории, в зале.')], ''),
    ('barinov', 'А на кухню ко мне не лезь!', 'And do not get into my kitchen!', [(57, 'А ко мне на кухню не лезь.')], ''),
]
WALK = [
    (0, None, ["'Vitya, look at this advertising flyer!' Listen to how ", ('vika', 'Витя'), ' is the short, familiar form of Viktor. Here we have ', ('vika', 'рекламный'), ('vika', 'буклет'), " is just 'advert' with a new ending, plus 'booklet' with a Russian accent."]),
    (1, None, ["'What kind of strange word is Arcobaleno?' Barinov uses a handy frame: ", ('barinov', 'Что'), ('barinov', 'это'), ('barinov', 'за'), " plus a noun asks 'what kind of ... is this?'. 'Word' is neuter, so 'strange' takes the matching ending to make ", ('barinov', 'странное'), ('barinov', 'слово'), '.']),
    (2, None, ["'What is that anyway, a rare kidney disease?' Now we can consider the speech: ", ('barinov', 'вообще'), " means 'in general' and 'at all', and Russians put it everywhere. Notice for illness, ", ('barinov', 'болезнь'), ", is feminine, so 'rare' becomes ", ('barinov', 'редкая'), ". Notice how 'kidneys' is ", ('barinov', 'почек'), ', a plural shape.']),
    (3, None, ["'Arcobaleno means rainbow in Italian, Vitya.' The term ", ('vika', 'значит'), " means 'means' and it's also a filler like 'so' in speech. 'In Italian' is one word: ", ('vika', 'по'), '-', ('vika', 'итальянски'), ", with parts added front and back to make 'in that language'."]),
    (4, None, ["'I will not go to their cafe!' Notice how ", ('barinov', 'их'), " means 'their' and never changes, whatever it describes. 'Cafe' doesn't change either."]),
    (5, None, ["'In a week they are opening right next to us.' Now we can inspect the dialogue: ", ('vika', 'Через'), ('vika', 'неделю'), " is how Russians say 'in a week'. Notice for 'they open', ", ('vika', 'открываются'), ", ends with a sound that makes it 'they open themselves'."]),
    (6, None, ["'Oh, I am scared, cafe Rainbow will bankrupt us!' Barinov uses the Russian word for 'rainbow', ", ('barinov', 'Радуга'), ", as an insult. 'I am scared' is a single word, ", ('barinov', 'боюсь'), '.']),
    (7, None, ["'Vitya, it is time for us to attract new guests.' The expression ", ('vika', 'нам'), ('vika', 'пора'), " means 'to us time', which is how Russians say 'it's time for us'. Notice how ", ('vika', 'новых'), ('vika', 'гостей'), ' takes the plural shape for a group of things being attracted.']),
    (8, None, ["'We need to urgently change our menu.' Now we can look at this line: ", ('vika', 'нужно'), " means 'necessary', and the action word follows it. Notice for 'menu', ", ('vika', 'меню'), ", doesn't change shape, just like 'cafe'."]),
    (9, None, ["'We are the best, and people love us for that!' Nobody says 'they' here. The bare word ", ('barinov', 'любят'), " means 'people love'. Russian does that a lot when nobody in particular is meant."]),
    (10, None, ["'The restaurant needs fresh and bold ideas.' The term ", ('vika', 'Ресторану'), " takes a 'u' sound since the restaurant is the one in need. 'Bold' and 'fresh' both end in 'e' because ", ('vika', 'идеи'), ' is a group.']),
    (11, None, ["'Change everything in the dining room, on your turf!' Now let's look at this part: ", ('barinov', 'Меняй'), " is the order 'change'. 'Hall' turns into ", ('barinov', 'в'), ('barinov', 'зале'), " after 'in'. The expression ", ('barinov', 'на'), ('barinov', 'своей'), ('barinov', 'территории'), " means 'on your own territory', using the 'own' word again."]),
    (12, None, ["'And do not get into my kitchen!' Let's break down the words: ", ('barinov', 'не'), ('barinov', 'лезь'), " is the rude, informal way of saying 'stay out'. The expression ", ('barinov', 'ко'), ('barinov', 'мне'), " is 'to me', with an extra vowel to make it easier to say."]),
]
