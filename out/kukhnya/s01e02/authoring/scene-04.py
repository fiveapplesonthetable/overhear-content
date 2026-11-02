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
OUTRO = 'A missing knife, and no one is allowed home. In the next episode, you might hear some of these useful phrases again.'
CLOSING = ("nastya", "Счастливо!")
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
    (0, None, ['\'And where is my knife?\' Literally, "and where my knife", with no "is" anywhere, since Russian drops the existence word for now. The little word ', ('barinov', 'А'), ' in front just nudges the question along, like a weary "so".']),
    (1, None, ['\'Who took my knife?\' ', ('barinov', 'Кто взял'), ' translates to "who took". The term for "who" always takes the default past form for a man, so it ends with a plain -l, whoever the thief turns out to be.']),
    (2, None, ['\'Chef, I didn\'t take it.\' ', ('nastya', 'я не брала.'), ' literally means "I not took". Nastya switches to the everyday action word for taking, because she is denying any taking at all. The little "a" at the end shows she is a woman.']),
    (3, None, ['\'I repeat: who took my knife?\' The term for "I repeat" is ', ('barinov', 'Повторяю.'), ', built from the term for a repeat. This is what you say when your patience has run out.']),
    (4, None, ['\'I don\'t know, chef.\' ', ('nastya', 'Я не знаю,'), ' translates to "I not know", and is one of the most useful sentences in Russian. The little word for "not" goes right in front of the action word it cancels.']),
    (5, None, ['\'Nobody will go home from here.\' Russian doubles the negative, so "nobody" and "not" both appear before the action word. Going home is the single word ', ('barinov', 'домой'), ', and ', ('barinov', 'отсюда'), ' translates to "from here".']),
    (6, None, ['\'Until you find the knife.\' Russian has no separate word for "until" here. It translates to "while you don\'t find", so it uses ', ('barinov', 'Пока'), ' plus the term for "not". And that first word is also the casual "bye", which really means "for now".']),
    (7, None, ['\'Understood, chef.\' The term for "understood" is ', ('nastya', 'Понятно,'), ', which literally means "it\'s clear". Nastya needs no "I" in it, and it\'s the usual way to show you got the message.']),
    (8, None, ['\'I will not cook anything.\' The words for "I will not" and "nothing" both say no, and Russian insists on both. The action word for cooking is ', ('barinov', 'готовить.'), ', built from the describing word for "ready": cooking is getting things ready.']),
    (9, None, ['\'Right, everyone, look for the knife.\' ', ('barinov', 'Так,'), ' works as "right" or "so". ', ('barinov', 'все ищем'), ' translates to "all of us look", with the "we" form of the action word, so the chef counts himself in.']),
    (10, None, ['\'Quick!\' ', ('barinov', 'Живо!'), ' is built from the describing word for "alive", so it translates to "look lively" or "get a move on".']),
    (11, None, ['\'What is the problem?\' ', ('nastya', 'что за'), ' translates to "what kind of", so Nastya\'s question literally means "what kind of problem?". You can ask this about nearly anything.']),
    (12, None, ['\'We will buy the same knife.\' ', ('nastya', 'такой же'), ' translates to "the same kind of", and the term for "we\'ll buy" is a single action word. Nastya makes it sound very simple.']),
    (13, None, ['\'And do you know what kind of knife this is?\' Look for the phrase ', ('barinov', 'что это за'), ' again: it translates to "what kind of knife is this". The chef uses the term for "you" in the friendly way to Nastya, as bosses do in kitchens.']),
]
