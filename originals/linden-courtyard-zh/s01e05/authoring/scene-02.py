# Authoring module for linden-courtyard-zh-s01e05-scene-02.
ID = 'linden-courtyard-zh-s01e05-scene-02'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = 'Three Years of Silence  (三年的沉默)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '回到前台，格雷厄姆打开储物柜，把保管了一整周的深蓝行李箱交还给凯勒布。凯勒布终于说起了他和哥哥欧文之间长达三年的隔阂。先完整听一遍吧。'
OPENER = '现在让我们逐句细听，了解这段兄弟心结背后的英语表达。'
TRANSITION = '听懂了每句话里的细腻情感，我们再连贯听一遍整场对话。'
OUTRO = '原来那张没敢署名的明信片背后，藏着弟弟既想求和又怕被拒的忐忑心情。幸好在这家温暖的客栈里，他不再打算躲去街对面了。待会儿见。'
CLOSING = ('graham', 'See you later!')
STORY = [
    ('graham', 'So our mystery Friday caller was sleeping upstairs under my attic roof all along.', '原来我们那位神秘的星期五来电人，一直就睡在楼上我的阁楼屋顶下呀。'),
    ('caleb', 'Sorry for the trouble, Graham. Thank you for guarding this bag all week.', '给您添麻烦了，格雷厄姆。谢谢您整整一周都替我守着这只包。'),
    ('hannah', 'Why could you not simply hand Owen the wooden train at his front door?', '你为什么不能干脆去欧文家门口，亲手把木头小火车交给他呢？'),
    ('caleb', 'Three years ago, after our grandfather died, Owen and I argued bitterly over selling the old house.', '三年前爷爷去世后，欧文和我因为卖老房子的事激烈争吵了一番。'),
    ('graham', 'Family houses and old memories, those arguments cut deep.', '家族老宅加上旧日回忆，那种争吵最伤感情。'),
    ('caleb', 'We have not spoken since that day. Last week I sent him one short postcard.', '从那天起我们就再没说过话。上周我给他寄了一张简短的明信片。'),
    ('hannah', 'Asking him to meet you here on Friday at noon?', '约他星期五中午来这里见你吗？'),
    ('caleb', "Actually, I only wrote: 'Something from Grandfather is waiting at the Linden Courtyard Inn Friday at noon.'", '其实我只写了：“有件爷爷留下的东西，星期五中午在菩提树庭院客栈等你。”'),
    ('graham', 'Aha! You feared that if you signed your name, stubborn big brother would stay home!', '啊哈！你是怕一旦签上你的名字，倔脾气的大哥就会待在家里不肯来！'),
    ('caleb', 'You know older brothers well, Graham.', '您真了解当哥哥的人，格雷厄姆。'),
    ('hannah', 'Wait, were you planning to let the clerk hand him the bag and watch from across the street?!', '等等，你原本打算让前台店员把包交给他，自己躲在街对面偷偷看吗？！'),
    ('caleb', 'That was my cowardly Monday plan... before I met all of you.', '那是我星期一时的胆小鬼计划……在认识你们大家之前。'),
]
WALK = [
    (0, None, ["'原来我们那位神秘的星期五来电人，一直就睡在楼上我的阁楼屋顶下呀。' 句尾的副词短语", (None, 'all along'), '专门用来恍然大悟地感叹“从头到尾、自始至终原来都是如此”。']),
    (1, None, ["'给您添麻烦了，格雷厄姆。谢谢您整整一周都替我守着这只包。' 日常为给人添了周折而致歉时，一句得体诚恳的", (None, 'Sorry for the trouble'), '在生活和职场里都极其实用。']),
    (2, None, ["'你为什么不能干脆去欧文家门口，亲手把木头小火车交给他呢？' 名词“手”直接作及物动词，接双宾语组成", (None, 'hand Owen'), '简洁传神地表达“亲手递给欧文”。']),
    (3, None, ["'三年前爷爷去世后，欧文和我因为卖老房子的事激烈争吵了一番。' 谈论围绕某件事发生争执时，英语常在争吵后面接介词短语", (None, 'over selling'), '点明双方起分歧的具体原因。']),
    (4, None, ["'家族老宅加上旧日回忆，那种争吵最伤感情。' 格雷厄姆用简短有力的比喻", (None, 'cut deep'), '字面意思是割得很深，形象道出亲人之间的争执往往格外伤人。']),
    (5, None, ["'从那天起我们就再没说过话。上周我给他寄了一张简短的明信片。' 现在完成时搭配时间起点", (None, 'since that day'), "清楚表明沉默从那一天一直延续到今天。"]),
    (6, None, ["'约他星期五中午来这里见你吗？' 汉娜顺着对方上一句的明信片接着追问，直接用分词短语", (None, 'Asking him to meet you'), '承接上文补充提问，对话衔接紧凑自然。']),
    (7, None, ["'其实我只写了：“有件爷爷留下的东西，星期五中午在菩提树庭院客栈等你。”' 字条里用现在进行时", (None, 'is waiting at'), '把静物拟人化，仿佛爷爷的遗物正静静在客栈等候他到来。']),
    (8, None, ["'啊哈！你是怕一旦签上你的名字，倔脾气的大哥就会待在家里不肯来！' 站在过去的时间点推测假设的后果，英语用过去将来结构", (None, 'would stay home'), '准确写出心里担心的情形。']),
    (9, None, ["'您真了解当哥哥的人，格雷厄姆。' 称赞对方深谙某类人的脾气秉性时，把副词放在宾语后面说出", (None, 'know older brothers well'), '简短一句透着会心的默契。']),
    (10, None, ["'等等，你原本打算让前台店员把包交给他，自己躲在街对面偷偷看吗？！' 双重介词短语", (None, 'from across the street'), "把视线起点定在马路对过，画面感十足地勾勒出远远张望的样子。"]),
    (11, None, ["'那是我星期一时的胆小鬼计划……在认识你们大家之前。' 注意词尾带后缀的", (None, 'cowardly'), '虽然看着像副词，其实是个地道的形容词，用来坦率自嘲当初怯懦的打算。']),
]
