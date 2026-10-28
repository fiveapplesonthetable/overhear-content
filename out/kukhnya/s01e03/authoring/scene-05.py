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
    ('barinov', 'Что опять стряслось, огузок?', 'What happened again, runt?', [], ''),
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
    (0, None, '\'Chef, I have big problems.\' "At me" is Russian\'s way of saying "I have". Both "big" and "problems" take the plural ending.'),
    (1, None, '\'What happened again, runt?\' "Happened" is a colloquial one, used for bad surprises. Barinov calls him by the nickname, "oguzok".'),
    (2, None, '\'A terrible prosecutor is looking for me.\' Max puts "me" first, so you hear the fear. "Terrible" is the "Terrible" of "Ivan the Terrible", and it means "formidable".'),
    (3, None, '\'And why is he looking for you?\' "For what" is the Russian for "why" when you mean "what for". The small "zhe" sharpens the question.'),
    (4, None, '\'He knows about me and Vika.\' "About" is a casual short word here. Vika turns into "Viku", because she is the thing he knows about.'),
    (5, None, '\'You slept with someone else\'s woman?\' "Someone else\'s" is useful for anything that belongs to another person. The chef says it bluntly.'),
    (6, None, '\'I did not know that she is married.\' "Married", for a woman, comes from "behind a husband". A married man uses a different word, with "wife" at its root.'),
    (7, None, '\'He was the most talented cook.\' Barinov switches to "was" for the eulogy. "The most talented" is the "samyy" pattern again.'),
    (8, None, '\'Whom I ever knew.\' "Whom" takes the person-object shape. "Ever" is built with "-libo", just like "-nibud\'" and "-to".'),
    (9, None, '\'Chef, are you already burying me?\' Max uses the polite "you" with the chef. "Already" is the small word of impatience.'),
    (10, None, '\'You don\'t mess with a prosecutor.\' Word for word it\'s "with a prosecutor jokes are bad". It\'s a fixed phrase, and you can use it for anyone dangerous.'),
    (11, None, '\'He will quickly send you behind bars.\' Russian says "behind the grille", and it means jail. The "will send" at the end carries the threat.'),
    (12, None, '\'What should I do now?\' "What then to me to do" is the pattern for asking for advice. It\'s one of the most useful questions you can learn.'),
    (13, None, '\'Go work and do not chat.\' Two commands in a row, "go work", then "don\'t chatter". The slang "chatter" is the one Max used in the first episode.'),
]
