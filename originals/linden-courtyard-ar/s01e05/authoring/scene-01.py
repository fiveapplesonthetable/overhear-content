# Authoring module for linden-courtyard-ar-s01e05-scene-01.
ID = 'linden-courtyard-ar-s01e05-scene-01'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Truth in the Courtyard  (الحقيقة في الساحة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'evelyn': 'Evelyn'}
INTRO = 'في ساحة النزل يروي كاليب لإيفلين وهانا كيف أخذ حقيبة إيفلين في قطار الاثنين بمحض الخطأ، وكيف ارتبك عندما لمح شقيقه الأكبر أوين في الشارع فترك الحقيبة على العتبة مع ملاحظة يوم الجمعة. استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نتتبع الآن تفاصيل هذا الاعتراف الصادق جملةً بعد جملة.'
TRANSITION = 'لنستمع الآن مرةً ثانية إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'اتضحت أخيراً حكاية الحقيبتين الزرقاوين المتطابقتين، وبقي سر الخلاف القديم بين الشقيقين كاليب وأوين. نلتقي في المشهد الثاني أمام مكتب الاستقبال.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('evelyn', 'Let me look at you properly, Caleb! You grew taller than the piano!', 'دعني أنظر إليك جيداً يا كاليب! لقد كبرتَ وصرتَ أطول من البيانو!'),
    ('caleb', 'I cannot believe you are staying in the exact same guesthouse, Miss Evelyn.', 'لا أصدق أنكِ تقيمين في النزل نفسه تماماً يا آنسة إيفلين.'),
    ('hannah', 'Wait, so you rode the same train on Monday and took her suitcase?', 'مهلاً، إذن ركبتما القطار نفسه يوم الاثنين وأخذتَ أنت حقيبتها؟'),
    ('caleb', "By complete accident! At my cousin's apartment I opened it and saw sheet music and a red ribbon.", 'بمحض المصادفة غير المقصودة! في شقة ابن عمي فتحتها ورأيتُ نوتات موسيقية وشريطاً أحمر.'),
    ('evelyn', 'Why did you leave my bag on the step at night and run away?', 'لماذا تركتَ حقيبتي على العتبة ليلاً وفررتَ مسرعاً؟'),
    ('caleb', 'Because when I walked here on Monday evening, I saw my older brother walking down this street!', 'لأنني حين مشيتُ إلى هنا مساء الاثنين، لمحتُ أخي الأكبر يمشي في هذا الشارع!'),
    ('hannah', 'Your older brother lives here in Portland?', 'أخوك الأكبر يعيش هنا في بورتلاند؟'),
    ('caleb', 'Yes. I panicked, rang your bell, and slipped the Friday note onto the handle.', 'نعم. أصابني الارتباك، فقرعتُ جرسكم، ودسستُ ملاحظة يوم الجمعة على المقبض.'),
    ('evelyn', 'Wait, and Wednesday night you checked in here under your real name?', 'مهلاً، وفي ليلة الأربعاء سجلتَ دخولك هنا باسمك الحقيقي؟'),
    ('caleb', 'I needed a quiet place nearby before Friday, and honestly felt too shy to ask for my bag!', 'كنت بحاجة إلى مكان هادئ قريب قبل يوم الجمعة، وبصراحة شعرت بالخجل الشديد من طلب حقيبتي!'),
    ('hannah', 'Even after you called us on Tuesday about the white package!', 'حتى بعد أن اتصلت بنا يوم الثلاثاء بشأن الرزمة البيضاء!'),
    ('caleb', 'Everything in that white paper belongs to my brother Owen, not me.', 'كل ما في تلك الورقة البيضاء يخص أخي أوين، لا يخصني أنا.'),
]
WALK = [
    (0, None, ["'دعني أنظر إليك جيداً يا كاليب! لقد كبرتَ وصرتَ أطول من البيانو!' يعبر الظرف", (None, 'properly'), 'عن تأمل الملامح بشوق بعد طول غياب.']),
    (1, None, ["'لا أصدق أنكِ تقيمين في النزل نفسه تماماً يا آنسة إيفلين.' تجمع عبارة التوكيد", (None, 'the exact same guesthouse'), 'بين التحديد والتعجب من المصادفة.']),
    (2, None, ["'انتظر، إذن ركبنا القطار نفسه يوم الاثنين، وأخذتَ أنت حقيبتها؟' يُستعمل الفعل", (None, 'rode the same train'), 'للحديث عن رحلات القطارات والحافلات.']),
    (3, None, ["'بمحض المصادفة غير المقصودة! في شقة ابن عمي فتحتها ورأيتُ نوتات موسيقية وشريطاً أحمر.' تشدد العبارة", (None, 'By complete accident'), 'على براءة الموقف تماماً.']),
    (4, None, ["'لماذا تركتَ حقيبتي على العتبة ليلاً وفررتَ مسرعاً؟' يصوّر الفعل المركب", (None, 'run away'), 'الانسحاب السريع من الحرج.']),
    (5, None, ["'لأنني حين مشيتُ إلى هنا مساء الاثنين، لمحتُ أخي الأكبر يمشي في هذا الشارع!' يأتي بعد فعل الرؤية", (None, 'saw my older brother walking'), 'الفعل بصيغة الاستمرار لتصوير المشهد أمام العين.']),
    (6, None, ["'أخوك الأكبر يعيش هنا في بورتلاند؟' نبرة الاستفهام على الجملة الخبرية", (None, 'lives here in Portland'), 'تكفي لإظهار المفاجأة في المحادثة.']),
    (7, None, ["'نعم. أصابني الارتباك، فقرعتُ جرسكم، ودسستُ ملاحظة يوم الجمعة على المقبض.' يجمع الفعل مع حرف الجر", (None, 'slipped the Friday note onto'), 'بين السرعة والهدوء.']),
    (8, None, ["'مهلاً، وفي ليلة الأربعاء سجلتَ دخولك هنا باسمك الحقيقي؟' تعني العبارة الفندقية", (None, 'checked in here under your real name'), 'تدوين الاسم في سجل النزلاء.']),
    (9, None, ["'احتجتُ إلى مكان هادئ في الجوار قبل يوم الجمعة، ونسيتُ بصدق أن حقيبتي لا تزال لديكم!' تأتي كلمة", (None, 'nearby'), 'مباشرةً بعد الاسم من غير حاجة إلى حرف جر.']),
    (10, None, ["'حتى اتصلتَ بنا يوم الثلاثاء طالباً منا عدم فتح اللفافة البيضاء!' يوضح النفي قبل المصدر في", (None, 'called us on Tuesday about'), 'طريقة صياغة الرجاء المنفي.']),
    (11, None, ["'كل ما في تلك الورقة البيضاء يخص أخي أوين، لا يخصني أنا.' يربط الفعل", (None, 'belongs to'), 'الغرض المحفوظ بصاحبه الحقيقي.']),
]
