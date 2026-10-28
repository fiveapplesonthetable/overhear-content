# Authoring module for kukhnya-s01e18-scene-15.
ID = 'kukhnya-s01e18-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 15
TITLE = 'Ошибочная бутылка  (The Wrong Bottle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "Senya is ill, and Max suspects the bar's fake cognac is to blame. At the same moment Barinov asks Kostya for a bottle of cognac, and Kostya hands him exactly the wrong one. Keep an eye on which bottle ends up on the table."
OPENER = 'Now the bottle mix-up, slowly.'
TRANSITION = 'Here it is again, mix-up and all.'
OUTRO = 'Kostya has to get a bottle back from the chef\'s table, which is easier said than done. Remember that in Russian a bottle stands: "butylka stoit". See you next time!'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, это просто ужас!', 'Kostya, this is just a nightmare!', [(285, 'просто')], ''),
    ('max', 'Сеня отравился нашим коньяком.', 'Senya got poisoned by our cognac.', [(281, 'что Сеня отравился этим коньяком.')], ''),
    ('kostya', 'О нет, что делать?', 'Oh no, what to do?', [], ''),
    ('barinov', 'Костя, дай мне бутылку коньяка.', 'Kostya, give me a bottle of cognac.', [(289, 'мне')], ''),
    ('barinov', 'Ту, которая стоит справа.', 'The one that stands on the right.', [], ''),
    ('kostya', 'Вот эту бутылку?', 'This bottle right here?', [(282, 'вот')], ''),
    ('barinov', 'Нет, дай мне другую. Да, эту.', 'No, give me another one. Yes, this one.', [(289, 'мне'), (289, 'мне')], ''),
    ('max', 'Шеф забрал наш коньяк!', 'Chef took our cognac!', [], ''),
    ('max', 'Надо забрать эту бутылку назад.', 'We need to take this bottle back.', [(291, 'Надо забрать бутылку, Костян.')], ''),
    ('kostya', 'Я не могу к нему подойти.', 'I can not approach him.', [(293, 'Я же не могу к ней подойти.')], ''),
    ('max', 'Давай, Костя, ты должен.', 'Come on, Kostya, you must.', [(294, 'Давай, Костян, давай, дружок.')], ''),
    ('kostya', 'Хорошо, я пойду.', 'All right, I will go.', [], ''),
]
WALK = [
    (0, None, '\'Kostya, this is just awful!\' "Uzhas", horror, is the everyday way to say something is awful.'),
    (1, None, '\'Senya\'s been poisoned by our cognac.\' "Otravilsya" ends in "-sya": \'poisoned himself\'. The cause takes the \'by\' ending: "nashim konyakom".'),
    (2, None, '\'Oh no, what do we do?\' "Chto delat?", \'what to do?\', needs no \'we\' at all. It\'s also the title of a famous Russian novel.'),
    (3, None, '\'Kostya, give me a bottle of cognac.\' "Day", give!, is the friendly form. No \'of\' needed: "butylku konyaka".'),
    (4, None, '\'The one on the right.\' In Russian a bottle stands, "stoit", rather than sits. "Sprava", on the right.'),
    (5, None, '\'This bottle here?\' "Vot" points: here it is. "Butylka" becomes "butylku" as the thing handed over.'),
    (6, None, '\'No, give me another. Yes, that one.\' "Druguyu", another, ends the same way as "butylku", the bottle it stands for.'),
    (7, None, '\'The chef\'s taken our cognac!\' "Zabral", took away: the "za-" means he took it for himself.'),
    (8, None, '\'We need to get this bottle back.\' "Nazad", back, finishes the line. "Nado zabrat", \'needed to take away\'.'),
    (9, None, '\'I can\'t just walk up to him.\' "Podoyti", to go up to: "pod-" means up close. After "k", to, "emu" becomes "nemu".'),
    (10, None, '\'Come on, Kostya, you have to.\' "Davay", literally \'give\', is the Russian \'come on\'. "Dolzhen", must, is the form for a man.'),
    (11, None, '\'All right, I\'ll go.\' "Poydu", I\'ll go, on foot. "Khorosho" here just means okay.'),
]
