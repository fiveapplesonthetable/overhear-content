# Authoring module for kukhnya-s01e02-scene-22.
ID = 'kukhnya-s01e02-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 22
TITLE = 'Ищите везде  (Look Everywhere)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "The chef is in a terrible mood, and he is stomping round the kitchen picking at things. A dirty box is in the wrong place, and he still hasn't found his knife. Lyova, his sous-chef, has to answer for it. Here is the exchange in Russian first."
OPENER = "Now the chef's questions again."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Lyova hurries off to keep looking, and he has no idea where the knife actually is. You\'ve heard "ishchite", the command "look!" for a group.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Ты почему тут поставил грязную коробку?', 'Why did you put a dirty box here?', [(235, 'коробку грязную поставил')], ''),
    ('barinov', 'Убери её отсюда очень быстро!', 'Remove it from here very quickly!', [(236, 'Убери давай быстро.')], ''),
    ('barinov', 'Лёва, вы уже нашли мой нож?', 'Lyova, have you already found my knife?', [(237, 'Лёва, нож нашли?')], ''),
    ('lyova', 'Мы ещё не нашли его, шеф.', 'We have not found it yet, Chef.', [(238, 'Ещё нет, шеф.')], ''),
    ('barinov', 'Вы точно везде хорошо искали?', 'Did you definitely look well everywhere?', [(238, 'Везде смотрели?')], ''),
    ('lyova', 'Да, мы всё проверили на кухне.', 'Yes, we checked everything in the kitchen.', [(239, 'Везде.')], ''),
    ('barinov', 'Значит, продолжайте искать дальше!', 'Then continue to look further!', [(239, 'Ну ищите.')], ''),
    ('barinov', 'Кто-то мог случайно оставить нож внутри.', 'Someone could accidentally leave the knife inside.', [(240, 'оставил там нож')], ''),
    ('barinov', 'Например, кто-то забыл нож в рыбе.', 'For example, someone forgot the knife in the fish.', [(241, 'Ну, в рыбе, например.')], ''),
    ('lyova', 'В рыбе? Это невозможно, шеф!', 'In the fish? That is impossible, Chef!', [(242, 'В рыбе?')], ''),
    ('barinov', 'Я не знаю. Ищите везде!', 'I do not know. Look everywhere!', [(243, 'Ищите везде.')], ''),
    ('lyova', 'Хорошо, шеф, мы всё найдём.', 'Alright, Chef, we will find everything.', [(244, 'Да, шеф.')], ''),
    ('barinov', 'Без ножа мы не сможем работать!', 'Without the knife we will not be able to work!', [], ''),
]
WALK = [
    (0, None, '\'Why did you put a dirty box here?\' "Put" is the word for "make stand", so a box is "stood" somewhere. The two describing words end in "-uyu" as the object.'),
    (1, None, '\'Remove it from here very quickly!\' The word for "it" is feminine, because "box" is a feminine word. "Remove" is a friendly command.'),
    (2, None, '\'Lyova, have you already found my knife?\' The chef says "vy", but here it\'s the plural, "you all", not the polite one. He means Lyova and the others.'),
    (3, None, '\'We have not found it yet, Chef.\' "Not yet" is "still not". The little "yego" for "it" never changes.'),
    (4, None, '\'Did you definitely look well everywhere?\' "Definitely" and "everywhere" are two short words, with "well" between. It sounds like a real interrogation.'),
    (5, None, '\'Yes, we checked everything in the kitchen.\' "Checked" ends in "-li", the plural for "we". "Everything" is one short word.'),
    (6, None, '\'Then continue to look further!\' "Continue" is a command to a group. "Further" is also the word for "more", in the sense of keep going.'),
    (7, None, '\'Someone could accidentally leave the knife inside.\' "Could" is a short word, "mog". "Accidentally" comes from the word for "chance", and "inside" is one small word.'),
    (8, None, '\'For example, someone forgot the knife in the fish.\' "For example" is "on example". "Forgot" ends in -l, and "in the fish" has an -e on the fish.'),
    (9, None, '\'In the fish? That is impossible, Chef!\' Lyova repeats the words with a question in his voice. "Impossible" is "not" plus "possible".'),
    (10, None, '\'I do not know. Look everywhere!\' "Ishchite" is the command "look for", in the form for a group. The chef has stopped being logical.'),
    (11, None, '\'Alright, Chef, we will find everything.\' "We will find" is one word. Lyova is trying to calm him.'),
    (12, None, '\'Without the knife we will not be able to work!\' "Without" makes "knife" take an -a. "Will be able" is one word, with "not" before it.'),
]
