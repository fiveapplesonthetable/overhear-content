# Authoring module for kukhnya-s01e08-scene-11.
ID = 'kukhnya-s01e08-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 11
TITLE = 'Комплимент от шефа  (A Compliment from the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Elena is running Barinov's kitchen at Claude Monet for the day. She stops beside Fedya, one of the cooks, and praises the way he fries fish. Fedya is not used to compliments. It's in Russian first."
OPENER = 'Slowly now. Each compliment from Elena gets a suspicious answer from Fedya, until he gives in.'
TRANSITION = 'Now the whole conversation again, in one go.'
OUTRO = "Fedya's line mne nikogda ne govorili takikh slov, 'nobody ever told me such words', is a good way to accept a compliment. And s pervogo vzglyada, 'at first sight', works for talent and for love. See you next time."
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('elena', 'Федя, скажите, вы случайно учились во Франции?', 'Fedya, tell me, did you by chance study in France?', [(125, 'Федя, вы учились во Франции')], ''),
    ('fedya', 'Делать мне больше нечего, чем учиться там!', 'Like I had nothing better to do than study there!', [(126, 'Дел с меня больше нечего')], ''),
    ('elena', 'У вас просто потрясающая техника обжарки рыбы.', 'You have simply amazing technique for frying fish.', [(127, 'просто такую обжарку делают только в Лионе')], ''),
    ('fedya', 'Я просто жарю рыбу на горячей сковороде.', 'I simply fry fish on a hot pan.', [], ''),
    ('elena', 'Такую обжарку делают только в Лионе у Бокюза.', "They only do such searing in Lyon at Bocuse's.", [(127, 'только в Лионе у мэтра Бакёза')], ''),
    ('fedya', 'Вы серьёзно сравниваете меня с французским мастером?', 'Are you seriously comparing me to a French master?', [], ''),
    ('elena', 'Абсолютно серьёзно, у вас редкий природный дар.', 'Absolutely seriously, you have a rare natural gift.', [(128, 'у вас природный дар')], ''),
    ('fedya', 'Мне никогда раньше не говорили таких слов.', 'Nobody ever told me such words before.', [], ''),
    ('elena', 'Настоящий талант всегда виден с первого взгляда.', 'True talent is always visible at first sight.', [], ''),
    ('fedya', 'Спасибо большое за такую высокую оценку, шеф.', 'Thank you very much for such high praise, Chef.', [], ''),
    ('elena', 'Продолжайте готовить, гости будут в полном восторге.', 'Continue cooking, the guests will be in complete delight.', [], ''),
    ('fedya', 'Обещаю сделать самое вкусное блюдо сегодня!', 'I promise to make the most delicious dish today!', [], ''),
]
WALK = [
    (0, None, "'Fedya, tell me, did you by chance study in France?' Elena says skazhite, the polite 'tell', much like 'tell me' in English. Putting sluchayno, 'by chance', in the question softens it, like 'did you happen to'."),
    (1, None, "'Like I had nothing better to do than study there!' Fedya's delat mne bolshe nechego, literally 'to do for me more nothing', is a sarcastic 'as if I had nothing better to do'. And uchitsya, 'to study', always carries its -sya."),
    (2, None, "'You have simply amazing technique for frying fish.' Cooks call searing obzharka, from obzharit, 'to fry on all sides'. And ryby, 'of fish', is ryba with the 'of' ending."),
    (3, None, "'I simply fry fish on a hot pan.' For frying, Russian has zharit, so 'I fry' is zharyu. On a hot pan is na goryachey skovorode, with the location endings -ey and -e."),
    (4, None, "'They only do such searing in Lyon at Bocuse's.' To say 'at someone's place', Russian uses u plus the person, the way u menya can mean 'at my place'. With delayut, 'they do', and no subject, it means 'it is done'."),
    (5, None, "'Are you seriously comparing me to a French master?' After sravnivat, 'to compare', comes s, 'with', and the -im, -om endings: s frantsuzskim masterom. Elena repeats his seryozno, 'seriously', in her answer."),
    (6, None, "'Absolutely seriously, you have a rare natural gift.' Like English 'gift', dar means a talent, and comes from darit, 'to give a present'. The word prirodnyy, 'natural', is built on priroda, 'nature'."),
    (7, None, "'Nobody ever told me such words before.' With no subject, mne ne govorili, literally 'to me they didn't say', means 'nobody told me'. After ne, the object switches to the 'of' form: takikh slov."),
    (8, None, "'True talent is always visible at first sight.' The short form viden, 'visible', would be vidna with a feminine word. The set phrase s pervogo vzglyada, literally 'from the first look', means 'at first sight'."),
    (9, None, "'Thank you very much for such high praise, Chef.' A vysokaya otsenka is literally a high mark, as at school, and here it means high praise. After za, it becomes takuyu vysokuyu otsenku."),
    (10, None, "'Continue cooking, the guests will be in complete delight.' Elena's prodolzhayte, 'carry on', is polite, and the activity follows it: prodolzhayte gotovit. To be thrilled is to be v polnom vostorge, 'in complete delight'."),
    (11, None, "'I promise to make the most delicious dish today!' Fedya's obeshchayu, 'I promise', takes the action straight after it: obeshchayu sdelat. For 'the most', Russian puts samyy in front, here samoye vkusnoye to match blyudo."),
]
