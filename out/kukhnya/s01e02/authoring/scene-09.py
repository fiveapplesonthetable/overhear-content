# Authoring module for kukhnya-s01e02-scene-09.
ID = 'kukhnya-s01e02-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 9
TITLE = 'Хорошо или плохо?  (Good or Bad?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Senya, Fedya and Max are crowded behind the kitchen window, watching a guest taste their secretly cooked fricassee. She looks calm, and they can't tell what she thinks. Here's the Russian first."
OPENER = "Now let's go over the nervous watching."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Suspense is at its peak, with a guest who calls the waitress over. You\'ve heard "khorosho" and its opposite, "plokho", good and bad.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('senya', 'Смотрите, официант уже подал наше блюдо.', 'Look, the waiter has already served our dish.', [], ''),
    ('fedya', 'Она взяла вилку и пробует соус.', 'She picked up the fork and is tasting the sauce.', [], ''),
    ('max', 'Она улыбается или хмурится?', 'Is she smiling or frowning?', [], ''),
    ('senya', 'Она очень внимательно жуёт первый кусочек.', 'She is chewing the first piece very attentively.', [], ''),
    ('fedya', 'И почему-то совсем молчит.', 'And for some reason she is completely silent.', [], ''),
    ('max', 'А это хорошо или плохо?', 'Is that good or bad?', [(130, 'А это хорошо или плохо')], ''),
    ('senya', 'Я сам ничего пока не понимаю.', 'I do not understand anything yet myself.', [], ''),
    ('fedya', 'Главное, чтобы она не позвала директора.', 'The main thing is that she does not call the director.', [], ''),
    ('max', 'Смотрите, она сделала ещё один глоток.', 'Look, she took another sip.', [], ''),
    ('senya', 'Кажется, наше фрикасе ей понравилось!', 'It seems she liked our fricassee!', [], ''),
    ('fedya', 'Не радуйся раньше времени.', 'Do not celebrate too early.', [], ''),
    ('max', 'Ой, она зовёт официантку к столу!', 'Oh, she is calling the waitress to the table!', [], ''),
]
WALK = [
    (0, None, '\'Look, the waiter has already served our dish.\' "Smotrite" is "look", said to a group. "Podal", "served", is the past of "podat\'", the same family as "podavay", serve.'),
    (1, None, '\'She picked up the fork and is tasting the sauce.\' The -a on "vzyala", "took", shows it\'s a woman. "Probuyet" means both "tastes" and "tries".'),
    (2, None, '\'Is she smiling or frowning?\' "Ulybayetsya", "smiles", comes from "ulybka", a smile, and "khmuritsya" is "frowns". "Ili" is "or".'),
    (3, None, '\'She is chewing the first piece very attentively.\' "Kusochek" is "kusok", a piece, made small. "Vnimatel\'no", attentively, comes from "vnimaniye", attention.'),
    (4, None, '\'And for some reason she is completely silent.\' "Pochemu-to" is "why" plus "-to", which makes it "for some reason". Russians add "-to" to question words when the answer is unknown.'),
    (5, None, '\'Is that good or bad?\' "Khorosho ili plokho", "good or bad", is two opposites joined by "ili". They\'re short and easy to remember.'),
    (6, None, '\'I do not understand anything yet myself.\' "Nichego ne", "nothing not", is the double negative once more. "Poka" here means "for now", the same word as the casual "bye".'),
    (7, None, '\'The main thing is that she does not call the director.\' "Glavnoye" opens it, then "chtoby", "so that". After "chtoby" the verb takes its past form, "ne pozvala", even though it\'s about a hope.'),
    (8, None, '\'Look, she took another sip.\' "Glotok", a sip, is one swallow: the verb "glotat\'" means to swallow. "Yeshchyo odin" is "one more".'),
    (9, None, '\'It seems she liked our fricassee!\' "Kazhetsya" is "it seems". "Yey ponravilos\'" is "to her it pleased", and the "-os\'" ending matches "frikase", a neuter word.'),
    (10, None, '\'Do not celebrate too early.\' "Ne raduysya", "don\'t rejoice", comes from "rad", glad. "Ran\'she vremeni", "earlier than time", is how Russians say "too early".'),
    (11, None, '\'Oh, she is calling the waitress to the table!\' "Ofitsiantka" is "ofitsiant", a waiter, with "-ka" for a woman. "K stolu" is "to the table": "stol" adds -u after "k".'),
]
