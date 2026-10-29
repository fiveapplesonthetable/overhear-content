# Authoring module for kukhnya-s01e10-scene-39.
ID = 'kukhnya-s01e10-scene-39'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 39
TITLE = 'Поспешное решение  (A Hasty Decision)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "The pretend engagement is going further than either of them expected. They talk about the registry office, and then both of them get cold feet. Listen first, and I'll explain afterwards."
OPENER = "Let's unpack it."
TRANSITION = 'Back to the full version.'
OUTRO = 'The wedding is on hold, at least for now, and the football match is about to begin. Max goes back to work. Take care until then.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Мы подадим заявление в загс?', 'Shall we apply at the registry office?', [(276, 'подадим заявление')], ''),
    ('vika', 'Таня, у тебя есть знакомые в загсе?', 'Tanya, do you have acquaintances at the registry office?', [(277, 'Тань, у тебя есть кто-нибудь')], ''),
    ('max', 'Пожалуйста, помогите нам расписаться как можно быстрее.', 'Please help us get married as fast as possible.', [(278, 'побыстрее расписать')], ''),
    ('vika', 'Давайте расскажем эту новость всем гостям ресторана!', "Let's tell this news to all the guests of the restaurant!", [(280, 'давайте скажем всем'), (281, 'Обрадуем')], ''),
    ('max', 'Подожди, кажется, я немножко поторопился.', 'Wait, it seems I rushed a little.', [(281, 'Подожди'), (283, 'А я с предложением')], ''),
    ('vika', 'Честно говоря, я тоже поторопилась с ответом.', 'To be honest, I also rushed with my answer.', [(282, 'немножко поторопилась с ответом')], ''),
    ('max', 'Значит, нам обоим нужно хорошенько подумать.', 'So, both of us need to think carefully.', [(283, 'Мы немножко подумаем')], ''),
    ('vika', 'Да, нам лучше немного подождать со свадьбой.', 'Yes, it is better for us to wait a little with the wedding.', [(284, 'Да, мы подумаем')], ''),
    ('max', 'Шеф, вы поможете нам спокойно разобраться?', 'Chef, will you help us sort this out calmly?', [(285, 'разбирайтесь сами')], ''),
    ('max', 'Шеф не хочет слушать наши семейные споры.', "The chef doesn't want to listen to our family arguments.", [(285, 'разбирайтесь сами')], ''),
    ('vika', 'У Виктора сейчас начинается важный футбольный матч.', 'Viktor has an important football match starting now.', [(286, 'футбол начинается')], ''),
    ('max', 'Тогда мы сами во всём разберёмся позже.', 'Then we will sort everything out ourselves later.', [(287, 'Идите, идите')], ''),
    ('vika', 'Иди работай, свадьба пока точно подождёт!', 'Go work, the wedding will definitely wait for now!', [(287, 'Идите, идите')], ''),
]
WALK = [
    (0, None, '\'Shall we apply at the registry office?\' "ZAGS" is an old abbreviation for the civil registry office, and Russians still say it. "Podadim zayavlenie" is "we will hand in an application"; "podat" is the verb of Senya\'s "pora podavat blyudo".'),
    (1, None, '\'Tanya, do you have acquaintances at the registry office?\' "Znakomye", "acquaintances", comes from Max\'s "davayte znakomitsya". "U tebya est" is "at you there are", "you have". Vika turns to her sister.'),
    (2, None, '\'Please help us get married as fast as possible.\' "Raspisatsya", literally "sign each other", means to register a marriage. "Kak mozhno bystree" is "as fast as can be". "Pomogite" is the polite "help".'),
    (3, None, '\'Let\'s tell this news to all the guests of the restaurant!\' "Davayte rasskazhem" is "let\'s tell", with the same "rasskazat" as Tanya\'s complaint. "Vsem gostyam" is "to all the guests". Vika raises the stakes.'),
    (4, None, '\'Wait, it seems I rushed a little.\' "Potoropilsya" is "I rushed", with -sya. "Nemnozhko" is "a little bit", a softer "nemnogo". "Kazhetsya" is "it seems". Max starts to back away.'),
    (5, None, '\'To be honest, I also rushed with my answer.\' "Chestno govorya" is "honestly speaking", a fixed phrase. "Potoropilas" has the -las for a woman. "S otvetom" is "with the answer". Vika backs away too.'),
    (6, None, '\'So, both of us need to think carefully.\' "Nam oboim nuzhno" is "to us both it is needed". "Khoroshenko" is a homely form of "khorosho", "well", meaning "properly". "Podumat" is "to think it over".'),
    (7, None, '\'Yes, it is better for us to wait a little with the wedding.\' For "it is better for us", Russian says "nam luchshe", "to us better". "So svadboy" is "with the wedding": "svadba" becomes "svadboy". "Podozhdat" is "to wait a while".'),
    (8, None, '\'Chef, will you help us sort this out calmly?\' "Razobratsya" is "to sort out", from Barinov\'s "Ne nado nikomu zvonit, ya razberus" about the stove. "Pomozhete" is "will you help", polite.'),
    (9, None, '\'The chef doesn\'t want to listen to our family arguments.\' "Semeynye" is "family" as an adjective, from "semya". "Spory" are "arguments". Barinov has no time for them.'),
    (10, None, '\'Viktor has an important football match starting now.\' "U Viktora" works like "u menya": "at Viktor" means "Viktor has", and "Viktor" takes -a after "u". "Nachinaetsya", "is beginning", ends in -sya because the match begins by itself.'),
    (11, None, '\'Then we will sort everything out ourselves later.\' The word "sami", "ourselves", puts the job back on the two of them. "Vo vsyom razberyomsya" is "in everything we will sort ourselves out", the same verb as before. "Pozzhe" is "later".'),
    (12, None, '\'Go work, the wedding will definitely wait for now!\' "Idi rabotay" is "go work", two commands with no "and". "Poka" here means "for now", the same word as "bye". "Podozhdyot" is "will wait".'),
]
