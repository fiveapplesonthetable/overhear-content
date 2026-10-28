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
    ('barinov', 'Огузок, ты всё ещё здесь стоишь?', 'Runt, are you still standing here?', [(356, 'ты еще здесь?')], ''),
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
    (0, None, '\'Runt, are you still standing here?\' "Oguzok" is the chef\'s nickname for Max, a cut of meat from the rear of the animal. "Vsyo yeshchyo" is "all still", Russian for "still".'),
    (1, None, '\'Chef, please, do not humiliate me anymore.\' "Ne nado" is "not necessary", the Russian way to say "don\'t". "Unizhat\'" is "to humiliate", from "nizkiy", low: to make someone low.'),
    (2, None, '\'Tomorrow morning come to work on time.\' "Zavtra utrom" is "tomorrow in the morning". "Prikhodi" is "come" for something that repeats. "Vovremya" is "on time".'),
    (3, None, '\'Are you letting me stay to work in the restaurant?\' "Ostavlyayete" is "you leave", used for "you keep". Max says "vy" to his boss, and "menya" is "me".'),
    (4, None, '\'Chef, but why did you change your mind?\' "Peredumali" is "pere-", over, plus "dumat\'", to think: to think again. It ends in "-li" because Max says "vy".'),
    (5, None, '\'Do not ask foolish questions, or I\'ll change my mind!\' "A to" is "or else", literally "and that". "Peredumayu" is "I will change my mind", one word.'),
    (6, None, '\'Chef, are you really letting him stay?\' "Pravda" is "truth", used for "really". "Yego" is "him", and Ainura says "vy" to the chef.'),
    (7, None, '\'I bet that he will run away on his own!\' "Poporil" is "bet", the family of "posporim". "Sbezhit" is "will run away", from "bezhat\'", to run. "Sam" is "himself".'),
    (8, None, '\'In a week this guy will leave on his own.\' "Cherez nedelyu" is "through a week", for "in a week". "Paren\'" is the casual "guy", and "uydyot" is "will leave".'),
    (9, None, '\'Every person has the right to a chance.\' "Imeyet pravo" is "has the right", with the formal "imet\'" for "have". "Pravo" also means "law".'),
    (10, None, '\'To some, life itself gives a second chance.\' "Nekotorym" is "to some". "Sama zhizn\'" is "life itself", with "sama" the feminine of "sam". "Vtoroy" is "second".'),
    (11, None, '\'I will definitely prove my culinary mastery.\' "Obyazatel\'no" is "definitely", from "obyazatel\'nyy", obligatory. "Masterstvo" has "master" inside it, as in "mastera".'),
    (12, None, '\'In short, our life is full of surprises.\' "V obshchem" is "in general", family of "obshchego" in "a lot in common". "Polna" is the feminine "full", to match "zhizn\'".'),
    (13, None, '\'And the main adventure is only just beginning!\' "Nachinayetsya" has a "self" on the end, so the adventure "begins itself". "Glavnoye" is "main", as in "main instrument".'),
]
