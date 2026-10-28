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
OUTRO = 'Fedya walks out of the office relieved that the machine did not catch his secrets. The word to keep is "pravda", truth, which you may already know.'
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
    (0, None, '\'Come in, Fedya. Sit down on the chair.\' "Zakhodi" is "come in", with "za-", and "sadis\'" is "sit yourself down", so the "-s\'" at the end is a little "self".'),
    (1, None, '\'Chef, what is this thing?\' "Chto eto takoye" is "what is this such", a very handy way to ask what something is.'),
    (2, None, '\'This is a real lie detector, Fedya.\' "Lozh\'" is a lie, and "lzhi" is "of a lie", with some letters dropped. The machine\'s name is a phrase, "detector of lies".'),
    (3, None, '\'I must catch the rat in the kitchen.\' Russians say "rat" for a traitor, just as English does. "Poymat\'" is "to catch".'),
    (4, None, '\'Answer only yes or no.\' "Otvechayte" is the polite command, with the "-te".'),
    (5, None, '\'Fine, that is completely clear to me.\' "Vpolne" is "in full", so "completely". "Ponyatno" means "it\'s clear" and needs no "I".'),
    (6, None, '\'Tell me, is today really Wednesday?\' "Sreda" is Wednesday, and it also means "middle", since it\'s the middle of the week. "Deystvitel\'no" is "really".'),
    (7, None, '\'Yes, today is Wednesday.\' Fedya answers with the same word and no verb, because Russian leaves out "is".'),
    (8, None, '\'Is your real name Fyodor?\' The expert asks for Fedya\'s real name, which is the full form, "Fyodor", of the short "Fedya". "Real" ends in a neuter "-oye", because "imya", name, is neuter.'),
    (9, None, '\'Yes.\' "Da" is the simplest word in the scene. It\'s the one he is allowed to say.'),
    (10, None, '\'Did you go to the neighboring restaurant?\' "Khodil" is "went and came back", the round-trip kind of "go". "Sosedniy" comes from "sosed", neighbour.'),
    (11, None, '\'No, I did not go anywhere.\' "Nikuda" is "nowhere", and with "ne" it\'s the double negative. Fedya answers with a bigger "no" than the question needed.'),
    (12, None, '\'You are free to go. Call Senya in here.\' "Svoboden" is "free", the short form for a man. "Pozovi" is "call", a command, and "Senyu" is the object form of "Senya".'),
]
