# Authoring module for linden-courtyard-zh-s01e01-scene-03.
ID = 'linden-courtyard-zh-s01e01-scene-03'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Where Are My Glasses?  (我的眼镜在哪儿？)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '离第一位住客抵达越来越近，客栈老板亚瑟风风火火地赶到前台，一边叮嘱今天四号房的接待不能出半点差错，一边到处找他的老花镜。先完整听一遍吧。'
OPENER = '下面我们一句句来听这段手忙脚乱又让人忍俊不禁的晨间插曲。'
TRANSITION = '搞清楚了每一个笑点和句型，我们再从头到尾听一遍现场原声。'
OUTRO = '眼镜总算在亚瑟自己的额头上平安现身，门外黄色出租车也刚好停稳，重头戏马上登场。我们下场戏接着听。'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('arthur', 'Good morning, everyone! Welcome, Hannah. Is everything ready?', '大家早上好！欢迎你，汉娜。一切都准备就绪了吗？'),
    ('hannah', 'Good morning! Yes, the desk is clean and the keys are ready.', '早上好！是的，前台干干净净，钥匙也都准备好了。'),
    ('arthur', "Today's guest in room four is staying all week. Everything must be perfect!", '今天四号房的住客要住整整一周。一切都必须十全十美！'),
    ('graham', 'Relax, Arthur. The room is clean and the towels are fresh.', '放轻松，亚瑟。房间打扫干净了，毛巾也清爽妥当。'),
    ('arthur', 'I need to read the reservation book, but I cannot find my glasses!', '我得看一眼预订登记簿，可我找不到我的眼镜了！'),
    ('hannah', 'Are they in your coat pocket?', '它们在您的大衣口袋里吗？'),
    ('arthur', 'No, only my pen and three old receipts!', '不在，只有我的钢笔和三张旧收据！'),
    ('graham', 'Look in the mirror behind the desk, boss.', '照照前台后面的镜子吧，老板。'),
    ('arthur', 'Why would my glasses be in the... oh! They are on my head!', '我的眼镜怎么会在镜子……噢！它们在我头上呢！'),
    ('hannah', 'Right there on your forehead, safe and sound.', '就架在您的额头上呢，安然无恙。'),
    ('arthur', 'Do not tell anyone! Now, smile brightly when the bell rings.', '千万别告诉任何人！好了，门铃一响就露出灿烂的微笑。'),
    ('graham', 'Here comes a taxi at the gate right now.', '大门口这会儿正好来了一辆出租车。'),
]
WALK = [
    (0, None, ["'大家早上好！欢迎你，汉娜。一切都准备就绪了吗？' 不定代词作主语一律按单数对待，因此提问时把单数系动词放在最前面，说出", (None, 'Is everything ready'), '听起来紧凑又干练。']),
    (1, None, ["'早上好！是的，前台干干净净，钥匙也都准备好了。' 常用表语形容词", (None, 'ready'), '不论主语是单数还是复数都保持原样，只要搭配对应的系动词就能表示“准备妥当”。']),
    (2, None, ["'今天四号房的住客要住整整一周。一切都必须十全十美！' 英语不仅人名能加所有格，时间副词后面同样可以加撇号和词尾，组成", (None, "Today's guest"), '简洁表达“今天入住的客人”。']),
    (3, None, ["'放轻松，亚瑟。房间打扫干净了，毛巾也清爽妥当。' 安抚别人别紧张时，格雷厄姆只用一个动词原形", (None, 'Relax'), '单独成句，比长篇大论更有定心丸的效果。']),
    (4, None, ["'我得看一眼预订登记簿，可我找不到我的眼镜了！' 情态动词否定式直接拼成一个词，接上动词原形构成", (None, 'cannot find'), '清晰表达眼下“找不到、寻不着”的着急状态。']),
    (5, None, ["'它们在您的大衣口袋里吗？' 英语里眼镜由两片镜片组成，永远算复数，所以汉娜用", (None, 'Are they'), '来指代眼镜，并询问是不是放在', (None, 'coat pocket'), '也就是大衣口袋里。']),
    (6, None, ["'不在，只有我的钢笔和三张旧收据！' 听收据复数词", (None, 'receipts'), '的发音要特别留心：拼写里倒数第二个辅音字母完全不发音，千万别把双唇音读出来。']),
    (7, None, ["'照照前台后面的镜子吧，老板。' 英语说照镜子不用介词在表面上，而说看进镜子里面：", (None, 'in the mirror'), '后面再接方位短语', (None, 'behind the desk'), '点明镜子就挂在前台后方。']),
    (8, None, ["'我的眼镜怎么会在镜子……噢！它们在我头上呢！' 亚瑟满腹狐疑地用", (None, 'Why would'), '开头反问，带着一种“按理说怎么可能会那样”的纳闷语气，话没说完自己先乐了。']),
    (9, None, ["'就架在您的额头上呢，安然无恙。' 经典的成对习语", (None, 'safe and sound'), '原本形容人平安归来，这里汉娜俏皮地拿来形容老花镜稳稳当当架在额头上。']),
    (10, None, ["'千万别告诉任何人！好了，门铃一响就露出灿烂的微笑。' 否定祈使句在句首加上助动词和否定词，说出", (None, 'Do not tell anyone'), '既自然又带点老板爱面子的小幽默。']),
    (11, None, ["'大门口这会儿正好来了一辆出租车。' 当看见车辆或行人正朝眼前驶来时，口语常用倒装结构", (None, 'Here comes'), '把来人或来车放在后面作焦点，画面感十足。']),
]
