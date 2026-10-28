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
    (0, None, '\'And where is my knife?\' "Gde" is "where", and "moy nozh" is "my knife". The little "a" at the start can mean "and" or "but", and here it just pushes the question along.'),
    (1, None, '\'Who took my knife?\' "Kto vzyal" is "who took". "Kto" always takes the masculine past, so it\'s "vzyal" with a plain -l, whoever the thief turns out to be.'),
    (2, None, '\'Chef, I didn\'t take it.\' "Ya ne brala" is "I not took". Nastya switches to "brat\'", the everyday partner of "vzyat\'", because she\'s denying any taking at all. The "-a" shows she\'s a woman; a man would say "ne bral".'),
    (3, None, '\'I repeat: who took my knife?\' "Povtoryayu" is "I repeat", from "povtor", a repeat. This is what you say when your patience has run out.'),
    (4, None, '\'I don\'t know, chef.\' "Ya ne znayu", "I not know", is one of the most useful sentences in Russian. "Ne" goes right in front of the word it cancels.'),
    (5, None, '\'Nobody will go home from here.\' Russian doubles the negative, so "nobody" and "not" both appear before the verb. Going home is the single word "domoy", and "otsyuda" means "from here".'),
    (6, None, '\'Until you find the knife.\' Russian has no separate word for "until" here. It says "while you don\'t find", so "poka" plus "ne". And "poka" is also the casual "bye", which really means "for now".'),
    (7, None, '\'Understood, chef.\' "Ponyatno" is one word that means "it\'s clear". Nastya needs no "I" in it, and it\'s the usual way to show you got the message.'),
    (8, None, '\'I will not cook anything.\' "Ne budu" and "nichego" both say no, and Russian insists on both. "Gotovit\'", to cook, has "gotov", ready, inside it: cooking is getting things ready.'),
    (9, None, '\'Right, everyone, look for the knife.\' "Tak" works as "right" or "so". "Vse ishchem" is "all of us look", with the "we" form of the verb, so the chef counts himself in.'),
    (10, None, '\'Quick!\' "Zhivo" comes from "zhivoy", alive, so it\'s "look lively", get a move on.'),
    (11, None, '\'What is the problem?\' "Chto za" means "what kind of", so Nastya\'s question is "what kind of problem?". You can ask "chto za" about nearly anything.'),
    (12, None, '\'We will buy the same knife.\' "Takoy zhe" is "the same kind of", and "kupim", "we\'ll buy", is a single word. Nastya makes it sound very simple.'),
    (13, None, '\'And do you know what kind of knife this is?\' Look for the "chto za" again: "what kind of knife is this". The chef says "you" the friendly way to Nastya, as bosses do in kitchens.'),
]
