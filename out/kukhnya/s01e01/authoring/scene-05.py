# Authoring module for kukhnya-s01e01-scene-05.
ID = 'kukhnya-s01e01-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = 'Мечта о кухне  (Dream of the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "This scene steps back to Max's army days, when he cooked in a military kitchen. He starts by telling us he always knew he'd be a cook, and then the famous owner of Claude Monet, Nagiyev, drops by, tastes his soup and makes him an offer. Here it is in Russian first."
OPENER = "Let's go through it slowly."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'One bowl of soup, and Max has a job offer from a restaurant owner he\'d only seen on television. Keep an ear out for "my dream" and "of course", because you\'ll hear both again.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Я всегда знал, что буду поваром.', 'I always knew I would be a chef.', [(35, 'что буду поваром')], ''),
    ('max', 'Не пожарным и не космонавтом.', 'Not a firefighter and not an astronaut.', [(36, 'не пожарным, не космонавтом')], ''),
    ('max', 'Даже не президентом. А именно поваром.', 'Not even president. Exactly a chef.', [(37, 'Даже не президентом'), (37, 'А именно поваром')], ''),
    ('nagiyev', 'Вот он, наш герой!', 'Here he is, our hero!', [(46, 'Вот он наш герой')], ''),
    ('nagiyev', 'Мне очень понравилась ваша солянка.', 'I really liked your solyanka.', [(47, 'Мне очень понравилась ваша солянка')], ''),
    ('max', 'Спасибо! Я очень старался.', 'Thank you! I tried very hard.', [(44, 'мои старания')], ''),
    ('nagiyev', 'Молодец. Из ничего практически шедевр.', 'Well done. Practically a masterpiece out of nothing.', [(48, 'Молодец'), (48, 'Из ничего практически шедевр')], ''),
    ('nagiyev', 'Хотите поработать в хорошем ресторане?', 'Would you like to work in a good restaurant?', [(49, 'поработать в хорошем ресторане')], ''),
    ('max', 'Конечно! Это моя мечта.', 'Of course! That is my dream.', [], ''),
    ('nagiyev', 'Милости просим. Буду рад.', 'You are welcome. I will be glad.', [(50, 'милости просим, буду рад')], ''),
    ('nagiyev', 'Я говорю совершенно серьёзно.', 'I am speaking completely seriously.', [(50, 'Я серьезно')], ''),
    ('max', 'В каком ресторане?', 'In which restaurant?', [], ''),
    ('nagiyev', 'Ресторан Клод Моне в Москве.', 'Restaurant Claude Monet in Moscow.', [(51, 'Ресторан Клод Мане'), (51, 'в Москве')], ''),
    ('max', 'Спасибо огромное! Я обязательно приду.', 'Thank you very much! I will definitely come.', [], ''),
]
WALK = [
    (0, None, '\'I always knew I would be a chef.\' "Znal" ends in -l because Max is a man. "Budu povarom" is "I will be a cook", and "povarom" has the same "as a" ending as before.'),
    (1, None, '\'Not a firefighter and not an astronaut.\' "Ne... i ne" is the Russian "neither this nor that". "Pozharnyy" has "pozhar", a fire, inside it, and both jobs end in "-ym" and "-om", the "as a" endings.'),
    (2, None, '\'Not even president. Exactly a chef.\' "Dazhe ne" is "not even". "Imenno" means "precisely", and Russians put it right before the thing they want to underline.'),
    (3, None, '\'Here he is, our hero!\' "Vot" is the pointing word, "here is". "Vot on" is "here he is". "Nash", "our", is what makes the cook sound like one of the family.'),
    (4, None, '\'I really liked your solyanka.\' This is "mne nravitsya" again, but with "po-" added and in the past: "ponravilas\'". The ending is feminine because "solyanka", a thick sour soup, is a feminine word, and the soup is what did the pleasing.'),
    (5, 'Спасибо! Я очень старался.', '\'Thank you! I tried very hard.\' "Starat\'sya" means to try, to make an effort. In the past it ends in -l for a man, "staralsya", and in -la for a woman, so you can tell a lot about the speaker from one letter.'),
    (6, None, '\'Well done. Practically a masterpiece out of nothing.\' "Molodets" is what you say to someone who did well, and it comes from "molodoy", young. It\'s used for women too. "Iz nichego" is literally "out of nothing".'),
    (7, None, '\'Would you like to work in a good restaurant?\' "Khotite" is "you want" in the formal register, fitting for an owner speaking to a stranger. The "po-" in "porabotat\'" means to work for a while, a trial run.'),
    (8, None, '\'Of course! That is my dream.\' "Konechno" is spelled with a "ch" but pronounced "koneshno". Remember that one. "Moya mechta" is "my dream". "Moya" is the feminine "my".'),
    (9, None, '\'You are welcome. I will be glad.\' "Milosti prosim" is a warm old phrase, literally "we ask for your kindness", and it means "welcome". "Budu rad" is "I will be glad", the future of "to be" plus "rad".'),
    (10, None, '\'I am speaking completely seriously.\' "Sovershenno" is "completely", and "ser\'yozno" is "seriously". Nagiyev piles them up so there\'s no doubt that he means it.'),
    (11, None, '\'In which restaurant?\' It\'s the same "v kakom restorane" as in the night-time talk, with "kakom" and "restorane" taking their endings after "v".'),
    (12, None, '\'Restaurant Claude Monet in Moscow.\' "V Moskve" is "in Moscow", and now the name takes -e after "v". When it meant "of Moscow" it ended in -y.'),
    (13, 'Спасибо огромное! Я обязательно приду.', '\'Thank you very much! I will definitely come.\' "Ogromnoye" means "huge", so "spasibo ogromnoye" is "huge thanks". "Pridu" is the future of "come", with no "will" in front.'),
]
