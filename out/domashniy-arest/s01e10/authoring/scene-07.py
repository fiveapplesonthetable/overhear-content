# Authoring module for domashniy-arest-s01e10-scene-07.
ID = 'domashniy-arest-s01e10-scene-07'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 7
TITLE = 'Наблюдательное оборудование  (Surveillance Equipment)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'lavrov': 'Лавров', 'lyova': 'Лёва'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = "In this short scene, agent Sokolov prepares for his surveillance assignment outside Anikeyev's former home. When he asks his partner Anatoly for professional surveillance equipment, he is told that his own two eyes are more than enough. Noticing a bottle on the table, Sokolov realizes what his colleagues plan to do in his absence. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine Sokolov's comedic briefing line by line. Sokolov discovers what equipment he gets for surveillance."
TRANSITION = "Now let's listen to Anatoly and Sokolov's conversation once more without pauses."
OUTRO = 'Equipped only with his own eyes, Sokolov heads out to the cold stakeout. See you next time!'
CLOSING = ('lavrov', 'Пока!')
STORY = [
    ('lyova', 'Я прямо сейчас должен идти?', 'Must I go right now?', [(211, 'Прямо на работе')], ''),
    ('lavrov', 'Да, Соколов, именно сейчас.', 'Yes, Sokolov, right now.', [], 'Anatoly confirms the immediate order'),
    ('lyova', 'А что у меня из оборудования?', 'And what equipment do I have?', [(213, 'А что у меня из наблюдательного оборудования')], ''),
    ('lavrov', 'Твои собственные глаза!', 'Your own eyes!', [(214, 'Глаза')], ''),
    ('lyova', 'И это всё моё оборудование?', 'And is that all my equipment?', [], 'Sokolov expresses skepticism'),
    ('lavrov', 'Этого тебе вполне достаточно.', 'That is quite enough for you.', [], 'Anatoly dismisses complaints'),
    ('lyova', 'А что это у вас на столе?', 'And what is that on your table?', [(215, 'А вы что тут')], ''),
    ('lyova', 'Вы что, пить алкоголь собрались?', 'Are you planning to drink alcohol?', [(215, 'пить собрались')], ''),
    ('lavrov', 'Ну вот, твои глаза отлично работают!', 'Well look, your eyes work excellently!', [(216, 'наблюдательное оборудование функционирует')], ''),
    ('lavrov', 'Наблюдательное оборудование в полном порядке.', 'The surveillance equipment is in full working order.', [(216, 'Ну вот, наблюдательное оборудование функционирует')], ''),
    ('lyova', 'Вы будете отдыхать, а я мёрзнуть?', 'You will relax while I freeze?', [], 'Sokolov resents the unfair assignment'),
    ('lavrov', 'Приказ начальника надо выполнять.', "The chief's order must be carried out.", [], 'Anatoly appeals to authority'),
    ('lavrov', 'Иди и действуй, Соколов!', 'Go and take action, Sokolov!', [(217, 'Действуй, Соколов')], ''),
    ('lyova', 'Понял, уже иду наблюдать.', 'Understood, I am already going to observe.', [], 'Sokolov resigns to his task'),
]
WALK = [
    (0, None, "'Must I go right now?' Hoping to stall for a few minutes, Sokolov double-checks whether the order means this very second."),
    (1, None, "'Yes, Sokolov, right now.' Anatoly wants him out of the room immediately and leaves no wiggle room."),
    (2, None, "'And what equipment do I have?' Expecting high-tech spy gear, he asks what tools he gets for the stakeout."),
    (3, None, "'Your own eyes!' That is the whole kit: no binoculars, no cameras, just his own two eyes."),
    (4, None, "'And is that all my equipment?' Lyova cannot believe the agency is sending him out empty-handed."),
    (5, None, "'That is quite enough for you.' With a deadpan face, Lavrov insists that a pair of eyes is plenty for this job."),
    (6, None, "'And what is that on your table?' Then Sokolov spots a bottle sitting right on the desk."),
    (7, None, "'Are you planning to drink alcohol?' Suddenly it clicks: his colleagues are clearing him out so they can pour a drink."),
    (8, None, "'Well look, your eyes work excellently!' Turning the complaint into a joke, Anatoly congratulates him on his sharp eyesight."),
    (9, None, "'The surveillance equipment is in full working order.' Calling Lyova's eyes \"surveillance equipment\" in stiff official language makes the teasing even funnier."),
    (10, None, "'You will relax while I freeze?' While the senior officers stay warm inside with a bottle, the junior guy gets the freezing street corner."),
    (11, None, "'The chief's order must be carried out.' Whenever he needs to end an argument, Lavrov hides behind the boss's authority."),
    (12, None, "'Go and take action, Sokolov!' Two brisk commands usher the reluctant agent toward the exit."),
    (13, None, "'Understood, I am already going to observe.' Defeated, he trudges out into the cold to watch the house."),
]
