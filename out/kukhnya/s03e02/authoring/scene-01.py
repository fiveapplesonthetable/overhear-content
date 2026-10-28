# Authoring module for kukhnya-s03e02-scene-01.
ID = 'kukhnya-s03e02-scene-01'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 2
SCENE = 1
TITLE = "Терпение официанта  (A Waiter's Patience)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.02'
SOURCE_FILE = 'sources/kukhnya/s03/e02.ru.srt'
INTRO = 'In Episode Two of Season Three, Max reflects on what quality matters most for a waiter at Claude Monet: not just manners or dramatic presentation, but endless patience with indecisive guests.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes our opening scene. Listen for the contrast between the guest who orders a single coffee after ten minutes and the guest who leaves a generous tip. Until next time!'
CLOSING = ('max', 'До завтра!')
STORY = [
    ('max', 'Что самое важное в работе официанта?', "What is the most important thing in a waiter's job?", [(1, 'что самое важное в работе официанта')], ''),
    ('max', 'Манеры? Вежливость?', 'Manners? Politeness?', [(2, 'Манеры'), (3, 'Может быть')], 'adapted'),
    ('max', 'Эффектная подача блюд делает их вкуснее.', 'Spectacular presentation of dishes makes them tastier.', [(4, 'эффектная подача блюд'), (4, 'вкуснее')], 'adapted'),
    ('max', 'Индивидуальный подход?', 'An individual approach?', [(5, 'Индивидуальный подход')], ''),
    ('guest', 'Так, это мне нельзя. Это тоже.', 'Right, I am not allowed to have this. This either.', [(6, 'Так, это мне нельзя'), (7, 'Это тоже')], ''),
    ('max', 'По-моему, главное — это терпение.', 'In my opinion, the main thing is patience.', [(8, 'По-моему, главное в работе официанта – это терпение')], 'adapted'),
    ('guest', 'Знаете что, дайте мне кофе.', 'You know what, give me a coffee.', [(9, 'Знаете что, дайте мне кофе')], ''),
    ('guest', 'И всё.', 'And that is all.', [(10, 'И всё')], ''),
    ('max', 'Ты что делаешь? Заказал просто кофе!', 'What are you doing? He ordered just coffee!', [(11, 'Ты что делаешь'), (11, 'заказал просто кофе')], 'adapted'),
    ('guest', 'Кофе? Да, дайте мне кофе эспрессо.', 'Coffee? Yes, give me an espresso coffee.', [(13, 'Кофе? Да, дайте мне кофе эспрессо')], ''),
    ('guest', 'И вот, сдачи не надо.', 'And here, keep the change.', [(14, 'И вот, сдачи не надо')], ''),
    ('max', 'Порой терпение очень щедро вознаграждается.', 'Sometimes patience is very generously rewarded.', [(15, 'порой терпение в нашей работе очень щедро вознаграждается')], 'adapted'),
]
WALK = [
    (0, None, '\'What is the most important thing in a waiter\'s job?\' Highlighting a waiter on the spot, Max puts the weight on "ofitsianta" ("waiter", from "ofitsiant") as the exchange unfolds.'),
    (1, None, "'Manners? Politeness?' Dwelling on the politeness right here, Max keeps normal statement word order here, turning the line into a question for the guest purely through rising pitch."),
    (2, None, "'Spectacular presentation of dishes makes them tastier.' Max opens up firmly in this moment, bringing things back to earth after the buildup."),
    (3, None, '\'An individual approach?\' Mentioning an individual approach before the guest, Max puts the emphasis on "individualnyy" ("individual") in the middle of the talk.'),
    (4, None, '\'Right, I am not allowed to have this. This either.\' Pushing back firmly before Max, the guest leans on "nelzya" ("it is not allowed, one must not"), which carries the whole predicate in Russian without needing "it is".'),
    (5, None, "'In my opinion, the main thing is patience.' Max continues promptly in their talk, making his position completely clear."),
    (6, None, '\'You know what, give me a coffee.\' Highlighting a coffee right here, the guest chooses "kofe" ("of coffee") so Max gets the point right away.'),
    (7, None, '\'And that is all.\' Pressing on dryly beside Max, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (8, None, "'What are you doing? He ordered just coffee!' Max tests calmly before the guest can change the subject."),
    (9, None, '\'Coffee? Yes, give me an espresso coffee.\' Touching on an espresso at once, the guest puts the emphasis on "espresso" ("espresso") in the middle of the talk.'),
    (10, None, '\'And here, keep the change.\' Talking about the change during the talk, the guest leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
    (11, None, "'Sometimes patience is very generously rewarded.' Max opens up bluntly with a nod, before the guest can change the subject."),
]
