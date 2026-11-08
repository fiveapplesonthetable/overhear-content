# Authoring module for linden-courtyard-ar-s01e06-scene-04.
ID = 'linden-courtyard-ar-s01e06-scene-04'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 6
SCENE = 4
TITLE = 'Lemon Cake and Sharp Eyes  (كعكة الليمون والعيون النابهة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'tessa': 'Tessa', 'owen': 'Owen', 'caleb': 'Caleb'}
INTRO = 'تقدم تيسا كعكة الليمون الساخنة للشقيقين فيندهش أوين من مذاقها المطابق لذكريات شارع الزيزفون، غير أن عينيه النابهتين تلمحان ملامح الحزن على وجه آرثر خلف النافذة فيعرض مع كاليب خبرتهما القانونية والمعمارية فوراً! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نستعرض هذا المشهد المفعم بالمودة والنجدة جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'اجتمع خبير عقود البلدية أوين ومهندس التراث كاليب لفحص الرسالة، وانطلقت تيسا بهما إلى مكتب الاستقبال! نلتقي في المشهد الخامس.'
CLOSING = ('tessa', 'See you soon!')
STORY = [
    ('tessa', 'Fresh from the oven: Friday lemon cake with extra corner pieces!', 'طازجة من الفرن: كعكة الليمون ليوم الجمعة مع قطع زوايا إضافية!'),
    ('owen', 'One bite... Caleb, close your eyes! That tastes exactly like Linden Street!', 'لقمة واحدة... كاليب، أغمض عينيك! مذاقها يشبه شارع الزيزفون تماماً!'),
    ('caleb', 'Tessa baked it this morning when Miss Evelyn told her our Friday story.', 'خبزتها تيسا هذا الصباح عندما روت لها الآنسة إيفلين حكاية يوم الجمعة الخاصة بنا.'),
    ('owen', 'What kind of magical guesthouse did you walk into, little brother?', 'أي نزل ساحر هذا الذي دخلتَ إليه يا أخي الصغير؟'),
    ('caleb', "The kind that fixes attic lamps in the rain and guards a stranger's bag.", 'النزل الذي يصلح مصابيح العلية تحت المطر ويحرس حقيبة رجل غريب.'),
    ('owen', 'Then tell me why the poor gentleman behind the front desk looks ready to cry.', 'إذن أخبراني لماذا يبدو السيد المسكين خلف مكتب الاستقبال على وشك البكاء.'),
    ('tessa', 'Oh! Did you see Arthur through the window? I tried to smile twice as wide!', 'أوه! هل رأيتَ آرثر عبر النافذة؟ حاولتُ أن أبتسم ابتسامةً مضاعفة الاتساع!'),
    ('caleb', 'Tessa, is something wrong inside? Did the boiler pipe leak again?', 'تيسا، هل هناك خطب ما في الداخل؟ هل سرّب أنبوب الغلاية مرة أخرى؟'),
    ('tessa', 'Worse than a pipe... a registered letter came from the building owner at noon.', 'أسوأ من الأنبوب... وصلت رسالة مسجلة من مالك المبنى وقت الظهر.'),
    ('owen', 'A property letter? Let Caleb and me see it. I work in city contracts, and he knows heritage law!', 'رسالة عقارية؟ دعيني أنا وكاليب نراها. أنا أعمل في عقود المدينة، وهو خبير بقانون التراث!'),
    ('caleb', "Wait, Owen, you still work at City Hall's contract desk?!", 'مهلاً يا أوين، ألا تزال تعمل في مكتب العقود في دار البلدية؟!'),
    ('tessa', 'Both of you?! Leave your teacups, come inside this very second!', 'أنتما الاثنان معاً؟! اتركا فنجاني الشاي وادخلا في هذه الثانية بالذات!'),
]
WALK = [
    (0, None, ["'طازجة من الفرن: كعكة الليمون ليوم الجمعة مع قطع زوايا إضافية!' تُقال عبارة", (None, 'Fresh from the oven'), 'عند تقديم المخبوزات الدافئة.']),
    (1, None, ["'لقمة واحدة... كاليب، أغمض عينيك! مذاقها يشبه شارع الزيزفون تماماً!' يربط التركيب الحسي", (None, 'tastes exactly like'), 'الطعم ببيت الطفولة كله.']),
    (2, None, ["'خبزتها تيسا هذا الصباح عندما روت لها الآنسة إيفلين حكاية يوم الجمعة الخاصة بنا.' يأخذ الفعل", (None, 'told her our Friday story'), 'المستمع أولاً ثم القصة المروية.']),
    (3, None, ["'أي نزل ساحر هذا الذي دخلتَ إليه يا أخي الصغير؟' يعبر السؤال الإعجابي", (None, 'What kind of magical guesthouse'), 'عن الدهشة من كرم المكان.']),
    (4, None, ["'النزل الذي يصلح مصابيح العلية تحت المطر ويحرس حقيبة رجل غريب.' يجيب كاليب بقوله", (None, 'The kind that fixes'), 'ملخصاً مواقف الأسبوع الجميلة.']),
    (5, None, ["'إذن أخبراني لماذا يبدو السيد المسكين خلف مكتب الاستقبال على وشك البكاء.' تفيد الصفة", (None, 'poor gentleman'), 'التعاطف الصادق، وتعني', (None, 'ready to cry'), 'شدة التأثر.']),
    (6, None, ["'أوه! هل رأيتَ آرثر عبر النافذة؟ حاولتُ أن أبتسم ابتسامةً مضاعفة الاتساع!' تأتي المقارنة المضاعفة في", (None, 'twice as wide'), 'لبيان محاولتها إخفاء القلق.']),
    (7, None, ["'تيسا، هل هناك خطب ما في الداخل؟ هل سرّب أنبوب الغلاية مرة أخرى؟' تأتي الصفة بعد الضمير المبهم في", (None, 'is something wrong'), 'للسؤال اللطيف عن المشكلة.']),
    (8, None, ["'أسوأ من الأنبوب... وصلت رسالة مسجلة من مالك المبنى وقت الظهر.' تصف عبارة", (None, 'a registered letter'), 'الخطاب القانوني الموقّع.']),
    (9, None, ["'رسالة عقارية؟ دعيني أنا وكاليب نراها. أنا أعمل في عقود المدينة، وهو خبير بقانون التراث!' تأتي ضمائر المفعول بعد فعل السماح في", (None, 'Let Caleb and me see it'), 'على القاعدة الفصيحة.']),
    (10, None, ["'مهلاً يا أوين، ألا تزال تعمل في مكتب العقود في دار البلدية؟!' يشير اللقب المؤسسي", (None, "City Hall's contract desk"), 'إلى خبرة أوين الدقيقة في اللوائح.']),
    (11, None, ["'أنتما الاثنان معاً؟! اتركا فنجاني الشاي وادخلا في هذه الثانية بالذات!' تشدد العبارة الزمنية", (None, 'this very second'), 'على الحماسة الفورية.']),
]
