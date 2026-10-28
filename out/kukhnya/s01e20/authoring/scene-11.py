# Authoring module for kukhnya-s01e20-scene-11.
ID = 'kukhnya-s01e20-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 11
TITLE = "Секрет шефа  (The Chef's Secret)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = 'The restaurant owner calls the Chef to his table and tells him that he is now very famous. They talk about the video on the internet, which has many views. The Chef is very surprised by this news.'
OPENER = "Now let's examine this conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The Chef is very happy that he is not fired. He goes back to the kitchen to cook food for all the new guests. Next time you watch the episode, listen for the Russian expressions for 'to have a look' and 'video' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('nagiyev', 'Посмотри на это видео.', 'Look at this video.', [(154, 'Ах ты красавица.')], ''),
    ('barinov', 'Я не понимаю. Я уволен?', "I don't understand. Am I fired?", [], ''),
    ('nagiyev', 'Нет, ты звезда!', 'No, you are a star!', [], ''),
    ('barinov', 'Почему я звезда?', 'Why am I a star?', [], ''),
    ('nagiyev', 'У видео миллион просмотров.', 'The video has a million views.', [], ''),
    ('vika', 'Все хотят видеть вас.', 'Everyone wants to see you.', [], ''),
    ('barinov', 'У нас много гостей?', 'Do we have many guests?', [], ''),
    ('vika', 'Да, все столики заняты.', 'Yes, all tables are taken.', [], ''),
    ('nagiyev', 'Ты очень популярен сейчас.', 'You are very popular now.', [], ''),
    ('barinov', 'Значит, я могу работать дальше?', 'So, can I work further?', [], ''),
    ('nagiyev', 'Конечно! Иди на кухню.', 'Of course! Go to the kitchen.', [], ''),
    ('barinov', 'Спасибо, я пойду работать.', 'Thank you, I will go work.', [], ''),
    ('nagiyev', 'Жду вкусный обед сегодня.', 'I expect a tasty lunch today.', [], ''),
    ('barinov', 'Будет сделано, мой босс.', 'It will be done, my boss.', [], ''),
]
WALK = [
    (0, None, "'Look at this video.' Nagiyev immediately shoves a video in his chef's face."),
    (1, None, "'I don't understand. Am I fired?' Barinov starts to object or express confusion."),
    (2, None, "'No, you are a star!' Nagiyev excitedly declares that Viktor is now famous."),
    (3, None, "'Why am I a star?' Barinov is totally confused as to why he would be considered a star."),
    (4, None, "'The video has a million views.' Nagiyev explains the massive online success of the clip."),
    (5, None, "'Everyone wants to see you.' Vika chimes in to confirm his sudden burst of popularity."),
    (6, None, "'Do we have many guests?' Barinov checks if this internet fame translates to actual restaurant customers."),
    (7, None, "'Yes, all tables are taken.' Vika confirms the dining room is completely packed."),
    (8, None, "'You are very popular now.' Nagiyev reiterates just how famous his chef has become."),
    (9, None, "'So, can I work further?' Barinov just wants to get back to his kitchen and asks to leave."),
    (10, None, "'Of course! Go to the kitchen.' Nagiyev happily dismisses him to capitalize on the rush."),
    (11, None, "'Thank you, I will go work.' Barinov politely excuses himself to return to his duties."),
    (12, None, "'I expect a tasty lunch today.' Nagiyev sets high expectations for the day's service."),
    (13, None, "'It will be done, my boss.' Barinov promises to deliver, addressing him respectfully."),
]
