# Authoring module for linden-courtyard-ar-s01e02-scene-03.
ID = 'linden-courtyard-ar-s01e02-scene-03'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'Counting the Change  (عدّ الباقي)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'hannah': 'Hannah', 'arthur': 'Arthur', 'tessa': 'Tessa'}
INTRO = 'تعود هانا في تسع دقائق فقط حاملةً المشتريات كاملةً وتعدّ باقي النقود بدقة أمام آرثر، لكن تيسا تلاحظ تفصيلاً صغيراً على غلاف الزبدة الذهبي! استمع إلى المشهد كاملاً باللغة الإنجليزية.'
OPENER = 'لنتابع الآن حوار الحساب والزبدة المملحة جملةً بعد جملة.'
TRANSITION = 'لنستمع الآن مرةً ثانية إلى المشهد كاملاً.'
OUTRO = 'حولت سرعة بديهة تيسا الزبدة البحرية المالحة من مشكلة مع المربى إلى سرّ لذيذ لطبق البيض المخفوق. نلتقي في المشهد الرابع.'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('hannah', 'Nine minutes! Here are the milk, the eggs, and the apples!', 'تسع دقائق! هاكم الحليب والبيض والتفاح!'),
    ('tessa', 'You are a hero, Hannah! Give me the milk first for the coffee machine.', 'أنتِ بطلة يا هانا! أعطيني الحليب أولاً من أجل آلة القهوة.'),
    ('arthur', 'Impressive speed! Did the shopkeeper give you a receipt?', 'سرعة مذهلة! هل أعطاكِ صاحب المتجر إيصالاً؟'),
    ('hannah', 'Right here! Everything cost thirty-eight, so here is twelve in change.', 'ها هو ذا! كلّف كل شيء ثمانيةً وثلاثين، وإليك اثنا عشر باقياً.'),
    ('arthur', 'Ten, eleven, twelve. Exact to the last coin, thank you!', 'عشرة، أحد عشر، اثنا عشر. مضبوط حتى آخر قطعة نقدية، شكراً لكِ!'),
    ('tessa', 'Wait a second, Hannah... which pack of butter did you grab?', 'انتظري ثانيةً يا هانا... أي عبوة زبدة التقطتِ؟'),
    ('hannah', 'The gold wrapper on the top shelf. Why?', 'ذات الغلاف الذهبي من الرف العلوي. لماذا؟'),
    ('tessa', 'That is extra salty sea butter! My sweet jam rolls need plain butter!', 'تلك زبدة بحرية شديدة الملوحة! لفائف المربى الحلوة تحتاج إلى زبدة عادية غير مملحة!'),
    ('hannah', 'Oh no! All the wrappers looked the same when I was running!', 'أوه لا! لقد بدت جميع الأغلفة متشابهةً بينما كنت أركض!'),
    ('arthur', 'Can we serve salty butter with sweet strawberry jam?', 'هل يمكننا تقديم الزبدة المالحة مع مربى الفراولة الحلو؟'),
    ('tessa', 'Wait, salty butter is terrible for jam, but amazing for scrambled eggs!', 'انتظروا، الزبدة المالحة سيئة جداً مع المربى، لكنها مذهلة مع البيض المخفوق!'),
    ('hannah', 'Phew! Quick thinking saves breakfast again.', 'الحمد لله! سرعة البديهة تنقذ الفطور من جديد.'),
]
WALK = [
    (0, None, ["'تسع دقائق! هاكم الحليب والبيض والتفاح!' عند تقديم عدة أشياء مجموعةً أمام المخاطب نقول", (None, 'Here are'), 'بصيغة الجمع المناسبة للقائمة.']),
    (1, None, ["'أنتِ بطلة يا هانا! أعطيني الحليب أولاً من أجل آلة القهوة.' الثناء اليومي المحبب", (None, 'You are a hero'), 'يقال بمرح لمن ينقذ الموقف في اللحظة الحرجة.']),
    (2, None, ["'سرعة مذهلة! هل أعطاكِ صاحب المتجر إيصالاً؟' بعد فعل الإعطاء في", (None, 'give you a receipt'), 'يأتي ضمير الشخص أولاً ثم الشيء الممنوح مباشرةً.']),
    (3, None, ["'ها هو ذا! كلّف كل شيء ثمانيةً وثلاثين، وإليك اثنا عشر باقياً.' الفعل غير القياسي", (None, 'Everything cost'), 'يحتفظ بصورته نفسها في الماضي والمضارع، وتعني', (None, 'in change'), 'المبلغ المسترد.']),
    (4, None, ["'عشرة، أحد عشر، اثنا عشر. مضبوط حتى آخر قطعة نقدية، شكراً لكِ!' تشيد عبارة الدقة الحسابية", (None, 'Exact to the last coin'), 'بأمانة الحساب.']),
    (5, None, ["'انتظري ثانيةً يا هانا... أي عبوة زبدة التقطتِ؟' عندما تختار من أنواع محددة على الرف تسأل بـ", (None, 'which pack of butter'), 'وليس بأداة الاستفهام العامة.']),
    (6, None, ["'ذات الغلاف الذهبي من الرف العلوي. لماذا؟' يحدد التعبير المكاني", (None, 'on the top shelf'), 'موضع العبوة التي تناولتها هانا على عجل.']),
    (7, None, ["'تلك زبدة بحرية شديدة الملوحة! لفائف المربى الحلوة تحتاج إلى زبدة عادية غير مملحة!' تقابل تيسا بين", (None, 'extra salty'), 'وبين كلمة', (None, 'plain butter'), 'المخصصة للحلويات.']),
    (8, None, ["'أوه لا! لقد بدت جميع الأغلفة متشابهةً بينما كنت أركض!' يصور الماضي المستمر في", (None, 'when I was running'), 'الخلفية السريعة التي وقعت خلالها العجلة.']),
    (9, None, ["'هل يمكننا تقديم الزبدة المالحة مع مربى الفراولة الحلو؟' يسأل آرثر عن الإمكانية العملية عبر", (None, 'Can we serve'), 'بحثاً عن مخرج سريع.']),
    (10, None, ["'انتظروا، الزبدة المالحة سيئة جداً مع المربى، لكنها مذهلة مع البيض المخفوق!' تبرز المقابلة الذكية بين", (None, 'terrible for jam'), 'وبين عبارة الإعجاب المقابلة', (None, 'amazing for scrambled eggs'), 'كيف انقلب الخطأ إلى ميزة.']),
    (11, None, ["'الحمد لله! سرعة البديهة تنقذ الفطور من جديد.' تبدأ هانا بصوت الارتياح", (None, 'Phew'), 'وتسمي التفكير السريع الحاضر', (None, 'Quick thinking'), 'بإيجاز معبر.']),
]
