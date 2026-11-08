# Authoring module for linden-courtyard-zh-s01e05-scene-03.
ID = 'linden-courtyard-zh-s01e05-scene-03'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = 'Friday Lemon Cake  (星期五柠檬蛋糕)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'evelyn': 'Evelyn', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = '早餐咖啡角里，伊芙琳女士回忆起两兄弟小时候每周五上完钢琴课最爱的甜点，这一下子给了烘焙师泰莎一个绝妙的主意。我们先听为快。'
OPENER = '现在让我们一句一句品味这场充满柠檬甜香的温馨对话。'
TRANSITION = '熟悉了这些生动的日常表达，我们再完整听一遍整场戏。'
OUTRO = '篮子里恰好躺着六个黄柠檬，泰莎已经挽起袖子准备烤一盘带边角的星期五柠檬蛋糕了。我们也去庭院看看准备得怎么样吧，先再见啦。'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('tessa', 'So, Caleb, you are really staying in the courtyard to greet Owen at noon?', '这么说，凯勒布，你真的要留在庭院里，中午亲自迎接欧文吗？'),
    ('caleb', 'Yes, Tessa. Even if he turns around and walks straight back out the gate.', '是的，泰莎。哪怕他一转身就径直走出大门。'),
    ('evelyn', 'Owen will not walk out. He always acted tough for five seconds, then softened.', '欧文不会走掉的。他以前总是硬撑五秒钟，随后就心软了。'),
    ('caleb', 'You still remember that after all these years?', '过了这么多年，您还记得这些呀？'),
    ('evelyn', 'Of course! Every Friday when he missed a piano note, he frowned at the wall.', '那当然啦！以前每个星期五他只要弹错一个琴键，就会对着墙壁皱眉头。'),
    ('tessa', 'How did you get him smiling again, Miss Evelyn?', '那您是怎么逗他重新笑起来的呢，伊芙琳女士？'),
    ('evelyn', 'His grandfather sliced warm lemon cake with powdered sugar on top!', '他爷爷会切开温热的柠檬蛋糕，上面还撒着一层糖粉！'),
    ('caleb', 'Oh! Yellow lemon glaze! We fought over the corner piece every single Friday!', '噢！黄澄澄的柠檬糖霜！那时候每个星期五我们都抢着要边角那一块！'),
    ('tessa', 'Hold everything! What time is it right now? Nine thirty-five!', '全都先停一下！现在几点了？九点三十五分！'),
    ('caleb', 'Tessa, please do not do extra work because of us.', '泰莎，请千万别因为我们额外忙活。'),
    ('tessa', 'Six yellow lemons are sitting in my basket right now. This kitchen was waiting for today!', '眼下我篮子里正好放着六个黄柠檬呢。这间厨房简直就是为了今天而准备的！'),
    ('evelyn', 'Bake plenty of corner pieces, my dear!', '多烤几块边角料吧，亲爱的！'),
]
WALK = [
    (0, None, ["'这么说，凯勒布，你真的要留在庭院里，中午亲自迎接欧文吗？' 用现在进行时穿插强调副词组成", (None, 'you are really staying'), '带着关切向对方确认这个刚刚下定决心的安排。']),
    (1, None, ["'是的，泰莎。哪怕他一转身就径直走出大门。' 句首用让步连词短语", (None, 'Even if'), '表示“就算、哪怕”，后面搭配动词短语', (None, 'turns around'), '形容对方掉头转身的动作。']),
    (2, None, ["'欧文不会走掉的。他以前总是硬撑五秒钟，随后就心软了。' 系动词般使用的行为动词接形容词构成", (None, 'acted tough'), '精准刻画出嘴硬心软、故意装出强硬姿态的神情。']),
    (3, None, ["'过了这么多年，您还记得这些呀？' 感叹时光流逝却记忆犹新时，固定短语", (None, 'after all these years'), '读起来温情脉脉，相当于汉语的“这么多年过去了”。']),
    (4, None, ["'那当然啦！以前每个星期五他只要弹错一个琴键，就会对着墙壁皱眉头。' 弹琴漏掉或按错一个音符，英语不直说弹错，而是用温和地道的", (None, 'missed a piano note'), '十分符合钢琴老师的口吻。']),
    (5, None, ["'那您是怎么逗他重新笑起来的呢，伊芙琳女士？' 这里的使役短语结构", (None, 'get him smiling'), '用现在分词作宾语补足语，生动表达“想办法让他重新展露笑容”。']),
    (6, None, ["'他爷爷会切开温热的柠檬蛋糕，上面还撒着一层糖粉！' 描述食物表面铺洒着配料时，句尾轻轻加上方位短语", (None, 'on top'), '就能立刻让人眼前浮现出蛋糕顶层洁白糖粉的画面。']),
    (7, None, ["'噢！黄澄澄的柠檬糖霜！那时候每个星期五我们都抢着要边角那一块！' 在星期前面加上强调词构成", (None, 'every single Friday'), '意思是一周都不落、每一个星期五都如此。']),
    (8, None, ["'全都先停一下！现在几点了？九点三十五分！' 脑海里突然冒出好点子、叫全场暂停时，口语里喊一句", (None, 'Hold everything'), '活泼又有戏剧张力，相当于“大家先停一停”。']),
    (9, None, ["'泰莎，请千万别因为我们额外忙活。' 客气地劝对方别为自己破费劳神时，复合介词短语", (None, 'because of us'), '后接代词宾格，清楚礼貌地点出原因。']),
    (10, None, ["'眼下我篮子里正好放着六个黄柠檬呢。这间厨房简直就是为了今天而准备的！' 英语描写物品静静摆放在某处时，常生动地用进行时", (None, 'are sitting in my basket'), '仿佛柠檬正乖巧地坐在篮中待命。']),
    (11, None, ["'多烤几块边角料吧，亲爱的！' 长辈对晚辈温和嘱咐时，句尾附上一声亲昵的称呼", (None, 'my dear'), '满是慈爱与笑意，让整场戏收尾得格外暖心。']),
]
