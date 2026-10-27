ID = "kukhnya-s01e20-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 11
TITLE = "Секрет шефа  (The Chef's Secret)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'chef': 'anja', 'vika': 'angelina'}
LABELS = {'anya': 'Нагиев', 'chef': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 11"

INTRO = "The restaurant owner calls the Chef to his table and tells him that he is now very famous. They talk about the video on the internet, which has many views. The Chef is very surprised by this news."
OPENER = "Now let's examine this conversation line by line."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "The Chef is very happy that he is not fired. He goes back to the kitchen to cook food for all the new guests."

STORY = [
    ("anya", "Посмотри на это видео.", "Look at this video.", [], "adapted"),
    ("chef", "Я не понимаю. Я уволен?", "I don't understand. Am I fired?", [], "adapted"),
    ("anya", "Нет, ты звезда!", "No, you are a star!", [], "adapted"),
    ("chef", "Почему я звезда?", "Why am I a star?", [], "adapted"),
    ("anya", "У видео миллион просмотров.", "The video has a million views.", [], "adapted"),
    ("vika", "Все хотят видеть вас.", "Everyone wants to see you.", [], "adapted"),
    ("chef", "У нас много гостей?", "Do we have many guests?", [], "adapted"),
    ("vika", "Да, все столики заняты.", "Yes, all tables are taken.", [], "adapted"),
    ("anya", "Ты очень популярен сейчас.", "You are very popular now.", [], "adapted"),
    ("chef", "Значит, я могу работать дальше?", "So, can I work further?", [], "adapted"),
    ("anya", "Конечно! Иди на кухню.", "Of course! Go to the kitchen.", [], "adapted"),
    ("chef", "Спасибо, я пойду работать.", "Thank you, I will go work.", [], "adapted"),
    ("anya", "Жду вкусный обед сегодня.", "I expect a tasty lunch today.", [], "adapted"),
    ("chef", "Будет сделано, мой босс.", "It will be done, my boss.", [], "adapted"),
]

WALK = [
    (0, None, "'Look at this video.' -- He tells the Chef to look at the video."),
    (1, None, "'I don't understand. Am I fired?' -- He asks if he is fired."),
    (2, None, "'No, you are a star!' -- He says that he is a star."),
    (3, None, "'Why am I a star?' -- He asks why he is a star."),
    (4, None, "'The video has a million views.' -- He says the video has a million views."),
    (5, None, "'Everyone wants to see you.' -- She says everyone wants to see him."),
    (6, None, "'Do we have many guests?' -- He asks if they have many guests."),
    (7, None, "'Yes, all tables are taken.' -- She says all tables are taken."),
    (8, None, "'You are very popular now.' -- He says he is very popular now."),
    (9, None, "'So, can I work further?' -- He asks if he can work further."),
    (10, None, "'Of course! Go to the kitchen.' -- He tells him to go to the kitchen."),
    (11, None, "'Thank you, I will go work.' -- He says he will go work."),
    (12, None, "'I expect a tasty lunch today.' -- He expects a tasty lunch today."),
    (13, None, "'It will be done, my boss.' -- He says it will be done."),
]

CLOSING = ("chef", "Будет сделано, мой босс.")
