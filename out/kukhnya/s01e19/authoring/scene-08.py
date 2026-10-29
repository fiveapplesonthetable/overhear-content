# Authoring module for kukhnya-s01e19-scene-08.
ID = 'kukhnya-s01e19-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 8
TITLE = 'Новый план  (The New Plan)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Later at the bar, Kostya tries to cheer Max up after that bouquet, with a line about boats and the ocean. Listen in Russian before anything else; don't chase every word."
OPENER = "Now let's go through the pep talk slowly."
TRANSITION = "Here's the whole pep talk again, boat and all."
OUTRO = "Kostya's big wisdom turned out to be borrowed, but you can now say \"glavnoe\" for 'the main thing'. See you next time!"
CLOSING = ('kostya', 'Ладно, увидимся!')
STORY = [
    ('kostya', 'Макс, ты только не переживай.', 'Max, just do not worry.', [(174, 'Ты только не переживай')], ''),
    ('max', 'А как тут не переживать?', 'And how can I not worry here?', [], ''),
    ('max', 'Ты видел этот огромный букет?', 'Did you see that huge bouquet?', [], ''),
    ('kostya', 'Размер букета совсем не важен.', 'The size of the bouquet is not important at all.', [], ''),
    ('kostya', 'Главное — это не размер лодки.', 'The main thing is not the size of the boat.', [(175, 'Главное же, это не размер лодки')], ''),
    ('kostya', 'Главное — это волнение океана.', 'The main thing is the swell of the ocean.', [(175, 'волнение океана')], ''),
    ('max', 'Подожди, откуда такие красивые слова?', 'Wait, where are such beautiful words from?', [], ''),
    ('max', 'Ты что, чей-то статус в интернете прочитал?', "Did you read someone's status on the internet?", [(176, 'Ты что, чей-то статус в интернете прочитал?')], ''),
    ('kostya', 'Да, это Настин новый статус.', "Yes, it is Nastya's new status.", [(177, 'Настин')], ''),
    ('kostya', 'Она написала это сегодня утром.', 'She wrote it this morning.', [], ''),
    ('kostya', 'Интересно, о чём это она?', 'I wonder what she is hinting at?', [(178, 'Интересно, о чем')], ''),
    ('max', 'Наверное, она пишет про ваши отношения.', 'Probably she is writing about your relationship.', [], ''),
]
WALK = [
    (0, None, "'Max, just do not worry.' \"Ne perezhivay\", 'don't worry', is one of the most useful lines in Russian. \"Tol'ko\", usually 'only', here softens it to 'just'."),
    (1, None, "'And how can I not worry here?' Russian asks this with the dictionary form: \"kak ne perezhivat'\", 'how not to worry'. No 'I' or 'can' is needed."),
    (2, None, "'Did you see that huge bouquet?' \"Videl\", 'saw', is the form for a man, because Kostya is the one asked. \"Buket\" comes from French bouquet."),
    (3, None, "'The size of the bouquet is not important at all.' \"Razmer buketa\" is 'size of the bouquet', with -a doing the work of 'of'. \"Vazhen\" is the short form of \"vazhny\", 'important'."),
    (4, None, "'The main thing is not the size of the boat.' \"Glavnoe\", 'the main thing', starts countless Russian sentences. \"Lodka\", 'boat', becomes \"lodki\" after \"razmer\"."),
    (5, None, "'The main thing is the swell of the ocean.' \"Volnenie\" comes from \"volna\", 'wave', and it also means 'nerves, excitement'. So the line is a pun about feelings."),
    (6, None, "'Wait, where are such beautiful words from?' Otkuda means 'from where'. Russian keeps three of these apart: \"gde\" 'where', \"kuda\" 'where to' and otkuda 'where from'."),
    (7, None, "'Did you read someone's status on the internet?' Add '-to' to 'chey', whose, and you get 'chey-to', someone's. 'Prochital' is masculine past, so Max is teasing a man."),
    (8, None, "'Yes, it is Nastya's new status.' \"Nastin\" means 'Nastya's'; add -in to a name like hers and you get 'belonging to'. \"Mama\" gives \"mamin\", 'Mum's'."),
    (9, None, "'She wrote it this morning.' \"Segodnya utrom\" is 'this morning', literally 'today in the morning'. \"Napisala\", 'wrote', has a feminine -a, since Nastya is the writer."),
    (10, None, "'I wonder what she is hinting at?' \"Interesno\", 'interesting', opens the sentence where English says 'I wonder'. \"O chyom\", 'about what', asks what something's about."),
    (11, None, "'Probably she is writing about your relationship.' \"Vashi\", 'your', is plural because Max means Kostya and Nastya. \"Pro\", 'about', is the chattier partner of \"o\"."),
]
