# Authoring module for linden-courtyard-zh-s01e02-scene-01.
ID = 'linden-courtyard-zh-s01e02-scene-01'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = 'The Red Ribbon  (红丝带失而复得)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '星期二清晨，阳光洒进前台。伊芙琳下楼准备吃早饭，一眼就看到了昨晚神秘人送回石阶上的那只深蓝色行李箱。先完整听一遍这段对话吧。'
OPENER = '现在我们放慢脚步，逐句拆解这场失而复得的晨间对话。'
TRANSITION = '理清了每一句的细节与悬念，我们再连贯听一遍整场戏。'
OUTRO = '红丝带和心爱的瓷茶杯全都完好无损，而吊牌上似曾相识的笔迹又勾起了伊芙琳二十五年前在波特兰教钢琴的往事。我们下场戏见。'
CLOSING = ('evelyn', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Miss Evelyn! Look what arrived at our gate last night.', '伊芙琳女士，早上好！快看昨晚有什么送到咱们院门口了。'),
    ('evelyn', 'My suitcase! Let me open the top pocket... yes, my red ribbon!', '我的行李箱！让我打开顶部外袋看看……没错，是我的红丝带！'),
    ('graham', 'And your teacup inside? Is it still in one piece?', '那您放在里面的茶杯呢？还完好无损吗？'),
    ('evelyn', 'Not a single crack! Who brought it back?', '连一道细纹都没有！是谁把它送回来的？'),
    ('hannah', 'We do not know. Someone left it on the step and rang the bell.', '我们也不知道。有人把它留在石阶上，按了一下门铃。'),
    ('evelyn', 'And he did not ask for his own suitcase with the wooden train?', '那他没有索要他自己那只装着木头火车的行李箱吗？'),
    ('graham', 'He left a short note asking us to keep it until Friday.', '他留下了一张简短的字条，请我们替他保管到星期五。'),
    ('evelyn', 'How curious! The handwriting on that tag felt oddly familiar to me.', '真奇特呀！那张吊牌上的笔迹让我莫名觉得有些眼熟。'),
    ('hannah', 'Really? Do you know someone in Portland?', '真的吗？您在波特兰认识什么人吗？'),
    ('evelyn', 'Twenty-five years ago I taught piano near here, though memories fade.', '二十五年前我在这附近教过钢琴，不过许多往事都渐渐淡忘了。'),
    ('graham', 'For now, his bag stays safe under lock and key.', '眼下，他的包会严严实实锁好，安全保管。'),
    ('evelyn', 'Wonderful! Now I am ready for a big breakfast.', '太好了！现在我准备好享用一顿丰盛的早餐了。'),
]
WALK = [
    (0, None, ["'伊芙琳女士，早上好！快看昨晚有什么送到咱们院门口了。' 英语说“昨天晚上”直接用两个词组成", (None, 'last night'), '放在句尾作时间状语，前面千万不要加任何介词或冠词。']),
    (1, None, ["'我的行李箱！让我打开顶部外袋看看……没错，是我的红丝带！' 自己动手做某事前先跟身旁的人打声招呼，用使役动词原形说出", (None, 'Let me open'), '后面直接跟动词原形打开，不加不定式符号。']),
    (2, None, ["'那您放在里面的茶杯呢？还完好无损吗？' 常用口语短语", (None, 'in one piece'), '字面意思是“还是完整的一整块”，专门用来询问易碎瓷器有没有摔坏。']),
    (3, None, ["'连一道细纹都没有！是谁把它送回来的？' 当疑问词本身充当主语提问“是谁做的”时，英语不需要加助动词，直接按陈述语序说出", (None, 'Who brought it back'), '既简洁又自然。']),
    (4, None, ["'我们也不知道。有人把它留在石阶上，按了一下门铃。' 实义动词“知道”变否定时不能直接加否定词，必须借用助动词说出", (None, 'We do not know'), '这是英语日常最核心的基础句型之一。']),
    (5, None, ["'那他没有索要他自己那只装着木头火车的行李箱吗？' 动词“问”后面一旦接上表目的的介词组成", (None, 'ask for'), '意思就从询问问题变成了“索取、要回某样东西”。']),
    (6, None, ["'他留下了一张简短的字条，请我们替他保管到星期五。' 现在分词短语", (None, 'asking us to keep'), '紧跟在字条后面作补充说明，清楚交代字条上所写的请求内容。']),
    (7, None, ["'真奇特呀！那张吊牌上的笔迹让我莫名觉得有些眼熟。' 复合不可数名词", (None, 'handwriting'), '由手和书写拼合而成，专指一个人手写留下的字迹。']),
    (8, None, ["'真的吗？您在波特兰认识什么人吗？' 英语里同一个动词", (None, 'know someone'), '既能表示知道某件事，也能表示“认识某个人”，注意词首字母并不发音。']),
    (9, None, ["'二十五年前我在这附近教过钢琴，不过许多往事都渐渐淡忘了。' 回忆具体多少年前的往事，把时间长度放在前面组成", (None, 'Twenty-five years ago'), '主句动词则配合使用不规则过去式', (None, 'taught'), '表示当年曾经教过。']),
    (10, None, ["'眼下，他的包会严严实实锁好，安全保管。' 地道成对习语", (None, 'under lock and key'), '字面意思是“在锁与钥匙的看护之下”，生动表示把贵重物品稳妥锁好。']),
    (11, None, ["'太好了！现在我准备好享用一顿丰盛的早餐了。' 形容词后面接上介词构成固定搭配", (None, 'ready for'), '用来引出接下来满心期待去享用的美餐或活动。']),
]
