# Authoring module for kukhnya-s01e01-scene-10.
ID = 'kukhnya-s01e01-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 10
TITLE = 'Знакомое лицо в зале  (A Familiar Face in the Hall)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "Arriving at Claude Monet for his job interview, Max steps into the elegant dining hall and speaks with a waitress. Looking across the room, he is horrified to spot Vika—his date from the night before—commanding the floor as the art director. Let's listen to their conversation in Russian first."
OPENER = "Let's replay a few lines to examine key phrases and grammar."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max quickly retreats toward the corridor to avoid being spotted. Next time you watch the episode, listen for the Russian expressions for 'art director' and 'meeting' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Здравствуйте! Я пришёл на встречу.', 'Hello! I arrived for an appointment.', [], ''),
    ('sasha', 'Добрый день! Вы к Дмитрию Владимировичу?', 'Good day! Are you here to see Dmitry Vladimirovich?', [], ''),
    ('max', 'Да, он приглашал меня на работу.', 'Yes, he invited me for a job.', [], ''),
    ('sasha', 'Хозяин пока занят на кухне.', 'The owner is busy in the kitchen for now.', [], ''),
    ('max', 'Понятно. А кто руководит залом?', 'Understood. And who is managing the dining room?', [], ''),
    ('sasha', 'Вон та строгая девушка у окна.', 'That strict young woman over by the window.', [], ''),
    ('max', 'Как зовут эту красивую девушку?', "What is this beautiful young woman's name?", [], ''),
    ('sasha', 'Это Виктория Сергеевна, наш арт-директор.', 'This is Viktoria Sergeyevna, our art director.', [], ''),
    ('max', 'О нет, какая неприятная ситуация!', 'Oh no, what an unpleasant situation!', [(72, 'Дерьмо')], ''),
    ('sasha', 'Что случилось? Вы так побледнели!', 'What happened? You turned so pale!', [], ''),
    ('max', 'Ничего страшного, голова кружится.', 'Nothing terrible, my head is spinning.', [], ''),
    ('sasha', 'Хотите сесть за свободный столик?', 'Would you like to sit at an available table?', [], ''),
    ('max', 'Нет, спасибо, я отойду назад.', 'No, thank you, I will step back.', [], ''),
]
WALK = [
    (0, None, "'Are you here to see Dmitry Vladimirovich?' Sasha asks a polite question to figure out if the visitor has a scheduled appointment."),
    (1, None, "'This is Viktoria Sergeyevna, our art director.' Pointing out her manager, the waitress formally introduces the woman running the restaurant floor."),
    (2, None, "'Oh no, what an unpleasant situation!' Max quietly panics upon realizing that his one-night stand holds a high-ranking position here."),
    (3, None, "'Would you like to sit at an available table?' Offering standard hospitality, the staff member invites the distressed man to take a seat."),
]
