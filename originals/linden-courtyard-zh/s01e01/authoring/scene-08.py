# Authoring module for linden-courtyard-zh-s01e01-scene-08.
ID = 'linden-courtyard-zh-s01e01-scene-08'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'Left on the Step  (留在石阶上的箱子)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '夜里九点钟，庭院大门口的门铃突然响了一声。汉娜和格雷厄姆一起打开门，院子里空无一人，石阶上却静静放着一只深蓝色行李箱。先听一遍第一集压轴戏。'
OPENER = '现在让我们逐句拆解这段夜色中的悬念对话。'
TRANSITION = '揭开了信封里的神秘留言，我们再连贯听一遍整场戏。'
OUTRO = '伊芙琳自己的行李箱失而复得，可那位神秘物主却拜托客栈把装有木头小火车的蓝箱子一直保管到星期五！第一集就到这里，祝你晚安，我们第二集见。'
CLOSING = ('graham', 'Have a good night!')
STORY = [
    ('hannah', 'Did you hear that, Graham? Someone just rang the gate bell!', '格雷厄姆，你听见了吗？刚才有人按了院门铃！'),
    ('graham', "At nine o'clock? Wait, let us open the gate together.", '九点钟？等等，咱们一起去开大门。'),
    ('hannah', 'Hello? Good evening! Nobody is standing at the gate!', '喂，有人吗？晚上好！大门前根本没人站着呀！'),
    ('graham', 'Wait. Look down on the stone step.', '等等。往下面的石阶上看。'),
    ('hannah', "Another dark blue suitcase! Is this Miss Evelyn's bag?", '又是一只深蓝色行李箱！这是伊芙琳女士的包吗？'),
    ('graham', 'Check the zipper... yes, her initials are right here!', '看看拉链那儿……没错，她的姓名首字母就在这儿！'),
    ('hannah', 'Why did the person run away without taking his own suitcase back?', '为什么那个人没拿回他自己的行李箱就跑掉了呢？'),
    ('graham', 'Look, there is a folded white envelope taped to the handle.', '你看，提手上用胶带粘着一个折好的白信封。'),
    ('hannah', "Let me read it: 'Sorry for the mistake. Please keep my blue bag until Friday.'", '让我念念：“抱歉弄错了。请替我保管这只蓝包直到星期五。”'),
    ('graham', 'Until Friday? No name, no signature!', '一直到星期五？既没留名字，也没签落款！'),
    ('hannah', 'Why leave your own shoes and wooden train with strangers until Friday?', '干嘛把自己的鞋子和木头火车留在陌生人这儿一直到星期五呢？'),
    ('graham', 'Welcome to the Linden Courtyard Inn, Hannah. Your second day will not be boring.', '欢迎来到菩提树庭院客栈，汉娜。你上班的第二天可绝对不会无聊了。'),
]
WALK = [
    (0, None, ["'格雷厄姆，你听见了吗？刚才有人按了院门铃！' 夜深人静听到门外异响时，最自然的确认问句就是", (None, 'Did you hear that'), '用指示代词指代刚刚响起的那声铃音。']),
    (1, None, ["'九点钟？等等，咱们一起去开大门。' 表达不带分钟的整点时刻，英语在数字后面加上缩合词构成", (None, "nine o'clock"), "专门表示“九点整”。"]),
    (2, None, ["'喂，有人吗？晚上好！大门前根本没人站着呀！' 哪怕到了夜里，只要是见面打招呼，英语依然要说", (None, 'Good evening'), "而不能用道别睡觉时才说的晚安。"]),
    (3, None, ["'等等。往下面的石阶上看。' 动词后面加上表示向下的副词构成", (None, 'Look down'), '简洁有力地提醒同伴低头往脚下看。']),
    (4, None, ["'又是一只深蓝色行李箱！这是伊芙琳女士的包吗？' 看到同款式的第二只箱子出现，句首用限定词", (None, 'Another'), '精准表达“又一个、再一只”的惊喜。']),
    (5, None, ["'看看拉链那儿……没错，她的姓名首字母就在这儿！' 英语复数名词", (None, 'her initials'), '专指把名和姓的开头字母缩写印在皮具上的标记，一眼就能确认箱子归属。']),
    (6, None, ["'为什么那个人没拿回他自己的行李箱就跑掉了呢？' 介词后面如果要跟动作“拿走”，必须把动词变成动名词形式，组成", (None, 'without taking'), '地道表达“没拿……就离开了”。']),
    (7, None, ["'你看，提手上用胶带粘着一个折好的白信封。' 名词胶带在英语里可以直接转化成动词，用过去分词", (None, 'taped'), '放在信封后面说明“用胶带粘贴在提手上”的状态。']),
    (8, None, ["'让我念念：“抱歉弄错了。请替我保管这只蓝包直到星期五。”' 字条开头这句简短真诚的", (None, 'Sorry for the mistake'), '是日常因疏忽给别人添麻烦时最实用的书面与口头致歉语。']),
    (9, None, ["'一直到星期五？既没留名字，也没签落款！' 这里的时间短语", (None, 'Until Friday'), '把表示截止期限的介词放在星期五前面，清楚点明替他代为保管的时间终点。']),
    (10, None, ["'干嘛把自己的鞋子和木头火车留在陌生人这儿一直到星期五呢？' 可数名词复数", (None, 'strangers'), '指素不相识的陌生人，汉娜这一问把悬念彻底拉满了。']),
    (11, None, ["'欢迎来到菩提树庭院客栈，汉娜。你上班的第二天可绝对不会无聊了。' 格雷厄姆用将来否定结构", (None, 'will not be boring'), '冷幽默地收尾：形容事情本身不枯燥乏味，要用现在分词形式的形容词。']),
]
