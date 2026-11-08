# Authoring module for linden-courtyard-zh-s01e04-scene-07.
ID = 'linden-courtyard-zh-s01e04-scene-07'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = 'Sunlight on the Tag  (阳光下的行李牌)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '格雷厄姆打扫行李储藏间时，把那只一直没人认领的蓝色行李箱暂时拎到了阳光明亮的前厅。伊芙琳女士凑近细看纸吊牌，竟认出了二十五年前自己每周五去教钢琴的菩提树街十二号！我们先听一遍整场戏。'
OPENER = '现在让我们放慢语速，一句一句细听这段尘封往事浮出水面的对话。'
TRANSITION = '熟悉了这些充满故事感的表达，我们再完整听一遍。'
OUTRO = '菩提树街十二号的老木匠、弹钢琴的哥哥，还有痴迷小火车的弟弟……所有线索都和箱子里的木头玩具小火车对上了！我们下场戏见。'
CLOSING = ('evelyn', 'Bye for now!')
STORY = [
    ('graham', 'Let me set this blue suitcase here for five minutes while I sweep the closet.', '趁我清扫储藏间的工夫，让我把这只蓝行李箱在这儿放五分钟。'),
    ('hannah', 'Careful with it, Graham. Friday at noon is tomorrow!', '轻拿轻放啊，格雷厄姆。星期五中午就是明天！'),
    ('evelyn', "Oh, is that the twin suitcase from Monday's train?", '噢，那就是星期一那趟火车上拿错的双胞胎行李箱吗？'),
    ('hannah', "Yes, ma'am, still waiting for its owner.", '是的，夫人，还在等着它的主人来认领呢。'),
    ('evelyn', 'May I look at the paper tag again here in the bright sunlight?', '我可以借着这明亮的阳光再看看那张纸吊牌吗？'),
    ('graham', "Go right ahead, ma'am. Monday afternoon the lobby was dark.", '请尽管看吧，夫人。星期一下午大堂里光线太暗了。'),
    ('evelyn', 'Wait a moment... Number twelve, Linden Street, and two childhood initials written in the corner!', '等一下……菩提树街十二号，边角上还写着两个童年名字的首字母缩写！'),
    ('hannah', 'Miss Evelyn, you look amazed! Do you know Number twelve, Linden Street?', '伊芙琳女士，您看起来好惊讶呀！您知道菩提树街十二号吗？'),
    ('evelyn', 'Know it? Every Friday for six years I climbed those wooden stairs to teach piano!', '何止知道？整整六年里，每个星期五我都爬上那段木楼梯去教钢琴！'),
    ('graham', 'Twenty-five years ago? In that same house?', '二十五年前？就在同一栋老房子里？'),
    ('evelyn', 'A carpenter lived there with his two grandsons. The older boy played piano, and the little one loved trains!', '一位老木匠带着两个孙子住在那儿。哥哥弹钢琴，小的那个超爱火车！'),
    ('hannah', 'A carpenter... and a little wooden toy train inside the bag!', '一位木匠……而且包里正好装着一列木头玩具小火车！'),
]
WALK = [
    (0, None, ["'趁我清扫储藏间的工夫，让我把这只蓝行李箱在这儿放五分钟。' 说明动作持续一小段时间，用介词搭配时间长度说出", (None, 'for five minutes'), '清晰交代只是临时摆放五分钟。']),
    (1, None, ["'轻拿轻放啊，格雷厄姆。星期五中午就是明天！' 表示正午十二点整这个精确的时间点，英语固定用小介词搭配名词，说成", (None, 'at noon'), "中间同样不加任何冠词。"]),
    (2, None, ["'噢，那就是星期一那趟火车上拿错的双胞胎行李箱吗？' 两只外观一模一样、成双配对的箱子，英语直接借用双胞胎一词作定语，叫作", (None, 'twin suitcase'), '既形象又好记。']),
    (3, None, ["'是的，夫人，还在等着它的主人来认领呢。' 把等待的对象引出来，必须给动词配好搭档介词，说出", (None, 'waiting for its owner'), '注意物主代词不带撇号，指代行李箱的主人。']),
    (4, None, ["'我可以借着这明亮的阳光再看看那张纸吊牌吗？' 表示置身于灿烂的阳光笼罩之下，英语用空间介词说成", (None, 'in the bright sunlight'), '就像整个人沐浴在光线里一样。']),
    (5, None, ["'请尽管看吧，夫人。星期一下午大堂里光线太暗了。' 爽快答应别人的礼貌请求时，一句热情大方的", (None, 'Go right ahead'), '比单调的可以地道得多，意思是“您请便、尽管看”。']),
    (6, None, ["'等一下……菩提树街十二号，边角上还写着两个童年名字的首字母缩写！' 过去分词短语放在名词后面作定语，", (None, 'written in the corner'), "生动描绘出写在角落里的字迹。"]),
    (7, None, ["'伊芙琳女士，您看起来好惊讶呀！您知道菩提树街十二号吗？' 看到对方脸上露出震惊神色，用感官系动词搭配过去分词形容词说出", (None, 'you look amazed'), '描述人的内心感受一定要用词尾带过去分词特征的形式。']),
    (8, None, ["'何止知道？整整六年里，每个星期五我都爬上那段木楼梯去教钢琴！' 讲授乐器或学科课程时，动词后面直接跟乐器名称，不加定冠词，说成", (None, 'teach piano'), '和弹钢琴必须加定冠词的习惯恰好形成对比。']),
    (9, None, ["'二十五年前？就在同一栋老房子里？' 把具体时间段放在副词前面，组成", (None, 'Twenty-five years ago'), '直接把时间坐标拉回到四分之一个世纪以前。']),
    (10, None, ["'一位老木匠带着两个孙子住在那儿。哥哥弹钢琴，小的那个超爱火车！' 为了避免重复前面刚提过的男孩一词，英语用代词顶替，说出", (None, 'the little one'), '亲切自然地指代“年纪小的那个孩子”。']),
    (11, None, ["'一位木匠……而且包里正好装着一列木头玩具小火车！' 多个形容词排成一队时遵循固定语序：", (None, 'little wooden toy train'), '先说大小，再说木头材质，接着是用途类别玩具，最后才是核心词火车。']),
]
