# Authoring module for kukhnya-s01e15-scene-08.
ID = 'kukhnya-s01e15-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 8
TITLE = 'Переезд  (Moving Out)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "Max has moved out of Kostya's flat, and he tells Vika about it. She isn't sure what to make of it. Here is their talk."
OPENER = 'Again, slowly.'
TRANSITION = 'Now their talk, all the way through.'
OUTRO = 'Max is now between flats, and Vika will not do him any favours. Who is more stubborn? Catch you next time.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Ну что? Поговорил с Костей?', 'Well? Did you talk to Kostya?', [(156, 'Ну что? Поговорил с Костей?')], ''),
    ('max', 'Да, он умоляет меня не переезжать.', 'Yes, he begs me not to move.', [], ''),
    ('vika', 'Почему он так сильно этого не хочет?', 'Why does he strongly not want this?', [], ''),
    ('max', 'У него сейчас с деньгами проблема.', 'He has a problem with money now.', [], ''),
    ('vika', 'Но ты все-таки решился и съехал.', 'But you still decided and moved out.', [], ''),
    ('max', 'Да так быстро, что я забыл бумажник.', 'Yes so fast that I forgot the wallet.', [], ''),
    ('vika', 'И где ты живешь?', 'And where do you live?', [], ''),
    ('max', 'Пока нигде.', 'Nowhere for now.', [], ''),
    ('vika', 'То есть лучше нигде, чем со мной?', 'So better nowhere than with me?', [], ''),
    ('max', 'Ну ладно, давай к тебе приеду.', 'Well alright, let me come to you.', [], ''),
    ('vika', 'Нет, мне одолжение делать не надо.', 'No, you do not need to do me a favor.', [], ''),
    ('max', 'То есть ты не приедешь?', 'So you will not come?', [], ''),
    ('vika', 'Ты пойми, важно, чтобы мы хотели.', 'You understand, it is important that we want.', [], ''),
]
WALK = [
    (0, None, ["'Well? Did you talk to Kostya?' The person you talk with takes a special ending in Russian, so the name becomes ", ('vika', 'Костей'), '. Vika sounds brisk.']),
    (1, None, ["'Yes, he begs me not to move.' We can examine the words: ", ('max', 'умоляет'), " is stronger than 'asks', closer to 'pleads'. After ", ('max', 'не'), ', the action is ', ('max', 'переезжать'), ', which is the usual form chosen when asking someone not to do something.']),
    (2, None, ["'Why does he strongly not want this?' After ", ('vika', 'не'), ('vika', 'хочет'), ", the term for 'this' changes to ", ('vika', 'этого'), '. Russian changes the ending of what you do not want in this way.']),
    (3, None, ["'He has a problem with money now.' We can break down the dialogue: ", ('max', 'У'), ('max', 'него'), ", meaning 'at him', stands for 'he has'. Money is only ever plural in Russian."]),
    (4, None, ["'But you still decided and moved out.' We can look at the phrase: ", ('vika', 'решился'), " has an ending meaning 'yourself', so it means you made up your own mind. ", ('vika', 'съехал'), " is 'rode off', Russian for 'moved out'."]),
    (5, None, ["'Yes so fast that I forgot the wallet.' We can inspect this line: ", ('max', 'так'), ('max', 'быстро'), ', ', ('max', 'что'), " is 'so fast that', the pattern for results. ", ('max', 'бумажник'), ' is a wallet, built on the term for paper.']),
    (6, None, ["'And where do you live?' Let us analyze the words: ", ('vika', 'где'), ('vika', 'ты'), ('vika', 'живешь'), " is 'where you live', with no helper word. ", ('vika', 'И'), " at the start means 'and'."]),
    (7, None, ["'Nowhere for now.' You know ", ('max', 'Пока'), " as 'bye', but its first meaning is 'for now', 'for the time being'. ", ('max', 'нигде'), " is 'nowhere', and it needs no extra negative word when it stands alone."]),
    (8, None, ["'So better nowhere than with me?' We can consider the words: ", ('vika', 'То'), ('vika', 'есть'), ", meaning 'that is', opens the line like 'so you mean'. ", ('vika', 'чем'), " is 'than', the link between the two choices."]),
    (9, None, ["'Well alright, let me come to you.' Let's break down the sentence: ", ('max', 'давай'), ' and ', ('max', 'приеду'), " combine as 'let me come', the usual offer. ", ('max', 'к'), ('max', 'тебе'), " is 'to your place'."]),
    (10, None, ["'No, you do not need to do me a favor.' We can examine this part: ", ('vika', 'одолжение'), ('vika', 'делать'), " is 'to do a favour', and Russians often use it the way English uses 'do not do me any favours'. ", ('vika', 'мне'), ' and ', ('vika', 'не'), ('vika', 'надо'), " mean 'to me not needed'."]),
    (11, None, ["'So you will not come?' Let us inspect the dialogue: ", ('max', 'То'), ('max', 'есть'), ' again, summing up. ', ('max', 'не'), ('max', 'приедешь'), " is 'you will not come', and the start of the term is the part that means arriving."]),
    (12, None, ["'You understand, it is important that we want.' Let's consider the words: ", ('vika', 'Ты'), ('vika', 'пойми'), " is a command to understand, with 'you' added for weight, like 'you have to understand'. After ", ('vika', 'важно'), ', ', ('vika', 'чтобы'), ', the action goes into the past form in ', ('vika', 'хотели'), '.']),
]
