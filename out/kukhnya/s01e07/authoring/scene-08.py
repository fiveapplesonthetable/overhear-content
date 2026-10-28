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
INTRO = "Back at Claude Monet, Max has a problem. Kostya, who runs the bar, has offered Nastya a room in the very flat where Max has just agreed to live. Max doesn't want to share it, and he knows how to talk Nastya out of it. First, the Russian."
OPENER = "Let's replay the talk. Max is smooth and a bit sly, and the lines are short."
TRANSITION = 'Now the whole conversation in one go.'
OUTRO = "Max's trick is to make his friend sound unbearable: 'he snores'. It works, and it also gives you a good Russian word for a very common complaint. See you next time."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('max', 'Настя, ты знаешь, где снять квартиру?', 'Nastya, do you know where to rent a flat?', [(86, 'Настя, тебя никто знакомый квартиру не сдает')], 'a tenant rents with the word for снять, so the line says where to take a flat'),
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
    (0, None, '\'Nastya, do you know where to rent a flat?\' A tenant rents with snyat\', which also means to take down or take off. "Gde snyat\'" is just \'where to rent\'; Russian needs no \'should\' here.'),
    (1, None, '\'I was looking for a place myself this morning.\' Nastya drops \'I\' and starts with sama, the feminine \'myself\', and iskala ends in -la for a woman. "Zhilyo", a place to live, came up in Max\'s chat with Kostya.'),
    (2, None, "'And did you manage to find a room?' Tebe udalos', 'to you it succeeded', is Russian for 'you managed'. It works for any success: mne udalos', I managed."),
    (3, None, '\'Kostik helped me, I am moving to his place.\' "Pomog", \'helped\', is a man\'s past tense with no -l, and it takes mne, \'to me\'. K nemu, \'to him\', means to his place.'),
    (4, None, '\'Wait, Kostya invited you to live together?\' "Pogodi" is a casual \'hang on\'. "Pozval" is literally \'called\', so Kostya \'called you to live together\'.'),
    (5, None, '\'Yes, after all he and I are dating.\' My s nim, \'we with him\', means \'he and I\'. "Ved\'" adds \'after all\', as if it were obvious.'),
    (6, None, '\'To be honest, I do not envy you at all.\' "Zavidovat\'", to envy, is aimed at a person with tebe, \'to you\': you envy \'to\' someone. "Sovsem ne" means \'not at all\'.'),
    (7, None, '\'Why? Kostya is such a sweet guy.\' "Milyy" is \'sweet\' or \'nice\' for a person, and takoy milyy is \'such a sweet\'. "Paren\'" is the casual word for a young man.'),
    (8, None, '\'At night he snores terribly and loudly!\' "Strashno", \'terribly\', shares a root with strakh, fear. "Khrapit", \'snores\', comes from the same root as khrap, snoring.'),
    (9, None, '\'Oh, I cannot stand snoring at all!\' "Vynosit\'" is literally to carry out, but ne vynoshu means \'I can\'t stand\'. "Khrap" is the noun for snoring.'),
    (10, None, '\'Think well before agreeing.\' "Prezhde chem", \'before\', is followed by the \'to\' form: prezhde chem soglashat\'sya, before agreeing.'),
    (11, None, '\'You are right, I will look for another option.\' "Ty prav" is said to a man; to a woman it would be ty prava. Variant is a false friend: it means \'option\'.'),
]
