# Authoring module for linden-courtyard-zh-s01e02-scene-05.
ID = 'linden-courtyard-zh-s01e02-scene-05'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'Juice on the Tie  (洒在领带上的橙汁)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'evelyn': 'Evelyn', 'hannah': 'Hannah'}
INTRO = '早餐准时开席，伊芙琳悠然坐在餐桌旁品尝红茶与热面包。老板亚瑟热情上前想要亲自展现一番五星级倒果汁服务，没想到壶嘴太宽出了点小洋相。先完整听一遍吧。'
OPENER = '现在让我们逐句来听餐桌点单与化解小尴尬的得体英语。'
TRANSITION = '记住了这些优雅的餐桌用语，我们再连贯听一遍整场戏。'
OUTRO = '亚瑟体面地退回办公室擦领带去了，而泰莎和汉娜用海盐黄油现炒的法式嫩蛋赢得了伊芙琳的由衷赞美。我们下场戏见。'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', 'Good morning again, Miss Evelyn! Would you like coffee or black tea?', '伊芙琳女士，又见面了，早上好！您想喝咖啡还是红茶？'),
    ('evelyn', 'Black tea without sugar, please, and one slice of warm bread.', '请来一杯不加糖的红茶，再来一片温热的面包。'),
    ('arthur', "Allow me to pour the fresh orange juice, ma'am!", '女士，请让我来为您斟鲜榨橙汁吧！'),
    ('evelyn', 'Oh, how kind of you, sir. Just half a glass.', '噢，先生，您真是太客气了。只要半杯就好。'),
    ('arthur', 'At our guesthouse, five-star service comes naturally... whoops!', '在我们这家客栈，五星级服务向来自然流露……哎哟！'),
    ('hannah', 'Careful, Arthur, the pitcher spout is wide!', '当心呀，亚瑟，那只水壶的壶嘴很宽！'),
    ('arthur', 'Oh dear! Not a drop on the table, thank goodness... all of it is on my tie!', '哎呀糟糕！谢天谢地，桌上一滴也没洒……全洒在我的领带上了！'),
    ('evelyn', 'Do not worry! Cold sparkling water takes orange juice right out.', '别担心！冰气泡水一下子就能把橙汁渍洗掉。'),
    ('hannah', 'Here is a clean cloth and cold water, Arthur.', '亚瑟，给你一块干净抹布和冷水。'),
    ('arthur', "Excuse me, ma'am, I shall retreat to my office with dignity!", '女士，失陪一下，容我体面地退回办公室去处理吧！'),
    ('evelyn', 'Your scrambled eggs are delicious, Hannah. Tell Tessa my compliments!', '汉娜，你们做的炒蛋真美味。请代我向泰莎转达称赞！'),
    ('hannah', 'I will! Enjoy your morning.', '我一定转达！祝您早上愉快。'),
]
WALK = [
    (0, None, ["'伊芙琳女士，又见面了，早上好！您想喝咖啡还是红茶？' 餐饮服务中向客人提供选择时，最温和有礼的固定句式就是", (None, 'Would you like'), '语气比直接问你想要什么委婉动听得多。']),
    (1, None, ["'请来一杯不加糖的红茶，再来一片温热的面包。' 面包在英语里属于不可数名词，不能直接和数字连用，必须借助表示薄片的量词说出", (None, 'one slice of warm bread'), '才能准确点单。']),
    (2, None, ["'女士，请让我来为您斟鲜榨橙汁吧！' 亚瑟用彬彬有礼的服务套语", (None, 'Allow me to pour'), '主动请缨帮客人倒果汁，把小客栈的仪式感拉得满满的。']),
    (3, None, ["'噢，先生，您真是太客气了。只要半杯就好。' 感谢别人的周到照顾时常感叹一句", (None, 'how kind of you'), '接着说要半杯时注意冠词放在中间，表达为', (None, 'half a glass'), '顺序非常地道。']),
    (4, None, ["'在我们这家客栈，五星级服务向来自然流露……哎哟！' 连字符复合定语", (None, 'five-star service'), '里面的星级要用单数形式；话音未落一声感叹词', (None, 'whoops'), '就把手滑洒汁的瞬间演活了。']),
    (5, None, ["'当心呀，亚瑟，那只水壶的壶嘴很宽！' 看到别人手头动作眼看要洒出来，紧急提醒时不必说整句话，直接喊一声形容词", (None, 'Careful'), '就能让人立刻留神。']),
    (6, None, ["'哎呀糟糕！谢天谢地，桌上一滴也没洒……全洒在我的领带上了！' 庆幸餐桌布保住了的时候，口语常说", (None, 'thank goodness'), '相当于汉语里的“谢天谢地、幸亏”，结果后半句大反转让人忍俊不禁。']),
    (7, None, ["'别担心！冰气泡水一下子就能把橙汁渍洗掉。' 英语里带气的苏打水叫作", (None, 'sparkling water'), '伊芙琳接着用生活妙招短语', (None, 'takes orange juice right out'), '告诉他能把污渍彻底清除干净。']),
    (8, None, ["'亚瑟，给你一块干净抹布和冷水。' 注意单数名词", (None, 'cloth'), '指一块擦拭用的抹布或餐布，千万别跟它加了复数词尾后专指“衣服”的同源词弄混了。']),
    (9, None, ["'女士，失陪一下，容我体面地退回办公室去处理吧！' 亚瑟故意选用古典郑重的助动词说出", (None, 'I shall retreat'), '拿自己狼狈退场开起了绅士玩笑，立刻化解了尴尬。']),
    (10, None, ["'汉娜，你们做的炒蛋真美味。请代我向泰莎转达称赞！' 吃完饭想夸奖大厨手艺好，英语最地道的说法就是请服务员转达复数形式的", (None, 'my compliments'), '听起来格外优雅得体。']),
    (11, None, ["'我一定转达！祝您早上愉快。' 答应别人的嘱托时，只用主语加上将来意愿助动词回答一句", (None, 'I will'), '简短干脆，省去了后面重复的动词短语。']),
]
