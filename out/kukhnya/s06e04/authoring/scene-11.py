# Authoring module for kukhnya-s06e04-scene-11.
ID = 'kukhnya-s06e04-scene-11'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 11
TITLE = 'Знакомство с Элеонорой и подача блюда  (Meeting Eleonora and Serving the Dish)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'In the dining room, Katya introduces Olivier to her mother Eleonora, who showers him with compliments before Chef Barinov arrives at the table to present his wild pigeon dish.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Barinov hovers beside the table, holding his breath as the Frenchman takes his first bite of the pigeon. Until next time!'
CLOSING = ('barinov', 'До свидания!')
STORY = [
    ('barinov', 'Руки убрал, все в порядке?', 'Hands off, is everything in order?', [(177, 'Руки убрал?'), (178, 'Все в порядке?')], 'adapted'),
    ('eleonora', 'Смотри, моя мама сейчас как бы случайно нас заметит.', 'Watch, my mom is about to notice us as if by chance.', [(179, 'Смотри, моя мама сейчас как бы случайно нас заметит')], 'exact'),
    ('eleonora', 'Оливье, познакомься, это моя мама Элеонора.', 'Olivier, meet my mom Eleonora.', [(180, 'Оливье, познакомься, это моя мама Элеонора')], 'exact'),
    ('guest', 'Очень приятно познакомиться.', 'Very pleased to meet you.', [(181, 'Приятно познакомиться')], 'adapted'),
    ('eleonora', 'И мне очень приятно, присоединяйтесь к нам.', 'And I am very pleased too, join us.', [(182, 'И мне очень приятно'), (183, 'Присоединяйтесь к нам')], 'adapted'),
    ('guest', 'Кстати, спасибо, что переселили меня в люкс.', 'By the way, thank you for moving me to the luxury suite.', [(184, 'Кстати, спасибо, что переселили меня в люкс')], 'exact'),
    ('guest', 'Номер просто великолепный.', 'The suite is simply magnificent.', [(185, 'Номер великолепный')], 'adapted'),
    ('guest', 'Вы ко всем гостям так относитесь?', 'Do you treat all guests like this?', [(186, 'так относитесь?')], 'adapted'),
    ('eleonora', 'Все наши гости получают только самое лучшее.', 'All our guests receive only the very best.', [(187, 'Все наши гости получают только самое лучшее')], 'exact'),
    ('barinov', 'Добрый день, я шеф-повар этого ресторана.', 'Good afternoon, I am the head chef of this restaurant.', [(188, 'Добрый день'), (189, 'Я шеф-повар этого ресторана')], 'adapted'),
    ('barinov', 'Вот ваше филе дикого голубя в соусе.', 'Here is your fillet of wild pigeon in sauce.', [(190, 'Ваше филе дикого голубя в')], 'adapted'),
    ('guest', 'Большое спасибо, Виктор.', 'Thank you very much, Viktor.', [(184, 'Спасибо')], 'adapted'),
]
WALK = [
    (0, None, '\'Hands off, is everything in order?\' Questioning whether hands off is everything in order is how Barinov tests Eleonora\'s story. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'Watch, my mom is about to notice us as if by chance.' Here watching her is about to notice them as if by chance sets up the next turn in their exchange."),
    (2, None, "'Olivier, meet my mom Eleonora.' With the dish and sauce in play, Eleonora keeps this short reply brisk and direct."),
    (3, None, "'Very pleased to meet you.' Over the dish and the sauce, the guest answers Barinov without a second thought."),
    (4, None, "'And I am very pleased too, join us.' Saying that she is very pleased too join them is how Eleonora sets the tone with Barinov."),
    (5, None, "'By the way, thank you for moving me to the luxury suite.' Around the dish and sauce, the guest sets a calm, everyday tone with Barinov."),
    (6, None, "'The suite is simply magnificent.' The guest mentions that the suite is simply magnificent so Barinov sees what is at stake."),
    (7, None, '\'Do you treat all guests like this?\' Asking whether Barinov treats all guests like this is how the guest puts Barinov on the spot. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (8, None, "'All our guests receive only the very best.' With the dish and table in play, Eleonora keeps this short reply brisk and direct."),
    (9, None, "'Good afternoon, I am the head chef of this restaurant.' Barinov explains that he is the head of this restaurant, keeping his voice calm and direct."),
    (10, None, '\'Here is your fillet of wild pigeon in sauce.\' Realizing that here is Eleonora\'s fillet of wild pigeon in sauce changes how Barinov handles the situation. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (11, None, "'Thank you very much, Viktor.' Around the dish and conversation, the guest sets a calm, everyday tone with Barinov."),
]
