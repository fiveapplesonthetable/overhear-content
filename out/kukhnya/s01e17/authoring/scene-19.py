# Authoring module for kukhnya-s01e17-scene-19.
ID = 'kukhnya-s01e17-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 19
TITLE = 'Сюрприз для всех  (A Surprise for Everyone)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "Max has plans for the evening. Vika is waiting for him at home for a quiet dinner, but he has brought his friends along as a surprise. We'll hear their phone call in Russian first."
OPENER = "Let's go back over the phone call, slowly."
TRANSITION = 'Now the phone call once more, without a break.'
OUTRO = 'Vika is not ready for guests, and Max is about to find out how much. "Vsyo budet khorosho", everything will be fine, is what Russians say right before it isn\'t. See you next time!'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Макс, ну ты где?', 'Max, well where are you?', [(295, 'Макс, ну ты где?')], ''),
    ('vika', 'Ты скоро?', 'Are you coming soon?', [(295, 'Скоро ты?')], ''),
    ('max', 'Я уже здесь.', 'I am already here.', [(296, 'Я уже здесь.')], ''),
    ('vika', 'Почему ты там стоишь?', 'Why are you standing there?', [], ''),
    ('max', 'Я жду своих друзей.', 'I am waiting for my friends.', [], ''),
    ('vika', 'Каких друзей?', 'What friends?', [], ''),
    ('max', 'Настю и Костю.', 'Nastya and Kostya.', [], ''),
    ('vika', 'Ты их позвал сюда?', 'Did you invite them here?', [], ''),
    ('max', 'Да, это сюрприз.', 'Yes, it is a surprise.', [], ''),
    ('vika', 'Я не готова к гостям.', 'I am not ready for guests.', [], ''),
    ('max', 'Всё будет хорошо.', 'Everything will be fine.', [], ''),
    ('vika', 'Заходи быстрее.', 'Come in faster.', [], ''),
]
WALK = [
    (0, None, '\'Max, where are you?\' "Nu" adds impatience, and "ty gde?" is literally "you where?".'),
    (1, None, '\'Will you be long?\' "Ty skoro?" is literally "you soon?", with no word for coming at all.'),
    (2, None, '\'I\'m already here.\' "Uzhe" means already, and "zdes" means here.'),
    (3, None, '\'Why are you standing there?\' "Stoish" comes from "stoyat", to stand, the word Barinov barked earlier.'),
    (4, None, '\'I\'m waiting for my friends.\' "Zhdu", I\'m waiting, takes the friends straight after it, with no "for".'),
    (5, None, '\'What friends?\' "Kakikh druzey" copies the ending of "svoikh druzey" in Max\'s line.'),
    (6, None, '\'Nastya and Kostya.\' Both names switch "-ya" to "-yu", since they\'re still the people being waited for.'),
    (7, None, '\'Did you invite them here?\' "Pozval", called over, comes from "zvat", to call. "Ikh" means them.'),
    (8, None, '\'Yes, it\'s a surprise.\' "Syurpriz" is borrowed from French, like many party words.'),
    (9, None, '\'I\'m not ready for guests.\' "Gotova", ready, ends in "-a" for a woman. "K gostyam" is "for guests", literally "towards guests".'),
    (10, None, '\'Everything will be fine.\' "Vsyo budet khorosho" is the classic Russian reassurance.'),
    (11, None, '\'Hurry up and come in.\' "Zakhodi" is "come in", and "bystree", faster, turns it into "hurry up".'),
]
