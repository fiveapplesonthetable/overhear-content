# Authoring module for kukhnya-s01e12-scene-04.
ID = 'kukhnya-s01e12-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 4
TITLE = 'Приступ аппендицита  (An Appendicitis Attack)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = "In the dining room near the waiter station, Max stages an elaborate medical emergency to get waitress Sasha's attention. Pretending to suffer from acute appendicitis, he draws her close before surprising her with cinema tickets. Let's listen to their playful encounter in Russian."
OPENER = "Let's examine the dialogue sentence by sentence. Notice the symptoms of distress, medical emergency phrasing, and casual conversational invitations."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Sasha heads off to her tables with a laugh while Max celebrates the success of his clever theatrical ploy. Great work practicing conversational Russian! Next time you watch the episode, listen for the Russian expressions for 'appendicitis' and 'performer' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Саша, привет! Как дела?', 'Sasha, hi! How are things?', [(27, 'Саш, привет.')], ''),
    ('sasha', 'Привет, поварёнок! Всё нормально.', 'Hi, little cook! Everything is normal.', [(27, 'О, привет, Ваваренок.')], ''),
    ('max', 'Ой, ай! Как больно!', 'Oh, ow! How painful!', [(28, 'Ай!')], ''),
    ('sasha', 'Что с тобой случилось?', 'What happened to you?', [(29, 'Чего такое?')], ''),
    ('max', 'У меня сильно колет в боку.', 'I have a sharp pain in my side.', [(30, 'Чего-то букует.')], ''),
    ('sasha', 'С какой именно стороны?', 'On which side exactly?', [(31, 'С какой стороны?')], ''),
    ('max', 'Вот здесь, с правой стороны.', 'Right here, on the right side.', [(31, 'Да с правой.')], ''),
    ('sasha', 'С правой? Это может быть аппендицит!', 'On the right? That could be appendicitis!', [(32, 'Слушай, с правой это аппендицит.')], ''),
    ('sasha', 'Давай я срочно вызову скорую?', 'Shall I urgently call an ambulance?', [(33, 'А давай скорую вызову?')], ''),
    ('max', 'Нет, не надо никакой скорой!', 'No, no need for any ambulance!', [(33, 'Да не надо.')], ''),
    ('max', 'Смотри, у меня два билета!', 'Look, I have two tickets!', [(34, 'О, билетики.')], ''),
    ('sasha', 'Что? Ты просто придурок, Макс!', 'What? You are just a jerk, Max!', [(36, 'Ну ты придурок.')], ''),
    ('max', 'Пойдёшь со мной вечером в кино?', 'Will you go to the movies with me tonight?', [(35, 'Пойдешь')], ''),
    ('sasha', 'Ладно, пойдём! До вечера, артист.', "All right, let's go! See you tonight, actor.", [], ''),
]
WALK = [
    (0, None, "'Sasha, hi! How are things?' Max greets Sasha and asks how she is doing."),
    (1, None, "'Hi, little cook! Everything is normal.' Sasha says hello back. She calls him a little cook in a friendly way."),
    (2, None, "'Oh, ow! How painful!' Max fakes stomach pain again. He cries out in fake agony."),
    (3, None, "'What happened to you?' Sasha asks what is wrong with him."),
    (4, None, "'I have a sharp pain in my side.' Max complains about a sharp stabbing pain in his side."),
    (5, None, "'On which side exactly?' Sasha wants to know exactly which side hurts."),
    (6, None, "'Right here, on the right side.' Max points out that the pain is on his right side."),
    (7, None, "'On the right? That could be appendicitis!' Sasha gets worried because right side pain could mean appendicitis."),
    (8, None, "'Shall I urgently call an ambulance?' Sasha offers to call for medical help right away. The word for ambulance literally means fast."),
    (9, None, "'No, no need for any ambulance!' Max quickly stops her from calling anyone."),
    (10, None, "'Look, I have two tickets!' Max reveals his trick and shows her the movie tickets instead."),
    (11, None, "'What? You are just a jerk, Max!' Sasha is shocked and calls him a jerk for the stupid joke."),
    (12, None, "'Will you go to the movies with me tonight?' Max asks her if she will join him for a movie later."),
    (13, None, "'All right, let's go! See you tonight, actor.' Sasha agrees to go. She calls him an actor because of his fake pain."),
]
