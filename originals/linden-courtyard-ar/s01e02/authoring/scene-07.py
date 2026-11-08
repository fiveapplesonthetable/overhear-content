# Authoring module for linden-courtyard-ar-s01e02-scene-07.
ID = 'linden-courtyard-ar-s01e02-scene-07'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = 'How Regulars Order  (كيف يطلب الزبائن الدائمون)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'في فترة الهدوء بعد الظهر، تجلس تيسا مع هانا لشرب القهوة والتقاط الأنفاس، بينما يصلح غراهام برغياً مرتخياً في كرسي الزاوية بمفكه الذي لا يفارقه. استمع إلى المشهد كاملاً باللغة الإنجليزية.'
OPENER = 'لنستعرض الآن جمل هذه الاستراحة الودودة خطوةً بخطوة.'
TRANSITION = 'لنستمع الآن إلى الحوار متصلاً مرةً أخرى.'
OUTRO = 'استمتع الثلاثة باستراحة القهوة الدافئة وضحكوا على فضول غراهام الخفي، غير أن المساء يحمل مشكلة غير متوقعة في دفتر الحجوزات! نلتقي في المشهد الأخير.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('tessa', 'Sit down, Hannah! You ran half the city this morning, drink some coffee.', 'اجلسي يا هانا! لقد ركضتِ نصف المدينة هذا الصباح، اشربي بعض القهوة.'),
    ('hannah', 'Gladly! With milk and a little sugar, please.', 'بكل سرور! مع الحليب وقليل من السكر من فضلك.'),
    ('graham', 'Watch that corner chair, wait ten seconds while I tighten this screw.', 'انتبهي لكرسي الزاوية ذاك، انتظري عشر ثوانٍ ريثما أشد هذا البرغي.'),
    ('hannah', 'Done already? You carry a screwdriver everywhere, Graham!', 'أانتهيتَ بهذه السرعة؟ أنت تحمل مفك براغٍ في كل مكان يا غراهام!'),
    ('graham', 'Old houses loosen one screw every Tuesday. Now sit.', 'البيوت القديمة ترخي برغياً واحداً كل يوم ثلاثاء. والآن اجلسي.'),
    ('tessa', 'Look, you survived the breakfast rush and the mystery phone call!', 'انظري، لقد اجتزتِ زحمة الفطور والمكالمة الهاتفية الغامضة بنجاح!'),
    ('hannah', 'Honestly, I like it here much better than my old gray office.', 'بصراحة، أنا أحب العمل هنا أكثر بكثير من مكتبي الرمادي القديم.'),
    ('tessa', 'Wait until Friday at noon, I want a front row seat when the suitcase man walks in!', 'انتظروا حتى ظهر يوم الجمعة، أريد مقعداً في الصف الأمامي حين يدخل صاحب الحقيبة!'),
    ('graham', 'Nobody stares at guests. We hand over the bag and mind our business.', 'لا أحد يحدق في الضيوف. نحن نسلم الحقيبة ونهتم بشؤون عملنا.'),
    ('tessa', 'Listen to him! Graham is twice as curious as we are!', 'اسمعي كلامه! غراهام متشوق للفضول ضعفينا نحن الاثنتين!'),
    ('graham', 'I am simply checking security. That is my job.', 'أنا أتحقق من الأمن فحسب. هذا هو عملي.'),
    ('hannah', 'Sure, Graham, your secret is safe with us!', 'طبعاً يا غراهام، سرك في بئر أمينة معنا!'),
]
WALK = [
    (0, None, ["'اجلسي يا هانا! لقد ركضتِ نصف المدينة هذا الصباح، اشربي بعض القهوة.' المبالغة الودودة اللطيفة في", (None, 'ran half the city'), 'تشيد بمجهود هانا الكبير في الصباح.']),
    (1, None, ["'بكل سرور! مع الحليب وقليل من السكر من فضلك.' كلمة القبول المبهجة", (None, 'Gladly'), 'تليها عبارة الكمية الصغيرة لغير المعدود', (None, 'a little sugar'), 'بأدب جم.']),
    (2, None, ["'انتبهي لكرسي الزاوية ذاك، انتظري عشر ثوانٍ ريثما أشد هذا البرغي.' تربط أداة التزامن في", (None, 'while I tighten this screw'), 'بين الانتظار القصير وإصلاح الكرسي.']),
    (3, None, ["'أانتهيتَ بهذه السرعة؟ أنت تحمل مفك براغٍ في كل مكان يا غراهام!' السؤال المقتضب المتعجب", (None, 'Done already'), 'يعبر عن الإعجاب بالمهارة الخاطفة.']),
    (4, None, ["'البيوت القديمة ترخي برغياً واحداً كل يوم ثلاثاء. والآن اجلسي.' مع التكرار الأسبوعي المنتظم نقول", (None, 'every Tuesday'), 'بصيغة المفرد بعد أداة التوزيع.']),
    (5, None, ["'انظري، لقد اجتزتِ زحمة الفطور والمكالمة الهاتفية الغامضة بنجاح!' يصور التعبير المرح", (None, 'survived the breakfast rush'), 'ضغط العمل الصباحي بروح خفيفة.']),
    (6, None, ["'بصراحة، أنا أحب العمل هنا أكثر بكثير من مكتبي الرمادي القديم.' لتقوية المفاضلة نضع كلمة الكثرة قبل صيغة التفضيل في", (None, 'much better than'), 'فتبدو المقارنة صادقة.']),
    (7, None, ["'انتظروا حتى ظهر يوم الجمعة، أريد مقعداً في الصف الأمامي حين يدخل صاحب الحقيبة!' استعارة المسرح الطريفة", (None, 'a front row seat'), 'تعبر عن شدة الحماس لرؤية المشهد.']),
    (8, None, ["'لا أحد يحدق في الضيوف. نحن نسلم الحقيبة ونهتم بشؤون عملنا.' يجمع غراهام بين", (None, 'hand over the bag'), 'وبين العبارة الشهيرة', (None, 'mind our business'), 'بنبرة جدية مصطنعة.']),
    (9, None, ["'اسمعي كلامه! غراهام متشوق للفضول ضعفينا نحن الاثنتين!' تبنى مضاعفة الصفة في الإنجليزية عبر تركيب التساوي المسبوق بالضعف في", (None, 'twice as curious as'), 'بصورة سلسة.']),
    (10, None, ["'أنا أتحقق من الأمن فحسب. هذا هو عملي.' يخفف الظرف الهادئ", (None, 'simply checking security'), 'دفاع غراهام اللطيف عن نفسه.']),
    (11, None, ["'طبعاً يا غراهام، سرك في بئر أمينة معنا!' العبارة الختامية الدافئة", (None, 'your secret is safe with us'), 'تختم المزاح بابتسامة ودودة.']),
]
