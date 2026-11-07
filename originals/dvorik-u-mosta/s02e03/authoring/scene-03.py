# Authoring module for dvorik-u-mosta-s02e03-scene-03.
ID = 'dvorik-u-mosta-s02e03-scene-03'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 3
SCENE = 3
TITLE = 'Внутри пианино  (Inside the Piano Action)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'matvey': 'Матвей', 'larisa': 'Лариса', 'roman': 'Роман'}
INTRO = 'In room nine, Matvey kneels beside his tool kit and carefully lifts off the front wooden panel of the upright piano while Larisa and Roman watch the row of felt hammers inside. Listen first.'
OPENER = "Let's look inside the piano again, one line at a time."
TRANSITION = 'Now listen to the whole repair conversation again from beginning to end.'
OUTRO = "No cracked wood, just one slipped brass pin waiting for Matvey's steady hands. Let's see what else is in the chest next time."
CLOSING = ('matvey', 'Пока!')
STORY = [
    ('matvey', 'Я чинил котлы, замки и часы, Лариса Борисовна, но пианино никогда.', 'I have fixed boilers, locks, and clocks, Larisa Borisovna, but never a piano.'),
    ('larisa', 'Пианино — это просто честное дерево, войлок и стальная проволока, Матвей.', 'A piano is just honest wood, felt, and steel wire, Matvey.'),
    ('roman', 'Сначала нажмите соседнюю клавишу слева, чтобы увидеть здоровый молоточек.', 'First press the next key on the left, so we see a healthy hammer.'),
    ('larisa', 'Смотрите: молоточек легко поднимается и бьёт по трём струнам.', 'Look: the hammer rises easily and strikes the three strings.'),
    ('matvey', 'А теперь нажмём молчащую клавишу рядом.', "And now let's press the silent key next to it."),
    ('larisa', 'Смотрите: клавиша идёт вниз, а молоточек стоит криво!', 'Look: the key goes down, but the hammer stands crooked!'),
    ('roman', 'Ближе лампу! Маленький латунный гвоздик наполовину вылез из дерева!', 'Bring the lamp closer! A tiny brass pin has come halfway out of the wood!'),
    ('matvey', 'Подождите... ничего не треснуло! Сырой воздух просто ослабил войлок.', 'Wait... nothing is cracked! The damp air simply loosened the felt.'),
    ('larisa', 'Вы сможете поставить такой маленький гвоздик и не сломать дерево?', 'Can you set such a tiny pin without breaking the wood?'),
    ('matvey', 'Завтра утром дайте мне тишину, хороший свет, тонкий пинцет и клей.', 'Tomorrow morning give me quiet, good light, thin tweezers, and glue.'),
    ('roman', 'Когда молоточек будет стоять ровно, Лариса Борисовна настроит всю середину?', 'Once the hammer stands straight, will Larisa Borisovna tune the whole middle?'),
    ('larisa', 'Матвей, у вас есть ключ для настройки в кедровом ящике? Посмотрите внизу!', 'Matvey, is there a tuning key in the cedar chest? Look at the bottom!'),
]
WALK = [
    (0, None, ["'I have fixed boilers, locks, and clocks, Larisa Borisovna, but never a piano.' One word, ", (None, 'часы,'), " does triple duty: clocks, a wristwatch, and hours."]),
    (1, None, ["'A piano is just honest wood, felt, and steel wire, Matvey.' In writing, a dash stands in for 'is', and ", (None, 'это'), " after it works like 'that is': ", (None, 'Пианино — это'), " means 'a piano is'."]),
    (2, None, ["'First press the next key on the left, so we see a healthy hammer.' Russian loves cute endings: ", (None, 'молоточек'), " is a little hammer, the small cousin of an ordinary one."]),
    (3, None, ["'Look: the hammer rises easily and strikes the three strings.' Hitting a surface takes 'along' in Russian, so ", (None, 'бьёт по трём струнам.'), " is literally 'beats along three strings'."]),
    (4, None, ["'And now let's press the silent key next to it.' Matvey's ", (None, 'нажмём'), " is just 'we will press', but said like this it becomes an invitation: 'let's press'."]),
    (5, None, ["'Look: the key goes down, but the hammer stands crooked!' Russian hammers 'stand' rather than sit or lean, and ", (None, 'стоит криво!'), " means 'stands crooked', off to one side."]),
    (6, None, ["'Bring the lamp closer! A tiny brass pin has come halfway out of the wood!' Inside ", (None, 'наполовину'), " hides the word for half, so it means 'by half', or 'halfway'."]),
    (7, None, ["'Wait... nothing is cracked! The damp air simply loosened the felt.' A useful double meaning: ", (None, 'Сырой воздух'), " is damp air, but the same adjective on food means 'raw'."]),
    (8, None, ["'Can you set such a tiny pin without breaking the wood?' Where English says 'without breaking', Larisa says ", (None, 'и не сломать'), ", 'and not break'."]),
    (9, None, ["'Tomorrow morning give me quiet, good light, thin tweezers, and glue.' English tweezers are always plural, but Russian has just one: ", (None, 'тонкий пинцет'), " is a single thin tool."]),
    (10, None, ["'Once the hammer stands straight, will Larisa Borisovna tune the whole middle?' Roman's ", (None, 'настроит'), " means 'will tune', and it shares a root with the word for mood, so tuning sets the mood."]),
    (11, None, ["'Matvey, is there a tuning key in the cedar chest? Look at the bottom!' A door key and a tuning key share one word, ", (None, 'ключ'), ", while the key you press on a piano gets a different word entirely."]),
]
