# Authoring module for alrawabi-school-s01e01-scene-03.
ID = 'alrawabi-school-s01e01-scene-03'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = "قيم المدرسة  (School Values)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"mariam": "مريم", "faten": "مس فاتن", "layan": "ليان"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "Still dealing with the fallout at AlRawabi School, Principal Ms. Faten lectures the students on honesty and responsibility and asks for witnesses. Layan steps forward with her friends to corner Mariam. Listen to the whole scene in Jordanian Arabic first."
OPENER = "Let's slow down and look at each line one by one."
TRANSITION = "Now let's listen to the whole exchange again from start to finish."
OUTRO = "Outnumbered by false witnesses, Mariam sees her favorite place turn against her. Notice how \"kamaan\" for \"also\" and \"hada\" for \"anyone\" pop up naturally throughout the conversation. See you next time."
CLOSING = ("faten", "إلى اللقاء!")
STORY = [
    ('mariam', 'المدرسة صارت كابوس إلي.', 'School became a nightmare for me.', [(20, 'المدرسة صارت')], 'clear Jordanian phrasing'),
    ('faten', 'أهم القيم عنا هون بمدرسة الروابي واضحة.', 'The most important values we have here at AlRawabi School are clear.', [(21, 'في مدرسة الروابي')], 'natural Jordanian عنا هون'),
    ('faten', 'لازم نتحمل المسؤولية ونحكي الصدق.', 'We must take responsibility and tell the truth.', [(22, 'والصدق')], 'active present phrasing for A1'),
    ('faten', 'بظن صار الوقت نحكي الحقيقة.', 'I think it is time we tell the truth.', [(23, 'صار الوقت'), (23, 'الحقيقة')], 'restored بظن and نحكي'),
    ('faten', 'أي حدا منكم شاف اللي صار؟', 'Did any one of you see what happened?', [(24, 'حدا منكم شاف اللي صار')], ''),
    ('layan', 'نعم يا مس، أنا شفت كل إشي.', 'Yes Miss, I saw everything.', [(25, 'أنا')], 'natural witness claim'),
    ('layan', 'وصحباتي كمان شافوا اللي صار.', 'And my friends also saw what happened.', [(26, 'كمان')], 'expanded cue 26'),
    ('mariam', 'لا يا مس، ليان ما بتحكي الحقيقة.', 'No Miss, Layan is not telling the truth.', [], 'Mariam pushes back'),
    ('faten', 'الغرفة مليانة بنات يا مريم.', 'The room is full of girls, Mariam.', [(28, 'مليانة بنات')], 'restored الغرفة from Whisper cue'),
    ('faten', 'وكلهم شهدوا على إشي واحد.', 'And all of them testified to one thing.', [(29, 'على اشي واحد')], 'restored شهدوا'),
    ('faten', 'وإنتي بدك أصدقك لحالك؟', 'And you want me to believe you alone?', [(30, 'وانتي')], 'restored natural Jordanian question'),
    ('mariam', 'أنا بحكي الصدق بس ما حدا سامعني.', 'I am telling the truth, only nobody hears me.', [], 'closing emotional turn'),
]
WALK = [
    (0, None, "'School became a nightmare for me.' \"Saarat\" means \"she became\", matching \"school\", and \"kaaboos\" is the Arabic word for a nightmare."),
    (1, None, "'The most important values we have here at AlRawabi School are clear.' \"Ahamm\" means \"most important\", and \"inna hon\" is smooth Jordanian speech for \"we have here\"."),
    (2, None, "'We must take responsibility and tell the truth.' \"Laazim\" is an unchangeable helper word meaning \"must\"—you never have to alter its shape no matter who speaks."),
    (3, None, "'I think it is time we tell the truth.' \"Bazzunn\" means \"I think\", and \"saar il-waqt\" literally says \"the time became\", which is how Arabic says \"it's time\"."),
    (4, None, "'Did any one of you see what happened?' Notice \"illi saar\" at the end: \"illi\" means \"that which\" or \"what\", so \"illi saar\" is \"what happened\"."),
    (5, None, "'Yes Miss, I saw everything.' Layan uses polite \"naam\" with the principal, and \"shuft\" comes from \"shaaf\", the everyday Levantine word for seeing."),
    (6, None, "'And my friends also saw what happened.' Drop \"kamaan\" into almost any sentence when you want to say \"also\", \"too\", or \"even more\"."),
    (7, None, "'No Miss, Layan is not telling the truth.' Putting \"ma\" right before \"btihki\" flips \"she speaks\" into \"she does not speak\"."),
    (8, None, "'The room is full of girls, Mariam.' \"Malyaane\" means \"full\", built from the root for filling something to the brim."),
    (9, None, "'And all of them testified to one thing.' \"Kulhom\" glues \"all\" and \"them\" into a single word, a pattern Arabic uses constantly."),
    (10, None, "'And you want me to believe you alone?' \"Biddik\" means \"you want\" when speaking to a woman, while \"lahaalik\" literally says \"by your own state\" for \"all alone\"."),
    (11, None, "'I am telling the truth, only nobody hears me.' Pairing \"ma\" with \"hada\" gives \"nobody\", and \"saamiani\" tacks \"me\" straight onto the end of \"hearing\"."),
]
