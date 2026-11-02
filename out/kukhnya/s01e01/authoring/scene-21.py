# Authoring module for kukhnya-s01e01-scene-21.
ID = 'kukhnya-s01e01-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 21
TITLE = 'Пари на кухне  (A Bet in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "Max proudly shows off his festive dessert, and the guest who is supposed to taste it turns out to be Eleonora Andreyevna, a dog. She won't even look at it. Max is furious at the unfairness, and ends up challenging the chef to a bet. Here is the Russian first."
OPENER = 'Back to the kitchen, slowly.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So the stakes are set: one dish, one taster, and Max\'s job on the line. Remember "let\'s bet" and "I agree", the two phrases that start the whole wager.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Шеф, праздничный десерт уже готов!', 'Chef, the festive dessert is already ready!', [(244, 'Десерт'), (244, 'готов')], ''),
    ('barinov', 'Все внимание! Гостья пробует блюдо новичка.', "Attention everyone! The guest is tasting the newcomer's dish.", [(245, 'Все внимание'), (246, 'будет пробовать')], ''),
    ('barinov', 'Иди сюда, милая собачка! Попробуй десерт.', 'Come here, sweet little doggy! Taste the dessert.', [(251, 'Ко мне'), (252, 'Прошу')], ''),
    ('barinov', 'Она даже не смотрит на тарелку.', "She doesn't even look at the plate.", [(253, 'не жрет')], ''),
    ('max', 'Шеф, это нечестно! Это же собака.', 'Chef, that is unfair! After all, it is a dog.', [(255, 'Шеф, ну так нечестно'), (255, 'это же собака')], ''),
    ('barinov', 'Мир вообще не идеален, молодой человек.', 'The world is not ideal at all, young man.', [(256, 'мир не идеален')], ''),
    ('max', 'Давайте поспорим, шеф!', "Let's make a bet, chef!", [(259, 'давайте поспорим')], ''),
    ('barinov', 'О чём мы будем спорить?', 'What will we bet about?', [(260, 'Чего')], ''),
    ('max', 'Обычному человеку понравится моё горячее блюдо.', 'An ordinary person will like my hot dish.', [(261, 'простой нормальный человек'), (261, 'понравится мое блюдо')], ''),
    ('barinov', 'Хорошо! Ты приготовишь блюдо для меня.', 'Good! You will cook a dish for me.', [(262, 'Давай поспорим'), (263, 'Ты приготовишь блюдо для меня')], ''),
    ('barinov', 'Если мне понравится, ты остаёшься здесь.', 'If I like it, you stay here.', [(264, 'Если мне понравится, ты'), (264, 'остаешься')], ''),
    ('barinov', 'Если нет, ты уйдёшь отсюда навсегда.', 'If not, you will leave here forever.', [(265, 'Если выиграю я'), (265, 'ты уйдешь отсюда')], ''),
    ('max', 'Я согласен на этот спор!', 'I agree to this bet!', [(266, 'Согласен')], ''),
    ('barinov', 'Посмотрим, какой из тебя повар!', 'We will see what kind of cook you are!', [(274, 'Папочка готовить будет')], ''),
]
WALK = [
    (0, None, ['\'Chef, the festive dessert is already ready!\' ', ('max', 'Праздничный'), ' comes from the word for a holiday. ', ('max', 'Уже готов'), ' is "already ready", which sounds clumsy in English but perfectly normal in Russian.']),
    (1, None, ['\'Attention everyone! The guest is tasting the newcomer\'s dish.\' A woman guest is ', ('barinov', 'гостья'), ', the same word with a feminine ending. ', ('barinov', 'Блюдо новичка'), ' is "dish of newcomer", with a short "of" ending on the word for newcomer and no \'s.']),
    (2, None, ['\'Come here, sweet little doggy! Taste the dessert.\' ', 'The word for doggy is the word for dog with a small ending that makes it a pet name. ', ('barinov', 'Милая'), ' is "sweet", the feminine of the word for sweet. ', ('barinov', 'Попробуй'), ' is a command from the verb to try.']),
    (3, None, ['\'She doesn\'t even look at the plate.\' A dog is ', ('barinov', 'она'), ', she, because the word for doggy is a feminine word. The verb means "to look at", and ', ('barinov', 'тарелку'), ' takes -u.']),
    (4, None, ['\'Chef, that is unfair! After all, it is a dog.\' ', ('max', 'Нечестно'), ' is ', ('max', 'не'), ' plus ', ('max', 'честно'), ', honestly, the word from "frankly speaking". ', ('max', 'Это же собака'), ' has the ', ('max', 'же'), ' for "after all".']),
    (5, None, ['\'The world is not ideal at all, young man.\' ', ('barinov', 'Мир'), ' means both "world" and "peace". ', ('barinov', 'Идеален'), ' is the short form of the word for ideal, the shape Russian uses after "is".']),
    (6, None, ['\'Let\'s make a bet, chef!\' ', ('max', 'Давайте'), ' means "give", but before another verb it means "let\'s", and it\'s one of the most useful words in Russian. ', ('max', 'Поспорим'), ' comes from ', ('max', 'спор'), ', an argument or bet.']),
    (7, None, ['\'What will we bet about?\' ', ('barinov', 'О чём'), ' is "about what", as before. ', ('barinov', 'Мы будем спорить'), ' is "we will bet", the future "will be" plus "to bet".']),
    (8, None, ['\'An ordinary person will like my hot dish.\' ', ('max', 'Обычному человеку'), ' is "to an ordinary person", both words with the "to" ending, because the person is the one pleased. ', ('max', 'Горячее'), ' is "hot".']),
    (9, None, ['\'Good! You will prepare a dish for me.\' ', ('barinov', 'Для меня'), ' is "for me". Where English has one "me", Russian has several forms, and this is the "for" one.']),
    (10, None, ['\'If I like it, you stay here.\' Russian turns liking around: ', ('barinov', 'мне понравится'), ' is "it will please me", so the dish is the subject and Barinov is "to me". Then ', ('barinov', 'остаёшься'), ', you stay, is in the present, which makes the promise sound settled.']),
    (11, None, ['\'If not, you will leave here forever.\' ', ('barinov', 'Навсегда'), ' is ', ('barinov', 'на'), ' plus ', ('barinov', 'всегда'), ', always: forever. ', ('barinov', 'Отсюда'), ' is "from here", the partner of ', ('barinov', 'сюда'), ', "to here".']),
    (12, None, ['\'I agree to this bet!\' A man says ', ('max', 'согласен'), ', and a woman would use a different ending. ', ('max', 'На этот спор'), ' is "to this bet".']),
    (13, None, ['\'We will see what kind of cook you are!\' ', ('barinov', 'Посмотрим'), ' is "we will see". ', ('barinov', 'Какой из тебя повар'), ' is literally "what from you cook", Russian for "what kind of cook you\'ll turn out to be".']),
]
