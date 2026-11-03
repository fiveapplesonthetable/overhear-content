# Authoring module for kukhnya-s01e14-scene-11.
ID = 'kukhnya-s01e14-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 11
TITLE = 'Разбитое сердце  (Broken Heart)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'girl': 'Девушка', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'Near the entrance, an upset young woman stops Max. He has been a bad boyfriend, and she tells him so. Hear it in Russian first.'
OPENER = 'Slowly, and watch him try to calm her down.'
TRANSITION = 'Now the scene in one go.'
OUTRO = "She storms off, and Max is left standing there. She gave him two sharp commands to remember: 'forget it' and 'go away'. Catch you later."
CLOSING = ('girl', 'Пока!')
STORY = [
    ('girl', 'Макс, ты разбил моё бедное сердце!', 'Max, you broke my poor heart!', [(172, 'разбил мое сердце, подлый бабник.')], ''),
    ('max', 'Подожди, давай спокойно поговорим об этом.', 'Wait, let us talk calmly about this.', [], ''),
    ('girl', 'Ты просто ужасный и подлый обманщик!', 'You are simply a terrible and vile deceiver!', [(172, 'подлый бабник')], ''),
    ('max', 'Я не хотел обидеть тебя тогда.', 'I did not want to offend you back then.', [], ''),
    ('girl', 'Ты обещал звонить мне каждый день.', 'You promised to call me every single day.', [], ''),
    ('max', 'У меня было очень много работы.', 'I had a huge amount of work.', [], ''),
    ('girl', 'Забудь навсегда мой личный номер телефона!', 'Forget my personal phone number forever!', [(173, 'Забудь мой номер телефона.')], ''),
    ('max', 'Не злись, пожалуйста, выслушай меня сейчас.', 'Do not be angry, please, listen to me now.', [], ''),
    ('girl', 'Забудь, что у меня вообще есть телефон!', 'Forget that I even have a phone at all!', [(174, 'Забудь, что у меня в принципе есть телефон.')], ''),
    ('max', 'Мне искренне жаль, прости меня, пожалуйста.', 'I am sincerely sorry, forgive me, please.', [], ''),
    ('girl', 'Я больше никогда не поверю тебе.', 'I will never believe you anymore.', [], ''),
    ('max', 'Дай мне один маленький последний шанс.', 'Give me one small last chance.', [], ''),
    ('girl', 'Уходи немедленно, я не хочу слушать!', 'Leave immediately, I do not want to listen!', [], ''),
]
WALK = [
    (0, None, ["'Max, you broke my poor heart!' Notice how ", ('girl', 'разбил'), " means smashed to bits. We hear for 'my poor' is ", ('girl', 'моё'), ('girl', 'бедное'), '.']),
    (1, None, ["'Wait, let us talk calmly about this.' To say 'let's talk', use ", ('max', 'давай'), ' and ', ('max', 'поговорим'), ". And 'about this' is ", ('max', 'об'), ('max', 'этом'), '.']),
    (2, None, ["'You are simply a terrible and vile deceiver!' A liar or deceiver is ", ('girl', 'обманщик'), ', and mean or vile is ', ('girl', 'подлый'), '.']),
    (3, None, ["'I did not want to offend you back then.' To hurt someone's feelings is ", ('max', 'обидеть'), ". He says he didn't want to, using ", ('max', 'не'), ('max', 'хотел'), '.']),
    (4, None, ["'You promised to call me every single day.' In Russian you call to someone, so 'to me' is ", ('girl', 'мне'), '. To say promised, use ', ('girl', 'обещал'), '.']),
    (5, None, ["'I had a huge amount of work.' He says 'I had' as ", ('max', 'У'), ('max', 'меня'), ('max', 'было'), '. The phrase for a lot of work is ', ('max', 'много'), ('max', 'работы'), '.']),
    (6, None, ["'Forget my personal phone number forever!' To say forever, use ", ('girl', 'навсегда'), '. A phone number is ', ('girl', 'номер'), ('girl', 'телефона'), '.']),
    (7, None, ["'Do not be angry, please, listen to me now.' To say 'don't get angry', use ", ('max', 'Не'), ('max', 'злись'), ". And to say 'hear me out', use ", ('max', 'выслушай'), '.']),
    (8, None, ["'Forget that I even have a phone at all!' To say 'I have a phone', use ", ('girl', 'у'), ('girl', 'меня'), ('girl', 'вообще'), ('girl', 'есть'), ('girl', 'телефон'), '. Normally Russian drops the verb for is, but ', ('girl', 'есть'), ' stays here for emphasis.']),
    (9, None, ["'I am sincerely sorry, forgive me, please.' To say 'I am sorry', use ", ('max', 'Мне'), ('max', 'искренне'), ('max', 'жаль'), '. And to ask for forgiveness, say ', ('max', 'прости'), ('max', 'меня'), '.']),
    (10, None, ["'I will never believe you anymore.' You believe 'to' someone in Russian, so 'you' becomes ", ('girl', 'тебе'), ". Here we have for 'never anymore' is ", ('girl', 'больше'), ('girl', 'никогда'), ('girl', 'не'), '.']),
    (11, None, ["'Give me one small last chance.' To say give, use ", ('max', 'Дай'), '. Last is ', ('max', 'последний'), ', and a chance is ', ('max', 'шанс'), '.']),
    (12, None, ["'Leave immediately, I do not want to listen!' To say go away, use ", ('girl', 'Уходи'), ". And 'I do not want' is ", ('girl', 'не'), ('girl', 'хочу'), '.']),
]
