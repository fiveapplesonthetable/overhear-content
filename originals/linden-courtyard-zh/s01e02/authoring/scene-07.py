# Authoring module for linden-courtyard-zh-s01e02-scene-07.
ID = 'linden-courtyard-zh-s01e02-scene-07'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = 'How Regulars Order  (老熟客的点单默契)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '到了安静的午后歇息时光，泰莎招呼早上跑遍半座城买牛奶的汉娜坐下来喝杯热咖啡，格雷厄姆则掏出随身携带的螺丝刀修好了角落晃动的木椅。先完整听一遍吧。'
OPENER = '现在让我们一句一句品味同事间轻松诙谐的午后闲聊。'
TRANSITION = '听懂了大家互相打趣的幽默，我们再连贯听一遍整场对话。'
OUTRO = '嘴上说从不多管闲事的格雷厄姆，其实心里比谁都好奇星期五中午那位箱子主人是谁！休息片刻后，傍晚的前台又出新状况了，我们待会儿见。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('tessa', 'Sit down, Hannah! You ran half the city this morning, drink some coffee.', '快坐下吧，汉娜！你今天早上跑了大半座城，喝点咖啡歇歇。'),
    ('hannah', 'Gladly! With milk and a little sugar, please.', '太乐意了！请加点牛奶和一点儿糖。'),
    ('graham', 'Watch that corner chair, wait ten seconds while I tighten this screw.', '当心角落那把椅子，等十秒钟让我把这颗螺丝拧紧。'),
    ('hannah', 'Done already? You carry a screwdriver everywhere, Graham!', '这么快就弄好啦？格雷厄姆，你去哪儿都随身带着螺丝刀呀！'),
    ('graham', 'Old houses loosen one screw every Tuesday. Now sit.', '老房子每到星期二就爱松一颗螺丝。好了，坐吧。'),
    ('tessa', 'Look, you survived the breakfast rush and the mystery phone call!', '你看，你顺利扛过了早餐高峰期，还接下了那通神秘电话！'),
    ('hannah', 'Honestly, I like it here much better than my old gray office.', '说实话，我喜欢这儿，比我以前那间灰扑扑的旧办公室好太多了。'),
    ('tessa', 'Wait until Friday at noon, I want a front row seat when the suitcase man walks in!', '等着瞧星期五中午吧，等那位行李箱男士走进门来的时候，我可得占个第一排座位！'),
    ('graham', 'Nobody stares at guests. We hand over the bag and mind our business.', '谁也不许盯着住客看。我们把包交还人家，管好咱们自己的本分事。'),
    ('tessa', 'Listen to him! Graham is twice as curious as we are!', '听听他说的！格雷厄姆心里比咱们俩好奇两倍呢！'),
    ('graham', 'I am simply checking security. That is my job.', '我只不过是在例行检查安全状况。那是我的本职工作。'),
    ('hannah', 'Sure, Graham, your secret is safe with us!', '行啦，格雷厄姆，你的秘密在我们这儿绝对安全！'),
]
WALK = [
    (0, None, ["'快坐下吧，汉娜！你今天早上跑了大半座城，喝点咖啡歇歇。' 泰莎用夸张又心疼的说法", (None, 'half the city'), '夸汉娜大清早来回飞奔，注意定冠词直接跟在一半这个词的后面。']),
    (1, None, ["'太乐意了！请加点牛奶和一点儿糖。' 点咖啡想要微甜口味时，在不可数名词糖前面加上定量短语", (None, 'a little sugar'), '礼貌又清晰地说明只要少许一点糖。']),
    (2, None, ["'当心角落那把椅子，等十秒钟让我把这颗螺丝拧紧。' 形容词“紧的”加上动词词尾就变成及物动词", (None, 'tighten'), '专门用来表示把松动的螺丝或瓶盖拧紧固定好。']),
    (3, None, ["'这么快就弄好啦？格雷厄姆，你去哪儿都随身带着螺丝刀呀！' 复合工具名词", (None, 'screwdriver'), '由螺丝和拧动器两个词直接拼成，正是维修主管寸步不离的看家法宝。']),
    (4, None, ["'老房子每到星期二就爱松一颗螺丝。好了，坐吧。' 与刚才的拧紧正好相反，形容词“松的”加词尾变成动词", (None, 'loosen'), '格雷厄姆一本正经地拿', (None, 'every Tuesday'), '开玩笑，把老房子的脾气说得活灵活现。']),
    (5, None, ["'你看，你顺利扛过了早餐高峰期，还接下了那通神秘电话！' 英语日常口语特别爱用略带幽默的说法", (None, 'survived the breakfast rush'), '把挺过忙乱的早晨说得像打赢了一场胜仗。']),
    (6, None, ["'说实话，我喜欢这儿，比我以前那间灰扑扑的旧办公室好太多了。' 想在比较级前面加强语气表示“好得多”，英语不能用“很”，而要改用程度词构成", (None, 'much better than'), '再引出对比的旧办公室。']),
    (7, None, ["'等着瞧星期五中午吧，等那位行李箱男士走进门来的时候，我可得占个第一排座位！' 后半句的时间从句", (None, 'when the suitcase man walks in'), '用一般现在时来描绘周五中午那令人期待的一幕，把行李箱直接放在男士前作外号也十分地道。']),
    (8, None, ["'谁也不许盯着住客看。我们把包交还人家，管好咱们自己的本分事。' 前面的动词短语", (None, 'stares at'), '指直勾勾地盯着别人看；后半句习语', (None, 'mind our business'), '则是地道口语“各司其职、不多管闲事”。']),
    (9, None, ["'听听他说的！格雷厄姆心里比咱们俩好奇两倍呢！' 英语表达倍数比较时，把表示两倍的词放在原级比较结构最前面，说出", (None, 'twice as curious as'), '一针见血拆穿了格雷厄姆的嘴硬。']),
    (10, None, ["'我只不过是在例行检查安全状况。那是我的本职工作。' 格雷厄姆一本正经地搬出可数名词短语", (None, 'my job'), '强调这属于自己的工作职责，冷面幽默让人忍俊不禁。']),
    (11, None, ["'行啦，格雷厄姆，你的秘密在我们这儿绝对安全！' 朋友之间善意打趣或承诺守口如瓶时，最地道的一句俏皮话就是", (None, 'your secret is safe with us'), '既亲近又默契十足。']),
]
