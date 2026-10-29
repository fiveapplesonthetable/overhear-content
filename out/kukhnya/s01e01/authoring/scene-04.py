# Authoring module for kukhnya-s01e01-scene-04.
ID = 'kukhnya-s01e01-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Утро после клуба  (The Morning After the Club)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "The morning after. Max is trying to slip out of Vika's flat without a fuss, but she is awake, and he has got hold of completely the wrong idea about what she expects from him. Here is the awkward conversation in Russian first."
OPENER = "Now let's untangle it."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That is a messy start to a love story. On the way you picked up "I have to" and "I don\'t need", two patterns that will serve you well in everyday Russian.'
CLOSING = ('vika', 'До встречи!')
STORY = [
    ('max', 'Мне уже идти надо.', 'I need to go now.', [(24, 'мне идти надо')], ''),
    ('vika', 'Ты что, убегаешь?', 'What, are you running away?', [(25, 'Ты что'), (25, 'убегаешь')], ''),
    ('max', 'Почему убегаю? Нет, просто ухожу.', "Why running away? No, I'm just leaving.", [(26, 'Почему убегаю'), (26, 'Нет, просто ухожу')], ''),
    ('vika', 'Вот так? И всё?', "Just like that? And that's all?", [(27, 'Вот так вот'), (27, 'И все')], ''),
    ('vika', 'А то, что между нами было?', 'What about what was between us?', [(28, 'то, что между нами было')], ''),
    ('max', 'Спасибо. Прикольно было.', 'Thank you. It was fun.', [(29, 'Спасибо'), (29, 'прикольно было')], ''),
    ('vika', 'Прикольно, и всё?', "Fun, and that's it?", [(30, 'Прикольно и все')], ''),
    ('max', 'А что ещё?', 'What else?', [(31, 'А что ещё')], ''),
    ('vika', 'Да ладно тебе.', 'Oh, come on.', [(32, 'Да ладно')], ''),
    ('max', 'Нет, денег у меня нет.', 'No, I have no money.', [(33, 'Нет, денег у меня нет')], ''),
    ('max', 'Мы с тобой так не договаривались.', "You and I didn't agree to that.", [(34, 'мы с тобой так не договаривались')], ''),
    ('vika', 'Мне не нужны твои деньги.', "I don't need your money.", [], ''),
    ('max', 'Тогда я пошёл. У меня дела.', 'Then I am off. I have things to do.', [], ''),
    ('vika', 'Уходи. И не возвращайся сюда.', 'Leave. And do not come back here.', [], ''),
]
WALK = [
    (0, None, '\'I need to go now.\' "Mne idti nado" is "to me to go is necessary", the same "mne nado" pattern for needing to do something. "Uzhe", "already", turns it into a ready-made excuse.'),
    (1, None, '\'What, are you running away?\' "Ubegayesh\'" is "bezhat\'", to run, with "u-" on the front for "away". "Ty chto" at the start is like "what, you...?", a little burst of disbelief.'),
    (2, 'Почему убегаю?', '\'Why running away?\' Max throws her word back at her with one change. Hers ended in "-esh", "you", and his ends in "-yu", "I".'),
    (2, 'Нет, просто ухожу.', '\'No, I\'m just leaving.\' "Prosto", "simply", is back, and it makes the sentence sound like a shrug. "Ukhozhu" uses the same "u-" for "away" as Vika\'s "run away", this time on foot.'),
    (3, None, '\'Just like that? And that\'s all?\' Two tiny phrases do all the work. "I vsyo?", literally "and all?", is how Russians say "and that\'s it?", handy whenever something turns out simpler than expected. "Vot tak" is "like this", the way you\'d say it while showing someone.'),
    (4, None, '\'What about what was between us?\' Word for word it\'s "and that what between us was". "Nami" is "us" in the form that comes after "between", and "bylo", "was", is the neuter one, because it refers to "that".'),
    (5, 'Спасибо. Прикольно было.', '\'Thank you. It was fun.\' "Prikol\'no" is slang for fun or cool, from "prikol", a gag or a joke. It\'s exactly the wrong word to use after a night like this, and she hears it that way.'),
    (6, None, "'Fun, and that's it?' Vika picks up his slang word and hands it straight back. Repeating someone's word is the quickest way in any language to say you didn't like it."),
    (7, None, '\'What else?\' "A chto yeshchyo" is "and what more". The "a" at the start works like "so" in English, and Max sounds blank.'),
    (8, None, '\'Oh, come on.\' "Da ladno" is, word for word, "yes, fine", but with the right tone it means "come on!" or "you can\'t be serious". Adding "tebe", "to you", gives it a bit of scolding.'),
    (9, None, '\'No, I have no money.\' The two "nyet" words do different jobs: the first is "no", and the second is "there isn\'t". After "there isn\'t", "money" changes shape and becomes "deneg". Putting "money" first gives it the stress.'),
    (10, None, '\'You and I didn\'t agree to that.\' "My s toboy", "we with you", is the usual Russian for "you and I". "Dogovarivalis\'", "agreed", has "dogovor", an agreement, inside it, and the "-li" is the plural past, because it\'s the two of them.'),
    (11, None, '\'I don\'t need your money.\' "Mne ne nuzhny" is the "to me needed" pattern, but with plural "nuzhny" because "den\'gi" is always plural in Russian. It\'s a bit like "pants" in English.'),
    (12, None, '\'Then I am off. I have things to do.\' "Ya poshyol" means "I went", and Russians say it to mean "I\'m off", as if they\'ve already gone. "U menya dela" is the "at me" pattern with "dela", things to do.'),
    (13, None, '\'Leave. And do not come back here.\' "Ukhodi" is the command form of the same "ukhozhu", "I\'m leaving". "Syuda" is "to here", used when you move toward the place. For being there, Russians say a different word.'),
]
