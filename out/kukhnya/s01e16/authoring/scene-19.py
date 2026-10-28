# Authoring module for kukhnya-s01e16-scene-19.
ID = 'kukhnya-s01e16-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 19
TITLE = 'Проверка документов  (Document Check)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "Having seen right through Louis's disguise in the dining room, the migration officer demands to inspect his official work papers. When the French pastry chef admits that his documents are not in order, the inspector firmly escorts him toward Chef Barinov's office. Let's listen to their exchange in Russian."
OPENER = "Let's see how the migration officer questions Louis and orders him to the office."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That wraps up this scene from Kukhnya. Listen for these everyday Russian expressions when you watch the episode. See you next time!'
CLOSING = ('inspector', 'Пока!')
STORY = [
    ('inspector', 'Где ваше разрешение на работу?', 'Where is your work permit?', [], ''),
    ('louis', 'Мои документы лежат в кабинете шефа.', "My documents are lying in the chef's office.", [], ''),
    ('inspector', 'У вас нет нужных бумаг?', 'Do you not have the necessary papers?', [], ''),
    ('louis', 'Я просто забыл сделать новые документы.', 'I simply forgot to make new documents.', [], ''),
    ('inspector', 'Это очень большая проблема для ресторана.', 'This is a very big problem for the restaurant.', [], ''),
    ('louis', 'Я делаю здесь лучшие десерты!', 'I make the best desserts here!', [], ''),
    ('inspector', 'Закон один для всех людей.', 'The law is one for all people.', [], ''),
    ('louis', 'Что вы теперь будете делать?', 'What are you going to do now?', [], ''),
    ('inspector', 'Мне нужно поговорить с вашим начальником.', 'I need to talk to your boss.', [], ''),
    ('louis', 'Наш шеф сейчас очень занят.', 'Our chef is very busy right now.', [], ''),
    ('inspector', 'Он быстро найдёт время для меня.', 'He will quickly find time for me.', [], ''),
    ('inspector', 'Вставайте, сейчас пройдёмте со мной.', 'Get up, now come with me.', [(270, 'Пройдемте')], ''),
    ('louis', 'Хорошо, пойдёмте в кабинет шефа.', "All right, let's go to the chef's office.", [], ''),
]
WALK = [
    (0, None, "'Where is your work permit?' A direct demand is fired off, asking for official authorization to hold a job in the country."),
    (1, None, "'I simply forgot to make new documents.' Louis tries to excuse himself by claiming he merely slipped up on renewing his paperwork."),
    (2, None, "'I need to talk to your boss.' Firm and serious, the migration officer insists on speaking directly with the manager in charge."),
    (3, None, "'Get up, now come with me.' An authoritative command tells the cook to stand and follow him immediately."),
]
