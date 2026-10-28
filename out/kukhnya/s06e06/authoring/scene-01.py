# Authoring module for kukhnya-s06e06-scene-01.
ID = 'kukhnya-s06e06-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 6
SCENE = 1
TITLE = 'Приглашение в Париж  (Invitation to Paris)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'guest': 'Гость', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.06'
SOURCE_FILE = 'sources/kukhnya/s06/e06.ru.srt'
INTRO = 'Welcome to episode six of Kukhnya season six. Over a romantic dinner, Olivier invites Katya to fly to Paris with him, while Denis and Nikita watch jealously from across the dining room.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Denis's desperate attempt to ruin the date with a fire alarm and spilled wine only brings Katya and Olivier closer together. Until next time!"
CLOSING = ('katya', 'Хорошего дня!')
STORY = [
    ('guest', 'Тебе ещё не надоела серая Москва?', 'Are you not tired of gray Moscow yet?', [(1, 'тебе не надоело эта серая Москва')], 'adapted'),
    ('guest', 'Может, поедешь со мной в Париж?', 'Maybe you will go to Paris with me?', [(2, 'Может, со мной в Париж')], 'adapted'),
    ('guest', 'Там мы найдём тебе хорошую работу.', 'There we will find you a good job.', [(3, 'Там, Париж. Найдем тебе работу')], 'adapted'),
    ('guest', 'Или тебя здесь что-то держит?', 'Or is something keeping you here?', [(4, 'Или тебя здесь что-то держат')], 'adapted'),
    ('katya', 'Нет, меня здесь ничего не держит.', 'No, nothing is keeping me here.', [(5, 'Ну, нет')], 'adapted'),
    ('katya', 'А ты случайно не слишком торопишься?', 'Are you not rushing things a bit too much?', [(6, 'А ты не слишком торопишься')], 'adapted'),
    ('guest', 'Я целую тебя впервые за пять лет.', 'I am kissing you for the first time in five years.', [(7, 'Я целую тебя впервые за пять лет знакомства')], 'adapted'),
    ('guest', 'По-моему, я уже жутко опаздываю.', 'In my opinion, I am already terribly late.', [(8, 'По-моему, я жутко опаздываю')], 'adapted'),
    ('katya', 'Слышишь, это сработала пожарная сигнализация.', 'Listen, the fire alarm has gone off.', [(9, 'Это пожарная сигнализация')], 'adapted'),
    ('katya', 'Нам сейчас срочно надо идти на улицу.', 'We urgently need to go outside right now.', [(10, 'Надо идти')], 'adapted'),
    ('denis', 'Прости, пожалуйста, я совсем случайно.', 'Forgive me, please, it was completely accidental.', [(12, 'Прости, пожалуйста')], 'adapted'),
    ('guest', 'Ничего страшного, это просто красное вино.', 'No big deal, it is just red wine.', [(12, 'Ничего, ничего, ничего')], 'adapted'),
]
WALK = [
    (0, None, "'Are you not tired of gray Moscow yet?' Here asking whether Denis not tired of gray Moscow yet shows the guest looking for the real truth."),
    (1, None, '\'Maybe you will go to Paris with me?\' Wondering if maybe Denis will go to Paris with him shows the guest caught off guard. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, '\'There we will find you a good job.\' Noting that there they will find Denis a good job keeps the guest\'s side of the story simple and clear. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (3, None, "'Or is something keeping you here?' Checking whether something keeping Denis here is how the guest puts Denis on the spot."),
    (4, None, '\'No, nothing is keeping me here.\' Admitting that nothing is keeping her here shows Katya being honest for a change. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (5, None, '\'Are you not rushing things a bit too much?\' By asking whether Denis not rushing things a bit too much, Katya presses Denis for a straight answer. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (6, None, "'I am kissing you for the first time in five years.' Being kissing Denis for the first time in five years moves the conversation forward without extra drama."),
    (7, None, "'In my opinion, I am already terribly late.' Adding that in his opinion he is already terribly late fills in the missing piece for Denis."),
    (8, None, '\'Listen, the fire alarm has gone off.\' Katya tells Denis that the fire alarm has gone off without dressing it up. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (9, None, "'We urgently need to go outside right now.' With the wine and dinner in play, Katya keeps this short reply brisk and direct."),
    (10, None, "'Forgive me, please, it was completely accidental.' Mentioning that it was completely accidental moves the talk in a new direction."),
    (11, None, '\'No big deal, it is just red wine.\' The guest reminds Denis that big deal it is just red wine before the moment passes. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
]
