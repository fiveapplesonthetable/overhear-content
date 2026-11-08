# Authoring module for linden-courtyard-zh-s01e04-scene-04.
ID = 'linden-courtyard-zh-s01e04-scene-04'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 4
SCENE = 4
TITLE = 'Down in the Cellar  (地下锅炉房抢修)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah'}
INTRO = '汉娜气喘吁吁地冲进地下锅炉房，递上刚买回来的两只黄铜阀门。她打稳手电筒配合格雷厄姆拧紧新螺纹、点亮蓝色火苗，热水终于重新奔涌进管道！我们先听一遍整场戏。'
OPENER = '现在让我们放慢节奏，一句一句拆解这段默契十足的抢修对话。'
TRANSITION = '熟悉了这些实用的动手操作表达，我们再完整听一遍。'
OUTRO = '铜管迅速升温，只要三分钟热水就能一路送到三楼。这对最佳搭档漂亮地打赢了清晨热水保卫战！我们下场戏见。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Here are both brass valves, Graham! Catch my breath? Never!', '两只黄铜阀门都在这儿啦，格雷厄姆！喘口气？绝不耽误！'),
    ('graham', 'Hold this flashlight steady on the pipe joint right here.', '把手电筒拿稳了，照准这儿的管道接口。'),
    ('hannah', 'Got it! Did you turn off the main water tap already?', '好嘞！你已经把总水阀关掉了吗？'),
    ('graham', 'Off and drained. Pass me the heavy wrench on your left.', '关掉并且排空积水了。把你左手边那把重扳手递给我。'),
    ('hannah', 'This big iron one? Here you go.', '是这把大铁扳手吗？给您。'),
    ('graham', 'One turn, two turns... look how clean that new brass thread fits.', '拧一圈，拧两圈……快看这新黄铜螺纹咬合得多利落严实。'),
    ('hannah', 'No drips at all! Can we light the boiler now?', '一滴水都不漏！咱们现在可以点着锅炉了吗？'),
    ('graham', 'Open the blue wheel slowly to the left, not too fast.', '把那个蓝色手轮往左慢慢拧开，别拧得太快。'),
    ('hannah', 'Turning slowly... listen! Water is rushing in!', '正在慢慢拧……快听！水流哗哗涌进来了！'),
    ('graham', 'And there goes the burner flame, steady blue, just how it should be.', '燃烧器的火苗也着起来了，稳稳的蓝火，正该是这个样儿。'),
    ('hannah', 'Touch the copper pipe! It is warming up already!', '摸摸这根铜管！它已经在热起来了！'),
    ('graham', 'Three minutes to reach the third floor. Good run today, partner.', '三分钟就能送到三楼。今天这一趟跑得漂亮，好搭档。'),
]
WALK = [
    (0, None, ["'两只黄铜阀门都在这儿啦，格雷厄姆！喘口气？绝不耽误！' 剧烈奔跑之后停下来平复急促的呼吸，英语形象地说是“抓住自己的呼吸”，即", (None, 'Catch my breath'), '汉娜连气都顾不上喘就投入抢修。']),
    (1, None, ["'把手电筒拿稳了，照准这儿的管道接口。' 请帮手拿稳照明工具别晃动，在动词和宾语后面跟上形容词做补足语，说出", (None, 'Hold this flashlight steady'), '简洁清晰地交代动作要求。']),
    (2, None, ["'好嘞！你已经把总水阀关掉了吗？' 关闭水龙头、煤气阀或电灯开关，英语统统可以用短语动词", (None, 'turn off'), '最早就源于旋转阀门切断水流这个动作。']),
    (3, None, ["'关掉并且排空积水了。把你左手边那把重扳手递给我。' 修水管拧螺母必不可少的金属扳手，美式英语叫作", (None, 'wrench'), '注意开头的辅音字母完全不发音。']),
    (4, None, ["'是这把大铁扳手吗？给您。' 同事之间顺手把工具或物品递过去时，随口一句轻快的", (None, 'Here you go'), '自然又默契，相当于汉语里的“给你、拿好了”。']),
    (5, None, ["'拧一圈，拧两圈……快看这新黄铜螺纹咬合得多利落严实。' 感叹零件尺寸严丝合缝，用感叹从句", (None, 'how clean that new brass thread fits'), '这里的干净引申为切口利落、严密贴合。']),
    (6, None, ["'一滴水都不漏！咱们现在可以点着锅炉了吗？' 这里的词不是电灯名词，而是用作及物动词表示点火，说出", (None, 'light the boiler'), '也就是把燃气锅炉重新点火启动。']),
    (7, None, ["'把那个蓝色手轮往左慢慢拧开，别拧得太快。' 提醒操作幅度别超过安全限度时，用程度副词修饰快慢，说成", (None, 'too fast'), '叮嘱放水进炉时一定要循序渐进。']),
    (8, None, ["'正在慢慢拧……快听！水流哗哗涌进来了！' 形容水流带着强劲势头奔涌进空管道，现在进行时短语", (None, 'is rushing in'), '把耳朵听见的哗哗进水声描绘得活灵活现。']),
    (9, None, ["'燃烧器的火苗也着起来了，稳稳的蓝火，正该是这个样儿。' 看到机器运转恢复到最理想的标准状态，满意地点头说一句", (None, 'just how it should be'), '地道传达“这就对了、正该如此”。']),
    (10, None, ["'摸摸这根铜管！它已经在热起来了！' 描述冰凉的金属管道温度逐渐往上升，用现在进行时搭配短语动词说出", (None, 'is warming up'), '满是抢修成功的喜悦。']),
    (11, None, ["'三分钟就能送到三楼。今天这一趟跑得漂亮，好搭档。' 表示抵达某个地方或高度时，及物动词直接跟地点宾语，说出", (None, 'reach the third floor'), '中间绝不能多加任何方向介词。']),
]
