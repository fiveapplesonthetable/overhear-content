# Authoring module for kukhnya-s01e05-scene-16.
ID = 'kukhnya-s01e05-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 16
TITLE = 'Укромный уголок  (A Secluded Corner)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Back at Claude Monet, Nastya the waitress leads Kostya, the bartender, into a quiet corner of the storeroom. She needs his help with a plan, and nobody else can hear it. Listen in Russian first.'
OPENER = "Let's slow it down. Nastya whispers, Kostya is curious, and the lines stay short."
TRANSITION = 'Once more, all the way through.'
OUTRO = 'Hold on to the verbs for \'I promise\' and the phrase for \'I\'m all ears\'. Kostya still has no idea what he\'s just agreed to.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Всё, тут нам никто не помешает.', 'There, nobody will bother us here.', [(207, 'никто не помешает')], ""),
    ('kostya', 'Настя, зачем мы сюда пришли?', 'Nastya, why did we come here?', [], ""),
    ('nastya', 'Нам нужно тихо поговорить без свидетелей.', 'We need to talk quietly without witnesses.', [], ""),
    ('kostya', 'Здесь действительно очень тихо и спокойно.', 'It is indeed very quiet and peaceful here.', [], ""),
    ('nastya', 'Ты готов мне немного помочь?', 'Are you ready to help me a little?', [], ""),
    ('kostya', 'Конечно, я всегда рад помочь тебе.', 'Of course, I am always glad to help you.', [], ""),
    ('nastya', 'Только пообещай никому ничего не рассказывать.', 'Only promise not to tell anyone anything.', [], ""),
    ('kostya', 'Обещаю, это будет наша общая тайна.', 'I promise, this will be our shared secret.', [], ""),
    ('nastya', 'Отлично, тогда слушай меня очень внимательно.', 'Great, then listen to me very carefully.', [], ""),
    ('kostya', 'Я весь во внимании, говори скорее.', 'I am all ears, speak quickly.', [], ""),
    ('nastya', 'Мы разыграем один очень хитрый спектакль!', 'We will play out a very clever show!', [], ""),
    ('kostya', 'Ну да, я пока ничего не понимаю.', 'Well yeah, I do not understand anything yet.', [(208, 'Ну да')], ""),
    ('nastya', 'Скоро ты сам всё отлично поймёшь!', 'Soon you will understand everything perfectly yourself!', [], ""),
]
WALK = [
    (0, None, ['\'There, nobody will bother us here.\' here translates to \'right, that\'s it\', ', ('nastya', 'Всё,'), " not 'everything'. ", ('nastya', 'никто'), ('nastya', 'не'), ('nastya', 'помешает.'), " keeps the negative term even with the pronoun for 'nobody'."]),
    (1, None, ['\'Nastya, why did we come here?\' asks about the purpose, \'what ', ('kostya', 'зачем'), " for'. ", ('kostya', 'сюда'), " is 'here' in the sense of 'to here', for movement, and ", ('kostya', 'пришли?'), " indicates arriving on foot."]),
    (2, None, ['\'We need to talk quietly without witnesses.\' translates literally to \'to us it\'s ', ('nastya', 'Нам'), ('nastya', 'нужно'), " needed'. The preposition ", ('nastya', 'без'), ", 'without', precedes ", ('nastya', 'свидетелей.'), ", meaning 'witnesses'."]),
    (3, None, ['\'It is indeed very quiet and peaceful here.\' There is no verb for \'is\' in the Russian sentence. ', ('kostya', 'тихо'), " and ", ('kostya', 'спокойно.'), " denote 'it's quiet' and 'it's calm'."]),
    (4, None, ['\'Are you ready to help me a little?\' , \'ready\', is in the masculine ', ('nastya', 'готов'), " form because it is said to a man. ", ('nastya', 'помочь?'), " pairs with 'to me', ", ('nastya', 'мне'), ", as if providing help to someone."]),
    (5, None, ['\'Of course, I am always glad to help you.\' A man says ', ('kostya', 'рад'), ", while a woman would use a different ending. ", ('kostya', 'помочь'), ('kostya', 'тебе.'), ", 'to help you', mirrors Nastya's earlier phrase."]),
    (6, None, ['\'Only promise not to tell anyone anything.\' acts as the command \'promise\'. Then ', ('nastya', 'пообещай'), " come the stacked negatives, ", ('nastya', 'никому'), ('nastya', 'ничего'), ('nastya', 'не'), ('nastya', 'рассказывать.'), ", standing literally for 'to nobody nothing not tell'."]),
    (7, None, ['\'I promise, this will be our shared secret.\' , \'I promise\', directly answers Nastya\'s ', ('kostya', 'Обещаю,'), " command. ", ('kostya', 'общая'), " represents 'shared' or 'common', and ", ('kostya', 'тайна.'), " stands for a secret."]),
    (8, None, ['\'Great, then listen to me very carefully.\' functions as \'great\' or \'excellent\', ', ('nastya', 'Отлично,'), " and ", ('nastya', 'тогда'), " equates to 'then'. ", ('nastya', 'внимательно.'), ", 'carefully', is related to the noun for 'attention'."]),
    (9, None, ['\'I\'m all ears, speak quickly.\' is word for word \'I\'m all ', ('kostya', 'Я'), ('kostya', 'весь'), ('kostya', 'во'), ('kostya', 'внимании,'), " in attention', serving as the Russian version of 'all ears'. ", ('kostya', 'говори'), ('kostya', 'скорее.'), " conveys 'talk faster', suggesting 'go on, quick'."]),
    (10, None, ['\'We will play out a very clever show!\' refers to staging a prank on ', ('nastya', 'разыграем'), " someone. ", ('nastya', 'спектакль!'), " denotes a stage play, while ", ('nastya', 'хитрый'), " carries the meaning of 'cunning'."]),
    (11, None, ['\'Well yeah, I don\'t understand anything yet.\' here expresses \'so far\' or \'yet\', ', ('kostya', 'пока'), " identical to the casual farewell. ", ('kostya', 'ничего'), ('kostya', 'не'), ('kostya', 'понимаю.'), " puts 'nothing' and 'not' together."]),
    (12, None, ['\'Soon you will understand everything perfectly yourself!\' , \'yourself\', adds weight, akin to ', ('nastya', 'сам'), " saying 'on your own'. ", ('nastya', 'поймёшь!'), " describes the future moment when it all clicks."]),
]
