# Authoring module for domashniy-arest-s01e04-scene-10.
ID = 'domashniy-arest-s01e04-scene-10'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 10
TITLE = 'Будущий мэр  (The Future Mayor)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'samson': 'Самсон', 'yulia': 'Юля'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "Last time, passers-by recognised Samson in his giant waffle-cone costume and crowded around him for selfies. Back in the communal flat, Arkady paces his room inventing a campaign slogan while the secret-service agents watch him through binoculars from across the street and wonder if he has lost his mind. Then Samson storms home furious at Yulia for posting the video. Let's listen in Russian first."
OPENER = "Let's walk through it. First, in his room, Arkady is already planning Samson's election campaign out loud."
TRANSITION = "Now let's listen to the whole scene in the communal flat again."
OUTRO = "So Arkady unveils his grand plan to the Samsonov family: turn viral hero Ivan Samsonov into the next mayor of Sineozersk. Listen for the slogan 'Everyone talks, while I do!' when you watch. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Какой наш кандидат? Простой, работящий, свой!', 'What is our candidate like? Simple, hardworking, one of our own!', [(280, 'наш'), (282, 'Простой, работящий'), (283, 'Свой')], ''),
    ('arkady', 'Не словом, а делом! Все болтают, а я работаю.', 'Not in word, but in deed! Everyone chatters, while I work.', [(284, 'Не словом, а делом'), (286, 'Все болтают, а я работаю')], ''),
    ('arkady', 'Нет, лучше так: все говорят, а я делаю! Прекрасно.', 'No, better like this: everyone talks, while I do! Excellent.', [(280, 'Нет'), (287, 'Все говорят, а я делаю'), (293, 'Прекрасно')], ''),
    ('samson', 'Юля, ты что сделала?', 'Yulia, what have you done?', [(319, 'ты что сделала')], "'Юль' -> 'Юля'"),
    ('yulia', 'А что? Папа у нас теперь звезда!', 'What? Dad is a star now!', [(320, 'А что? Папа у нас теперь звезда')], ''),
    ('samson', 'Звезда? Ты зачем это видео в интернет выложила?', 'A star? Why did you post that video on the internet?', [(321, 'Звезда? Ты зачем это')], "cue 321 slip 'выложил-то' -> feminine 'выложила', 'видео в интернет' added"),
    ('yulia', 'Ролик уже набрал четыре миллиона просмотров!', 'The clip has already got four million views!', [(318, 'Ролик уже набрал'), (318, 'просмотров')], "TV news line in cue 318 spoken by Yulia; '4' written out"),
    ('samson', 'Там на улице журналисты! Они меня ждут!', "There are reporters out on the street! They're waiting for me!", [], 'summarising the reporters outside the flat in cues 297-305'),
    ('arkady', 'Друзья мои, не ссорьтесь, пожалуйста.', "My friends, please don't quarrel.", [(323, 'Друзья мои, не ссорьтесь, пожалуйста')], ''),
    ('arkady', 'На самом деле вчера был судьбоносный день.', 'In fact, yesterday was a fateful day.', [(324, 'На самом деле вчера был судьбоносный день')], ''),
    ('arkady', 'Вы думаете, перед вами стоит простой Ваня Самсонов?', 'Do you think ordinary Vanya Samsonov is standing before you?', [(325, 'Вы думаете, перед вами стоит простой'), (325, 'Самсонов')], "'Ванька' -> 'Ваня'"),
    ('samson', 'А кто же ещё?', 'Who else, then?', [], "Samson's baffled reaction"),
    ('arkady', 'Нет, друзья мои! Перед вами стоит Иван Васильевич Самсонов.', 'No, my friends! Standing before you is Ivan Vasilyevich Samsonov.', [(326, 'Нет, друзья мои'), (327, 'Перед вами'), (328, 'Иван Васильевич Самсонов')], ''),
    ('arkady', 'Это будущий мэр Синеозерска!', 'He is the future mayor of Sineozersk!', [(329, 'будущий мэр Синеозерска')], ''),
]
WALK = [
    (0, None, "'What is our candidate like? Simple, hardworking, one of our own!' The third adjective literally means 'one's own' — someone who belongs to us, a local man of the people."),
    (1, None, "'Not in word, but in deed! Everyone chatters, while I work.' Both 'word' and 'deed' are in the 'with/as' form: by word, by deed. Then Arkady sharpens the slogan."),
    (2, None, "'No, better like this: everyone talks, while I do! Excellent.' Outside the building, reporters have already gathered on the pavement, and Samson has to duck past them into the flat. He bursts into the hallway shouting for his daughter."),
    (3, None, "'Yulia, what have you done?' Meanwhile, Yulia isn't sorry at all."),
    (4, None, "'What? Dad is a star now!' Literally 'Dad by us is now a star'."),
    (5, None, "'A star? Why did you post that video on the internet?' The verb at the end literally means 'laid out' and is the standard Russian word for uploading or posting online."),
    (6, None, "'The clip has already got four million views!' Literally 'gathered four million views'. Samson is not happy about his sudden fame."),
    (7, None, "'There are reporters out on the street! They're waiting for me!' Just then, Arkady steps out into the corridor with his arms spread wide like a statesman."),
    (8, None, "'My friends, please don't quarrel.' Putting 'my' after 'friends' gives it a warm, theatrical ring."),
    (9, None, "'In fact, yesterday was a fateful day.' The long adjective comes from the words for 'fate' and 'carry': a day that brings destiny."),
    (10, None, "'Do you think ordinary Vanya Samsonov is standing before you?' After the preposition 'before' or 'in front of', 'you' takes the 'with'-form form."),
    (11, None, "'Who else, then?' Samson looks at him as if he is crazy, and Arkady delivers his grand announcement."),
    (12, None, "'No, my friends! Standing before you is Ivan Vasilyevich Samsonov.' No longer 'Vanya', but full first name, patronymic and surname."),
    (13, None, "'He is the future mayor of Sineozersk!' Here, Samson, Nina and Yulia stare at Arkady in stunned silence."),
]
