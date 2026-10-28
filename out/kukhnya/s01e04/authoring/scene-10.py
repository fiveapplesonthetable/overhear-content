# Authoring module for kukhnya-s01e04-scene-10.
ID = 'kukhnya-s01e04-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 10
TITLE = 'Детектор лжи  (The Lie Detector)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'expert': 'Эксперт', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = 'The chef is determined to find the traitor, so he has hired a lie-detector expert and set up a machine in his office. Fedya, the fish cook, is the first to be questioned. Here is the Russian first.'
OPENER = "Let's go through the questioning."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Fedya passes the test and is sent to fetch Senya. The phrase to keep is "detektor lzhi", "lie detector", where "lozh\'" is a lie.'
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('barinov', 'Заходи, Федя. Садись на стул.', 'Come in, Fedya. Sit down on the chair.', [(114, 'Заходи')], ''),
    ('fedya', 'Шеф, а что это такое?', 'Chef, what is this thing?', [(116, 'Шеф, это чего')], ''),
    ('barinov', 'Это настоящий детектор лжи, Федя.', 'This is a real lie detector, Fedya.', [(117, 'Это детектор лжи, Федя')], ''),
    ('barinov', 'Я должен поймать крысу на кухне.', 'I must catch the rat in the kitchen.', [(118, 'поймать крысу')], ''),
    ('expert', 'Отвечайте только «да» или «нет».', "Answer only 'yes' or 'no'.", [(120, 'Отвечайте только')], ''),
    ('fedya', 'Хорошо, это мне вполне понятно.', 'Fine, that is completely clear to me.', [(121, 'Понятно')], ''),
    ('expert', 'Скажите, сегодня действительно среда?', 'Tell me, is today really Wednesday?', [(123, 'Скажите, сегодня среда')], ''),
    ('fedya', 'Да, сегодня среда.', 'Yes, today is Wednesday.', [(124, 'Да')], ''),
    ('expert', 'Ваше настоящее имя Фёдор?', 'Is your real name Fyodor?', [(129, 'Ваше имя Фёдор')], ''),
    ('fedya', 'Да.', 'Yes.', [(130, 'Да')], ''),
    ('barinov', 'Ты ходил в соседний ресторан?', 'Did you go to the neighboring restaurant?', [(135, 'соседний ресторан')], ''),
    ('fedya', 'Нет, я никуда не ходил.', 'No, I did not go anywhere.', [(137, 'Нет')], ''),
    ('barinov', 'Свободен. Позови сюда Сеню.', 'You are free to go. Call Senya in here.', [(138, 'Свободен'), (139, 'позови там Сеню')], ''),
]
WALK = [
    (0, None, '\'Come in, Fedya. Sit down on the chair.\' "Zakhodi" is "come in", with "za-" for going inside. "Sadis\'" is "seat yourself", with -s\' for the self.'),
    (1, None, '\'Chef, what is this thing?\' "Chto eto takoye?" is "what is this such?", a handy way to ask what something is.'),
    (2, None, '\'This is a real lie detector, Fedya.\' "Lozh\'", a lie, drops its vowel in "lzhi", of a lie. The machine is "detektor lzhi", detector of a lie.'),
    (3, None, '\'I must catch the rat in the kitchen.\' "Krysa", rat, is also Russian slang for a traitor. "Poymat\'" is "to catch", and "dolzhen" is "must" for a man.'),
    (4, None, '\'Answer only yes or no.\' "Otvechayte" is a command with the polite -te. "Tol\'ko" is "only", and "ili" is "or".'),
    (5, None, '\'Fine, that is completely clear to me.\' "Vpolne" is "in full", from "polnyy", full. "Mne ponyatno", to me it\'s clear, needs no "I".'),
    (6, None, '\'Tell me, is today really Wednesday?\' "Sreda", Wednesday, is related to "seredina", middle, since it falls mid-week. "Deystvitel\'no" is "really".'),
    (7, None, '\'Yes, today is Wednesday.\' Fedya repeats "sreda" with no verb, because Russian leaves out "is".'),
    (8, None, '\'Is your real name Fyodor?\' "Fyodor" is the full name behind "Fedya". "Nastoyashcheye", real, ends in -eye because "imya", name, is neuter.'),
    (9, None, '\'Yes.\' Just "da", which is what the expert asked for.'),
    (10, None, '\'Did you go to the neighboring restaurant?\' "Khodil" is "went and came back". "Sosedniy", neighbouring, is from "sosed", neighbour.'),
    (11, None, '\'No, I did not go anywhere.\' "Nikuda ne khodil" is "nowhere not went", the double negative.'),
    (12, None, '\'You are free to go. Call Senya in here.\' "Svoboden" is the man\'s short "free". "Pozovi" is "call", and "Senya" turns into "Senyu" as the one called.'),
]
