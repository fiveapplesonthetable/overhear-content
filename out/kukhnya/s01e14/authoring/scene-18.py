# Authoring module for kukhnya-s01e14-scene-18.
ID = 'kukhnya-s01e14-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 18
TITLE = 'Режим терминатора  (Terminator Mode)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'lyova': 'Лёва', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'Lyova is in charge of the kitchen and he has found his voice. Senya and Fedya encourage him as he tries to speed up the cooks. Hear it in Russian first.'
OPENER = 'Again, and listen to how the cooks cheer him on.'
TRANSITION = 'Now the pep talk again, in full.'
OUTRO = "The Terminator is switched on, and the orders are on their way. Notice how often everyone says 'let's go' and 'faster' here. Until the next scene."
CLOSING = ('senya', 'Пока!')
STORY = [
    ('lyova', 'Ребята, давайте работать быстрее.', "Guys, let's work faster.", [(273, 'Ребят, давайте ускоримся.')], ''),
    ('lyova', 'У нас ещё три блюда.', 'We still have three dishes.', [(274, 'У нас три блюда еще.')], ''),
    ('fedya', 'Сейчас мы всё сделаем.', 'We will do everything now.', [(275, 'Сейчас все сделаем.')], ''),
    ('senya', 'Ну, чего вы стоите?', 'Well, why are you standing?', [(276, 'Ну что встали?')], ''),
    ('senya', 'Шеф сказал работать быстрее.', 'The chef said to work faster.', [(276, 'Шеф сказал ускориться.')], ''),
    ('senya', 'Молодец, Лёва.', 'Well done, Lyova.', [(277, 'Ай, молодец, Лёва, шеф.')], ''),
    ('senya', 'Ты хороший шеф.', 'You are a good chef.', [(277, 'Ай, молодец, Лёва, шеф.')], ''),
    ('lyova', 'Ты молодец.', 'You did great.', [(278, 'Молодец ты.')], ''),
    ('fedya', 'Ну что, мы включаем режим терминатора?', 'Well, are we switching on Terminator mode?', [(279, 'Ну что, включаем режим терминатора?')], ''),
    ('lyova', 'Да, включаем.', 'Yes, we are switching it on.', [], ''),
    ('senya', 'Тогда быстрее за работу.', 'Then faster to work.', [], ''),
    ('fedya', 'Терминатор готов готовить еду.', 'The terminator is ready to cook food.', [], ''),
    ('lyova', 'Отлично, давайте быстрее.', "Excellent, let's go faster.", [], ''),
    ('senya', 'Всё будет готово вовремя.', 'Everything will be ready on time.', [], ''),
]
WALK = [
    (0, None, ["'Guys, let's work faster.' We will focus on the words: ", ('lyova', 'Ребята'), ' is a friendly term for a group. ', ('lyova', 'давайте'), " is used with an action to mean 'let's'."]),
    (1, None, ["'We still have three dishes.' We can analyze the sentence: ", ('lyova', 'У'), ('lyova', 'нас'), " is how you say 'we have'. After ", ('lyova', 'три'), ", meaning 'three', the word for dish changes its ending."]),
    (2, None, ["'We will do everything now.' Let's inspect the dialogue: ", ('fedya', 'сделаем'), ' describes a completed action, so it points to the future here. ', ('fedya', 'Сейчас'), " can mean 'right now' or 'in a second'."]),
    (3, None, ["'Well, why are you standing?' Let us analyze this part: ", ('senya', 'чего'), " literally means 'of what', and in casual speech it's a blunt 'why'. It is what you'd say to people who should be moving."]),
    (4, None, ["'The chef said to work faster.' After ", ('senya', 'сказал'), ", which means 'said', the order follows in its basic form. That's how you report an instruction."]),
    (5, None, ["'Well done, Lyova.' We will analyze the phrase: ", ('senya', 'Молодец'), " is the standard way to say 'well done', and it can be used for anyone."]),
    (6, None, ["'You are a good chef.' The sentence has no verb, just 'you good chef'. ", ('senya', 'хороший'), " uses that ending because 'chef' refers to a man."]),
    (7, None, ["'You did great.' Lyova hands the praise straight back with ", ('lyova', 'Ты'), ('lyova', 'молодец'), ". It's a natural way to say 'you too'."]),
    (8, None, ["'Well, are we switching on Terminator mode?' Let's break down the phrase: ", ('fedya', 'включаем'), ' is the verb for switching on lights, machines, and modes alike. ', ('fedya', 'терминатора'), " has an ending that means 'of'."]),
    (9, None, ["'Yes, we are switching it on.' Lyova answers with Fedya's own verb, ", ('lyova', 'включаем'), ". Repeating the verb is a natural way to say 'yes, we are'."]),
    (10, None, ["'Then faster to work.' Let us inspect this line: ", ('senya', 'за'), ('senya', 'работу'), ' is the set call to get started. No verb is needed.']),
    (11, None, ["'The terminator is ready to cook food.' Now we can focus on the phrase: ", ('fedya', 'готов'), ' and ', ('fedya', 'готовить'), " share a root, so it sounds like 'ready to ready'. Fedya is playing with the words."]),
    (12, None, ["'Excellent, let's go faster.' Now let's consider the speech: ", ('lyova', 'Отлично'), ' on its own is a full reply. ', ('lyova', 'быстрее'), " is the comparing form of 'quickly'."]),
    (13, None, ["'Everything will be ready on time.' The ending of the term for 'ready' changes to match 'everything', so it becomes ", ('senya', 'готово'), '. ', ('senya', 'вовремя'), ' is written as a single word.']),
]
