# Authoring module for kukhnya-s01e03-scene-07.
ID = 'kukhnya-s01e03-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = 'Строгий судья  (The Strict Judge)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'judge': 'Судья'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "In the dining room, Chef Barinov brings a dessert to an important guest himself, boasting that he does whatever the guests ask. Then the guest tells him what she does for a living, and the chef goes pale. Here's the Russian first."
OPENER = "Let's go back to the table."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'The judge is not about to give back his licence, and Barinov slinks back to the kitchen. Take that last phrase with you: it\'s how Russians say "count yourself lucky".'
CLOSING = ('judge', 'Пока!')
STORY = [
    ('barinov', 'Вот десерт от нашего кондитера.', 'Here is dessert from our pastry chef.', [(167, 'от нашего кондитера')], ''),
    ('judge', 'Спасибо, что изменили меню для меня.', 'Thank you for changing the menu for me.', [(169, 'Спасибо, что вы внесли изменения')], ''),
    ('barinov', 'Я шеф и выполняю любые заказы.', 'I am the chef and I fulfill any orders.', [(170, 'Я шеф-повар и выполняю любые')], ''),
    ('barinov', 'А вы кем работаете, если не секрет?', 'And what do you do, if it is not a secret?', [(171, 'А вы, кстати, чем занимаетесь')], ''),
    ('judge', 'Я работаю судьёй в Тверском суде.', 'I work as a judge at the Tverskoy court.', [(173, 'Я судья'), (181, 'в Тверском суде работаю')], ''),
    ('barinov', 'Ого! А меня вчера лишили прав!', 'Whoa! And they suspended my license yesterday!', [(178, 'Прав лишили')], ''),
    ('judge', 'Как ваша фамилия?', 'What is your last name?', [(183, 'Как ваша фамилия')], ''),
    ('barinov', 'Моя фамилия Баринов. Виктор Баринов.', 'My last name is Barinov. Viktor Barinov.', [(184, 'Баринов. Виктор Баринов')], ''),
    ('judge', 'Так это я вынесла такое решение!', 'So it was I who issued that decision!', [(185, 'я выносила решение по вашему делу')], ''),
    ('barinov', 'Может быть, мы можем всё исправить?', 'Maybe we can fix everything?', [(188, 'можно что-то исправить')], ''),
    ('judge', 'Нет. Вы сбили светофор на дороге!', 'No. You knocked down a traffic light on the road!', [(190, 'сбитый светофор')], ''),
    ('barinov', 'Но у меня было уважительное оправдание.', 'But I had a valid excuse.', [(191, 'у меня есть оправдание')], ''),
    ('judge', 'Скажите спасибо, что срок всего год.', 'Say thank you that the suspension is only a year.', [(192, 'спасибо скажите, что вас только на год')], ''),
]
WALK = [
    (0, None, [
        '\'Here is dessert from our pastry chef.\' The phrase for "from our pastry chef", ',
        ('barinov', 'от нашего кондитера.'),
        ', puts a special ending on both words. This word translates to a person who makes cakes and pastries.'
    ]),
    (1, None, [
        "'Thank you for changing the menu for me.' The phrase for thanking someone is ",
        ('judge', 'Спасибо, что'),
        ', which literally means "thanks that". The word for "changed" is ',
        ('judge', 'изменили'),
        ' which has the ending for the polite "you".'
    ]),
    (2, None, [
        '\'I am the chef and I fulfill any orders.\' The word for "any", ',
        ('barinov', 'любые'),
        ', is built from the word for "to love", so it literally means "whichever you like". And ',
        ('barinov', 'выполняю'),
        ' translates to "I fulfill".'
    ]),
    (3, None, [
        '\'And what do you do, if it is not a secret?\' The phrase for "what do you do" is ',
        ('barinov', 'кем работаете,'),
        ' which literally asks "as whom do you work?". The phrase ',
        ('barinov', 'если не секрет?'),
        ' translates to "if it is not a secret" and softens a personal question.'
    ]),
    (4, None, [
        '\'I work as a judge at the Tverskoy court.\' The word for a judge takes a special ending to mean "as a judge", becoming ',
        ('judge', 'судьёй'),
        '. The phrase for "in the Tverskoy court" is ',
        ('judge', 'в Тверском суде.'),
        ' which has special word shapes for being inside a place.'
    ]),
    (5, None, [
        '\'Whoa! And they suspended my license yesterday!\' A driving licence translates to "rights" and is always in a shape for more than one, which here is ',
        ('barinov', 'прав!'),
        ' The phrase for suspending a license literally means "they deprived me of rights", using ',
        ('barinov', 'лишили'),
        ' for "they deprived", without actually naming who "they" are.'
    ]),
    (6, None, [
        '\'What is your last name?\' The word for "surname", ',
        ('judge', 'фамилия?'),
        ', looks like "family" but only means your last name. The full question translates to "how is your surname?", asked as ',
        ('judge', 'Как ваша фамилия?')
    ]),
    (7, None, [
        '\'My last name is Barinov. Viktor Barinov.\' Russian leaves out the word for "is", so you just say ',
        ('barinov', 'Моя фамилия Баринов.'),
        ' His first name is given as ',
        ('barinov', 'Виктор')
    ]),
    (8, None, [
        "'So it was I who issued that decision!' The phrase for a court passing a ruling is built from the action words to carry out a decision, shown here as ",
        ('judge', 'вынесла'),
        ' followed by ',
        ('judge', 'решение!'),
        ' Saying ',
        ('judge', 'это я'),
        ' literally translates to "it\'s I", putting the weight on her.'
    ]),
    (9, None, [
        '\'Maybe we can fix everything?\' The phrase for "maybe" is ',
        ('barinov', 'Может быть,'),
        ' which literally means "may be". The word for "to fix", ',
        ('barinov', 'исправить?'),
        ', is built from the root for "right", so it translates to "set right".'
    ]),
    (10, None, [
        '\'No. You knocked down a traffic light on the road!\' The word for "traffic light", ',
        ('judge', 'светофор'),
        ', joins the word for "light" to a Greek root for "carrying". The action word ',
        ('judge', 'сбили'),
        ' means "knocked down", and ',
        ('judge', 'на дороге!'),
        ' translates to "on the road".'
    ]),
    (11, None, [
        '\'But I had a valid excuse.\' The phrase for "I had" is ',
        ('barinov', 'у меня было'),
        ', which literally means "at me there was". The word for "valid", ',
        ('barinov', 'уважительное'),
        ', is built from the root for "respect", and ',
        ('barinov', 'оправдание.'),
        ' translates to "excuse".'
    ]),
    (12, None, [
        '\'Say thank you that the suspension is only a year.\' The phrase for "be grateful that" is literally ',
        ('judge', 'Скажите спасибо, что'),
        ' which translates to "say thank you that". The word for a fixed term is ',
        ('judge', 'срок'),
        ', and ',
        ('judge', 'всего год.'),
        ' means "in all a year".'
    ]),
]
