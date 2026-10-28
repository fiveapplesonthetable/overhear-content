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
    (0, 'Аркаш, ну что скажешь?', "'Arkasha, so what do you say?' He uses a short, friendly form of Arkady's name, as old neighbours do."),
    (0, 'Когда начинать?', "'When do I start?' Literally, 'when to start?' Just the word for 'when' and a verb in its basic form. Arkady is all smiles."),
    (1, None, "'Any time you like.' Literally, 'at any moment'. Samson doesn't need to be asked twice."),
    (2, None, "'Right, I'm ready!' The first word means 'all', but here it just means 'that's settled'. Then Arkady slips in one more thing."),
    (3, None, "'There's just one small formality.' The long word sounds just like its English cousin. Samson is puzzled."),
    (4, None, "'What formality?' The question word changes its ending to match the feminine noun. Arkady's answer is short."),
    (5, None, "'Kiss me.' This is the command form of the verb 'to kiss'. In the show he names a crude, humiliating kind of kiss; we keep it simple. Samson can't believe his ears."),
    (6, None, "'What?' A casual, rather rough way to say it. So Arkady reminds him of their childhood."),
    (7, None, "'Do you remember the toilet in the communal flat?' When they were boys, Samson used to push little Arkasha's head into that toilet. Notice that the endings change after the little word for 'in'. And the boy made a promise."),
    (8, None, "'I told you back then: you'll kiss me one day.' The verb for 'told' is past tense and masculine, because Arkady is a man. Samson is amazed."),
    (9, None, "'What, you remember all that?' In this moment, Arkady's answer is the line he has waited thirty years to say."),
    (10, None, "'Oh, I remember everything.' The little word at the start, meaning 'and' or 'but', gives it a quiet, calm sting. Samson hopes it's a joke."),
    (11, None, "'Are you joking?' But Arkady keeps a straight face."),
    (12, None, "'No. I'm serious.' A phrase Arkady likes; you'll hear it from him again. Samson explodes."),
    (13, None, "'No! Never!' He is furious and comes at Arkady, who doesn't even get up."),
    (14, None, "'Don't, Samson. Security will be here any second.' Two very useful words open this line: they mean 'don't' or 'no need'. And the guards do come in."),
    (15, None, "'Please see him out.' To the guards Arkady is polite, so the verb has the formal, plural ending. And as Samson leaves, one last line."),
    (16, 'Передумаешь — приходи.', "'If you change your mind, come back.' There is no word for 'if': the first verb, in the future, does that job."),
    (16, 'Должность ждёт.', "'The job is waiting.' The word here means a post, a position, rather than simple work."),
]
