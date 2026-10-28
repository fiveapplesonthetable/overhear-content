# Authoring module for kukhnya-s01e10-scene-04.
ID = 'kukhnya-s01e10-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 4
TITLE = 'Низкий гонорар  (A Low Fee)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'girl': 'Девушка'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = 'Barinov goes out to meet the woman who was asking for him. She works for a television show, the one he appeared on recently, and she has an offer. He is not impressed by the number. The Russian comes first.'
OPENER = "We'll take it a bit at a time."
TRANSITION = 'And again, the whole conversation.'
OUTRO = "Barinov won't work for kopecks, and we can guess he's thinking about his betting money. A TV job will have to wait. On to the next."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Здравствуйте, я вас внимательно слушаю.', 'Hello, I am listening to you attentively.', [(7, 'Я вас слушаю. Здравствуйте, Виктор')], ''),
    ('girl', 'Вы отлично выступали в нашем кулинарном шоу.', 'You performed wonderfully on our culinary show.', [(8, 'кулинарном шоу?')], ''),
    ('barinov', 'И что решили ваши строгие продюсеры?', 'And what did your strict producers decide?', [(9, 'нашим продюсерам.')], ''),
    ('girl', 'Мы хотим предложить вам постоянную работу.', 'We want to offer you a permanent job.', [(10, 'хотят предложить вам')], ''),
    ('barinov', 'Во сколько вы оценили мою работу?', 'At how much did you value my work?', [(12, 'во сколько ваши продюсеры оценили мою работу?')], ''),
    ('girl', 'Десять тысяч за каждую новую передачу.', 'Ten thousand for each new broadcast.', [(14, 'Десять, десять одна программа.')], ''),
    ('barinov', 'Десять тысяч евро за один выпуск?', 'Ten thousand euros for one episode?', [(15, 'Евро?')], ''),
    ('girl', 'Нет, мы платим десять тысяч рублей.', 'No, we pay ten thousand rubles.', [(15, 'Рублей.')], ''),
    ('barinov', 'Тогда до свидания, а лучше прощайте!', 'Then goodbye, or rather farewell!', [(16, 'До свидания. Нет, лучше прощайте.')], ''),
    ('girl', 'Подождите, Виктор, давайте спокойно всё обсудим.', 'Wait, Viktor, let us calmly discuss everything.', [(17, 'Подождите. Давайте мы с вами обсудим.')], ''),
    ('barinov', 'Вы предлагаете работать в мой выходной день.', 'You propose that I work on my day off.', [(18, 'Вы мне предлагаете работать в мой выходной день')], ''),
    ('girl', 'Это сделает ваш ресторан очень известным.', 'This will make your restaurant very famous.', [], ''),
    ('barinov', 'Я не работаю за такие смешные копейки!', 'I do not work for such ridiculous kopecks!', [(19, 'да еще за копейки.')], ''),
]
WALK = [
    (0, None, '\'Hello, I am listening to you attentively.\' "Ya vas vnimatelno slushayu", "I you attentively listen", is a set polite opening for a business talk, with the formal "vas". Barinov is playing the gentleman.'),
    (1, None, '\'You performed wonderfully on our culinary show.\' "Vystupali" means "performed", appeared in front of an audience. "Kulinarnom" is "culinary", and "shou" is borrowed and never changes.'),
    (2, None, '\'And what did your strict producers decide?\' "Prodyusery" is borrowed from English "producers". "Reshili" is "decided", with the plural -li. "Vashi strogie" is "your strict", both plural to match. He goes straight to business.'),
    (3, None, '\'We want to offer you a permanent job.\' "Postoyannuyu", "permanent", grows out of "postoyanno", "constantly". "Predlozhit vam" is "offer to you", with the polite "vam". It sounds like good news, until she names the sum.'),
    (4, None, '\'At how much did you value my work?\' "Vo skolko", "into how much", is Russian for "at what price". "Otsenili" is "valued" or "rated". It\'s a blunt way to ask about money.'),
    (5, None, '\'Ten thousand for each new broadcast.\' "Peredacha", "broadcast", is something passed on, from "peredat". "Za kazhduyu" is "for each": "za" here means "in exchange for". She says it brightly, as if it were a lot.'),
    (6, None, '\'Ten thousand euros for one episode?\' "Evro" never changes its ending. "Vypusk", "episode" or "issue", is something released, from "vypustit", "to let out". Barinov hopes she means euros.'),
    (7, None, '\'No, we pay ten thousand rubles.\' "Platim" is "we pay", from the same family as "zaplatili", "paid", in the cake scene. After "desyat tysyach", "rubl" becomes "rubley".'),
    (8, None, '\'Then goodbye, or rather farewell!\' "Do svidaniya" is "until seeing", until we meet again. "Proshchayte" is a final farewell. So Barinov means he doesn\'t want to see her again, ever.'),
    (9, None, '\'Wait, Viktor, let us calmly discuss everything.\' "Podozhdite" and "davayte" both end in -te: the polite "wait" and "let\'s". "Obsudim" is "we will discuss". A television woman knows how to keep a man in the room.'),
    (10, None, '\'You propose that I work on my day off.\' "Vykhodnoy den", "day off", comes from "vykhodit", "to go out". "Predlagaete" is "you propose", the polite form. Barinov lines up his objections like plates.'),
    (11, None, '\'This will make your restaurant very famous.\' "Izvestnym" is "famous", literally "known"; for the pastry chef it was "znamenity", which is stronger. "Sdelaet" is "will make". She changes tack, from his fee to the restaurant\'s name.'),
    (12, None, '\'I do not work for such ridiculous kopecks!\' A hundred "kopeyki" make a ruble, so it\'s what English calls peanuts. "Smeshnye", "ridiculous", is the word for "funny". "Za takie" is "for such".'),
]
