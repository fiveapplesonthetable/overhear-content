# Authoring module for kukhnya-s02e01-scene-01.
ID = 'kukhnya-s02e01-scene-01'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = 'Новый хозяин  (The New Owner)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'igor': 'Игорь', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = 'In the dining room of Claude Monet, Dmitry Nagiyev shocks the staff by announcing that he has sold the entire restaurant to a strict new owner, Igor Valentinovich. Igor immediately pulls Chef Viktor aside to establish harsh new rules. Let us listen to their conversation in Russian first.'
OPENER = 'Now let us examine the arrival of the new owner line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "With Igor Valentinovich taking over Claude Monet, Chef Viktor faces an unprecedented ban on alcohol and the threat of losing his kitchen if he disobeys. Next time you watch the episode, listen for the Russian expressions for 'friend' and 'to sell' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('nagiyev', 'Друзья мои, я продал весь наш ресторан.', 'My friends, I sold our entire restaurant.', [(34, 'Ресторан я все тютю продал.')], ''),
    ('barinov', 'Дмитрий, кому вы продали этот прекрасный ресторан?', 'Dmitry, to whom did you sell this wonderful restaurant?', [(33, 'В смысле? В прямом.')], ''),
    ('nagiyev', 'Знакомьтесь, Игорь теперь ваш новый главный хозяин.', 'Meet Igor, he is now your new main owner.', [(30, 'Извини мне. Вон Игорь Валентинович.')], ''),
    ('igor', 'Добрый день, Виктор, давайте сразу серьёзно поговорим.', 'Good afternoon, Viktor, let us talk seriously right away.', [(47, 'Как раз об этом я с вами собирался серьезно поговорить.')], ''),
    ('barinov', 'О чём вы хотите говорить со мной?', 'What do you want to talk about with me?', [], ''),
    ('igor', 'Дмитрий сказал, что вы часто пьёте алкоголь.', 'Dmitry said that you often drink alcohol.', [(48, 'Дима рассказывал у вас проблемы с алкоголем.')], ''),
    ('barinov', 'У меня совсем нет проблем с алкоголем.', 'I have no problems with alcohol at all.', [(49, 'Никаких проблем с алкоголем.')], ''),
    ('igor', 'Вы прекрасно понимаете, о чём я говорю.', 'You understand very well what I am talking about.', [(51, 'Вы прекрасно понимаете, о чем я говорю.')], ''),
    ('igor', 'Сегодня я строго решил запретить пить здесь.', 'Today I strictly decided to forbid drinking here.', [(52, 'С сегодняшнего дня я запрещаю вам пить на работе.')], ''),
    ('barinov', 'А если я выпью немного вечером дома?', 'And what if I drink a little at home in the evening?', [(53, 'До работы, кстати, тоже.')], ''),
    ('igor', 'До работы тоже нельзя пить никакой алкоголь.', 'Before work you also cannot drink any alcohol.', [(53, 'До работы, кстати, тоже.')], ''),
    ('igor', 'Иначе мы быстро расстанемся с вами навсегда.', 'Otherwise we will quickly part ways with you forever.', [(54, 'Или считайте, что мы не сработались и нам надо расстаться.')], ''),
    ('barinov', 'Хорошо, хозяин, я понял ваши новые правила.', 'Fine, boss, I understood your new rules.', [(56, 'Хозяин барин, у вас все?')], ''),
]
WALK = [
    (0, None, "'My friends, I sold our entire restaurant.' Nagiyev drops the bombshell on the whole staff that he has sold the restaurant."),
    (1, None, "'Dmitry, to whom did you sell this wonderful restaurant?' Barinov is stunned and demands to know who bought his beloved kitchen."),
    (2, None, "'Meet Igor, he is now your new main owner.' Nagiyev introduces Igor as the new boss in charge of everyone."),
    (3, None, "'Good afternoon, Viktor, let us talk seriously right away.' Igor greets Viktor politely and asks for a serious private talk right away."),
    (4, None, "'What do you want to talk about with me?' Barinov wonders what the new owner wants to discuss with him."),
    (5, None, "'Dmitry said that you often drink alcohol.' Igor brings up the rumor from Dmitry about Viktor drinking on the job."),
    (6, None, "'I have no problems with alcohol at all.' Viktor immediately denies having any trouble with alcohol at all."),
    (7, None, "'You understand very well what I am talking about.' Igor does not buy the excuse and tells Viktor he knows the truth."),
    (8, None, "'Today I strictly decided to forbid drinking here.' the speaker puts the word for 'today' together with 'sternly' and 'has decided' in a crisp, natural spoken turn of phrase."),
    (9, None, "'And what if I drink a little at home in the evening?' Barinov tries to bargain for a little evening drink at home."),
    (10, None, "'Before work you also cannot drink any alcohol.' Igor shuts that down too, banning alcohol even before a shift starts."),
    (11, None, "'Otherwise we will quickly part ways with you forever.' the speaker expresses this naturally by combining the word for 'otherwise' with 'quickly' and 'will break up'."),
    (12, None, "'Fine, boss, I understood your new rules.' Left with no choice, Viktor reluctantly accepts the new owner's strict rules."),
]
