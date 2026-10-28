# Authoring module for kukhnya-s01e06-scene-05.
ID = 'kukhnya-s01e06-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = 'Бритьё рук  (Shaving Arms)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "In the cooks' changing room at Claude Monet, Senya and Fedya, the two kitchen pranksters, have a new victim: Max, who has only just joined. They tell him a health inspection is coming and that cooks have to shave their arms. It's in Russian first, and you're about to hear a story that is complete nonsense."
OPENER = 'Now through it slowly. Notice how serious the two of them sound.'
TRANSITION = "Here's the whole prank again, without stopping."
OUTRO = '"Brit", to shave, and "britva", razor, aren\'t words you\'ll need every day, but "da ladno", come on, and "gluposti", nonsense, are. See you next time.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Привет, парни! Как ваши дела?', 'Hello, guys! How are your things?', [(33, 'Салют'), (34, 'Как сам')], ''),
    ('fedya', 'Сеня, ты скоро? Мне нужна пена!', 'Senya, are you nearly done? I need the foam!', [(35, 'ты скоро, мне пена нужна')], ''),
    ('senya', 'Сейчас побрею правую руку и всё.', "I will just shave my right arm, and that's it.", [(36, 'Сейчас добрею, руку правую, все')], ''),
    ('max', 'А что вы делаете? Руки бреете?', 'And what are you doing? Shaving your arms?', [(37, 'А вы что делаете, руки бреете')], ''),
    ('fedya', 'Сегодня пятнадцатое число, большая санитарная проверка!', 'Today is the fifteenth, a big sanitary inspection!', [(39, 'Сегодня 15-е число, проверка')], ''),
    ('senya', 'Волосы не должны попасть в еду!', 'Hair must not fall into the food!', [(38, 'если волосы в еду попадут')], ''),
    ('max', 'Да ладно вам, это же глупости!', 'Come on, this is complete nonsense!', [(40, 'Да ладно, это же идиотизм')], ''),
    ('fedya', 'Это строгое правило санитарной инспекции.', 'This is a strict rule of the sanitary inspection.', [(42, 'А бритье рук — это требование санэпидемстанции')], ''),
    ('senya', 'Найдут один волос — сразу уволят!', "If they find even one hair — you'll be fired immediately!", [(43, 'Волосочек найдут, сразу уволят')], ''),
    ('max', 'Почему вы меня не предупредили раньше?', "Why didn't you warn me earlier?", [(44, 'хотя бы предупредили')], ''),
    ('max', 'У меня с собой даже бритвы нет.', "I don't even have a razor with me.", [(44, 'у меня даже бритвы нет')], ''),
    ('fedya', 'Ладно, огузок, возьми мою бритву.', 'All right, runt, take my razor.', [(45, 'Ну, ладно, возьми мою')], ''),
    ('fedya', 'Для рук мне бритву совсем не жалко.', "For arms I don't mind the razor at all.", [(46, 'не жалко')], ''),
    ('max', 'Спасибо, Федя, я быстро всё побрею.', 'Thank you, Fedya, I will quickly shave everything.', [(47, 'Спасибо')], ''),
]
WALK = [
    (0, None, '\'Hello, guys! How are your things?\' "Parni", guys, is more than one "paren", young man. "Kak dela", \'how are things\', is the question for a friend, and Max says "vashi", your, because he\'s talking to two people.'),
    (1, None, '\'Senya, are you nearly done? I need the foam!\' "Ty skoro", \'you soon?\', has no verb at all, and it\'s exactly how you\'d hurry someone. "Mne nuzhna pena" is literally \'to me is needed foam\'.'),
    (2, None, '\'I will just shave my right arm, and that\'s it.\' "Ruka" is both \'arm\' and \'hand\'; Russian doesn\'t split them. "I vsyo", \'and all\', means \'and that\'s it\'.'),
    (3, None, '\'And what are you doing? Shaving your arms?\' "Breete", you shave, comes from "brit", which changes its stem: "ya breyu", "vy breete". Max\'s second question is just two words and a rising voice.'),
    (4, None, '\'Today is the fifteenth, a big sanitary inspection!\' Russians give a date with "chislo", number: "pyatnadtsatoe chislo", \'the fifteenth number\'. "Proverka", check, is what Russians call any inspection.'),
    (5, None, '\'Hair must not fall into the food!\' "Volosy", hair, is plural in Russian, like \'hairs\', so "dolzhny", must, is plural too. "V edu", into the food, takes -u because it\'s movement into.'),
    (6, None, '\'Come on, this is complete nonsense!\' "Da ladno vam" is \'come off it, you two\'. "Gluposti", nonsense, is literally \'stupidities\', more than one "glupost", from "glupyy", stupid.'),
    (7, None, '\'This is a strict rule of the sanitary inspection.\' "Inspektsiya" becomes "inspektsii" for \'of the inspection\'. Fedya sounds like he\'s reading from an official notice.'),
    (8, None, '\'If they find even one hair — you\'ll be fired immediately!\' "Naydut" and "uvolyat", they\'ll find and they\'ll fire, come with no \'they\': nobody in particular, just \'the authorities\'. One hair is "volos", without the -y.'),
    (9, None, '\'Why didn\'t you warn me earlier?\' "Predupredili", you warned, starts with pred-, \'before\', so a warning is telling someone ahead of time. The -li ending is the past for "vy".'),
    (10, None, '\'I don\'t even have a razor with me.\' "U menya net" is \'I don\'t have\', and after "net" the razor changes: "britva" becomes "britvy". "S soboy", with me, is literally \'with oneself\'.'),
    (11, None, '\'All right, runt, take my razor.\' "Vozmi", take, is the command from "vzyat". "Moyu britvu", my razor, both end in -u, the ending for the thing taken.'),
    (12, None, '\'For arms I don\'t mind the razor at all.\' "Mne ne zhalko", \'to me not a pity\', is how you say \'I don\'t begrudge it\'. "Sovsem ne" is \'not at all\'.'),
    (13, None, '\'Thank you, Fedya, I will quickly shave everything.\' "Pobreyu", I\'ll shave, is the po- partner of "brit", the one for a job you finish. Max thanks the man who has just tricked him.'),
]
