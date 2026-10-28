# Authoring module for kukhnya-s02e02-scene-06.
ID = 'kukhnya-s02e02-scene-06'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 2
SCENE = 6
TITLE = 'Заказ  (The Order)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.02'
SOURCE_FILE = 'sources/kukhnya/s02/e02.ru.dual.srt'
INTRO = "In the restaurant, a normal day is suddenly interrupted. Someone needs urgent medical help. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around The Order line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Someone needs urgent medical help. Next time you watch the episode, listen for the Russian expressions for 'pleasant' and 'appetite' — you will catch every word right away. See you next time!"
CLOSING = ('sasha', 'До свидания!')
STORY = [
    ('sasha', 'Приятного аппетита.', 'Enjoy your meal.', [(104, 'Приятного аппетита')], ''),
    ('guest', 'Саша, привет.', 'Sasha, hi.', [], ''),
    ('guest', 'Я хочу есть.', 'I want to eat.', [], ''),
    ('guest', 'Ты попросишь Калифорнию?', 'Will you ask for a California roll?', [(105, 'попросишь'), (105, 'Калифорнию')], ''),
    ('sasha', 'Да, конечно.', 'Yes, of course.', [], ''),
    ('sasha', 'Хорошо, спасибо.', 'Okay, thanks.', [(106, 'Хорошо, спасибо')], ''),
    ('sasha', 'Ой, что это?', 'Oh, what is this?', [], ''),
    ('guest', 'Человеку плохо!', 'A person is feeling bad!', [], ''),
    ('sasha', 'Что случилось?', 'What happened?', [], ''),
    ('guest', 'Ему очень плохо.', 'He is very bad.', [], ''),
    ('sasha', 'Помогите!', 'Help!', [], ''),
    ('guest', 'Скорую вызовите.', 'Call an ambulance.', [(107, 'Скорую вызовите')], ''),
    ('sasha', 'Скорую нужно вызвать.', 'We need an ambulance.', [(108, 'Скорую нужно')], ''),
]
WALK = [
    (0, None, "'Enjoy your meal.' Serving a table in the dining room, Sasha wishes the guest a pleasant meal."),
    (1, None, "'Sasha, hi.' the guest delivers a punchy conversational reaction built around the Russian word meaning 'hi'."),
    (2, None, "'I want to eat.' Another guest tells Sasha that he is hungry and ready to order."),
    (3, None, "'Will you ask for a California roll?' the guest turns a statement into a question purely through rising intonation on the word meaning 'to ask' to make the point directly in conversation."),
    (4, None, "'Yes, of course.' When the guest asks for a 'California' roll, Sasha gladly agrees to bring it."),
    (5, None, "'Okay, thanks.' She thanks the guest and turns to place the sushi order."),
    (6, None, "'Oh, what is this?' Suddenly noticing a commotion at a nearby table, Sasha gasps in alarm."),
    (7, None, "'A person is feeling bad!' A diner shouts that someone in the hall has fallen terribly ill."),
    (8, None, "'What happened?' Sasha rushes over and asks what happened to the guest."),
    (9, None, "'He feels really bad.' The bystander explains that the man is in bad shape after eating."),
    (10, None, "'Help!' Panicking, Sasha calls out to the staff for help."),
    (11, None, "'Call an ambulance.' The guest urges everyone to call an ambulance right away."),
    (12, None, "'We need an ambulance.' Sasha repeats the urgent call to get paramedics to the restaurant."),
]
