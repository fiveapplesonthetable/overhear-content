# Authoring module for kukhnya-s01e03-scene-03.
ID = 'kukhnya-s01e03-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = 'Поиски киллера  (Looking for a Hitman)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'Out in the backyard, Max and Kostya, the bartender, are staring at the goose. Neither of them can bring themselves to kill it, and a few silly ideas fail. Desperate, Max goes to Ainura and asks for help. Here is the conversation in Russian first.'
OPENER = "Let's go through the dilemma."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'A thousand rubles, no questions asked: Ainura has a way of solving problems. You\'ve heard "ya ne mogu", "I can\'t", and "dogovorilis\'", "agreed".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Я не могу убить этого гуся.', 'I cannot kill this goose.', [(116, 'Не могу я')], ''),
    ('kostya', 'Может, ты попробуешь ещё раз?', 'Maybe you will try once more?', [(116, 'Может, ты')], ''),
    ('max', 'Нет, я точно не смогу это сделать.', 'No, I definitely cannot do this.', [(116, 'Нет, я точно не смогу')], ''),
    ('kostya', 'Давай резко напугаем его в темноте!', 'Let us suddenly scare him in the dark!', [(122, 'Давай напугаем его')], ''),
    ('max', 'Костя, это какой-то полный бред.', 'Kostya, this is complete nonsense.', [(117, 'ну это какой-то бред')], ''),
    ('kostya', 'У птиц очень слабое сердце.', 'Birds have a very weak heart.', [(121, 'слабая сердечно-сосудистая система')], ''),
    ('max', 'Видишь, он стоит и громко шипит.', 'See, he is standing and hissing loudly.', [], ''),
    ('max', 'Мне срочно нужен настоящий специалист.', 'I urgently need a real specialist.', [(127, 'Мне нужен киллер, профессионал')], ''),
    ('max', 'Айнура, помоги нам решить проблему!', 'Ainura, help us solve the problem!', [(129, 'помоги гуся убить')], ''),
    ('ainura', 'Что нужно сделать с этой птицей?', 'What needs to be done with this bird?', [], ''),
    ('max', 'Нужно быстро и аккуратно убрать гуся.', 'The goose needs to be removed quickly and neatly.', [], ''),
    ('ainura', 'Тысяча рублей, и вы его никогда не увидите.', 'A thousand rubles, and you will never see him.', [(130, 'Тысяча рублей'), (131, 'никогда')], ''),
    ('max', 'Договорились, вот твои деньги!', 'Deal, here is your money!', [], ''),
]
WALK = [
    (0, None, '\'I cannot kill this goose.\' "Ya ne mogu" is "I not can". "Etogo gusya" puts -ogo on "this" and -ya on "goose", the object shape for a living creature.'),
    (1, None, '\'Maybe you will try once more?\' "Mozhet" is a clipped "maybe", and "yeshchyo raz" is "once more". "Poprobuyesh\'", you\'ll try, is the "ty" form of Max\'s "poprobuyu".'),
    (2, None, '\'No, I definitely cannot do this.\' "Smogu" is the finished partner of "mogu": "I\'ll manage", one time, as opposed to being able in general. "Tochno" is "definitely".'),
    (3, None, '\'Let us suddenly scare him in the dark!\' "Davay" plus a "we" verb, here "napugayem", gives "let\'s". "Rezko" is "sharply", and "v temnote" is "in the darkness".'),
    (4, None, '\'Kostya, this is complete nonsense.\' "Kakoy-to" is "some kind of": the -to makes "kakoy" vague. "Polnyy bred" is "full nonsense", and "bred" also means a fever\'s raving.'),
    (5, None, '\'Birds have a very weak heart.\' "U ptits" is "at birds", the usual way to say "have". The "d" in "serdtse", heart, is silent, so it sounds like "sertse". "Slaboye" is "weak".'),
    (6, None, '\'See, he is standing and hissing loudly.\' "Vidish\'" is "you see". "Shipit", hisses, sounds like what it means, and Russian says the goose "stoit", stands.'),
    (7, None, '\'I urgently need a real specialist.\' "Mne nuzhen" is "to me needed", masculine to match "spetsialist". "Srochno" is "urgently", and "nastoyashchiy" is "real".'),
    (8, None, '\'Ainura, help us solve the problem!\' "Pomogi nam", help us, puts "we" in its "to" shape, because Russians help "to" someone. "Reshit\'" means both "decide" and "solve".'),
    (9, None, '\'What needs to be done with this bird?\' "Chto nuzhno sdelat\'" is "what is needed to do". "Ptitsa", bird, becomes "s etoy ptitsey", with -ey after "s", with.'),
    (10, None, '\'The goose needs to be removed quickly and neatly.\' "Ubrat\'" means to take away and also to tidy up, so it makes a gentle way to say "get rid of". "Akkuratno" is "neatly".'),
    (11, None, '\'A thousand rubles, and you will never see him.\' After "tysyacha", thousand, comes "rubley", the "of" plural of "rubl\'". "Nikogda ne uvidite" is "never not will see".'),
    (12, None, '\'Deal, here is your money!\' "Dogovorilis\'", we\'ve agreed, is the word that seals a deal. "Den\'gi", money, is always plural, so "your" is "tvoi".'),
]
