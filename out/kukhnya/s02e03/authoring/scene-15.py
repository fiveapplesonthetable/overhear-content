# Authoring module for kukhnya-s02e03-scene-15.
ID = 'kukhnya-s02e03-scene-15'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 3
SCENE = 15
TITLE = 'Забытый салат  (The Forgotten Salad)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.03'
SOURCE_FILE = 'sources/kukhnya/s02/e03.ru.dual.srt'
INTRO = "In the kitchen, Victoria complains that guests in the dining room have been waiting ages for their salad while Senya is nowhere to be found. Trying to help, Max grabs the bowl sitting on Senya's counter and puts it on the pass, unaware that it contains Senya's sliced leather belt."
OPENER = 'Listen to Victoria and Max looking for the missing salad order in the kitchen.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Thinking they have solved the delay, Max and Victoria accidentally send Senya's leather belt salad out to a guest. Next time you watch the episode, listen for the Russian expressions for 'to say' and 'now' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Макс, скажи, где сейчас Сеня?', 'Max, tell me, where is Senya right now?', [(278, 'Где Сеня?')], ''),
    ('max', 'Он только что вышел из кухни.', 'He just stepped out of the kitchen.', [(278, 'Где Сеня?')], ''),
    ('vika', 'Гости в зале ждут свой заказ!', 'The guests in the hall are waiting for their order!', [(278, 'Там у вас салат уже полдня ждут')], ''),
    ('vika', 'Они ждут этот салат очень долго.', 'They have been waiting for this salad for a very long time.', [(278, 'салат уже полдня ждут')], ''),
    ('max', 'Сеня уже давно приготовил салат.', 'Senya prepared the salad a long time ago.', [(278, 'салат')], ''),
    ('vika', 'Тогда почему блюдо ещё на кухне?', 'Then why is the dish still in the kitchen?', [(279, 'на столик раздачи поставить')], ''),
    ('vika', 'Ну что за странный человек!', 'Well what a strange person!', [(279, 'Что за человек?')], ''),
    ('vika', 'Разве трудно поставить тарелку на стол?', 'Is it really hard to put the plate on the table?', [(279, 'Трудно, что ли, на столик раздачи поставить')], ''),
    ('max', 'Смотри, вот стоит какая-то тарелка.', 'Look, here stands some plate.', [(279, 'на столик')], ''),
    ('vika', 'Наверное, это и есть наш салат.', 'Probably this is our salad.', [(278, 'салат')], ''),
    ('max', 'Давай я быстро отнесу его официанту.', 'Let me quickly take it to the waiter.', [(279, 'поставить')], ''),
    ('vika', 'Да, поставь его скорее на стол!', 'Yes, put it on the table quickly!', [(279, 'на столик раздачи поставить')], ''),
    ('max', 'Готово, теперь гости будут довольны.', 'Done, now the guests will be satisfied.', [(278, 'ждут')], ''),
]
WALK = [
    (0, None, "'Max, tell me, where is Senya right now?' Victoria enters the kitchen looking for the cook."),
    (1, None, "'He just stepped out of the kitchen.' Max explains that Senya left his station a moment ago."),
    (2, None, "'The guests in the hall are waiting for their order!' Victoria stresses that the customers are getting impatient."),
    (3, None, "'They have been waiting for this salad for a very long time.' Vika complains that the table has been waiting ages for their salad."),
    (4, None, "'Senya prepared the salad a long time ago.' Max recalls seeing Senya make a salad earlier."),
    (5, None, "'Then why is the dish still in the kitchen?' When Max says Senya already made it, Vika asks why the bowl is still sitting in the kitchen."),
    (6, None, "'Well what a strange person!' This exclamatory phrase expresses frustration."),
    (7, None, "'Is it really hard to put the plate on the table?' Cooks must place finished dishes on the pass table for the waiters."),
    (8, None, "'Look, here stands some plate.' Max notices a finished salad sitting on Senya's counter."),
    (9, None, "'Probably this is our salad.' Neither of them realizes Senya mixed his leather belt into that bowl."),
    (10, None, "'Let me quickly take it to the waiter.' Trying to be helpful, Max offers to run the salad out to the waiter right now."),
    (11, None, "'Yes, put it on the table quickly!' Victoria tells him to hurry so the waiter can serve it."),
    (12, None, "'Done, now the guests will be satisfied.' Max unwittingly sends the belt salad out to the dining room. Now listen to Victoria and Max in the kitchen again."),
]
