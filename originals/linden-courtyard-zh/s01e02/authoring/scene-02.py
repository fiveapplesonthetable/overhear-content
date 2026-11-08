# Authoring module for linden-courtyard-zh-s01e02-scene-02.
ID = 'linden-courtyard-zh-s01e02-scene-02'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = 'No Milk in the Fridge  (冰箱里没牛奶了)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = '离七点半开早饭只剩二十分钟，厨房里突然传来了泰莎的惊呼：送奶货车在镇外爆胎了，而冰箱里几乎空空如也！先完整听一遍这场紧急动员吧。'
OPENER = '现在让我们一句一句来听大家如何分秒必争化解厨房危机。'
TRANSITION = '记住了采购清单上的每一项食材，我们再连贯听一遍整场戏。'
OUTRO = '汉娜揣上五十美元现金、拎起购物袋冲出了大门。她真能在十分钟之内跑个来回吗？我们待会儿见。'
CLOSING = ('hannah', 'See you later!')
STORY = [
    ('tessa', 'Oh no! Arthur, Hannah, we have a kitchen emergency!', '噢糟糕！亚瑟，汉娜，咱们厨房出紧急状况了！'),
    ('arthur', 'Please do not say the word emergency before my morning coffee!', '在我喝上早间咖啡之前，求你千万别提“紧急状况”这个词！'),
    ('tessa', 'The dairy van has a flat tire outside town. Look in the fridge!', '送乳品的货车在镇外爆胎了。你们看冰箱里！'),
    ('hannah', 'One tiny splash of milk, two eggs, and no butter at all!', '只有一丁点儿牛奶、两个鸡蛋，而且黄油一点儿都没了！'),
    ('arthur', 'Eight hungry guests will come down the stairs at seven thirty!', '八位饥肠辘辘的住客七点半就要顺着楼梯下来了！'),
    ('tessa', 'My bread dough is ready in the oven, at least.', '起码我的面包面团已经在烤箱里准备好了。'),
    ('hannah', 'Give me a bag and some cash! The corner market opens at seven.', '快给我一个袋子和一点现金！街角集市七点开门。'),
    ('arthur', 'Can you run there and back in ten minutes?', '你能在十分钟之内跑个来回吗？'),
    ('hannah', 'Watch me! Tell me exactly what to buy.', '看我的吧！快告诉我具体要买什么。'),
    ('tessa', 'Three bottles of milk, twenty eggs, butter, cheese, and red apples!', '三瓶牛奶、二十个鸡蛋、黄油、奶酪，还有红苹果！'),
    ('arthur', 'Here is fifty from the cash box. Bring back the receipt!', '从现金盒里拿五十美元给你。记得把收据带回来！'),
    ('hannah', 'Hold the fort, I am already out the door!', '你们守好摊子，我已经冲出门啦！'),
]
WALK = [
    (0, None, ["'噢糟糕！亚瑟，汉娜，咱们厨房出紧急状况了！' 英语常把场所名词直接摆在前面修饰突发事件，说出", (None, 'kitchen emergency'), '一下子把火烧眉毛的紧张感拉满了。']),
    (1, None, ["'在我喝上早间咖啡之前，求你千万别提“紧急状况”这个词！' 礼貌而恳切地请对方别做某事，句首用请字加上否定祈使结构", (None, 'Please do not say'), '亚瑟这句起床气十足的哀叹格外真实幽默。']),
    (2, None, ["'送乳品的货车在镇外爆胎了。你们看冰箱里！' 形容车胎没气瘪掉了，英语不用“破”而用“平的”，固定说成", (None, 'a flat tire'), '形象描绘轮胎瘪平贴地的样子。']),
    (3, None, ["'只有一丁点儿牛奶、两个鸡蛋，而且黄油一点儿都没了！' 先用否定词加不可数名词说出", (None, 'no butter'), '句末再补上加强语气的短语', (None, 'at all'), '彻底强调连半星黄油都不剩了。']),
    (4, None, ["'八位饥肠辘辘的住客七点半就要顺着楼梯下来了！' 形容词直接放在复数名词前组成", (None, 'hungry guests'), '提醒大家八位饿着肚子的客人马上就要下楼开饭了。']),
    (5, None, ["'起码我的面包面团已经在烤箱里准备好了。' 在忙乱局面中找出一桩好消息给自己打气时，把", (None, 'at least'), '放在句尾或句首，就相当于汉语里的“至少、好在还有”。']),
    (6, None, ["'快给我一个袋子和一点现金！街角集市七点开门。' 现金在英语里属于不可数名词，不能论个计数，所以汉娜用模糊定量词说出", (None, 'some cash'), '表示拿些钞票应急。']),
    (7, None, ["'你能在十分钟之内跑个来回吗？' 短小精悍的副词组合", (None, 'there and back'), '字面意思是“去那儿再回来”，在口语里专门表示往返跑一趟。']),
    (8, None, ["'看我的吧！快告诉我具体要买什么。' 自信满满地接下任务时说一句", (None, 'Watch me'), '干劲十足；后半句用疑问词加不定式结构', (None, 'what to buy'), '简洁明了地请对方报出采购清单。']),
    (9, None, ["'三瓶牛奶、二十个鸡蛋、黄油、奶酪，还有红苹果！' 牛奶本身不可数，采购多瓶时要把容器变成复数，说成", (None, 'Three bottles of milk'), '而后面的鸡蛋和苹果则是直接计数的可数名词。']),
    (10, None, ["'从现金盒里拿五十美元给你。记得把收据带回来！' 动词加上表示返回的副词构成", (None, 'Bring back'), '叮嘱汉娜买完东西务必把小票一并带回店里记账。']),
    (11, None, ["'你们守好摊子，我已经冲出门啦！' 经典口语习语", (None, 'Hold the fort'), '原指守卫要塞堡垒，现代日常口语里常用来招呼同伴“你们先看顾好店里，我去去就回”。']),
]
