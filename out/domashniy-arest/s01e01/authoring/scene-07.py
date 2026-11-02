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
    (0, 'Аркаш, ну что скажешь?', "'Arkasha, so what do you say?' \"Chto skazhesh?\" literally asks 'what will you say?', while clipped \"Arkash\" keeps it chummy."),
    (0, 'Когда начинать?', "'When do I start?' Literally, 'when to start?' — \"kogda\" ('when') plus dictionary-form \"nachinat\" ('to begin') is all Russian needs here. Arkady is all smiles."),
    (1, None, "'Any time you like.' Literally, 'in any moment' — \"v lyuboy moment\". Samson doesn't need to be asked twice."),
    (2, None, "'Right, I'm ready!' \"Vsyo\" literally means 'all' or 'everything', and at the start of a line it signals 'right, that's settled!'. Then Arkady slips in one more thing."),
    (3, None, "'There's just one small formality.' \"Formalnost\" is an easy cognate with English 'formality', softened by \"malenkaya\" ('little'). Samson is puzzled."),
    (4, None, "'What formality?' \"Kakaya\" ends in '-aya' to match feminine \"formalnost\". Arkady's answer is short."),
    (5, None, "'Kiss me.' \"Potseluy menya\" comes from \"tselovat\" ('to kiss'); in the show he names a much cruder humiliation, which we keep polite here. Samson can't believe his ears."),
    (6, None, "'What?' \"Chego?\" is a blunt, streetwise cousin of \"chto?\" ('what?'), showing instant disbelief. So Arkady reminds him of their childhood."),
    (7, None, "'Do you remember the toilet in the communal flat?' \"Pomnish\" ('do you remember?') leads straight into \"v kommunalnoy kvartire\", where both endings shift after \"v\" ('in')."),
    (8, None, "'I told you back then: you'll kiss me one day.' \"Togda\" means 'back then', and \"yeshchyo potseluyesh\" warns 'you'll kiss me yet!'. Samson is amazed."),
    (9, None, "'What, you remember all that?' \"Ty chto\" up front expresses stunned 'wait, what?!', followed by \"vsyo pomnish?\" ('you remember everything?')."),
    (10, None, "'Oh, I remember everything.' Opening with \"a\" in \"a ya vsyo pomnyu\" gives a quiet, icy contrast — 'oh, I remember it all'. Samson hopes it's a joke."),
    (11, None, "'Are you joking?' \"Shutish\" comes from \"shutka\" ('a joke'), asking 'are you kidding me?'. Arkady keeps a straight face."),
    (12, None, "'No. I'm serious.' Russian skips 'am' and uses the '-no' form \"seryozno\": literally 'I seriously'. Samson explodes."),
    (13, None, "'No! Never!' \"Nikogda!\" ('never!') echoes \"net!\" as Samson lunges forward, while Arkady doesn't even get up."),
    (14, None, "'Don't, Samson. Security will be here any second.' \"Ne nado\" calmly warns 'don't do that', and \"okhrana\" means 'security guards'. Right on cue, they step in."),
    (15, None, "'Please see him out.' Addressing the guards formally, Arkady adds '-te' in \"provodite\" ('escort him out'). As Samson leaves, one last line lands."),
    (16, 'Передумаешь — приходи.', "'If you change your mind, come back.' Russian needs no 'if' here: \"peredumayesh\" ('you'll rethink it') followed by \"prikhodi\" ('come on over') says it all."),
    (16, 'Должность ждёт.', "'The job is waiting.' \"Dolzhnost\" means an official post or managerial position, rather than ordinary \"rabota\"."),
]
