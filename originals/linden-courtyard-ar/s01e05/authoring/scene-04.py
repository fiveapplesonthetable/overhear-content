# Authoring module for linden-courtyard-ar-s01e05-scene-04.
ID = 'linden-courtyard-ar-s01e05-scene-04'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = 'Two Chairs Under the Tree  (كرسيان تحت الشجرة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'ترتب هانا وتيسا وغراهام طاولة خشبية هادئة تحت شجرة الزيزفون بعيداً عن نافذة البهو، ويلمّع غراهام الفوانيس الورقية المعلقة متظاهراً بأنها مجرد صيانة عادية، فيما يبدّل كاليب قميصه في العلية من فرط التوتر! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'لنتأمل الآن استعدادات الساحة الدافئة جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'أصبحت الطاولة والفناجين الزرقاء وكعكة الليمون جاهزة، وبقي أن تهدّئ هانا توتر كاليب قبل دقات الظهر. نلتقي في المشهد الخامس.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Let us put the small wooden table right here under the tree, away from the door.', 'دعونا نضع الطاولة الخشبية الصغيرة هنا تماماً تحت الشجرة، بعيداً عن الباب.'),
    ('graham', 'Good spot. Two solid chairs, facing the garden herbs instead of the lobby window.', 'مكان رائع. كرسيان متينان، يتجهان نحو أعشاب الحديقة بدلاً من نافذة البهو.'),
    ('tessa', 'Here is a clean white cloth and two blue teacups.', 'تفضلا مفرشاً أبيض نظيفاً وفنجاني شاي أزرقين.'),
    ('hannah', 'Graham, are you hanging those paper lanterns for noon?', 'يا غراهام، هل تعلّق تلك الفوانيس الورقية استعداداً لفترة الظهيرة؟'),
    ('graham', 'The wire needed straightening anyway. Nothing sentimental about good maintenance.', 'كان السلك يحتاج إلى تعديل على أي حال. ليس في الصيانة الجيدة أي عاطفة.'),
    ('tessa', 'Oh, listen to Mister Maintenance! Yesterday you fixed the boiler, today you fix two brothers!', 'أوه، استمعوا إلى السيد خبير الصيانة! أمس أصلحتَ الغلاية، واليوم تصلح ما بين شقيقين!'),
    ('graham', 'I fix pipes and chairs. People have to fix their own words.', 'أنا أصلح الأنابيب والكراسي. أما الناس فعليهم أن يصلحوا كلماتهم بأنفسهم.'),
    ('hannah', 'What time does your watch say now, Graham?', 'كم تشير ساعتك الآن يا غراهام؟'),
    ('graham', 'Eleven twenty. Cake ready, Tessa?', 'الحادية عشرة وعشرون دقيقة. هل الكعكة جاهزة يا تيسا؟'),
    ('tessa', 'Cooling on the rack right now, golden crust and sweet lemon sugar!', 'تبرد على الشبكة المعدنية الآن، بقشرة ذهبية وسكر ليمون حلو!'),
    ('hannah', 'Look upstairs at the attic window: Caleb has changed his shirt three times!', 'انظرا إلى الأعلى نحو نافذة العلية: لقد غيّر كاليب قميصه ثلاث مرات!'),
    ('tessa', 'Go talk to him, Hannah, before he wears out the wooden floor!', 'اذهبي وتحدثي معه يا هانا، قبل أن يبلي الأرضية الخشبية من كثرة المشي!'),
]
WALK = [
    (0, None, ["'دعونا نضع الطاولة الخشبية الصغيرة هنا تماماً تحت الشجرة، بعيداً عن الباب.' تحدد عبارة", (None, 'away from the door'), 'خصوصية الجلسة للضيفين.']),
    (1, None, ["'مكان رائع. كرسيان متينان، يتجهان نحو أعشاب الحديقة بدلاً من نافذة البهو.' تصف كلمة", (None, 'facing'), 'وجهة الجلوس المريحة بعيداً عن الأنظار.']),
    (2, None, ["'تفضلا مفرشاً أبيض نظيفاً وفنجاني شاي أزرقين.' تعني كلمة", (None, 'cloth'), 'هنا غطاء المائدة المكوي النظيف.']),
    (3, None, ["'غراهام، هل تلمّع تلك الفوانيس الورقية المعلقة استعداداً لوقت الظهر؟' توضح الصفة في", (None, 'hanging those paper lanterns'), 'هيئة الزينة الممتدة فوق الساحة.']),
    (4, None, ["'كان السلك يحتاج إلى تعديل على أي حال. ليس في الصيانة الجيدة أي عاطفة.' يأتي بعد الفعل", (None, 'needed straightening'), 'اسم الفعل للدلالة على متطلبات الإصلاح.']),
    (5, None, ["'أوه، استمعوا إلى السيد خبير الصيانة! أمس أصلحتَ الغلاية، واليوم تصلح ما بين شقيقين!' اللقب المازح", (None, 'Mister Maintenance'), 'يداعب وقار غراهام بمودة كبيرة.']),
    (6, None, ["'أنا أصلح الأنابيب والكراسي. أما الناس فعليهم أن يصلحوا كلماتهم بأنفسهم.' يقوي التركيب", (None, 'their own words'), 'معنى المسؤولية الشخصية في المصالحة.']),
    (7, None, ["'كم تشير ساعتك الآن يا غراهام؟' في الإنجليزية يسألون عن قراءة الساعة بقولهم", (None, 'What time does your watch say'), 'في تعبير يومي شائع.']),
    (8, None, ["'الحادية عشرة وعشرون دقيقة. هل الكعكة جاهزة يا تيسا؟' تُقرأ الدقائق بعد الساعة مباشرةً في", (None, 'Eleven twenty'), 'دون أداة ربط في الحديث السريع.']),
    (9, None, ["'تبرد على الشبكة المعدنية الآن، بقشرة ذهبية وسكر ليمون حلو!' تشير عبارة", (None, 'Cooling on the rack'), 'إلى المرحلة الأخيرة بعد إخراج الكعكة من الفرن.']),
    (10, None, ["'انظرا إلى الأعلى نحو نافذة العلية: لقد غيّر كاليب قميصه ثلاث مرات!' يبرز المضارع التام", (None, 'has changed his shirt three times'), 'شدة قلقه المتواصل.']),
    (11, None, ["'اذهبي وتحدثي معه يا هانا، قبل أن يبلي الأرضية الخشبية من كثرة المشي!' الفعل المركب الطريف", (None, 'wears out'), 'يصف ذهابه وإيابه المتوتر في الغرفة.']),
]
