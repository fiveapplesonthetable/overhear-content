# Authoring module for domashniy-arest-s01e05-scene-01.
ID = 'domashniy-arest-s01e05-scene-01'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Авария  (The Crash)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'ilona': 'Илона', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.05'
SOURCE_FILE = 'sources/domashniy-arest/s01/e05.ru.dual.srt'
INTRO = "Welcome back to House Arrest. We open at the crash site as traffic police make drunken Samson breathe into a breathalyser tube, and then cut back to the communal flat where Arkady and Ilona watch the breaking news report in horror. Let's listen in Russian first."
OPENER = "Let's go back through the scene step by step. Outside the damaged building of the Sineozersk Society for the Blind, police officers hold a breathalyser tube up to Samson's face."
TRANSITION = "Now let's hear the whole opening scene again from the start."
OUTRO = "So Samson's test drive has ended inside the wall of the Society for the Blind, and Ilona thinks their campaign for mayor is finished. See you next time!"
CLOSING = ('ilona', 'Пока!')
STORY = [
    ('samson', 'Что я пил? Шипучку!', 'What was I drinking? Fizzy wine!', [(1, 'Что пил'), (3, 'Шипучку')], "police officer's 'Что пил?' echoed by Samson as 'Что я пил?'"),
    ('samson', 'Надо дышать? В трубку дышать?', 'Do I have to breathe? Breathe into the tube?', [(8, 'Надо дышать'), (10, 'В трубку дышать')], "officer's prompts turned into Samson's questions"),
    ('samson', 'Отпустите, пожалуйста! Отпустите меня!', 'Let me go, please! Let me go!', [(11, 'Отпустите, пожалуйста'), (12, 'Отпустите')], "'меня' added"),
    ('samson', 'Три с половиной промилле? У меня семь кредитов!', 'Three and a half per mille? I have seven loans!', [(17, 'Три с половиной промилле'), (18, 'У меня семь кредитов')], "officer's reading (17) echoed by Samson"),
    ('samson', 'Нет, не надо! Дань, ну скажи им!', "No, don't! Danya, come on, tell them!", [(26, 'Нет'), (7, 'Не надо'), (13, 'Дань, ну скажи')], "'им' added; Samson appeals to his lawyer friend Danila Golovkin"),
    ('arkady', 'Смотри новости!', 'Look at the news!', [(37, 'смотри')], 'Arkady points at the television screen'),
    ('arkady', 'У общества слепых произошла страшная авария!', 'A terrible crash happened at the Society for the Blind!', [(40, 'общества слепых'), (41, 'произошла страшная авария')], 'TV news report (40-41) voiced by Arkady watching television'),
    ('arkady', 'На огромной скорости машина врезалась в здание!', 'At huge speed the car crashed into the building!', [(42, 'на огромной скорости'), (43, 'в здании')], "cue 43 garbled 'обрезалась в здании' -> 'машина врезалась в здание'"),
    ('arkady', 'Там начался пожар! Везде пожарные машины и полиция!', 'A fire started there! Fire engines and police are everywhere!', [(44, 'начался пожар'), (44, 'пожарных машин')], 'cue 44 adapted'),
    ('ilona', 'Ну что я тебе скажу, Аркаша? Это полный кошмар!', 'Well, what can I tell you, Arkasha? This is a total nightmare!', [(45, 'ну что я тебе скажу, Аркаша, это полный')], "slang 'полярный лис / песец' replaced with 'кошмар'"),
    ('ilona', 'Вот я дура! Надо было работать на Осипенко.', 'What a fool I am! I should have worked for Osipenko.', [(46, 'вот я дура, надо было работать на Осипенко')], ''),
    ('arkady', 'Тихо, тихо! Ещё не всё потеряно!', 'Easy, easy! Not everything is lost yet!', [(25, 'Тихо, тихо')], 'Arkady tries to calm Ilona down'),
]
WALK = [
    (0, None, "'What was I drinking? Fizzy wine!' The word Samson uses for sparkling wine comes from the verb 'to fizz' and is in the direct-object form after the verb 'was drinking'."),
    (1, None, "'Do I have to breathe? Breathe into the tube?' Literally 'it is necessary to breathe', followed by the preposition 'into' with the direct-object form of 'little tube'."),
    (2, None, "'Let me go, please! Let me go!' He uses the polite plural command of the single-action form 'to let go'."),
    (3, 'Три с половиной промилле?', "'Three and a half per mille?' Per mille is parts per thousand of blood alcohol — three and a half is an enormous reading. Notice the 'with/as' form after 'with': 'three with a half'."),
    (3, 'У меня семь кредитов!', "'I have seven loans!' After numbers from five upwards, Russian nouns take the plural 'of' form. As the police lead him away, Samson calls out to his lawyer friend Danila Golovkin."),
    (4, None, "'No, don't! Danya, come on, tell them!' Danila tries to intervene, while back at the communal flat Arkady and Ilona stare at the television screen."),
    (5, None, "'Look at the news!' Arkady points at the screen."),
    (6, None, "'A terrible crash happened at the Society for the Blind!' The preposition for 'by' or 'at' takes the 'of' form of 'society', and 'of the blind' is the plural 'of' form of the adjective used as a noun."),
    (7, None, "'At huge speed the car crashed into the building!' Notice how 'on huge speed' uses the location form, while 'into the building' uses the direct-object form for motion into a place."),
    (8, None, "'A fire started there! Fire engines and police are everywhere!' Literally 'fire machines and police'. Ilona buries her face in her hands."),
    (9, 'Ну что я тебе скажу, Аркаша?', "'Well, what can I tell you, Arkasha?' She uses the future-tense form 'what will I say to you' and the warm diminutive of Arkady's name."),
    (9, 'Это полный кошмар!', "'This is a total nightmare!' And she regrets turning down Mayor Pasha Osipenko."),
    (10, 'Вот я дура!', "'What a fool I am!' Literally 'here I am a fool'."),
    (10, 'Надо было работать на Осипенко.', "'I should have worked for Osipenko.' Literally 'it was necessary to work on Osipenko' — working for a boss uses the preposition 'on' with the direct-object form."),
    (11, None, "'Easy, easy! Not everything is lost yet!' Literally 'quietly, quietly', using the short passive form 'lost' in the neuter form."),
]
