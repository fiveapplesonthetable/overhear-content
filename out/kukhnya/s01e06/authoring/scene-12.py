# Authoring module for kukhnya-s01e06-scene-12.
ID = 'kukhnya-s01e06-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 12
TITLE = 'Строгая проверка  (A Strict Inspection)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Inside the kitchen at Claude Monet the sanitary inspector is checking everything: the floor, the grill, a bottle that should not be open. Barinov, the head chef, follows him and tries to keep up appearances. It's in Russian first."
OPENER = 'Slowly now. The inspector speaks in short official remarks, and Barinov answers with excuses.'
TRANSITION = 'Here is the inspection again, from the slippery floor on.'
OUTRO = 'Barinov keeps saying "lichno", personally, and the inspector keeps saying "narushenie", violation. Between them they\'ve given you the vocabulary of a very bad afternoon. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('inspector', 'Скользкий пол — это источник опасности.', 'A slippery floor is a source of danger.', [(160, 'Скользкий пол — это источник опасности для сотрудников')], ''),
    ('barinov', 'Мы сейчас же вытрем эту воду.', 'We will wipe up this water immediately.', [], ''),
    ('inspector', 'Почему у гриля открыта эта бутылка?', 'Why is this bottle open by the grill?', [(161, 'Почему у гриля открыта бутылка с алкоголем')], ''),
    ('barinov', 'Это вино нужно для мясного соуса.', 'This wine is needed for meat sauce.', [], ''),
    ('inspector', 'Понятно, но это всё равно нарушение.', 'Understood, but that is still a violation.', [(162, 'Понятно')], ''),
    ('barinov', 'Я лично уберу бутылку в шкаф.', 'I will personally put the bottle in the cupboard.', [], ''),
    ('inspector', 'Простым штрафом вы здесь не отделаетесь!', "You won't get off with a simple fine here!", [(163, 'простым штрафом вы здесь не отделаетесь')], ''),
    ('barinov', 'Поверьте, у нас образцовый ресторан!', 'Believe me, we have an exemplary restaurant!', [], ''),
    ('inspector', 'Пойдёмте дальше, я осмотрю склад.', "Let's move on, I will inspect the storage.", [(164, 'Пойдемте дальше')], ''),
    ('barinov', 'Прошу вас, идите прямо за мной.', 'Please, walk right behind me.', [], ''),
    ('inspector', 'А что находится за этой дверью?', 'And what is located behind this door?', [(165, 'А тут что')], ''),
    ('barinov', 'Там наш склад для закрытых бутылок.', 'There is our storage for unopened bottles.', [(166, 'Склад алкоголя')], ''),
    ('inspector', 'Откройте замок, я должен всё увидеть.', 'Open the lock, I must see everything.', [], ''),
]
WALK = [
    (0, None, '\'A slippery floor is a source of danger.\' The dash stands in for \'is\', which Russian doesn\'t say in the present. "Istochnik", source, is also the word for a natural spring.'),
    (1, None, '\'We will wipe up this water immediately.\' "Seychas zhe", \'this very minute\', adds "zhe" for urgency. "Vytrem", we\'ll wipe, is a finished-action form, so it means the future.'),
    (2, None, '\'Why is this bottle open by the grill?\' "Otkryta", open, takes its -a from "butylka", bottle. "U grilya", by the grill, adds -ya to "gril" after u.'),
    (3, None, '\'This wine is needed for meat sauce.\' "Vino", wine, is neuter, so "nuzhno", needed, ends in -o. "Myasnoy sous", \'meaty sauce\', turns "myaso" into a describing word.'),
    (4, None, '\'Understood, but that is still a violation.\' "Ponyatno", understood, is the everyday \'got it\'. "Vsyo ravno", \'all equal\', means \'anyway\' or \'still\'.'),
    (5, None, '\'I will personally put the bottle in the cupboard.\' "Uberu", I\'ll put away, is from "ubrat", the finished partner of "ubirat". "V shkaf", into the cupboard, keeps "shkaf" unchanged because it\'s masculine.'),
    (6, None, '\'You won\'t get off with a simple fine here!\' "Otdelaetes", you\'ll get off, needs the -s at the end. "Prostym shtrafom", with a simple fine, has -ym and -om because it means \'by means of\'.'),
    (7, None, '\'Believe me, we have an exemplary restaurant!\' "Pover\'te", believe me, is the polite command from "poverit". "Obraztsovyy", exemplary, is from obrazets, a model or sample.'),
    (8, None, '\'Let\'s move on, I will inspect the storage.\' "Poydyomte", let\'s go, takes "poydyom" and adds -te to make it polite. "Osmotryu", I\'ll inspect, starts with o-, around: to look all over.'),
    (9, None, '\'Please, walk right behind me.\' "Proshu vas", \'I ask you\', is a formal \'please\'. "Za mnoy", behind me, turns "ya" into "mnoy" after "za".'),
    (10, None, '\'And what is located behind this door?\' "Nakhoditsya", is located, is literally \'finds itself\'. "Za etoy dveryu", behind this door, turns "dver" into "dveryu" after "za".'),
    (11, None, '\'There is our storage for unopened bottles.\' "Zakrytykh", closed, here means \'sealed\'. "Dlya", for, turns "butylki" into "butylok".'),
    (12, None, '\'Open the lock, I must see everything.\' "Zamok", lock, is stressed at the end; stressed on the first syllable, the same spelling means \'castle\'. "Dolzhen", I must, is the form a man uses.'),
]
