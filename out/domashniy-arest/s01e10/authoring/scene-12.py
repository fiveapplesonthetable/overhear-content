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
    (0, None, "'And who are you?' Starting a question with \"and\" makes it sound direct and surprised when a stranger speaks up."),
    (1, None, "'I am the new editor for the culture desk.' Russian leaves out \"am\" here, linking \"I\" straight to \"new editor\" as he introduces himself."),
    (2, None, "'Bravo! A bonus for our HR department!' Literally \"a bonus to our personnel department\", joking about what a prize hire they made."),
    (3, None, "'Excuse me, can I have my phone back?' Asking \"is it possible my phone back\" is the easiest polite way to retrieve what is yours."),
    (4, None, "'Yes, of course! Someone is suffering in there.' Tatyana teases him about the dramatic text messages lighting up his screen."),
    (5, None, "'If you need help, just ask us right away.' Still keeping a straight face, she offers the whole newsroom as his personal advice column."),
    (6, None, "'Reading other people's messages is bad manners!' The Russian word for \"bad manners\" literally means \"uncultured\", which fits the new culture editor."),
    (7, None, "'Look, the new editor is already editing everyone!' She plays on the words for \"editor\" and \"is editing\" to mock his lecture."),
    (8, None, "'For that, you get one month of coffee detention!' Combining \"coffee\" with the word for a prison solitary cell, she invents an office punishment on the spot."),
    (9, None, "'You will bring tea and coffee to everyone for a month.' Here is what \"coffee detention\" actually means: playing office waiter for thirty days."),
    (10, None, "'A cappuccino for me! Who else wants coffee?' Without missing a beat, she places the very first order by saying \"to me a cappuccino\"."),
    (11, None, "'And green tea for me, two bags.' Accepting his fate, the new guy puts in his own order for a double-bagged green tea."),
]
