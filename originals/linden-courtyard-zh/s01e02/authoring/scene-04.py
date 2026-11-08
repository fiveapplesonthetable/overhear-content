# Authoring module for linden-courtyard-zh-s01e02-scene-04.
ID = 'linden-courtyard-zh-s01e02-scene-04'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 2
SCENE = 4
TITLE = 'Herbs from the Courtyard  (庭院里的新鲜香草)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'graham': 'Graham', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = '院子里的格雷厄姆听到厨房嚷嚷黄油的事，特意剪来一把刚摘的翠绿新鲜香草，给法式炒蛋添上画龙点睛的一笔。七点二十九分，客人们正走下楼梯！先听一遍吧。'
OPENER = '现在我们逐句拆解开餐前一分钟井然有序的准备对话。'
TRANSITION = '熟悉了餐具摆放和厨房配合的说法，我们再完整听一遍整场戏。'
OUTRO = '四张餐桌、八把椅子全部摆放就位，热气腾腾的早餐准时迎客，汉娜也收获了格雷厄姆难得的一句夸奖。我们回头见。'
CLOSING = ('graham', 'See you soon!')
STORY = [
    ('graham', 'I heard shouting about butter from all the way out in the courtyard.', '我在外面的庭院里大老远就听见屋里在嚷嚷黄油的事了。'),
    ('tessa', 'Hannah bought sea salt butter, so today we are making French style eggs!', '汉娜买了海盐黄油，所以今天咱们改做法式炒蛋！'),
    ('graham', 'Good. Put these fresh green herbs on top before you serve them.', '挺好。端上桌之前，把这些新鲜翠绿的香草撒在上面。'),
    ('hannah', 'Did you grow those herbs yourself, Graham?', '格雷厄姆，那些香草是你自己亲手种的吗？'),
    ('graham', 'Somebody has to take care of the courtyard plants.', '庭院里的花草总得有人照料嘛。'),
    ('tessa', 'Smell that! Warm bread, hot eggs, and fresh herbs.', '你闻闻！温热的面包、热腾腾的炒蛋，还有清新的香草。'),
    ('hannah', 'Where do the small spoons and napkins go?', '小勺子和餐巾该摆放在哪儿呢？'),
    ('tessa', 'Put one napkin and one small spoon beside every blue cup.', '在每个蓝杯子旁边放一块餐巾和一把小勺子。'),
    ('graham', 'Seven twenty-nine on my watch. Guests are coming down the stairs.', '我手表上七点二十九分了。住客们正走下楼梯呢。'),
    ('hannah', 'Four tables, eight chairs, everything in place!', '四张餐桌，八把椅子，一切摆放就位！'),
    ('tessa', 'Pour the hot water into the teapot, Hannah, here they come!', '汉娜，快把热水倒进茶壶里，客人们过来啦！'),
    ('graham', 'Not bad for day two, rookie.', '上班第二天能干成这样，很不赖嘛，新手。'),
]
WALK = [
    (0, None, ["'我在外面的庭院里大老远就听见屋里在嚷嚷黄油的事了。' 感官动词过去式后面接现在分词构成", (None, 'I heard shouting'), '生动再现刚才院外隐约听见屋里一阵阵喧哗的场景。']),
    (1, None, ["'汉娜买了海盐黄油，所以今天咱们改做法式炒蛋！' 购买一词的不规则过去式", (None, 'bought'), '拼写虽然长，但中间四个字母组合完全不发辅音，干脆读出一个单音节即可。']),
    (2, None, ["'挺好。端上桌之前，把这些新鲜翠绿的香草撒在上面。' 留意定语顺序", (None, 'fresh green herbs'), '先说新鲜程度再说颜色，而且美式口语里香草词首字母不发音；后面用', (None, 'on top'), '简洁表示撒在炒蛋最上面。']),
    (3, None, ["'格雷厄姆，那些香草是你自己亲手种的吗？' 这里把反身代词", (None, 'yourself'), '放在句尾并不是作宾语，而是专门用来加强语气，夸问是不是“你本人亲自动手”栽种的。']),
    (4, None, ["'庭院里的花草总得有人照料嘛。' 日常照看花草、宠物或家人，最通用的三词短语就是", (None, 'take care of'), '格雷厄姆嘴上淡淡一句，足见平时打理院子有多用心。']),
    (5, None, ["'你闻闻！温热的面包、热腾腾的炒蛋，还有清新的香草。' 体会英语里两种热度的细腻差别：", (None, 'Warm bread'), '是柔和宜人的温热面包，而刚出锅滚烫冒气的鸡蛋则说', (None, 'hot eggs'), '冷暖温度层次格外分明。']),
    (6, None, ["'小勺子和餐巾该摆放在哪儿呢？' 询问物品平时固定归放在哪个位置，英语最地道的问法就是用动词去构成", (None, 'Where do the small spoons and napkins go'), '比生硬地问放在何处自然得多。']),
    (7, None, ["'在每个蓝杯子旁边放一块餐巾和一把小勺子。' 表示紧挨在茶杯左手或右手一侧，直接用方位介词", (None, 'beside'), '单个词就能交代得清清楚楚。']),
    (8, None, ["'我手表上七点二十九分了。住客们正走下楼梯呢。' 英语说看手表上显示的时间，固定搭配介词说出", (None, 'on my watch'), '仿佛指针和数字就印在表盘表面上。']),
    (9, None, ["'四张餐桌，八把椅子，一切摆放就位！' 短小精悍的介词短语", (None, 'in place'), '专门用来形容桌椅餐具全都各归其位、整整齐齐。']),
    (10, None, ["'汉娜，快把热水倒进茶壶里，客人们过来啦！' 倾倒液体用动词", (None, 'Pour'), '后面配合动态方向介词', (None, 'into'), '准确画出热水从水壶注入茶壶内部的动作轨迹。']),
    (11, None, ["'上班第二天能干成这样，很不赖嘛，新手。' 平时不苟言笑的前辈说出一句", (None, 'Not bad'), '其实已经是相当高的肯定了；句尾亲切调侃一声', (None, 'rookie'), '证明汉娜已经赢得了大家的认可。']),
]
