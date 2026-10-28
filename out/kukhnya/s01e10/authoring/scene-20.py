# Authoring module for kukhnya-s01e10-scene-20.
ID = 'kukhnya-s01e10-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 20
TITLE = 'Шокирующая новость  (Shocking News)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = 'Max is on his way to the kitchen when Vika stops him. She says she has something to tell him, something she has no right to keep from him. Just listen, and see how much you pick up.'
OPENER = 'This time, with explanations.'
TRANSITION = 'Once more, at the pace of a real conversation.'
OUTRO = 'Max is left with the biggest piece of news of his life. He has no answer. Back soon.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Привет, Вика. Как твои дела?', 'Hi, Vika. How are you doing?', [(156, 'Привет'), (156, 'Как дела?')], ''),
    ('vika', 'Привет. Всё нормально, а у тебя?', 'Hi. Everything is fine, and with you?', [(156, 'Привет'), (157, 'у тебя')], ''),
    ('max', 'У меня тоже всё хорошо, бегу.', 'Everything is fine with me too, running.', [(157, 'у меня')], ''),
    ('vika', 'Стой, подожди хотя бы одну секунду.', 'Wait, wait at least one second.', [(158, 'Стой')], ''),
    ('max', 'Что такое? Шеф ждёт на кухне.', 'What is it? The chef is waiting in the kitchen.', [], ''),
    ('vika', 'Мне срочно нужно поговорить с тобой.', 'I urgently need to talk to you.', [(159, 'Мне нужно поговорить с тобой')], ''),
    ('vika', 'Есть одна очень важная личная вещь.', 'There is one very important personal thing.', [(160, 'Есть одна вещь')], ''),
    ('max', 'Ты пугаешь меня таким серьёзным видом.', 'You scare me with such a serious look.', [], ''),
    ('vika', 'Я не могу больше скрывать правду.', 'I can no longer hide the truth.', [(160, 'скрывать от тебя')], ''),
    ('vika', 'Я знаю, что я нравлюсь тебе.', 'I know that you like me.', [(161, 'тебе нравлюсь')], ''),
    ('vika', 'Я беременна от тебя, Макс.', 'I am pregnant with your child, Max.', [(161, 'Я беременна от тебя')], ''),
    ('max', 'Что ты только что сейчас сказала?', 'What did you just say right now?', [], ''),
    ('vika', 'Ты слышал меня отлично с первого раза.', 'You heard me perfectly the first time.', [], ''),
]
WALK = [
    (0, None, '\'Hi, Vika. How are you doing?\' "Privet" is the friendly hello. "Kak tvoi dela", literally "how are your affairs", is the everyday "how are you". "Tvoi" is the informal "your".'),
    (1, None, '\'Hi. Everything is fine, and with you?\' "Vsyo normalno", "everything normal", is how people say "I\'m fine". "A u tebya?", literally "and at you?", is "and you?". It\'s an ordinary exchange.'),
    (2, None, '\'Everything is fine with me too, running.\' "U menya tozhe" is "with me too". "Begu", "I\'m running", is the usual way to say "I\'ve got to go". Max is trying to leave.'),
    (3, None, '\'Wait, wait at least one second.\' "Stoy", literally "stand", is "stop" or "wait". "Podozhdi" is "wait" too. "Khotya by", "at least", is two small words. Vika asks for one second.'),
    (4, None, '\'What is it? The chef is waiting in the kitchen.\' "Chto takoe?" is "what is it?" or "what\'s up?". "Zhdyot" is "is waiting", and "na kukhne" is "in the kitchen". Max uses the chef as an excuse.'),
    (5, None, '\'I urgently need to talk to you.\' "Mne nuzhno", literally "to me it is needed", is "I need". "Pogovorit s toboy" is "to talk with you". "Srochno" is "urgently".'),
    (6, None, '\'There is one very important personal thing.\' "Est" opens the line and means "there is". "Lichnaya veshch" is "a personal thing": "veshch" is a general word for "thing". "Vazhnaya" is "important".'),
    (7, None, '\'You scare me with such a serious look.\' "Pugaesh" is "you scare", the family of "ispugalsya", "got scared". "Takim seryoznym vidom" is "with such a serious look": "vid" means "look" or "appearance". Max is nervous.'),
    (8, None, '\'I can no longer hide the truth.\' "Skryvat" is "to hide, to keep secret". "Ne mogu bolshe", literally "I can\'t more", is "I can no longer". "Pravdu" is "the truth", from "pravda".'),
    (9, None, '\'I know that you like me.\' "Ya nravlyus tebe", literally "I am pleasing to you", is how Russian says "you like me". The person who is liked comes first. "Znayu" is "I know".'),
    (10, None, '\'I am pregnant with your child, Max.\' "Beremenna ot tebya", literally "pregnant from you", is how Russian says it. "Beremenna" has the -a ending because Vika is a woman. She says it plainly.'),
    (11, None, '\'What did you just say right now?\' "Skazala" is "you said", with -la because he is talking to a woman. To a man it would be "skazal". "Tolko chto" is "just now".'),
    (12, None, '\'You heard me perfectly the first time.\' "S pervogo raza", literally "from the first time", is "the first time". "Slyshal" is "heard", with the -l for Max. "Otlichno" is "perfectly". She won\'t repeat it.'),
]
