# Authoring module for kukhnya-s01e07-scene-08.
ID = 'kukhnya-s01e07-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 8
TITLE = 'Совет от Макса  (Advice from Max)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "In the dining room between shifts, Max asks waitress Nastya if she knows of any cheap rooms for rent in Moscow. To his horror, she reveals that Kostya just invited her to move into their shared flat. Desperate to protect his living space, Max cleverly persuades Nastya that living with Kostya would be a noisy nightmare. Let's listen to their conversation in Russian first."
OPENER = "Let's review this sneaky and hilarious conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Relieved that his bachelor apartment is safe, Max smiles as Nastya decides to find alternative lodging. See you next time!'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('max', 'Настя, ты знаешь, где сдать квартиру?', 'Nastya, do you know where to rent a flat?', [(86, 'Настя, тебя никто знакомый квартиру не сдает')], ''),
    ('nastya', 'Сама искала жильё сегодня утром.', 'I was looking for a place myself this morning.', [(88, 'Сама только утром искала')], ''),
    ('max', 'И тебе удалось найти комнату?', 'And did you manage to find a room?', [], ''),
    ('nastya', 'Мне помог Костик, я переезжаю к нему.', 'Kostik helped me, I am moving to his place.', [(89, 'Ну, предложил у него пожить')], ''),
    ('max', 'Погоди, Костя позвал тебя жить вместе?', 'Wait, Kostya invited you to live together?', [(91, 'Погоди. То есть, Костя тебя позвал, да')], ''),
    ('nastya', 'Да, мы ведь с ним встречаемся.', 'Yes, after all he and I are dating.', [(90, 'Мы вообще встречаемся')], ''),
    ('max', 'Честно говоря, я тебе совсем не завидую.', 'To be honest, I do not envy you at all.', [(93, 'Хотя, не завидую я тебе')], ''),
    ('nastya', 'Почему? Костя такой милый парень.', 'Why? Kostya is such a sweet guy.', [], ''),
    ('max', 'Он ночью страшно и громко храпит!', 'At night he snores terribly and loudly!', [(94, 'просто он храпит по-конски')], ''),
    ('nastya', 'Ой, я совсем не выношу храп!', 'Oh, I cannot stand snoring at all!', [(104, 'Все-таки не люблю, когда храпят')], ''),
    ('max', 'Подумай хорошо, прежде чем соглашаться.', 'Think well before agreeing.', [(103, 'Знаешь, наверное, не буду у Кости жить')], ''),
    ('nastya', 'Ты прав, поищу другой вариант.', 'You are right, I will look for another option.', [(107, 'Спасибо, Макс')], ''),
]
WALK = [
    (0, None, "'Nastya, do you know where to rent a flat?' Max casually asks if she has any apartment leads."),
    (1, None, "'I was looking for a place myself this morning.' Nastya explains that she was recently displaced herself."),
    (2, None, "'And did you manage to find a room?' Max asks whether she had any luck on the rental market."),
    (3, None, "'Kostik helped me, I am moving to his place.' Nastya uses the action verb meaning 'helped' to focus on the single completed result, pairing it with 'am moving'."),
    (4, None, "'Wait, Kostya invited you to live together?' Max freezes upon realizing his flatmate offered up their shared apartment."),
    (5, None, "'Yes, after all he and I are dating.' Nastya treats moving in together as the natural next step."),
    (6, None, "'To be honest, I do not envy you at all.' The phrasing opens with 'honestly' before bringing in 'speaking' and 'at all' to make the point clear."),
    (7, None, "'Why? Kostya is such a sweet guy.' Russian omits the present-tense verb 'to be' here, linking 'why' directly with 'sweet', combining 'why' with 'sweet' and 'guy'."),
    (8, None, "'At night he snores terribly and loudly!' Max fabricates a severe sleep disruption to scare her off."),
    (9, None, "'Oh, I cannot stand snoring at all!' Nastya admits that nighttime noise is her biggest pet peeve."),
    (10, None, "'Think well before agreeing.' Max feigns brotherly concern as he protects his bachelor pad."),
    (11, None, "'You are right, I will look for another option.' Nastya gratefully takes his advice and cancels her move."),
]
