ID = 'kukhnya-s06e02-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 1
TITLE = "Разговор с рыбой и звонок олигарху  (Talking to the Fish and Calling the Oligarch)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "lyova": "angelina", "chef": "anja"}
LABELS = {"lyova": "Лёва", "chef": "Шеф"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'

INTRO = 'After his doctor warns him to avoid stress, Chef Viktor Barinov asks his aquarium fish Arkady whether he should quit the restaurant and calls oligarch Alyokhin to accept the private chef job.'

STORY = [
    ('chef', 'Давай, стреляй.', 'Go ahead, shoot.', [(2, 'Давай, стреляй')], 'exact'),
    ('chef', 'Может, действительно бросить этот дурдом?', 'Maybe I really should quit this madhouse?', [(3, 'а может, действительно бросить этот дурдом?')], 'adapted'),
    ('chef', 'А то помру раньше времени.', 'Otherwise I will die before my time.', [(4, 'А то помру')], 'adapted'),
    ('chef', 'И не будет у меня звезды.', 'And I will not have a star.', [(4, 'звезды')], 'adapted'),
    ('lyova', 'Витя, я же рыба.', 'Vitya, I am a fish.', [(5, 'Витя, я же рыба')], 'exact'),
    ('lyova', 'Решай сам.', 'Decide for yourself.', [(6, 'Решай сам')], 'exact'),
    ('chef', 'Я согласен у вас работать.', 'I agree to work for you.', [(8, 'Я согласен у вас работать')], 'exact'),
    ('lyova', 'Интересный был фильм, да?', 'It was an interesting movie, right?', [(9, 'Интересный был фильм, да?')], 'exact'),
    ('lyova', 'Не знаю, я на экран не смотрел особо.', 'I do not know, I did not really look at the screen.', [(9, 'Не знаю, я на экран не смотрел особо')], 'exact'),
    ('chef', 'Ну, я пошла?', 'Well, shall I go?', [(10, 'Ну, я пошла?')], 'exact'),
    ('lyova', 'Ну да, пока.', 'Well yes, bye.', [(11, 'Ну, да. Пока')], 'exact'),
    ('lyova', 'Идём гулять завтра.', "Let's go for a walk tomorrow.", [(12, 'Гулять')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Go ahead, shoot.' Chef Barinov anchors the line on 'come on', while 'shoot' completes the thought."),
    (1, None, "'Maybe I really should quit this madhouse?' The meaning hinges on 'maybe' working together with 'madhouse' in spoken Russian."),
    (2, None, "'Otherwise I will die before my time.' The meaning hinges on 'and' working together with 'time' in spoken Russian."),
    (3, None, "'And I will not have a star.' In Russian, the idea of 'and' flows naturally into 'star' without extra filler words."),
    (4, None, "'Vitya, I am a fish.' Spoken Russian keeps this brisk, leaning on 'I' and finishing on 'fish'."),
    (5, None, "'Decide for yourself.' Notice how Russian expresses 'to decide' and 'yourself' with crisp inflection rather than helper words. Chef Barinov answers right away."),
    (6, None, "'I agree to work for you.' Spoken Russian keeps this brisk, leaning on 'I' and finishing on 'to work'."),
    (7, None, "'It was an interesting movie, right?' In Russian, the idea of 'interesting' flows naturally into 'yes' without extra filler words."),
    (8, None, "'I do not know, I did not really look at the screen.' Spoken Russian keeps this brisk, leaning on 'not' and finishing on 'particularly'. Chef Barinov answers right away."),
    (9, None, "'Well, shall I go?' In Russian, the idea of 'come on' flows naturally into 'am off' without extra filler words."),
    (10, None, "'Well yes, bye.' The meaning hinges on 'come on' working together with 'for now' in spoken Russian."),
    (11, None, "'Let's go for a walk tomorrow.' In Russian, the idea of 'are going' flows naturally into 'tomorrow' without extra filler words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Having told the oligarch he will take the quiet private job, Barinov heads home to break the news to Elena. Until next time!'
CLOSING = ("lyova", "Хорошего дня!")
