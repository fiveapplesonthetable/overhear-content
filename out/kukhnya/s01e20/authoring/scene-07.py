# Authoring module for kukhnya-s01e20-scene-07.
ID = 'kukhnya-s01e20-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 7
TITLE = 'Неожиданный поворот  (An Unexpected Turn)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = 'Nastya tries a third time, and Kostya keeps finding reasons to be somewhere else. Listen to it in Russian first.'
OPENER = "Let's look closer."
TRANSITION = 'One more time from the top.'
OUTRO = "Kostya runs off to the kitchen again. The pair bolshe ne means 'no longer' or 'not any more'. See you next time!"
CLOSING = ('kostya', 'Увидимся!')
STORY = [
    ('nastya', 'Костя, давай поговорим.', 'Kostya, let us talk.', [], ''),
    ('kostya', 'Сейчас? Я очень занят.', 'Now? I am very busy.', [], ''),
    ('nastya', 'Ты всегда занят.', 'You are always busy.', [], ''),
    ('kostya', 'Ты больше не сердишься?', 'You are not angry any more?', [(140, 'Ты больше')], ''),
    ('nastya', 'Я не сержусь. Я просто хочу поговорить.', 'I am not angry. I just want to talk.', [], ''),
    ('kostya', 'Давай завтра, хорошо?', 'Let us do it tomorrow, okay?', [], ''),
    ('nastya', 'Нет, Костя, надо сейчас.', 'No, Kostya, it has to be now.', [], ''),
    ('kostya', 'Ой, мне надо на кухню.', 'Oh, I have to go to the kitchen.', [], ''),
]
WALK = [
    (0, None, "'Kostya, let's talk.' The word davay, 'come on', plus a 'we' form, pogovorim, makes 'let's' in Russian."),
    (1, None, "'Now? I'm very busy.' The word zanyat, 'busy', has no ending because Kostya is a man; Nastya would say zanyata."),
    (2, None, "'You're always busy.' Russian puts vsegda, 'always', before the word it goes with, just like English."),
    (3, None, "'You're not angry any more?' The pair bolshe ne means 'no longer'; on its own bolshe means 'more'."),
    (4, None, "'I'm not angry. I just want to talk.' In serzhus, 'I'm angry', the d of serdishsya turns into zh, and the ending changes for 'I'."),
    (5, None, "'Let's do it tomorrow, okay?' Russian needs no verb here: davay zavtra means 'let's make it tomorrow'."),
    (6, None, "'No, Kostya, it has to be now.' Russian says nado seychas, literally 'needed now', with no 'it' and no 'be'."),
    (7, None, "'Oh, I have to go to the kitchen.' Again Russian drops 'to go': mne nado na kukhnyu. After na, kukhnya becomes kukhnyu."),
]
