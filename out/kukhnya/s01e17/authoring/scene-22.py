# Authoring module for kukhnya-s01e17-scene-22.
ID = 'kukhnya-s01e17-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 22
TITLE = 'Бокал для шефа  (A Glass for the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = 'With the row over, Barinov wants a proper toast. He sends Nastya for glasses, and the kitchen gathers round. Here is the toast in Russian first.'
OPENER = 'Now the toast again, slowly.'
TRANSITION = "Here's the toast once more, from the top."
OUTRO = 'The glasses are up, and the toast is "za druzhbu", to friendship. Remember "molodets", well done, which Russians say to anyone, man or woman. See you next time!'
CLOSING = ('barinov', 'Ну, удачи всем!')
STORY = [
    ('barinov', 'Настя, принеси мне чистый бокал.', 'Nastya, bring me a clean glass.', [(326, 'принеси бокал.')], ''),
    ('nastya', 'Сейчас принесу, шеф.', 'I will bring it right away, chef.', [], ''),
    ('barinov', 'Мы должны выпить за праздник.', 'We must drink to the holiday.', [], ''),
    ('max', 'Шеф, это очень приятно.', 'Chef, this is very pleasant.', [], ''),
    ('barinov', 'Наливай всем хорошее вино.', 'Pour good wine for everyone.', [], ''),
    ('nastya', 'Вот ваш бокал, шеф.', 'Here is your glass, chef.', [], ''),
    ('barinov', 'Спасибо, Настя, молодец.', 'Thank you, Nastya, well done.', [], ''),
    ('max', 'Какой красивый бокал!', 'What a beautiful glass!', [], ''),
    ('barinov', 'Для хорошего вина нужен красивый бокал.', 'For good wine one needs a beautiful glass.', [], ''),
    ('nastya', 'Я принесла бокалы для всех.', 'I brought glasses for everyone.', [], ''),
    ('max', 'Теперь у всех есть бокалы.', 'Now everyone has glasses.', [], ''),
    ('barinov', 'Поднимите ваши бокалы.', 'Raise your glasses.', [], ''),
    ('barinov', 'Давайте выпьем за дружбу!', 'Let us drink to friendship!', [], ''),
]
WALK = [
    (0, None, '\'Nastya, bring me a clean glass.\' "Prinesi" is "bring" to one person. "Bokal" is a wine glass, not a tumbler.'),
    (1, None, '\'Coming right up, chef.\' "Seychas prinesu" is literally "now I\'ll bring", a waiter\'s standard reply.'),
    (2, None, '\'We have to drink to the celebration.\' "Vypit za" means "to drink to"; "za" is always the toast word.'),
    (3, None, '\'Chef, that\'s very kind.\' "Priyatno", pleasant, here means "that\'s nice of you".'),
    (4, None, '\'Pour everyone some good wine.\' "Nalivay" means "pour". "Vsem" is "for everyone".'),
    (5, None, '\'Here\'s your glass, chef.\' "Vot vash" is "here is your", with the polite "vash".'),
    (6, None, '\'Thanks, Nastya, well done.\' "Molodets" means "well done" or "good job", and Russians say it to women too.'),
    (7, None, '\'What a beautiful glass!\' "Kakoy" at the start turns the line into "what a...!".'),
    (8, None, '\'Good wine needs a beautiful glass.\' "Dlya" means "for", and "vino" becomes "vina" after it.'),
    (9, None, '\'I brought glasses for everyone.\' "Prinesla", brought, carries the woman\'s "-a": it was Nastya who fetched them.'),
    (10, None, '\'Now everyone has a glass.\' "U vsekh est" is "at everyone there is", the Russian "everyone has".'),
    (11, None, '\'Raise your glasses.\' "Podnimite" is "raise" said to the whole room.'),
    (12, None, '\'Let\'s drink to friendship!\' "Druzhba", friendship, is built on "drug", friend, and becomes "druzhbu" after "za".'),
]
