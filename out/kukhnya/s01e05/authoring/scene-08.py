# Authoring module for kukhnya-s01e05-scene-08.
ID = 'kukhnya-s01e05-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = 'Звонок от мамы  (Call from Mom)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "The cook-off is on in the Claude Monet kitchen, and Chef Barinov has decided Max needs help, but he can't be seen giving it. So he rings the kitchen phone and pretends to be Max's mother, with the recipe. Max catches on and plays along in front of the other cooks. Listen in Russian first."
OPENER = "Let's replay the phone call, from the moment Max hears who's on the line."
TRANSITION = 'Now the call in one go.'
OUTRO = "That's a whole phone call in miniature: saying hello to pick up, promising you'll call back, giving kisses and a casual bye to hang up. Max now has the chef's recipe, and nobody knows it."
CLOSING = ('max', 'До скорого!')
STORY = [
    ('max', 'Кто? Мама?', 'Who? Mom?', [(124, 'Кто? Мама?')], ""),
    ('max', 'А откуда она знает этот номер?', 'And how does she know this number?', [(125, 'А откуда она знает этот номер')], ""),
    ('max', 'Алло, мама?', 'Hello, Mom?', [(126, 'Алло, мама?')], ""),
    ('barinov', 'Да, мама я, твоя мама.', 'Yes, it is Mom, your mom.', [(126, 'Да, мама я, твоя мама')], ""),
    ('barinov', 'Будешь готовить форель с обычным жюльеном.', 'You will cook trout with classic julienne.', [(127, 'Будешь готовить форель с обычным')], ""),
    ('barinov', 'Для начала выпотроши свежую рыбу.', 'First, clean the fresh fish.', [(128, 'Для начала выпотроши рыбу')], ""),
    ('barinov', 'Потом аккуратно удали хребет.', 'Then carefully remove the backbone.', [(128, 'удали хребет')], ""),
    ('barinov', 'И положи филе в холодильник.', 'And put the fillet in the fridge.', [(128, 'и положи филе в холодильник')], ""),
    ('barinov', 'Ты всё понял, мамуля?', 'Did you understand everything, Mommy?', [(129, 'Понял, мамуля?')], ""),
    ('max', 'Да я тебе попозже перезвоню, некогда.', 'I will call you back later, I am busy.', [(130, 'Да я тебе попозже перезвоню'), (130, 'некогда')], ""),
    ('max', 'Целую тебя, пока.', 'Kisses to you, bye.', [(131, 'Целую тебя пока')], ""),
    ('max', 'Это звонила мама из Воронежа.', 'That was Mom calling from Voronezh.', [(132, 'Мама из Воронежа')], ""),
]
WALK = [
    (0, None, [
        "'Who? Mom?' Two one-word questions. ",
        ('max', 'Мама?'),
        " is the word Russian children use, just like English 'mama'."
    ]),
    (1, None, [
        "'And how does she know this number?' literally expresses 'from where', and it ",
        ('max', 'откуда'),
        " erally expresses 'from where', and it is used here for 'how come'. ",
        ('max', 'этот'),
        ('max', 'номер?'),
        " expresses 'this number'."
    ]),
    (2, None, [
        "'Hello, Mom?' is the greeting you say when ",
        ('max', 'Алло,'),
        " you pick up the phone. Face to face you'd use a different hello."
    ]),
    (3, None, [
        "'Yes, it is Mom, your mom.' Barinov says ",
        ('barinov', 'мама'),
        ('barinov', 'я,'),
        " which literally means 'mom I', with no 'am'. ",
        ('barinov', 'твоя'),
        " is the feminine 'your', to go with ",
        ('barinov', 'мама.')
    ]),
    (4, None, [
        "'You will cook trout with classic julienne.' translates to 'you will cook'. ",
        ('barinov', 'Будешь'),
        ('barinov', 'готовить'),
        ' After ',
        ('barinov', 'с'),
        ", meaning 'with', the word for julienne takes a new ending, becoming ",
        ('barinov', 'жюльеном.')
    ]),
    (5, None, [
        "'First, clean the fresh fish.' is the phrase for 'for a ",
        ('barinov', 'Для'),
        ('barinov', 'начала'),
        " se for 'for a start'. ",
        ('barinov', 'выпотроши'),
        " literally expresses 'gut it', which is exactly how you clean a fish."
    ]),
    (6, None, [
        "'Then carefully remove the backbone.' is used for 'then' or 'after ",
        ('barinov', 'Потом'),
        " that'. ",
        ('barinov', 'аккуратно'),
        " looks like 'accurately' but actually expresses 'carefully' or 'neatly'."
    ]),
    (7, None, [
        "'And put the fillet in the fridge.' The word for 'fridge', ",
        ('barinov', 'холодильник'),
        ", grows out of the root for 'cold'. ",
        ('barinov', 'положи'),
        " is the verb for 'put', specifically for laying something down."
    ]),
    (8, None, [
        "'Did you understand everything, Mommy?' is an extra-tender 'mommy'. Coming from ",
        ('barinov', 'мамуля?'),
        " the chef, it's pure comedy."
    ]),
    (9, None, [
        "'I will call you back later, I am busy.' is built from the verb 'to ",
        ('max', 'перезвоню,'),
        " call' with a prefix meaning 'again'. ",
        ('max', 'некогда'),
        " is used for 'there's no time', and ",
        ('max', 'попозже'),
        " literally translates to 'a bit later'."
    ]),
    (10, None, [
        "'Kisses to you, bye.' literally means 'I kiss you', which ",
        ('max', 'Целую'),
        ('max', 'тебя,'),
        ' is how Russians end calls with family. Then ',
        ('max', 'пока'),
        ", the casual 'bye'."
    ]),
    (11, None, [
        "'That was Mom calling from Voronezh.' has a feminine ending to agree ",
        ('max', 'звонила'),
        ' with ',
        ('max', 'мама'),
        ". After ",
        ('max', 'из'),
        ", meaning 'from', the city of Voronezh takes a new ending, becoming ",
        ('max', 'Воронежа.')
    ]),
]
