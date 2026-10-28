# Authoring module for kukhnya-s01e18-scene-04.
ID = 'kukhnya-s01e18-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 4
TITLE = 'Дорогой коньяк  (Expensive Cognac)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "Max's lessons for Kostya go on behind the bar. This time Max plays a rich customer, and the trick involves expensive cognac. Here it is in Russian first; just get a feel for the role-play."
OPENER = "Let's unpack it, line by line."
TRANSITION = 'Now the role-play again, without stopping.'
OUTRO = 'Kostya plays along, but he doesn\'t like where this is going. Listen again for "koroche", literally \'shorter\', which Max uses to get to the point. See you next time!'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Это ещё не всё, слушай дальше.', 'That is not all yet, listen further.', [(129, 'Еще не все. Слушай дальше.')], ''),
    ('kostya', 'Какой ещё секрет ты мне покажешь?', 'What other secret will you show me?', [], ''),
    ('max', 'Сейчас я покажу тебе новый фокус.', 'Now I will show you a new trick.', [], ''),
    ('max', 'Короче, сначала ты берёшь чистый стакан.', 'In short, first you take a clean glass.', [(130, 'берешь стакан')], ''),
    ('kostya', 'Хорошо, я взял большой красивый бокал.', 'Alright, I took a large beautiful glass.', [], ''),
    ('max', 'Теперь представь, что я богатый гость.', 'Now imagine that I am a rich guest.', [], ''),
    ('kostya', 'Что вы желаете заказать сегодня вечером?', 'What would you like to order tonight?', [], ''),
    ('max', 'Налей мне пятьдесят грамм дорогого коньяка.', 'Pour me fifty grams of expensive cognac.', [(131, '50 грамм')], ''),
    ('kostya', 'Отличный выбор, сейчас всё будет сделано.', 'Great choice, everything will be done right now.', [(132, 'Будет сделано.')], ''),
    ('max', 'Но наливай не дорогой, а дешёвый коньяк!', 'But pour cheap cognac, not the expensive one!', [], ''),
    ('kostya', 'Ты думаешь, гость совсем ничего не заметит?', 'Do you think the guest will notice nothing at all?', [], ''),
    ('max', 'Поверь мне, никто не почувствует разницу!', 'Believe me, nobody will feel the difference!', [], ''),
]
WALK = [
    (0, None, '\'That\'s not all, keep listening.\' "Eshchyo ne vsyo", literally \'still not all\'. "Slushay dalshe", listen further, means \'there\'s more\'.'),
    (1, None, '\'What other secret are you going to show me?\' "Kakoy eshchyo" means \'what other\', a bit wary. "Pokazhesh" ends in "-esh" because Kostya says "ty" to Max.'),
    (2, None, '\'Now I\'ll show you a new trick.\' A "fokus" is a magic trick, not focus. In "pokazhu", I\'ll show, the \'z\' of "pokazat" turns into \'zh\'.'),
    (3, None, '\'Anyway, first you take a clean glass.\' "Koroche" is literally \'shorter\', meaning \'long story short\'. "Beryosh", you take, is the general \'you\' of instructions.'),
    (4, None, '\'Okay, I\'ve got a big, beautiful glass.\' "Vzyal", took, ends in "-l", the past tense for a man. A "bokal" is a stemmed glass, fancier than a "stakan".'),
    (5, None, '\'Now imagine I\'m a rich guest.\' "Predstav" is a command to one friend: imagine. Present tense has no \'am\', so it\'s just \'that I rich guest\'.'),
    (6, None, '\'What would you like to order this evening?\' In the role-play Kostya switches to the polite "vy": "chto vy zhelaete", what do you wish, is waiter talk.'),
    (7, None, '\'Pour me fifty grams of expensive cognac.\' "Nalei" is the command \'pour\'. After fifty you get "gramm", and the cognac takes \'of\' endings: "dorogogo konyaka".'),
    (8, None, '\'Excellent choice, it\'ll be done right away.\' "Budet sdelano", will be done, ends in \'o\' to agree with "vsyo", everything. Bartenders really say it.'),
    (9, None, '\'But don\'t pour the expensive one, pour the cheap one!\' The pattern "ne" X, "a" Y means \'not X but Y\'. Here: "ne dorogoy, a deshyovyy".'),
    (10, None, '\'You think the guest won\'t notice anything at all?\' Three negative words in a row are normal Russian: "sovsem nichego ne zametit", literally \'at all nothing not will notice\'.'),
    (11, None, '\'Trust me, nobody will taste the difference!\' "Pover mne": the verb takes "mne", to me, not \'me\'. "Pochuvstvuet" means will feel, here will taste.'),
]
