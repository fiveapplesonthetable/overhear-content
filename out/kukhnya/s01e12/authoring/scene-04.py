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
INTRO = 'After Vika, Max tries the same trick on someone else. He finds Sasha, a waitress, by the service station and suddenly groans in pain. First, the Russian.'
OPENER = "This one is mostly about how Sasha reacts, so let's follow her."
TRANSITION = 'And the whole scene again, with no stops.'
OUTRO = "Sasha calls him an actor, but Max finally gets a yes. Sasha's 'what happened to you' is a question worth keeping in your pocket for real emergencies."
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
    (0, None, ["'Sasha, hi! How are things?' Observe how ", ('max', 'привет'), ' gives the casual hi, for friends only. We hear ', ('max', 'Как'), ('max', 'дела'), " means 'how deeds', and it's what Russians say instead of 'how are you'."]),
    (1, None, ["'Hi, little cook! Everything is normal.' Sasha's nickname, ", ('sasha', 'поварёнок'), ", is the word for 'cook' plus an ending that means 'young one'. Baby animals get the same ending."]),
    (2, None, ["'Oh, ow! How painful!' The sound ", ('max', 'ай'), " is the Russian 'ow', while 'oh' is just 'oh'. The expression ", ('max', 'Как'), ('max', 'больно'), " has no 'is' in it, as you'd expect by now."]),
    (3, None, ["'What happened to you?' The term for 'happened' uses an ending because 'what' counts as neuter in Russian. Notice how ", ('sasha', 'Что'), ('sasha', 'с'), ('sasha', 'тобой'), " is 'what with you', the standard way to ask what's wrong."]),
    (4, None, ["'I have a sharp pain in my side.' Russian says 'at me strongly stabs in the side'. Notice how ", ('max', 'У'), ('max', 'меня'), ", meaning 'at me', is how you say 'I have'. 'In the side' is ", ('max', 'в'), ('max', 'боку'), ", taking an unusual stressed 'u' sound."]),
    (5, None, ["'On which side exactly?' The first part means 'from what side'. Notice how ", ('sasha', 'именно'), " means 'exactly'; it's a useful word for asking someone to be specific."]),
    (6, None, ["'Right here, on the right side.' We will focus on the words: ", ('max', 'Вот'), ' points, so ', ('max', 'Вот'), ('max', 'здесь'), " is almost the spoken version of jabbing a finger. It echoes the 'from the right side' Vika used."]),
    (7, None, ["'On the right? That could be appendicitis!' Let us consider the words: ", ('sasha', 'может'), ('sasha', 'быть'), " means 'can be', while it's also how Russians say 'maybe'. The word for appendicitis is nearly the English one, wearing a Russian ending."]),
    (8, None, ["'Shall I urgently call an ambulance?' The word for ambulance is really 'quick', short for 'quick help'. It's feminine, so ", ('sasha', 'скорую'), ' takes that ending when it is the thing being called.']),
    (9, None, ["'No, no need for any ambulance!' Two negatives sit together again: ", ('max', 'никакой'), ", 'no kind of', and 'not'. Notice how ", ('max', 'не'), ('max', 'надо'), " is 'not necessary', daily Russian for 'no need'."]),
    (10, None, ["'Look, I have two tickets!' He uses 'at me' again: this time he has tickets, not a pain. After 'two', notice how ", ('max', 'билета'), " takes an 'a' ending."]),
    (11, None, ["'What? You are just a jerk, Max!' Let's inspect this part: ", ('sasha', 'просто'), " means 'simply' or 'just'. Notice how ", ('sasha', 'придурок'), " keeps that same everyday insult Vika used, roughly 'jerk'."]),
    (12, None, ["'Will you go to the movies with me tonight?' The 'you' form of 'go' does the job of 'will you go', with no helper word. Notice how ", ('max', 'вечером'), " takes the 'om' ending, which is what makes it 'in the evening'."]),
    (13, None, ["'All right, let's go! See you tonight, actor.' Pay attention to how ", ('sasha', 'До'), ('sasha', 'вечера'), " is 'until evening', common speech for 'see you later today'. The last word is 'actor', and Sasha is teasing him about the performance."]),
]
