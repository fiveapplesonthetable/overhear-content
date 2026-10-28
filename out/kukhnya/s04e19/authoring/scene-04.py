# Authoring module for kukhnya-s04e19-scene-04.
ID = 'kukhnya-s04e19-scene-04'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 19
SCENE = 4
TITLE = "Странный сон Дениса  (Denis's Strange Dream)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'katya': 'Катя', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.19'
SOURCE_FILE = 'sources/kukhnya/s04/e19.ru.srt'
INTRO = "In the middle of the night, Denis bolts upright in bed after having a bizarre nightmare about his own hands. Meanwhile, early the next morning, Nastya tries to wake a sleepy Kostya so he can drive their baby son to her parents' house. Let's listen to both bedroom scenes in Russian."
OPENER = "Now let's examine Denis's midnight scare and Kostya's early wake-up call line by line."
TRANSITION = "Let's hear the night and morning bedroom exchanges again from start to finish."
OUTRO = 'Katya reassures Denis that he still has two normal hands, while reluctant Kostya finally drags himself out of bed. Listen for the plural noun meaning hands and the verbs meaning sleep and get up. See you next time!'
CLOSING = ('denis', 'До встречи!')
STORY = [
    ('denis', 'Катя, посмотри на мои руки.', 'Katya, look at my hands.', [(48, 'Катя'), (48, 'посмотри на мои руки')], 'adapted'),
    ('denis', 'Скажи, с ними всё хорошо?', 'Tell me, is everything all right with them?', [(48, 'с ними все хорошо')], 'adapted'),
    ('katya', 'Господи, их две у тебя.', 'Good grief, you have two of them.', [(49, 'Господи, их две у тебя')], ''),
    ('katya', 'Ложись обратно и спи давай.', 'Lie back down and go to sleep.', [(50, 'Спи давай')], 'adapted'),
    ('denis', 'Мне просто приснился странный сон.', 'I just had a strange dream.', [], 'new'),
    ('katya', 'Утром всё расскажешь, спокойной ночи.', 'You will tell me everything in the morning, good night.', [], 'new'),
    ('katya', 'Костя, уже шесть часов, пора вставать.', "Kostya, it is six o'clock already, time to get up.", [(51, 'Костя, Костя'), (51, 'пора вставать')], 'adapted'),
    ('katya', 'Надо Стёпу к родителям отвезти.', "We need to take Styopa to my parents' place.", [(52, 'Надо Степу к родителям отвезти')], 'adapted'),
    ('kostya', 'Настя, может, он сам доедет?', 'Nastya, maybe he can get there by himself?', [(53, 'Настя, может он сам')], 'adapted'),
    ('kostya', 'Я ему всё подробно объясню.', 'I will explain everything to him in detail.', [(53, 'а я ему объясню')], 'adapted'),
    ('kostya', 'Там же совсем не сложно.', 'It is not complicated at all.', [(53, 'там не сложно же')], 'adapted'),
    ('kostya', 'Ладно, не злись, я уже встаю.', 'All right, do not be angry, I am getting up already.', [(54, 'Я встаю')], 'adapted'),
]
WALK = [
    (0, None, '\'Katya, look at my hands.\' Denis highlights one memorable term on cue: "posmotri" means "look" (from "posmotret"), giving the line its exact edge.'),
    (1, None, '\'Tell me, is everything all right with them?\' Denis gives that reply beside Kostya: the single Russian word "khorosho" ("good, well") sets up the whole statement without needing a separate word for "it is".'),
    (2, None, "'Good grief, you have two of them.' Katya steps in honestly in their talk, testing Denis's reaction in the middle of the exchange."),
    (3, None, '\'Lie back down and go to sleep.\' Katya grounds one pointed piece at once: "obratno" means "back", and it carries the main weight of what Katya is saying.'),
    (4, None, '\'I just had a strange dream.\' Denis shares this point with candor: the little word "prosto" ("simply, just") works like a shrug in the sentence, making a big claim sound effortless.'),
    (5, None, "'You will tell me everything in the morning, good night.' Katya weighs in lightly hearing Kostya, to clear the air between them once and for all."),
    (6, None, '\'Kostya, it is six o\'clock already, time to get up.\' Katya chooses this direct word for Denis: "chasov" means "o\'clock" (from "chas"), giving the line its exact edge.'),
    (7, None, '\'We need to take Styopa to my parents\' Katya sends the reply before Kostya: the single Russian word "nado" ("it is necessary, one needs to") sets up the whole statement without needing a separate word for "it is".'),
    (8, None, "'Nastya, maybe he can get there by himself?' Kostya quizzes deadpan whether Denis really thought this through."),
    (9, None, '\'I will explain everything to him in detail.\' Kostya emphasizes one colorful word at once: "podrobno" means "in detail", and it carries the main weight of what Kostya is saying.'),
    (10, None, '\'It is not complicated at all.\' Kostya frames this point before Denis: adding "sovsem" ("completely, at all") pushes the statement all the way, leaving zero room for doubt.'),
    (11, None, "'All right, do not be angry, I am getting up already.' Kostya steps in boldly facing Katya, so Katya knows he is not just making small talk."),
]
