# Authoring module for kukhnya-s03e20-scene-11.
ID = 'kukhnya-s03e20-scene-11'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 20
SCENE = 11
TITLE = 'Находка в номере отеля  (The Find in the Hotel Room)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.20'
SOURCE_FILE = 'sources/kukhnya/s03/e20.ru.srt'
INTRO = "When Sergey catches Chef Barinov drinking champagne during work hours, Chef announces he is celebrating Sergey's resignation—and pulls out Olya's missing earring, which he found in Sergey's hotel room!"
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "During his second visit to Sergey's hotel bathroom, Chef Barinov hid a tiny video camera—and Lyova is bringing the disc right now. Until next time!"
CLOSING = ('barinov', 'Всего хорошего!')
STORY = [
    ('inspector', 'Виктор Петрович, почему это вы пьёте в рабочее время?', 'Viktor Petrovich, why are you drinking during work hours?', [(192, 'Почему это вы пьете в рабочее время')], 'adapted'),
    ('barinov', 'А я праздную ваше скорое увольнение, Сергей Владимирович!', 'I am celebrating your imminent resignation, Sergey Vladimirovich!', [(193, 'А я праздную ваше увольнение, Сергей Владимирович')], 'adapted'),
    ('inspector', 'Интересно, с какой это стати я должен уволиться?', 'Interesting, why on earth should I resign?', [(194, 'стати я должен уволиться')], 'adapted'),
    ('barinov', 'А вот именно из-за этой красивой вещички!', 'Because of this pretty little thing right here!', [(195, 'А вот из-за этого')], 'adapted'),
    ('barinov', 'Посмотри внимательно на неё, ты её узнаёшь?', 'Look closely at it, do you recognize it?', [(196, 'Узнаешь')], 'adapted'),
    ('max', 'Ой, неужели я вчера случайно её потеряла?', 'Oh, did I really lose it by accident yesterday?', [(197, 'Неужели я ее потеряла')], 'adapted'),
    ('inspector', 'Не вижу логики, почему я должен уволиться из-за серёжки?', 'I see no logic, why should I resign because of an earring?', [(198, 'Не вижу логики. Почему я должен уволиться из-за этой сережки')], 'adapted'),
    ('barinov', 'А ты знаешь, где именно я её вчера нашёл?', 'And do you know where exactly I found it yesterday?', [(199, 'А ты знаешь, где я ее нашел')], 'adapted'),
    ('barinov', 'Я нашёл её на полу, когда уронил пробку у тебя!', 'I found it on the floor when I dropped the cork at your place!', [(200, 'Сергей, нам надо прояснить ситуацию'), (202, 'Виноват')], 'adapted'),
    ('inspector', 'Вы обнаружили её в моём номере, это ничего не значит.', 'You found it in my room, and that means nothing.', [(203, 'вы обнаружили ее в моем номере')], 'adapted'),
    ('barinov', 'А я знал, что ты так скажешь, поэтому пришёл снова!', 'And I knew you would say that, which is why I came a second time!', [(204, 'А я знал, что ты так скажешь, поэтому и пришел к тебе')], 'adapted'),
    ('barinov', 'Именно поэтому я тогда и спросил, где у вас туалет!', 'That is precisely why I asked where your restroom was back then!', [(205, 'Где у вас туалет')], 'adapted'),
]
WALK = [
    (0, None, '\'Viktor Petrovich, why are you drinking during work hours?\' Describing how work things are at once, the inspector puts the question word "pochemu" right at the start so Barinov hears the focus immediately.'),
    (1, None, "'I am celebrating your imminent resignation, Sergey Vladimirovich!' Barinov chimes in dryly beside the inspector, before the inspector can change the subject."),
    (2, None, '\'Interesting, why on earth should I resign?\' The inspector follows up pointedly to Barinov and brings in "dolzhen" ("has to, must") to make the meaning unmistakable.'),
    (3, None, '\'Because of this pretty little thing right here!\' Barinov answers directly in front of the inspector and centers the thought on "veshchichki" ("little thing", from "veshchichka") without wasting a word.'),
    (4, None, "'Look closely at it, do you recognize it?' Barinov presses briskly while looking straight at Max here."),
    (5, None, '\'Oh, did I really lose it by accident yesterday?\' Max steps in dryly right here and centers the remark on "sluchayno" ("by any chance") without any extra fuss.'),
    (6, None, '\'I see no logic, why should I resign because of an earring?\' Mentioning an earring during the talk, the inspector puts the question word "pochemu" right at the start so Barinov hears the focus immediately.'),
    (7, None, "'And do you know where exactly I found it yesterday?' Barinov wonders point-blank where this conversation is heading next."),
    (8, None, '\'I found it on the floor when I dropped the cork at your place!\' Underscoring the traffic jam in the exchange, Barinov centers the thought on "probku" ("traffic jam", from "probka") without wasting a word.'),
    (9, None, '\'You found it in my room, and that means nothing.\' Pointing to his room at once, the inspector pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (10, None, "'And I knew you would say that, which is why I came a second time!' Barinov follows up frankly facing the inspector, shifting the mood of the conversation in a single beat."),
    (11, None, '\'That is precisely why I asked where your restroom was back then!\' Touching on the toilet in this beat, Barinov brings in "tualet" ("toilet") to make the meaning unmistakable.'),
]
