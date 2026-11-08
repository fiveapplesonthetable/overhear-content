# Authoring module for linden-courtyard-zh-s01e01-scene-01.
ID = 'linden-courtyard-zh-s01e01-scene-01'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Lift the Handle  (先提门把手)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '清晨，汉娜第一天来到缅因州波特兰的菩提树庭院客栈上早班。前台后面，老练的维修兼夜班主管格雷厄姆正在给自己倒热茶。先完整听一遍这段英语对话，不用急着听懂每一个词。'
OPENER = '现在我们放慢节奏，一句一句细细品味这段对话。'
TRANSITION = '接下来，让我们按自然语速再完整听一遍整场戏。'
OUTRO = '汉娜顺利进了门，八把黄铜钥匙整齐挂在木牌上，她在客栈的第一个清晨正式开始了。就算刚才有几个词一晃而过也不用担心，后面还会反复听到。我们下场戏见。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Good morning! Excuse me, is the door locked?', '早上好！打扰一下，请问门锁着吗？'),
    ('graham', 'Good morning. No, lift the handle first, then push.', '早上好。没锁，先把把手往上提，然后再推。'),
    ('hannah', 'Oh, it opens! Thank you. I am Hannah, the new receptionist.', '噢，门开了！谢谢您。我是汉娜，新来的前台接待员。'),
    ('graham', 'I am Graham. You are ten minutes early.', '我是格雷厄姆。你早到了十分钟。'),
    ('hannah', 'I always walk fast on my first day. Where is the computer?', '我第一天上班走路总是很快。请问电脑在哪里？'),
    ('graham', 'In the drawer. Here we use this big paper book and a pencil.', '在抽屉里。在这里我们用这本大纸质登记簿和一支铅笔。'),
    ('hannah', 'A paper book? Really?', '纸质登记簿？真的吗？'),
    ('graham', 'Paper never loses the room list when it rains.', '下雨的时候，纸质账本可绝不会弄丢客房名单。'),
    ('hannah', 'Fair enough! And these are the keys?', '说得有理！那这些就是客房钥匙吗？'),
    ('graham', 'Yes, eight rooms, eight brass keys. Room four is arriving today.', '对，八间客房，八把黄铜钥匙。四号房的客人今天抵达。'),
    ('hannah', 'Great. Tell me everything I need to know.', '太好了。把所有我需要知道的事都告诉我吧。'),
    ('graham', 'Rule one: drink hot tea first, then answer the bell.', '第一条规矩：先喝热茶，再去接门铃。'),
]
WALK = [
    (0, None, ["'早上好！打扰一下，请问门锁着吗？' 英语早晨问好用单数形式", (None, 'Good morning'), '而要把陈述句变成一般疑问句，只需把系动词', (None, 'is'), '提前到主语门的前面。']),
    (1, None, ["'早上好。没锁，先把把手往上提，然后再推。' 英语给出操作指引非常干脆，直接用动词原形", (None, 'lift'), '紧接着再用动词原形', (None, 'push'), '前面完全不需要加代词你。']),
    (2, None, ["'噢，门开了！谢谢您。我是汉娜，新来的前台接待员。' 汉语常直接说“开了”，但英语绝不能省掉单数物主语，必须用代词指代那扇门，说出", (None, 'it opens'), '而且一般现在时第三人称单数词尾要带咝音。']),
    (3, None, ["'我是格雷厄姆。你早到了十分钟。' 汉语里说“早到”，英语不用动词来，而是用系动词搭配形容词，直接表达为", (None, 'You are ten minutes early'), '字面意思是你处于提早十分钟的状态。']),
    (4, None, ["'我第一天上班走路总是很快。请问电脑在哪里？' 谈到具体的某一天，比如入职第一天，英语固定选用介词", (None, 'on my first day'), '就像把这件大事稳稳落在日历的那一格上。']),
    (5, None, ["'在抽屉里。在这里我们用这本大纸质登记簿和一支铅笔。' 留意名词前的排列顺序：", (None, 'big paper book'), '先说大小，再把表示材质的纸直接放在书的前面，中间不用加任何连接词。']),
    (6, None, ["'纸质登记簿？真的吗？' 日常聊天里听到意想不到的新鲜事，只要把语调轻轻往上一扬，单说一个词", (None, 'Really'), '就能地道传达出“真的吗、不会吧”的惊讶语气。']),
    (7, None, ["'下雨的时候，纸质账本可绝不会弄丢客房名单。' 汉语说“下雨时”不需要主语，英语谈论天气却必须补上形式主语，说成", (None, 'when it rains'), '用这个中性代词来充当句子的语法支柱。']),
    (8, None, ["'说得有理！那这些就是客房钥匙吗？' 当对方的解释合情合理、让你心服口服时，口语里回一句", (None, 'Fair enough'), '既随和又自然，相当于汉语的“有道理、说得也是”。']),
    (9, None, ["'对，八间客房，八把黄铜钥匙。四号房的客人今天抵达。' 这里用现在进行时结构", (None, 'is arriving today'), '来表示今天早已排定好的入住行程，在旅馆前台尤为地道常见。']),
    (10, None, ["'太好了。把所有我需要知道的事都告诉我吧。' 英语在不定代词", (None, 'everything'), '后面直接紧跟修饰分句', (None, 'I need to know'), '中间省去了引导词，读起来一气呵成。']),
    (11, None, ["'第一条规矩：先喝热茶，再去接门铃。' 英语里的回应一词用途很广，不仅能接电话，前台听见铃响去接待客人也叫", (None, 'answer the bell'), '一句小幽默道出了客栈从容不迫的脾气。']),
]
