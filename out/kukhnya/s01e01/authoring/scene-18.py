# Authoring module for kukhnya-s01e01-scene-18.
ID = 'kukhnya-s01e01-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 18
TITLE = 'Кто здесь главный  (Who Is the Boss)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'Vika marches into the kitchen to stop Chef Barinov hiring Max. The chef will not be told what to do in his own kitchen, so he does the opposite: he hires Max on the spot. Here is the fight in Russian first.'
OPENER = "Let's take the argument slowly."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "So Max gets the job, mostly because the chef wanted to win an argument. You've also met the chef's nickname for him, which comes back again and again."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('vika', 'Виктор Петрович, этот парень здесь работать не будет!', 'Viktor Petrovich, this guy will not work here!', [(152, 'Он здесь работать не будет')], ''),
    ('barinov', 'Секундочку, с каких это пор ты здесь командуешь?', 'Just a second, since when do you give orders here?', [(154, 'С каких-то пор ты стала здесь командовать')], ''),
    ('vika', 'Я арт-директор ресторана и знаю наши стандарты!', 'I am the restaurant art director and know our standards!', [(152, 'Он здесь работать не будет')], ''),
    ('barinov', 'Сеня, скажи громко, кто на этой кухне главный?', 'Senya, say loudly, who is the boss in this kitchen?', [(156, 'Кто здесь главный')], ''),
    ('barinov', 'Все повара отлично знают, что я здесь главный.', 'All the cooks know perfectly well that I am the boss here.', [(158, 'в этой части к кухне я главный')], ''),
    ('vika', 'Вы нанимаете первого встречного человека с улицы!', 'You are hiring the first random person from the street!', [(153, 'Вот этот')], ''),
    ('barinov', 'Я один решаю, кому работать на моей кухне!', 'I alone decide who works in my kitchen!', [(162, 'я один буду решать'), (163, 'Кому работать на моей кухне')], ''),
    ('vika', 'Вы пожалеете об этом странном и глупом решении.', 'You will regret this strange and foolish decision.', [(152, 'Он здесь работать не будет')], ''),
    ('barinov', 'Огузок, ты официально принят в штат нашего ресторана!', 'Oguzok, you are officially hired onto our restaurant staff!', [(164, 'Агузок, ты принят в штат')], ''),
    ('barinov', 'Будешь работать по графику два через два.', 'You will work on a two-on, two-off schedule.', [(164, 'будешь работать два через два')], ''),
    ('vika', 'Это просто возмутительное и совершенно недопустимое поведение!', 'This is simply outrageous and completely unacceptable behavior!', [(152, 'не будет')], ''),
    ('barinov', 'А вы можете идти командовать своими официантами.', 'And you can go command your waiters.', [(165, 'А некоторые могут отправляться в зал командовать своими официантами')], ''),
    ('barinov', 'Создавайте прекрасную атмосферу в зале нашего заведения!', 'Create a wonderful atmosphere in the hall of our establishment!', [(166, 'неповторимые атмосферы нашего ресторана')], ''),
]
WALK = [
    (0, None, ['\'Viktor Petrovich, this guy will not work here!\' Vika uses the chef\'s first name and father\'s name, which is formal and a bit cold. ', ('vika', "Работать не будет"), ' is "work will-not", the "not" standing in front of "will".']),
    (1, None, ['\'Just a second, since when do you give orders here?\' ', ('barinov', "Секундочку"), ' is "second" with "-ochk-", a small ending that makes it "a little second". ', ('barinov', "с каких это пор"), ' is "since when", literally "from which times".']),
    (2, None, ['\'I am the restaurant art director and know our standards!\' ', ('vika', "Знаю"), ' is "I know" a fact; for a skill Russian uses ', 'a different word', '. ', ('vika', "Наши стандарты"), ' is "our standards", plural.']),
    (3, None, ['\'Senya, say loudly, who is the boss in this kitchen?\' ', ('barinov', "Скажи"), ' is the command form to say. ', ('barinov', "Главный"), ' means both "main" and "the boss", so ', ('barinov', "кто на этой кухне главный"), ' is "who\'s in charge".']),
    (4, None, ['\'All the cooks know perfectly well that I am the boss here.\' ', ('barinov', "Повара"), ' is the plural of ', ('barinov', "повар"), ', and the -a plural looks odd but is normal for some masculine words. ', ('barinov', "Знают"), ' is "they know".']),
    (5, None, ['\'You are hiring the first random person from the street!\' ', ('vika', "встречного"), ' is "met", from the word for meeting: the first person you happen to meet. ', ('vika', "Нанимаете"), ' is "you hire", a third way to say it. ', ('vika', "С улицы"), ' is "from the street".']),
    (6, None, ['\'I alone decide who works in my kitchen!\' ', ('barinov', "Один"), ' is "one", and here "alone". ', ('barinov', "Кому работать"), ' is "to whom to work", the Russian for "who gets to work". ', ('barinov', "На моей кухне"), ' is "in my kitchen".']),
    (7, None, ['\'You will regret this strange and foolish decision.\' ', ('vika', "Пожалеете"), ' is "you will regret", one word. ', ('vika', "решении"), ' is "decision" and comes from the verb to decide.']),
    (8, None, ['\'Oguzok, you are officially hired onto our restaurant staff!\' ', ('barinov', "Огузок"), ' is a butcher\'s word for a cut of beef from the rump, and Barinov makes it his nickname for Max. ', ('barinov', "Штат"), ' is the staff list, so ', ('barinov', "в штат"), ' is "onto the staff".']),
    (9, None, ['\'You will work on a two-on, two-off schedule.\' ', ('barinov', "Два через два"), ', literally "two through two", is everyday Russian shorthand for two days on, two days off. ', ('barinov', "Будешь работать"), ' builds the future the long way, "you will" plus "to work", because it\'s an ongoing routine.']),
    (10, None, ['\'This is simply outrageous and completely unacceptable behavior!\' ', ('vika', "Недопустимое"), ' is ', ('vika', "не"), ' plus ', ('vika', "допустимое"), ', permissible. Both big describing words end in "-oye" because ', ('vika', "поведение"), ' is a neuter word.']),
    (11, None, ['\'And you can go command your waiters.\' ', ('barinov', "Можете идти командовать"), ' is three words in a row, "can go command", with no "to" between them. ', ('barinov', "Официантами"), ' has the ending "-ami" that ', ('barinov', "командовать"), ' calls for.']),
    (12, None, ['\'Create a wonderful atmosphere in the hall of our establishment!\' ', ('barinov', "Создавайте"), ' is the polite command "create". ', ('barinov', "прекрасную"), ', the word Max used for Vika at night, here becomes ', ('barinov', "прекрасную"), ' because the atmosphere is the thing being created.']),
]