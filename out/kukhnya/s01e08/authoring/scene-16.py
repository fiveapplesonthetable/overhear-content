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
OUTRO = "The small word zato, 'but on the other hand', wins arguments. And bystro za rabotu, 'quick, to work', is what every boss says sooner or later. See you next time."
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
    (0, None, "'Well, how do you like the new head chef?' Senya's kak tebe, literally 'how to you', is a short, casual way to ask an opinion. The nu at the start is a filler, like 'well'."),
    (1, None, "'She seems a bit boring to me.' With kazhetsya mne, 'seems to me', the person gets a 'to' form. After kazatsya, 'to seem', the description takes the ending -oy: skuchnoy."),
    (2, None, "'On the other hand she is calm and polite.' Here zato means 'but then, on the plus side', bringing in a point in her favour. Since they describe Elena, spokoynaya and vezhlivaya end in -aya."),
    (3, None, "'That is true, she never yells.' Like nikto ne, nikogda, 'never', needs ne before the action: nikogda ne krichit. And krichit, 'she yells', comes from krichat."),
    (4, None, "'With her the kitchen is quiet and pleasant.' After s, 'with', ona becomes ney: s ney. Russian needs no subject here: tikho and priyatno simply describe the mood."),
    (5, None, "'Slackers! Scraps! What are you doing?' A bezdelnik, 'slacker', is someone bez dela, 'without work'. An ogryzok is literally an apple core or a gnawed leftover, and as an insult it's very rude."),
    (6, None, "'I returned to restore complete order!' In vernulsya, 'I came back', the -lsya shows the speaker is a man. The fixed phrase navesti poryadok, 'to bring order', means sorting a place out."),
    (7, None, "'Chef, we were just cleaning the fish.' Fedya's chistili describes what they were busy with when Barinov walked in. To clean fish, chistit rybu, means scaling and gutting it."),
    (8, None, "'We are very glad to see you!' The short plural rady, 'glad', comes from rad. After videt, 'to see', vy becomes vas."),
    (9, None, "'Stop chatting and take your knives!' Barinov's prekratite, 'stop', is said to all of them, with the action after it: boltat, 'to chatter'. With berite, 'take', he means 'get on with it'."),
    (10, None, "'Who permitted you to stand idle?' The one allowed gets a 'to' form after razreshil, so it's vam. And bez dela, 'without work', is the idea behind bezdelnik."),
    (11, None, "'We will chop everything right now, chef.' In narezhem, na- means cutting up a whole batch. Here seychas means 'right away'."),
    (12, None, "'Get to work quickly, lively!' The call to start is za rabotu, 'to work'. And zhivo, 'lively', comes from zhivoy, 'alive', and means 'look sharp'."),
]
