# Authoring module for dvorik-u-mosta-s01e04-scene-02.
ID = 'dvorik-u-mosta-s01e04-scene-02'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'Синяя дверь  (The Blue Door)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'matvey': 'Матвей'}
INTRO = 'Ten minutes later, Kira has crossed the bridge in St Petersburg, yet two narrow streets branch off behind the pharmacy. She phones Matvey from beside a stone fountain. Listen first.'
OPENER = "Now let's follow Kira's phone call from the square line by line."
TRANSITION = "Let's hear the whole conversation again from beginning to end."
OUTRO = 'Two new brass valves in her pocket and early risers already stirring upstairs. Next time, Zoya and Yaroslav try to keep everyone busy at breakfast.'
CLOSING = ('matvey', 'До скорого!')
STORY = [
    ('kira', 'Матвей, ты меня слышишь? Я только что прошла зелёную аптеку!', 'Matvey, can you hear me? I just passed the green pharmacy!'),
    ('matvey', 'Слышу отлично. Ты стоишь у маленького каменного фонтана?', 'I hear you loud and clear. Are you standing by the small stone fountain?'),
    ('kira', 'Да! Слева две узкие улицы — по какой мне идти?', 'Yes! On the left are two narrow streets — which one should I walk down?'),
    ('matvey', 'Иди по второй улице у цветочного киоска, а не по тёмному переулку.', 'Walk down the second street by the flower stall, not down the dark lane.'),
    ('kira', 'Иду... о, я вижу золотой ключ и синюю дверь!', 'Walking... oh, I see the golden key and the blue door!'),
    ('matvey', 'Отлично! Лавка уже открыта?', 'Great! Is the shop open already?'),
    ('kira', 'Мастер открывает замок прямо сейчас! Подожди секунду на линии.', 'The craftsman is unlocking it right now! Wait one second on the line.'),
    ('matvey', 'Проверь кольцо внутри — ровно двадцать миллиметров.', 'Check the ring inside — twenty millimetres sharp.'),
    ('kira', 'Он приложил его к старому — на полке осталось две штуки!', 'He held it against the old one — two pieces are left on the shelf!'),
    ('matvey', 'Бери оба! Запасной вентиль спасёт нас следующей зимой.', 'Take both! A spare valve will save us next winter.'),
    ('kira', 'Заплатила наличными! Открывай ящик с инструментами, я бегу назад через мост!', 'Paid in cash! Open your toolbox, I am running back across the bridge!'),
    ('matvey', 'Скорее — я слышу шаги на лестнице второго этажа!', 'Hurry — I hear footsteps on the second-floor stairs!'),
]
WALK = [
    (0, None, ["'Matvey, can you hear me? I just passed the green pharmacy!' Every phone check starts naturally with ", (None, 'ты меня слышишь?'), " — 'do you hear me?'."]),
    (1, None, ["'I hear you loud and clear. Are you standing by the small stone fountain?' Russian drops 'loud and clear' for crisp ", (None, 'Слышу отлично.'), " — 'I hear excellently'."]),
    (2, None, ["'Yes! On the left are two narrow streets — which one should I walk down?' Walking 'along' a street uses ", (None, 'по какой'), " — 'along which one?'."]),
    (3, None, ["'Walk down the second street by the flower stall, not down the dark lane.' Again ", (None, 'а не'), ' cleanly steers Kira toward the right street and away from the wrong alley.']),
    (4, None, ["'Walking... oh, I see the golden key and the blue door!' One present action word, ", (None, 'Иду...'), " reports 'I am walking right now'."]),
    (5, None, "'Great! Is the shop open already?' Notice how 'open' here echoes the very first morning scene at the front door."),
    (6, None, ["'The craftsman is unlocking it right now! Wait one second on the line.' Staying connected on a phone call is ", (None, 'на линии.'), " — 'on the line'."]),
    (7, None, ["'Check the ring inside — twenty millimetres sharp.' Inside a pipe fitting sits ", (None, 'кольцо'), ' — the same everyday word as a finger ring.']),
    (8, None, ["'He held it against the old one — two pieces are left on the shelf!' Counting individual items on a shelf uses ", (None, 'две штуки!'), " — 'two pieces, two units'."]),
    (9, None, ["'Take both! A spare valve will save us next winter.' Masculine 'both' has its own compact word, ", (None, 'оба!'), ' distinct from the feminine version.']),
    (10, None, ["'Paid in cash! Open your toolbox, I am running back across the bridge!' Paying with bills and coins compresses into ", (None, 'наличными!'), " — 'by cash'."]),
    (11, None, ["'Hurry — I hear footsteps on the second-floor stairs!' One urgent word, ", (None, 'Скорее'), " means 'faster, hurry up!'."]),
]
