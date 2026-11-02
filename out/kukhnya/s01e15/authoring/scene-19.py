# Authoring module for kukhnya-s01e15-scene-19.
ID = 'kukhnya-s01e15-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 19
TITLE = "Омлет шефа  (The Chef's Omelet)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва', 'mama': 'Мама'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "It's morning in Lyova's flat, and Barinov has made breakfast for everyone. Lyova suspects it's his way of apologising. Listen in Russian first."
OPENER = 'Slowly, around the breakfast table.'
TRANSITION = 'Now the breakfast scene, uncut.'
OUTRO = "Barinov's omelette does his apologising for him, and nobody says the word out loud. Speak soon."
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('mama', 'Доброе утро, Лёва.', 'Good morning, Lyova.', [(366, 'Доброе утро. Доброе, доброе.')], 'adapted: the greeting goes to Lyova, not to Barinov himself'),
    ('lyova', 'Доброе утро.', 'Good morning.', [(366, 'Доброе, доброе.')], ''),
    ('mama', 'Виктор приготовил такой омлет.', 'Viktor made such an omelet.', [(367, 'Виктор Петрович приготовил такой омлет.')], ''),
    ('lyova', 'Это типа извинения?', 'Is this a kind of apology?', [(368, 'Это типа извинения?')], ''),
    ('barinov', 'Это типа омлет.', 'This is a kind of omelet.', [(369, 'Это типа омлет.')], ''),
    ('barinov', 'Ешь давай.', 'Come on, eat.', [(370, 'Ешь давай, я на работу опоздаю.')], ''),
    ('barinov', 'Я опоздаю на работу.', 'I will be late for work.', [(370, 'я на работу опоздаю.')], ''),
    ('mama', 'Да, кушайте быстрее.', 'Yes, eat faster.', [], ''),
    ('lyova', 'Ладно, я съем это.', 'Alright, I will eat this.', [], ''),
    ('lyova', 'Это очень вкусно.', 'This is very delicious.', [], ''),
    ('mama', 'Нам пора идти.', 'It is time for us to go.', [], ''),
    ('lyova', 'Спасибо за завтрак.', 'Thank you for the breakfast.', [], ''),
]
WALK = [
    (0, None, ["'Good morning, Lyova.' The term morning takes a matching ending, so ", ('mama', 'Доброе'), ' ends in an o-e sound.']),
    (1, None, ["'Good morning.' Lyova hands the same two words ", ('lyova', 'Доброе'), ('lyova', 'утро'), ' straight back.']),
    (2, None, ["'Viktor made such an omelet.' We can examine the speech: ", ('mama', 'такой'), ' means such a, matching the form of ', ('mama', 'омлет'), ', a word Russian took from French. The verb ', ('mama', 'приготовил'), ' means made or cooked.']),
    (3, None, ["'Is this a kind of apology?' The term ", ('lyova', 'типа'), ' comes from type, and is everyday slang for sort of. The term meaning apology shows up here as ', ('lyova', 'извинения'), '.']),
    (4, None, ["'This is a kind of omelet.' Barinov throws ", ('barinov', 'типа'), ' back but leaves ', ('barinov', 'омлет'), ' unchanged. In slang, it does not have to change the term after it.']),
    (5, None, ["'Come on, eat.' We can look at this line: ", ('barinov', 'Ешь'), ' is the order eat for a friend. Tacking on ', ('barinov', 'давай'), ' at the end makes it a nudge.']),
    (6, None, ["'I will be late for work.' Now we can consider the sentence: ", ('barinov', 'опоздаю'), ('barinov', 'на'), ('barinov', 'работу'), ' means to be late onto work, using an ending for when you go to work.']),
    (7, None, ["'Yes, eat faster.' We can consider the words: ", ('mama', 'кушайте'), ' is a cosy eat, with an ending that makes it polite and plural. Notice ', ('mama', 'быстрее'), ' means faster.']),
    (8, None, ["'Alright, I will eat this.' Let us break down the words: ", ('lyova', 'съем'), ' means I will eat it up, and the starting sound adds the finishing. Notice ', ('lyova', 'Ладно'), ' is a grudging alright.']),
    (9, None, ["'This is very delicious.' We will look at this line: ", ('lyova', 'вкусно'), ' comes from taste, and Russian needs no is here.']),
    (10, None, ["'It is time for us to go.' The expression ", ('mama', 'Нам'), ('mama', 'пора'), ' means to us time, which translates as it is time we went. The verb ', ('mama', 'идти'), ' is to go on foot.']),
    (11, None, ["'Thank you for the breakfast.' Use ", ('lyova', 'Спасибо'), ('lyova', 'за'), ' plus the thing, making it ', ('lyova', 'за'), ('lyova', 'завтрак'), '. The term meaning breakfast comes from the same root as tomorrow, both built on morning.']),
]
