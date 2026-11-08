# Authoring module for linden-courtyard-zh-s01e01-scene-02.
ID = 'linden-courtyard-zh-s01e01-scene-02'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = 'Warm Rolls and Two Rings  (热餐包与两声铃响)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'tessa': 'Tessa', 'graham': 'Graham'}
INTRO = '五分钟后，刚出炉的面包香气从早餐咖啡角飘满了前厅。早班烘焙师泰莎端着一篮热气腾腾的小餐包走出来，跟新同事汉娜打招呼。我们先听为快。'
OPENER = '现在让我们逐句拆解，听听她们是怎么热络聊起来的。'
TRANSITION = '理解了这些地道表达，我们再连贯听一遍整场对话。'
OUTRO = '汉娜手里捧着温热的小餐包，转眼就和厨房里的泰莎熟络起来了，连老房子爱自己响两声的脾气也摸清了一半。我们待会儿见。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('tessa', 'Hello! You must be Hannah. I am Tessa from the kitchen.', '你好呀！你一定就是汉娜吧。我是厨房的泰莎。'),
    ('hannah', 'Nice to meet you, Tessa. Something smells wonderful!', '很高兴认识你，泰莎。有什么东西闻起来真香啊！'),
    ('tessa', 'Fresh morning rolls! Take one while it is still warm.', '刚出炉的早安小餐包！趁还热乎着快拿一个尝尝。'),
    ('hannah', 'Thank you! Do we use first names here?', '谢谢你！咱们在这儿都直接叫名字吗？'),
    ('tessa', 'With me, always! Leave the stiff polite talk for the guests.', '跟我说话永远直呼其名就好！把那些拘谨生硬的客套话留给住客吧。'),
    ('graham', 'Tessa talks to everyone on our street like old friends.', '泰莎跟咱们这条街上的每一个人聊天都像老朋友一样。'),
    ('tessa', 'Because good coffee and warm bread make people friendly!', '因为好咖啡和热面包能让大家变得亲切友好呀！'),
    ('hannah', 'What was that bell? Somebody rang twice!', '刚才那是什么铃声？有人按了两下铃！'),
    ('graham', 'Nobody is there. That is the buzzer from room four.', '那边没有人。那是四号房传来的电门铃声。'),
    ('tessa', 'Even when room four is empty, the old wire rings twice.', '就算四号房空着没人住，那根老电线也会自己响两声。'),
    ('hannah', 'So the house says hello on its own?', '所以这栋老房子会自己打招呼啰？'),
    ('tessa', 'Exactly! You already fit right in.', '一点没错！你已经完全融入咱们这儿啦。'),
]
WALK = [
    (0, None, ["'你好呀！你一定就是汉娜吧。我是厨房的泰莎。' 第一次见面凭情理笃定地猜测对方身份时，英语最爱用", (None, 'You must be'), '语气亲切又自然，就像汉语说的“你准是汉娜吧”。']),
    (1, None, ["'很高兴认识你，泰莎。有什么东西闻起来真香啊！' 在表示嗅觉的感官动词", (None, 'smells'), '后面，英语直接跟形容词', (None, 'wonderful'), '来描述散发出的迷人香气，千万不要换成副词。']),
    (2, None, ["'刚出炉的早安小餐包！趁还热乎着快拿一个尝尝。' 这里用双词短语", (None, 'still warm'), '把表示“仍然”的小词放在形容词前面，精准形容面包刚出烤箱温热松软的口感。']),
    (3, None, ["'谢谢你！咱们在这儿都直接叫名字吗？' 询问日常习惯时，句首用助动词引出一般现在时问句", (None, 'Do we use first names'), '在英语职场里，直呼教名代表着随和亲近的同事关系。']),
    (4, None, ["'跟我说话永远直呼其名就好！把那些拘谨生硬的客套话留给住客吧。' 泰莎口中所说的", (None, 'polite talk'), '把形容词放在谈话一词前面，特指迎宾时彬彬有礼却略显客套的寒暄用语。']),
    (5, None, ["'泰莎跟咱们这条街上的每一个人聊天都像老朋友一样。' 主语泰莎是第三人称单数，所以日常动作要加词尾变成", (None, 'talks to everyone'), '注意交谈这个词中间的舌边音字母并不发音。']),
    (6, None, ["'因为好咖啡和热面包能让大家变得亲切友好呀！' 英语用使役动词", (None, 'make'), '接上复数名词', (None, 'people'), '再跟形容词作补语，地道表达“让人们变得友善热络”。']),
    (7, None, ["'刚才那是什么铃声？有人按了两下铃！' 英语表示“两次”不用数字二加次数，而是专门用一个干脆利落的单音节词", (None, 'twice'), '放在动词后面即可。']),
    (8, None, ["'那边没有人。那是四号房传来的电门铃声。' 复合代词本身就包含否定含义，说出", (None, 'Nobody is there'), '时谓语动词直接用单数肯定形式，不能再重复加否定词。']),
    (9, None, ["'就算四号房空着没人住，那根老电线也会自己响两声。' 句首用强调组合", (None, 'Even when'), '引出让步时间分句，相当于汉语里说的“哪怕当……的时候”。']),
    (10, None, ["'所以这栋老房子会自己打招呼啰？' 汉娜风趣地用拟人说法", (None, 'says hello'), '再配上固定短语', (None, 'on its own'), '活灵活现地说出老房子“靠它自己、自发地”问好。']),
    (11, None, ["'一点没错！你已经完全融入咱们这儿啦。' 地道的三词习语", (None, 'fit right in'), '是夸奖新人迅速适应新环境、跟大家打成一片的绝佳口语表达。']),
]
