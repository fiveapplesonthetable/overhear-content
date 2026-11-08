# Authoring module for linden-courtyard-ar-s01e05-scene-06.
ID = 'linden-courtyard-ar-s01e05-scene-06'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = 'Ten Minutes to Twelve  (عشر دقائق قبل الثانية عشرة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'في الحادية عشرة وخمسين دقيقة يسلّم ساعي البريد مظروفاً سميكاً مختوماً بختم أحمر رسمي باسم مالك المبنى، فيضعه آرثر جانباً ريثما تدق ساعة الكنيسة الثانية عشرة ظهراً. استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'لنتابع الآن الدقائق الأخيرة قبل الظهر جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'بدأت ساعة الكنيسة في آخر الشارع تدق الثانية عشرة، وتوجهت الأنظار كلها نحو البوابة الحديدية! نلتقي في المشهد السابع.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'How does my tie look today, Hannah? Zero orange juice in sight!', 'كيف تبدو ربطة عنقي اليوم يا هانا؟ لا أثر لأي عصير برتقال في الأفق!'),
    ('hannah', 'Sharp and spotless, Arthur! Even your glasses are on your nose instead of your forehead.', 'أنيقة وناصعة النظافة يا آرثر! بل إن نظارتك فوق أنفك بدلاً من جبهتك.'),
    ('arthur', 'Progress! Today our courtyard hosts a family reunion. Quiet dignity from everyone!', 'هذا تقدم! اليوم تستضيف ساحتنا لمّ شمل عائلياً. نريد وقاراً هادئاً من الجميع!'),
    ('tessa', 'Says the man peeking through the lace curtain every thirty seconds!', 'يقول هذا الرجل الذي يختلس النظر من خلف ستارة الدانتيل كل ثلاثين ثانية!'),
    ('arthur', 'I am checking the weather, Tessa! Who left this thick envelope by the bell?', 'أنا أتفقد حالة الطقس يا تيسا! من ترك هذا المظروف السميك بجانب الجرس؟'),
    ('hannah', 'The mailman just asked me to sign for it. It has a red property office stamp.', 'طلب مني ساعي البريد للتو التوقيع لاستلامه. عليه ختم أحمر من مكتب العقارات.'),
    ('arthur', "From the building landlord's lawyer? Strange, our rent is paid until next summer.", 'من محامي مالك المبنى؟ أمر غريب، فإيجارنا مدفوع حتى الصيف القادم.'),
    ('tessa', 'Open it after twelve, boss! Look at the clock: five minutes to noon!', 'افتحه بعد الثانية عشرة يا مدير! انظر إلى الساعة: بقيت خمس دقائق على الظهر!'),
    ('arthur', 'Right you are. Paperwork can wait. Put it beside the book for now.', 'معكِ كل الحق. يمكن للمعاملات الورقية أن تنتظر. ضعيه بجانب الدفتر في الوقت الحالي.'),
    ('hannah', "I placed the blue suitcase right beside Caleb's table under the tree.", 'وضعتُ الحقيبة الزرقاء بجانب طاولة كاليب مباشرةً تحت الشجرة.'),
    ('tessa', 'And the teapot is hot! Everybody step back from the window!', 'وإبريق الشاي ساخن! تراجعوا جميعاً خطوةً عن النافذة!'),
    ('arthur', 'Listen... the church clock down the street is starting to chime twelve!', 'أنصتوا... لقد بدأت ساعة الكنيسة في آخر الشارع تدق الثانية عشرة!'),
]
WALK = [
    (0, None, ["'كيف تبدو ربطة عنقي اليوم يا هانا؟ لا أثر لأي عصير برتقال في الأفق!' تجمع المزحة اللطيفة بين", (None, 'Zero orange juice in sight'), 'وذكريات الصباح الأول.']),
    (1, None, ["'أنيقة وناصعة النظافة يا آرثر! بل إن نظارتك فوق أنفك بدلاً من جبهتك.' تمدح الصفتان", (None, 'Sharp and spotless'), 'هندام آرثر المرتب.']),
    (2, None, ["'هذا تقدم! اليوم تستضيف ساحتنا لمّ شمل عائلياً. نريد وقاراً هادئاً من الجميع!' الفعل", (None, 'hosts a family reunion'), 'يرتقي بالمناسبة في عيني آرثر.']),
    (3, None, ["'يقول هذا الرجل الذي يختلس النظر من خلف ستارة الدانتيل كل ثلاثين ثانية!' يفتتح التعليق المرح بـ", (None, 'Says the man peeking'), 'لكشف فضوله الودود.']),
    (4, None, ["'أنا أتفقد حالة الطقس يا تيسا! من ترك هذا المظروف السميك بجانب الجرس؟' يتذرع آرثر بعبارة", (None, 'checking the weather'), 'ثم يسأل عن الرسالة المسجلة.']),
    (5, None, ["'طلب مني ساعي البريد للتو التوقيع لاستلامه. عليه ختم أحمر من مكتب العقارات.' تعني العبارة البريدية", (None, 'sign for it'), 'البريد المسجل الرسمي.']),
    (6, None, ["'من محامي مالك المبنى؟ أمر غريب، فإيجارنا مدفوع حتى الصيف القادم.' تتتابع ياء وسين الملكية في", (None, "the building landlord's lawyer"), 'لربط الصفة المهنية بصاحب العقار.']),
    (7, None, ["'افتحه بعد الثانية عشرة يا مدير! انظر إلى الساعة: بقيت خمس دقائق على الظهر!' تُقرأ الدقائق المتبقية بحرف الجر في", (None, 'five minutes to noon'), 'بإيجاز واضح.']),
    (8, None, ["'معكِ كل الحق. يمكن للمعاملات الورقية أن تنتظر. ضعيه بجانب الدفتر في الوقت الحالي.' تفيد عبارة التأييد", (None, 'Right you are'), 'موافقةً فورية دافئة.']),
    (9, None, ["'وضعتُ الحقيبة الزرقاء بجانب طاولة كاليب مباشرةً تحت الشجرة.' الفعل المهذب الدقيق", (None, 'placed'), 'يناسب ترتيب المكان للمناسبة.']),
    (10, None, ["'وإبريق الشاي ساخن! تراجعوا جميعاً خطوةً عن النافذة!' يوجّه النداء المرح", (None, 'Everybody step back'), 'إلى ترك الخصوصية للشقيقين.']),
    (11, None, ["'أنصتوا... لقد بدأت ساعة الكنيسة في آخر الشارع تدق الثانية عشرة!' يصف الفعل", (None, 'to chime twelve'), 'رنين أجراس الساعات الكبيرة.']),
]
