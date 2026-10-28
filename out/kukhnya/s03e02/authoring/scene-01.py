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
    (0, None, '\'What is the most important thing in a waiter\'s job?\' Max queries lightly as they speak, linking "samoye" ("the most"), "vazhnoye" ("important"), and "rabote" ("work") in one brisk exchange.'),
    (1, None, '\'Manners? Politeness?\' Max queries candidly in the room, leaning on "manery" ("manners") before closing the thought with "vezhlivost" ("politeness").'),
    (2, None, '\'Spectacular presentation of dishes makes them tastier.\' Max establishes a measured course as the scene unfolds, combining "effektnaya" ("spectacular") and "podacha" ("presentation") so the key meaning lands right away.'),
    (3, None, '\'An individual approach?\' Max prompts naturally in this moment, pairing "individualnyy" ("individual") with "podkhod" ("approach") to get the point across in plain spoken Russian.'),
    (4, None, '\'Right, I am not allowed to have this. This either.\' The guest brings a calm note for Max, linking "nelzya" ("not allowed") directly with "tozhe" ("too"), since Russian drops "is" and "are" in the present.'),
    (5, None, '\'In my opinion, the main thing is patience.\' Max establishes a sharp attitude at once, weaving "po-moyemu" ("in my opinion") together with "glavnoye" ("important") just the way native speakers do.'),
    (6, None, '\'You know what, give me a coffee.\' The guest displays a direct style without hesitation, putting "znayete" ("know") alongside "dayte" ("give") in a tight, everyday turn of phrase.'),
    (7, None, '\'And that is all.\' The guest holds a candid position with Max, leaning on "vsyo" ("everything") as a compact, one-word response that needs no extra words.'),
    (8, None, '\'What are you doing? He ordered just coffee!\' Max prompts steadily as the beat lands, linking "delayesh" ("are you doing"), "zakazal" ("ordered"), and "prosto" ("just") in one brisk exchange.'),
    (9, None, '\'Coffee? Yes, give me an espresso coffee.\' The guest probes naturally in the room, linking "kofe" ("of coffee"), "dayte" ("give"), and "espresso" ("espresso") in one brisk exchange.'),
    (10, None, '\'And here, keep the change.\' The guest shares a candid direction on the spot, combining "sdachi" ("change, surrender") and "nado" ("it is necessary") so the key meaning lands right away.'),
    (11, None, '\'Sometimes patience is very generously rewarded.\' Max displays a candid view toward the guest, pairing "poroy" ("at times, occasionally") with "terpeniye" ("patience") to get the point across in plain spoken Russian.'),
]
