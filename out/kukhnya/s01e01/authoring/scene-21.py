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
    (0, None, '\'Chef, the festive dessert is already ready!\' "Prazdnichnyy" comes from "prazdnik", holiday. "Gotov" is the short "ready", and it comes from the same root as "to cook".'),
    (1, None, '\'Attention everyone! The guest is tasting the newcomer\'s dish.\' A woman guest is "gost\'ya", the same word with a feminine ending. "Blyudo novichka" is "dish of newcomer", with a short "of" ending on "novichok" and no \'s.'),
    (2, None, '\'Come here, sweet little doggy! Taste the dessert.\' "Sobachka" is "sobaka", dog, with a small ending that makes it a pet name. "Milaya" is "sweet", the feminine of "milyy". "Poprobuy" is a command from "probovat\'", to try.'),
    (3, None, '\'She doesn\'t even look at the plate.\' A dog is "ona", she, because "sobachka" is a feminine word. "Smotret\' na" is "to look at", and "tarelku" takes -u.'),
    (4, None, '\'Chef, that is unfair! After all, it is a dog.\' "Nechestno" is "ne" plus "chestno", honestly, the word from "frankly speaking". "Eto zhe sobaka" has the "zhe" for "after all".'),
    (5, None, '\'The world is not ideal at all, young man.\' "Mir" means both "world" and "peace". "Ideal\'en" is the short form of "ideal\'nyy". The chef lectures Max with "young man".'),
    (6, None, '\'Let\'s make a bet, chef!\' "Davayte" is literally "give", but before another word it means "let\'s", and it\'s one of the most useful words in Russian. "Posporim" comes from "spor", an argument or bet.'),
    (7, None, '\'What will we bet about?\' "O chyom" is "about what", as before. "My budem sporit\'" is "we will bet", the future "will be" plus "to bet".'),
    (8, None, '\'An ordinary person will like my hot dish.\' "Obychnomu cheloveku" is "to an ordinary person", both words with the "to" ending, because the person is the one pleased. "Goryacheye" is "hot".'),
    (9, None, '\'Good! You will prepare a dish for me.\' "Dlya menya" is "for me". Where English has one "me", Russian has several forms, and this is the "for" one.'),
    (10, None, '\'If I like it, you stay here.\' "Yesli mne ponravitsya" is "if it pleases me". "Ostayosh\'sya" is "you stay", in the present, which Russians use for firm promises.'),
    (11, None, '\'If not, you will leave here forever.\' "Navsegda" is "na" plus "vsegda", always: forever. "Otsyuda" is "from here", the partner of "syuda", "to here".'),
    (12, None, '\'I agree to this bet!\' A man says "soglasen", and a woman would say "soglasna". "Na etot spor" is "to this bet".'),
    (13, None, '\'We will see what kind of cook you are!\' "Posmotrim" is "we will see". "Kakoy iz tebya povar" is literally "what from you cook", Russian for "what kind of cook you\'ll turn out to be".'),
]
