# Authoring module for kukhnya-s01e03-scene-05.
ID = 'kukhnya-s01e03-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 5
TITLE = 'Паника на кухне  (Panic in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "Max rushes into the kitchen in a panic. A prosecutor, Vika's ex-husband, is after him, and he tells the chef. Barinov has little sympathy, and starts speaking about Max as though he were already dead. This is the Russian first."
OPENER = "Now let's go over the chef's joke."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'The chef sends Max back to work, which is the best advice a cynic can give. You\'ve learned the phrase for "you don\'t joke with a prosecutor".'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Шеф, у меня большие проблемы.', 'Chef, I have big problems.', [], ''),
    ('barinov', 'Что опять стряслось, огузок?', 'What happened again, Oguzok?', [], ''),
    ('max', 'Меня ищет грозный прокурор.', 'A terrible prosecutor is looking for me.', [], ''),
    ('barinov', 'И за что же он тебя ищет?', 'And why is he looking for you?', [], ''),
    ('max', 'Он знает про меня и Вику.', 'He knows about me and Vika.', [], ''),
    ('barinov', 'Ты спал с чужой женщиной?', "You slept with someone else's woman?", [(162, 'спал с чужой')], ''),
    ('max', 'Я не знал, что она замужем.', 'I did not know that she is married.', [], ''),
    ('barinov', 'Это был самый талантливый повар.', 'He was the most talented cook.', [(161, 'Это был самый талантливый')], ''),
    ('barinov', 'Которого я когда-либо знал.', 'Whom I ever knew.', [(161, 'которого я знал')], ''),
    ('max', 'Шеф, вы меня уже хороните?', 'Chef, are you already burying me?', [], ''),
    ('barinov', 'С прокурором шутки плохи.', "You don't mess with a prosecutor.", [], ''),
    ('barinov', 'Он тебя быстро за решётку отправит.', 'He will quickly send you behind bars.', [], ''),
    ('max', 'Что же мне теперь делать?', 'What should I do now?', [], ''),
    ('barinov', 'Иди работай и не болтай.', 'Go work and do not chat.', [], ''),
]
WALK = [
    (0, None, '\'Chef, I have big problems.\' "U menya", "at me", is the Russian "I have". "Bol\'shiye problemy" puts the plural -iye and -y on both words.'),
    (1, None, '\'What happened again, Oguzok?\' "Stryaslos\'" is a colloquial "happened", kept for unpleasant surprises. "Opyat\'" is "again", and the chef uses his nickname for Max.'),
    (2, None, '\'A terrible prosecutor is looking for me.\' "Menya ishchet" puts "me" first, then "looks for". "Groznyy" is the tsar\'s title that English gives as "the Terrible", and it means fearsome.'),
    (3, None, '\'And why is he looking for you?\' "Za chto" is "for what", the "why" you ask about a punishment. "Zhe" sharpens the question.'),
    (4, None, '\'He knows about me and Vika.\' "Pro" is the spoken word for "about". After it, "Vika" becomes "Viku", and "ya" becomes "menya".'),
    (5, None, '\'You slept with someone else\'s woman?\' "Spal s" is "slept with", and after "s" the words take -oy: "s chuzhoy zhenshchinoy". "Chuzhoy" is "someone else\'s".'),
    (6, None, '\'I did not know that she is married.\' "Zamuzhem", for a woman, is "za muzhem", behind a husband. A married man is "zhenat", from "zhena", wife.'),
    (7, None, '\'He was the most talented cook.\' "Eto byl" is "this was", and Barinov talks about Max in the past. "Samyy talantlivyy" is "the most talented".'),
    (8, None, '\'Whom I ever knew.\' "Kotorogo", whom, is "kotoryy" in its object shape for a person. "Kogda-libo" is "ever", "kogda", when, with -libo.'),
    (9, None, '\'Chef, are you already burying me?\' Max says "vy" to the chef. "Khoronite" is "you bury", and "uzhe" is "already".'),
    (10, None, '\'You don\'t mess with a prosecutor.\' "S prokurorom shutki plokhi" is "with a prosecutor jokes are bad". It\'s a fixed phrase, and "prokuror" can be swapped for anyone dangerous.'),
    (11, None, '\'He will quickly send you behind bars.\' "Za reshyotku" is "behind the grille", which means prison. "Otpravit" is "will send".'),
    (12, None, '\'What should I do now?\' "Chto mne delat\'?" is "what to me to do?", the pattern for asking advice. "Teper\'" is "now", and "zhe" adds despair.'),
    (13, None, '\'Go work and do not chat.\' "Idi rabotay" puts two commands side by side, "go" and "work". "Ne boltay" is "don\'t chatter", from "boltat\'".'),
]
