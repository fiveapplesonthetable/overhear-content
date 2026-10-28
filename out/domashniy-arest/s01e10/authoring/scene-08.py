# Authoring module for domashniy-arest-s01e10-scene-08.
ID = 'domashniy-arest-s01e10-scene-08'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 8
TITLE = 'Звонок заведующей  (Call to the Director)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'galina': 'Галина', 'officer': 'Офицер'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = "Meanwhile, an undercover FSB officer makes an intimidating phone call to Galina Valeryevna, the director of the local kindergarten. He demands that young Alexei Belynkin receive special care and complete comfort. When the stunned director asks if she is being blackmailed, the officer confirms it openly. Let's listen to their phone conversation in Russian first."
OPENER = "Now let's examine the covert blackmail call line by line. An FSB officer pressures the kindergarten director over the phone."
TRANSITION = "Now let's listen to the tense phone conversation once more without pauses."
OUTRO = 'Under direct threat from the FSB, the director has no choice but to favor Alexei. See you next time!'
CLOSING = ('officer', 'Пока!')
STORY = [
    ('officer', 'Здравствуйте, Галина Валерьевна.', 'Hello, Galina Valeryevna.', [(221, 'Галина Валерьевна')], ''),
    ('officer', 'У меня к вам деловое предложение.', 'I have a business proposal for you.', [(223, 'у меня к вам есть предложение')], ''),
    ('galina', 'Слушаю вас. Очень интересно.', 'I am listening. Very interesting.', [(220, 'Слушаю'), (224, 'Интересно')], ''),
    ('officer', 'К вам в садик ходит мальчик Алексей.', 'A boy named Alexei attends your kindergarten.', [(225, 'К вам в садик ходит мальчик Алексей')], ''),
    ('officer', 'Он должен чувствовать себя комфортно.', 'He must feel comfortable.', [(227, 'было максимально комфортным')], ''),
    ('officer', 'Иначе вас ждут большие неприятности!', 'Otherwise big troubles await you!', [(228, 'В противном случае вас ждут большие неприятности')], ''),
    ('galina', 'Вы меня сейчас шантажируете?', 'Are you blackmailing me right now?', [(241, 'Вы меня что, шантажируете')], ''),
    ('officer', 'Да, наконец до вас дошло!', 'Yes, finally you get it!', [(242, 'Наконец дошло')], ''),
    ('galina', 'Но это же просто омерзительно!', 'But this is simply revolting!', [(244, 'это омерзительно')], ''),
    ('officer', 'Согласен, но жизнь бывает жестокой.', 'I agree, but life can be cruel.', [(245, 'Согласен')], ''),
    ('galina', 'Что именно я должна делать?', 'What exactly must I do?', [(248, 'Что я должна делать')], ''),
    ('officer', 'Вы подумайте об этом сами.', 'Think about that yourself.', [(249, 'А вы подумайте')], ''),
    ('officer', 'Вечером мальчик всё расскажет дома.', 'In the evening the boy will tell all at home.', [(250, 'Алексей придет сегодня вечером домой и расскажет')], ''),
    ('officer', 'Надеюсь, ему всё понравится.', 'I hope he will like everything.', [(251, 'хорошо ли ему было в садике')], ''),
]
WALK = [
    (0, None, "'Hello, Galina Valeryevna.' Using her first name and patronymic gives the phone call a polite, official opening."),
    (1, None, "'I have a business proposal for you.' Calling a shakedown a \"business proposal\" is classic bureaucratic menace."),
    (2, None, "'I am listening. Very interesting.' Having no idea who is on the line yet, the kindergarten director answers cautiously."),
    (3, None, "'A boy named Alexei attends your kindergarten.' Without wasting time, the caller names the exact child he is calling about."),
    (4, None, "'He must feel comfortable.' Behind the polite wording is an order: make sure little Lyosha is treated like royalty."),
    (5, None, "'Otherwise big troubles await you!' Literally \"big troubles wait for you\", dropping the polite mask altogether."),
    (6, None, "'Are you blackmailing me right now?' Stunned, Galina can hardly believe someone is threatening her over a daycare group."),
    (7, None, "'Yes, finally you get it!' Literally \"it finally reached to you\", a blunt Russian idiom for when the penny drops."),
    (8, None, "'But this is simply revolting!' Outraged, she tells him straight out how disgusting this intimidation is."),
    (9, None, "'I agree, but life can be cruel.' Rather than arguing, the agent cheerfully agrees and shrugs it off as the way of the world."),
    (10, None, "'What exactly must I do?' Realizing she cannot fight the security services, the director gives in and asks for her orders."),
    (11, None, "'Think about that yourself.' Leaving the details to her imagination makes her work even harder to please them."),
    (12, None, "'In the evening the boy will tell all at home.' Little Alexei's bedtime report to his mother will be the test of whether she obeyed."),
    (13, None, "'I hope he will like everything.' Said in this tone, a polite wish sounds more like a final warning."),
]
