# Authoring module for linden-courtyard-ar-s01e06-scene-07.
ID = 'linden-courtyard-ar-s01e06-scene-07'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 6
SCENE = 7
TITLE = 'Under the Golden Lanterns  (تحت الفوانيس الذهبية)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'owen': 'Owen'}
INTRO = 'مع حلول المساء تتلألأ الفوانيس الورقية الذهبية فوق ساحة الزيزفون، فيجتمع أوين وإيفلين وهانا متأملين كيف قادت حقيبة زرقاء أُخذت خطأً من الرصيف الثاني إلى مصالحة شقيقين وإنقاذ النزل! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نستمتع بهدوء هذه الأمسية الساحرة جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'أمسية هادئة دافئة تحت الفوانيس الذهبية... غير أن قبو النزل لا يزال يخبئ سراً أخيراً في المشهد الثامن! نلتقي بعد لحظات.'
CLOSING = ('evelyn', 'Good night!')
STORY = [
    ('evelyn', 'Look up at those golden lanterns against the evening sky. How peaceful!', 'انظروا إلى الأعلى نحو تلك الفوانيس الذهبية قبالة سماء المساء. يا للسكينة!'),
    ('owen', 'To think on Monday morning Caleb picked up the wrong blue bag on Platform Two.', 'من يتخيل أن كاليب التقط في صباح الاثنين الحقيبة الزرقاء الخاطئة على الرصيف الثاني.'),
    ('hannah', 'If he had picked up the right bag, none of us would be standing here tonight!', 'لو أنه التقط الحقيبة الصحيحة، لما كان أحد منا واقفاً هنا هذه الليلة!'),
    ('evelyn', 'My teacup survived, two brothers made peace, and Hannah found a new home.', 'نجا فنجان الشاي الخاص بي، وتصالح شقيقان، ووجدت هانا بيتاً جديداً.'),
    ('owen', 'Miss Evelyn, Caleb and I booked a quiet dinner nearby. Will you join us tomorrow?', 'آنسة إيفلين، حجزتُ أنا وكاليب عشاءً هادئاً في الجوار. هل تنضمين إلينا غداً؟'),
    ('evelyn', 'Gladly, Owen, as long as nobody talks about selling old pianos!', 'بكل سرور يا أوين، ما دام لا أحد يتحدث عن بيع أجهزة البيانو القديمة!'),
    ('hannah', 'And tomorrow morning at eight, your first courtyard coffees are on the house!', 'وفي صباح الغد عند الثامنة، قهوتكم الأولى في الساحة ضيافةٌ على حساب النزل!'),
    ('owen', "We will bring half of City Hall to Tessa's tables next week, I promise.", 'سنحضر نصف موظفي دار البلدية إلى طاولات تيسا في الأسبوع القادم، أعدكم بذلك.'),
    ('evelyn', 'Listen, even the buzzer from room four has been quiet all evening!', 'أنصتوا، حتى الجرس الكهربائي للغرفة الرابعة ظل هادئاً طوال المساء!'),
    ('hannah', 'Do not tempt it, Miss Evelyn! I am almost fond of those two rings now.', 'لا تستفزيه يا آنسة إيفلين! لقد كدتُ أولع بهاتين الرنتين الآن.'),
    ('owen', 'Here is to the Linden Courtyard Inn, the loudest quiet place in Portland!', 'تحيةً لنزل ساحة الزيزفون، أكثر الأماكن الهادئة صخباً بالحياة في بورتلاند!'),
    ('hannah', 'To good neighbors, warm bread, and open gates!', 'تحيةً للجيران الطيبين، والخبز الدافئ، والبوابات المفتوحة!'),
]
WALK = [
    (0, None, ["'انظروا إلى الأعلى نحو تلك الفوانيس الذهبية قبالة سماء المساء. يا للسكينة!' يصوّر حرف الجر", (None, 'against the evening sky'), 'تباين الضوء الدافئ مع زرقة الغروب.']),
    (1, None, ["'من يتخيل أن كاليب التقط في صباح الاثنين الحقيبة الزرقاء الخاطئة على الرصيف الثاني.' يفتتح المصدر التاملي", (None, 'To think'), 'استرجاع المصادفة الأولى.']),
    (2, None, ["'لو أنه التقط الحقيبة الصحيحة، لما كان أحد منا واقفاً هنا هذه الليلة!' يجمع الشرط الامتناعي بين", (None, 'If he had picked up'), 'في الماضي وبين النتيجة الحالية.']),
    (3, None, ["'نجا فنجان الشاي الخاص بي، وتصالح شقيقان، ووجدت هانا بيتاً جديداً.' تعني العبارة الاصطلاحية", (None, 'made peace'), 'عودة المودة الصافية.']),
    (4, None, ["'آنسة إيفلين، حجزتُ أنا وكاليب عشاءً هادئاً في الجوار. هل تنضمين إلينا غداً؟' يتعدى فعل الدعوة في", (None, 'Will you join us tomorrow'), 'إلى الضمير مباشرةً بلا حرف جر.']),
    (5, None, ["'بكل سرور يا أوين، ما دام لا أحد يتحدث عن بيع أجهزة البيانو القديمة!' تربط أداة الشرط اللطيفة", (None, 'as long as'), 'القبول بمزحة محببة.']),
    (6, None, ["'وفي صباح الغد عند الثامنة، قهوتكم الأولى في الساحة ضيافةٌ على حساب النزل!' العبارة الشهيرة في المقاهي والفنادق", (None, 'on the house'), 'تعبر عن الكرم والاحتفال.']),
    (7, None, ["'سنحضر نصف موظفي دار البلدية إلى طاولات تيسا في الأسبوع القادم، أعدكم بذلك.' يختم الفعل", (None, 'I promise'), 'الجملة بتأكيد ودي صادق.']),
    (8, None, ["'أنصتوا، حتى الجرس الكهربائي للغرفة الرابعة ظل هادئاً طوال المساء!' يشير المضارع التام", (None, 'has been quiet all evening'), 'إلى سكون الجرس المعتاد.']),
    (9, None, ["'لا تستفزيه يا آنسة إيفلين! لقد كدتُ أولع بهاتين الرنتين الآن.' تُقال عبارة", (None, 'Do not tempt it'), 'بطرافة، وتفيد', (None, 'fond of'), 'نشوء الألفة مع تفاصيل المكان.']),
    (10, None, ["'تحيةً لنزل ساحة الزيزفون، أكثر الأماكن الهادئة صخباً بالحياة في بورتلاند!' تفتتح عبارة الاحتفاء", (None, 'Here is to'), 'كلمات التقدير في المناسبات السعيدة.']),
    (11, None, ["'تحيةً للجيران الطيبين، والخبز الدافئ، والبوابات المفتوحة!' تكمل هانا التحية بحرف الجر", (None, 'To good neighbors'), 'في ختام دافئ يجمع روح القصة.']),
]
