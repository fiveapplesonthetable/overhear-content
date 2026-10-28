# Authoring module for kukhnya-s01e11-scene-11.
ID = 'kukhnya-s01e11-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 11
TITLE = "Гость Насти  (Nastya's Guest)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'sasha': 'Саша', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "Noticing an unfamiliar man sitting quietly at a corner table with a notebook, Victoria becomes increasingly suspicious. She quickly calls over waitress Sasha to investigate who the silent visitor is and which server is assigned to his table. Let's listen to their urgent hallway exchange in Russian."
OPENER = "Let's examine how Victoria questions Sasha about the quiet man taking notes in the dining area."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That wraps up this scene from Kukhnya. Listen for these everyday Russian expressions when you watch the episode. See you next time!'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Саша, подойди сюда на секунду.', 'Sasha, come over here for a second.', [], ''),
    ('sasha', 'Что случилось, Виктория Сергеевна?', 'What happened, Victoria Sergeyevna?', [], ''),
    ('vika', 'Кто сидит за пятым столиком?', 'Who is sitting at the fifth table?', [], ''),
    ('sasha', 'Там сидит довольно странный мужчина.', 'A rather strange man is sitting there.', [], ''),
    ('vika', 'Почему он ничего не заказывает?', 'Why is he not ordering anything?', [], ''),
    ('sasha', 'Я не знаю, это гость Насти.', "I do not know, this is Nastya's guest.", [(159, 'Я не знаю')], ''),
    ('vika', 'Она уже подошла к нему?', 'Did she already approach him?', [], ''),
    ('sasha', 'Да, она только что дала меню.', 'Yes, she just gave him the menu.', [], ''),
    ('vika', 'Он внимательно изучает наш зал?', 'Is he carefully studying our hall?', [], ''),
    ('sasha', 'Он постоянно пишет в свой блокнот.', 'He is constantly writing in his notebook.', [], ''),
    ('vika', 'Это очень похоже на проверку.', 'This looks very much like an inspection.', [], ''),
    ('sasha', 'Мне позвать Настю к вам?', 'Should I call Nastya to you?', [], ''),
    ('vika', 'Да, позови её прямо сейчас.', 'Yes, call her right now.', [], ''),
]
WALK = [
    (0, None, "'Who is sitting at the fifth table?' Vika notices someone new. She wants to know the identity of the person at table five."),
    (1, None, "'I do not know, this is Nastya's guest.' Sasha has no idea who the man is. He points out that the other waitress is serving that table."),
    (2, None, "'He is constantly writing in his notebook.' He shares an observation. The man keeps writing things down in a little book."),
    (3, None, "'This looks very much like an inspection.' Vika gets suspicious right away. To her, taking notes looks exactly like what a critic would do."),
]
