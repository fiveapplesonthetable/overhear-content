# Authoring module for kukhnya-s03e11-scene-03.
ID = 'kukhnya-s03e11-scene-03'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 11
SCENE = 3
TITLE = 'Гость из Парижа  (A Guest from Paris)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'katya': 'Катя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.11'
SOURCE_FILE = 'sources/kukhnya/s03/e11.ru.srt'
INTRO = 'Chef Barinov warmly greets his old Parisian friend Paul, who has been offered a job in Russia. Watching from the kitchen, Katya panics and confesses to Max that Paul was the curator at her culinary academy in Paris—from which she was expelled.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Chef Barinov proudly boasts about Katya graduating from the academy, completely unaware that she was expelled. Next, Barinov calls Katya out to say hello to Paul. Until next time!'
CLOSING = ('katya', 'Хорошего дня!')
STORY = [
    ('barinov', 'Виктор, как я рад тебя видеть!', 'Viktor, how glad I am to see you!', [(29, 'Виктор, как я рад тебя видеть')], 'adapted'),
    ('barinov', 'Это мой старый друг из Парижа.', 'This is my old friend from Paris.', [(30, 'друг из Парижа')], 'adapted'),
    ('barinov', 'Мы раньше долго работали вместе.', 'We used to work together for a long time.', [(31, 'Работали вместе')], 'adapted'),
    ('barinov', 'Ты когда приехал? Пойдём, всё расскажешь.', 'When did you arrive? Let us go, you will tell me everything.', [(32, 'Ты когда приехал')], 'adapted'),
    ('katya', 'Макс, откуда он здесь взялся?', 'Max, where did he come from here?', [(33, 'Откуда он взялся')], 'adapted'),
    ('max', 'Его Нагиев привёл, это знакомый шефа.', 'Nagiyev brought him, he is an acquaintance of the chef.', [(35, 'Его Нагиев привел, какой-то знакомый шефа')], 'adapted'),
    ('max', 'А ты тоже хорошо его знаешь?', 'Do you also know him well?', [(36, 'А ты что, тоже его знаешь')], 'adapted'),
    ('katya', 'Да, он учил нас в Париже.', 'Yes, he taught us in Paris.', [(38, 'запрос в Париж')], 'adapted'),
    ('katya', 'И меня ведь тогда выгнали оттуда.', 'And they kicked me out of there back then.', [(39, 'мне ответили, что тебя отчислили')], 'adapted'),
    ('barinov', 'Мне недавно предложили поработать в России.', 'I was recently offered work in Russia.', [(41, 'Мне предложили поработать в России')], 'adapted'),
    ('barinov', 'Работать в Москве сейчас хотят все.', 'Everyone wants to work in Moscow now.', [(42, 'работать хотят все')], 'adapted'),
    ('barinov', 'Катя тоже недавно вернулась сюда.', 'Katya also recently returned here.', [(43, 'Катя тоже после того, как закончила академию, вернулась сюда')], 'adapted'),
    ('barinov', 'Теперь она работает у меня здесь.', 'Now she works for me here.', [(44, 'Теперь работает у меня')], 'adapted'),
]
WALK = [
    (0, None, "'Viktor, how glad I am to see you!' Barinov reacts quietly in their talk, keeping the focus on what actually matters here."),
    (1, None, '\'This is my old friend from Paris.\' Talking about the friend before Katya, Barinov leans on "staryy" ("old") to give the whole sentence its punch.'),
    (2, None, '\'We used to work together for a long time.\' Barinov jumps in dryly with Katya and puts the weight on "rabotali" ("worked", from "rabotat") as the exchange unfolds.'),
    (3, None, "'When did you arrive? Let us go, you will tell me everything.' Barinov wonders plainly whether Katya really thought this through."),
    (4, None, '\'Max, where did he come from here?\' Katya chimes in smoothly in the exchange and chooses "vzyalsya" ("appeared, came from", from the root "vzyatsya") so Max hears the exact meaning.'),
    (5, None, '\'Nagiyev brought him, he is an acquaintance of the chef.\' Stressing how familiar he is around Barinov, Max leans on "znakomyy" ("familiar") to give the whole sentence its punch.'),
    (6, None, "'Do you also know him well?' Max presses evenly if there is more going on behind the scenes."),
    (7, None, '\'Yes, he taught us in Paris.\' Katya reacts plainly before Max and brings in "uchil" ("to learn, to teach", from "uchit") as the key Russian word here.'),
    (8, None, '\'And they kicked me out of there back then.\' Katya answers directly in this beat and puts the weight on "vygnali" ("kicked out", from "vygnat") as the exchange unfolds.'),
    (9, None, "'I was recently offered work in Russia.' Barinov cuts in wryly around Katya, grounding the moment in plain reality."),
    (10, None, '\'Everyone wants to work in Moscow now.\' Barinov pushes back earnestly right here and brings in "rabotat" ("to work") to make the meaning unmistakable.'),
    (11, None, '\'Katya also recently returned here.\' Jumping in quietly around Katya, the "-sya" ending on "vernulas" ("returned") marks an action that unfolds mutually or turns back on the speaker.'),
    (12, None, "'Now she works for me here.' Barinov follows up warmly toward Katya, steering the talk right where he wants it."),
]
