# Authoring module for linden-courtyard-zh-s01e04-scene-02.
ID = 'linden-courtyard-zh-s01e04-scene-02'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = 'The Blue Door  (蓝色木门)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '汉娜一路小跑过了河，站在广场的小石喷泉旁给格雷厄姆打电话确认最后一个路口，赶在店主刚开卷帘门的那一刻买到了同款黄铜阀门。我们先听为快。'
OPENER = '现在让我们放慢节奏，逐句听听这段电话连线里的鲜活表达。'
TRANSITION = '熟悉了这些电话沟通和购物的常用语，我们再完整听一遍。'
OUTRO = '两个新阀门稳稳到手，连明年冬天的备用件都有着落了。汉娜付完现金立刻往回飞奔，而客栈二楼已经传来了客人的脚步声！我们待会儿见。'
CLOSING = ('graham', 'Bye for now!')
STORY = [
    ('hannah', 'Graham, can you hear me? I just passed the green pharmacy!', '格雷厄姆，你能听见我说话吗？我刚经过那家绿色药店！'),
    ('graham', 'Loud and clear. Are you standing by the little stone fountain?', '又响亮又清楚。你正站在小石喷泉旁边吗？'),
    ('hannah', 'Yes! There are two small streets on the left. Which one do I take?', '对！左边有两条小街。我该走哪一条？'),
    ('graham', 'Take the second street, beside the flower stand, not the narrow alley.', '走第二条街，就在花摊旁边，别走那条窄巷子。'),
    ('hannah', 'Walking now... oh, I see the golden key sign and the blue door!', '正在走过去……噢，我看见金色钥匙招牌和蓝木门啦！'),
    ('graham', 'Good! Is the shutter open?', '太好了！卷帘门开了吗？'),
    ('hannah', 'The clerk is unlocking it right now! Stay on the phone one second.', '店员正在开锁呢！电话先别挂，等我一秒钟。'),
    ('graham', 'Make sure the brass ring inside is twenty millimeters wide.', '务必确认里面的黄铜垫圈是二十毫米宽。'),
    ('hannah', 'He matched it against the old one. He has two left on the shelf!', '他拿旧阀门比对过了。货架上正好还剩两个！'),
    ('graham', 'Buy both! A spare valve saves next winter too.', '两个都买下来！留一个备用阀门连明年冬天都省心了。'),
    ('hannah', 'Paid in cash! Keep your toolbox open, I am running back across the bridge!', '付过现金啦！把你的工具箱打开备好，我正跑回桥这边来！'),
    ('graham', 'Hurry, I just heard footsteps on the second floor stairs!', '快点儿，我刚听见二楼楼梯上有脚步声了！'),
]
WALK = [
    (0, None, ["'格雷厄姆，你能听见我说话吗？我刚经过那家绿色药店！' 打电话或视频连线开头确认信号好不好，最标准的开场问句就是", (None, 'can you hear me'), '简单直接地询问对方能不能听清。']),
    (1, None, ["'又响亮又清楚。你正站在小石喷泉旁边吗？' 电话那头回答声音非常清晰，最地道的四字成语式短语就是", (None, 'Loud and clear'), '语气干脆爽朗，一听就让人安心。']),
    (2, None, ["'对！左边有两条小街。我该走哪一条？' 面对有限的几个明确选项做挑拣时，英语不用宽泛的什么，而是用", (None, 'Which one'), '精准询问“两条里面选哪一条”。']),
    (3, None, ["'走第二条街，就在花摊旁边，别走那条窄巷子。' 街头露天卖鲜花的小摊位，英语用两个简单词组合成", (None, 'flower stand'), '这里的站立一词做名词，指街边货摊。']),
    (4, None, ["'正在走过去……噢，我看见金色钥匙招牌和蓝木门啦！' 找路时突然映入眼帘发现了目标，直接用感官动词说出", (None, 'I see'), '强调眼睛实实在在看见了结果。']),
    (5, None, ["'太好了！卷帘门开了吗？' 临街商铺门窗外防盗挡雨的百叶窗或金属卷帘门，英语统称为", (None, 'shutter'), '早上开门营业前都得先把它拉起来。']),
    (6, None, ["'店员正在开锁呢！电话先别挂，等我一秒钟。' 请电话那头的人稍等片刻、保持通话不断线，口语常说", (None, 'Stay on the phone'), "比正式商务用语更贴近朋友同事间的紧急连线。"]),
    (7, None, ["'务必确认里面的黄铜垫圈是二十毫米宽。' 英语描述长宽高等具体尺寸时，把数字和单位放在前面，形容词殿后，组成", (None, 'twenty millimeters wide'), '顺序和汉语“宽二十毫米”恰好相反。']),
    (8, None, ["'他拿旧阀门比对过了。货架上正好还剩两个！' 表示卖完或用完之后还剩余多少，把过去分词直接放在数字后面，说成", (None, 'two left'), '短短两词就把“还剩两个”交代得明明白白。']),
    (9, None, ["'两个都买下来！留一个备用阀门连明年冬天都省心了。' 当货架上一共就剩两个、决定全部拿下时，直接用代词说出", (None, 'Buy both'), '果断利落，绝不浪费这趟早起跑腿的功夫。']),
    (10, None, ["'付过现金啦！把你的工具箱打开备好，我正跑回桥这边来！' 结账时说明用纸币现钞付款，固定搭配介词说成", (None, 'in cash'), '注意如果是刷信用卡则要换成另一个介词。']),
    (11, None, ["'快点儿，我刚听见二楼楼梯上有脚步声了！' 紧急关头催促对方加快动作，单说一个动词", (None, 'Hurry'), '急促有力，瞬间把抢修倒计时的紧张感拉到顶点。']),
]
