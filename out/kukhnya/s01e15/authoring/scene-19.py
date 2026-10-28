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
    (0, None, "'Good morning, Lyova.' 'Utro' is a neuter word, so 'dobroe', good, ends in 'oe' to match."),
    (1, None, "'Good morning.' Lyova hands the same two words straight back."),
    (2, None, "'Viktor made such an omelet.' 'Takoy' is 'such a', in the masculine to match 'omlet', a word Russian took from French. 'Prigotovil' is 'made, cooked'."),
    (3, None, "'Is this a kind of apology?' 'Tipa' comes from 'tip', type, and is everyday slang for 'sort of'. 'Izvinenie', apology, shows up here as 'izvineniya'."),
    (4, None, "'This is a kind of omelet.' Barinov throws 'tipa' back but leaves 'omlet' unchanged. In slang, 'tipa' doesn't have to change the word after it."),
    (5, None, "'Come on, eat.' 'Esh'' is the order 'eat!', for a friend. 'Davay' tacked on at the end makes it a nudge."),
    (6, None, "'I will be late for work.' 'Opozdat na rabotu' is 'to be late onto work': 'na' with the 'u' ending, as when you go to work."),
    (7, None, "'Yes, eat faster.' 'Kushayte' is a cosy 'eat', with the 'te' that makes it polite and plural. 'Bystree' is 'faster'."),
    (8, None, "'Alright, I will eat this.' 'Syem' is 'I will eat it up', and the 's' at the front adds the finishing. 'Ladno' is a grudging 'alright'."),
    (9, None, "'This is very delicious.' 'Vkusno', tasty, comes from 'vkus', taste, and Russian needs no 'is'."),
    (10, None, "'It is time for us to go.' 'Nam pora', literally 'to us time', is 'it's time we went'. 'Idti' is to go on foot."),
    (11, None, "'Thank you for the breakfast.' 'Spasibo za' plus the thing: 'za zavtrak'. 'Zavtrak' comes from the same root as 'zavtra', tomorrow; both are built on 'utro', morning."),
]
