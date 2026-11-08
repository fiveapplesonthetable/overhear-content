# Authoring module for linden-courtyard-ar-s01e01-scene-03.
ID = 'linden-courtyard-ar-s01e01-scene-03'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Where Are My Glasses?  (أين نظّارتي؟)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'يدخل آرثر صاحب النزل مسرعاً وهو قلق بشأن وصول ضيفة الغرفة الرابعة اليوم، ويبحث في كل مكان عن نظارته دون أن ينتبه إلى مكانها الطريف. استمع إلى المشهد كاملاً باللغة الإنجليزية.'
OPENER = 'لنراجع الآن تفاصيل هذا الموقف الطريف جملةً فجملة.'
TRANSITION = 'لنستمع الآن إلى المشهد كاملاً مرةً أخرى.'
OUTRO = 'وجد آرثر نظارته فوق جبينه أخيراً، وتوقفت سيارة أجرة صفراء عند البوابة الخارجية معلنةً وصول أول ضيفة. إلى اللقاء في المشهد التالي.'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('arthur', 'Good morning, everyone! Welcome, Hannah. Is everything ready?', 'صباح الخير جميعاً! أهلاً بكِ يا هانا. هل كل شيء جاهز؟'),
    ('hannah', 'Good morning! Yes, the desk is clean and the keys are ready.', 'صباح الخير! نعم، المكتب نظيف والمفاتيح جاهزة.'),
    ('arthur', "Today's guest in room four is staying all week. Everything must be perfect!", 'ضيفة اليوم في الغرفة الرابعة ستقيم طوال الأسبوع. يجب أن يكون كل شيء مثالياً!'),
    ('graham', 'Relax, Arthur. The room is clean and the towels are fresh.', 'اهدأ يا آرثر. الغرفة نظيفة والمناشف طازجة ونظيفة.'),
    ('arthur', 'I need to read the reservation book, but I cannot find my glasses!', 'أحتاج إلى قراءة دفتر الحجوزات، لكنني لا أستطيع العثور على نظارتي!'),
    ('hannah', 'Are they in your coat pocket?', 'هل هي في جيب معطفك؟'),
    ('arthur', 'No, only my pen and three old receipts!', 'لا، لا يوجد سوى قلمي وثلاثة إيصالات قديمة!'),
    ('graham', 'Look in the mirror behind the desk, boss.', 'انظر في المرآة خلف المكتب يا مدير.'),
    ('arthur', 'Why would my glasses be in the... oh! They are on my head!', 'ولماذا ستكون نظارتي في... أوه! إنها فوق رأسي!'),
    ('hannah', 'Right there on your forehead, safe and sound.', 'ها هي ذي على جبينك تماماً، سالمة وآمنة.'),
    ('arthur', 'Do not tell anyone! Now, smile brightly when the bell rings.', 'لا تخبروا أحداً! والآن ابتسموا بإشراق عندما يرن الجرس.'),
    ('graham', 'Here comes a taxi at the gate right now.', 'ها هي سيارة أجرة تصل إلى البوابة الآن.'),
]
WALK = [
    (0, None, ["'صباح الخير جميعاً! أهلاً بكِ يا هانا. هل كل شيء جاهز؟' يطرح آرثر سؤاله السريع", (None, 'Is everything ready'), 'بفعل مفرد لأن ضمائر الشمول تعامل معاملة المفرد دائماً.']),
    (1, None, ["'صباح الخير! نعم، المكتب نظيف والمفاتيح جاهزة.' قارن بين المفرد في", (None, 'the desk is clean'), 'وبين الجمع في', (None, 'the keys are ready'), 'لتلاحظ تغير فعل الكينونة.']),
    (2, None, ["'ضيفة اليوم في الغرفة الرابعة ستقيم طوال الأسبوع. يجب أن يكون كل شيء مثالياً!' للتعبير عن اللزوم القوي يستعمل آرثر", (None, 'Everything must be perfect'), 'مستعيناً بفعل الوجوب متبوعاً بالمصدر.']),
    (3, None, ["'اهدأ يا آرثر. الغرفة نظيفة والمناشف طازجة ونظيفة.' تبدأ التهدئة الودودة بكلمة واحدة هي", (None, 'Relax'), 'لطمأنة آرثر بأن الترتيبات مكتملة.']),
    (4, None, ["'أحتاج إلى قراءة دفتر الحجوزات، لكنني لا أستطيع العثور على نظارتي!' لاحظ الجمع بين", (None, 'cannot find'), 'واسم الجمع الدائم', (None, 'my glasses'), 'لأن النظارة ذات عدستين.']),
    (5, None, ["'هل هي في جيب معطفك؟' تسأل هانا بصيغة الجمع", (None, 'Are they'), 'عوداً على النظارة، وتسبق كلمة المعطف كلمة الجيب في', (None, 'coat pocket'), 'لتحديد نوعه.']),
    (6, None, ["'لا، لا يوجد سوى قلمي وثلاثة إيصالات قديمة!' تفيد كلمة الحصر", (None, 'only my pen'), 'عدم وجود أي غرض آخر سوى القلم والإيصالات.']),
    (7, None, ["'انظر في المرآة خلف المكتب يا مدير.' حرف الجر المعتاد مع النظر في المرآة هو", (None, 'Look in the mirror'), 'متبوعاً بمكانها خلف المكتب.']),
    (8, None, ["'ولماذا ستكون نظارتي في... أوه! إنها فوق رأسي!' ما إن يلمح آرثر انعكاسه حتى يهتف", (None, 'They are on my head'), 'مستعملاً حرف الجر الدال على ملامسة السطح.']),
    (9, None, ["'ها هي ذي على جبينك تماماً، سالمة وآمنة.' الثنائية الإنجليزية الشائعة", (None, 'safe and sound'), 'تقال بطرافة وارتياح عند العثور على غرض مفقود.']),
    (10, None, ["'لا تخبروا أحداً! والآن ابتسموا بإشراق عندما يرن الجرس.' يبنى النهي المهذب أو العاجل بـ", (None, 'Do not tell anyone'), 'قبل الفعل المجرد مباشرةً.']),
    (11, None, ["'ها هي سيارة أجرة تصل إلى البوابة الآن.' للفت الانتباه إلى قدوم شيء أمام العين نقول", (None, 'Here comes a taxi'), 'بتقديم ظرف المكان في مطلع العبارة.']),
]
