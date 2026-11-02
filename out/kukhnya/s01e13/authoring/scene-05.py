# Authoring module for kukhnya-s01e13-scene-05.
ID = 'kukhnya-s01e13-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 5
TITLE = "Опоздание Макса  (Max's Tardiness)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Max turns up late to the kitchen and has a lame excuse ready. Chef Barinov sends him to the stockroom and asks Vika what she thinks. The original language first."
OPENER = 'Again, and this time listen out for the excuses.'
TRANSITION = 'Now the whole scene again.'
OUTRO = "Max is sent down to the stockroom for the day. Vika sided with the boss, so Max walks to work alone and works alone. Bye for now."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Привет всем.', 'Hi to everyone.', [(64, 'Привет всем.')], ''),
    ('max', 'Шеф, извините, я просто проспал.', 'Boss, excuse me, I simply overslept.', [(66, 'Шеф, извините.'), (71, 'Я просто проспал.')], ''),
    ('max', 'Больше такое не повторится.', 'Such a thing will not happen again.', [(72, 'больше такое не повторится.')], ''),
    ('barinov', 'Сегодня ты работаешь на складе.', 'Today you are working in the stockroom.', [(61, 'сегодня')], ''),
    ('barinov', 'Ещё раз проспишь — я тебя уволю.', 'Oversleep one more time — I will fire you.', [(59, 'еще')], ''),
    ('max', 'Но шеф, я отличный повар.', 'But boss, I am an excellent cook.', [], ''),
    ('barinov', 'Повар должен приходить на работу вовремя.', 'A cook must arrive at work on time.', [], ''),
    ('max', 'Я обещаю больше никогда не опаздывать.', 'I promise to never be late again.', [], ''),
    ('barinov', 'Я сказал своё слово.', 'I have said my word.', [], ''),
    ('barinov', 'Виктория Сергеевна, почему вы так молчите?', 'Victoria Sergeyevna, why are you so silent?', [], ''),
    ('vika', 'Надо раньше ложиться спать, чтобы не проспать.', 'It is necessary to go to bed earlier to not oversleep.', [(61, 'надо')], ''),
    ('barinov', 'Вот видите, она со мной согласна.', 'Here you see, she agrees with me.', [], ''),
]
WALK = [
    (0, None, ["'Hi to everyone.' Let's inspect the sentence: ", ('max', 'всем'), " means 'to everyone'. Max says 'hi to all', using ", ('max', 'Привет'), ", and there is no 'I say'."]),
    (1, None, ["'Boss, excuse me, I simply overslept.' The term for 'overslept', ", ('max', 'проспал'), ", is made from the term to sleep, with a prefix meaning 'through'. The term ", ('max', 'извините'), ' supplies a polite form for a boss.']),
    (2, None, ["'Such a thing will not happen again.' The language says 'will not repeat itself', ", ('max', 'не'), ('max', 'повторится'), ", and the 'itself' is in the ending. The term for 'more', ", ('max', 'Больше'), ", stands in for 'any more' at the front."]),
    (3, None, ["'Today you are working in the stockroom.' Notice for 'you work', ", ('barinov', 'работаешь'), ", is used for 'you are working' and 'you will work'. The expression for 'in the stockroom', ", ('barinov', 'на'), ('barinov', 'складе'), ", is literally 'on the store', and uses the usual word for 'on'."]),
    (4, None, ["'Oversleep one more time — I will fire you.' No 'if' appears in the sentence. It is 'one more time you oversleep, I fire you', ", ('barinov', 'я'), ('barinov', 'тебя'), ('barinov', 'уволю'), ", and the dash does the work of 'then'."]),
    (5, None, ["'But boss, I am an excellent cook.' With no 'am' it is just 'I excellent cook', which makes it sound blunt. The term for 'excellent', ", ('max', 'отличный'), ", is a word you'll hear for 'excellent' and for the top mark in school."]),
    (6, None, ["'A cook must arrive at work on time.' Notice for 'on time', ", ('barinov', 'вовремя'), ", literally says 'in time', glued together from 'in' and 'time'. Notice for arriving on foot, ", ('barinov', 'приходить'), ", goes with 'must', ", ('barinov', 'должен'), ', in front.']),
    (7, None, ["'I promise to never be late again.' The language happily piles up 'more', 'never', and 'not', using ", ('max', 'больше'), ('max', 'никогда'), ('max', 'не'), ", literally 'more never not be late'. That triple negative is correct, and the verb for 'to be late' is ", ('max', 'опаздывать'), '.']),
    (8, None, ["'I have said my word.' Notice for 'my own word', ", ('barinov', 'своё'), ('barinov', 'слово'), ", matches the gender of 'word'. It is a set phrase, a bit like saying 'my word is final'."]),
    (9, None, ["'Victoria Sergeyevna, why are you so silent?' Barinov uses the polite formal 'you' and her full name with patronymic. Notice for 'you are silent' is ", ('barinov', 'молчите'), ". Notice for 'so' is ", ('barinov', 'так'), '.']),
    (10, None, ["'It is necessary to go to bed earlier to not oversleep.' Locals say 'lay yourself to sleep', ", ('vika', 'ложиться'), ('vika', 'спать'), ", for going to bed. Then the expression for 'in order to', ", ('vika', 'чтобы'), ', brings in the thing to avoid.']),
    (11, None, ["'Here you see, she agrees with me.' Notice for 'there, you see', ", ('barinov', 'Вот'), ('barinov', 'видите'), ", is the stock expression for 'told you so'. The ending on the word for 'agrees', ", ('barinov', 'согласна'), ', shows that the agreeing person is a woman.']),
]
