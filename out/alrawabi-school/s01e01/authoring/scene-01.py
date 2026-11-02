# Authoring module for alrawabi-school-s01e01-scene-01.
ID = 'alrawabi-school-s01e01-scene-01'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = "ليلة الفيلم والمدرسة  (Movie Night and School)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"dina": "دينا", "mariam": "مريم"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "At AlRawabi School for Girls in Amman, loyal best friends Dina and Mariam catch up in the sunny courtyard before class. Dina apologizes for missing movie night because of homework, and Mariam reflects on how much she loves her school life. First, listen to the whole conversation in Jordanian Arabic without worrying about catching every word."
OPENER = "Now let's walk through the scene line by line."
TRANSITION = "Now let's hear the whole conversation again from beginning to end."
OUTRO = "That warm morning chat shows Mariam's peaceful school life just before everything changes. Listen out for \"kteer\" and \"heik\", two everyday Jordanian words you will hear in almost every scene. See you next time."
CLOSING = ("dina", "أشوفك بكرة!")
STORY = [
    ('dina', 'آسفة ما إجيت عالفيلم مبارح.', 'Sorry I did not come to the movie yesterday.', [(1, 'ما إجت على الفيلم البارح')], 'natural Jordanian 1st-person form'),
    ('dina', 'كنت بعمل وظيفة وما كان عندي وقت.', 'I was doing homework and did not have time.', [(2, 'كنت بعمل')], 'replaced misheard English loanword with natural Arabic وظيفة'),
    ('mariam', 'طبعاً، كالعادة يا دينا.', 'Of course, as usual, Dina.', [(3, 'كل عادة')], 'standard spelling كالعادة'),
    ('dina', 'شو، كيف كان الفيلم؟', 'So, how was the movie?', [(4, 'شو؟ كيف')], 'natural Jordanian question'),
    ('dina', 'راح علي إشي حلو؟', 'Did I miss anything good?', [], 'natural reconstruction of conversational follow-up'),
    ('mariam', 'الفيلم كان كتير حلو.', 'The movie was really good.', [], 'clean natural reply'),
    ('dina', 'يلا، المرة الجاي باجي معك.', 'Alright, next time I will come with you.', [], 'bridging line'),
    ('mariam', 'المدرسة مكاني المفضل.', 'School is my favorite place.', [(6, 'المدرسة كانت مكاني المفضل')], 'present-tense adaptation for A1'),
    ('mariam', 'والكل بعرف هاد الإشي عني.', 'And everyone knows this thing about me.', [(7, 'والكل بعرفها')], 'natural Jordanian phrasing'),
    ('mariam', 'عندي صحبات كتير هون.', 'I have lots of friends here.', [(8, 'عندي صحبات كتير')], 'present-tense adaptation'),
    ('dina', 'وإحنا بنحب نقعد مع بعض كل يوم.', 'And we love sitting together every day.', [], 'warm friendship turn'),
    ('mariam', 'الحياة حلوة كتير هون.', 'Life is very sweet here.', [(9, 'الحياة حلوة')], 'present-tense adaptation'),
]
WALK = [
    (0, None, "'Sorry I did not come to the movie yesterday.' Dina says \"aasfe\", the female form of \"sorry\", and \"mbaareh\" is how Jordanians say \"yesterday\" in everyday speech."),
    (1, None, "'I was doing homework and did not have time.' Instead of an action word for \"have\", Arabic says \"at me\" with \"indi\", so \"ma kaan indi waqt\" is literally \"there was not at me time\"."),
    (2, None, "'Of course, as usual, Dina.' Mariam teases her gently. That little word \"ya\" right before Dina's name is how Arabic calls out directly to the person you are talking to."),
    (3, None, "'So, how was the movie?' Jordanian conversations constantly open with \"shu\", a tiny all-purpose word for \"what\" or \"so\"."),
    (4, None, "'Did I miss anything good?' Word for word, \"raah alayy\" says \"it went past on me\", a handy everyday chunk whenever you miss an event. And \"ishi\" is pure Amman speech for \"anything\" or \"something\"."),
    (5, None, "'The movie was really good.' Notice \"kteer\", which means \"very\" or \"a lot\", and \"hilu\", which literally means \"sweet\" and doubles as \"nice\" or \"good\"."),
    (6, None, "'Alright, next time I will come with you.' You will hear \"yalla\" everywhere in Jordan to mean \"come on\" or \"alright\". The \"b-\" sound at the start of \"baaji\" marks everyday habits and near plans."),
    (7, None, "'School is my favorite place.' Arabic drops the word \"is\" in simple statements like this, putting \"the school\" right next to \"my favorite place\"."),
    (8, None, "'And everyone knows this thing about me.' Here \"il-kull\" means \"everyone\", literally \"the all\", and \"haad\" is the casual Jordanian word for \"this\"."),
    (9, None, "'I have lots of friends here.' \"Sahbaat\" means female friends, built from the root for companionship, and \"hon\" is the everyday Levantine word for \"here\"."),
    (10, None, "'And we love sitting together every day.' \"Maa baad\" means \"together\" or \"with each other\", a reusable pair of words you can drop into almost any plans with friends."),
    (11, None, "'Life is very sweet here.' Notice how \"hilwe\" adds a soft \"-e\" ending to \"hilu\" to match \"il-hayaah\", \"life\"."),
]
