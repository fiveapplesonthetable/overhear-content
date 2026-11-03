# Authoring module for kukhnya-s01e08-scene-16.
ID = 'kukhnya-s01e08-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 16
TITLE = "Возвращение Шефа  (The Chef's Return)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Back in the kitchen at Claude Monet, Senya and Fedya, two of Barinov's cooks, are comparing their new, polite chef, Elena, with the old one. Then Barinov comes back in a terrible temper. It's in Russian first."
OPENER = 'Slowly now. The first half is a quiet chat, and the second half is Barinov.'
TRANSITION = 'Now the whole thing again, calm and then loud.'
OUTRO = "That small Russian connector meaning 'but on the other hand' wins plenty of arguments, while Barinov's 'quick, back to work' is what every boss barks sooner or later. See you next time."
CLOSING = ('senya', 'Пока!')
STORY = [
    ('senya', 'Ну, как тебе новый шеф-повар?', 'Well, how do you like the new head chef?', [(203, 'Ну и как тебе новый шеф')], ''),
    ('fedya', 'Она кажется мне немного скучной.', 'She seems a bit boring to me.', [(204, 'какая-то она нудная')], ''),
    ('senya', 'Зато она спокойная и вежливая.', 'On the other hand she is calm and polite.', [(205, 'Зато адекватная')], ''),
    ('fedya', 'Это правда, она никогда не кричит.', 'That is true, she never yells.', [(206, 'Ну да, не то что этот')], ''),
    ('senya', 'С ней на кухне тихо и приятно.', 'With her the kitchen is quiet and pleasant.', [], ''),
    ('barinov', 'Бездельники! Огрызки! Что вы делаете?', 'Slackers! Scraps! What are you doing?', [(207, 'Гузки!'), (208, 'Огрызки! Огрызки! Уничтожу!')], ''),
    ('barinov', 'Я вернулся навести полный порядок!', 'I returned to restore complete order!', [(208, 'Уничтожу!')], ''),
    ('fedya', 'Шеф, мы просто чистили рыбу.', 'Chef, we were just cleaning the fish.', [(210, 'Ой, шеф, а мы это')], ''),
    ('senya', 'Мы очень рады видеть вас!', 'We are very glad to see you!', [], ''),
    ('barinov', 'Прекратите болтать и берите ножи!', 'Stop chatting and take your knives!', [(209, 'Раз, два, два!')], ''),
    ('barinov', 'Кто разрешил вам стоять без дела?', 'Who permitted you to stand idle?', [], ''),
    ('fedya', 'Мы сейчас всё нарежем, шеф.', 'We will chop everything right now, chef.', [], ''),
    ('barinov', 'Быстро за работу, живо!', 'Get to work quickly, lively!', [(211, 'Да пошли вы')], ''),
]
WALK = [
    (0, None, ["'Well, how do you like the new head chef?' The question ends with the title ", ('senya', 'шеф-повар'), ', which is an imported word for head chef.']),
    (1, None, ["'She seems a bit boring to me.' He finds the new situation quite ", ('fedya', 'скучной'), ', a word for dull or boring.']),
    (2, None, ["'On the other hand she is calm and polite.' He prefers how their new boss is ", ('senya', 'вежливая'), ', the word for polite or courteous.']),
    (3, None, ["'That is true, she never yells.' It is a relief that nobody ", ('fedya', 'кричит'), ', meaning yells or shouts loudly.']),
    (4, None, ["'With her the kitchen is quiet and pleasant.' Now the working environment feels remarkably ", ('senya', 'тихо'), ', meaning quiet and peaceful.']),
    (5, None, ["'Slackers! Scraps! What are you doing?' The angry entrance starts by shouting ", ('barinov', 'Бездельники'), ', a harsh insult for people who do no work.']),
    (6, None, ["'I returned to restore complete order!' He announces his arrival by stating he ", ('barinov', 'вернулся'), ', meaning returned or came back.']),
    (7, None, ["'Chef, we were just cleaning the fish.' Trying to look busy, they claim they ", ('fedya', 'чистили'), ', meaning they were cleaning or scaling.']),
    (8, None, ["'We are very glad to see you!' They try to smooth things over by saying they are ", ('senya', 'рады'), ', meaning glad or happy.']),
    (9, None, ["'Stop chatting and take your knives!' He orders them to pick up their ", ('barinov', 'ножи'), ', the tools they need for cutting food.']),
    (10, None, ["'Who permitted you to stand idle?' The boss demands to know who ", ('barinov', 'разрешил'), ', meaning allowed or gave permission.']),
    (11, None, ["'We will chop everything right now, chef.' Promising immediate action, they say they will ", ('fedya', 'нарежем'), ', meaning chop or slice up a batch of ingredients.']),
    (12, None, ["'Get to work quickly, lively!' Barking a final order, he adds ", ('barinov', 'живо'), ', meaning lively or look sharp.']),
]
