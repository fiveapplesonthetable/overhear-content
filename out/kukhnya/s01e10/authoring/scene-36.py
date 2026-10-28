# Authoring module for kukhnya-s01e10-scene-36.
ID = 'kukhnya-s01e10-scene-36'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 36
TITLE = 'Неожиданная новость  (Unexpected News)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'tanya': 'Таня', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "A new customer sits at the corner table: Tanya, Vika's sister and Alisa's mother. She has heard something from the chef. See what you can catch."
OPENER = "Here's what is going on, line by line."
TRANSITION = 'Now you can hear it all again.'
OUTRO = 'The rumour has come from Barinov, and Vika knows it is not true. She has a few words to say to him. Until the next scene.'
CLOSING = ('tanya', 'Пока!')
STORY = [
    ('tanya', 'Здравствуй, Вика! Я сяду за угловой столик.', 'Hello, Vika! I will sit at the corner table.', [(254, 'Угловой столик')], ''),
    ('vika', 'Привет, Таня! Что случилось?', 'Hi, Tanya! What happened?', [(253, 'проходите, пожалуйста')], ''),
    ('tanya', 'Почему ты мне совсем ничего не рассказала?', "Why didn't you tell me anything at all?", [(255, 'почему ты мне не позвонил')], ''),
    ('vika', 'Таня, я не понимаю твоих странных вопросов.', "Tanya, I don't understand your strange questions.", [(256, 'Что случилось')], ''),
    ('tanya', 'Ты должна была сразу позвонить родной сестре!', 'You should have immediately called your own sister!', [(255, 'наконец-то')], ''),
    ('vika', 'Объясни мне спокойно, что вообще произошло?', 'Explain to me calmly, what happened at all?', [(256, 'Что случилось')], ''),
    ('tanya', 'Ты беременна, а я узнаю об этом последней!', 'You are pregnant, and I find out about it last!', [(257, 'Ты же беременна')], ''),
    ('vika', 'С чего ты вообще взяла такую глупость?', 'Where did you get such nonsense at all?', [(258, 'С чего ты взяла')], ''),
    ('tanya', 'Мне об этом лично сказал шеф Витя!', 'Chef Vitya told me about this personally!', [(258, 'Мне Витя сказал')], ''),
    ('vika', 'Виктор опять придумал эту безумную историю!', 'Viktor again made up this insane story!', [(258, 'Витя сказал')], ''),
    ('tanya', 'Значит, ты совсем не ждёшь ребёнка?', 'So, you are not expecting a baby at all?', [(257, 'беременна')], ''),
    ('vika', 'Конечно нет, это просто неправда!', 'Of course not, it is simply not true!', [(258, 'С чего ты взяла')], ''),
    ('tanya', 'Тогда тебе нужно срочно поговорить с Виктором.', 'Then you need to urgently speak with Viktor.', [(258, 'Мне Витя сказал')], ''),
]
WALK = [
    (0, None, '\'Hello, Vika! I will sit at the corner table.\' "Zdravstvuy" is the long hello for one person you know. "Syadu" is "I will sit down". Russians sit "za" a table, "behind" it: "za uglovoy stolik", as in Kostya\'s "Gost za pyatym stolikom".'),
    (1, None, '\'Hi, Tanya! What happened?\' "Privet" is the informal hello. "Chto sluchilos?" is "what happened?", the usual question when something seems wrong. Vika can see it in her sister\'s face.'),
    (2, None, '\'Why didn\'t you tell me anything at all?\' Russian has "skazat", "to say", and "rasskazat", "to tell", for news or a story, as in Max\'s "Mne tolko chto rasskazali samuyu bezumnuyu novost". "Nichego ne rasskazala" is the double negative.'),
    (3, None, '\'Tanya, I don\'t understand your strange questions.\' After "ne ponimayu", "voprosy" can turn into "voprosov": "tvoikh strannykh voprosov". "Strannye" is "strange". Vika has no idea what Tanya means.'),
    (4, None, '\'You should have immediately called your own sister!\' "Dolzhna byla" is "had to", "should have": "dolzhna" plus "byla", "was". "Rodnoy sestre" is "to your own sister"; "rodnoy" means "related by blood", as in Vika\'s "eyo rodnoy papa".'),
    (5, None, '\'Explain to me calmly, what happened at all?\' "Obyasni" is "explain", from Barinov\'s "Tanya, podozhdi, ya vsyo obyasnyu!". "Spokoyno" is "calmly". "Proizoshlo" is "happened".'),
    (6, None, '\'You are pregnant, and I find out about it last!\' This is Vika\'s complaint about the stove, word for word: "Pochemu ya uznayu ob etom posledney?". "Beremenna" is "pregnant". Now it is Tanya who finds out last.'),
    (7, None, '\'Where did you get such nonsense at all?\' "S chego ty vzyala" is "from what did you take", meaning "what makes you think so". "Glupost", "nonsense", comes from "glupy", "stupid".'),
    (8, None, '\'Chef Vitya told me about this personally!\' "Lichno" is "personally", Barinov\'s word in "Ya lichno otvyoz eyo v servis". The person comes last: "lichno skazal shef Vitya", "personally said chef Vitya". Tanya names her source.'),
    (9, None, '\'Viktor again made up this insane story!\' "Pridumal" is "made up". "Bezumnaya", "insane", is "bez" plus "um", "without mind", heard in Max\'s "bezumnuyu novost". "Opyat" is "again".'),
    (10, None, '\'So, you are not expecting a baby at all?\' "Znachit" is "so", literally "it means". "Zhdat rebyonka" is "to expect a baby", the phrase in Max\'s plan to wait for the baby together.'),
    (11, None, '\'Of course not, it is simply not true!\' "Nepravda" is "untruth": "ne" plus "pravda". "Konechno net" is "of course not". Vika denies it in the plainest way.'),
    (12, None, '\'Then you need to urgently speak with Viktor.\' "Pogovorit s Viktorom" is "to talk with Viktor", the verb in Vika\'s "Nam nado seryozno pogovorit". "Srochno" is "urgently". "Tebe nuzhno" is "to you it is needed".'),
]
