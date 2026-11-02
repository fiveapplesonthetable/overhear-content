# Authoring module for kukhnya-s01e13-scene-15.
ID = 'kukhnya-s01e13-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 15
TITLE = 'Разговор на складе  (Talk in the Stockroom)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = 'Vika goes into the stockroom and finds Max hiding among the boxes. She wants to talk to him about being sensible. Hear their talk in Russian first.'
OPENER = 'Again, slowly this time.'
TRANSITION = 'Now the stockroom talk, all the way through.'
OUTRO = "Vika tries to stay serious, and Max wins her over a little anyway. Note how she calls him a child, and then a romantic. Talk soon."
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Макс, почему ты снова прячешься здесь?', 'Max, why are you hiding here again?', [], ''),
    ('max', 'Я просто ждал тебя здесь.', 'I was simply waiting for you here.', [], ''),
    ('vika', 'Какой же ты всё-таки несерьёзный ребёнок!', 'What an unserious child you are!', [(211, 'все')], ''),
    ('max', 'Тогда строго накажи меня за это!', 'Then punish me strictly for that!', [(202, 'Тогда накажи меня.')], ''),
    ('vika', 'Макс, перестань шутить, я говорю серьёзно.', 'Max, stop joking, I am serious.', [(203, 'я не шучу.')], ''),
    ('vika', 'Ты молодой, тебе хочется веселья.', 'You are young, you want fun.', [(204, 'Я понимаю, что ты молодой, а тебе хочется веселиться.')], ''),
    ('vika', 'На работе надо быть взрослым человеком.', 'At work one must be an adult.', [(205, 'Но иногда надо быть серьезней.')], ''),
    ('max', 'Вика, почему ты так переживаешь?', 'Vika, why are you so worried?', [(205, 'что ты переживаешь')], ''),
    ('max', 'Разница в возрасте совсем не важна.', 'The age difference is not important.', [], ''),
    ('vika', 'Мне кажется, мы совершаем ошибку.', 'It seems we are making a mistake.', [], ''),
    ('max', 'Рядом со мной ты забудешь тревоги.', 'Beside me you will forget all worries.', [], ''),
    ('vika', 'Макс, ты просто неисправимый романтик.', 'Max, you are an incorrigible romantic.', [(211, 'просто')], ''),
    ('max', 'Потому что я очень люблю тебя, Вика.', 'Because I love you very much, Vika.', [], ''),
]
WALK = [
    (0, None, ["'Max, why are you hiding here again?' The ending in ", ('vika', 'прячешься'), " makes it 'hide yourself'. The term ", ('vika', 'снова'), " is a one-word 'again'."]),
    (1, None, ["'I was simply waiting for you here.' Russian says 'waited you', without 'for'. The verb ", ('max', 'ждал'), " is a man's past form, and ", ('max', 'тебя'), " is 'you'."]),
    (2, None, ["'What an unserious child you are!' The word ", ('vika', 'несерьёзный'), " is 'serious' with 'not' in front. Also, ", ('vika', 'ребёнок'), ' is one child, and the plural looks nothing like it.']),
    (3, None, ["'Then punish me strictly for that!' The verb ", ('max', 'накажи'), " is the order 'punish!'. The word ", ('max', 'строго'), ', strictly, is the adverb of strict, and ', ('max', 'за'), ('max', 'это'), " is 'for that'."]),
    (4, None, ["'Max, stop joking, I am serious.' The term ", ('vika', 'перестань'), " is 'stop', followed by ", ('vika', 'шутить'), ", 'to joke'. Notice ", ('vika', 'говорю'), ('vika', 'серьёзно'), ", I speak seriously, is how Russians say 'I mean it'."]),
    (5, None, ["'You are young, you want fun.' We will examine this line: ", ('vika', 'тебе'), ('vika', 'хочется'), " says 'to you it wants itself', so Russians say that a wish happens to you. Notice ", ('vika', 'веселья'), " means 'of fun', since 'want' brings that ending."]),
    (6, None, ["'At work one must be an adult.' The term ", ('vika', 'надо'), " is the impersonal 'one must'. After ", ('vika', 'быть'), ', to be, the wording ', ('vika', 'взрослым'), ('vika', 'человеком'), " has the endings for the 'as a' form."]),
    (7, None, ["'Vika, why are you so worried?' We can inspect the dialogue: ", ('max', 'переживаешь'), " is built from to live, and through. So to worry is to 'live through' something."]),
    (8, None, ["'The age difference is not important.' Max waves the whole subject away in one short sentence. Notice ", ('max', 'важна'), ", important, takes a woman's ending since ", ('max', 'Разница'), ', difference, is feminine.']),
    (9, None, ["'It seems we are making a mistake.' Let's inspect the phrase: ", ('vika', 'Мне'), ('vika', 'кажется'), " word-for-word means 'to me it seems', Russian for 'I think'. And Russians 'commit' a mistake, ", ('vika', 'совершаем'), ('vika', 'ошибку'), ', where English makes one.']),
    (10, None, ["'Beside me you will forget all worries.' The verb ", ('max', 'забудешь'), " is a future, 'you will forget'. Notice ", ('max', 'тревоги'), ', worries, is the plural of alarm or anxiety.']),
    (11, None, ["'Max, you are an incorrigible romantic.' The term ", ('vika', 'неисправимый'), " is made of 'not' and 'to fix or correct'. So it is 'unfixable'. The term ", ('vika', 'романтик'), ' is the English word.']),
    (12, None, ["'Because I love you very much, Vika.' Now let's focus on this part: ", ('max', 'Потому'), ('max', 'что'), " is 'because', and it is often how you answer 'why'. The verb ", ('max', 'люблю'), " is 'I love', and ", ('max', 'тебя'), ' is its object.']),
]
