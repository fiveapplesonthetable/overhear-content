# Authoring module for linden-courtyard-zh-s01e03-scene-04.
ID = 'linden-courtyard-zh-s01e03-scene-04'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'In from the Rain  (冒雨进屋)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'tessa': 'Tessa'}
INTRO = '文静的客人凯勒布浑身湿透地从雨夜里走进客栈前厅。汉娜和泰莎先递上干毛巾和热汤帮他暖身子，随后坦诚道出了七号房预订重叠的失误。先完整听一遍这段对话。'
OPENER = '现在让我们放慢节奏，逐句体会汉娜真诚得体的沟通方式。'
TRANSITION = '理解了这些礼貌又温暖的表达，我们再连贯听一遍。'
OUTRO = '一碗热汤暖了胃，汉娜坦率的歉意也稳住了局面，凯勒布答应先上三楼看看那间安静的阁楼书房。我们下场戏见。'
CLOSING = ('caleb', 'See you soon!')
STORY = [
    ('hannah', 'Good evening! Come inside out of the rain, sir.', '晚上好！快进屋避避雨吧，先生。'),
    ('caleb', 'Good evening. Sorry for dripping water on your clean floor.', '晚上好。抱歉把水滴在你们干净的地板上了。'),
    ('hannah', 'Do not worry at all! You must be Caleb.', '一点儿都别介意！您一定就是凯勒布吧。'),
    ('caleb', 'Yes, Caleb. I booked room seven by phone yesterday.', '是的，我是凯勒布。我昨天打电话预订了七号房。'),
    ('tessa', 'Here is a dry towel for your coat and a cup of hot soup, sir.', '先生，给您一条干毛巾擦擦外套，再来一杯热汤。'),
    ('caleb', 'Hot soup? After that cold walk in the rain, that sounds wonderful.', '热汤？在雨中冷得发抖地走过来之后，这听起来太棒了。'),
    ('hannah', 'Sir, before we go upstairs, I owe you an honest apology.', '先生，在咱们上楼之前，我欠您一个坦诚的道歉。'),
    ('caleb', 'Oh? Is there a problem with my booking?', '噢？我的预订出什么问题了吗？'),
    ('hannah', 'We accidentally booked two guests into room seven tonight.', '我们不小心给今晚的七号房登记了两位客人。'),
    ('caleb', 'Ah... in this rain? Every hotel near the station looked full.', '啊……下着这么大的雨？火车站附近的每家旅馆看着都住满了。'),
    ('hannah', 'Please do not worry! We prepared our quiet third floor attic study just for you.', '请千万别担心！我们专门为您准备了安静的三楼阁楼书房。'),
    ('caleb', 'An attic study? May I see it first?', '阁楼书房？我可以先看看吗？'),
]
WALK = [
    (0, None, ["'晚上好！快进屋避避雨吧，先生。' 英语善于用方位介词的组合画出动态画面，", (None, 'inside out of the rain'), '先说进到屋里，再说脱离外面的雨水，合起来就是“进屋避雨”。']),
    (1, None, ["'晚上好。抱歉把水滴在你们干净的地板上了。' 为自己正在造成的小麻烦致歉时，形容词后面接介词加动名词，说成", (None, 'Sorry for dripping'), '礼貌又谦逊地表达“不好意思弄滴水了”。']),
    (2, None, ["'一点儿都别介意！您一定就是凯勒布吧。' 在否定祈使句末尾加上短语", (None, 'at all'), '能把安慰的诚意拉满，相当于“完全没事、一点儿也不用放在心上”。']),
    (3, None, ["'是的，我是凯勒布。我昨天打电话预订了七号房。' 说明通过电话、邮件等通讯手段办事时，介词后直接跟单数名词且不加冠词，固定说成", (None, 'by phone'), '简洁指明“通过电话预订”。']),
    (4, None, ["'先生，给您一条干毛巾擦擦外套，再来一杯热汤。' 把手里的东西递给客人时，最贴心自然的开场句式就是", (None, 'Here is a dry towel'), '一边递上一边轻声招呼，服务分外周到。']),
    (5, None, ["'热汤？在雨中冷得发抖地走过来之后，这听起来太棒了。' 听到别人的提议觉得格外合心意时，用感官系动词搭配形容词说出", (None, 'that sounds wonderful'), "真诚赞叹“听起来真是太好了”。"]),
    (6, None, ["'先生，在咱们上楼之前，我欠您一个坦诚的道歉。' 主动承认失误、郑重致歉时，用双宾语结构说出", (None, 'I owe you'), '字面意思是“我欠您一份道歉”，态度显得格外诚恳负责。']),
    (7, None, ["'噢？我的预订出什么问题了吗？' 礼貌询问是否遇到了麻烦或差错，英语常用存现疑问句", (None, 'Is there a problem'), '语气克制得体，不会给人咄咄逼人的感觉。']),
    (8, None, ["'我们不小心给今晚的七号房登记了两位客人。' 英语用动词", (None, 'booked'), "来表示“为客人登记预订”的动作。"]),
    (9, None, ["'啊……下着这么大的雨？火车站附近的每家旅馆看着都住满了。' 即使心里指的是附近所有的旅馆，限定词", (None, 'Every hotel'), '在语法上依然把整体拆成逐一来看，后面必须紧跟单数名词。']),
    (10, None, ["'请千万别担心！我们专门为您准备了安静的三楼阁楼书房。' 句尾加上暖心短语", (None, 'just for you'), '强调“专门为您一人量身准备”，瞬间把换房的尴尬化作了特别款待。']),
    (11, None, ["'阁楼书房？我可以先看看吗？' 向服务人员提出礼貌得体的请求时，用情态动词开头说出", (None, 'May I see it'), '比普通的能不能更显温文尔雅，符合凯勒布沉稳的学者气质。']),
]
