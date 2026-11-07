# Authoring module for dvorik-u-mosta-s02e04-scene-01.
ID = 'dvorik-u-mosta-s02e04-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 4
SCENE = 1
TITLE = 'Мастерская в коридоре  (An Indoor Paint Shop)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'matvey': 'Матвей', 'roman': 'Роман'}
INTRO = "Steady Monday rain taps on the courtyard roof at the Bridge Courtyard Inn, where four bare wooden shutters lean inside the back hallway. Roman joins Kira and Matvey with a roll of brown paper and a small fan. Listen first."
OPENER = "Now let's set up the rainy-day paint shop, one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = "With brown paper on the floor and warm air moving gently, the rainy Monday paint shop is open, right as Yaroslav arrives in a crisp white shirt! See you next time."
CLOSING = ('matvey', 'До встречи!')
STORY = [
    ('kira', 'На улице всё ещё дождь, Матвей. Краска в доме высохнет к среде?', 'It is still raining outside, Matvey. Will the paint dry indoors by Wednesday?'),
    ('roman', 'Высохнет, если мы положим бумагу на пол и включим тёплый воздух.', 'It will dry if we put paper on the floor and turn on warm air.'),
    ('matvey', 'Краска на воде. Почти не пахнет и быстро сохнет, если воздух двигается.', 'Water-based paint. It hardly smells and dries fast if the air moves.'),
    ('kira', 'Куда поставить вентилятор, Роман?', 'Where should we put the fan, Roman?'),
    ('roman', 'Откроем форточку на два сантиметра и направим сухой воздух туда.', "We'll open the little top window two centimetres and point the dry air there."),
    ('matvey', 'Умно! Воздух идёт мимо дерева, а дождь в дом не попадает.', "Smart! The air goes past the wood, and the rain doesn't get into the house."),
    ('kira', 'Смотрите, какой цвет в банке! Тёмно-зелёный, как лист липы!', 'Look at the colour in the tin! Dark green, like a linden leaf!'),
    ('matvey', 'Тонкий слой и вдоль дерева, Кира. Толстая краска долго липкая.', 'A thin coat and along the grain, Kira. Thick paint stays sticky for a long time.'),
    ('roman', 'Первый слой до обеда, второй вечером, а во вторник всё будет сухое!', 'First coat before lunch, second in the evening, and on Tuesday everything will be dry!'),
    ('kira', 'Дай мне широкую кисть, Матвей. Первая ставня моя!', 'Give me the wide brush, Matvey. The first shutter is mine!'),
    ('matvey', 'Маленькую кисть оставим для углов. И кто-нибудь, смотрите на дверь: вдруг придёт шеф.', "We'll keep the small brush for the corners. And somebody watch the door, in case the boss comes."),
    ('kira', 'Поздно! Вот идёт Ярослав Ильич в чистой белой рубашке!', 'Too late! Here comes Yaroslav Ilyich in a clean white shirt!'),
]
WALK = [
    (0, None, ["'It is still raining outside, Matvey. Will the paint dry indoors by Wednesday?' A deadline takes the little word for 'towards': ", (None, 'к среде?'), " means 'by Wednesday'."]),
    (1, None, ["'It will dry if we put paper on the floor and turn on warm air.' Roman answers with the same verb Kira used, ", (None, 'Высохнет,'), " which is the natural Russian way to say 'yes, it will'."]),
    (2, None, ["'Water-based paint. It hardly smells and dries fast if the air moves.' Paint 'on water' is how Russians say water-based: ", (None, 'Краска на воде.')]),
    (3, None, ["'Where should we put the fan, Roman?' To ask 'where should I put it?', Kira uses just ", (None, 'Куда поставить'), ", 'where to' plus the verb, no 'should' needed."]),
    (4, None, ["'We'll open the little top window two centimetres and point the dry air there.' A Russian window often has a small airing pane, ", (None, 'форточку'), ", that opens on its own."]),
    (5, None, ["'Smart! The air goes past the wood, and the rain doesn't get into the house.' The word ", (None, 'мимо'), " is 'past', for anything that goes by without stopping."]),
    (6, None, ["'Look at the colour in the tin! Dark green, like a linden leaf!' Shades are built by joining two words: ", (None, 'Тёмно-зелёный,'), " is 'dark green', from the word for dark."]),
    (7, None, ["'A thin coat and along the grain, Kira. Thick paint stays sticky for a long time.' Matvey's tip ", (None, 'вдоль дерева,'), " means 'along the wood', following its lines."]),
    (8, None, ["'First coat before lunch, second in the evening, and on Tuesday everything will be dry!' A coat of paint is a 'layer': ", (None, 'Первый слой'), ", the same word as a layer of cake."]),
    (9, None, ["'Give me the wide brush, Matvey. The first shutter is mine!' Among friends Kira says ", (None, 'Дай мне'), ", the casual 'give me', instead of the polite form."]),
    (10, None, ["'We'll keep the small brush for the corners. And somebody watch the door, in case the boss comes.' The little word ", (None, 'вдруг'), " means 'suddenly', and here 'what if'."]),
    (11, None, ["'Too late! Here comes Yaroslav Ilyich in a clean white shirt!' To announce someone arriving, Kira uses ", (None, 'Вот идёт'), ", 'here comes', with the walking verb."]),
]
