# Authoring module for linden-courtyard-ar-s01e06-scene-02.
ID = 'linden-courtyard-ar-s01e06-scene-02'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = 'The Wooden Train  (القطار الخشبي)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'caleb': 'Caleb', 'owen': 'Owen', 'evelyn': 'Evelyn'}
INTRO = 'يفتح أوين اللفافة البيضاء فيجد قاطرة القطار الخشبية التي نحتها الجد وكتب تحت عجلاتها اسميهما معاً، وفي تلك اللحظة تتقدم معلمة البيانو الآنسة إيفلين لتحييهما فتكتمل فرحة اللقاء! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'لنتأمل الآن جمال هذه المفاجأة المزدوجة جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'اجتمع الشقيقان مع معلمتهما إيفلين حول طاولة الساحة، بينما تدور خلف نافذة البهو مشاورات لإنقاذ النزل! نلتقي في المشهد الثالث.'
CLOSING = ('evelyn', 'See you later!')
STORY = [
    ('caleb', 'Before the movers cleared Linden Street, I saved this box from the attic shelf.', 'قبل أن يُخلي عمال النقل بيت شارع الزيزفون، أنقذتُ هذا الصندوق من رف العلية.'),
    ('owen', "Open the white paper... no! Grandfather's carved wooden train engine!", 'افتح الورقة البيضاء... مستحيل! قاطرة القطار الخشبية التي نحتها الجد!'),
    ('caleb', 'Look underneath the wheels. Your name and mine are still penciled there.', 'انظر تحت العجلات. اسمك واسمي لا يزالان مكتوبين بقلم الرصاص هناك.'),
    ('owen', 'I thought this was lost when we sold the house! Why keep it for me?', 'ظننتُ أن هذه ضاعت عندما بعنا البيت! لماذا احتفظتَ بها من أجلي؟'),
    ('caleb', 'Because a house is brick and timber, Owen, while family is what we keep.', 'لأن البيت طوب وخشب بناء يا أوين، بينما العائلة هي ما نحتفظ به.'),
    ('evelyn', 'And you two boys kept the best part of Number twelve right here.', 'وأنتما أيها الفتيان احتفظتما بأجمل جزء من بيت الرقم اثني عشر هنا تماماً.'),
    ('owen', "Excuse me, ma'am... wait. That voice! Miss Evelyn, my piano teacher?!", 'عفواً يا سيدتي... مهلاً. ذلك الصوت! الآنسة إيفلين، معلمة البيانو الخاصة بي؟!'),
    ('evelyn', 'Still waiting for you to play your F major scale slowly, Owen!', 'لا أزال أنتظر منك أن تعزف سلّم فا الكبير ببطء يا أوين!'),
    ('owen', 'Am I dreaming?! Did you plan this whole reunion, Caleb?', 'هل أنا أحلم؟! هل خططتَ لهذا اللقاء العائلي كله يا كاليب؟'),
    ('caleb', "Pure luck, and one swapped blue suitcase on Monday morning's train!", 'محض حظ سعيد، وحقيبة زرقاء واحدة استُبدلت في قطار صباح يوم الاثنين!'),
    ('evelyn', 'Life arranges better duets than we do, my dear boys.', 'ترتب الحياة مقطوعات ثنائية أجمل مما نرتب نحن يا ولديّ العزيزين.'),
    ('owen', 'Please sit with us, Miss Evelyn! Tell me I am not twenty-five years late for my lesson!', 'أرجوكِ اجلسي معنا يا آنسة إيفلين! قولي لي إنني لم أتأخر خمسةً وعشرين عاماً عن درسي!'),
]
WALK = [
    (0, None, ["'قبل أن يُخلي عمال النقل بيت شارع الزيزفون، أنقذتُ هذا الصندوق من رف العلية.' يشير الجمع", (None, 'the movers'), 'إلى الشركة التي أفرغت المنزل القديم عند البيع.']),
    (1, None, ["'افتح الورقة البيضاء... مستحيل! قاطرة القطار الخشبية التي نحتها الجد!' يتتبع الوصف في", (None, 'carved wooden train engine'), 'طريقة الصنع فالمادة فالنوع.']),
    (2, None, ["'انظر تحت العجلات. اسمك واسمي لا يزالان مكتوبين بقلم الرصاص هناك.' تتحول كلمة القلم إلى صفة فعلية في", (None, 'still penciled there'), 'بإيجاز أنيق.']),
    (3, None, ["'ظننتُ أن هذه ضاعت عندما بعنا البيت! لماذا احتفظتَ بها من أجلي؟' تختصر صيغة السؤال", (None, 'Why keep it for me'), 'الفعل المساعد والفاعل لصدق الانفعال.']),
    (4, None, ["'لأن البيت طوب وخشب بناء يا أوين، بينما العائلة هي ما نحتفظ به.' تقابل أداة التوازن", (None, 'while family is what we keep'), 'بين حجارة المباني وروابط القربى.']),
    (5, None, ["'وأنتما أيها الفتيان احتفظتما بأجمل جزء من بيت الرقم اثني عشر هنا تماماً.' يخاطب التعبير الحنون", (None, 'you two boys'), 'الرجلين كما كانا في طفولتهما.']),
    (6, None, ["'عفواً يا سيدتي... مهلاً. ذلك الصوت! الآنسة إيفلين، معلمة البيانو الخاصة بي؟!' يسبق المضاف في", (None, 'piano teacher'), 'الاسم الأخير بلا حرف جر.']),
    (7, None, ["'لا أزال أنتظر منك أن تعزف سلّم فا الكبير ببطء يا أوين!' يُسمّى السلم الموسيقي في الإنجليزية", (None, 'F major scale'), 'بحرف أبجدي يتبعه نوع المقام.']),
    (8, None, ["'هل أنا أحلم؟! هل خططتَ لهذا اللقاء العائلي كله يا كاليب؟' السؤال التعجبي", (None, 'Am I dreaming'), 'يُقال عند توالي المفاجآت السعيدة.']),
    (9, None, ["'محض حظ سعيد، وحقيبة زرقاء واحدة استُبدلت في قطار صباح يوم الاثنين!' تلخص عبارة", (None, 'Pure luck'), 'جمال المصادفة غير المدبرة.']),
    (10, None, ["'ترتب الحياة مقطوعات ثنائية أجمل مما نرتب نحن يا ولديّ العزيزين.' تستعير المعلمة مصطلح الموسيقى في", (None, 'arranges better duets'), 'لتصف التقاء الأقدار.']),
    (11, None, ["'أرجوكِ اجلسي معنا يا آنسة إيفلين! قولي لي إنني لم أتأخر خمسةً وعشرين عاماً عن درسي!' تأتي المدة الزمنية قبل الصفة في", (None, 'twenty-five years late'), 'لدعابة دافئة.']),
]
