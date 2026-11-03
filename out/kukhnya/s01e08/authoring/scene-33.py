# Authoring module for kukhnya-s01e08-scene-33.
ID = 'kukhnya-s01e08-scene-33'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 33
TITLE = 'Право на ошибку  (The Right to Make Mistakes)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "After a hard evening at Claude Monet, Kostya, one of the cooks, is still upset about the chef shouting at him. Max, his friend, cheers him up with a little speech about why mistakes are useful. Here it is in Russian first."
OPENER = "Let's go through the pep talk. Kostya worries, and Max has an answer for everything."
TRANSITION = "Now the full conversation once more."
OUTRO = "Max's idea is that mistakes help you find 'the right path' — a reassuring thought for a young cook and for anyone learning a new language. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('kostya', 'Макс, я сегодня натворил глупостей.', 'Max, I did stupid things today.', [], ''),
    ('max', 'Не переживай, все повара делают ошибки.', 'Do not worry, all cooks make mistakes.', [], ''),
    ('kostya', 'Но шеф так громко на меня кричал!', 'But the chef shouted so loudly at me!', [], ''),
    ('max', 'Мы не можем не совершать разные ошибки.', 'We cannot help making various mistakes.', [(363, 'Мы не можем не совершать ошибки.')], ''),
    ('kostya', 'Ты правда думаешь, что это нормально?', 'Do you really think that this is normal?', [], ''),
    ('max', 'Ошибки — это важная часть нашей жизни.', 'Mistakes are an important part of our life.', [(364, 'Они часть нашей жизни.')], ''),
    ('kostya', 'И чему же они могут нас научить?', 'And what can they teach us?', [], ''),
    ('max', 'Они помогают нам найти правильный путь.', 'They help us find the right path.', [(365, 'А самое главное, они помогают найти нам правильный путь.')], ''),
    ('kostya', 'Значит, каждый промах делает нас сильнее?', 'So every blunder makes us stronger?', [], ''),
    ('max', 'Именно так мы становимся настоящими мастерами.', 'That is precisely how we become true masters.', [], ''),
    ('kostya', 'Тогда я больше не буду сильно расстраиваться.', 'Then I will not be so upset anymore.', [], ''),
    ('max', 'Главное — помнить свои уроки и двигаться вперёд.', 'The main thing is to remember your lessons and move forward.', [], ''),
    ('kostya', 'Спасибо за поддержку, ты отличный друг.', 'Thank you for the support, you are a great friend.', [], ''),
    ('max', 'Завтра мы покажем на кухне высший класс!', 'Tomorrow we will show top class in the kitchen!', [], ''),
]
WALK = [
    (0, None, ["'Max, I did stupid things today.' In the beginning of the conversation we hear ", ('kostya', 'натворил'), ' which is a fun way to say you made a mess of things.']),
    (1, None, ["'Do not worry, all cooks make mistakes.' To reassure his friend, Max mentions all the ", ('max', 'повара'), ' to remind him that every cook makes mistakes.']),
    (2, None, ["'But the chef shouted so loudly at me!' The memory of the chef yelling so ", ('kostya', 'громко'), ' is still bothering Kostya, since nobody likes loud shouting.']),
    (3, None, ["'We cannot help making various mistakes.' People often make mistakes, and they can be quite ", ('max', 'разные'), ' meaning all sorts of different kinds.']),
    (4, None, ["'Do you really think that this is normal?' Wondering if this is actually true, the word ", ('kostya', 'правда'), ' is used here to ask if Max really means it.']),
    (5, None, ["'Mistakes are an important part of our life.' Our day to day experience is captured by the word ", ('max', 'жизни'), ' which simply means life in this context.']),
    (6, None, ["'And what can they teach us?' Finding out what mistakes can actually ", ('kostya', 'научить'), ' us is the whole point of this interesting question about learning.']),
    (7, None, ["'They help us find the right path.' Discovering the correct way forward involves finding the right ", ('max', 'путь'), ' or path to take in the future.']),
    (8, None, ["'So every blunder makes us stronger?' Every time we mess up we become a bit ", ('kostya', 'сильнее'), ' which means stronger and better equipped for the next challenge.']),
    (9, None, ["'That is precisely how we become true masters.' True experts are forged through practice, and being ", ('max', 'настоящими'), ' implies they are genuine and authentic masters of their craft.']),
    (10, None, ["'Then I will not be so upset anymore.' Feeling down and being upset is described by the long word ", ('kostya', 'расстраиваться'), ' which Kostya promises he will try not to do anymore.']),
    (11, None, ["'The main thing is to remember your lessons and move forward.' Moving on and looking to the future means pushing ", ('max', 'вперёд'), ' without getting stuck on past failures.']),
    (12, None, ["'Thank you for the support, you are a great friend.' Having someone to lean on makes for an ", ('kostya', 'отличный'), ' or excellent friend when times are tough.']),
    (13, None, ["'Tomorrow we will show top class in the kitchen!' Showing off top level skills requires delivering the absolute ", ('max', 'высший'), ' or highest class of performance possible.']),
]
