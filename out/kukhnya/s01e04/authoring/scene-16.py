# Authoring module for kukhnya-s01e04-scene-16.
ID = 'kukhnya-s01e04-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 16
TITLE = "Просьба друга  (A Friend's Request)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Behind the bar, Kostya is gloomy: his attempt to charm Nastya went badly. Max teases him a little, and then Kostya asks Max to talk to her on his behalf. Max, who thinks he is a born diplomat, agrees. Here's the Russian first."
OPENER = "Let's go back to the bar."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max promises to be gentle, which is not what he\'s known for. A nice thing to keep: "minut sem\'", where the number after the noun means "about".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Я понял, свидания у тебя не будет?', "I take it you won't have a date?", [(211, 'свидания у тебя не будет')], ''),
    ('kostya', 'Да, я опять сказал полную глупость.', 'Yes, I said something completely stupid again.', [], ''),
    ('max', 'Ты слишком сильно нервничаешь перед ней.', 'You get way too nervous around her.', [], ''),
    ('kostya', 'Не получается у меня красиво говорить!', 'I cannot manage to speak beautifully!', [(213, 'Не получается у меня красиво')], ''),
    ('max', 'Этому нужно долго и терпеливо учиться.', 'One needs to learn this long and patiently.', [], ''),
    ('kostya', 'Слушай, а может ты с ней поговоришь?', 'Listen, maybe you could talk with her?', [(215, 'может ты с ней')], ''),
    ('max', 'Что именно я должен ей сказать?', 'What exactly am I supposed to tell her?', [], ''),
    ('kostya', 'Объясни, что она мне очень нравится.', 'Explain that I really like her.', [], ''),
    ('max', 'Ладно, я попробую поговорить с Настей.', 'Okay, I will try to talk with Nastya.', [(216, 'Ладно')], ''),
    ('kostya', 'Спасибо, друг, ты меня очень выручишь!', 'Thank you, friend, you will really help me out!', [], ''),
    ('max', 'У меня как раз минут семь есть.', 'I have about seven minutes right now.', [(217, 'минут семь есть')], ''),
    ('kostya', 'Только скажи всё максимально нежно.', 'Just say everything as gently as possible.', [], ''),
    ('max', 'Не волнуйся, я прирождённый дипломат!', 'Do not worry, I am a natural diplomat!', [], ''),
]
WALK = [
    (0, None, '\'I take it you won\'t have a date?\' "Ya ponyal", I understood, opens the line as "I take it". "U tebya ne budet" is "at you there won\'t be", and after "ne budet", "svidaniye" becomes "svidaniya".'),
    (1, None, '\'Yes, I said something completely stupid again.\' Russian says "skazal glupost\'", said a stupidity. "Polnuyu", complete, takes -uyu as the object.'),
    (2, None, '\'You get way too nervous around her.\' "Slishkom" is "too". "Nervnichayesh\'" is from "nervy", nerves, and "pered ney" is "in front of her".'),
    (3, None, '\'I cannot manage to speak beautifully!\' Russians often skip "I can\'t" and say "ne poluchayetsya u menya", it doesn\'t work out at me, as if the speech itself were failing. "Krasivo" is the adverb from "krasivyy", beautiful.'),
    (4, None, '\'One needs to learn this long and patiently.\' "Terpelivo", patiently, is from "terpet\'", to endure. "Uchit\'sya" takes "to" for the subject learned, so "eto" becomes "etomu".'),
    (5, None, '\'Listen, maybe you could talk with her?\' Familiar from the first word: "slushay" is the ty form of "listen". In "pogovorish\'", the "po-" makes it one short talk, and -ish\' means "you will".'),
    (6, None, '\'What exactly am I supposed to tell her?\' "Dolzhen" is "must" for a man. "Yey" is "to her".'),
    (7, None, '\'Explain that I really like her.\' "Ob\'\'yasni" is "explain". In "ona mne nravitsya", she does the pleasing and "mne" receives it.'),
    (8, None, '\'Okay, I will try to talk with Nastya.\' After "s", with, "Nastya" becomes "Nastey".'),
    (9, None, '\'Thank you, friend, you will really help me out!\' "Vyruchish\'" is "you\'ll get me out of a jam", warmer than "pomozhesh\'", you\'ll help.'),
    (10, None, '\'I have about seven minutes right now.\' Putting the number after the noun makes it rough: "minut sem\'" is about seven, "sem\' minut" is seven.'),
    (11, None, '\'Just say everything as gently as possible.\' "Maksimal\'no" is borrowed, "maximally". "Nezhno", gently, is from "nezhnyy", tender.'),
    (12, None, '\'Do not worry, I am a natural diplomat!\' "Prirozhdyonnyy" is "pri-" plus "rozhdyonnyy", born: born to it. "Diplomat" was borrowed into Russian unchanged.'),
]
