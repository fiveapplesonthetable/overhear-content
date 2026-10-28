# Authoring module for kukhnya-s06e09-scene-03.
ID = 'kukhnya-s06e09-scene-03'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 9
SCENE = 3
TITLE = 'Приглашение на обед  (Invitation to Lunch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.09'
SOURCE_FILE = 'sources/kukhnya/s06/e09.ru.srt'
INTRO = 'On the kitchen floor, Chef Barinov calls Elena and invites her to have lunch together at the restaurant. Lyova then asks for a break to dine with his mother and her friend, while upstairs Eleonora refuses to eat breakfast after her breakup with Nagiyev.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'While Eleonora takes her heartbreak out on the staff, downstairs Denis is nursing his bruised arm from the morning accident. Until next time!'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('barinov', 'Елена, привет, я уже очень соскучился.', 'Elena, hello, I have missed you very much already.', [(30, 'привет'), (31, 'Что-то я соскучился')], 'adapted'),
    ('barinov', 'Не пора ли нам пообедать вместе?', "Isn't it time for us to have lunch together?", [(32, 'Не пора ли нам пообедать вместе')], 'adapted'),
    ('barinov', 'Прекрасно, тогда я тебя очень жду.', 'Wonderful, then I am waiting for you eagerly.', [(34, 'Прекрасно. Жду')], 'adapted'),
    ('lyova', 'Виктор Петрович, можно вас на минуту?', 'Viktor Petrovich, may I have a minute?', [(35, 'Виктор Петрович, что тебе')], 'adapted'),
    ('barinov', 'Что тебе нужно, говори быстрее.', 'What do you need, speak faster.', [(35, 'что тебе')], 'adapted'),
    ('lyova', 'Мама с подругой хотят у нас пообедать.', 'Mom and her friend want to have lunch at our place.', [(36, 'Мама с подругой хотят у нас пообедать')], 'adapted'),
    ('lyova', 'Можно я им сегодня составлю компанию?', 'May I keep them company today?', [(37, 'Можно я им составлю компанию')], 'adapted'),
    ('barinov', 'Хорошо, иди, только не очень долго.', 'Alright, go, just not for very long.', [(38, 'Иди')], 'adapted'),
    ('eleonora', 'Чего тебе нужно в моём номере?', 'What do you need in my room?', [(39, 'Чего тебе')], 'adapted'),
    ('lyova', 'Я вам свежий горячий завтрак принёс.', 'I brought you a fresh hot breakfast.', [(40, 'Я вам завтрак принес')], 'adapted'),
    ('eleonora', 'Ладно, просто оставь это на столе.', 'Alright, just leave it on the table.', [(41, 'Оставь на столе')], 'adapted'),
    ('lyova', 'Вы со вчерашнего дня ничего не ели.', 'You have not eaten anything since yesterday.', [(46, 'Вы же со вчерашнего дня ничего не ели')], 'adapted'),
    ('eleonora', 'Немедленно убери это и выйди отсюда!', 'Take this away immediately and get out of here!', [(46, 'Убери это')], 'adapted'),
]
WALK = [
    (0, None, "'Elena, hello, I have missed you very much already.' Mentioning that he has missed Eleonora very much already moves the talk in a new direction."),
    (1, None, "'Isn't it time for us to have lunch together?' Here asking whether not it time for them to have lunch together shows Barinov looking for the real truth."),
    (2, None, '\'Wonderful, then I am waiting for you eagerly.\' Adding that wonderful then he is waiting for Eleonora eagerly fills in the missing piece for Eleonora. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (3, None, "'Viktor Petrovich, may I have a minute?' Around the point and friend, Lyova wants to know where Barinov really stands. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (4, None, "'What do you need, speak faster.' Since what do Eleonora needs speak faster, Barinov does not waste words on excuses."),
    (5, None, '\'Mom and her friend want to have lunch at our place.\' Mentioning that Mom and her friend want to have lunch at their place moves the talk in a new direction. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (6, None, '\'May I keep them company today?\' Questioning whether may he keeps them company today is how Lyova tests Barinov\'s story. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (7, None, "'Alright, go, just not for very long.' With the restaurant and friend in play, Barinov keeps this short reply brisk and direct."),
    (8, None, '\'What do you need in my room?\' Asking what Barinov needs in her room is how Eleonora puts Barinov on the spot. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (9, None, '\'I brought you a fresh hot breakfast.\' Lyova mentions that he brought Barinov a fresh hot breakfast so Barinov sees what is at stake. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (10, None, "'Alright, just leave it on the table.' With the restaurant and breakup in play, Eleonora keeps this short reply brisk and direct."),
    (11, None, '\'You have not eaten anything since yesterday.\' Pointing out that Barinov has not eaten anything since yesterday gives Barinov a sobering reality check. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (12, None, '\'Take this away immediately and get out of here!\' Declaring that Barinov should take this away immediately and get out of here brings Eleonora\'s temper right to the surface. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
]
