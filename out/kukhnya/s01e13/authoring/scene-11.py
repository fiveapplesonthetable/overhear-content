# Authoring module for kukhnya-s01e13-scene-11.
ID = 'kukhnya-s01e13-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 11
TITLE = 'Мусорные баки  (The Trash Bins)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'timur': 'Тимур'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = 'Outside the restaurant, Barinov and Elena are arguing over where the trash bins should stand. She has a document from the district office, and he has a problem with his supplier. Listen to the argument in Russian first.'
OPENER = 'Slowly, bit by bit.'
TRANSITION = 'Now the whole argument in one go.'
OUTRO = "Timur chooses sides, and the chef's debt is the reason. If you ever need to say 'you owe me', you've just heard it. Until the next scene."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'С одной вашей мусоркой я справился.', 'I handled one of your trash bins.', [(145, 'С одной вашей мусоркой справился')], ''),
    ('elena', 'Вот документ, который это подтверждает.', 'Here is a document that proves it.', [(147, 'Вот, кстати, документ, который это подтверждает.')], ''),
    ('elena', 'Это план из управы.', 'This is the plan from the district office.', [(148, 'Это план из управы')], ''),
    ('elena', 'Баки должны стоять именно в этом месте.', 'The bins must stand exactly in this place.', [(148, 'баки должны стоять именно вот в этом'), (149, 'месте.')], ''),
    ('elena', 'Вопросы ко мне есть еще?', 'Are there any more questions for me?', [(149, 'Вопросы ко мне есть еще?')], ''),
    ('barinov', 'Тимур? Ты решил поставлять ей продукты?', 'Timur? You decided to supply her with food?', [(152, 'Тимур?'), (156, 'будешь ей поставлять продукты')], ''),
    ('timur', 'Виктор Петрович, моё почтение.', 'Viktor Petrovich, my respects.', [(153, 'Виктор Петрович, мое почтение.')], ''),
    ('barinov', 'Учти, я долг не верну.', 'Keep in mind, I will not return the debt.', [(156, 'учти,'), (156, 'долг не верну.')], ''),
    ('timur', 'Извините, наше сотрудничество подошло к концу.', 'Excuse me, our cooperation has come to an end.', [(157, 'Извините,'), (157, 'наше сотрудничество подошло к концу.')], ''),
    ('timur', 'Я не могу перечить старшему.', 'I cannot contradict an older man.', [(158, 'не могу перечить старшему')], ''),
    ('timur', 'Тем более, вы должны мне пятнадцать тысяч.', 'Especially since you owe me fifteen thousand.', [(158, 'тем более,'), (159, 'у меня торчит 15 штук.')], ''),
    ('barinov', 'Десять.', 'Ten.', [], ''),
]
WALK = [
    (0, None, ["'I handled one of your trash bins.' Notice how ", ('barinov', 'справился'), " takes 'with' after it, like 'coped with'. We hear ", ('barinov', 'С'), ('barinov', 'одной'), ('barinov', 'вашей'), ('barinov', 'мусоркой'), " means 'with one of your bins'."]),
    (1, None, ["'Here is a document that proves it.' The linking word ", ('elena', 'который'), ' joins the two halves. And ', ('elena', 'подтверждает'), ' is a formal verb that suits a document.']),
    (2, None, ["'This is the plan from the district office.' The office is called ", ('elena', 'управы'), ', and ', ('elena', 'из'), ('elena', 'управы'), " means 'from the office'."]),
    (3, None, ["'The bins must stand exactly in this place.' Russian says that bins stand, ", ('elena', 'стоять'), ', and the same word is used for people. Also, ', ('elena', 'именно'), " means 'precisely', and ", ('elena', 'должны'), " is 'must'."]),
    (4, None, ["'Are there any more questions for me?' The expression ", ('elena', 'Вопросы'), ('elena', 'ко'), ('elena', 'мне'), ('elena', 'есть'), ('elena', 'еще'), " means 'any more questions'. The term ", ('elena', 'есть'), ' is said out loud here, though Russian often leaves it out.']),
    (5, None, ["'Timur? You decided to supply her with food?' The verb for supply, ", ('barinov', 'поставлять'), ", is used for businesses delivering goods. 'Her' changes shape to ", ('barinov', 'ей'), ", as in 'supply to her'."]),
    (6, None, ["'Viktor Petrovich, my respects.' The greeting ", ('timur', 'моё'), ('timur', 'почтение'), " is old-fashioned, almost bowing. It's a polite, slightly stiff way of saying hello."]),
    (7, None, ["'Keep in mind, I will not return the debt.' The order ", ('barinov', 'Учти'), " means 'take into account'. Here we have ", ('barinov', 'долг'), ('barinov', 'не'), ('barinov', 'верну'), " puts the debt first, then 'not', then 'I will return'."]),
    (8, None, ["'Excuse me, our cooperation has come to an end.' The long word ", ('timur', 'сотрудничество'), ' comes from work. The set phrase ', ('timur', 'подошло'), ('timur', 'к'), ('timur', 'концу'), " means 'is over'."]),
    (9, None, ["'I cannot contradict an older man.' Now we can look at the dialogue: ", ('timur', 'старшему'), " comes from old, and works as 'someone senior'. After ", ('timur', 'перечить'), ', to contradict, the person takes a different ending.']),
    (10, None, ["'Especially since you owe me fifteen thousand.' Russian says 'you must me' for 'you owe me', using the same word that means 'must'. And ", ('timur', 'Тем'), ('timur', 'более'), " means 'especially since'."]),
    (11, None, ["'Ten.' It's just the number, ", ('barinov', 'Десять'), '. Barinov is bargaining the debt down in one word.']),
]
