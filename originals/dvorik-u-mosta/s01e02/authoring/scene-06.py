# Authoring module for dvorik-u-mosta-s01e02-scene-06.
ID = 'dvorik-u-mosta-s01e02-scene-06'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'Пятничный звонок  (The Friday Caller)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'matvey': 'Матвей'}
INTRO = 'After breakfast, the lobby is quiet while Kira updates the paper ledger and Matvey oils the front door hinge. Suddenly the desk telephone rings. Listen to the Russian first.'
OPENER = "Let's listen closely to each line of that mysterious phone call."
TRANSITION = "Now let's hear the whole conversation again without pauses."
OUTRO = 'Now they have an exact appointment — Friday at noon — and a nervous voice on the phone who refuses to give his name. See you next time.'
CLOSING = ('kira', 'До свидания!')
STORY = [
    ('kira', 'Гостевой дом Дворик у моста, доброе утро! Кира слушает.', 'Bridge Courtyard Inn, good morning! Kira speaking.'),
    ('matvey', 'Кто это? Ещё одна бронь на выходные?', 'Who is it? Another booking for the weekend?'),
    ('kira', 'Подождите — здравствуйте! Вы звоните насчёт тёмно-синего чемодана?', 'Wait — hello! Are you calling about the dark-blue suitcase?'),
    ('matvey', 'Спроси его имя! Запиши в книгу!', 'Ask his name! Write it down in the book!'),
    ('kira', 'Да, ваша сумка под замком в кладовке. Скажите, пожалуйста, как вас зовут?', 'Yes, your bag is locked in the closet. Tell me, please, what is your name?'),
    ('matvey', 'Что он говорит? Почему ты хмуришься?', 'What is he saying? Why are you frowning?'),
    ('kira', 'Алло? Он говорит: пожалуйста, не открывайте белый свёрток, я приду в пятницу в полдень.', 'Hello? He says: please do not open the white parcel, I will come on Friday at noon.'),
    ('matvey', 'Дай мне трубку — я сам спрошу как следует!', 'Give me the receiver — I will ask him properly myself!'),
    ('kira', 'Поздно! Он сказал спасибо и положил трубку!', 'Too late! He said thank you and hung up!'),
    ('matvey', 'Голос вежливый? Молодой или пожилой?', 'Was the voice polite? Young or elderly?'),
    ('kira', 'Тихий, вежливый, лет тридцать пять. Он волновался, а не злился.', 'Quiet, polite, around thirty-five. He was nervous, not angry.'),
    ('matvey', 'Волновался из-за деревянного поезда? С каждым часом всё страннее.', 'Nervous because of a wooden train? Every hour this gets stranger.'),
]
WALK = [
    (0, None, ["'Bridge Courtyard Inn, good morning! Kira speaking.' Answering a work phone uses ", (None, 'Кира слушает.'), " — literally 'Kira is listening', rather than 'Kira speaking'."]),
    (1, None, ["'Who is it? Another booking for the weekend?' Days off at the end of the week are ", (None, 'на выходные?'), " — literally 'off-going days' when you don't go to work."]),
    (2, None, ["'Wait — hello! Are you calling about the dark-blue suitcase?' Useful for business calls, ", (None, 'насчёт'), " means 'concerning' or 'regarding'."]),
    (3, None, ["'Ask his name! Write it down in the book!' Matvey whispers urgent casual commands: ", (None, 'Спроси'), " for 'ask' and ", (None, 'Запиши'), " for 'write down'."]),
    (4, None, ["'Yes, your bag is locked in the closet. Tell me, please, what is your name?' Literally 'how do people call you?', ", (None, 'как вас зовут?'), " is the universal polite way to ask someone's name."]),
    (5, None, ["'What is he saying? Why are you frowning?' Knitting your brows together is ", (None, 'хмуришься?'), " — 'you frown'."]),
    (6, None, ["'Hello? He says: please do not open the white parcel, I will come on Friday at noon.' Midday packs 'half' and 'day' into one neat word: ", (None, 'в полдень.'), " — 'at noon'."]),
    (7, None, ["'Give me the receiver — I will ask him properly myself!' Idiomatic ", (None, 'как следует!'), " means 'properly, the way one ought to'."]),
    (8, None, ["'Too late! He said thank you and hung up!' Hanging up a phone still keeps the old handset image: ", (None, 'положил трубку!'), " literally says 'put down the receiver'."]),
    (9, None, ["'Was the voice polite? Young or elderly?' Respectful Russian uses ", (None, 'пожилой?'), " — 'having lived awhile' — rather than blunt 'old' when speaking of people."]),
    (10, None, ["'Quiet, polite, around thirty-five. He was nervous, not angry.' Putting 'years' before the number in ", (None, 'лет тридцать пять.'), " flips the order to mean 'around thirty-five' — a neat Russian trick!"]),
    (11, None, ["'Nervous because of a wooden train? Every hour this gets stranger.' Giving the cause of worry uses ", (None, 'из-за'), " — 'because of'."]),
]
