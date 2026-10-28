ID = 'kukhnya-s04e18-scene-03'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 18
SCENE = 3
TITLE = "Ролик из Риги  (The Video from Riga)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "chef": "anja", "senya": "angelina"}
LABELS = {"chef": "Шеф", "senya": "Сеня"}
SOURCE_NAME = 'Кухня (Kukhnya) S4.18'
SOURCE_FILE = 'sources/kukhnya/s04/e18.ru.srt'

INTRO = "In the kitchen of Claude Monet, Senya and Fedya browse online videos between orders and stumble upon a shocking clip. The video shows their new head chef German in a violent brawl, and Viktor Petrovich immediately recognizes another man in the footage. Let's listen to their discovery in Russian."

STORY = [
    ('chef', 'Там стейк из конины заказали.', 'They ordered a horsemeat steak out there.', [(21, 'Там стейк из конины заказали')], ''),
    ('senya', 'Смотри, есть ещё один ролик.', 'Look, there is one more video clip.', [(23, 'смотри. Есть еще ролик')], 'adapted'),
    ('chef', 'У него такое же название.', 'It has the exact same title.', [(23, 'с таким названием')], 'adapted'),
    ('senya', 'Это что, наш Герман, что ли?', 'Wait, is that our German or what?', [(24, 'Это'), (25, 'что, Герберт, что ли')], 'adapted'),
    ('chef', 'Интересно, где это всё было?', 'I wonder where all this took place?', [(26, 'Интересно, где это')], 'adapted'),
    ('chef', 'Останови, я его хорошо знаю.', 'Stop it, I know him well.', [(27, 'Останови. Я его знаю')], 'adapted'),
    ('chef', 'Он раньше в Риге работал.', 'He used to work in Riga.', [(28, 'Он в Риге работал')], 'adapted'),
    ('chef', 'Это же мой знакомый Маркус.', 'That is my acquaintance Markus.', [(29, 'Маркус')], 'adapted'),
    ('chef', 'Дай телефон, я ему позвоню.', 'Give me the phone, I will call him.', [], 'new'),
    ('chef', 'Алло, Маркус, привет, дорогой.', 'Hello, Markus, hi there, my friend.', [(30, 'Алло, Маркус, привет')], 'adapted'),
    ('chef', 'Расскажи мне про этого Германа.', 'Tell me about this German.', [], 'new'),
    ('chef', 'Спасибо тебе большое за информацию.', 'Thank you very much for the information.', [(31, 'Спасибо')], 'adapted'),
]

OPENER = "Now let's examine how the cooks uncover the video of German line by line."

WALK = [
    (0, None, "'They ordered a horsemeat steak out there.' An indefinite third-person plural past verb reports a customer order without naming a specific subject."),
    (1, None, "'Look, there is one more video clip.' Senya pairs 'watch' with 'video clip' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (2, None, "'It has the exact same title.' Russians say 'by me' or 'with us' where English says 'I have' or 'we have', without needing a separate word for 'have'."),
    (3, None, "'Wait, is that our German or what?' Colloquial question particles frame Senya's disbelief as he recognizes the new head chef on screen."),
    (4, None, "'I wonder where all this took place?' An impersonal introductory adverb meaning interesting leads into an indirect question about location."),
    (5, None, "'Stop it, I know him well.' Chef Barinov pairs 'stop' with 'know' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (6, None, "'He used to work in Riga.' Notice how Russian puts 'earlier' and 'worked' together in a short, direct phrase where word endings show how the ideas connect."),
    (7, None, "'That is my acquaintance Markus.' Here Chef Barinov anchors the thought on 'familiar' and finishes on 'markus', keeping the spoken rhythm brisk and natural."),
    (8, None, "'Give me the phone, I will call him.' In everyday Russian, 'give' flows straight into 'will call' without extra linking words."),
    (9, None, "'Hello, Markus, hi there, my friend.' Barinov greets his Latvian colleague warmly on the phone using standard telephone greetings."),
    (10, None, "'Tell me about this German.' Notice how Russian puts 'tell' and 'german' together in a short, direct phrase where word endings show how the ideas connect."),
    (11, None, "'Thank you very much for the information.' Chef Barinov uses a polite everyday Russian courtesy expression that sets the tone of the conversation right away."),
]

TRANSITION = "Let's hear the whole kitchen conversation again from start to finish."
OUTRO = 'Viktor Petrovich identifies his Riga acquaintance Markus in the video and calls him right away to get the full story. Notice the imperative verb meaning stop and the past-tense verb meaning worked. Until next time!'
CLOSING = ("chef", "До свидания!")
