# Authoring module for kukhnya-s01e17-scene-02.
ID = 'kukhnya-s01e17-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 2
TITLE = 'До встречи в Аркобалено  (See You at Arcobaleno)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "Still at the market, Barinov and Senya run into Elena Pavlovna, the head chef of Arcobaleno, the rival restaurant next door. She agrees about the old fish, then reminds Barinov that he owes her a return visit. Here is the meeting in Russian."
OPENER = 'Now the meeting again, one line at a time.'
TRANSITION = "Here's the whole meeting once more, all the way through."
OUTRO = 'Senya protests a little too much about a place he has never been. Keep "do vstrechi", until the meeting: it is the goodbye for when you know you will see someone again. See you next time!'
CLOSING = ('elena', 'До встречи!')
STORY = [
    ('elena', 'А вот тут я с вами согласна.', 'Well, there I agree with you.', [(15, 'А вот тут я с вами согласна.')], ''),
    ('barinov', 'Да, пять дней. Для вашего ресторана это как раз.', 'Yes, five days. Just right for your restaurant.', [(16, 'Пять дней? Да.'), (17, 'Ну, для вашего ресторана это как раз.')], ''),
    ('elena', 'Вы думаете? Тогда во вторник я вам её приготовлю.', 'You think so? Then I will cook it for you on Tuesday.', [(18, 'Вы думаете? Тогда во вторник я вам ее и приготовлю.')], ''),
    ('elena', 'До встречи.', 'See you then.', [(19, 'До встречи.')], ''),
    ('barinov', 'Какой ещё встречи?', 'See me when?', [(19, 'Да какой еще встречи?')], ''),
    ('elena', 'Вы же к нам собираетесь с ответным визитом.', 'You are paying us a return visit, are you not?', [(20, 'Вы же к нам собираетесь с ответным визитом')], ''),
    ('elena', 'Мне так сказали, во всяком случае.', 'That is what I was told, anyway.', [(21, 'Мне так сказали, во всяком случае.')], ''),
    ('elena', 'Так что до встречи в Аркобалено.', 'So, see you at Arcobaleno.', [(22, 'Так что до встречи, Варкабалена.')], ''),
    ('barinov', 'Вот чёрт, делать мне больше нечего.', 'Oh, damn, as if I had nothing better to do.', [(23, 'Вот чёрт, делать мне больше нечего.')], ''),
    ('senya', 'На самом деле, шеф, там очень даже ничего.', 'Actually, chef, it is not bad at all there.', [(24, 'Ну, на самом деле, шеф, там очень даже ничего.')], ''),
    ('barinov', 'А ты откуда знаешь? Ты что, был в Аркобалено?', 'And how would you know? What, have you been to Arcobaleno?', [(25, 'Да ты-то откуда знаешь?'), (26, 'Ты что, был в Варкабалена?')], ''),
    ('senya', 'Я? Нет, конечно.', 'Me? No, of course not.', [(27, 'Что, я?'), (28, 'Да нет, конечно.')], ''),
    ('senya', 'Мне просто друг рассказывал.', 'A friend just told me about it.', [(29, 'Просто мне друг рассказывал')], ''),
    ('senya', 'Я потом с ним даже общаться перестал.', 'I even stopped talking to him after that.', [(30, 'Я вообще после этого с ним даже общаться перестал.')], ''),
    ('barinov', 'Да ладно, я просто спросил.', 'Oh, relax, I was just asking.', [(32, 'Да ладно, я так просто спросил.')], ''),
]
WALK = [
    (0, None, '\'Well, there I agree with you.\' "Soglasna" ends in "-a" because Elena is a woman; Barinov would say "soglasen". "S vami" is "with you", the polite form she keeps for her rival.'),
    (1, None, '\'Yes, five days. Just right for your restaurant.\' "Kak raz" means "exactly right" or "just the thing", and here it is pure sarcasm: old fish suits her restaurant.'),
    (2, None, '\'You think so? Then I\'ll cook it for you on Tuesday.\' "Vo vtornik" is "on Tuesday": days of the week take "v", which turns into "vo" before "vt". "Eyo" here is "her", meaning the fish.'),
    (3, None, '\'See you then.\' "Do vstrechi" is literally "until the meeting". It is the goodbye you use when the next meeting is already planned.'),
    (4, None, '\'See me when?\' Barinov throws her own word back: "kakoy eshchyo vstrechi?", what meeting is that? "Kakoy eshchyo" before a noun is an indignant "what on earth".'),
    (5, None, '\'You\'re paying us a return visit, aren\'t you?\' "Otvetny vizit" is a return visit, from "otvet", answer. "Vy zhe" with "zhe" means "surely you are", a reminder rather than a question.'),
    (6, None, '\'That\'s what I was told, anyway.\' "Mne tak skazali" is "to me so they said", with no "they" at all. The plural ending hides who did the telling.'),
    (7, None, '\'So, see you at Arcobaleno.\' "Tak chto" means "so" when it draws a conclusion. Foreign names ending in "-o", like Arcobaleno, never change their ending in Russian.'),
    (8, None, '\'Damn, as if I had nothing better to do.\' "Delat mne bolshe nechego" is literally "to do, to me, nothing more". Russians use it to grumble about a chore they did not ask for.'),
    (9, None, '\'Actually, chef, it\'s not bad at all there.\' "Nichego" usually means "nothing", but "ochen dazhe nichego" means "really rather good". Context decides which one you hear.'),
    (10, None, '\'And how would you know? What, have you been to Arcobaleno?\' "Otkuda" is "from where"; "otkuda ty znaesh" asks where your knowledge comes from. "Byl" is the past of "to be", and its bare ending means a man is speaking.'),
    (11, None, '\'Me? No, of course not.\' "Konechno", of course, is said "koneshno": the "ch" sounds like "sh" in this word. Senya says it a little too fast.'),
    (12, None, '\'A friend just told me about it.\' "Rasskazyval" is the long, unfinished kind of past: the friend talked about it, maybe more than once. "Mne" is "to me".'),
    (13, None, '\'I even stopped talking to him after that.\' "Perestal" means "stopped", and the next verb stays in its dictionary form, "obshchatsya", to talk to each other.'),
    (14, None, '\'Oh, relax, I was just asking.\' "Da ladno" is a shrug, roughly "come on" or "never mind". "Prosto" means "simply", here "just".'),
]
