# Authoring module for kukhnya-s01e08-scene-29.
ID = 'kukhnya-s01e08-scene-29'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 29
TITLE = 'Пари между шефами  (Bet Between the Chefs)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "The service is over. Barinov sits down with Elena Pavlovna, the chef from the rival restaurant, to enjoy winning their bet: she couldn't run his kitchen. Elena does not take it lying down. Here it is in Russian first."
OPENER = "Let's go through the gloating. Barinov is triumphant, and Elena has her own view."
TRANSITION = "Now the whole showdown in one go."
OUTRO = "Elena concedes politely while still claiming her prize: 'you owe me an excellent dinner'. Notice how one Russian word does the work of both 'owe' and 'must'. See you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Что и требовалось доказать, Елена Павловна!', 'That proves my point, Elena Pavlovna!', [(343, 'Что и требовалось доказать.')], ''),
    ('barinov', 'Я снова оказался абсолютно прав сегодня.', 'I turned out absolutely right again today.', [(344, 'Я говорю, что я оказался прав.')], ''),
    ('barinov', 'Впрочем, как и всегда, я выиграл пари!', 'As always, I won the bet!', [(345, 'Впрочем, как и всегда. Я выиграл парень.')], ''),
    ('elena', 'Виктор, прекратите говорить эту глупую ерунду.', 'Viktor, stop talking this silly nonsense.', [(346, 'Да не говорите ерунду.')], ''),
    ('elena', 'Я проработала на вашей кухне целый день.', 'I worked in your kitchen the whole day.', [(347, 'Я проработала у вас на кухне целый день')], ''),
    ('elena', 'Сначала всё было совершенно спокойно и нормально.', 'At first everything was completely calm and normal.', [(347, 'и все было нормально.')], ''),
    ('elena', 'А потом все повара словно заболели!', 'And then all the cooks seemed to get sick!', [(348, 'что-то случилось'), (349, 'Все как будто заболели.')], ''),
    ('elena', 'У вас на кухне работают сплошные инвалиды!', 'You have nothing but cripples working in your kitchen!', [(350, 'У вас не повара, а инвалиды.')], ''),
    ('barinov', 'Правильно, но это мои родные люди!', 'Right, but these are my own people!', [(351, 'Правильно.'), (352, 'Но это мои инвалиды.')], ''),
    ('barinov', 'И только я имею право их ругать.', 'And only I have the right to scold them.', [(352, 'И только я имею право их так называть.')], ''),
    ('barinov', 'Работа шефа — сделать из них команду!', "The chef's job is to make a team out of them!", [(353, 'И разве не в этом состоит работа шефа?'), (354, 'высококлассную команду?')], ''),
    ('elena', 'Вы умеете красиво оправдать любой беспорядок.', 'You know how to beautifully justify any mess.', [], ''),
    ('elena', 'Шеф, вы мне должны отличный ужин!', 'Chef, you owe me a great dinner!', [(355, 'А? Шеф?'), (356, 'Вы мне ужин должны.')], ''),
]
WALK = [
    (0, None, ["'That proves my point, Elena Pavlovna!' To wrap up a mathematical proof, you might use the phrase containing ", ('barinov', 'доказать'), ', which literally means to prove.']),
    (1, None, ["'I turned out absolutely right again today.' When a situation ends up being true, the word ", ('barinov', 'оказался'), ' captures the idea of how it turned out.']),
    (2, None, ["'As always, I won the bet!' Borrowed from French, the term for a wager is ", ('barinov', 'пари'), ', and it keeps its shape no matter how it fits into the sentence.']),
    (3, None, ["'Viktor, stop talking this silly nonsense.' Pushing back against his smugness, she calls his talk ", ('elena', 'ерунду'), ', a dismissive word for nonsense or rubbish.']),
    (4, None, ["'I worked in your kitchen the whole day.' Because she spent a continuous block of time doing the job, the word for working stretches into ", ('elena', 'проработала'), ' to reflect that endurance.']),
    (5, None, ["'At first everything was completely calm and normal.' Opening her side of the story, she uses ", ('elena', 'Сначала'), ' to mean at the beginning, setting up a contrast with what happened later.']),
    (6, None, ["'And then all the cooks seemed to get sick!' Comparing the situation to a sudden outbreak, she drops in ", ('elena', 'словно'), ' to mean as if or like.']),
    (7, None, ["'You have nothing but cripples working in your kitchen!' Describing an unbroken or continuous state, the word ", ('elena', 'сплошные'), ' emphasizes that she sees absolutely nothing but incompetence.']),
    (8, None, ["'Right, but these are my own people!' Flipping her insult into a point of pride, he calls them ", ('barinov', 'родные'), ", meaning kin or one's own family."]),
    (9, None, ["'And only I have the right to scold them.' Claiming exclusive privilege to yell at his team, he brings up his ", ('barinov', 'право'), ', which translates to a legal or moral right.']),
    (10, None, ["'The chef's job is to make a team out of them!' The goal is to build or construct something new out of the raw material, so he uses ", ('barinov', 'сделать'), ' for making or producing.']),
    (11, None, ["'You know how to beautifully justify any mess.' Hidden inside the term for justifying, ", ('elena', 'оправдать'), ', is the idea of truth, since he always manages to make his chaos sound correct.']),
    (12, None, ["'Chef, you owe me a great dinner!' Since it covers both owing a debt and being obliged to do something, she lands heavily on ", ('elena', 'должны'), ' to demand her prize.']),
]
