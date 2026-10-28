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
INTRO = 'At the restaurant, Max finds Sasha admiring a new cake she has decorated. He compliments her, and he has an idea for what to do next. Here is the scene in Russian first.'
OPENER = 'Now the chat once more, taken slowly.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Sasha leaves her apron behind, and the two of them head outside. When you watch, keep an eye on the cake. Speak soon.'
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
    (0, None, "'Sasha, did you see the new beautiful cake?' 'Videla' ends in 'a' because Sasha is a woman. Both 'novy' and 'krasivy' end in 'y' to match 'tort', a masculine word."),
    (1, None, "'Of course, I decorated it myself today.' 'Sama' is 'by myself', and it ends in 'a' because Sasha is speaking. 'Ego' is 'it', and in Russian a cake is a 'he'."),
    (2, None, "'It looks simply magnificent.' Russian says 'he looks', 'on vyglyadit', because 'tort' is a masculine word. 'Velikolepno' is the adverb 'magnificently'."),
    (3, None, "'Thank you, I tried very hard.' 'Staralas'' ends in 'sya', so it's 'I tried myself'. 'Ochen silno' is 'very strongly', which is how you say 'very hard' in Russian."),
    (4, None, "'Has the chef already seen your new work?' 'Tvoyu novuyu rabotu' is 'your new work', where 'work' takes the 'u' it needs after 'saw'. 'Uzhe' means 'already'."),
    (5, None, "'Yes, he was very satisfied with me.' 'Dovolen' is 'pleased', and it takes the ending 'oy' on the person: 'mnoy' is 'with me'. So Russian says 'pleased by me'."),
    (6, None, "'And you pulled it off.' 'U vas poluchilos'' is literally 'at you it turned out', which is how Russians say 'you managed it'. Max suddenly switches to the formal 'you'."),
    (7, None, "'And now we can rest a little.' 'Mozhno' is the handy word for 'it's allowed' or 'we can'. 'Otdokhnut' is 'to have a rest'."),
    (8, None, "'Who wants to have some fun?' 'Povesilitsya' is 'to enjoy oneself', and it's from 'veselye', fun. The 'sya' at the end makes it 'amuse oneself'."),
    (9, None, "'I do.' Sasha answers with just 'ya khochu', 'I want', and leaves out anything else. Russians answer a question by repeating its verb, so there is no word for 'yes' needed."),
    (10, None, "'Then let us go outside with me.' 'Na ulitsu' is 'onto the street', which is how Russians say 'outside'. 'Poydyom' is 'let's go', and 'so mnoy' is 'with me'."),
    (11, None, "'Wait, I will just take off my apron.' 'Snimu' is 'I will take off', and the thing you take off is the apron, 'fartuk'. 'Svoy' means 'my own', which Russians like to add."),
]
