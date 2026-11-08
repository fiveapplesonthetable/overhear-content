# Authoring module for linden-courtyard-ar-s01e03-scene-06.
ID = 'linden-courtyard-ar-s01e03-scene-06'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = 'A Five-Star Sigh of Relief  (تنهدة ارتياح من خمس نجوم)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'في الطابق السفلي يحتفل آرثر بنجاح الموقف، غير أن هانا تلمح دفتر ملاحظات جلدياً صغيراً نسيه كاليب على المنضدة مفتوحاً على رسوم وتقييمات غامضة، فيظنون أنه مفتش فنادق! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'لنتتبع الآن مفاجآت هذا المشهد جملةً تلو جملة.'
TRANSITION = 'لنستمع الآن إلى المشهد كاملاً مرةً ثانية.'
OUTRO = 'قبل أن يفيقوا من دهشة الدفتر، دوّت طرقة معدنية عالية في أنابيب التدفئة. نلتقي في المشهد السابع لمعرفة مصدر الصوت.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'Well? Did he shout? Did he ask for his money back?', 'حسناً؟ هل صرخ؟ هل طلب استرداد ماله؟'),
    ('hannah', 'Neither! He loved the quiet roof beams and thanked us.', 'لا هذا ولا ذاك! لقد أحب عوارض السقف الهادئة وشكرنا.'),
    ('arthur', 'Hannah, you have a gift for hospitality! My blood pressure is saved!', 'هانا، لديكِ موهبة فطرية في حسن الضيافة! لقد نجا ضغط دمي!'),
    ('tessa', 'He even finished every drop of vegetable soup before going up.', 'بل إنه أنهى كل قطرة من حساء الخضار قبل صعوده.'),
    ('hannah', 'Wait, whose small brown leather notebook is this on the counter?', 'انتظروا، لمن دفتر الملاحظات الجلدي البني الصغير هذا فوق المنضدة؟'),
    ('tessa', 'Caleb set it down when he took the dry towel from me!', 'وضعه كاليب هناك عندما أخذ المنشفة الجافة مني!'),
    ('arthur', 'Do not snoop, of course... wait, it fell open to the middle page!', 'لا تتلصصوا بالطبع... انتظروا، لقد انفتح وحده على الصفحة الوسطى!'),
    ('hannah', 'Why are there neat pencil drawings of three guesthouses on our street?', 'لماذا توجد رسوم أنيقة بقلم الرصاص لثلاثة نُزُل في شارعنا؟'),
    ('tessa', "Look at the words beside ours: 'Courtyard width, street noise, quiet score: nine out of ten!'", 'انظروا إلى الكلمات بجانب نزلنا: عرض الساحة، ضجيج الشارع، درجة الهدوء: تسع من عشر!'),
    ('arthur', 'Nine out of ten?! Nobody measures lobbies unless...', 'تسع من عشر؟! لا أحد يقيس أبعاد البهو إلا إذا...'),
    ('tessa', 'Unless he writes for the annual Portland Travel Guide!', 'إلا إذا كان يكتب لصالح دليل السفر السنوي لمدينة بورتلاند!'),
    ('hannah', 'Quick, close it! Let us take it upstairs... wait, what is that loud clanking sound?', 'بسرعة، أغلقيه! دعونا نأخذه إلى الأعلى... انتظروا، ما صوت القرقعة المعدنية العالي هذا؟'),
]
WALK = [
    (0, None, ["'حسناً؟ هل صرخ؟ هل طلب استرداد ماله؟' تعني العبارة الفعلية", (None, 'ask for his money back'), 'المطالبة بإرجاع المبلغ المدفوع.']),
    (1, None, ["'لا هذا ولا ذاك! لقد أحب عوارض السقف الهادئة وشكرنا.' تختصر الكلمة الواحدة", (None, 'Neither'), 'نفي السؤالين السابقين معاً برشاقة.']),
    (2, None, ["'هانا، لديكِ موهبة فطرية في حسن الضيافة! لقد نجا ضغط دمي!' تمدح عبارة", (None, 'a gift for hospitality'), 'البراعة الفطرية في الترحيب بالناس.']),
    (3, None, ["'بل إنه أنهى كل قطرة من حساء الخضار قبل صعوده.' تضيف كلمة", (None, 'even'), 'دليلاً إضافياً على ارتياح الضيف وسروره.']),
    (4, None, ["'انتظروا، لمن دفتر الملاحظات الجلدي البني الصغير هذا فوق المنضدة؟' تسأل أداة الملكية", (None, 'whose'), 'عن صاحب الغرض المتبوع بالاسم الموصوف مباشرةً.']),
    (5, None, ["'وضعه كاليب هناك عندما أخذ المنشفة الجافة مني!' يفيد الفعل المركب", (None, 'set it down'), 'ترك الشيء برفق فوق سطح مستوٍ.']),
    (6, None, ["'لا تتلصصوا بالطبع... انتظروا، لقد انفتح وحده على الصفحة الوسطى!' يصف التعبير", (None, 'fell open'), 'انفراج صفحات الدفتر بلا قصد أحد.']),
    (7, None, ["'لماذا توجد رسوم أنيقة بقلم الرصاص لثلاثة نُزُل في شارعنا؟' يحدد المركب", (None, 'neat pencil drawings'), 'أداة الرسم قبل اسم اللوحات المرسومة.']),
    (8, None, ["'انظروا إلى الكلمات بجانب نزلنا: عرض الساحة، ضجيج الشارع، درجة الهدوء: تسع من عشر!' ينوب ضمير الملكية المستقل", (None, 'ours'), 'عن تكرار كلمة النزل، وتُقرأ النتيجة', (None, 'nine out of ten'), 'بهذا النسق.']),
    (9, None, ["'تسع من عشر؟! لا أحد يقيس أبعاد البهو إلا إذا...' تمهّد أداة الاستثناء الشرطي", (None, 'unless'), 'لاستنتاج واحد لا ثاني له.']),
    (10, None, ["'إلا إذا كان يكتب لصالح دليل السفر السنوي لمدينة بورتلاند!' يفيد الفعل مع حرف الجر", (None, 'writes for'), 'العمل محرراً أو مقيّماً في منشور دوري.']),
    (11, None, ["'بسرعة، أغلقيه! دعونا نأخذه إلى الأعلى... انتظروا، ما صوت القرقعة المعدنية العالي هذا؟' تحاكي الصفة الصوتية", (None, 'clanking sound'), 'رنين ارتطام الحديد في الأنابيب.']),
]
