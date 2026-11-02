# Authoring module for alrawabi-school-s01e01-scene-04.
ID = 'alrawabi-school-s01e01-scene-04'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = "واحدة ورا الثانية  (One After Another)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"mariam": "مريم", "dina": "دينا", "noaf": "نوف"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "Out in the hallway after being blamed in Ms. Faten's office, Mariam meets up with Dina and newcomer Noaf. Tired of staying quiet while Layan's clique bullies others, the three girls decide they have reached their limit. Let's hear the whole conversation in Jordanian Arabic first."
OPENER = "Now let's break down the scene line by line."
TRANSITION = "Let's hear the full hallway conversation one more time."
OUTRO = "That hallway pact marks the start of Mariam, Dina, and Noaf pushing back together. Keep an ear out for \"رح\" before future plans and \"بعد هيك\" for \"after this\". See you next time."
CLOSING = ("noaf", "نشوفك!")
STORY = [
    ('dina', 'مريم، ليش زعلانة هيك اليوم؟', 'Mariam, why are you upset like this today?', [], 'opening check-in from Dina'),
    ('mariam', 'ليان وصحباتها كذبوا علي قدام المديرة.', 'Layan and her friends lied about me in front of the principal.', [], 'recaps previous scene'),
    ('noaf', 'هدول البنات دايماً بعملوا مشاكل.', 'Those girls always make trouble.', [], 'Noaf weighs in'),
    ('mariam', 'الواحد بيقدر يضل يتحمل أشياء كتير.', 'A person can keep putting up with many things.', [(33, 'الواحد بيقدر يضل يتحمل')], 'lightly completed cue 33'),
    ('noaf', 'صح، ويكبت بقلبه لمرحلة معينة.', 'Right, and hold it in his heart up to a certain point.', [(35, 'بمرحلة معينة')], 'restored ويكبت from cue 34/376'),
    ('dina', 'طيب، شو بدك تعملي هلأ يا مريم؟', 'Alright, what do you want to do now, Mariam?', [], 'Dina asks about next step'),
    ('mariam', 'رح أخلص من ظلمهم بالمدرسة.', 'I am going to put an end to their unfairness at school.', [(31, 'رح اخلص')], 'clean A1 phrasing'),
    ('mariam', 'رح نحاسبهم واحدة ورا الثانية.', 'We will hold them accountable one after another.', [(32, 'واحدة'), (32, 'الثانية')], 'colloquial ورا'),
    ('dina', 'بس الخطة صعبة شوي علينا.', 'But the plan is a little hard for us.', [], 'Dina hesitates'),
    ('noaf', 'لا، لازم نربيهم على غلطهم.', 'No, we must teach them a lesson for their mistake.', [(36, 'نربيهم')], 'natural Jordanian sense of نربيهم'),
    ('mariam', 'أكيد، ما رح يأذوا حدا بعد هيك.', 'Definitely, they will not hurt anyone after this.', [(37, 'انهم ما رح يأذوا حدا بعد هيك')], 'direct main clause'),
    ('dina', 'خلص، أنا معكم بكل خطوة.', 'Deal, I am with you in every step.', [], 'warm solidarity close'),
]
WALK = [
    (0, None, ["'Mariam, why are you upset like this today?' ", ('dina', 'زعلانة'), ' means "upset" or "hurt"—a warm, everyday feeling word far softer than furious anger.']),
    (1, None, ["'Layan and her friends lied about me in front of the principal.' ", ('mariam', 'قدام'), ' means "in front of", and ', ('mariam', 'المديرة'), ' is "the female principal" or director.']),
    (2, None, ["'Those girls always make trouble.' ", ('noaf', 'مشاكل'), ' is the everyday word for "problems" or "trouble", built from مشكلة, a single problem.']),
    (3, None, ["'A person can keep putting up with many things.' Jordanians use ", ('mariam', 'الواحد'), ', literally "the one", the same way English speakers say "a person" or "you" in general.']),
    (4, None, ["'Right, and hold it in his heart up to a certain point.' ", ('noaf', 'يكبت'), ' means bottling feelings up inside, and ', ('noaf', 'بقلبه'), ' literally adds "in his heart".']),
    (5, None, ["'Alright, what do you want to do now, Mariam?' ", ('dina', 'طيب'), ' literally means "good", and in conversation it works just like "alright" or "okay then".']),
    (6, None, ["'I am going to put an end to their unfairness at school.' Putting the little word ", ('mariam', 'رح'), ' in front of ', ('mariam', 'أخلص'), ' is the cleanest spoken way to talk about the future, like "going to".']),
    (7, None, ["'We will hold them accountable one after another.' ", ('mariam', 'ورا'), ' means "behind" or "after", so ', ('mariam', 'واحدة ورا الثانية'), ' paints them lining up one behind the next.']),
    (8, None, ["'But the plan is a little hard for us.' ", ('dina', 'شوي'), ' is a tiny gem in Levantine Arabic meaning "a little bit"—useful for softening complaints or polite requests.']),
    (9, None, ["'No, we must teach them a lesson for their mistake.' ", ('noaf', 'نربيهم'), ' comes from bringing up children with manners, so between teenagers it means teaching bullies a proper lesson.']),
    (10, None, ["'Definitely, they will not hurt anyone after this.' Notice ", ('mariam', 'ما رح'), ' for "will not", and ', ('mariam', 'بعد هيك'), ', literally "after like this", for "after this".']),
    (11, None, ["'Deal, I am with you in every step.' When someone opens with ", ('dina', 'خلص'), ', literally "finished", it means "settled" or "deal"—decision made.']),
]
