# Authoring module for linden-courtyard-zh-s01e06-scene-06.
ID = 'linden-courtyard-zh-s01e06-scene-06'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = 'Permanent Keys  (正式入职的钥匙)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = '危机解除，咖啡角里喜气洋洋。亚瑟当场拍板明天一早就向全街开放庭院咖啡馆，紧接着又转向汉娜，提起了她五天试用期满的大事。我们先听为快。'
OPENER = '现在让我们一句一句分享泰莎圆梦与汉娜转正的双喜临门时刻。'
TRANSITION = '感受了这份热闹欢快的团队情谊，我们再完整听一遍整场戏。'
OUTRO = '泰莎拥有了梦想中的庭院咖啡馆，汉娜的名字也用永久墨水写进了那本大纸质登记簿里。夜幕缓缓降临，庭院里的金色灯笼就要亮起来了，待会儿见。'
CLOSING = ('arthur', 'See you later!')
STORY = [
    ('arthur', 'Tessa, how many cinnamon rolls and lemon cakes can your oven bake each morning?', '泰莎，你的烤箱每天早上能烤出多少个肉桂卷和柠檬蛋糕？'),
    ('tessa', 'Double what I make now! Are we really opening the courtyard cafe to our street?', '比我现在做的翻一倍都没问题！咱们真的要向整条街开放庭院咖啡馆吗？'),
    ('arthur', 'Starting tomorrow at eight! Four tables inside, three tables under the tree!', '从明天早上八点就开始！屋里摆四张桌子，大树底下再摆三张！'),
    ('tessa', "My dream cafe, right here in our own courtyard! Wait until I tell the baker's market!", '我梦寐以求的咖啡馆，就开在咱们自家庭院里！等着瞧我去告诉烘焙市集的伙伴们吧！'),
    ('arthur', 'And now, Hannah, today is Friday, the last day of your five day trial week.', '接下来轮到你了，汉娜，今天是星期五，是你五天试用期的最后一天。'),
    ('hannah', 'Oh! With the suitcases, the boiler, and the letter, I completely forgot!', '噢！忙着行李箱、锅炉还有那封信，我竟然忘得一干二净了！'),
    ('arthur', 'On Monday you opened our tricky door; since then you saved rooms, pipes, breakfast, and our lease.', '星期一你推开了咱们那扇难搞的门；从那以后，你保住了客房、水管、早餐，还有咱们的租约。'),
    ('tessa', 'If you do not hire her full time, Arthur, I am hiring her in my kitchen!', '您要是不全职聘用她，亚瑟，我可要把她招进我的厨房啦！'),
    ('arthur', 'Hands off, Tessa! Hannah, would you stay as our permanent front desk manager?', '别跟我抢，泰莎！汉娜，你愿意留下来担任我们正式的前台经理吗？'),
    ('hannah', 'Stay here with all of you? Yes, a hundred times yes!', '留在这里和你们大家在一起？愿意，一百个愿意！'),
    ('arthur', "Wonderful! Your name goes in Graham's big paper book in permanent ink!", '太棒了！你的名字要用永久墨水写进格雷厄姆那本大纸质登记簿里！'),
    ('hannah', 'Best first week of my life!', '这是我人生中最棒的入职第一周！'),
]
WALK = [
    (0, None, ["'泰莎，你的烤箱每天早上能烤出多少个肉桂卷和柠檬蛋糕？' 询问可数点心的具体数量时，句首固定用疑问词组", (None, 'how many'), '开启热火朝天的筹备计划。']),
    (1, None, ["'比我现在做的翻一倍都没问题！咱们真的要向整条街开放庭院咖啡馆吗？' 表达产量翻倍时，直接把双倍放在从句前说出", (None, 'Double what I make now'), '干脆利落又干劲十足。']),
    (2, None, ["'从明天早上八点就开始！屋里摆四张桌子，大树底下再摆三张！' 句首这个现在分词短语", (None, 'Starting tomorrow'), '常在口语中独立成句，雷厉风行地敲定开张日期。']),
    (3, None, ["'我梦寐以求的咖啡馆，就开在咱们自家庭院里！等着瞧我去告诉烘焙市集的伙伴们吧！' 名词梦想直接放在中心词前作定语，组成", (None, 'My dream cafe'), '地道表达心中向往已久的理想小店。']),
    (4, None, ["'接下来轮到你了，汉娜，今天是星期五，是你五天试用期的最后一天。' 修饰名词的复合定语", (None, 'five day trial week'), '中表示五天的名词保持单数形式，指入职考察试用的第一周。']),
    (5, None, ["'噢！忙着行李箱、锅炉还有那封信，我竟然忘得一干二净了！' 副词修饰过去式动词构成", (None, 'I completely forgot'), '自然道出这一周充实得让人忘了时间。']),
    (6, None, ["'星期一你推开了咱们那扇难搞的门；从那以后，你保住了客房、水管、早餐，还有咱们的租约。' 承上启下的时间短语", (None, 'since then'), '意为从那时起直到现在，把汉娜五天来的功劳串联成线。']),
    (7, None, ["'您要是不全职聘用她，亚瑟，我可要把她招进我的厨房啦！' 职场里正式全职录用某人，固定说", (None, 'hire her full time'), '泰莎用抢人玩笑表达对汉娜的喜爱。']),
    (8, None, ["'别跟我抢，泰莎！汉娜，你愿意留下来担任我们正式的前台经理吗？' 活泼俏皮的口语短语", (None, 'Hands off'), '字面意思是把手拿开、别打主意；随后郑重用委婉邀请句', (None, 'would you stay'), '发出正式聘请。']),
    (9, None, ["'留在这里和你们大家在一起？愿意，一百个愿意！' 满口答应时用夸张叠语", (None, 'a hundred times yes'), '把欣喜与归属感推向顶点。']),
    (10, None, ["'太棒了！你的名字要用永久墨水写进格雷厄姆那本大纸质登记簿里！' 表示使用某种书写墨水时用介词搭配成", (None, 'in permanent ink'), '呼应第一集铅笔登记簿的伏笔，寓意正式成为一家人。']),
    (11, None, ["'这是我人生中最棒的入职第一周！' 省去主谓的感叹句", (None, 'Best first week of my life'), '用最高级为汉娜精彩的试用周画上圆满惊叹号。']),
]
