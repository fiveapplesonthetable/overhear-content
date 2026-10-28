# Authoring module for kukhnya-s01e04-scene-07.
ID = 'kukhnya-s01e04-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = 'Костя влюбился  (Kostya Is in Love)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Max notices that Kostya keeps staring at Nastya, and he decides to help. He teases his friend until Kostya admits he likes her, and then pushes him into giving her a compliment. Here's the Russian first."
OPENER = "Let's go through the matchmaking."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Kostya gets a compliment back, and a lot more confidence than before. Remember "ona mne nravitsya", "I like her", which is "she is pleasing to me".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, посмотри на Настю.', 'Kostya, look at Nastya.', [(59, 'Костян, смотри')], ''),
    ('kostya', 'Она очень красивая девушка.', 'She is a very pretty girl.', [(61, 'Красивое')], ''),
    ('max', 'Она тебе нравится? Признайся честно!', 'Do you like her? Admit it honestly!', [(62, 'Она чё, тебе нравится')], ''),
    ('kostya', 'Ну ладно, она мне очень нравится.', 'Well all right, I like her very much.', [(64, 'Костян втюрился')], ''),
    ('max', 'Тогда скажи ей приятный комплимент.', 'Then give her a nice compliment.', [(68, 'хочет сказать')], ''),
    ('kostya', 'Я боюсь, я не умею говорить.', 'I am afraid, I cannot talk smoothly.', [(67, 'Зачем')], ''),
    ('nastya', 'Привет, мальчики! О чём вы говорите?', 'Hi, boys! What are you talking about?', [(69, 'Чё надо')], ''),
    ('max', 'Костя хочет сказать тебе важные слова.', 'Kostya wants to tell you important words.', [(68, 'Тебе тут Костян что-то хочет сказать')], ''),
    ('kostya', 'Настя, у тебя очень красивая причёска!', 'Nastya, you have a very pretty hairstyle!', [(71, 'очень красивая')], ''),
    ('nastya', 'Спасибо, Костя! Ты очень милый парень.', 'Thank you, Kostya! You are a very sweet guy.', [], ''),
    ('kostya', 'Ты слышал? Она назвала меня милым!', 'Did you hear? She called me sweet!', [], ''),
    ('max', 'Видишь? Главное — всегда быть смелым!', 'See? The main thing is to always be brave!', [(74, 'будь смелее')], ''),
]
WALK = [
    (0, None, '\'Kostya, look at Nastya.\' "Posmotri na" is "look at", and "Nastya" becomes "Nastyu" as the thing you look at.'),
    (1, None, '\'She is a very pretty girl.\' Kostya says "devushka", the word for a girl or a young woman. There\'s no "is" in it.'),
    (2, None, '\'Do you like her? Admit it honestly!\' "Ona tebe nravitsya" is literally "she to you is pleasing". "Priznaysya" has "-sya" at the end, since you "admit yourself".'),
    (3, None, '\'Well all right, I like her very much.\' Kostya gives in with "nu ladno", "well, fine", and then says "I like her" the Russian way: "she is pleasing to me". The one who likes is "me".'),
    (4, None, '\'Then give her a nice compliment.\' Max sets him a task: "say to her" a nice compliment. The "to her" form is "yey", a tiny word that slips into the middle.'),
    (5, None, '\'I am afraid, I cannot talk smoothly.\' "Boyus\'" is "I\'m afraid", with "-s\'" at the end. "Ne umeyu" is "I don\'t know how".'),
    (6, None, '\'Hi, boys! What are you talking about?\' "Privet" is the casual hello. "Mal\'chiki" is "boys", with a small ending. "O chyom" is "about what".'),
    (7, None, '\'Kostya wants to tell you important words.\' Max passes the message on with a flourish. "Important words" is plural, so both words end alike, and "to you" is the short "tebe".'),
    (8, None, '\'Nastya, you have a very pretty hairstyle!\' "U tebya" is "at you", the "have" pattern. "Prichyoska" comes from "to comb", so it\'s a "combing".'),
    (9, None, '\'Thank you, Kostya! You are a very sweet guy.\' "Milyy" is "sweet" or "nice", and it\'s the word Vika used in the very first episode. "Paren\'" is "guy".'),
    (10, None, '\'Did you hear? She called me sweet!\' "Nazvala" is "called", with a woman\'s -a. "Milym" has "-ym", the ending that goes after "call".'),
    (11, None, '\'See? The main thing is to always be brave!\' Max is proud of his coaching. "Do you see?" is one word, and "brave" ends in "-ym" after "to be".'),
]
