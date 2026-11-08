# Authoring module for linden-courtyard-zh-s01e01-scene-05.
ID = 'linden-courtyard-zh-s01e01-scene-05'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = 'Not My Clothes!  (这不是我的衣服！)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '刚上二楼四号房没过几分钟，前台的呼叫铃就急促地响了起来。汉娜和格雷厄姆赶紧上楼查看，只见伊芙琳对着敞开的蓝色行李箱目瞪口呆。先完整听一遍吧。'
OPENER = '现在让我们一句一句听听箱子里到底装了什么让人吃惊的东西。'
TRANSITION = '理清了每一句的词汇和语气，我们再按正常语速听一遍整场戏。'
OUTRO = '原来在火车站有人错拿了一模一样的深蓝行李箱！汉娜和格雷厄姆准备把箱子提回楼下光线充足的前台，仔细查查提手上的小吊牌。我们下场戏见。'
CLOSING = ('hannah', 'Goodbye!')
STORY = [
    ('hannah', 'Miss Evelyn, is everything all right? You rang the bell!', '伊芙琳女士，一切还好吗？您刚才按了铃！'),
    ('evelyn', 'Look inside this suitcase, Hannah! This is not my bag!', '快看这只行李箱里面，汉娜！这不是我的包！'),
    ('hannah', 'Wait, it is dark blue, just like yours!', '等等，它是深蓝色的呀，跟您的一模一样！'),
    ('evelyn', 'The outside is identical, yes! But look inside!', '外表是一模一样，没错！可你看看里面！'),
    ('graham', "Two pairs of big brown men's shoes and gray sweaters.", '两双大号棕色男士皮鞋，还有几件灰毛衣。'),
    ('hannah', 'And what is this wrapped in white paper? A little wooden train!', '那这个用白纸包着的是什么？一列小木头火车！'),
    ('evelyn', 'I certainly do not wear size eleven shoes!', '我肯定不穿十一码的大鞋呀！'),
    ('graham', 'No wonder it was so heavy. Wood and leather!', '难怪刚才拎着那么沉。全是木头和皮革呀！'),
    ('evelyn', 'Someone at the train station took my blue suitcase by mistake!', '火车站有人不小心错拿了我的蓝色行李箱！'),
    ('hannah', "Please sit down, ma'am. Do not worry, we will check the tag right now.", '女士，请您先坐下。别担心，我们马上查看行李牌。'),
    ('graham', 'There is a small paper card tied to the side handle.', '侧边提手上系着一张小纸卡。'),
    ('evelyn', 'Oh, let us bring it downstairs to the light!', '噢，咱们把它拿到楼下亮堂的地方看吧！'),
]
WALK = [
    (0, None, ["'伊芙琳女士，一切还好吗？您刚才按了铃！' 对熟识的女性住客，在名字前加上尊称唤作", (None, 'Miss Evelyn'), '既礼貌又亲切；句末用不规则过去式', (None, 'rang'), '表示您刚刚按响了呼叫铃。']),
    (1, None, ["'快看这只行李箱里面，汉娜！这不是我的包！' 英语否定判断句只要在单数系动词后面直接加上否定词，说出", (None, 'This is not'), '语气干脆明确，一下子道出事情不对劲。']),
    (2, None, ["'等等，它是深蓝色的呀，跟您的一模一样！' 为了避免重复再说一遍“您的包”，英语改用独立物主代词", (None, 'yours'), '单独挑起“您的那只箱子”的意思，简洁又自然。']),
    (3, None, ["'外表是一模一样，没错！可你看看里面！' 留意这两个反义词的灵活切换：前一句加定冠词作名词主语", (None, 'The outside'), '表示箱子外部，后半句用副词', (None, 'inside'), '让对方往箱子里面瞧。']),
    (4, None, ["'两双大号棕色男士皮鞋，还有几件灰毛衣。' 男人一词先通过改变中间元音变成不规则复数，再加撇号所有格构成", (None, "men's shoes"), '用来专指“男士尺码的鞋子”。']),
    (5, None, ["'那这个用白纸包着的是什么？一列小木头火车！' 在木材一词后面加上表材质的词尾，就变成了定语形容词，组成", (None, 'wooden train'), '专门形容手工木头做的小火车。']),
    (6, None, ["'我肯定不穿十一码的大鞋呀！' 英语表达把鞋帽、衣服或眼镜穿戴在身上，统一使用动词", (None, 'wear'), '伊芙琳哭笑不得的一句话把大家都逗乐了。']),
    (7, None, ["'难怪刚才拎着那么沉。全是木头和皮革呀！' 恍然大悟找到原因时，句首脱口而出一句", (None, 'No wonder'), '就等于汉语里常说的“怪不得、难怪呢”，后面直接跟完整句子即可。']),
    (8, None, ["'火车站有人不小心错拿了我的蓝色行李箱！' 固定介词搭配", (None, 'by mistake'), '放在句尾修饰动作，地道说明对方并非故意，而是阴差阳错“误拿、拿混了”。']),
    (9, None, ["'女士，请您先坐下。别担心，我们马上查看行李牌。' 遇到突发状况安抚客人时，最温暖管用的一句定心丸就是", (None, 'Do not worry'), '先让对方悬着的心放下来。']),
    (10, None, ["'侧边提手上系着一张小纸卡。' 英语描述“某处存在某物”不说某地有，而是用引导词加系动词的句型", (None, 'There is'), '后面紧跟单数名词一张小纸卡。']),
    (11, None, ["'噢，咱们把它拿到楼下亮堂的地方看吧！' 提议大家一起动手做某事时，可以用祈使结构", (None, 'let us bring it downstairs'), '注意“往楼下”本身就是地点副词，前面绝不加介词。']),
]
