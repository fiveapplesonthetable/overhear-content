# Authoring module for kukhnya-s01e06-scene-02.
ID = 'kukhnya-s01e06-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = 'Финальный штрих  (The Final Touch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Back in the kitchen at Claude Monet, Chef Barinov is at the pass, the shelf where finished plates wait for the waiters. He is checking one dish, and he wants Max, his trainee, to see the last step. It's in Russian first, so don't worry about catching every word."
OPENER = "Let's go through the plate. Barinov inspects it, and Max asks careful questions."
TRANSITION = 'And now the whole exchange in one piece.'
OUTRO = 'Barinov\'s last step is herbs, and yours is to keep a few kitchen words: "tarelka", plate, "blyudo", dish, "zelen", herbs. They\'ll come back. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Огузок, посмотри на эту тарелку.', 'Oguzok, look at this plate.', [], ''),
    ('max', 'Шеф, это блюдо уже готово?', 'Chef, is this dish already ready?', [], ''),
    ('barinov', 'Осталось главное: украсить его зеленью.', 'The main thing remains: to garnish it with herbs.', [(4, 'Его украшают')], ''),
    ('max', 'Каждая деталь имеет важное значение.', 'Every detail has important meaning.', [], ''),
    ('barinov', 'Еда обязана выглядеть красиво и аппетитно.', 'Food is obliged to look beautiful and appetizing.', [(4, 'украшают')], ''),
    ('max', 'Положим сюда свежую зелень?', 'Shall we put fresh herbs here?', [], ''),
    ('barinov', 'Аккуратно! Не испорти дорогую подачу.', 'Carefully! Do not ruin the expensive presentation.', [], ''),
    ('max', 'Я делаю всё очень аккуратно, шеф.', 'I do everything very carefully, chef.', [], ''),
    ('barinov', 'Красивая подача очень важна для гостей.', 'Beautiful presentation is very important for guests.', [], ''),
    ('max', 'Официанты уже ждут на кухне.', 'The waiters are already waiting in the kitchen.', [], ''),
    ('barinov', 'Зови официанта, пусть несут заказ.', 'Call the waiter, let them carry the order.', [], ''),
    ('max', 'Саша, забери готовое горячее блюдо!', 'Sasha, take the ready hot dish!', [], ''),
    ('barinov', 'Отлично, продолжаем работать дальше.', 'Great, we continue working further.', [], ''),
]
WALK = [
    (0, None, '\'Oguzok, look at this plate.\' Barinov uses his nickname for Max before anything else. "Tarelka", plate, becomes "tarelku" because it\'s the thing being looked at.'),
    (1, None, '\'Chef, is this dish already ready?\' No \'is\', no \'do\': the voice rises and that makes it a question. "Gotovo", ready, ends in -o to match "blyudo".'),
    (2, None, '\'The main thing remains: to garnish it with herbs.\' "Ukrasit", to decorate, shares a root with "krasivyy", beautiful. "Zelen", greens, becomes "zelenyu", and that ending alone says \'with\', as in \'using\'.'),
    (3, None, '\'Every detail has important meaning.\' "Detal", detail, ends in a soft sign and is a feminine word, which is why \'every\' is "kazhdaya" here. "Imet znachenie", to have meaning, is a stiff way of saying \'it matters\'.'),
    (4, None, '\'Food is obliged to look beautiful and appetizing.\' "Eda", food, is feminine, so \'obliged\' comes out as "obyazana". Russian food looks "krasivo", \'beautifully\', with the -o of a how-word.'),
    (5, None, '\'Shall we put fresh herbs here?\' "Polozhim" is \'we\'ll put\', and as a question it works like \'shall we put\'. "Syuda" means \'to here\', because putting something is a movement.'),
    (6, None, '\'Carefully! Do not ruin the expensive presentation.\' "Ne isporti" is the warning \'don\'t go and spoil it\'. "Dorogoy" means both \'expensive\' and \'dear\', so the plate is precious either way.'),
    (7, None, '\'I do everything very carefully, chef.\' "Delayu", I do, has the -yu ending for \'I\'. Max hands Barinov\'s own word back to him, "akkuratno", carefully.'),
    (8, None, '\'Beautiful presentation is very important for guests.\' "Podacha", presentation, comes from "podavat", to serve. "Vazhna", important, ends in -a to agree with it.'),
    (9, None, '\'The waiters are already waiting in the kitchen.\' "Zhdut", they wait, is from "zhdat", with the -ut ending for \'they\'. "Na kukhne" again: the kitchen is a place you\'re \'on\'.'),
    (10, None, '\'Call the waiter, let them carry the order.\' "Pust" is \'let\', and you put it before any verb to mean \'let them do it\'. "Nesut", they carry, is from "nesti", carrying something in your hands as you go.'),
    (11, None, '\'Sasha, take the ready hot dish!\' "Zaberi", take it away, is the command \'take\' with za- in front, the sense of collecting something. On a menu, "goryachee" alone means the hot main courses.'),
    (12, None, '\'Great, we continue working further.\' "Otlichno" is also the top school grade, so it\'s a real \'excellent\'. "Prodolzhaem rabotat" is literally \'we continue to work\'.'),
]
