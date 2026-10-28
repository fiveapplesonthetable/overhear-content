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
INTRO = "Max compliments Sasha on her work and suggests they have some fun. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around Thirst for Fun line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "They sneak out of the kitchen for a quick break. Next time you watch the episode, listen for the Russian expressions for 'to see' and 'new' — you will catch every word right away. See you next time!"
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
    (0, None, "'Sasha, did you see the new beautiful cake?' Max compliments Sasha on the cake. He asks if she saw how beautiful it looks."),
    (1, None, "'Of course, I decorated it myself today.' Sasha proudly takes credit. She mentions she decorated it herself."),
    (2, None, "'It looks simply magnificent.' Max flatters her work. He calls the cake absolutely magnificent."),
    (3, None, "'Thank you, I tried very hard.' Sasha thanks him sincerely. She admits she put a lot of effort into it."),
    (4, None, "'Has the chef already seen your new work?' Max asks about the Chef's reaction. He wonders if the boss noticed her hard work."),
    (5, None, "'Yes, he was very satisfied with me.' Sasha beams with pride. She confirms that the Chef was very happy with her."),
    (6, None, "'And you pulled it off.' Max congratulates her success. He says she really managed to pull it off."),
    (7, None, "'And now we can rest a little.' Sasha feels relieved. She says they can finally take a short break."),
    (8, None, "'Who wants to have some fun?' Max takes the opportunity to flirt. He asks who wants to have some fun."),
    (9, None, "'I do.' Sasha eagerly agrees. She says she definitely wants to have fun."),
    (10, None, "'Then let us go outside with me.' Max invites her outside. He suggests they go out to the street together."),
    (11, None, "'Wait, I will just take off my apron.' Sasha asks him to hold on for a second. She just needs to take off her apron."),
]
