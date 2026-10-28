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
INTRO = "The duel is on, and Chef Barinov has decided that Max needs help, but he can't be seen giving it. So he rings the kitchen phone and pretends to be Max's mother. Max, who is not stupid, plays along in front of the other cooks. Listen to it in Russian first."
OPENER = "Let's replay the phone call. It starts with Max not knowing who this could be."
TRANSITION = 'Now put it all back together.'
OUTRO = "Phone calls have their own small words: the hello, the 'I'll call you back', and the 'bye'. You've heard all three. See you next time."
CLOSING = ('max', 'До скорого!')
STORY = [
    ('max', 'Кто? Мама?', 'Who? Mom?', [(124, 'Кто? Мама?')], ''),
    ('max', 'А откуда она знает этот номер?', 'And how does she know this number?', [(125, 'А откуда она знает этот номер')], ''),
    ('max', 'Алло, мама?', 'Hello, Mom?', [(126, 'Алло, мама?')], ''),
    ('barinov', 'Да, мама я, твоя мама.', 'Yes, it is Mom, your mom.', [(126, 'Да, мама я, твоя мама')], ''),
    ('barinov', 'Будешь готовить форель с обычным жульеном.', 'You will cook trout with classic julienne.', [(127, 'Будешь готовить форель с обычным')], ''),
    ('barinov', 'Для начала выпотроши свежую рыбу.', 'First, clean the fresh fish.', [(128, 'Для начала выпотроши рыбу')], ''),
    ('barinov', 'Потом аккуратно удали хребет.', 'Then carefully remove the backbone.', [(128, 'удали хребет')], ''),
    ('barinov', 'И положи филе в холодильник.', 'And put the fillet in the fridge.', [(128, 'и положи филе в холодильник')], ''),
    ('barinov', 'Ты всё понял, мамуля?', 'Did you understand everything, Mommy?', [(129, 'Понял, мамуля?')], ''),
    ('max', 'Да я тебе попозже перезвоню, некогда.', 'I will call you back later, I am busy.', [(130, 'Да я тебе попозже перезвоню'), (130, 'некогда')], ''),
    ('max', 'Целую тебя, пока.', 'Kisses to you, bye.', [(131, 'Целую тебя пока')], ''),
    ('max', 'Это звонила мама из Воронежа.', 'That was Mom calling from Voronezh.', [(132, 'Мама из Воронежа')], ''),
]
WALK = [
    (0, None, "'Who? Mom?' Max says it twice, once as 'who' and once as 'mom'. 'mom' sounds just like it does in English."),
    (1, None, "'And how does she know this number?' Russian opens with 'from where', which it uses for 'how come'. 'Knows' is the form from 'I don't know'."),
    (2, None, "'Hello, Mom?' 'hello' that Max uses is only for the phone. You'd say a different one in person."),
    (3, None, "'Yes, it is Mom, your mom.' Barinov puts 'mom' first, which makes it sound funnier than 'I am your mother'. Notice the lack of 'is' again."),
    (4, None, "'You will cook trout with classic julienne.' The future is built with 'you will be' plus a second word, 'to cook'. That is a very common way to say 'you will do'. 'Classic' is closer to 'usual'."),
    (5, None, "'First, clean the fresh fish.' Now it's the chef giving the instructions. 'For a start' is literally 'for a beginning', and the command means 'gut', which is how you clean a fish."),
    (6, None, "'Then carefully remove the backbone.' The first word means 'then', or 'after that'. 'carefully' is also used for 'neatly', and the command ends with 'backbone'."),
    (7, None, "'And put the fillet in the fridge.' 'Fillet' is borrowed from French, and 'fridge' starts from 'cold'. The command is from 'lay down'."),
    (8, None, "'Did you understand everything, Mommy?' The pet name for 'mom' is longer and sweeter. 'Understood' ends in a consonant, as Max is a man."),
    (9, None, "'I will call you back later, I am busy.' 'Call back' is 'call' with a prefix meaning 'again'. The last word is a short way of saying 'no time', from 'not when'."),
    (10, None, "'Kisses to you, bye.' 'I kiss' is the verb for kissing, in the same family as 'kiss'. The last word is 'bye', which is also 'for now'."),
    (11, None, "'That was Mom calling from Voronezh.' Max says it to the room. Voronezh is his home town. 'Called' ends in 'la', because it agrees with 'mom'."),
]
