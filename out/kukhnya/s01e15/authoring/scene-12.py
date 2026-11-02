# Authoring module for kukhnya-s01e15-scene-12.
ID = 'kukhnya-s01e15-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 12
TITLE = 'Выселение шефа  (Evicting the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = 'Lyova is standing outside the bathroom, and he has had enough of his flatmate. He tells Barinov through the door that he must leave. Listen in Russian first.'
OPENER = "Slowly now, line by line."
TRANSITION = 'And the scene again, uninterrupted.'
OUTRO = "Barinov starts packing, and Lyova waits to hear the door. Does Barinov really leave? We'll find out."
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('lyova', 'Открывай, нам надо поговорить.', 'Open up, we need to talk.', [(288, 'Открывай, поговорить надо.')], ''),
    ('barinov', 'Лёва, что ты хочешь?', 'Leva, what do you want?', [(289, 'Лёва, что ты хочешь, Лёва?')], ''),
    ('lyova', 'Я хочу сказать тебе одну вещь.', 'I want to tell you one thing.', [(291, 'Я хочу сказать.')], ''),
    ('lyova', 'Чтобы ноги твоей больше не было в моём доме.', 'So that your foot is no longer in my house.', [(292, 'Чего? Чтобы ноги вашей больше в моем доме не было.')], ''),
    ('lyova', 'Сегодня же собирай вещи и уезжай.', 'Today pack your things and leave.', [(293, 'Сегодня же собираете вещи и уезжаете.')], ''),
    ('lyova', 'Больше ты у нас с мамой не живёшь.', 'You no longer live with me and Mom.', [(294, 'Больше вы у нас с мамой не живете.')], ''),
    ('lyova', 'Тебе это ясно?', 'Is that clear to you?', [(295, 'Ясно?')], ''),
    ('barinov', 'Да пожалуйста.', 'Yes, sure.', [(295, 'Да пожалуйста.')], ''),
    ('barinov', 'Очень мне надо.', 'As if I need it.', [(296, 'Больно надо.')], ''),
    ('lyova', 'Я жду, пока ты уйдёшь.', 'I am waiting until you leave.', [], ''),
    ('barinov', 'Я уже ухожу.', 'I am already leaving.', [], ''),
    ('lyova', 'Ключи оставь на столе.', 'Leave the keys on the table.', [], ''),
]
WALK = [
    (0, None, ["'Open up, we need to talk.' The term ", ('lyova', 'Открывай'), " is the order to open, in a form that sounds like 'come on, open up'. The expression ", ('lyova', 'нам'), ('lyova', 'надо'), " means 'we need'."]),
    (1, None, ["'Leva, what do you want?' The term ", ('barinov', 'хочешь'), " means 'you want', adding the ending that goes with addressing someone informally. The two of them are speaking casually here."]),
    (2, None, ["'I want to tell you one thing.' Notice for 'one thing' becomes ", ('lyova', 'одну'), ('lyova', 'вещь'), ' because it is the thing being told. The noun also refers to a physical object.']),
    (3, None, ["'So that your foot is no longer in my house.' This is an idiom. Here we have ", ('lyova', 'Чтобы'), ('lyova', 'ноги'), ('lyova', 'твоей'), ' combined with ', ('lyova', 'не'), ('lyova', 'было'), " roughly means 'never set foot'."]),
    (4, None, ["'Today pack your things and leave.' We can consider the phrase: ", ('lyova', 'Сегодня'), ('lyova', 'же'), " means 'today, right now', with the second word stressing the immediacy. The verbs ", ('lyova', 'собирай'), ' and ', ('lyova', 'уезжай'), " are two orders joined by 'and'."]),
    (5, None, ["'You no longer live with me and Mom.' The phrasing ", ('lyova', 'у'), ('lyova', 'нас'), ('lyova', 'с'), ('lyova', 'мамой'), " is how you say 'with me and Mom'. Here we have ", ('lyova', 'не'), ('lyova', 'живёшь'), " means 'you do not live'."]),
    (6, None, ["'Is that clear to you?' We can inspect this line: ", ('lyova', 'Тебе'), ('lyova', 'это'), ('lyova', 'ясно'), " means 'to you this clear', with no verb at all. It is a classic schoolteacher's question."]),
    (7, None, ["'Yes, sure.' We will break down the phrase: ", ('barinov', 'Да'), ('barinov', 'пожалуйста'), " sounds polite, but here it means 'fine, be my guest'. The tone makes all the difference."]),
    (8, None, ["'As if I need it.' The expression ", ('barinov', 'Очень'), ('barinov', 'мне'), ('barinov', 'надо'), " translates as 'very much needed to me', which in the right voice means the opposite: 'as if I cared'. Sarcasm is built in."]),
    (9, None, ["'I am waiting until you leave.' We will break down the dialogue: ", ('lyova', 'пока'), " can mean both 'while' and 'until', and here it points to the future."]),
    (10, None, ["'I am already leaving.' The present tense verb ", ('barinov', 'ухожу'), " describes something happening right now: 'I am on my way out'."]),
    (11, None, ["'Leave the keys on the table.' We can focus on the words: ", ('lyova', 'Ключи'), " is the plural of 'key'. The verb ", ('lyova', 'оставь'), " is the command 'leave', and ", ('lyova', 'на'), ('lyova', 'столе'), " means 'on the table'."]),
]
