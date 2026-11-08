# Authoring module for linden-courtyard-ar-s01e06-scene-01.
ID = 'linden-courtyard-ar-s01e06-scene-01'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = 'At the Iron Gate  (عند البوابة الحديدية)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'caleb': 'Caleb', 'owen': 'Owen', 'hannah': 'Hannah'}
INTRO = 'تحضر هانا الشاي الساخن إلى طاولة الساحة بينما ينطق كاليب بجمله الثلاث البسيطة الصادقة، فيبتسم شقيقه الأكبر أوين ويعترف بأنه عرف خط يده منذ اللحظة الأولى واشتاق إليه بدوره طوال السنوات الثلاث. استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نستمع إلى دفء المصالحة بين الشقيقين جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'ذاب جليد السنوات الثلاث في دقائق معدودة، وحان وقت فتح الحقيبة الزرقاء القديمة من ورشة الجد. نلتقي في المشهد الثاني.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('owen', "So 'someone with something from Grandfather' was you all along, Caleb.", 'إذن عبارة شخص لديه شيء من الجد لم تكن سواك أنت طوال الوقت يا كاليب.'),
    ('caleb', 'Hello, Owen. Thank you for coming today.', 'مرحباً يا أوين. شكراً لك على مجيئك اليوم.'),
    ('owen', 'I recognized your neat block handwriting on that postcard in two seconds.', 'تعرفتُ على خط يدك المرتب بالحروف المنفصلة على تلك البطاقة البريدية في ثانيتين.'),
    ('caleb', 'Wait, you knew it was from me and came anyway?', 'مهلاً، أكنتَ تعلم أنها مني وجئتَ على أي حال؟'),
    ('owen', 'Of course I came. Why did you hide behind a mystery note?', 'بالطبع جئت. لماذا اختبأتَ خلف ملاحظة غامضة؟'),
    ('caleb', 'Because I was afraid you were still angry. I missed you these three years.', 'لأنني خشيتُ أن تكون لا تزال غاضباً. لقد اشتقتُ إليك طوال هذه السنوات الثلاث.'),
    ('owen', 'Three stubborn years... honestly, little brother, I missed you too.', 'ثلاث سنوات من العناد... بصراحة يا أخي الصغير، أنا اشتقتُ إليك أيضاً.'),
    ('hannah', 'Excuse me, gentlemen. Here is hot tea, and warm lemon cake is on the way.', 'عفواً أيها السيدان. تفضلا الشاي الساخن، وكعكة الليمون الدافئة في الطريق إليكما.'),
    ('owen', 'Lemon cake? Wait, how did she know about Friday lemon cake?', 'كعكة الليمون؟ مهلاً، كيف عرفت هي بشأن كعكة الليمون ليوم الجمعة؟'),
    ('caleb', 'Sit down, Owen, take off your heavy coat, and look at this blue suitcase.', 'اجلس يا أوين، اخلع معطفك الثقيل، وانظر إلى هذه الحقيبة الزرقاء.'),
    ('owen', "Is that the old dark blue bag from Grandfather's workshop?", 'أليست تلك الحقيبة الزرقاء الداكنة القديمة من ورشة الجد؟'),
    ('hannah', 'Take all the time you need. The courtyard is yours.', 'خذا كل الوقت الذي تحتاجان إليه. الساحة لكما.'),
]
WALK = [
    (0, None, ["'إذن عبارة شخص لديه شيء من الجد لم تكن سواك أنت طوال الوقت يا كاليب.' تختم عبارة", (None, 'was you all along'), 'الغموض بابتسامة معرفة.']),
    (1, None, ["'مرحباً يا أوين. شكراً لك على مجيئك اليوم.' يفتتح كاليب كلامه بأولى الجمل البسيطة", (None, 'Thank you for coming today'), 'فتؤتي ثمارها في الحال.']),
    (2, None, ["'تعرفتُ على خط يدك المرتب بالحروف المنفصلة على تلك البطاقة البريدية في ثانيتين.' يصف المركب", (None, 'neat block handwriting'), 'دقة خط المهندس المعماري.']),
    (3, None, ["'مهلاً، أكنتَ تعلم أنها مني وجئتَ على أي حال؟' توضع كلمة", (None, 'anyway'), 'في آخر السؤال لإظهار التأثر والدهشة السارة.']),
    (4, None, ["'بالطبع جئت. لماذا اختبأتَ خلف ملاحظة غامضة؟' يرد أوين بالتأكيد القاطع", (None, 'Of course I came'), 'مزيلاً كل شك قديم.']),
    (5, None, ["'لأنني خشيتُ أن تكون لا تزال غاضباً. لقد اشتقتُ إليك طوال هذه السنوات الثلاث.' يتبع التركيب", (None, 'I was afraid you were'), 'توافق الزمن الماضي في الإنجليزية.']),
    (6, None, ["'ثلاث سنوات من العناد... بصراحة يا أخي الصغير، أنا اشتقتُ إليك أيضاً.' تنقل الصفة في", (None, 'Three stubborn years'), 'وصف العناد إلى السنين نفسها إيجازاً وبلاغة.']),
    (7, None, ["'عفواً أيها السيدان. تفضلا الشاي الساخن، وكعكة الليمون الدافئة في الطريق إليكما.' تعني عبارة", (None, 'is on the way'), 'قرب وصول الطلب من المطبخ.']),
    (8, None, ["'كعكة الليمون؟ مهلاً، كيف عرفت هي بشأن كعكة الليمون ليوم الجمعة؟' يسأل الفعل مع حرف الجر", (None, 'know about'), 'عن مصدر معرفتها بالسر العائلي.']),
    (9, None, ["'اجلس يا أوين، اخلع معطفك الثقيل، وانظر إلى هذه الحقيبة الزرقاء.' يدعو الفعل المركب", (None, 'take off your heavy coat'), 'إلى الاسترخاء والإقامة المريحة.']),
    (10, None, ["'أليست تلك الحقيبة الزرقاء الداكنة القديمة من ورشة الجد؟' تحدد ياء وسين الملكية في", (None, "Grandfather's workshop"), 'المكان العزيز الذي خرجت منه الحقيبة.']),
    (11, None, ["'خذا كل الوقت الذي تحتاجان إليه. الساحة لكما.' تمنح العبارتان", (None, 'Take all the time you need'), 'ومعها العبارة', (None, 'The courtyard is yours'), 'قمة اللطف وحسن الضيافة.']),
]
