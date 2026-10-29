# Authoring module for kukhnya-s01e04-scene-02.
ID = 'kukhnya-s01e04-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'Встреча конкурентов  (Encounter of the Competitors)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = 'Outside, Chef Barinov meets his rival, Elena Sokolova, and mocks her for hiring cooks through a newspaper ad. Elena replies smoothly that some very good people have already applied, and some may be from his own kitchen. Here is the Russian first.'
OPENER = 'Back to the war of words.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Barinov swears he\'ll eat his hat, and Elena calmly wishes him bon appetit. If you remember anything, take "ya s\'\'yem kolpak", the Russian "I\'ll eat my hat".'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Елена, вы набираете поваров по объявлению?', 'Elena, are you hiring cooks through an ad?', [(6, 'вы персонал по объявлению набираете')], ''),
    ('elena', 'Здравствуйте, Виктор Петрович. Да, мы расширяемся.', 'Hello, Viktor Petrovich. Yes, we are expanding.', [(6, 'Виктор Петрович')], ''),
    ('barinov', 'Поставьте лучше табличку возле метро!', 'You had better put a sign near the metro!', [(7, 'Вы бы лучше табличку у метро поставили')], ''),
    ('elena', 'В этом нет никакой необходимости.', 'There is no need for that.', [(9, 'в этом нет необходимости')], ''),
    ('barinov', 'Нормальные профессионалы не ищут работу по газетам.', 'Normal professionals do not look for work in newspapers.', [(8, 'проходимость профессиональных поваров выше')], ''),
    ('elena', 'Ко мне уже пришли отличные кандидаты.', 'Excellent candidates have already come to me.', [(10, 'пришло несколько отличных поваров')], ''),
    ('barinov', 'И из каких ресторанов эти люди?', 'And from which restaurants are these people?', [], ''),
    ('elena', 'Некоторые работают в очень достойных местах.', 'Some work in very respectable places.', [(11, 'некоторые из них работают в достойных ресторанах')], ''),
    ('barinov', 'Неужели кто-то уходит из хороших ресторанов?', 'Could someone really be leaving good restaurants?', [], ''),
    ('elena', 'Может быть, даже из вашего ресторана.', 'Maybe even from your restaurant.', [(13, 'если вы считаете свой ресторан')], ''),
    ('barinov', 'Я съем колпак, если мои повара уйдут!', "I will eat my chef's hat if my cooks leave!", [(14, 'Я съем свой колпак, если узнаю, что кто-то из моих')], ''),
    ('elena', 'Тогда заранее желаю вам приятного аппетита!', 'Then in advance I wish you bon appétit!', [(15, 'Тогда приятного аппетита')], ''),
    ('barinov', 'Мои люди преданы мне до конца.', 'My people are loyal to me to the end.', [], ''),
]
WALK = [
    (0, None, '\'Elena, are you hiring cooks through an ad?\' "Nabirat\'" is to gather up, and it is the verb for hiring a team. "Po ob\'\'yavleniyu" is "by an announcement", meaning through an ad.'),
    (1, None, '\'Hello, Viktor Petrovich. Yes, we are expanding.\' Elena uses his name and father\'s name, "Viktor Petrovich", which is formal. "Rasshiryayemsya" holds "shirokiy", wide: we widen ourselves.'),
    (2, None, '\'You had better put a sign near the metro!\' "Luchshe", better, before a command turns it into advice. "Tablichka" is a small sign, and "vozle" is "next to".'),
    (3, None, '\'There is no need for that.\' "Net nikakoy neobkhodimosti" is "there isn\'t any necessity". After "net", "neobkhodimost\'" takes the "of" form "neobkhodimosti".'),
    (4, None, '\'Normal professionals do not look for work in newspapers.\' "Ishchut", they look for, is from "iskat\'", to search. "Po gazetam" is "through newspapers", with -am after "po".'),
    (5, None, '\'Excellent candidates have already come to me.\' "Ko mne" is "k", to, with an extra -o so that "k mne" is easier to say. "Prishli", came, is the plural past.'),
    (6, None, '\'And from which restaurants are these people?\' "Iz", out of, puts both words in the plural "of" form: "kakikh restoranov".'),
    (7, None, '\'Some work in very respectable places.\' "Dostoynykh", worthy, shares a root with "dostoinstvo", dignity. "Mestakh" is "mesta", places, with the plural "in" ending -akh.'),
    (8, None, '\'Could someone really be leaving good restaurants?\' "Neuzheli" opens a question of disbelief, like "can it really be?". "Iz khoroshikh restoranov" is "from good restaurants".'),
    (9, None, '\'Maybe even from your restaurant.\' Word for word, "may be, even out of your restaurant". Elena stays on polite "vy", so "your" is "vash", and after "iz" it takes the "of" ending: "vashego restorana".'),
    (10, None, '\'I will eat my chef\'s hat if my cooks leave!\' "S\'\'yem", I will eat, is the irregular future of "s\'\'yest\'". "Kolpak" is the tall chef\'s hat, and "uydut" is "they will leave".'),
    (11, None, '\'Then in advance I wish you bon appétit!\' "Zaraneye" is "in advance". "Priyatnogo appetita" is in the "of" form because a wish usually takes it after "zhelayu", I wish.'),
    (12, None, '\'My people are loyal to me to the end.\' "Predany", devoted, and "predat\'", to betray, both come from "hand over": you hand yourself to someone, or hand them to the enemy. "Do kontsa" is "to the end", from "konets".'),
]
