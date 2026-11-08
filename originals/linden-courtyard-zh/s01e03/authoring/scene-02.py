# Authoring module for linden-courtyard-zh-s01e03-scene-02.
ID = 'linden-courtyard-zh-s01e03-scene-02'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'The Sunny Attic  (向阳的阁楼房)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '汉娜、格雷厄姆和泰莎一口气爬上安静的三楼阁楼房，一边听着屋顶上的雨声，一边盘点房间里还缺哪些布置。先完整听一遍这段对话。'
OPENER = '接下来我们放慢语速，逐句听听他们是怎么盘点房间的。'
TRANSITION = '熟悉了这些描述房间陈设的表达，我们再完整听一遍。'
OUTRO = '木梁温馨、热水充足，只要再添上铜台灯、地毯和软枕头，这间阁楼房就能焕然一新了。我们待会儿见。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('hannah', 'Oh, look at this room! Big wooden beams and a window over the courtyard!', '噢，快看这间屋子！粗大的木房梁，还有一扇朝向庭院的窗户！'),
    ('tessa', 'Listen to the rain on the roof. It feels so cozy up here!', '听听屋顶上的雨声。待在上面这儿感觉真温馨啊！'),
    ('graham', 'Dry, warm, and quiet. Now tell me what is missing.', '干燥、暖和又安静。现在告诉我还缺些什么。'),
    ('hannah', 'Okay: there is a bed, a table, and a chair, but no bedside lamp.', '好：有一张床、一张桌子和一把椅子，但没有床头灯。'),
    ('tessa', 'And no mirror on the wall, and the floor feels bare without a rug.', '而且墙上没有镜子，地上没铺地毯也显得空荡荡的。'),
    ('graham', 'There is a brass reading lamp in my workshop downstairs.', '楼下我的工具间里有一盏黄铜阅读灯。'),
    ('tessa', 'And I have two soft pillows and a woven blue rug in the closet!', '而且我储藏柜里有两个软枕头和一块编织蓝地毯！'),
    ('hannah', 'What about the small bathroom next door? Does the light work?', '隔壁的小洗手间呢？电灯亮不亮？'),
    ('graham', 'New bulb last week, clean soap, plenty of hot water.', '上周刚换的新灯泡，干净香皂，还有充足的热水。'),
    ('tessa', 'Give us fifteen minutes and this attic will beat room seven!', '给我们十五分钟，这间阁楼房准能胜过七号房！'),
    ('hannah', 'Grab those cardboard boxes, Graham. Down the stairs we go!', '抱起那些纸板箱吧，格雷厄姆。咱们下楼喽！'),
    ('graham', 'Careful on the turn, do not bump the wall!', '拐弯处当心点，别磕碰到墙壁！'),
]
WALK = [
    (0, None, ["'噢，快看这间屋子！粗大的木房梁，还有一扇朝向庭院的窗户！' 想引起大家注意眼前的景象，必须搭配介词才能接宾语，说出", (None, 'look at this room'), '单用动词看是不能直接跟房间的。']),
    (1, None, ["'听听屋顶上的雨声。待在上面这儿感觉真温馨啊！' 和看一样，专注倾听某个声音时，英语也要在动词后紧跟介词，说成", (None, 'Listen to the rain'), '邀大家一起静心细听雨落屋檐。']),
    (2, None, ["'干燥、暖和又安静。现在告诉我还缺些什么。' 在动词后面接宾语从句时，如果疑问词本身就是主语，语序保持不变，直接说", (None, 'what is missing'), '自然表达“缺了什么东西”。']),
    (3, None, ["'好：有一张床、一张桌子和一把椅子，但没有床头灯。' 列举屋里现存的多样物品时，存现句的系动词要跟着紧挨它的第一个单数名词走，说成", (None, 'there is a bed'), '这就是英语里常见的就近原则。']),
    (4, None, ["'而且墙上没有镜子，地上没铺地毯也显得空荡荡的。' 镜子或画框贴挂在墙体表面，英语固定使用表面接触介词，表达为", (None, 'on the wall'), '而不用表示嵌在墙体内部的词。']),
    (5, None, ["'楼下我的工具间里有一盏黄铜阅读灯。' 英语里的方位词", (None, 'downstairs'), '本身就已经是副词，直接放在地点名词后面修饰“在楼下的工具间”，前面绝不需要再加任何介词。']),
    (6, None, ["'而且我储藏柜里有两个软枕头和一块编织蓝地毯！' 形容手工梭织而成的织物质感时，英语用编织的过去分词", (None, 'woven'), '放在颜色和名词前面作定语，显得格外温馨雅致。']),
    (7, None, ["'隔壁的小洗手间呢？电灯亮不亮？' 盘点完卧室顺势把话题转到隔壁区域时，句首用", (None, 'What about'), '承上启下，轻松引出“那……怎么样呢”的追问。']),
    (8, None, ["'上周刚换的新灯泡，干净香皂，还有充足的热水。' 日常口语表示分量绰绰有余，用短语", (None, 'plenty of hot water'), '比死板的许多更显丰盛贴心，可数和不可数名词都能接。']),
    (9, None, ["'给我们十五分钟，这间阁楼房准能胜过七号房！' 这里的动词原意是击败，在口语里说", (None, 'will beat'), '生动表达品质上“比……更胜一筹、完全盖过风头”。']),
    (10, None, ["'抱起那些纸板箱吧，格雷厄姆。咱们下楼喽！' 把表示方向的介词短语提前到句首，说出", (None, 'Down the stairs we go'), '自带一种轻快活泼的节奏感，就像喊着号子一起出发。']),
    (11, None, ["'拐弯处当心点，别磕碰到墙壁！' 搬东西提醒别人别撞到墙面时，用否定祈使句", (None, 'do not bump'), '这个动词专门形容不算太重但闷响一下的磕碰。']),
]
