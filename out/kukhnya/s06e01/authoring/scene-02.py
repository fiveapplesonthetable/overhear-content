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
    (0, None, '\'Everything is ready.\' Confirming how ready things are during the talk, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (1, None, "'What?' Senya prompts openly before Barinov can change the subject."),
    (2, None, '\'Nothing, I am very happy.\' Showing how happy he is with Senya, Barinov centers the thought on "schastliv" ("happy, lucky", from "schastlivyy") without wasting a word.'),
    (3, None, '\'I hope I do not need to repeat to you.\' Opening up smoothly with Senya, Barinov leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
    (4, None, "'Today is a very important banquet.' Barinov continues promptly without a pause, to clear the air between them once and for all."),
    (5, None, '\'And I am warning everyone right away.\' Barinov follows up plainly with Senya and leans on "preduprezhdayu" ("to warn", a form of "preduprezhdat") to give the remark its edge.'),
    (6, None, "'If a lobster disappears, I will fire you.' Barinov cuts in calmly without holding back, letting the remark speak for itself."),
    (7, None, "'Chef, everyone back to work.' Senya responds sharply toward Barinov, testing Barinov's reaction in the middle of the exchange."),
    (8, None, '\'Chef, is everything alright?\' Bringing up the order beside Barinov, Senya uses "poryadke" ("order", from "poryadok") to make the point stick.'),
    (9, None, '\'Everything is fine, just magnetic storms.\' Noting how magnetic things are in this beat, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (10, None, "'I will go lie down for a bit.' Barinov reacts pointedly with Senya, making his position completely clear."),
    (11, None, '\'Why are we standing around?\' Barinov opens up firmly during the talk and brings in "stoim" ("to stand", from "stoyat") as the key Russian word here.'),
]
