# Authoring module for linden-courtyard-zh-s01e05-scene-08.
ID = 'linden-courtyard-zh-s01e05-scene-08'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = 'The Red-Stamped Letter  (盖着红印章的来信)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '庭院大树下，欧文和凯勒布终于面对面站到了一起。可在前厅里，店主亚瑟随手拆开了那封房东来信，脸色却在瞬间变得煞白。我们先听为快。'
OPENER = '现在让我们一句一句拆解这场悲喜交加、悬念骤起的重头戏。'
TRANSITION = '听清了这封产权转让通知的内容，我们再完整听一遍整场戏。'
OUTRO = '整栋八号庭院楼竟然面临挂牌出售改成写字楼的危机！但亚瑟深明大义，叮嘱大家先把消息压在心底，别惊扰院里两兄弟的重逢。不过汉娜注意到的第二页又藏着什么？第五集到此结束，我们第六集再见。'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('tessa', 'Hannah, look through the glass. They are standing face to face under the tree!', '汉娜，透过玻璃往外看。他们俩正面对面站在大树底下呢！'),
    ('hannah', 'Neither of them walked away! Caleb is pointing at the two chairs right now!', '两个人谁都没有转身离开！凯勒布这会儿正指着那两把椅子呢！'),
    ('arthur', 'Wonderful... let me just glance at this landlord letter while we wait.', '太好了……趁咱们在屋里等着的工夫，我先扫一眼这封房东来信。'),
    ('tessa', 'Probably a boring notice about painting the street shutters.', '多半是封无聊的通知，讲什么重新粉刷临街百叶窗之类的事。'),
    ('arthur', 'Oh... oh no. Where is my chair? My knees feel weak.', '噢……噢不。我的椅子在哪儿？我两条腿都在发软。'),
    ('hannah', 'Arthur! Your face went completely white! Sit down, what does the letter say?', '亚瑟！您的脸全白了！快坐下，信上到底写了什么？'),
    ('arthur', 'Read the top line for me, Hannah. Tell me my glasses are playing tricks again!', '帮我念念最上面那一行吧，汉娜。快告诉我又是我的眼镜在捉弄人了！'),
    ('hannah', "'Notice of Property Transfer: Number Eight Courtyard Building offered for commercial office sale.'", '“产权转让通知：八号庭院楼挂牌出售，拟作商业办公用途。”'),
    ('tessa', 'Commercial office sale?! Turn our guesthouse and kitchen into gray offices?!', '挂牌作商业办公出售？！要把咱们的客栈和厨房改成灰扑扑的办公室吗？！'),
    ('arthur', 'They give us thirty days before new buyers inspect the building!', '他们只给我们留了三十天，新买家就要上门查验这栋楼了！'),
    ('hannah', 'Wait, there is a second folded page clipped to the back of this notice...', '等等，这份通知背面还用回形针别着折叠起来的第二页……'),
    ('arthur', 'Not a word to anyone outside yet! Let the two brothers have their Friday afternoon first!', '先别向外面任何人透露半个字！让那两兄弟先安安静静过完这个星期五下午吧！'),
]
WALK = [
    (0, None, ["'汉娜，透过玻璃往外看。他们俩正面对面站在大树底下呢！' 英语里的固定短语", (None, 'face to face'), '不用加任何冠词，直接作状语修饰站立，描绘兄弟俩迎面相对的动人一刻。']),
    (1, None, ["'两个人谁都没有转身离开！凯勒布这会儿正指着那两把椅子呢！' 表示两者之中没有任何一方做某事时，句首用否定代词短语", (None, 'Neither of them'), '比分别否定两个人简洁得多。']),
    (2, None, ["'太好了……趁咱们在屋里等着的工夫，我先扫一眼这封房东来信。' 漫不经心地快速看上一眼，英语用固定搭配", (None, 'glance at'), '为下一秒的突发惊吓埋下反差伏笔。']),
    (3, None, ["'多半是封无聊的通知，讲什么重新粉刷临街百叶窗之类的事。' 说明通知涉及什么主题，直接在名词后接介词加动名词", (None, 'about painting'), '语气轻松随意。']),
    (4, None, ["'噢……噢不。我的椅子在哪儿？我两条腿都在发软。' 受到惊吓站立不稳时，英语非常形象地说", (None, 'My knees feel weak'), '字面意思是膝盖发虚无力。']),
    (5, None, ["'亚瑟！您的脸全白了！快坐下，信上到底写了什么？' 动词去在英语里常作变化系动词，短语", (None, 'went completely white'), '生动描述脸色唰一下变得苍白。']),
    (6, None, ["'帮我念念最上面那一行吧，汉娜。快告诉我又是我的眼镜在捉弄人了！' 不愿相信眼前坏消息时，口语常说眼睛或眼镜在耍花招，即", (None, 'playing tricks'), '透着慌乱中的一丝侥幸。']),
    (7, None, ["'“产权转让通知：八号庭院楼挂牌出售，拟作商业办公用途。”' 正式公文里用介词短语", (None, 'for commercial office sale'), '冷冰冰地点明大楼将被作为商业办公楼出售。']),
    (8, None, ["'挂牌作商业办公出售？！要把咱们的客栈和厨房改成灰扑扑的办公室吗？！' 把某种场所改造成另一种模样，用旋转一词搭配介词构成", (None, 'Turn our guesthouse and kitchen into'), '道出泰莎满腔的难以置信。']),
    (9, None, ["'他们只给我们留了三十天，新买家就要上门查验这栋楼了！' 时间状语从句", (None, 'before new buyers inspect'), '点明只剩短短三十天缓冲期，紧迫感扑面而来。']),
    (10, None, ["'等等，这份通知背面还用回形针别着折叠起来的第二页……' 过去分词短语", (None, 'clipped to the back'), '精准描述文件背面夹附着另一页纸，悄悄埋下转机线索。']),
    (11, None, ["'先别向外面任何人透露半个字！让那两兄弟先安安静静过完这个星期五下午吧！' 叮嘱大家守口如瓶时，省略动词的名词短句", (None, 'Not a word to anyone'), '简短坚定，尽显老店主的仁厚胸怀。']),
]
