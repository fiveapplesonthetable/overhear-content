# Authoring module for kukhnya-s01e14-scene-02.
ID = 'kukhnya-s01e14-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 2
TITLE = 'Жажда веселья  (Thirst for Fun)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'At the restaurant, Max finds Sasha admiring a new cake she has decorated. He compliments her, and he has an idea for what to do next. The Russian is first.'
OPENER = 'Their chat again, slowly.'
TRANSITION = 'Now the whole chat, straight through.'
OUTRO = 'Sasha leaves her apron behind, and the two of them head outside. Keep an eye on the cake. Speak soon.'
CLOSING = ('sasha', 'Пока!')
STORY = [
    ('max', 'Саша, ты видела новый красивый торт?', 'Sasha, did you see the new beautiful cake?', [], ''),
    ('sasha', 'Конечно, я сама его сегодня украшала.', 'Of course, I decorated it myself today.', [], ''),
    ('max', 'Он выглядит просто великолепно.', 'It looks simply magnificent.', [], ''),
    ('sasha', 'Спасибо, я очень сильно старалась.', 'Thank you, I tried very hard.', [], ''),
    ('max', 'Шеф уже видел твою новую работу?', 'Has the chef already seen your new work?', [], ''),
    ('sasha', 'Да, он был очень доволен мной.', 'Yes, he was very satisfied with me.', [], ''),
    ('max', 'И это у вас получилось.', 'And you pulled it off.', [(4, 'И это у вас получилось.')], ''),
    ('sasha', 'А теперь можно немного отдохнуть.', 'And now we can rest a little.', [], ''),
    ('max', 'Кто тут хочет повеселиться?', 'Who wants to have some fun?', [(5, 'Кто тут хочет повеселиться?')], ''),
    ('sasha', 'Я хочу.', 'I do.', [(6, 'Я хочу.')], ''),
    ('max', 'Тогда пойдём со мной на улицу.', 'Then let us go outside with me.', [], ''),
    ('sasha', 'Подожди, я только сниму свой фартук.', 'Wait, I will just take off my apron.', [], ''),
]
WALK = [
    (0, None, "'Sasha, did you see the new beautiful cake?' The 'a' on 'videla' is there because the question is to a woman. 'Tort' is masculine, which is why 'new' and 'beautiful' both end in 'y'."),
    (1, None, "'Of course, I decorated it myself today.' Sasha's 'sama' means 'by myself' and has an 'a' because she is a woman. Russians call a cake 'he', so the 'it' is 'him' again."),
    (2, None, "'It looks simply magnificent.' The cake is masculine, so Russian says 'he looks'. After 'looks' comes 'velikolepno', and it describes how he looks."),
    (3, None, "'Thank you, I tried very hard.' Literally 'I tried myself', because 'staralas'' ends in 'sya'. And 'very hard' is 'very strongly' in Russian."),
    (4, None, "'Has the chef already seen your new work?' 'Tvoyu novuyu rabotu' is 'your new work', where 'work' takes the 'u' it needs after 'saw'. 'Uzhe' means 'already'."),
    (5, None, "'Yes, he was very satisfied with me.' Russian says 'pleased by me', so 'me' takes the ending 'oy' and becomes 'mnoy'. A man would be 'dovolen', with no ending."),
    (6, None, "'And you pulled it off.' Literally, 'at you it turned out'. Max suddenly switches to the formal 'you', as if he were a judge of the cake."),
    (7, None, "'And now we can rest a little.' 'Mozhno' is the handy word for 'it's allowed' or 'we can'. 'Otdokhnut' is 'to have a rest'."),
    (8, None, "'Who wants to have some fun?' Fun comes from 'veselye', and the 'sya' on the end of the action turns it into 'enjoy oneself'."),
    (9, None, "'I do.' Sasha answers with just 'ya khochu', 'I want', and nothing else. Russians answer by repeating the action word, so a separate 'yes' isn't needed."),
    (10, None, "'Then let us go outside with me.' Russians say 'onto the street' for 'outside'. Max's 'let's go' is a single word, and 'with me' is 'so mnoy'."),
    (11, None, "'Wait, I will just take off my apron.' 'Snimu' is 'I will take off'. The 'my own' that Russians like to add means the apron is hers."),
]
