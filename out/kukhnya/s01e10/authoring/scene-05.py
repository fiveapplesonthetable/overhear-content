# Authoring module for kukhnya-s01e10-scene-05.
ID = 'kukhnya-s01e10-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 5
TITLE = 'Неожиданное признание  (An Unexpected Confession)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "Max finds Barinov in a dark mood and asks what's wrong. The chef has lost money on football, but that's not the worst of it. He has a piece of news for Max, and it's about Vika. Listen to the tone before the words."
OPENER = 'Now for the details.'
TRANSITION = 'Once more, the whole thing through.'
OUTRO = "Max can't quite believe it, and he asks whether it's a joke. The news came from a little girl, and it will turn his day upside down. Until next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Здравствуйте, шеф, как ваши дела сегодня?', 'Hello, chef, how are your affairs today?', [(21, 'Здрасте.')], ''),
    ('barinov', 'Макс, не задавай мне глупых вопросов.', 'Max, do not ask me foolish questions.', [], ''),
    ('max', 'Вы опять проиграли деньги на ставках?', 'Did you lose money on bets again?', [(22, 'Опять проигрался?')], ''),
    ('barinov', 'Я бы сейчас с удовольствием выпил водки.', 'I would gladly drink vodka right now.', [(23, 'Да я бы водки хлебнул.')], ''),
    ('max', 'Что ещё неприятного у вас случилось?', 'What else unpleasant has happened to you?', [(24, 'Что случилось?')], ''),
    ('barinov', 'Дело вовсе не в моих ставках.', 'The matter is not at all about my bets.', [], ''),
    ('max', 'А в чём тогда настоящая проблема?', 'Then what is the real problem?', [], ''),
    ('barinov', 'У меня есть для тебя важная новость.', 'I have important news for you.', [], ''),
    ('max', 'Какая новость, шеф, говорите скорее.', 'What news, chef, tell me quickly.', [], ''),
    ('barinov', 'Тётя Вика сказала, что любит тебя.', 'Aunt Vika said that she loves you.', [(25, 'А тетя Вика сказала, что любит тебя.')], ''),
    ('max', 'Что? Этого просто не может быть!', 'What? That simply cannot be!', [], ''),
    ('barinov', 'Она сама призналась мне в этом.', 'She herself confessed this to me.', [], ''),
    ('max', 'Шеф, вы точно не шутите сейчас?', 'Chef, are you definitely not joking right now?', [], ''),
]
WALK = [
    (0, None, '\'Hello, chef, how are your affairs today?\' Russians ask "kak vashi dela", "how are your affairs", in the plural, where we say "how are you". With a friend it\'s "kak dela". Max has no idea what he\'s in for.'),
    (1, None, '\'Max, do not ask me foolish questions.\' Russians "zadavat", "set", a question, like setting a task. After "ne", "glupye voprosy" becomes "glupykh voprosov". Barinov is short with him, as usual.'),
    (2, None, '\'Did you lose money on bets again?\' "Proigrali" is the losing-in-a-game word the mother used in the first scene. "Na stavkakh" is "on bets", with -akh after "na". Max has guessed, and he\'s right.'),
    (3, None, '\'I would gladly drink vodka right now.\' "By" makes "would", and it goes with the past: "ya by vypil", "I would drank". "S udovolstviem", "with pleasure", is Russian for "gladly". "Vodki" is "some vodka".'),
    (4, None, '\'What else unpleasant has happened to you?\' "Nepriyatnogo" is "not pleasant" with the "of" ending after "chto eshchyo". "U vas sluchilos" is "at you happened". Max says "vas", politely.'),
    (5, None, '\'The matter is not at all about my bets.\' Russians say "delo v", "the matter is in", and then the thing. So "delo ne v moikh stavkakh" is "the matter is not in my bets". "Vovse" is "at all".'),
    (6, None, '\'Then what is the real problem?\' "A v chyom", "and in what", picks up the "delo v" from the chef\'s line. "Nastoyashchaya" is "real", the same word as in "true friend". "Problema" is easy.'),
    (7, None, '\'I have important news for you.\' Here Russian does add "est", "there is": "u menya est dlya tebya", "at me there is for you". It stresses that he has something. Barinov says "tebya", the casual "you".'),
    (8, None, '\'What news, chef, tell me quickly.\' "Kakaya", "what", ends in -aya because "novost" is a she-word. "Govorite" is the polite "speak", with -te. "Skoree" is "quicker".'),
    (9, None, '\'Aunt Vika said that she loves you.\' Barinov keeps his daughter\'s way of saying it, "tyotya Vika". There\'s no "she" in the Russian, only "skazala, chto lyubit tebya", "said that loves you".'),
    (10, None, '\'What? That simply cannot be!\' After "ne", "eto" becomes "etogo": "etogo ne mozhet byt", a set phrase. And "mozhet byt" on its own means "maybe".'),
    (11, None, '\'She herself confessed this to me.\' "Sama" is "herself", and it gives the claim weight. "Priznalas", "confessed", ends in the woman\'s -las. "V etom" is "in this": Russians confess "in" something.'),
    (12, None, '\'Chef, are you definitely not joking right now?\' "Tochno" is "definitely", and "vy ne shutite" is the polite "you aren\'t joking". "Shutka" is a joke, and "shutit" is to joke.'),
]
