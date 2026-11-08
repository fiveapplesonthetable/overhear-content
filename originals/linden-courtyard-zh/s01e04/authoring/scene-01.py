# Authoring module for linden-courtyard-zh-s01e04-scene-01.
ID = 'linden-courtyard-zh-s01e04-scene-01'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Six Forty-Five  (清晨六点四十五分)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah'}
INTRO = '天刚蒙蒙亮，客人们还没起床，格雷厄姆把拆下来的坏黄铜阀门交给汉娜，细致指点她怎么过石桥去老五金店买新零件。我们先完整听一遍这段清晨出发前的对话。'
OPENER = '现在放慢语速，一句一句跟着他们学习问路与指路的实用表达。'
TRANSITION = '记住了这些清晰的指路短语，我们再连贯听一遍。'
OUTRO = '四号房的客人七点十五分就要起床了，汉娜揣好旧阀门，一路默念着尺寸飞奔出门。我们下场戏见。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Graham! Are the showers upstairs really cold already?', '早上好，格雷厄姆！楼上淋浴间的水真的已经变凉了吗？'),
    ('graham', 'Cold as river water. Take this broken brass valve in your coat pocket.', '凉得像河水一样。把这个坏掉的黄铜阀门揣进你的外套口袋里。'),
    ('hannah', 'Got it. Now tell me how to find the hardware shop.', '明白。现在告诉我怎么找到那家五金店吧。'),
    ('graham', 'Turn left outside our gate and walk straight to the stone bridge.', '出了咱们大门往左转，一直走到石桥那儿。'),
    ('hannah', 'Left at the gate, straight to the bridge. Do I cross the river?', '出大门左转，直走去石桥。我要过河吗？'),
    ('graham', 'Yes, cross the bridge, then pass the green pharmacy on your right.', '对，过桥，然后经过你右手边那家绿色药店。'),
    ('hannah', 'Bridge, then green pharmacy on the right. And after that?', '过桥，然后是右手边的绿色药店。在那之后呢？'),
    ('graham', 'Turn left into the small square. Look for a blue wooden door.', '左转拐进小广场。找一扇蓝色的木门。'),
    ('hannah', 'Does the shop have a big sign outside?', '店门外面挂着大招牌吗？'),
    ('graham', 'Only a painted golden key above the door. Show the clerk this valve.', '门上方只画着一把金色钥匙。把这个阀门拿给店员看。'),
    ('hannah', 'Twenty millimeters, brass, boiler valve. I will repeat it all the way!', '二十毫米、黄铜、锅炉阀门。我会一路念叨着它的！'),
    ('graham', 'Run fast, Hannah. Room four wakes up at seven fifteen!', '快跑吧，汉娜。四号房七点十五分就起床啦！'),
]
WALK = [
    (0, None, ["'早上好，格雷厄姆！楼上淋浴间的水真的已经变凉了吗？' 地点副词放在名词后面作后置定语，说出", (None, 'Are the showers upstairs'), '自然流畅地询问“楼上的淋浴间是不是已经凉了”。']),
    (1, None, ["'凉得像河水一样。把这个坏掉的黄铜阀门揣进你的外套口袋里。' 口语里打比方常省掉第一个比较词，直接说", (None, 'Cold as river water'), '简短有画面感，生动形容水凉得像清晨的河水。']),
    (2, None, ["'明白。现在告诉我怎么找到那家五金店吧。' 接过东西或听懂指令时，美式口语最干脆的一句回应就是", (None, 'Got it'), '省去主语和助动词，地道传达“拿到了、明白了”。']),
    (3, None, ["'出了咱们大门往左转，一直走到石桥那儿。' 指路让人沿着路笔直往前走到某个地标，固定用", (None, 'walk straight to'), '中间的副词直接修饰步行，指明“径直走向……”。']),
    (4, None, ["'出大门左转，直走去石桥。我要过河吗？' 确认自己接下来该怎么走，英语常用一般现在时提问", (None, 'Do I cross'), '复述路线并核对步骤时显得格外清晰利落。']),
    (5, None, ["'对，过桥，然后经过你右手边那家绿色药店。' 指明建筑物位于行进方向的哪一侧，英语固定搭配表面介词说成", (None, 'on your right'), '千万别误用成表示在里面的介词。']),
    (6, None, ["'过桥，然后是右手边的绿色药店。在那之后呢？' 听别人一步步指路时，顺势追问下一步怎么走，一句简短的", (None, 'And after that'), '就能自然引出后续路线。']),
    (7, None, ["'左转拐进小广场。找一扇蓝色的木门。' 当转弯的动作直接带你进入某个广场或街巷时，转向后面紧跟动态介词，说出", (None, 'Turn left into'), '把“左转进入”合二为一。']),
    (8, None, ["'店门外面挂着大招牌吗？' 询问店铺门外的情况，只需在句尾轻轻放上地点副词", (None, 'outside'), '不需要再加任何多余的名词或介词。']),
    (9, None, ["'门上方只画着一把金色钥匙。把这个阀门拿给店员看。' 经典的英语双宾语祈使句", (None, 'Show the clerk this valve'), '先说看的对象店员，再说展示的物品阀门，紧凑又地道。']),
    (10, None, ["'二十毫米、黄铜、锅炉阀门。我会一路念叨着它的！' 表示从出发一直持续到目的地全程不间断，句尾加上短语", (None, 'all the way'), '生动描绘出汉娜边跑边背诵规格的模样。']),
    (11, None, ["'快跑吧，汉娜。四号房七点十五分就起床啦！' 英语口语里既可以用房号借指里面的客人，搭配短语动词说出", (None, 'wakes up'), '表示醒来起床；报钟点时也常直接连读数字', (None, 'seven fifteen'), '简洁明快地催促时间紧迫。']),
]
