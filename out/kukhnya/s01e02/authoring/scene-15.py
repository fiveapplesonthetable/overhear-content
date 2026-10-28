# Authoring module for kukhnya-s01e02-scene-15.
ID = 'kukhnya-s01e02-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 15
TITLE = 'В погоне за вором  (Chasing the Thief)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'The cognac is gone from the shelf, and Vika wants answers. Kostya realises the "repairman" must have taken it, and he runs out to catch him. This is the Russian first.'
OPENER = 'Now the chase, from the start.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Kostya is off down the street after a thief, with a threat from Vika behind him. You\'ve now met "kuda", the "where to" question, next to "gde", "where".'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Куда пропала бутылка дорогого коньяка?', 'Where did the bottle of expensive cognac disappear to?', [(192, 'Я не знаю')], ''),
    ('kostya', 'Честно говоря, я совсем не знаю.', "Honestly speaking, I don't know at all.", [(192, 'Я не знаю')], ''),
    ('vika', 'А кто должен знать, если не ты?', 'And who should know if not you?', [(193, 'А кто знает')], ''),
    ('vika', 'Костя, тебя нужно немедленно уволить с работы!', 'Kostya, you need to be fired from your job immediately!', [(193, 'Костя тебя что уволить')], ''),
    ('kostya', 'Он точно стоял здесь, я сам помню.', 'It definitely stood here, I remember myself.', [(194, 'Он здесь стоял я видел его')], ''),
    ('vika', 'Значит, этот фальшивый мастер украл его.', 'So that fake repairman stole it.', [(195, 'Вот падла')], ''),
    ('kostya', 'Вот же наглый подлый вор!', 'What an insolent, vile thief!', [(195, 'Вот падла')], ''),
    ('vika', 'Эта бутылка стоит огромных денег.', 'This bottle costs huge money.', [(193, 'тебя что уволить')], ''),
    ('kostya', 'Извините меня, я сейчас всё исправлю.', 'Excuse me, I will fix everything right now.', [(196, 'Извините я сейчас')], ''),
    ('vika', 'Куда ты так быстро побежал?', 'Where did you run so fast?', [(196, 'я сейчас')], ''),
    ('kostya', 'Я догоню этого вора и верну коньяк!', 'I will catch up with that thief and return the cognac!', [(196, 'я сейчас')], ''),
    ('vika', 'Попробуй только не вернуть его назад!', 'Just you dare not bring it back!', [(193, 'уволить')], ''),
]
WALK = [
    (0, None, '\'Where did the bottle of expensive cognac disappear to?\' "Kuda" means "where to", and it\'s different from "gde", "where it is". Russian wants one for moving and one for staying.'),
    (1, None, '\'Honestly speaking, I don\'t know at all.\' "Chestno govorya" is "honestly speaking", exactly as in English. "Sovsem ne znayu" is "at all not I know".'),
    (2, None, '\'And who should know if not you?\' "Dolzhen znat\'" is "must know" or "is supposed to know". "Yesli ne ty", "if not you", is as short as it sounds.'),
    (3, None, '\'Kostya, you need to be fired from your job immediately!\' "Tebya nuzhno uvolit\'" is "you necessary to fire": "ty" becomes "tebya" because Kostya is the one being fired. "S raboty" is "from work".'),
    (4, None, '\'It definitely stood here, I remember myself.\' "Tochno", definitely, and "sam", myself, add weight. "Pomnyu" is "I remember", and "on", it, is the cognac, a masculine word.'),
    (5, None, '\'So that fake repairman stole it.\' "Fal\'shivyy", fake, comes from German "falsch". "Ukral", stole, is the singular of the chef\'s "ukrali".'),
    (6, None, '\'What an insolent, vile thief!\' "Vot zhe" turns the sentence into "what a...!". "Naglyy" is "cheeky" or "insolent", "podlyy" is "vile", and "vor" is a thief.'),
    (7, None, '\'This bottle costs huge money.\' "Stoit", costs, is spelled exactly like "stoit", stands, and context tells you which. Russians say "ogromnykh deneg", "of huge money".'),
    (8, None, '\'Excuse me, I will fix everything right now.\' "Ispravlyu", I\'ll fix, comes from "pravyy", right: you make it right again. "Izvinite" is the polite "excuse me".'),
    (9, None, '\'Where did you run so fast?\' "Kuda", where to, again. "Pobezhal" is "ran off", and the "po-" marks the start of the run.'),
    (10, None, '\'I will catch up with that thief and return the cognac!\' "Dogonyu", I\'ll catch up, is "gonyat\'", to chase, with "do-", as far as. "Vernu" is "I\'ll return".'),
    (11, None, '\'Just you dare not bring it back!\' "Poprobuy tol\'ko" is "just try", a threat, close to "don\'t you dare". "Nazad", back, ends it.'),
]
