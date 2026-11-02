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
INTRO = 'Max has just made up his mind to go after Vika, and his first idea is a bad one. He meets her in the corridor and suddenly clutches his side and groans. The Russian comes first.'
OPENER = "Let's slow down and watch the trick come apart."
TRANSITION = 'Here it all is again, at a quicker pace.'
OUTRO = "Vika is not amused, and Max is left holding two tickets and no one to use them with. Keep an ear out for 'to me painful', because Russian pain always happens to you."
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
    (0, None, ["'Ouch! How it hurts me in the stomach!' Russian doesn't say 'I am in pain'. Notice how 'to me painful' uses ", ('max', 'мне'), " for 'to me'. 'In the stomach' is ", ('max', 'в'), ('max', 'животе'), ", picking up an 'e' sound after 'in' when it means where."]),
    (1, None, ["'Max, what is it? Does it hurt you a lot?' The first question, ", ('vika', 'что'), ('vika', 'такое'), ", is a handy idiom for 'what's the matter?'. The second uses 'to you painful', the same pattern as 'to me painful', with ", ('vika', 'Тебе'), " for 'you'."]),
    (2, None, ["'I do not know what this is.' Notice how ", ('max', 'Я'), ('max', 'не'), ('max', 'знаю'), " means 'I not know', with the 'not' word just going in front of the verb. We hear ", ('max', 'что'), ('max', 'это'), ('max', 'такое'), " is a fuller version of Vika's question."]),
    (3, None, ["'Oh, on the right side this is very bad!' Pay attention to how Russian says 'from the right side', ", ('vika', 'с'), ('vika', 'правой'), ('vika', 'стороны'), ", where English says 'on'. Vika knows that a pain on the right can mean the appendix."]),
    (4, None, ["'My god, how much it hurts me now.' Pay attention to how ", ('max', 'Боже'), " is a special shape of 'God', used only when you call out to him. Notice ", ('max', 'сейчас'), " means 'now', and it is also what people say for 'in a moment'."]),
    (5, None, ["'Let me quickly call a doctor for you.' It starts with ", ('vika', 'Давай'), ", meaning 'give', which is how Russians say 'let me' or 'let's'. 'Call' here means 'summon', so 'I will summon you a doctor'."]),
    (6, None, ["'No, seriously, do not call doctors.' Listen to how ", ('max', 'не'), ('max', 'надо'), " means 'not necessary', which is the everyday way to say 'don't' or 'no need'. And ", ('max', 'врачей'), ' is the plural form for doctors.']),
    (7, None, ["'Why? You need urgent help after all.' The small word ", ('vika', 'же'), " is the 'after all' in the sentence, with a touch of 'come on'. Notice how ", ('vika', 'нужна'), " ends in an 'a' sound to match 'help', which is a feminine word."]),
    (8, None, ["'Look, here are two tickets to the cinema.' You can hear how ", ('max', 'Смотри'), " is 'look!', the order form you use with a friend. Notice ", ('max', 'вот'), " means 'here it is', and you'll hear it everywhere. Notice for cinema never changes shape, whether it's 'to the cinema' or 'at the cinema'."]),
    (9, None, ["'Well you are a jerk, honestly!' The start of the sentence works like a rolled-eyes 'well, aren't you something'. The last two words, ", ('vika', 'честное'), ('vika', 'слово'), ", mean 'honest word', which is how Russians say 'honestly'."]),
    (10, None, ["'Shall we go to the cinema tonight, eh?' You can hear how 'Let's go' is the 'we' form of 'go', which Russians use for invitations. 'Evening' takes an ending here to mean 'in the evening'. The little ", ('max', 'а'), " at the end is like asking 'right?'."]),
    (11, None, ["'You are a real idiot, I will not go anywhere!' Let's examine the words: ", ('vika', 'никуда'), ' and ', ('vika', 'не'), " sit side by side, because Russian likes two 'no' words together. The term 'real' is a handy booster here."]),
    (12, None, ["'Alright, then I will go to the cinema alone.' Notice for 'alone', ", ('max', 'один'), ", shares that with the number 'one'. Notice ", ('max', 'Ладно'), " is a shrug that means 'fine'."]),
]
