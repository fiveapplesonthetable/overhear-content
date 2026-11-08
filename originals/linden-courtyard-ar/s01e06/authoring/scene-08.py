# Authoring module for linden-courtyard-ar-s01e06-scene-08.
ID = 'linden-courtyard-ar-s01e06-scene-08'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = 'Room Nine  (الغرفة التاسعة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = 'بينما يحضر غراهام كراسي المقهى الإضافية من خلف غرفة الغلاية، يعثر خلف جدار طوبي قديم على صندوق صغير من خشب الأرز منقوش على لوحته النحاسية الغرفة التاسعة ومعه مفتاح نحاسي تاسع ومخطط لباب مخفي! استمع إلى المشهد الختامي للموسم الأول باللغة الإنجليزية.'
OPENER = 'دعنا نستكشف هذا اللغز المعماري المشوق في ختام الموسم جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد الختامي كاملاً بالسرعة الطبيعية.'
OUTRO = 'مفتاح نحاسي تاسع وباب مخفي مرسوم على مخطط الطابق الأرضي... هكذا انتهى أسبوع هانا الأول وبدأت مغامرة جديدة في نزل ساحة الزيزفون! تهانينا على إتمام الموسم الأول كاملاً، وإلى اللقاء!'
CLOSING = ('graham', 'Until tomorrow!')
STORY = [
    ('hannah', 'Did you find the three folding chairs behind the boiler room, Graham?', 'هل وجدتَ الكراسي الثلاثة القابلة للطي خلف غرفة الغلاية يا غراهام؟'),
    ('graham', 'Found the chairs, and behind an old brick wall, I found this.', 'وجدتُ الكراسي، وخلف جدار طوبي قديم وجدتُ هذا.'),
    ('arthur', 'A small cedar chest? I have never seen that box in fifteen years!', 'صندوق صغير من خشب الأرز؟ لم أرَ ذلك الصندوق قط طوال خمسة عشر عاماً!'),
    ('hannah', 'Brush the dust off the brass plate on top... wait, read that number!', 'امسح الغبار عن اللوحة النحاسية في الأعلى... انتظر، اقرأ ذلك الرقم!'),
    ('arthur', "Let me pull my glasses down from my forehead... 'Room Nine'?!", 'دعوني أنزل نظارتي من فوق جبهتي... الغرفة التاسعة؟!'),
    ('hannah', 'Graham, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!', 'غراهام، انظر إلى لوحة المفاتيح الخشبية خلفنا: واحد، اثنان، ثلاثة، أربعة، خمسة، ستة، سبعة، ثمانية!'),
    ('arthur', 'This guesthouse has only ever had eight rooms! Where on earth is Room Nine?!', 'لم يضم هذا النزل في تاريخه قط سوى ثماني غرف! أين بحق السماء تقع الغرفة التاسعة؟!'),
    ('graham', 'Listen when I tilt the box. Something metal just slid inside.', 'أنصتوا عندما أميل الصندوق. لقد انزلق شيء معدني في الداخل للتو.'),
    ('hannah', 'There is a tiny keyhole on the front latch, and look taped underneath: an old brass key!', 'يوجد ثقب مفتاح صغير جداً على المزلاج الأمامي، وانظروا إلى ما أُلصق في الأسفل: مفتاح نحاسي قديم!'),
    ('arthur', 'A ninth brass key?! Do we open it tonight or wait until morning?!', 'مفتاح نحاسي تاسع؟! أنفتحه هذه الليلة أم ننتظر حتى الصباح؟!'),
    ('graham', 'Look at the folded blueprint sticking out of the hinge. There is a hidden door drawn on this floor!', 'انظروا إلى المخطط الهندسي المطوي البارز من عند المفصلة. هناك باب مخفي مرسوم في هذا الطابق!'),
    ('hannah', 'Grab the flashlight, both of you. My second week starts right now!', 'أمسكا بالمصباح اليدوي أنتما الاثنان. أسبوعي الثاني يبدأ في هذه اللحظة!'),
]
WALK = [
    (0, None, ["'هل وجدتَ الكراسي الثلاثة القابلة للطي خلف غرفة الغلاية يا غراهام؟' يصف المركب", (None, 'folding chairs'), 'المقاعد الإضافية المدخرة للمناسبات.']),
    (1, None, ["'وجدتُ الكراسي، وخلف جدار طوبي قديم وجدتُ هذا.' يؤخر غراهام اسم الإشارة في", (None, 'I found this'), 'لإثارة الفضول وهو يضع الصندوق على المكتب.']),
    (2, None, ["'صندوق صغير من خشب الأرز؟ لم أرَ ذلك الصندوق قط طوال خمسة عشر عاماً!' يقترن المضارع التام المنفي", (None, 'I have never seen'), 'بالمدة الممتدة حتى اللحظة الحاضرة.']),
    (3, None, ["'امسح الغبار عن اللوحة النحاسية في الأعلى... انتظر، اقرأ ذلك الرقم!' يفيد الفعل مع حرف الجر", (None, 'Brush the dust off'), 'إزالة الطبقة المغبرة باليد.']),
    (4, None, ["'دعوني أنزل نظارتي من فوق جبهتي... الغرفة التاسعة؟!' تعيد المزحة المحببة", (None, 'pull my glasses down from my forehead'), 'طبع آرثر المألوف منذ الحلقة الأولى.']),
    (5, None, ["'غراهام، انظر إلى لوحة المفاتيح الخشبية خلفنا: واحد، اثنان، ثلاثة، أربعة، خمسة، ستة، سبعة، ثمانية!' يشير المركب", (None, 'wooden key board'), 'إلى اللوحة المثبتة خلف مكتب الاستقبال.']),
    (6, None, ["'لم يضم هذا النزل في تاريخه قط سوى ثماني غرف! أين بحق السماء تقع الغرفة التاسعة؟!' تشدد عبارة", (None, 'has only ever had'), 'على الاستغراب، وتقويه', (None, 'Where on earth'), 'بدهشة مهذبة.']),
    (7, None, ["'أنصتوا عندما أميل الصندوق. لقد انزلق شيء معدني في الداخل للتو.' في الإنجليزية تتأخر المادة أو الصفة بعد الضمائر المبهمة في", (None, 'Something metal'), 'مباشرةً.']),
    (8, None, ["'يوجد ثقب مفتاح صغير جداً على المزلاج الأمامي، وانظروا إلى ما أُلصق في الأسفل: مفتاح نحاسي قديم!' يصف التركيب", (None, 'taped underneath'), 'موضع إخفاء المفتاح.']),
    (9, None, ["'مفتاح نحاسي تاسع؟! أنفتحه هذه الليلة أم ننتظر حتى الصباح؟!' الترقيم الترتيبي في", (None, 'A ninth brass key'), 'يمهد للغز الجديد.']),
    (10, None, ["'انظروا إلى المخطط الهندسي المطوي البارز من عند المفصلة. هناك باب مخفي مرسوم في هذا الطابق!' يصف الفعل المركب", (None, 'sticking out of the hinge'), 'طرف المخطط القديم.']),
    (11, None, ["'أمسكا بالمصباح اليدوي أنتما الاثنان. أسبوعي الثاني يبدأ في هذه اللحظة!' تختتم هانا الموسم الأول بروح المبادرة الحماسية في", (None, 'My second week starts right now'), 'فاتحةً الباب لمغامرة قادمة.']),
]
