# Authoring module for bayt-al-yasmin-s01e01-scene-04.
ID = 'bayt-al-yasmin-s01e01-scene-04'
SHOW = 'bayt-al-yasmin'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'غرفة أربعة بالطابق التاني  (Room Four on the Second Floor)'
LEVEL = 'A1 — beginner'
PAIR = 'ar-en'
LABELS = {"nour": "نور", "suad": "سعاد", "tariq": "طارق"}
INTRO = "At the front desk, retired music teacher Suad steps inside from her taxi pulling a large dark-blue suitcase. Nour greets her first real guest while Tariq stands ready to help with the bag. Let's hear how it goes."
OPENER = "Let's break down the conversation line by line."
TRANSITION = "Let's listen to the entire check-in scene one more time."
OUTRO = 'Nour handled her first check-in smoothly, though Tariq noticed that blue suitcase felt strangely heavy after her intercity bus ride. See you next time to find out why.'
CLOSING = ('suad', 'مع السلامة!')
STORY = [
    ('nour', 'أهلا وسهلا! صباح الخير مدام.', 'Welcome! Good morning, madam.'),
    ('suad', 'صباح النور يا حبيبتي. عندي حجز باسم سعاد.', 'Good morning, my dear. I have a booking for Suad.'),
    ('nour', 'نعم، غرفة أربعة بالطابق التاني! كيف كانت رحلة الباص؟', 'Yes, room four on the second floor! How was the bus trip?'),
    ('suad', 'هادية ومريحة، شكرا، بس هادي الشنتة تقيلة كتير اليوم.', 'Quiet and comfortable, thank you, though this suitcase is very heavy today.'),
    ('tariq', 'عن إذنك. يا لطيف، حاطة حجار جوا؟', 'Allow me. Goodness, did you pack stones inside?'),
    ('suad', 'بس فساتين، ودفتر موسيقى، وفنجاني المفضل!', 'Only dresses, a music book, and my favourite cup!'),
    ('nour', 'تفضلي مفتاحك، رقم أربعة. الفطور من السبعة ونص للعشرة.', 'Here is your key, number four. Breakfast is from seven thirty to ten.'),
    ('suad', 'ممتاز. الشباك عالشارع ولا عالساحة؟', 'Wonderful. Is the window on the street or on the courtyard?'),
    ('nour', 'عالساحة، فوق الشجرة القديمة. المكان هادي كتير.', 'On the courtyard, above the old tree. The place is very quiet.'),
    ('suad', 'هاد اللي بدي إياه. وين الدرج؟', 'Just what I want. Where are the stairs?'),
    ('tariq', 'من هاد القوس. رح أطلع الشنتة الزرقا عنك.', 'Through this archway. I will carry the blue bag up for you.'),
    ('suad', 'شكرا كتير إلكم.', 'Thank you both very much.'),
]
WALK = [
    (0, None, ["'Welcome! Good morning, madam.' The classic Arabic hospitality greeting ", (None, 'أهلا وسهلا'), ' wishes a guest friendly family and smooth ground underfoot.']),
    (1, None, ["'Good morning, my dear. I have a booking for Suad.' Arabic has no separate word for 'have', so ", (None, 'عندي حجز'), " literally says 'at me is a booking'."]),
    (2, None, ["'Yes, room four on the second floor! How was the bus trip?' Asking how something went uses ", (None, 'كيف كانت'), ", 'how was she', matching the feminine word for trip."]),
    (3, None, ["'Quiet and comfortable, thank you, though this suitcase is very heavy today.' Place ", (None, 'كتير'), ' after a describing word like ', (None, 'تقيلة كتير'), " to mean 'very heavy'."]),
    (4, None, ["'Allow me. Goodness, did you pack stones inside?' In Arabic, before lifting a bag or stepping past someone, ", (None, 'عن إذنك'), " politely asks 'by your permission'."]),
    (6, None, ["'Here is your key, number four. Breakfast is from seven thirty to ten.' Handing anything to a woman comes with ", (None, 'تفضلي'), ", the warm all-purpose 'please, go ahead'."]),
    (7, None, ["'Wonderful. Is the window on the street or on the courtyard?' In an either-or question, ", (None, 'ولا'), " means 'or', shortened from 'or not'."]),
    (11, None, ["'Thank you both very much.' Adding ", (None, 'إلكم'), " turns a simple thank-you into 'to you all', thanking Nour and Tariq together."]),
]
