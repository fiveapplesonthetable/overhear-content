# Authoring module for domashniy-arest-s01e10-scene-33.
ID = 'domashniy-arest-s01e10-scene-33'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 33
TITLE = 'Я отказываюсь от проекта  (I Am Dropping the Project)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'dean': 'Эдуард Владимирович', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = "Unwilling to profit at the expense of impoverished colleagues, she firmly announces the immediate cancellation of her project. In response, the terrified dean makes a frantic confession about the violent blackmail he faces behind the scenes. Let's listen to their heated exchange in Russian first; don't worry about catching every word."
OPENER = 'Let us walk through this intense academic confrontation step by step to examine each phrase.'
TRANSITION = 'Now let us listen to the complete office argument once more, noting the emotional desperation.'
OUTRO = "Marina stands firm on her moral principles despite Eduard's panic about mysterious dangerous figures. Superb progress following this dramatic Russian confrontation. See you next time!"
CLOSING = ('marina', 'Пока!')
STORY = [
    ('marina', 'Эдуард Валентинович, что здесь происходит?', 'Eduard Valentinovich, what is going on here?', [(1008, 'Что происходит')], 'adapted cue 1008'),
    ('marina', 'Почему вы обижаете наших сотрудников?', 'Why are you mistreating our staff?', [(1009, 'ущемляете сотрудников')], 'simplified cue 1009'),
    ('dean', 'Их зарплаты пошли на ваш проект.', 'Their salaries went toward your project.', [(1010, 'Потому что их зарплаты пошли'), (1011, 'на ваш проект')], 'combined cues 1010-1011'),
    ('marina', 'Значит, не будет никакого проекта!', 'Then there will be no project!', [(1012, 'Значит, не будет никакого проекта')], 'verbatim cue 1012'),
    ('marina', 'Я полностью отказываюсь от него.', 'I completely drop it.', [(1012, 'Я отказываюсь от него')], 'adapted cue 1012'),
    ('dean', 'Стойте! Что значит отказываетесь?', 'Wait! What do you mean you drop it?', [(1013, 'Стойте! Что значит отказываюсь')], 'adapted cue 1013'),
    ('dean', 'Вы должны делать этот проект!', 'You must do this project!', [(1014, 'Вы должны делать этот проект')], 'verbatim cue 1014'),
    ('marina', 'Я ничего не должна другим людям!', 'I owe nothing to other people!', [(1015, 'Ничего я не должна за счет других людей')], 'simplified cue 1015'),
    ('dean', 'Подождите! Иначе меня просто убьют!', 'Wait! Otherwise they will simply kill me!', [(1016, 'Да ждите'), (1018, 'иначе меня'), (1019, 'убьют')], 'combined cues 1016-1019'),
    ('marina', 'Кто вас убьёт? Вы шутите?', 'Who will kill you? Are you joking?', [], 'added skeptical question'),
    ('dean', 'Меня бьют буквально каждый день!', 'They beat me literally every day!', [(1020, 'Меня бьют каждый день')], 'expanded cue 1020'),
    ('dean', 'Два огромных и страшных человека!', 'Two huge and scary men!', [(1021, 'Два таких здоровенных')], 'adapted cue 1021'),
    ('marina', 'Это ваши проблемы, а не мои.', 'These are your problems, not mine.', [], 'added firm refusal'),
    ('marina', 'Я не буду работать за чужие деньги.', "I will not work for someone else's money.", [], 'added moral stance'),
]
WALK = [
    (0, None, "'Eduard Valentinovich, what is going on here?' Storming into the dean's office, Marina demands an explanation."),
    (1, None, "'Why are you mistreating our staff?' She confronts him directly over the slashed faculty paychecks."),
    (2, None, "'Their salaries went toward your project.' Eduard admits it plainly, as if robbing the staff were a romantic gesture."),
    (3, None, "'Then there will be no project!' Without hesitation, she kills her own dream project on the spot."),
    (4, None, "'I completely drop it.' Marina wants nothing to do with money taken from her colleagues."),
    (5, None, "'Wait! What do you mean you drop it?' Panic hits Eduard's voice as she turns to leave."),
    (6, None, "'You must do this project!' Suddenly the polite suitor sounds desperate and frantic."),
    (7, None, "'I owe nothing to other people!' In the original line she refuses to do anything at other people's expense."),
    (8, None, "'Wait! Otherwise they will simply kill me!' Cornered, the dean finally blurts out why he is so terrified."),
    (9, None, "'Who will kill you? Are you joking?' Thinking it is just another pathetic excuse, she doesn't believe him."),
    (10, None, "'They beat me literally every day!' That explains the mysterious \"nut allergy\" bruises on his face."),
    (11, None, "'Two huge and scary men!' Those two thugs sent by Arkady have been shaking him down behind the scenes to keep Marina happy."),
    (12, None, "'These are your problems, not mine.' Coldly, she refuses to be blackmailed into taking stolen wages."),
    (13, None, "'I will not work for someone else's money.' Meanwhile, all the clues are starting to point back to Arkady's meddling."),
]
