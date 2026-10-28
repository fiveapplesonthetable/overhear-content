# Authoring module for domashniy-arest-s01e04-scene-26.
ID = 'domashniy-arest-s01e04-scene-26'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 4
SCENE = 26
TITLE = 'Старые счёты  (Old Scores)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ilona': 'Илона', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.04'
SOURCE_FILE = 'sources/domashniy-arest/s01/e04.ru.dual.srt'
INTRO = "In the mayor's office later that evening. Last time, Samson and Nina used their free deposit at the Italian restaurant Francesco, toasting their new life with sparkling wine and seafood. Meanwhile, Pasha watches the video of drunk Samson that Ilona got from Klavdia's phone, and Ilona asks him a question about Arkady. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's take the scene line by line. Pasha has just watched the video of Samson."
TRANSITION = "Now let's hear the whole scene once more, start to finish."
OUTRO = 'So Pasha insults the woman who just won his campaign battle, and forbids her to bring Arkady even a pillow. We will soon see what Ilona does with that pillow. See you next time!'
CLOSING = ('ilona', 'Пока!')
STORY = [
    ('pasha', 'Ну что же, неплохо. Ты молодец.', 'Well then, not bad. Good job.', [(1053, 'Ну что же, неплохо')], "'Будем считать, что справилась' (1054) -> 'Ты молодец.'"),
    ('pasha', 'Сейчас мы выложим это видео в интернет.', "Now we'll upload this video to the internet.", [], "new: clean A1 for cue 1055 'Давай-ка заливает в сеть'"),
    ('ilona', 'Павел Юрьевич, у меня ещё к вам вопрос.', 'Pavel Yuryevich, I have one more question for you.', [(1056, 'Павел Юрьевич, у меня еще к вам вопрос')], ''),
    ('pasha', 'Какой вопрос?', 'What question?', [(1057, 'Какой')], "'вопрос' added"),
    ('ilona', 'По поводу Аникеева.', 'About Anikeev.', [(1058, 'По поводу')], "mistranscribed 'Никеева' -> 'Аникеева'"),
    ('pasha', 'А что с ним такое?', "And what's the matter with him?", [(1059, 'А что с ним такое')], ''),
    ('ilona', 'Он живёт в ужасных условиях.', "He's living in terrible conditions.", [(1060, 'он живет в'), (1060, 'условиях')], "'каких-то нечеловеческих' -> 'ужасных'"),
    ('ilona', 'У него даже постельного белья нет.', "He doesn't even have bed linen.", [(1062, 'У него даже постельного белья нет')], ''),
    ('ilona', 'Может, вы перевезёте его в другое место?', 'Maybe you will move him to another place?', [(1064, 'Может, вы'), (1064, 'его'), (1064, 'в другое место')], "'могли бы куда-то его перевезти' -> 'перевезёте его'"),
    ('pasha', 'Нет. Ничего такого я делать не буду.', "No. I'm not going to do anything like that.", [(1066, 'Нет'), (1067, 'Ничего'), (1067, 'я делать не буду')], "'подобного' -> 'такого'"),
    ('ilona', 'Но вы же с ним учились вместе!', 'But you studied together with him!', [(1070, 'Вы же с ним')], "'вроде как однокурсники' -> 'учились вместе'"),
    ('ilona', 'Без него вы бы возили сувениры из Китая.', 'Without him you would be hauling souvenirs from China.', [(1072, 'вы бы'), (1072, 'из Китая возили')], "shortened from cue 1072 ('Насколько я знаю, если бы не он, вы бы до сих пор сувенирку из Китая возили')"),
    ('pasha', 'Я что-то не понял. Ты кто такая?', "I don't quite understand. Who do you think you are?", [(1073, 'Я что-то не понял')], "clean stand-in for Pasha's slur in cue 1074"),
    ('ilona', 'Я в клубе танцевала.', 'I danced in a club.', [(1076, 'Я в')], "garbled 'в трепете станцевала' -> 'в клубе танцевала'"),
    ('pasha', 'Иди работай давай!', 'Go on, get to work!', [(1079, 'Иди работай давай')], 'crude lines 1077-1078 omitted'),
    ('pasha', 'Привезёшь ему подушку — сразу уволю! Ясно? Иди!', "Bring him a pillow and I'll fire you at once! Clear? Go!", [(1080, 'ему'), (1080, 'подушку'), (1081, 'ясно'), (1082, 'Иди')], "clean A1 for cues 1080-1082 ('А если я узнаю, что ты ему хотя бы подушку привезла, вылетишь отсюда...')"),
    ('ilona', 'Всего доброго. До свидания.', 'All the best. Goodbye.', [(1083, 'Всего доброго'), (1084, 'До свидания')], ''),
]
WALK = [
    (0, None, "'Well then, not bad. Good job.' Pasha is pleased with himself: Ilona got the video of drunk Samson from old Klavdia's phone. He gives the order."),
    (1, None, "'Now we'll upload this video to the internet.' The action word literally means 'we will lay it out', the everyday Russian word for posting a video online. But Ilona doesn't leave."),
    (2, None, "'Pavel Yuryevich, I have one more question for you.' She uses his first name and patronymic, and 'for you' is literally 'towards you'. Pasha looks up."),
    (3, None, "'What question?' The question word takes the masculine singular form to match 'question'."),
    (4, None, "'About Anikeev.' The two-word phrase at the start means 'regarding' or 'about', and Anikeev takes the 'of' ending. Pasha frowns."),
    (5, None, "'And what's the matter with him?' Literally, 'what is such a thing with him?'. Ilona remembers what she saw in Arkady's tiny room behind the wardrobe."),
    (6, None, "'He's living in terrible conditions.' After 'in', both the describing word and the plural word take the location plural ending. She adds a detail."),
    (7, None, "'He doesn't even have bed linen.' After 'there isn't', 'bed linen' goes into the 'of' case. So she makes a polite suggestion."),
    (8, None, "'Maybe you will move him to another place?' In the show she notes that Arkady owns a dozen flats around town. Pasha's answer is ice-cold."),
    (9, None, "'No. I'm not going to do anything like that.' Another Russian double negative: 'nothing like that I will not do'. Ilona reminds him of the past."),
    (10, None, "'But you studied together with him!' In Russian, 'you with him' means 'you and he', so the expression takes the plural past ending. And she touches Pasha's sorest spot."),
    (11, None, "'Without him you would be hauling souvenirs from China.' Before Arkady made him deputy mayor, Pasha ran a small souvenir business. The little word after 'you' makes the sentence 'would be'. Pasha explodes."),
    (12, None, "'I don't quite understand. Who do you think you are?' The word meaning 'somehow' modifies the word for 'understood' to sharpen the tone."),
    (13, None, "'I danced in a club.' Years ago, Arkady helped her leave that club and paid for her university studies in Moscow. Pasha shouts at her."),
    (14, None, "'Go on, get to work!' Literally, 'go work, come on': two commands side by side. And he adds a threat."),
    (15, 'Привезёшь ему подушку — сразу уволю!', "'Bring him a pillow and I'll fire you at once!' The furious governor warns his aide that if anyone brings Pasha a pillow, they are fired on the spot."),
    (15, 'Иди!', "'Clear? Go!' He points at the door. Ilona's face is calm, and her voice is dangerously polite."),
    (16, None, "'All the best. Goodbye.' The first two words are a formal farewell, literally 'of everything good'. Pasha has just made a very dangerous enemy."),
]
