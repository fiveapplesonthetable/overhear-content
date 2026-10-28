# Authoring module for kukhnya-s04e19-scene-05.
ID = 'kukhnya-s04e19-scene-05'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 19
SCENE = 5
TITLE = 'Шоу для неудачников  (A Show for Losers)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.19'
SOURCE_FILE = 'sources/kukhnya/s04/e19.ru.srt'
INTRO = "The dining room of Claude Monet has been transformed into a bright television studio for the upcoming contest. When Nagiyev spots Viktor Petrovich watching the preparations, he warns the veteran chef not to dare enter the competition. Let's listen to their fiery exchange in Russian."
OPENER = "Now let's break down the argument between Nagiyev and Chef Barinov line by line."
TRANSITION = "Let's hear the confrontation in the studio again from beginning to end."
OUTRO = "Viktor Petrovich proudly declares that real chefs work in kitchens rather than chasing television fame, though Fedya's pride is stung. Listen for the words meaning studio, smell, and cooks. Until next time!"
CLOSING = ('barinov', 'До завтра!')
STORY = [
    ('fedya', 'Смотрите, там в зале настоящая студия.', 'Look, there is a real studio out in the dining room.', [(55, 'Там настоящая студия')], 'adapted'),
    ('fedya', 'Мы с Сеней тоже решили попробовать.', 'Senya and I decided to give it a try too.', [(58, 'тоже решили попробовать')], 'adapted'),
    ('fedya', 'А вы, шеф, будете там участвовать?', 'And will you participate out there, Chef?', [(59, 'ну что, шеф, будете участвовать')], 'adapted'),
    ('nagiyev', 'Витя, ты даже не пробуй.', 'Vitya, do not even try.', [(60, 'Только попробуй')], 'adapted'),
    ('nagiyev', 'Я пять лет ел твою еду.', 'I ate your food for five years.', [(62, 'Я пять лет, пять лет')], 'adapted'),
    ('nagiyev', 'Я по запаху твои блюда узнаю.', 'I will recognize your dishes by their smell.', [(64, 'Я по запаху'), (64, 'узнаю')], 'adapted'),
    ('nagiyev', 'И сразу выгоню тебя с конкурса.', 'And I will kick you out of the contest right away.', [], 'new'),
    ('barinov', 'Я давно уже ничего не боюсь.', 'I have not been afraid of anything for a long time.', [(66, 'Да я уже давно ничего не боюсь')], 'adapted'),
    ('barinov', 'Если бы хотел, я бы победил.', 'If I wanted to, I would win.', [(67, 'А если бы хотел, то пришел бы, увидел и победил')], 'adapted'),
    ('barinov', 'Но твоё шоу — для неудачников.', 'But your show is for losers.', [(68, 'Только твое шоу – это же фигня для неудачников')], 'adapted'),
    ('barinov', 'Нормальные повара спокойно работают на кухне.', 'Normal cooks work quietly in the kitchen.', [(69, 'А нормальные повара работают')], 'adapted'),
    ('fedya', 'Подождите, это кто тут у нас неудачник?', 'Wait a second, who are you calling a loser here?', [(70, 'Это кто этот неудачник')], 'adapted'),
]
WALK = [
    (0, None, '\'Look, there is a real studio out in the dining room.\' Describing how real things are at once, Fedya brings in "nastoyashchaya" ("real, genuine", from "nastoyashchiy") as the key Russian word here.'),
    (1, None, "'Senya and I decided to give it a try too.' Fedya speaks up right away during the talk, before Nagiyev can change the subject."),
    (2, None, '\'And will you participate out there, Chef?\' Fedya continues smoothly around Barinov and centers the remark on "uchastvovat" ("to participate") without any extra fuss.'),
    (3, None, "'Vitya, do not even try.' Nagiyev speaks dryly in this moment, without trying to dress up how he really feels."),
    (4, None, "'I ate your food for five years.' Nagiyev speaks bluntly in their talk, grounding the moment in plain reality."),
    (5, None, '\'I will recognize your dishes by their smell.\' Focusing on the smell before Barinov, Nagiyev uses "zapakhu" ("smell, scent", from "zapakh") to make the point stick.'),
    (6, None, "'And I will kick you out of the contest right away.' Nagiyev fires back pointedly beside Barinov, to clear the air between them once and for all."),
    (7, None, "'I have not been afraid of anything for a long time.' Barinov continues wryly with a nod, so Nagiyev knows he is not just making small talk."),
    (8, None, "'If I wanted to, I would win.' Barinov reacts promptly without a pause, testing Nagiyev's reaction in the middle of the exchange."),
    (9, None, '\'But your show is for losers.\' Checking on the losers to Fedya, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (10, None, "'Normal cooks work quietly in the kitchen.' Barinov follows up wryly beside Fedya, to clear the air between them once and for all."),
    (11, None, '\'Wait a second, who are you calling a loser here?\' Discussing a loser to Barinov, Fedya reaches for the Russian word "neudachnik" ("loser, unlucky guy") right at the heart of the line.'),
]
