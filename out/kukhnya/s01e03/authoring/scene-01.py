# Authoring module for kukhnya-s01e03-scene-01.
ID = 'kukhnya-s01e03-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'Живой гусь  (The Live Goose)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "This is Kukhnya, the Russian comedy about a hot-tempered chef and the staff of a smart Moscow restaurant called Claude Monet. In this third episode, Max, the young cook, has spent a week unloading deliveries and is longing to be allowed near a stove. Instead, Chef Barinov hands him something very different: a live goose. Here is their conversation in Russian first, so don't worry about catching every word."
OPENER = "Let's go back and watch Max's face."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So Max has been given a goose and an ultimatum. If "zhivoy", alive, sticks in your head after this, good: you\'ll meet it again.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Доброе утро, шеф!', 'Good morning, chef!', [(46, 'Доброе утро, шеф')], ''),
    ('barinov', 'Здравствуй, огузок. Вот твоя работа.', 'Hello, oguzok. Here is your work.', [(48, 'Иди разгружай продукты')], ''),
    ('max', 'Шеф, это живой гусь!', 'Chef, this is a live goose!', [(36, 'Это чего? Гусь'), (40, 'живой гусь')], ''),
    ('barinov', 'У нас сегодня очень важный банкет.', 'We have a very important banquet today.', [(38, 'у нас же сегодня банкет')], ''),
    ('max', 'Зачем нам живой гусь на кухне?', 'Why do we need a live goose in the kitchen?', [(40, 'На хрена мне на кухне живой гусь')], ''),
    ('barinov', 'Гостям нужен самый свежий продукт!', 'The guests need the freshest product!', [(41, 'вы просили самого свежего')], ''),
    ('max', 'Но я повар, а не мясник.', 'But I am a cook, not a butcher.', [(49, 'ну я же не грузчик, я повар')], ''),
    ('barinov', 'Каждый повар обязан уметь разделывать мясо.', 'Every chef is obliged to know how to butcher meat.', [(59, 'Каждый повар должен быть готов')], ''),
    ('max', 'Что, мне нужно убить его?', 'What, do I need to kill it?', [(56, 'Что, прям насмерть')], ''),
    ('barinov', 'А ты думал, мясо растёт на деревьях?', 'Did you think meat grows on trees?', [(58, 'ты думаешь, что мясо кусочком на деревьях растет')], ''),
    ('max', 'Я никогда в жизни этого не делал.', 'I have never done this in my life.', [], ''),
    ('barinov', 'Убей гуся, или ты уволен!', 'Kill the goose, or you are fired!', [(53, 'Убей гуся'), (60, 'Убей, гуся')], ''),
    ('max', 'Хорошо, я попробую сделать это.', 'Fine, I will try to do it.', [], ''),
]
WALK = [
    (0, None, '\'Good morning, chef!\' "Dobroye utro" puts -oye on "good" because "utro", morning, is a neuter word. For the evening it changes to "dobryy vecher", since "vecher" is masculine.'),
    (1, None, '\'Hello, oguzok. Here is your work.\' "Zdravstvuy" is the hello for one person you call "ty". Add -te and you get "zdravstvuyte", the polite one. "Oguzok" is a butcher\'s word for the rump cut, and "vot tvoya rabota" is "here your work".'),
    (2, None, '\'Chef, this is a live goose!\' "Eto zhivoy gus\'" is "this live goose", with no word for "is". "Zhivoy" means alive, and "gus\'" is a goose.'),
    (3, None, '\'We have a very important banquet today.\' "U nas", "at us", is how Russian says "we have". "Vazhnyy" is "important", and "banket" is the banquet.'),
    (4, None, '\'Why do we need a live goose in the kitchen?\' "Zachem nam" is "what for, to us", and that "nam" carries the "we need". Note "na kukhne": Russians are "on" the kitchen, not "in" it.'),
    (5, None, '\'The guests need the freshest product!\' The guests get the "to" ending -am, "gostyam", because in Russian the thing needed is the subject. So "nuzhen" agrees with "produkt", masculine, and "samyy svezhiy" builds "freshest" out of "most fresh".'),
    (6, None, '\'But I am a cook, not a butcher.\' "Ya povar, a ne myasnik": the little "a ne", "and not", sets one job against the other. "Myasnik" is built on "myaso", meat.'),
    (7, None, '\'Every chef is obliged to know how to butcher meat.\' "Obyazan", obliged, has a man\'s ending, and for a woman it would be "obyazana". "Umet\'" is "know how", for skills, and "razdelyvat\'" is to cut a carcass into pieces.'),
    (8, None, '\'What, do I need to kill it?\' "Mne nuzhno" is "to me necessary", the plain "I need to". "Ubit\'" is "to kill", and "yego", him, is the goose.'),
    (9, None, '\'Did you think meat grows on trees?\' "Dumal" ends in -l, so Barinov is talking to a man. "Derevo", tree, has the odd plural "derev\'ya", and "on trees" is "na derev\'yakh".'),
    (10, None, '\'I have never done this in my life.\' "Nikogda... ne delal" is "never not did", the Russian double negative. "Etogo", this, takes its "of" form after the "ne", and "v zhizni" is "in life".'),
    (11, None, '\'Kill the goose, or you are fired!\' "Ubey" is the command "kill". "Gus\'" becomes "gusya" as the thing killed, the ending for a living creature. "Ty uvolen" is "you are fired".'),
    (12, None, '\'Fine, I will try to do it.\' "Poprobuyu", I\'ll try, is the future of "poprobovat\'", the finished partner of "probovat\'". "Sdelat\' eto" is "to do it".'),
]
