# Authoring module for bayt-al-yasmin-s01e05-scene-06.
ID = 'bayt-al-yasmin-s01e05-scene-06'
SHOW = 'bayt-al-yasmin'
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = 'عشر دقايق لاطنعش  (Ten Minutes to Twelve)'
LEVEL = 'A1 — beginner'
PAIR = 'ar-en'
LABELS = {"mazen": "مازن", "nour": "نور", "salma": "سلمى"}
INTRO = 'Inside at the front desk at eleven fifty, Mazen straightens his clean blue tie while Nour and Salma check the clock—just as the postman leaves a thick white envelope on the counter. Listen first.'
OPENER = "Let's look closely at the five minutes before noon, line by line."
TRANSITION = "Let's hear the scene at the front desk again from start to finish."
OUTRO = "That thick envelope with the red property stamp sits unopened on the desk as the downtown clock tower begins to strike twelve! Let's step out to the gate next time. See you next time."
CLOSING = ('salma', 'مع السلامة!')
STORY = [
    ('mazen', 'كيف شكل كرافتي اليوم يا نور؟ ولا نقطة عصير برتقال!', 'How does my tie look today, Nour? Not a single drop of orange juice!'),
    ('nour', 'مرتبة ونظيفة يا أستاذ مازن! وحتى نظارتك على أنفك مش على جبينك.', 'Neat and clean, Mr Mazen! And even your glasses are on your nose, not on your forehead.'),
    ('mazen', 'تطور ممتاز! اليوم ساحتنا بتجمع عيلة، بدنا هدوء ووقار من الكل!', 'Excellent progress! Today our courtyard reunites a family, we want calm and dignity from everyone!'),
    ('salma', 'بيحكي هيك وهو بيطل من ورا الستارة كل نص دقيقة!', 'Says the man peeking from behind the curtain every half minute!'),
    ('mazen', 'أنا بتفقد الطقس يا سلمى! مين ترك هاد المغلف السميك جنب الجرس؟', 'I am checking the weather, Salma! Who left this thick envelope beside the bell?'),
    ('nour', 'ساعي البريد طلب توقيعي هلا. عليه ختم أحمر من دائرة العقارات.', 'The postman just asked for my signature. It has a red stamp from the property office.'),
    ('mazen', 'من محامي صاحب البناية؟ غريب، إيجارنا مدفوع للصيف الجاي.', "From the building owner's lawyer? Strange, our rent is paid until next summer."),
    ('salma', 'افتحه بعد الاطنعش يا معلم! طلع عالساعة: اطنعش إلا خمسة!', 'Open it after twelve, boss! Look at the clock: five to twelve!'),
    ('mazen', 'معك حق. الأوراق بتستنى، حطيه جنب الدفتر هلا.', 'You are right. Paperwork can wait, put it beside the ledger for now.'),
    ('nour', 'حطيت الشنتة الزرقا جنب طاولة رامي تحت الشجرة.', "I placed the blue suitcase beside Rami's table under the tree."),
    ('salma', 'وإبريق الشاي سخن! ابعدوا كلكم عن الشباك!', 'And the teapot is hot! Step back from the window, everyone!'),
    ('mazen', 'اسمعوا... برج الساعة بوسط البلد بلش يدق اطنعش!', 'Listen... the downtown clock tower is starting to chime twelve!'),
]
WALK = [
    (0, None, ["'How does my tie look today, Nour? Not a single drop of orange juice!' Literally 'how is the shape of', start with ", (None, 'كيف شكل'), ", 'how is the look of?'."]),
    (1, None, ["'Neat and clean, Mr Mazen! And even your glasses are on your nose, not on your forehead.' Describing someone well-dressed or tidy uses ", (None, 'مرتبة'), ", 'neat and smart'."]),
    (6, None, ["'From the building owner's lawyer? Strange, our rent is paid until next summer.' Rent is ", (None, 'إيجارنا'), ", 'our rent', paired with ", (None, 'مدفوع'), " for 'paid'."]),
    (7, None, ["'Open it after twelve, boss! Look at the clock: five to twelve!' Telling time before the hour uses ", (None, 'إلا'), ", 'except', so ", (None, 'اطنعش إلا خمسة'), ' is five minutes to twelve.']),
    (8, None, ["'You are right. Paperwork can wait, put it beside the ledger for now.' Literally 'papers wait', ", (None, 'الأوراق بتستنى'), ' brushes off office chores smoothly.']),
    (9, None, ["'I placed the blue suitcase beside Rami's table under the tree.' In Arabic, notice ", (None, 'تحت الشجرة'), " for 'under the tree', with the sun-letter sh assimilating 'the'."]),
    (10, None, ["'And the teapot is hot! Step back from the window, everyone!' Plural command ", (None, 'ابعدوا كلكم'), ' shoos everyone back from the glass.']),
    (11, None, ["'Listen... the downtown clock tower is starting to chime twelve!' Built from the words for tower and clock, downtown's landmark ", (None, 'برج الساعة'), ", 'the clock tower', rings out across downtown at noon."]),
]
