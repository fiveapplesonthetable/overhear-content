# Authoring module for kukhnya-s06e16-scene-10.
ID = 'kukhnya-s06e16-scene-10'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 16
SCENE = 10
TITLE = 'Пропавшая туника и слухи  (The Missing Tunic and Rumors)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.16'
SOURCE_FILE = 'sources/kukhnya/s06/e16.ru.srt'
INTRO = "In the morning, Chef Barinov tells Elena that he could not get tickets to the fashion show so she will not find out about his scheme, while hiding her turquoise tunic in his bag. Back at the hotel, Mikhail catches Senya and Fedya sneaking food to an empty room number, and Polina brags about partying with yesterday's bartender!"
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Overhearing the model boast about spending the night with yesterday's bartender, Nastya immediately assumes it was Kostya! See you next time!"
CLOSING = ('mikhail', 'Пока!')
STORY = [
    ('barinov', 'Лена, там ограниченное число пригласительных билетов.', 'Lena, there is a limited number of invitation tickets.', [(140, 'А там ограниченное число пригласительных')], 'adapted'),
    ('barinov', 'Я просил оставить нам хотя бы пару.', 'I asked them to save at least a couple for us.', [(141, 'Я просил меня оставить парочку')], 'adapted'),
    ('elena', 'Очень жаль, что нам не дали.', 'It is a great pity that they did not give us any.', [(142, 'Не дали. Жаль')], 'adapted'),
    ('elena', 'Витя, ты не видел мою тунику?', 'Vitya, have you seen my tunic?', [(143, 'Витя, а ты не видел мою бирюзовую тунику')], 'adapted'),
    ('barinov', 'И я тебя люблю, до вечера!', 'And I love you too, see you tonight!', [(144, 'И я тебя люблю до вечера')], 'adapted'),
    ('elena', 'Кажется, он уже совсем глухой стал.', 'It seems he has gone completely deaf already.', [(145, 'Совсем глухой стал')], 'adapted'),
    ('mikhail', 'Опять несёте мясо для костюмера?', 'Are you carrying meat for the costume designer again?', [(149, 'Опять мясо для костюмера')], 'adapted'),
    ('mikhail', 'Я узнавал, в том номере никто не живёт.', 'I checked, nobody lives in that room.', [(152, 'никто не живет')], 'adapted'),
    ('mikhail', 'Вы носите еду мимо нашей кассы!', 'You are carrying food past our cash register!', [(153, 'таскаете еду мимо кассы')], 'adapted'),
    ('mikhail', 'Я вычту стоимость из вашей зарплаты.', 'I will deduct the cost from your salary.', [(154, 'Я просто вычту ее стоимость из вашей'), (155, 'Зарплаты')], 'adapted'),
    ('barinov', 'Ладно, ведь высокая цель оправдывает средства.', 'Alright, a noble goal justifies the means after all.', [(158, 'Цель оправдывает средства')], 'adapted'),
    ('elena', 'Жаль, не видно вчерашнего симпатичного бармена.', "Too bad yesterday's handsome bartender is not around.", [(161, 'не видно вчерашнего симпатичного бармена')], 'adapted'),
]
WALK = [
    (0, None, "'Lena, there is a limited number of invitation tickets.' Barinov reminds Elena that someone there is a limited number of invitation tickets before the moment passes."),
    (1, None, "'I asked them to save at least a couple for us.' Because he asked them to save at least a couple for them, Barinov treats the matter as settled."),
    (2, None, "'It is a great pity that they did not give us any.' Mentioning that it is a great pity that they did not give them any moves the talk in a new direction."),
    (3, None, "'Vitya, have you seen my tunic?' Here checking whether Barinov seen her tunic shows Elena looking for the real truth."),
    (4, None, '\'And I love you too, see you tonight!\' Insisting that he loves Elena too see Elena tonight shows Barinov is not backing down. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (5, None, "'It seems he has gone completely deaf already.' Pointing out that it seems he has gone completely deaf already gives Barinov a sobering reality check."),
    (6, None, "'Are you carrying meat for the costume designer again?' Asking whether Barinov carrying meat for the costume designer again is how Mikhail puts Barinov on the spot."),
    (7, None, '\'I checked, nobody lives in that room.\' Realizing that he checked nobody lives in that room changes how Mikhail handles the situation. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (8, None, '\'You are carrying food past our cash register!\' Mikhail insists that Barinov is carrying food past their cash register, leaving Barinov no room to argue. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (9, None, "'I will deduct the cost from your salary.' Even though he will deduct the cost from Barinov's salary, Mikhail keeps a steady face in front of Barinov."),
    (10, None, "'Alright, a noble goal justifies the means after all.' Admitting that Alright a noble goal justifies the means after all shows Barinov being honest for a change."),
    (11, None, "'Too bad yesterday's handsome bartender is not around.' Saying that too bad yesterday handsome bartender is not around is how Elena sets the tone with Barinov."),
]
