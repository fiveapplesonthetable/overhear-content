ID = "kukhnya-s02e03-scene-17"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 17
TITLE = 'Недовольный гость  (A Dissatisfied Guest)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja", "guest": "angelina"}
LABELS = {"anya": "Макс", "vika": "Вика", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"
SOURCE_NOTE = "Scene 17"

INTRO = 'A demanding guest sits in the restaurant and waits for someone to assist him. He becomes increasingly annoyed by the lack of attention and decides to call a waiter.'

STORY = [
    ('guest', 'Девушка, можно вас?',
     'Miss, could you come here?',
     [], 'new'),
    ('vika', 'Да, я вас слушаю.',
     'Yes, I am listening to you.',
     [], 'new'),
    ('guest', 'У нас проблема с заказом.',
     'We have a problem with our order.',
     [], 'new'),
    ('vika', 'Что-то не так с едой?',
     'Is something wrong with the food?',
     [], 'new'),
    ('guest', 'Я просил без лука.',
     'I asked for no onions.',
     [], 'new'),
    ('vika', 'Извините, сейчас всё исправим.',
     'Sorry, we will fix everything right now.',
     [], 'new'),
    ('guest', 'И принесите ещё вина.',
     'And bring more wine.',
     [], 'new'),
    ('vika', 'Конечно, одну минуту.',
     'Of course, one minute.',
     [], 'new'),
    ('guest', 'Официанты тут вообще работают?',
     'Do waiters even work here?',
     [], 'new'),
    ('guest', 'Уважаемые.',
     'Excuse me.',
     [(281, 'Уважаемые')], 'adapted'),
    ('anya', 'Что вам угодно?',
     'What would you like?',
     [], 'new'),
    ('guest', 'Я хочу поговорить с поваром.',
     'I want to speak with the chef.',
     [], 'new'),
    ('anya', 'Я передам вашу просьбу.',
     'I will pass on your request.',
     [], 'new'),
]

OPENER = "Let us break down this interaction."

WALK = [
    (2, None,
     "'We have a problem with our order.' -- ENG The customer complains about a mistake."),
    (4, None,
     "'I asked for no onions.' -- ENG He points out the specific error in his dish."),
    (9, None,
     "'Excuse me.' -- ENG He loudly demands attention from the passing staff."),
    (11, None,
     "'I want to speak with the chef.' -- ENG He requests to see the person responsible for the kitchen."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = 'The waiter quickly approaches the unhappy customer to resolve the problem and calm him down.'
CLOSING = ('anya', 'Я передам вашу просьбу.')
