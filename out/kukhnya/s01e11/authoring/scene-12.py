# Authoring module for kukhnya-s01e11-scene-12.
ID = 'kukhnya-s01e11-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 12
TITLE = 'Второй критик  (The Second Critic)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "Barinov wants to know about the mystery man at table five, and he asks Nastya, who has been serving him. The answer makes him think of a second critic. Take it in once, and don't worry about the details."
OPENER = 'Now the same thing, but slowly.'
TRANSITION = 'Now put it all together.'
OUTRO = 'The chef now has two possible critics, and a lot to feed them. He sends the menu to the man. The next scene looks at this from another side. Bye for now.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Настя, давно у тебя этот гость?', 'Nastya, how long have you had this guest?', [(160, 'Давно у тебя этот гость?')], ''),
    ('nastya', 'Какой именно гость, шеф?', 'Which guest exactly, chef?', [(160, 'Какой гость?')], ''),
    ('barinov', 'Тот странный мужчина в тёмном пиджаке.', 'That strange man in the dark jacket.', [], ''),
    ('nastya', 'Можно сказать, довольно давно.', 'You could say, quite a long time.', [(161, 'Можно сказать, давно')], ''),
    ('barinov', 'Что он уже успел заказать?', 'What has he already managed to order?', [(162, 'Что он заказал?')], ''),
    ('nastya', 'Пока совершенно ничего, только воду.', 'Nothing at all so far, only water.', [(162, 'Пока ничего')], ''),
    ('nastya', 'Он всё время что-то пишет.', 'He is writing something the whole time.', [(162, 'он все время что-то пишет')], ''),
    ('barinov', 'Он что, известный писатель?', 'Is he some famous writer?', [(162, 'что')], ''),
    ('nastya', 'Вы же говорили про ту девушку!', 'But you were talking about that girl!', [], ''),
    ('barinov', 'Получается, у меня теперь два критика?', 'It turns out I have two critics now?', [], ''),
    ('nastya', 'Что мне теперь делать, шеф?', 'What should I do now, chef?', [], ''),
    ('barinov', 'Немедленно отнеси ему наше фирменное меню.', 'Immediately take him our signature menu.', [], ''),
    ('nastya', 'Я всё сделаю в лучшем виде.', 'I will do everything in the best way.', [], ''),
]
WALK = [
    (0, None, ["'Nastya, how long have you had this guest?' Russian has two ways to express long. ", ('barinov', 'давно'), ' looks back from now, and another word measures a stretch of time. Barinov asks ', ('barinov', 'давно'), ('barinov', 'у'), ('barinov', 'тебя'), '.']),
    (1, None, ["'Which guest exactly, chef?' The expression ", ('nastya', 'Какой'), ('nastya', 'именно'), ' means which exactly. The word ', ('nastya', 'именно'), ' is one Barinov used before. Nastya is not sure which guest he means.']),
    (2, None, ["'That strange man in the dark jacket.' The word ", ('barinov', 'тёмном'), ' is the dark in dark chocolate. The expression ', ('barinov', 'в'), ('barinov', 'тёмном'), ('barinov', 'пиджаке'), ' means in a dark jacket, changing the ending of the thing.']),
    (3, None, ["'You could say, quite a long time.' Now let's look at the dialogue: ", ('nastya', 'Можно'), ('nastya', 'сказать'), ' means you could say, based on it is possible. And ', ('nastya', 'довольно'), ('nastya', 'давно'), ' is rather long ago.']),
    (4, None, ["'What has he already managed to order?' The word ", ('barinov', 'успел'), ' means managed to, or had time to. It is the same action Lyova used earlier about managing everything in time.']),
    (5, None, ["'Nothing at all so far, only water.' Let's inspect the phrase: ", ('nastya', 'Пока'), ' is the expression that also means bye. The expression ', ('nastya', 'совершенно'), ('nastya', 'ничего'), ' means completely nothing, and ', ('nastya', 'воду'), ' takes an ending as the thing he ordered.']),
    (6, None, ["'He is writing something the whole time.' Add a short particle to a question word and it goes vague: what becomes ", ('nastya', 'что'), '-', ('nastya', 'то'), ', meaning something. We hear ', ('nastya', 'всё'), ('nastya', 'время'), ' means all the time.']),
    (7, None, ["'Is he some famous writer?' Now we can look at this line: ", ('barinov', 'известный'), ' means famous, or known. A writer is ', ('barinov', 'писатель'), ', based on the action to write. The expression ', ('barinov', 'Он'), ('barinov', 'что'), ' adds surprise.']),
    (8, None, ["'But you were talking about that girl!' The little particle ", ('nastya', 'же'), ' acts like a reminder. Notice ', ('nastya', 'про'), ('nastya', 'ту'), ('nastya', 'девушку'), ' means about that girl. Nastya points out what the chef said earlier.']),
    (9, None, ["'It turns out I have two critics now?' The word ", ('barinov', 'Получается'), ' is the usual way to say it turns out. After the number two, the word is ', ('barinov', 'критика'), '.']),
    (10, None, ["'What should I do now, chef?' Let's break down the phrase: ", ('nastya', 'Что'), ('nastya', 'мне'), ' asks what to do, using the plain form ', ('nastya', 'делать'), ' instead of needing should. Nastya asks for orders.']),
    (11, None, ["'Immediately take him our signature menu.' The command ", ('barinov', 'отнеси'), ' means take away to. Notice ', ('barinov', 'фирменное'), " means signature, familiar from Lyova's signature meat."]),
    (12, None, ["'I will do everything in the best way.' Now let's look at the sentence: ", ('nastya', 'в'), ('nastya', 'лучшем'), ('nastya', 'виде'), ' is the promise Lyova made to Barinov earlier. Nastya says it the same way.']),
]
