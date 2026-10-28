# Authoring module for kukhnya-s03e15-scene-09.
ID = 'kukhnya-s03e15-scene-09'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 15
SCENE = 9
TITLE = 'Перепутанные телефоны и ключи  (Mixed-Up Phones and Keys)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.15'
SOURCE_FILE = 'sources/kukhnya/s03/e15.ru.srt'
INTRO = "In the corridor, Max bitterly accuses Vika of ruining their relationship by sleeping with Nagiyev. Then Kostya realizes he accidentally took Max's identical phone earlier—meaning Vika texted Kostya's number, not Max's! Listen first."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Max realizes Vika only asked 'Who is this?' because he texted her from Kostya's phone! And in Scene Ten, Chef Barinov drops an even bigger bombshell on Max. Until next time!"
CLOSING = ('max', 'Увидимся!')
STORY = [
    ('max', 'Красивый букет, это очередной поклонник подарил?', 'Nice bouquet, did another admirer give it to you?', [(127, 'Очередной поклонник подарил')], 'adapted'),
    ('max', 'Ты уже совсем забыла про меня в новой жизни.', 'You have completely forgotten about me in your new life.', [(128, 'Совсем забыла про меня')], 'adapted'),
    ('max', 'Напомню, меня зовут Макс, я работаю поваром.', 'Let me remind you, my name is Max, I work as a cook.', [(129, 'Напомню, меня зовут Макс. Работаю поваром')], 'adapted'),
    ('max', 'Что, угробила наши отношения и теперь уходишь?', 'What, you ruined our relationship and now you are leaving?', [(130, 'угробила наши отношения')], 'adapted'),
    ('vika', 'Это я угробила наши отношения, а кто?', 'I ruined our relationship, and who else?', [(131, 'Это я'), (132, 'Угробила. А кто')], 'adapted'),
    ('max', 'Во всяком случае, я с Нагиевым не спал!', 'In any case, I did not sleep with Nagiyev!', [(133, 'Я с Нагиевым не спал')], 'adapted'),
    ('vika', 'Макс, прекрати, я больше не хочу ничего слышать!', 'Max, stop it, I do not want to hear anything more!', [(135, 'Макс, прекрати, я больше не хочу ничего слышать')], 'adapted'),
    ('kostya', 'Макс, Виктория Сергеевна свои ключи забыла, позвони ей!', 'Max, Viktoria Sergeyevna forgot her keys, call her!', [(136, 'Виктория Сергеевна ключи забыла'), (137, 'позвони')], 'adapted'),
    ('kostya', 'Чёрт, я опять перепутал, это Макса телефон!', "Damn, I mixed them up again, this is Max's phone!", [(138, 'я опять перепутал там Макса телефон')], 'adapted'),
    ('max', 'Виктория Сергеевна, хорошо, что вы не уехали, вы ключи забыли.', 'Viktoria Sergeyevna, it is a good thing you did not leave, you forgot your keys.', [(141, 'Виктория Сергеевна, хорошо, что вы не уехали, вы ключи забыли')], 'adapted'),
    ('max', 'Подожди, значит, ты не удалила мой номер?', 'Wait, so you did not delete my number?', [(143, 'Ты не удалила мой номер')], 'adapted'),
    ('vika', 'Прощай навсегда, Макс!', 'Farewell forever, Max!', [(144, 'Прощай'), (145, 'Макс')], 'adapted'),
]
WALK = [
    (0, None, "'Nice bouquet, did another admirer give it to you?' Max probes plainly what Vika is actually getting at here."),
    (1, None, '\'You have completely forgotten about me in your new life.\' Discussing the life with Vika, Max chooses "zhizni" ("life", from the root "zhizn") so Vika hears the exact meaning.'),
    (2, None, '\'Let me remind you, my name is Max, I work as a cook.\' Discussing a cook before Vika, Max centers the thought on "povarom" ("as a cook", from "povar") without wasting a word.'),
    (3, None, "'What, you ruined our relationship and now you are leaving?' Max checks calmly why things suddenly took this turn between them."),
    (4, None, '\'I ruined our relationship, and who else?\' Emphasizing the relations in this beat, Vika brings in "otnosheniya" ("relations, relationship", from "otnosheniye") as the key Russian word here.'),
    (5, None, '\'In any case, I did not sleep with Nagiyev!\' Emphasizing the case before Vika, Max reaches for the Russian word "sluchaye" ("case, event", built from "sluchay") right at the center of the line.'),
    (6, None, "'Max, stop it, I do not want to hear anything more!' Vika pushes back boldly with a smile, refusing to let the moment slip past."),
    (7, None, '\'Max, Viktoria Sergeyevna forgot her keys, call her!\' Mentioning the keys with Max, Kostya uses "klyuchi" ("the keys", from "klyuch") to make the point stick.'),
    (8, None, '\'Damn, I mixed them up again, this is Max\'s phone!\' Mentioning the phone in the exchange, Kostya brings in "telefon" ("phone") to make the meaning unmistakable.'),
    (9, None, "'Viktoria Sergeyevna, it is a good thing you did not leave, you forgot your keys.' Max continues plainly during the talk, before Kostya can change the subject."),
    (10, None, '\'Wait, so you did not delete my number?\' Emphasizing his number beside Vika, Max reaches for the Russian word "podozhdi" ("wait", built from "podozhdat") right at the center of the line.'),
    (11, None, "'Farewell forever, Max!' Turning plainly on the spot, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
]
