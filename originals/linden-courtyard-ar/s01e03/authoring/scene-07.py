# Authoring module for linden-courtyard-ar-s01e03-scene-07.
ID = 'linden-courtyard-ar-s01e03-scene-07'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = 'Returning the Notebook  (إعادة دفتر الملاحظات)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = 'تصعد هانا لتعيد دفتر الملاحظات الجلدي إلى كاليب في غرفة العلية، فيشكرها بحرارة، لكنهما يلاحظان معاً أن مشعاع التدفئة بدأ يبرد من الأسفل بعد تلك الطرقة المعدنية. استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نقرأ الآن هذا الحوار الهادئ جملةً بعد جملة.'
TRANSITION = 'لنستمع الآن مرةً ثانية إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'قابل كاليب برودة المشعاع بصبر ولطف، فيما أسرعت هانا إلى الطابق السفلي لتفقد الغلاية مع غراهام. نلتقي في المشهد الثامن.'
CLOSING = ('caleb', 'Have a good night!')
STORY = [
    ('hannah', 'Excuse me, Caleb? Sorry to disturb you.', 'عفواً يا كاليب؟ عذراً على إزعاجك.'),
    ('caleb', 'Oh, my leather notebook! Thank you! I was just looking for it.', 'أوه، دفتري الجلدي! شكراً لكِ! كنتُ أبحث عنه للتو.'),
    ('hannah', 'You left it by the soup cup on the front counter.', 'لقد تركته بجانب كوب الحساء على المنضدة الأمامية.'),
    ('caleb', 'All my street notes from this week are in here. You saved me.', 'كل ملاحظاتي عن الشوارع من هذا الأسبوع موجودة هنا. لقد أنقذتني.'),
    ('hannah', 'We are glad you find our courtyard peaceful for your... work.', 'يسعدنا أن تجد ساحتنا هادئة ومناسبة... لعملك.'),
    ('caleb', 'Very peaceful! Though did you hear a funny metal knock just now?', 'هادئة جداً! غير أنكِ هل سمعتِ طرقة معدنية غريبة قبل لحظة؟'),
    ('hannah', 'Yes! It sounded like it came from the heating pipe in the corner.', 'نعم! بدت كأنها صادرة من أنبوب التدفئة في الزاوية.'),
    ('caleb', 'Feel the radiator. The bottom is warm, while the top is turning cool.', 'تحسس المشعاع. الجزء السفلي دافئ، بينما الجزء العلوي بدأ يبرد.'),
    ('hannah', 'Oh! Sometimes old pipes have a little air bubble at night.', 'أوه! تتكون أحياناً في الأنابيب القديمة فقاعة هواء صغيرة ليلاً.'),
    ('caleb', 'I have a warm blanket, so I am quite comfortable tonight.', 'لديّ بطانية دافئة، لذا فأنا مرتاح تماماً هذه الليلة.'),
    ('hannah', 'Thank you for being so patient! Graham will check the basement right away.', 'شكراً لك على سعة صدرك وصبرك! سيتفقد غراهام القبو على الفور.'),
    ('caleb', 'Good night, Hannah. See you at breakfast.', 'تصبحين على خير يا هانا. أراكِ على الفطور.'),
]
WALK = [
    (0, None, ["'عفواً يا كاليب؟ عذراً على إزعاجك.' عند طرق باب ضيف بلباقة نبدأ بعبارة", (None, 'Sorry to disturb you'), 'احتراماً لهدوئه.']),
    (1, None, ["'أوه، دفتري الجلدي! شكراً لكِ! كنتُ أبحث عنه للتو.' يصف الماضي المستمر في", (None, 'I was just looking for it'), 'انشغاله بالبحث لحظة طرق الباب.']),
    (2, None, ["'لقد تركته بجانب كوب الحساء على المنضدة الأمامية.' يفيد حرف الجر", (None, 'by'), 'القرب المكاني المباشر على سطح المنضدة.']),
    (3, None, ["'كل ملاحظاتي عن الشوارع من هذا الأسبوع موجودة هنا. لقد أنقذتني.' تعبّر الجملة القصيرة", (None, 'You saved me'), 'عن امتنان عميق صادق في الحديث اليومي.']),
    (4, None, ["'يسعدنا أن تجد ساحتنا هادئة ومناسبة... لعملك.' يأخذ الفعل", (None, 'find'), 'مفعوله متبوعاً بالصفة', (None, 'peaceful'), 'لبيان الانطباع الشخصي.']),
    (5, None, ["'هادئة جداً! غير أنكِ هل سمعتِ طرقة معدنية غريبة قبل لحظة؟' تعني الصفة", (None, 'funny'), 'هنا صوتاً مستغرباً لا صوتاً مضحكاً.']),
    (6, None, ["'نعم! بدت كأنها صادرة من أنبوب التدفئة في الزاوية.' يربط التركيب", (None, 'It sounded like'), 'بين ما سمعته الأذن ومصدره المرجح.']),
    (7, None, ["'المسي مشعاع التدفئة. الجزء العلوي دافئ، بينما يميل الجزء السفلي إلى البرودة.' يفيد الفعل مع الصفة في", (None, 'is turning cool'), 'التحول المستمر في درجة الحرارة.']),
    (8, None, ["'أوه! تتكون أحياناً في الأنابيب القديمة فقاعة هواء صغيرة ليلاً.' يحدد الاسم المركب", (None, 'air bubble'), 'السبب الشائع لانحباس الماء الساخن في الأنابيب.']),
    (9, None, ["'لديّ بطانية دافئة، لذا فأنا مرتاح تماماً هذه الليلة.' يقوي الظرف", (None, 'quite comfortable'), 'الصفة بأسلوب مهذب مطمئن.']),
    (10, None, ["'شكراً لك على سعة صدرك وصبرك! سيتفقد غراهام القبو على الفور.' نشكر الضيف المتفهم بقولنا", (None, 'for being so patient'), 'قبل وعده بالإصلاح العاجل.']),
    (11, None, ["'تصبحين على خير يا هانا. أراكِ على الفطور.' نستخدم حرف الجر", (None, 'at breakfast'), 'لتحديد اللقاء عند موعد الطعام الصباحي.']),
]
