# domashniy-arest/s01e03/scene-01.py
ID = "domashniy-arest-s01e03-scene-01"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = "Адвокаты из Москвы  (Lawyers from Moscow)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
VOICES = {"narrator": "sky", "mishkin": "angelina", "anya": "alisa", "judge": "anja"}
LABELS = {"mishkin": "Мишкин", "anya": "Аркадий", "judge": "Илья Олегович"}
INTRO = "Welcome back to House Arrest. We open as three sleek Moscow lawyers led by Andrei Iosifovich Mishkin arrive by train, visit Arkady in the flat, and march into the office of Judge Ilya Olegovich Berg. Let's listen in Russian first."
STORY = [
    ("mishkin", "Аркадий Борисович, мы ваши адвокаты из Москвы.", "Arkady Borisovich, we are your lawyers from Moscow.", [(14, 'Аркадий Борисович, мы из')], "'из адвокатской конторы Мишкин и сыновей' simplified to 'ваши адвокаты из Москвы'"),
    ("anya", "Добрый день, господа! Я очень вас жду. Прошу вас.", "Good afternoon, gentlemen! I've been waiting for you. Come in, please.", [(15, 'Добрый день. Я очень вас жду, господа. Прошу вас')], ""),
    ("anya", "Посмотрите, какие тут условия. В эту комнату, пожалуйста.", "Look what the conditions are like here. Into this room, please.", [(16, 'условия'), (17, 'В эту комнату, пожалуйста')], "'Прошу обратить внимание на условия моего проживания' simplified to 'Посмотрите, какие тут условия'"),
    ("mishkin", "Здравствуйте, Илья Олегович.", "Hello, Ilya Olegovich.", [(21, 'Здравствуйте, Илья Олегович')], "in Judge Berg's office"),
    ("judge", "Простите, а вы кто? Это что?", "Excuse me, who are you? What is this?", [(23, 'Простите, а вы кто'), (26, 'Это что')], ""),
    ("mishkin", "Я адвокат Мишкин, занимаюсь этим делом.", "I am the lawyer Mishkin, I'm handling this case.", [(24, 'Мишкин'), (25, 'делом')], "adapted from the assistant's third-person introduction in cues 24-25"),
    ("mishkin", "Вот бумага из прокуратуры. Слушание будет сегодня вечером.", "Here is an order from the prosecutor's office. The hearing will be this evening.", [(28, 'в прокуратуре'), (29, 'слушания')], "cues 28-29 ('выбил в прокуратуре постановление о назначении срочного судебного слушания') simplified to A1"),
    ("judge", "Как это сегодня вечером? Это невозможно!", "What do you mean, this evening? That's impossible!", [(30, 'Как это сегодня вечером'), (31, 'Это невозможно')], ""),
    ("judge", "Мы уже приняли решение по этому делу. Пересмотр только через два месяца.", "We have already made a decision on this case. A review is only in two months.", [(32, 'Мы уже приняли решение'), (33, 'по этому делу'), (34, 'Пересмотр'), (35, 'только через два месяца')], ""),
    ("mishkin", "А прокуратура думает иначе. В деле много грубых ошибок.", "The prosecutor's office thinks otherwise. There are many serious mistakes in the case.", [(36, 'А прокуратура'), (37, 'думает иначе'), (39, 'В деле много грубых')], "'процессуальных нарушений' -> 'ошибок'"),
    ("mishkin", "Мы требуем заменить домашний арест. Нужна подписка о невыезде.", "We demand that house arrest be replaced. What's needed is a travel ban.", [(43, 'Мы требуем заменить домашний арест'), (44, 'подписку о невыезде')], "split into two short sentences; 'На подписку' -> 'Нужна подписка'"),
    ("anya", "Вы думаете, это реально?", "Do you think that's really possible?", [(47, 'Вы думаете, это реально')], "back at the communal flat"),
    ("mishkin", "Нет причин держать вас под арестом. Сегодня вы выйдете отсюда.", "There is no reason to keep you under arrest. Today you will walk out of here.", [(52, 'причин держать'), (52, 'под арестом'), (53, 'Сегодня вы выйдете отсюда')], "'его' -> 'вас'"),
    ("mishkin", "А потом, Аркадий Борисович, мы закроем ваше дело.", "And then, Arkady Borisovich, we will close your case.", [(54, 'А потом, Аркадий Борисович, мы'), (54, 'ваше дело')], "'развалим ваше дело до суда' -> 'закроем ваше дело'"),
    ("anya", "Ангелы мои, это вам! Советская привычка.", "My angels, this is for you! An old Soviet habit.", [(57, 'Ангелы мои'), (57, 'это вам'), (58, 'Советская привычка')], "'спасители мои' dropped"),
    ("mishkin", "До свидания, Аркадий Борисович.", "Goodbye, Arkady Borisovich.", [(59, 'До свидания')], "'Аркадий Борисович' added"),
]
OPENER = "Let's go back through the scene step by step. First, the Moscow lawyers arrive at the communal flat and introduce themselves to Arkady."
WALK = [
    (0, None, "'Arkady Borisovich, we are your lawyers from Moscow.' Russian drops the word for 'are' in the present tense, and after the preposition 'from' the city name Moscow changes its ending. Arkady is delighted to see them."),
    (1, 'Добрый день, господа!', "'Good afternoon, gentlemen!' Literally 'good day', followed by the old-fashioned polite word for 'gentlemen'."),
    (1, 'Я очень вас жду. Прошу вас.', "'I've been waiting for you. Come in, please.' Literally 'I very much wait for you', using the present tense because he is still waiting as they walk in. The last two words mean 'I ask you', the polite way to invite someone inside. He shows them the flat."),
    (2, None, "'Look what the conditions are like here. Into this room, please.' 'Into this room' uses the direct-object form because he is pointing them where to go. Next, the lawyer Mishkin marches straight into the office of the city court chairman, Judge Ilya Olegovich Berg."),
    (3, None, "'Hello, Ilya Olegovich.' The formal greeting, with first name and father's name. The judge has no idea who just walked past his secretary."),
    (4, None, "'Excuse me, who are you? What is this?' Literally 'forgive me, and you who?'. Mishkin introduces himself and lays a paper on the desk."),
    (5, None, "'I am the lawyer Mishkin, I'm handling this case.' The verb 'to handle' or 'to be occupied with' takes the 'with/as' form after it: 'with this case'."),
    (6, None, "'Here is an order from the prosecutor's office. The hearing will be this evening.' Literally 'today in the evening'. Judge Berg cannot believe his ears."),
    (7, None, "'What do you mean, this evening? That's impossible!' Literally 'how is this, today in the evening?'. And he explains the normal rule."),
    (8, None, "'We have already made a decision on this case. A review is only in two months.' The preposition before 'two months' literally means 'through' or 'across', and with time it means 'in' or 'after'. Mishkin does not care."),
    (9, None, "'The prosecutor's office thinks otherwise. There are many serious mistakes in the case.' Literally 'coarse mistakes'. After the word for 'many', the noun and adjective take the plural 'of' form."),
    (10, 'Мы требуем заменить домашний арест.', "'We demand that house arrest be replaced.' Literally 'we demand to replace house arrest'."),
    (10, 'Нужна подписка о невыезде.', "'What's needed is a travel ban.' The first word means 'needed', with a feminine ending to match the feminine noun for a written undertaking not to leave town. Back at the flat, Arkady asks if it can really work."),
    (11, None, "'Do you think that's really possible?' Mishkin is completely confident."),
    (12, None, "'There is no reason to keep you under arrest. Today you will walk out of here.' Literally 'you will go out from here', a future-tense form for a single result."),
    (13, None, "'And then, Arkady Borisovich, we will close your case.' Another future-tense form: 'we will close'. Arkady is so grateful that he hands them a little gift."),
    (14, 'Ангелы мои, это вам!', "'My angels, this is for you!' Putting 'my' after the noun makes it sound warm and theatrical. And he excuses the little sweetener."),
    (14, 'Советская привычка.', "'An old Soviet habit.' Meaning the habit of never letting an important person leave empty-handed."),
    (15, None, "'Goodbye, Arkady Borisovich.' The lawyers take their leave, and Arkady is sure he will be free by nightfall."),
]
TRANSITION = "Now let's listen to the whole scene again from the beginning."
OUTRO = "So the expensive Moscow lawyers have promised to get Arkady out of house arrest this very evening. See you next time!"
CLOSING = ("anya", "До свидания!")
