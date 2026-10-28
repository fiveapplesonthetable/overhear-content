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
INTRO = "Nagiyev has called Barinov over to show him something on a phone: a video of the chef that has gone viral. Barinov assumes the worst, and is surprised by what he hears. We'll hear it in Russian first."
OPENER = 'Here it is again, line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Barinov leaves with his job and his dignity intact. Remember that 'zvezda' means a star in the sky and a star in the film, and Russians use the one word for both. See you next time!"
CLOSING = ('barinov', 'До свидания!')
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
    (0, None, "'Look at this video.' 'Look' is the casual command. 'Video' never changes, whatever its role."),
    (1, None, "'I don't understand. Am I fired?' 'Fired' is a short masculine form, so no 'am'. The question lives on the voice."),
    (2, None, "'No, you're a star!' 'Star' is feminine. There's no 'are'."),
    (3, None, "'Why am I a star?' The same word again, in the same shape. Barinov is baffled."),
    (4, None, "'The video has a million views.' 'At the video' stands for 'has'. 'Million' is followed by the 'of' plural, 'views'."),
    (5, None, "'Everyone wants to see you.' 'They want' ends in 'yat'. 'You' takes the 'a' form, 'vas'."),
    (6, None, "'Do we have many guests?' 'At us' stands for 'we have'. After 'many', 'guests' takes the 'ey' ending."),
    (7, None, "'Yes, all the tables are taken.' 'Taken' is a plural short form. 'Tables' are little tables, plural."),
    (8, None, "'You're very popular now.' 'Popular' is a short masculine form. 'Now' ends the line."),
    (9, None, "'So can I go on working?' 'Can I' is one word. 'Further' means 'on'."),
    (10, None, "'Of course! Go to the kitchen.' 'Go' is the casual command. 'To the kitchen' uses 'on' and a 'u' ending."),
    (11, None, "'Thanks, I'll go and work.' 'I'll go' is a future form. 'Work' is the plain form."),
    (12, None, "'I expect a tasty lunch today.' 'Wait' stands for 'expect'. 'Tasty lunch' has masculine endings."),
    (13, None, "'It'll be done, my boss.' 'Will be done' is a neuter short form. 'Boss' is borrowed."),
]
