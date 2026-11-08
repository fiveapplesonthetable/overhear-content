# Authoring module for linden-courtyard-zh-s01e01-scene-06.
ID = 'linden-courtyard-zh-s01e01-scene-06'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'The Luggage Tag  (行李牌上的线索)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'arthur': 'Arthur'}
INTRO = '回到前台，亚瑟戴上老花镜仔细辨认行李牌上的手写小字，汉娜则立刻拨通火车站失物招领处的电话。这只神秘蓝箱子能顺利物归原主吗？先听一遍完整对话。'
OPENER = '现在我们一句一句来听他们如何核对线索、打电话挂失。'
TRANSITION = '熟悉了电话问询和线索表达后，我们再连贯听一遍整场戏。'
OUTRO = '车站失物招领处暂时还没有消息，好在咖啡角的泰莎朝汉娜挥了挥手，想到了一个暖心的好办法。我们接着往下听。'
CLOSING = ('arthur', 'See you soon!')
STORY = [
    ('arthur', 'Dear me, what a mix-up! Let me look at the tag with my glasses.', '哎呀天哪，真是好一场乌龙！让我戴上眼镜看看这张吊牌。'),
    ('evelyn', 'Is there a name or a phone number on it?', '上面写着名字或者电话号码吗？'),
    ('arthur', 'No phone number, unfortunately. Only two initials and an old street name.', '很遗憾，没有电话号码。只有两个姓名首字母和一个老街名。'),
    ('hannah', 'Wait, that street is right here in our neighborhood, five minutes away!', '等等，那条街就在咱们这片街区，离这儿只有五分钟路程！'),
    ('evelyn', 'How strange! We rode the same morning train to the same district.', '真奇怪！我们坐了同一趟早班火车，来的又是同一个街区。'),
    ('arthur', 'Hannah, call the station lost and found office right away.', '汉娜，马上给火车站失物招领处打电话。'),
    ('hannah', 'I am dialing now... Hello? Did anyone report a swapped blue suitcase?', '我正在拨号……喂，您好？请问有人挂失一只拿混了的蓝色行李箱吗？'),
    ('evelyn', 'Tell them mine has a red ribbon inside the top pocket!', '告诉他们，我的那只包顶部外袋里有一条红丝带！'),
    ('hannah', 'Not yet? Please take our guesthouse number and address. Thank you!', '还没有吗？请记下我们客栈的电话号码和地址。谢谢您！'),
    ('arthur', "They have nothing yet, ma'am, I am terribly sorry.", '女士，他们那边暂时还没有任何消息，我真是万分抱歉。'),
    ('evelyn', 'It is not your fault. Still, I only have the coat on my back!', '这不是您的错。不过话说回来，我现在就只剩身上穿的这件大衣了！'),
    ('hannah', 'Wait one moment, Tessa in the cafe just waved to me with an idea!', '请稍等片刻，咖啡角那边的泰莎刚刚朝我挥手，她想到办法了！'),
]
WALK = [
    (0, None, ["'哎呀天哪，真是好一场乌龙！让我戴上眼镜看看这张吊牌。' 地道的感叹短语", (None, 'what a mix-up'), '生动道出东西拿混的乱子；后面看某样具体物品时，不及物动词后要跟介词组成', (None, 'look at'), '才能接宾语吊牌。']),
    (1, None, ["'上面写着名字或者电话号码吗？' 把存在句里的系动词移到最前面构成提问：", (None, 'Is there'), '就能自然询问吊牌上“有没有”留名字或电话。']),
    (2, None, ["'很遗憾，没有电话号码。只有两个姓名首字母和一个老街名。' 名词前面直接放否定限定词构成", (None, 'No phone number'), '比完整的否定句更简洁地道，语气上表示“半个号码也没留”。']),
    (3, None, ["'等等，那条街就在咱们这片街区，离这儿只有五分钟路程！' 英语表达两地相距多远，会把距离或步行时间放在副词前面，说出", (None, 'five minutes away'), '简洁明了地表示“相隔五分钟路程”。']),
    (4, None, ["'真奇怪！我们坐了同一趟早班火车，来的又是同一个街区。' 短促的感叹短句", (None, 'How strange'), '用疑问副词直接修饰形容词表惊奇；后半句动词不规则过去式', (None, 'rode'), '专门用来表示乘坐了火车或出租车。']),
    (5, None, ["'汉娜，马上给火车站失物招领处打电话。' 车站、机场和商场里最实用的固定名称就是", (None, 'lost and found'), '字面意思是“丢失与寻获”，合起来专指失物招领处。']),
    (6, None, ["'我正在拨号……喂，您好？请问有人挂失一只拿混了的蓝色行李箱吗？' 询问过去有没有人报备某事，用过去时助动词开头说出", (None, 'Did anyone report'), '后面的实义动词申报恢复原形即可。']),
    (7, None, ["'告诉他们，我的那只包顶部外袋里有一条红丝带！' 伊芙琳用独立物主代词", (None, 'mine'), '直接作从句主语，一个词就干脆利落地代表了“我的那只行李箱”。']),
    (8, None, ["'还没有吗？请记下我们客栈的电话号码和地址。谢谢您！' 简短实用的短语", (None, 'Not yet'), '在英语日常对话中出场率极高，用来表示某事“目前还没有发生，但接下来可能会有进展”。']),
    (9, None, ["'女士，他们那边暂时还没有任何消息，我真是万分抱歉。' 亚瑟在道歉词前面加上程度副词", (None, 'terribly sorry'), '这里并不是说可怕，而是郑重诚恳地表示“实在太抱歉了”。']),
    (10, None, ["'这不是您的错。不过话说回来，我现在就只剩身上穿的这件大衣了！' 体谅对方不必自责时，最暖心体面的回应就是", (None, 'It is not your fault'), '温和地把责任从对方肩上卸下来。']),
    (11, None, ["'请稍等片刻，咖啡角那边的泰莎刚刚朝我挥手，她想到办法了！' 副词紧挨着过去式动词构成", (None, 'just waved'), '用来捕捉眼前“刚刚才发生”的一瞬间动作。']),
]
