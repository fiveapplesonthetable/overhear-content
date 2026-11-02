# Authoring module for domashniy-arest-s01e01-scene-07.
ID = 'domashniy-arest-s01e01-scene-07'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 7
TITLE = 'Одна формальность  (One Small Formality)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Still in the mayor's office, a moment later. Last time, Samson, the bully from Arkady's childhood, came to ask for a better job, and Arkady talked him into phoning his boss and quitting on the spot. Now Samson wants to know when he starts, and Arkady has one small condition. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go back through it. Samson has just quit his old job, so he is in a hurry to start the new one."
TRANSITION = "Let's listen to the whole scene once more."
OUTRO = "That's it for this part: a childhood promise, kept after thirty years. When you watch the episode, listen for Arkady's calm reply about remembering everything; you'll catch it now. See you next time!"
CLOSING = ('arkady', 'До свидания!')
STORY = [
    ('samson', 'Аркаш, ну что скажешь? Когда начинать?', 'Arkasha, so what do you say? When do I start?', [(292, 'Аркаш, ну')], "'Что скажешь? Когда начинать?' adapted from cue 293 (приступать -> начинать)"),
    ('arkady', 'В любой момент.', 'Any time you like.', [(294, 'В любой момент')], ''),
    ('samson', 'Всё, готов!', "Right, I'm ready!", [(295, 'Всё, готов')], ''),
    ('arkady', 'Только есть одна маленькая формальность.', "There's just one small formality.", [(296, 'формальность')], "adapted from cue 296: word order made standard, 'маленькая' added"),
    ('samson', 'Какая формальность?', 'What formality?', [], 'new; cue 297 is garbled'),
    ('arkady', 'Поцелуй меня.', 'Kiss me.', [(298, 'Поцелуй меня')], 'cut: the crude rest of the cue is dropped; the narrator explains the humiliating kiss'),
    ('samson', 'Чего?', 'What?', [(299, 'Чего')], ''),
    ('arkady', 'Помнишь туалет в коммунальной квартире?', 'Do you remember the toilet in the communal flat?', [(301, 'Помнишь'), (301, 'в коммунальной квартире')], "adapted: 'головой в унитаз окунал' (dunked my head in the toilet) -> just 'the toilet'"),
    ('arkady', 'Я тебе тогда сказал: ты меня ещё поцелуешь.', "I told you back then: you'll kiss me one day.", [(302, 'я тебе сказал')], "'тогда' added; the crude 'в жопу целовать будешь' -> 'ещё поцелуешь'"),
    ('samson', 'Ты что, всё помнишь?', 'What, you remember all that?', [(306, 'ты все помнишь')], "'очкарик' (four-eyes) dropped, 'что' added"),
    ('arkady', 'А я всё помню.', 'Oh, I remember everything.', [(307, 'А я все помню')], ''),
    ('samson', 'Ты шутишь?', 'Are you joking?', [], 'new, after cue 311 (Samson thinks it is a prank)'),
    ('arkady', 'Нет. Я серьёзно.', "No. I'm serious.", [(310, 'Я серьезно')], "'Нет.' added"),
    ('samson', 'Нет! Никогда!', 'No! Never!', [], "new: Samson's refusal (in the source he swears and lunges)"),
    ('arkady', 'Не надо, Самсон. Сейчас придёт охрана.', "Don't, Samson. Security will be here any second.", [(320, 'Не надо'), (317, 'Сейчас')], 'adapted from cues 316-320 (the guards will come running)'),
    ('arkady', 'Проводите его, пожалуйста.', 'Please see him out.', [(321, 'Проводите')], "'товарищи' -> 'его, пожалуйста' (said to the guards)"),
    ('arkady', 'Передумаешь — приходи. Должность ждёт.', 'If you change your mind, come back. The job is waiting.', [(322, 'Передумаешь, приходи'), (322, 'Должность ждет')], ''),
]
WALK = [
    (0, 'Аркаш, ну что скажешь?', ["'Arkasha, so what do you say?' ", ('samson', 'Что скажешь?'), " literally asks 'what will you say?', while the short name ", ('samson', 'Аркаш'), " keeps it chummy."]),
    (0, 'Когда начинать?', ["'When do I start?' Literally, 'when to start?' — ", ('samson', 'Когда'), " is the translation for 'when', plus the action word ", ('samson', 'начинать'), " is all Russian needs here. Arkady is all smiles."]),
    (1, None, ["'Any time you like.' Literally, 'in any moment' — ", ('arkady', 'В любой момент.'), " Samson doesn't need to be asked twice."]),
    (2, None, ["'Right, I'm ready!' the Russian word ", ('samson', 'Всё'), " literally translates to 'all' or 'everything', and at the start of a line it signals 'right, that's settled!'. Then Arkady slips in one more thing."]),
    (3, None, ["'There's just one small formality.' meaning formality is an easy match with English — ", ('arkady', 'формальность,'), " softened by the describing word ", ('arkady', 'маленькая.'), " Samson is puzzled."]),
    (4, None, ["'What formality?' the term for 'what' is ", ('samson', 'Какая,'), " ending with a matching sound for 'formality'. Arkady's answer is short."]),
    (5, None, ["'Kiss me.' ", ('arkady', 'Поцелуй меня,'), " comes from the action word 'to kiss'; in the show he names a much cruder humiliation, which we keep polite here. Samson can't believe his ears."]),
    (6, None, ["'What?' ", ('samson', 'Чего?'), " is a blunt, streetwise cousin of the usual word for 'what?', showing instant disbelief. So Arkady reminds him of their childhood."]),
    (7, None, ["'Do you remember the toilet in the communal flat?' the term meaning 'do you remember' is ", ('arkady', 'Помнишь.'), " It leads straight into the phrase for 'in the communal flat' — ", ('arkady', 'в коммунальной квартире,'), " where both endings shift after the little word 'in'."]),
    (8, None, ["'I told you back then: you'll kiss me one day.' the translation for 'back then' is ", ('arkady', 'тогда,'), " and the phrase ", ('arkady', 'ещё поцелуешь'), " warns 'you'll kiss me yet!'. Samson is amazed."]),
    (9, None, ["'What, you remember all that?' The little phrase ", ('samson', 'Ты что'), " up front expresses a stunned 'wait, what?!', followed by ", ('samson', 'всё помнишь?'), " which translates to 'you remember everything?'."]),
    (10, None, ["'Oh, I remember everything.' Opening with the little word ", ('arkady', 'А'), " in ", ('arkady', 'А я всё помню'), " gives a quiet, icy contrast — 'oh, I remember it all'. Samson hopes it's a joke."]),
    (11, None, ["'Are you joking?' ", ('samson', 'Шутишь?'), " translates to 'are you kidding me?', built from the expression for 'a joke'. Arkady keeps a straight face."]),
    (12, None, ["'No. I'm serious.' Russian skips 'am' and uses ", ('arkady', 'серьёзно:'), " literally 'I seriously'. Samson explodes."]),
    (13, None, ["'No! Never!' the expression meaning 'never!' is ", ('samson', 'Никогда!'), " It echoes 'no!' as Samson lunges forward, while Arkady doesn't even get up."]),
    (14, None, ["'Don't, Samson. Security will be here any second.' The phrase ", ('arkady', 'Не надо'), " calmly warns 'don't do that', and which translates to 'security guards' is ", ('arkady', 'охрана.'), " Right on cue, they step in."]),
    (15, None, ["'Please see him out.' Addressing the guards politely, Arkady adds a respectful ending to ", ('arkady', 'Проводите,'), " which translates to 'escort him out'. As Samson leaves, one last line lands."]),
    (16, 'Передумаешь — приходи.', ["'If you change your mind, come back.' Russian needs no 'if' here: ", ('arkady', 'Передумаешь'), " translates to 'you'll rethink it', followed by ", ('arkady', 'приходи,'), " which literally means 'come on over' — that says it all."]),
    (16, 'Должность ждёт.', ["'The job is waiting.' the term for an official post or managerial position is ", ('arkady', 'Должность,'), " rather than the ordinary word for work."]),
]
