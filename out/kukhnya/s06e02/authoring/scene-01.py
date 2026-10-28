# Authoring module for kukhnya-s06e02-scene-01.
ID = 'kukhnya-s06e02-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 1
TITLE = 'Разговор с рыбой и звонок олигарху  (Talking to the Fish and Calling the Oligarch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = 'After his doctor warns him to avoid stress, Chef Viktor Barinov asks his aquarium fish Arkady whether he should quit the restaurant and calls oligarch Alyokhin to accept the private chef job.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Having told the oligarch he will take the quiet private job, Barinov heads home to break the news to Elena. Until next time!'
CLOSING = ('lyova', 'Хорошего дня!')
STORY = [
    ('barinov', 'Давай, стреляй.', 'Go ahead, shoot.', [(2, 'Давай, стреляй')], 'exact'),
    ('barinov', 'Может, действительно бросить этот дурдом?', 'Maybe I really should quit this madhouse?', [(3, 'а может, действительно бросить этот дурдом?')], 'adapted'),
    ('barinov', 'А то помру раньше времени.', 'Otherwise I will die before my time.', [(4, 'А то помру')], 'adapted'),
    ('barinov', 'И не будет у меня звезды.', 'And I will not have a star.', [(4, 'звезды')], 'adapted'),
    ('lyova', 'Витя, я же рыба.', 'Vitya, I am a fish.', [(5, 'Витя, я же рыба')], 'exact'),
    ('lyova', 'Решай сам.', 'Decide for yourself.', [(6, 'Решай сам')], 'exact'),
    ('barinov', 'Я согласен у вас работать.', 'I agree to work for you.', [(8, 'Я согласен у вас работать')], 'exact'),
    ('lyova', 'Интересный был фильм, да?', 'It was an interesting movie, right?', [(9, 'Интересный был фильм, да?')], 'exact'),
    ('lyova', 'Не знаю, я на экран не смотрел особо.', 'I do not know, I did not really look at the screen.', [(9, 'Не знаю, я на экран не смотрел особо')], 'exact'),
    ('elena', 'Ну, я пошла?', 'Well, shall I go?', [(10, 'Ну, я пошла?')], 'exact'),
    ('lyova', 'Ну да, пока.', 'Well yes, bye.', [(11, 'Ну, да. Пока')], 'exact'),
    ('lyova', 'Идём гулять завтра.', "Let's go for a walk tomorrow.", [(12, 'Гулять')], 'adapted'),
]
WALK = [
    (0, None, '\'Go ahead, shoot.\' Barinov opens up calmly before Lyova and puts the weight on "strelyay" ("shoot", from "strelyat") as the exchange unfolds.'),
    (1, None, "'Maybe I really should quit this madhouse?' Returning to the madhouse in front of Lyova, Barinov keeps normal statement word order here, turning the line into a question for Lyova purely through rising pitch."),
    (2, None, "'Otherwise I will die before my time.' Barinov speaks up sharply watching Lyova, grounding the moment in plain reality."),
    (3, None, '\'And I will not have a star.\' Discussing the stars in the exchange, Barinov chooses "zvezdy" ("stars", from the root "zvezda") so Lyova hears the exact meaning.'),
    (4, None, '\'Vitya, I am a fish.\' Touching on a fish during the talk, Lyova links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (5, None, "'Decide for yourself.' Lyova replies wryly beside Barinov, testing Barinov's reaction in the middle of the exchange."),
    (6, None, '\'I agree to work for you.\' Barinov reacts evenly at once and brings in "soglasen" ("agreed", from "soglasnyy") as the key Russian word here.'),
    (7, None, "'It was an interesting movie, right?' Mentioning an interesting movie right here, Lyova keeps normal statement word order here, turning the line into a question for Barinov purely through rising pitch."),
    (8, None, "'I do not know, I did not really look at the screen.' Touching on the screen in their talk, Lyova brings the exchange with Elena back to practical reality."),
    (9, None, '\'Well, shall I go?\' Elena responds earnestly during the talk and centers the thought on "poshla" ("am off", from "poyti") without wasting a word.'),
    (10, None, '\'Well yes, bye.\' Lyova evenly chooses this casual farewell while facing Elena using "poka" ("bye") — the quick everyday word for "bye for now" between people on close terms.'),
    (11, None, "'Let's go for a walk tomorrow.' Lyova answers calmly without any doubt, keeping the focus on what actually matters here."),
]
