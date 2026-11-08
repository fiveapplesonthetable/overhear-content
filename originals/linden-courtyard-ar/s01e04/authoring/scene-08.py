# Authoring module for linden-courtyard-ar-s01e04-scene-08.
ID = 'linden-courtyard-ar-s01e04-scene-08'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = 'The Boy on the Stairs  (الصبي الجالس على الدرج)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = 'في الساحة تصف إيفلين لهانا ذلك الشقيق الأصغر الهادئ الذي كان يجلس على الدرجة الثالثة مصغياً لرنين البيانو وقت المطر، وفي تلك اللحظة يخرج كاليب ويجيب عن سؤال طفولته بنفسه! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نعيش لحظة التعارف المؤثرة هذه جملةً بعد جملة.'
TRANSITION = 'لنستمع الآن مرةً ثانية إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'تعرّفت المعلمة إيفلين على تلميذ الدرج الصغير كاليب، وحان وقت سماع الحقيقة الكاملة وراء الحقيبة الزرقاء في الحلقة الخامسة! إلى اللقاء.'
CLOSING = ('caleb', 'Goodbye!')
STORY = [
    ('hannah', 'Tell me more about the two boys on Linden Street, Miss Evelyn!', 'أخبريني بالمزيد عن الصبيين في شارع الزيزفون يا آنسة إيفلين!'),
    ('evelyn', 'The older brother was bold and loud, always rushing through his music scales.', 'كان الأخ الأكبر جريئاً وصاخباً، يسرع دائماً في عزف السلالم الموسيقية.'),
    ('hannah', 'And the younger brother with the wooden train?', 'وماذا عن الأخ الأصغر صاحب القطار الخشبي؟'),
    ('evelyn', 'Quiet as a mouse! He sat on the third stair listening to every single note.', 'هادئ تماماً كالفأر! كان يجلس على الدرجة الثالثة مصغياً إلى كل نغمة واحدة.'),
    ('hannah', 'Listening to the sound of the room... wait a second!', 'يصغي إلى صوت الغرفة... انتظري ثانية واحدة!'),
    ('evelyn', 'Whenever I finished playing, he asked why the piano sounded warmer when it rained.', 'كلما انتهيتُ من العزف، كان يسأل لماذا يبدو صوت البيانو أدفأ عندما تمطر.'),
    ('caleb', 'Because wet wooden shutters soften the echo from the stone street...', 'لأن المصاريع الخشبية المبتلة تخفف صدى الصوت القادم من الشارع الحجري...'),
    ('hannah', 'Caleb! Were you standing right there?!', 'كاليب! هل كنتَ واقفاً هناك تماماً؟!'),
    ('evelyn', 'Good heavens... look at your eyes! Little Caleb from the third stair?!', 'يا للسماء... انظر إلى عينيك! كاليب الصغير الجالس على الدرجة الثالثة؟!'),
    ('caleb', "Miss Evelyn?! My brother's Friday piano teacher?!", 'آنسة إيفلين؟! معلمة البيانو لأخي أيام الجمعة؟!'),
    ('hannah', 'Wait, then Monday night on our step... the second blue suitcase...', 'انتظر، إذن ليلة الاثنين على عتبتنا... الحقيبة الزرقاء الثانية...'),
    ('caleb', 'Yes, Hannah. That blue suitcase is mine, and I owe you both the whole truth.', 'نعم يا هانا. تلك الحقيبة الزرقاء لي، وأنا مدين لكما معاً بالحقيقة كاملة.'),
]
WALK = [
    (0, None, ["'أخبريني بالمزيد عن الصبيين في شارع الزيزفون يا آنسة إيفلين!' تدعو العبارة الحوارية", (None, 'Tell me more about'), 'إلى إكمال الذكريات بشوق.']),
    (1, None, ["'كان الأخ الأكبر جريئاً وصاخباً، يسرع دائماً في عزف السلالم الموسيقية.' يصف الفعل المركب", (None, 'rushing through'), 'العزف السريع بلا تأنٍّ.']),
    (2, None, ["'وماذا عن الأخ الأصغر صاحب القطار الخشبي؟' يحدد حرف الجر", (None, 'with the wooden train'), 'علامته المميزة منذ الطفولة.']),
    (3, None, ["'هادئ تماماً كالفأر! كان يجلس على الدرجة الثالثة مصغياً إلى كل نغمة واحدة.' التشبيه الودود الشهير", (None, 'Quiet as a mouse'), 'يمدح هدوء الأطفال المهذبين.']),
    (4, None, ["'يصغي إلى صوت الغرفة... انتظري ثانية واحدة!' تربط هانا بين طفولته ومهنته الحالية ثم تستوقف الحديث بـ", (None, 'wait a second'), 'لحظة انتباهها للسر.']),
    (5, None, ["'كلما انتهيتُ من العزف، كان يسأل لماذا يبدو صوت البيانو أدفأ عندما تمطر.' تفيد أداة التكرار", (None, 'Whenever I finished playing'), 'تجدد السؤال في كل درس.']),
    (6, None, ["'لأن المصاريع الخشبية المبتلة تخفف صدى الصوت القادم من الشارع الحجري...' يكمل كاليب الجواب العلمي الشعري بالفعل", (None, 'soften the echo'), 'كاشفاً هويته دون أن يشعر.']),
    (7, None, ["'كاليب! هل كنتَ واقفاً هناك تماماً؟!' يبرز الماضي المستمر", (None, 'Were you standing right there'), 'مفاجأة حضوره الهادئ.']),
    (8, None, ["'يا للسماء... انظر إلى عينيك! كاليب الصغير الجالس على الدرجة الثالثة؟!' تعبّر الصيغة الكلاسيكية اللطيفة", (None, 'Good heavens'), 'عن تأثر عاطفي عميق.']),
    (9, None, ["'آنسة إيفلين؟! معلمة البيانو لأخي أيام الجمعة؟!' تتقدم الإضافة العائلية واليوم في", (None, "My brother's Friday piano teacher"), 'في سلسلة وصفية مترابطة.']),
    (10, None, ["'انتظر، إذن ليلة الاثنين على عتبتنا... الحقيبة الزرقاء الثانية...' تجمع هانا خيوط القصة بعبارة", (None, 'Monday night on our step'), 'لتصل إلى استنتاجها.']),
    (11, None, ["'نعم يا هانا. تلك الحقيبة الزرقاء لي، وأنا مدين لكما معاً بالحقيقة كاملة.' يختم ضمير الملكية المستقل", (None, 'mine'), 'الاعتراف، وتعد عبارة', (None, 'the whole truth'), 'بكشف القصة كلها.']),
]
