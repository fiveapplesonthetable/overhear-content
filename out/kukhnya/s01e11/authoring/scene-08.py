# Authoring module for kukhnya-s01e11-scene-08.
ID = 'kukhnya-s01e11-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 8
TITLE = 'Потерянный телефон  (The Lost Phone)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "At the Claude Monet bar counter, an exhausted and hungover visitor approaches bartender Kostya. Relieved to recover the mobile phone he left behind the night before, he unburdens his romantic sorrows to the sympathetic bartender. Let's listen to their friendly bar exchange in Russian."
OPENER = "Now let's examine how Kostya assists the forgetful guest at the bar line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Comforted by the bartender's hospitality, the customer rests at the bar before facing the rest of his day. Next time you watch the episode, listen for the Russian expressions for 'bartender' and 'to come back' — you will catch every word right away. See you next time!"
CLOSING = ('guest', 'Пока!')
STORY = [
    ('guest', 'Привет! Как твои дела, бармен?', 'Hello! How are things, bartender?', [(100, 'Здрасте.')], ''),
    ('kostya', 'Здравствуйте! Как вы себя сегодня чувствуете?', 'Hello! How are you feeling today?', [(101, 'Как себя чувствуете?')], ''),
    ('guest', 'Эх, сегодня мне хуже, чем вчера.', 'Ugh, today I feel worse than yesterday.', [(101, 'Эх, хуже, чем вчера.')], ''),
    ('guest', 'Ты случайно не находил мой телефон?', 'Did you happen to find my phone?', [(102, 'Ты мой телефон не находил?')], ''),
    ('kostya', 'Да, я нашёл его возле стойки.', 'Yes, I found it near the counter.', [(103, 'Находил.')], ''),
    ('guest', 'Огромное спасибо за помощь, друг!', 'Huge thanks for the help, friend!', [(103, 'О, спасибо.')], ''),
    ('guest', 'Скажи честно, моя девушка не звонила?', 'Tell me honestly, did my girlfriend not call?', [(104, 'Она не звонила?')], ''),
    ('kostya', 'Нет, сюда пока никто не звонил.', 'No, no one has called here yet.', [(104, 'Нет.')], ''),
    ('guest', 'Она ещё не вернулась из Саратова.', 'She has not returned from Saratov yet.', [(105, 'Наверное, еще не вернулась из Саратова.')], ''),
    ('kostya', 'Вы вчера долго говорили про неё.', 'Yesterday you spoke about her for a long time.', [(107, 'Ну, вы же мне вчера рассказывали.')], ''),
    ('guest', 'Да, память медленно возвращается ко мне.', 'Yes, my memory is slowly returning to me.', [(108, 'Да.')], ''),
    ('kostya', 'Вот вам напиток за счёт заведения.', 'Here is a drink for you on the house.', [(110, 'За счет заведения.')], ''),
    ('guest', 'Спасибо тебе за доброту, дружище!', 'Thank you for your kindness, buddy!', [(111, 'Спасибо тебе, дружище.')], ''),
]
WALK = [
    (0, None, "'Hello! How are things, bartender?' The guest says hello and asks how things are with the bartender. He is friendly. He calls the bartender 'barmen'."),
    (1, None, "'Hello! How are you feeling today?' Kostya says hello and asks how he is feeling today. He remembers the man was drinking yesterday. 'Chuvstvuete' relates to feeling."),
    (2, None, "'Ugh, today I feel worse than yesterday.' The guest groans that today he feels worse than yesterday. He has a hangover. 'Khuzhe chem vchera' means worse than yesterday."),
    (3, None, "'Did you happen to find my phone?' The guest asks if he happened to find his phone. He lost it while drinking. 'Sluchayno ne nakhodil' means did not happen to find."),
    (4, None, "'Yes, I found it near the counter.' Kostya confirms he found it near the counter. He is being helpful. 'Vozle stoyki' means near the bar counter."),
    (5, None, "'Huge thanks for the help, friend!' The guest gives huge thanks for the help, calling him a friend. He is very relieved. 'Ogromnoe spasibo' means huge thanks."),
    (6, None, "'Tell me honestly, did my girlfriend not call?' The guest asks him to tell honestly if his girlfriend called. He is worried he missed her call. 'Skazhi chestno' means tell honestly."),
    (7, None, "'No, no one has called here yet.' Kostya replies no one has called there yet. The phone has been quiet. 'Poka nikto' means no one yet."),
    (8, None, "'She has not returned from Saratov yet.' The guest mentions she has not returned from another city yet. He is explaining why she might call. He is referring to another Russian city."),
    (9, None, "'Yesterday you spoke about her for a long time.' Kostya notes he spoke about her for a long time yesterday. The man was very talkative while drunk. 'Dolgo govorili' means talked for a long time."),
    (10, None, "'Yes, my memory is slowly returning to me.' The guest admits his memory is slowly returning to him. He was very drunk. 'Medlenno vozvrashchaetsya' means slowly returning."),
    (11, None, "'Here is a drink for you on the house.' Kostya offers a drink on the house. He is being a good bartender. 'Za schyot zavedeniya' means at the establishment's expense."),
    (12, None, "'Thank you for your kindness, buddy!' The guest thanks his buddy for his kindness. He appreciates the free drink. 'Dobrotu' means kindness."),
]
