# Authoring module for linden-courtyard-ar-s01e05-scene-05.
ID = 'linden-courtyard-ar-s01e05-scene-05'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = 'Simple Words First  (كلمات بسيطة أولاً)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'قبل الظهر بعشرين دقيقة يجلس كاليب في الساحة متدرباً على خطاب طويل متكلف من تسعة عشر سبباً، فتقنعه هانا بطي الورقة والاكتفاء بثلاث جمل صادقة وبسيطة من القلب. استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نتأمل نصيحة هانا الحكيمة جملةً بعد جملة.'
TRANSITION = 'لنستمع الآن مرةً ثانية إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'طوى كاليب ورقته وحفظ جمله الثلاث الصادقة، ولم يبقَ سوى عشر دقائق على دقات الظهر! نلتقي في المشهد السادس.'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('hannah', 'Here, drink a sip of cool water, Caleb. What is on that paper?', 'تفضّل، اشرب رشفة من الماء المنعش يا كاليب. ماذا في تلك الورقة؟'),
    ('caleb', 'A five minute speech explaining nineteen reasons why we were both wrong in April.', 'خطاب من خمس دقائق يشرح تسعة عشر سبباً جعلنا مخطئين معاً في شهر أبريل.'),
    ('hannah', 'Nineteen reasons?! Are you welcoming your brother or reading a train schedule?', 'تسعة عشر سبباً؟! هل تستقبل أخاك أم تقرأ جدول مواعيد قطارات؟'),
    ('caleb', 'When I get nervous, my sentences grow very long and formal!', 'عندما أتوتر، تصبح جملي طويلة جداً ورسمية!'),
    ('hannah', 'Fold that paper and put it in your pocket right now.', 'اطوِ تلك الورقة وضعها في جيبك الآن فوراً.'),
    ('caleb', 'Without my notes, what do I say when he walks through that gate?', 'من دون ملاحظاتي، ماذا أقول عندما يدخل عبر تلك البوابة؟'),
    ('hannah', "Start with three short sentences. First: 'Hello, Owen, thank you for coming.'", 'ابدأ بثلاث جمل قصيرة. الأولى: مرحباً يا أوين، شكراً لك على مجيئك.'),
    ('caleb', "'Hello, Owen, thank you for coming.' Okay, I can remember that.", 'مرحباً يا أوين، شكراً لك على مجيئك. حسناً، أستطيع تذكر ذلك.'),
    ('hannah', "Second: 'I missed you these three years.'", 'الثانية: لقد اشتقتُ إليك طوال هذه السنوات الثلاث.'),
    ('caleb', "'I missed you these three years.' Honest and clear. And third?", 'لقد اشتقتُ إليك طوال هذه السنوات الثلاث. صادقة وواضحة. والثالثة؟'),
    ('hannah', "'Sit down, there is hot tea and Friday lemon cake.'", 'اجلس، يوجد شاي ساخن وكعكة الليمون ليوم الجمعة.'),
    ('caleb', 'Tea and lemon cake! Hannah, you should open a school for nervous brothers.', 'شاي وكعكة ليمون! هانا، ينبغي أن تفتتحي مدرسة للإخوة المتوترين.'),
]
WALK = [
    (0, None, ["'تفضّل، اشرب رشفة من الماء المنعش يا كاليب. ماذا في تلك الورقة؟' تقدم كلمة", (None, 'Here'), 'الكوب بلطف، وتعني', (None, 'a sip of cool water'), 'جرعة تبلل الريق وتهدئ التوتر.']),
    (1, None, ["'خطاب من خمس دقائق يشرح تسعة عشر سبباً جعلنا مخطئين معاً في شهر أبريل.' يبقى الاسم مفرداً في الصفة المركبة", (None, 'five minute speech'), 'لأنه يتقدم على الاسم الموصوف.']),
    (2, None, ["'تسعة عشر سبباً؟! هل تستقبل أخاك أم تقرأ جدول مواعيد قطارات؟' المقابلة المازحة مع", (None, 'train schedule'), 'تخفف وطأة التوتر بابتسامة ذكية.']),
    (3, None, ["'عندما أتوتر، تصبح جملي طويلة جداً ورسمية!' يعمل الفعلان", (None, 'get nervous'), 'ومعه الفعل', (None, 'grow very long'), 'لبيان التغير التدريجي في الحالة.']),
    (4, None, ["'اطوِ تلك الورقة وضعها في جيبك الآن فوراً.' يجمع الأمر الودود بين", (None, 'Fold that paper'), 'ووضعها جانباً للتحرر من التكلف.']),
    (5, None, ["'من دون ملاحظاتي، ماذا أقول عندما يدخل عبر تلك البوابة؟' بعد أداة الزمان", (None, 'when he walks'), 'تستعمل الإنجليزية المضارع البسيط للدلالة على المستقبل القريب.']),
    (6, None, ["'ابدأ بثلاث جمل قصيرة. الأولى: مرحباً يا أوين، شكراً لك على مجيئك.' يأتي بعد حرف الجر في", (None, 'thank you for coming'), 'الفعل المنتهي بلاحقة الاسمية دائماً.']),
    (7, None, ["'مرحباً يا أوين، شكراً لك على مجيئك. حسناً، أستطيع تذكر ذلك.' تمهّد كلمة الموافقة", (None, 'Okay'), 'لاستعادة الثقة والهدوء.']),
    (8, None, ["'الثانية: لقد اشتقتُ إليك طوال هذه السنوات الثلاث.' يتعدى الفعل الإنجليزي في", (None, 'I missed you'), 'إلى المخاطَب مباشرةً بلا حرف جر.']),
    (9, None, ["'لقد اشتقتُ إليك طوال هذه السنوات الثلاث. صادقة وواضحة. والثالثة؟' تلخص الصفتان", (None, 'Honest and clear'), 'سر قوة الكلمات البسيطة.']),
    (10, None, ["'اجلس، يوجد شاي ساخن وكعكة الليمون ليوم الجمعة.' تدعو عبارة", (None, 'Sit down'), 'إلى الراحة قبل أي نقاش طويل.']),
    (11, None, ["'شاي وكعكة ليمون! هانا، ينبغي أن تفتتحي مدرسة للإخوة المتوترين.' تفيد صيغة", (None, 'you should open'), 'الثناء المرح على حكمتها.']),
]
