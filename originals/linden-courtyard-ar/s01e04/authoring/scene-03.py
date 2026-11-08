# Authoring module for linden-courtyard-ar-s01e04-scene-03.
ID = 'linden-courtyard-ar-s01e04-scene-03'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 4
SCENE = 3
TITLE = 'Hot Cinnamon Rolls  (لفائف القرفة الساخنة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'tessa': 'Tessa', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = 'في الطابق السفلي تخرج لفائف القرفة الساخنة من فرن تيسا في اللحظة المناسبة، فيشغل آرثر وتيسا الضيفة المبكرة إيفلين بالشاي الساخن واللفائف الشهية ريثما تعود المياه الساخنة! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نبتسم مع هذا الحوار الصباحي اللطيف جملةً بعد جملة.'
TRANSITION = 'لنستمع الآن مرةً ثانية إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'في تمام السابعة وأربع عشرة دقيقة دخلت هانا راكضةً عبر بوابة الساحة، ونجت خطة الصباح في اللحظة الأخيرة! نلتقي في القبو في المشهد الرابع.'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('evelyn', 'Good morning! Something smells like warm cinnamon all the way upstairs!', 'صباح الخير! تفوح رائحة قرفة دافئة زكية حتى آخر الطابق العلوي!'),
    ('tessa', 'Good morning, Miss Evelyn! My cinnamon rolls just came out of the oven.', 'صباح الخير يا آنسة إيفلين! لقد خرجت لفائف القرفة من الفرن للتو.'),
    ('arthur', "Sit right down by the sunny window, ma'am! No rush to go upstairs yet!", 'تفضّلي بالجلوس هنا بجانب النافذة المشمسة يا سيدتي! لا داعي للعجلة في الصعود بعد!'),
    ('evelyn', 'Actually, I only came down to ask why the bathroom tap felt so chilly.', 'في الواقع، نزلتُ فقط لأسأل لماذا بدا صنبور الحمام بارداً هكذا.'),
    ('arthur', 'Chilly? Ah, yes! Our neighborhood water pipes take a gentle morning stretch!', 'بارداً؟ آه، نعم! أنابيب المياه في حينا تأخذ تمدداً صباحياً لطيفاً!'),
    ('tessa', 'Have a hot cup of tea and a cinnamon roll for ten minutes first!', 'تناولي كوباً ساخناً من الشاي ولفافة قرفة لمدة عشر دقائق أولاً!'),
    ('evelyn', 'Well, nobody wise says no to warm cinnamon bread at seven in the morning.', 'حسناً، لا أحد حكيم يرفض خبز القرفة الدافئ عند السابعة صباحاً.'),
    ('arthur', 'Wonderful choice! Would you like honey or apple jam beside it?', 'اختيار رائع! هل ترغبين في العسل أم مربى التفاح بجانبه؟'),
    ('evelyn', 'Just a little butter, thank you. Why are you looking at your watch, sir?', 'قليل من الزبدة فقط، شكراً لك. لماذا تنظر إلى ساعتك يا سيدي؟'),
    ('arthur', 'Me? Oh, I simply love being on time! Seven fourteen is a beautiful minute!', 'أنا؟ أوه، أنا ببساطة أحب دقة المواعيد! السابعة وأربع عشرة دقيقة لحظة جميلة جداً!'),
    ('tessa', 'Look through the courtyard window, Arthur. Someone just ran through the gate!', 'انظر عبر نافذة الساحة يا آرثر. لقد دخل شخص راكضاً من البوابة للتو!'),
    ('arthur', "Saved! Excuse me one moment, ma'am, enjoy your hot tea!", 'نجونا! اعذريني لحظةً واحدة يا سيدتي، واستمتعي بشايكِ الساخن!'),
]
WALK = [
    (0, None, ["'صباح الخير! تفوح رائحة قرفة دافئة زكية حتى آخر الطابق العلوي!' تعني العبارة", (None, 'all the way upstairs'), 'وصول الرائحة الشهية إلى الطوابق العلوية كلها.']),
    (1, None, ["'صباح الخير يا آنسة إيفلين! لقد خرجت لفائف القرفة من الفرن للتو.' يدل الفعل المركب", (None, 'just came out of'), 'على طزاجة المخبوزات في هذه اللحظة.']),
    (2, None, ["'تفضّلي بالجلوس هنا بجانب النافذة المشمسة يا سيدتي! لا داعي للعجلة في الصعود بعد!' تمنح كلمة", (None, 'Sit right down'), 'ترحيباً حاراً، وتفيد', (None, 'No rush'), 'التأني المريح.']),
    (3, None, ["'في الواقع، نزلتُ فقط لأسأل لماذا بدا صنبور الحمام بارداً هكذا.' تمهد كلمة", (None, 'Actually'), 'لتوضيح السبب الفعلي لنزولها بلطف.']),
    (4, None, ["'بارداً؟ آه، نعم! أنابيب المياه في حينا تأخذ تمدداً صباحياً لطيفاً!' يصوغ آرثر عذراً فكاهياً طريفاً بعبارة", (None, 'take a gentle morning stretch'), 'كأن الأنابيب تستيقظ على مهل.']),
    (5, None, ["'تناولي كوباً ساخناً من الشاي ولفافة قرفة لمدة عشر دقائق أولاً!' يبدأ العرض المضياف بالفعل", (None, 'Have a hot cup of tea'), 'مفضلاً إياه على فعل الشرب المباشر.']),
    (6, None, ["'حسناً، لا أحد حكيم يرفض خبز القرفة الدافئ عند السابعة صباحاً.' في الإنجليزية تأتي الصفة بعد الضمائر المبهمة مباشرةً في", (None, 'nobody wise'), 'وليس قبلها.']),
    (7, None, ["'اختيار رائع! هل ترغبين في العسل أم مربى التفاح بجانبه؟' سؤال الضيافة المهذب", (None, 'Would you like'), 'يخيّر الضيف بلطف بين صنفين على المائدة.']),
    (8, None, ["'قليل من الزبدة فقط، شكراً لك. لماذا تنظر إلى ساعتك يا سيدي؟' يصف المضارع المستمر في", (None, 'Why are you looking at'), 'حركة عيني آرثر القلقة في تلك اللحظة.']),
    (9, None, ["'أنا؟ أوه، أنا ببساطة أحب دقة المواعيد! السابعة وأربع عشرة دقيقة لحظة جميلة جداً!' بعد الفعل", (None, 'love'), 'يأتي المصدر المنتهي بلاحقة الاسمية في', (None, 'being on time'), 'للتعبير عن عادة محببة.']),
    (10, None, ["'انظر عبر نافذة الساحة يا آرثر. لقد دخل شخص راكضاً من البوابة للتو!' يجمع التعبير الحركي", (None, 'ran through the gate'), 'بين سرعة الجري وعبور المدخل.']),
    (11, None, ["'نجونا! اعذريني لحظةً واحدة يا سيدتي، واستمتعي بشايكِ الساخن!' للاستئذان بالانصراف المؤقت نقول بأدب جمّ", (None, 'Excuse me one moment'), 'مع دعاء طيب للضيف.']),
]
