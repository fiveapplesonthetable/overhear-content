# Authoring module for domashniy-arest-s01e08-scene-02.
ID = 'domashniy-arest-s01e08-scene-02'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 2
TITLE = 'Внук полицая  (Grandson of a Collaborator)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'pasha': 'Паша', 'slavik': 'Славик'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "In our last scene, a wartime flashback revealed that Ivan Samsonov's grandfather was accused of collaborating with the enemy during the war. Now in the mayor's office, acting mayor Pasha Osipenko and his media assistant Slava prepare a devastating campaign video to destroy Samsonov's chances in the upcoming televised mayoral debate. Let's listen to the scene in Russian first; don't worry about catching every word."
OPENER = "Now let's examine Pasha Osipenko's campaign speech line by line. Pasha faces the video camera with a dramatic frown."
TRANSITION = "Now let's listen to the entire smear video rehearsal again in Russian."
OUTRO = 'With the debate only hours away, Pasha is convinced this video will destroy Samsonov once and for all. See you next time!'
CLOSING = ('pasha', 'Пока!')
STORY = [
    ('pasha', 'Вы посмотрите, до чего мы докатились!', 'Just look at what we have come to!', [(30, 'Вы посмотрите, до чего мы докатились')], ''),
    ('pasha', 'Внук полицая рвётся во власть!', 'The grandson of a collaborator is clawing his way into power!', [(31, 'Внук полицая'), (31, 'рвется во власть')], ''),
    ('pasha', 'И это в нашем любимом городе!', 'And that is in our beloved city!', [(32, 'И это все в нашем'), (32, 'любимом'), (32, 'городе')], ''),
    ('slavik', 'Но ведь внук за деда не отвечает.', 'But after all, a grandson is not responsible for his grandfather.', [(33, 'Но ведь внук за деда не отвечает')], ''),
    ('pasha', 'Так-то оно так! Но яблоко от яблони недалеко падает.', 'That may be so! But the apple does not fall far from the tree.', [(34, 'Так-то оно так'), (35, 'яблоко от яблони')], "'недалеко падает' added to complete the Russian proverb"),
    ('pasha', 'Это ведь вопрос воспитания. Кого может воспитать предатель?', 'It is a question of upbringing, after all. Whom can a traitor raise?', [(36, 'вопрос воспитания'), (37, 'кого может воспитать')], ''),
    ('pasha', 'Только человека, похожего на себя!', 'Only a person similar to himself!', [(37, 'себе подобного')], ''),
    ('pasha', 'Вот кандидат Самсонов выбросил человека в окно!', 'Look, candidate Samsonov threw a man out the window!', [(38, 'кандидат Самсонов'), (39, 'Выбросил человека в окно')], ''),
    ('slavik', 'Бывшего мэра, взяточника Аникеева?', 'The former mayor, the bribe-taker Anikeyev?', [(40, 'Бывшего мэра'), (40, 'взяточника')], "'Аникеева' added for clarity"),
    ('pasha', 'Не важно! Он человека просто выбросил в окно!', "It doesn't matter! He simply threw a human being out the window!", [(41, 'Не важно'), (41, 'человека просто'), (41, 'в окно')], ''),
    ('pasha', 'На плече татуировка десантника.', 'On his shoulder is a paratrooper tattoo.', [(42, 'татуировка ВДВ')], "abbreviation ВДВ replaced with 'десантника'"),
    ('pasha', 'А дети всё это снимают на телефон.', 'And the children film all of this on a phone.', [(43, 'А дети его все это снимают')], "'на телефон' added"),
    ('pasha', 'И вся его семья радуется!', 'And his whole family is thrilled!', [(44, 'И вся семья радуется')], ''),
    ('pasha', 'Это получается какая-то странная семейка!', 'It turns out to be quite a strange little family!', [(45, 'какая-то'), (45, 'семейка-то получается')], 'softened phrasing'),
    ('pasha', 'Посмотрим, придёт ли этот кандидат на дебаты!', 'We will see whether this candidate comes to the debate!', [(46, 'Посмотрим, хватит ли у этого кандидата в мэры'), (46, 'явиться на дебаты')], ''),
]
WALK = [
    (0, None, "'Just look at what we have come to!' Pasha puts on his best outraged voice for the camera, using an everyday idiom that literally means 'rolled all the way down to this point'."),
    (1, None, "'The grandson of a collaborator is clawing his way into power!' He paints his rival as a ruthless climber trying to force his way into the mayor's chair."),
    (2, None, "'And that is in our beloved city!' Adding 'in our beloved city' makes the supposed scandal sound like a personal insult to every voter."),
    (3, None, "'But after all, a grandson is not responsible for his grandfather.' Slava raises the obvious fair point: you cannot blame a man for what his grandfather did in the war."),
    (4, None, "'That may be so! But the apple does not fall far from the tree.' Pasha cites the classic proverb about family inheritance."),
    (5, None, "'It is a question of upbringing, after all. Whom can a traitor raise?' Pasha pivots straight to family upbringing, asking a loaded question designed to smear Ivan."),
    (6, None, "'Only a person similar to himself!' Pasha argues that values are passed down directly from parent to child."),
    (7, None, "'Look, candidate Samsonov threw a man out the window!' He brings up Samsonov's notorious kitchen brawl with Arkady."),
    (8, None, "'The former mayor, the bribe-taker Anikeyev?' Slava cautiously reminds him who the victim actually was."),
    (9, None, "'It doesn't matter! He simply threw a human being out the window!' Pasha brushes the objection aside for maximum drama."),
    (10, None, "'On his shoulder is a paratrooper tattoo.' He points to the footage of Ivan's bare shoulder as if a paratrooper tattoo were proof of violent tendencies."),
    (11, None, "'And the children film all of this on a phone.' To make it sound even worse, Pasha highlights that the kids were standing right there filming the brawl."),
    (12, None, "'And his whole family is thrilled!' In Pasha's telling, the whole household was cheering on the defenestration."),
    (13, None, "'It turns out to be quite a strange little family!' He tacks a little suffix onto the word for 'family' so it comes out sounding like 'that weird little clan'."),
    (14, None, "'We will see whether this candidate comes to the debate!' The little word 'li' turns his closing taunt into a challenge: let's see if Samsonov even dares show up."),
]
