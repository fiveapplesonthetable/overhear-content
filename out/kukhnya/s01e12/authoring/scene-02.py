# Authoring module for kukhnya-s01e12-scene-02.
ID = 'kukhnya-s01e12-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 2
TITLE = 'Фальшивая боль  (Fake Pain)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = "In the restaurant corridor, Max suddenly grabs his right side and groans in pain. When a concerned Victoria rushes over to help him, he miraculously recovers and reveals his true intentions. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine this tricky conversation in the corridor line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Furious at being tricked into worrying about his health, Victoria storms off, leaving Max standing alone with his cinema tickets. Next time you watch the episode, listen for the Russian expressions for 'ticket' and 'hurts' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Ай! Как мне больно в животе!', 'Ouch! How it hurts me in the stomach!', [(8, 'Блин, что это?'), (12, 'Ой, что это?')], ''),
    ('vika', 'Макс, что такое? Тебе очень больно?', 'Max, what is it? Does it hurt you a lot?', [(9, 'Что такое? Больно так?')], ''),
    ('max', 'Я не знаю, что это такое.', 'I do not know what this is.', [(10, 'Не знаю, что это.')], ''),
    ('vika', 'Ой, с правой стороны это очень плохо!', 'Oh, on the right side this is very bad!', [(11, 'Боже мой.')], ''),
    ('max', 'Боже мой, как мне сейчас больно.', 'My god, how much it hurts me now.', [], ''),
    ('vika', 'Давай я быстро вызову тебе врача.', 'Let me quickly call a doctor for you.', [], ''),
    ('max', 'Нет, серьёзно, не надо вызывать врачей.', 'No, seriously, do not call doctors.', [(10, 'Нет, всё нормально, всё нормально.')], ''),
    ('vika', 'Почему? Тебе же нужна срочная помощь.', 'Why? You need urgent help after all.', [], ''),
    ('max', 'Смотри, вот два билета в кино.', 'Look, here are two tickets to the cinema.', [(13, 'Билетики. Пойдем в кино, а?')], ''),
    ('vika', 'Ну ты и придурок, честное слово!', 'Well you are a jerk, honestly!', [(14, 'Дебил.')], ''),
    ('max', 'Пойдём в кино сегодня вечером, а?', 'Shall we go to the cinema tonight, eh?', [(13, 'Пойдем в кино, а?')], ''),
    ('vika', 'Ты настоящий идиот, я никуда не пойду!', 'You are a real idiot, I will not go anywhere!', [(14, 'Дебил.')], ''),
    ('max', 'Ладно, тогда я пойду в кино один.', 'Alright, then I will go to the cinema alone.', [], ''),
]
WALK = [
    (0, None, "'Ouch! How it hurts me in the stomach!' Russian omits the present-tense verb 'to be' here, linking 'ouch' directly with 'how', pairing it with 'hurts' and 'stomach'."),
    (1, None, "'Max, what is it? Does it hurt you a lot?' Russian omits the present-tense verb 'to be' here, linking 'a lot' directly with 'hurts' to make the point directly in conversation."),
    (2, None, "'I do not know what this is.' Max delivers a punchy conversational reaction built around the Russian word meaning 'know'."),
    (3, None, "'Oh, on the right side this is very bad!' Russian omits the present-tense verb 'to be' here, linking 'oh' directly with 'right', pairing it with 'side' and 'very'."),
    (4, None, "'My god, how much it hurts me now.' Russian omits the present-tense verb 'to be' here, linking 'God' directly with 'how', pairing it with 'now' and 'hurts'."),
    (5, None, "'Let me quickly call a doctor for you.' Here Vika anchors the line on the word meaning 'quickly' and builds the thought around 'will call' and 'doctor'."),
    (6, None, "'No, seriously, do not call doctors.' The phrasing opens with 'seriously' before bringing in 'must' and 'to call' to make the point clear."),
    (7, None, "'Why? You need urgent help after all.' Russian omits the present-tense verb 'to be' here, linking 'why' directly with 'needed', pairing it with 'urgent' and 'help'."),
    (8, None, "'Look, here are two tickets to the cinema.' Max leads with the direct command form meaning 'look', pairing it with 'two' and 'tickets'."),
    (9, None, "'Well you are a jerk, honestly!' Russian omits the present-tense verb 'to be' here, linking 'jerk' directly with 'honest', followed by 'word'."),
    (10, None, "'Shall we go to the cinema tonight, eh?' Max turns a statement into a question purely through rising intonation on the word meaning 'shall we go', pairing it with 'cinema' and 'today'."),
    (11, None, "'You are a real idiot, I will not go anywhere!' Vika expresses this naturally by combining the word for 'real' with 'idiot' and 'nowhere'."),
    (12, None, "'Alright, then I will go to the cinema alone.' Max puts the word for 'alright' together with 'then' and 'will go' in a crisp, natural spoken turn of phrase."),
]
