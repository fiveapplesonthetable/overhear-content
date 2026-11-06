# Authoring module for bayt-al-yasmin-s01e05-scene-01.
ID = 'bayt-al-yasmin-s01e05-scene-01'
SHOW = 'bayt-al-yasmin'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'الحقيقة بالساحة  (Truth in the Courtyard)'
LEVEL = 'A1 — beginner'
PAIR = 'ar-en'
LABELS = {"nour": "نور", "rami": "رامي", "suad": "سعاد"}
INTRO = "Still standing under the courtyard tree at the Jasmine Courtyard House in Amman, Rami sits down with Nour and Suad to explain Monday night's mystery from the very beginning. Listen first."
OPENER = "Now let's walk through Rami's explanation, line by line."
TRANSITION = "Let's hear the whole courtyard confession again."
OUTRO = 'All the puzzle pieces from Monday and Tuesday finally click together! Next time, Rami explains why he has not spoken to his brother Ziad in three years. See you next time.'
CLOSING = ('nour', 'مع السلامة!')
STORY = [
    ('suad', 'خليني أطلع فيك منيح يا رامي! صرت أطول من البيانو!', 'Let me look at you properly, Rami! You grew taller than the piano!'),
    ('rami', 'مش مصدق إنك نازلة بنفس النزل يا مدام سعاد.', 'I cannot believe you are staying at the very same guesthouse, Madam Suad.'),
    ('nour', 'لحظة، يعني ركبتوا نفس الباص يوم التنين، وأخدت شنتتها؟', 'Wait, so you rode the same bus on Monday, and you took her suitcase?'),
    ('rami', 'بالغلط والله! ببيت ابن عمي فتحتها وشفت دفتر موسيقى وشريطة حمرا.', "By mistake, honestly! At my cousin's house I opened it and saw a music book and a red ribbon."),
    ('suad', 'طيب ليش تركت شنتتي عالعتبة بالليل وهربت؟', 'Then why did you leave my bag on the step at night and run away?'),
    ('rami', 'لأني لما مشيت لهون ليلة التنين، شفت أخوي الكبير ماشي بهاد الشارع!', 'Because when I walked here Monday night, I saw my older brother walking on this street!'),
    ('nour', 'أخوك الكبير ساكن هون بعمان؟', 'Your older brother lives here in Amman?'),
    ('rami', 'آه. ارتبكت، رنيت جرسكم، وحطيت ورقة يوم الجمعة عاليد.', 'Yes. I panicked, rang your bell, and put the Friday note on the handle.'),
    ('suad', 'وليلة الأربعا حجزت هون باسمك الحقيقي؟', 'And on Wednesday night you booked in here under your real name?'),
    ('rami', 'كنت محتاج مكان هادي قريب قبل الجمعة، ونسيت إنه شنتتي لسا عندكم!', 'I needed a quiet place nearby before Friday, and forgot that my bag was still with you!'),
    ('nour', 'لحد ما اتصلت فينا يوم التلاتا وطلبت ما نفتح اللفة البيضا!', 'Until you called us on Tuesday and asked us not to open the white parcel!'),
    ('rami', 'كل شي جوا الورق الأبيض لأخوي زياد، مش إلي.', 'Everything inside the white paper belongs to my brother Ziad, not to me.'),
]
WALK = [
    (0, None, ["'Let me look at you properly, Rami! You grew taller than the piano!' In Arabic, comparing height uses ", (None, 'أطول من'), ", 'taller than'."]),
    (1, None, ["'I cannot believe you are staying at the very same guesthouse, Madam Suad.' Expressing amazement uses ", (None, 'مش مصدق'), ", 'I cannot believe!', while ", (None, 'نازلة'), " means 'staying as a guest'."]),
    (3, None, ["'By mistake, honestly! At my cousin's house I opened it and saw a music book and a red ribbon.' Arabic distinguishes family sides precisely, so ", (None, 'ابن عمي'), " means 'my father's brother's son'."]),
    (5, None, ["'Because when I walked here Monday night, I saw my older brother walking on this street!' Adding 'I' onto 'because' creates ", (None, 'لأني'), ", 'because I'."]),
    (6, None, ["'Your older brother lives here in Amman?' Describing where someone lives uses active ", (None, 'ساكن'), ", 'residing' or 'living'."]),
    (9, None, ["'I needed a quiet place nearby before Friday, and forgot that my bag was still with you!' This warm phrase, past 'I was' with 'needing' in ", (None, 'كنت محتاج'), " says 'I needed' naturally."]),
    (10, None, ["'Until you called us on Tuesday and asked us not to open the white parcel!' This handy chunk for 'until' is ", (None, 'لحد ما'), ", 'until'."]),
    (11, None, ["'Everything inside the white paper belongs to my brother Ziad, not to me.' In Arabic, contrast ", (None, 'لأخوي'), ", 'for my brother', with ", (None, 'مش إلي'), ", 'not for me'."]),
]
