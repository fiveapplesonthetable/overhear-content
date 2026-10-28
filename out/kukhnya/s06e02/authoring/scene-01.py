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
    (0, None, "'Go ahead, shoot.' Realizing that Elena should go ahead shoot changes how Barinov handles the situation."),
    (1, None, '\'Maybe I really should quit this madhouse?\' Barinov asks whether maybe he really should quit this madhouse, refusing to let the point slide. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'Otherwise I will die before my time.' Realizing that otherwise he will die before his time changes how Barinov handles the situation."),
    (3, None, "'And I will not have a star.' Noting that he will not have a star keeps Barinov's side of the story simple and clear."),
    (4, None, "'Vitya, I am a fish.' Saying that he is a fish is how Lyova sets the tone with Barinov."),
    (5, None, "'Decide for yourself.' Even though Barinov should decide for themselves, Lyova keeps a steady face in front of Barinov."),
    (6, None, "'I agree to work for you.' Noting that he agrees to work for Elena keeps Barinov's side of the story simple and clear."),
    (7, None, '\'It was an interesting movie, right?\' Questioning whether it was an interesting movie right is how Lyova tests Barinov\'s story. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, "'I do not know, I did not really look at the screen.' Around the moment and doctor, Lyova sets a calm, everyday tone with Barinov."),
    (9, None, "'Well, shall I go?' Elena asks whether shall she goes, refusing to let the point slide."),
    (10, None, "'Well yes, bye.' Between the moment and the doctor, Lyova gives Barinov a quick, grounded response."),
    (11, None, "'Let's go for a walk tomorrow.' Explaining that they should go for a walk tomorrow lays the cards on the table for Barinov."),
]
