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
    (0, None, '\'Everything is ready.\' Barinov voices the comment right away: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (1, None, "'What?' Senya prompts openly where this conversation is heading next."),
    (2, None, '\'Nothing, I am very happy.\' Barinov frames this key word at once: "schastliv" means "happy, lucky" (from "schastlivyy"), giving the line its exact edge.'),
    (3, None, '\'I hope I do not need to repeat to you.\' Barinov shares that remark on cue: the single Russian word "nado" ("it is necessary, one needs to") sets up the whole statement without needing a separate word for "it is".'),
    (4, None, "'Today is a very important banquet.' Barinov holds firm promptly as things stand, testing Senya's reaction in the middle of the exchange."),
    (5, None, '\'And I am warning everyone right away.\' Barinov focuses on one colorful touch on cue: "preduprezhdayu" means "to warn" (from "preduprezhdat"), giving the line its exact edge.'),
    (6, None, '\'If a lobster disappears, I will fire you.\' Barinov points to this direct word on cue: "propadet" means "disappears" (from "propast"), giving the line its exact edge.'),
    (7, None, "'Chef, everyone back to work.' Senya cuts in sharply with a shrug, watching Barinov's face to see how the news lands."),
    (8, None, '\'Chef, is everything alright?\' Senya stresses this telling element in reply: "poryadke" means "order" (from "poryadok"), giving the line its exact edge.'),
    (9, None, '\'Everything is fine, just magnetic storms.\' Barinov makes this warning briskly now: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (10, None, "'I will go lie down for a bit.' Barinov pushes back pointedly facing Senya, bringing things back to earth after the buildup."),
    (11, None, '\'Why are we standing around?\' Barinov colors one concrete term toward Senya: "stoim" means "to stand" (from "stoyat"), giving the line its exact edge.'),
]
