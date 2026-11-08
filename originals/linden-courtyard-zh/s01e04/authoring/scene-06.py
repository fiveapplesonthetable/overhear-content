# Authoring module for linden-courtyard-zh-s01e04-scene-06.
ID = 'linden-courtyard-zh-s01e04-scene-06'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = 'The Acoustic Architect  (声学建筑师)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '在菩提树下，凯勒布翻开笔记本给汉娜和泰莎细看：原来本子上测量的不是旅馆星级，而是分贝与庭院静音度！更巧的是，他提到自己童年就住在两条街外，而且星期五对他意义非凡。我们先完整听一遍。'
OPENER = '现在放慢节奏，一句一句拆解凯勒布的真实身份和意外线索。'
TRANSITION = '理清了这些细腻的口语表达，我们再连贯听一遍。'
OUTRO = '亚瑟竟然为了分贝数字白白紧张了一整夜！可凯勒布口中那个重要的“星期五”，立刻让泰莎联想到了那只神秘的蓝色行李箱。我们待会儿见。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('caleb', 'Look closely at this page. It measures decibels and quietness, not hotel stars!', '仔细看这一页。上面测量的是分贝和安静程度，可不是旅馆星级！'),
    ('hannah', "Decibels? So 'nine out of ten' was not a review of my front desk?", '分贝？所以“十分中的九分”并不是对我前台工作的评价喽？'),
    ('caleb', 'Well, your front desk deserves ten! Honestly, though, I am an acoustic architect.', '嗯，你的前台服务绝对配得上十分！不过老实说，我是一名声学建筑师。'),
    ('tessa', 'An acoustic architect! Do you design concert halls?', '声学建筑师！您是设计音乐厅的吗？'),
    ('caleb', 'Small libraries and courtyards, mostly. I measure how old stone walls block street noise.', '主要是小型图书馆和庭院。我专门测量老石墙是怎么隔绝街道噪音的。'),
    ('hannah', 'That is why you listened for cars up in the attic last night!', '怪不得您昨晚在阁楼上特意倾听街上有没有汽车声呢！'),
    ('caleb', 'Exactly. Outside on the avenue it is loud, yet inside this courtyard you hear leaves and birds.', '一点没错。外面的大道上车水马龙很吵闹，可是在这座庭院里却只听得见树叶和鸟鸣。'),
    ('tessa', 'Wait until Arthur hears he panicked all night over decibels!', '等着瞧亚瑟听说自己为分贝白慌了一整夜会是什么表情吧！'),
    ('caleb', 'Truthfully, I also chose this neighborhood for an old family reason.', '说实在的，我挑中这片街区，也是为了一个老旧的家族缘故。'),
    ('hannah', 'Oh? Did your family live near here once?', '噢？您的家人以前在这附近住过吗？'),
    ('caleb', 'Two streets away, when I was small. Friday is... an important day for me.', '就在两条街外，在我还小的时候。星期五对我来说……是个重要的日子。'),
    ('tessa', 'Wait, did he just say Friday?!', '等等，他刚才是不是说了星期五？！'),
]
WALK = [
    (0, None, ["'仔细看这一页。上面测量的是分贝和安静程度，可不是旅馆星级！' 请别人凑近一点端详细节时，用副词修饰看这个动作，说出", (None, 'Look closely'), '这里的副词表示“凑近仔细地观察”。']),
    (1, None, ["'分贝？所以“十分中的九分”并不是对我前台工作的评价喽？' 汉娜恍然大悟，用过去时否定结构确认", (None, 'was not a review'), '这里的名词专门指顾客对店铺或旅馆写的点评。']),
    (2, None, ["'嗯，你的前台服务绝对配得上十分！不过老实说，我是一名声学建筑师。' 英语口语常把转折词", (None, 'though'), '轻轻夹在句子中间作副词，比句首生硬的但是柔和得多，自然带出“不过呢”的语气。']),
    (3, None, ["'声学建筑师！您是设计音乐厅的吗？' 举办交响乐和钢琴独奏的大型演出场馆，英语固定称为", (None, 'concert halls'), '一听到声学设计，大家第一反应往往就是它。']),
    (4, None, ["'主要是小型图书馆和庭院。我专门测量老石墙是怎么隔绝街道噪音的。' 口语回答问题时常把主要内容先说出来，句尾再补上一个副词", (None, 'mostly'), '随和地说明“大多数情况下是这些”。']),
    (5, None, ["'怪不得您昨晚在阁楼上特意倾听街上有没有汽车声呢！' 突然明白前因后果时，脱口而出一句", (None, 'That is why'), '相当于汉语的“怪不得、难怪”；而留神搜寻有没有某个声音要用介词搭配成', (None, 'listened for cars'), '强调竖起耳朵去捕捉车声。']),
    (6, None, ["'一点没错。外面的大道上车水马龙很吵闹，可是在这座庭院里却只听得见树叶和鸟鸣。' 连接两个形成鲜明反差的分句时，连词", (None, 'yet'), '既有转折含义又带有一丝诗意，突显一墙之隔的幽静。']),
    (7, None, ["'等着瞧亚瑟听说自己为分贝白慌了一整夜会是什么表情吧！' 期待某人得知真相时的好戏场面，口语爱用祈使句式", (None, 'Wait until Arthur hears'), '注意时间状语从句里用一般现在时代替将来时。']),
    (8, None, ["'说实在的，我挑中这片街区，也是为了一个老旧的家族缘故。' 留心选择这个不规则动词，它的过去式拼写和发音都变成了", (None, 'chose'), '讲述自己当初预订房间时的特意挑选。']),
    (9, None, ["'噢？您的家人以前在这附近住过吗？' 放在疑问句末尾的副词", (None, 'once'), '在这里不是指一次，而是表示过去某个时期“曾经、以前”。']),
    (10, None, ["'就在两条街外，在我还小的时候。星期五对我来说……是个重要的日子。' 回忆童年时光，最朴素亲切的说法就是", (None, 'when I was small'), '比正式的幼年时期更有温暖的生活气息。']),
    (11, None, ["'等等，他刚才是不是说了星期五？！' 不敢相信自己的耳朵、向身旁同伴求证刚才那句话时，用助动词重读问出", (None, 'did he just say'), '瞬间把星期五之约的线索串联起来了。']),
]
