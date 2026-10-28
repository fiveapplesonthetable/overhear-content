# Authoring module for domashniy-arest-s01e02-scene-24.
ID = 'domashniy-arest-s01e02-scene-24'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 24
TITLE = 'Копилка  (The Piggy Bank)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'lyosha': 'Лёша', 'yulia': 'Юля'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "Still in the communal flat, a minute later. Last time, Yulia told Arkady about an app that can fake the number on a phone call, so he could ring the governor pretending to be Tretyakov. But the app costs five hundred roubles, and Arkady hasn't got a penny. So he turns to the children, and to Lyosha, Marina's son. Let's listen in Russian first."
OPENER = "Let's take it line by line. Arkady starts by simply asking."
TRANSITION = "Let's hear the whole scene once more, start to finish."
OUTRO = "So Lyosha gives up half a year of savings to prove he isn't greedy, and Arkady has his five hundred roubles. You followed a whole bargain in Russian; well done. See you next time!"
CLOSING = ('lyosha', 'Пока!')
STORY = [
    ('arkady', 'Ребята, дайте денег, а?', 'Kids, give me some money, eh?', [(758, 'дайте денег, а')], "'Так, ребятушки' -> 'Ребята'"),
    ('yulia', 'У меня нет.', "I haven't got any.", [(760, 'У меня нет')], 'speaker of cue 760 given to Yulia'),
    ('arkady', 'А у кого есть? Так, Шнурок, есть же копилка?', "So who has? Right, Shoelace, you've got a piggy bank, haven't you?", [(762, 'А у кого есть'), (763, 'Так, Шнурок'), (764, 'Есть же копилка')], ''),
    ('lyosha', 'Мы с мамой на приставку копим.', 'Mum and I are saving up for a games console.', [(766, 'Мы с мамой'), (766, 'копим')], "'на пей-шопе' (a PSP, garbled) -> 'на приставку'"),
    ('arkady', 'Да? И сколько уже накопили?', 'Really? And how much have you saved so far?', [(767, 'Да? И сколько уже накопили')], ''),
    ('lyosha', 'Семьсот пятьдесят рублей. Копим полгода.', "Seven hundred and fifty roubles. We've been saving for half a year.", [(768, 'Семьсот пятьдесят рублей'), (772, 'Полгода')], "'Копим' added; cue 771 (Arkady's question) folded in"),
    ('arkady', 'А сколько стоит приставка?', 'And how much does the console cost?', [(769, 'А сколько стоит')], "'твоя пипися' (a mocking name for the PSP) -> 'приставка'"),
    ('lyosha', 'Пять тысяч рублей.', 'Five thousand roubles.', [(770, 'Пять тысяч рублей')], ''),
    ('arkady', 'Послушай, малыш, у меня есть деловое предложение.', "Listen, kid, I've got a business proposal.", [(774, 'Послушай, малыш, у меня есть'), (774, 'деловое предложение')], "'к тебе' dropped"),
    ('arkady', 'Ты даёшь пятьсот рублей, а я покупаю тебе лучшую приставку в мире.', 'You give me five hundred roubles, and I get out and buy you the best console in the world.', [(775, 'даешь пятьсот рублей'), (776, 'покупаю тебе'), (776, 'в мире')], "'Смотри,' dropped; 'лучшие пи-спи' -> 'лучшую приставку'"),
    ('lyosha', 'А если не выйдете?', "And what if you don't get out?", [(777, 'А если не выйдете')], ''),
    ('arkady', 'Видишь эти часы? Это швейцарское золото.', "See this watch? It's Swiss gold.", [(778, 'эти часы')], "'Вот видите' -> 'Видишь' (said to Lyosha); 'Это Швейцария. Золото.' (779-780) -> 'Это швейцарское золото.'"),
    ('arkady', 'Я их продам и куплю тебе приставку. Ну, согласен?', "I'll sell it and buy you a console. Well, deal?", [(781, 'Я их продам'), (783, 'Ну, согласен')], "'А тебе куплю' (782) -> 'и куплю тебе приставку'"),
    ('lyosha', 'Мама сказала, что вы все жулики.', "Mum said you're all crooks.", [(784, 'Мама сказала, что вы')], "'сволочи, вы все к жареным' -> 'все жулики' (clean)"),
    ('arkady', 'Допустим, я жулик. А ты жадина и не помогаешь людям в беде.', "All right, let's say I'm a crook. But you're greedy, and you don't help people in trouble.", [(785, 'допустим, я'), (785, 'а ты жадина'), (785, 'не помогаешь людям')], "'сволочь' -> 'жулик'; 'жлоб' dropped; 'которые в беде' -> 'в беде'"),
    ('arkady', 'Что, обиделся? Иди, иди.', 'What, are you offended? Go on, off you go.', [(786, 'Что, обиделся? Иди, иди')], "'Ну и чем ты лучше меня?' dropped"),
    ('lyosha', 'Вот. Я не жадина.', "Here. I'm not greedy.", [(792, 'Я не жадин')], "'Вот.' added: Lyosha comes back with the money; cue 792 has the slip 'жадин'"),
    ('arkady', 'Вижу, вижу, ты герой. Молодец.', "I see, I see, you're a hero. Well done.", [(793, 'Вижу, вижу, ты герой. Молодец')], ''),
]
WALK = [
    (0, None, "'Kids, give me some money, eh?' After 'give', the money takes the form for 'some': literally, 'give of money'. Yulia answers first."),
    (1, None, "'I haven't got any.' Literally, 'at me there isn't'. The same pattern as 'I have', with the word for 'there isn't'. So Arkady looks around the room."),
    (2, 'А у кого есть?', "'So who has?' Literally, 'and at whom is there?' Then he turns to the quiet boy on crutches."),
    (2, 'Так, Шнурок, есть же копилка?', "'Right, Shoelace, you've got a piggy bank, haven't you?' Shoelace is Arkady's cheeky nickname for skinny Lyosha. The little word in the middle turns the question into 'surely you have'."),
    (3, None, "'Mum and I are saving up for a games console.' Russian says 'we with mum', which means 'Mum and I'. Arkady gets interested."),
    (4, None, "'Really? And how much have you saved so far?' The word for saving has a little prefix here, which means the result: the money already in the bank."),
    (5, None, "'Seven hundred and fifty roubles. We've been saving for half a year.' Russian uses the present form for something that started in the past and is still going on. And the price?"),
    (6, None, "'And how much does the console cost?' The word for 'costs' is the third person form of 'to cost'."),
    (7, None, "'Five thousand roubles.' After five and above, the word takes the plural form for 'of': so 'five of thousands', 'five thousand of roubles'. Now Arkady has an offer."),
    (8, None, "'Listen, kid, I've got a business proposal.' The word for 'kid' literally means 'little one'. And here is the deal."),
    (9, None, "'You give five hundred roubles, and I buy you the best console in the world.' He promises in the present, as if it were already happening. Lyosha isn't a fool."),
    (10, None, "'And what if you don't get out?' He uses the polite 'you' with the grown-up. Arkady shows him his wrist."),
    (11, None, "'See this watch? It's Swiss gold.' In Russian, a watch is always plural, like 'scissors' in English. That's why the next line says 'them'."),
    (12, None, "'I'll sell it and buy you a console. Well, deal?' Both action words are one-time action words, so they're in the future: one complete action each. The last word, literally 'agreed?', is masculine, because Lyosha is a boy. But Lyosha remembers what his mum said."),
    (13, None, "'Mum said you're all crooks.' She means all the officials. Arkady turns it around."),
    (14, None, "'Let's say I'm a crook. But you're greedy, and you don't help people in trouble.' The word for 'greedy' here is a childish one, 'a greedy-guts'. 'People' takes the form for 'to', because you help to someone in Russian. Lyosha is hurt and walks out."),
    (15, None, "'What, are you offended? Go on, off you go.' Repeating the command makes it sound dismissive. But a moment later Lyosha is back, holding out his money."),
    (16, None, "'Here. I'm not greedy.' The same childish word, now with 'not' in front. He has proved his point."),
    (17, None, "'I see, I see, you're a hero. Well done.' The last word is the everyday praise for children, and for adults too."),
]
