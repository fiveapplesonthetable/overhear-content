# Authoring module for linden-courtyard-zh-s01e06-scene-05.
ID = 'linden-courtyard-zh-s01e06-scene-05'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = 'Page Two, Clause Fourteen  (第二页，第十四条)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = '前台桌面上摊开了那封盖红章的来信。凯勒布翻开别在背面的第二页，用铅笔精准点出了老城区保护法案第十四条——原来拯救客栈的钥匙一直就在大家手边。先完整听一遍吧。'
OPENER = '现在我们逐句拆解这段峰回路转、柳暗花明的精彩对话。'
TRANSITION = '弄明白了第十四条保护条款的妙处，我们再完整听一遍整场戏。'
OUTRO = '只要每天早晨敞开庭院大门为街坊供应咖啡与热面包，客栈租约就能再受市政法律保护整整十年！亚瑟高兴得连眼镜都从鼻梁上滑下来了。多保重。'
CLOSING = ('hannah', 'Take care!')
STORY = [
    ('arthur', "Look at page one, Caleb: 'commercial office conversion next month.' We are finished!", '快看第一页，凯勒布：“下个月改建为商业办公楼。”咱们彻底完了！'),
    ('caleb', 'Wait a moment, sir. Did you read page two clipped underneath?', '请等一下，先生。您读了别在底下的第二页吗？'),
    ('arthur', 'Only small gray numbers! My heart stopped at page one!', '上面全是灰扑扑的小数字！我的心脏在第一页就停跳了！'),
    ('hannah', 'Look where Caleb is pointing with his pencil, Arthur!', '快看凯勒布正用铅笔指着的地方，亚瑟！'),
    ('caleb', 'Clause fourteen of the Portland Old Quarter Act, and my brother here just nodded!', '《波特兰老城区法案》第十四条，而且这里我哥哥刚刚也点头确认了！'),
    ('arthur', 'In plain words, please! What does Clause fourteen say?', '拜托用大白话说吧！第十四条到底写了什么？'),
    ('caleb', 'No courtyard building over eighty years old may become private offices if the first floor serves neighbors daily.', '凡是超过八十年历史的老庭院建筑，只要一楼每天向街坊邻里提供日常服务，就不得改建为私人办公室。'),
    ('hannah', "'Serves neighbors daily'... like a public morning cafe?!", '“每天向街坊邻里提供服务”……比如说一家对公众开放的早间咖啡馆？！'),
    ('caleb', 'Exactly! Right now your four tables only serve overnight hotel guests.', '一点没错！目前你们那四张桌子只接待留宿的旅馆住客。'),
    ('arthur', 'Wait, if we open our courtyard gate every morning for neighborhood coffee and bread...', '等等，要是我们每天早上敞开庭院大门，给街坊邻里供应咖啡和面包……'),
    ('caleb', 'Then your guesthouse lease is protected for another ten years by city law!', '那么你们客栈的租约就能受市政法律保护，再稳稳延续十年！'),
    ('hannah', 'Arthur! Your glasses just fell off your nose for a happy reason!', '亚瑟！您的眼镜这回可是因为高兴的事从鼻梁上滑下来啦！'),
]
WALK = [
    (0, None, ["'快看第一页，凯勒布：“下个月改建为商业办公楼。”咱们彻底完了！' 形容走投无路、彻底没戏了，口语里常用系表结构", (None, 'We are finished'), '夸张道出亚瑟此刻的绝望。']),
    (1, None, ["'请等一下，先生。您读了别在底下的第二页吗？' 英语给页码或房间编号时，常把基数词直接放在名词后面不加冠词，说成", (None, 'read page two'), '简洁干练地提醒大家看附件。']),
    (2, None, ["'上面全是灰扑扑的小数字！我的心脏在第一页就停跳了！' 夸张形容吓得魂飞魄散时，一句", (None, 'My heart stopped'), '生动传神又充满喜剧色彩。']),
    (3, None, ["'快看凯勒布正用铅笔指着的地方，亚瑟！' 引导视线聚焦某处时，动词看后面直接接地点从句", (None, 'where Caleb is pointing'), '一下子把所有人的目光聚拢过来。']),
    (4, None, ["'《波特兰老城区法案》第十四条，而且这里我哥哥刚刚也点头确认了！' 副词加规则过去式", (None, 'just nodded'), "表示刚刚点头赞同，配合默契十足。"]),
    (5, None, ["'拜托用大白话说吧！第十四条到底写了什么？' 面对绕口的法律术语，请求对方用通俗易懂的日常话解释，最地道的说法就是", (None, 'In plain words'), '在生活里既实用又自然。']),
    (6, None, ["'凡是超过八十年历史的老庭院建筑，只要一楼每天向街坊邻里提供日常服务，就不得改建为私人办公室。' 法律条文中情态动词搭配否定主语构成", (None, 'may become'), '正式严谨地表示不得变更为私人办公场所。']),
    (7, None, ["'“每天向街坊邻里提供服务”……比如说一家对公众开放的早间咖啡馆？！' 汉娜瞬间举一反三，用介词短语", (None, 'like a public morning cafe'), '把冰冷法条变成了客栈触手可及的新生机。']),
    (8, None, ["'一点没错！目前你们那四张桌子只接待留宿的旅馆住客。' 形容词放在名词前组成", (None, 'overnight hotel guests'), '特指在客栈过夜留宿的房客，与街坊散客形成对比。']),
    (9, None, ["'等等，要是我们每天早上敞开庭院大门，给街坊邻里供应咖啡和面包……' 以连词引导的条件从句", (None, 'if we open'), '用一般现在时铺开美好设想，亚瑟的眼睛一下子亮了起来。']),
    (10, None, ["'那么你们客栈的租约就能受市政法律保护，再稳稳延续十年！' 在整段时间前面加上限定词构成", (None, 'another ten years'), '把额外顺延的十年当成一个整体来表达，振奋人心。']),
    (11, None, ["'亚瑟！您的眼镜这回可是因为高兴的事从鼻梁上滑下来啦！' 不规则过去式搭配脱落介词组成", (None, 'fell off your nose'), '首尾呼应亚瑟爱滑落的眼镜，让全屋转忧为喜。']),
]
