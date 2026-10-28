# Authoring module for kukhnya-s01e20-scene-06.
ID = 'kukhnya-s01e20-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 6
TITLE = 'Нам надо поговорить  (We Need to Talk)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = 'A little later Nastya tries again, and this time Kostya changes the subject. Here it is in Russian.'
OPENER = 'Now the pieces, one by one.'
TRANSITION = 'And again, the whole thing.'
OUTRO = "Another escape: change the subject, just as Max told him. A compliment like ty takaya krasivaya, 'you're so beautiful', is a classic way to do it. See you next time!"
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Костя, нам надо поговорить.', 'Kostya, we need to talk.', [(138, 'Нам надо поговорить.')], ''),
    ('kostya', 'Настя, я так по тебе соскучился.', 'Nastya, I have missed you so much.', [(139, 'Настя, я так по тебе соскучился.')], ''),
    ('nastya', 'Мы с тобой виделись утром.', 'We saw each other this morning.', [], ''),
    ('kostya', 'Ты сегодня такая красивая.', 'You look so beautiful today.', [], ''),
    ('nastya', 'Спасибо. Но нам надо поговорить.', 'Thank you. But we need to talk.', [], ''),
    ('kostya', 'Давай поговорим потом, хорошо?', 'Let us talk later, okay?', [], ''),
    ('nastya', 'Ты опять убегаешь от разговора.', 'You are running away from the conversation again.', [], ''),
    ('kostya', 'Нет, у меня просто много работы.', 'No, I just have a lot of work.', [], ''),
]
WALK = [
    (0, None, "'Kostya, we need to talk.' Russian says nam nado, 'to us it is necessary', rather than 'we need'."),
    (1, None, "'Nastya, I've missed you so much.' Russian misses 'along' someone: po tebe. The word soskuchilsya comes from skuchat, 'to be bored'."),
    (2, None, "'We saw each other this morning.' The -sya ending in videlis makes it 'saw each other'. The word utrom, 'in the morning', is utro with the ending -om."),
    (3, None, "'You look so beautiful today.' Russian has no 'look' here: ty takaya krasivaya, literally 'you are such beautiful'."),
    (4, None, "'Thanks. But we need to talk.' She repeats nam nado pogovorit word for word."),
    (5, None, "'Let's talk later, okay?' The word davay with a 'we' form, pogovorim, makes 'let's'. The word potom means 'later'."),
    (6, None, "'You're running away from the conversation again.' The word ubegaesh, 'you run away', is built from u-, 'away', and begat, 'to run'."),
    (7, None, "'No, I just have a lot of work.' After mnogo, 'a lot of', rabota, 'work', changes its ending to raboty."),
]
