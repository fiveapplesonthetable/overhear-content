# Authoring module for linden-courtyard-ar-s01e01-scene-06.
ID = 'linden-courtyard-ar-s01e01-scene-06'
SHOW = 'linden-courtyard-ar'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'The Luggage Tag  (بطاقة الأمتعة)'
LEVEL = 'A1 — مبتدئ'
PAIR = 'en-ar'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = 'أمام مكتب الاستقبال، يقرأ آرثر الخط الصغير المكتوب على بطاقة الحقيبة بنظارته، بينما تتصل هانا بمكتب المفقودات في محطة القطار. استمع إلى المشهد كاملاً باللغة الإنجليزية.'
OPENER = 'دعنا نفصّل الآن عبارات البحث والاتصال الهاتفي جملةً بعد جملة.'
TRANSITION = 'لنستمع الآن مرةً ثانية إلى المشهد كاملاً.'
OUTRO = 'لم يبلّغ أحد في المحطة عن الحقيبة بعد، غير أن تيسا لوّحت من ركن المقهى بفكرة لطيفة تخفف عن إيفلين تعب السفر. إلى اللقاء في المشهد السابع.'
CLOSING = ('arthur', 'See you soon!')
STORY = [
    ('arthur', 'Dear me, what a mix-up! Let me look at the tag with my glasses.', 'يا إلهي، يا له من التباس! دعوني أنظر إلى البطاقة بنظارتي.'),
    ('evelyn', 'Is there a name or a phone number on it?', 'هل يوجد عليها اسم أو رقم هاتف؟'),
    ('arthur', 'No phone number, unfortunately. Only two initials and an old street name.', 'لا يوجد رقم هاتف للأسف. حرفان أوليان فقط واسم شارع قديم.'),
    ('hannah', 'Wait, that street is right here in our neighborhood, five minutes away!', 'انتظروا، ذلك الشارع يقع هنا في حينا، على بعد خمس دقائق!'),
    ('evelyn', 'How strange! We rode the same morning train to the same district.', 'يا للغرابة! لقد ركبنا قطار الصباح نفسه إلى الحي نفسه.'),
    ('arthur', 'Hannah, call the station lost and found office right away.', 'يا هانا، اتصلي بمكتب المفقودات في المحطة فوراً.'),
    ('hannah', 'I am dialing now... Hello? Did anyone report a swapped blue suitcase?', 'أنا أتصل الآن... مرحباً؟ هل أبلغ أحد عن حقيبة زرقاء جرى تبديلها؟'),
    ('evelyn', 'Tell them mine has a red ribbon inside the top pocket!', 'أخبريهم أن حقيبتي فيها شريط أحمر داخل الجيب العلوي!'),
    ('hannah', 'Not yet? Please take our guesthouse number and address. Thank you!', 'ليس بعد؟ تفضل بتسجيل رقم هاتف نزلنا وعنوانه. شكراً لك!'),
    ('arthur', "They have nothing yet, ma'am, I am terribly sorry.", 'ليس لديهم أي خبر بعد يا سيدتي، أنا آسف للغاية.'),
    ('evelyn', 'It is not your fault. Still, I only have the coat on my back!', 'ليس هذا خطأكم. ومع ذلك، لا أملك سوى المعطف الذي أرتديه الآن!'),
    ('hannah', 'Wait one moment, Tessa in the cafe just waved to me with an idea!', 'انتظروا لحظةً واحدة، لقد لوّحت لي تيسا من المقهى للتو ومعها فكرة!'),
]
WALK = [
    (0, None, ["'يا إلهي، يا له من التباس! دعوني أنظر إلى البطاقة بنظارتي.' كلمة", (None, 'what a mix-up'), 'تعبير إنجليزي خفيف ولطيف لوصف تبادل الأغراض عن غير قصد.']),
    (1, None, ["'هل يوجد عليها اسم أو رقم هاتف؟' للسؤال عن وجود شيء مفرد نقدم الفعل على ظرف المكان في", (None, 'Is there a name'), 'مع نبرة استفهام واضحة.']),
    (2, None, ["'لا يوجد رقم هاتف للأسف. حرفان أوليان فقط واسم شارع قديم.' تشير كلمة", (None, 'two initials'), 'إلى أول حرف من الاسم الشخصي وأول حرف من اسم العائلة.']),
    (3, None, ["'انتظروا، ذلك الشارع يقع هنا في حينا، على بعد خمس دقائق!' تحدد عبارة المسافة الزمنية", (None, 'five minutes away'), 'قرب المكان بوضوح وسرعة.']),
    (4, None, ["'يا للغرابة! لقد ركبنا قطار الصباح نفسه إلى الحي نفسه.' للتعجب من أمر غير مألوف نقول", (None, 'How strange'), 'ثم يتكرر الوصف التطابقي في', (None, 'the same morning train'), 'لإبراز المصادفة.']),
    (5, None, ["'يا هانا، اتصلي بمكتب المفقودات في المحطة فوراً.' المصطلح الثابت لقسم الأشياء الضائعة هو", (None, 'lost and found office'), 'وتختم الجملة بـ', (None, 'right away'), 'لطلب السرعة.']),
    (6, None, ["'أنا أتصل الآن... مرحباً؟ هل أبلغ أحد عن حقيبة زرقاء جرى تبديلها؟' يعبر المضارع المستمر في", (None, 'I am dialing now'), 'عن عمل يجري في لحظة الكلام بالضبط.']),
    (7, None, ["'أخبريهم أن حقيبتي فيها شريط أحمر داخل الجيب العلوي!' يختصر ضمير الملكية المستقل", (None, 'mine has a red ribbon'), 'العبارة بذكاء لتوضيح العلامة الفارقة.']),
    (8, None, ["'ليس بعد؟ تفضل بتسجيل رقم هاتف نزلنا وعنوانه. شكراً لك!' يختزل الرد القصير جداً", (None, 'Not yet'), 'معنى «لم يحدث ذلك حتى هذه اللحظة» في كلمتين اثنتين.']),
    (9, None, ["'ليس لديهم أي خبر بعد يا سيدتي، أنا آسف للغاية.' يرفع الظرف في", (None, 'I am terribly sorry'), 'درجة اللباقة والتعاطف في الاعتذار الرسمي.']),
    (10, None, ["'ليس هذا خطأكم. ومع ذلك، لا أملك سوى المعطف الذي أرتديه الآن!' تواسي إيفلين الجميع بقولها", (None, 'It is not your fault'), 'وتصف حالها بالتعبير التصويري', (None, 'the coat on my back'), 'أي ما ترتديه في اللحظة الراهنة.']),
    (11, None, ["'انتظروا لحظةً واحدة، لقد لوّحت لي تيسا من المقهى للتو ومعها فكرة!' الفعل متبوعاً بحرف الجر في", (None, 'just waved to me'), 'يوضح لمن توجهت الإشارة عبر البهو.']),
]
