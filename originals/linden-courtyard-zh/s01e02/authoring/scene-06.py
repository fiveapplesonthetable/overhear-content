# Authoring module for linden-courtyard-zh-s01e02-scene-06.
ID = 'linden-courtyard-zh-s01e02-scene-06'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'The Friday Caller  (星期五的神秘来电)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '早餐过后，前台电话响了起来。电话那头是一位声音温和却透着紧张的年轻男士，专门来打听那只深蓝色行李箱，却怎么也不肯留下姓名。先完整听一遍吧。'
OPENER = '现在我们一句一句拆解这通神秘来电里的电话用语。'
TRANSITION = '听清了电话里的每一个细节，我们再完整听一遍整场戏。'
OUTRO = '不许拆开那个装着木头玩具火车的白纸包，星期五中午十二点再来取！这桩蓝色行李箱的谜团真是越来越吊人胃口了。先再见啦，我们下场戏接着听。'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('hannah', 'Linden Courtyard Inn, good morning! Hannah speaking.', '菩提树庭院客栈，早上好！我是汉娜，请讲。'),
    ('graham', 'Who is it? Another booking for the weekend?', '是谁打来的？又是预订周末房间的客人吗？'),
    ('hannah', 'Wait, hello, sir! You are calling about the dark blue suitcase?', '等等，您好，先生！您打电话来是问那只深蓝色行李箱的事吗？'),
    ('graham', 'Ask him his name! Write it down!', '快问他叫什么名字！把它记下来！'),
    ('hannah', 'Yes, sir, we locked your bag safely in our closet. What is your name, please?', '是的，先生，我们已经把您的包稳妥锁进储物间了。请问您怎么称呼？'),
    ('graham', 'What is he saying? Why are you frowning?', '他在说什么？你干嘛皱着眉头？'),
    ('hannah', "Sir? He says, 'Please do not open the white paper package. I will come Friday at noon.'", '先生？他说：“请不要打开那个白纸包。我星期五中午十二点过来。”'),
    ('graham', 'Give me the phone, let me ask him properly!', '把电话给我，让我好好问问他！'),
    ('hannah', "Too late! He said 'Thank you' and hung up!", '来不及了！他说了声“谢谢你”就挂断了！'),
    ('graham', 'Polite voice? Young or old?', '说话声音有礼貌吗？听着是年轻人还是年长者？'),
    ('hannah', 'Quiet, polite, maybe thirty-five. He sounded nervous, not angry.', '声音很轻，很有礼貌，大概三十五岁吧。他听起来很紧张，倒不是生气。'),
    ('graham', 'Nervous about a wooden toy train? This story gets stranger every hour.', '为了一列木头玩具火车这么紧张？这件事真是每个小时都变得更离奇了。'),
]
WALK = [
    (0, None, ["'菩提树庭院客栈，早上好！我是汉娜，请讲。' 英语接起办公电话自报家门时，直接在自己名字后面加上现在分词说", (None, 'Hannah speaking'), '简洁表示“汉娜正在接听”。']),
    (1, None, ["'是谁打来的？又是预订周末房间的客人吗？' 询问电话那头或门外的人是谁，英语习惯用中性代词代表尚不知晓的来电者，问一句", (None, 'Who is it'), '听起来既自然又地道。']),
    (2, None, ["'等等，您好，先生！您打电话来是问那只深蓝色行李箱的事吗？' 确认对方来电目的时，用现在进行时搭配介词说出", (None, 'You are calling about'), '后面直接跟上所询问的事情。']),
    (3, None, ["'快问他叫什么名字！把它记下来！' 格雷厄姆急忙提醒汉娜动笔记下，当宾语是代词时必须夹在动词和副词中间，说成", (None, 'Write it down'), '语序紧凑有力。']),
    (4, None, ["'是的，先生，我们已经把您的包稳妥锁进储物间了。请问您怎么称呼？' 在最常用的基础问句", (None, 'What is your name'), '末尾轻轻补上一个“请”字，立刻让前台核实身份的询问变得礼貌周全。']),
    (5, None, ["'他在说什么？你干嘛皱着眉头？' 看见对方神情疑惑，用现在分词", (None, 'frowning'), '配合系动词构成现在进行时，形象描绘汉娜边听电话边眉头紧锁的样子。']),
    (6, None, ["'先生？他说：“请不要打开那个白纸包。我星期五中午十二点过来。”' 英语里正午十二点是一个精确的时间点，所以固定搭配介词说", (None, 'at noon'), '不用再额外加数字十二。']),
    (7, None, ["'把电话给我，让我好好问问他！' 放在句末的副词", (None, 'properly'), '表示按规矩、正儿八经地把话问清楚，透出格雷厄姆老练严谨的职业习惯。']),
    (8, None, ["'来不及了！他说了声“谢谢你”就挂断了！' 英语表达“挂断电话”用的是悬挂一词的不规则过去式加上小词，构成", (None, 'hung up'), '源于早年把听筒挂回墙上支架的动作。']),
    (9, None, ["'说话声音有礼貌吗？听着是年轻人还是年长者？' 日常对话紧急追问特征时常常省略主语和系动词，直接甩出对比短句", (None, 'Young or old'), '节奏干脆利落。']),
    (10, None, ["'声音很轻，很有礼貌，大概三十五岁吧。他听起来很紧张，倒不是生气。' 凭电话里的嗓音判断对方情绪，用感官动词过去式接形容词说出", (None, 'sounded nervous'), '准确区分了心里忐忑与发脾气的不同。']),
    (11, None, ["'为了一列木头玩具火车这么紧张？这件事真是每个小时都变得更离奇了。' 请特别留意这里的", (None, 'gets stranger'), '可不是指陌生人，而是动词变得接上形容词“奇怪”的比较级，表示越来越蹊跷。']),
]
