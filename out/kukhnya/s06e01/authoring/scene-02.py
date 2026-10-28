ID = 'kukhnya-s06e01-scene-02'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 2
TITLE = "Инструктаж перед банкетом  (Pre-Banquet Briefing)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "chef": "anja", "senya": "angelina"}
LABELS = {"chef": "Шеф", "senya": "Сеня"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'

INTRO = 'Down in the kitchen, Chef Viktor Barinov gathers his culinary brigade before the wedding banquet for his ex-wife Eleonora and Dmitry Nagiyev, issuing a stern warning to Senya before a sudden wave of dizziness hits him.'

STORY = [
    ('chef', 'Все готово.', 'Everything is ready.', [(15, 'Все готово')], 'exact'),
    ('senya', 'Что?', 'What?', [(17, 'Что?')], 'exact'),
    ('chef', 'Ничего, счастлив я сильно.', 'Nothing, I am very happy.', [(18, 'Счастлив я')], 'adapted'),
    ('chef', 'Я надеюсь, вам повторять не надо.', 'I hope I do not need to repeat to you.', [(19, 'Я надеюсь, вам повторять не надо')], 'exact'),
    ('chef', 'Сегодня очень важный банкет.', 'Today is a very important banquet.', [(20, 'сегодня очень важный банкет')], 'adapted'),
    ('chef', 'И сразу предупреждаю всех.', 'And I am warning everyone right away.', [(22, 'И сразу предупреждаю всех')], 'exact'),
    ('chef', 'Если пропадет омар, я тебя уволю.', 'If a lobster disappears, I will fire you.', [(23, 'Если пропадет хоть один')], 'adapted'),
    ('senya', 'Шеф, все за работу.', 'Chef, everyone back to work.', [(24, 'за работу')], 'adapted'),
    ('senya', 'Шеф, все в порядке?', 'Chef, is everything alright?', [(26, 'Все в порядке')], 'adapted'),
    ('chef', 'Все в порядке, магнитные бури.', 'Everything is fine, just magnetic storms.', [(27, 'Магнитные бури')], 'adapted'),
    ('chef', 'Пойду прилягу.', 'I will go lie down for a bit.', [(27, 'Пойду прилягу')], 'exact'),
    ('chef', 'Что стоим?', 'Why are we standing around?', [(28, 'Что стоим?')], 'exact'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Everything is ready.' Notice how Russian expresses 'all' and 'ready' with crisp inflection rather than helper words."),
    (1, None, "'What?' Notice how Russian expresses 'what' and 'what' with crisp inflection rather than helper words. Chef Barinov answers right away."),
    (2, None, "'Nothing, I am very happy.' Chef Barinov brings out the contrast between 'nothing' and 'happy' in a few short words."),
    (3, None, "'I hope I do not need to repeat to you.' Notice how Russian expresses 'I' and 'need' with crisp inflection rather than helper words."),
    (4, None, "'Today is a very important banquet.' The grammar packs 'tonight' and 'banquet' into a tight, idiomatic kitchen exchange."),
    (5, None, "'And I am warning everyone right away.' The meaning hinges on 'and' working together with 'everyone' in spoken Russian."),
    (6, None, "'If a lobster disappears, I will fire you.' In Russian, the idea of 'if' flows naturally into 'will fire' without extra filler words."),
    (7, None, "'Chef, everyone back to work.' Spoken Russian keeps this brisk, leaning on 'Chef Barinov' and finishing on 'work'."),
    (8, None, "'Chef, is everything alright?' Senya anchors the line on 'Chef Barinov', while 'order' completes the thought."),
    (9, None, "'Everything is fine, just magnetic storms.' Here the Russian phrasing highlights 'all' before landing on 'storms'."),
    (10, None, "'I will go lie down for a bit.' Chef Barinov brings out the contrast between 'will go' and 'will lie down briefly' in a few short words."),
    (11, None, "'Why are we standing around?' Here the Russian phrasing highlights 'what' before landing on 'to stand'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Barinov blames his sudden dizziness on magnetic storms and retreats to his office to lie down. See you next time!'
CLOSING = ("chef", "Всего хорошего!")
