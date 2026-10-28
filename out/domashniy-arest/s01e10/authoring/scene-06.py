# Authoring module for domashniy-arest-s01e10-scene-06.
ID = 'domashniy-arest-s01e10-scene-06'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 6
TITLE = "Приказ начальника  (The Chief's Order)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'lyova': 'Лёва', 'warden': 'Начальник'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = "A moment later, the FSB chief severely scolds agent Sokolov for his lack of results. Sokolov rashly proposes using force to extract the hidden millions, but the chief cuts him off. Instead of violent tactics, the chief orders Sokolov on a routine surveillance post outside Anikeyev's former residence. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine the chief's stern order line by line. The FSB chief reprimands Sokolov for his crude methods."
TRANSITION = "Now let's listen to the chief and Sokolov's confrontation once more without pauses."
OUTRO = 'Rebuked by his superior, Sokolov is dispatched to a tedious stakeout. See you next time!'
CLOSING = ('warden', 'Пока!')
STORY = [
    ('warden', 'Вы совсем не умеете работать!', 'You do not know how to work at all!', [(186, 'Потому что вы мышей не ловите')], 'idiom softened to standard A1'),
    ('warden', 'Скоро вас обоих просто уволят.', 'Soon both of you will simply be fired.', [(188, 'Вот вас снимут')], ''),
    ('lyova', 'Я могу быстро найти эти деньги.', 'I can quickly find that money.', [(190, 'А я быстро эти бабки вытащу')], ''),
    ('warden', 'И как же ты их найдёшь?', 'And how exactly will you find it?', [(191, 'Да ты что, и как же')], ''),
    ('lyova', 'С помощью силы и угроз!', 'With the help of force and threats!', [(192, 'Силовыми методами'), (194, 'угрозы')], ''),
    ('warden', 'Соколов, тебе детского сада мало?', "Sokolov, wasn't the kindergarten enough for you?", [(195, 'Соколов, тебе детского сада мало')], ''),
    ('warden', 'Ты находишься в моём подчинении.', 'You are under my command.', [(197, 'Ты находишься в прямом моем подчинении')], ''),
    ('warden', 'Ноги со стола быстро убери!', 'Take your feet off the table quickly!', [(199, 'ноги убрал')], ''),
    ('warden', 'Ты сейчас идёшь на задание.', 'You are going on an assignment now.', [(200, 'сейчас идешь')], ''),
    ('warden', 'Установи наблюдение за домом Аникеева.', "Set up surveillance on Anikeyev's house.", [(200, 'устанавливаешь наблюдение'), (201, 'За бывшим домом Аникиева')], ''),
    ('lyova', 'Вы что, просто сливаете меня?', 'Are you just throwing me under the bus?', [(205, 'Вы что, меня сливаете')], ''),
    ('warden', 'Да, но приказы не обсуждаются!', 'Yes, but orders are not discussed!', [(206, 'Да'), (207, 'Но приказы не обсуждаются')], ''),
    ('lyova', 'Ладно, я всё понял.', 'Fine, I understood everything.', [(208, 'Ладно')], ''),
    ('warden', 'Не ладно, а так точно!', 'Not fine, but yes sir!', [(209, 'Не ладно, а есть')], 'military response'),
]
WALK = [
    (0, None, "'You do not know how to work at all!' Fed up with empty-handed reports, the FSB boss tears into his agents."),
    (1, None, "'Soon both of you will simply be fired.' In Russian, saying \"they will fire you\" without naming who makes the threat sound like fate."),
    (2, None, "'I can quickly find that money.' Ever the hothead, Sokolov brags that he can crack the case in no time."),
    (3, None, "'And how exactly will you find it?' Knowing Sokolov's track record, his superior asks the question with heavy skepticism."),
    (4, None, "'With the help of force and threats!' Being subtle is not in Lyova's playbook; he just wants to rough people up."),
    (5, None, "'Sokolov, wasn't the kindergarten enough for you?' Earlier in the season, Lyova's undercover stint at a daycare ended in complete farce."),
    (6, None, "'You are under my command.' Pulling rank, the boss reminds his reckless operative who gives the orders here."),
    (7, None, "'Take your feet off the table quickly!' Even while being chewed out, Sokolov was lounging like he owned the office."),
    (8, None, "'You are going on an assignment now.' Sending him out the door right this minute leaves zero room for backtalk."),
    (9, None, "'Set up surveillance on Anikeyev's house.' Instead of action, he gets stuck watching the mayor's empty mansion."),
    (10, None, "'Are you just throwing me under the bus?' Literally \"draining me away\", a vivid Russian slang word for dumping someone off a case."),
    (11, None, "'Yes, but orders are not discussed!' Notice the brutal honesty: the boss doesn't even deny sidelining him."),
    (12, None, "'Fine, I understood everything.' Grumbling like a teenager, Lyova slouches toward the door."),
    (13, None, "'Not fine, but yes sir!' Casual \"ladno\" won't fly in uniform; the boss demands a crisp military \"tak tochno\"."),
]
