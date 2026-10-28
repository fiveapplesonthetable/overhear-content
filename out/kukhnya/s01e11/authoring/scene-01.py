# Authoring module for kukhnya-s01e11-scene-01.
ID = 'kukhnya-s01e11-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 1
TITLE = 'Кто главный в ресторане  (Who Runs the Restaurant)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "At the Claude Monet bar counter, junior cook Max poses a philosophical question to his friend Kostya about restaurant hierarchy. They consider whether the director, head chef, or wealthy owner holds true power, before agreeing that the guests ultimately dictate everything. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine this barroom discussion line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "With their philosophical debate settled in favor of the customer, Max and Kostya return to their duties, ready to accommodate whatever demanding patrons arrive next. Next time you watch the episode, listen for the Russian expressions for 'rich' and 'to happen' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, кто самый главный в нашем ресторане?', 'Kostya, who is the most important in our restaurant?', [(1, 'кто главный в ресторане?')], ''),
    ('kostya', 'Может быть, наш строгий шеф-повар?', 'Maybe our strict head chef?', [(3, 'Шеф?')], ''),
    ('max', 'Или богатый хозяин ресторана Дмитрий?', 'Or the rich restaurant owner Dmitry?', [(4, 'ресторана?')], ''),
    ('kostya', 'А может, наш строгий директор Виктория?', 'Or maybe our strict director Victoria?', [(2, 'Директор?')], ''),
    ('max', 'Нет, самые главные здесь — это гости.', 'No, the most important here are the guests.', [(5, 'Главный в ресторане — это гости.')], ''),
    ('kostya', 'Это правда, наши гости бывают разные.', 'That is true, our guests can be very different.', [(7, 'гости бывают разные.')], ''),
    ('max', 'Одни гости бывают слишком жадными.', 'Some guests can be too stingy.', [(8, 'Бывают очень жадные.')], ''),
    ('kostya', 'Другие гости бывают очень весёлыми.', 'Other guests can be very cheerful.', [(13, 'Бывают очень')], ''),
    ('max', 'И они часто обнимают тебя?', 'And do they often hug you?', [], ''),
    ('kostya', 'Да, постоянно говорят разные добрые слова.', 'Yes, they constantly say various kind words.', [(17, 'Хороший ты парень, Костя.')], ''),
    ('max', 'Они платят деньги за этот обед.', 'They pay money for this lunch.', [], ''),
    ('kostya', 'Поэтому мы всегда улыбаемся каждому гостю.', 'Therefore we always smile at every guest.', [], ''),
    ('max', 'Гость всегда остаётся самым главным.', 'The guest always remains the most important.', [], ''),
]
WALK = [
    (0, None, "'Kostya, who is the most important in our restaurant?' Max asks Kostya who the most important person is in their restaurant. He uses 'samyy glavnyy' to mean the main one. He wonders who is the boss."),
    (1, None, "'Maybe our strict head chef?' Kostya guesses it might be their strict head chef. He adds 'mozhet byt' to mean maybe. It is a logical guess."),
    (2, None, "'Or the rich restaurant owner Dmitry?' Max suggests it could be the rich restaurant owner, Dmitry. He uses 'ili' meaning or. Owners usually hold the most power."),
    (3, None, "'Or maybe our strict director Victoria?' Kostya proposes another option, their strict director Victoria. He says 'a mozhet' as or maybe. She definitely acts like the boss."),
    (4, None, "'No, the most important here are the guests.' Max corrects him, stating that the guests are the most important here. He is sharing a service industry motto. The word 'gosti' means guests."),
    (5, None, "'That is true, our guests can be very different.' Kostya agrees this is true but notes their guests can be very different. He says 'eto pravda' for that is true. They see all kinds of people."),
    (6, None, "'Some guests can be too stingy.' Max points out that some guests can be too stingy. He uses 'odni' to mean some here. The word 'zhadnymi' describes greedy people."),
    (7, None, "'Other guests can be very cheerful.' Kostya adds that other guests can be very cheerful. He starts with 'drugie' meaning others. Cheerful guests are much better."),
    (8, None, "'And do they often hug you?' Max jokes by asking if they often hug the bartender. He is making a funny observation. 'Obnimayut' means they are hugging."),
    (9, None, "'Yes, they constantly say various kind words.' Kostya confirms and says they constantly say various kind words. He uses 'postoyanno' to mean constantly. It is nice when people are polite."),
    (10, None, "'They pay money for this lunch.' Max reminds him that they pay money for this lunch. This is the real reason they are important. Cash makes them the boss."),
    (11, None, "'Therefore we always smile at every guest.' Kostya concludes that therefore they always smile at every guest. He says 'poetomu' meaning for this reason. Smiling is part of their job."),
    (12, None, "'The guest always remains the most important.' Max states firmly that the guest always remains the most important. He sums up his initial point. The customer is king."),
]
