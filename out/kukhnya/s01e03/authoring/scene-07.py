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
OUTRO = 'The judge is not about to give back his licence, and Barinov slinks back to the kitchen. Take "skazhite spasibo" with you: it\'s how Russians say "count yourself lucky".'
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
    (0, None, '\'Here is dessert from our pastry chef.\' "Ot nashego konditera" puts the "from" ending on both words, -ego and -a. A "konditer" makes cakes and pastries.'),
    (1, None, '\'Thank you for changing the menu for me.\' "Spasibo, chto" is "thanks that", the frame for thanking someone for what they did. "Izmenili", changed, has the -li of the polite "vy".'),
    (2, None, '\'I am the chef and I fulfill any orders.\' "Lyubyye", any, comes from "lyubit\'", to love, so it\'s "whichever you like". "Vypolnyayu zakazy" is "I fulfill orders".'),
    (3, None, '\'And what do you do, if it is not a secret?\' "Kem vy rabotayete?" is "as whom do you work?", with "kto" changed to "kem". "Yesli ne sekret" softens a personal question.'),
    (4, None, '\'I work as a judge at the Tverskoy court.\' "Sud\'ya" becomes "sud\'yoy" for "as a judge". "V Tverskom sude" is "in the Tverskoy court", with -om and -e for being in a place.'),
    (5, None, '\'Whoa! And they suspended my license yesterday!\' A driving licence is "prava", rights, always plural. "Menya lishili prav" is "they deprived me of rights", with no one named as "they".'),
    (6, None, '\'What is your last name?\' "Familiya" looks like "family", but it means only your surname. "Kak vasha familiya?" is "how your surname?".'),
    (7, None, '\'My last name is Barinov. Viktor Barinov.\' Russian leaves out "is": "moya familiya Barinov". "Viktor" is his first name.'),
    (8, None, '\'So it was I who issued that decision!\' "Vynesti resheniye", to carry out a decision, is how a court passes a ruling. "Eto ya", it\'s I, puts the weight on her.'),
    (9, None, '\'Maybe we can fix everything?\' "Mozhet byt\'" is "may be", the full "maybe". "Ispravit\'", to fix, has "pravyy", right, at its core, so it means "set right".'),
    (10, None, '\'No. You knocked down a traffic light on the road!\' "Svetofor" joins "svet", light, to a Greek root for "carrying". "Sbili" is "knocked down", and "na doroge" is "on the road".'),
    (11, None, '\'But I had a valid excuse.\' "U menya bylo" is "at me there was", the past of "I have". "Uvazhitel\'noye", valid, shares a root with "uvazheniye", respect, and "opravdaniye" is "excuse".'),
    (12, None, '\'Say thank you that the suspension is only a year.\' "Skazhite spasibo, chto" means "be grateful that". "Srok" is a fixed term, and "vsego god" is "in all a year".'),
]
