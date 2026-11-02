# Authoring module for kukhnya-s01e01-scene-25.
ID = 'kukhnya-s01e01-scene-25'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 25
TITLE = 'Второй шанс  (A Second Chance)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "It's late. The restaurant is closing, and Max is still standing in the kitchen, waiting to be thrown out. Instead, Chef Barinov gives him an unexpected order, and Max wonders why the chef changed his mind. A kitchen helper called Ainura asks the same question. Here it is in Russian first."
OPENER = "Let's go back through the chef's decision."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max has a second chance, even if the chef's motives are not noble. Now that you've met this chef, you can see why his bets drive the story."
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Огузок, ты всё ещё здесь стоишь?', 'Oguzok, are you still standing here?', [(356, 'ты еще здесь?')], ''),
    ('max', 'Шеф, пожалуйста, не надо меня больше унижать.', 'Chef, please, do not humiliate me anymore.', [(357, 'Шеф, я все понял, не надо меня больше унижать.')], ''),
    ('barinov', 'Завтра утром приходи на работу вовремя.', 'Tomorrow morning come to work on time.', [], ''),
    ('max', 'Вы меня оставляете работать в ресторане?', 'Are you letting me stay to work in the restaurant?', [(360, 'Вы меня оставляете?')], ''),
    ('max', 'Шеф, но почему вы передумали?', 'Chef, but why did you change your mind?', [(360, 'Ну почему?')], ''),
    ('barinov', 'Не задавай глупых вопросов, а то передумаю!', "Do not ask foolish questions, or I'll change my mind!", [(361, 'я тебя точно уволю.')], ''),
    ('ainura', 'Шеф, вы правда его оставляете?', 'Chef, are you really letting him stay?', [(362, 'Шеф, вы что, его оставляете?')], ''),
    ('barinov', 'Я поспорил, что он сбежит сам!', 'I bet that he will run away on his own!', [(363, 'он сбежит сам.')], ''),
    ('barinov', 'Через неделю этот парень сам уйдёт.', 'In a week this guy will leave on his own.', [(363, 'что через неделю')], ''),
    ('max', 'Каждый человек имеет право на шанс.', 'Every person has the right to a chance.', [(365, 'Каждый человек имеет право на второй шанс.')], ''),
    ('max', 'Некоторым сама жизнь даёт второй шанс.', 'To some, life itself gives a second chance.', [(367, 'Некоторым сама жизнь дает второй шанс.')], ''),
    ('max', 'Я обязательно докажу своё кулинарное мастерство.', 'I will definitely prove my culinary mastery.', [], ''),
    ('max', 'В общем, наша жизнь полна сюрпризов.', 'In short, our life is full of surprises.', [(369, 'В общем, жизнь...'), (370, 'Полна сюрпризов.')], ''),
    ('max', 'И главное приключение ещё только начинается!', 'And the main adventure is only just beginning!', [], ''),
]
WALK = [
    (0, None, ['\'Oguzok, are you still standing here?\' The chef uses his butcher\'s nickname for Max again. ', ('barinov', 'Всё ещё'), ', literally "all still", is the everyday Russian for "still".']),
    (1, None, ['\'Chef, please, do not humiliate me anymore.\' ', ('max', 'Не надо'), ' is "not necessary", the Russian way to say "don\'t". ', ('max', 'Унижать'), ' is "to humiliate", from ', ('max', 'ниж'), ', low: to make someone low.']),
    (2, None, ['\'Tomorrow morning come to work on time.\' Times of day work like adverbs: ', ('barinov', 'утром'), ', in the morning, is just ', ('barinov', 'утро'), ' with an ', ('barinov', '-ом'), ' ending, so ', ('barinov', 'завтра утром'), ' is tomorrow morning. ', ('barinov', 'Вовремя'), ', on time, is written as one word; split in two, it means "during".']),
    (3, None, ['\'Are you letting me stay to work in the restaurant?\' ', ('max', 'Оставляете'), ' is "you leave", used for "you keep". Max says ', ('max', 'вы'), ' to his boss, and ', ('max', 'меня'), ' is "me".']),
    (4, None, ['\'Chef, but why did you change your mind?\' ', ('max', 'Передумали'), ' is ', ('max', 'пере-'), ', over, plus ', ('max', 'думал'), ', to think: to think again. It ends in ', ('max', '-ли'), ' because Max says ', ('max', 'вы'), '.']),
    (5, None, ['\'Do not ask foolish questions, or I\'ll change my mind!\' ', ('barinov', 'А то'), ' is "or else", literally "and that". ', ('barinov', 'Передумаю'), ' is "I will change my mind", one word.']),
    (6, None, ['\'Chef, are you really letting him stay?\' ', ('ainura', 'Правда'), ' is "truth", used for "really". ', ('ainura', 'Его'), ' is "him", and Ainura says ', ('ainura', 'вы'), ' to the chef.']),
    (7, None, ['\'I bet that he will run away on his own!\' ', ('barinov', 'Поспорил'), ' is "I bet", the family of ', ('barinov', 'поспори'), ', "let\'s bet". ', ('barinov', 'Сбежит'), ' is "will run away", from ', ('barinov', 'бежи'), ', to run, and ', ('barinov', 'сам'), ' is "on his own".']),
    (8, None, ['\'In a week this guy will leave on his own.\' ', ('barinov', 'Через неделю'), ' is "through a week", for "in a week". ', ('barinov', 'Парень'), ' is the casual "guy", and ', ('barinov', 'уйдёт'), ' is "will leave".']),
    (9, None, ['\'Every person has the right to a chance.\' ', ('max', 'Имеет право'), ' is "has the right", using the formal ', ('max', 'имеет'), ' for "has". ', ('max', 'Право'), ' also means "law".']),
    (10, None, ['\'To some, life itself gives a second chance.\' Who gets the chance comes first: ', ('max', 'некоторым'), ', "to some", is in the "to" form, and the giver, ', ('max', 'сама жизнь'), ', life itself, follows. ', ('max', 'Сама'), ' is feminine because ', ('max', 'жизнь'), ' is a feminine word, even though it ends in a soft sign.']),
    (11, None, ['\'I will definitely prove my culinary mastery.\' ', ('max', 'Обязательно'), ' is "definitely", from ', ('max', 'обязательн'), ', obligatory. ', ('max', 'Мастерство'), ' has ', ('max', 'мастер'), ' inside it, as in ', ('max', 'мастер'), '.']),
    (12, None, ['\'In short, our life is full of surprises.\' ', ('max', 'В общем'), ' is "in general", family of ', ('max', 'общем'), ' in "a lot in common". ', ('max', 'Полна'), ' is the feminine "full", to match ', ('max', 'жизнь'), '.']),
    (13, None, ['\'And the main adventure is only just beginning!\' ', ('max', 'Начинается'), ', "is beginning", carries ', ('max', '-ся'), ' because the adventure begins by itself, with nobody starting it. ', ('max', 'Только'), ' with ', ('max', 'ещё'), ' is "only just".']),
]
