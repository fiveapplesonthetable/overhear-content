# Authoring module for linden-courtyard-zh-s01e04-scene-03.
ID = 'linden-courtyard-zh-s01e04-scene-03'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 4
SCENE = 3
TITLE = 'Hot Cinnamon Rolls  (热气腾腾的肉桂卷)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'tessa': 'Tessa', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = '就在汉娜往回赶的这几分钟里，早起的伊芙琳女士已经下楼来问为什么洗手间水龙头这么凉。泰莎和亚瑟赶紧端出刚出炉的热肉桂卷和热茶，巧妙拖延时间。我们先完整听一遍。'
OPENER = '现在放慢语速，一句一句品味泰莎和亚瑟机智周到的待客之道。'
TRANSITION = '听懂了这些幽默又礼貌的表达，我们再连贯听一遍。'
OUTRO = '亚瑟一边盯着手表一边夸七点十四分是个美妙的时刻，话音刚落，窗外就闪过了汉娜冲进庭院大门的身影！我们下场戏见。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('evelyn', 'Good morning! Something smells like warm cinnamon all the way upstairs!', '早上好！一股暖暖的肉桂香气一路飘到楼上去了！'),
    ('tessa', 'Good morning, Miss Evelyn! My cinnamon rolls just came out of the oven.', '早上好，伊芙琳女士！我的肉桂卷刚刚出烤箱。'),
    ('arthur', "Sit right down by the sunny window, ma'am! No rush to go upstairs yet!", '快请坐在向阳的窗边吧，夫人！先别急着上楼去！'),
    ('evelyn', 'Actually, I only came down to ask why the bathroom tap felt so chilly.', '其实，我下楼只是想问问为什么浴室水龙头摸着这么凉。'),
    ('arthur', 'Chilly? Ah, yes! Our neighborhood water pipes take a gentle morning stretch!', '微凉？啊，是呀！咱们这片老街区的水管早上都得温柔地伸个懒腰呢！'),
    ('tessa', 'Have a hot cup of tea and a cinnamon roll for ten minutes first!', '先喝杯热茶、吃个肉桂卷暖和十分钟吧！'),
    ('evelyn', 'Well, nobody wise says no to warm cinnamon bread at seven in the morning.', '嗯，聪明人可不会在早上七点拒绝热乎乎的肉桂面包。'),
    ('arthur', 'Wonderful choice! Would you like honey or apple jam beside it?', '绝佳的选择！您想在旁边配点蜂蜜还是苹果酱呢？'),
    ('evelyn', 'Just a little butter, thank you. Why are you looking at your watch, sir?', '只要一点点黄油就好，谢谢。先生，您为什么一直看手表呀？'),
    ('arthur', 'Me? Oh, I simply love being on time! Seven fourteen is a beautiful minute!', '我吗？噢，我纯粹是热爱守时！七点十四分真是美妙的一分钟啊！'),
    ('tessa', 'Look through the courtyard window, Arthur. Someone just ran through the gate!', '快透过庭院窗户往外看，亚瑟。刚有人跑进大门啦！'),
    ('arthur', "Saved! Excuse me one moment, ma'am, enjoy your hot tea!", '得救啦！失陪一小会儿，夫人，请慢用您的热茶！'),
]
WALK = [
    (0, None, ["'早上好！一股暖暖的肉桂香气一路飘到楼上去了！' 描述闻起来像某种具体食物的香味，在感官动词后加上介词，说出", (None, 'smells like warm cinnamon'), '让人仿佛隔着声音都能闻到甜香。']),
    (1, None, ["'早上好，伊芙琳女士！我的肉桂卷刚刚出烤箱。' 形容烘焙点心新鲜出炉，美式口语常用副词搭配一般过去时说出", (None, 'just came out'), '凸显热乎劲儿十足的新鲜感。']),
    (2, None, ["'快请坐在向阳的窗边吧，夫人！先别急着上楼去！' 热情招呼客人就座时，在动词和副词中间插进强调词，说成", (None, 'Sit right down'), '听起来比普通请坐更加殷勤热络。']),
    (3, None, ["'其实，我下楼只是想问问为什么浴室水龙头摸着这么凉。' 委婉道出自己真正的来意或纠正别人的话头时，句首放一个副词", (None, 'Actually'), '语气优雅自然，意思是“说起来、其实呢”。']),
    (4, None, ["'微凉？啊，是呀！咱们这片老街区的水管早上都得温柔地伸个懒腰呢！' 形容带着几分寒意的凉飕飕，英语常用形容词", (None, 'Chilly'), '亚瑟顺着这个词急中生智编了个风趣的借口。']),
    (5, None, ["'先喝杯热茶、吃个肉桂卷暖和十分钟吧！' 热情劝客人享用热饮茶点时，英语不用生硬的喝和吃，而是用百搭动词说出", (None, 'Have a hot cup'), '显得亲切好客又大方。']),
    (6, None, ["'嗯，聪明人可不会在早上七点拒绝热乎乎的肉桂面包。' 修饰复合不定代词时，形容词必须老老实实排在代词后面，组成", (None, 'nobody wise'), '风趣表达“凡是明智的人都不会拒绝”。']),
    (7, None, ["'绝佳的选择！您想在旁边配点蜂蜜还是苹果酱呢？' 餐饮服务中询问客人喜好和点单需求，最礼貌得体的黄金句式永远是", (None, 'Would you like'), '比直白的你要不要优雅得多。']),
    (8, None, ["'只要一点点黄油就好，谢谢。先生，您为什么一直看手表呀？' 礼貌表示自己只需要少许配料时，用副词搭配不可数定量短语说出", (None, 'Just a little butter'), '既温和又有分寸感。']),
    (9, None, ["'我吗？噢，我纯粹是热爱守时！七点十四分真是美妙的一分钟啊！' 在喜爱一词后面接系动词的动名词形式，组成", (None, 'love being on time'), '亚瑟强装镇定地掩饰自己盯着表等救兵的心慌。']),
    (10, None, ["'快透过庭院窗户往外看，亚瑟。刚有人跑进大门啦！' 目光穿过玻璃窗看向外面的院子，英语使用表示穿透空间的介词，说成", (None, 'through the courtyard window'), '精准描绘出隔窗望见的画面。']),
    (11, None, ["'得救啦！失陪一小会儿，夫人，请慢用您的热茶！' 离开餐桌前祝客人愉快享用饮品或美食，一句温暖地道的", (None, 'enjoy your hot tea'), '正好对应汉语服务里的“请您慢用”。']),
]
