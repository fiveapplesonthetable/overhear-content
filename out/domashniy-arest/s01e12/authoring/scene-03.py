# Authoring module for domashniy-arest-s01e12-scene-03.
ID = 'domashniy-arest-s01e12-scene-03'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 12
SCENE = 3
TITLE = 'Стена монастыря  (The Monastery Wall)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'builder': 'Строитель', 'professor': 'Профессор'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.12'
SOURCE_FILE = 'sources/domashniy-arest/s01/e12.ru.dual.srt'
INTRO = "In the present day, a university history professor lectures his students before an ancient stone wall. This wall is the only surviving remnant of the medieval monastery burned down eight hundred years ago. Suddenly, a construction crew arrives with orders to tear down the historic monument to build a shopping center. Let's listen to their confrontation in Russian first."
OPENER = "Now let's examine the professor and builder's dispute line by line."
TRANSITION = "Now let's listen to the monastery wall confrontation again without interruption."
OUTRO = "Outraged citizens protest against the demolition ordered by the mayor's administration. See you next time!"
CLOSING = ('professor', 'Пока!')
STORY = [
    ('professor', 'Эта стена — наш главный исторический памятник.', 'This wall is our main historical monument.', [(40, 'Эта стена – это настоящий памятник')], 'adapted'),
    ('professor', 'Она осталась от древнего монастыря.', 'It remained from an ancient monastery.', [(41, 'осталось от сожженного татарами монастыря')], 'adapted'),
    ('professor', 'Здесь была написана великая летопись.', 'A great chronicle was written here.', [(39, 'подлинник повести временных лет')], 'adapted'),
    ('arkady', 'Каждый студент должен помнить историю.', 'Every student must remember history.', [(42, 'привожу своих студентов')], 'adapted'),
    ('professor', 'Что вы здесь делаете, гражданин?', 'What are you doing here, citizen?', [(50, 'Вы что здесь делаете')], ''),
    ('builder', 'Я собираюсь сносить эту старую стену.', 'I am going to demolish this old wall.', [(53, 'Стену сносить буду')], 'adapted'),
    ('professor', 'Как вы можете разрушать историю?', 'How can you destroy history?', [(56, 'Как строить? Да это же')], 'adapted'),
    ('builder', 'Мы построим здесь большой торговый центр.', 'We will build a big shopping center here.', [(55, 'Торговый центр тут буду строить')], 'adapted'),
    ('professor', 'Это же наше национальное достояние!', 'This is our national heritage!', [(57, 'Это же историческое достояние')], 'adapted'),
    ('builder', 'У меня есть официальное разрешение на снос.', 'I have official permission for demolition.', [], 'new'),
    ('builder', 'Все ваши вопросы задавайте в мэрию!', "Address all your questions to the mayor's office!", [(60, 'все вопросы в мэрию')], 'adapted'),
    ('professor', 'Это настоящий произвол городских властей!', 'This is true arbitrariness by city authorities!', [(64, 'Беспредел')], 'adapted'),
    ('professor', 'Мэр города разрушает наши памятники!', 'The city mayor is destroying our monuments!', [(65, 'Мэр-вандал')], 'adapted'),
    ('builder', 'Отойдите в сторону от техники!', 'Step aside away from the equipment!', [(62, 'Вот идите, давайте')], 'adapted'),
]
WALK = [
    (0, None, "'This wall is our main historical monument.' Eight centuries after the raid, the professor stands before the one piece of stonework that survived the fire."),
    (1, None, "'It remained from an ancient monastery.' That little survival is the whole point of his lecture: the wooden buildings burned, but this wall stayed."),
    (2, None, "'A great chronicle was written here.' He connects the bricks in front of the students to the famous medieval manuscript from the opening scene."),
    (3, None, "'Every student must remember history.' Arkady chimes in piously from the side, playing the cultured academic now that he teaches at the university."),
    (4, None, '\'What are you doing here, citizen?\' Calling a stranger "citizen" in Russian isn\'t friendly—it is the stiff, official word you use when someone is trespassing.'),
    (5, None, "'I am going to demolish this old wall.' To the hard-hatted contractor, eight hundred years of history is just an old brick obstacle."),
    (6, None, '\'How can you destroy history?\' The professor is appalled, though notice he still keeps the polite plural "vy" even while shouting.'),
    (7, None, "'We will build a big shopping center here.' Classic modern Russian satire: tear down a twelfth-century relic to put up another mall."),
    (8, None, '\'This is our national heritage!\' Slipping the tiny word "zhe" after "this" adds the outrage: "this is our national heritage, don\'t you see!"'),
    (9, None, "'I have official permission for demolition.' Paper beats history in bureaucracy, and the foreman waves his permit like a shield."),
    (10, None, "'Address all your questions to the mayor's office!' He didn't make the decision; he is just the guy with the bulldozer pointing up the chain of command."),
    (11, None, '\'This is true arbitrariness by city authorities!\' "Proizvol" is a heavy Russian word for officials doing whatever they please with zero regard for the law.'),
    (12, None, "'The city mayor is destroying our monuments!' Now the blame lands squarely on acting mayor Pasha Osipenko, who signed off on the mall."),
    (13, None, "'Step aside away from the equipment!' Unmoved by the history lesson, the worker tells the crowd to clear the way for the machines."),
]
