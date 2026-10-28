# Authoring module for kukhnya-s01e01-scene-02.
ID = 'kukhnya-s01e01-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = 'Коктейль в баре  (Cocktails at the Bar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "A little later Max and Vika are sitting at a bar. She orders white wine, but Max sticks to juice, because tomorrow is the job interview he keeps mentioning. Here's their conversation in Russian first."
OPENER = "Let's go back and pick out the useful bits."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Ordering a drink is half of what you need at a Russian bar, and you've now heard both the question and the answer. Max keeps his head clear, which will matter more than he thinks."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Какой коктейль ты будешь пить, Вика?', 'What cocktail will you drink, Vika?', [], ''),
    ('vika', 'Я люблю белое сухое вино.', 'I like dry white wine.', [], ''),
    ('max', 'Бармен, принесите нам бокал белого вина!', 'Bartender, bring us a glass of white wine!', [], ''),
    ('vika', 'А что ты сам будешь пить?', 'And what will you drink yourself?', [(22, 'А')], ''),
    ('max', 'Я выпью немного хорошего сока.', 'I will drink a little good juice.', [], ''),
    ('vika', 'Ты совсем не пьёшь крепкие напитки?', 'Do you not drink strong drinks at all?', [], ''),
    ('max', 'Завтра утром мне нужна свежая голова.', 'Tomorrow morning I need a clear head.', [], ''),
    ('vika', 'Ты очень серьёзно относишься к работе.', 'You take your work very seriously.', [], ''),
    ('max', 'Я мечтаю стать самым лучшим шефом!', 'I dream of becoming the very best chef!', [], ''),
    ('vika', 'Мне очень нравится твоя большая мечта.', 'I like your big dream very much.', [], ''),
    ('max', 'Ты сегодня выглядишь просто потрясающе.', 'You look simply stunning tonight.', [], ''),
    ('vika', 'Спасибо, Макс, мне очень приятно.', 'Thank you, Max, I am very pleased.', [], ''),
    ('max', 'Пойдём танцевать под эту красивую музыку!', "Let's go dance to this beautiful music!", [], ''),
]
WALK = [
    (0, None, '\'What cocktail will you drink, Vika?\' "Budesh\' pit\'" is "you will drink", built like English: a word for "will" and then the plain "to drink". Max ends with her name, and a name needs no change to be called out.'),
    (1, None, '\'I like dry white wine.\' "Lyublyu" is "I love", and Russians use it for liking things too, like wine. "Beloye", "sukhoye" and "vino" all end in the same sound, and that echo is how Russian shows that the describing words belong to "wine".'),
    (2, None, '\'Bartender, bring us a glass of white wine!\' "Prinesite" is a polite order: "bring". The "-ite" on the end addresses a formal "you". "A glass of white wine" makes both "white" and "wine" change their endings, and that change is the "of".'),
    (3, None, '\'And what will you drink yourself?\' "Sam" means "yourself", and it turns the question back at Max: what about you? The little "a" at the start isn\'t "and" exactly. It means something like "and as for you".'),
    (4, None, '\'I will drink a little good juice.\' "Vypyu" has the little prefix "vy-", which means to drink something up, a serving, rather than just "be drinking". "Nemnogo", "a little", is useful in any sentence.'),
    (5, None, '\'Do you not drink strong drinks at all?\' "Sovsem ne" is "not at all", and notice how Russian puts "at all" first. "Krepkiye napitki" are "strong drinks", the usual way to talk about alcohol.'),
    (6, None, '\'Tomorrow morning I need a clear head.\' There\'s no "I need" in the Russian. It says "mne nuzhna", "to me is needed", and then the thing. A "fresh head" is just how Russians say a clear one.'),
    (7, None, '\'You take your work very seriously.\' "Ser\'yozno" is "seriously": take "ser\'yozny", serious, and swap the ending for -o, and you get the how-word. Almost any describing word can do this.'),
    (8, None, '\'I dream of becoming the very best chef!\' "Mechtayu" comes from "mechta", a dream, so you can see where it grows from. "Shefom" has the "-om" ending that means "as a", the same as "povarom" earlier.'),
    (9, None, '\'I like your big dream very much.\' This is the other way to like something: "mne nravitsya", "to me is pleasing". The dream is the one doing the pleasing, so the verb follows the dream and not the "I".'),
    (10, None, '\'You look simply stunning tonight.\' "Potryasayushche" comes from a word meaning "to shake", so something stunning is something that shakes you. "Prosto", "simply", is the shrug that makes the compliment sound easy.'),
    (11, None, '\'Thank you, Max, I\'m very pleased.\' "Mne priyatno" is "to me it\'s pleasant". It\'s the standard polite reply to a compliment, and it\'s the same "to me" pattern again.'),
    (12, None, '\'Let\'s go dance to this beautiful music!\' "Poydyom" is "let\'s go", then "tantsevat\'", "to dance". "Pod muzyku" means "to the music", but "pod" literally means "under", so Russians dance under the music.'),
]
