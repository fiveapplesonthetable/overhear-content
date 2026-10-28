# Authoring module for kukhnya-s01e14-scene-01.
ID = 'kukhnya-s01e14-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 1
TITLE = 'Утренние игры  (Morning Games)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "Max wakes up in Vika's apartment and tries to be playful, but Vika is focused on her day. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around Morning Games line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max heads to the shower while Vika prepares for her busy day at the restaurant. Next time you watch the episode, listen for the Russian expressions for 'wake up' and 'today' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Вика, ты уже проснулась сегодня?', 'Vika, are you awake already today?', [], ''),
    ('vika', 'Да, я уже давно не сплю.', 'Yes, I have not been sleeping for a long time.', [], ''),
    ('max', 'Почему ты так рано встала?', 'Why did you get up so early?', [], ''),
    ('vika', 'У меня сегодня очень много дел.', 'I have a lot of things today.', [], ''),
    ('max', 'А как же наш вкусный завтрак?', 'And what about our tasty breakfast?', [], ''),
    ('vika', 'Ты можешь приготовить его сам.', 'You can prepare it yourself.', [], ''),
    ('max', 'И Макс, я озабоченный человек-паук.', 'And Max, I am a horny Spider-Man.', [(1, 'И Макс, я озабоченный человек-паук.')], ''),
    ('vika', 'Очень смешно, но мне надо идти.', 'Very funny, but I need to go.', [], ''),
    ('max', 'Сейчас я тебя. Какой я тебя?', 'I will get you now. What am I getting you?', [(2, 'Сейчас я тебя. Какой я тебя?')], ''),
    ('vika', 'Макс, прекрати это немедленно!', 'Max, stop this immediately!', [], ''),
    ('max', 'Хорошо, я иду варить нам кофе.', 'Alright, I am going to brew coffee for us.', [], ''),
    ('vika', 'Пока ты не сходишь в душ.', 'Before you go take a shower.', [(3, 'Пока ты не сходишь в душ.')], ''),
]
WALK = [
    (0, None, "'Vika, are you awake already today?' Max turns a statement into a question purely through rising intonation on the word meaning 'already', pairing it with 'wake up' and 'today'."),
    (1, None, "'Yes, I have not been sleeping for a long time.' Here Vika anchors the line on the word meaning 'already' and builds the thought around 'for a long time' and 'sleep'."),
    (2, None, "'Why did you get up so early?' The phrasing opens with 'why' before bringing in 'early' and 'get up!' to make the point clear."),
    (3, None, "'I have a lot of things today.' Vika uses the classic Russian possession phrasing — literally 'at me' rather than a verb meaning 'to have', pairing it with 'today' and 'very much'."),
    (4, None, "'And what about our tasty breakfast?' Russian omits the present-tense verb 'to be' here, linking 'how' directly with 'delicious', combining 'how' with 'delicious' and 'breakfast'."),
    (5, None, "'You can prepare it yourself.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (6, None, "'And Max, I am a horny Spider-Man.' Max delivers a punchy conversational reaction built around the Russian word meaning 'preoccupied'."),
    (7, None, "'Very funny, but I need to go.' Vika expresses this naturally by combining the word for 'very much' with 'ridiculous' and 'it is necessary'."),
    (8, None, "'I will get you now. What am I getting you?' Max delivers a punchy one-word reaction built around the Russian word meaning 'now'."),
    (9, None, "'Max, stop this immediately!' Vika leads with the direct command form meaning 'stop it', followed by 'immediately'."),
    (10, None, "'Alright, I am going to brew coffee for us.' The phrasing opens with 'good' before bringing in 'going' and 'to boil' to make the point clear."),
    (11, None, "'Before you go take a shower.' Vika expresses this naturally by combining the word for 'bye' with 'to go' and 'shower'."),
]
