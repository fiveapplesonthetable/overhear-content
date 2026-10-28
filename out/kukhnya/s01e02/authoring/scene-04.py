# Authoring module for kukhnya-s01e02-scene-04.
ID = 'kukhnya-s01e02-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 4
TITLE = 'Где мой нож?  (Where Is My Knife?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Chef Barinov has lost his favourite knife, and he is not going to let anyone forget it. Nastya is one of the people he questions. Here's the whole scene in Russian first, and don't worry about catching every word."
OPENER = "Let's go back and watch the chef lose his temper."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'A missing knife, and no one is allowed home. If you hear "ne znayu" or "ne budu" in the next episode, you\'ll know what they mean.'
CLOSING = ('nastya', 'До встречи!')
STORY = [
    ('barinov', 'А где мой нож?', 'And where is my knife?', [(76, 'где мой нож')], ''),
    ('barinov', 'Кто взял мой нож?', 'Who took my knife?', [(80, 'Кто взял мой нож')], ''),
    ('nastya', 'Шеф, я не брала.', "Chef, I didn't take it.", [], ''),
    ('barinov', 'Повторяю. Кто взял мой нож?', 'I repeat: who took my knife?', [(81, 'Повторяю'), (82, 'Кто взял мой нож')], ''),
    ('nastya', 'Я не знаю, шеф.', "I don't know, chef.", [], ''),
    ('barinov', 'Никто отсюда домой не уйдёт.', 'Nobody will go home from here.', [(87, 'никто из вас отсюда домой не уйдет')], ''),
    ('barinov', 'Пока вы не найдёте нож.', 'Until you find the knife.', [(87, 'Пока вы мне не найдете нож')], ''),
    ('nastya', 'Понятно, шеф.', 'Understood, chef.', [(88, 'Понятно')], ''),
    ('barinov', 'Я не буду ничего готовить.', 'I will not cook anything.', [(89, 'Не буду ничего готовить')], ''),
    ('barinov', 'Так, все ищем нож.', 'Right, everyone, look for the knife.', [(90, 'Так, все ищем нож')], ''),
    ('barinov', 'Живо!', 'Quick!', [(91, 'Живо')], ''),
    ('nastya', 'А что за проблема?', 'What is the problem?', [(92, 'А что за проблема')], ''),
    ('nastya', 'Мы такой же нож купим.', 'We will buy the same knife.', [(92, 'такой же нож купим')], ''),
    ('barinov', 'А ты знаешь, что это за нож?', 'And do you know what kind of knife this is?', [(93, 'А ты знаешь, что это за нож')], ''),
]
WALK = [
    (0, None, '\'And where is my knife?\' The question word comes first, as in English, and "my" sits in front of the knife. That small "a" at the start can mean "and" or "but", and here it just pushes the question along.'),
    (1, None, '\'Who took my knife?\' Again the question word leads. The "-l" on the end of "took" is the past tense, used for a man or a thing.'),
    (2, None, '\'Chef, I didn\'t take it.\' Literally, "I not took". The "-a" at the end of the last word tells you the speaker is a woman, and a man would say "bral".'),
    (3, None, '\'I repeat: who took my knife?\' Think of "povtor", a repeat, with "-yayu" for "I". This is what you say when your patience has run out.'),
    (4, None, '\'I don\'t know, chef.\' One of the most useful sentences in Russian, and it\'s built exactly as it sounds: "I not know". The "ne" goes right in front of the word it cancels.'),
    (5, None, '\'Nobody will go home from here.\' Russian doubles the negative, so "nobody" and "not" both appear before the verb. "Domoy" is a single word for "to home", and "otsyuda" means "from here".'),
    (6, None, '\'Until you find the knife.\' Russian has no separate word for "until" here. It says "while you don\'t find", so "poka" plus "ne". And "poka" is also the casual "bye", which really means "for now".'),
    (7, None, '\'Understood, chef.\' One short word for "understood", literally "it\'s clear". Nastya needs no "I" in it, and it\'s the usual way to show you got the message.'),
    (8, None, '\'I will not cook anything.\' Here\'s another double negative: "ne budu" and "nichego" both say no, and Russian insists on both. "To cook" has "ready" hiding inside it, because cooking is getting things ready.'),
    (9, None, '\'Right, everyone, look for the knife.\' The first word works as "right" or "so". The chef says "we look", so he is joining the search, which is a nice touch for a boss.'),
    (10, None, '\'Quick!\' It comes from the word for "alive", so "look lively", get a move on.'),
    (11, None, '\'What is the problem?\' "Chto za" means "what kind of", so Nastya\'s question is "what kind of problem?". You can ask "chto za" about nearly anything.'),
    (12, None, '\'We will buy the same knife.\' "The same kind of" is two little words, and "we will buy" is just one. Nastya makes it sound very simple.'),
    (13, None, '\'And do you know what kind of knife this is?\' Look for the "chto za" again: "what kind of knife is this". The chef says "you" the friendly way to Nastya, as bosses do in kitchens.'),
]
