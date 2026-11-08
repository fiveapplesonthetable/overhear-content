# Authoring module for dvorik-u-mosta-s01e03-scene-08.
ID = 'dvorik-u-mosta-s01e03-scene-08'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = 'Холодные трубы  (Ice-Cold Pipes)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'matvey': 'Матвей', 'kira': 'Кира', 'yaroslav': 'Ярослав'}
INTRO = 'Down at the front desk, Kira and Yaroslav wait anxiously by the cellar door until Matvey climbs up wiping his hands on a rag and shaking his head. Listen first.'
OPENER = "Now let's hear Matvey's cellar report line by line."
TRANSITION = "Let's listen to the whole conversation again from beginning to end."
OUTRO = "A suspected travel-guide inspector upstairs, a broken brass valve in the cellar, and a seven o'clock race across the bridge tomorrow morning. Episode 3 is complete — see you in Episode 4."
CLOSING = ('matvey', 'До завтра!')
STORY = [
    ('yaroslav', 'Матвей, скажи, что это просто воздух в трубе! Пожалуйста!', 'Matvey, tell me it is just air in the pipe! Please!'),
    ('matvey', 'Плохие новости. Латунный вентиль на старом котле треснул.', 'Bad news. The brass valve on the old boiler cracked.'),
    ('kira', 'Значит, ночью не будет отопления и горячей воды тоже?', 'Does that mean tonight there will be no heating and no hot water either?'),
    ('matvey', 'До утра в комнатах будет тепло, Кира, кирпичные стены держат жар.', 'Until morning the rooms will stay warm, Kira, the brick walls hold heat.'),
    ('yaroslav', 'Слава богу! А утренний душ для гостей?', 'Thank goodness! And the morning shower for the guests?'),
    ('matvey', 'К завтрашнему утру вода в душе будет ледяной.', 'By tomorrow morning, the shower water will be ice cold.'),
    ('yaroslav', 'Ледяной душ?! Когда на третьем этаже спит автор гида по Петербургу?!', 'An ice-cold shower?! When the St Petersburg guidebook author is sleeping on the third floor?!'),
    ('kira', 'У тебя в ящике есть запасной латунный вентиль?', 'Do you have a spare brass valve in your toolbox?'),
    ('matvey', 'Последний я поставил зимой. Такой размер продают только в старой лавке за мостом.', 'I installed my last one in winter. Only the old shop past the bridge sells that size.'),
    ('kira', 'Во сколько открывается эта лавка?', 'What time does that shop open?'),
    ('matvey', 'Ровно в семь — за полчаса до завтрака.', 'At seven sharp — half an hour before breakfast.'),
    ('kira', 'Ставь будильник, Матвей. Завтра утром мы обгоним ледяной душ!', 'Set your alarm, Matvey. Tomorrow morning we will outrun the ice-cold shower!'),
]
WALK = [
    (0, None, "'Matvey, tell me it is just air in the pipe! Please!' In sheer panic Yaroslav slips into casual speech with his longtime handyman, begging for good news."),
    (1, None, ["'Bad news. The brass valve on the old boiler cracked.' Notice ", (None, 'Плохие новости.'), " — 'news' is plural in Russian, unlike English."]),
    (2, None, ["'Does that mean tonight there will be no heating and no hot water either?' Future absence uses singular ", (None, 'не будет'), " — 'there will not be'."]),
    (3, None, ["'Until morning the rooms will stay warm, Kira, the brick walls hold heat.' Impersonal ", (None, 'будет тепло,'), ' reassures them that warmth will hold inside the rooms until dawn.']),
    (4, None, ["'Thank goodness! And the morning shower for the guests?' Notice ", (None, 'утренний душ'), ' — a shower in Russian is short and masculine.']),
    (5, None, ["'Tomorrow at seven in the morning the shower water will be ice-cold.' Built directly from the word for ice, ", (None, 'ледяной.'), ' paints water cold enough to make anyone gasp.']),
    (6, None, ["'An ice-cold shower?! When the St Petersburg guidebook author is sleeping on the third floor?!' Notice ", (None, 'спит'), " — 'is sleeping', while poor Yaroslav won't sleep a wink."]),
    (7, None, ["'Do you have a spare brass valve in your toolbox?' Worth knowing for keys, tyres, or parts, ", (None, 'запасной'), " means 'spare, kept in reserve'."]),
    (8, None, ["'I installed my last one in winter. Only the old shop past the bridge sells that size.' Across or beyond a landmark uses ", (None, 'за мостом.'), " — 'beyond the bridge', echoing the inn's own neighbourhood."]),
    (9, None, ["'What time does that shop open?' Asking 'at what hour?' uses the essential two-word question ", (None, 'Во сколько'), " — 'at how much?'."]),
    (10, None, ["'At seven sharp — half an hour before breakfast.' Just like 'forty minutes from now' earlier, ", (None, 'за полчаса до завтрака.'), " marks 'half an hour before breakfast'."]),
    (11, None, ["'Set your alarm, Matvey. Tomorrow morning we will outrun the ice-cold shower!' An alarm clock has a great transparent name: ", (None, 'будильник,'), " literally 'the waker-upper'!"]),
]
