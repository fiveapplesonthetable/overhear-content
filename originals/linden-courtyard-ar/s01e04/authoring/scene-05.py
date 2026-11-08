# Authoring module for linden-courtyard-ar-s01e04-scene-05.
ID = 'linden-courtyard-ar-s01e04-scene-05'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 4
SCENE = 5
TITLE = 'Five-Star Showers  (حمامات دافئة من خمس نجوم)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'ينزل كاليب إلى الفطور مبتهجاً بنومه الهادئ وماء الاستحمام الساخن، فيتحمس آرثر ويزلّ لسانه بذكر درجات التقييم ودليل السفر، ليتبين أن كاليب ليس مفتش فنادق أصلاً! استمع إلى المشهد باللغة الإنجليزية.'
OPENER = 'دعنا نستمتع بتفاصيل هذا الموقف الطريف جملةً بعد جملة.'
TRANSITION = 'والآن أنصت إلى الحوار كاملاً بالسرعة الطبيعية.'
OUTRO = 'انكشف سوء الفهم اللطيف، ودعا كاليب الجميع إلى الساحة ليريهم طبيعة عمله الحقيقي. نلتقي تحت شجرة الزيزفون في المشهد السادس.'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('caleb', 'Good morning, Hannah! Good morning, sir! What a bright morning after the rain.', 'صباح الخير يا هانا! صباح الخير يا سيدي! يا له من صباح مشرق بعد المطر.'),
    ('hannah', 'Good morning, Caleb! Did you sleep well under the roof beams?', 'صباح الخير يا كاليب! هل نمتَ جيداً تحت عوارض السقف؟'),
    ('caleb', 'Best sleep I have had all month, and the shower water was wonderfully hot!', 'أفضل نوم نمته طوال الشهر، وكان ماء الاستحمام ساخناً على نحو رائع!'),
    ('arthur', 'Hot! Hear that, Hannah? Reliable, modern, five-star hot water!', 'ساخن! هل تسمعين ذلك يا هانا؟ مياه ساخنة موثوقة وحديثة ومن خمس نجوم!'),
    ('caleb', 'Old brick buildings usually take ages to warm up on the top floor.', 'تستغرق المباني الطوبية القديمة في العادة وقتاً طويلاً جداً لتسخن في الطابق العلوي.'),
    ('arthur', "Please write that down! 'Hot water on the third floor: ten out of ten!'", 'أرجوك دوّن ذلك! الماء الساخن في الطابق الثالث: عشر درجات من عشر!'),
    ('caleb', 'Excuse me? Ten out of ten?', 'عفواً؟ عشر درجات من عشر؟'),
    ('hannah', 'What Arthur means is... we hope every guest feels ten out of ten here!', 'ما يقصده آرثر هو... نأمل أن يشعر كل ضيف هنا بعشر درجات من عشر!'),
    ('arthur', 'No, Hannah, let us be honest professionals! Sir, we respect the Portland Travel Guide!', 'لا يا هانا، دعينا نكن محترفين صادقين! سيدي، نحن نحترم دليل سفر بورتلاند!'),
    ('caleb', 'The Portland Travel Guide? Wait, do you think I am a hotel inspector?', 'دليل سفر بورتلاند؟ انتظروا، هل تظنون أنني مفتش فنادق؟'),
    ('hannah', "When your notebook fell open on the counter last night, we saw 'nine out of ten'...", 'عندما انفتح دفترك على المنضدة الليلة الماضية، لمحنا عبارة تسع من عشر...'),
    ('caleb', 'Oh! Come outside to the courtyard for a minute. Let me show you what I really do!', 'أوه! اخرجوا معي إلى الساحة دقيقةً واحدة. دعوني أريكم ما أعمله في الحقيقة!'),
]
WALK = [
    (0, None, ["'صباح الخير يا هانا! صباح الخير يا سيدي! يا له من صباح مشرق بعد المطر.' تفتتح صيغة التعجب", (None, 'What a bright morning'), 'الحديث بإشراقة ودودة.']),
    (1, None, ["'صباح الخير يا كاليب! هل نمتَ جيداً تحت عوارض السقف؟' التحية الصباحية المألوفة للنزلاء هي", (None, 'Did you sleep well'), 'بصيغة الماضي البسيط.']),
    (2, None, ["'أفضل نوم نمته طوال الشهر، وكان ماء الاستحمام ساخناً على نحو رائع!' تقترن صيغة التفضيل", (None, 'Best sleep I have had'), 'بالمضارع التام، ويقوي الظرف', (None, 'wonderfully hot'), 'الصفة بجمال.']),
    (3, None, ["'ساخن! هل تسمعين ذلك يا هانا؟ مياه ساخنة موثوقة وحديثة ومن خمس نجوم!' تختصر عبارة", (None, 'Hear that'), 'السؤال الكامل في لهجة احتفالية حماسية.']),
    (4, None, ["'تستغرق المباني الطوبية القديمة في العادة وقتاً طويلاً جداً لتسخن في الطابق العلوي.' التعبير الاصطلاحي", (None, 'take ages'), 'مبالغة محادثة لطيفة لطول الانتظار.']),
    (5, None, ["'أرجوك دوّن ذلك! الماء الساخن في الطابق الثالث: عشر درجات من عشر!' يعني الفعل المركب", (None, 'write that down'), 'تثبيت الملاحظة على الورق.']),
    (6, None, ["'عفواً؟ عشر درجات من عشر؟' بنبرة استفهام مرتفعة تعني عبارة", (None, 'Excuse me'), 'طلب توضيح لشيء مفاجئ غير مفهوم.']),
    (7, None, ["'ما يقصده آرثر هو... نأمل أن يشعر كل ضيف هنا بعشر درجات من عشر!' يبدأ التوضيح الدبلوماسي اللبق بعبارة", (None, 'What Arthur means is'), 'لإنقاذ الموقف بلطف.']),
    (8, None, ["'لا يا هانا، دعينا نكن محترفين صادقين! سيدي، نحن نحترم دليل سفر بورتلاند!' تجمع عبارة", (None, 'honest professionals'), 'بين الصراحة والاحتراف.']),
    (9, None, ["'دليل سفر بورتلاند؟ انتظروا، هل تظنون أنني مفتش فنادق؟' يكشف السؤال", (None, 'do you think I am'), 'منشأ الالتباس الطريف.']),
    (10, None, ["'عندما انفتح دفترك على المنضدة الليلة الماضية، لمحنا عبارة تسع من عشر...' تربط أداة الزمان", (None, 'When your notebook fell open'), 'بين المصادفة ورؤية الرقم.']),
    (11, None, ["'أوه! اخرجوا معي إلى الساحة دقيقةً واحدة. دعوني أريكم ما أعمله في الحقيقة!' يدعو التركيب", (None, 'Let me show you what I really do'), 'إلى كشف اللغز عياناً.']),
]
