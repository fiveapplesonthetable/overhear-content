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
    (0, None, ['\'What cocktail will you drink, Vika?\' ', ('max', 'будешь пить'), ' is "you will drink", built just like English: ', ('max', 'будешь'), ', "you will", and then the plain ', ('max', 'пить'), ', "to drink". Max is on the friendly form of "you" with her now.']),
    (1, None, ['\'I like dry white wine.\' ', ('vika', 'Люблю'), ' is "I love", and Russians use it for liking things too, like wine. ', ('vika', 'белое'), ' and ', ('vika', 'сухое'), ' end in the same way to match ', ('vika', 'вино'), ', a neuter word, so all three chime together.']),
    (2, None, ['\'Bartender, bring us a glass of white wine!\' ', ('max', 'принесите'), ', "bring", ends in the polite form you\'d use with a bartender. For "a glass of white wine", the words for "white wine" turn into ', ('max', 'белого вина'), ', and that change of ending is the "of".']),
    (3, None, ['\'And what will you drink yourself?\' ', ('vika', 'сам'), ' means "yourself", and it turns the question back at Max: what about you? The little ', ('vika', 'А'), ' at the start isn\'t "and" exactly. It means something like "and as for you".']),
    (4, None, ['\'I will drink a little good juice.\' ', ('max', 'выпью'), ' is "I\'ll drink", a future with no "will" word in it at all. After ', ('max', 'немного'), ', "a little", the word for "juice" becomes ', ('max', 'сока'), ', as if he said "a little of good juice".']),
    (5, None, ['\'Do you not drink strong drinks at all?\' ', ('vika', 'совсем не'), ' is "not at all", and it comes before the verb. ', ('vika', 'крепкие напитки'), ', "strong drinks", is the polite way to talk about spirits.']),
    (6, None, ['\'Tomorrow morning I need a clear head.\' There\'s no "I need" in the Russian. It says ', ('max', 'мне нужна'), ', "to me is needed", and then the thing. A "fresh head" is just how Russians say a clear one.']),
    (7, None, ['\'You take your work very seriously.\' ', ('vika', 'серьёзно'), ' is "seriously": take the word for "serious", and swap the ending for -o, and you get the how-word. Almost any describing word can do this.']),
    (8, None, ['\'I dream of becoming the very best chef!\' ', ('max', 'Мечтаю'), ', "I dream", comes straight from the word for "a dream". And ', ('max', 'шефом'), ' has the ending that means "as", like when he first said he wanted to be a cook.']),
    (9, None, ['\'I like your big dream very much.\' This is the other way to like something: ', ('vika', 'Мне очень нравится'), ', "to me is pleasing". The dream is the one doing the pleasing, so the verb follows the dream and not the "I".']),
    (10, None, ['\'You look simply stunning tonight.\' ', ('max', 'потрясающе'), ' comes from a verb meaning "to shake", so something stunning is something that shakes you. ', ('max', 'просто'), ', "simply", makes the compliment sound easy and unforced.']),
    (11, None, ['\'Thank you, Max, I\'m very pleased.\' ', ('vika', 'мне очень приятно'), ' is "to me it\'s pleasant". It\'s the standard polite reply to a compliment, and it\'s the same "to me" pattern again.']),
    (12, None, ['\'Let\'s go dance to this beautiful music!\' ', ('max', 'Пойдём'), ' is "let\'s go", then ', ('max', 'танцевать'), ', "to dance". ', ('max', 'под эту красивую музыку'), ' means "to the music", but ', ('max', 'под'), ' literally means "under", so Russians dance under the music.']),
]
