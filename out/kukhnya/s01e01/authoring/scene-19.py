# Authoring module for kukhnya-s01e01-scene-19.
ID = 'kukhnya-s01e01-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 19
TITLE = 'Настоящий профессионал  (A True Professional)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'Max has been given a kitchen jacket and is eager to show off. Chef Barinov first sends everybody back to work, and then turns to Max with some pointed questions about what a professional cook actually does. This is the conversation in Russian first.'
OPENER = "Let's go back over the chef's questions."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max feels like a professional, but the chef has a job in mind that is not cooking. You\'ve learned a few ways to say "I can" and "I know how".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Все за работу, быстро!', 'Everyone get to work, quickly!', [(168, 'все за работу')], ''),
    ('barinov', 'А ты иди переодевайся!', 'And you, go get changed!', [(171, 'Иди переодевайся')], ''),
    ('max', 'Шеф, я готов. Что мне делать?', 'Chef, I am ready. What should I do?', [(174, 'Шеф, я готов'), (175, 'Что мне делать')], ''),
    ('barinov', 'Почему ты пришёл на эту кухню?', 'Why did you come to this kitchen?', [(179, 'Чего тебе на кухню понесло')], ''),
    ('max', 'Потому что я повар. Я настоящий профессионал.', 'Because I am a cook. I am a true professional.', [(180, 'потому что я повар'), (181, 'Я профессионал')], ''),
    ('barinov', 'Профессионал? Иди сюда.', 'A professional? Come here.', [(183, 'Профессионал'), (183, 'Иди сюда')], ''),
    ('barinov', 'Посмотри вокруг на моих поваров.', 'Look around at my cooks.', [(184, 'Вон, видишь')], ''),
    ('barinov', 'Что ты сам умеешь делать?', 'What can you do yourself?', [(194, 'А ты что можешь')], ''),
    ('max', 'Я очень хорошо умею готовить.', 'I can cook very well.', [(195, 'Я готовить умею')], ''),
    ('barinov', 'Да ну? Всем внимание на кухне!', 'Really? Attention everyone in the kitchen!', [(196, 'Да ну'), (197, 'Внимание')], ''),
    ('barinov', 'К нам пришёл великий повар!', 'A great cook has come to us!', [(199, 'человек, который умеет готовить')], ''),
    ('barinov', 'Мы так долго ждали его!', 'We waited for him for so long!', [(200, 'Мы пять лет ждали его'), (201, 'Он пришел')], ''),
    ('max', 'Какая у меня будет работа?', 'What work will I have?', [(203, 'Есть работа')], ''),
    ('barinov', 'Для тебя есть особенная работа!', 'There is a special job for you!', [(203, 'Есть работа'), (204, 'Только тебе')], ''),
]
WALK = [
    (0, None, '\'Everyone get to work, quickly!\' No verb at all: Barinov just says "everyone onto work", and "za rabotu" with -u is how you send people to a task. "Bystro", quickly, is the word behind "bystreye", faster.'),
    (1, None, '\'And you, go get changed!\' "A ty" is "and you", with "a" for contrast: everyone else works, you change. "Pereodevaysya" is "pere-", re-, plus "odevat\'", to dress, and the final "-sya" means you\'re dressing yourself.'),
    (2, None, '\'Chef, I am ready. What should I do?\' "Gotov" is "ready", from the same family as "gotovit\'", to cook: cooking is getting things ready. "Chto mne delat\'" is "what to me to do".'),
    (3, None, '\'Why did you come to this kitchen?\' The chef says "ty" to his new cook straight away. "Na etu kukhnyu" ends in -u because it\'s movement toward a place; being in the kitchen would be "na etoy kukhne".'),
    (4, None, '\'Because I am a cook. I am a true professional.\' "Pochemu" asks and "potomu chto" answers: "why" and "because" are a matching pair. "Professional" is borrowed.'),
    (5, None, '\'A professional? Come here.\' "Idi syuda" is literally "go here". Russian uses one verb, "idti", for both "come" and "go" on foot, and "syuda", "to here", tells you which.'),
    (6, None, '\'Look around at my cooks.\' "Vokrug" is "v" plus "krug", in a circle, so "around". "Posmotri" is "look". "Moikh povarov" is "my cooks", ending in the plural "-ov".'),
    (7, None, '\'What can you do yourself?\' "Sam" is "yourself", which pushes the question back at Max. "Umeyesh\'" is "you know how to", the skill word.'),
    (8, None, '\'I can cook very well.\' "Khorosho" is "well", from "khoroshiy", good. "Umeyu gotovit\'" is "I know how to cook", with Max sure of himself.'),
    (9, None, '\'Really? Attention everyone in the kitchen!\' "Da nu" is a sarcastic "really?". "Vsem vnimaniye" is "to everyone, attention", with "vsem" the "to" form of "all".'),
    (10, None, '\'A great cook has come to us!\' "Velikiy" is "great", as in a great king, and here it\'s mockery. "K nam" is "to us".'),
    (11, None, '\'We waited for him for so long!\' The -li on "zhdali" is the plural past ending, so "we waited". "Yego", him, is the same word as "his", and in that "his" sense it never changes.'),
    (12, None, '\'What work will I have?\' "U menya budet" is "at me will be", the "I have" pattern in the future. "Kakaya", "what kind of", ends in "-aya" to match "rabota".'),
    (13, None, '\'There is a special job for you!\' "Yest\'" is "there is", a word Russian often leaves out in the present, so when the chef says it, he means it. "Dlya tebya" is "for you", in the friendly form.'),
]
