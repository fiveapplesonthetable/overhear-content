# Authoring module for domashniy-arest-s01e11-scene-34.
ID = 'domashniy-arest-s01e11-scene-34'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 11
SCENE = 34
TITLE = 'Разборка на кухне  (Showdown in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'danya': 'Даня', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 11'
SOURCE_FILE = 'sources/domashniy-arest/s01/e11.ru.dual.srt'
INTRO = "In the communal apartment kitchen, Ivan Samsonov's jealousy boils over into explosive fury. He bitterly accuses Nina of destroying their marriage and memories, before turning his anger onto handsome young lawyer Danya. When Danya talks back, Nina must step in to prevent bloodshed."
OPENER = "Let's explore the tense confrontation as Samsonov faces Nina and Danya in the kitchen."
TRANSITION = "Now let's listen to the heated confrontation in the kitchen once more."
OUTRO = "Samsonov glares with simmering fury, but Nina's resolute protection keeps the peace intact. See you next time!"
CLOSING = ('nina', 'Пока!')
STORY = [
    ('samson', 'Ты всё у меня украла!', 'You stole everything from me!', [(1050, 'Ты все у меня украла')], 'exact cue'),
    ('samson', 'Ты украла даже мои воспоминания!', 'You stole even my memories!', [(1051, 'Даже воспоминания')], 'adapted cue'),
    ('nina', 'Ваня, ты сейчас абсолютно не прав.', 'Vanya, you are absolutely wrong right now.', [(1057, 'Ваня, ты сейчас не прав')], 'adapted cue'),
    ('nina', 'Ты сам всё разрушил своими руками!', 'You destroyed everything yourself with your own hands!', [(1058, 'ты сам все разрушил')], 'adapted cue'),
    ('samson', 'Это ты влез в нашу семью!', 'It was you who wormed into our family!', [(1060, 'Это ты влез в нашу семью')], 'exact cue'),
    ('samson', 'Ты всё окончательно испортил, понял?', 'You ruined everything completely, understand?', [(1061, 'Ты все испортил, понял?')], 'adapted cue'),
    ('danya', 'Там уже нечего было портить!', 'There was nothing left to ruin there!', [(1062, 'Там нечего было портить')], 'adapted cue'),
    ('danya', 'От вашей семьи остались одни руины.', 'Only ruins remained of your family.', [(1063, 'Там одни руины остались')], 'adapted cue'),
    ('samson', 'Кого ты сейчас назвал руинами?', 'Who did you just call ruins?', [(1067, 'Ты кого руинами назвал?')], 'adapted cue'),
    ('samson', 'Ты так хочешь со мной разговаривать?', 'Is that how you want to talk with me?', [(1073, 'Ты так хочешь разговаривать?')], 'adapted cue'),
    ('nina', 'Отойди немедленно от него, Ваня!', 'Back off from him immediately, Vanya!', [(1081, 'Отойди.')], 'expanded cue'),
    ('nina', 'Если тронешь его, я ударю тебя!', 'If you touch him, I will hit you!', [(1077, 'Если ты его пальцем')], 'polite adaptation of cue'),
    ('samson', 'Она спасает тебя от больницы!', 'She is saving you from the hospital!', [(1080, 'Она тебя от реанимации спасает.')], 'adapted cue'),
    ('nina', 'Я защищаю человека от твоей злости.', 'I am protecting a human being from your anger.', [], "Nina's moral stance"),
]
WALK = [
    (0, None, "'You stole everything from me!' Fresh out of the clinic and still wired, Samson corners Nina and Danya in the kitchen."),
    (1, None, "'You stole even my memories!' Remember the nineties cafe flashback that opened the episode—those memories are what hurt him most."),
    (2, None, "'Vanya, you are absolutely wrong right now.' Nina stays calm and uses his warm home name \"Vanya\" to try to ground him."),
    (3, None, "'You destroyed everything yourself with your own hands!' Years of neglect and stubbornness broke their marriage long before Danya showed up."),
    (4, None, "'It was you who wormed into our family!' Turning on Danya, Ivan uses the blunt word \"vlez\"—literally \"climbed in\" where you don't belong."),
    (5, None, "'You ruined everything completely, understand?' Adding \"ponyal?\"—\"got it?\"—at the end of a sentence is a classic street challenge."),
    (6, None, "'There was nothing left to ruin there!' Instead of backing down, the young lawyer fires right back."),
    (7, None, "'Only ruins remained of your family.' Calling their marriage \"only ruins\" is accurate, cruel, and guaranteed to start a fight."),
    (8, None, "'Who did you just call ruins?' Ivan takes the metaphor literally and steps in with his fists clenched."),
    (9, None, "'Is that how you want to talk with me?' That quiet question is the last warning before punches fly."),
    (10, None, "'Back off from him immediately, Vanya!' Nina throws herself between the two men before the kitchen turns into a boxing ring."),
    (11, None, "'If you touch him, I will hit you!' Nobody in the apartment doubts for a second that Nina would make good on that threat."),
    (12, None, "'She is saving you from the hospital!' In the original Russian, Ivan says \"intensive care\" rather than just \"the hospital\"."),
    (13, None, "'I am protecting a human being from your anger.' However she feels about either man, she refuses to let Ivan turn violent."),
]
