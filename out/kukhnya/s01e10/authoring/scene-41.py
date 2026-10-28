# Authoring module for kukhnya-s01e10-scene-41.
ID = 'kukhnya-s01e10-scene-41'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 41
TITLE = 'Подозрительная икра  (Suspicious Caviar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = 'In the lavish dining hall of Claude Monet, restaurant owner Dmitry Nagiyev summons Chef Viktor Barinov to his table. Eyeing a plate of strangely colored black caviar intended for wealthy guests, Nagiyev demands an immediate and honest explanation.'
OPENER = "Let's watch Nagiyev confront Chef Barinov over suspicious caviar served in the main dining hall."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Cornered by his sharp-eyed boss in front of empty tables, Barinov realizes his culinary deception cannot last. Next time you watch the episode, listen for the Russian expressions for 'to lie' and 'to speak' — you will catch every word right away. See you next time!"
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('nagiyev', 'Витя, иди скорее сюда к столу!', 'Vitya, come quickly here to the table!', [], ''),
    ('barinov', 'Что случилось, Дмитрий Владимирович, в чём дело?', 'What happened, Dmitry Vladimirovich, what is the matter?', [], ''),
    ('nagiyev', 'Витя, скажи мне прямо, это чего?', 'Vitya, tell me straight, what is this?', [(293, 'Вить, это чего?')], ''),
    ('barinov', 'Чего? Вот это на тарелке чего?', 'What? What is this on the plate?', [(294, 'Чего? Вот это чего?')], ''),
    ('barinov', 'Это самая настоящая свежая русская икра.', 'This is real fresh Russian caviar.', [(295, 'Икра.')], ''),
    ('barinov', 'Причём очень дорогая и очень хорошая икра!', 'And very expensive and very good caviar!', [(296, 'Причем очень хорошая.')], ''),
    ('nagiyev', 'Витя, ты совсем дурак или притворяешься?', 'Vitya, are you a complete fool or pretending?', [(297, 'Вить, ты дурак?')], ''),
    ('barinov', 'В каком смысле дурак, не понимаю вас!', 'In what sense a fool, I do not understand you!', [(297, 'В смысле?')], ''),
    ('nagiyev', 'Вот это чего, я тебя строго спрашиваю?!', 'What is this, I am strictly asking you?!', [(298, 'Вот это чего я тебя спрашиваю?')], ''),
    ('barinov', 'Гости просили чёрную икру к праздничному столу.', 'The guests asked for black caviar for the holiday table.', [], ''),
    ('nagiyev', 'Но цвет у этой икры странный и подозрительный.', 'But the color of this caviar is strange and suspicious.', [], ''),
    ('barinov', 'Особый свет в зале меняет все оттенки.', 'Special lighting in the hall changes all shades.', [], ''),
    ('nagiyev', 'Не ври мне, говори сейчас всю правду!', 'Do not lie to me, tell the whole truth now!', [], ''),
]
WALK = [
    (0, None, "'Vitya, come quickly here to the table!' Nagiyev calls the head chef into the dining room."),
    (1, None, "'What happened, Dmitry Vladimirovich, what is the matter?' Approaching Nagiyev's table, Barinov asks what the urgent matter is."),
    (2, None, "'Vitya, tell me straight, what is this?' Pointing down at the bowl on the table, Nagiyev demands to know what he is looking at."),
    (3, None, "'What? What is this on the plate?' Pointing straight at the suspiciously dark appetizer, Barinov demands to know what is sitting on the plate."),
    (4, None, "'This is real fresh Russian caviar.' Putting on a confident front, Viktor declares it is genuine fresh Russian caviar."),
    (5, None, "'And very expensive and very good caviar!' He piles on the praise, calling it top-shelf luxury roe."),
    (6, None, "'Vitya, are you a complete fool or pretending?' Having seen the black food dye bleeding onto the plate, Nagiyev asks if Viktor thinks he is a complete fool."),
    (7, None, "'In what sense a fool, I do not understand you!' Viktor plays innocent and claims he has no idea what Dmitry means."),
    (8, None, "'What is this, I am strictly asking you?!' Nagiyev taps the stained plate and demands an honest answer right now."),
    (9, None, "'The guests asked for black caviar for the holiday table.' Viktor reminds him that the VIP guests ordered black caviar for their celebration."),
    (10, None, "'But the color of this caviar is strange and suspicious.' Nagiyev points out that the 'black' caviar is leaking a very suspicious dark ring."),
    (11, None, "'Special lighting in the hall changes all shades.' Thinking fast, Viktor blames the restaurant's lighting for playing tricks on the color."),
    (12, None, "'Do not lie to me, tell the whole truth now!' Nagiyev cuts him off and orders him to stop lying and confess the truth."),
]
