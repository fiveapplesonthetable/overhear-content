# Authoring module for bayt-al-yasmin-s01e02-scene-03.
ID = 'bayt-al-yasmin-s01e02-scene-03'
SHOW = 'bayt-al-yasmin'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'حساب الباقي  (Counting the Change)'
LEVEL = 'A1 — beginner'
PAIR = 'ar-en'
LABELS = {"mazen": "مازن", "nour": "نور", "salma": "سلمى"}
INTRO = 'Nine minutes later, Nour bursts back through the courtyard gate carrying two heavy bags of groceries for Salma and Mazen. Listen to the scene in Arabic first.'
OPENER = "Now let's go back through the groceries and the change, line by line."
TRANSITION = "Let's hear the whole scene again from start to finish."
OUTRO = 'An accidental packet of salted butter nearly caused a jam crisis, until Salma turned it into the secret ingredient for the eggs. See you next time.'
CLOSING = ('salma', 'نشوفك!')
STORY = [
    ('nour', 'تسع دقايق! هي الحليب والبيض والتفاح!', 'Nine minutes! Here are the milk, the eggs, and the apples!'),
    ('salma', 'إنتي بطلة يا نور! أعطيني الحليب أول لماكينة القهوة.', 'You are a hero, Nour! Give me the milk first for the coffee machine.'),
    ('mazen', 'سرعة ممتازة! البياع أعطاكي فاتورة؟', 'Excellent speed! Did the shopkeeper give you a receipt?'),
    ('nour', 'تفضل! الحساب تمانية وتلاتين، وهي اطنعش دينار باقي.', 'Here you go! The bill was thirty-eight, and here is twelve dinars change.'),
    ('mazen', 'عشرة، حدعش، اطنعش. تمام لآخر قرش، شكرا!', 'Ten, eleven, twelve. Exact to the last piastre, thank you!'),
    ('salma', 'استني ثانية يا نور... أي علبة زبدة جبتي؟', 'Wait a second, Nour... which packet of butter did you bring?'),
    ('nour', 'العلبة الدهبية عالرف الفوقاني. ليش؟', 'The golden packet on the top shelf. Why?'),
    ('salma', 'هادي زبدة مالحة كتير! خبز المربى الحلو بده زبدة عادية!', 'That is very salty butter! Sweet jam bread needs plain butter!'),
    ('nour', 'يا الله! كل العلب كان شكلها واحد وأنا بركض!', 'Oh no! All the packets looked the same while I was running!'),
    ('mazen', 'بنقدر نقدم زبدة مالحة مع مربى فراولة حلو؟', 'Can we serve salty butter with sweet strawberry jam?'),
    ('salma', 'لحظة، الزبدة المالحة صعبة للمربى، بس رهيبة مع البيض المقلي!', 'Wait, salty butter is tough for jam, yet amazing with fried eggs!'),
    ('nour', 'الحمد لله! التفكير السريع أنقذ الفطور كمان مرة.', 'Thank goodness! Quick thinking saved breakfast once again.'),
]
WALK = [
    (0, None, ["'Nine minutes! Here are the milk, the eggs, and the apples!' Pointing things out as you hand them over uses little ", (None, 'هي'), ", 'here is'."]),
    (1, None, ["'You are a hero, Nour! Give me the milk first for the coffee machine.' Praising a woman who saves the day uses ", (None, 'بطلة'), ", 'hero' or 'champion'."]),
    (3, None, ["'Here you go! The bill was thirty-eight, and here is twelve dinars change.' Numbers above twenty put ones first in ", (None, 'تمانية وتلاتين'), ', while ', (None, 'باقي'), " means 'change'."]),
    (4, None, ["'Ten, eleven, twelve. Exact to the last piastre, thank you!' One dinar divides into a hundred ", (None, 'قرش'), ", piastres, so 'to the last piastre' means to the last penny."]),
    (5, None, ["'Wait a second, Nour... which packet of butter did you bring?' In Arabic, put ", (None, 'أي'), " right before a noun to ask 'which packet?'."]),
    (7, None, ["'That is very salty butter! Sweet jam bread needs plain butter!' Even inanimate things use ", (None, 'بده'), "—literally 'sweet bread wants plain butter'."]),
    (10, None, ["'Wait, salty butter is tough for jam, yet amazing with fried eggs!' Literally 'awesome' or 'terrific', ", (None, 'رهيبة'), ' is glowing praise in everyday Amman speech.']),
    (11, None, ["'Thank goodness! Quick thinking saved breakfast once again.' Every sigh of relief in Arabic starts with ", (None, 'الحمد لله'), ", 'thank goodness'."]),
]
