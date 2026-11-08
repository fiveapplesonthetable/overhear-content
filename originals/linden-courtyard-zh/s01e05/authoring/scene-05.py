# Authoring module for linden-courtyard-zh-s01e05-scene-05.
ID = 'linden-courtyard-zh-s01e05-scene-05'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = 'Simple Words First  (先说简单真挚的话)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = '上午十一点四十分，凯勒布攥着密密麻麻的手写讲稿在庭院里来回踱步。汉娜端来一杯凉水，帮他把僵硬的长篇大论换成了三句最朴实的心里话。我们先听为快。'
OPENER = '现在我们逐句拆解这段既幽默又让人心头一暖的对话。'
TRANSITION = '记住了这三句真诚的开场白，我们再完整听一遍整场戏。'
OUTRO = '把十九条理由折进口袋，只留下问候、思念与热茶蛋糕——凯勒布终于松了一口气。正午的脚步越来越近了，多保重。'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('hannah', 'Here, drink a sip of cool water, Caleb. What is on that paper?', '给，喝口凉水缓一缓，凯勒布。那张纸上写着什么呀？'),
    ('caleb', 'A five minute speech explaining nineteen reasons why we were both wrong in April.', '一篇五分钟的演讲稿，解释当年四月我们俩都有错的十九个理由。'),
    ('hannah', 'Nineteen reasons?! Are you welcoming your brother or reading a train schedule?', '十九个理由？！你这是在迎接亲哥哥，还是在念火车时刻表呀？'),
    ('caleb', 'When I get nervous, my sentences grow very long and formal!', '我一紧张起来，说出来的句子就会变得又长又正式！'),
    ('hannah', 'Fold that paper and put it in your pocket right now.', '现在就把那张纸折起来，揣进你的口袋里去。'),
    ('caleb', 'Without my notes, what do I say when he walks through that gate?', '没了稿子，等他走进那扇铁门时我该说什么呢？'),
    ('hannah', "Start with three short sentences. First: 'Hello, Owen, thank you for coming.'", '先从三句简短的话开始。第一句：“你好，欧文，谢谢你能来。”'),
    ('caleb', "'Hello, Owen, thank you for coming.' Okay, I can remember that.", '“你好，欧文，谢谢你能来。”好，这句我记得住。'),
    ('hannah', "Second: 'I missed you these three years.'", '第二句：“这三年我很想你。”'),
    ('caleb', "'I missed you these three years.' Honest and clear. And third?", '“这三年我很想你。”坦诚又清楚。那第三句呢？'),
    ('hannah', "'Sit down, there is hot tea and Friday lemon cake.'", '“坐下吧，这儿有热茶和星期五柠檬蛋糕。”'),
    ('caleb', 'Tea and lemon cake! Hannah, you should open a school for nervous brothers.', '热茶和柠檬蛋糕！汉娜，你真该给紧张的弟弟们办一所学校。'),
]
WALK = [
    (0, None, ["'给，喝口凉水缓一缓，凯勒布。那张纸上写着什么呀？' 询问纸页表面写了什么内容时，英语固定用介词短语", (None, 'on that paper'), '把字迹看作落在纸面之上的东西。']),
    (1, None, ["'一篇五分钟的演讲稿，解释当年四月我们俩都有错的十九个理由。' 数词加时间名词直接放在中心词前作定语时，中间的名词保持单数，说成", (None, 'five minute speech'), '地道表示时长五分钟的发言。']),
    (2, None, ["'十九个理由？！你这是在迎接亲哥哥，还是在念火车时刻表呀？' 汉娜用现在进行时一般疑问句", (None, 'Are you welcoming'), '打趣他把兄弟重逢搞得像宣读列车表一样死板。']),
    (3, None, ["'我一紧张起来，说出来的句子就会变得又长又正式！' 这句里连用两个生动的渐变系动词：先用", (None, 'get nervous'), '表示情绪开始紧张，再用', (None, 'grow very long'), '形容句子不知不觉越拉越长。']),
    (4, None, ["'现在就把那张纸折起来，揣进你的口袋里去。' 祈使句开头干脆使用动词原形", (None, 'Fold that paper'), '温柔而果断地帮凯勒布放下包袱。']),
    (5, None, ["'没了稿子，等他走进那扇铁门时我该说什么呢？' 时间状语从句", (None, 'when he walks through'), '用一般现在时代替将来，同时用穿过一词画出迈进大门的立体动作。']),
    (6, None, ["'先从三句简短的话开始。第一句：“你好，欧文，谢谢你能来。”' 欢迎客人在约定的日子赴约，最温暖得体的开场莫过于", (None, 'thank you for coming'), '简简单单却分量十足。']),
    (7, None, ["'“你好，欧文，谢谢你能来。”好，这句我记得住。' 重复默念一遍后给自己打气说", (None, 'I can remember that'), '语气从慌乱慢慢稳了下来。']),
    (8, None, ["'第二句：“这三年我很想你。”' 英语里的想念和错过是同一个词，用过去式说出", (None, 'I missed you'), '坦诚道出过去三年时光里心底的牵挂。']),
    (9, None, ["'“这三年我很想你。”坦诚又清楚。那第三句呢？' 日常对话顺着序列往下追问时，不用把整句问全，简短一句", (None, 'And third'), '就能自然引出最后一条建议。']),
    (10, None, ["'“坐下吧，这儿有热茶和星期五柠檬蛋糕。”' 亲人之间招呼落座，直接用短语动词", (None, 'Sit down'), '配上一杯热茶和儿时甜点，胜过千言万语。']),
    (11, None, ["'热茶和柠檬蛋糕！汉娜，你真该给紧张的弟弟们办一所学校。' 情态动词搭配动词原形组成", (None, 'you should open'), '带着轻松的玩笑夸赞汉娜太懂得安抚人心。']),
]
