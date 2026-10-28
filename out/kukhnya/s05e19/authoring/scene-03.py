# Authoring module for kukhnya-s05e19-scene-03.
ID = 'kukhnya-s05e19-scene-03'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 19
SCENE = 3
TITLE = 'План экономии и таинственная записка  (The Savings Plan and the Mysterious Note)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'katya': 'Катя', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.19'
SOURCE_FILE = 'sources/kukhnya/s05/e19.ru.srt'
INTRO = 'At the bar counter, Kostya tells Max that if he finds a way to reduce kitchen costs, Chef Barinov might raise his pay. Nearby, Katya finds the next clue inside the coffee maker and questions Denis.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Inspired by Kostya's advice, Max begins drafting a plan to optimize the kitchen budget. Until next time!"
CLOSING = ('kostya', 'Увидимся!')
STORY = [
    ('kostya', 'Или просто попроси у шефа повышения.', 'Or simply ask the chef for a promotion.', [(43, 'Ну или просто попроси повышения')], 'adapted'),
    ('max', 'Ага, повысить от огузка до старшего огузка.', 'Yeah, promote me from rookie to senior rookie.', [(44, 'У шефа повысить от')], 'adapted'),
    ('kostya', 'Найди способ, как уменьшить расходы кухни.', "Find a way to reduce the kitchen's expenses.", [(45, 'найди способ, как уменьшить расходы кухни')], 'adapted'),
    ('kostya', 'Тогда шеф точно повысит твою зарплату.', 'Then the chef will definitely raise your salary.', [(46, 'и шеф повысит')], 'adapted'),
    ('kostya', 'Вот я убрал из коктейля одну оливку.', 'For instance, I removed one olive from a cocktail.', [(47, 'Я убрал из коктейля одну оливку')], 'adapted'),
    ('kostya', 'Это хорошая экономия каждый месяц.', 'That is a nice savings every month.', [(48, 'в месяц')], 'adapted'),
    ('kostya', 'Ладно, давай мы попозже поговорим.', "Alright, let's talk a little later.", [(50, 'Ладно, давай позже поговорим')], 'adapted'),
    ('katya', 'Денис, ты ничего не хочешь мне сказать?', 'Denis, is there nothing you want to tell me?', [(51, 'Ты ничего не хочешь мне сказать')], 'adapted'),
    ('max', 'А что случилось, решила утром взбодриться?', 'What happened, did you decide to perk up this morning?', [(52, 'Что решила взбодриться')], 'adapted'),
    ('katya', 'Значит, эту записку написал не ты?', 'So you were not the one who wrote this note?', [(51, 'не хочешь мне сказать')], 'adapted'),
    ('max', 'Понятия не имею, о чём ты говоришь.', 'I have no idea what you are talking about.', [(50, 'поговорим')], 'adapted'),
    ('katya', 'Ладно, посмотрим, что будет дальше.', "Alright, let's see what happens next.", [(52, 'решила взбодриться')], 'adapted'),
]
WALK = [
    (0, None, "'Or simply ask the chef for a promotion.' Kostya proceeds at once with a shrug, watching Max's face to see how the news lands."),
    (1, None, '\'Yeah, promote me from rookie to senior rookie.\' Max responds briskly around Kostya and reaches for the Russian word "starshego" ("older, elder", built from "starshiy") right at the center of the line.'),
    (2, None, '\'Find a way to reduce the kitchen\'s expenses.\' Turning to the expenses to Max, Kostya chooses "raskhody" ("expenses", from the root "raskhod") so Max hears the exact meaning.'),
    (3, None, "'Then the chef will definitely raise your salary.' Kostya counters right away around Max, shifting the mood of the conversation in a single beat."),
    (4, None, '\'For instance, I removed one olive from a cocktail.\' Focusing on a cocktail around Max, Kostya puts the weight on "kokteylya" ("cocktail", from "kokteyl") as the exchange unfolds.'),
    (5, None, '\'That is a nice savings every month.\' Describing how good things are right here, Kostya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (6, None, '\'Alright, let\'s talk a little later.\' Kostya calmly chooses this word of agreement to Katya using "ladno" ("alright") — built from the old Russian root for harmony and order, used every day for "okay, fine".'),
    (7, None, '\'Denis, is there nothing you want to tell me?\' Katya pushes back decisively in this beat and leans on "khochesh" ("do you want", a form of "khotet") to give the remark its edge.'),
    (8, None, '\'What happened, did you decide to perk up this morning?\' Reacting dryly at once, the "-sya" ending on "vzbodritsya" ("to perk up") marks an action that unfolds mutually or turns back on the speaker.'),
    (9, None, "'So you were not the one who wrote this note?' Katya inquires eagerly before Max can change the subject."),
    (10, None, '\'I have no idea what you are talking about.\' Turning to the concept in front of Katya, Max puts the weight on "ponyatiya" ("concept, idea", from "ponyatiye") as the exchange unfolds.'),
    (11, None, '\'Alright, let\'s see what happens next.\' Katya gently voices this word of agreement toward Max using "ladno" ("alright") — built from the old Russian root for harmony and order, used every day for "okay, fine".'),
]
