# Authoring module for linden-courtyard-zh-s01e03-scene-01.
ID = 'linden-courtyard-zh-s01e03-scene-01'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'Thirty-Five Minutes  (三十五分钟)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '雨夜将至，菩提树庭院客栈的店主亚瑟发现七号房今晚竟被重复预订了两次，急得团团转，而格雷厄姆拿出了一把通往三楼阁楼的小银钥匙。先完整听一遍这段对话，感受一下现场紧张又热闹的气氛。'
OPENER = '现在我们放慢节奏，一句一句拆解这段救急商量。'
TRANSITION = '弄清了这些实用表达，我们按正常语速再完整听一遍。'
OUTRO = '一把小银钥匙打开了新思路，三人决定立刻冲上三楼去收拾阁楼房。就算刚才有几个词听得不太真切也没关系，后面还会不断重现。我们下场戏见。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('arthur', 'Thirty-five minutes! He will write a terrible one star review!', '还有三十五分钟！他肯定会写一条糟糕透顶的一星差评！'),
    ('hannah', 'Take a deep breath, Arthur. Nobody has written anything yet.', '深呼吸，亚瑟。现在还没有人写任何评价呢。'),
    ('graham', 'Here is the small silver key for the third floor attic door.', '这是三楼阁楼房门的那把小银钥匙。'),
    ('arthur', 'Does the attic even have a proper bed?', '阁楼里到底有没有一张像样的床啊？'),
    ('graham', 'Yes, a good wooden bed, a clean desk, and the best view in the house.', '有啊，一张结实的木床、一张干净的书桌，还有全客栈最棒的视野。'),
    ('hannah', 'Then why do we never rent it to guests?', '那我们为什么从来不把它租给客人呢？'),
    ('graham', 'Because the stairs are narrow and Arthur keeps old lamp boxes there.', '因为楼梯很窄，而且亚瑟把旧灯具纸箱堆在那儿了。'),
    ('arthur', 'Only three small boxes! Maybe four!', '只有三个小箱子！也许四个吧！'),
    ('hannah', 'We can move four boxes in five minutes. Let us go look right now!', '四个箱子我们五分钟就能搬走。咱们现在就上去看看！'),
    ('graham', 'Up the stairs, turn left at the landing, last door at the top.', '上楼梯，在平台处左转，最顶头最后一扇门就是。'),
    ('arthur', 'I will bring clean white sheets from the linen closet!', '我去布草储藏柜拿干净的白床单过来！'),
    ('hannah', 'Come on, race you to the third floor!', '快走吧，跟你比赛看谁先到三楼！'),
]
WALK = [
    (0, None, ["'还有三十五分钟！他肯定会写一条糟糕透顶的一星差评！' 亚瑟预感坏事即将发生，用助动词加动词原形说出", (None, 'will write'), '生动表现出他对客人差评的担忧预测。']),
    (1, None, ["'深呼吸，亚瑟。现在还没有人写任何评价呢。' 安抚紧张的朋友时，英语最地道的一句劝慰就是", (None, 'Take a deep breath'), '字面意思是深深吸一口气，让心情平复下来。']),
    (2, None, ["'这是三楼阁楼房门的那把小银钥匙。' 留意英语一连串名词修饰语的排列顺序：", (None, 'third floor attic door'), '先说楼层，再说阁楼，最后落脚在门这个核心词上。']),
    (3, None, ["'阁楼里到底有没有一张像样的床啊？' 疑问句里插进副词", (None, 'even'), '语气立刻多了一层怀疑和夸张，相当于汉语追问“到底、甚至连……都有吗”。']),
    (4, None, ["'有啊，一张结实的木床、一张干净的书桌，还有全客栈最棒的视野。' 夸赞房间景色数一数二，英语用最高级结构", (None, 'best view in the house'), '介词用在这个建筑内部，地道表达“全屋最佳景观”。']),
    (5, None, ["'那我们为什么从来不把它租给客人呢？' 询问某个一贯的做法背后的原因时，把频率副词放在实义动词前面，说出", (None, 'why do we never rent'), '语序紧凑又自然。']),
    (6, None, ["'因为楼梯很窄，而且亚瑟把旧灯具纸箱堆在那儿了。' 英语里的楼梯通常指一连串台阶，因此常用复数主语搭配复数系动词，说成", (None, 'the stairs are narrow'), '千万别误用成单数形式。']),
    (7, None, ["'只有三个小箱子！也许四个吧！' 心虚地往回找补或者拿不准数量时，句首轻轻加一个词", (None, 'Maybe'), '就能精准传达出“也许、大概”的犹豫口吻。']),
    (8, None, ["'四个箱子我们五分钟就能搬走。咱们现在就上去看看！' 美式口语督促大家赶紧行动时，常把两个动词原形连在一起用，说出", (None, 'go look'), '省掉中间的连词，听起来干脆利落。']),
    (9, None, ["'上楼梯，在平台处左转，最顶头最后一扇门就是。' 在楼道里指路时，用祈使句搭配精准的地点介词说出", (None, 'turn left at the landing'), '表示到了楼梯拐角平台那个点再往左转。']),
    (10, None, ["'我去布草储藏柜拿干净的白床单过来！' 当场主动揽下任务、决定马上去做某事时，英语习惯脱口而出", (None, 'I will bring'), '表示“我去拿过来”，比计划好的将来时更有即时感。']),
    (11, None, ["'快走吧，跟你比赛看谁先到三楼！' 朋友之间开玩笑说“跟你比比谁快”，口语里直接省掉主语说", (None, 'race you'), '把比赛一词直接用作及物动词，活泼又有朝气。']),
]
