# Authoring module for kukhnya-s01e11-scene-23.
ID = 'kukhnya-s01e11-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 23
TITLE = 'Урок для критика  (A Lesson for the Critic)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "Something has happened in the dining room, and the cooks have seen it all. Senya and Fedya, two of the kitchen's gossips, report that Kostya did something brave and foolish. First, the language."
OPENER = "Now let's look at it closely."
TRANSITION = 'Now hear it again with fresh ears.'
OUTRO = "The bartender is a hero to the cooks and a problem for the chef. Whether it ends in a firing is the next scene's question. Speak soon."
CLOSING = ('senya', 'Пока!')
STORY = [
    ('senya', 'Ты видел, что сейчас произошло в зале?', 'Did you see what just happened in the hall?', [], ''),
    ('fedya', 'Наш бармен смело подошёл к столику критика.', "Our bartender boldly stepped up to the critic's table.", [], ''),
    ('senya', 'Этот критик опять грубо обижал нашу Настю.', 'This critic was rudely insulting our Nastya again.', [], ''),
    ('fedya', 'Костя не стал терпеть такое наглое поведение.', 'Kostya did not start tolerating such insolent behavior.', [], ''),
    ('senya', 'Что, гость заказал напиток из бара сейчас?', 'What, did the guest order a drink from the bar now?', [(311, 'что-то из вары заказал?')], ''),
    ('fedya', 'Точно, он получил заказ по полной программе!', 'Exactly, he received an order to the fullest program!', [(311, 'Точно, по полной заказал.')], ''),
    ('senya', 'Костя вылил стакан прямо на его костюм!', 'Kostya poured a glass right onto his suit!', [], ''),
    ('fedya', 'Наш тихий бармен оказался настоящим храбрым героем.', 'Our quiet bartender turned out to be a real brave hero.', [], ''),
    ('senya', 'Теперь этот важный критик весь мокрый сидит.', 'Now this important critic sits completely wet.', [], ''),
    ('fedya', 'Но шеф будет ужасно зол из-за скандала.', 'But the chef will be terribly angry because of the scandal.', [], ''),
    ('senya', 'Виктория уже быстро бежит в обеденный зал.', 'Viktoria is already quickly running into the dining hall.', [], ''),
    ('fedya', 'Косте сейчас точно грозит очень быстрое увольнение.', 'A very swift dismissal definitely threatens Kostya right now.', [], ''),
    ('senya', 'Зато он храбро защитил свою любимую девушку!', 'At least he courageously protected his beloved girl!', [], ''),
]
WALK = [
    (0, None, ["'Did you see what just happened in the hall?' Senya asks using the familiar form of address, as friends do. ", ('senya', 'видел'), ' is the masculine form of saw. ', ('senya', 'произошло'), ' is a more formal word for happened.']),
    (1, None, ["'Our bartender boldly stepped up to the critic's table.' Now let's analyze the speech: ", ('fedya', 'смело'), ' is boldly. ', ('fedya', 'подошёл'), ' means walked up, with a prefix for up to. ', ('fedya', 'столику'), ' is a small table, the term for tables in a restaurant.']),
    (2, None, ["'This critic was rudely insulting our Nastya again.' Now we can examine the phrase: ", ('senya', 'обижал'), ' is a repeated action, and the form shows it. ', ('senya', 'нашу'), ('senya', 'Настю'), ' is how they speak of someone they are fond of. Senya is outraged.']),
    (3, None, ["'Kostya did not start tolerating such insolent behavior.' We can inspect the speech: ", ('fedya', 'не'), ('fedya', 'стал'), ('fedya', 'терпеть'), " means did not become tolerating, and is the wording for didn't put up with it. ", ('fedya', 'поведение'), ' means behaviour. Fedya is full of admiration.']),
    (4, None, ["'What, did the guest order a drink from the bar now?' Senya's ", ('senya', 'Что'), ' here is a surprised what. ', ('senya', 'напиток'), ' means a drink. ', ('senya', 'из'), ('senya', 'бара'), ' is from the bar.']),
    (5, None, ["'Exactly, he received an order to the fullest program!' Now let's inspect the words: ", ('fedya', 'по'), ('fedya', 'полной'), ('fedya', 'программе'), ' means by the full programme, and is the idiom for the works. ', ('fedya', 'Точно'), ' is exactly. The critic got more than he ordered.']),
    (6, None, ["'Kostya poured a glass right onto his suit!' The prefix in ", ('senya', 'вылил'), ' means out, for poured. ', ('senya', 'стакан'), ' is the tall glass, and ', ('senya', 'костюм'), ' is suit. Senya says it with relish.']),
    (7, None, ["'Our quiet bartender turned out to be a real brave hero.' Let us consider the words: ", ('fedya', 'оказался'), ' is turned out to be, and after it hero changes its ending. ', ('fedya', 'храбрым'), ' is brave, and ', ('fedya', 'тихий'), ' is quiet. Fedya admires him.']),
    (8, None, ["'Now this important critic sits completely wet.' Let's focus on the phrase: ", ('senya', 'мокрый'), ' is wet. ', ('senya', 'весь'), ' means whole, and is used for completely here, all wet. Senya has an eye for the picture: the great man dripping at his table.']),
    (9, None, ["'But the chef will be terribly angry because of the scandal.' We will inspect the dialogue: ", ('fedya', 'из'), '-', ('fedya', 'за'), ' means because of, and is the small word that blames something. ', ('fedya', 'ужасно'), ' means terribly. Fedya sees the trouble coming.']),
    (10, None, ["'Viktoria is already quickly running into the dining hall.' Now we can consider the words: ", ('senya', 'быстро'), ' is quickly. ', ('senya', 'бежит'), ' means is running. Viktoria rushes to deal with the disaster.']),
    (11, None, ["'A very swift dismissal definitely threatens Kostya right now.' Now let's break down this part: ", ('fedya', 'грозит'), ' means threatens. ', ('fedya', 'увольнение'), " means dismissal. Fedya knows Barinov's temper."]),
    (12, None, ["'At least he courageously protected his beloved girl!' Let's break down this line: ", ('senya', 'Зато'), ' means at least, looking on the bright side. ', ('senya', 'защитил'), ' means protected. ', ('senya', 'любимую'), ('senya', 'девушку'), ' means beloved girl.']),
]
