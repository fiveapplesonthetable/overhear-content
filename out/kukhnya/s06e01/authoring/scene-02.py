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
    (0, None, "'Everything is ready.' Even though everything is ready, Barinov keeps a steady face in front of Senya."),
    (1, None, '\'What?\' Over the banquet and the wedding, Senya presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'Nothing, I am very happy.' Saying that nothing he is very happy is how Barinov sets the tone with Senya."),
    (3, None, '\'I hope I do not need to repeat to you.\' Realizing that he hopes he does not need to repeat to Senya changes how Barinov handles the situation. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (4, None, "'Today is a very important banquet.' Adding that today is a very important banquet fills in the missing piece for Senya."),
    (5, None, "'And I am warning everyone right away.' Claiming that he is warning everyone right away sounds confident, even if Senya has doubts."),
    (6, None, '\'If a lobster disappears, I will fire you.\' Since if a lobster disappears he will fire Senya, Barinov does not waste words on excuses. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (7, None, "'Chef, everyone back to work.' Between the conversation and the wedding, Senya gives Barinov a quick, grounded response."),
    (8, None, "'Chef, is everything alright?' Asking whether everything alright cuts straight through the tension between Senya and Barinov."),
    (9, None, "'Everything is fine, just magnetic storms.' Because everything is fine just magnetic storms, Barinov treats the matter as settled."),
    (10, None, "'I will go lie down for a bit.' Explaining that he will go lie down for a bit lays the cards on the table for Senya."),
    (11, None, "'Why are we standing around?' Asking why they standing around are is how Barinov puts Senya on the spot."),
]
