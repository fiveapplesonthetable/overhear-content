# Authoring module for linden-courtyard-zh-s01e06-scene-08.
ID = 'linden-courtyard-zh-s01e06-scene-08'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = 'Room Nine  (九号房)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = '送走庭院里的客人后，格雷厄姆去地下锅炉房后面搬备用折叠椅，却在老砖墙后意外翻出了一只尘封十五年的雪松木箱。第一季大结局的悬念正式揭开，先完整听一遍吧。'
OPENER = '现在让我们一句一句拆解这场充满寻宝气息的压轴大戏。'
TRANSITION = '听清了木箱上的铭牌、钥匙与暗门蓝图，我们再完整听一遍整场戏。'
OUTRO = '明明只有八间客房的菩提树庭院客栈，竟然出现了刻着“九号房”的木箱、第九把黄铜钥匙和一扇画在平面图上的神秘暗门！汉娜的第二周冒险才刚刚开始。感谢一路收听，我们明天见！'
CLOSING = ('graham', 'Until tomorrow!')
STORY = [
    ('hannah', 'Did you find the three folding chairs behind the boiler room, Graham?', '您在锅炉房后面找到那三把折叠椅了吗，格雷厄姆？'),
    ('graham', 'Found the chairs, and behind an old brick wall, I found this.', '椅子找到了，而且在一堵老砖墙后面，我还发现了这个。'),
    ('arthur', 'A small cedar chest? I have never seen that box in fifteen years!', '一只小小的雪松木箱？我在这儿十五年了，从来没见过这只箱子！'),
    ('hannah', 'Brush the dust off the brass plate on top... wait, read that number!', '把顶上黄铜铭牌的灰尘拂掉……等等，快念念那个数字！'),
    ('arthur', "Let me pull my glasses down from my forehead... 'Room Nine'?!", '让我把眼镜从额头上拉下来看看……“九号房”？！'),
    ('hannah', 'Graham, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!', '格雷厄姆，快看咱们身后的木头钥匙牌：一、二、三、四、五、六、七、八！'),
    ('arthur', 'This guesthouse has only ever had eight rooms! Where on earth is Room Nine?!', '这家客栈从来就只有八间客房呀！九号房究竟在哪里？！'),
    ('graham', 'Listen when I tilt the box. Something metal just slid inside.', '我把箱子倾斜的时候你们仔细听。里面刚刚有什么金属物件滑了一下。'),
    ('hannah', 'There is a tiny keyhole on the front latch, and look taped underneath: an old brass key!', '正面锁扣上有一个小小的锁眼，再看箱底贴着什么：一把老黄铜钥匙！'),
    ('arthur', 'A ninth brass key?! Do we open it tonight or wait until morning?!', '第九把黄铜钥匙？！咱们是今晚就打开它，还是等到明天早上？！'),
    ('graham', 'Look at the folded blueprint sticking out of the hinge. There is a hidden door drawn on this floor!', '快看从合页缝里露出来的那张折叠蓝图。这一层平面图上画着一扇暗门！'),
    ('hannah', 'Grab the flashlight, both of you. My second week starts right now!', '你们二位快拿上手电筒。我的入职第二周，从现在正式开始啦！'),
]
WALK = [
    (0, None, ["'您在锅炉房后面找到那三把折叠椅了吗，格雷厄姆？' 分词作定语修饰名词构成", (None, 'folding chairs'), '专门指不用时可以收拢折起来的备用折叠椅。']),
    (1, None, ["'椅子找到了，而且在一堵老砖墙后面，我还发现了这个。' 口语回答时常省去主语我，直接以过去式开头说出", (None, 'Found the chairs'), '干脆利落地把焦点引向手里的神秘木箱。']),
    (2, None, ["'一只小小的雪松木箱？我在这儿十五年了，从来没见过这只箱子！' 表达人生经历中从未见过某物，标准使用现在完成时", (None, 'I have never seen'), '瞬间吊起所有人的好奇心。']),
    (3, None, ["'把顶上黄铜铭牌的灰尘拂掉……等等，快念念那个数字！' 形象生动的动作短语", (None, 'Brush the dust off'), '用刷子一词作动词搭配脱离介词，画出轻轻拂去陈年积灰的动作。']),
    (4, None, ["'让我把眼镜从额头上拉下来看看……“九号房”？！' 连贯动作短语", (None, 'pull my glasses down from'), '再次活灵活现地写出亚瑟把老花镜从额头拉回鼻梁的招牌动作。']),
    (5, None, ["'格雷厄姆，快看咱们身后的木头钥匙牌：一、二、三、四、五、六、七、八！' 方位介词短语", (None, 'behind us'), '指就在前台两人背后墙上挂着的那块八房木牌。']),
    (6, None, ["'这家客栈从来就只有八间客房呀！九号房究竟在哪里？！' 在特殊疑问词后面加上强调词组构成", (None, 'Where on earth'), '把“究竟、到底在哪儿”的惊讶语气拉到极致。']),
    (7, None, ["'我把箱子倾斜的时候你们仔细听。里面刚刚有什么金属物件滑了一下。' 修饰不定代词时形容词或材质词必须后置，说成", (None, 'Something metal'), '指某样金属质地的东西。']),
    (8, None, ["'正面锁扣上有一个小小的锁眼，再看箱底贴着什么：一把老黄铜钥匙！' 钥匙与孔洞拼合成复合词", (None, 'keyhole'), '一目了然指锁扣正面的钥匙插孔。']),
    (9, None, ["'第九把黄铜钥匙？！咱们是今晚就打开它，还是等到明天早上？！' 注意序数词第九的拼写与发音", (None, 'ninth'), '去掉了基数词九末尾不发音的字母，特指排在第八之后的第九把钥匙。']),
    (10, None, ["'快看从合页缝里露出来的那张折叠蓝图。这一层平面图上画着一扇暗门！' 这里的现在分词短语", (None, 'sticking out of'), '生动描绘纸角从箱盖合页缝隙里探出一截的样子。']),
    (11, None, ["'你们二位快拿上手电筒。我的入职第二周，从现在正式开始啦！' 一般现在时搭配强调时间词组", (None, 'starts right now'), '元气满满地宣告全新冒险即刻启程！']),
]
