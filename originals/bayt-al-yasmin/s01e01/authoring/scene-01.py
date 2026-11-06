# Authoring module for bayt-al-yasmin-s01e01-scene-01.
ID = 'bayt-al-yasmin-s01e01-scene-01'
SHOW = 'bayt-al-yasmin'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'ارفع اليد  (Lift the Handle)'
LEVEL = 'A1 — beginner'
PAIR = 'ar-en'
LABELS = {"nour": "نور", "tariq": "طارق"}
INTRO = 'Nour arrives early for her very first morning at the Jasmine Courtyard House in Amman. Behind the front desk, veteran handyman Tariq is already pouring hot tea. Listen to the scene in Arabic first without worrying about catching every word.'
OPENER = "Now let's take it slowly, one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Nour is inside, the eight brass keys are on the board, and her first morning has begun. Don't worry if a few words went past quickly; they come back all week. See you next time."
CLOSING = ('nour', 'مع السلامة!')
STORY = [
    ('nour', 'صباح الخير! عفوا، الباب مسكر؟', 'Good morning! Excuse me, is the door locked?'),
    ('tariq', 'صباح النور. لا، ارفعي اليد أول، وبعدين ادفعي.', 'Good morning. No, lift the handle first, then push.'),
    ('nour', 'آه، فتح! شكرا. أنا نور، موظفة الاستقبال الجديدة.', 'Oh, it opened! Thank you. I am Nour, the new receptionist.'),
    ('tariq', 'أهلا، أنا طارق. إجيتي بكير عشر دقايق.', 'Welcome, I am Tariq. You arrived ten minutes early.'),
    ('nour', 'دايما بمشي بسرعة بأول يوم. وين الكمبيوتر؟', 'I always walk fast on my first day. Where is the computer?'),
    ('tariq', 'بالدرج. هون بنستعمل هاد الدفتر الكبير وقلم رصاص.', 'In the drawer. Here we use this big notebook and a pencil.'),
    ('nour', 'دفتر ورق؟ عن جد؟', 'A paper notebook? Really?'),
    ('tariq', 'الورق ما بيضيع أسماء الغرف وقت المطر.', 'Paper never loses the room names when it rains.'),
    ('nour', 'معك حق! وهدول المفاتيح؟', 'You have a point! And these are the keys?'),
    ('tariq', 'آه، تمن غرف وتمن مفاتيح نحاس. غرفة أربعة جاية اليوم.', 'Yes, eight rooms and eight brass keys. Room four is arriving today.'),
    ('nour', 'ممتاز. احكيلي كل شي لازم أعرفه.', 'Great. Tell me everything I need to know.'),
    ('tariq', 'أول قاعدة: اشربي شاي سخن أول، وبعدين ردي عالجرس.', 'Rule one: drink hot tea first, then answer the bell.'),
]
WALK = [
    (0, None, ["'Good morning! Excuse me, is the door locked?' She greets him with ", (None, 'صباح الخير'), ', wishing him a morning of goodness, and adds ', (None, 'عفوا'), ' to get his attention politely.']),
    (1, None, ["'Good morning. No, lift the handle first, then push.' Notice how Tariq answers a morning greeting with ", (None, 'صباح النور'), ', literally a morning of light.']),
    (2, None, ["'Oh, it opened! Thank you. I am Nour, the new receptionist.' Arabic drops the word for 'am' in the present, so ", (None, 'أنا نور'), " is simply 'I Nour'."]),
    (3, None, ["'Welcome, I am Tariq. You arrived ten minutes early.' The everyday Amman word ", (None, 'بكير'), ' means early, and you will hear it every morning across Amman.']),
    (4, None, ["'I always walk fast on my first day. Where is the computer?' Spoken Jordanian puts a soft b-sound at the start of everyday habits like ", (None, 'بمشي'), " for 'I walk'."]),
    (5, None, ["'In the drawer. Here we use this big notebook and a pencil.' Location comes first with ", (None, 'هون'), ", the everyday Jordanian word for 'here'."]),
    (6, None, ["'A paper notebook? Really?' When Jordanian speakers want to ask 'really?' or 'seriously?', they reach for the two-word chunk ", (None, 'عن جد'), '.']),
    (8, None, ["'You have a point! And these are the keys?' Literally, ", (None, 'معك حق'), " says 'truth is with you', a warm everyday way to agree with someone."]),
    (10, None, ["'Great. Tell me everything I need to know.' Instead of an infinitive like 'to know', Arabic links ", (None, 'لازم'), " directly to 'I know' in ", (None, 'لازم أعرفه'), '.']),
    (11, None, ["'Rule one: drink hot tea first, then answer the bell.' In Arabic, describing words follow the thing they describe, so hot tea is ", (None, 'شاي سخن'), ', tea hot.']),
]
