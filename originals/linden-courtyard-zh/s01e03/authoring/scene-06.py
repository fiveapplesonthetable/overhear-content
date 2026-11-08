# Authoring module for linden-courtyard-zh-s01e03-scene-06.
ID = 'linden-courtyard-zh-s01e03-scene-06'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = 'A Five-Star Sigh of Relief  (如释重负的惊喜)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '回到楼下前台，亚瑟得知客人不仅没发火还连声道谢，顿时喜出望外。可就在这时，汉娜发现柜台上落了一本棕色小皮笔记本，里面画满了整条街客栈的速写和评分。我们先听为快。'
OPENER = '现在放慢节奏，一句一句听听他们是怎么猜出客人“神秘身份”的。'
TRANSITION = '理清了这些生动的口语表达，我们再连贯听一遍。'
OUTRO = '众人误以为凯勒布是波特兰旅游指南的暗访评审员，正打算悄悄把笔记本送回楼上，角落里却突然传来一阵响亮的金属撞击声。我们待会儿见。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('arthur', 'Well? Did he shout? Did he ask for his money back?', '怎么样？他大喊大叫了吗？他要求退钱了吗？'),
    ('hannah', 'Neither! He loved the quiet roof beams and thanked us.', '都没有！他特别喜欢安静的屋顶木梁，还向我们道了谢。'),
    ('arthur', 'Hannah, you have a gift for hospitality! My blood pressure is saved!', '汉娜，你天生就有做旅馆待客这一行的天赋！我的血压得救啦！'),
    ('tessa', 'He even finished every drop of vegetable soup before going up.', '他上楼之前甚至把那杯蔬菜汤喝得一滴不剩。'),
    ('hannah', 'Wait, whose small brown leather notebook is this on the counter?', '等等，柜台上这本棕色小皮笔记本是谁的呀？'),
    ('tessa', 'Caleb set it down when he took the dry towel from me!', '凯勒布刚从我手里接干毛巾的时候把它顺手放下了！'),
    ('arthur', 'Do not snoop, of course... wait, it fell open to the middle page!', '当然不能偷看啦……等等，它自己翻开停在中间那一页了！'),
    ('hannah', 'Why are there neat pencil drawings of three guesthouses on our street?', '为什么上面画着咱们这条街上三家客栈工整的铅笔速写呢？'),
    ('tessa', "Look at the words beside ours: 'Courtyard width, street noise, quiet score: nine out of ten!'", '快看咱们客栈旁边的字：“庭院宽度、街道噪音、安静评分：十分中的九分！”'),
    ('arthur', 'Nine out of ten?! Nobody measures lobbies unless...', '十分中的九分？！没人会去测量旅馆大堂，除非……'),
    ('tessa', 'Unless he writes for the annual Portland Travel Guide!', '除非他是给年度波特兰旅游指南撰稿的评审员！'),
    ('hannah', 'Quick, close it! Let us take it upstairs... wait, what is that loud clanking sound?', '快合上！咱们赶紧把它送上楼……等等，那阵响亮的金属哐当声是什么？'),
]
WALK = [
    (0, None, ["'怎么样？他大喊大叫了吗？他要求退钱了吗？' 要求商家退还已付的房款，日常口语不用生僻专业词，直接说", (None, 'ask for his money back'), '把副词放在钱的后面表示“把钱要回来”。']),
    (1, None, ["'都没有！他特别喜欢安静的屋顶木梁，还向我们道了谢。' 当别人一连问了两个是非问题，而你要把两件事双双否定掉时，单用一个词", (None, 'Neither'), '就能干净利落地回答“两个都没有”。']),
    (2, None, ["'汉娜，你天生就有做旅馆待客这一行的天赋！我的血压得救啦！' 夸奖某人在某方面特别有灵气和才华，固定搭配是", (None, 'have a gift for'), '这里的礼物一词引申为老天赏赐的天赋。']),
    (3, None, ["'他上楼之前甚至把那杯蔬菜汤喝得一滴不剩。' 当时间介词后面没有跟主语时，动词直接变成动名词形式，说成", (None, 'before going up'), '简洁流畅地交代“在上楼之前”。']),
    (4, None, ["'等等，柜台上这本棕色小皮笔记本是谁的呀？' 询问眼前的物品归谁所有，句首用疑问所有格代词", (None, 'whose'), '紧贴着后面一长串名词短语“棕色小皮笔记本”一起提问。']),
    (5, None, ["'凯勒布刚从我手里接干毛巾的时候把它顺手放下了！' 把手里拿着的东西平稳放到台面上，短语动词是", (None, 'set it down'), '当代词做宾语时，必须夹在动词和副词正中间。']),
    (6, None, ["'当然不能偷看啦……等等，它自己翻开停在中间那一页了！' 书本或册子顺势散开、摊开在桌面上，英语形象地把掉落和形容词结合成", (None, 'fell open'), '巧妙替亚瑟找了个“不是故意偷看”的借口。']),
    (7, None, ["'为什么上面画着咱们这条街上三家客栈工整的铅笔速写呢？' 把存现句变成特殊疑问句时，把系动词提前到引导词前面，说出", (None, 'Why are there'), '因为后面的速写是复数，所以系动词对应使用复数形式。']),
    (8, None, ["'快看咱们客栈旁边的字：“庭院宽度、街道噪音、安静评分：十分中的九分！”' 英语表达打分比例非常直观，", (None, 'nine out of ten'), '字面意思是十个里面占了九个，也就是满分十分得了九分。']),
    (9, None, ["'十分中的九分？！没人会去测量旅馆大堂，除非……' 引出唯一的例外推论时，连词", (None, 'unless'), '相当于汉语的“除非……否则绝不会”，吊足了大家的胃口。']),
    (10, None, ["'除非他是给年度波特兰旅游指南撰稿的评审员！' 泰莎顺着上一句的话头接下去，说出", (None, 'Unless he writes'), '用一般现在时表示某人的职业工作是为指南杂志撰稿。']),
    (11, None, ["'快合上！咱们赶紧把它送上楼……等等，那阵响亮的金属哐当声是什么？' 英语有很多生动的拟声词，形容厚重金属管道互相撞击发出的沉闷巨响就叫", (None, 'clanking sound'), '一听就让人联想到老旧暖气管。']),
]
