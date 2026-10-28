# Authoring module for domashniy-arest-s01e10-scene-30.
ID = 'domashniy-arest-s01e10-scene-30'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 30
TITLE = 'Конкурс поделок  (The Craft Contest)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'caregiver': 'Воспитательница', 'tatyana': 'Татьяна'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = 'Parents and children assemble in the kindergarten hall for the climax of the crafts contest. The kindergarten director and the lead teacher take the stage to praise all the young participants before announcing who took the top prize. Listen to the Russian announcement first, and do not worry about catching every single word.'
OPENER = "Let's examine how the kindergarten director builds suspense line by line."
TRANSITION = 'Now listen to the kindergarten contest announcement once again.'
OUTRO = 'Suspense peaks in the auditorium as the director prepares to reveal the top craft. See you next time!'
CLOSING = ('tatyana', 'Пока!')
STORY = [
    ('tatyana', 'Дорогие родители и дети!', 'Dear parents and children!', [], 'the director welcomes the crowd'),
    ('caregiver', 'Наш конкурс поделок подошёл к концу.', 'Our craft contest has come to an end.', [], 'the teacher steps up'),
    ('tatyana', 'Все наши юные творцы сделали замечательные поделки!', 'All our young creators made wonderful crafts!', [(955, 'Все наши юные творцы'), (956, 'сделали замечательные поделки')], ''),
    ('caregiver', 'Каждая работа была очень интересной.', 'Every work was very interesting.', [], 'she points to the display tables'),
    ('tatyana', 'Выбрать было очень сложно!', 'It was very difficult to choose!', [(957, 'Выбрать было очень сложно')], ''),
    ('caregiver', 'Все ребята очень старались.', 'All the children tried very hard.', [], 'the teacher nods affectionately'),
    ('tatyana', 'Давайте поаплодируем всем нашим участникам!', "Let's give a round of applause to all our participants!", [(958, 'Давайте поаплодируем всем')], ''),
    ('caregiver', 'Они заслужили самые громкие аплодисменты.', 'They deserved the loudest applause.', [], 'the room begins to clap'),
    ('tatyana', 'А теперь наступил долгожданный момент.', 'And now the long-awaited moment has arrived.', [], 'she holds up the sealed envelope'),
    ('tatyana', 'Перед тем, как я объявлю победителя, внимание!', 'Before I announce the winner, your attention!', [(959, 'перед тем, как я объявлю победителя')], ''),
    ('caregiver', 'Кто же занял первое место?', 'Who took first place after all?', [], 'the room falls silent in anticipation'),
    ('tatyana', 'Давайте узнаем имя нашего главного победителя!', "Let's find out the name of our grand winner!", [], 'the director opens the envelope'),
]
WALK = [
    (0, None, "'Dear parents and children!' Standing before the crowded hall, the announcer opens the kindergarten ceremony."),
    (1, None, "'Our craft contest has come to an end.' Literally \"walked up to its end\", a natural Russian phrase for wrapping up an event."),
    (2, None, "'All our young creators made wonderful crafts!' Calling the kindergarteners \"young creators\" gives the little contest grand ceremony."),
    (3, None, "'Every work was very interesting.' She praises the whole table of clay figures before the fixed results are read out."),
    (4, None, "'It was very difficult to choose!' In truth, the choice was made for them by an intimidating phone call."),
    (5, None, "'All the children tried very hard.' \"Rebyata\" is the warm, everyday word teachers use for a group of kids."),
    (6, None, "'Let's give a round of applause to all our participants!' Leading the parents in a round of clapping, she warms up the room."),
    (7, None, "'They deserved the loudest applause.' In Russian, \"applause\" is always plural, just like \"glasses\" or \"scissors\"."),
    (8, None, "'And now the long-awaited moment has arrived.' \"Dolgozhdanny\" welds \"long\" and \"awaited\" into one dramatic word."),
    (9, None, "'Before I announce the winner, your attention!' Holding up the envelope, she stretches out the suspense."),
    (10, None, "'Who took first place after all?' Both teachers pretend to wonder, even though the fix is already in."),
    (11, None, "'Let's find out the name of our grand winner!' Everything is set for little Lyosha's unexpected triumph."),
]
