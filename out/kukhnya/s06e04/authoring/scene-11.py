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
    ('barinov', 'Оливье, познакомься, это моя мама Элеонора.', 'Olivier, meet my mom Eleonora.', [(180, 'Оливье, познакомься, это моя мама Элеонора')], 'exact'),
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
    (0, None, "'Hands off, is everything in order?' Focusing on the order during the talk, Barinov keeps normal statement word order here, turning the line into a question for Eleonora purely through rising pitch."),
    (1, None, "'Watch, my mom is about to notice us as if by chance.' Eleonora continues bluntly toward Barinov, shifting the mood of the conversation in a single beat."),
    (2, None, '\'Olivier, meet my mom Eleonora.\' Underscoring the mum right here, Barinov reaches for the Russian word "poznakomsya" ("to get acquainted", built from "poznakomitsya") right at the center of the line.'),
    (3, None, '\'Very pleased to meet you.\' Reacting calmly beside Barinov, the "-sya" ending on "poznakomitsya" ("to meet") marks an action that unfolds mutually or turns back on the speaker.'),
    (4, None, "'And I am very pleased too, join us.' Eleonora speaks candidly hearing the guest, letting the remark speak for itself."),
    (5, None, '\'By the way, thank you for moving me to the luxury suite.\' Turning to the thank with Eleonora, the guest reaches for the Russian word "spasibo" ("thank you") right at the heart of the line.'),
    (6, None, '\'The suite is simply magnificent.\' Highlighting how magnificent things are around Eleonora, the guest uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (7, None, "'Do you treat all guests like this?' The guest tests straight out before Eleonora can change the subject."),
    (8, None, '\'All our guests receive only the very best.\' Discussing the visitors at once, Eleonora lands on "luchsheye" ("best", built on "luchshiy") to keep the statement grounded.'),
    (9, None, '\'Good afternoon, I am the head chef of this restaurant.\' Mentioning the head beside Eleonora, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (10, None, "'Here is your fillet of wild pigeon in sauce.' Barinov follows up sharply hearing the guest, grounding the moment in plain reality."),
    (11, None, '\'Thank you very much, Viktor.\' The guest plainly speaks this word of thanks toward Barinov using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
]
