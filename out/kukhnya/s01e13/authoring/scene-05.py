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
INTRO = 'Max turns up late to the kitchen and has a lame excuse ready. Chef Barinov sends him to the stockroom and asks Vika what she thinks. The Russian first.'
OPENER = 'Again, and this time listen out for the excuses.'
TRANSITION = 'Now the whole scene again.'
OUTRO = "Max is sent down to the stockroom for the day. Watch who looks guiltiest, because it isn't the one being punished. See you next time."
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
    (0, None, "'Hi to everyone.' 'Vsem' means 'to everyone'. Max says 'privet vsem', 'hi to all', and there's no 'I say'."),
    (1, None, "'Boss, excuse me, I simply overslept.' 'Prospal' means 'overslept', made from 'spat', to sleep, with 'pro' meaning 'through'. 'Izvinite' is the polite form for a boss."),
    (2, None, "'Such a thing will not happen again.' Russian says 'will not repeat itself', and the 'itself' is the 'sya'. 'Any more' is a single word, and Max sounds almost solemn."),
    (3, None, "'Today you are working in the stockroom.' 'Rabotaesh' is 'you work', and Russian uses it for 'you are working' and 'you will work'. 'Na sklade' is 'in the warehouse', with 'na' again, and it's the usual way to say it."),
    (4, None, "'Oversleep one more time and I will fire you.' No 'if' appears in the Russian. It's 'one more time you oversleep, I fire you', and the dash does the work of 'then'."),
    (5, None, "'But boss, I am an excellent cook.' With no 'am' it's just 'I excellent cook', which makes it sound blunt. 'Otlichny' is a word you'll hear for 'excellent' and for the top mark in school."),
    (6, None, "'A cook must arrive at work on time.' 'Vovremya' is literally 'in time', glued together from 'v' and 'vremya'. 'Prikhodit' is the verb for arriving on foot, with an 'dolzhen' in front for 'must'."),
    (7, None, "'I promise to never be late again.' Russian happily piles up 'more', 'never' and 'not', literally 'more never not be late'. That triple negative is correct, and the verb 'opazdyvat' is 'to be late'."),
    (8, None, "'I have said my word.' 'Svoyo slovo' is 'my own word', neuter to match 'slovo'. It's a set phrase, a bit like saying 'my word is final'."),
    (9, None, "'Victoria Sergeyevna, why are you so silent?' Barinov uses the polite 'vy' with Vika here, in front of the staff. 'Molchite' is 'you are silent'. 'Tak' means 'so'."),
    (10, None, "'It is necessary to go to bed earlier to not oversleep.' Russians say 'lay yourself to sleep' for going to bed. Then 'chtoby', in order to, brings in the thing to avoid."),
    (11, None, "'Here you see, she agrees with me.' The pointing word 'vot' does the work of 'there'. The ending 'a' on 'soglasna' shows that the agreeing person is a woman."),
]
