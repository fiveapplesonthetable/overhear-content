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
INTRO = "The inspector has seen through Louis, and now he asks for the one thing a guest wouldn't have to show: his work permit. Louis explains that his papers are somewhere else, and things go downhill from there. First, the Russian."
OPENER = "Let's go through it in order."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The inspector politely marches Louis off to see the chef. Next time you hear someone say 'proydyomte', which is the polite way to say 'come along', you'll know what it is. See you next time!"
CLOSING = ('inspector', 'До свидания!')
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
    (0, None, "'Where is your work permit?' 'Permit' comes from the verb 'to allow', so it's a permission. 'For work' is two small words, with the work in a form ending in 'u'."),
    (1, None, "'My documents are in the chef's office.' Russians say that papers 'lie' somewhere, as if they were people having a rest. The chef's office has two endings, 'e' for 'in' and 'a' for 'of the chef'."),
    (2, None, "'Don't you have the necessary papers?' After 'there isn't', the missing thing takes a different ending, here on both 'necessary' and 'papers'. The first words are the 'at you there isn't' pattern."),
    (3, None, "'I simply forgot to make new documents.' 'Forgot' has the masculine 'l', and it is followed by the plain 'to make', as in English. 'New documents' are plural, and so are the endings."),
    (4, None, "'This is a very big problem for the restaurant.' 'Big' ends in 'aya' because 'problem' is feminine. 'For the restaurant' is a short word and the 'a' ending."),
    (5, None, "'I make the best desserts here!' 'Best' is irregular, and it doesn't look like 'good'. 'Desserts' is plural, so it has a 'y' ending."),
    (6, None, "'The law is one for all people.' It has no 'is' and is shaped like a proverb. 'For all people' puts both words in the plural 'for' form."),
    (7, None, "'What are you going to do now?' 'Will you do' is made from 'will be' plus 'do', as in English. 'Now' is a word you'll hear every day."),
    (8, None, "'I need to speak to your boss.' The pattern is 'to me needed', then 'to have a talk' with the 'po' prefix that makes it a short chat. 'With your boss' has an 'im' ending."),
    (9, None, "'Our chef is very busy right now.' 'Busy' is a short form, and the ending would change for a woman. 'Right now' is a good one-word reply to a request for someone's time."),
    (10, None, "'He will quickly find time for me.' 'Will find' is a future made from a finished action. The 'me' after 'for' has the ending that Russian puts on it whenever it is the one affected."),
    (11, None, "'Get up, now come with me.' The first word is the polite plural order for 'stand up'. The second word, with the 'te' at the end, is the formal 'come along'."),
    (12, None, "'Alright, let's go to the chef's office.' Louis uses the same 'te' form but this time as 'let's go'. The office doesn't change since it's a direction."),
]
