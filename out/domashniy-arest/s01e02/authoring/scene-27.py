# Authoring module for domashniy-arest-s01e02-scene-27.
ID = 'domashniy-arest-s01e02-scene-27'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 27
TITLE = 'Звонит Третьяков  (A Call from Tretyakov)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'governor': 'Губернатор', 'ksyusha': 'Ксюша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "Meanwhile, in the governor's office, a meeting is about to begin. Last time, Samson's boss gave him holiday vouchers for a chilly March in Crimea that nobody else wanted; now the governor, Viktor Stepanovich, wants every official to like his new judo photo online, and then a very important call comes in. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go through it slowly. The governor sits at the head of a long table and checks on his officials first."
TRANSITION = 'Now the whole meeting again, likes, phone call and all.'
OUTRO = "That's it for this scene; if the phone call went by fast, don't worry, just listen for the order to release him, and the governor's last word. See you next time!"
CLOSING = ('governor', 'Пока!')
STORY = [
    ('governor', 'Ну что, все лайкнули?', 'Well, has everyone liked it?', [(918, 'Ну что, все лайкнули')], ''),
    ('ksyusha', 'Вот здесь сердечко, видите? Жмите на него.', "There's a little heart right here, see? Press it.", [(922, 'вот здесь сердечко, видите'), (923, 'жмите на него')], "'Ну' dropped twice; said to an older official"),
    ('governor', 'Сколько там?', 'How many is it?', [(931, 'сколько там')], "'Ну что' dropped"),
    ('ksyusha', 'Сто семнадцать лайков.', 'A hundred and seventeen likes.', [(932, 'лайков')], 'the number written out in words'),
    ('governor', 'А почему так мало?', 'And why so few?', [(933, 'так мало')], "colloquial 'чего ... -то' -> 'почему'"),
    ('ksyusha', 'Мы же только начинаем. Через месяц будет пять тысяч.', "But we're only just starting. In a month there'll be five thousand.", [(934, 'мы же только начинаем'), (934, 'Через месяц')], "'по 5 тысяч' -> 'пять тысяч'"),
    ('governor', 'Смотри, не будет — я тебя уволю.', "Watch out: if there aren't, I'll fire you.", [(935, 'Смотри, не будет'), (935, 'я тебя уволю')], ''),
    ('ksyusha', 'Виктор Степанович, вам звонит Третьяков!', 'Viktor Stepanovich, Tretyakov is calling you!', [], 'tells the listener who is (supposedly) on the line'),
    ('governor', 'Так, тихо все! Алло?', 'Right, quiet, everyone! Hello?', [(938, 'Так, тихо все')], "'Алло?' added"),
    ('arkady', 'Ты меня слышишь? Почему у вас Аникеев под арестом?', 'Can you hear me? Why is Anikeev under arrest over there?', [(949, 'Почему у вас'), (949, 'под арестом')], "garbled 'антикейф' read as 'Аникеев'; first sentence new, standing in for the mocking cues 942-948"),
    ('governor', 'Ну так он же на взятке попался.', 'Well, he got caught taking a bribe.', [(951, 'Ну так он же')], "'на взятки' -> 'на взятке'"),
    ('arkady', 'Какая взятка? Отпустить немедленно!', 'What bribe? Release him immediately!', [(953, 'Какая взятка'), (955, 'Отпустить немедленно')], 'insults and the threat in 952 and 954 left out'),
    ('governor', 'Пётр Олегович, вы же сами сказали…', 'Pyotr Olegovich, but you said yourself…', [(956, 'Петр Олегович, вы же сами сказали')], ''),
    ('arkady', 'Ты что, с первого раза не понимаешь?', "What, you don't understand the first time?", [(958, 'с первого раза не понимаешь')], "'Ты' + 'что' instead of 'Ты ... что ли'; crude cues 960-962 left out"),
    ('governor', 'Понял. Пётр Олегович, а вопрос с полярником?', 'Understood. Pyotr Olegovich, and what about the matter of the polar explorer?', [(965, 'Понял'), (970, 'полярником')], 'cues 965-970 joined and simplified'),
    ('arkady', 'Я уже всё решил. Одну треть на кладбище, две трети над океаном.', "I've already sorted it all out. One third goes to the cemetery, two thirds over the ocean.", [(971, 'Я решил'), (989, 'одну треть на'), (989, 'две трети над океаном')], "the long story of the explorer's ashes (972-988) left to the narrator; the cemetery's name dropped"),
    ('governor', 'Гениально. Просто гениально.', 'Brilliant. Simply brilliant.', [(990, 'Гениально')], "'Вот просто и' -> 'Просто'"),
    ('arkady', 'Всё, не благодари меня. И с Аникеевым реши.', "That's it, don't thank me. And sort out Anikeev.", [(991, 'не благодари меня')], "garbled 'Аникейовым' -> 'Аникеевым'"),
]
WALK = [
    (0, None, "'Well, has everyone liked it?' Viktor checks on the room after the presentation, asking if everyone enjoyed it."),
    (1, 'Вот здесь сердечко, видите?', "'There's a little heart right here, see?' The word for 'heart' has a small, cute ending: a little heart. Then a clear instruction."),
    (1, 'Жмите на него.', "'Press it.' Literally 'press on it'. It's the polite command, because the official is older. The governor wants numbers."),
    (2, None, "'How many is it?' The first word means 'how many' or 'how much'. Ksenia checks her phone."),
    (3, None, "'A hundred and seventeen likes.' After a number like that, the noun goes into the plural form you hear at the end. The governor is not pleased."),
    (4, None, "'And why so few?' The first word asks 'why', and the last one means 'few' or 'little'. Ksenia has an excuse."),
    (5, 'Мы же только начинаем.', "'But we're only just starting.' The little word after 'we' adds 'but, you see'. And she makes a promise."),
    (5, 'Через месяц будет пять тысяч.', "'In a month there'll be five thousand.' The first word, followed by a time, means 'in', as in 'in a month's time'. The governor answers with a threat."),
    (6, None, "'Watch out: if there aren't, I'll fire you.' The first word literally means 'look', but here it's a warning. Then Ksenia sees who is calling."),
    (7, None, "'Viktor Stepanovich, Tretyakov is calling you!' Right then, Tretyakov is the powerful man in Moscow that the governor is terrified of. What nobody in the room knows is that it's really Arkady, using a phone app that fakes the number, bought with little Lyosha's five hundred roubles, and doing his best Tretyakov voice. The governor silences the room."),
    (8, None, "'Right, quiet, everyone! Hello?' The last word is just how Russians answer the phone. 'Tretyakov' starts shouting at once."),
    (9, 'Ты меня слышишь?', "'Can you hear me?' He uses the casual 'you' to a regional governor, which shows who is the boss here. Then the question that matters."),
    (9, 'Почему у вас Аникеев под арестом?', "'Why is Anikeev under arrest over there?' Anikeev is Arkady's own surname, so he is asking about himself. The phrase for 'under arrest' is easy to hear. The governor explains, nervously."),
    (10, None, "'Well, he got caught taking a bribe.' The verb means 'got caught', and it's masculine, because it's about Arkady. 'Tretyakov' explodes."),
    (11, 'Какая взятка?', "'What bribe?' The question word changes its ending to match the bribe, which is a feminine noun. Then an order."),
    (11, 'Отпустить немедленно!', "'Release him immediately!' An order made with just the basic form of the verb sounds very harsh and official. The governor is confused."),
    (12, None, "'Pyotr Olegovich, but you said yourself…' He means the orders about Arkady's case came from Tretyakov himself. But 'Tretyakov' won't listen."),
    (13, None, "'What, you don't understand the first time?' Literally 'from the first time'. It's the same bossy voice Arkady used earlier to make the children laugh. The governor gives in, and then dares to ask one more thing."),
    (14, 'Понял.', "'Understood.' Literally 'I understood', in the masculine past form. It's how you say 'got it' to a boss."),
    (14, 'Пётр Олегович, а вопрос с полярником?', "'Pyotr Olegovich, and what about the matter of the polar explorer?' A famous polar explorer has died, and Tretyakov promised to sort out his funeral. Arkady has no idea, so he improvises."),
    (15, 'Я уже всё решил.', "'I've already sorted it all out.' The verb means 'decided' or 'solved'. Then his wonderful solution: the explorer wanted his ashes scattered over the Arctic Ocean, but people wanted a grave for their hero."),
    (15, 'Одну треть на кладбище, две трети над океаном.', "'One third goes to the cemetery, two thirds over the ocean.' The words for one third and two thirds are worth knowing, and the cemetery word is long but clear. The governor is overwhelmed."),
    (16, None, "'Brilliant. Simply brilliant.' The first word sounds just like the English 'genius'. And 'Tretyakov' signs off in style."),
    (17, None, "'That's it, don't thank me. And sort out Anikeev.' The verb for 'sort out' is the same one as before, now as a casual command. Arkady has just ordered his own release."),
]
