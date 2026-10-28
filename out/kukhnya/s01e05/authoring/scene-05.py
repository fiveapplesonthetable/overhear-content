# Authoring module for kukhnya-s01e05-scene-05.
ID = 'kukhnya-s01e05-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = 'Кулинарный спор  (A Culinary Bet)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Earlier that morning, in the Claude Monet kitchen, Max turns up late again and Chef Barinov is waiting for him. Then Fedya, another cook, starts needling Max about his cooking, and it ends in a bet. Listen in Russian first; the odd missed word doesn't matter."
OPENER = "Now line by line, from Max's greeting. Notice that nobody in this kitchen says anything nice."
TRANSITION = 'And now the whole morning without stopping.'
OUTRO = 'Starting a bet in Russian takes one word, "sporim", and "davay" before a verb is how you suggest anything at all. Max and Fedya now have something to prove.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Доброе утро, шеф!', 'Good morning, Chef!', [(69, 'Доброе утро, шеф')], ''),
    ('barinov', 'Огузок, ты постоянно опаздываешь на работу.', 'Runt, you are constantly late for work.', [(69, 'Агузик'), (70, 'Ты постоянно'), (71, 'ты опять опоздал')], ''),
    ('max', 'Шеф, мне не выдали форму вовремя.', 'Chef, they did not issue my uniform on time.', [(72, 'мне'), (72, 'форму не выдало')], ''),
    ('barinov', 'Хватит оправданий, быстро иди работать!', 'Enough excuses, quickly go to work!', [(68, 'За работу')], ''),
    ('fedya', 'Ты так же плохо шутишь, как и готовишь.', 'You joke as badly as you cook.', [(78, 'Ты так же'), (78, 'шутишь, как и готовишь')], ''),
    ('max', 'Я не понял твоей шутки, Федя.', "I didn't understand your joke, Fedya.", [(79, 'Не понял')], ''),
    ('fedya', 'Это обычное состояние для твоего мозга.', 'This is a normal state for your brain.', [(79, 'привычное состояние для твоего мозга')], ''),
    ('max', 'Ты хочешь сказать, что я плохо готовлю?', 'Do you want to say that I cook badly?', [(80, 'он сказал, что я'), (82, 'ты хочешь сказать')], ''),
    ('fedya', 'Да, именно это я и говорю.', 'Yes, that is exactly what I say.', [], ''),
    ('max', 'А ты думаешь, ты готовишь лучше меня?', 'And do you think you cook better than me?', [(82, 'ты лучше готовишь')], ''),
    ('fedya', 'Уж точно намного лучше тебя!', 'Certainly much better than you!', [(83, 'уж не хуже')], ''),
    ('max', 'Тогда давай устроим кулинарный спор!', "Then let's make a culinary bet!", [(84, 'Спорим')], ''),
    ('fedya', 'Спорим, огузок! Я легко тебя обыграю!', 'Wanna bet, runt! I will easily beat you!', [(84, 'Спорим')], ''),
    ('max', 'Посмотрим, кто из нас лучший повар!', 'We will see which of us is the best cook!', [], ''),
]
WALK = [
    (0, None, '\'Good morning, Chef!\' Literally \'kind morning\'. "Dobroe" ends in -oe to match "utro", a word ending in -o. "Shef" is borrowed from French, and in this kitchen it simply means \'boss\'.'),
    (1, None, '\'Runt, you are constantly late for work.\' Oguzok, Barinov\'s name for Max, is really the rump cut of beef. "Opazdyvaesh" is a present-tense verb, and with "postoyanno", \'constantly\', it means \'you keep being late\'.'),
    (2, None, '\'Chef, they did not issue my uniform on time.\' Max says "mne ne vydali", \'to me they didn\'t issue\', so nobody in particular gets the blame. "Vovremya", \'on time\', is written as one word.'),
    (3, None, '\'Enough excuses, quickly go to work!\' After "khvatit", \'enough\', the thing you\'ve had enough of takes a genitive ending: "opravdaniy". "Idi rabotat" is just \'go work\', two verbs side by side.'),
    (4, None, '\'You joke as badly as you cook.\' The two halves match: "tak zhe plokho", \'just as badly\', and "kak i", \'as also\'. "Gotovish", \'you cook\', also means \'you prepare\'.'),
    (5, None, '\'I didn\'t understand your joke, Fedya.\' After "ne ponyal", \'didn\'t understand\', the joke turns into "shutki", and "tvoya" into "tvoey". "Ponyal", without -a, tells you a man is talking.'),
    (6, None, '\'This is a normal state for your brain.\' "Dlya", \'for\', changes what follows it: "tvoy mozg" becomes "tvoego mozga". It\'s an insult said almost calmly.'),
    (7, None, '\'Do you want to say that I cook badly?\' "Khochesh skazat" is \'you want to say\', two verbs and no \'to\'. "Chto" here means \'that\', though it\'s also the word for \'what\'.'),
    (8, None, '\'Yes, that is exactly what I say.\' "Imenno" means \'exactly\' or \'precisely\'. The small "i" before "govoryu" isn\'t \'and\' here: it just leans on the word for emphasis.'),
    (9, None, '\'And do you think you cook better than me?\' No word for \'than\'. Russian puts \'me\' into the form "menya" and says "luchshe menya", \'better of me\'.'),
    (10, None, '\'Certainly much better than you!\' The same pattern, "luchshe tebya". "Namnogo" in front makes it \'much better\', and "uzh tochno" is a cocky \'that\'s for sure\'.'),
    (11, None, '\'Then let\'s make a culinary bet!\' "Davay" comes from the verb \'to give\', and before another verb it means \'let\'s\'. "Spor" is an argument; "kulinarnyy spor" makes it a cook-off on a bet.'),
    (12, None, '\'Wanna bet, runt! I will easily beat you!\' "Sporim", from "sporit", \'to argue\', is how Russians say \'wanna bet?\'. "Obygrayu" means \'I\'ll beat you at it\', with the loser as the object, "tebya".'),
    (13, None, '\'We will see which of us is the best cook!\' "Posmotrim" again, the \'we\'ll see\' Kostya used. "Kto iz nas" is \'who out of us\', a handy chunk for comparing people.'),
]
