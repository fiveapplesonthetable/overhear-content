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
    ('barinov', 'Огузок, ты официально принят в штат нашего ресторана!', 'Rump, you are officially hired onto our restaurant staff!', [(164, 'Агузок, ты принят в штат')], ''),
    ('barinov', 'Будешь работать по графику два через два.', 'You will work on a two-on, two-off schedule.', [(164, 'будешь работать два через два')], ''),
    ('vika', 'Это просто возмутительное и совершенно недопустимое поведение!', 'This is simply outrageous and completely unacceptable behavior!', [(152, 'не будет')], ''),
    ('barinov', 'А вы можете идти командовать своими официантами.', 'And you can go command your waiters.', [(165, 'А некоторые могут отправляться в зал командовать своими официантами')], ''),
    ('barinov', 'Создавайте прекрасную атмосферу в зале нашего заведения!', 'Create a wonderful atmosphere in the hall of our establishment!', [(166, 'неповторимые атмосферы нашего ресторана')], ''),
]
WALK = [
    (0, None, '\'Viktor Petrovich, this guy will not work here!\' Vika uses the chef\'s first name and father\'s name, which is formal and a bit cold. "Rabotat\' ne budet" is "work will-not", the "not" standing in front of "will".'),
    (1, None, '\'Just a second, since when do you give orders here?\' "Sekundochku" is "second" with "-ochk-", a small ending that makes it "a little second". "S kakikh por" is "since when", literally "from which times".'),
    (2, None, '\'I am the restaurant art director and know our standards!\' "Znayu" is "I know" a fact; for a skill Russian uses "umeyu". "Nashi standarty" is "our standards", plural.'),
    (3, None, '\'Senya, say loudly, who is the boss in this kitchen?\' "Skazhi" is an irregular command, "say!". "Gromko" is "loudly". "Glavnyy" is both "main" and "boss".'),
    (4, None, '\'All the cooks know perfectly well that I am the boss here.\' "Povara" is the plural of "povar", and the -a plural looks odd but is normal for some masculine words. "Znayut" is "they know".'),
    (5, None, '\'You are hiring the first random person from the street!\' "Vstrechnyy" is "met", from "vstrecha", meeting: the first person you happen to meet. "Nanimayete" is "you hire", a third way to say it. "S ulitsy" is "from the street".'),
    (6, None, '\'I alone decide who works in my kitchen!\' "Odin" is "one", and here "alone". "Komu rabotat\'" is "to whom to work", the Russian for "who gets to work". "Na moyey kukhne" is "in my kitchen".'),
    (7, None, '\'You will regret this strange and foolish decision.\' "Pozhaleyete" is "you will regret", one word. "Resheniye" is "decision" and comes from "reshit\'", to decide.'),
    (8, None, '\'Rump, you are officially hired onto our restaurant staff!\' "Oguzok" is Barinov\'s nickname for Max, a cut of meat from the rear of the animal. "Shtat" is the staff roster, so "v shtat" is "onto the staff".'),
    (9, None, '\'You will work on a two-on, two-off schedule.\' "Budesh\' rabotat\'" is "you will work". "Dva cherez dva" is "two through two", the Russian shorthand for two days on, two days off.'),
    (10, None, '\'This is simply outrageous and completely unacceptable behavior!\' "Nedopustimoye" is "ne" plus "dopustimoye", permissible. Both big describing words end in "-oye" because "povedeniye" is a neuter word.'),
    (11, None, '\'And you can go command your waiters.\' "Mozhete idti komandovat\'" is three words in a row, "can go command", with no "to" between them. "Ofitsiantami" has the ending "-ami" that "komandovat\'" calls for.'),
    (12, None, '\'Create a wonderful atmosphere in the hall of our establishment!\' "Sozdavayte" is the formal command "create". "Prekrasnuyu" is the same "beautiful" Max used for Vika. The chef is being sarcastic.'),
]
