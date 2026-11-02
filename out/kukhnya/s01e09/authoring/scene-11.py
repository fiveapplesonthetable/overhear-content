# Authoring module for kukhnya-s01e09-scene-11.
ID = 'kukhnya-s01e09-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 11
TITLE = 'Игра в Рататуя  (Playing Ratatouille)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'alisa': 'Алиса', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "Max and Alisa have found a quiet corner of the kitchen and a game: they are decorating a cake and pretending to be characters from a cartoon about a cooking rat. Meanwhile, the rest of the restaurant has begun to wonder where the chef's daughter has gone. Here they are, in Russian."
OPENER = "Let's go through it again, line by line."
TRANSITION = 'And now without my interruptions.'
OUTRO = 'Nastya has told them the chef is looking for Alisa, and the game is over for now. Next, the search begins. See you next time.'
CLOSING = ('max', 'Пока')
STORY = [
    ('max', 'Остался самый последний штрих.', 'Only the very last touch remains.', [(245, 'Остался последний штрих')], ''),
    ('alisa', 'Смотри, я сама это приготовила!', 'Look, I made this myself!', [(248, 'И я это приготовил!')], ''),
    ('max', 'Это я управляю тобой, как в мультике!', 'It is I who control you, like in the cartoon!', [(249, 'Не ты, а я управляю тобой!'), (250, 'Как в мультике «Рататуйя»!')], ''),
    ('alisa', 'То есть ты хитрая маленькая крыса?', 'So you are a clever little rat?', [(251, 'То есть ты крыса? Уи!')], ''),
    ('max', 'Художники всегда подписывают свой шедевр.', 'Artists always sign their masterpiece.', [(253, 'Что делают художники, когда заканчивают свой шедевр?'), (255, 'Ну, ставят автограф!')], ''),
    ('max', 'Куда пропал наш жидкий шоколад?', 'Where has our liquid chocolate gone?', [(256, 'Где мой жидкий шоколад?')], ''),
    ('alisa', 'Ты сам его только что съел!', 'You ate it yourself just now!', [(257, 'Ты сожрал?'), (258, 'Не я, а ты')], ''),
    ('max', 'Неправда, я оставил его для украшения.', 'Not true, I left it for decoration.', [], ''),
    ('nastya', 'Макс, ты не видел маленькую Алису?', 'Max, have you not seen little Alisa?', [(262, 'Настя, что там у вас?'), (263, 'Алисы нигде нет')], ''),
    ('max', 'Она сидит здесь и помогает мне.', 'She is sitting here helping me.', [], ''),
    ('nastya', 'Шеф уже ищет её по всему ресторану!', 'The chef is already looking for her all over the restaurant!', [(259, 'ее нигде нет'), (261, 'Ищи!')], ''),
    ('alisa', 'Мы готовим самое вкусное блюдо на свете!', 'We are cooking the most delicious dish in the world!', [], ''),
    ('nastya', 'Беги скорее к папе, пока он добрый.', 'Run to dad quickly, while he is kind.', [], ''),
]
WALK = [
    (0, None, ["'Only the very last touch remains.' Max is applying the final ", ('max', 'штрих'), ', a borrowed word meaning a stroke of a pen or brush.']),
    (1, None, ["'Look, I made this myself!' Notice how Alisa proudly uses ", ('alisa', 'сама'), ', showing she did it entirely on her own.']),
    (2, None, ["'It is I who control you, like in the cartoon!' Max talks about a ", ('max', 'мультике'), ', which is a cozy short form for an animated show.']),
    (3, None, ["'So you are a clever little rat?' She jokingly calls him a ", ('alisa', 'крыса'), ', treating him like the clever rodent from the movie.']),
    (4, None, ["'Artists always sign their masterpiece.' When completing his great work, Max mentions his ", ('max', 'шедевр'), ', which comes directly from the French phrase for a great piece of art.']),
    (5, None, ["'Where has our liquid chocolate gone?' Since the sweet treat has vanished, Max asks ", ('max', 'Куда'), ', the exact word used for asking where something went rather than where it is.']),
    (6, None, ["'You ate it yourself just now!' Alisa points out that he recently ", ('alisa', 'съел'), ' the whole thing, finishing the action entirely.']),
    (7, None, ["'Not true, I left it for decoration.' Denying the accusation completely, Max starts with ", ('max', 'Неправда'), ", squishing the words for 'not' and 'truth' together."]),
    (8, None, ["'Max, have you not seen little Alisa?' Nastya is searching and calls out for ", ('nastya', 'Алису'), ', altering the shape of the name since she is the target of the search.']),
    (9, None, ["'She is sitting here helping me.' Max explains that his new assistant ", ('max', 'помогает'), ' him with the important work they are doing together.']),
    (10, None, ["'The chef is already looking for her all over the restaurant!' Nastya warns them that he is currently ", ('nastya', 'ищет'), ' the missing girl everywhere he can.']),
    (11, None, ["'We are cooking the most delicious dish in the world!' The proud girl boasts about their ", ('alisa', 'вкусное'), ' creation, completely unaware of any trouble brewing outside.']),
    (12, None, ["'Run to dad quickly, while he is kind.' Giving some practical advice, Nastya tells them to go ", ('nastya', 'пока'), ' the boss is still in a good mood.']),
]
