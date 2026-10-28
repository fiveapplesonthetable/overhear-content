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
INTRO = 'Vika catches Max near the bar and sends him back to the kitchen. Then she gathers the waiting staff for an announcement about a new rule. Here is the scene in Russian first.'
OPENER = "Let's go through it slowly, and watch the announcement land."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Nobody in the room is happy about the new rule, and a few people look rather guilty. When you watch the episode, notice who looks away first. Speak soon.'
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
    (0, None, "'Max, what are you doing here?' 'Chto ty delaesh' is 'what you do', and it covers both 'what do you do' and 'what are you doing'. 'Zdes' is 'here'."),
    (1, None, "'I brought fresh oranges to the bar.' 'Prinyos' is 'brought', ending in a bare consonant because Max is a man. 'K baru' is 'to the bar', where 'k' means 'towards' and the bar gets a 'u'."),
    (2, None, "'Then attend to your oranges in the kitchen!' 'Zanimaysya' ends in 'sya', so it's 'busy yourself', and it's followed by 'with your oranges'. 'Svoimi' means 'your own', with a plural 'with' ending."),
    (3, None, "'All right, I am already leaving.' 'Ukhozhu' means 'I am going away'. 'Uzhe' is 'already' and 'obratno' is 'back', so he leaves 'already back'."),
    (4, None, "'So, have all the waitstaff gathered here?' 'Tak' is the 'so' or 'right' that people use before an announcement. 'Sobralis' ends like 'sya' words do, so it's literally 'gathered themselves'."),
    (5, None, "'Yes, everyone is listening to you very attentively.' 'Slushayut' is 'they listen', with no 'they' written. 'Vnimatelno' means 'attentively', and Max says it a little too eagerly."),
    (6, None, "'Starting today we have a strict ban.' 'S segodnyashnego dnya' is literally 'from today's day'. 'U nas' is 'at us', and Russians use it for 'we have'. 'Zapret' is 'ban'."),
    (7, None, "'What sort of ban in our restaurant?' 'Kakoy eshchyo' is 'what, then', with the little 'eshchyo' making it a challenge. 'V nashem restorane' is 'in our restaurant'."),
    (8, None, "'Any personal relationships at work are forbidden.' 'Zapreshchenny' is related to 'zapret', ban, as 'forbidden' is to 'ban'. 'Lyubye' means 'any' and 'otnosheniya' is 'relationships', always in the plural."),
    (9, None, "'But why do we need such a new rule?' 'Zachem nam' is 'what for to us'. 'Takoe' is 'such' and 'pravilo' is 'rule'."),
    (10, None, "'Now the restaurant has very difficult times.' 'U restorana' is 'at the restaurant', so 'the restaurant has'. 'Slozhnoe vremya' is 'difficult time', and 'vremya' is neuter, so 'slozhnoe' ends in 'oe'."),
    (11, None, "'You must think only about work!' Vika isn't speaking to Max alone but to the whole room, so it's the plural 'vy dolzhny'. 'About work' is 'o rabote', and 'work' picks up an 'e' on the end."),
    (12, None, "'And what will happen for breaking the rule?' 'Chto budet' is 'what will be', which Russians use for 'what will happen'. 'Za narushenie' is literally 'for the breaking', the way you'd say 'as the price of'."),
    (13, None, "'For breaking this rule there will be dismissal!' It repeats 'for the breaking', then 'budet', 'will be', and the answer: 'uvolnenie', the word for being fired. It's all one blunt sentence."),
]
