# Authoring module for bayt-al-yasmin-s01e01-scene-06.
ID = 'bayt-al-yasmin-s01e01-scene-06'
SHOW = 'bayt-al-yasmin'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'بطاقة الشنتة  (The Luggage Tag)'
LEVEL = 'A1 — beginner'
PAIR = 'ar-en'
LABELS = {"mazen": "مازن", "nour": "نور", "suad": "سعاد"}
INTRO = 'Back at the front desk, Nour, Suad, and owner Mazen lean over the blue suitcase under the desk lamp. Mazen finally puts his glasses to good use. Listen to the scene first.'
OPENER = "Let's go back through the scene one line at a time."
TRANSITION = "Let's hear the full conversation at the front desk again."
OUTRO = "No luck at the bus station yet, and the mysterious suitcase owner lives just five minutes away. Next time, Salma steps in to rescue Suad's evening."
CLOSING = ('mazen', 'مع السلامة!')
STORY = [
    ('mazen', 'يا ساتر، شو هاللخبطة! خليني أشوف البطاقة بنظارتي.', 'Goodness, what a mix-up! Let me look at the tag with my glasses.'),
    ('suad', 'مكتوب عليها اسم أو رقم تليفون؟', 'Is a name or a phone number written on it?'),
    ('mazen', 'للاسف ما في رقم تليفون. بس حرفين واسم شارع قديم.', 'Unfortunately there is no phone number. Only two letters and an old street name.'),
    ('nour', 'لحظة، هاد الشارع هون بحارتنا، خمس دقايق مشي!', 'Wait a moment, that street is right here in our neighbourhood, five minutes walking!'),
    ('suad', 'غريب كتير! ركبنا نفس باص الصبح لنفس المنطقة.', 'How strange! We rode the same morning bus to the same district.'),
    ('mazen', 'يا نور، اتصلي بمكتب المفقودات بالمحطة فورا.', 'Nour, call the lost-and-found office at the station right away.'),
    ('nour', 'عم برن هلا... ألو؟ في حدا بلغ عن شنتة زرقا تبدلت؟', 'I am dialling now... Hello? Did anyone report a swapped blue suitcase?'),
    ('suad', 'احكيلهم شنتتي فيها شريطة حمرا بالجيبة الفوقانية!', 'Tell them my bag has a red ribbon in the top pocket!'),
    ('nour', 'لسا؟ خد رقم النزل وعنواننا لو سمحت. شكرا!', 'Not yet? Take the guesthouse number and our address, please. Thank you!'),
    ('mazen', 'ما عندهم خبر لسا يا مدام، أنا آسف كتير.', 'They have no news yet, madam, I am very sorry.'),
    ('suad', 'مش غلطتكم. بس ما معي غير المعطف اللي علي!', 'It is not your fault. Still, I have nothing except the coat on me!'),
    ('nour', 'استنوا شوي، سلمى بالكافيه أشرتلي وعندها فكرة!', 'Wait a bit, Salma in the café waved to me and has an idea!'),
]
WALK = [
    (0, None, ["'Goodness, what a mix-up! Let me look at the tag with my glasses.' Starting a suggestion with ", (None, 'خليني'), " means 'let me', followed straight by the action."]),
    (2, None, ["'Unfortunately there is no phone number. Only two letters and an old street name.' Soften bad news politely with ", (None, 'للاسف'), ", 'unfortunately'."]),
    (3, None, ["'Wait a moment, that street is right here in our neighbourhood, five minutes walking!' Amman residents call their local neighbourhood ", (None, 'حارتنا'), ", 'our quarter'."]),
    (6, None, ["'I am dialling now... Hello? Did anyone report a swapped blue suitcase?' In Arabic, putting ", (None, 'عم'), ' before ', (None, 'برن'), " marks an action happening right this second, 'I am ringing'."]),
    (8, None, ["'Not yet? Take the guesthouse number and our address, please. Thank you!' Alone as a question, ", (None, 'لسا'), " means 'not yet?', while ", (None, 'لو سمحت'), " politely says 'please' to a man."]),
    (9, None, ["'They have no news yet, madam, I am very sorry.' Because Mazen is a man, he says ", (None, 'آسف'), ' without the feminine ending.']),
    (10, None, ["'It is not your fault. Still, I have nothing except the coat on me!' Combining 'not with me except' in ", (None, 'ما معي غير'), " is how Jordanian speakers naturally say 'I only have on me'."]),
    (11, None, ["'Wait a bit, Salma in the café waved to me and has an idea!' Ask a whole group to hold on a moment with ", (None, 'استنوا شوي'), ", 'wait a little'."]),
]
