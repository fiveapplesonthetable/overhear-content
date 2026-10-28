# Authoring module for kukhnya-s01e16-scene-22.
ID = 'kukhnya-s01e16-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 22
TITLE = 'Мой долг  (My duty)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "At Claude Monet, the news is bad. Barinov asks what has just been said, and Nastya tells him they've been told to go; for a moment it looks like the end of everything. We'll hear it in Russian first."
OPENER = "Now let's go through it carefully."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Nobody in the kitchen is sure what happens next. Remember that 'dolg' means both 'duty' and 'debt', which is why Russians use it for obligations of any kind. See you next time!"
CLOSING = ('nastya', 'До свидания!')
STORY = [
    ('barinov', 'Что он сказал?', 'What did he say?', [], ''),
    ('nastya', 'Он сказал нам уходить.', 'He told us to leave.', [], ''),
    ('barinov', 'Я не верю в это.', 'I do not believe this.', [], ''),
    ('nastya', 'Это конец?', 'Is this the end?', [], ''),
    ('barinov', 'Я не знаю.', 'I do not know.', [], ''),
    ('max', 'Шеф, что делать?', 'Chef, what to do?', [], ''),
    ('barinov', 'Мы должны уйти.', 'We must leave.', [], ''),
    ('nastya', 'Мне очень жаль.', 'I am very sorry.', [], ''),
    ('nastya', 'Собирайтесь.', 'Pack your things.', [(285, 'Собирайтесь.')], ''),
    ('nastya', 'Извините.', 'I am sorry.', [(286, 'Извините,')], ''),
    ('nastya', 'Это мой долг.', 'It is my duty.', [(286, 'это мой долг.')], ''),
    ('barinov', 'Хорошо.', 'Good.', [], ''),
]
WALK = [
    (0, None, "'What did he say?' The order is just like English. The past form of 'say' ends in a bare 'l' because the one who spoke is a man."),
    (1, None, "'He told us to leave.' Russian says 'said to us', with an 'am' type ending, and then simply 'to leave'. It leaves out the 'that'."),
    (2, None, "'I don't believe it.' Russians believe 'in' something, so a small word for 'in' comes before 'this'. The 'u' at the end of 'believe' is the 'I' ending."),
    (3, None, "'Is this the end?' There's no word for 'is', and the question comes only from the rising voice. 'End' ends in a hard 'ts'."),
    (4, None, "'I don't know.' This time the 'I' is spelled out, which gives the line a heavier tone. Without it, the line would sound a touch more casual."),
    (5, None, "'Chef, what do we do?' It's just 'what to do', in the basic form, with no 'we' at all. Max talks to the boss with a plain title."),
    (6, None, "'We have to leave.' 'Must' is plural to go with 'we'. 'Leave' is the finished kind, meaning to go away for good."),
    (7, None, "'I'm very sorry.' Russian says 'to me very pity', so the sorrow is something that happens to you. It's a gentle way to give bad news."),
    (8, None, "'Pack your things.' The 'sya' on the end means 'gather yourselves', and 'te' makes it a command to several people. In real life it also means 'get ready to go'."),
    (9, None, "'Excuse me.' It's the standard word for apologising to a stranger, like bumping into someone. It ends in 'ite', the polite command ending again."),
    (10, None, "'It's my duty.' 'Duty' is also 'debt', so duty is what you owe. 'My' is masculine to match."),
    (11, None, "'Good.' It sounds resigned here, like 'fine' or 'all right'. Barinov has nothing left to argue with."),
]
