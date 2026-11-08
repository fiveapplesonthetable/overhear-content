# Authoring module for linden-courtyard-ar-s01e03-scene-05.
ID = 'linden-courtyard-ar-s01e03-scene-05'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 3
SCENE = 5
TITLE = 'Half Price and Quiet Beams  (نصف السعر وعوارض هادئة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'graham': 'Graham'}
INTRO = 'يصعد كاليب مع هانا وغراهام إلى غرفة العلية تحت السقف السندياني العتيق، فينبهر بهدوء المكان وتناسق عوارضه الخشبية، ويتسلم المفتاح الفضي بسعادة بالغة. استمع إلى المشهد كاملاً باللغة الإنجليزية.'
OPENER = 'دعنا نستعرض الآن حوار هذا المشهد الهادئ جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد متصلاً بالسرعة الطبيعية.'
OUTRO = 'أحب كاليب هدوء العلية ومكتبها الواسع، وتنفس الجميع الصعداء بعد حل مشكلة الحجز المزدوج. نلتقي في المشهد السادس في الطابق السفلي.'
CLOSING = ('hannah', 'Good night!')
STORY = [
    ('hannah', 'Here we are, sir. Watch your head on this low wooden beam.', 'ها قد وصلنا يا سيدي. انتبه لرأسك من هذه العارضة الخشبية المنخفضة.'),
    ('caleb', 'Oh... look at the proportions of this timber roof!', 'أوه... انظروا إلى تناسق أبعاد هذا السقف الخشبي!'),
    ('graham', 'Solid oak, eighty years old. Not a single leak.', 'سنديان مصمت، عمره ثمانون عاماً. ليس فيه ولا تسرب واحد.'),
    ('hannah', 'Because of our mistake, tonight is half price, with breakfast included.', 'بسبب خطئنا، الإقامة الليلة بنصف السعر، مع فطور مشمول.'),
    ('caleb', 'Listen for a second... you cannot hear a single car from the street.', 'أنصتا لثانية واحدة... لا يمكنك سماع سيارة واحدة من الشارع.'),
    ('hannah', 'Only the courtyard tree and the rain.', 'فقط شجرة الساحة وصوت المطر.'),
    ('caleb', 'To tell you the truth, I hate noisy first floor rooms. I love this space!', 'الحق يُقال، أنا أكره غرف الطابق الأول الصاخبة. لقد أحببتُ هذه الفسحة!'),
    ('graham', 'Really? You do not mind the extra stairs?', 'حقاً؟ ألا تمانع الدرج الإضافي؟'),
    ('caleb', 'Not at all! And this wide desk under the window is ideal for my work.', 'على الإطلاق! وهذا المكتب العريض تحت النافذة مثالي لعملي.'),
    ('hannah', 'What a relief! Here is your silver key, Caleb.', 'يا للارتياح! تفضّل مفتاحك الفضي يا كاليب.'),
    ('caleb', 'Thank you both for being honest instead of sending me back into the rain.', 'شكراً لكما معاً على صراحتكما بدلاً من إعادتي إلى المطر.'),
    ('graham', 'Sleep well, sir. Breakfast starts at seven thirty downstairs.', 'نوماً هانئاً يا سيدي. يبدأ الفطور عند السابعة والنصف في الطابق السفلي.'),
]
WALK = [
    (0, None, ["'ها قد وصلنا يا سيدي. انتبه لرأسك من هذه العارضة الخشبية المنخفضة.' تنبّه عبارة", (None, 'Watch your head'), 'مرافقك بلطف عند المرور تحت سقف منخفض.']),
    (1, None, ["'أوه... انظروا إلى تناسق أبعاد هذا السقف الخشبي!' تصف الكلمة المعمارية", (None, 'proportions'), 'انسجام الارتفاع والعرض في التصميم الهندسي.']),
    (2, None, ["'سنديان مصمت، عمره ثمانون عاماً. ليس فيه ولا تسرب واحد.' تؤكد عبارة النفي المشدد", (None, 'Not a single leak'), 'متانة السقف عبر السنين.']),
    (3, None, ["'بسبب خطئنا، الإقامة الليلة بنصف السعر، مع فطور مشمول.' تأتي الصفة في", (None, 'with breakfast included'), 'بعد الاسم مباشرةً على عادة لوائح الفنادق.']),
    (4, None, ["'أنصتا لثانية واحدة... لا يمكنك سماع سيارة واحدة من الشارع.' يوظّف المتحدث الضمير العام في", (None, 'you cannot hear'), 'ليشمل كل من يقف في الغرفة.']),
    (5, None, ["'فقط شجرة الساحة وصوت المطر.' هذا الجواب المختصر المبدوء بكلمة", (None, 'Only'), 'يكمل الجملة السابقة دون حاجة إلى تكرار الفعل.']),
    (6, None, ["'الحق يُقال، أنا أكره غرف الطابق الأول الصاخبة. لقد أحببتُ هذه الفسحة!' تمهد العبارة الاستفتاحية", (None, 'To tell you the truth'), 'لبوح صريح ومطمئن.']),
    (7, None, ["'حقاً؟ ألا تمانع الدرج الإضافي؟' السؤال بصيغة", (None, 'You do not mind'), 'يتحقق بلطف من رضا الضيف عن صعود الطوابق.']),
    (8, None, ["'على الإطلاق! وهذا المكتب العريض تحت النافذة مثالي لعملي.' تقترن الصفة", (None, 'ideal for'), 'بحرف الجر الدال على الغاية والعمل.']),
    (9, None, ["'يا للارتياح! تفضّل مفتاحك الفضي يا كاليب.' صيغة التعجب", (None, 'What a relief'), 'تعبر عفوياً عن زوال قلق ثقيل.']),
    (10, None, ["'شكراً لكما معاً على صراحتكما بدلاً من إعادتي إلى المطر.' بعد التركيب", (None, 'instead of'), 'يأتي الفعل مضافاً إليه لاحقة الاسمية في', (None, 'sending'), 'اطّراداً مع حروف الجر.']),
    (11, None, ["'نوماً هانئاً يا سيدي. يبدأ الفطور عند السابعة والنصف في الطابق السفلي.' تُستعمل صيغة المضارع البسيط في", (None, 'Breakfast starts'), 'للجداول اليومية الثابتة.']),
]
