# Authoring module for kukhnya-s01e12-scene-09.
ID = 'kukhnya-s01e12-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 9
TITLE = 'Открытая кухня  (The Open Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'Barinov has found out about the glass wall, and he storms across the dining room to find Vika. She stays calm, which only makes him angrier. Listen to the quarrel in Russian before we look inside it.'
OPENER = 'Back through the quarrel, to hear what each of them is really saying.'
TRANSITION = 'Here is the quarrel in one piece.'
OUTRO = "Vika has an answer for everything, and Barinov is left insisting he is a chef and not a fish. Talk soon."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('barinov', 'Вика, что происходит в моем ресторане?', 'Vika, what is happening in my restaurant?', [], ''),
    ('vika', 'Вообще-то этот важный вопрос к тебе!', 'Actually, this important question is for you!', [(76, 'Вообще-то этот вопрос к тебе')], ''),
    ('barinov', 'Зачем вы убрали стену на кухне?', 'Why did you remove the kitchen wall?', [], ''),
    ('vika', 'Гости хотят видеть работу лучших поваров.', 'Guests want to see the work of the best cooks.', [(77, 'гости')], ''),
    ('barinov', 'Это не кухня, а дурацкий цирк!', 'This is not a kitchen, but a foolish circus!', [], ''),
    ('vika', 'Все наши гости любят этот красивый зал.', 'All our guests love this beautiful hall.', [(77, 'гости')], ''),
    ('barinov', 'Они смотрят на меня как на рыбу!', 'They look at me like at a fish!', [], ''),
    ('vika', 'Гости до сих пор в шоке от крика.', 'The guests are still in shock from shouting.', [(77, 'Гости до сих пор в шоке от твоего появления')], ''),
    ('barinov', 'Я великий шеф, а не рыба!', 'I am a great chef, not a fish!', [], ''),
    ('vika', 'Тогда веди себя спокойно перед людьми.', 'Then behave calmly in front of people.', [], ''),
    ('barinov', 'Я не потерплю этот новый цирк!', 'I will not tolerate this new circus!', [(76, 'этот')], ''),
    ('vika', 'Привыкай, это современный и красивый ресторан.', 'Get used to it, this is a modern and beautiful restaurant.', [], ''),
]
WALK = [
    (0, None, ["'Vika, what is happening in my restaurant?' We can analyze the dialogue: ", ('barinov', 'что'), ('barinov', 'происходит'), " is the standard way to say 'what is going on?'. In ", ('barinov', 'в'), ('barinov', 'моем'), ('barinov', 'ресторане'), ", the term for restaurant takes a different ending after 'in'."]),
    (1, None, ["'Actually, this important question is for you!' Let's break down the speech: ", ('vika', 'Вообще'), '-', ('vika', 'то'), " means 'in fact', with an ending that makes it sound pointed. ", ('vika', 'к'), ('vika', 'тебе'), " is 'to you', so she turns the question back to him."]),
    (2, None, ["'Why did you remove the kitchen wall?' The word ", ('barinov', 'вы'), " here is plural for Vika and her team, even though these two usually talk to each other using the informal 'you'. ", ('barinov', 'убрали'), " means 'removed', and ", ('barinov', 'стену'), ' is the wall as the thing being removed.']),
    (3, None, ["'Guests want to see the work of the best cooks.' Now we can break down the words: ", ('vika', 'хотят'), " means 'they want' and goes with ", ('vika', 'видеть'), ", 'to see'. ", ('vika', 'лучших'), " means 'of the best', and ", ('vika', 'поваров'), " is 'of cooks'."]),
    (4, None, ["'This is not a kitchen, but a foolish circus!' We can look at the sentence: ", ('barinov', 'а'), " carries the meaning of 'but' in sentences matching 'not this, but that'. ", ('barinov', 'дурацкий'), ', meaning foolish, comes from the term for a fool.']),
    (5, None, ["'All our guests love this beautiful hall.' The term ", ('vika', 'красивый'), " means 'beautiful' for a room and 'handsome' for a person. ", ('vika', 'Все'), ('vika', 'наши'), ('vika', 'гости'), ' are all plural, and ', ('vika', 'любят'), " means 'they love'."]),
    (6, None, ["'They look at me like at a fish!' Now we can inspect the sentence: ", ('barinov', 'как'), ('barinov', 'на'), ('barinov', 'рыбу'), " translates directly to 'like at a fish', keeping 'at' in front of the fish. Notice for fish changes its ending as the thing being looked at."]),
    (7, None, ["'The guests are still in shock from shouting.' We will inspect the dialogue: ", ('vika', 'до'), ('vika', 'сих'), ('vika', 'пор'), " is how Russians say 'still'. ", ('vika', 'от'), ('vika', 'крика'), " means 'from shouting', where the term for shout takes a new ending after 'from'."]),
    (8, None, ["'I am a great chef, not a fish!' Now let's focus on this part: ", ('barinov', 'великий'), " means 'great' in the sense of 'grand', not just 'big'. ", ('barinov', 'а'), ('barinov', 'не'), " means 'and not'."]),
    (9, None, ["'Then behave calmly in front of people.' To say 'behave', Russians say 'to lead oneself', and ", ('vika', 'веди'), ('vika', 'себя'), ' is the command. After ', ('vika', 'перед'), ", meaning 'in front of', the term for people changes to ", ('vika', 'людьми'), '.']),
    (10, None, ["'I will not tolerate this new circus!' We will focus on this part: ", ('barinov', 'не'), ('barinov', 'потерплю'), " is 'I will not put up with it' in the future. As a masculine object, ", ('barinov', 'цирк'), ' keeps its plain shape along with ', ('barinov', 'этот'), ('barinov', 'новый'), '.']),
    (11, None, ["'Get used to it, this is a modern and beautiful restaurant.' We can focus on the sentence: ", ('vika', 'Привыкай'), " is the command 'get used to it'. Notice for restaurant is masculine, so both describing words take matching endings in ", ('vika', 'современный'), ('vika', 'и'), ('vika', 'красивый'), '.']),
]
