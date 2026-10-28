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
    (0, None, "'Look, there is a real studio out in the dining room.' Fedya pushes back promptly to settle things, before Barinov can change the subject."),
    (1, None, "'Senya and I decided to give it a try too.' Fedya counters right away around Nagiyev, testing Nagiyev's reaction in the middle of the exchange."),
    (2, None, '\'And will you participate out there, Chef?\' Fedya stresses one direct expression with Barinov: "uchastvovat" means "to participate", and it carries the main weight of what Fedya is saying.'),
    (3, None, '\'Vitya, do not even try.\' Nagiyev picks one practical choice in reply: "probuy" means "to try, to taste" (from "probovat"), giving the line its exact edge.'),
    (4, None, "'I ate your food for five years.' Nagiyev jumps in bluntly hearing Barinov, watching Barinov's face to see how the news lands."),
    (5, None, '\'I will recognize your dishes by their smell.\' Nagiyev picks one concrete term toward Fedya: "zapakhu" means "smell, scent" (from "zapakh"), giving the line its exact edge.'),
    (6, None, '\'And I will kick you out of the contest right away.\' Nagiyev underscores one concrete element with Barinov: "konkursa" means "contest" (from "konkurs"), giving the line its exact edge.'),
    (7, None, "'I have not been afraid of anything for a long time.' Barinov cuts in wryly before Nagiyev, steering the talk right where he wants it."),
    (8, None, '\'If I wanted to, I would win.\' Barinov features one sharp choice right here: "pobedil" means "won" (from "pobedit"), giving the line its exact edge.'),
    (9, None, '\'But your show is for losers.\' Barinov directs this update with ease: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (10, None, "'Normal cooks work quietly in the kitchen.' Barinov follows up wryly to be clear, keeping the focus on what actually matters here."),
    (11, None, '\'Wait a second, who are you calling a loser here?\' Fedya favors one sharp expression right here: "neudachnik" means "loser, unlucky guy", and it carries the main weight of what Fedya is saying.'),
]
