# Authoring module for bayt-al-yasmin-s01e04-scene-01.
ID = 'bayt-al-yasmin-s01e04-scene-01'
SHOW = 'bayt-al-yasmin'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'الستة وخمسة وأربعين  (Six Forty-Five)'
LEVEL = 'A1 — beginner'
PAIR = 'ar-en'
LABELS = {"nour": "نور", "tariq": "طارق"}
INTRO = 'It is six forty-five in the morning at the Jasmine Courtyard House in Amman. While the guests still sleep upstairs, Tariq sketches a quick street map on paper for Nour. Listen to the whole scene first.'
OPENER = "Let's trace Tariq's street directions in Amman, line by line."
TRANSITION = "Now let's hear all the dawn directions again without stopping."
OUTRO = 'Left at the gate, across the downtown overpass, past the green pharmacy, and left into the square—Nour is off on her dawn mission. See you next time.'
CLOSING = ('nour', 'مع السلامة!')
STORY = [
    ('nour', 'صباح الخير يا طارق! المي فوق صارت باردة عن جد؟', 'Good morning, Tariq! Did the water upstairs really turn cold already?'),
    ('tariq', 'باردة متل مية الشتا. حطي هاد الصمام المكسور بجيبة معطفك.', 'Cold as winter rain. Put this broken valve in your coat pocket.'),
    ('nour', 'تمام. هلا احكيلي كيف ألاقي دكان الخردوات.', 'Got it. Now tell me how to find the hardware shop.'),
    ('tariq', 'لفي شمال برا البوابة وامشي دغري للدرج الحجري والجسر.', 'Turn left outside the gate and walk straight to the stone stairs and the overpass.'),
    ('nour', 'شمال عند البوابة، ودغري للجسر. أعبر الجسر لوسط البلد؟', 'Left at the gate, and straight to the overpass. Do I cross the overpass into downtown?'),
    ('tariq', 'آه، اعبري الجسر، وبعدين مري من جنب الصيدلية الخضرا على يمينك.', 'Yes, cross the overpass, then pass beside the green pharmacy on your right.'),
    ('nour', 'الجسر، وبعدين الصيدلية الخضرا عاليمين. وبعد هيك؟', 'The overpass, then the green pharmacy on the right. And after that?'),
    ('tariq', 'لفي شمال عالساحة الصغيرة. دوري على باب خشب أزرق.', 'Turn left into the small square. Look for a blue wooden door.'),
    ('nour', 'الدكان عليه آرمة كبيرة برا؟', 'Does the shop have a big sign outside?'),
    ('tariq', 'بس مفتاح دهبي مرسوم فوق الباب. فرجي البياع هاد الصمام.', 'Only a golden key painted above the door. Show the clerk this valve.'),
    ('nour', 'عشرين مليمتر، نحاس، صمام سخان... رح أعيدها طول الطريق!', 'Twenty millimetres, brass, boiler valve... I will repeat it the whole way!'),
    ('tariq', 'اركضي بسرعة يا نور. غرفة أربعة بتصحى عالسبعة وربع!', 'Run fast, Nour. Room four wakes up at seven fifteen!'),
]
WALK = [
    (0, None, ["'Good morning, Tariq! Did the water upstairs really turn cold already?' Expressing 'became' or 'turned' is the job of ", (None, 'صارت'), ', here matching feminine water.']),
    (3, None, ["'Turn left outside the gate and walk straight to the stone stairs and the overpass.' Every street direction in Amman uses ", (None, 'دغري'), " for 'straight ahead'."]),
    (4, None, ["'Left at the gate, and straight to the overpass. Do I cross the overpass into downtown?' Residents call historic downtown Amman ", (None, 'وسط البلد'), ", literally 'the middle of town'."]),
    (6, None, ["'The overpass, then the green pharmacy on the right. And after that?' To keep directions moving, you can say ", (None, 'وبعد هيك؟'), ", 'and after that?'."]),
    (7, None, ["'Turn left into the small square. Look for a blue wooden door.' In Arabic, searching for something combines ", (None, 'دوري على'), ", 'look for'."]),
    (8, None, ["'Does the shop have a big sign outside?' Street signs across Amman are called ", (None, 'آرمة'), ', an everyday local word.']),
    (9, None, ["'Only a golden key painted above the door. Show the clerk this valve.' Handing an item over for someone to inspect uses ", (None, 'فرجي'), ", 'show!'."]),
    (11, None, ["'Run fast, Nour. Room four wakes up at seven fifteen!' Quarter past the hour is ", (None, 'وربع'), ", so 'seven and a quarter' means seven fifteen."]),
]
