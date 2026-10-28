# Authoring module for domashniy-arest-s01e08-scene-01.
ID = 'domashniy-arest-s01e08-scene-01'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 1
TITLE = 'Допрос в сорок втором  (Interrogation in Forty-Two)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'captain': 'Капитан', 'partisan': 'Партизан', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Welcome to Episode Eight of Domashniy Arest, the Russian comedy about disgraced mayor Arkady Anikeyev living under house arrest in his old communal apartment. We open with a dramatic black-and-white wartime flashback to 1942, where a captured young partisan boy is being interrogated in a basement by a German captain and local collaborator Pavel Samsonov, Ivan Samsonov's grandfather. Let's listen in Russian first."
OPENER = "Now let's examine the wartime interrogation line by line. The German officer stands over the young partisan in the dim room."
TRANSITION = "Now let's listen to the entire wartime scene again in Russian."
OUTRO = 'This dark family history will soon become a weapon in the modern mayoral campaign. See you next time!'
CLOSING = ('partisan', 'Пока!')
STORY = [
    ('captain', 'В последний раз спрашиваю! Говори, где партизаны!', 'I am asking you one last time! Tell me where the partisans are!', [(1, 'В последний раз спрашиваю, говори, где партизаны')], ''),
    ('captain', 'Ничего не говорит. Самсонов, разберись с ним!', 'He is not saying anything. Samsonov, deal with him!', [(8, 'Ничего не говорит, разберись')], "cues 4-7 (Hans's report) narrated"),
    ('pasha', 'Сейчас заговорит! В глаза мне смотри!', 'He will talk soon! Look me in the eyes!', [(9, 'Сейчас заговорит'), (12, 'Глаза смотри')], ''),
    ('pasha', 'Говори, где дядька? Где командир?', 'Speak, where is your uncle? Where is the commander?', [(13, 'Говори, где дядька'), (14, 'Где дядька')], ''),
    ('partisan', 'Ничего я тебе не скажу, предатель!', "I won't tell you anything, traitor!", [(15, 'Ничего я тебе не скажу, предатель')], ''),
    ('partisan', 'Потомки тебя проклянут!', 'Your descendants will curse you!', [(16, 'Потомки тебя проклянут')], ''),
    ('captain', 'Что он сказал?', 'What did he say?', [(17, 'Что он сказал')], ''),
    ('pasha', 'Мои потомки будут ездить на немецких машинах.', 'My descendants will be driving German cars.', [(18, 'Мои потомки будут ездить на немецких машинах')], ''),
    ('pasha', 'И будут пить немецкое пиво! Понял?', 'And they will drink German beer! Understood?', [(19, 'и пить немецкое пиво'), (21, 'Понял')], 'cue 20 insult omitted'),
    ('partisan', 'Не будет такого никогда!', 'That will never happen!', [(22, 'Не будет такого никогда')], ''),
    ('partisan', 'Мы победим!', 'We will win!', [], 'German slogan in cue 23 replaced with clean Russian'),
    ('captain', 'Какой храбрый мальчик! Ты что творишь, Самсонов?', 'What a brave boy! What are you doing, Samsonov?', [(24, 'Какой храбрый мальчик'), (25, 'Ты что творишь, Самсонов')], ''),
    ('captain', 'Нам надо узнать информацию. Допроси его спокойно.', 'We need to find out information. Interrogate him calmly.', [(25, 'Нам надо узнать информацию'), (26, 'Допроси его')], "'спокойно' added"),
    ('pasha', 'Где дядька? Отвечай!', 'Where is your uncle? Answer!', [(28, 'Где дядька')], ''),
    ('partisan', 'Ничего я тебе не скажу, Павел!', "I won't tell you anything, Pavel!", [(29, 'Ничего я тебе не скажу, Павел')], ''),
]
WALK = [
    (0, 'В последний раз спрашиваю!', "'I am asking you one last time!' The German officer is out of patience as he stands over the captured boy."),
    (0, 'Говори, где партизаны!', "'Tell me where the partisans are!' He barks a blunt order demanding the location of the resistance unit."),
    (1, None, "'He is not saying anything. Samsonov, deal with him!' The captain calls in local collaborator Pavel Samsonov to take over."),
    (2, None, "'He will talk soon! Look me in the eyes!' In this moment, Samsonov steps up and demands that the boy look at him."),
    (3, None, "'Speak, where is your uncle? Where is the commander?' In wartime colloquial speech, the Russian word refers to the boy's elder relative or detachment leader."),
    (4, None, "'I won't tell you anything, traitor!' Russian stacks two negatives here — literally 'nothing to you I will not say' — to make the refusal hit harder."),
    (5, None, "'Your descendants will curse you!' Even with his hands tied, the young partisan looks his captor in the eye and warns him what history will think."),
    (6, None, "'What did he say?' The German captain does not understand Russian well and asks for a translation."),
    (7, None, "'My descendants will be driving German cars.' Pavel Samsonov laughs off the curse and brags that his grandchildren will live in German luxury."),
    (8, None, "'And they will drink German beer! Understood?' In this moment, Samsonov sneers at the boy with cynical contempt."),
    (9, None, "'That will never happen!' Literally 'there will not be such a thing ever'."),
    (10, None, "'We will win!' The brave young boy declares his faith in victory."),
    (11, None, "'What a brave boy! What are you doing, Samsonov?' The captain intervenes when Samsonov loses his temper."),
    (12, None, "'We need to find out information. Interrogate him calmly.' Literally, 'to us it is necessary to find out information' — the officer wants answers, not a beating."),
    (13, None, "'Where is your uncle? Answer!' In response, Samsonov repeats his demand one more time."),
    (14, None, "'I won't tell you anything, Pavel!' The boy stands firm and addresses the collaborator by his first name."),
]
