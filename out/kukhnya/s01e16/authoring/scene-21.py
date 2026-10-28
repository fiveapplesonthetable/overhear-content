# Authoring module for kukhnya-s01e16-scene-21.
ID = 'kukhnya-s01e16-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 21
TITLE = 'Может помочь  (Can I help)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'The inspector has left Barinov with a fine and Fedya with an order to leave the country. Fedya asks the chef for help, and Barinov, out of ideas, thinks aloud.'
OPENER = "Let's go back through it slowly."
TRANSITION = 'Once more, all the way through.'
OUTRO = "Barinov has no plan, only a bad joke. Keep an ear out for 'mozhet': on its own at the start of a sentence it means 'maybe', although its first meaning is 'can'. See you next time!"
CLOSING = ('barinov', 'Ну, удачи!')
STORY = [
    ('fedya', 'Шеф, может, поможете?', 'Chef, maybe you can help?', [(277, 'Шеф, может помочь?')], ''),
    ('barinov', 'Не знаю.', "I don't know.", [(278, 'Не знаю.')], ''),
    ('barinov', 'Меня он оштрафовал.', 'He fined me.', [(278, 'Меня он оштрафовал')], ''),
    ('barinov', 'А тебя хотят депортировать.', 'And they want to deport you.', [(278, 'тебя депортировать.')], ''),
    ('fedya', 'И ничего нельзя сделать?', 'And nothing can be done?', [], ''),
    ('barinov', 'Думаю, нет.', "I don't think so.", [(279, 'Думаю, нет.')], ''),
    ('barinov', 'С другим, может, договориться удастся.', 'With someone else, maybe, we could strike a deal.', [(280, 'С другим может...'), (281, 'Договориться удастся.')], ''),
    ('barinov', 'Хотя, если ты ему жизнь спасёшь...', 'Though, if you save his life...', [(283, 'Хотя, если ты ему жизнь спасешь,')], ''),
    ('barinov', 'Может, он нас и простит.', 'Maybe he will even forgive us.', [(283, 'может, он нас и простит.')], ''),
    ('fedya', 'Очень смешно, шеф.', 'Very funny, Chef.', [], ''),
]
WALK = [
    (0, None, "'Chef, maybe you can help?' 'Pomozhete' means 'you will help', said to someone you call 'vy'. Asking 'mozhet, pomozhete?', 'maybe you'll help?', is softer than a direct request."),
    (1, None, "'I don't know.' 'Ne znayu' has no 'I' at all, since the '-yu' ending already says who doesn't know. It's a flat, tired answer."),
    (2, None, "'He fined me.' The Russian is 'me he fined', with 'menya', 'me', first to put the weight on Barinov himself. 'Oshtrafovat' comes from 'shtraf', 'a fine'."),
    (3, None, "'And they want to deport you.' 'Khotyat', 'they want', has no 'they': Russian uses the plain plural verb for 'they' meaning the authorities. The '-irovat' ending turns many foreign words into Russian verbs."),
    (4, None, "'And nothing can be done?' 'Nelzya' usually means 'not allowed', but next to 'sdelat', 'to do', it means 'can't be done'. 'Nichego nelzya sdelat', 'nothing can be done', is the stock phrase for a hopeless case."),
    (5, None, "'I don't think so.' Russian says 'dumayu, net', literally 'I think, no'. It's a handy way to answer a question you don't like."),
    (6, None, "'With someone else, maybe, we could strike a deal.' 'Udastsya' means 'it will work out', and it has no subject at all. 'Dogovoritsya' means 'to come to an agreement'."),
    (7, None, "'Though, if you save his life...' 'Khotya' means 'although', the word for turning an idea around. 'Spasyosh', 'you will save', is a finished action, so the future is built into the ending."),
    (8, None, "'Maybe he will even forgive us.' 'Mozhet' here is short for 'mozhet byt', 'maybe'. The small 'i' before 'prostit' means 'even'."),
    (9, None, "'Very funny, Chef.' 'Smeshno' means 'funny', from 'smekh', 'laughter'. Said flatly, as here, it means the opposite, just as in English."),
]
