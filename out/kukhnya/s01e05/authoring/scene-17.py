# Authoring module for kukhnya-s01e05-scene-17.
ID = 'kukhnya-s01e05-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 17
TITLE = 'Невинный обман  (An Innocent Deception)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Still in the Claude Monet storeroom, Nastya has second thoughts. Using Kostya to get back at Max feels wrong, and she tells him so. Kostya is far too kind to take offence, and he has an idea of his own. Listen in Russian first.'
OPENER = 'Slowly now. Nastya owns up, Kostya reassures her, and together they settle on a plan.'
TRANSITION = "Here's the storeroom talk again, nonstop."
OUTRO = 'Two lines worth keeping: Nastya\'s "ya tak ne mogu", \'I can\'t do it like this\', and Kostya\'s "ya gotov na vsyo", \'I\'m ready for anything\'.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Костя, подожди, я так не могу.', 'Kostya, wait, I cannot do this.', [(209, 'Костя, подожди'), (210, 'Я так не могу')], ''),
    ('kostya', 'Что случилось, Настя, что не так?', 'What happened, Nastya, what is wrong?', [], ''),
    ('nastya', 'Я хотела отомстить Максиму через тебя.', 'I wanted to get back at Maxim through you.', [(211, 'чтобы отомстить Максиму')], ''),
    ('kostya', 'Макс вполне заслуживает хорошего урока, знаешь.', 'Max fully deserves a good lesson, you know.', [(212, 'он вообще заслуживает')], ''),
    ('nastya', 'Я не могу принять такую жертву.', 'I cannot accept such a sacrifice.', [(214, 'не могу принять от тебя такой жертвы')], ''),
    ('kostya', 'И что же нам теперь делать?', 'And what are we to do now?', [], ''),
    ('nastya', 'Давай просто всем скажем про нас.', 'Let us simply tell everyone about us.', [(215, 'всем скажем')], ''),
    ('kostya', 'А на самом деле ничего нет?', 'And in reality there is nothing?', [(216, 'А на самом деле ничего')], ''),
    ('nastya', 'Да, это будет только наш секрет.', 'Yes, this will be only our secret.', [], ''),
    ('kostya', 'Хорошо, пусть Макс немного поревнует.', 'Fine, let Max be slightly jealous.', [], ''),
    ('nastya', 'Костя, спасибо, ты просто самый классный!', 'Kostya, thank you, you are simply the best!', [(218, 'такой классный')], ''),
    ('kostya', 'Для тебя я готов на всё.', 'For you I am ready for anything.', [], ''),
    ('nastya', 'Мой заказ готов, я побегу работать!', "My order is ready, I'll run back to work!", [(219, 'заказ готов')], ''),
]
WALK = [
    (0, None, '\'Kostya, wait, I cannot do this.\' "Podozhdi" is \'wait\' for someone you call "ty". "Ya tak ne mogu", \'I so not can\', means \'I can\'t do it like this\'.'),
    (1, None, '\'What happened, Nastya, what is wrong?\' "Chto sluchilos" is the standard \'what happened?\'. "Chto ne tak" is literally \'what not so\', with no \'is\' at all.'),
    (2, None, '\'I wanted to get back at Maxim through you.\' Nastya uses Max\'s full name, Maksim, which sounds colder. "Otomstit", \'to take revenge\', puts \'to\' on the person you\'re getting back at: "otomstit Maksimu".'),
    (3, None, '\'Max fully deserves a good lesson, you know.\' "Zasluzhivaet", \'deserves\', takes the genitive here, so it\'s "khoroshego uroka". "Znaesh" at the end works like the English \'you know\'.'),
    (4, None, '\'I cannot accept such a sacrifice.\' "Zhertva" means both \'sacrifice\' and \'victim\', and the context decides. Here it\'s "zhertvu", with -u, as the thing she won\'t accept.'),
    (5, None, '\'And what are we to do now?\' "Chto zhe nam delat" is literally \'what then to us to do\', with "nam", \'to us\', in place of \'we\'. The little "zhe" adds a note of \'so then\'.'),
    (6, None, '\'Let us simply tell everyone about us.\' "Davay", from \'give\', turns what comes next into \'let\'s\': "davay skazhem". "Vsem", \'to everyone\', comes from "vse", \'all\', and pro "nas" means \'about us\'.'),
    (7, None, '\'And in reality there is nothing?\' "Na samom dele", literally \'on the very deed\', means \'actually\' or \'in reality\'. "Nichego net" is \'there is nothing\'.'),
    (8, None, '\'Yes, this will be only our secret.\' "Sekret" sounds almost English. "Budet", \'will be\', fills the slot that \'is\' leaves empty in the present.'),
    (9, None, '\'Fine, let Max be slightly jealous.\' "Pust", \'let\', is \'let\', like in \'let him\'. "Porevnuet" has "po-" on the front, which here means doing something for a little while.'),
    (10, None, '\'Kostya, thank you, you are simply the best!\' "Klassnyy", \'great\', is casual and built on "klass". "Samyy klassnyy" turns it into \'the very best\'.'),
    (11, None, '\'For you I am ready for anything.\' "Dlya tebya", \'for you\', goes first for emphasis. "Gotov na vsyo", with "na" and the accusative, is \'ready for anything\'.'),
    (12, None, '\'My order is ready, I\'ll run back to work!\' "Gotov" here describes "zakaz", a masculine noun, so it has the same bare form Kostya used about himself. "Pobegu", \'I\'ll run\', is the perfective of "bezhat".'),
]
