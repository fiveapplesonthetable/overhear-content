# Authoring module for linden-courtyard-ar-s01e06-scene-03.
ID = 'linden-courtyard-ar-s01e06-scene-03'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = 'Thirty Days on Paper  (ثلاثون يوماً على الورق)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'خلف مكتب الاستقبال يتحسر آرثر على إشعار الثلاثين يوماً، غير أن غراهام وهانا يذكرانه بوجود الصفحة الثانية المشبوكة خلف الرسالة وبأن كاليب الجالس في الساحة خبير بقوانين المباني التراثية في بورتلاند! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نتابع كيف يتحول القلق إلى تفكير عملي جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'في اللحظة نفسها عادت تيسا من طاولة الشقيقين ومعها مفاجأة غير متوقعة! نلتقي في المشهد الرابع.'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('arthur', 'Fifteen years of polishing brass keys and straightening ties... gone in thirty days!', 'خمسة عشر عاماً من تلميع المفاتيح النحاسية وتسوية ربطات العنق... تضيع في ثلاثين يوماً!'),
    ('graham', 'Stop burying us before we read the whole document, Arthur.', 'توقف عن نعينا قبل أن نقرأ الوثيقة كاملةً يا آرثر.'),
    ('hannah', 'Yes! Earlier I noticed a second page clipped behind the cover letter.', 'نعم! لاحظتُ في وقت سابق صفحة ثانية مشبوكة خلف الرسالة التعريفية.'),
    ('arthur', 'Legal paragraphs give me a headache even with two pairs of glasses!', 'الفقرات القانونية تصيبني بالصداع حتى مع نظارتين اثنتين!'),
    ('graham', 'This house survived eighty winters and one broken boiler valve yesterday.', 'صمد هذا البيت ثمانين شتاءً وتجاوز صمام غلاية مكسوراً يوم أمس.'),
    ('hannah', 'Wait, who is sitting ten meters away in our courtyard right now?', 'انتظروا، من يجلس على بُعد عشرة أمتار في ساحتنا الآن تماماً؟'),
    ('arthur', 'Two brothers eating lemon cake?', 'شقيقان يأكلان كعكة الليمون؟'),
    ('hannah', 'An architect who works with historic courtyard buildings all over Portland!', 'مهندس معماري يعمل في مباني الساحات التاريخية في أنحاء بورتلاند كلها!'),
    ('graham', 'Smart thinking, Hannah. Caleb reads city building rules every single week.', 'تفكير ذكي يا هانا. يقرأ كاليب لوائح البناء في المدينة كل أسبوع.'),
    ('arthur', 'Oh, I could never bother a paying guest with our landlord troubles!', 'أوه، لا يمكنني أبداً أن أزعج ضيفاً يدفع أجرة إقامته بمشكلات مالك العقار!'),
    ('hannah', 'After we guarded his blue suitcase all week? He will want to help!', 'بعد أن حرسنا حقيبته الزرقاء طوال الأسبوع؟ سيرغب هو نفسه في المساعدة!'),
    ('graham', 'Wait, here comes Tessa back from their table right now.', 'انتظروا، ها هي تيسا عائدة من طاولتهما في هذه اللحظة.'),
]
WALK = [
    (0, None, ["'خمسة عشر عاماً من تلميع المفاتيح النحاسية وتسوية ربطات العنق... تضيع في ثلاثين يوماً!' يأتي بعد حرف الجر اسما الفعل في", (None, 'polishing brass keys and straightening ties'), 'لتلخيص رحلة العمر.']),
    (1, None, ["'توقف عن نعينا قبل أن نقرأ الوثيقة كاملةً يا آرثر.' يستعمل غراهام المجاز الطريف", (None, 'Stop burying us'), 'لرفض الاستسلام قبل التثبت.']),
    (2, None, ["'نعم! لاحظتُ في وقت سابق صفحة ثانية مشبوكة خلف الرسالة التعريفية.' يحدد المصطلح الإداري", (None, 'cover letter'), 'الورقة الأولى من المعاملة.']),
    (3, None, ["'الفقرات القانونية تصيبني بالصداع حتى مع نظارتين اثنتين!' يُقال بالاصطلاح اليومي", (None, 'give me a headache'), 'للنصوص المعقدة المرهقة.']),
    (4, None, ["'صمد هذا البيت ثمانين شتاءً وتجاوز صمام غلاية مكسوراً يوم أمس.' يتعدى الفعل", (None, 'survived eighty winters'), 'إلى الشدائد والسنين مباشرةً بلا حرف جر.']),
    (5, None, ["'انتظروا، من يجلس على بُعد عشرة أمتار في ساحتنا الآن تماماً؟' تقاس المسافة القصيرة بقول", (None, 'ten meters away'), 'لتذكيرهم بقرب الحل.']),
    (6, None, ["'شقيقان يأكلان كعكة الليمون؟' تصف العبارة النعتية المختصرة", (None, 'eating lemon cake'), 'ما يراه آرثر بظاهر العين.']),
    (7, None, ["'مهندس معماري يعمل في مباني الساحات التاريخية في أنحاء بورتلاند كلها!' تعني عبارة", (None, 'all over Portland'), 'شمول خبرته للمدينة بأسرها.']),
    (8, None, ["'تفكير ذكي يا هانا. يقرأ كاليب لوائح البناء في المدينة كل أسبوع.' الإشادة السريعة", (None, 'Smart thinking'), 'تُقال لتثمين الاقتراح الموفق.']),
    (9, None, ["'أوه، لا يمكنني أبداً أن أزعج ضيفاً يدفع أجرة إقامته بمشكلات مالك العقار!' يصف المركب", (None, 'a paying guest'), 'أخلاقيات آرثر الفندقية الرفيعة.']),
    (10, None, ["'بعد أن حرسنا حقيبته الزرقاء طوال الأسبوع؟ سيرغب هو نفسه في المساعدة!' يؤكد المستقبل في", (None, 'He will want to help'), 'ثقة هانا برد الجميل.']),
    (11, None, ["'انتظروا، ها هي تيسا عائدة من طاولتهما في هذه اللحظة.' يقدم التركيب الإشاري", (None, 'here comes Tessa'), 'الشخص المقترب أمام الأنظار.']),
]
