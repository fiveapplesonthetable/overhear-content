# Authoring module for kukhnya-s01e18-scene-02.
ID = 'kukhnya-s01e18-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 2
TITLE = 'Низкая выручка  (Low Revenue)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "Nagiyev has been reading the restaurant's monthly report, and the takings are tiny. He wants Vika and Barinov to tell him where the customers went. Hear the Russian once first; just follow who is upset."
OPENER = 'Now slowly, one line after another.'
TRANSITION = "That's every piece. Here it is at full speed."
OUTRO = 'No one has a fix yet, and Nagiyev is staying put to keep an eye on things. Hold on to "malo", little or few: "malo deneg", little money, "malo gostey", few guests. See you next time!'
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('nagiyev', 'Что это за маленькие цифры в отчёте?', 'What are these small numbers in the report?', [(18, 'а что это за такие')], ''),
    ('nagiyev', 'Почему у нас так мало денег?', 'Why do we have so little money?', [(21, 'Почему так мало у нас')], ''),
    ('vika', 'Дмитрий Владимирович, сейчас у нас мало гостей.', 'Dmitry Vladimirovich, we have few guests right now.', [(22, 'Дмитрий Владимирович')], ''),
    ('vika', 'Рядом открылся новый итальянский ресторан.', 'A new Italian restaurant opened nearby.', [], ''),
    ('nagiyev', 'А мне что теперь делать?', 'And what am I supposed to do now?', [(24, 'А мне что делать')], ''),
    ('nagiyev', 'Мне нужно кормить свою большую семью!', 'I need to feed my big family!', [], ''),
    ('barinov', 'Дима, ну сейчас просто нет людей.', 'Dima, well there are simply no people right now.', [(27, 'ну нет людей')], ''),
    ('barinov', 'Мы не можем тащить их сюда силой.', 'We cannot drag them in here by force.', [(27, 'Не можем же мы их сюда')], ''),
    ('nagiyev', 'У вас всегда одна и та же история!', 'You always have the exact same story!', [(28, 'история')], ''),
    ('vika', 'Мы обязательно придумаем хорошее решение.', 'We will definitely come up with a good solution.', [], ''),
    ('nagiyev', 'Сегодня я никуда не поеду.', "I'm not going anywhere today.", [(36, 'Не сегодня')], ''),
    ('nagiyev', 'Я остаюсь в ресторане со своими коллегами!', 'I am staying at the restaurant with my colleagues!', [(37, 'с коллегами')], ''),
]
WALK = [
    (0, None, '\'What are these small numbers in the report?\' "Chto eto za" asks \'what sort of thing is this\'. "V otchyote", in the report: "otchyot" picks up an \'e\' after "v".'),
    (1, None, '\'Why do we have so little money?\' After "malo", little, money turns into "deneg". "Dengi" to "deneg" is irregular, so learn the pair together.'),
    (2, None, '\'Dmitry Vladimirovich, we have few guests right now.\' First name plus patronymic is how Vika addresses the boss. "Malo gostey": after "malo", guest, "gost", becomes "gostey".'),
    (3, None, '\'A new Italian restaurant opened nearby.\' "Otkrylsya" ends in "-sya", so nobody opens it; the restaurant simply opened. "Ryadom" means right next door, nearby.'),
    (4, None, '\'And what am I supposed to do now?\' Literally \'and to me what now to do\'. "Mne" plus a bare verb, "delat", is the Russian way to ask what you should do.'),
    (5, None, '\'I need to feed my big family!\' "Mne nuzhno", I need, then the verb "kormit", to feed. "Semya", family, is feminine, so as the thing being fed it becomes "svoyu bolshuyu semyu".'),
    (6, None, '\'Dima, there just aren\'t any people right now.\' Barinov, an old friend, calls him by the short form of Dmitry. "Net lyudey": after "net", people, "lyudi", becomes "lyudey".'),
    (7, None, '\'We can\'t drag them in here by force.\' "Sila" is force; "siloy" means \'by force\', the "-oy" ending saying how it\'s done. "Tashchit" is to drag, a heavy, physical verb.'),
    (8, None, '\'You always have the exact same story!\' "Odna i ta zhe", literally \'one and that same\'. It\'s feminine to match "istoriya", story.'),
    (9, None, '\'We will definitely come up with a good solution.\' "Obyazatelno" promises \'without fail\'. "Pridumaem" is future: we\'ll think something up. "Reshenie", a solution, comes from "reshit", to solve.'),
    (10, None, '\'I\'m not going anywhere today.\' Russian doubles the negative: "nikuda ne poedu", literally \'nowhere not I\'ll go\'. "Poedu" means going by car, the drive home he\'s skipping.'),
    (11, None, '\'I\'m staying at the restaurant with my colleagues!\' "Ostayus", I\'m staying. "S", with, becomes "so" before "svoimi", and "kollegami" carries the plural "-ami" ending that goes with "s".'),
]
