# Authoring module for kukhnya-s01e02-scene-13.
ID = 'kukhnya-s01e02-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 13
TITLE = 'Посторонний в баре  (An Outsider in the Bar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'master': 'Мастер', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Back at the bar, Vika sees a man behind the counter fiddling with the cash register. From behind she takes him for Kostya, but it isn't: it's a stranger, and she is not pleased. Here's their argument in Russian first."
OPENER = "Let's go through the confusion."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Vika throws the repairman out and sends for the real Kostya. You\'ve learned how to say "get out of here" and "strictly forbidden".'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Костя, ты уже починил нашу кассу?', 'Kostya, have you already fixed our register?', [(179, 'ты сикибер починил')], ''),
    ('master', 'Нет, я ещё работаю над этой кассой.', 'No, I am still working on this register.', [(180, 'Нет но и работу надо')], ''),
    ('vika', 'Что ты вообще делаешь за нашей барной стойкой?', 'What are you even doing behind our bar counter?', [(181, 'Что здесь делаешь')], ''),
    ('master', 'Я просто спокойно настраиваю эту сложную систему.', 'I am simply calmly adjusting this complex system.', [(181, 'чиню')], ''),
    ('vika', 'Быстро уходи отсюда вон из бара!', 'Leave here quickly, out of the bar!', [(182, 'давай вон из бара')], ''),
    ('master', 'Женщина, подождите, я мастер по ремонту.', 'Woman, wait, I am a repair technician.', [(186, 'что ты завелась-то')], ''),
    ('vika', 'Я сказала немедленно выйти отсюда вон!', 'I said to get out of here immediately!', [(183, 'Вон я сказала')], ''),
    ('master', 'Зачем вы так громко кричите на меня?', 'Why are you shouting so loudly at me?', [(186, 'что ты завелась')], ''),
    ('vika', 'Посторонним людям строго запрещено находиться здесь.', 'Outsiders are strictly forbidden to be here.', [(185, 'Что стоишь Вон из бара')], ''),
    ('master', 'Ладно, успокойтесь, я уже ухожу отсюда.', 'Fine, calm down, I am already leaving here.', [(186, 'А ладно')], ''),
    ('vika', 'Официант, быстро найди мне бармена Костю!', 'Waiter, quickly find bartender Kostya for me!', [(184, 'Артем быстро зови Костю')], ''),
    ('vika', 'Я хочу знать, кто пустил этого человека.', 'I want to know who let this person in.', [(184, 'зови Костю')], ''),
]
WALK = [
    (0, None, ['\'Kostya, have you already fixed our register?\' Vika thinks it\'s him. The word for fixed is ', ('vika', 'починил'), ', which she says in a way that shows she expects a man. She says the phrase for our register as ', ('vika', 'нашу кассу?'), ' with a special ending to show it is the thing being fixed.']),
    (1, None, ['\'No, I am still working on this register.\' The phrase for working on translates to ', ('master', 'работаю над'), ', which literally means working above. Because of this little word for above, the word for register changes shape to ', ('master', 'кассой.'), '.']),
    (2, None, ['\'What are you even doing behind our bar counter?\' The word for behind is ', ('vika', 'за'), ', and after it the phrase for bar counter changes shape to ', ('vika', 'барной стойкой?'), '. To sharpen the question, she adds the word for even, ', ('vika', 'вообще'), '.']),
    (3, None, ['\'I am simply calmly adjusting this complex system.\' The word for calmly translates to ', ('master', 'спокойно'), '. This is built from the word for peace, which is the root of the phrase for good night. The action word for adjusting translates to ', ('master', 'настраиваю'), ', which is how you would tune a radio.']),
    (4, None, ['\'Leave here quickly, out of the bar!\' A rude way to say out translates to ', ('vika', 'вон'), '. She piles that up with the phrase for out of the bar, ', ('vika', 'из бара!'), '. She also adds the word for from here, ', ('vika', 'отсюда'), '.']),
    (5, None, ['\'Woman, wait, I am a repair technician.\' Calling someone woman translates to ', ('master', 'Женщина,'), ', which is common but blunt. The phrase for a repairman translates to ', ('master', 'мастер по ремонту.'), ', literally meaning master in repair. The polite command for wait is ', ('master', 'подождите,'), '.']),
    (6, None, ['\'I said to get out of here immediately!\' The word for I said translates to ', ('vika', 'сказала'), ', which has a special ending because a woman is speaking. The word for immediately translates to ', ('vika', 'немедленно'), '. This is built from the little word for not plus the word for slowly.']),
    (7, None, ['\'Why are you shouting so loudly at me?\' A sharper word for why translates to ', ('master', 'Зачем'), ', literally meaning what for. The phrase for shouting at me translates to ', ('master', 'кричите на меня?'), ', which is built from the action word for shout, the little word for on, and the word for me.']),
    (8, None, ['\'Outsiders are strictly forbidden to be here.\' The word for outsider translates to ', ('vika', 'Посторонним'), '. This is built from the word for side, so it literally means people from the side. The phrase for strictly forbidden translates to ', ('vika', 'строго запрещено'), ', which is what you see on signs.']),
    (9, None, ['\'Fine, calm down, I am already leaving here.\' The action word for calm down translates to ', ('master', 'успокойтесь,'), ', which is built from the same root word for peace as before. The word for OK or fine translates to ', ('master', 'Ладно,'), '.']),
    (10, None, ['\'Waiter, quickly find bartender Kostya for me!\' The action word for find translates to ', ('vika', 'найди'), ', which is a friendly command. The phrase for bartender Kostya changes shape to ', ('vika', 'бармена Костю!'), ' to show he is the one being found.']),
    (11, None, ['\'I want to know who let this person in.\' Watch the phrase for this person change shape. Because they are the ones being let in, they become ', ('vika', 'этого человека.'), '. Also, the word for who translates to ', ('vika', 'кто'), ', which uses the action word for let in, ', ('vika', 'пустил'), '. This action word has an ending that assumes a man did it.']),
]
