# Authoring module for kukhnya-s01e04-scene-23.
ID = 'kukhnya-s01e04-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 23
TITLE = "Увольнение Макса  (Max's Dismissal)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "In his office, the chef is complaining to his pet fish, Arkady, while in the locker room Max packs his bag, and Nastya tries to comfort him. Here's the Russian first."
OPENER = "Let's go through the two sad scenes."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Nastya promises that Max won\'t be alone, and the two of them will think of something. If you take one phrase from here, make it the one for "you have me".'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('barinov', 'Только ты, Аркадий, меня понимаешь.', 'Only you, Arkady, understand me.', [(317, 'Только ты, Аркадий, меня и понимаешь.')], ''),
    ('barinov', 'Вокруг меня одни лентяи и неумехи!', 'Around me are only slackers and fools!', [], ''),
    ('nastya', 'Максим, ты куда сейчас собираешься?', 'Maxim, where are you getting ready to go now?', [(318, 'Ты куда?')], ''),
    ('max', 'Куда-нибудь, шеф меня только что уволил.', 'Anywhere, the chef just fired me.', [(319, 'Куда-нибудь. Меня только что уволили.')], ''),
    ('nastya', 'Может быть, шеф просто неудачно пошутил?', 'Maybe the chef was just joking unsuccessfully?', [(320, 'А может, он пошутил?')], ''),
    ('max', 'Нет, он никогда так не шутит.', 'No, he never jokes like that.', [(321, 'Он нас любит шутить.')], ''),
    ('nastya', 'Я очень не хочу, чтобы ты уходил!', 'I really do not want you to leave!', [(327, 'Максим, я не хочу, чтобы ты уходил.')], ''),
    ('max', 'Я тоже хотел остаться на этой кухне.', 'I also wanted to stay in this kitchen.', [(328, 'Я тоже.')], ''),
    ('nastya', 'Давай я спрячу тебя прямо здесь!', 'Let me hide you right here!', [(325, 'Я тебя спрячу.')], ''),
    ('max', 'Спасибо, Настя, но прятаться глупо.', 'Thank you, Nastya, but hiding is silly.', [], ''),
    ('nastya', 'Ты главное не переживай из-за шефа.', 'The main thing is do not worry because of the chef.', [(329, 'Ты не переживай.')], ''),
    ('nastya', 'Теперь у тебя в ресторане есть я!', 'Now you have me in the restaurant!', [(330, 'Теперь у тебя есть я.')], ''),
    ('max', 'Спасибо за поддержку, ты настоящий друг.', 'Thank you for the support, you are a true friend.', [], ''),
    ('nastya', 'Мы обязательно что-нибудь придумаем!', 'We will definitely come up with something!', [], ''),
]
WALK = [
    (0, None, [
        "'Only you, Arkady, understand me.' ",
        ('barinov', 'Только ты,'),
        " translates to 'only you'. He tells his fish ",
        ('barinov', 'понимаешь.'),
        " which is the phrase for 'you understand'."
    ]),
    (1, None, [
        "'Around me are only slackers and fools!' Here, ",
        ('barinov', 'одни'),
        " translates to 'nothing but'. The expression for slackers, ",
        ('barinov', 'лентяи'),
        " is built from the translation for laziness, and ",
        ('barinov', 'неумехи!'),
        " is built from the action word for not knowing how."
    ]),
    (2, None, [
        "'Maxim, where are you getting ready to go now?' ",
        ('nastya', 'собираешься?'),
        " literally means 'you gather yourself', which is the Russian expression for getting ready. ",
        ('nastya', 'куда'),
        " translates to 'where to'."
    ]),
    (3, None, [
        "'Anywhere, the chef just fired me.' ",
        ('max', 'Куда-нибудь,'),
        " translates to 'anywhere' or 'somewhere or other'. ",
        ('max', 'только что'),
        " is the Russian term for 'just now'."
    ]),
    (4, None, [
        "'Maybe the chef was just joking unsuccessfully?' The Russian expression for unsuccessfully, ",
        ('nastya', 'неудачно'),
        " is built from the phrase for luckily. The action word ",
        ('nastya', 'пошутил?'),
        " is built from the translation for a joke."
    ]),
    (5, None, [
        "'No, he never jokes like that.' ",
        ('max', 'никогда так не шутит.'),
        " literally translates to 'never so doesn\\'t joke'."
    ]),
    (6, None, [
        "'I really do not want you to leave!' After saying ",
        ('nastya', 'не хочу, чтобы'),
        " meaning 'I don\\'t want that', the following action word takes a past form, as in ",
        ('nastya', 'чтобы ты уходил!')
    ]),
    (7, None, [
        "'I also wanted to stay in this kitchen.' The expression for 'to stay' is ",
        ('max', 'остаться'),
        ". The phrase ",
        ('max', 'на этой кухне.'),
        " translates to 'in this kitchen'."
    ]),
    (8, None, [
        "'Let me hide you right here!' Using ",
        ('nastya', 'Давай я'),
        " followed by an action word for yourself translates to 'let me'. ",
        ('nastya', 'спрячу'),
        " is the expression for 'I\\'ll hide'."
    ]),
    (9, None, [
        "'Thank you, Nastya, but hiding is silly.' ",
        ('max', 'прятаться'),
        " translates to 'to hide oneself'. ",
        ('max', 'глупо.'),
        " meaning silly, is built from the describing word for stupid."
    ]),
    (10, None, [
        "'The main thing is do not worry because of the chef.' ",
        ('nastya', 'не переживай'),
        " translates to 'don\\'t fret', and is literally built from 'to live through'. ",
        ('nastya', 'из-за'),
        " is the little word for 'because of'."
    ]),
    (11, None, [
        "'Now you have me in the restaurant!' ",
        ('nastya', 'Теперь у тебя'),
        " means 'now at you', and ",
        ('nastya', 'есть я!'),
        " literally translates to 'there is me', which is how you express having something."
    ]),
    (12, None, [
        "'Thank you for the support, you are a true friend.' The phrase for support, ",
        ('max', 'поддержку,'),
        " is built from the word for 'under' and the action word for 'to hold'. ",
        ('max', 'настоящий'),
        " translates to 'real'."
    ]),
    (13, None, [
        "'We will definitely come up with something!' By adding an extra part to the action word for 'to think', you get ",
        ('nastya', 'придумаем!'),
        " meaning 'we will think up'. Tacking a little word onto 'what' gives ",
        ('nastya', 'что-нибудь'),
        " which is the translation for 'something'."
    ]),
]
