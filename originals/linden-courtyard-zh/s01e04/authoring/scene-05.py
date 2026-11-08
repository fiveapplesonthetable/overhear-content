# Authoring module for linden-courtyard-zh-s01e04-scene-05.
ID = 'linden-courtyard-zh-s01e04-scene-05'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 4
SCENE = 5
TITLE = 'Five-Star Showers  (五星级热水澡)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = '雨过天晴的早晨，凯勒布神清气爽地下楼吃早餐，连声夸赞三楼的热水澡舒服极了。激动过头的亚瑟一不小心说漏了嘴，把昨晚看到笔记本评分的事抖了出来。我们先听为快。'
OPENER = '现在让我们放慢语速，逐句听听这场让人忍俊不禁的早餐乌龙。'
TRANSITION = '理解了这些鲜活生动的口语，我们再连贯听一遍。'
OUTRO = '原来凯勒布根本不是波特兰旅游指南的旅馆评审员！他笑着邀请大家走到外面的庭院里，揭开他真正的职业秘密。我们下场戏见。'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('caleb', 'Good morning, Hannah! Good morning, sir! What a bright morning after the rain.', '早上好，汉娜！早上好，先生！雨后的清晨真明媚啊。'),
    ('hannah', 'Good morning, Caleb! Did you sleep well under the roof beams?', '早上好，凯勒布！昨晚在屋顶木梁下睡得好吗？'),
    ('caleb', 'Best sleep I have had all month, and the shower water was wonderfully hot!', '这是我整整一个月以来睡得最香的一觉，而且淋浴水热乎极了！'),
    ('arthur', 'Hot! Hear that, Hannah? Reliable, modern, five-star hot water!', '热乎极了！听见没，汉娜？可靠、现代化的五星级热水！'),
    ('caleb', 'Old brick buildings usually take ages to warm up on the top floor.', '老砖房的顶楼通常要花好半天时间才能把水烧热。'),
    ('arthur', "Please write that down! 'Hot water on the third floor: ten out of ten!'", '快请把这句话写下来吧！“三楼热水：十分满分！”'),
    ('caleb', 'Excuse me? Ten out of ten?', '您说什么？十分满分？'),
    ('hannah', 'What Arthur means is... we hope every guest feels ten out of ten here!', '亚瑟的意思是……我们希望每一位客人在这儿都有十分满分的感受！'),
    ('arthur', 'No, Hannah, let us be honest professionals! Sir, we respect the Portland Travel Guide!', '不，汉娜，咱们要做坦诚的专业人士！先生，我们非常敬重波特兰旅游指南！'),
    ('caleb', 'The Portland Travel Guide? Wait, do you think I am a hotel inspector?', '波特兰旅游指南？等等，你们以为我是旅馆评审员吗？'),
    ('hannah', "When your notebook fell open on the counter last night, we saw 'nine out of ten'...", '昨晚您的笔记本在柜台上翻开时，我们瞄到了“十分中的九分”……'),
    ('caleb', 'Oh! Come outside to the courtyard for a minute. Let me show you what I really do!', '噢！跟我到外面的庭院来一分钟吧。让我给你们看看我到底是做什么工作的！'),
]
WALK = [
    (0, None, ["'早上好，汉娜！早上好，先生！雨后的清晨真明媚啊。' 感叹清晨阳光灿烂、天气晴好，用感叹句结构说出", (None, 'What a bright morning'), '一开口就带出雨过天晴的好心情。']),
    (1, None, ["'早上好，凯勒布！昨晚在屋顶木梁下睡得好吗？' 早上前台问候住客昨晚休息得如何，最温暖贴心的一句日常问候就是", (None, 'Did you sleep well'), '简单自然又充满关怀。']),
    (2, None, ["'这是我整整一个月以来睡得最香的一觉，而且淋浴水热乎极了！' 在最高级“最好的一觉”后面紧跟现在完成时定语从句", (None, 'I have had all month'), '表示从月初到现在整个月里最棒的睡眠体验。']),
    (3, None, ["'热乎极了！听见没，汉娜？可靠、现代化的五星级热水！' 听到顺耳的夸奖想让身旁同伴赶紧注意，口语常省掉助动词和主语，直接得意地问", (None, 'Hear that'), '意思是“你听见这话没”。']),
    (4, None, ["'老砖房的顶楼通常要花好半天时间才能把水烧热。' 夸张地形容做某件事慢吞吞、要等好久好久，日常口语超爱用短语", (None, 'take ages'), '字面意思是花掉好几个时代那么漫长。']),
    (5, None, ["'快请把这句话写下来吧！“三楼热水：十分满分！”' 把刚说的话记录在纸上或本子里，短语动词是", (None, 'write that down'), '代词做宾语时稳稳放在动词和副词中间。']),
    (6, None, ["'您说什么？十分满分？' 当别人说出莫名其妙的话、让你一头雾水时，把语调往上一扬说出", (None, 'Excuse me'), '就不再是借过，而是惊讶追问“您刚才说什么”。']),
    (7, None, ["'亚瑟的意思是……我们希望每一位客人在这儿都有十分满分的感受！' 替口误的同伴打圆场、重新解释对方话里的意思时，黄金救场句型就是", (None, 'What Arthur means is'), '主语从句把全场的注意力稳稳接过来。']),
    (8, None, ["'不，汉娜，咱们要做坦诚的专业人士！先生，我们非常敬重波特兰旅游指南！' 亚瑟一本正经地号召大家实话实说，用祈使结构说出", (None, 'let us be'), '后面直接跟名词词组“坦诚的专业人士”。']),
    (9, None, ["'波特兰旅游指南？等等，你们以为我是旅馆评审员吗？' 专门暗访检查酒店服务和星级标准的评审员，英语叫作", (None, 'a hotel inspector'), '凯勒布终于听明白大家昨晚在紧张什么了。']),
    (10, None, ["'昨晚您的笔记本在柜台上翻开时，我们瞄到了“十分中的九分”……' 英语说“昨天晚上”千万不能按字面拼成昨天加夜晚，固定地道说法永远是", (None, 'last night'), '前面也不需要加任何介词。']),
    (11, None, ["'噢！跟我到外面的庭院来一分钟吧。让我给你们看看我到底是做什么工作的！' 主动提出带大家亲眼瞧一瞧真相时，一句热情的", (None, 'Let me show you'), '自然引出下一场戏的揭秘时刻。']),
]
