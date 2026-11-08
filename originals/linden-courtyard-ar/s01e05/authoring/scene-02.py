# Authoring module for linden-courtyard-ar-s01e05-scene-02.
ID = 'linden-courtyard-ar-s01e05-scene-02'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = 'Three Years of Silence  (ثلاث سنوات من الصمت)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'أمام مكتب الاستقبال يفتح غراهام خزانة الأمتعة ويسلم كاليب حقيبته الزرقاء، فيحكي كاليب لهانا وغراهام عن الخلاف الحاد الذي فرق بينه وبين أخيه أوين بعد وفاة جدهما قبل ثلاث سنوات. استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'لنتأمل الآن كلمات هذا البوح الأخوي جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'قرر كاليب التخلي عن خطة الاختباء القديمة ومواجهة أخيه وجهاً لوجه عند الظهر بفضل دفء أهل النزل. نلتقي في المشهد الثالث في ركن المقهى.'
CLOSING = ('graham', 'See you later!')
STORY = [
    ('graham', 'So our mystery Friday caller was sleeping upstairs under my attic roof all along.', 'إذن المتصل الغامض ليوم الجمعة كان نائماً في الأعلى تحت سقف عليتي طوال الوقت.'),
    ('caleb', 'Sorry for the trouble, Graham. Thank you for guarding this bag all week.', 'عذراً على الإزعاج يا غراهام. شكراً لك على حراسة هذه الحقيبة طوال الأسبوع.'),
    ('hannah', 'Why could you not simply hand Owen the wooden train at his front door?', 'لماذا لم تستطع ببساطة أن تسلّم أوين القطار الخشبي عند باب بيته؟'),
    ('caleb', 'Three years ago, after our grandfather died, Owen and I argued bitterly over selling the old house.', 'قبل ثلاث سنوات، بعد وفاة جدنا، تجادلتُ أنا وأوين بمرارة حول بيع البيت القديم.'),
    ('graham', 'Family houses and old memories, those arguments cut deep.', 'بيوت العائلة والذكريات القديمة... تلك الخلافات تجرح القلب بعمق.'),
    ('caleb', 'We have not spoken since that Sunday. Last week I sent him one short postcard.', 'لم نتحدث منذ يوم الأحد ذاك. وفي الأسبوع الماضي أرسلتُ له بطاقة بريدية قصيرة واحدة.'),
    ('hannah', 'Asking him to meet you here on Friday at noon?', 'تطلب منه فيها أن يلتقي بك هنا يوم الجمعة عند الظهر؟'),
    ('caleb', "Actually, I only wrote: 'Something from Grandfather is waiting at the Linden Courtyard Inn Friday at noon.'", 'في الواقع، كتبتُ فقط: هناك شيء من الجد ينتظرك في نزل ساحة الزيزفون يوم الجمعة عند الظهر.'),
    ('graham', 'Aha! You feared that if you signed your name, stubborn big brother would stay home!', 'أها! خشيتَ إن وقّعتَ اسمك أن يبقى الأخ الكبير العنيد في بيته!'),
    ('caleb', 'You know older brothers well, Graham.', 'أنت تعرف الإخوة الكبار جيداً يا غراهام.'),
    ('hannah', 'Wait, were you planning to hand the clerk the bag and watch from across the street?!', 'مهلاً، هل كنتَ تخطط لتسليم الحقيبة لموظف الاستقبال والمراقبة من الجهة المقابلة من الشارع؟!'),
    ('caleb', 'That was my cowardly Monday plan... before I met all of you.', 'كانت تلك خطتي الجبانة ليوم الاثنين... قبل أن ألتقي بكم جميعاً.'),
]
WALK = [
    (0, None, ["'إذن المتصل الغامض ليوم الجمعة كان نائماً في الأعلى تحت سقف عليتي طوال الوقت.' تختم العبارة", (None, 'all along'), 'الجملة لإبراز المفارقة اللطيفة.']),
    (1, None, ["'عذراً على الإزعاج يا غراهام. شكراً لك على حراسة هذه الحقيبة طوال الأسبوع.' نشكر من صان أمانةً بقولنا", (None, 'for guarding this bag'), 'بصيغة اسم الفعل.']),
    (2, None, ["'لماذا لم تستطع ببساطة أن تسلّم أوين القطار الخشبي عند باب بيته؟' يعني الفعل", (None, 'hand Owen the wooden train'), 'التسليم الشخصي المباشر.']),
    (3, None, ["'قبل ثلاث سنوات، بعد وفاة جدنا، تجادلتُ أنا وأوين بمرارة حول بيع البيت القديم.' يقدم المتحدث الإنجليزي اسم غيره على نفسه في", (None, 'Owen and I argued'), 'أدباً في العطف.']),
    (4, None, ["'بيوت العائلة والذكريات القديمة... تلك الخلافات تجرح القلب بعمق.' التعبير المجازي", (None, 'cut deep'), 'يصف أثر الخلافات العائلية بإيجاز مؤثر.']),
    (5, None, ["'لم نتحدث منذ يوم الأحد ذاك. وفي الأسبوع الماضي أرسلتُ له بطاقة بريدية قصيرة واحدة.' يقترن المضارع التام المنفي", (None, 'We have not spoken since'), 'بنقطة بداية القطيعة.']),
    (6, None, ["'تطلب منه فيها أن يلتقي بك هنا يوم الجمعة عند الظهر؟' يحدد التعبير الزمني", (None, 'on Friday at noon'), 'اليوم أولاً ثم الساعة.']),
    (7, None, ["'في الواقع، كتبتُ فقط: هناك شيء من الجد ينتظرك في نزل ساحة الزيزفون يوم الجمعة عند الظهر.' يضفي التنكير في", (None, 'Something from Grandfather'), 'غموضاً يدفع الأخ إلى الحضور.']),
    (8, None, ["'أها! خشيتَ إن وقّعتَ اسمك أن يبقى الأخ الكبير العنيد في بيته!' تُستعمل عبارة", (None, 'stay home'), 'في الإنجليزية الأمريكية دون حرف جر قبل البيت.']),
    (9, None, ["'أنت تعرف الإخوة الكبار جيداً يا غراهام.' يوضع ظرف الإجادة", (None, 'well'), 'في نهاية الجملة بعد المفعول به.']),
    (10, None, ["'مهلاً، هل كنتَ تخطط لتسليم الحقيبة لموظف الاستقبال والمراقبة من الجهة المقابلة من الشارع؟!' تحدد عبارة", (None, 'from across the street'), 'المراقبة عن بُعد.']),
    (11, None, ["'كانت تلك خطتي الجبانة ليوم الاثنين... قبل أن ألتقي بكم جميعاً.' على الرغم من انتهاء", (None, 'cowardly'), 'بلاحقة تشبه الظروف، فهي صفة تسبق الاسم مباشرةً.']),
]
