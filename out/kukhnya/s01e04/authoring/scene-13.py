# Authoring module for kukhnya-s01e04-scene-13.
ID = 'kukhnya-s01e04-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 13
TITLE = 'Заказ у бара  (Order at the Bar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "At the bar, Nastya gives Kostya an urgent drinks order. Kostya, who is secretly in love with her, loses track of what she said and has to ask again. Here's the conversation in Russian first."
OPENER = 'Now the drinks order.'
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = 'Kostya makes the drinks, and Nastya hurries off. You\'ve heard "v luchshem vide", "in the best way", which means he\'ll do it properly.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('nastya', 'Костя, приготовь срочный заказ для гостей.', 'Kostya, prepare an urgent order for the guests.', [(166, 'мне коньяку')], ''),
    ('kostya', 'Я слушаю тебя очень внимательно.', 'I am listening to you very attentively.', [(168, 'Сделаем')], ''),
    ('nastya', 'Мне нужно триста грамм хорошего коньяка.', 'I need three hundred grams of good cognac.', [(166, 'коньяку 300')], ''),
    ('nastya', 'И налей два виски по сто грамм.', 'And pour two whiskeys of a hundred grams each.', [(166, 'виски два по сто')], ''),
    ('nastya', 'А ещё принеси три горячих чайника чая.', 'And also bring three hot pots of tea.', [(167, 'три чайника')], ''),
    ('kostya', 'Конечно, сделаем всё быстро и аккуратно.', 'Of course, we will do everything quickly and neatly.', [(168, 'Сделаем')], ''),
    ('nastya', 'Почему ты стоишь и не работаешь?', 'Why are you standing and not working?', [(169, 'И что мы стоим')], ''),
    ('kostya', 'Настя, я хотел спросить кое-что.', 'Nastya, I wanted to ask something.', [(170, 'Настя, а')], ''),
    ('nastya', 'Что именно ты хочешь узнать?', 'What exactly do you want to find out?', [(170, 'Что')], ''),
    ('kostya', 'Сколько именно виски нужно наливать в стаканы?', 'How much whiskey exactly do I need to pour into the glasses?', [(171, 'Сколько наливать')], ''),
    ('nastya', 'Два раза по сто грамм, как обычно!', 'Two times a hundred grams, as usual!', [(172, 'Два по сто')], ''),
    ('kostya', 'Понял, сейчас всё приготовлю в лучшем виде.', 'Got it, now I will prepare everything in the best way.', [(172, 'так и говори')], ''),
]
WALK = [
    (0, None, '\'Kostya, prepare an urgent order for the guests.\' "Prigotov\'" is the familiar command "prepare". "Srochnyy" is "urgent", and "dlya gostey" is "for the guests".'),
    (1, None, '\'I am listening to you very attentively.\' "Slushayu" is the present "I listen", which also covers "I am listening". "Vnimatel\'no" is "attentively".'),
    (2, None, '\'I need three hundred grams of good cognac.\' "Trista", three hundred, has "sta", a form of "sto", hundred. "Khoroshego kon\'yaka" takes the "of" endings -ego and -a.'),
    (3, None, '\'And pour two whiskeys of a hundred grams each.\' "Po sto" is "a hundred each", with "po" for each. "Viski" never changes its ending.'),
    (4, None, '\'And also bring three hot pots of tea.\' "Chaynik", teapot, is from "chay", tea. After "tri", it becomes "chaynika", and "goryachiy" becomes "goryachikh".'),
    (5, None, '\'Of course, we will do everything quickly and neatly.\' "Sdelayem" is "we\'ll do", one word. "Akkuratno" is "neatly", a borrowed word.'),
    (6, None, '\'Why are you standing and not working?\' "Stoish\'" is "you stand", Russian for being idle. "Ne rabotayesh\'" is "not working".'),
    (7, None, '\'Nastya, I wanted to ask something.\' "Koye-chto" is "something" in particular. "Khotel sprosit\'" is "wanted to ask".'),
    (8, None, '\'What exactly do you want to find out?\' "Imenno" is "exactly", pointing at the very thing. "Uznat\'" is "to find out".'),
    (9, None, '\'How much whiskey exactly do I need to pour into the glasses?\' "Skol\'ko", how much, also covers "how many". "V stakany" is "into the glasses", with the motion form of "v".'),
    (10, None, '\'Two times a hundred grams, as usual!\' "Dva raza" is "two times", with "raz" turning into "raza" after "dva". "Kak obychno" is "as usual".'),
    (11, None, '\'Got it, now I will prepare everything in the best way.\' "V luchshem vide" is "in the best form", a fixed phrase for doing a thing properly. "Prigotovlyu" is "I\'ll prepare".'),
]
