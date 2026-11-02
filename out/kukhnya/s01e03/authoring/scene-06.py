# Authoring module for kukhnya-s01e03-scene-06.
ID = 'kukhnya-s01e03-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = 'Ложная тревога  (A False Alarm)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'Max runs to the bar and accuses Kostya of telling the prosecutor everything. Kostya has no idea what he is talking about, and the truth turns out to be much funnier. Here is their talk in Russian first.'
OPENER = 'Back through the misunderstanding.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max\'s terrifying prosecutor was only looking for the restroom. The phrase to take away is the one for "thank goodness", which is what Max says once the danger has passed.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Костя, зачем ты ему сказал?', 'Kostya, why did you tell him?', [(163, 'Зачем ты ему сказал')], ''),
    ('max', 'Мне же теперь полный конец.', 'I am completely finished now.', [(163, 'Мне ж теперь конец')], ''),
    ('kostya', 'Кому я сказал?', 'Who did I tell?', [(164, 'Кому')], ''),
    ('max', 'Тому мужику в костюме.', 'That man in the suit.', [(164, 'Этому мужику')], ''),
    ('max', 'Чего он у тебя спрашивал?', 'What was he asking you?', [(164, 'Чего он спрашивал')], ''),
    ('kostya', 'Да успокойся ты наконец.', 'Oh, calm down already.', [], ''),
    ('kostya', 'Он просто спрашивал про туалет.', 'He was simply asking about the restroom.', [(165, 'Он спрашивал, где туалет')], ''),
    ('max', 'Серьёзно? Только про туалет?', 'Seriously? Only about the restroom?', [], ''),
    ('kostya', 'Да, он искал туалет.', 'Yes, he was looking for the restroom.', [], ''),
    ('max', 'А про меня не спрашивал?', "And he didn't ask about me?", [], ''),
    ('kostya', 'Кому ты вообще нужен?', 'Who needs you anyway?', [], ''),
    ('max', 'Слава богу, пронесло.', 'Thank goodness, dodged a bullet.', [], ''),
    ('kostya', 'Ты чего такой нервный сегодня?', 'Why are you so nervous today?', [], ''),
    ('max', 'Неважно, налей мне скорее воды.', 'Never mind, pour me some water quickly.', [], ''),
]
WALK = [
    (0, None, [
        "'Kostya, why did you tell him?' The word for 'what for' is ",
        ('max', 'зачем'),
        ", which sounds very accusing. The 'to him' part translates to ",
        ('max', 'ему'),
        '.'
    ]),
    (1, None, [
        "'I am completely finished now.' Literally, this translates to 'to me, you know, now a full end'. This is how people say 'I am done for' using the word for 'end', which is ",
        ('max', 'конец.')
    ]),
    (2, None, [
        "'Who did I tell?' The word for 'to whom' is ",
        ('kostya', 'Кому'),
        ", which is the 'to' shape of 'who'. Kostya throws the question right back."
    ]),
    (3, None, [
        "'That man in the suit.' A slightly rough word for a man is ",
        ('max', 'мужику'),
        ". He answers the question with 'to that man', and 'in a suit' translates to ",
        ('max', 'в'),
        ('max', 'костюме.')
    ]),
    (4, None, [
        "'What was he asking you?' People say 'to ask at' someone, so 'at you' is built from ",
        ('max', 'у'),
        ' and ',
        ('max', 'тебя'),
        ". The word for 'what' here is ",
        ('max', 'Чего'),
        ', which people often use in fast speech.'
    ]),
    (5, None, [
        "'Oh, calm down already.' The word for 'calm yourself' is ",
        ('kostya', 'успокойся'),
        ", which is built from the idea of peace. This adds impatience using the word for 'finally', which is ",
        ('kostya', 'наконец.')
    ]),
    (6, None, [
        "'He was simply asking about the restroom.' The word for 'about' is ",
        ('kostya', 'про'),
        ", which does not change the shape of following words. The word for 'restroom' comes from French and translates to ",
        ('kostya', 'туалет.')
    ]),
    (7, None, [
        "'Seriously? Only about the restroom?' Literally, this starts with ",
        ('max', 'Серьёзно?'),
        " The phrase 'only about' puts ",
        ('max', 'Только'),
        ' right in front of ',
        ('max', 'про'),
        '.'
    ]),
    (8, None, [
        "'Yes, he was looking for the restroom.' The word for 'looked for' is ",
        ('kostya', 'искал'),
        '. It ends with a special sound because it describes a man in the past.'
    ]),
    (9, None, [
        "'And he didn't ask about me?' The opening ",
        ('max', 'А'),
        " marks a contrast, like 'and what about...'. The phrase 'about me' translates to ",
        ('max', 'про'),
        ('max', 'меня'),
        ", and 'didn't ask' is ",
        ('max', 'не'),
        ('max', 'спрашивал?')
    ]),
    (10, None, [
        "'Who needs you anyway?' Here, the person needed is the main focus, ",
        ('kostya', 'ты'),
        ", and the one who needs goes in the 'to' shape, ",
        ('kostya', 'Кому'),
        ". The word for 'anyway' is ",
        ('kostya', 'вообще'),
        ', which adds a bit of scorn.'
    ]),
    (11, None, [
        "'Thank goodness, dodged a bullet.' Literally, 'thank goodness' is built from ",
        ('max', 'Слава'),
        ' and ',
        ('max', 'богу,'),
        " meaning 'glory to God'. The word for 'dodged a bullet' translates to ",
        ('max', 'пронесло.')
    ]),
    (12, None, [
        "'Why are you so nervous today?' The casual phrase for 'why are you' is built from ",
        ('kostya', 'Ты'),
        ' and ',
        ('kostya', 'чего'),
        ". The word for 'such nervous' translates to ",
        ('kostya', 'такой'),
        ('kostya', 'нервный'),
        ", and 'today' is ",
        ('kostya', 'сегодня?')
    ]),
    (13, None, [
        "'Never mind, pour me some water quickly.' The word for 'never mind' is ",
        ('max', 'Неважно,'),
        " which is built from the word for 'no' and the word for important. When asking for some water, the word changes its shape for 'some of', becoming ",
        ('max', 'воды.')
    ]),
]
