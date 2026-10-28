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
INTRO = 'Max has just made up his mind to go after Vika, and his first idea is a bad one. He meets her in the corridor and suddenly clutches his side and groans. Here it is in Russian first.'
OPENER = "Let's slow down and watch the trick come apart."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Vika is not amused, and Max is left holding two tickets and no one to use them with. When you watch, notice that Russian pain is always 'to me', never 'I'."
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
    (0, None, "'Ouch! How it hurts me in the stomach!' Russian doesn't say 'I am in pain'. It says 'to me painful', and 'to me' is the word 'mne'. 'Stomach' picks up an 'e' on the end because of 'in'."),
    (1, None, "'Max, what is it? Does it hurt you a lot?' The first question, 'chto takoe', is a handy way to say 'what's the matter?', literally 'what such'. The second uses 'to you painful', the same pattern as 'to me painful', with 'tebe' for 'you'."),
    (2, None, "'I do not know what this is.' It's three flat words, 'I not know'. Max keeps it vague on purpose."),
    (3, None, "'Oh, on the right side this is very bad!' 'On the right side' is literally 'from the right side'. The word for 'right' is also the root of the word for 'correct', so Russian is saying 'right' and 'right' with the same sound. Vika is already worried."),
    (4, None, "'My God, how much it hurts me now.' The first word is a special shape of 'God', used only when you call out to him. 'Seychas' means 'now', and it is also what people say for 'in a moment'."),
    (5, None, "'Let me quickly call a doctor for you.' It starts with 'give', which is how Russians say 'let me' or 'let's'. 'Call' here means 'summon', so 'I will summon you a doctor'."),
    (6, None, "'No, seriously, do not call doctors.' 'Ne nado', 'not necessary', is the standard way to say 'don't' or 'no need'. 'Doctors' is the plural and ends in 'ey'."),
    (7, None, "'Why? You need urgent help after all.' The small word 'zhe' is the 'after all' in the sentence, with a touch of 'come on'. 'Needed' ends in 'a' to match 'help', which is a feminine word."),
    (8, None, "'Look, here are two tickets to the cinema.' 'Look' is the order form. 'Vot' means 'here it is', and you'll hear it everywhere. The word for cinema never changes shape, whether it's 'to the cinema' or 'at the cinema'."),
    (9, None, "'Well you are a jerk, honestly!' 'Nu ty i' works like a rolled-eyes 'well, aren't you something'. The last two words are literally 'honest word', which is how Russians say 'I swear'."),
    (10, None, "'Shall we go to the cinema tonight, eh?' 'Let's go' is the 'we' form of 'go', which Russians use for invitations. 'Evening' ends in 'om' here to mean 'in the evening'. The little 'a' at the end is a 'right?'."),
    (11, None, "'You are a real idiot, I will not go anywhere!' 'Nowhere' and 'not' sit side by side, so it's literally 'nowhere not I will go'. That is correct Russian. 'Real' is a handy booster: a real idiot, a real friend, a real chef."),
    (12, None, "'Alright, then I will go to the cinema alone.' The word for 'alone' is the same as the number 'one', so literally he says 'I will go one'. 'Ladno' is a shrug that means 'fine'."),
]
