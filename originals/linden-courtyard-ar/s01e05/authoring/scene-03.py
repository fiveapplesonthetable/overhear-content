# Authoring module for linden-courtyard-ar-s01e05-scene-03.
ID = 'linden-courtyard-ar-s01e05-scene-03'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = 'Friday Lemon Cake  (كعكة الليمون ليوم الجمعة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'evelyn': 'Evelyn', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = 'تتذكر الآنسة إيفلين كيف كان الجد يقطع كعكة الليمون الدافئة المغطاة بالسكر المطحون بعد كل درس بيانو يوم الجمعة ليصالح أوين مع البيانو، فتلمع في ذهن تيسا فكرة رائعة لموعد الظهر! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نستمتع الآن بذكريات كعكة الليمون جملةً بعد جملة.'
TRANSITION = 'لنستمع الآن مرةً ثانية إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'ست ليمونات صفراء جاهزة في سلة تيسا، والمطبخ يستعد لخبز أجمل كعكة مصالحة قبل الظهر! نلتقي في المشهد الرابع في الساحة.'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('tessa', 'So, Caleb, you are really staying in the courtyard to greet Owen at noon?', 'إذن يا كاليب، هل ستبقى حقاً في الساحة لاستقبال أوين عند الظهر؟'),
    ('caleb', 'Yes, Tessa. Even if he turns around and walks straight back out the gate.', 'نعم يا تيسا. حتى لو استدار وعاد خارجاً من البوابة مباشرةً.'),
    ('evelyn', 'Owen will not walk out. He always acted tough for five seconds, then softened.', 'لن ينصرف أوين. كان دائماً يتظاهر بالصرامة خمس ثوانٍ، ثم يلين طبعه.'),
    ('caleb', 'You still remember that after all these years?', 'ألا تزالين تتذكرين ذلك بعد كل هذه السنين؟'),
    ('evelyn', 'Of course! Every Friday when he missed a piano note, he frowned at the wall.', 'بالطبع! في كل يوم جمعة حين يخطئ في نغمة بيانو، كان يقطب حاجبيه ناظراً إلى الجدار.'),
    ('tessa', 'How did you get him smiling again, Miss Evelyn?', 'وكيف كنتِ تجعلينه يبتسم من جديد يا آنسة إيفلين؟'),
    ('evelyn', 'His grandfather sliced warm lemon cake with powdered sugar on top!', 'كان جده يقطع شرائح كعكة ليمون دافئة فوقها سكر ناعم مطحون!'),
    ('caleb', 'Oh! Yellow lemon glaze! We fought over the corner piece every single Friday!', 'أوه! طبقة الليمون الصفراء اللامعة! كنا نتشاجر على قطعة الزاوية في كل جمعة بلا استثناء!'),
    ('tessa', 'Hold everything! What time is it right now? Nine thirty-five!', 'توقفوا جميعاً! كم الساعة الآن تماماً؟ التاسعة وخمس وثلاثون دقيقة!'),
    ('caleb', 'Tessa, please do not do extra work because of us.', 'تيسا، أرجوكِ لا تتكلفي عملاً إضافياً بسببنا.'),
    ('tessa', 'Six yellow lemons are sitting in my basket right now. This kitchen was waiting for today!', 'ست ليمونات صفراء تنتظر في سلتي الآن. هذا المطبخ كان ينتظر هذا اليوم!'),
    ('evelyn', 'Bake plenty of corner pieces, my dear!', 'اخبزي قطعاً وافرة من الزوايا يا عزيزتي!'),
]
WALK = [
    (0, None, ["'إذن يا كاليب، هل ستبقى حقاً في الساحة لاستقبال أوين عند الظهر؟' يستعمل المضارع المستمر في", (None, 'you are really staying'), 'لتأكيد القرار المتخذ لموعد قريب.']),
    (1, None, ["'نعم يا تيسا. حتى لو استدار وعاد خارجاً من البوابة مباشرةً.' تربط أداة الشرط", (None, 'Even if he turns around'), 'العزم الثابت بأسوأ الاحتمالات.']),
    (2, None, ["'لن ينصرف أوين. كان دائماً يتظاهر بالصرامة خمس ثوانٍ، ثم يلين طبعه.' يصوّر التقابل بين", (None, 'acted tough'), 'وبين الفعل اللاحق', (None, 'softened'), 'شخصية الأخ الأكبر بدقة.']),
    (3, None, ["'ألا تزالين تتذكرين ذلك بعد كل هذه السنين؟' تبرز عبارة", (None, 'after all these years'), 'دهشة الوفاء بالذكريات البعيدة.']),
    (4, None, ["'بالطبع! في كل يوم جمعة حين يخطئ في نغمة بيانو، كان يقطب حاجبيه ناظراً إلى الجدار.' في الموسيقى نقول", (None, 'missed a piano note'), 'عند عدم إصابة المفتاح الصحيح.']),
    (5, None, ["'وكيف كنتِ تجعلينه يبتسم من جديد يا آنسة إيفلين؟' يفيد التركيب السببي الودود", (None, 'get him smiling again'), 'النجاح في تغيير مزاجه بلطف.']),
    (6, None, ["'كان جده يقطع شرائح كعكة ليمون دافئة فوقها سكر ناعم مطحون!' تحدد عبارة", (None, 'with powdered sugar on top'), 'اللمسة الأخيرة على الحلوى.']),
    (7, None, ["'أوه! طبقة الليمون الصفراء اللامعة! كنا نتشاجر على قطعة الزاوية في كل جمعة بلا استثناء!' تشدد عبارة", (None, 'every single Friday'), 'على تكرار الذكرى الطفولية المحببة.']),
    (8, None, ["'توقفوا جميعاً! كم الساعة الآن تماماً؟ التاسعة وخمس وثلاثون دقيقة!' صيحة الحماسة المرحة", (None, 'Hold everything'), 'تعلن ولادة فكرة فورية.']),
    (9, None, ["'تيسا، أرجوكِ لا تتكلفي عملاً إضافياً بسببنا.' يعتذر الضيف المهذب بعبارة", (None, 'because of us'), 'كي لا يشق على مضيفه.']),
    (10, None, ["'ست ليمونات صفراء تنتظر في سلتي الآن. هذا المطبخ كان ينتظر هذا اليوم!' تشخيص المكان في", (None, 'This kitchen was waiting for today'), 'يفيض مودةً وكرماً.']),
    (11, None, ["'اخبزي قطعاً وافرة من الزوايا يا عزيزتي!' يجمع الطلب المازح بين", (None, 'plenty of corner pieces'), 'ومخاطبة المودة في الختام.']),
]
