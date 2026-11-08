# Authoring module for linden-courtyard-zh-s01e06-scene-03.
ID = 'linden-courtyard-zh-s01e06-scene-03'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = 'Thirty Days on Paper  (纸上的三十天)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '回到前台后面，亚瑟还在为三十天后的卖楼通知唉声叹气。格雷厄姆和汉娜却没有放弃，汉娜突然想到了院子里坐着的那位大行家。先完整听一遍吧。'
OPENER = '现在我们逐句拆解大家在危机面前急中生智的对话。'
TRANSITION = '听懂了汉娜灵光一闪的好主意，我们再连贯听一遍整场戏。'
OUTRO = '没错，凯勒布可是精通波特兰历史庭院建筑的建筑师！这时泰莎端着空托盘从庭院走回来了，转机也许就在眼前。先再见。'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('arthur', 'Fifteen years of polishing brass keys and straightening ties... gone in thirty days!', '十五年来擦亮黄铜钥匙、整理领带的心血……三十天后就要化为乌有了！'),
    ('graham', 'Stop burying us before we read the whole document, Arthur.', '整份文件还没读完呢，先别急着给咱们判死刑呀，亚瑟。'),
    ('hannah', 'Yes! Earlier I noticed a second page clipped behind the cover letter.', '对呀！刚才我就注意到首页信函背面还别着第二页呢。'),
    ('arthur', 'Legal paragraphs give me a headache even with two pairs of glasses!', '就算戴上两副眼镜，那些法律条文也看得我直头疼！'),
    ('graham', 'This house survived eighty winters and one broken boiler valve yesterday.', '这栋老房子熬过了八十个寒冬，昨天还刚挺过一个坏掉的锅炉阀门呢。'),
    ('hannah', 'Wait, who is sitting ten meters away in our courtyard right now?', '等等，此时此刻坐在咱们庭院里十米开外的人是谁呀？'),
    ('arthur', 'Two brothers eating lemon cake?', '正在吃柠檬蛋糕的两兄弟？'),
    ('hannah', 'An architect who works with historic courtyard buildings all over Portland!', '是一位专门跟波特兰全城历史庭院建筑打交道的建筑师呀！'),
    ('graham', 'Smart thinking, Hannah. Caleb reads city building rules every single week.', '脑筋转得真快，汉娜。凯勒布每个星期都在研究市政建筑法规呢。'),
    ('arthur', 'Oh, I could never bother a paying guest with our landlord troubles!', '噢，我怎么好意思拿咱们和房东的麻烦事去打扰付费入住的客人呢！'),
    ('hannah', 'After we guarded his blue suitcase all week? He will want to help!', '咱们可是替他守了一整周蓝箱子呢！他肯定巴不得帮忙！'),
    ('graham', 'Wait, here comes Tessa back from their table right now.', '等等，泰莎这会儿正好从他们那桌走回来了。'),
]
WALK = [
    (0, None, ["'十五年来擦亮黄铜钥匙、整理领带的心血……三十天后就要化为乌有了！' 过去分词搭配时间介词构成", (None, 'gone in thirty days'), '这里的介词表示在三十天之后一切便将消逝。']),
    (1, None, ["'整份文件还没读完呢，先别急着给咱们判死刑呀，亚瑟。' 格雷厄姆用夸张比喻", (None, 'Stop burying us'), '字面意思是别急着把咱们埋了，劝老搭档先冷静把文件看完。']),
    (2, None, ["'对呀！刚才我就注意到首页信函背面还别着第二页呢。' 正式文件最前面概述来意的附函在英语里叫作", (None, 'cover letter'), '精准区分了首页通知与背面的详细附件。']),
    (3, None, ["'就算戴上两副眼镜，那些法律条文也看得我直头疼！' 抱怨繁琐文字让人头昏脑涨时，英语习惯用双宾语短语", (None, 'give me a headache'), '既口语化又生动好记。']),
    (4, None, ["'这栋老房子熬过了八十个寒冬，昨天还刚挺过一个坏掉的锅炉阀门呢。' 及物动词直接接宾语组成", (None, 'survived eighty winters'), '无需添加任何介词就能有力表达历经八十年风霜依然屹立。']),
    (5, None, ["'等等，此时此刻坐在咱们庭院里十米开外的人是谁呀？' 距离数量词加副词组成", (None, 'ten meters away'), '清楚点出救星其实近在咫尺，就在十米之外。']),
    (6, None, ["'正在吃柠檬蛋糕的两兄弟？' 亚瑟还没反应过来，顺口用名词加现在分词", (None, 'Two brothers eating'), '茫然作答，制造出温情又好笑的反差。']),
    (7, None, ["'是一位专门跟波特兰全城历史庭院建筑打交道的建筑师呀！' 句尾这个介词短语", (None, 'all over Portland'), '意为遍及整个波特兰城，一下子点醒大家凯勒布的专业实力。']),
    (8, None, ["'脑筋转得真快，汉娜。凯勒布每个星期都在研究市政建筑法规呢。' 夸赞同伴点子妙、反应快时，一句简短的", (None, 'Smart thinking'), '在日常合作中既真诚又提气。']),
    (9, None, ["'噢，我怎么好意思拿咱们和房东的麻烦事去打扰付费入住的客人呢！' 情态动词加否定词构成", (None, 'I could never bother'), '贴切表现出老派店主不愿给客人添麻烦的矜持。']),
    (10, None, ["'咱们可是替他守了一整周蓝箱子呢！他肯定巴不得帮忙！' 笃定推测对方一定乐意相助时，用将来时说出", (None, 'He will want to help'), '语气干脆又充满信心。']),
    (11, None, ["'等等，泰莎这会儿正好从他们那桌走回来了。' 看到某人正朝这边走来，口语常用全倒装句", (None, 'here comes Tessa'), '把人物名字放在动词后面，自然引出下一场戏。']),
]
