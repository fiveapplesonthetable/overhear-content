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
OUTRO = "Viktor Petrovich proudly declares that real chefs work in kitchens rather than chasing television fame, though Fedya's pride is stung. Listen for the nouns meaning studio, smell, and cooks. Until next time!"
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
    (0, None, "'Look, there is a real studio out in the dining room.' Once there is a real studio out in the dining room, Fedya can finally tell Barinov what he means."),
    (1, None, "'Senya and I decided to give it a try too.' Adding that Senya and he decided to give it a try fills in the missing piece for Barinov."),
    (2, None, "'And will you participate out there, Chef?' By asking whether Barinov participate out there, Fedya presses Barinov for a straight answer."),
    (3, None, '\'Vitya, do not even try.\' Since do not even try, Nagiyev does not waste words on excuses. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (4, None, "'I ate your food for five years.' Mentioning that he ate Barinov's food for five years moves the talk in a new direction."),
    (5, None, "'I will recognize your dishes by their smell.' Saying that he will recognize Barinov's dishes by their smell is how Nagiyev sets the tone with Barinov."),
    (6, None, '\'And I will kick you out of the contest right away.\' Because he will kick Barinov out of the contest right away, Nagiyev treats the matter as settled. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (7, None, '\'I have not been afraid of anything for a long time.\' By having not been afraid of anything for a long time, Barinov keeps his side of the story grounded. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (8, None, "'If I wanted to, I would win.' Barinov mentions that if he wanted to he would win so Fedya sees what is at stake."),
    (9, None, '\'But your show is for losers.\' Claiming that Fedya\'s show is for losers sounds confident, even if Fedya has doubts. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (10, None, "'Normal cooks work quietly in the kitchen.' Pointing out that normal cooks work quietly in the kitchen gives Fedya a sobering reality check."),
    (11, None, "'Wait a second, who are you calling a loser here?' Wondering if a second who are Barinov calling a loser here shows Fedya caught off guard."),
]
