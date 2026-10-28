# Authoring module for kukhnya-s01e16-scene-09.
ID = 'kukhnya-s01e16-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 9
TITLE = 'Проверка у конкурентов  (Inspection at the Rivals)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "A migration inspector finishes his check at Elena's restaurant. He is very impressed. He says there are no illegal workers. They decide to eat at Claude Monet. Let us listen to their conversation in Russian first."
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "A migration inspector finishes his check at Elena's restaurant. He is very impressed. He says there are no illegal workers. They decide to eat at Claude Monet. Next time you watch the episode, listen for the Russian expressions for 'restaurant' and 'to be' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('inspector', 'Ваш ресторан будет отличным.', 'Your restaurant will be excellent.', [(62, 'Ну что же, уважаемая Елена Павловна, мне кажется, что ваш ресторан будет...'), (63, 'весьма успешным.')], ''),
    ('elena', 'Мы все делаем правильно.', 'We do everything right.', [], ''),
    ('elena', 'Большое спасибо вам.', 'Thank you very much.', [(64, 'Спасибо.')], ''),
    ('inspector', 'Вы меня очень удивили.', 'You really surprised me.', [(66, 'Признаюсь, вы меня очень сильно удивили.')], ''),
    ('inspector', 'Ни одного повара без документов.', 'Not a single cook without documents.', [(67, 'Ни одного нелегального работника на кухне.')], ''),
    ('elena', 'Я привыкла работать по закону.', 'I got used to working by the law.', [(68, 'Дело в том, что я очень долго работала за границей и привыкла,'), (69, 'чтобы все было по закону.')], ''),
    ('inspector', 'Мне было очень приятно.', 'It was very pleasant for me.', [(72, 'Мне было чрезвычайно приятно с вами познакомиться.')], ''),
    ('inspector', 'Пойдём в другой ресторан?', 'Let us go to another restaurant?', [(74, 'Может, мы еще куда-нибудь прогуляемся?')], ''),
    ('inspector', 'Тут есть Клод Моне.', 'Here is Claude Monet.', [(75, 'В этом же здании есть ресторан.'), (76, 'Клод Мане.')], ''),
    ('elena', 'Отлично, люблю французскую кухню.', 'Excellent, I love French cuisine.', [(77, 'Отлично. Я обожаю французскую кухню.')], ''),
    ('barinov', 'К нам идёт проверка!', 'An inspection is coming to us!', [(79, 'К нам идет проверка ФМС.')], ''),
    ('barinov', 'Все без документов, вон!', 'Everyone without documents, get out!', [(84, 'Все нелегалы немедленно вон из ресторана.')], ''),
]
WALK = [
    (0, None, "'Your restaurant will be excellent.' Offering a compliment, the official gives a glowing review of the establishment."),
    (1, None, "'We do everything right.' Elena responds proudly, asserting that they always handle their business properly."),
    (2, None, "'Thank you very much.' Expressing her gratitude, she thanks the visitor for the kind words."),
    (3, None, "'You really surprised me.' Admitting his shock, the official says he did not expect such a flawless operation."),
    (4, None, "'Not a single cook without documents.' Highlighting the perfection, he points out that every single worker had their paperwork in order."),
    (5, None, "'I got used to working by the law.' Stating her principles, the owner mentions that following the rules is just how she operates."),
    (6, None, "'It was very pleasant for me.' Wrapping up the visit, the official remarks on how enjoyable the experience was."),
    (7, None, "'Let us go to another restaurant?' Suggesting a new target, he proposes they move on to the next place."),
    (8, None, "'Here is Claude Monet.' Pointing out the location, he identifies the establishment right next door."),
    (9, None, "'Excellent, I love French cuisine.' Elena eagerly agrees, sharing her fondness for that specific style of food."),
    (10, None, "'An inspection is coming to us!' Barinov sounds the alarm, warning his staff that trouble is walking through the door."),
    (11, None, "'Everyone without documents, get out!' Barking a harsh command, he orders anyone without proper paperwork to flee immediately."),
]
