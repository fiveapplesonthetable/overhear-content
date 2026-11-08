# Authoring module for linden-courtyard-zh-s01e05-scene-06.
ID = 'linden-courtyard-zh-s01e05-scene-06'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = 'Ten Minutes to Twelve  (差十分钟十二点)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '十一点五十分，店主亚瑟整理好领带走进前台。邮递员刚送来一封盖着红色印章的挂号信，可眼看正午将至，大家都把心思放在了庭院外。先完整听一遍吧。'
OPENER = '现在我们一句一句细听正午钟声敲响前前台里的热闹动静。'
TRANSITION = '掌握了这些鲜活的口语表达，我们再按正常语速听一遍整场戏。'
OUTRO = '那封来自房东律师的厚信封暂时躺在了登记簿旁，而街角教堂的正午钟声已经敲响了第一下。我们赶紧去铁门边看看，待会儿见。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'How does my tie look today, Hannah? Zero orange juice in sight!', '我今天的领带看起来怎么样，汉娜？半点橙汁渍都看不见吧！'),
    ('hannah', 'Sharp and spotless, Arthur! Even your glasses are on your nose instead of your forehead.', '利落又一尘不染，亚瑟！连您的眼镜都好好架在鼻梁上，没推到额头上呢。'),
    ('arthur', 'Progress! Today our courtyard hosts a family reunion. Quiet dignity from everyone!', '大有进步！今天咱们的庭院要接待一场家庭重聚。各位都要保持安静得体！'),
    ('tessa', 'Says the man peeking through the lace curtain every thirty seconds!', '说这话的人自己却每隔三十秒就扒着蕾丝窗帘偷看一回！'),
    ('arthur', 'I am checking the weather, Tessa! Who left this thick envelope by the bell?', '我那是在看天气，泰莎！是谁把这个厚信封留在按铃旁边的？'),
    ('hannah', 'The mailman just asked me to sign for it. It has a red property office stamp.', '邮递员刚才让我签收的。上面盖着红色的房产事务处印章。'),
    ('arthur', "From the building landlord's lawyer? Strange, our rent is paid until next summer.", '这栋楼房东的律师寄来的？真奇怪，咱们的房租一直付到了明年夏天呀。'),
    ('tessa', 'Open it after twelve, boss! Look at the clock: five minutes to noon!', '过了十二点再拆吧，老板！快看钟：差五分钟就到正午啦！'),
    ('arthur', 'Right you are. Paperwork can wait. Put it beside the book for now.', '你说得对。公文可以先等一等。暂时把它放在登记簿旁边吧。'),
    ('hannah', "I placed the blue suitcase right beside Caleb's table under the tree.", '我已经把那只蓝色行李箱稳稳放在树下凯勒布的桌子旁边了。'),
    ('tessa', 'And the teapot is hot! Everybody step back from the window!', '茶壶也滚烫热乎着呢！大家统统从窗户边往后退！'),
    ('arthur', 'Listen... the church clock down the street is starting to chime twelve!', '快听……顺着街道那头的教堂钟楼开始敲响正午十二点了！'),
]
WALK = [
    (0, None, ["'我今天的领带看起来怎么样，汉娜？半点橙汁渍都看不见吧！' 句末这个介词短语", (None, 'in sight'), '表示在视线范围之内，用来得意地宣告领带上再也瞧不见半点污渍。']),
    (1, None, ["'利落又一尘不染，亚瑟！连您的眼镜都好好架在鼻梁上，没推到额头上呢。' 这里用到的形容词", (None, 'spotless'), '在斑点词根后加上否定后缀，字面意思是毫无污点，夸赞衣着干净整洁。']),
    (2, None, ["'大有进步！今天咱们的庭院要接待一场家庭重聚。各位都要保持安静得体！' 名词主人直接活用作动词单三形式", (None, 'hosts'), '郑重表达客栈庭院今天承办并见证这场兄弟团聚。']),
    (3, None, ["'说这话的人自己却每隔三十秒就扒着蕾丝窗帘偷看一回！' 口语里温和调侃对方言行不一时，常倒装说出", (None, 'Says the man'), '幽默拆穿亚瑟嘴上叫大家镇定、自己却最心急。']),
    (4, None, ["'我那是在看天气，泰莎！是谁把这个厚信封留在按铃旁边的？' 疑问代词直接充当主语提问时无需助动词，一句", (None, 'Who left'), '自然引出那封神秘挂号信。']),
    (5, None, ["'邮递员刚才让我签收的。上面盖着红色的房产事务处印章。' 接收挂号信或快递包裹时，固定用短语", (None, 'sign for it'), '表示动笔签名确认收件。']),
    (6, None, ["'这栋楼房东的律师寄来的？真奇怪，咱们的房租一直付到了明年夏天呀。' 句尾的时间介词短语", (None, 'until next summer'), '清楚标出租金有效期一直延续到明年夏季。']),
    (7, None, ["'过了十二点再拆吧，老板！快看钟：差五分钟就到正午啦！' 英语报还差几分钟到整点时，用介词把分钟数连向下一个整点，说成", (None, 'five minutes to noon'), '地道表示十一点五十五分。']),
    (8, None, ["'你说得对。公文可以先等一等。暂时把它放在登记簿旁边吧。' 爽快赞同别人提醒时可说倒装短语", (None, 'Right you are'), '然后在句子末尾加上', (None, 'for now'), '表示眼下暂且先放一放。']),
    (9, None, ["'我已经把那只蓝色行李箱稳稳放在树下凯勒布的桌子旁边了。' 相比普通动词放，过去式", (None, 'I placed'), '更能体现小心翼翼、郑重摆放到位的动作。']),
    (10, None, ["'茶壶也滚烫热乎着呢！大家统统从窗户边往后退！' 催促围观的众人往后撤一步留出空间，直接用短语", (None, 'step back'), '画面感立刻活了起来。']),
    (11, None, ["'快听……顺着街道那头的教堂钟楼开始敲响正午十二点了！' 英语里的方位短语", (None, 'down the street'), '在日常口语中指顺着同一条街往前不远的地方，伴随着钟声拉满悬念。']),
]
