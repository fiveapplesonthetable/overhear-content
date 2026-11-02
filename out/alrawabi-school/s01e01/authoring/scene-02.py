# Authoring module for alrawabi-school-s01e01-scene-02.
ID = 'alrawabi-school-s01e01-scene-02'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = "مشكلة الباص  (Trouble on the Bus)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"layan": "ليان", "mariam": "مريم", "faten": "مس فاتن"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "Moments after that calm morning, popular student Layan blocks Mariam from riding the school bus, and soon Principal Ms. Faten calls Mariam into her office over a false report. Listen to the whole exchange in Jordanian Arabic first."
OPENER = "Let's go back through the scene and unpack each line."
TRANSITION = "Now listen to the whole scene again at natural speed."
OUTRO = "Layan twists the bus incident in her favor, leaving Mariam on the defensive with Ms. Faten. Keep an ear out for مش and عم, two tiny building blocks of spoken Jordanian Arabic. See you next time."
CLOSING = ("mariam", "مع السلامة!")
STORY = [
    ('layan', 'قلت للسائق هدول البنات مش معنا عالباص.', 'I told the driver these girls are not with us on the bus.', [(10, 'قلت له هذول بنات مش معانا')], 'clean Jordanian phrasing'),
    ('mariam', 'ليش بتحكي هيك يا ليان؟', 'Why are you talking like that, Layan?', [], 'bridging reaction'),
    ('layan', 'يلا، انزلي من الباص هلأ.', 'Come on, get off the bus right now.', [], 'natural command on the bus'),
    ('mariam', 'ليش دايماً بتحكموا فينا هيك؟', 'Why do you always boss us around like this?', [(11, 'بتحكموا فينا')], 'natural Jordanian adaptation'),
    ('mariam', 'عاملين حالهم عصابة بالمدرسة.', 'They act like a gang at school.', [(12, 'كلهم')], 'clean Jordanian idiom عاملين حالهم'),
    ('mariam', 'بس مش بعد اليوم.', 'But not after today.', [(13, 'بس مش بعد اليوم')], ''),
    ('faten', 'بعرف إنك هربتي من الباص اليوم.', 'I know that you skipped the bus today.', [(15, 'من الباص')], 'restored natural Jordanian هربتي'),
    ('mariam', 'لا يا مس فاتن، هاد الحكي مش صح.', 'No, Ms. Faten, this talk is not true.', [(14, 'لا')], 'expanded natural protest'),
    ('mariam', 'مين حكى إلك هاد الإشي؟', 'Who told you this thing?', [(16, 'مين حكي لك')], 'clear Jordanian spelling'),
    ('mariam', 'البنات عم بكذبوا عليكي.', 'The girls are lying to you.', [(16, 'عليكي')], 'restored بكذبوا from Whisper artifact'),
    ('faten', 'زميلتك بالصف حكت إلي كل إشي.', 'Your classmate told me everything.', [(17, 'عليكي')], 'natural Jordanian adaptation'),
    ('faten', 'وهاد الموضوع لفت انتباهي.', 'And this matter caught my attention.', [(18, 'لفتة انتباهي')], 'corrected to verbal phrase لفت انتباهي'),
]
WALK = [
    (0, None, ["'I told the driver these girls are not with us on the bus.' Layan uses ", ('layan', 'هدول'), ' for "these" when talking about people, and ', ('layan', 'عالباص'), ' fuses "on" and "the bus" into one smooth spoken word.']),
    (1, None, ["'Why are you talking like that, Layan?' In Jordanian Arabic, ", ('mariam', 'ليش'), ' means "why"—shortened from "for what thing"—and ', ('mariam', 'هيك'), ' means "like that".']),
    (2, None, ["'Come on, get off the bus right now.' Notice ", ('layan', 'هلأ'), ', the everyday Amman word for "now", squeezed down from the longer phrase "this hour".']),
    (3, None, ["'Why do you always boss us around like this?' ", ('mariam', 'دايماً'), ' means "always", and ', ('mariam', 'بتحكموا فينا'), ' literally says "you rule in us", a vivid way to say someone bosses you around.']),
    (4, None, ["'They act like a gang at school.' The handy expression ", ('mariam', 'عاملين حالهم'), ' literally means "making themselves", which is how Jordanians say people are acting like big shots.']),
    (5, None, ["'But not after today.' Short and punchy: ", ('mariam', 'بس'), ' means "but" or "only", and ', ('mariam', 'مش'), ' is the everyday spoken word for "not".']),
    (6, None, ["'I know that you skipped the bus today.' Ms. Faten says ", ('faten', 'هربتي'), ', built from the root for running away, which school staff use when a student skips class or the bus.']),
    (7, None, ["'No, Ms. Faten, this talk is not true.' Here ", ('mariam', 'الحكي'), ' means "the talk" or "what people are saying", and ', ('mariam', 'مش صح'), ' is the quickest way to say "not true".']),
    (8, None, ["'Who told you this thing?' ", ('mariam', 'مين'), ' asks "who" in Levantine Arabic, while ', ('mariam', 'حكى'), ' is the everyday word for "spoke" or "told".']),
    (9, None, ["'The girls are lying to you.' Putting the tiny word ", ('mariam', 'عم'), ' before ', ('mariam', 'بكذبوا'), ' works just like English "-ing", showing they are lying right now.']),
    (10, None, ["'Your classmate told me everything.' ", ('faten', 'زميلتك'), ' means "your female classmate", with ', ('faten', 'ك'), ' tacked onto the end to mean "your" when speaking to a girl.']),
    (11, None, ["'And this matter caught my attention.' Word for word, ", ('faten', 'لفت انتباهي'), ' says "it turned my attention", a polished phrase Ms. Faten uses in formal school moments.']),
]
