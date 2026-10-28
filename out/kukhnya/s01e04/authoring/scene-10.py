# Authoring module for kukhnya-s01e04-scene-10.
ID = 'kukhnya-s01e04-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 10
TITLE = "Детектор лжи  (The Lie Detector)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "chef": "anja", "expert": "angelina"}
LABELS = {"chef": "Шеф", "expert": "Эксперт"}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Determined to discover which kitchen staff member secretly interviewed at the rival restaurant Arcobaleno, Chef Barinov hires a polygraph examiner. Hooked up to the lie detector machine in Barinov's office, fish cook Fedya undergoes a tense interrogation. Let's listen to their conversation in Russian first."
OPENER = "Let's replay a few lines to examine key phrases and vocabulary."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "Fedya hurries out of the office, relieved that his dark secrets went undetected. Next time you watch the episode, listen for the Russian expressions for 'quite' and 'really' — you will catch every word right away. See you next time!"
CLOSING = ("chef", "Пока!")
STORY = [
    ('chef', 'Заходи, Федя. Садись на стул.', 'Come in, Fedya. Sit down on the chair.', [(114, 'Заходи')], ''),
    ('chef', 'Шеф, а что это такое?', 'Chef, what is this thing?', [(116, 'Шеф, это чего')], ''),
    ('chef', 'Это настоящий детектор лжи, Федя.', 'This is a real lie detector, Fedya.', [(117, 'Это детектор лжи, Федя')], ''),
    ('chef', 'Я должен поймать крысу на кухне.', 'I must catch the rat in the kitchen.', [(118, 'поймать крысу')], ''),
    ('expert', 'Отвечайте только «да» или «нет».', "Answer only 'yes' or 'no'.", [(120, 'Отвечайте только')], ''),
    ('chef', 'Хорошо, это мне вполне понятно.', 'Fine, that is completely clear to me.', [(121, 'Понятно')], ''),
    ('expert', 'Скажите, сегодня действительно среда?', 'Tell me, is today really Wednesday?', [(123, 'Скажите, сегодня среда')], ''),
    ('chef', 'Да, сегодня среда.', 'Yes, today is Wednesday.', [(124, 'Да')], ''),
    ('expert', 'Ваше настоящее имя Фёдор?', 'Is your real name Fyodor?', [(129, 'Ваше имя Фёдор')], ''),
    ('chef', 'Да.', 'Yes.', [(130, 'Да')], ''),
    ('chef', 'Ты ходил в соседний ресторан?', 'Did you go to the neighboring restaurant?', [(135, 'соседний ресторан')], ''),
    ('chef', 'Нет, я никуда не ходил.', 'No, I did not go anywhere.', [(137, 'Нет')], ''),
    ('chef', 'Свободен. Позови сюда Сеню.', 'You are free to go. Call Senya in here.', [(138, 'Свободен'), (139, 'позови там Сеню')], ''),
]
WALK = [
    (0, None, "'This is a real lie detector, Fedya.' Barinov announces sternly as the specialist hooks up the wires."),
    (1, None, "'Answer only 'yes' or 'no'.' the polygraph examiner instructs before beginning the baseline questions."),
    (2, None, "'Did you go to the neighboring restaurant?' Chef Barinov asks abruptly, getting to the true point of the test."),
    (3, None, "'You are free to go. Call Senya here.' Barinov orders, satisfied that Fedya is not the traitor. Now listen to the full lie detector interrogation once more. Now let's listen to the whole conversation again from start to finish."),
]
