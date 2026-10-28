# Authoring module for kukhnya-s01e01-scene-17.
ID = 'kukhnya-s01e01-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 17
TITLE = 'Неожиданная встреча  (An Unexpected Encounter)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'Vika turns a corner in the corridor and runs straight into Max, the man she met in the nightclub. Max plays it cool and says the head chef is begging him to join the kitchen, which makes her furious. Here is the argument in Russian first.'
OPENER = 'Now the argument, piece by piece.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Vika storms off to check his story with the chef herself. Max, meanwhile, has shown you how a cheeky person swings between "you" and "your".'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Подожди минуту... Ты что здесь вообще делаешь?', 'Wait a minute... What are you doing here at all?', [(149, 'Ты что здесь делаешь')], ''),
    ('max', 'Привет, я просто гуляю по твоему ресторану.', 'Hello, I am simply strolling through your restaurant.', [(150, 'Да вот болтал')], ''),
    ('vika', 'Как ты посмел прийти в моё заведение?', 'How did you dare to come into my establishment?', [(149, 'Ты что здесь делаешь')], ''),
    ('max', 'Я только что долго болтал с вашим шеф-поваром.', 'I was just chatting for a long time with your head chef.', [(150, 'болтал с вашим шеф-поваром')], ''),
    ('vika', 'И о чём же ты с ним разговаривал?', 'And what did you talk with him about?', [(150, 'с вашим шеф-поваром')], ''),
    ('max', 'Он настойчиво зовёт меня работать к себе.', 'He is persistently inviting me to work with him.', [(151, 'Зовет к себе')], ''),
    ('vika', 'Ты шутишь, шеф никогда не берёт новичков!', 'You are joking, the chef never takes novices!', [(151, 'Зовет к себе')], ''),
    ('max', 'Вот стою и думаю, соглашаться или нет.', 'Here I stand and think, whether to agree or not.', [(151, 'Вот думаете или нет')], ''),
    ('vika', 'Ты смеешь ещё сомневаться в нашем уровне?', 'Do you dare to still doubt our level?', [(151, 'кухня, скажешь, простовато')], ''),
    ('max', 'Честно говоря, ваша кухня мне кажется простоватой.', 'Frankly speaking, your kitchen seems a bit basic to me.', [(151, 'кухня, скажешь, простовато')], ''),
    ('vika', 'Наш ресторан — один из лучших в Москве!', 'Our restaurant is one of the best in Moscow!', [(151, 'кухня')], ''),
    ('max', 'Тогда я, пожалуй, соглашусь показать свой талант.', 'Then I, perhaps, will agree to show my talent.', [(151, 'Зовет к себе')], ''),
    ('vika', 'Я сейчас лично проверю эти нелепые слова!', 'I will personally check these ridiculous words right now!', [(149, 'Ты что здесь делаешь')], ''),
]
WALK = [
    (0, None, '\'Wait a minute... What are you doing here at all?\' "Podozhdi" is the friendly command "wait", and "minutu" takes an -u. "Vobshche" is "at all", the word that makes her sound exasperated.'),
    (1, None, '\'Hello, I am simply strolling through your restaurant.\' "Privet" is the casual hello, as opposed to the long polite one. "Po tvoyemu restoranu" is "around your restaurant": "po" calls for that ending.'),
    (2, None, '\'How did you dare to come into my establishment?\' "Posmel" is "dared", with -l. "Zavedeniye" is a word for any place that\'s been "set up": restaurant, cafe, bar. It sounds a little grand, which suits Vika.'),
    (3, None, '\'I was just chatting for a long time with your head chef.\' "Tol\'ko chto" is "just now", literally "only what". "Boltal" is slang for chatting. Here Max says "vashim", the polite "your", after "tvoyemu" earlier, so he slides between friendly and formal.'),
    (4, None, '\'And what did you talk with him about?\' "O chyom" is "about what": "chto" turns into "chyom" after "o". "S nim" is "with him", and Russian adds an "n" to "him" after "s".'),
    (5, None, '\'He is persistently inviting me to work with him.\' "Nastoychivo" is "persistently", from "nastoychivyy", with the -o ending. "K sebe" is "to himself", which Russian uses for "to his place".'),
    (6, None, '\'You are joking, the chef never takes novices!\' "Shutish\'" comes from "shutka", a joke. "Nikogda ne beryot" is "never not takes", with the double negative. "Novichok" is a newcomer, from "novyy".'),
    (7, None, '\'Here I stand and think, whether to agree or not.\' "Vot stoyu" is "here I stand", close to the English phrase. "Ili net" is "or not", literally "or no".'),
    (8, None, '\'Do you dare to still doubt our level?\' "Smeyesh\'" is "you dare", from the same root as "posmel", and "yeshchyo" is "still". "Somnevat\'sya v" is "to doubt in".'),
    (9, None, '\'Frankly speaking, your kitchen seems a bit basic to me.\' "Chestno govorya" is literally "honestly speaking". "Mne kazhetsya" is "it seems to me". And "prostovataya" has "-ovat-", which adds "somewhat" to "prostaya", simple.'),
    (10, None, '\'Our restaurant is one of the best in Moscow!\' "Odin iz luchshikh" is "one of the best", literally "one from the best", with a plural ending on "best". The dash stands for "is".'),
    (11, None, '\'Then I, perhaps, will agree to show my talent.\' "Pozhaluy" is "perhaps", a softener you can drop into any sentence. "Soglashus\'" is "I will agree", and "svoy" is "my own".'),
    (12, None, '\'I will personally check these ridiculous words right now!\' "Lichno" is "personally", from "lichnyy". "Proveryu" is "I will check", and "nelepyye" is "ridiculous", plural to match "slova", words.'),
]
