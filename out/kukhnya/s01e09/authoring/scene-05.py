# Authoring module for kukhnya-s01e09-scene-05.
ID = 'kukhnya-s01e09-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 5
TITLE = 'Прятки с дядей Лёвой  (Hide and Seek with Uncle Lyova)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'alisa': 'Алиса', 'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "Barinov has work to do, so he hands his daughter to the tall sous-chef Lyova and gives him three strict orders. Alisa has her own plans. We'll hear it through once before I say a word about it."
OPENER = "I'll take you through it now."
TRANSITION = 'Everything again, from the beginning.'
OUTRO = 'Alisa has her new playmate, and Lyova has a hundred to count. He will need to open his eyes eventually. Until then.'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('barinov', 'Лёва, сиди здесь и смотри за Алисой.', 'Lyova, sit here and watch over Alisa.', [(93, 'Сиди здесь.'), (94, 'Смотри за Алисой.')], ''),
    ('barinov', 'Глаз с нее не спускай.', 'Do not take your eyes off her.', [(95, 'Глаз с нее не спускай.')], ''),
    ('barinov', 'И не давай шоколад, у нее аллергия.', 'And do not give her chocolate, she has an allergy.', [(96, 'И не давай шоколад. У нее аллергия.')], ''),
    ('alisa', 'Дядя Лёва, давай играть!', 'Uncle Lyova, let us play!', [(97, 'Давай играть.')], ''),
    ('lyova', 'Может, лучше просто посидим?', 'Maybe we could just sit here instead?', [(98, 'Может, лучше просто посидим?')], ''),
    ('alisa', 'Я папе скажу, он тебя уволит!', 'I will tell Dad, he will fire you!', [(99, 'Я папе скажу. Он тебя уволит.')], ''),
    ('lyova', 'Хорошо, во что будем играть?', 'All right, what should we play?', [(101, 'Во что будем играть?')], ''),
    ('alisa', 'Давай в прятки!', 'Let us play hide and seek!', [], ''),
    ('lyova', 'А кто будет прятаться?', 'And who will hide?', [(103, 'А кто будет прятаться?')], ''),
    ('alisa', 'Конечно, я буду прятаться!', 'Of course, I will hide!', [(104, 'Конечно, я.')], ''),
    ('alisa', 'Тебя такого длинного нигде не спрячешь.', 'You are so tall, you cannot be hidden anywhere.', [(104, 'Тебя такого длинного нигде не спрячешь.')], ''),
    ('alisa', 'Закрывай глаза, считай до ста.', 'Close your eyes, count to a hundred.', [(105, 'Закрывай глаза, считай до ста.')], ''),
    ('lyova', 'Раз, два, три, четыре...', 'One, two, three, four...', [(106, 'Раз, два.')], ''),
    ('alisa', 'Считай медленно, я иду прятаться!', 'Count slowly, I am going to hide!', [], ''),
]
WALK = [
    (0, None, ["'Lyova, sit here and watch over Alisa.' The boss commands his sous-chef to watch over ", ('barinov', 'Алисой'), ', giving him clear instructions to stay put.']),
    (1, None, ["'Do not take your eyes off her.' This serious-sounding idiom starts with the word ", ('barinov', 'Глаз'), ', emphasizing that he should never look away from the child.']),
    (2, None, ["'And do not give her chocolate, she has an allergy.' He adds a medical warning by mentioning ", ('barinov', 'аллергия'), ', meaning that she will react badly to chocolate.']),
    (3, None, ["'Uncle Lyova, let us play!' The young girl eagerly demands to start ", ('alisa', 'играть'), ', completely ignoring the strict orders just given to her babysitter.']),
    (4, None, ["'Maybe we could just sit here instead?' Hoping for a quieter afternoon, the tall man suggests ", ('lyova', 'посидим'), ' instead of engaging in an active game.']),
    (5, None, ["'I will tell Dad, he will fire you!' She immediately resorts to a harsh threat, using ", ('alisa', 'уволит'), ' to remind him who has the power to fire him.']),
    (6, None, ["'All right, what should we play?' Giving in to the threat, he sighs and says ", ('lyova', 'Хорошо'), ', accepting his fate as a playmate.']),
    (7, None, ["'Let us play hide and seek!' Her game of choice is the classic ", ('alisa', 'прятки'), ', where one person runs away and the other has to find them.']),
    (8, None, ["'And who will hide?' He asks a very logical question starting with ", ('lyova', 'кто'), ' to figure out the exact roles for their upcoming activity.']),
    (9, None, ["'Of course, I will hide!' She claims the fun role without hesitation, leading with ", ('alisa', 'Конечно'), ' as if it was incredibly obvious.']),
    (10, None, ["'You are so tall, you cannot be hidden anywhere.' To justify her choice, she calls him ", ('alisa', 'длинного'), ', pointing out that a man of his size could never conceal himself.']),
    (11, None, ["'Close your eyes, count to a hundred.' She then issues the starting command with ", ('alisa', 'Закрывай'), ', making sure he covers his vision before counting to a hundred.']),
    (12, None, ["'One, two, three, four...' He obediently begins the long process, reaching ", ('lyova', 'четыре'), ' before the sneaky child interrupts him with one final instruction.']),
    (13, None, ["'Count slowly, I am going to hide!' Wanting more time to find a spot, she demands he count ", ('alisa', 'медленно'), ' while she runs away to hide.']),
]
