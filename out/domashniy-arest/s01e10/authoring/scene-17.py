# Authoring module for domashniy-arest-s01e10-scene-17.
ID = 'domashniy-arest-s01e10-scene-17'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 17
TITLE = 'Выбор фильма  (Choosing a Movie)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест S01E10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = 'Back in the communal apartment, Samsonov nervously tries to pick a good movie for his evening date while Nina comments sarcastically on every choice he makes.'
OPENER = "Now let's see how Samsonov browses movie listings in front of his wife Nina."
TRANSITION = "Let's listen to the comical argument once again from the beginning."
OUTRO = "Samsonov remains determined to take Ilona out despite Nina's teasing remarks. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('samson', 'Так, посмотрим расписание в кино.', "So, let's look at the schedule in the cinema.", [], 'new line'),
    ('samson', 'Вот фильм: Тернистый путь.', 'Here is a movie: A Thorny Path.', [(527, 'Тернистый путь.')], ''),
    ('samson', 'Жанр фильма — тяжёлая драма.', "The film's genre is heavy drama.", [(528, 'Драма.')], 'adapted cue 528'),
    ('samson', 'Эта история рассказывает о женщине.', 'This story tells about a woman.', [(531, 'Эта история рассказывает о женщине')], ''),
    ('samson', 'Женщина борется с тяжёлой болезнью.', 'A woman battles a severe illness.', [(532, 'которая борется с болезнью')], 'adapted cue 532'),
    ('samson', 'Она не хочет забыть любимого.', 'She does not want to forget her beloved.', [(533, 'чтобы не забыть того')], 'adapted cue 533'),
    ('samson', 'Мрачняк какой-то, не пойдёт.', "Kind of a downer, won't do.", [(535, 'Мрачняк какой-то.')], 'adapted cue 535'),
    ('samson', 'О, вот новая комедия!', 'Oh, here is a new comedy!', [(536, 'О, бабушка нова.'), (537, 'Комедия.')], 'adapted cues 536 and 537'),
    ('samson', 'Наверное, это очень смешно.', 'Probably this is very funny.', [(540, 'Смешно, наверное.')], 'adapted cue 540'),
    ('nina', 'Там никакой романтики нет!', 'There is no romance in it at all!', [(542, 'И романтики на ней никакой.')], 'adapted cue 542'),
    ('nina', 'Зачем ты вообще ведёшь её в кино?', 'Why are you even taking her to the movies?', [(543, 'Да нафига тебе ее вообще в кино-то везти?')], 'adapted cue 543'),
    ('nina', 'Вы что, маленькие подростки?', 'What are you, little teenagers?', [(544, 'Подростки, что ли?')], 'adapted cue 544'),
    ('samson', 'Ты сама сказала добиваться женщины!', 'You yourself said to court a woman!', [(545, 'Ты же сама сказала добиваться.')], 'adapted cue 545'),
    ('samson', 'Вот я и добиваюсь.', "So that's what I'm doing.", [(546, 'Вот я добиваюсь.')], ''),
    ('nina', 'Лучше бы ты дома посуду помыл.', 'You would do better to wash the dishes at home.', [], 'new line'),
]
WALK = [
    (1, None, "'Here is a movie: A Thorny Path.' Samsonov reads the first movie title from the local cinema guide."),
    (3, None, "'This story tells about a woman.' The verb takes the preposition and location case to describe the subject."),
    (6, None, "'Kind of a downer, won't do.' The colloquial word describes a grim or depressing movie plot."),
    (10, None, "'Why are you even taking her to the movies?' Nina questions the childish choice of a cinema date."),
    (12, None, "'You yourself said to court a woman!' Samsonov throws Nina's own advice back at her."),
]
