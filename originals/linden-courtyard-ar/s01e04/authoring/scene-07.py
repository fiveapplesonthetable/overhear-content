# Authoring module for linden-courtyard-ar-s01e04-scene-07.
ID = 'linden-courtyard-ar-s01e04-scene-07'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = 'Sunlight on the Tag  (ضوء الشمس على البطاقة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'يُخرج غراهام الحقيبة الزرقاء خمس دقائق ريثما يكنس الخزانة، فتتأمل إيفلين بطاقتها الورقية تحت ضوء الشمس الساطع وتتعرف بدهشة غامرة على عنوان بيت النجار وحفيديه اللذين علّمتهما البيانو قبل خمسة وعشرين عاماً! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نتأمل خيوط هذا الاكتشاف الجميل جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى المشهد كاملاً بالسرعة الطبيعية.'
OUTRO = 'النجار وحفيداه الصغيران والقطار الخشبي المنحوت... اقتربت الحقيقة خطوةً كبيرة! نلتقي في المشهد الثامن في الساحة.'
CLOSING = ('evelyn', 'Bye for now!')
STORY = [
    ('graham', 'Let me set this blue suitcase here for five minutes while I sweep the closet.', 'دعيني أضع هذه الحقيبة الزرقاء هنا خمس دقائق ريثما أكنس الخزانة.'),
    ('hannah', 'Careful with it, Graham. Tomorrow at noon is Friday!', 'تعامل معها بحذر يا غراهام. غداً عند الظهر يحل يوم الجمعة!'),
    ('evelyn', "Oh, is that the twin suitcase from Monday's train?", 'أوه، هل تلك هي الحقيبة التوأم من قطار يوم الاثنين؟'),
    ('hannah', "Yes, ma'am, still waiting for its owner.", 'نعم يا سيدتي، لا تزال في انتظار صاحبها.'),
    ('evelyn', 'May I look at the paper tag again here in the bright sunlight?', 'هل لي أن أنظر إلى البطاقة الورقية مرة أخرى هنا في ضوء الشمس الساطع؟'),
    ('graham', "Go right ahead, ma'am. Monday afternoon the lobby was dark.", 'تفضّلي على الرحب يا سيدتي. بعد ظهر يوم الاثنين كان البهو معتماً.'),
    ('evelyn', 'Wait a moment... Number twelve, Linden Street, and two childhood initials carved on the corner!', 'انتظرا لحظة... الرقم اثنا عشر، شارع الزيزفون، وحرفا طفولة منقوشان على الزاوية!'),
    ('hannah', 'Miss Evelyn, you look amazed! Do you know Number twelve, Linden Street?', 'آنسة إيفلين، تبدين مندهشة جداً! هل تعرفين الرقم اثني عشر في شارع الزيزفون؟'),
    ('evelyn', 'Know it? Every Friday for six years I climbed those wooden stairs to teach piano!', 'أأعرفه؟ في كل جمعة طوال ست سنوات كنت أصعد ذلك الدرج الخشبي لأعلّم البيانو!'),
    ('graham', 'Twenty-five years ago? In that same house?', 'قبل خمسة وعشرين عاماً؟ في ذلك البيت نفسه؟'),
    ('evelyn', 'A carpenter lived there with his two grandsons. The older boy played piano, and the little one loved trains!', 'عاش هناك نجار مع حفيديه. كان الصبي الأكبر يعزف البيانو، وكان الصغير يعشق القطارات!'),
    ('hannah', 'A carpenter... and a little wooden toy train inside the bag!', 'نجار... وقطار لعبة خشبي صغير داخل الحقيبة!'),
]
WALK = [
    (0, None, ["'دعيني أضع هذه الحقيبة الزرقاء هنا خمس دقائق ريثما أكنس الخزانة.' تربط أداة التزامن", (None, 'while I sweep'), 'بين وضع الحقيبة مؤقتاً وتنظيف المكان.']),
    (1, None, ["'تعامل معها بحذر يا غراهام. غداً عند الظهر يحل يوم الجمعة!' تحدد العبارة الزمنية", (None, 'Tomorrow at noon'), 'الموعد المرتقب في الملاحظة الورقية.']),
    (2, None, ["'أوه، هل تلك هي الحقيبة التوأم من قطار يوم الاثنين؟' تصف كلمة", (None, 'twin suitcase'), 'تطابق الحقيبتين في اللون والشكل.']),
    (3, None, ["'نعم يا سيدتي، لا تزال في انتظار صاحبها.' تختصر عبارة", (None, 'still waiting for its owner'), 'حال الحقيبة المحفوظة بأمان.']),
    (4, None, ["'هل لي أن أنظر إلى البطاقة الورقية مرة أخرى هنا في ضوء الشمس الساطع؟' يجمع الاستئذان اللطيف بين", (None, 'May I look at'), 'وبين وضوح الرؤية في ضوء النهار.']),
    (5, None, ["'تفضّلي على الرحب يا سيدتي. بعد ظهر يوم الاثنين كان البهو معتماً.' العبارة الترحيبية", (None, 'Go right ahead'), 'تمنح الإذن الفوري بأطيب أسلوب.']),
    (6, None, ["'انتظرا لحظة... الرقم اثنا عشر، شارع الزيزفون، وحرفا طفولة منقوشان على الزاوية!' يُقرأ رقم المنزل في العناوين بصيغة", (None, 'Number twelve'), 'متبوعاً باسم الشارع.']),
    (7, None, ["'آنسة إيفلين، تبدين مندهشة جداً! هل تعرفين الرقم اثني عشر في شارع الزيزفون؟' يصف التركيب", (None, 'you look amazed'), 'ملامح الوجه المندهشة.']),
    (8, None, ["'أأعرفه؟ في كل جمعة طوال ست سنوات كنت أصعد ذلك الدرج الخشبي لأعلّم البيانو!' تكرار الفعل للاستفهام التعجبي في", (None, 'Know it'), 'يؤكد شدة الألفة بالمكان.']),
    (9, None, ["'قبل خمسة وعشرين عاماً؟ في ذلك البيت نفسه؟' تحدد عبارة", (None, 'in that same house'), 'تطابق المكان عبر ربع قرن.']),
    (10, None, ["'عاش هناك نجار مع حفيديه. كان الصبي الأكبر يعزف البيانو، وكان الصغير يعشق القطارات!' تقابل الجملة بين الشقيقين باستعمال", (None, 'The older boy'), 'وبين العبارة الثانية', (None, 'the little one'), 'بسلاسة قصصية.']),
    (11, None, ["'نجار... وقطار لعبة خشبي صغير داخل الحقيبة!' يتوالى الوصف في", (None, 'little wooden toy train'), 'وفق ترتيب الحجم فالمادة فالغرض قبل الاسم.']),
]
