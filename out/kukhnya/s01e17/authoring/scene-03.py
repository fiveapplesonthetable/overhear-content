# Authoring module for kukhnya-s01e17-scene-03.
ID = 'kukhnya-s01e17-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 3
TITLE = 'Долг и меню  (Debt and Menu)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = 'Barinov is alone in the kitchen with his pet fish, Arkady, when Vika comes in. She reminds him that he owes her money, and also that he promised a new dish for the season. Here is their talk in Russian first.'
OPENER = "Let's go back through what Vika says, one line at a time."
TRANSITION = 'Now listen to Vika and Barinov again from the top.'
OUTRO = 'Vika gives him until tomorrow, and the chef promises to think of something. Keep "cherez nedelyu", in a week, for the next time you need to buy yourself some time. See you next time!'
CLOSING = ('vika', 'До завтра, Виктор!')
STORY = [
    ('barinov', 'Приятного аппетита, мой дорогой Аркадий.', 'Enjoy your meal, my dear Arkady.', [(35, 'приятного аппетита, Аркадий.')], ''),
    ('vika', 'Ты кормишь рыбу лучше наших гостей.', 'You feed the fish better than our guests.', [(36, 'ты для своей селедки готовишь с большим удовольствием')], ''),
    ('barinov', 'Аркадий, молчи и не слушай её.', 'Arkady, be quiet and do not listen to her.', [(37, 'Аркадий, не отвечай.')], ''),
    ('vika', 'Ты помнишь, что завтра первое число?', 'Do you remember that tomorrow is the first?', [(39, 'Ты помнишь, что завтра первое число?')], ''),
    ('barinov', 'Я верну тебе деньги через неделю.', 'I will return your money in a week.', [(40, 'отдам деньги через неделю.')], ''),
    ('vika', 'Ты обещал вернуть долг сегодня.', 'You promised to return the debt today.', [], ''),
    ('barinov', 'Твои деньги сейчас у футболиста Магиди.', 'Your money is with the footballer Magidi right now.', [(42, 'твои деньги у Магиди.')], ''),
    ('vika', 'Он не забил гол, при чём тут он?', "He didn't score a goal, so what has he got to do with it?", [(43, 'он не забил с двух метров.')], ''),
    ('barinov', 'Спроси свои деньги прямо с него.', 'Ask for your money directly from him.', [(44, 'Вот с него и спрашивай.')], ''),
    ('vika', 'Ты обещал новое сезонное блюдо, Виктор.', 'You promised a new seasonal dish, Viktor.', [(45, 'ты обещал новое сезонное блюдо от шефа.')], ''),
    ('barinov', 'Когда нужны деньги, всегда много обещаешь.', 'When money is needed, one always promises a lot.', [(46, 'когда тебе нужны деньги, ты еще не то пообещаешь.')], ''),
    ('vika', 'Завтра я жду деньги или блюдо.', 'Tomorrow I expect the money or the dish.', [(47, 'завтра у меня должны быть либо мои деньги, либо сезонное блюдо.')], ''),
    ('barinov', 'Хорошо, Вика, я что-нибудь придумаю.', 'Fine, Vika, I will come up with something.', [], ''),
]
WALK = [
    (0, None, '\'Enjoy your meal, my dear Arkady.\' "Priyatnogo appetita" is what Russians say to anyone about to eat, here to a fish. "Moy dorogoy" means "my dear".'),
    (1, None, '\'You feed the fish better than our guests.\' "Kormish" comes from "kormit", to feed. After "luchshe", better, the guests just change their ending: "nashikh gostey".'),
    (2, None, '\'Arkady, be quiet and don\'t listen to her.\' Two commands in a row, "molchi" and "ne slushay". "Ona", she, turns into "eyo" after "slushat".'),
    (3, None, '\'Do you remember that tomorrow is the first?\' "Pervoe chislo", literally "the first number", is how Russians say the first of the month.'),
    (4, None, '\'I\'ll give you the money back in a week.\' "Verny" means "I\'ll return", and "cherez nedelyu" is literally "through a week", Russian for "a week from now".'),
    (5, None, '\'You promised to pay back the debt today.\' Vika throws his own word back: "vernut dolg", to return a debt, means "pay it back".'),
    (6, None, '\'Your money is with the footballer Magidi right now.\' "U futbolista", at the footballer\'s: "u" plus a person tells you who has something.'),
    (7, None, '\'He didn\'t score a goal, so what\'s he got to do with it?\' "Pri chyom tut on" is a fixed way to ask that. "Zabil gol" is literally "hammered in a goal".'),
    (8, None, '\'Ask him for your money yourself.\' "Sprosi s nego" is literally "ask from him": "s" plus a person here means holding them to account.'),
    (9, None, '\'You promised a new seasonal dish, Viktor.\' "Sezonnoe", seasonal, comes from "sezon". "Blyudo", dish, ends in "-o", so both words before it end in "-oe" to match.'),
    (10, None, '\'When you need money, you always promise a lot.\' "Dengi", money, is always plural in Russian, so "nuzhny", needed, is plural too.'),
    (11, None, '\'Tomorrow I expect the money or the dish.\' "Zhdu" comes from "zhdat", to wait for or expect. "Ili" is "or", and she leaves him exactly two choices.'),
    (12, None, '\'All right, Vika, I\'ll think of something.\' "Chto-nibud" is "something or other": "chto", what, with "-nibud" added. "Pridumayu" means "I\'ll come up with".'),
]
