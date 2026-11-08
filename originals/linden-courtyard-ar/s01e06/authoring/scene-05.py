# Authoring module for linden-courtyard-ar-s01e06-scene-05.
ID = 'linden-courtyard-ar-s01e06-scene-05'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = 'Page Two, Clause Fourteen  (الصفحة الثانية، البند الرابع عشر)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'يفحص كاليب الصفحة الثانية المشبوكة خلف الإشعار ويشير بقلمه إلى البند الرابع عشر من قانون الحي القديم في بورتلاند: لا يجوز تحويل أي مبنى ذي ساحة يتجاوز عمره ثمانين عاماً إلى مكاتب خاصة إذا كان طابقه الأرضي يخدم جيران الحي يومياً! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نقرأ تفاصيل هذا المخرج القانوني الرائع جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'وجد النزل طوق النجاة لعشر سنوات قادمة، وسقطت نظارة آرثر عن أنفه من شدة الفرح! نلتقي في المشهد السادس للاحتفال بالقرار.'
CLOSING = ('hannah', 'Take care!')
STORY = [
    ('arthur', "Look at page one, Caleb: 'commercial office conversion next month.' We are finished!", 'انظر إلى الصفحة الأولى يا كاليب: تحويل إلى مكاتب تجارية في الشهر القادم. لقد انتهى أمرنا!'),
    ('caleb', 'Wait a moment, sir. Did you read page two clipped underneath?', 'انتظر لحظةً يا سيدي. هل قرأتَ الصفحة الثانية المشبوكة في الأسفل؟'),
    ('arthur', 'Only small gray numbers! My heart stopped at page one!', 'مجرد أرقام رمادية صغيرة! لقد توقف قلبي عند الصفحة الأولى!'),
    ('hannah', 'Look where Caleb is pointing with his pencil, Arthur!', 'انظر إلى حيث يشير كاليب بقلمه الرصاص يا آرثر!'),
    ('caleb', 'Clause fourteen of the Portland Old Quarter Act, and my brother outside just nodded!', 'البند الرابع عشر من قانون الحي القديم في بورتلاند، وقد أومأ أخي في الخارج موافقاً للتو!'),
    ('arthur', 'In plain words, please! What does Clause fourteen say?', 'بكلمات واضحة مبسطة من فضلك! ماذا يقول البند الرابع عشر؟'),
    ('caleb', 'No courtyard building over eighty years old may become private offices if the first floor serves neighbors daily.', 'لا يجوز لأي مبنى ذي ساحة يتجاوز عمره ثمانين عاماً أن يتحول إلى مكاتب خاصة إذا كان الطابق الأول يخدم الجيران يومياً.'),
    ('hannah', "'Serves neighbors daily'... like a public morning cafe?!", 'يخدم الجيران يومياً... مثل مقهىً صباحي مفتوح للجمهور؟!'),
    ('caleb', 'Exactly! Right now your four tables only serve overnight hotel guests.', 'بالضبط! في الوقت الحالي تخدم طاولاتكم الأربع نزلاء الفندق المقيمين فقط.'),
    ('arthur', 'Wait, if we open our courtyard gate every morning for neighborhood coffee and bread...', 'مهلاً، إذا فتحنا بوابة ساحتنا كل صباح لقهوة الحي والخبز الطازج...'),
    ('caleb', 'Then your guesthouse lease is protected for another ten years by city law!', 'عندئذٍ يصبح عقد إيجار نزلكم محمياً لعشر سنوات أخرى بقوة قانون المدينة!'),
    ('hannah', 'Arthur! Your glasses just fell off your nose for a happy reason!', 'آرثر! لقد سقطت نظارتك عن أنفك للتو لسبب سعيد!'),
]
WALK = [
    (0, None, ["'انظر إلى الصفحة الأولى يا كاليب: تحويل إلى مكاتب تجارية في الشهر القادم. لقد انتهى أمرنا!' تعبّر صيغة المبالغة", (None, 'We are finished'), 'عن ذروة قلق آرثر قبل معرفة الحقيقة.']),
    (1, None, ["'انتظر لحظةً يا سيدي. هل قرأتَ الصفحة الثانية المشبوكة في الأسفل؟' يأتي اسم المفعول مع الظرف في", (None, 'clipped underneath'), 'للفت النظر إلى الملحق القانوني.']),
    (2, None, ["'مجرد أرقام رمادية صغيرة! لقد توقف قلبي عند الصفحة الأولى!' يصوّر المجاز اليومي", (None, 'My heart stopped at page one'), 'عدم قدرته على إكمال القراءة.']),
    (3, None, ["'انظر إلى حيث يشير كاليب بقلمه الرصاص يا آرثر!' يوجّه التركيب", (None, 'Look where Caleb is pointing'), 'الأنظار كلها إلى السطر الحاسم.']),
    (4, None, ["'البند الرابع عشر من قانون الحي القديم في بورتلاند، وقد أومأ أخي في الخارج موافقاً للتو!' يُقرأ رقم المادة القانونية مفرداً بعد الاسم في", (None, 'Clause fourteen'), 'بلا أداة تعريف.']),
    (5, None, ["'بكلمات واضحة مبسطة من فضلك! ماذا يقول البند الرابع عشر؟' تطلب عبارة", (None, 'In plain words'), 'تبسيط النص القانوني.']),
    (6, None, ["'لا يجوز لأي مبنى ذي ساحة يتجاوز عمره ثمانين عاماً أن يتحول إلى مكاتب خاصة إذا كان الطابق الأول يخدم الجيران يومياً.' في الصياغة القانونية تفيد عبارة النفي مع", (None, 'may become'), 'المنع الرسمي القاطع.']),
    (7, None, ["'يخدم الجيران يومياً... مثل مقهىً صباحي مفتوح للجمهور؟!' تفرّق الصفة", (None, 'public morning cafe'), 'بين الخدمة المغلقة والخدمة المفتوحة للجميع.']),
    (8, None, ["'بالضبط! في الوقت الحالي تخدم طاولاتكم الأربع نزلاء الفندق المقيمين فقط.' تحدد عبارة", (None, 'overnight hotel guests'), 'نطاق الخدمة السابق.']),
    (9, None, ["'مهلاً، إذا فتحنا بوابة ساحتنا كل صباح لقهوة الحي والخبز الطازج...' يرسم الشرط بالمضارع", (None, 'if we open our courtyard gate'), 'مشروع الصباح الجميل.']),
    (10, None, ["'عندئذٍ يصبح عقد إيجار نزلكم محمياً لعشر سنوات أخرى بقوة قانون المدينة!' تجمع صيغة المبني للمجهول", (None, 'is protected for another ten years'), 'الأمان القانوني والاستقرار.']),
    (11, None, ["'آرثر! لقد سقطت نظارتك عن أنفك للتو لسبب سعيد!' تختم عبارة", (None, 'fell off your nose for a happy reason'), 'المشهد بابتسامة دافئة.']),
]
