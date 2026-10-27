ID = "kukhnya-s01e17-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 19
TITLE = "Сюрприз для всех  (A Surprise for Everyone)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'max': 'anja'}
LABELS = {'anya': 'Vika', 'max': 'Max'}

INTRO = 'Vika calls Max, who is waiting outside her apartment with unexpected guests. We will hear it in Russian first, do not worry about catching every word.'
OPENER = "Let's walk through it. Vika is looking for Max."
TRANSITION = "Now let's hear the scene once more."
OUTRO = 'Max is about to ruin the evening. See you next time.'

STORY = [
    ('anya', 'Макс, ну ты где?', 'Max, well where are you?', [(295, 'Макс, ну ты где?')], ''),
    ('anya', 'Ты скоро?', 'Are you coming soon?', [(295, 'Скоро ты?')], 'Simplified'),
    ('max', 'Я уже здесь.', 'I am already here.', [(296, 'Я уже здесь.')], ''),
    ('anya', 'Почему ты там стоишь?', 'Why are you standing there?', [], ''),
    ('max', 'Я жду своих друзей.', 'I am waiting for my friends.', [], ''),
    ('anya', 'Каких друзей?', 'What friends?', [], ''),
    ('max', 'Настю и Костю.', 'Nastya and Kostya.', [], ''),
    ('anya', 'Ты их позвал сюда?', 'Did you invite them here?', [], ''),
    ('max', 'Да, это сюрприз.', 'Yes, it is a surprise.', [], ''),
    ('anya', 'Я не готова к гостям.', 'I am not ready for guests.', [], ''),
    ('max', 'Всё будет хорошо.', 'Everything will be fine.', [], ''),
    ('anya', 'Заходи быстрее.', 'Come in faster.', [], ''),
]

WALK = [
    (0, None, "'Max, well where are you?' Vika calls him impatiently."),
    (1, None, "'Are you coming soon?' She wants to know his ETA."),
    (2, None, "'I am already here.' He is waiting outside her door."),
    (3, None, "'Why are you standing there?' She is confused by his delay."),
    (4, None, "'I am waiting for my friends.' He reveals he is not alone."),
    (5, None, "'What friends?' She has no idea what he is talking about."),
    (6, None, "'Nastya and Kostya.' He names his colleagues from the restaurant."),
    (7, None, "'Did you invite them here?' She is shocked by his boldness."),
    (8, None, "'Yes, it is a surprise.' He thinks it is a great idea."),
    (9, None, "'I am not ready for guests.' She is unprepared for a party."),
    (10, None, "'Everything will be fine.' He tries to reassure her."),
    (11, None, "'Come in faster.' She tells him to enter the apartment."),
]

CLOSING = ('anya', 'Скорее.')
