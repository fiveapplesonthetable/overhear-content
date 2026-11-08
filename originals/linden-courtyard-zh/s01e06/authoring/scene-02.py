# Authoring module for linden-courtyard-zh-s01e06-scene-02.
ID = 'linden-courtyard-zh-s01e06-scene-02'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = 'The Wooden Train  (木头小火车)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'caleb': 'Caleb', 'owen': 'Owen', 'evelyn': 'Evelyn'}
INTRO = '凯勒布打开深蓝行李箱，取出那件层层白纸包裹的木雕小火车头。就在兄弟俩低头查看车轮底下的铅笔字迹时，伊芙琳女士微笑着走了过来。我们先听为快。'
OPENER = '现在让我们逐句细听这场跨越二十五年的温馨重聚。'
TRANSITION = '品味了这些充满诗意的句子，我们再完整听一遍整场戏。'
OUTRO = '儿时的木头火车头回到了哥哥手中，连当年的钢琴老师也同坐一桌。可与此同时，前厅里的亚瑟正对着那封挂号信发愁呢。待会儿见。'
CLOSING = ('evelyn', 'See you later!')
STORY = [
    ('caleb', 'Before the movers cleared Linden Street, I saved this box from the attic shelf.', '在搬家工人清空菩提树街老宅之前，我从阁楼架子上把这只盒子抢救了下来。'),
    ('owen', "Open the white paper... no! Grandfather's carved wooden train engine!", '打开这层白纸……天哪！是爷爷亲手雕刻的木头火车头！'),
    ('caleb', 'Look underneath the wheels. Your name and mine are still penciled there.', '快看车轮底下。你的名字和我的名字还用铅笔写在上面呢。'),
    ('owen', 'I thought this was lost when we sold the house! Why keep it for me?', '我还以为卖房子的时候它早就丢了！为什么要替我留着它呢？'),
    ('caleb', 'Because a house is brick and timber, Owen, while family is what we keep.', '因为房子不过是砖块和木料，欧文，而家人情分才是我们真正留住的东西。'),
    ('evelyn', 'And you two boys kept the best part of Number twelve right here.', '而你们这两个孩子，把十二号老宅最珍贵的部分好好留在了这里。'),
    ('owen', "Excuse me, ma'am... wait. That voice! Miss Evelyn, my piano teacher?!", '失礼了，女士……等等。这声音！伊芙琳女士，我的钢琴老师？！'),
    ('evelyn', 'Still waiting for you to play your F major scale slowly, Owen!', '我可还在等你把那串单降号大调音阶慢悠悠弹稳呢，欧文！'),
    ('owen', 'Am I dreaming?! Did you plan this whole reunion, Caleb?', '我是在做梦吗？！这一整场重聚都是你策划好的吗，凯勒布？'),
    ('caleb', "Pure luck, and one swapped blue suitcase on Monday morning's train!", '纯属运气，外加星期一早班火车上拿错的一只蓝色行李箱！'),
    ('evelyn', 'Life arranges better duets than we do, my dear boys.', '生活编排出的二重奏可比我们自己谱写的精彩多了，亲爱的孩子们。'),
    ('owen', 'Please sit with us, Miss Evelyn! Tell me I am not twenty-five years late for my lesson!', '快请坐到我们这儿来吧，伊芙琳女士！快告诉我这堂课我没有迟到二十五年！'),
]
WALK = [
    (0, None, ["'在搬家工人清空菩提树街老宅之前，我从阁楼架子上把这只盒子抢救了下来。' 英语在移动一词后加上表示人的后缀并用复数", (None, 'the movers'), '专门指代搬家公司的工人。']),
    (1, None, ["'打开这层白纸……天哪！是爷爷亲手雕刻的木头火车头！' 英语里的复合名词", (None, 'train engine'), '特指整列火车最前面牵引动力的火车头，正是第一集摇晃作响的神秘物件。']),
    (2, None, ["'快看车轮底下。你的名字和我的名字还用铅笔写在上面呢。' 表示正下方的介词", (None, 'underneath'), '强调物品底面的位置；并列主语', (None, 'Your name and mine'), '用独立物主代词避免重复名字一词。']),
    (3, None, ["'我还以为卖房子的时候它早就丢了！为什么要替我留着它呢？' 口语中疑问词直接加动词原形", (None, 'Why keep it'), '省去助动词与主语，急切又真挚地追问弟弟的心意。']),
    (4, None, ["'因为房子不过是砖块和木料，欧文，而家人情分才是我们真正留住的东西。' 句末这个表语从句", (None, 'what we keep'), '字面意思是我们所珍藏留存之物，用最朴素的词说出全剧最动人的哲理。']),
    (5, None, ["'而你们这两个孩子，把十二号老宅最珍贵的部分好好留在了这里。' 长辈眼中无论过去多少年他们仍是少年，同位语短语", (None, 'you two boys'), '听来格外慈祥亲切。']),
    (6, None, ["'失礼了，女士……等等。这声音！伊芙琳女士，我的钢琴老师？！' 这里的双词复合名词", (None, 'piano teacher'), '把乐器直接放在老师前面作定语，道出欧文听声辨人的惊喜。']),
    (7, None, ["'我可还在等你把那串单降号大调音阶慢悠悠弹稳呢，欧文！' 英语音乐术语用字母标记调名，把带一个降号的大调音阶称为", (None, 'F major scale'), '老师一句玩笑瞬间唤醒了童年琴房的记忆。']),
    (8, None, ["'我是在做梦吗？！这一整场重聚都是你策划好的吗，凯勒布？' 遇到不可思议的惊喜时，现在进行时疑问句", (None, 'Am I dreaming'), '生动传达出恍如梦境的惊叹。']),
    (9, None, ["'纯属运气，外加星期一早班火车上拿错的一只蓝色行李箱！' 两个词组成的感叹短语", (None, 'Pure luck'), '意为十足的巧合与好运，概括了这一整周阴差阳错的奇妙缘分。']),
    (10, None, ["'生活编排出的二重奏可比我们自己谱写的精彩多了，亲爱的孩子们。' 比较结构末尾用助动词替代前文动词，写成", (None, 'than we do'), '避免重复编排一词，行文优雅简练。']),
    (11, None, ["'快请坐到我们这儿来吧，伊芙琳女士！快告诉我这堂课我没有迟到二十五年！' 固定形容词搭配", (None, 'late for my lesson'), '表示上课迟到，欧文顺着老师的话幽默接梗，满院都是笑声。']),
]
