# Authoring module for domashniy-arest-s01e02-scene-02.
ID = 'domashniy-arest-s01e02-scene-02'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = "Вот теперь сорок  (Now It's Forty)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "Still New Year's Eve, at Arkady's house. Last time, he arrived late with his deputy Pasha, left his wife Vika waiting with the champagne, and led Pasha away to another room. Now we see why: he wants to show Pasha something, and then he has plans of his own for the night. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's take it a line at a time. The two men are alone now, and Arkady proudly shows Pasha a big pile of cash."
TRANSITION = "Here's the whole scene again, from the pyramid to the phone call."
OUTRO = "Forty million on the table, a bonus for the deputy, and three districts in the dark so the boss can slip out. If you remember the joke about counting to forty, you've got the heart of it; goodbye for now. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Вот, Паша. Моя пирамида.', 'Here, Pasha. My pyramid.', [(38, 'Моя пирамида')], "'Вот, Паша' added"),
    ('arkady', 'Ну-ка скажи, сколько здесь?', 'Go on, tell me: how much is here?', [(41, 'Ну-ка скажи, сколько здесь')], ''),
    ('pasha', 'Не знаю. Думаю, сорок.', "I don't know. Forty, I think.", [(42, 'не знаю, думаю, сорок')], "'Ну' dropped"),
    ('arkady', 'Эх, Паша, Паша. Ты считать не умеешь.', "Oh, Pasha, Pasha. You can't count.", [(44, 'считать не умеешь')], "crude 'Ни хрена' dropped; 'Эх, Паша, Паша' added"),
    ('arkady', 'И это мой заместитель!', 'And this is my deputy!', [], "adapted from cue 43 ('What kind of deputy am I keeping?'), rewritten, so not cited"),
    ('arkady', 'Вот теперь сорок.', "Now it's forty.", [(47, 'Вот теперь сорок')], ''),
    ('arkady', 'Вот теперь с Новым годом!', 'Now, Happy New Year!', [(48, 'Вот теперь с Новым годом')], ''),
    ('pasha', 'Слушай, Аркаша, а ты не пробовал это вложить?', 'Listen, Arkasha, have you ever tried investing it?', [(54, 'Слушай, Аркаша'), (54, 'а ты не пробовал это вложить')], "'извини' dropped; 'как-то' dropped"),
    ('pasha', 'Деньги же должны работать.', 'Money should work, after all.', [(55, 'деньги же должны работать')], "'Ну' dropped"),
    ('arkady', 'На тебе бонус, Паша. Вложи.', "Here's a bonus for you, Pasha. Invest it.", [(58, 'На тебе бонус, Паша'), (59, 'Вложи')], ''),
    ('pasha', 'Аркаша, я не ожидал. Спасибо!', "Arkasha, I didn't expect that. Thank you!", [(60, 'Аркаша, я не ожидал'), (52, 'Спасибо')], "'Спасибо' borrowed from cue 52, a moment earlier"),
    ('arkady', 'Слушай, я уеду на полтора часа. Ты с Викой посиди, понял?', "Listen, I'm going out for an hour and a half. You stay with Vika, got it?", [(61, 'Слушай'), (62, 'Ты с Викой посиди, понял')], "'я, короче, отъеду сейчас на часик-полтора' -> 'я уеду на полтора часа'"),
    ('pasha', 'А что я скажу?', 'But what will I say?', [(63, 'я скажу')], "'ж' and '-то' dropped"),
    ('arkady', 'Скажи: салют попал в станцию. Три района без света.', 'Say a firework hit the power station. Three districts without electricity.', [(66, 'Салют'), (67, 'Три района без света')], "'Салют по станции попал' -> 'салют попал в станцию' (standard grammar); 'Скажи' moved from cue 65"),
    ('arkady', 'И позвони Цыганкову, пусть отключат свет.', 'And phone Tsygankov, have them cut the power.', [(68, 'пусть отключат')], "word order changed ('Цыганкову позвони' -> 'позвони Цыганкову'); 'свет' added"),
    ('pasha', 'Виталий Алексеевич, с Новым годом! Отключи, пожалуйста, три района.', 'Vitaly Alekseyevich, Happy New Year! Please cut the power in three districts.', [(72, 'Виталий Алексеевич'), (72, 'С Новым годом'), (73, 'пожалуйста')], "'ты можешь вырубить Ленинский, Октябрьский и Симашка' -> 'Отключи три района'"),
    ('pasha', 'Ну, потянуло кота на сметану.', 'Well, the cat has smelled the cream.', [(76, 'Ну, потянуло кота на сметану')], ''),
]
WALK = [
    (0, None, "'Here, Pasha. My pyramid.' The pyramid is a neat stack of banknotes on the table. The first word, 'here', points at it. Then he tests his deputy."),
    (1, None, "'Go on, tell me: how much is here?' The first word is a playful 'come on, go on', and the question word means 'how much'. Pasha takes a guess."),
    (2, None, "'I don't know. Forty, I think.' He means forty million. Notice 'I think' needs no 'I' in Russian here: the verb ending already says who is thinking. Arkady sighs."),
    (3, None, "'Oh, Pasha, Pasha. You can't count.' Literally, 'you don't know how to count'. The verb for 'to count' sits in its basic form before the verb meaning 'can, know how to'."),
    (4, None, "'And this is my deputy!' The word for 'deputy' is a long one, but you'll hear it a lot in this series. Then Arkady takes a few bundles off the top and puts them away in a smaller briefcase."),
    (5, None, "'Now it's forty.' So Pasha was wrong, and now the pile matches his guess exactly. Arkady is very pleased with his little joke."),
    (6, None, "'Now, Happy New Year!' The same two opening words again, 'well, now'. Pasha has a clever idea."),
    (7, None, "'Listen, Arkasha, have you ever tried investing it?' The verb at the end means 'to put money into something'. Remember it, because Arkady is about to throw it back at him."),
    (8, None, "'Money should work, after all.' The word for money is always plural in Russian, so the verb is plural too. Arkady answers with a gesture."),
    (9, 'На тебе бонус, Паша.', "'Here's a bonus for you, Pasha.' The first two words, literally 'on you', mean 'here, take this'. He hands Pasha a bundle of notes."),
    (9, 'Вложи.', "'Invest it.' A one-word command, from the same verb Pasha used. Pasha is surprised."),
    (10, None, "'Arkasha, I didn't expect that. Thank you!' The verb is past tense and masculine, because Pasha is a man. Then Arkady gets to the real business of the evening."),
    (11, 'Слушай, я уеду на полтора часа.', "'Listen, I'm going out for an hour and a half.' The verb means leaving by car, and the phrase at the end is literally 'for one and a half hours'."),
    (11, 'Ты с Викой посиди, понял?', "'You stay with Vika, got it?' The command literally means 'sit for a while'. The little question at the end, 'understood?', is very common. Pasha has a practical question."),
    (12, None, "'But what will I say?' Like the verb for going out, this one looks present but means the future. Arkady already has a story ready."),
    (13, 'Скажи: салют попал в станцию.', "'Say a firework hit the power station.' The first word is the command 'say'. A New Year firework is the perfect excuse."),
    (13, 'Три района без света.', "'Three districts without electricity.' The word for 'without' makes the next word change its ending. The light has gone out, so no one can go anywhere. And to make the lie true, he gives one more order."),
    (14, None, "'And phone Tsygankov, have them cut the power.' Tsygankov is the man in charge of the town's electricity. The word in the middle means 'let them'. So Arkady is ready to plunge three districts into darkness for his alibi. As soon as he's gone, Pasha makes the call."),
    (15, None, "'Vitaly Alekseyevich, Happy New Year! Please cut the power in three districts.' He uses the man's first name and his father's name, which is polite, but the casual 'you' in the command, so they know each other well. And he explains with a saying."),
    (16, None, "'Well, the cat has smelled the cream.' A Russian saying: someone has gone off after something tempting. Pasha guesses that Arkady is off to see a woman. The song that follows asks how much money you need to be happy."),
]
