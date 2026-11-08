# Authoring module for linden-courtyard-ar-s01e06-scene-06.
ID = 'linden-courtyard-ar-s01e06-scene-06'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = 'Permanent Keys  (مفاتيح دائمة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'arthur': 'Arthur', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = 'يعلن آرثر ببهجة غامرة افتتاح مقهى الساحة الصباحي لأهل الشارع ابتداءً من الثامنة صباح الغد محققاً حلم تيسا، ويعرض على هانا في ختام أسبوع تجربتها الأول منصب مديرة الاستقبال الدائمة! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نحتفل مع أبطال النزل في هذا المشهد جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'دُوّن اسم هانا بالحبر الدائم في دفتر النزل الكبير، وأصبح نزل ساحة الزيزفون بيتاً دافئاً للجميع. نلتقي تحت الفوانيس الذهبية في المشهد السابع.'
CLOSING = ('arthur', 'See you later!')
STORY = [
    ('arthur', 'Tessa, how many cinnamon rolls and lemon cakes can your oven bake each morning?', 'تيسا، كم لفافة قرفة وكعكة ليمون يستطيع فرنكِ أن يخبز كل صباح؟'),
    ('tessa', 'Double what I make now! Are we really opening the courtyard cafe to our street?', 'ضعف ما أعدّه الآن! هل سنفتتح حقاً مقهى الساحة لشارعنا؟'),
    ('arthur', 'Starting tomorrow at eight! Four tables inside, three tables under the tree!', 'ابتداءً من الغد عند الثامنة! أربع طاولات في الداخل، وثلاث طاولات تحت الشجرة!'),
    ('tessa', 'My dream cafe, right here in our own courtyard! Wait until I tell the whole street!', 'مقهى أحلامي، هنا تماماً في ساحتنا الخاصة! انتظروا حتى أخبر الشارع بأكمله!'),
    ('arthur', 'And now, Hannah, today is Friday, the last day of your five day trial week.', 'والآن يا هانا، اليوم هو الجمعة، آخر يوم في أسبوع التجربة ذي الأيام الخمسة.'),
    ('hannah', 'Oh! With the suitcases, the boiler, and the letter, I completely forgot!', 'أوه! مع الحقائب، والغلاية، والرسالة، نسيتُ الأمر تماماً!'),
    ('arthur', 'On Monday you opened our tricky door; since then you saved rooms, pipes, breakfast, and our lease.', 'في يوم الاثنين فتحتِ بابنا المراوغ؛ ومنذ ذلك الحين أنقذتِ الغرف والأنابيب والفطور وعقد إيجارنا.'),
    ('tessa', 'If you do not hire her full time, Arthur, I am hiring her in my kitchen!', 'إذا لم توظفها بدوام كامل يا آرثر، فسأوظفها أنا في مطبخي!'),
    ('arthur', 'Hands off, Tessa! Hannah, would you stay as our permanent front desk manager?', 'ارفعي يديكِ عنها يا تيسا! هانا، هل تقبلين البقاء مديرةً دائمة لمكتب الاستقبال لدينا؟'),
    ('hannah', 'Stay here with all of you? Yes, a hundred times yes!', 'أبقى هنا معكم جميعاً؟ نعم، مئة مرة نعم!'),
    ('arthur', "Wonderful! Your name goes in Graham's big paper book in permanent ink!", 'رائع! سيُكتب اسمكِ في دفتر غراهام الورقي الكبير بالحبر الدائم!'),
    ('hannah', 'Best first week of my life!', 'أجمل أسبوع أول في حياتي!'),
]
WALK = [
    (0, None, ["'تيسا، كم لفافة قرفة وكعكة ليمون يستطيع فرنكِ أن يخبز كل صباح؟' للسؤال عن العدد المعدود نبدأ بـ", (None, 'how many cinnamon rolls'), 'متبوعاً بصيغة الجمع.']),
    (1, None, ["'ضعف ما أعدّه الآن! هل سنفتتح حقاً مقهى الساحة لشارعنا؟' تعني العبارة السريعة", (None, 'Double what I make now'), 'الاستعداد التام لمضاعفة الإنتاج.']),
    (2, None, ["'ابتداءً من الغد عند الثامنة! أربع طاولات في الداخل، وثلاث طاولات تحت الشجرة!' تفتتح كلمة", (None, 'Starting tomorrow at eight'), 'موعد الانطلاق الرسمي.']),
    (3, None, ["'مقهى أحلامي، هنا تماماً في ساحتنا الخاصة! انتظروا حتى أخبر الشارع بأكمله!' يعبّر المركب", (None, 'My dream cafe'), 'عن تحقق أمنيتها الكبرى.']),
    (4, None, ["'والآن يا هانا، اليوم هو الجمعة، آخر يوم في أسبوع التجربة ذي الأيام الخمسة.' في الصفة المركبة", (None, 'five day trial week'), 'يبقى التمييز مفرداً قبل الاسم.']),
    (5, None, ["'أوه! مع الحقائب، والغلاية، والرسالة، نسيتُ الأمر تماماً!' يبرز الظرف في", (None, 'I completely forgot'), 'انغماسها المخلص في شؤون النزل.']),
    (6, None, ["'في يوم الاثنين فتحتِ بابنا المراوغ؛ ومنذ ذلك الحين أنقذتِ الغرف والأنابيب والفطور وعقد إيجارنا.' تربط عبارة", (None, 'since then'), 'بداية الأسبوع بجميع الإنجازات المتتالية.']),
    (7, None, ["'إذا لم توظفها بدوام كامل يا آرثر، فسأوظفها أنا في مطبخي!' تحدد العبارة الوظيفية", (None, 'hire her full time'), 'العمل الرسمي الثابت.']),
    (8, None, ["'ارفعي يديكِ عنها يا تيسا! هانا، هل تقبلين البقاء مديرةً دائمة لمكتب الاستقبال لدينا؟' تُقال عبارة", (None, 'Hands off'), 'هنا بمزاح ودي لطيف.']),
    (9, None, ["'أبقى هنا معكم جميعاً؟ نعم، مئة مرة نعم!' التوكيد البليغ المبهج", (None, 'a hundred times yes'), 'يعلن القبول الفوري من القلب.']),
    (10, None, ["'رائع! سيُكتب اسمكِ في دفتر غراهام الورقي الكبير بالحبر الدائم!' تشير عبارة", (None, 'in permanent ink'), 'إلى رسوخ مكانها بين أسرة النزل.']),
    (11, None, ["'أجمل أسبوع أول في حياتي!' تختصر الجملة التعجبية", (None, 'Best first week of my life'), 'سعادة البدايات الجميلة.']),
]
