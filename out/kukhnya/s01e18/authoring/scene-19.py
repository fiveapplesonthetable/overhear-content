# Authoring module for kukhnya-s01e18-scene-19.
ID = 'kukhnya-s01e18-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 19
TITLE = 'Экономия на бармене  (Saving on the Bartender)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "Nagiyev's savings plan has reached the bar. He has found a way to economise on staff, and Kostya is the first to hear. Listen for how little time it takes."
OPENER = "Here's how the firing goes, word by word."
TRANSITION = 'Now the dismissal again, short and brutal.'
OUTRO = 'Kostya has been dismissed in a few short sentences, and he takes it with surprising calm. "Balbes", blockhead, is rude but mild: Russians often say it half-jokingly. See you next time!'
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('kostya', 'Я просто делал свою работу.', 'I was just doing my job.', [], ''),
    ('nagiyev', 'Мы экономим на всём.', 'We are saving on everything.', [], ''),
    ('nagiyev', 'Мы сэкономили на бармене.', 'We saved on the bartender.', [(351, 'на Бармене сэкономили')], ''),
    ('kostya', 'Вы не можете меня уволить.', 'You cannot fire me.', [], ''),
    ('nagiyev', 'Ты уволен, балбес.', 'You are fired, idiot.', [(352, 'Ты уволен, балбес')], ''),
    ('kostya', 'Балбес, да?', 'An idiot, huh?', [(353, 'Балбес, да')], ''),
    ('kostya', 'Это очень несправедливо.', 'This is very unfair.', [], ''),
    ('nagiyev', 'Ресторан в трудном положении.', 'The restaurant is in a difficult situation.', [], ''),
    ('kostya', 'Кто будет наливать напитки?', 'Who will pour drinks?', [], ''),
    ('nagiyev', 'Это больше не твоя проблема.', 'This is no longer your problem.', [], ''),
    ('kostya', 'Хорошо, я уйду сегодня.', 'Fine, I will leave today.', [], ''),
    ('nagiyev', 'Вот и отлично.', 'That is excellent.', [], ''),
]
WALK = [
    (0, None, '\'I was just doing my job.\' "Svoyu", my own, points back to "ya". "Delal", was doing, paints it as ongoing work.'),
    (1, None, '\'We\'re saving on everything.\' You save on something: "na". After it, "vsyo", everything, becomes "vsyom".'),
    (2, None, '\'We\'ve saved on the bartender.\' The "s-" in "sekonomili" marks it as done. "Barmen" becomes "barmene" after "na".'),
    (3, None, '\'You can\'t fire me.\' Kostya says the polite "vy mozhete" to the owner, who says "ty" back.'),
    (4, None, '\'You\'re fired, idiot.\' "Uvolen", fired, is a short form, so no \'are\' is needed. "Balbes" is a blockhead.'),
    (5, None, '\'An idiot, huh?\' A "da?" tacked on the end works like \'huh?\' or \'is that so?\'.'),
    (6, None, '\'That\'s really unfair.\' "Nespravedlivo" is "ne", not, plus "spravedlivo", fair, which shares a root with "prav", right.'),
    (7, None, '\'The restaurant\'s in a tight spot.\' "Polozhenie", situation, literally a position. "V trudnom polozhenii", in a difficult one.'),
    (8, None, '\'Who\'ll pour the drinks?\' "Budet nalivat", will be pouring: a job that goes on. "Napitki", drinks, comes from "pit", to drink.'),
    (9, None, '\'That\'s no longer your problem.\' "Bolshe ne", \'more not\': no longer. "Problema" is feminine, so your is "tvoya".'),
    (10, None, '\'Fine, I\'ll leave today.\' "Uydu", I\'ll leave: the "u-" means away. "Segodnya", today, is said "sevodnya".'),
    (11, None, '\'Well, that\'s great.\' "Vot i otlichno", \'so there, excellent\': that settles it.'),
]
