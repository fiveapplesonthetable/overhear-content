# Authoring module for linden-courtyard-ar-s01e05-scene-07.
ID = 'linden-courtyard-ar-s01e05-scene-07'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 5
SCENE = 7
TITLE = 'Twelve Chimes  (اثنتا عشرة دقّة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'تنقضي دقات الظهر الاثنتا عشرة والشارع خالٍ تماماً، فيكاد اليأس يتسلل إلى قلب كاليب، وإذا بسيارة أجرة صفراء تتوقف عند حافة الرصيف ويترجل منها رجل طويل بمعطف رمادي داكن! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نعيش لحظات الترقب الحاسمة هذه جملةً بعد جملة.'
TRANSITION = 'لنستمع الآن مرةً ثانية إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'رن جرس البوابة رنةً واحدة حازمة، وذهبت هانا لتفتح الباب لأوين! نلتقي في المشهد الثامن الأخير من هذه الحلقة.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('caleb', 'Twelve chimes... and the street outside the gate is completely empty.', 'اثنتا عشرة دقة... والشارع خارج البوابة خالٍ تماماً.'),
    ('hannah', 'Give it a few minutes, Caleb. City traffic at noon is always slow.', 'أمهل الأمر بضع دقائق يا كاليب. فحركة السير في المدينة وقت الظهر بطيئة دائماً.'),
    ('graham', 'And big brothers never arrive early when they want to look calm.', 'والإخوة الكبار لا يصلون مبكرين أبداً حين يريدون أن يبدوا هادئين.'),
    ('caleb', 'Look, it is four minutes past twelve already. Maybe he threw my postcard in the trash.', 'انظرا، مضت أربع دقائق بعد الثانية عشرة بالفعل. ربما رمى بطاقتي البريدية في القمامة.'),
    ('hannah', 'Do not sit down defeated yet! Keep looking toward the corner.', 'لا تجلس مستسلماً للهزيمة بعد! واصل النظر باتجاه الزاوية.'),
    ('caleb', 'Three years was too long to wait, Hannah. I should have called him two winters ago.', 'ثلاث سنوات كانت فترة طويلة جداً للانتظار يا هانا. كان ينبغي أن أتصل به قبل شتاءين.'),
    ('graham', 'Hold still, both of you. Hear that car engine stopping at the curb?', 'اثبتا في مكانكما أنتما الاثنان. هل تسمعان محرك تلك السيارة يتوقف عند حافة الرصيف؟'),
    ('hannah', 'A yellow taxi just pulled up outside the iron gate!', 'توقفت سيارة أجرة صفراء للتو خارج البوابة الحديدية!'),
    ('caleb', 'My hands are shaking. Is there a tall man in a dark gray coat?', 'يداي ترتجفان. هل يقف هناك رجل طويل يرتدي معطفاً رمادياً داكناً؟'),
    ('hannah', 'Tall, dark gray coat, looking up at our guesthouse sign right now!', 'طويل القامة، بمعطف رمادي داكن، ينظر إلى الأعلى نحو لافتة نزلنا في هذه اللحظة!'),
    ('graham', 'There goes the gate bell. One firm ring.', 'ها قد رن جرس البوابة. رنة واحدة حازمة.'),
    ('hannah', 'Shoulders back, Caleb. Remember your three simple sentences. I will open the gate!', 'افرد كتفيك يا كاليب. تذكّر جملك الثلاث البسيطة. سأفتح أنا البوابة!'),
]
WALK = [
    (0, None, ["'اثنتا عشرة دقة... والشارع خارج البوابة خالٍ تماماً.' يقوي الظرف", (None, 'completely empty'), 'شعور الوحشة في لحظة الانتظار.']),
    (1, None, ["'أمهل الأمر بضع دقائق يا كاليب. فحركة السير في المدينة وقت الظهر بطيئة دائماً.' تهدئ العبارة", (None, 'Give it a few minutes'), 'قلق المنتظر بلطف واقعي.']),
    (2, None, ["'والإخوة الكبار لا يصلون مبكرين أبداً حين يريدون أن يبدوا هادئين.' يجمع الفعل والصفة في", (None, 'to look calm'), 'ملاحظةً نفسية طريفة من غراهام.']),
    (3, None, ["'انظرا، مضت أربع دقائق بعد الثانية عشرة بالفعل. ربما رمى بطاقتي البريدية في القمامة.' يُعبر عن الدقائق المنقضية بعد الساعة بقول", (None, 'four minutes past twelve'), 'بترتيب الدقائق أولاً.']),
    (4, None, ["'لا تجلس مستسلماً للهزيمة بعد! واصل النظر باتجاه الزاوية.' يأتي بعد الفعل في", (None, 'Keep looking toward'), 'صيغة الاستمرار للدلالة على عدم اليأس.']),
    (5, None, ["'ثلاث سنوات كانت فترة طويلة جداً للانتظار يا هانا. كان ينبغي أن أتصل به قبل شتاءين.' تفيد صيغة الندم في الماضي", (None, 'I should have called him'), 'لوم النفس على تأخير المبادرة.']),
    (6, None, ["'اثبتا في مكانكما أنتما الاثنان. هل تسمعان محرك تلك السيارة يتوقف عند حافة الرصيف؟' تطلب عبارة", (None, 'Hold still'), 'الإنصات التام للصوت القادم.']),
    (7, None, ["'توقفت سيارة أجرة صفراء للتو خارج البوابة الحديدية!' يعني الفعل المركب", (None, 'just pulled up'), 'توقف المركبات عند المدخل.']),
    (8, None, ["'يداي ترتجفان. هل يقف هناك رجل طويل يرتدي معطفاً رمادياً داكناً؟' يحدد حرف الجر", (None, 'in a dark gray coat'), 'اللباس المميز للشخص.']),
    (9, None, ["'طويل القامة، بمعطف رمادي داكن، ينظر إلى الأعلى نحو لافتة نزلنا في هذه اللحظة!' يصف الفعل المركب", (None, 'looking up at'), 'قراءة اللافتة المعلقة.']),
    (10, None, ["'ها قد رن جرس البوابة. رنة واحدة حازمة.' تصف العبارة الوجيزة", (None, 'One firm ring'), 'شخصية الطارق من طريقة ضغطه للجرس.']),
    (11, None, ["'افرد كتفيك يا كاليب. تذكّر جملك الثلاث البسيطة. سأفتح أنا البوابة!' تشجع العبارة", (None, 'Shoulders back'), 'على الوقوف بشجاعة وطمأنينة.']),
]
