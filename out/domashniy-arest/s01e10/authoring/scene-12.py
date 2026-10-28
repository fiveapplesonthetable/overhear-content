# Authoring module for domashniy-arest-s01e10-scene-12.
ID = 'domashniy-arest-s01e10-scene-12'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 12
TITLE = 'Новый редактор  (The New Editor)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'editor': 'Редактор', 'tatyana': 'Татьяна'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = "In the television newsroom, Tatyana catches a colleague reading someone else's text messages aloud as a prank. When the newcomer introduces himself as the new culture editor, she sentences the pranksters to a month of fetching coffee and tea. Let's listen in Russian first."
OPENER = "Let's go through the newsroom prank line by line and notice how the office banter works in Russian."
TRANSITION = "Now let's listen to the whole conversation again at normal speed."
OUTRO = 'Tatyana sends the pranksters off to make coffee and tea for the whole newsroom. See you next time!'
CLOSING = ('tatyana', 'Пока!')
STORY = [
    ('tatyana', 'А вы кто?', 'And who are you?', [(311, 'А вы кто?')], ''),
    ('editor', 'Я новый редактор отдела по культуре.', 'I am the new editor for the culture desk.', [(312, 'Я новый редактор отдела по культуре.')], ''),
    ('tatyana', 'Браво! Премию нашему отделу кадров!', 'Bravo! A bonus for our HR department!', [(313, 'Браво!'), (314, 'Премию отделу кадров.')], 'added нашему'),
    ('editor', 'Извините, можно мой телефон назад?', 'Excuse me, can I have my phone back?', [(307, 'Извините.'), (316, 'Можно телефон назад?')], 'combined cues 307 and 316'),
    ('tatyana', 'Да, конечно! Там ведь человек страдает.', 'Yes, of course! Someone is suffering in there.', [(317, 'Да, конечно'), (318, 'Там человек страдает.')], 'combined cues 317 and 318'),
    ('tatyana', 'Если нужна помощь, сразу обращайтесь к нам.', 'If you need help, just ask us right away.', [(319, 'Если какая-то помощь нужна, обращайтесь.')], 'shortened for A1'),
    ('editor', 'Читать чужие сообщения — это некультурно!', "Reading other people's messages is bad manners!", [(321, 'Читать чужие смс некультурно')], 'смс -> сообщения'),
    ('tatyana', 'Смотрите, новый редактор уже всех редактирует!', 'Look, the new editor is already editing everyone!', [(322, 'Вот, редактор.'), (323, 'Редактирует уже.')], 'combined cues 322 and 323'),
    ('tatyana', 'За это вам месяц кофейного карцера!', 'For that, you get one month of coffee detention!', [(325, 'Месяц кофейного карцера.')], 'added За это вам'),
    ('tatyana', 'Вы будете месяц носить всем чай и кофе.', 'You will bring tea and coffee to everyone for a month.', [(326, 'Это месяц разносить всем чай-кофе.')], 'simplified for A1'),
    ('tatyana', 'Мне капучино! Кто ещё хочет кофе?', 'A cappuccino for me! Who else wants coffee?', [(328, 'Мне капучино. Кто-нибудь еще что-нибудь хочет?')], 'shortened for A1'),
    ('editor', 'А мне зелёный чай, два пакетика.', 'And green tea for me, two bags.', [(330, 'А мне тоже чай. Зеленый. Два пакетика.')], 'shortened for A1'),
]
WALK = [
    (0, None, "'And who are you?' Starting a question with 'and' makes it sound direct and surprised."),
    (1, None, "'I am the new editor for the culture desk.' Russian leaves out 'am' in the present tense, linking 'I' straight to 'new editor'."),
    (2, None, "'Bravo! A bonus for our HR department!' Literally 'a bonus to our department of personnel', joking about what a great hire they made."),
    (3, None, "'Excuse me, can I have my phone back?' Starting the request with the word for 'is it possible' is the easiest polite way to ask for something."),
    (4, None, "'Yes, of course! Someone is suffering in there.' Tatyana teases him about the sad text message on his screen."),
    (5, None, "'If you need help, just ask us right away.' Literally 'if help is needed, turn to us right away'."),
    (6, None, "'Reading other people's messages is bad manners!' The word for 'bad manners' literally means 'uncultured', fitting for the new culture editor."),
    (7, None, "'Look, the new editor is already editing everyone!' Tatyana plays on the words for 'editor' and 'is editing'."),
    (8, None, "'For that, you get one month of coffee detention!' She invents a playful office punishment."),
    (9, None, "'You will bring tea and coffee to everyone for a month.' Combining 'you will' with the action verb forms the future tense for a repeated chore."),
    (10, None, "'A cappuccino for me! Who else wants coffee?' In cafés and offices, Russians order simply by saying 'to me' plus the drink."),
    (11, None, "'And green tea for me, two bags.' After the number 'two', the noun for 'tea bag' takes a special ending."),
]
