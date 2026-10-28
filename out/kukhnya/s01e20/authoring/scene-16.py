# Authoring module for kukhnya-s01e20-scene-16.
ID = 'kukhnya-s01e20-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 16
TITLE = 'Старые часы  (Old Watch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'old_man': 'Старик'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "Out on the street, Max gives his granddad's old watch to an old man. Here it is in Russian."
OPENER = 'Now the words up close.'
TRANSITION = "Here's the street scene again."
OUTRO = "Max walks on, and the old man keeps the watch. In Russian, the polite reply to spasibo is ne za chto, literally 'not for anything'. See you next time!"
CLOSING = ('old_man', 'Счастливо!')
STORY = [
    ('max', 'На, держись, старик.', 'Here. Hang in there, old man.', [(286, 'На, держись, старик')], ''),
    ('old_man', 'Это мне?', 'Is this for me?', [], ''),
    ('max', 'Тебе. Тебе нужнее.', 'For you. You need it more.', [(287, 'Тебе нужнее')], ''),
    ('old_man', 'Спасибо, сынок.', 'Thank you, son.', [], ''),
    ('max', 'Не за что.', "Don't mention it.", [], ''),
    ('old_man', 'Дай бог тебе здоровья.', 'God bless you.', [], ''),
]
WALK = [
    (0, None, "'Here. Hang in there, old man.' Russian hands things over with na, a little word like 'here, take it', and derzhis literally means 'hold on'."),
    (1, None, "'Is this for me?' Russian needs no verb here: eto mne, literally 'this to me'."),
    (2, None, "'For you. You need it more.' The word nuzhnee means 'more needed', so tebe nuzhnee is literally 'to you it's more needed'."),
    (3, None, "'Thank you, son.' Older people in Russian call a young man synok, literally 'little son', even a stranger."),
    (4, None, "'Don't mention it.' The reply ne za chto literally means 'not for anything', the usual answer to spasibo."),
    (5, None, "'God bless you.' Russian says dai bog tebe zdorovya, literally 'may God give you health', a thank-you you hear from older people."),
]
