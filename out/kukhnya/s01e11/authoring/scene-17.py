# Authoring module for kukhnya-s01e11-scene-17.
ID = 'kukhnya-s01e11-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 17
TITLE = 'Назойливый клиент  (The Pushy Customer)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "Nastya has a difficult customer at her table. He is the man who writes in a notebook, and he turns out to be pushy as well. Here's the Russian, from the top."
OPENER = "Let's go back to the beginning."
TRANSITION = 'Here is the full story once more.'
OUTRO = 'Nastya escapes to the kitchen, and the man stays at the table. She will tell Vika that he is a nuisance. Keep listening.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Что вы хотите заказать сегодня у нас?', 'What do you want to order with us today?', [(192, 'вы что-нибудь покушаете у нас?')], ''),
    ('guest', 'Принеси мне любое блюдо на твой вкус.', 'Bring me any dish to your taste.', [(193, 'на твое усмотрение')], ''),
    ('nastya', 'Хорошо, я выберу для вас лучшее.', 'Good, I will choose the best for you.', [(195, 'Хорошо')], ''),
    ('guest', 'А почему бы тебе не присесть рядом?', 'Why do you not take a seat nearby?', [(196, 'Может, ты присядешь?')], ''),
    ('nastya', 'Извините, но я сейчас на работе.', 'Excuse me, but I am at work right now.', [(197, 'Я вообще-то на работе')], ''),
    ('guest', 'Я твой клиент и плачу за всё.', 'I am your customer and I pay for everything.', [(198, 'Я твой клиент')], ''),
    ('nastya', 'Я обязана только приносить ваши блюда.', 'I am obliged only to bring your dishes.', [], ''),
    ('guest', 'Ты первая строила мне красивые глазки.', 'You were the first to make pretty eyes at me.', [(199, 'ты же первая начала мне строить глазки')], ''),
    ('nastya', 'Я просто вежливо улыбалась вам, как всем.', 'I was simply smiling politely at you, guest.', [(200, 'Я ничего не начинала')], ''),
    ('guest', 'Не уходи, посиди со мной немного.', 'Do not leave, sit with me a little.', [(199, 'Ну, не ломайся')], ''),
    ('nastya', 'Я не имею права сидеть здесь.', 'I do not have the right to sit here.', [], ''),
    ('guest', 'Ты должна выполнять любые мои просьбы.', 'You must fulfill any requests of mine.', [(198, 'ты должна выполнять все мои желания')], ''),
    ('nastya', 'Извините, я сейчас пойду на кухню.', 'Excuse me, I am going to the kitchen right now.', [(201, 'Извините')], ''),
]
WALK = [
    (0, None, ["'What do you want to order with us today?' Russians say ", ('nastya', 'у'), ('nastya', 'нас'), ', at us, for with us, meaning at our place. Nastya uses the polite form in ', ('nastya', 'Что'), ('nastya', 'вы'), ('nastya', 'хотите'), ('nastya', 'заказать'), '.']),
    (1, None, ["'Bring me any dish to your taste.' The man uses the informal form with a waitress, which is rude. ", ('guest', 'любое'), ' is any at all. ', ('guest', 'на'), ('guest', 'твой'), ('guest', 'вкус'), ' is to your taste.']),
    (2, None, ["'Good, I will choose the best for you.' We will look at the speech: ", ('nastya', 'выберу'), ' means I will choose, which is the verb Senya used when talking about choosing the best goods. ', ('nastya', 'лучшее'), ' is the best thing. Nastya keeps the polite form with ', ('nastya', 'для'), ('nastya', 'вас'), '.']),
    (3, None, ["'Why do you not take a seat nearby?' Let us analyze the words: ", ('guest', 'почему'), ('guest', 'бы'), ('guest', 'тебе'), ('guest', 'не'), " is why wouldn't you, a soft-sounding suggestion. ", ('guest', 'присесть'), ' is to sit down for a moment. ', ('guest', 'рядом'), ' is nearby.']),
    (4, None, ["'Excuse me, but I am at work right now.' Russians are ", ('nastya', 'на'), ('nastya', 'работе'), ', on work, not in it. ', ('nastya', 'Извините'), ' marks the polite excuse me, not the casual one. Nastya refuses gently.']),
    (5, None, ["'I am your customer and I pay for everything.' Let us look at the speech: ", ('guest', 'клиент'), ' is client. ', ('guest', 'плачу'), ('guest', 'за'), ('guest', 'всё'), ' is I pay for everything. The man says it as a threat.']),
    (6, None, ["'I am obliged only to bring your dishes.' Let's examine the phrase: ", ('nastya', 'обязана'), ' means obliged, and has a feminine ending. ', ('nastya', 'только'), ' means only, which is the term Louis used for only white. ', ('nastya', 'приносить'), ' is to bring.']),
    (7, None, ["'You were the first to make pretty eyes at me.' The idiom is to build little eyes, meaning to flirt, using ", ('guest', 'строила'), ' and ', ('guest', 'глазки'), '. ', ('guest', 'первая'), ' means first, and has a feminine ending. It is an accusation.']),
    (8, None, ["'I was simply smiling politely at you, guest.' We can break down this part: ", ('nastya', 'улыбалась'), ' means was smiling, with a feminine ending. ', ('nastya', 'как'), ('nastya', 'всем'), ' is as to everyone, meaning the smile is part of the job.']),
    (9, None, ["'Do not leave, sit with me a little.' Let us break down the sentence: ", ('guest', 'Не'), ('guest', 'уходи'), " is don't go away. ", ('guest', 'посиди'), ' is sit a while, with a prefix for a short stay. ', ('guest', 'со'), ('guest', 'мной'), ' is with me.']),
    (10, None, ["'I do not have the right to sit here.' Now we can break down the sentence: ", ('nastya', 'не'), ('nastya', 'имею'), ('nastya', 'права'), ' uses a formal verb for have that is rare in everyday speech. The word for right becomes ', ('nastya', 'права'), ' after the negative.']),
    (11, None, ["'You must fulfill any requests of mine.' We will break down the sentence: ", ('guest', 'должна'), ' means must, and has a feminine ending, since he is addressing her. ', ('guest', 'просьбы'), ' means requests.']),
    (12, None, ["'Excuse me, I am going to the kitchen right now.' Let us examine the speech: ", ('nastya', 'Извините'), ' is used again, with the polite form. ', ('nastya', 'пойду'), ' is I will go. ', ('nastya', 'на'), ('nastya', 'кухню'), ' is onto the kitchen.']),
]
