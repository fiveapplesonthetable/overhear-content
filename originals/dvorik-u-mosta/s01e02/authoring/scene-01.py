# Authoring module for dvorik-u-mosta-s01e02-scene-01.
ID = 'dvorik-u-mosta-s01e02-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = 'Красная лента  (The Red Ribbon)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'larisa': 'Лариса', 'matvey': 'Матвей'}
INTRO = 'Tuesday morning dawns bright and clear at the Bridge Courtyard Inn. Larisa Borisovna hurries downstairs to the front desk, where Kira and Matvey have her returned suitcase waiting. Listen to the Russian scene first.'
OPENER = "Let's step through their Tuesday morning conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Larisa has her teacup and clothes back, and a twenty-five-year-old memory is starting to stir. Next, trouble brews in the breakfast kitchen. See you next time.'
CLOSING = ('larisa', 'До встречи!')
STORY = [
    ('kira', 'Доброе утро, Лариса Борисовна! Посмотрите, что принесли вчера вечером к воротам.', 'Good morning, Larisa Borisovna! Look what someone brought to the gate last night.'),
    ('larisa', 'Мой чемодан! Сейчас открою верхний карман... да, моя красная лента!', 'My suitcase! Let me open the top pocket... yes, my red ribbon!'),
    ('matvey', 'А ваша чашка внутри? Она целая?', 'And your teacup inside? Is it whole?'),
    ('larisa', 'Ни одной трещины! А кто принёс чемодан обратно?', 'Not a single crack! And who brought the suitcase back?'),
    ('kira', 'Мы не знаем. Кто-то оставил его на ступеньке и позвонил.', 'We do not know. Someone left it on the step and rang.'),
    ('larisa', 'И он не попросил свой чемодан с деревянным поездом?', 'And he did not ask for his own suitcase with the wooden train?'),
    ('matvey', 'Он оставил короткую записку и попросил беречь его до пятницы.', 'He left a short note and asked us to guard it until Friday.'),
    ('larisa', 'Как интересно! Почерк на той бирке показался мне очень знакомым.', 'How interesting! The handwriting on that tag seemed very familiar to me.'),
    ('kira', 'Правда? Вы знаете кого-то в Петербурге?', 'Really? Do you know someone in St Petersburg?'),
    ('larisa', 'Двадцать пять лет назад я учила здесь детей играть на пианино.', 'Twenty-five years ago I taught children to play the piano near here.'),
    ('matvey', 'Пока его сумка лежит в кладовке под замком.', 'For now, his bag is sitting in the closet under lock and key.'),
    ('larisa', 'Чудесно! А теперь я готова к большому завтраку.', 'Wonderful! And now I am ready for a big breakfast.'),
]
WALK = [
    (0, None, ["'Good morning, Larisa Borisovna! Look what someone brought to the gate last night.' Plural ", (None, 'принесли'), " without 'they' is how Russian says 'somebody brought it'."]),
    (1, None, ["'My suitcase! Let me open the top pocket... yes, my red ribbon!' Putting ", (None, 'Сейчас открою'), " together literally says 'now I will open', the natural way to say 'let me open it right now'."]),
    (2, None, ["'And your teacup inside? Is it whole?' Instead of 'in one piece', Russian asks ", (None, 'целая?'), " — 'whole, unbroken?'."]),
    (3, None, ["'Not a single crack! And who brought the suitcase back?' Notice ", (None, 'обратно?'), " at the end, adding the clear sense of 'back again'."]),
    (4, None, ["'We do not know. Someone left it on the step and rang.' Simple and essential, ", (None, 'Мы не знаем.'), " gives you 'we do not know' for any mystery."]),
    (5, None, ["'And he did not ask for his own suitcase with the wooden train?' Russian has a special reflexive word ", (None, 'свой'), " meaning 'his own', pointing right back to the stranger himself."]),
    (6, None, ["'He left a short note and asked us to guard it until Friday.' A brief handwritten message on paper is ", (None, 'записку'), ' — built from the root for writing down.']),
    (7, None, ["'How interesting! The handwriting on that tag seemed very familiar to me.' Handwriting is ", (None, 'Почерк'), ' — linked to drawing neat strokes and lines on paper.']),
    (8, None, ["'Really? Do you know someone in St Petersburg?' Notice how ", (None, 'кого-то'), " turns 'whom' into 'somebody specific' in a polite question."]),
    (9, None, ["'Twenty-five years ago I taught children to play the piano near here.' Placing ", (None, 'назад'), " after a span of years literally says 'twenty-five years back' for 'ago'."]),
    (10, None, ["'For now, his bag is sitting in the closet under lock and key.' English says 'under lock and key', while Russian keeps it tight as ", (None, 'под замком.'), " — 'under a lock'."]),
    (11, None, ["'Wonderful! And now I am ready for a big breakfast.' Because Larisa is speaking, 'ready' takes its feminine short form ", (None, 'готова'), ' rather than the masculine shape.']),
]
