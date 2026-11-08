# Authoring module for linden-courtyard-zh-s01e05-scene-01.
ID = 'linden-courtyard-zh-s01e05-scene-01'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Truth in the Courtyard  (庭院里的真相)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'evelyn': 'Evelyn'}
INTRO = '星期五清晨的阳光洒进菩提树庭院客栈。阁楼住客凯勒布终于和童年钢琴老师伊芙琳女士迎面相认，汉娜在一旁听他把周一火车上错拿行李箱的来龙去脉全盘托出。先完整听一遍这段对话。'
OPENER = '现在我们放慢节奏，一句一句拆解凯勒布揭开谜底时的地道英语表达。'
TRANSITION = '理清了事情的来龙去脉，我们按自然语速再完整听一遍整场戏。'
OUTRO = '原来周一深夜门阶上的神秘包裹、周二的急电和周三入住的阁楼房客，全都连在凯勒布和哥哥欧文身上。我们下场戏见。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('evelyn', 'Let me look at you properly, Caleb! You grew taller than the piano!', '让我好好看看你，凯勒布！你长高得都超过钢琴啦！'),
    ('caleb', 'I cannot believe you are staying in the exact same guesthouse, Miss Evelyn.', '我真不敢相信您竟然住在这同一家客栈里，伊芙琳女士。'),
    ('hannah', 'Wait, so we rode the same train on Monday, and you took her suitcase?', '等等，这么说星期一我们坐了同一班火车，而你拿走了她的行李箱？'),
    ('caleb', "By complete accident! At my cousin's apartment I opened it and saw sheet music and a red ribbon.", '完全是一场意外！到了表亲的公寓我打开箱子，看见了乐谱和一条红丝带。'),
    ('evelyn', 'Why did you leave my bag on the step at night and run away?', '那你为什么大晚上把我的包留在台阶上就跑掉了呢？'),
    ('caleb', 'Because when I walked here on Monday evening, I saw my older brother walking down this street!', '因为星期一傍晚我走到这里时，看见我哥哥正顺着这条街走过来！'),
    ('hannah', 'Your older brother lives here in Portland?', '你哥哥就住在这儿波特兰吗？'),
    ('caleb', 'Yes. I panicked, rang your bell, and slipped the Friday note onto the handle.', '是的。我慌了神，按响了你们的门铃，把那张星期五字条套在了提手上。'),
    ('evelyn', 'Wait, and Wednesday night you checked in here under your real name?', '等等，那星期三晚上你又用真名住进了这里？'),
    ('caleb', 'I needed a quiet place nearby before Friday, and honestly forgot you still had my bag!', '星期五之前我需要在附近找个安静的地方，老实说我全忘了我的包还在你们这儿！'),
    ('hannah', 'Until you called us on Tuesday asking us not to open the white package!', '直到星期二你打电话过来，拜托我们不要打开那个白色包裹！'),
    ('caleb', 'Everything in that white paper belongs to my brother Owen, not me.', '那层白纸里包着的一切都属于我哥哥欧文，而不是我。'),
]
WALK = [
    (0, None, ["'让我好好看看你，凯勒布！你长高得都超过钢琴啦！' 久别重逢端详晚辈时，副词", (None, 'properly'), '表示好好地看个仔细；后面用比较级短语', (None, 'taller than the piano'), '打趣他如今个头比钢琴还要高。']),
    (1, None, ["'我真不敢相信您竟然住在这同一家客栈里，伊芙琳女士。' 遇到巧合得令人惊叹的事，英语最常脱口而出", (None, 'I cannot believe'), '后面再叠加强调词组', (None, 'exact same'), '突出分毫不差就是同一家客栈。']),
    (2, None, ["'等等，这么说星期一我们坐了同一班火车，而你拿走了她的行李箱？' 英语说搭乘火车时常用动词过去式组成", (None, 'rode the same train'), '把原本表示骑乘的词自然延伸到乘坐列车上。']),
    (3, None, ["'完全是一场意外！到了表亲的公寓我打开箱子，看见了乐谱和一条红丝带。' 急着澄清自己绝非故意时，介词短语", (None, 'By complete accident'), '比单独说意外更有分量，强调纯属无心之失。']),
    (4, None, ["'那你为什么大晚上把我的包留在台阶上就跑掉了呢？' 助动词提前构成疑问后，后面并列两个动词原形：先用", (None, 'leave'), '表示把箱子留在原地，再用短语', (None, 'run away'), '描绘转身跑开的慌张模样。']),
    (5, None, ["'因为星期一傍晚我走到这里时，看见我哥哥正顺着这条街走过来！' 感官动词看见后面接现在分词短语", (None, 'walking down this street'), '生动捕捉到当时亲眼撞见哥哥正沿街走来的那一幕。']),
    (6, None, ["'你哥哥就住在这儿波特兰吗？' 陈述句直接升调就能变成确认事实的问句，其中", (None, 'lives here in Portland'), '用一般现在时表示长期定居在波特兰这座城市。']),
    (7, None, ["'是的。我慌了神，按响了你们的门铃，把那张星期五字条套在了提手上。' 复合介词短语", (None, 'onto the handle'), '自带动态方向感，精准画出把字条悄悄滑到箱子提手上面的动作。']),
    (8, None, ["'等等，那星期三晚上你又用真名住进了这里？' 旅馆办理登记入住固定说", (None, 'checked in'), '而后面的介词短语', (None, 'under your real name'), '则地道表达“登记在你的真实姓名名下”。']),
    (9, None, ["'星期五之前我需要在附近找个安静的地方，老实说我全忘了我的包还在你们这儿！' 表示“在附近、离这儿不远”只需一个轻巧的词", (None, 'nearby'), '直接放在地点名词后面作修饰，干净又顺口。']),
    (10, None, ["'直到星期二你打电话过来，拜托我们不要打开那个白色包裹！' 转述请求对方别做某事时，否定词一定要放在不定式符号前面，说成", (None, 'not to open'), '顺序千万不能颠倒。']),
    (11, None, ["'那层白纸里包着的一切都属于我哥哥欧文，而不是我。' 说明物品归谁所有时，英语不用系动词加所有格，而是用固定短语", (None, 'belongs to my brother'), '语气郑重又清晰。']),
]
