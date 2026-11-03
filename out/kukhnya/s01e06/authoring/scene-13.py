# Authoring module for kukhnya-s01e06-scene-13.
ID = 'kukhnya-s01e06-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 13
TITLE = 'Неожиданная находка  (An Unexpected Find)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'rodion': 'Родион'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Behind Claude Monet, Max and Kostya are digging through the bins. The 'rotten potatoes' they threw out were the chef's truffles, and now a very polite stranger called Rodion is holding the box. It's in Russian first."
OPENER = 'Let\'s go through the meeting. Max is in a hurry and says "ty", Rodion takes his time and says "vy".'
TRANSITION = 'Once more, the whole meeting by the bins.'
OUTRO = 'Digging through the bins behind Claude Monet only leads Max and Kostya to a remarkably courteous stranger, Rodion, who now holds both the truffles and all the leverage. See you next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Где ты нашёл эту коробку?', 'Where did you find this box?', [(182, 'не это ищете')], ''),
    ('rodion', 'Вы искали дорогие трюфели на помойке.', 'You were looking for expensive truffles in the trash.', [(182, 'Вы, случайно, не это ищете?')], ''),
    ('max', 'Пожалуйста, отдай их нам скорее обратно!', 'Please, give them back to us quickly!', [(183, 'А ну-ка, дай сюда!')], ''),
    ('rodion', 'Сначала представьтесь вежливо, молодой человек.', 'First introduce yourself politely, young man.', [(185, 'Как грубо!')], ''),
    ('max', 'Меня зовут Макс, а это Костя.', 'My name is Max, and this is Kostya.', [(186, 'позволь')], ''),
    ('rodion', 'Очень приятно, а я Родион Сергеевич.', 'Very pleased, and I am Rodion Sergeyevich.', [(186, 'Меня зовут Родион Сергеевич')], ''),
    ('max', 'Что ты хочешь за эти грибы?', 'What do you want for these mushrooms?', [(187, 'А трюфели в надежном месте')], ''),
    ('rodion', 'Мне нужна одна небольшая дружеская услуга.', 'I need one small friendly favor.', [(189, 'обмен на маленькую услугу')], ''),
    ('max', 'Мы можем заплатить тебе немного денег.', 'We can pay you a little money.', [(178, 'денег')], ''),
    ('rodion', 'Нет, я хочу роскошный обед здесь.', 'No, I want a luxurious lunch here.', [(169, 'нет')], ''),
    ('max', 'Но охранники не пустят тебя внутрь!', "But the guards won't let you inside!", [(190, 'Его не пустят в зал')], ''),
    ('rodion', 'Тогда найдите мне подходящую чистую одежду.', 'Then find me suitable clean clothes.', [(192, 'Я гражданин мира')], ''),
    ('max', 'Хорошо, пойдём скорее в нашу раздевалку.', "Alright, let's go quickly into our locker room.", [(193, 'Это шкафчик')], ''),
]
WALK = [
    (0, None, ["'Where did you find this box?' Max is demanding answers about the ", ('max', 'коробку'), ', the box they threw out earlier.']),
    (1, None, ["'You were looking for expensive truffles in the trash.' The polite stranger points toward the ", ('rodion', 'помойке'), ', meaning the trash or dump.']),
    (2, None, ["'Please, give them back to us quickly!' In a complete panic, he begs ", ('max', 'скорее'), ', to get it back quickly.']),
    (3, None, ["'First introduce yourself politely, young man.' He calmly asks them to act ", ('rodion', 'вежливо'), ', showing some basic polite manners.']),
    (4, None, ["'My name is Max, and this is Kostya.' Giving up the fight, he uses ", ('max', 'зовут'), ' to say what they call him.']),
    (5, None, ["'Very pleased, and I am Rodion Sergeyevich.' Meeting someone new usually starts with ", ('rodion', 'приятно'), ', meaning it is very pleasant.']),
    (6, None, ["'What do you want for these mushrooms?' Trying to strike a deal for ", ('max', 'грибы'), ', the expensive mushrooms they lost.']),
    (7, None, ["'I need one small friendly favor.' Instead of money, he requests an ", ('rodion', 'услуга'), ', a friendly favor from them.']),
    (8, None, ["'We can pay you a little money.' Hoping to just buy him off, ", ('max', 'заплатить'), ' means they will pay him.']),
    (9, None, ["'No, I want a luxurious lunch here.' The request is actually for a ", ('rodion', 'роскошный'), ' or luxurious lunch at their place.']),
    (10, None, ["'But the guards won't let you inside!' They are worried that the strict ", ('max', 'охранники'), ' standing guard will stop him.']),
    (11, None, ["'Then find me suitable clean clothes.' His solution is simply to find ", ('rodion', 'одежду'), ', some clean clothes to wear.']),
    (12, None, ["'Alright, let's go quickly into our locker room.' Sneaking him away into their staff ", ('max', 'раздевалку'), ', the locker room to change.']),
]
