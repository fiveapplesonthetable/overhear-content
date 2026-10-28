# Authoring module for kukhnya-s01e11-scene-24.
ID = 'kukhnya-s01e11-scene-24'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 24
TITLE = 'Трус и увольнение  (The Coward and the Firing)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'The chef has heard what Kostya did, and he is about to deal with it. Nastya apologises to Kostya first, in the kitchen corridor. Just listen, and see how much you pick up.'
OPENER = 'This time, with explanations.'
TRANSITION = 'Once more, at the pace of a real conversation.'
OUTRO = "Kostya is fired, and Nastya wants him back. The two of them have only a few hours before the critic's article comes out. Back soon."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Костя, подожди секунду, выслушай меня пожалуйста.', 'Kostya, wait a second, listen to me please.', [], ''),
    ('nastya', 'Прости, что я глупо назвала тебя трусом.', 'Forgive me for stupidly calling you a coward.', [(312, 'Прости, что назвала тебя трусом.')], ''),
    ('kostya', 'Ты поступила со мной очень несправедливо.', 'You treated me very unfairly.', [], ''),
    ('nastya', 'Я сильно ошиблась и очень сожалею об этом.', 'I was very mistaken and deeply regret it.', [], ''),
    ('barinov', 'Костя, ты уволен, быстро собирай свои вещи!', 'Kostya, you are fired, quickly pack your things!', [(313, 'Костя, ты уволец, собирай вещи.')], ''),
    ('kostya', 'Шеф, неужели вы выгоняете меня с работы?', 'Chef, are you really driving me out of work?', [], ''),
    ('barinov', 'Ты устроил скандал с важным ресторанным критиком!', 'You caused a scandal with an important restaurant critic!', [], ''),
    ('nastya', 'Шеф, это я во всём виновата!', 'Chef, it is I who am to blame for everything!', [], ''),
    ('barinov', 'Мне всё равно, бармен уходит прямо сейчас.', 'I do not care, the bartender leaves right now.', [], ''),
    ('kostya', 'Хорошо, шеф, я сейчас же сниму форму.', 'All right, chef, I will take off the uniform immediately.', [], ''),
    ('nastya', 'Мы не можем потерять лучшего бармена ресторана.', "We cannot lose the restaurant's best bartender.", [], ''),
    ('barinov', 'У нашего ресторана сейчас будут огромные проблемы.', 'Our restaurant will have huge problems now.', [(319, 'Я думаю, у нас большие проблемы.')], ''),
    ('nastya', 'Мы должны всё исправить до выхода статьи.', 'We must fix everything before the article comes out.', [], ''),
]
WALK = [
    (0, None, '\'Kostya, wait a second, listen to me please.\' "Vyslushay" has the prefix vy-, so Nastya asks him to listen to the end. "Podozhdi" is "wait". She uses "ty" with him, and she is gentle.'),
    (1, None, '\'Forgive me for stupidly calling you a coward.\' After "nazvala", "called", the coward becomes "trusom". "Prosti", "forgive", is what Kostya said to her earlier: "Nastya, nu prosti menya za vcherashnee". Now it is her turn.'),
    (2, None, '\'You treated me very unfairly.\' "Nespravedlivo" is "ne spravedlivo", "not fairly", made from the word for justice. "Postupila", "acted", is the verb from Nastya\'s own line: "tak postupayut zlye lyudi". Kostya is hurt.'),
    (3, None, '\'I was very mistaken and deeply regret it.\' "Oshiblas", "was mistaken", has -las for a woman. "Sozhaleyu", "I regret", is related to "pozhaleesh", in Barinov\'s "Dmitry, ty pozhaleesh ob etom!". Nastya apologises in full.'),
    (4, None, '\'Kostya, you are fired, quickly pack your things!\' "Uvolen" is "fired", a short passive form. "Sobiray", "pack", is literally "collect". "Veshchi" is "things", as in Vika\'s "vazhnuyu veshch" to Max. Barinov is blunt.'),
    (5, None, '\'Chef, are you really driving me out of work?\' "Vygonyaesh" is "drive out", with vy- for "out". "S raboty" is "from work". "Neuzheli" is "can it really be". Kostya cannot believe it.'),
    (6, None, '\'You caused a scandal with an important restaurant critic!\' "Ustroil skandal", "arranged a scandal", is the Russian way to say "made a scene". "S vazhnym kritikom" is "with an important critic". Barinov is stern.'),
    (7, None, '\'Chef, it is I who am to blame for everything!\' "Vinovata", "guilty", is a short form that ends in -a for a woman. "Vo vsyom" is "in everything". Nastya takes the blame, and it is a brave thing to do.'),
    (8, None, '\'I do not care, the bartender leaves right now.\' "Mne vsyo ravno" is the idiom Barinov used about the critic in the soup scene. "Barmen" comes from English "barman". "Pryamo seychas" is "right now".'),
    (9, None, '\'All right, chef, I will take off the uniform immediately.\' "Forma" is the Russian for "uniform", the same word as "form" or "shape". "Snimu" is "I will take off". Kostya accepts, with dignity.'),
    (10, None, '\'We cannot lose the restaurant\'s best bartender.\' "Poteryat", "lose", is the verb in Barinov\'s "poteryala svoyu glupuyu golovu". "Luchshego", "best", grows from "luchshe", "better". Nastya says "my", "we".'),
    (11, None, '\'Our restaurant will have huge problems now.\' "U nashego restorana budut", "at our restaurant will be", is the pattern for "will have". "Ogromnye" is "huge". Barinov knows what the article could say.'),
    (12, None, '\'We must fix everything before the article comes out.\' "Do vykhoda statyi" is "before the exit of the article": "vykhod", "exit", is the word for a publication coming out. "Ispravit" is "to fix". Nastya sets the deadline.'),
]
