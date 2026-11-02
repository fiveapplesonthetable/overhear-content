# Authoring module for kukhnya-s01e12-scene-11.
ID = 'kukhnya-s01e12-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 11
TITLE = 'Запрет на отношения  (Ban on Relationships)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'Vika catches Max near the bar and sends him back to the kitchen. Then she gathers the waiting staff for an announcement about a new rule. First the Russian.'
OPENER = 'Slowly, and watch the announcement land.'
TRANSITION = 'Now the whole announcement again.'
OUTRO = "Nobody in the room likes the new rule. When you watch, listen for 'for breaking' in Vika's last line. Speak soon."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Макс, что ты здесь делаешь?', 'Max, what are you doing here?', [(89, 'А ты что здесь делаешь?')], ''),
    ('max', 'Я принёс свежие апельсины к бару.', 'I brought fresh oranges to the bar.', [(90, 'Я апельсины к бару принес.')], ''),
    ('vika', 'Вот и занимайся своими апельсинами на кухне!', 'Then attend to your oranges in the kitchen!', [(91, 'Вот и занимайся апельсинами.')], ''),
    ('max', 'Хорошо, я уже ухожу обратно.', 'All right, I am already leaving.', [], ''),
    ('vika', 'Так, все официанты собрались здесь?', 'So, have all the waitstaff gathered here?', [(92, 'Так, все тут? Да.')], ''),
    ('max', 'Да, все слушают тебя очень внимательно.', 'Yes, everyone is listening to you very attentively.', [], ''),
    ('vika', 'С сегодняшнего дня у нас строгий запрет.', 'Starting today we have a strict ban.', [(93, 'С сегодняшнего дня у нас вводится запрет')], ''),
    ('max', 'Какой ещё запрет в нашем ресторане?', 'What sort of ban in our restaurant?', [], ''),
    ('vika', 'Запрещены любые личные отношения на работе.', 'Any personal relationships at work are forbidden.', [(93, 'запрет на личные отношения на'), (94, 'работе.')], ''),
    ('max', 'Но зачем нам такое новое правило?', 'But why do we need such a new rule?', [], ''),
    ('vika', 'Сейчас у ресторана очень сложное время.', 'Now the restaurant has very difficult times.', [(95, 'У нас сложный период.')], ''),
    ('vika', 'Вы должны думать только о работе!', 'You must think only about work!', [(96, 'вы думали о работе, а не о посторонних вещах.')], ''),
    ('max', 'А что будет за нарушение правила?', 'And what will happen for breaking the rule?', [(98, 'За нарушение этого правила увольнение.')], ''),
    ('vika', 'За нарушение этого правила будет увольнение!', 'For breaking this rule there will be dismissal!', [(98, 'За нарушение этого правила увольнение.')], ''),
]
WALK = [
    (0, None, ["'Max, what are you doing here?' We can focus on this line: ", ('vika', 'что'), ('vika', 'ты'), ('vika', 'здесь'), ('vika', 'делаешь'), " covers both 'what do you do here' and 'what are you doing here'."]),
    (1, None, ["'I brought fresh oranges to the bar.' The verb ", ('max', 'принёс'), ' ends in a bare consonant because Max is a man. Notice ', ('max', 'к'), ('max', 'бару'), ", where the first word means 'towards' and the bar gets a 'u' at the end."]),
    (2, None, ["'Then attend to your oranges in the kitchen!' The term ", ('vika', 'занимайся'), " means 'busy yourself', and it's followed by ", ('vika', 'своими'), ('vika', 'апельсинами'), " for 'with your own oranges'."]),
    (3, None, ["'All right, I am already leaving.' Let's examine the dialogue: ", ('max', 'ухожу'), " for 'I am leaving', an action already under way, and ", ('max', 'обратно'), " for 'back'."]),
    (4, None, ["'So, have all the waitstaff gathered here?' People use ", ('vika', 'Так'), " as the 'so' or 'right' before an announcement. Notice how ", ('vika', 'собрались'), " has the sense of 'gathered themselves'."]),
    (5, None, ["'Yes, everyone is listening to you very attentively.' Let's inspect the sentence: ", ('max', 'слушают'), " for 'they listen', with no 'they' written. And ", ('max', 'внимательно'), " relates to 'attention'."]),
    (6, None, ["'Starting today we have a strict ban.' Let us break down the words: ", ('vika', 'С'), ('vika', 'сегодняшнего'), ('vika', 'дня'), " translates as 'from today's day'. Russians use ", ('vika', 'у'), ('vika', 'нас'), ", or 'at us', to say 'we have'. Notice ", ('vika', 'запрет'), " for 'ban'."]),
    (7, None, ["'What sort of ban in our restaurant?' On its own, ", ('max', 'ещё'), " can mean 'more' or 'still', but after ", ('max', 'Какой'), " it turns indignant, like 'what ban now?'. In ", ('max', 'в'), ('max', 'нашем'), ('max', 'ресторане'), ' both words change to reflect being inside.']),
    (8, None, ["'Any personal relationships at work are forbidden.' Observe how ", ('vika', 'Запрещены'), " relates to the previous 'ban', just as 'forbidden' relates to 'ban' in English. We have ", ('vika', 'любые'), " for 'any' and ", ('vika', 'личные'), ('vika', 'отношения'), " for 'personal relationships', which is normally plural in this sense."]),
    (9, None, ["'But why do we need such a new rule?' We see ", ('max', 'зачем'), ('max', 'нам'), " for 'what for to us'. Because the rule is neuter, both 'such' and 'new' get matching endings in ", ('max', 'такое'), ('max', 'новое'), ('max', 'правило'), '.']),
    (10, None, ["'Now the restaurant has very difficult times.' Now let's break down this part: ", ('vika', 'у'), ('vika', 'ресторана'), " for 'at the restaurant', giving us 'the restaurant has'. We see ", ('vika', 'сложное'), ('vika', 'время'), " for 'difficult time', with matching neuter endings."]),
    (11, None, ["'You must think only about work!' Vika isn't speaking to Max alone but to the whole room, so she uses the plural ", ('vika', 'Вы'), ('vika', 'должны'), '. We see ', ('vika', 'о'), ('vika', 'работе'), " for 'about work', where 'work' picks up an extra letter on the end."]),
    (12, None, ["'And what will happen for breaking the rule?' We will analyze the dialogue: ", ('max', 'что'), ('max', 'будет'), " for 'what will be', used to say 'what will happen'. We see ", ('max', 'за'), ('max', 'нарушение'), " for 'for breaking', the way you might say 'as the price of'."]),
    (13, None, ["'For breaking this rule there will be dismissal!' It repeats 'for breaking', then adds ", ('vika', 'будет'), " for 'will be', and the answer is ", ('vika', 'увольнение'), " for being fired. It's all one blunt sentence."]),
]
