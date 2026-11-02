# Authoring module for kukhnya-s01e11-scene-21.
ID = 'kukhnya-s01e11-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 21
TITLE = 'Все равны  (Everyone Is Equal)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'Barinov carries the soup himself, to the guest who ordered it first. Vika watches in horror, because the critic is still waiting. Let the language wash over you first.'
OPENER = 'Time to look at it properly.'
TRANSITION = 'Now, from the top, in one go.'
OUTRO = "In the chef's kitchen, everyone is equal, even critics. It's the kind of principle you can admire from a distance. That's all for now."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Твой суп, дружище, приятного аппетита.', 'Your soup, buddy, enjoy your meal.', [(282, 'Твой суп, дружище, приятного аппетита.')], ''),
    ('vika', 'Витя, ты что делаешь?', 'Vitya, what are you doing?', [(283, 'Ты что делаешь?')], ''),
    ('barinov', 'Я делаю то, что должен делать.', 'I am doing what I must do.', [(284, 'То, что должен.')], ''),
    ('vika', 'Но там же сидит важный критик!', 'But an important critic is sitting right there!', [(284, 'Там же критик.')], ''),
    ('barinov', 'Мне всё равно, кто там сидит.', 'I do not care who is sitting there.', [(285, 'Мне что, это только одно и надо?')], ''),
    ('barinov', 'Этот гость заказал суп раньше.', 'This guest ordered soup earlier.', [(287, 'Этот человек раньше заказал суп, он его получил.')], ''),
    ('vika', 'Критик очень зол, он уйдёт!', 'The critic is very angry, he will leave!', [], ''),
    ('barinov', 'Пусть уходит, если не умеет ждать.', 'Let him leave if he does not know how to wait.', [], ''),
    ('vika', 'Ты рискуешь репутацией нашего ресторана.', "You are risking our restaurant's reputation.", [], ''),
    ('barinov', 'Да будь он хоть трижды критик!', 'Even if he were three times a critic!', [(285, 'Да будь он хоть трижды критик,')], ''),
    ('barinov', 'Я всем гостям подаю по очереди.', 'I serve all guests in turn.', [(286, 'я всем подаю по очереди.')], ''),
    ('barinov', 'У меня на кухне все равны!', 'In my kitchen everyone is equal!', [(289, 'У меня на кухне все равны.')], ''),
]
WALK = [
    (0, None, ["'Your soup, buddy, enjoy your meal.' Let's focus on this part: ", ('barinov', 'приятного'), ('barinov', 'аппетита'), ' means enjoy your meal. ', ('barinov', 'дружище'), ' is a warm word for buddy. Barinov serves the man himself.']),
    (1, None, ["'Vitya, what are you doing?' Vika uses the short name Vitya. ", ('vika', 'ты'), ('vika', 'что'), ('vika', 'делаешь'), ' sounds like asking what on earth are you doing. She can see perfectly well what he is doing.']),
    (2, None, ["'I am doing what I must do.' Let's inspect this part: ", ('barinov', 'должен'), ' means must. Barinov answers calmly.']),
    (3, None, ["'But an important critic is sitting right there!' The particle in ", ('vika', 'там'), ('vika', 'же'), ' adds emphasis. ', ('vika', 'важный'), ('vika', 'критик'), ' means an important critic. Vika points at the table.']),
    (4, None, ["'I do not care who is sitting there.' We can focus on the speech: ", ('barinov', 'Мне'), ('barinov', 'всё'), ('barinov', 'равно'), ' is the idiom for not caring. Barinov is clear.']),
    (5, None, ["'This guest ordered soup earlier.' We will examine the sentence: ", ('barinov', 'раньше'), ' means earlier. ', ('barinov', 'заказал'), ('barinov', 'суп'), ' means ordered soup. The guest at the bar had ordered first, and for Barinov that settles it.']),
    (6, None, ["'The critic is very angry, he will leave!' We can inspect the words: ", ('vika', 'зол'), ' means angry. ', ('vika', 'уйдёт'), " means he will leave. Vika's voice is rising."]),
    (7, None, ["'Let him leave if he does not know how to wait.' Let us look at this part: ", ('barinov', 'Пусть'), ' means let him. ', ('barinov', 'умеет'), ' means knows how to. Barinov dares the critic to go.']),
    (8, None, ["'You are risking our restaurant's reputation.' Here you risk with something, so reputation changes form. ", ('vika', 'нашего'), ('vika', 'ресторана'), " means of our restaurant. This is Vika's real fear."]),
    (9, None, ["'Even if he were three times a critic!' Now we can consider the dialogue: ", ('barinov', 'будь'), ('barinov', 'он'), ' means even if he were. ', ('barinov', 'трижды'), ' means three times. Barinov exaggerates, and it is part of the charm.']),
    (10, None, ["'I serve all guests in turn.' Now let's inspect this line: ", ('barinov', 'подаю'), ' means I serve. ', ('barinov', 'всем'), ('barinov', 'гостям'), ' means to all guests. ', ('barinov', 'по'), ('barinov', 'очереди'), ' means in turn.']),
    (11, None, ["'In my kitchen everyone is equal!' Now let's analyze the sentence: ", ('barinov', 'равны'), ' means equal. ', ('barinov', 'У'), ('barinov', 'меня'), ('barinov', 'на'), ('barinov', 'кухне'), ' means in my kitchen. Barinov ends the argument on a principle.']),
]
