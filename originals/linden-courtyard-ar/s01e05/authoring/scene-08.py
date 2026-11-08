# Authoring module for linden-courtyard-ar-s01e05-scene-08.
ID = 'linden-courtyard-ar-s01e05-scene-08'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = 'The Red-Stamped Letter  (الرسالة ذات الختم الأحمر)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'بينما يقف كاليب وأوين وجهاً لوجه تحت شجرة الساحة في الخارج، يفتح آرثر رسالة المالك داخل مكتب الاستقبال، فيشحب وجهه فجأةً حين يقرأ إشعاراً بعرض المبنى للبيع وتحويله إلى مكاتب تجارية خلال ثلاثين يوماً! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'لنتتبع الآن هذا التحول الدرامي المفاجئ جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'أخفى آرثر وهانا وتيسا قلقهما مؤقتاً كي لا يفسدوا لقاء الشقيقين في الخارج، بينما تلوح خلف الإشعار صفحة ثانية مطوية! نلتقي في الحلقة السادسة والأخيرة.'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('tessa', 'Hannah, look through the glass. They are standing face to face under the tree!', 'هانا، انظري عبر الزجاج. إنهما يقفان وجهاً لوجه تحت الشجرة!'),
    ('hannah', 'Neither of them walked away! Caleb is pointing at the two chairs right now!', 'لم ينصرف أي منهما! يشير كاليب إلى الكرسيين في هذه اللحظة!'),
    ('arthur', 'Wonderful... let me just glance at this landlord letter while we wait.', 'رائع... دعوني ألقِ نظرة سريعة على رسالة المالك هذه ريثما ننتظر.'),
    ('tessa', 'Probably a boring notice about painting the street shutters.', 'على الأرجح إشعار ممل بشأن طلاء مصاريع الشارع.'),
    ('arthur', 'Oh... oh no. Where is my chair? My knees feel weak.', 'أوه... أوه لا. أين كرسيي؟ أشعر بوهن في ركبتيّ.'),
    ('hannah', 'Arthur! Your face went completely white! Sit down, what does the letter say?', 'آرثر! لقد شحب وجهك تماماً! اجلس، ماذا تقول الرسالة؟'),
    ('arthur', 'Read the top line for me, Hannah. Tell me my glasses are playing tricks again!', 'اقرئي لي السطر العلوي يا هانا. قولي لي إن نظارتي تخدعني مرة أخرى!'),
    ('hannah', "'Notice of Property Transfer: Number Eight Courtyard Building offered for commercial office sale.'", 'إشعار نقل ملكية عقارية: مبنى الساحة رقم ثمانية معروض للبيع كمكاتب تجارية.'),
    ('tessa', 'Commercial office sale?! Turn our guesthouse and kitchen into gray offices?!', 'بيع كمكاتب تجارية؟! أَيحوّلون نزلنا ومطبخنا إلى مكاتب رمادية؟!'),
    ('arthur', 'They give us thirty days before new buyers inspect the building!', 'يمهلوننا ثلاثين يوماً قبل أن يعاين المشترون الجدد المبنى!'),
    ('hannah', 'Wait, there is a second folded page clipped to the back of this notice...', 'انتظروا، توجد صفحة ثانية مطوية مشبوكة خلف هذا الإشعار...'),
    ('arthur', 'Not a word to anyone outside yet! Let the two brothers have their Friday afternoon first!', 'ولا كلمة لأحد في الخارج بعد! دعوا الشقيقين يحظيان بأمسية جمعتهما أولاً!'),
]
WALK = [
    (0, None, ["'هانا، انظري عبر الزجاج. إنهما يقفان وجهاً لوجه تحت الشجرة!' تصف العبارة المتناظرة", (None, 'face to face'), 'اللقاء الصريح بعد طول فراق.']),
    (1, None, ["'لم ينصرف أي منهما! يشير كاليب إلى الكرسيين في هذه اللحظة!' ينفي التركيب", (None, 'Neither of them walked away'), 'المخاوف السابقة كلها.']),
    (2, None, ["'رائع... دعوني ألقِ نظرة سريعة على رسالة المالك هذه ريثما ننتظر.' يفيد الفعل مع حرف الجر", (None, 'glance at'), 'تصفح الورقة على عجل.']),
    (3, None, ["'على الأرجح إشعار ممل بشأن طلاء مصاريع الشارع.' يتبع حرف الجر", (None, 'about painting'), 'صيغة الاسمية للفعل.']),
    (4, None, ["'أوه... أوه لا. أين كرسيي؟ أشعر بوهن في ركبتيّ.' يصوّر التعبير", (None, 'My knees feel weak'), 'وقع الصدمة المفاجئة.']),
    (5, None, ["'آرثر! لقد شحب وجهك تماماً! اجلس، ماذا تقول الرسالة؟' تعبر الإنجليزية عن شحوب الوجه بقول", (None, 'went completely white'), 'كما تسأل عن مضمون المكتوب بفعل القول.']),
    (6, None, ["'اقرئي لي السطر العلوي يا هانا. قولي لي إن نظارتي تخدعني مرة أخرى!' يفيد التعبير الاصطلاحي", (None, 'playing tricks'), 'تمني أن تكون القراءة خاطئة.']),
    (7, None, ["'إشعار نقل ملكية عقارية: مبنى الساحة رقم ثمانية معروض للبيع كمكاتب تجارية.' تحذف الصياغات الرسمية أفعال الكينونة في", (None, 'offered for commercial office sale'), 'إيجازاً في العناوين.']),
    (8, None, ["'بيع كمكاتب تجارية؟! أَيحوّلون نزلنا ومطبخنا إلى مكاتب رمادية؟!' يقترن الفعل", (None, 'Turn our guesthouse and kitchen into'), 'بحرف الجر الدال على النتيجة.']),
    (9, None, ["'يمهلوننا ثلاثين يوماً قبل أن يعاين المشترون الجدد المبنى!' يستعمل المضارع البسيط بعد", (None, 'before new buyers inspect'), 'للدلالة على الموعد المستقبلي المحدد.']),
    (10, None, ["'انتظروا، توجد صفحة ثانية مطوية مشبوكة خلف هذا الإشعار...' تصف الصفتان المتتاليتان", (None, 'folded page clipped'), 'تفصيلاً صغيراً سيغير مجرى القصة.']),
    (11, None, ["'ولا كلمة لأحد في الخارج بعد! دعوا الشقيقين يحظيان بأمسية جمعتهما أولاً!' صيغة الكتمان المؤقت", (None, 'Not a word to anyone'), 'تُظهر نبل آرثر وإيثاره لضيوفه.']),
]
