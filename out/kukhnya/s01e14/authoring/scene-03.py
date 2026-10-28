# Authoring module for kukhnya-s01e14-scene-03.
ID = 'kukhnya-s01e14-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 3
TITLE = 'Серьёзный парень  (A Serious Guy)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'eleonora': 'Элеонора', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'Vika has a visitor at the restaurant: a woman she calls Mum. The woman has plenty to say about Max. Hear their talk in Russian before we look closer.'
OPENER = "Now slowly, with Vika's mother doing most of the talking."
TRANSITION = 'The whole scene once more, in one piece.'
OUTRO = "Vika's mother backs off for now, but she hasn't changed her mind about Max. Listen for the difference between 'mam' at the start and 'mama' at the end. See you in the next scene."
CLOSING = ('eleonora', 'Пока!')
STORY = [
    ('vika', 'Мам, зачем ты пришла сюда сегодня?', 'Mom, why did you come here today?', [], ''),
    ('eleonora', 'Зачем тебе этот странный тинейджер?', 'What do you want with that strange teenager?', [(7, 'Зачем тебе этот тинейджер?')], ''),
    ('vika', 'Макс серьёзный парень и хороший повар.', 'Max is a serious guy and a good cook.', [(11, 'Макс серьёзный парень.')], ''),
    ('eleonora', 'Почему ты вечно впадаешь в крайности?', 'Why do you always go to extremes?', [(9, 'Вика, ну почему ты вечно впадаешь в какие-то крайности?')], ''),
    ('vika', 'Это моя жизнь, и я сама решаю.', 'This is my life, and I decide myself.', [], ''),
    ('eleonora', 'То женатики, то дети, сразу дети.', 'First married men, then kids, kids right away.', [(10, 'То женатики, то дети. В общем, сразу дети.')], ''),
    ('vika', 'Хватит критиковать меня каждый день!', 'Stop criticizing me every single day!', [], ''),
    ('eleonora', 'Скажи, а ты записала парня в школу?', 'Tell me, did you enroll the guy in school?', [(13, 'Скажи, а ты успела записать серьёзного парня в школу?')], ''),
    ('vika', 'Я не хочу это обсуждать сейчас.', 'I do not want to discuss this now.', [], ''),
    ('eleonora', 'А то я могла бы вам помочь.', 'Otherwise I could have helped you.', [(14, 'А то я могу бы хлопотать.')], ''),
    ('vika', 'Мама, пожалуйста, просто уходи отсюда.', 'Mom, please, just leave from here.', [], ''),
    ('eleonora', 'Ладно, я оставлю вас в покое пока.', 'Alright, I will leave you in peace for now.', [], ''),
]
WALK = [
    (0, None, "'Mom, why did you come here today?' 'Mam' is the clipped form of 'mama' that you use to call your mother. 'Prishla', came, ends in 'a' because the 'you' is her mother."),
    (1, None, "'What do you want with that strange teenager?' 'Zachem tebe?' is literally 'what for to you?', the usual way to ask why someone needs something. 'Tineydzher' is just the English 'teenager' in Russian letters."),
    (2, None, "'Max is a serious guy and a good cook.' 'Seryozny paren', literally 'serious guy', comes with no word for 'is'. 'Paren' is the everyday word for a young man."),
    (3, None, "'Why do you always go to extremes?' 'Vpadat v kraynosti' is literally 'fall into extremes', and 'kraynost' is built on 'kray', the edge. 'Vechno', literally 'eternally', is the grumbling 'always'."),
    (4, None, "'This is my life, and I decide myself.' 'Zhizn', life, is feminine, so 'my' is 'moya'. 'Sama', by myself, has the 'a' because Vika is a woman."),
    (5, None, "'First married men, then kids, kids right away.' 'To ... to ...' means 'one minute ..., the next ...'. 'Zhenatiki' is a jokey, slightly mocking word built on 'zhenat', married, said of a man."),
    (6, None, "'Stop criticizing me every single day!' 'Khvatit' means 'that's enough', and with a verb after it, 'khvatit kritikovat', it works as 'stop criticizing'. 'Kritikovat' is 'criticize' with the Russian verb ending '-ovat', which turns many borrowed words into verbs."),
    (7, None, "'Tell me, did you enroll the guy in school?' 'Paren' becomes 'parnya' as the one being enrolled; the 'e' drops out when the ending is added. 'Zapisat v shkolu', literally 'write into school', is how you sign a child up."),
    (8, None, "'I do not want to discuss this now.' 'Ne khochu obsuzhdat', 'I don't want to discuss': after 'khochu' the verb stays in its basic form. Russian is happy to put 'seychas', now, at the very end."),
    (9, None, "'Otherwise I could have helped you.' 'A to' at the start means 'or else' or 'because otherwise'. 'Mogla by', could, is the past 'mogla' plus little 'by', which turns it into 'would'. 'Vam' is plural, meaning Vika and Max."),
    (10, None, "'Mom, please, just leave from here.' Now Vika uses the full 'mama'. 'Ukhodi', go away, is the 'ty' order, and 'otsyuda' means 'from here', so no separate 'from' is needed."),
    (11, None, "'Alright, I will leave you in peace for now.' 'Ostavit v pokoe', literally 'leave in calm', is the set phrase for leaving someone alone. 'Poka' here means 'for now'; it's the same word as the 'poka' for goodbye."),
]
