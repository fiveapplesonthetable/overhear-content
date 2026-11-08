# Authoring module for linden-courtyard-zh-s01e01-scene-04.
ID = 'linden-courtyard-zh-s01e01-scene-04'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Room Four on the Second Floor  (二楼的四号房)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '退休钢琴老师伊芙琳乘早班火车抵达波特兰，提着一只深蓝色行李箱走进客栈办理入住。不知为什么，今天这只箱子拎在手里格外沉重。先完整听一遍对话。'
OPENER = '现在我们逐句来听前台接待入住时温文尔雅的英语表达。'
TRANSITION = '掌握了这些贴心的接待用语，我们再完整听一遍整场戏。'
OUTRO = '格雷厄姆帮伊芙琳把那只沉甸甸的蓝色行李箱提上了二楼四号房。可箱子里装的真是连衣裙和琴谱吗？下一场谜底就要揭晓了，回头见。'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', "Welcome! Good morning, ma'am.", '欢迎光临！早上好，女士。'),
    ('evelyn', 'Good morning, my dear. I have a room for Evelyn.', '早上好，亲爱的。我预订了一间登记在伊芙琳名下的客房。'),
    ('hannah', 'Yes, room four on the second floor! How was your train trip?', '有的，二楼四号房！您坐火车一路上还顺利吗？'),
    ('evelyn', 'Quiet and pleasant, thank you, though this suitcase feels very heavy today.', '很安静也很惬意，谢谢你，不过这只行李箱今天拎着觉得特别沉。'),
    ('graham', 'Allow me. Goodness, did you pack stones in here?', '请让我来吧。好家伙，您在里面装石头了吗？'),
    ('evelyn', 'Only dresses, sheet music, and my favorite teacup!', '只有几条连衣裙、乐谱，还有我最心爱的茶杯呀！'),
    ('hannah', 'Here is your key, number four. Breakfast is from seven thirty to ten.', '给您钥匙，四号房。早餐时间是七点半到十点。'),
    ('evelyn', 'Wonderful. Is the window facing the street or the courtyard?', '太好了。请问窗户是朝向街道还是朝向庭院？'),
    ('hannah', 'The courtyard, right above the old tree. It is very quiet.', '朝向庭院，就在那棵老树正上方。非常清静。'),
    ('evelyn', 'Just what I need. Where are the stairs?', '正合我意。请问楼梯在哪里？'),
    ('graham', 'Right through this archway. I will carry the blue bag up for you.', '穿过这道拱门就是。我帮您把这只蓝箱子提上楼吧。'),
    ('evelyn', 'Thank you both very much.', '非常感谢你们二位。'),
]
WALK = [
    (0, None, ["'欢迎光临！早上好，女士。' 在美式英语服务场合，称呼成年女性最得体礼貌的词就是", (None, "ma'am"), '放在问候语末尾显得既尊重又亲切。']),
    (1, None, ["'早上好，亲爱的。我预订了一间登记在伊芙琳名下的客房。' 客人到前台报名字办理入住时，常温和地说", (None, 'I have a room for'), '后面直接跟上预订人自己的名字即可。']),
    (2, None, ["'有的，二楼四号房！您坐火车一路上还顺利吗？' 寒暄旅途感受最自然的问法就是用过去式系动词提问：", (None, 'How was your train trip'), '关心客人刚才那段车程是否顺心。']),
    (3, None, ["'很安静也很惬意，谢谢你，不过这只行李箱今天拎着觉得特别沉。' 这里的感官短语", (None, 'feels very heavy'), '并不是说箱子自己有知觉，而是描述人手拎上去“摸起来、拎起来觉得很沉”。']),
    (4, None, ["'请让我来吧。好家伙，您在里面装石头了吗？' 主动上前帮客人提重物时，一句简短优雅的", (None, 'Allow me'), '比问需不需要帮忙更显周到；紧接着一句感叹词', (None, 'Goodness'), '温和地道出了箱子分量惊人。']),
    (5, None, ["'只有几条连衣裙、乐谱，还有我最心爱的茶杯呀！' 英语里的音乐本身不可数，要指印在纸页上的琴谱或乐谱，就用复合词", (None, 'sheet music'), '字面意思是一页页的音乐。']),
    (6, None, ["'给您钥匙，四号房。早餐时间是七点半到十点。' 日常口语报半点时刻非常省事，直接按顺序连读小时和分钟，把七点半说成", (None, 'seven thirty'), '中间不需要加任何介词。']),
    (7, None, ["'太好了。请问窗户是朝向街道还是朝向庭院？' 询问房间采光或窗户朝向时，英语把“脸”用作动词分词，说出", (None, 'facing the street'), '形象地表示窗户正对着街道那一面。']),
    (8, None, ["'朝向庭院，就在那棵老树正上方。非常清静。' 在方位介词前加上强调副词构成", (None, 'right above'), '精准点出房间窗户“不偏不倚就在正上方”的位置感。']),
    (9, None, ["'正合我意。请问楼梯在哪里？' 听到满意的安排时，简短一句", (None, 'Just what I need'), '字面意思是“恰恰是我所需要的”，地道表达“太合我心意了”。']),
    (10, None, ["'穿过这道拱门就是。我帮您把这只蓝箱子提上楼吧。' 当场主动替对方效劳时，英语用将来助动词说出", (None, 'I will carry'), '句尾再配上方向小词', (None, 'up'), '清楚表示一路提上楼去。']),
    (11, None, ["'非常感谢你们二位。' 当同时向面前的两个人道谢时，只需在宾语后面紧跟表示两者的代词，说出", (None, 'Thank you both'), '既周全又倍显温暖。']),
]
