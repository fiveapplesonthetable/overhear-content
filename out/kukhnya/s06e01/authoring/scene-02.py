# Authoring module for kukhnya-s06e01-scene-02.
ID = 'kukhnya-s06e01-scene-02'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 2
TITLE = 'Инструктаж перед банкетом  (Pre-Banquet Briefing)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = 'Down in the kitchen, Chef Viktor Barinov gathers his culinary brigade before the wedding banquet for his ex-wife Eleonora and Dmitry Nagiyev, issuing a stern warning to Senya before a sudden wave of dizziness hits him.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Barinov blames his sudden dizziness on magnetic storms and retreats to his office to lie down. See you next time!'
CLOSING = ('barinov', 'Всего хорошего!')
STORY = [
    ('barinov', 'Все готово.', 'Everything is ready.', [(15, 'Все готово')], 'exact'),
    ('senya', 'Что?', 'What?', [(17, 'Что?')], 'exact'),
    ('barinov', 'Ничего, счастлив я сильно.', 'Nothing, I am very happy.', [(18, 'Счастлив я')], 'adapted'),
    ('barinov', 'Я надеюсь, вам повторять не надо.', 'I hope I do not need to repeat to you.', [(19, 'Я надеюсь, вам повторять не надо')], 'exact'),
    ('barinov', 'Сегодня очень важный банкет.', 'Today is a very important banquet.', [(20, 'сегодня очень важный банкет')], 'adapted'),
    ('barinov', 'И сразу предупреждаю всех.', 'And I am warning everyone right away.', [(22, 'И сразу предупреждаю всех')], 'exact'),
    ('barinov', 'Если пропадет омар, я тебя уволю.', 'If a lobster disappears, I will fire you.', [(23, 'Если пропадет хоть один')], 'adapted'),
    ('senya', 'Шеф, все за работу.', 'Chef, everyone back to work.', [(24, 'за работу')], 'adapted'),
    ('senya', 'Шеф, все в порядке?', 'Chef, is everything alright?', [(26, 'Все в порядке')], 'adapted'),
    ('barinov', 'Все в порядке, магнитные бури.', 'Everything is fine, just magnetic storms.', [(27, 'Магнитные бури')], 'adapted'),
    ('barinov', 'Пойду прилягу.', 'I will go lie down for a bit.', [(27, 'Пойду прилягу')], 'exact'),
    ('barinov', 'Что стоим?', 'Why are we standing around?', [(28, 'Что стоим?')], 'exact'),
]
WALK = [
    (0, None, '\'Everything is ready.\' Barinov holds a warm tempo across the room, building the phrase around "gotovo" ("ready") and "vse" ("all") for a crisp, natural delivery.'),
    (1, None, '\'What?\' Senya asks evenly in this moment, leaning on "chto" ("what") as a compact, one-word response that needs no extra words.'),
    (2, None, '\'Nothing, I am very happy.\' Barinov holds a resolute tempo without hesitation, anchoring the Russian line on "schastliv" ("happy, lucky") and "silno" ("strongly, much") without extra filler.'),
    (3, None, '\'I hope I do not need to repeat to you.\' Barinov sets an emphatic position beside Senya, putting "nadeyus" ("hope so") alongside "povtoryat" ("to repeat") in a tight, everyday turn of phrase.'),
    (4, None, '\'Today is a very important banquet.\' Barinov picks a firm style for Senya, weaving "segodnya" ("today") together with "ochen" ("very much") just the way native speakers do.'),
    (5, None, '\'And I am warning everyone right away.\' Barinov offers a sharp stance in their talk, leaning on "srazu" ("at once") before closing the thought with "preduprezhdayu" ("to warn").'),
    (6, None, '\'If a lobster disappears, I will fire you.\' Barinov chooses a pointed tempo straight away, leaning on "propadet" ("disappears") before closing the thought with "omar" ("lobster").'),
    (7, None, '\'Chef, everyone back to work.\' Senya establishes a sharp manner during the exchange, combining "rabotu" ("job") and "shef" ("Chef") so the key meaning lands right away.'),
    (8, None, '\'Chef, is everything alright?\' Senya inquires firmly in this moment, anchoring the Russian line on "poryadke" ("order") and "shef" ("Chef") without extra filler.'),
    (9, None, '\'Everything is fine, just magnetic storms.\' Barinov projects a playful tone in their talk, linking "poryadke" ("order") directly with "magnitnyye" ("magnetic"), since Russian drops "is" and "are" in the present.'),
    (10, None, '\'I will go lie down for a bit.\' Barinov displays a lively posture as the scene unfolds, combining "poydu" ("go") and "prilyagu" ("will lie down briefly") so the key meaning lands right away.'),
    (11, None, '\'Why are we standing around?\' Barinov checks briskly without a pause, joining "stoim" ("to stand") to "chto" ("what") so every word pulls its weight.'),
]
