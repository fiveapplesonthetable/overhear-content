# Authoring module for domashniy-arest-s01e08-scene-35.
ID = 'domashniy-arest-s01e08-scene-35'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 35
TITLE = 'Сказать забыл!  (Forgot to Tell Her!)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'klavdia': 'Клавдия Викторовна', 'lyolya': 'Лёля'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Inside Arkady's room and the hallway a moment later. Last time, Lyolya visited Arkady to complain about Osipenko's advances and tried to give him a back massage. In the middle of it, Arkady steps on a loose screw from the floor and suddenly remembers that he forgot to tell Marina something urgent about her son's surgery. Let's listen in Russian first."
OPENER = "Let's go through the scene line by line. First, Arkady winces in pain and hops on one foot across the wooden floor."
TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = 'Next time, in the hallway, Arkady desperately tries to reach Marina before forcing his security guard to drive him to the hospital. Well done following that frantic realization in Russian. See you next time!'
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Ой! Что-то острое в ногу впилось!', 'Ow! Something sharp poked into my foot!', [(784, 'в ногу что-то впилось')], ''),
    ('lyolya', 'Что там такое? Это шуруп?', 'What is that there? Is it a screw?', [(783, 'Что такое'), (785, 'Это шуруп')], ''),
    ('arkady', 'Да, шуруп из старого пола.', 'Yes, a screw from the old floor.', [(786, 'я малому поль чиню')], "ASR 'поль' -> 'пол'"),
    ('arkady', 'Боже мой! Какой же я идиот!', 'My goodness! What an idiot I am!', [(789, 'Что ж я за идиот такой')], ''),
    ('lyolya', 'Аркаша, что с тобой случилось?', 'Arkasha, what has happened to you?', [(790, 'Что такое')], ''),
    ('arkady', 'Я забыл сказать главное!', 'I forgot to say the main thing!', [(791, 'Сказать забыл')], ''),
    ('arkady', 'Надо было срочно сказать Марине!', 'I needed to tell Marina urgently!', [(792, 'Надо срочно было сказать')], ''),
    ('lyolya', 'Подожди! Куда ты побежал?', 'Wait! Where are you running off to?', [(793, 'А я что, не срочно')], ''),
    ('arkady', 'Жди здесь! Я сейчас вернусь.', "Wait here! I'll be right back.", [(794, 'Жди здесь')], ''),
    ('arkady', 'Марина! Где Марина?', 'Marina! Where is Marina?', [(795, 'Марина'), (796, 'а где Марина')], ''),
    ('klavdia', 'Чего ты кричишь на весь дом?', 'Why are you shouting at the whole house?', [(796, 'Клавдия Викторовна')], 'Klavdia comes out of kitchen'),
    ('arkady', 'Клавдия Викторовна, где Марина?', 'Klavdia Viktorovna, where is Marina?', [(796, 'Клавдия Викторовна, а где Марина')], ''),
    ('klavdia', 'В больнице она, с Лёхой на операции.', "She's at the hospital, with Lyokha having surgery.", [(797, 'В больнице Марина с Лехой на операции')], ''),
    ('arkady', 'Как на операции? О господи, какой кошмар!', 'What do you mean, surgery? Good grief, what a nightmare!', [(798, 'Как на операции')], ''),
    ('arkady', 'Какой же я тупой!', 'How stupid I am!', [(800, 'Тупой, тупой')], ''),
]
WALK = [
    (0, None, "'Ow! Something sharp poked into my foot!' Limping across the room, Arkady yelps as something sharp jabs right into the sole of his foot."),
    (1, None, "'What is that there? Is it a screw?' Lyolya peers down at the floorboards to see if he stepped on a metal wood screw."),
    (2, None, "'Yes, a screw from the old floor.' Right then, Samson had dropped it earlier while fixing the floorboards for Lyoshka."),
    (3, None, "'My goodness! What an idiot I am!' Seeing the screw triggers Arkady's memory of the hospital mix-up."),
    (4, None, "'Arkasha, what has happened to you?' Lyolya uses the affectionate diminutive for Arkady in surprise."),
    (5, None, "'I forgot to say the main thing!' In all the chaos, he completely forgot to pass on the most important message of all."),
    (6, None, "'I needed to tell Marina urgently!' Dr. Tenenbaum's warning about the misdiagnosis had to reach Marina before the surgeons started!"),
    (7, None, "'Wait! Where are you running off to?' Lyolya is confused by his sudden panic."),
    (8, None, "'Wait here! I'll be right back.' Arkady rushes out of his room into the communal corridor in his socks."),
    (9, None, "'Marina! Where is Marina?' He bangs on Marina's bedroom door, but nobody answers."),
    (10, None, "'Why are you shouting at the whole house?' Klavdia Viktorovna emerges from the kitchen with a rag in her hand."),
    (11, None, "'Klavdia Viktorovna, where is Marina?' Arkady grabs the elderly neighbor by the shoulders in desperation."),
    (12, None, "'She's at the hospital, with Lyokha having surgery.' The doctors are about to operate on a healthy knee due to mixed-up X-rays."),
    (13, None, "'What do you mean, surgery? Good grief, what a nightmare!' Arkady realizes the catastrophic consequences of his silence."),
    (14, None, "'How stupid I am!' Arkady curses himself bitterly for forgetting when a child's health is on the line."),
]
