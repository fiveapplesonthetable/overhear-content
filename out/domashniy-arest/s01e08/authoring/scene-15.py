# Authoring module for domashniy-arest-s01e08-scene-15.
ID = 'domashniy-arest-s01e08-scene-15'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 15
TITLE = 'Вставай, страна огромная  (Waking Ivan)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'neighbor': 'Сосед', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "The next morning, neighbours find Samsonov fast asleep on a snow-covered bench after his drinking binge and try to wake him up. Let's listen in Russian first."
OPENER = "Let's walk through the dialogue. A passerby tries to revive Samsonov from his freezing stupor."
TRANSITION = "Now let's listen to the short scene again at full speed."
OUTRO = 'Samsonov drags himself off the snowy bench with a massive hangover, still clinging to thoughts of toy tanks and family honour. See you next time!'
CLOSING = ('samson', 'Пока!')
STORY = [
    ('neighbor', 'Эй, Ваня, вставай, вставай!', 'Hey, Vanya, get up, get up!', [(220, 'Вставай, вставай')], ''),
    ('neighbor', 'Давай, вставай, замёрзнешь на снегу!', "Come on, get up, you'll freeze in the snow!", [(221, 'Давай, вставай')], ''),
    ('samson', 'Вставай, страна огромная...', 'Arise, vast country...', [(222, 'Страна огромная')], 'patriotic song quote'),
    ('neighbor', 'Какая страна? Вставай на ноги!', 'What country? Get on your feet!', [(223, 'Страна огромная')], ''),
    ('samson', 'Страна огромная...', 'A vast country...', [(223, 'Страна огромная')], ''),
    ('neighbor', 'Ты всю ночь тут проспал!', 'You slept here all night!', [(221, 'Давай, вставай')], "neighbour's scolding"),
    ('samson', 'Где я? Который час?', 'Where am I? What time is it?', [(220, 'вставай')], ''),
    ('neighbor', 'Уже утро, люди идут мимо.', "It's already morning, people are walking past.", [(221, 'вставай')], ''),
    ('samson', 'Лёха! Где мой друг Лёха?', 'Lyokha! Where is my friend Lyokha?', [(224, 'Леха')], ''),
    ('neighbor', 'Дома спит твой друг.', 'Your friend is sleeping at home.', [(224, 'Леха')], ''),
    ('samson', 'Слышишь, танк нужен тебе?', 'Listen, do you need a tank?', [(225, 'Слышь, танк нужен')], ''),
    ('samson', 'Иди и забирай его!', 'Go and take it!', [(225, 'Иди забирай')], ''),
]
WALK = [
    (0, None, "'Hey, Vanya, get up, get up!' A passing neighbor shakes Ivan by the shoulder to rouse him from the snowy bench."),
    (1, None, "'Come on, get up, you'll freeze in the snow!' Sleeping outdoors in a Russian winter is a quick way to freeze to death."),
    (2, None, "'Arise, vast country...' Ivan groggily mutters the opening line of the famous World War II anthem 'The Sacred War'."),
    (3, None, "'What country? Get on your feet!' The neighbour urges him to stand up before someone calls the police."),
    (4, None, "'A vast country...' Ivan repeats the lyrics like a broken record in his half-conscious state."),
    (5, None, "'You slept here all night!' The neighbor cannot believe Ivan spent the entire freezing night out on that bench."),
    (6, None, "'Where am I? What time is it?' Ivan slowly opens his bloodshot eyes and looks around the courtyard."),
    (7, None, "'It's already morning, people are walking past.' The neighbour points out neighbours heading to work."),
    (8, None, "'Lyokha! Where is my friend Lyokha?' Ivan remembers someone he promised something to."),
    (9, None, "'Your friend is sleeping at home.' The neighbour tells him that everyone else is warm inside."),
    (10, None, "'Listen, do you need a tank?' Ivan confusingly offers away the toy tank he obtained."),
    (11, None, "'Go and take it!' Ivan waves his heavy hand in the air and struggles to sit up on the bench."),
]
