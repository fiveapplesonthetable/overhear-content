# Authoring module for domashniy-arest-s01e09-scene-28.
ID = 'domashniy-arest-s01e09-scene-28'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 9
SCENE = 28
TITLE = 'В аквапарк за счёт ФСБ  (To the Water Park on the FSB)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'agent': 'Сотрудник', 'commander': 'Командир'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.09'
SOURCE_FILE = 'sources/domashniy-arest/s01/e09.ru.dual.srt'
INTRO = "Back in the town, special operations officers launch a sudden raid on a suspicious daycare facility. The commander decides to clear the premises by treating the bewildered children to a trip to the water park, before breaking down the heavy internal doors. Let's listen to their brief exchange in Russian first; don't worry about catching every word."
OPENER = 'Let us walk through this intense and humorous scene together, step by step, to understand each phrase.'
TRANSITION = 'Now let us listen to the complete exchange once more, paying attention to the decisive military orders.'
OUTRO = 'The children are happily dispatched to the water park, while the officers prepare to enter the inner facility. Well done following this rapid tactical dialogue in Russian. See you next time!'
CLOSING = ('commander', 'Пока!')
STORY = [
    ('agent', 'Товарищ командир, здание полностью окружено.', 'Comrade commander, the building is completely surrounded.', [], 'added operational opening'),
    ('commander', 'Отлично. Быстро заходим внутрь.', 'Excellent. We go inside quickly.', [], 'added commander order'),
    ('agent', 'Здесь в коридоре маленькие дети!', 'Here in the corridor are small children!', [], 'added children sighting'),
    ('commander', 'Так, детей сразу в автобус!', 'Right, put the children into the bus immediately!', [(751, 'Так, детей в автобус')], 'adapted cue 751'),
    ('commander', 'Отвезите их в аквапарк.', 'Take them to the water park.', [(751, 'в аквапарк')], 'adapted cue 751'),
    ('commander', 'Всё за счёт ФСБ!', 'Everything is on the FSB!', [(751, 'за счет ФСБ')], 'verbatim cue 751 with yo'),
    ('agent', 'У них же плавочек нет!', 'But they do not have swimsuits!', [(752, 'У них же плавочек нет')], 'verbatim cue 752'),
    ('commander', 'Ничего страшного.', 'No big deal.', [(753, 'Ничего страшного')], 'verbatim cue 753'),
    ('commander', 'На берегу спокойно посидят.', 'They will sit quietly on the shore.', [(753, 'на берегу посидят')], 'adapted cue 753'),
    ('agent', 'Понял. Я посажу их в автобус.', 'Understood. I will put them into the bus.', [(754, 'Так')], 'expanded cue 754'),
    ('agent', 'А что делать с этой дверью?', 'And what should we do with this door?', [], 'added breach question'),
    ('commander', 'Ну-ка, дай кувалду!', 'Come on, hand me the sledgehammer!', [(755, 'Ну-ка, дай кувалду')], 'verbatim cue 755'),
    ('commander', 'Мы сейчас откроем этот вход.', 'We will open this entrance right now.', [], 'added breach command'),
]
WALK = [
    (0, None, "'Comrade commander, the building is completely surrounded.' The subordinate reports the perimeter status clearly."),
    (1, None, "'Excellent. We go inside quickly.' The commander gives the order to storm the premises without delay."),
    (2, None, "'Here in the corridor are small children!' Bursting into the hallway in full tactical gear, the operative freezes at the sight of toddlers."),
    (3, None, "'Right, put the children into the bus immediately!' Thinking on his feet, the commander orders his men to load the kids onto a bus right away."),
    (4, None, "'Take them to the water park.' To keep the kids happy and out of the way, he tells the team to take them to the water park."),
    (5, None, "'Everything is on the FSB!' Literally 'at the expense of,' he grandly declares that the security service is picking up the tab."),
    (6, None, "'But they do not have swimsuits!' The operative points out a practical snag: none of the toddlers packed swim trunks."),
    (7, None, "'No big deal.' Literally 'nothing terrible,' the commander shrugs off the missing swimwear as a minor detail."),
    (8, None, "'They will sit quietly on the shore.' He figures the kids can just sit nicely by the edge of the pool."),
    (9, None, "'Understood. I will put them into the bus.' Following orders, the agent heads off to herd the children onto the bus."),
    (10, None, "'And what should we do with this door?' Pointing to a heavy locked door down the hall, he asks how they should handle it."),
    (11, None, "'Come on, hand me the sledgehammer!' Done with subtlety, the commander calls for a sledgehammer."),
    (12, None, "'We will open this entrance right now.' He prepares to smash the locked entrance open the old-fashioned way."),
]
