ID = 'kukhnya-s06e04-scene-11'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 11
TITLE = "Знакомство с Элеонорой и подача блюда  (Meeting Eleonora and Serving the Dish)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "guest": "anja", "eleonora": "angelina"}
LABELS = {"guest": "Гость", "eleonora": "Элеонора"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'

INTRO = 'In the dining room, Katya introduces Olivier to her mother Eleonora, who showers him with compliments before Chef Barinov arrives at the table to present his wild pigeon dish.'

STORY = [
    ('guest', 'Руки убрал, все в порядке?', 'Hands off, is everything in order?', [(177, 'Руки убрал?'), (178, 'Все в порядке?')], 'adapted'),
    ('eleonora', 'Смотри, моя мама сейчас как бы случайно нас заметит.', 'Watch, my mom is about to notice us as if by chance.', [(179, 'Смотри, моя мама сейчас как бы случайно нас заметит')], 'exact'),
    ('eleonora', 'Оливье, познакомься, это моя мама Элеонора.', 'Olivier, meet my mom Eleonora.', [(180, 'Оливье, познакомься, это моя мама Элеонора')], 'exact'),
    ('guest', 'Очень приятно познакомиться.', 'Very pleased to meet you.', [(181, 'Приятно познакомиться')], 'adapted'),
    ('eleonora', 'И мне очень приятно, присоединяйтесь к нам.', 'And I am very pleased too, join us.', [(182, 'И мне очень приятно'), (183, 'Присоединяйтесь к нам')], 'adapted'),
    ('guest', 'Кстати, спасибо, что переселили меня в люкс.', 'By the way, thank you for moving me to the luxury suite.', [(184, 'Кстати, спасибо, что переселили меня в люкс')], 'exact'),
    ('guest', 'Номер просто великолепный.', 'The suite is simply magnificent.', [(185, 'Номер великолепный')], 'adapted'),
    ('guest', 'Вы ко всем гостям так относитесь?', 'Do you treat all guests like this?', [(186, 'так относитесь?')], 'adapted'),
    ('eleonora', 'Все наши гости получают только самое лучшее.', 'All our guests receive only the very best.', [(187, 'Все наши гости получают только самое лучшее')], 'exact'),
    ('guest', 'Добрый день, я шеф-повар этого ресторана.', 'Good afternoon, I am the head chef of this restaurant.', [(188, 'Добрый день'), (189, 'Я шеф-повар этого ресторана')], 'adapted'),
    ('guest', 'Вот ваше филе дикого голубя в соусе.', 'Here is your fillet of wild pigeon in sauce.', [(190, 'Ваше филе дикого голубя в')], 'adapted'),
    ('guest', 'Большое спасибо, Виктор.', 'Thank you very much, Viktor.', [(184, 'Спасибо')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Hands off, is everything in order?' Spoken Russian keeps this brisk, leaning on 'hands' and finishing on 'order'."),
    (1, None, "'Watch, my mom is about to notice us as if by chance.' In Russian, the idea of 'watch' flows naturally into 'notices' without extra filler words."),
    (2, None, "'Olivier, meet my mom Eleonora.' Here the Russian phrasing highlights 'Olivier' before landing on 'Eleonora'."),
    (3, None, "'Very pleased to meet you.' The meaning hinges on 'very' working together with 'to get acquainted' in spoken Russian."),
    (4, None, "'And I am very pleased too, join us.' In everyday Russian, 'very' flows straight into 'join' without extra linking words."),
    (5, None, "'By the way, thank you for moving me to the luxury suite.' the guest brings out the contrast between 'by the way' and 'thank you' in a few short words."),
    (6, None, "'The suite is simply magnificent.' the guest anchors the line on 'number', while 'magnificent' completes the thought."),
    (7, None, "'Do you treat all guests like this?' the guest raises the pitch on 'treat' to turn the phrase into a direct spoken question. Eleonora answers right away."),
    (8, None, "'All our guests receive only the very best.' The meaning hinges on 'all' working together with 'the best' in spoken Russian."),
    (9, None, "'Good afternoon, I am the head chef of this restaurant.' In Russian, the idea of 'good' flows naturally into 'restaurant' without extra filler words."),
    (10, None, "'Here is your fillet of wild pigeon in sauce.' Notice how Russian expresses 'here' and 'sauce' with crisp inflection rather than helper words. the guest answers right away."),
    (11, None, "'Thank you very much, Viktor.' Notice how Russian expresses 'very much' and 'thank you' with crisp inflection rather than helper words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Barinov hovers beside the table, holding his breath as the Frenchman takes his first bite of the pigeon. Until next time!'
CLOSING = ("guest", "До свидания!")
