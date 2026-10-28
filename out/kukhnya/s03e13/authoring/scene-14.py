ID = 'kukhnya-s03e13-scene-14'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 13
SCENE = 14
TITLE = "Звонок Нагиеву и видеозапись  (Calling Nagiyev and the Video)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "kostya": "anja", "anya": "alisa", "vika": "angelina"}
LABELS = {"kostya": "Костя", "anya": "Макс", "vika": "Вика"}
SOURCE_NAME = 'Кухня (Kukhnya) S3.13'
SOURCE_FILE = 'sources/kukhnya/s03/e13.ru.srt'

INTRO = 'On the phone with Vika, Nagiyev orders Kostya to calculate the bar damages, but Kostya bursts into the office with shocking news from the restored security tape. Listen to the full exchange first, and then we will unpack it.'

STORY = [
    ('vika', 'Алло, Дмитрий Владимирович, это я.', 'Hello, Dmitry Vladimirovich, it is me.', [(215, 'Алло, Дмитрий Владимирович, это я')], 'adapted'),
    ('anya', 'Я прекрасно знаю, что это ты.', 'I know very well that it is you.', [(216, 'Я знаю, что это ты')], 'adapted'),
    ('vika', 'У нас тут проблема в баре произошла.', 'We had an emergency in the bar here.', [(217, 'в баре произошло')], 'adapted'),
    ('vika', 'Откуда вы уже об этом знаете?', 'How do you already know about this?', [(218, 'Откуда вы знаете')], 'adapted'),
    ('anya', 'В своём королевстве я знаю всё.', 'In my kingdom I know everything.', [(219, 'в своем королевстве я знаю все')], 'adapted'),
    ('anya', 'Дай мне бармена, я сейчас решу проблему.', 'Put the bartender on, I will solve the problem right now.', [(220, 'Дай-ка мне бармена'), (220, 'сейчас решу проблему')], 'adapted'),
    ('kostya', 'Алло, да, я вас понял.', 'Hello, yes, I understood you.', [(221, 'Алло'), (222, 'Понял')], 'adapted'),
    ('kostya', 'Хорошо, посчитаю общую сумму.', 'Alright, I will calculate the total amount.', [(223, 'Хорошо. Общая сумма')], 'adapted'),
    ('kostya', 'Хорошо, до свидания, Дмитрий Владимирович.', 'Alright, goodbye, Dmitry Vladimirovich.', [(224, 'Хорошо, до свидания')], 'adapted'),
    ('kostya', 'В общем, Макс с Катей не виноваты.', 'In short, Max and Katya are not guilty.', [(225, 'Макс с Катей, они как бы и не виноваты')], 'adapted'),
    ('kostya', 'Нет, виноваты, но только на две бутылки.', 'Well, they are guilty, but only of two bottles.', [(226, 'Нет, виноваты, но только на две бутылки')], 'adapted'),
    ('kostya', 'А включите видеозапись сами и всё посмотрите.', 'Turn on the video recording yourselves and watch it all.', [(227, 'а включите видеозапись сами и все посмотрите')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Hello, Dmitry Vladimirovich, it is me.' The grammar packs 'hello' and 'I' into a tight, idiomatic kitchen exchange."),
    (1, None, "'I know very well that it is you.' Max addresses the listener with the informal singular 'you' alongside 'you'. Vika answers right away."),
    (2, None, "'We had an emergency in the bar here.' The grammar packs 'at' and 'occurred' into a tight, idiomatic kitchen exchange."),
    (3, None, "'How do you already know about this?' Vika anchors the line on 'where from', while 'know' completes the thought."),
    (4, None, "'In my kingdom I know everything.' Notice how Russian expresses 'one's own' and 'everything' with crisp inflection rather than helper words."),
    (5, None, "'Put the bartender on, I will solve the problem right now.' Here the Russian phrasing highlights 'give' before landing on 'problem'."),
    (6, None, "'Hello, yes, I understood you.' The grammar packs 'hello' and 'understood' into a tight, idiomatic kitchen exchange."),
    (7, None, "'Alright, I will calculate the total amount.' Kostya anchors the line on 'well', while 'sum' completes the thought."),
    (8, None, "'Alright, goodbye, Dmitry Vladimirovich.' The grammar packs 'well' and 'Vladimirovich' into a tight, idiomatic kitchen exchange."),
    (9, None, "'In short, Max and Katya are not guilty.' The meaning hinges on 'shared' working together with 'guilty' in spoken Russian."),
    (10, None, "'Well, they are guilty, but only of two bottles.' In Russian, the idea of 'no' flows naturally into 'bottles' without extra filler words."),
    (11, None, "'Turn on the video recording yourselves and watch it all.' Spoken Russian keeps this brisk, leaning on 'and' and finishing on 'look'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'If Max and Katya only quietly took two bottles, who smashed the rest of the bar? See you next time!'
CLOSING = ("kostya", "До встречи!")
